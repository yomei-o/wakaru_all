// cdt2d_c1.cpp ── c=1 の壁を自分で叩く。
//
// 何を確かめたいか
// ----------------
// 2次元ユークリッド重力に物質を載せると、中心電荷 c が 1 を超えたところで壊れる：
// KPZ の式 Δ = (√(1-c+24Δ0) - √(1-c)) / (√(25-c) - √(1-c)) の平方根が複素数になり、
// 数値的には幾何が【枝分かれポリマー】に潰れる（d_H が 4 から 2 へ、d_s は 4/3 へ）。
// これがユークリッド DT で物理的な物質量を扱えない理由＝この路線が行き詰まった直接の原因。
//
// CDT にはこの壁が無いとされる。同じコードで確かめる。
//
// やり方：イジングを n 枚（独立なコピー）載せる。1枚が c=1/2 なので c = n/2。
//   n = 0, 1, 2, 3, 4, 6, 8  →  c = 0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0
// 幾何が壊れたかどうかは【平均グラフ距離 <r>】で見る：
//   c=0 のユークリッド DT は d_H=4 なので <r> ~ N^{1/4}（小さい）
//   枝分かれポリマーは d_H=2 なので <r> ~ N^{1/2}（大きい）
// つまり **壁を越えると DT の宇宙は急に「細長く」なる**。CDT は変わらないはず。
//
// 使い方:
//   cdt2d_c1 <T> <L> <cdt|dt> <ncopy> scan <b0> <b1> <nb> <sweeps> <meas> [seed]

#include <cstdio>
#include <cstdlib>
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
    int N, nc;                   // 三角形の数 / イジングのコピー数
    std::vector<int>  opp;       // opp[3t+k] = 相手の半辺 3u+j
    std::vector<char> space, isUp;
    std::vector<signed char> s;  // s[a*N+v]
};

static bool build(Geo& G, int T, int L, int nc) {
    int N = T * 2 * L;
    G.N = N; G.nc = nc;
    G.opp.assign(3 * N, -1); G.space.assign(3 * N, 0); G.isUp.assign(N, 0);
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
                tri[3*idx] = t*L+lo; tri[3*idx+1] = t*L+(lo+1)%L; tri[3*idx+2] = tn*L+up%L;
                G.isUp[idx] = 1; lo = (lo+1)%L;
            } else {
                tri[3*idx] = tn*L+(up+1)%L; tri[3*idx+1] = tn*L+up%L; tri[3*idx+2] = t*L+lo;
                G.isUp[idx] = 0; up++;
            }
            G.space[3*idx] = 1;
        }
    }
    std::map<std::pair<int,int>, int> em;
    for (int t = 0; t < N; ++t) for (int k = 0; k < 3; ++k) {
        int a = tri[3*t+k], b = tri[3*t+(k+1)%3];
        if (a == b) return false;
        auto key = std::make_pair(std::min(a,b), std::max(a,b));
        auto it = em.find(key);
        if (it == em.end()) em[key] = 3*t+k;
        else { G.opp[3*t+k] = it->second; G.opp[it->second] = 3*t+k; em.erase(it); }
    }
    if (!em.empty()) return false;
    G.s.assign((size_t)std::max(1,nc) * N, 1);
    for (size_t i = 0; i < G.s.size(); ++i) G.s[i] = (rnd() < 0.5) ? -1 : 1;
    return true;
}

static int count_vertices(const Geo& G) {
    std::vector<char> seen(3*G.N, 0); int V = 0;
    for (int h0 = 0; h0 < 3*G.N; ++h0) {
        if (seen[h0]) continue;
        V++; int h = h0;
        do { seen[h] = 1; int o = G.opp[h]; h = 3*(o/3) + (o%3+1)%3; } while (h != h0);
    }
    return V;
}

// 全コピー合計のエネルギー変化で幾何を動かす
static bool flip(Geo& G, bool causal, double beta) {
    int A = rndi(G.N), k = rndi(3);
    int h = 3*A+k, hb = G.opp[h];
    int B = hb/3, j = hb%3;
    if (B == A) return false;
    if (causal) { if (G.space[h]) return false; if (G.isUp[A] == G.isUp[B]) return false; }
    int hA1 = 3*A+(k+1)%3, hB1 = 3*B+(j+1)%3;
    int oX = G.opp[hA1], oY = G.opp[3*A+(k+2)%3], oZ = G.opp[hB1], oW = G.opp[3*B+(j+2)%3];
    for (int o : {oX, oY, oZ, oW}) { int tt = o/3; if (tt == A || tt == B) return false; }
    int X = oX/3, Z = oZ/3;
    double d = 0;
    for (int a = 0; a < G.nc; ++a) {
        const signed char* s = &G.s[(size_t)a*G.N];
        d += (double)(s[A]-s[B]) * (double)(s[X]-s[Z]);
    }
    if (d > 0 && rnd() >= exp(-beta*d)) return false;
    char sA1 = G.space[hA1], sB1 = G.space[hB1];
    G.space[h] = sB1; G.space[hA1] = 0; G.space[3*B+j] = sA1; G.space[hB1] = 0;
    G.opp[h] = oZ; G.opp[oZ] = h;
    G.opp[hA1] = hB1; G.opp[hB1] = hA1;
    G.opp[3*B+j] = oX; G.opp[oX] = 3*B+j;
    return true;
}

static std::vector<int> wstack;
static void wolff(Geo& G, double beta) {
    if (G.nc == 0) return;
    int a = rndi(G.nc);
    signed char* s = &G.s[(size_t)a*G.N];
    double padd = 1.0 - exp(-2.0*beta);
    int v0 = rndi(G.N); signed char sv = s[v0];
    wstack.clear(); wstack.push_back(v0); s[v0] = (signed char)(-sv);
    while (!wstack.empty()) {
        int v = wstack.back(); wstack.pop_back();
        for (int k = 0; k < 3; ++k) {
            int u = G.opp[3*v+k]/3;
            if (s[u] == sv && rnd() < padd) { s[u] = (signed char)(-sv); wstack.push_back(u); }
        }
    }
}
static void spin_sweep(Geo& G, double beta) {
    for (int a = 0; a < G.nc; ++a) {
        signed char* s = &G.s[(size_t)a*G.N];
        for (int n = 0; n < G.N; ++n) {
            int v = rndi(G.N); int sum = 0;
            for (int k = 0; k < 3; ++k) sum += s[G.opp[3*v+k]/3];
            double d = 2.0 * s[v] * sum;
            if (d <= 0 || rnd() < exp(-beta*d)) s[v] = (signed char)(-s[v]);
        }
    }
}
static double energy(const Geo& G) {
    double E = 0;
    for (int a = 0; a < G.nc; ++a) {
        const signed char* s = &G.s[(size_t)a*G.N];
        for (int v = 0; v < G.N; ++v) for (int k = 0; k < 3; ++k) E -= s[v]*s[G.opp[3*v+k]/3];
    }
    return E * 0.5;
}
// 拡散の戻り確率 P(σ) ~ σ^{-d_s/2}。双対は二部グラフに近いので【怠惰ウォーク】を使う
static void measure_ds(const Geo& G, int sigmax, int nstart,
                       std::vector<double>& Psum, long& Pn) {
    std::vector<double> p0(G.N), p1(G.N);
    for (int st = 0; st < nstart; ++st) {
        int v0 = rndi(G.N);
        std::fill(p0.begin(), p0.end(), 0.0); p0[v0] = 1.0;
        for (int sg = 1; sg <= sigmax; ++sg) {
            std::fill(p1.begin(), p1.end(), 0.0);
            for (int v = 0; v < G.N; ++v) {
                double pv = p0[v]; if (pv == 0.0) continue;
                p1[v] += 0.5*pv;
                double sh = pv/6.0;
                p1[G.opp[3*v]/3] += sh; p1[G.opp[3*v+1]/3] += sh; p1[G.opp[3*v+2]/3] += sh;
            }
            p0.swap(p1);
            Psum[sg] += p0[v0];
        }
        Pn++;
    }
}
static double meandist(const Geo& G, int nstart) {
    std::vector<int> dist(G.N), q; double acc = 0;
    for (int st = 0; st < nstart; ++st) {
        std::fill(dist.begin(), dist.end(), -1);
        int v0 = rndi(G.N); q.clear(); q.push_back(v0); dist[v0] = 0;
        size_t head = 0;
        while (head < q.size()) {
            int v = q[head++];
            for (int k = 0; k < 3; ++k) { int u = G.opp[3*v+k]/3;
                if (dist[u] < 0) { dist[u] = dist[v]+1; q.push_back(u); } }
        }
        double sm = 0; for (int v = 0; v < G.N; ++v) sm += dist[v];
        acc += sm / G.N;
    }
    return acc / nstart;
}

int main(int argc, char** argv) {
    if (argc < 10) {
        fprintf(stderr, "usage: cdt2d_c1 <T> <L> <cdt|dt> <ncopy> scan <b0> <b1> <nb> <sweeps> <meas> [seed]\n");
        return 1;
    }
    int T = atoi(argv[1]), L = atoi(argv[2]);
    std::string mode = argv[3];
    bool causal = (mode == "cdt");
    int nc = atoi(argv[4]);
    double b0 = atof(argv[6]), b1 = atof(argv[7]);
    int nb = atoi(argv[8]); long sweeps = atol(argv[9]);
    int meas = (argc > 10) ? atoi(argv[10]) : 200;
    if (argc > 11) { s0 = (uint64_t)atoll(argv[11]) | 1ull; for (int i = 0; i < 20; ++i) rnd64(); }

    // スペクトル次元も測る（環境変数 SIGMAX で拡散のステップ数を指定。0 なら測らない）
    int SIGMAX = 0;
    { const char* e = getenv("SIGMAX"); if (e) SIGMAX = atoi(e); }
    Geo G;
    if (!build(G, T, L, nc)) { fprintf(stderr, "初期配位を作れなかった\n"); return 1; }
    int V0 = count_vertices(G);
    printf("# %s  T=%d L=%d N=%d  イジング %d 枚 (c=%.1f)  曲面 V=%d(N/2=%d)%s\n",
           causal ? "CDT" : "DT", T, L, G.N, nc, nc*0.5, V0, G.N/2,
           (V0*2 == G.N) ? " OK" : " ★NG");
    printf("#%9s%12s%14s%12s%10s\n", "beta", "<e>", "C(比熱)", "<r>", "flip受理");

    for (int ib = 0; ib < nb; ++ib) {
        double beta = (nb == 1) ? b0 : b0 + (b1-b0)*ib/(nb-1);
        long long fa = 0, ft = 0;
        auto one = [&]() {
            for (int c = 0; c < 4; ++c) wolff(G, beta);
            spin_sweep(G, beta);
            for (int i = 0; i < G.N; ++i) { ft++; if (flip(G, causal, beta)) fa++; }
        };
        for (long sw = 0; sw < sweeps; ++sw) one();
        double sE = 0, sE2 = 0, sr = 0; long nm = 0;
        std::vector<double> Psum(SIGMAX+1, 0.0); long Pn = 0;
        for (int m = 0; m < meas; ++m) {
            for (int sw = 0; sw < 3; ++sw) one();
            double e = energy(G);
            sE += e; sE2 += e*e; nm++;
            if (m % 20 == 0) sr += meandist(G, 2);
            if (SIGMAX > 0 && m % 25 == 0) measure_ds(G, SIGMAX, 2, Psum, Pn);
        }
        if (SIGMAX > 0 && Pn > 0) {
            printf("#   d_s:");
            for (int sg = 8; sg <= SIGMAX/2; sg = (int)(sg*1.7)+1) {
                int s2 = std::min(SIGMAX, (int)(sg*1.7)+1);
                if (s2 <= sg) break;
                double P1 = Psum[sg]/Pn, P2 = Psum[s2]/Pn;
                printf("  s=%d:%.3f", sg, -2.0*(log(P2)-log(P1))/(log((double)s2)-log((double)sg)));
            }
            printf("\n");
        }
        double mE = sE/nm;
        double C = (nc ? beta*beta*(sE2/nm - mE*mE)/G.N : 0.0);
        printf("%10.5f%12.5f%14.5f%12.2f%10.3f\n",
               beta, (nc ? mE/G.N/nc : 0.0), C, sr/((meas+19)/20), (double)fa/(double)ft);
        fflush(stdout);
    }
    int V1 = count_vertices(G);
    printf("# 終了時の曲面チェック V=%d (N/2=%d)%s\n", V1, G.N/2, (V1*2 == G.N) ? " OK" : " ★NG");
    return 0;
}
