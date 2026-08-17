// cdt2d_vol.cpp ── 体積が変わる CDT（＋物質）。
//
// これまでの CDT はプロファイル固定（l_t = L）だった。それだと体積を再配分できないので、
// 「CDT は c=1 の壁を持たない」を裁けない（もともと d_H=2 に縛られている）。
// ここでは**スライスへの頂点の挿入・削除**を入れて、プロファイルを自由にする。
//
// 手（すべて葉層を保つ）
// ----------------------
//  ・フリップ： 時間的 かつ U-D の辺だけ（第3回で導出したとおり）
//  ・挿入：     スライス t の空間的な辺 ab に頂点 m を入れる。
//                 A=(a,b,c)[U] → A1=(a,m,c), A2=(m,b,c)   どちらも U
//                 B=(b,a,d)[D] → B1=(b,m,d), B2=(m,a,d)   どちらも D
//               三角形 +2、l_t +1。オイラーは V+1,E+3,F+2 で不変。
//  ・削除：     挿入の逆。CDT では **頂点の次数が 4 ⟺ 挿入で作られた頂点**。
//               （スライス t の頂点の次数は 2+2+u+d。u,d は「その頂点を尖端とする三角形」の数で、
//                 次数4 ⟺ u=d=0 ⟺ 4枚パターン）
//
// 詳細釣合い（グローバルな数え上げを使わない）
// -------------------------------------------
//   挿入は半辺を一様に1本引いて空間的なら実行（1辺=半辺2本）
//   削除は半辺を一様に1本引いてその根元の頂点の次数が4なら実行（次数4の頂点=半辺4本）
//   ⇒ 挿入 min(1, e^{-2λ}·2N/N')   削除 min(1, e^{+2λ}·N'/(2N))
//
// 物質（任意）
// ------------
//   イジングを nc 枚。1三角形につき uint32 のビットマスクで持つ。
//   Σ_a s^a_i s^a_j = nc - 2·popcount(x_i XOR x_j)
//   挿入で増える2枚には**ランダムな**スピンを与え、その分の 2^{2nc} を受理に入れる
//   （追加した自由度のエントロピーそのもの。これを入れないと詳細釣合いが壊れる）。
//   体積が暴れないよう、体積固定項 ε(N-N0)^2 を入れられる。
//
// 使い方:
//   cdt2d_vol <T> <L0> <lambda> <nc> <beta> <eps> <N0> <sweeps> <meas> [seed]
//     eps=0 なら体積固定なし（厳密解との突き合わせ用）

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdint>

static uint64_t S0 = 88172645463325252ull, S1 = 362436069362436069ull;
static inline uint64_t rnd64() {
    uint64_t x = S0, y = S1; S0 = y; x ^= x << 23; S1 = x ^ y ^ (x >> 17) ^ (y >> 26); return S1 + y;
}
static inline double rnd() { return (rnd64() >> 11) * (1.0 / 9007199254740992.0); }
static inline int rndi(int n) { return (int)(rnd() * n); }

struct Geo {
    int N = 0, nc = 0;
    std::vector<int>  opp;      // opp[3t+k] = 相手の半辺
    std::vector<char> space;    // その半辺の辺が空間的か
    std::vector<char> isUp;
    std::vector<uint32_t> spin; // nc 枚のイジングをビットで
    void resize(int n) { N = n; opp.resize(3*n); space.resize(3*n); isUp.resize(n); spin.resize(n); }
};

// 三角形を1枚追加して番号を返す
static inline int addTri(Geo& G) { G.resize(G.N + 1); return G.N - 1; }
// 三角形 t を消す（末尾を移動してくる）。opp の指し先も直す
static void delTri(Geo& G, int t) {
    int last = G.N - 1;
    if (t != last) {
        for (int k = 0; k < 3; ++k) {
            int o = G.opp[3*last + k];
            G.opp[3*t + k] = o;
            if (o >= 0) G.opp[o] = 3*t + k;
            G.space[3*t + k] = G.space[3*last + k];
        }
        G.isUp[t] = G.isUp[last]; G.spin[t] = G.spin[last];
    }
    G.resize(G.N - 1);
}
static inline void pair2(Geo& G, int h1, int h2) { G.opp[h1] = h2; G.opp[h2] = h1; }

// 頂点の次数（半辺 g の根元の頂点まわりを φ = next∘opp で回る）
static inline int vdeg(const Geo& G, int g) {
    int h = g, n = 0;
    do { int o = G.opp[h]; h = 3*(o/3) + (o%3 + 1)%3; n++; if (n > 64) return 99; } while (h != g);
    return n;
}
// 半辺 g の【根元の頂点】の代表元。φ = next∘opp の巡回に入る半辺番号の最小値。
// 頂点にIDを振っていないので、退化（近傍が同じ頂点）を判定するにはこれが要る。
static inline int vertexId(const Geo& G, int g) {
    int h = g, best = g, n = 0;
    do { if (h < best) best = h;
         int o = G.opp[h]; h = 3*(o/3) + (o%3 + 1)%3;
         if (++n > 200) return -1; } while (h != g);
    return best;
}
static int count_vertices(const Geo& G) {
    std::vector<char> seen(3*G.N, 0); int V = 0;
    for (int h0 = 0; h0 < 3*G.N; ++h0) {
        if (seen[h0]) continue;
        V++; int h = h0;
        do { seen[h] = 1; int o = G.opp[h]; h = 3*(o/3) + (o%3 + 1)%3; } while (h != h0);
    }
    return V;
}

// Σ_a s^a_i s^a_j
static inline int bond(const Geo& G, int i, int j) {
    if (!G.nc) return 0;
    return G.nc - 2 * __builtin_popcount(G.spin[i] ^ G.spin[j]);
}

// ---------------- フリップ（時間的 かつ U-D のみ）----------------
static bool flip(Geo& G, double beta) {
    int A = rndi(G.N), k = rndi(3);
    int h = 3*A+k, hb = G.opp[h];
    int B = hb/3, j = hb%3;
    if (B == A) return false;
    if (G.space[h]) return false;
    if (G.isUp[A] == G.isUp[B]) return false;
    int hA1 = 3*A+(k+1)%3, hB1 = 3*B+(j+1)%3;
    int oX = G.opp[hA1], oY = G.opp[3*A+(k+2)%3], oZ = G.opp[hB1], oW = G.opp[3*B+(j+2)%3];
    for (int o : {oX, oY, oZ, oW}) { int tt = o/3; if (tt == A || tt == B) return false; }
    int X = oX/3, Z = oZ/3;
    if (G.nc) {
        double d = (double)(bond(G,A,X) + bond(G,B,Z) - bond(G,A,Z) - bond(G,B,X));
        if (d > 0 && rnd() >= exp(-beta*d)) return false;
    }
    char sA1 = G.space[hA1], sB1 = G.space[hB1];
    // ★ フリップには2つの場合がある。U三角形は時間的な辺を2本持つので、
    //   どちらを共有しているかで結果が変わる：
    //     空間的な辺が slot k+2 にある場合  → A',B' の U/D は【そのまま】
    //     空間的な辺が slot k+1 にある場合  → A',B' の U/D が【入れ替わる】
    //   （後者では A'=(a,d,c) の2頂点が同時刻になり、U だった A が D になる）
    //   ここを更新していなかったので、空間的な辺が U-U をつなぐ配位が生まれ、
    //   その後の挿入・削除が全部おかしくなっていた。
    if (sA1) { char t = G.isUp[A]; G.isUp[A] = G.isUp[B]; G.isUp[B] = t; }
    G.space[h] = sB1; G.space[hA1] = 0; G.space[3*B+j] = sA1; G.space[hB1] = 0;
    pair2(G, h, oZ); pair2(G, hA1, hB1); pair2(G, 3*B+j, oX);
    (void)oY; (void)oW;
    return true;
}

// ---------------- 挿入 ----------------
static bool insertV(Geo& G, double lambda, double beta, double eps, double N0) {
    int h = rndi(3*G.N);
    if (!G.space[h]) return false;
    int A = h/3, p = h%3;
    int hb = G.opp[h]; int B = hb/3, q = hb%3;
    if (B == A) return false;
    if (G.isUp[A] == G.isUp[B]) return false;          // U と D でなければ空間的辺ではない
    int oY = G.opp[3*A+(p+2)%3];                        // A の c→a の相手
    int oX = G.opp[3*A+(p+1)%3];                        // A の b→c の相手
    int oZ = G.opp[3*B+(q+1)%3];                        // B の a→d の相手
    int oW = G.opp[3*B+(q+2)%3];                        // B の d→b の相手
    for (int o : {oX, oY, oZ, oW}) { int tt = o/3; if (tt == A || tt == B) return false; }
    // ★ 詳細釣合い：削除側にある棄却条件は、**挿入側にも同じものを置く**必要がある。
    //   削除は「まわりの4頂点 a,b,c,d が全部別」を要求するので、挿入も
    //   「作られる頂点 m のまわりが a,b,c,d で全部別」でなければ提案しない。
    //   これを忘れると削除だけが余分に棄却され、体積が一方的に増えて発散した。
    {
        int va = vertexId(G, 3*A+p);            // a→b の根元 = a
        int vb = vertexId(G, 3*A+(p+1)%3);      // b→c の根元 = b
        int vc = vertexId(G, 3*A+(p+2)%3);      // c→a の根元 = c
        int vd = vertexId(G, 3*B+(q+2)%3);      // d→b の根元 = d
        if (va<0||vb<0||vc<0||vd<0) return false;
        if (va==vb||va==vc||va==vd||vb==vc||vb==vd||vc==vd) return false;
    }
    int Xt = oX/3, Yt = oY/3, Zt = oZ/3, Wt = oW/3;

    // 新しい2枚のスピンはランダム。その分のエントロピー 2^{2nc} を受理に入れる
    uint32_t mask = (G.nc >= 32) ? 0xffffffffu : ((1u << G.nc) - 1u);
    uint32_t sA2 = (uint32_t)(rnd64() & mask), sB1 = (uint32_t)(rnd64() & mask);
    double dE = 0.0;
    if (G.nc) {
        // 前: A-B, A-X, A-Y, B-Z, B-W
        // 後: A1-B2(=A-B), A2-B1, A1-A2, B1-B2, A1-Y, A2-X, B1-W, B2-Z
        //   A1 は A のスピン、B2 は B のスピン、A2=sA2, B1=sB1
        int A1 = A, B2 = B;
        uint32_t xa = G.spin[A1], xb = G.spin[B2];
        auto bnd = [&](uint32_t u, uint32_t v){ return G.nc - 2*__builtin_popcount(u^v); };
        double before = bnd(xa,xb) + bnd(xa,G.spin[Xt]) + bnd(xa,G.spin[Yt])
                      + bnd(xb,G.spin[Zt]) + bnd(xb,G.spin[Wt]);
        double after  = bnd(xa,xb) + bnd(sA2,sB1) + bnd(xa,sA2) + bnd(sB1,xb)
                      + bnd(xa,G.spin[Yt]) + bnd(sA2,G.spin[Xt])
                      + bnd(sB1,G.spin[Wt]) + bnd(xb,G.spin[Zt]);
        dE = -(after - before);
    }
    int Nn = G.N + 2;
    double lw = -2.0*lambda - beta*dE + 2.0*G.nc*M_LN2 + log(2.0*G.N/(double)Nn);
    if (eps > 0) lw -= eps*((Nn-N0)*(Nn-N0) - (G.N-N0)*(G.N-N0));
    if (lw < 0 && rnd() >= exp(lw)) return false;

    // 手術：A→A1（スロットを 0=a→m,1=m→c,2=c→a に組み直す）, B→B2, 新規に A2, B1
    int A1 = A, B2 = B;
    int A2 = addTri(G), B1 = addTri(G);
    G.isUp[A2] = G.isUp[A1]; G.isUp[B1] = G.isUp[B2];
    G.spin[A2] = sA2; G.spin[B1] = sB1;
    G.space[3*A1+0]=1; G.space[3*A1+1]=0; G.space[3*A1+2]=0;
    G.space[3*A2+0]=1; G.space[3*A2+1]=0; G.space[3*A2+2]=0;
    G.space[3*B1+0]=1; G.space[3*B1+1]=0; G.space[3*B1+2]=0;
    G.space[3*B2+0]=1; G.space[3*B2+1]=0; G.space[3*B2+2]=0;
    pair2(G, 3*A1+0, 3*B2+0);      // a→m ↔ m→a
    pair2(G, 3*A2+0, 3*B1+0);      // m→b ↔ b→m
    pair2(G, 3*A1+1, 3*A2+2);      // m→c ↔ c→m
    pair2(G, 3*B1+1, 3*B2+2);      // m→d ↔ d→m
    pair2(G, 3*A1+2, oY);          // c→a
    pair2(G, 3*A2+1, oX);          // b→c
    pair2(G, 3*B1+2, oW);          // d→b
    pair2(G, 3*B2+1, oZ);          // a→d
    return true;
}

// ---------------- 削除 ----------------
static bool deleteV(Geo& G, double lambda, double beta, double eps, double N0) {
    if (G.N <= 8) return false;
    int g = rndi(3*G.N);
    if (vdeg(G, g) != 4) return false;                 // 次数4 ⟺ 挿入で作られた頂点
    // 頂点 m のまわりの4本の半辺（m から出るもの）
    int hs[4]; hs[0] = g;
    for (int i = 1; i < 4; ++i) { int o = G.opp[hs[i-1]]; hs[i] = 3*(o/3) + (o%3+1)%3; }
    int A1=-1,A2=-1,B1=-1,B2=-1, pA1=0,pA2=0,qB1=0,qB2=0;
    for (int i = 0; i < 4; ++i) {
        int t = hs[i]/3, s = hs[i]%3;
        if (G.isUp[t]) { if (G.space[hs[i]]) { A2=t; pA2=s; } else { A1=t; pA1=s; } }
        else           { if (G.space[hs[i]]) { B2=t; qB2=s; } else { B1=t; qB1=s; } }
    }
    if (A1<0||A2<0||B1<0||B2<0) return false;
    if (A1==A2||B1==B2||A1==B1||A1==B2||A2==B1||A2==B2) return false;
    int oY = G.opp[3*A1+(pA1+1)%3];      // A1 の c→a の相手
    int oX = G.opp[3*A2+(pA2+1)%3];      // A2 の b→c の相手
    int oZ = G.opp[3*B2+(qB2+1)%3];      // B2 の a→d の相手
    int oW = G.opp[3*B1+(qB1+1)%3];      // B1 の d→b の相手
    for (int o : {oX,oY,oZ,oW}) { int t=o/3; if (t==A1||t==A2||t==B1||t==B2) return false; }
    // ★ ここが要。次数4というだけでは足りない。まわりの4頂点 a,b,c,d が全部別でないと
    //   マージで頂点が同一視され、トポロジーが変わる（実際 V が 1 でなく 3 減った）。
    //   スライスが短くなりすぎた場合（l_t が 1 になる等）もここで弾かれる
    // ★ 4枚の【並び方】まで検査する。次数4かつ U2枚 D2枚でも、つながり方が
    //   挿入で作られた形 (A1,A2,B1,B2) でなければマージは正しくない。
    //   m のまわりは  A1.pA1(m→c) ↔ A2.(pA2+2)(c→m),  A2.pA2(m→b) ↔ B1.(qB1+2)(b→m),
    //                 B1.qB1(m→d) ↔ B2.(qB2+2)(d→m),  B2.qB2(m→a) ↔ A1.(pA1+2)(a→m)
    if (G.opp[3*A1+pA1] != 3*A2+(pA2+2)%3) return false;
    if (G.opp[3*A2+pA2] != 3*B1+(qB1+2)%3) return false;
    if (G.opp[3*B1+qB1] != 3*B2+(qB2+2)%3) return false;
    if (G.opp[3*B2+qB2] != 3*A1+(pA1+2)%3) return false;
    // 空間的なのは a→m と b→m のはず（A1 と B1 の (slot+2)）
    if (!G.space[3*A1+(pA1+2)%3] || !G.space[3*B1+(qB1+2)%3]) return false;
    {
        int va = vertexId(G, 3*A1+(pA1+2)%3);   // a→m の根元
        int vb = vertexId(G, 3*A2+(pA2+1)%3);   // b→c の根元
        int vc = vertexId(G, 3*A1+(pA1+1)%3);   // c→a の根元
        int vd = vertexId(G, 3*B1+(qB1+1)%3);   // d→b の根元
        if (va<0||vb<0||vc<0||vd<0) return false;
        if (va==vb||va==vc||va==vd||vb==vc||vb==vd||vc==vd) return false;
    }

    double dE = 0.0;
    if (G.nc) {
        auto bnd=[&](uint32_t u,uint32_t v){ return G.nc - 2*__builtin_popcount(u^v); };
        uint32_t xa=G.spin[A1], xb=G.spin[B2], sa2=G.spin[A2], sb1=G.spin[B1];
        double before = bnd(xa,xb) + bnd(sa2,sb1) + bnd(xa,sa2) + bnd(sb1,xb)
                      + bnd(xa,G.spin[oY/3]) + bnd(sa2,G.spin[oX/3])
                      + bnd(sb1,G.spin[oW/3]) + bnd(xb,G.spin[oZ/3]);
        double after  = bnd(xa,xb) + bnd(xa,G.spin[oX/3]) + bnd(xa,G.spin[oY/3])
                      + bnd(xb,G.spin[oZ/3]) + bnd(xb,G.spin[oW/3]);
        dE = -(after - before);
    }
    int Nn = G.N - 2;
    double lw = 2.0*lambda - beta*dE - 2.0*G.nc*M_LN2 + log((double)G.N/(2.0*Nn));
    if (eps > 0) lw -= eps*((Nn-N0)*(Nn-N0) - (G.N-N0)*(G.N-N0));
    if (lw < 0 && rnd() >= exp(lw)) return false;

    // A1,B2 を残して A=(a,b,c), B=(b,a,d) に組み直す（スロット 0=空間的）
    G.space[3*A1+0]=1; G.space[3*A1+1]=0; G.space[3*A1+2]=0;
    G.space[3*B2+0]=1; G.space[3*B2+1]=0; G.space[3*B2+2]=0;
    pair2(G, 3*A1+0, 3*B2+0);
    pair2(G, 3*A1+1, oX);
    pair2(G, 3*A1+2, oY);
    pair2(G, 3*B2+1, oZ);
    pair2(G, 3*B2+2, oW);
    // A2, B1 を消す（大きいほうから）
    int d1 = std::max(A2,B1), d2 = std::min(A2,B1);
    delTri(G, d1); delTri(G, d2);
    return true;
}

// ---------------- スピン ----------------
static std::vector<int> wstack;
static void wolff(Geo& G, double beta) {
    if (!G.nc) return;
    int a = rndi(G.nc); uint32_t bit = 1u << a;
    double padd = 1.0 - exp(-2.0*beta);
    int v0 = rndi(G.N); uint32_t sv = G.spin[v0] & bit;
    wstack.clear(); wstack.push_back(v0); G.spin[v0] ^= bit;
    while (!wstack.empty()) {
        int v = wstack.back(); wstack.pop_back();
        for (int k = 0; k < 3; ++k) {
            int u = G.opp[3*v+k]/3;
            if ((G.spin[u] & bit) == sv && rnd() < padd) { G.spin[u] ^= bit; wstack.push_back(u); }
        }
    }
}
static void spin_sweep(Geo& G, double beta) {
    if (!G.nc) return;
    for (int a = 0; a < G.nc; ++a) {
        uint32_t bit = 1u << a;
        for (int n = 0; n < G.N; ++n) {
            int v = rndi(G.N);
            int sv = (G.spin[v] & bit) ? 1 : -1, sum = 0;
            for (int k = 0; k < 3; ++k) { int u = G.opp[3*v+k]/3; sum += (G.spin[u]&bit)?1:-1; }
            double d = 2.0*sv*sum;
            if (d <= 0 || rnd() < exp(-beta*d)) G.spin[v] ^= bit;
        }
    }
}
static double meandist(const Geo& G, int ns) {
    std::vector<int> dist(G.N), q; double acc = 0;
    for (int s = 0; s < ns; ++s) {
        std::fill(dist.begin(), dist.end(), -1);
        int v0 = rndi(G.N); q.clear(); q.push_back(v0); dist[v0]=0;
        size_t head=0;
        while (head < q.size()) { int v=q[head++];
            for (int k=0;k<3;++k){ int u=G.opp[3*v+k]/3;
                if(dist[u]<0){dist[u]=dist[v]+1;q.push_back(u);} } }
        double sm=0; for(int v=0;v<G.N;++v) sm+=dist[v];
        acc += sm/G.N;
    }
    return acc/ns;
}

// ---------------- 初期配位（一様な筒）----------------
static bool build(Geo& G, int T, int L, int nc) {
    int N = T*2*L; G.nc = nc; G.resize(N);
    std::vector<int> tri(3*N); int idx=0;
    for (int t=0;t<T;++t) {
        int tn=(t+1)%T;
        std::vector<char> w(2*L);
        for(int i=0;i<L;++i) w[i]='U';
        for(int i=L;i<2*L;++i) w[i]='D';
        for(int i=2*L-1;i>=2;--i){int j=1+rndi(i);std::swap(w[i],w[j]);}
        w[0]='U';
        int lo=0, up=rndi(L);
        for(int k=0;k<2*L;++k,++idx){
            if(w[k]=='U'){ tri[3*idx]=t*L+lo; tri[3*idx+1]=t*L+(lo+1)%L; tri[3*idx+2]=tn*L+up%L;
                           G.isUp[idx]=1; lo=(lo+1)%L; }
            else { tri[3*idx]=tn*L+(up+1)%L; tri[3*idx+1]=tn*L+up%L; tri[3*idx+2]=t*L+lo;
                   G.isUp[idx]=0; up++; }
            G.space[3*idx]=1; G.space[3*idx+1]=0; G.space[3*idx+2]=0;
        }
    }
    std::map<std::pair<int,int>,int> em;
    for(int h=0;h<3*N;++h) G.opp[h]=-1;
    for(int t=0;t<N;++t) for(int k=0;k<3;++k){
        int a=tri[3*t+k], b=tri[3*t+(k+1)%3];
        auto key=std::make_pair(std::min(a,b),std::max(a,b));
        auto it=em.find(key);
        if(it==em.end()) em[key]=3*t+k; else { pair2(G,3*t+k,it->second); em.erase(it); }
    }
    if(!em.empty()) return false;
    uint32_t mask=(nc>=32)?0xffffffffu:((1u<<nc)-1u);
    for(int t=0;t<N;++t) G.spin[t]=(uint32_t)(rnd64()&mask);
    return true;
}

int main(int argc, char** argv) {
    if (argc < 10) {
        fprintf(stderr, "usage: cdt2d_vol <T> <L0> <lambda> <nc> <beta> <eps> <N0> <sweeps> <meas> [seed]\n");
        return 1;
    }
    int T=atoi(argv[1]), L0=atoi(argv[2]);
    double lambda=atof(argv[3]);
    int nc=atoi(argv[4]);
    double beta=atof(argv[5]), eps=atof(argv[6]), N0=atof(argv[7]);
    long sweeps=atol(argv[8]); int meas=atoi(argv[9]);
    if (argc>10){ S0=(uint64_t)atoll(argv[10])|1ull; for(int i=0;i<20;++i) rnd64(); }

    Geo G;
    if(!build(G,T,L0,nc)){ fprintf(stderr,"初期配位を作れなかった\n"); return 1; }
    int V0=count_vertices(G);
    printf("# 体積可変 CDT  T=%d L0=%d N=%d  λ=%.6f (λ-ln2=%+.6f)  イジング %d 枚(c=%.1f) β=%.3f  ε=%g N0=%g\n",
           T,L0,G.N,lambda,lambda-M_LN2,nc,nc*0.5,beta,eps,N0);
    printf("# 初期の曲面チェック V=%d (N/2=%d) %s\n", V0, G.N/2, (V0*2==G.N)?"OK":"★NG");

    long long fa=0,ft=0, ia=0,it_=0, da=0,dt_=0;
    auto one=[&](){
        for(int c=0;c<4;++c) wolff(G,beta);
        spin_sweep(G,beta);
        // ★ ループ境界は先に確定させる。G.N はこのループの中で増減するので
        //   for(i<G.N) と書くと挿入が受理されるたび上限が伸びて終わらなくなる（実際ハングした）
        int nf = G.N;
        for(int i=0;i<nf;++i){ ft++; if(flip(G,beta)) fa++; }
        int nv = G.N;
        for(int i=0;i<nv;++i){
            if(rnd()<0.5){ it_++; if(insertV(G,lambda,beta,eps,N0)) ia++; }
            else         { dt_++; if(deleteV(G,lambda,beta,eps,N0)) da++; }
        }
    };
    for(long s=0;s<sweeps;++s){ one(); if(G.N>4000000){ printf("# 体積が発散した\n"); return 0; } }

    double sN=0,sN2=0,sr=0; long nm=0; int nr=0;
    for(int m=0;m<meas;++m){
        for(int s=0;s<3;++s) one();
        sN+=G.N; sN2+=(double)G.N*G.N; nm++;
        if(m%10==0){ sr+=meandist(G,2); nr++; }
    }
    int V1=count_vertices(G);
    double mN=sN/nm;
    printf("# 終了時の曲面チェック V=%d (N/2=%d) %s   最終 N=%d\n",
           V1,G.N/2,(V1*2==G.N)?"OK":"★NG",G.N);
    printf("# 受理率  flip %.3f  insert %.4f  delete %.4f\n",
           (double)fa/ft, (double)ia/it_, (double)da/dt_);
    printf("%10.6f %12.2f %12.2f %10.3f\n", lambda, mN,
           sqrt(std::max(0.0,sN2/nm-mN*mN)), sr/std::max(1,nr));
    printf("#   ↑ lambda   <N>   sigma_N   <r>\n");
    return 0;
}
