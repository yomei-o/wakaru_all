// cdt3d.cpp ── 3次元 CDT（マイルストーン1：データ構造と初期配位、そして不変量の検算）
//
// なぜ3次元か
// -----------
// 2次元では曲率項 ∫√g R が位相不変量なので、素の作用は体積項だけだった。
// だから「測度が運動項を作る」ところまでしか見られない。
// **3次元では曲率項が力学に効く。** 共形モードは本当に逆符号の運動項を持ち、
// そのうえで測度がそれを直すのかどうかを見られる ── これが2次元では試せなかったこと。
// そして3次元には厳密解が無い。ここからが本当にシミュレータの出番。
//
// 3次元 CDT の中身
// ----------------
// 時刻 t の空間スライスは2次元三角形分割。t と t+1 のあいだ（サンドイッチ）は四面体で埋める。
// 四面体は3種類しかない（下の時刻に何頂点あるかで分類）：
//   (3,1) 下3・上1 / (2,2) 下2・上2 / (1,3) 下1・上3
// 手は (2,6), (2,3), (4,4) とその逆（Pachner 移動を因果的に制限したもの）。
//
// このファイルの範囲（マイルストーン1）
// ------------------------------------
// 初期配位を作り、**閉じた3次元多様体になっているかを検算する**。
//   ・すべての三角形の面がちょうど2つの四面体で共有されている
//   ・オイラー標数 χ = V - E + F - N = 0（閉じた3次元多様体）
//   ・面の総数 F = 2N（各四面体に4面、各面は2つで共有）
//   ・したがって E = V + N
//   ・N_31 = N_13 = N_22 = （空間の三角形数）×T   ← プリズム分解の場合
//
// 初期配位の作り方
// ----------------
// 空間はトーラス T²（Lx×Ly の格子を各セル2枚の三角形に割る）。時間もトーラス（T スライス）。
// 各サンドイッチは「三角柱 = 空間三角形 × 区間」を3つの四面体に割る：
//   頂点を大域的に順序づけて a<b<c とすると
//     (a,b,c,c')  → (3,1)
//     (a,b,b',c') → (2,2)
//     (a,a',b',c')→ (1,3)
//   隣のプリズムと共有する四角形の面は、どちらから見ても対角線 a–b'（小さい下→大きい上）で
//   割れるので**整合する**。ここが大域順序を使う理由。

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <array>
#include <algorithm>
#include <cstdint>

struct Tet {
    int v[4];        // 頂点（昇順に並べておく）
    int nb[4];       // nb[i] = 頂点 v[i] の【向かい】の面を共有する四面体
    int type;        // 下の時刻にある頂点数： 3=(3,1), 2=(2,2), 1=(1,3)
    int tslice;      // どのサンドイッチ（時刻 t と t+1 のあいだ）に属するか
};

struct Cdt3 {
    int T, Lx, Ly;
    int Vs;                        // 1スライスの頂点数
    std::vector<int> vtime;        // 各頂点の時刻
    std::vector<Tet> tet;
};

// 頂点 id：スライス t の格子点 (i,j)
static inline int vid(const Cdt3& C, int t, int i, int j) {
    return ((t % C.T) + C.T) % C.T * C.Vs + ((j % C.Ly) + C.Ly) % C.Ly * C.Lx + ((i % C.Lx) + C.Lx) % C.Lx;
}

static void build(Cdt3& C, int T, int Lx, int Ly) {
    C.T = T; C.Lx = Lx; C.Ly = Ly; C.Vs = Lx * Ly;
    int V = T * C.Vs;
    C.vtime.assign(V, 0);
    for (int t = 0; t < T; ++t) for (int k = 0; k < C.Vs; ++k) C.vtime[t * C.Vs + k] = t;
    C.tet.clear();

    // 空間の三角形（1スライスぶん）: 各セルを2枚に割る
    std::vector<std::array<int,3>> stri;
    for (int j = 0; j < Ly; ++j) for (int i = 0; i < Lx; ++i) {
        stri.push_back({ j * Lx + i, j * Lx + (i+1)%Lx, ((j+1)%Ly) * Lx + (i+1)%Lx });
        stri.push_back({ j * Lx + i, ((j+1)%Ly) * Lx + (i+1)%Lx, ((j+1)%Ly) * Lx + i });
    }

    for (int t = 0; t < T; ++t) {
        int tn = (t + 1) % T;
        for (auto& s : stri) {
            // 大域順序で a<b<c に並べる（隣のプリズムと整合させるため）
            int a = s[0], b = s[1], c = s[2];
            int tmp;
            if (a > b) { tmp=a; a=b; b=tmp; }
            if (b > c) { tmp=b; b=c; c=tmp; }
            if (a > b) { tmp=a; a=b; b=tmp; }
            int A = t*C.Vs+a,  B = t*C.Vs+b,  Cc = t*C.Vs+c;
            int A2= tn*C.Vs+a, B2= tn*C.Vs+b, C2 = tn*C.Vs+c;
            Tet t1, t2, t3;
            t1.v[0]=A;  t1.v[1]=B;  t1.v[2]=Cc; t1.v[3]=C2; t1.type=3; t1.tslice=t;
            t2.v[0]=A;  t2.v[1]=B;  t2.v[2]=B2; t2.v[3]=C2; t2.type=2; t2.tslice=t;
            t3.v[0]=A;  t3.v[1]=A2; t3.v[2]=B2; t3.v[3]=C2; t3.type=1; t3.tslice=t;
            C.tet.push_back(t1); C.tet.push_back(t2); C.tet.push_back(t3);
        }
    }
    // 面（3頂点の組）で四面体を貼り合わせる
    std::map<std::array<int,3>, std::pair<int,int>> fm;   // 面 -> (四面体, 向かいの頂点index)
    for (size_t k = 0; k < C.tet.size(); ++k) {
        std::sort(C.tet[k].v, C.tet[k].v + 4);
        for (int i = 0; i < 4; ++i) C.tet[k].nb[i] = -1;
    }
    for (size_t k = 0; k < C.tet.size(); ++k) {
        for (int i = 0; i < 4; ++i) {
            std::array<int,3> f;
            int p = 0;
            for (int m = 0; m < 4; ++m) if (m != i) f[p++] = C.tet[k].v[m];
            std::sort(f.begin(), f.end());
            auto it = fm.find(f);
            if (it == fm.end()) fm[f] = { (int)k, i };
            else {
                C.tet[k].nb[i] = it->second.first;
                C.tet[it->second.first].nb[it->second.second] = (int)k;
                fm.erase(it);
            }
        }
    }
    if (!fm.empty()) fprintf(stderr, "★ 貼り合わない面が %zu 枚ある\n", fm.size());
}

// 不変量の検算
static void audit(const Cdt3& C) {
    long N = (long)C.tet.size();
    // 面が全部2つで共有されているか
    long open = 0;
    for (auto& tt : C.tet) for (int i = 0; i < 4; ++i) if (tt.nb[i] < 0) open++;
    // 相互に指し合っているか
    long bad = 0;
    for (size_t k = 0; k < C.tet.size(); ++k) for (int i = 0; i < 4; ++i) {
        int u = C.tet[k].nb[i];
        if (u < 0) continue;
        bool back = false;
        for (int m = 0; m < 4; ++m) if (C.tet[u].nb[m] == (int)k) back = true;
        if (!back) bad++;
    }
    // 面・辺・頂点を数える
    std::map<std::array<int,3>,int> faces;
    std::map<std::array<int,2>,int> edges;
    std::vector<char> vused(C.vtime.size(), 0);
    for (auto& tt : C.tet) {
        for (int m = 0; m < 4; ++m) vused[tt.v[m]] = 1;
        for (int i = 0; i < 4; ++i) {
            std::array<int,3> f; int p=0;
            for (int m = 0; m < 4; ++m) if (m != i) f[p++] = tt.v[m];
            std::sort(f.begin(), f.end()); faces[f]++;
        }
        for (int i = 0; i < 4; ++i) for (int j = i+1; j < 4; ++j) {
            std::array<int,2> e = { tt.v[i], tt.v[j] };
            std::sort(e.begin(), e.end()); edges[e]++;
        }
    }
    long V = 0; for (char c : vused) if (c) V++;
    long E = (long)edges.size(), F = (long)faces.size();
    long fnot2 = 0; for (auto& kv : faces) if (kv.second != 2) fnot2++;
    long n31=0,n22=0,n13=0;
    for (auto& tt : C.tet) { if (tt.type==3) n31++; else if (tt.type==2) n22++; else n13++; }

    printf("# 3D CDT 初期配位  T=%d  空間 %dx%d\n", C.T, C.Lx, C.Ly);
    printf("#   四面体 N = %ld   (3,1)=%ld  (2,2)=%ld  (1,3)=%ld\n", N, n31, n22, n13);
    printf("#   頂点 V=%ld  辺 E=%ld  面 F=%ld\n", V, E, F);
    printf("#\n# --- 不変量の検算 ---\n");
    printf("  貼り合わない面           : %ld  %s\n", open, open==0?"OK":"★NG");
    printf("  指し合っていない隣接     : %ld  %s\n", bad, bad==0?"OK":"★NG");
    printf("  ちょうど2枚で共有でない面: %ld  %s\n", fnot2, fnot2==0?"OK":"★NG");
    printf("  F = 2N か                : %ld vs %ld  %s\n", F, 2*N, F==2*N?"OK":"★NG");
    printf("  E = V + N か             : %ld vs %ld  %s\n", E, V+N, E==V+N?"OK":"★NG");
    printf("  χ = V-E+F-N = %ld  %s（閉じた3次元多様体なら 0）\n", V-E+F-N, (V-E+F-N)==0?"OK":"★NG");
    printf("  N_31 = N_13 か           : %ld vs %ld  %s\n", n31, n13, n31==n13?"OK":"★NG");
    // 型ラベルが本当に「下の時刻にある頂点数」と合っているか（周期時間を考慮）
    long tbad = 0;
    for (auto& tt : C.tet) {
        int lo = 0;
        for (int m = 0; m < 4; ++m) if (C.vtime[tt.v[m]] == tt.tslice) lo++;
        if (lo != tt.type) tbad++;
    }
    printf("  型ラベルと時刻の整合     : ずれ %ld  %s\n", tbad, tbad==0?"OK":"★NG");

    // 因果構造：四面体は必ず隣り合う2時刻だけにまたがる（3時刻にまたがらない）
    long span = 0;
    for (auto& tt : C.tet) {
        int lo = 0, hi = 0;
        for (int m = 0; m < 4; ++m) {
            if (C.vtime[tt.v[m]] == tt.tslice)             lo++;
            else if (C.vtime[tt.v[m]] == (tt.tslice+1)%C.T) hi++;
        }
        if (lo + hi != 4) span++;
    }
    printf("  2時刻にだけまたがるか    : 違反 %ld  %s\n", span, span==0?"OK":"★NG");
}

int main(int argc, char** argv) {
    int T  = argc>1 ? atoi(argv[1]) : 8;
    int Lx = argc>2 ? atoi(argv[2]) : 6;
    int Ly = argc>3 ? atoi(argv[3]) : 6;
    Cdt3 C;
    build(C, T, Lx, Ly);
    audit(C);
    return 0;
}
