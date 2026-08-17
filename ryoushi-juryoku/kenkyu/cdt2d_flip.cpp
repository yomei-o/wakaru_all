// cdt2d_flip.cpp ── 因果律だけを消す対照実験。
//
// 何をするか
// ----------
// 1. 2次元 CDT の三角形分割をひとつ作る（葉層あり＝因果的）。
// 2. その【双対グラフ】で d_H と d_s を測る。
// 3. そこからフリップ（対角線の張り替え）を大量に打つ。
//    2次元では ∫√g R が位相不変量なので、**同じ位相・同じ三角形数の分割はすべて等重み**。
//    したがってフリップは無条件受理でよく、行き着く先は
//    「因果律を課さない一様アンサンブル」＝2次元ユークリッド動的三角形分割(DT)。
// 4. もう一度 d_H と d_s を測る。
//
// つまり **三角形の数もトポロジーも作用も変えず、因果律というひとつの条件だけを外す**。
// 既知の結果では CDT: d_H=2, d_s=2 / ユークリッド DT: d_H=4, d_s=2。
// もしこれが再現するなら、「短距離で d_s→2」は量子重力の signature ではなく、
// ランダム幾何一般に出る数だということになる（d_H のほうが幾何を区別している）。
//
// 双対グラフを使う理由：三角形は必ず3枚の隣を持つので【次数がぴったり3の正則グラフ】になり、
// ランダムウォークに次数ゆらぎの効果が入らない。CDT の文献の d_s もこの定義。
//
// 使い方:
//   cdt2d_flip <T> <delta> <nflipsweep> <nmeas> <sigmax> <nstart> [seed]

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdint>

static const double LN2 = 0.6931471805599453;
static uint64_t s0 = 88172645463325252ull, s1 = 362436069362436069ull;
static inline uint64_t rnd64() {
    uint64_t x = s0, y = s1; s0 = y; x ^= x << 23; s1 = x ^ y ^ (x >> 17) ^ (y >> 26); return s1 + y;
}
static inline double rnd() { return (rnd64() >> 11) * (1.0 / 9007199254740992.0); }
static inline int rndi(int n) { return (int)(rnd() * n); }

static std::vector<double> LG;
static inline double lg(int n) { return (n < (int)LG.size()) ? LG[n] : lgamma((double)n); }
static inline double lnK(int a, int b) { return lg(a + b) - lg(a) - lg(b + 1); }

// ---------------- 双対グラフ上の測定 ----------------
struct Dual {
    int N;                              // 三角形の数
    std::vector<int> nbr;               // nbr[3t+k] = 半辺(t,k)の相手の半辺 3u+j
};

// 半径 r 以内の三角形数 V(r)
static void measure_dH(const Dual& D, int nstart, std::vector<double>& Vsum, std::vector<long>& Vn,
                       double* rmean = nullptr, long* rn = nullptr) {
    std::vector<int> dist(D.N), q;
    for (int st = 0; st < nstart; ++st) {
        std::fill(dist.begin(), dist.end(), -1);
        int v0 = rndi(D.N);
        q.clear(); q.push_back(v0); dist[v0] = 0;
        size_t head = 0; int cnt = 1, cur = 0;
        std::vector<int> byR; byR.push_back(1);
        while (head < q.size()) {
            int v = q[head++];
            if (dist[v] > cur) { cur = dist[v]; byR.push_back(cnt); }
            for (int k = 0; k < 3; ++k) {
                int u = D.nbr[3 * v + k] / 3;
                if (dist[u] < 0) { dist[u] = dist[v] + 1; q.push_back(u); cnt++; }
            }
        }
        byR.push_back(cnt);
        if (byR.size() > Vsum.size()) { Vsum.resize(byR.size(), 0.0); Vn.resize(byR.size(), 0); }
        for (size_t r = 0; r < byR.size(); ++r) { Vsum[r] += byR[r]; Vn[r]++; }
        // 平均グラフ距離。有限サイズスケーリング <r> ~ N^{1/d_H} で d_H を決める。
        // 局所傾き d lnV/d lnr より有限サイズに強い
        if (rmean) { double sm = 0; for (int v = 0; v < D.N; ++v) sm += dist[v];
                     *rmean += sm / D.N; (*rn)++; }
    }
}

// 拡散の戻り確率 P(σ)。
// ★ 単純ランダムウォークは使えない。三角形分割の双対は【ほぼ二部グラフ】で
//   （上向き三角形と下向き三角形が交互に隣接する）、戻り確率が偶奇で激しく振動する。
//   実際それで d_s が負になった。**怠惰ウォーク**（確率1/2でその場に留まる）にすると
//   偶奇の振動が消える。拡散係数が半分になるだけなので、対数傾き＝d_s は変わらない。
static void measure_ds(const Dual& D, int sigmax, int nstart,
                       std::vector<double>& Psum, long& Pn) {
    std::vector<double> p0(D.N), p1(D.N);
    for (int st = 0; st < nstart; ++st) {
        int v0 = rndi(D.N);
        std::fill(p0.begin(), p0.end(), 0.0); p0[v0] = 1.0;
        Psum[0] += 1.0;
        for (int sg = 1; sg <= sigmax; ++sg) {
            std::fill(p1.begin(), p1.end(), 0.0);
            for (int v = 0; v < D.N; ++v) {
                double pv = p0[v]; if (pv == 0.0) continue;
                p1[v] += 0.5 * pv;                       // その場に留まる
                double sh = pv / 6.0;                    // 残り 1/2 を3方向へ
                p1[D.nbr[3 * v] / 3] += sh; p1[D.nbr[3 * v + 1] / 3] += sh;
                p1[D.nbr[3 * v + 2] / 3] += sh;
            }
            p0.swap(p1);
            Psum[sg] += p0[v0];
        }
        Pn++;
    }
}

// ---------------- フリップ（半辺で正しく組む） ----------------
//
// ★ ここを最初に間違えた。双対の隣接だけを nbr[3A+0..2] に順不同で書き戻したら、
//   スロットに入っている【三角形の向き付け】が壊れ、もはや曲面の双対でなくなった。
//   結果は 3-正則のランダムグラフ（エキスパンダ）になり、d_H が 5.6 まで発散した。
//   ── 見た目は動いているのに、測っている対象が別物になっていた。
//
// 正しくは半辺（half-edge）で持つ： opp[3t+k] = 3u+j。
// 三角形 A=(a,b,c) の半辺 k,k+1,k+2 は a→b, b→c, c→a（反時計回り）。
// 共有辺 ab で A=(a,b,c) と B=(b,a,d) をフリップすると
//   A' = (a,d,c) : 半辺 k=a→d, k+1=d→c, k+2=c→a
//   B' = (b,c,d) : 半辺 j=b→c, j+1=c→d, j+2=d→b
// なので張り替えは
//   opp[A.k]   <-> oZ (=B.j+1 の相手),   opp[A.k+1] <-> B.j+1
//   opp[B.j]   <-> oX (=A.k+1 の相手),   A.k+2 と B.j+2 は変わらない
static bool flip_once(Dual& D) {
    int A = rndi(D.N), k = rndi(3);
    int h = 3 * A + k, hb = D.nbr[h];
    int B = hb / 3, j = hb % 3;
    if (B == A) return false;
    int hA1 = 3 * A + (k + 1) % 3, hA2 = 3 * A + (k + 2) % 3;
    int hB1 = 3 * B + (j + 1) % 3, hB2 = 3 * B + (j + 2) % 3;
    int oX = D.nbr[hA1], oY = D.nbr[hA2], oZ = D.nbr[hB1], oW = D.nbr[hB2];
    // 退化（外側の相手が A か B 自身）を弾く。前後で同じ集合を見るので対称＝詳細釣合いOK
    for (int o : {oX, oY, oZ, oW}) { int tt = o / 3; if (tt == A || tt == B) return false; }
    D.nbr[h] = oZ;   D.nbr[oZ] = h;
    D.nbr[hA1] = hB1; D.nbr[hB1] = hA1;
    D.nbr[3 * B + j] = oX; D.nbr[oX] = 3 * B + j;
    (void)oY; (void)oW;                       // A.k+2 と B.j+2 は据え置き
    return true;
}
// 半辺の対合になっているか
static bool dual_ok(const Dual& D) {
    for (int h = 0; h < 3 * D.N; ++h) {
        int o = D.nbr[h];
        if (o < 0 || o >= 3 * D.N) return false;
        if (D.nbr[o] != h) return false;
        if (o / 3 == h / 3) return false;
    }
    return true;
}
// ★ 曲面のままかを検算する：頂点の数を数える。
//   頂点のまわりを回る置換は φ = next ∘ opp （next(t,k)=(t,k+1)）。その巡回の本数が V。
//   トーラスなら V - E + F = V - 3N/2 + N = 0 なので **V = N/2** でなければならない。
static int count_vertices(const Dual& D) {
    std::vector<char> seen(3 * D.N, 0);
    int V = 0;
    for (int h0 = 0; h0 < 3 * D.N; ++h0) {
        if (seen[h0]) continue;
        V++;
        int h = h0;
        do { seen[h] = 1; int o = D.nbr[h]; h = 3 * (o / 3) + (o % 3 + 1) % 3; } while (h != h0);
    }
    return V;
}

static void report(const char* tag, const std::vector<double>& Psum, long Pn,
                   const std::vector<double>& Vsum, const std::vector<long>& Vn, int sigmax) {
    printf("#\n# ===== %s =====\n", tag);
    printf("# スペクトル次元 d_s  （P(σ) ~ σ^{-d_s/2}）\n");
    printf("#%7s%16s%12s\n", "sigma", "P(sigma)", "d_s");
    for (int sg = 4; sg <= sigmax; sg = (int)(sg * 1.5) + 1) {
        int s2 = std::min(sigmax, (int)(sg * 1.5) + 1);
        if (s2 <= sg) break;
        double P1 = Psum[sg] / Pn, P2 = Psum[s2] / Pn;
        printf("%8d%16.6e%12.4f\n", sg, P1,
               -2.0 * (log(P2) - log(P1)) / (log((double)s2) - log((double)sg)));
    }
    printf("# ハウスドルフ次元 d_H  （V(r) ~ r^{d_H}）\n");
    printf("#%5s%16s%12s\n", "r", "V(r)", "d_H");
    for (size_t r = 2; r + 1 < Vsum.size(); r = (size_t)(r * 1.5) + 1) {
        size_t r2 = std::min(Vsum.size() - 1, (size_t)(r * 1.5) + 1);
        if (r2 <= r || Vn[r] == 0 || Vn[r2] == 0) break;
        double V1 = Vsum[r] / Vn[r], V2 = Vsum[r2] / Vn[r2];
        printf("%6zu%16.2f%12.4f\n", r, V1,
               (log(V2) - log(V1)) / (log((double)r2) - log((double)r)));
    }
}

int main(int argc, char** argv) {
    if (argc < 7) {
        fprintf(stderr, "usage: cdt2d_flip <T> <delta> <flipsweeps> <nmeas> <sigmax> <nstart> [seed]\n");
        return 1;
    }
    int    T      = atoi(argv[1]);
    double delta  = atof(argv[2]);
    long   fsw    = atol(argv[3]);      // フリップ掃引数（1掃引 = N 回の提案）
    int    nmeas  = atoi(argv[4]);
    int    sigmax = atoi(argv[5]);
    int    nstart = atoi(argv[6]);
    if (argc > 7) { s0 = (uint64_t)atoll(argv[7]) | 1ull; for (int i = 0; i < 20; ++i) rnd64(); }
    double lambda = LN2 + delta;

    LG.resize(4000000);
    for (int i = 0; i < (int)LG.size(); ++i) LG[i] = lgamma((double)std::max(1, i));

    std::vector<int> l(T, std::max(3, (int)(1.0 / sqrt(2 * delta))));
    const int bigStep = std::max(3, (int)(1.0 / sqrt(2 * delta)));
    auto local = [&](int t, int lt) {
        int p = l[(t - 1 + T) % T], n = l[(t + 1) % T];
        return lnK(p, lt) - lambda * (p + lt) + lnK(lt, n) - lambda * (lt + n);
    };
    auto sweep = [&]() {
        for (int k = 0; k < T; ++k) {
            int t = rndi(T), d;
            if (rnd() < 0.5) { d = rndi(6) - 3; if (d >= 0) d++; }
            else { d = rndi(2 * bigStep + 1) - bigStep; if (d == 0) continue; }
            int nl = l[t] + d;
            if (nl < 3) continue;                       // 双対が退化しないよう l>=3
            double w0 = local(t, l[t]), w1 = local(t, nl);
            if (w1 >= w0 || rnd() < exp(w1 - w0)) l[t] = nl;
        }
    };
    for (long s = 0; s < 4000; ++s) sweep();

    std::vector<double> PsC(sigmax + 1, 0.0), PsD(sigmax + 1, 0.0);
    long PnC = 0, PnD = 0;
    std::vector<double> VsC(1, 0.0), VsD(1, 0.0);
    std::vector<long>   VnC(1, 0),   VnD(1, 0);
    double sumN = 0; long nN = 0, okC = 0, okD = 0; long long accFlip = 0, tryFlip = 0;
    int vCDT = 0, vDT = 0;
    double rC = 0, rD = 0; long rnC = 0, rnD = 0;

    for (int m = 0; m < nmeas; ++m) {
        for (long s = 0; s < 600; ++s) sweep();

        // ---- CDT の三角形分割を作る（頂点つき）
        std::vector<int> off(T + 1); off[0] = 0;
        for (int t = 0; t < T; ++t) off[t + 1] = off[t] + l[t];
        int V = off[T];
        std::vector<int> tri;                       // 3個ずつ頂点
        tri.reserve(3 * 2 * V);
        for (int t = 0; t < T; ++t) {
            int L = l[t], Lp = l[(t + 1) % T], tn = (t + 1) % T;
            std::vector<char> w(L + Lp);
            for (int i = 0; i < L; ++i) w[i] = 'U';
            for (int i = L; i < L + Lp; ++i) w[i] = 'D';
            for (int i = L + Lp - 1; i >= 2; --i) { int jj = 1 + rndi(i); std::swap(w[i], w[jj]); }
            int lo = 0, up = rndi(Lp);
            for (int k = 0; k < L + Lp; ++k) {
                if (w[k] == 'U') {
                    tri.push_back(off[t] + lo); tri.push_back(off[t] + (lo + 1) % L);
                    tri.push_back(off[tn] + up % Lp);
                    lo = (lo + 1) % L;
                } else {
                    // ★ 向き付けを揃える。時間を上とすると、下向き三角形の反時計回りは
                    //   (上の右, 上の左, 下の頂点)。(up, up+1, lo) にすると向きが逆になり、
                    //   半辺が「同じ向き同士」で対になってフリップが曲面を壊す
                    tri.push_back(off[tn] + (up + 1) % Lp); tri.push_back(off[tn] + up % Lp);
                    tri.push_back(off[t] + lo);
                    up++;
                }
            }
        }
        int NT = (int)(tri.size() / 3);
        sumN += NT; nN++;

        // ---- 双対を作る： 辺 (v[k], v[k+1]) を共有する三角形を探す
        Dual D; D.N = NT; D.nbr.assign(3 * NT, -1);
        {
            std::map<std::pair<int,int>, std::pair<int,int>> em;   // 辺 -> (三角形, スロット)
            bool bad = false;
            for (int t = 0; t < NT && !bad; ++t) for (int k = 0; k < 3; ++k) {
                int a = tri[3 * t + k], b = tri[3 * t + (k + 1) % 3];
                if (a == b) { bad = true; break; }
                auto key = std::make_pair(std::min(a, b), std::max(a, b));
                auto it = em.find(key);
                if (it == em.end()) em[key] = {t, k};
                else {
                    int t2 = it->second.first, k2 = it->second.second;
                    D.nbr[3 * t + k] = 3 * t2 + k2; D.nbr[3 * t2 + k2] = 3 * t + k;
                    em.erase(it);
                }
            }
            if (bad || !em.empty()) { fprintf(stderr, "★ 双対が閉じない（残り辺 %zu）\n", em.size()); continue; }
        }
        if (!dual_ok(D)) { fprintf(stderr, "★ 双対の整合性エラー\n"); continue; }
        // 曲面のままか（トーラスなら V = N/2）
        { int Vc = count_vertices(D);
          if (Vc * 2 != NT) { fprintf(stderr, "★ CDT が曲面でない: V=%d, N/2=%d\n", Vc, NT / 2); continue; }
          vCDT = Vc; }
        okC++;

        // ---- 1: CDT のまま測る
        measure_ds(D, sigmax, nstart, PsC, PnC);
        measure_dH(D, nstart, VsC, VnC, &rC, &rnC);

        // ---- 2: フリップで因果律を消す（一様アンサンブル＝ユークリッド DT へ）
        for (long s = 0; s < fsw; ++s)
            for (int i = 0; i < NT; ++i) { tryFlip++; if (flip_once(D)) accFlip++; }
        if (!dual_ok(D)) { fprintf(stderr, "★ フリップ後に整合性エラー\n"); continue; }
        // ★ ここが要。フリップで曲面が壊れていないか（V=N/2 が保たれるか）を毎回見る
        { int Vc = count_vertices(D);
          if (Vc * 2 != NT) { fprintf(stderr, "★ フリップで曲面が壊れた: V=%d, N/2=%d\n", Vc, NT / 2); continue; }
          vDT = Vc; }
        okD++;

        // ---- 3: DT として測る
        measure_ds(D, sigmax, nstart, PsD, PnD);
        measure_dH(D, nstart, VsD, VnD, &rD, &rnD);
    }

    printf("# T=%d delta=%g  三角形数 <N>=%.0f  測定 %d 回  フリップ掃引 %ld  受理率 %.3f\n",
           T, delta, sumN / std::max(1L, nN), nmeas, fsw, (double)accFlip / (double)std::max(1LL, tryFlip));
    printf("# 双対の整合性: CDT %ld/%d  フリップ後 %ld/%d\n", okC, nmeas, okD, nmeas);
    printf("# 曲面チェック(トーラスなら V=N/2): CDT V=%d / フリップ後 V=%d / N/2=%.0f\n",
           vCDT, vDT, sumN / std::max(1L, nN) / 2);
    printf("# RSCALE  N= %.1f  rCDT= %.4f  rDT= %.4f\n",
           sumN / std::max(1L, nN), rC / std::max(1L, rnC), rD / std::max(1L, rnD));
    report("CDT（因果律あり・葉層あり）", PsC, PnC, VsC, VnC, sigmax);
    report("フリップ後（因果律なし＝2次元ユークリッド DT）", PsD, PnD, VsD, VnD, sigmax);
    return 0;
}
