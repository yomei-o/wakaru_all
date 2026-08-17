// cdt3d_mc.cpp ── 3次元 CDT（マイルストーン2：Pachner 移動 (2,3)/(3,2) と モンテカルロ）
//
// 3次元 CDT の手は (2,6),(2,3),(4,4) とその逆。まず (2,3)/(3,2) を入れる。
// これはサンドイッチの中だけで働き、空間スライスを変えずに (2,2) 四面体の数を変える。
// つまり **(2,2) セクターのエントロピー**だけを取り出せる。臨界結合 k_3^c が測れる。
//
// 今日の教訓を最初から入れる
// --------------------------
//  ・ポインタの張り替えを手で書かない。**面をキーにして局所的に貼り直す**（2次元でここで死んだ）
//  ・四面体が正しい CDT の形かを毎回 valid_tet() で検算する（型を推測しない）
//  ・不変量（χ=0, F=2N, E=V+N, 面はちょうど2枚共有）を走行後に必ず監査する
//  ・詳細釣合いの提案比を式で書き下し、受理率が予測値と合うか確かめる

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <array>
#include <algorithm>
#include <cstdint>

typedef std::array<int,3> Face;

struct Tet { int v[4]; int nb[4]; int type; int tslice; };

struct G3 {
    int T;
    std::vector<int> vtime;
    std::vector<Tet> tet;
    std::vector<std::vector<int>> vtets;   // 頂点 -> それを含む四面体の一覧
};

static long NMAX = 1<<28;
static double EPS = 0.0; static double NTGT = 0.0;      // 体積固定項 eps*(N-N0)^2
static inline double dvol(long a,long b){ if(EPS==0.0) return 0.0;
    double x=(double)a-NTGT, y=(double)b-NTGT; return EPS*(y*y-x*x); }
static uint64_t rs = 88172645463325252ULL;
static inline uint64_t rnd64(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double rnd(){ return (rnd64()>>11)*(1.0/9007199254740992.0); }
static inline int rndi(int n){ return (int)(rnd64()%(uint64_t)n); }

// ---- 四面体が CDT として正しいか（時刻ラベルだけから判定。型を推測しない）----
static bool valid_tet(const G3& G, int a,int b,int c,int d, int& type, int& tslice) {
    int t[4] = { G.vtime[a], G.vtime[b], G.vtime[c], G.vtime[d] };
    int lo = -1;
    // ちょうど2つの隣り合う時刻に載っているか（時間も周期）
    int s[4]; memcpy(s,t,sizeof(s)); std::sort(s,s+4);
    int u[2]; int nu=0;
    for (int i=0;i<4;++i) if (i==0 || s[i]!=s[i-1]) { if (nu==2) return false; u[nu++]=s[i]; }
    if (nu != 2) return false;
    if (u[1] == u[0]+1)                 lo = u[0];
    else if (u[0]==0 && u[1]==G.T-1)    lo = G.T-1;     // 周期の巻き
    else return false;
    int nlo=0; for (int i=0;i<4;++i) if (t[i]==lo) nlo++;
    if (nlo<1 || nlo>3) return false;                    // 4つ同時刻＝潰れている
    type = nlo; tslice = lo;
    return true;
}

static inline Face mkface(int a,int b,int c){ Face f={a,b,c}; std::sort(f.begin(),f.end()); return f; }

// ---- 頂点→四面体 の出し入れ ----
static inline void vt_add(G3& G,int k){ for(int m=0;m<4;++m) G.vtets[G.tet[k].v[m]].push_back(k); }
static inline void vt_del(G3& G,int k){
    for(int m=0;m<4;++m){ auto& L=G.vtets[G.tet[k].v[m]];
        for(size_t i=0;i<L.size();++i) if(L[i]==k){ L[i]=L.back(); L.pop_back(); break; } }
}
static inline void vt_ren(G3& G,int from,int to){
    for(int m=0;m<4;++m){ auto& L=G.vtets[G.tet[to].v[m]];
        for(size_t i=0;i<L.size();++i) if(L[i]==from){ L[i]=to; break; } }
}

// 末尾と入れ替えて削除（隣接ポインタも直す）
// ★ swap-remove は四面体を採番し直す。外に控えてあるインデックス(ext)も一緒に付け替えないと
//   古い番号を指したままになる（2次元でも同じ罠を踏んだ）。ext を渡して必ず同時に直す。
static void del_tet(G3& G,int k,std::vector<std::pair<Face,int>>* ext){
    vt_del(G,k);
    int last=(int)G.tet.size()-1;
    if(k!=last){
        G.tet[k]=G.tet[last];
        for(int i=0;i<4;++i){ int u=G.tet[k].nb[i]; if(u>=0 && u!=last)
            for(int m=0;m<4;++m) if(G.tet[u].nb[m]==last) G.tet[u].nb[m]=k; }
        for(int i=0;i<4;++i) if(G.tet[k].nb[i]==last) G.tet[k].nb[i]=k;   // 自己接着の保険
        vt_ren(G,last,k);
        if(ext) for(auto& e:*ext) if(e.second==last) e.second=k;
    }
    if(ext) for(auto& e:*ext) if(e.second==k && k==last) e.second=-1;
    G.tet.pop_back();
}

static int add_tet(G3& G,int a,int b,int c,int d,int type,int tslice){
    Tet t; t.v[0]=a;t.v[1]=b;t.v[2]=c;t.v[3]=d;
    std::sort(t.v,t.v+4);
    for(int i=0;i<4;++i) t.nb[i]=-1;
    t.type=type; t.tslice=tslice;
    G.tet.push_back(t);
    int k=(int)G.tet.size()-1; vt_add(G,k); return k;
}

// 与えた四面体たちの面を突き合わせて貼り直す（手で添字をいじらない）
static void relink(G3& G, const std::vector<int>& ks, const std::vector<std::pair<Face,int>>& ext) {
    std::map<Face,std::pair<int,int>> m;
    for(int k:ks) for(int i=0;i<4;++i){
        Face f=mkface(G.tet[k].v[(i+1)&3],G.tet[k].v[(i+2)&3],G.tet[k].v[(i+3)&3]);
        auto it=m.find(f);
        if(it==m.end()) m[f]={k,i};
        else { G.tet[k].nb[i]=it->second.first; G.tet[it->second.first].nb[it->second.second]=k; m.erase(it); }
    }
    // 残った面は外側の四面体と貼る
    for(auto& e:ext){
        auto it=m.find(e.first); if(it==m.end()) continue;
        int k=it->second.first, i=it->second.second, u=e.second;
        G.tet[k].nb[i]=u;
        if(u>=0) for(int j=0;j<4;++j){
            Face g=mkface(G.tet[u].v[(j+1)&3],G.tet[u].v[(j+2)&3],G.tet[u].v[(j+3)&3]);
            if(g==e.first){ G.tet[u].nb[j]=k; break; }
        }
        m.erase(it);
    }
}

// 辺 (x,y) を含む四面体を集める（頂点→四面体の一覧から）
static void tets_on_edge(const G3& G,int x,int y,std::vector<int>& out){
    out.clear();
    for(int k:G.vtets[x]){ bool hy=false; for(int m=0;m<4;++m) if(G.tet[k].v[m]==y) hy=true; if(hy) out.push_back(k); }
}
static bool edge_exists(const G3& G,int x,int y){
    for(int k:G.vtets[x]) for(int m=0;m<4;++m) if(G.tet[k].v[m]==y) return true;
    return false;
}
static bool face_exists(const G3& G,int x,int y,int z){
    for(int k:G.vtets[x]){ bool hy=false,hz=false;
        for(int m=0;m<4;++m){ if(G.tet[k].v[m]==y)hy=true; if(G.tet[k].v[m]==z)hz=true; }
        if(hy&&hz) return true; }
    return false;
}

// ================= 手 (2,3) =================
// 面 ABC を共有する2つの四面体 → 辺 DE を共有する3つの四面体。 N が +1。
static bool move23(G3& G,double k3){
    int k=rndi((int)G.tet.size());
    int i=rndi(4);
    int u=G.tet[k].nb[i];
    if(u<0||u==k) return false;
    int D=G.tet[k].v[i];
    int f[3]; { int p=0; for(int m=0;m<4;++m) if(m!=i) f[p++]=G.tet[k].v[m]; }
    int E=-1;
    for(int m=0;m<4;++m){ int w=G.tet[u].v[m];
        if(w!=f[0]&&w!=f[1]&&w!=f[2]) { E=w; break; } }
    if(E<0) return false;
    { int common=0;                                   // k と u が面を1枚だけ共有しているか
      for(int m=0;m<4;++m) for(int n=0;n<4;++n) if(G.tet[k].v[m]==G.tet[u].v[n]) common++;
      if(common!=3) return false; }
    // 因果律：面 ABC は時間的（3頂点が同時刻＝空間三角形なら不可）、頂点 D,E は別時刻
    if(G.vtime[f[0]]==G.vtime[f[1]] && G.vtime[f[1]]==G.vtime[f[2]]) return false;
    if(G.vtime[D]==G.vtime[E]) return false;
    if(edge_exists(G,D,E)) return false;                 // 既にある辺は作れない
    // 新しい3つの四面体が全部まっとうな CDT 四面体か
    int ty[3],ts[3];
    for(int a=0;a<3;++a){ int x=f[a],y=f[(a+1)%3];
        if(!valid_tet(G,x,y,D,E,ty[a],ts[a])) return false; }
    // 受理：ΔS = k3·(+1)、提案比 = N/N'
    int N=(int)G.tet.size(), Np=N+1;
    if(Np>NMAX) return false;
    double lw = -k3 - dvol(N,Np) + log((double)N/(double)Np);
    if(log(rnd()) > lw) return false;
    // 外側の面を記録
    std::vector<std::pair<Face,int>> ext;
    for(int j=0;j<4;++j){ if(j==i) continue;
        ext.push_back({mkface(G.tet[k].v[(j+1)&3],G.tet[k].v[(j+2)&3],G.tet[k].v[(j+3)&3]),G.tet[k].nb[j]}); }
    for(int j=0;j<4;++j){ if(G.tet[u].v[j]==E) continue;
        ext.push_back({mkface(G.tet[u].v[(j+1)&3],G.tet[u].v[(j+2)&3],G.tet[u].v[(j+3)&3]),G.tet[u].nb[j]}); }
    // 外側が k,u 自身を指している場合は無効化（あり得ないが保険）
    for(auto& e:ext) if(e.second==k||e.second==u) e.second=-1;
    int a0=std::max(k,u), a1=std::min(k,u);
    del_tet(G,a0,&ext); del_tet(G,a1,&ext);
    std::vector<int> ks;
    for(int a=0;a<3;++a){ int x=f[a],y=f[(a+1)%3]; ks.push_back(add_tet(G,x,y,D,E,ty[a],ts[a])); }
    relink(G,ks,ext);
    return true;
}

// ================= 手 (3,2) =================
// 辺 DE を共有する3つの四面体 → 面 ABC を共有する2つ。 N が −1。
static bool move32(G3& G,double k3){
    int k=rndi((int)G.tet.size());
    int e0=rndi(6);
    static const int E0[6]={0,0,0,1,1,2}, E1[6]={1,2,3,2,3,3};
    int D=G.tet[k].v[E0[e0]], E=G.tet[k].v[E1[e0]];
    if(G.vtime[D]==G.vtime[E]) return false;              // 時間的な辺だけ
    std::vector<int> ts; tets_on_edge(G,D,E,ts);
    if(ts.size()!=3) return false;
    // 3つの四面体の頂点の和は {D,E} + 3頂点
    std::vector<int> f;
    for(int q:ts) for(int m=0;m<4;++m){ int w=G.tet[q].v[m];
        if(w==D||w==E) continue;
        if(std::find(f.begin(),f.end(),w)==f.end()) f.push_back(w); }
    if(f.size()!=3) return false;
    if(face_exists(G,f[0],f[1],f[2])) return false;       // 既にある面は作れない
    int ty[2],tl[2];
    if(!valid_tet(G,f[0],f[1],f[2],D,ty[0],tl[0])) return false;
    if(!valid_tet(G,f[0],f[1],f[2],E,ty[1],tl[1])) return false;
    int N=(int)G.tet.size(), Np=N-1;
    if(Np<4) return false;
    double lw = +k3 - dvol(N,Np) + log((double)N/(double)Np);
    if(log(rnd()) > lw) return false;
    std::vector<std::pair<Face,int>> ext;
    for(int q:ts) for(int j=0;j<4;++j){
        Face g=mkface(G.tet[q].v[(j+1)&3],G.tet[q].v[(j+2)&3],G.tet[q].v[(j+3)&3]);
        bool hasD=false,hasE=false;
        for(int m=0;m<3;++m){ if(g[m]==D)hasD=true; if(g[m]==E)hasE=true; }
        if(hasD&&hasE) continue;                          // 内側の面
        ext.push_back({g,G.tet[q].nb[j]});
    }
    for(auto& p:ext) for(int q:ts) if(p.second==q) p.second=-1;
    std::sort(ts.begin(),ts.end(),std::greater<int>());
    for(int q:ts) del_tet(G,q,&ext);
    std::vector<int> ks;
    ks.push_back(add_tet(G,f[0],f[1],f[2],D,ty[0],tl[0]));
    ks.push_back(add_tet(G,f[0],f[1],f[2],E,ty[1],tl[1]));
    relink(G,ks,ext);
    return true;
}

// ================= 手 (2,6) / (6,2) =================
// 空間三角形 ABC（3頂点が同時刻 t）は、上の (3,1) と下の (1,3) にちょうど挟まれている。
// そこへ時刻 t の新しい頂点 X を差し込むと、2つが6つになる。N が +4、頂点が +1。
//
// ★ここが本体。(2,3) だけでは頂点数が凍っていて、真のエントロピーが出ない。
static std::vector<int> vfree;                    // 消した頂点の使い回し

static int new_vertex(G3& G,int t){
    if(!vfree.empty()){ int x=vfree.back(); vfree.pop_back(); G.vtime[x]=t; G.vtets[x].clear(); return x; }
    G.vtime.push_back(t); G.vtets.push_back({}); return (int)G.vtime.size()-1;
}

static bool move26(G3& G,double k3,double k0){
    int k=rndi((int)G.tet.size());
    int i=rndi(4);
    int u=G.tet[k].nb[i];
    if(u<0||u==k) return false;
    int f[3]; { int p=0; for(int m=0;m<4;++m) if(m!=i) f[p++]=G.tet[k].v[m]; }
    int t=G.vtime[f[0]];
    if(G.vtime[f[1]]!=t || G.vtime[f[2]]!=t) return false;      // 空間三角形だけ
    int D=G.tet[k].v[i], E=-1;
    for(int m=0;m<4;++m){ int w=G.tet[u].v[m]; if(w!=f[0]&&w!=f[1]&&w!=f[2]){ E=w; break; } }
    if(E<0) return false;
    if(G.vtime[D]==G.vtime[E]) return false;                    // 上下から挟まれていること
    // ★ 消す前に、できる6つの四面体の型を全部確定させる（消してから失敗すると復元できない）
    int tyD,tlD,tyE,tlE;
    if(G.vtime[D]==(t+1)%G.T)          { tyD=3; tlD=t; }
    else if(G.vtime[D]==(t+G.T-1)%G.T) { tyD=1; tlD=(t+G.T-1)%G.T; }
    else return false;
    if(G.vtime[E]==(t+1)%G.T)          { tyE=3; tlE=t; }
    else if(G.vtime[E]==(t+G.T-1)%G.T) { tyE=1; tlE=(t+G.T-1)%G.T; }
    else return false;
    int N=(int)G.tet.size(), Np=N+4;
    if(Np>NMAX) return false;
    // ΔS = 4·k3 − k0（頂点が1つ増える）、提案比 = 3N/N'
    double lw = -(4.0*k3 - k0) - dvol(N,Np) + log(3.0*(double)N/(double)Np);
    if(log(rnd()) > lw) return false;
    std::vector<std::pair<Face,int>> ext;
    for(int j=0;j<4;++j){ if(j==i) continue;
        ext.push_back({mkface(G.tet[k].v[(j+1)&3],G.tet[k].v[(j+2)&3],G.tet[k].v[(j+3)&3]),G.tet[k].nb[j]}); }
    for(int j=0;j<4;++j){ if(G.tet[u].v[j]==E) continue;
        ext.push_back({mkface(G.tet[u].v[(j+1)&3],G.tet[u].v[(j+2)&3],G.tet[u].v[(j+3)&3]),G.tet[u].nb[j]}); }
    for(auto& e:ext) if(e.second==k||e.second==u) e.second=-1;
    int a0=std::max(k,u),a1=std::min(k,u);
    del_tet(G,a0,&ext); del_tet(G,a1,&ext);
    int X=new_vertex(G,t);
    std::vector<int> ks;
    for(int a=0;a<3;++a){ int p=f[a],q=f[(a+1)%3];
        ks.push_back(add_tet(G,p,q,X,D,tyD,tlD));
        ks.push_back(add_tet(G,p,q,X,E,tyE,tlE));
    }
    relink(G,ks,ext);
    return true;
}

static bool move62(G3& G,double k3,double k0){
    int k=rndi((int)G.tet.size());
    int X=G.tet[k].v[rndi(4)];
    auto& L=G.vtets[X];
    if(L.size()!=6) return false;
    int t=G.vtime[X];
    // まわりの頂点は ちょうど {A,B,C}(時刻t) + U(t+1) + W(t-1) の5つ
    std::vector<int> sp, up, dn;
    for(int q:L) for(int m=0;m<4;++m){ int w=G.tet[q].v[m]; if(w==X) continue;
        std::vector<int>* tgt;
        if(G.vtime[w]==t) tgt=&sp;
        else if(G.vtime[w]==(t+1)%G.T) tgt=&up;
        else if(G.vtime[w]==(t+G.T-1)%G.T) tgt=&dn;
        else return false;
        if(std::find(tgt->begin(),tgt->end(),w)==tgt->end()) tgt->push_back(w); }
    if(sp.size()!=3||up.size()!=1||dn.size()!=1) return false;
    int A=sp[0],B=sp[1],C=sp[2],U=up[0],W=dn[0];
    if(face_exists(G,A,B,C)) return false;
    int ty0,tl0,ty1,tl1;
    if(!valid_tet(G,A,B,C,U,ty0,tl0)) return false;
    if(!valid_tet(G,A,B,C,W,ty1,tl1)) return false;
    int N=(int)G.tet.size(), Np=N-4;
    if(Np<8) return false;
    // 逆手の受理（提案比は (2,6) の逆数）
    double lw = +(4.0*k3 - k0) - dvol(N,Np) + log((double)N/(3.0*(double)Np));
    if(log(rnd()) > lw) return false;
    std::vector<int> ts=L;
    std::vector<std::pair<Face,int>> ext;
    for(int q:ts) for(int j=0;j<4;++j){
        if(G.tet[q].v[j]!=X) continue;                  // X の【向かい】の面だけが外側
        ext.push_back({mkface(G.tet[q].v[(j+1)&3],G.tet[q].v[(j+2)&3],G.tet[q].v[(j+3)&3]),G.tet[q].nb[j]}); }
    for(auto& p:ext) for(int q:ts) if(p.second==q) p.second=-1;
    std::sort(ts.begin(),ts.end(),std::greater<int>());
    for(int q:ts) del_tet(G,q,&ext);
    vfree.push_back(X); G.vtets[X].clear();
    std::vector<int> ks;
    ks.push_back(add_tet(G,A,B,C,U,ty0,tl0));
    ks.push_back(add_tet(G,A,B,C,W,ty1,tl1));
    relink(G,ks,ext);
    return true;
}

// ================= 手 (4,4) =================
// 空間的な辺 AB（同時刻 t）が ちょうど4つの四面体に囲まれているとき、
// その4つは 頂点 A,B,C,D(時刻t) + U(t+1) + W(t-1) の**八面体**をなす。
// 八面体の三角形分割は対角線の選び方で3通り。AB → CD に張り替えるのが (4,4)。
// （UW を対角線にするのは t+1 と t-1 をつなぐので因果律で禁止 ── ここにも因果律が一行で出る）
// N も頂点数も変わらないので ΔS=0、提案確率も前後で同じ（どちらの辺も四面体4つ）→ 常に受理。
//
// ★これが無いと空間スライスは「頂点を挿して作れる形」だけに縛られ、本物の3次元 CDT にならない。
static bool move44(G3& G){
    int k=rndi((int)G.tet.size());
    int e0=rndi(6);
    static const int E0[6]={0,0,0,1,1,2}, E1[6]={1,2,3,2,3,3};
    int A=G.tet[k].v[E0[e0]], B=G.tet[k].v[E1[e0]];
    int t=G.vtime[A];
    if(G.vtime[B]!=t) return false;                       // 空間的な辺だけ
    std::vector<int> ts; tets_on_edge(G,A,B,ts);
    if(ts.size()!=4) return false;
    std::vector<int> sp,up,dn;
    for(int q:ts) for(int m=0;m<4;++m){ int w=G.tet[q].v[m];
        if(w==A||w==B) continue;
        std::vector<int>* tg;
        if(G.vtime[w]==t) tg=&sp;
        else if(G.vtime[w]==(t+1)%G.T) tg=&up;
        else if(G.vtime[w]==(t+G.T-1)%G.T) tg=&dn;
        else return false;
        if(std::find(tg->begin(),tg->end(),w)==tg->end()) tg->push_back(w); }
    if(sp.size()!=2||up.size()!=1||dn.size()!=1) return false;
    int C=sp[0],D=sp[1],U=up[0],W=dn[0];
    if(edge_exists(G,C,D)) return false;
    int ty[4],tl[4];
    if(!valid_tet(G,C,D,A,U,ty[0],tl[0])) return false;
    if(!valid_tet(G,C,D,B,U,ty[1],tl[1])) return false;
    if(!valid_tet(G,C,D,A,W,ty[2],tl[2])) return false;
    if(!valid_tet(G,C,D,B,W,ty[3],tl[3])) return false;
    // 外側の面＝辺 AB を含まない面
    std::vector<std::pair<Face,int>> ext;
    for(int q:ts) for(int j=0;j<4;++j){
        Face g=mkface(G.tet[q].v[(j+1)&3],G.tet[q].v[(j+2)&3],G.tet[q].v[(j+3)&3]);
        bool hA=false,hB=false;
        for(int m=0;m<3;++m){ if(g[m]==A)hA=true; if(g[m]==B)hB=true; }
        if(hA&&hB) continue;
        ext.push_back({g,G.tet[q].nb[j]});
    }
    for(auto& p:ext) for(int q:ts) if(p.second==q) p.second=-1;
    std::sort(ts.begin(),ts.end(),std::greater<int>());
    for(int q:ts) del_tet(G,q,&ext);
    std::vector<int> ks;
    ks.push_back(add_tet(G,C,D,A,U,ty[0],tl[0]));
    ks.push_back(add_tet(G,C,D,B,U,ty[1],tl[1]));
    ks.push_back(add_tet(G,C,D,A,W,ty[2],tl[2]));
    ks.push_back(add_tet(G,C,D,B,W,ty[3],tl[3]));
    relink(G,ks,ext);
    return true;
}

// ================= 初期配位 =================
static void build(G3& G,int T,int Lx,int Ly){
    G.T=T; int Vs=Lx*Ly; int V=T*Vs;
    G.vtime.assign(V,0);
    for(int t=0;t<T;++t) for(int k=0;k<Vs;++k) G.vtime[t*Vs+k]=t;
    G.vtets.assign(V,{});
    G.tet.clear();
    std::vector<std::array<int,3>> stri;
    for(int j=0;j<Ly;++j) for(int i=0;i<Lx;++i){
        stri.push_back({ j*Lx+i, j*Lx+(i+1)%Lx, ((j+1)%Ly)*Lx+(i+1)%Lx });
        stri.push_back({ j*Lx+i, ((j+1)%Ly)*Lx+(i+1)%Lx, ((j+1)%Ly)*Lx+i });
    }
    for(int t=0;t<T;++t){ int tn=(t+1)%T;
        for(auto& s:stri){
            int a=s[0],b=s[1],c=s[2],tmp;
            if(a>b){tmp=a;a=b;b=tmp;} if(b>c){tmp=b;b=c;c=tmp;} if(a>b){tmp=a;a=b;b=tmp;}
            int A=t*Vs+a,B=t*Vs+b,C=t*Vs+c, A2=tn*Vs+a,B2=tn*Vs+b,C2=tn*Vs+c;
            add_tet(G,A,B,C,C2,3,t);
            add_tet(G,A,B,B2,C2,2,t);
            add_tet(G,A,A2,B2,C2,1,t);
        }
    }
    std::map<Face,std::pair<int,int>> fm;
    for(size_t k=0;k<G.tet.size();++k) for(int i=0;i<4;++i){
        Face f=mkface(G.tet[k].v[(i+1)&3],G.tet[k].v[(i+2)&3],G.tet[k].v[(i+3)&3]);
        auto it=fm.find(f);
        if(it==fm.end()) fm[f]={(int)k,i};
        else { G.tet[k].nb[i]=it->second.first; G.tet[it->second.first].nb[it->second.second]=(int)k; fm.erase(it); }
    }
    if(!fm.empty()) fprintf(stderr,"★初期配位で貼り合わない面 %zu\n",fm.size());
}

// ================= 監査 =================
static bool audit(const G3& G,const char* tag){
    long N=(long)G.tet.size(); long bad=0;
    std::map<Face,int> faces; std::map<std::array<int,2>,int> edges;
    std::vector<char> vu(G.vtime.size(),0);
    long tybad=0;
    for(auto& tt:G.tet){
        int ty,tl;
        if(!valid_tet(G,tt.v[0],tt.v[1],tt.v[2],tt.v[3],ty,tl) || ty!=tt.type || tl!=tt.tslice) tybad++;
        for(int m=0;m<4;++m) vu[tt.v[m]]=1;
        for(int i=0;i<4;++i){ faces[mkface(tt.v[(i+1)&3],tt.v[(i+2)&3],tt.v[(i+3)&3])]++;
            if(tt.nb[i]<0) bad++; }
        for(int i=0;i<4;++i) for(int j=i+1;j<4;++j){ std::array<int,2> e={tt.v[i],tt.v[j]};
            std::sort(e.begin(),e.end()); edges[e]++; }
    }
    long V=0; for(char c:vu) if(c) V++;
    long E=(long)edges.size(),F=(long)faces.size(),f2=0;
    for(auto& kv:faces) if(kv.second!=2) f2++;
    long mutu=0;
    for(size_t k=0;k<G.tet.size();++k) for(int i=0;i<4;++i){ int u=G.tet[k].nb[i];
        if(u<0) continue; bool ok=false; for(int m=0;m<4;++m) if(G.tet[u].nb[m]==(int)k) ok=true; if(!ok) mutu++; }
    bool good = (bad==0&&f2==0&&mutu==0&&tybad==0&&F==2*N&&E==V+N&&(V-E+F-N)==0);
    printf("# 監査[%s] N=%ld V=%ld E=%ld F=%ld | 開面%ld 非2枚%ld 非相互%ld 型ずれ%ld | F=2N:%s E=V+N:%s χ=%ld %s\n",
        tag,N,V,E,F,bad,f2,mutu,tybad,F==2*N?"OK":"NG",E==V+N?"OK":"NG",V-E+F-N,good?"→ 全部OK":"→ ★NG");
    return good;
}

int main(int argc,char** argv){
    int T   = argc>1?atoi(argv[1]):8;
    int L   = argc>2?atoi(argv[2]):6;
    double k3=argc>3?atof(argv[3]):1.0;
    double k0=argc>4?atof(argv[4]):0.0;
    long SW = argc>5?atol(argv[5]):20000;
    if(argc>7) NMAX=atol(argv[7]);
    if(argc>8){ NTGT=atof(argv[8]); EPS=(argc>9)?atof(argv[9]):2e-5; }
    if(argc>6) rs = (uint64_t)atol(argv[6])*2862933555777941757ULL+3037000493ULL;

    G3 G; build(G,T,L,L);
    printf("# 3D CDT  T=%d 空間%dx%d  k3=%.4f k0=%.4f  掃引=%ld\n",T,L,L,k3,k0,SW);
    audit(G,"初期");

    long a23=0,t23=0,a32=0,t32=0,a26=0,t26=0,a62=0,t62=0,a44=0,t44=0;
    long meas=0; double sN=0,sN22=0,sN31=0,sV=0,sQ=0,sQ2=0;
    // 体積プロファイル n_t = N_31(t)（＝スライス t の空間三角形の枚数）の相関
    // ★ここが3次元へ来た本来の目的。ゆらぎの共分散を逆に回すと有効作用の二次形式が出る。
    //   運動項の符号は「隣どうしの非対角成分の符号」に出る（正しい符号なら負）。
    std::vector<double> pn(T,0.0), pnn((size_t)T*T,0.0);
    for(long sw=0;sw<SW;++sw){
        long nmov=(long)G.tet.size();
        for(long q=0;q<nmov;++q){
            double r=rnd();
            if(r<0.20)      { t23++; if(move23(G,k3))    a23++; }
            else if(r<0.40) { t32++; if(move32(G,k3))    a32++; }
            else if(r<0.60) { t26++; if(move26(G,k3,k0)) a26++; }
            else if(r<0.80) { t62++; if(move62(G,k3,k0)) a62++; }
            else            { t44++; if(move44(G))       a44++; }
        }
        if(sw>=SW/2 && (sw%1)==0){
            long n22=0,n31=0;
            for(auto& tt:G.tet){ if(tt.type==2) n22++; else if(tt.type==3) n31++; }
            long nv=0; for(size_t z=0;z<G.vtime.size();++z) if(!G.vtets[z].empty()) nv++;
            double q=(double)n22/(double)G.tet.size();
            sN+=(double)G.tet.size(); sN22+=n22; sN31+=n31; sV+=nv; sQ+=q; sQ2+=q*q; meas++;
            std::vector<double> nt(T,0.0);
            for(auto& tt:G.tet) if(tt.type==3) nt[tt.tslice]+=1.0;
            for(int x=0;x<T;++x){ pn[x]+=nt[x];
                for(int y=0;y<T;++y) pnn[(size_t)x*T+y]+=nt[x]*nt[y]; }
        }
    }
    printf("#   受理率 (2,3)=%.4f (3,2)=%.4f (2,6)=%.4f (6,2)=%.4f (4,4)=%.4f\n",
        (double)a23/(t23?t23:1),(double)a32/(t32?t32:1),
        (double)a26/(t26?t26:1),(double)a62/(t62?t62:1),(double)a44/(t44?t44:1));
    printf("#   <N>=%.1f <N22>=%.1f <N31>=%.1f <V>=%.1f | N22/N=%.4f  V/N=%.4f\n",
        sN/meas,sN22/meas,sN31/meas,sV/meas,sN22/sN,sV/sN);
    { double mq=sQ/meas, vq=sQ2/meas-mq*mq;
      printf("#   秩序変数 q=N22/N : <q>=%.5f  分散*N=%.4f\n", mq, vq*(sN/meas)); }
    // 体積プロファイルの共分散。時間並進で不変なので距離 d = |t-t'| ごとにまとめる
    {
        printf("PROFILE %d\n",T);
        for(int x=0;x<T;++x) printf("MEAN %d %.8f\n",x,pn[x]/meas);
        std::vector<double> cd(T,0.0);
        for(int x=0;x<T;++x) for(int y=0;y<T;++y){
            double c = pnn[(size_t)x*T+y]/meas - (pn[x]/meas)*(pn[y]/meas);
            int d=(y-x+T)%T; if(d>T/2) d=T-d;
            cd[d]+=c;
        }
        for(int d=0;d<=T/2;++d){
            int cnt=0;
            for(int x=0;x<T;++x) for(int y=0;y<T;++y){ int e=(y-x+T)%T; if(e>T/2) e=T-e; if(e==d) cnt++; }
            printf("COV %d %.8f\n",d,cd[d]/cnt);
        }
    }
    bool ok=audit(G,"最終");
    return ok?0:1;
}
