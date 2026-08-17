// cdt2d.cpp ── 2次元 CDT（因果的動的三角形分割）のモンテカルロ
//
// 「宇宙を離散の差分式で書いて、格子ゲージ理論みたいに回す」をそのままやる。
//
// 何を回しているか
// ----------------
// 時空を「時刻 t の空間スライス（長さ l_t の輪）」の列で表す。t と t+1 のあいだは
// 三角形で埋める。埋め方の数は step1 で力ずくの列挙と一致することを確かめた:
//
//     N(l, l') = Γ(l+l') / (Γ(l) Γ(l'))          （両端に印を付けた数え）
//     K(l, l') = C(l+l'-1, l-1) = N(l,l')/l'      （転送行列を合成するときの数え）
//
// 素の格子作用は**体積項だけ**。2次元では曲率項 ∫√g R がオイラー標数（定数）なので、
// 力学に効くのは三角形の総数 N だけ:
//
//     S_bare = λ N,     N = Σ_t (l_t + l_{t+1})
//
// つまり運動項は一行も入れていない。それでも配位の重みは
//
//     W[{l}] = Π_t K(l_t, l_{t+1}) · e^{-λ N}
//
// なので、体積プロファイル {l_t} から見た有効作用は
//
//     S_eff = Σ_t [ λ(l_t+l_{t+1}) - ln K(l_t,l_{t+1}) ]
//           = Σ_t [ (λ-ln2)(l_t+l_{t+1}) + (l_{t+1}-l_t)²/(4 l_t) + (対数項) ]  + …
//
// ★ 運動項が【エントロピー（数え上げ）から】生えて、しかも符号が【正】。
//   これが「共形因子問題（第9回）」に離散が効く仕組み。連続では作用しか見ておらず、
//   同じ自由度の運動項が負符号で、経路積分が定義できなかった。
//
// β というツマミを付けてある: 重みを K^β にする。
//   β=1 … 本物の CDT（数え上げを正しく数える）
//   β=0 … 数え上げを無視（＝測度を平坦にした素朴な扱い）。運動項が消える
//   β<0 … 数え上げを逆符号で入れる。運動項が負になり、連続の病気が再現する
//
// 使い方:
//   cdt2d cap  <T> <lambda> <sweeps> [beta]   ビッグバン境界（l_0=1 固定）
//   cdt2d tor  <T> <lambda> <sweeps> [beta]   トーラス（時間も周期的）
//
// 検証済みの厳密解（step1〜3）:
//   λ_c = ln 2 = 0.693147…
//   cap・臨界点で  P_t(l) = (1/(t+1)) (t/(t+1))^{l-1},  <l(t)> = t+1  （厳密）
//   λ>λ_c では <l> が有限値で頭打ち、頭打ちの高さ ∝ (λ-λ_c)^{-1/2}

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>

static const double LN2 = 0.6931471805599453;

// ---- 乱数（xorshift128+）
static uint64_t s0 = 88172645463325252ull, s1 = 362436069362436069ull;
static inline uint64_t rnd64() {
    uint64_t x = s0, y = s1;
    s0 = y; x ^= x << 23; s1 = x ^ y ^ (x >> 17) ^ (y >> 26);
    return s1 + y;
}
static inline double rnd() { return (rnd64() >> 11) * (1.0 / 9007199254740992.0); }

// ---- lgamma の表（l は整数なので引ける。毎回 lgamma を呼ぶと遅い）
static std::vector<double> LG;
static inline double lg(int n) {                 // lgamma(n)
    if (n < (int)LG.size()) return LG[n];
    return lgamma((double)n);
}
static void init_lg(int n) {
    LG.resize(n + 2);
    for (int i = 0; i < (int)LG.size(); ++i) LG[i] = lgamma((double)std::max(1, i));
}

// 帯1枚ぶんの ln（数え上げ）: ln K(l,l') = lnΓ(l+l') - lnΓ(l) - lnΓ(l'+1)
static inline double lnK(int a, int b) { return lg(a + b) - lg(a) - lg(b + 1); }

int main(int argc, char** argv) {
    if (argc < 5) {
        fprintf(stderr,
            "usage: cdt2d <cap|tor> <T> <lambda> <sweeps> [beta] [seed]\n"
            "  cap: l_0=1 固定のビッグバン境界 / tor: 時間も周期的\n"
            "  beta: 数え上げの重み K^beta (既定 1.0)\n");
        return 1;
    }
    std::string mode = argv[1];
    int    T      = atoi(argv[2]);
    double lambda = atof(argv[3]);
    long   sweeps = atol(argv[4]);
    double beta   = (argc > 5) ? atof(argv[5]) : 1.0;
    if (argc > 6) { s0 = (uint64_t)atoll(argv[6]) | 1ull; for (int i = 0; i < 20; ++i) rnd64(); }
    // mode 1: 数え上げから先に ln2 の分（体積に比例する主要項）を引いてから β を掛ける。
    //   lnW = β[ lnK - ln2(l+l') ] - λ(l+l')
    // こうすると **体積項の係数は β によらず λ で一定**になり、β が動かすのは運動項だけになる。
    // mode 0（既定）だと β<0 で実効的な体積項 (λ-βln2) まで動いてしまい、
    // 「宇宙定数が負だから膨らんだ」のと区別が付かない
    int submode = (argc > 7) ? atoi(argv[7]) : 0;

    const int LCAP = 1 << 20;          // 安全弁（発散したら分かるように）
    init_lg(4 * LCAP);

    bool cap = (mode == "cap");
    std::vector<int> l(T, 1);
    // 初期配位: cap なら l_t = t+1 のあたりから、トーラスなら一様
    for (int t = 0; t < T; ++t) l[t] = cap ? (t + 1) : 4;
    if (cap) l[0] = 1;

    // 局所の重み（スライス t が絡む帯のぶん）
    auto local = [&](int t, int lt) -> double {
        double w = 0.0;
        int prev = (t == 0) ? -1 : l[t - 1];
        int next;
        if (cap) { if (t == T - 1) next = -1; else next = l[t + 1]; }
        else     { next = l[(t + 1) % T]; if (t == 0) prev = l[T - 1]; }
        if (prev > 0) w += beta * (lnK(prev, lt) - (submode ? LN2 * (prev + lt) : 0.0)) - lambda * (prev + lt);
        if (next > 0) w += beta * (lnK(lt, next) - (submode ? LN2 * (lt + next) : 0.0)) - lambda * (lt + next);
        return w;
    };

    const int bigStep = std::max(3, T / 2);   // 大きい歩幅。**l に依存させない**＝提案が対称

    long acc = 0, tot = 0;
    long meas = 0;
    // ビン統計（自己相関を含めた誤差評価）
    std::vector<double> bins; double binAcc = 0; long binCnt = 0;
    const long binSize = std::max(100L, sweeps / 200);
    std::vector<double> sumL(T, 0.0), sumL2(T, 0.0);
    double sumN = 0.0, sumN2 = 0.0;
    // <(Δl)²/l> を測る（有効作用の運動項の係数を取り出すため）
    double sumK = 0.0; long nK = 0;
    // 幾何分布の検証用ヒストグラム。
    // 厳密解 P_t(l)=(1/(t+1))(t/(t+1))^{l-1} は「t で切って先が無い」propagator の分布なので、
    // 比べる相手は**最終スライス**（その先に帯が無い）。途中のスライスは未来の帯にも
    // 引っ張られるので分布が変わる ── ここを間違えると一致しない
    int tprobe = cap ? (T - 1) : (T / 2);
    std::vector<long> hist(4096, 0);

    long therm = sweeps / 5;
    for (long sw = 0; sw < sweeps + therm; ++sw) {
        for (int k = 0; k < T; ++k) {
            int t = (int)(rnd() * T);
            if (cap && t == 0) continue;                 // 境界は固定
            // 更新は2種類混ぜる。臨界点では σ_l ≈ <l> ── つまり揺らぎが平均と同じ大きさなので、
            // ±1〜3 の小さい歩幅だけだと l~T のスケールを歩き切るのに (T/3)² 掃引かかる。
            // l に比例した大きい歩幅を半分混ぜて自己相関を潰す（提案は対称なので詳細釣合いはそのまま）
            // 更新は2種類混ぜる。臨界点では σ_l ≈ <l> ── 揺らぎが平均と同じ大きさなので、
            // ±1〜3 の小さい歩幅だけだと l~T のスケールを歩き切るのに (T/3)² 掃引かかる。
            // **歩幅は現在の l[t] に依存させてはいけない**（提案が非対称になり詳細釣合いが壊れる）。
            // 大域スケール bigStep で決めるので提案は l に依らず対称
            int d;
            if (rnd() < 0.5) { d = (int)(rnd() * 6) - 3; if (d >= 0) d++; }
            else {
                d = (int)(rnd() * (2 * bigStep + 1)) - bigStep;
                // d==0 を +1 に振り替えてはいけない。+1 の提案確率だけ2倍になって
                // 上向きに偏る（実際これで <l> が厳密解の2倍になった）。0 は空更新にする
                if (d == 0) continue;
            }
            int nl = l[t] + d;
            if (nl < 1 || nl > LCAP) continue;
            double w0 = local(t, l[t]);
            double w1 = local(t, nl);
            tot++;
            if (w1 >= w0 || rnd() < exp(w1 - w0)) { l[t] = nl; acc++; }
        }
        if (sw < therm) continue;
        // 測定
        double N = 0;
        for (int t = 0; t < T; ++t) {
            sumL[t] += l[t]; sumL2[t] += (double)l[t] * l[t];
            int nx = cap ? ((t + 1 < T) ? l[t + 1] : -1) : l[(t + 1) % T];
            if (nx > 0) {
                N += l[t] + nx;
                double dl = nx - l[t];
                sumK += dl * dl / (double)l[t]; nK++;
            }
        }
        sumN += N; sumN2 += N * N;
        if (l[tprobe] < (int)hist.size()) hist[l[tprobe]]++;
        // 最終スライスの平均をビンに分けて溜める（ビン間のばらつき＝自己相関込みの誤差）
        binAcc += l[T - 1]; binCnt++;
        if (binCnt == binSize) { bins.push_back(binAcc / binCnt); binAcc = 0; binCnt = 0; }
        meas++;
    }

    printf("# 2D CDT  mode=%s T=%d lambda=%.8f (lambda-ln2=%+.8f) beta=%.3f sweeps=%ld\n",
           mode.c_str(), T, lambda, lambda - LN2, beta, sweeps);
    printf("# 受理率 %.3f   測定回数 %ld\n", (double)acc / tot, meas);
    double mN = sumN / meas;
    printf("# <N(三角形の総数)> = %.3f   揺らぎ σ_N = %.3f\n",
           mN, sqrt(std::max(0.0, sumN2 / meas - mN * mN)));
    printf("# <(Δl)²/l> = %.5f   （有効作用の運動項が (Δl)²/(4l) なら、平衡で ≈ 2 になる）\n",
           sumK / nK);
    printf("#\n# t   <l_t>      σ_l\n");
    for (int t = 0; t < T; t += std::max(1, T / 12)) {
        double m = sumL[t] / meas, v = sumL2[t] / meas - m * m;
        printf("%5d %10.4f %10.4f\n", t, m, sqrt(std::max(0.0, v)));
    }
    {
        double m = sumL[T - 1] / meas, v = sumL2[T - 1] / meas - m * m;
        printf("%5d %10.4f %10.4f   <- 最終スライス\n", T - 1, m, sqrt(std::max(0.0, v)));
    }
    if (cap) {
        double m = sumL[T - 1] / meas, v = sumL2[T - 1] / meas - m * m;
        double bm = 0, bv = 0;
        for (double b : bins) bm += b;
        if (!bins.empty()) bm /= bins.size();
        for (double b : bins) bv += (b - bm) * (b - bm);
        double err = bins.size() > 1 ? sqrt(bv / (bins.size() * (bins.size() - 1))) : 0.0;
        printf("#\n# ★厳密解との比較（最終スライス t=%d、その先に帯が無いので propagator そのもの）\n", T - 1);
        printf("#   ビン数 %d（1ビン %ld 測定）\n", (int)bins.size(), binSize);
        printf("#   <l> 測定 = %.4f +- %.4f   厳密 t+1 = %d   比 = %.5f  (%.2f σ)\n",
               m, err, T, m / T, err > 0 ? (m - T) / err : 0.0);
        printf("#   σ_l 測定 = %.4f   厳密 sqrt(t(t+1)) = %.4f  比 = %.5f\n",
               sqrt(std::max(0.0, v)), sqrt((double)(T - 1) * T), sqrt(std::max(0.0, v)) / sqrt((double)(T - 1) * T));
        double p = 1.0 / T;
        printf("#\n# l の分布 vs 幾何分布 P(l)=p(1-p)^{l-1},  p=1/(t+1)=%.6f\n", p);
        printf("#   l      観測頻度        幾何分布      比\n");
        for (int L = 1; L < (int)hist.size() && L <= 5 * T; L += std::max(1, T / 4)) {
            double obs = (double)hist[L] / meas;
            double th = p * pow(1 - p, L - 1);
            printf("%5d %14.6e %14.6e %8.4f\n", L, obs, th, th > 0 ? obs / th : 0.0);
        }
    }
    return 0;
}
