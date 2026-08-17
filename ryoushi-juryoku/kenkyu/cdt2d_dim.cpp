// cdt2d_dim.cpp ── 2次元 CDT の【本物の三角形分割】を組んで、次元を2通りに測る。
//
// なぜやるか
// ----------
// 量子重力のどの仮説でも必ず引用される観測量が「スペクトル次元 d_s」で、
// 「短距離で 2 に落ちる（次元縮退）」が横断的な主張になっている。
// CDT4次元: 4→約2 / 漸近安全性: →2 / Hořava: z=3 から構成上 2。
// 自分で測れるようにしておかないと、この主張を裁けない。
//
// もうひとつ、次元は1つの数ではないという事実を確かめる：
//   ハウスドルフ次元 d_H  ── 半径 r の球に入る体積 V(r) ~ r^{d_H}
//   スペクトル次元   d_s  ── 拡散の戻り確率 P(σ) ~ σ^{-d_s/2}
// 2次元 CDT では両方 2 のはず。2次元ユークリッド DT（因果律なし）では d_H=4, d_s=2 と
// 【食い違う】ことが知られている ── つまり d_s だけ見ても幾何は分からない。
//
// 組み方
// ------
// 体積プロファイル {l_t} は前と同じメトロポリス（重み Π K(l_t,l_{t+1}) e^{-λN}）。
// 帯の中身は、プロファイルを固定すれば【一様分布】になる（重みが数え上げにしか依らないため）。
// step1 で確かめた表し方をそのまま使う:
//    下リンク i の三角形の頂点 apex[i] ∈ Z_{l'}、
//    d_i = apex[i+1]-apex[i] >= 0、Σd_i = l'、apex[0] は自由。
// → apex[0] を一様に、(d_i) を l' 個の星と l-1 本の棒のシャッフルで一様に引く。
//
// 使い方:
//   cdt2d_dim <T> <delta> <sweeps> <nmeas> <sigmax> <nstart> [seed]
//     delta = λ - ln2 （小さいほど宇宙が大きい。<l> ≒ 1/√(2δ)）

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdint>

static const double LN2 = 0.6931471805599453;

static uint64_t s0 = 88172645463325252ull, s1 = 362436069362436069ull;
static inline uint64_t rnd64() {
    uint64_t x = s0, y = s1;
    s0 = y; x ^= x << 23; s1 = x ^ y ^ (x >> 17) ^ (y >> 26);
    return s1 + y;
}
static inline double rnd() { return (rnd64() >> 11) * (1.0 / 9007199254740992.0); }
static inline int rndi(int n) { return (int)(rnd() * n); }

static std::vector<double> LG;
static inline double lg(int n) { return (n < (int)LG.size()) ? LG[n] : lgamma((double)n); }
static inline double lnK(int a, int b) { return lg(a + b) - lg(a) - lg(b + 1); }

int main(int argc, char** argv) {
    if (argc < 7) {
        fprintf(stderr, "usage: cdt2d_dim <T> <delta> <sweeps> <nmeas> <sigmax> <nstart> [seed]\n");
        return 1;
    }
    int    T      = atoi(argv[1]);
    double delta  = atof(argv[2]);
    long   sweeps = atol(argv[3]);
    int    nmeas  = atoi(argv[4]);
    int    sigmax = atoi(argv[5]);
    int    nstart = atoi(argv[6]);
    if (argc > 7) { s0 = (uint64_t)atoll(argv[7]) | 1ull; for (int i = 0; i < 20; ++i) rnd64(); }
    double lambda = LN2 + delta;

    const int LCAP = 200000;
    LG.resize(4 * LCAP + 4);
    for (int i = 0; i < (int)LG.size(); ++i) LG[i] = lgamma((double)std::max(1, i));

    // ---------------- プロファイルのモンテカルロ（時間もトーラス） ----------------
    std::vector<int> l(T, std::max(2, (int)(1.0 / sqrt(2 * delta))));
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
            if (nl < 1 || nl > LCAP) continue;
            double w0 = local(t, l[t]), w1 = local(t, nl);
            if (w1 >= w0 || rnd() < exp(w1 - w0)) l[t] = nl;
        }
    };
    for (long s = 0; s < sweeps * 5; ++s) sweep();     // 慣らし

    // ---------------- 測定 ----------------
    std::vector<double> Psum(sigmax + 1, 0.0);         // 戻り確率
    long Pn = 0;
    std::vector<double> Vsum(1, 0.0);                  // 距離 r 以内の頂点数
    std::vector<long>   Vn(1, 0);
    double sumN = 0; long nN = 0;
    long eulerOK = 0, eulerBad = 0, eulerSkip = 0;   // 三角形分割の検算カウンタ

    std::vector<int> off(T + 1);
    std::vector<int> apex;                             // 一時
    std::vector<int> adjStart, adjList;
    std::vector<double> p0, p1;
    std::vector<int> dist, queue_;

    for (int m = 0; m < nmeas; ++m) {
        for (long s = 0; s < sweeps; ++s) sweep();

        // --- 頂点の通し番号
        off[0] = 0;
        for (int t = 0; t < T; ++t) off[t + 1] = off[t] + l[t];
        int V = off[T];
        double Ntri = 0; for (int t = 0; t < T; ++t) Ntri += l[t] + l[(t + 1) % T];
        sumN += Ntri; nN++;

        // --- 辺を集める（重複は後で潰す）
        std::vector<std::pair<int,int>> ed;
        ed.reserve(3 * V + 16);
        for (int t = 0; t < T; ++t) {
            int L = l[t], Lp = l[(t + 1) % T];
            // 空間方向
            for (int i = 0; i < L; ++i) ed.push_back({off[t] + i, off[t] + (i + 1) % L});
            // 帯を一様に引く。
            // 帯を1周する三角形の列は、U（下を1つ進む＝上向き三角形）を L 個、
            // D（上を1つ進む＝下向き三角形）を Lp 個並べた語で決まる。
            // 下頂点0から下リンク0を渡るところから始めるので **先頭は必ず U**、
            // 残り L-1 個の U と Lp 個の D を一様にシャッフルする。開始の上頂点は一様。
            // （数は Lp × C(L+Lp-1, L-1) = N(L,Lp) で step1 の力ずく列挙と一致する）
            //
            // ※ 以前 apex[] だけで辺を張ったら、d_i>=2 のときの中間の上頂点への辺を
            //   取りこぼしていた。三角形を1つずつ作って3辺すべて張るのが安全。
            int tn = (t + 1) % T;
            {
                std::vector<char> w(L + Lp);
                for (int i = 0; i < L; ++i) w[i] = 'U';
                for (int i = L; i < L + Lp; ++i) w[i] = 'D';
                for (int i = L + Lp - 1; i >= 2; --i) { int j = 1 + rndi(i); std::swap(w[i], w[j]); }
                w[0] = 'U';
                int lo = 0, up = rndi(Lp);
                auto tri = [&](int a, int b, int c) {
                    ed.push_back({a, b}); ed.push_back({b, c}); ed.push_back({c, a});
                };
                for (int k = 0; k < L + Lp; ++k) {
                    if (w[k] == 'U') {
                        tri(off[t] + lo, off[t] + (lo + 1) % L, off[tn] + up % Lp);
                        lo = (lo + 1) % L;
                    } else {
                        tri(off[tn] + up % Lp, off[tn] + (up + 1) % Lp, off[t] + lo);
                        up++;
                    }
                }
            }
        }
        // 重複を潰して隣接リストへ（l=1 のスライスは自己ループを作るので落とす）
        for (auto& e : ed) if (e.first > e.second) std::swap(e.first, e.second);
        ed.erase(std::remove_if(ed.begin(), ed.end(),
                 [](const std::pair<int,int>& e){ return e.first == e.second; }), ed.end());
        std::sort(ed.begin(), ed.end());
        ed.erase(std::unique(ed.begin(), ed.end()), ed.end());
        // ★ 三角形分割が正しく張れているかの検算：トーラスなら V - E + F = 0。
        //   V=Σl, F=Σ(l_t+l_{t+1})=2Σl なので E は 3Σl でなければならない。
        {
            long Eexp = 3L * (long)V, Egot = (long)ed.size();
            bool tiny = false; for (int t = 0; t < T; ++t) if (l[t] <= 2) tiny = true;
            if (Egot != Eexp && !tiny) {
                eulerBad++;
                if (eulerBad <= 3)
                    fprintf(stderr, "★オイラー不一致: V=%d F=%.0f E=%ld (期待 %ld)\n",
                            V, Ntri, Egot, Eexp);
            } else if (Egot == Eexp) eulerOK++;
            else eulerSkip++;
        }
        std::vector<int> deg(V, 0);
        for (auto& e : ed) { deg[e.first]++; deg[e.second]++; }
        adjStart.assign(V + 1, 0);
        for (int v = 0; v < V; ++v) adjStart[v + 1] = adjStart[v] + deg[v];
        adjList.assign(adjStart[V], 0);
        std::vector<int> fill(adjStart.begin(), adjStart.end() - 1);
        for (auto& e : ed) { adjList[fill[e.first]++] = e.second; adjList[fill[e.second]++] = e.first; }

        // --- 拡散（戻り確率）: 出発点に δ を置いて σ ステップ回し、出発点の確率を読む
        p0.assign(V, 0.0); p1.assign(V, 0.0);
        for (int st = 0; st < nstart; ++st) {
            int v0 = rndi(V);
            std::fill(p0.begin(), p0.end(), 0.0);
            p0[v0] = 1.0;
            Psum[0] += 1.0;
            for (int sg = 1; sg <= sigmax; ++sg) {
                std::fill(p1.begin(), p1.end(), 0.0);
                for (int v = 0; v < V; ++v) {
                    double pv = p0[v];
                    if (pv == 0.0) continue;
                    int a = adjStart[v], b = adjStart[v + 1];
                    double share = pv / (double)(b - a);
                    for (int j = a; j < b; ++j) p1[adjList[j]] += share;
                }
                p0.swap(p1);
                Psum[sg] += p0[v0];
            }
            Pn++;
        }

        // --- 球の体積 V(r)（グラフ距離）
        dist.assign(V, -1);
        for (int st = 0; st < std::min(nstart, 24); ++st) {
            int v0 = rndi(V);
            std::fill(dist.begin(), dist.end(), -1);
            queue_.clear(); queue_.push_back(v0); dist[v0] = 0;
            size_t head = 0; int cnt = 1;
            std::vector<int> byR;
            byR.push_back(1);
            int cur = 0;
            while (head < queue_.size()) {
                int v = queue_[head++];
                if (dist[v] > cur) { cur = dist[v]; byR.push_back(cnt); }
                int a = adjStart[v], b = adjStart[v + 1];
                for (int j = a; j < b; ++j) {
                    int u = adjList[j];
                    if (dist[u] < 0) { dist[u] = dist[v] + 1; queue_.push_back(u); cnt++; }
                }
            }
            byR.push_back(cnt);
            if (byR.size() > Vsum.size()) { Vsum.resize(byR.size(), 0.0); Vn.resize(byR.size(), 0); }
            for (size_t r = 0; r < byR.size(); ++r) { Vsum[r] += byR[r]; Vn[r]++; }
        }
    }

    printf("# 2D CDT  T=%d  delta=%.6f (lambda=%.8f)  nmeas=%d  sigmax=%d  nstart=%d\n",
           T, delta, lambda, nmeas, sigmax, nstart);
    printf("# オイラー検算 V-E+F=0: 一致 %ld / 不一致 %ld / 判定外(l<=2を含む) %ld\n",
           eulerOK, eulerBad, eulerSkip);
    printf("# <N(三角形)> = %.1f   （厳密予言 <l>=1/sqrt(2delta)=%.2f → N≒2T<l>=%.0f）\n",
           sumN / nN, 1.0 / sqrt(2 * delta), 2.0 * T / sqrt(2 * delta));
    printf("#\n# --- スペクトル次元： P(σ) ~ σ^{-d_s/2},  d_s = -2 dlnP/dlnσ ---\n");
    printf("#%7s%16s%12s\n", "sigma", "P(sigma)", "d_s");
    for (int sg = 2; sg <= sigmax; sg = (int)(sg * 1.35) + 1) {
        int s2 = std::min(sigmax, (int)(sg * 1.35) + 1);
        if (s2 <= sg) break;
        double P1 = Psum[sg] / Pn, P2 = Psum[s2] / Pn;
        double ds = -2.0 * (log(P2) - log(P1)) / (log((double)s2) - log((double)sg));
        printf("%8d%16.8e%12.4f\n", sg, P1, ds);
    }
    printf("#\n# --- ハウスドルフ次元： V(r) ~ r^{d_H} ---\n");
    printf("#%5s%16s%12s\n", "r", "V(r)", "d_H");
    for (size_t r = 2; r + 1 < Vsum.size(); r = (size_t)(r * 1.4) + 1) {
        size_t r2 = std::min(Vsum.size() - 1, (size_t)(r * 1.4) + 1);
        if (r2 <= r || Vn[r] == 0 || Vn[r2] == 0) break;
        double V1 = Vsum[r] / Vn[r], V2 = Vsum[r2] / Vn[r2];
        double dh = (log(V2) - log(V1)) / (log((double)r2) - log((double)r));
        printf("%6zu%16.2f%12.4f\n", r, V1, dh);
    }
    return 0;
}
