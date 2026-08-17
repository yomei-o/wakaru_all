// cdt2d_matter.cpp ── 「量子重力は物質の振る舞いを変えるか」を測る。
//
// 今日ここまでで分かったこと
// --------------------------
// 2次元では、CDT と ユークリッド DT の差は【どのフリップを許すか】だけに落ちる：
//   ・空間的な辺（同じ時刻の2点を結ぶ辺）をフリップすると、3つの時刻にまたがる三角形が
//     できて葉層が壊れる → 禁止
//   ・時間的な辺でも U と U（同種）のあいだをフリップすると、スライスの中に潰れた三角形が
//     できる → 禁止
//   ・時間的な辺の U と D のあいだだけが許され、それは語の中の UD ↔ DU の入れ替えに等しい
// したがって
//     DT  = すべてのフリップ
//     CDT = 「時間的 かつ U-D」のフリップだけ
// 実装は if 一行。**同じコード・同じ体積・同じトポロジーで因果律だけを切り替えられる。**
//
// この上にイジング模型を載せる（スピンは三角形＝双対の格子点、次数はどこも3）。
//   H = -J Σ_<ij> s_i s_j
// 幾何とスピンを一緒に動かす（アニール）。2次元では純重力の作用が位相不変量なので、
// 全体の重み exp(-β H) だけで (幾何, スピン) を同時にサンプルすればよい。
//
// 期待される答え（文献）:
//   ユークリッド DT + イジング  … KPZ ドレッシングで指数が変わる（α = -1）→ 比熱は発散しない
//   CDT + イジング              … オンサーガーのまま（α = 0）→ 比熱は ln N で発散する
// つまり **比熱のピークが ln N で伸びるか、頭打ちになるか** が判定になる。
// 指数の規約も d_H も要らない、規約フリーの判別。
//
// フリップで変わる双対の辺は2本だけなので、イジングのエネルギー変化は
//     ΔE = J (s_A - s_B)(s_X - s_Z)
// と閉じた形になる（A-X と B-Z が消えて A-Z と B-X ができる。A-B は残る）。
//
// 使い方:
//   cdt2d_matter <T> <L> <mode:cdt|dt> <beta> <sweeps> <meas> [seed]
//   cdt2d_matter <T> <L> <mode> scan <b0> <b1> <nb> <sweeps> <meas> [seed]

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cstdint>

static uint64_t s0 = 88172645463325252ull, s1 = 362436069362436069ull;
static inline uint64_t rnd64() {
    uint64_t x = s0, y = s1; s0 = y; x ^= x << 23; s1 = x ^ y ^ (x >> 17) ^ (y >> 26); return s1 + y;
}
static inline double rnd() { return (rnd64() >> 11) * (1.0 / 9007199254740992.0); }
static inline int rndi(int n) { return (int)(rnd() * n); }

struct Geo {
    int N;                       // 三角形の数
    std::vector<int>  opp;       // opp[3t+k] = 相手の半辺 3u+j
    std::vector<char> space;     // space[3t+k] : その辺が空間的か
    std::vector<char> isUp;      // isUp[t]
    std::vector<signed char> s;  // イジングスピン（三角形ごと）
};

// ---- 固定プロファイル l_t = L, T スライス（時間方向もトーラス）で CDT 配位を作る
static bool build(Geo& G, int T, int L) {
    int Nstrip = 2 * L, N = T * Nstrip;
    G.N = N; G.opp.assign(3 * N, -1); G.space.assign(3 * N, 0); G.isUp.assign(N, 0);
    std::vector<int> tri(3 * N);
    int idx = 0;
    for (int t = 0; t < T; ++t) {
        int tn = (t + 1) % T;
        std::vector<char> w(2 * L);
        for (int i = 0; i < L; ++i) w[i] = 'U';
        for (int i = L; i < 2 * L; ++i) w[i] = 'D';
        for (int i = 2 * L - 1; i >= 2; --i) { int j = 1 + rndi(i); std::swap(w[i], w[j]); }
        w[0] = 'U';
        int lo = 0, up = rndi(L);
        for (int k = 0; k < 2 * L; ++k, ++idx) {
            if (w[k] == 'U') {
                // U: (lo, lo+1, up)   スロット0 = lo→lo+1 が空間的
                tri[3 * idx] = t * L + lo; tri[3 * idx + 1] = t * L + (lo + 1) % L;
                tri[3 * idx + 2] = tn * L + up % L;
                G.isUp[idx] = 1; lo = (lo + 1) % L;
            } else {
                // D: (up+1, up, lo)   スロット0 = up+1→up が空間的（向きは反時計回り）
                tri[3 * idx] = tn * L + (up + 1) % L; tri[3 * idx + 1] = tn * L + up % L;
                tri[3 * idx + 2] = t * L + lo;
                G.isUp[idx] = 0; up++;
            }
            G.space[3 * idx] = 1;
        }
    }
    std::map<std::pair<int,int>, int> em;
    for (int t = 0; t < N; ++t) for (int k = 0; k < 3; ++k) {
        int a = tri[3 * t + k], b = tri[3 * t + (k + 1) % 3];
        if (a == b) return false;
        auto key = std::make_pair(std::min(a, b), std::max(a, b));
        auto it = em.find(key);
        if (it == em.end()) em[key] = 3 * t + k;
        else { G.opp[3 * t + k] = it->second; G.opp[it->second] = 3 * t + k; em.erase(it); }
    }
    if (!em.empty()) return false;
    for (int h = 0; h < 3 * N; ++h) if (G.opp[h] < 0) return false;
    G.s.assign(N, 1);
    for (int i = 0; i < N; ++i) G.s[i] = (rnd() < 0.5) ? -1 : 1;
    return true;
}

// 曲面のままか（トーラスなら V = N/2）
static int count_vertices(const Geo& G) {
    std::vector<char> seen(3 * G.N, 0);
    int V = 0;
    for (int h0 = 0; h0 < 3 * G.N; ++h0) {
        if (seen[h0]) continue;
        V++; int h = h0;
        do { seen[h] = 1; int o = G.opp[h]; h = 3 * (o / 3) + (o % 3 + 1) % 3; } while (h != h0);
    }
    return V;
}

// ---- フリップ。causal=true なら CDT（時間的 かつ U-D のみ）
// 双対で消える辺は A-X と B-Z、できる辺は A-Z と B-X。A-B は残る。
//   ΔE = J (s_A - s_B)(s_X - s_Z)      （H = -J Σ s_i s_j、J=1 とする）
static bool flip(Geo& G, bool causal, double beta, double* dE) {
    int A = rndi(G.N), k = rndi(3);
    int h = 3 * A + k, hb = G.opp[h];
    int B = hb / 3, j = hb % 3;
    if (B == A) return false;
    if (causal) {
        if (G.space[h]) return false;                 // 空間的な辺は葉層を壊す
        if (G.isUp[A] == G.isUp[B]) return false;     // 同種どうしはスライス内に潰れる
    }
    int hA1 = 3 * A + (k + 1) % 3, hA2 = 3 * A + (k + 2) % 3;
    int hB1 = 3 * B + (j + 1) % 3, hB2 = 3 * B + (j + 2) % 3;
    int oX = G.opp[hA1], oY = G.opp[hA2], oZ = G.opp[hB1], oW = G.opp[hB2];
    for (int o : {oX, oY, oZ, oW}) { int tt = o / 3; if (tt == A || tt == B) return false; }
    int X = oX / 3, Z = oZ / 3;
    double d = (double)(G.s[A] - G.s[B]) * (double)(G.s[X] - G.s[Z]);
    if (d > 0 && rnd() >= exp(-beta * d)) return false;
    // 空間性フラグの移動（CDT の U-D フリップでは結局どれも動かないが、DT では意味を失う）
    char sA = G.space[h], sA1 = G.space[hA1], sB1 = G.space[hB1];
    (void)sA;
    G.space[h] = sB1; G.space[hA1] = 0;
    G.space[3 * B + j] = sA1; G.space[hB1] = 0;
    G.opp[h] = oZ;   G.opp[oZ] = h;
    G.opp[hA1] = hB1; G.opp[hB1] = hA1;
    G.opp[3 * B + j] = oX; G.opp[oX] = 3 * B + j;
    (void)oY; (void)oW; (void)hB2; (void)hA2;
    *dE += d;
    return true;
}

// ---- Wolff クラスター更新。
// 臨界点近くではメトロポリスの緩和が絶望的に遅い（実際、幾何を動かすと m が
// 20000掃引でもまだ上がり続けていた）。Wolff は任意のグラフでそのまま使える：
// 同じ向きの隣を確率 p=1-e^{-2β} でクラスターに入れ、まとめて反転する。
static std::vector<int> wstack;
static void wolff(Geo& G, double beta) {
    double padd = 1.0 - exp(-2.0 * beta);
    int v0 = rndi(G.N);
    signed char sv = G.s[v0];
    wstack.clear(); wstack.push_back(v0); G.s[v0] = (signed char)(-sv);
    while (!wstack.empty()) {
        int v = wstack.back(); wstack.pop_back();
        for (int k = 0; k < 3; ++k) {
            int u = G.opp[3 * v + k] / 3;
            if (G.s[u] == sv && rnd() < padd) { G.s[u] = (signed char)(-sv); wstack.push_back(u); }
        }
    }
}

// ---- スピンの1掃引（メトロポリス）
static void spin_sweep(Geo& G, double beta, double* E) {
    for (int n = 0; n < G.N; ++n) {
        int v = rndi(G.N);
        int sum = 0;
        for (int k = 0; k < 3; ++k) sum += G.s[G.opp[3 * v + k] / 3];
        double d = 2.0 * G.s[v] * sum;               // ΔE = 2 s_v Σ s_nb  (H=-Σ s s)
        if (d <= 0 || rnd() < exp(-beta * d)) { G.s[v] = -G.s[v]; *E += d; }
    }
}
static double energy(const Geo& G) {
    double E = 0;
    for (int v = 0; v < G.N; ++v) for (int k = 0; k < 3; ++k) E -= G.s[v] * G.s[G.opp[3 * v + k] / 3];
    return E * 0.5;                                   // 辺を2回数えている
}
static double magn(const Geo& G) {
    long m = 0; for (int v = 0; v < G.N; ++v) m += G.s[v];
    return fabs((double)m);
}
// 平均グラフ距離（幾何が壊れていないかの目安。d_H の代理）
static double meandist(const Geo& G, int nstart) {
    std::vector<int> dist(G.N), q; double acc = 0;
    for (int st = 0; st < nstart; ++st) {
        std::fill(dist.begin(), dist.end(), -1);
        int v0 = rndi(G.N); q.clear(); q.push_back(v0); dist[v0] = 0;
        size_t head = 0;
        while (head < q.size()) {
            int v = q[head++];
            for (int k = 0; k < 3; ++k) { int u = G.opp[3 * v + k] / 3;
                if (dist[u] < 0) { dist[u] = dist[v] + 1; q.push_back(u); } }
        }
        double sm = 0; for (int v = 0; v < G.N; ++v) sm += dist[v];
        acc += sm / G.N;
    }
    return acc / nstart;
}

int main(int argc, char** argv) {
    if (argc < 6) {
        fprintf(stderr,
          "usage: cdt2d_matter <T> <L> <cdt|dt> <beta> <sweeps> <meas> [seed]\n"
          "       cdt2d_matter <T> <L> <cdt|dt> scan <b0> <b1> <nb> <sweeps> <meas> [seed]\n");
        return 1;
    }
    int T = atoi(argv[1]), L = atoi(argv[2]);
    // mode: cdt=因果律あり / dt=因果律なし / fix=幾何を凍結（物質コードの検証用）
    std::string mode = argv[3];
    bool causal = (mode == "cdt");
    bool frozen = (mode == "fix");
    bool isScan = (std::string(argv[4]) == "scan");
    double b0, b1; int nb; long sweeps; int meas;
    if (isScan) {
        b0 = atof(argv[5]); b1 = atof(argv[6]); nb = atoi(argv[7]);
        sweeps = atol(argv[8]); meas = atoi(argv[9]);
        if (argc > 10) { s0 = (uint64_t)atoll(argv[10]) | 1ull; for (int i = 0; i < 20; ++i) rnd64(); }
    } else {
        b0 = b1 = atof(argv[4]); nb = 1; sweeps = atol(argv[5]); meas = atoi(argv[6]);
        if (argc > 7) { s0 = (uint64_t)atoll(argv[7]) | 1ull; for (int i = 0; i < 20; ++i) rnd64(); }
    }

    Geo G;
    if (!build(G, T, L)) { fprintf(stderr, "初期配位を作れなかった\n"); return 1; }
    int V0 = count_vertices(G);
    printf("# 2D %s + Ising   T=%d L=%d  N=%d  曲面チェック V=%d (N/2=%d) %s\n",
           frozen ? "凍結格子(幾何を動かさない)" : (causal ? "CDT(因果律あり)" : "DT(因果律なし)"),
           T, L, G.N, V0, G.N / 2,
           (V0 * 2 == G.N) ? "OK" : "★NG");
    printf("#%9s%12s%14s%14s%14s%12s%10s\n",
           "beta", "<e>", "C(比熱)", "<m>", "chi", "<r>", "flip受理");

    for (int ib = 0; ib < nb; ++ib) {
        double beta = (nb == 1) ? b0 : b0 + (b1 - b0) * ib / (nb - 1);
        long long fa = 0, ft = 0;
        double dummy = 0;
        // 1掃引 = Wolff を数発 + メトロポリス1掃引 + 幾何フリップ N 回。
        // エネルギーは測定のたびに直接計算する（差分追跡はやめた。バグの温床だった）
        auto one_sweep = [&]() {
            for (int c = 0; c < 4; ++c) wolff(G, beta);
            spin_sweep(G, beta, &dummy);
            if (!frozen) for (int i = 0; i < G.N; ++i) { ft++; if (flip(G, causal, beta, &dummy)) fa++; }
        };
        for (long sw = 0; sw < sweeps; ++sw) one_sweep();
        double sE = 0, sE2 = 0, sM = 0, sM2 = 0; long nm = 0;
        for (int m = 0; m < meas; ++m) {
            for (long sw = 0; sw < 3; ++sw) one_sweep();
            double e = energy(G), mm = magn(G);
            sE += e; sE2 += e * e; sM += mm; sM2 += mm * mm; nm++;
        }
        double mE = sE / nm, mM = sM / nm;
        double C = beta * beta * (sE2 / nm - mE * mE) / G.N;
        double chi = beta * (sM2 / nm - mM * mM) / G.N;
        // エネルギーのドリフト検算（差分で追ったものと直接計算が合うか）
        printf("%10.5f%12.5f%14.5f%14.5f%14.4f%12.2f%10.3f\n",
               beta, mE / G.N, C, mM / G.N, chi, meandist(G, 3),
               ft ? (double)fa / (double)ft : 0.0);
        fflush(stdout);
    }
    int V1 = count_vertices(G);
    printf("# 終了時の曲面チェック V=%d (N/2=%d) %s\n", V1, G.N / 2, (V1 * 2 == G.N) ? "OK" : "★NG");
    return 0;
}
