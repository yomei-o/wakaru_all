// 考える波 第 29 回 検証スクリプト
//   なぜ波の方程式は二階なのか
//   ── そして第 15 回の「狭い長方形」を測り直す
//
//   実行: node nikai.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

const C     = 2.99792458e8;
const HBAR  = 1.054571817e-34;
const QE    = 1.602176634e-19;
const ME    = 9.1093837015e-31;
const EPS0  = 8.8541878128e-12;

// ------------------------------------------------------------------
hr('1. 問い ── なぜ「二階」なのか');

console.log('  第 28 回で鎖の底に残ったのは、これでした：');
console.log('');
console.log('      ★ 波の方程式は、なぜ二階なのか。');
console.log('');
console.log('  第 15 回では「物理は α ∈ [−1/2, 2] の狭い長方形に住む」と書き、');
console.log('  下限は因果律・上限はオストログラツキーだと言いました。');
console.log('  ★ 本回はこれを測り直します。結論を先に言うと ──');
console.log('');
console.log('      ★★ 第 15 回の長方形は、両端を ★ 別々の単位で測っていました。');
console.log('      ★★ 単位を揃えると帯は [−1, +1]、幅ちょうど 2。');
console.log('      ★★ そして上端と下端は ★ 別々の定理で決まっています（交互に効く）。');

// ------------------------------------------------------------------
hr('2. 一階だと何が起きるか ── 拡散は波にならない');

console.log('  時間について一階の代表は拡散方程式：∂u/∂t = D ∂²u/∂x²');
console.log('  e^{i(kx−ωt)} を入れると：');
console.log('');
console.log('      −iω = −Dk²   →   ★ ω = −i D k²（純虚数）');
console.log('');
console.log('  ★ ω に実部がありません ── 振動しない。★ 減衰だけ。');
console.log('');
{
  const D = 1e-4;
  console.log('  ' + pad('k [1/m]',12) + pad('Re ω',14) + pad('Im ω',14) + '中身');
  console.log('  ' + '-'.repeat(52));
  [1,10,100,1000].forEach(function(k){
    console.log('  ' + pad(e(k,0),12) + pad('0',14) + pad(e(-D*k*k,3),14) + '減衰のみ');
  });
  console.log('');
  console.log('  ★ 二階（波動方程式 ∂²u/∂t² = c²∂²u/∂x²）だと ω² = c²k² で ω = ±ck ── 実数。');
  console.log('');
  console.log('  もう一つの症状 ── ★ 伝播速度が無限大。');
  console.log('  拡散の解 u = exp(−x²/4Dt)/√(4πDt) は、どんな t>0 でも全 x で 0 ではない：');
  console.log('');
  console.log('  ' + pad('t [s]',12) + pad('x [m]',10) + pad('x²/4Dt',16) + '振幅の桁');
  console.log('  ' + '-'.repeat(56));
  [[1e-9,1],[1e-6,1],[1e-3,1],[1,1]].forEach(function(p){
    const t=p[0], x=p[1], a=x*x/(4*D*t);
    console.log('  ' + pad(e(t,0),12) + pad(f(x,1),10) + pad(e(a,3),16)
      + '10^(−' + e(a/Math.LN10,2) + ')');
  });
  console.log('');
  console.log('  ★ 数学的には「無限の速さ」。★ でも 1 ns 後の 1 m 先は 10^(−1.1e12) ──');
  console.log('    ★★ 観測できない量です（第 11 回で熱伝導について書いたのと同じ話）。');
  console.log('');
  console.log('  ★ ただし公平のため：★ 時間も空間も一階なら、波は出ます。');
  console.log('      ∂u/∂t + c ∂u/∂x = 0   →   ω = ck（実数）── ちゃんと進む。');
  console.log('    ★ ただし ★ 片方向だけ。これが次節の主題です。');
}

// ------------------------------------------------------------------
hr('3. ★ 二階の正体 ── 「両方向」という意味だった');

console.log('  波動作用素は、一階の作用素二つに分解できます：');
console.log('');
console.log('      ∂²/∂t² − c²∂²/∂x² = (∂/∂t − c∂/∂x)(∂/∂t + c∂/∂x)');
console.log('');
console.log('  ★ 右向きの移流 × 左向きの移流。★ 二階とは「両方向」のことでした。');
console.log('');
{
  const c=1, h=1e-3;
  function g(x,t){ return Math.exp(-(x-0.3*t)*(x-0.3*t)) * Math.cos(2*x+t); }
  function dt(x,t){ return (g(x,t+h)-g(x,t-h))/(2*h); }
  function dx(x,t){ return (g(x+h,t)-g(x-h,t))/(2*h); }
  function box(x,t){
    const dtt=(g(x,t+h)-2*g(x,t)+g(x,t-h))/(h*h);
    const dxx=(g(x+h,t)-2*g(x,t)+g(x-h,t))/(h*h);
    return dtt - c*c*dxx;
  }
  function fact(x,t){
    const A=function(X,T){ return dt(X,T) + c*dx(X,T); };
    const dA_t=(A(x,t+h)-A(x,t-h))/(2*h);
    const dA_x=(A(x+h,t)-A(x-h,t))/(2*h);
    return dA_t - c*dA_x;
  }
  console.log('  ' + pad('(x, t)',16) + pad('□g 直接',18) + pad('因数分解から',18) + '相対差');
  console.log('  ' + '-'.repeat(62));
  [[0.2,0.5],[1.0,0.3],[-0.7,1.2]].forEach(function(p){
    const a=box(p[0],p[1]), b=fact(p[0],p[1]);
    console.log('  ' + pad('('+f(p[0],1)+', '+f(p[1],1)+')',16) + pad(f(a,8),18) + pad(f(b,8),18)
      + e(Math.abs(a-b)/Math.abs(a),2));
  });
  console.log('');
  console.log('  ★ 差分の打ち切り誤差の範囲で一致 ── 因数分解は正しい。');
  console.log('');

  console.log('  ★ 帰結：初期の山ひとつは、必ず ★ 左右 半分ずつに割れます（ダランベール）。');
  const N=4001, L=20, dx2=L/(N-1), dt2=0.4*dx2/c;
  let u0=new Float64Array(N), u1=new Float64Array(N), u2=new Float64Array(N);
  const X=i=>-L/2+i*dx2;
  for(let i=0;i<N;i++) u0[i]=Math.exp(-X(i)*X(i)/0.02);
  for(let i=1;i<N-1;i++){
    u1[i]=u0[i]+0.5*(c*dt2/dx2)*(c*dt2/dx2)*(u0[i+1]-2*u0[i]+u0[i-1]);
  }
  const steps=Math.round(5/dt2), r2=(c*dt2/dx2)*(c*dt2/dx2);
  for(let n=0;n<steps;n++){
    for(let i=1;i<N-1;i++) u2[i]=2*u1[i]-u0[i]+r2*(u1[i+1]-2*u1[i]+u1[i-1]);
    const t=u0; u0=u1; u1=u2; u2=t;
  }
  let mxR=0,mxL=0,iR=0,iL=0;
  for(let i=0;i<N;i++){ if(X(i)>0&&u1[i]>mxR){mxR=u1[i];iR=i;} if(X(i)<0&&u1[i]>mxL){mxL=u1[i];iL=i;} }
  console.log('');
  console.log('      5 秒後（c=1）：右の山 高さ ' + f(mxR,5) + ' 位置 ' + f(X(iR),3));
  console.log('                    左の山 高さ ' + f(mxL,5) + ' 位置 ' + f(X(iL),3));
  console.log('      ★ 高さは 0.5（半分ずつ）、位置は ±ct = ±5.0 の予言どおり。');
  console.log('');
  console.log('  ★★ 一階（移流）なら山は割れず、高さ 1 のまま片方向へ進みます。');
  console.log('    ── ★ 二階が要るのは「両方向へ行けること」のためでした。');
}

// ------------------------------------------------------------------
hr('4. 一階のまま波にする唯一の道 ── 平方根をとると、スピンが生える');

console.log('  では「一階で、しかも両方向」は無理なのか。★ 一つだけ道があります。');
console.log('  ★ 波動作用素の ★ 平方根 をとる ── ディラックのやり方です：');
console.log('');
console.log('      (iγ^μ ∂_μ)² = □     ⟺     {γ^μ, γ^ν} = 2η^{μν} I');
console.log('');
console.log('  ★ この条件を満たす「数」は存在しません（数なら 2ab=0 と a²=1 が両立しない）。');
console.log('  ★ 行列が要ります。何次の行列が要るか ── そこが本節です。');
console.log('');

function zeros(n){ const a=[]; for(let i=0;i<n;i++){ a.push([]); for(let j=0;j<n;j++) a[i].push([0,0]); } return a; }
function mul(A,B){ const n=A.length, R=zeros(n);
  for(let i=0;i<n;i++) for(let j=0;j<n;j++){ let re=0,im=0;
    for(let k=0;k<n;k++){ const a=A[i][k], b=B[k][j]; re+=a[0]*b[0]-a[1]*b[1]; im+=a[0]*b[1]+a[1]*b[0]; }
    R[i][j]=[re,im]; } return R; }
function add(A,B){ const n=A.length,R=zeros(n);
  for(let i=0;i<n;i++) for(let j=0;j<n;j++) R[i][j]=[A[i][j][0]+B[i][j][0], A[i][j][1]+B[i][j][1]];
  return R; }
function sub(A,B){ const n=A.length,R=zeros(n);
  for(let i=0;i<n;i++) for(let j=0;j<n;j++) R[i][j]=[A[i][j][0]-B[i][j][0], A[i][j][1]-B[i][j][1]];
  return R; }
function anti(A,B){ return add(mul(A,B), mul(B,A)); }
function maxabs(A){ let m=0; for(const r of A) for(const z of r) m=Math.max(m, Math.hypot(z[0],z[1])); return m; }
function scaleI(n,s){ const R=zeros(n); for(let i=0;i<n;i++) R[i][i]=[s,0]; return R; }
function scal(A,s){ const n=A.length,R=zeros(n);
  for(let i=0;i<n;i++) for(let j=0;j<n;j++) R[i][j]=[A[i][j][0]*s, A[i][j][1]*s]; return R; }

const S1=[[[0,0],[1,0]],[[1,0],[0,0]]];
const S2=[[[0,0],[0,-1]],[[0,1],[0,0]]];
const S3=[[[1,0],[0,0]],[[0,0],[-1,0]]];

{
  console.log('  ★ まず 2×2。パウリ行列 σ1,σ2,σ3 は互いに反交換します：');
  console.log('      |{σ1,σ2}| = ' + e(maxabs(anti(S1,S2)),1)
            + '、|{σ1,σ3}| = ' + e(maxabs(anti(S1,S3)),1)
            + '、|{σ2,σ3}| = ' + e(maxabs(anti(S2,S3)),1));
  console.log('');
  console.log('  ★ では 4 本目 M = a·I + b·σ1 + c·σ2 + d·σ3 が、三つ全部と反交換できるか。');
  console.log('    基底ごとの反交換子を計算して表にします（行＝M の成分、列＝相手）：');
  console.log('');
  const basis=[scaleI(2,1),S1,S2,S3], bn=['I ','σ1','σ2','σ3'];
  const part =[S1,S2,S3], pn=['σ1','σ2','σ3'];
  console.log('  ' + pad('{ · , · }',12) + pn.map(s=>pad(s,16)).join(''));
  console.log('  ' + '-'.repeat(60));
  basis.forEach(function(B,i){
    const cells = part.map(function(P){
      const A = anti(B,P);
      if(maxabs(A) < 1e-12) return pad('0',16);
      // 2I か 2σk の形になる
      const isI = maxabs(sub(A, scaleI(2,2))) < 1e-12;
      if(isI) return pad('2I',16);
      let lab='?';
      part.forEach(function(Q,qi){ if(maxabs(sub(A, scal(Q,2))) < 1e-12) lab='2'+pn[qi]; });
      return pad(lab,16);
    });
    console.log('  ' + pad(bn[i],12) + cells.join(''));
  });
  console.log('');
  console.log('  ★ 読み方：{M,σ1}=0 を課すと、表の σ1 列で 0 でない項が消えねばならない');
  console.log('    → a（I 行が 2σ1 を出す）と b（σ1 行が 2I を出す）が 0。');
  console.log('    同じことを σ2, σ3 でもやると c, d も 0。');
  console.log('');
  console.log('  ★★ したがって 4 本目は零行列だけ ── ★ 2×2 では 3 本が限界です。');
  console.log('    ★ 3+1 次元には γ^0..γ^3 の 4 本が要るので、2×2 では足りない。');
}

{
  console.log('');
  console.log('  ★ 4×4 なら作れます（ディラック表示）。機械精度で検算します：');
  const g0=zeros(4); g0[0][0]=[1,0]; g0[1][1]=[1,0]; g0[2][2]=[-1,0]; g0[3][3]=[-1,0];
  function gk(sig){ const G=zeros(4);
    for(let a=0;a<2;a++) for(let b=0;b<2;b++){
      G[a][2+b]=[sig[a][b][0], sig[a][b][1]];
      G[2+a][b]=[-sig[a][b][0], -sig[a][b][1]];
    } return G; }
  const G=[g0, gk(S1), gk(S2), gk(S3)];
  const eta=[1,-1,-1,-1];
  let worst=0;
  console.log('');
  console.log('  ' + pad('μ ν',8) + pad('{γ^μ,γ^ν} − 2η^{μν}I の最大絶対値',36) + '予言');
  console.log('  ' + '-'.repeat(60));
  for(let m=0;m<4;m++) for(let n=m;n<4;n++){
    const T=sub(anti(G[m],G[n]), scaleI(4, m===n?2*eta[m]:0));
    const err=maxabs(T); worst=Math.max(worst,err);
    if(m===n || (m===0&&n<3))
      console.log('  ' + pad(m+' '+n,8) + pad(e(err,2),36) + (m===n?('2η^{'+m+m+'} = '+(2*eta[m])):'0'));
  }
  console.log('');
  console.log('      ★ 全 10 通りでの最大誤差 = ' + e(worst,2));
  console.log('  ★★ 4 成分 ── ★ これがスピンです。');
  console.log('    ★ 「一階のまま両方向へ進みたい」と言った代償が、★ 4 成分の内部自由度でした。');
  console.log('    ★ 反粒子（2 成分ぶん）も、ここで一緒についてきます。');
}

// ------------------------------------------------------------------
hr('5. 三階にすると何が壊れるか ── アブラハム＝ローレンツ');

{
  const re = QE*QE/(4*Math.PI*EPS0*ME*C*C);
  const tau0 = 2*re/(3*C);
  console.log('  放射反作用を古典的に書くと、★ 三階微分の項が出ます：');
  console.log('');
  console.log('      m(ẍ − τ0 x⃛) = F,     τ0 = 2e²/(3·4πε0 m c³) = 2r_e/3c');
  console.log('');
  console.log('      古典電子半径 r_e = ' + e(re,4) + ' m');
  console.log('      ★ τ0 = ' + e(tau0,4) + ' s');
  console.log('');
  console.log('  ★ F = 0（力ゼロ）でも、ẍ = A·e^{t/τ0} という解が残ります ── ★ 暴走解。');
  console.log('');
  console.log('  ' + pad('経過時間',16) + pad('t/τ0',14) + pad('増幅率',24));
  console.log('  ' + '-'.repeat(56));
  [[tau0*Math.LN2,'τ0·ln2'],[1e-23,'10 zs'],[1e-21,'1 as'],[1e-12,'1 ps']].forEach(function(p){
    const r=p[0]/tau0;
    console.log('  ' + pad(p[1],16) + pad(e(r,3),14)
      + pad(r<50?f(Math.exp(r),3):('10^'+e(r/Math.LN10,3)),24));
  });
  console.log('');
  console.log('  ★ 倍になるのに ' + e(tau0*Math.LN2,3) + ' 秒。★ 1 ps で 10^(6.9e10) 倍。');
  console.log('');
  console.log('  数値でも確かめます（ẍ = τ0 x⃛ を a\' = a/τ0 として RK4 積分）：');
  let a=1e-30, t=0; const dt=tau0/2000;
  let tDouble=null;
  for(let n=0;n<400000;n++){
    const k1=a/tau0, k2=(a+0.5*dt*k1)/tau0, k3=(a+0.5*dt*k2)/tau0, k4=(a+dt*k3)/tau0;
    a += dt*(k1+2*k2+2*k3+k4)/6; t += dt;
    if(tDouble===null && a>=2e-30) tDouble=t;
  }
  console.log('      2 倍になった時刻 = ' + e(tDouble,6) + ' s（予言 τ0·ln2 = ' + e(tau0*Math.LN2,6) + '）');
  console.log('      ★ 差は ' + e(Math.abs(tDouble-tau0*Math.LN2)/(tau0*Math.LN2),2)
            + ' ── 刻み幅（τ0/2000）で判定しているぶんのずれ');
  console.log('');
  console.log('  ★ 暴走を避けようと境界条件を未来側で決めると、こんどは ★ 前加速 が出ます');
  console.log('    ── 力が来る ' + e(tau0,2) + ' 秒 前に、もう加速が始まる（第 12 回）。');
  console.log('');
  const tC = HBAR/(ME*C*C);
  console.log('  ★ ただし公平のため：τ0 = ' + e(tau0,3) + ' s に対し、');
  console.log('    電子のコンプトン時間 ħ/mc² = ' + e(tC,3) + ' s。');
  console.log('    ★ 比は ' + f(tC/tau0,1) + ' 倍 ── ★ τ0 は古典電磁気が通用しない領域の深く内側。');
  console.log('    ★ だから「因果律が壊れた」のではなく ★「使ってはいけない所で使った」が正確です。');
}

// ------------------------------------------------------------------
hr('6. ★ 梯子で読むと、三階が壊れる理由が一行で出る');

console.log('  第 12 回でこう測りました ── 力 F = k·D^α x のとき、');
console.log('  一周期あたりに系へ入る仕事は');
console.log('');
console.log('      ★ W = π k ω^α |x|² · sin(απ/2)');
console.log('');
console.log('  ★ ここでの α は「変位から力を作る階数」です。インピーダンス');
console.log('    Z = F/v の階数 β とは ★ β = α − 1 の関係（v = iωx だから）。');
console.log('  ★ sin の符号がそのまま「散逸か、供給か」を決めます。数値で確かめます：');
console.log('');

function workPerCycle(alpha, k, w, amp, N){
  const mag = k*Math.pow(w,alpha), ph = alpha*Math.PI/2;
  let W=0; const T=2*Math.PI/w, h=T/N;
  for(let n=0;n<N;n++){
    const t=(n+0.5)*h;
    W += mag*amp*Math.cos(w*t+ph) * (-amp*w*Math.sin(w*t)) * h;
  }
  return W;
}

{
  const k=1, w=1, amp=1, N=2000000;
  console.log('  ' + pad('α',7) + pad('β=α−1',8) + pad('部品',20) + pad('数値 W',14) + pad('予言',14) + '意味');
  console.log('  ' + '-'.repeat(84));
  [[-1,'（禁止領域）'],[-0.5,'（禁止領域）'],[0,'ばね'],[0.5,'★ ワールブルグ'],[1,'ダンパ'],
   [1.5,'半質量'],[2,'質量'],[2.5,'（禁止領域）'],[3,'★ 放射反作用'],[4,'パイス＝ウーレンベック']]
  .forEach(function(p){
    const a=p[0];
    const num=workPerCycle(a,k,w,amp,N);
    const th=Math.PI*k*Math.pow(w,a)*amp*amp*Math.sin(a*Math.PI/2);
    const s = th>1e-9?'散逸':(th<-1e-9?'★★ 供給（能動）':'無散逸');
    console.log('  ' + pad(f(a,1),7) + pad(f(a-1,1),8) + pad(p[1],20)
      + rpad(f(num,5),10) + pad('',4) + rpad(f(th,5),10) + pad('',4) + s);
  });
  console.log('');
  console.log('  ★ ワールブルグは α = +1/2（β = −1/2）── ★ ちゃんと散逸側にいます。');
  console.log('  ★★ α = 3（放射反作用）で W が ★ 負 ── ★ 系がエネルギーを受け取り続ける。');
  console.log('    ★ これが第 5 節の e^{t/τ0} の正体でした。');
  console.log('    ★ 第 12 回の sin(απ/2) と、アブラハム＝ローレンツの暴走が ★ 同じ一つのこと。');
  console.log('');
  console.log('  ★ そして α = 4 は W = 0 ── ★ 散逸の符号では捕まりません。次々節へ。');
}

// ------------------------------------------------------------------
hr('7. ★★ 第 15 回の長方形を測り直す');

console.log('  受動性（外へエネルギーを出しこそすれ、湧き出させない）は一行です：');
console.log('');
console.log('      ★ Re Z(ω) ≥ 0    （すべての ω で）');
console.log('');
console.log('  Z = (iω)^β なら Re Z = ω^β cos(βπ/2)。★ 符号は cos だけで決まります。');
console.log('');
{
  console.log('  ' + pad('β',8) + pad('α=β+1',9) + pad('cos(βπ/2)',13) + pad('位相 [度]',12) + '判定');
  console.log('  ' + '-'.repeat(60));
  [-3,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,3,4,5].forEach(function(b){
    const c=Math.cos(b*Math.PI/2);
    let v;
    if(c>1e-12) v='受動';
    else if(Math.abs(c)<1e-12) v='境界（無損失）';
    else v='★★ 能動 ＝ 禁止';
    console.log('  ' + pad(f(b,1),8) + pad(f(b+1,1),9) + rpad(f(c,5),9) + pad('',4)
      + rpad(f(b*90,1),8) + pad('',4) + v);
  });
  console.log('');
  console.log('  ★★ ここが大事です ── ★ 受動性が許すのは ★ 一つの帯ではありません：');
  console.log('');
  console.log('      ★ cos(βπ/2) ≥ 0  ⟺  β ∈ [−1, 1] ∪ [3, 5] ∪ [7, 9] ∪ …');
  console.log('        （4 おきに、幅 2 の帯が並ぶ）');
  console.log('');
  console.log('  ★ β = 3（＝ α = 4）は無損失なので、★ 受動性では落とせません。');
  console.log('    ★ ここを落とすのが ★ オストログラツキー（次節）です。');
  console.log('');
  console.log('  ★★ つまり二つの定理が ★ 交互に効いています：');
  console.log('');
  console.log('  ' + pad('階数 α',10) + pad('例',22) + pad('受動性',14) + pad('オストログラツキー',20) + '結論');
  console.log('  ' + '-'.repeat(84));
  [['0','ばね','◯ 通す','◯ 通す','許される'],
   ['1','ダンパ','◯ 通す','◯ 通す','許される'],
   ['2','質量・波動方程式','◯ 通す（境界）','◯ 通す','★ 許される'],
   ['3','放射反作用','★ 落とす','—','★ 禁止（暴走）'],
   ['4','パイス＝ウーレンベック','◯ 通してしまう','★ 落とす','★ 禁止（ゴースト）'],
   ['5','—','★ 落とす','—','禁止']
  ].forEach(function(r){ console.log('  ' + pad(r[0],10)+pad(r[1],22)+pad(r[2],14)+pad(r[3],20)+r[4]); });
  console.log('');
  console.log('  ★★ 奇数階は受動性が、偶数階はオストログラツキーが落とす。');
  console.log('    ★ どちらか一方では ★ 足りません。');
  console.log('');
  console.log('  ★ そのうえで第 15 回を採点します：');
  console.log('');
  console.log('  ' + pad('第 15 回の主張',28) + pad('判定',12) + '理由');
  console.log('  ' + '-'.repeat(86));
  [['長方形（幅 2 の帯）に住む',  '◎ 正しい', '★ 単位を揃えると β ∈ [−1, +1]'],
   ['上端は 2',                '△ 単位違い','★ 上端 α=2 は「方程式の階数」。β では +1'],
   ['下端は −1/2',             '× 誤り',   '★ −1/2 は「インピーダンスの階数」で、しかも端ではない'],
   ['下端の理由は因果律',        '× 誤り',   '★ 因果律ではなく受動性。(iω)^{−2} は因果的だが能動'],
   ['上端の理由はオストログラツキー','△ 半分',  '★ α=3 を落とすのは受動性。α=4 がオストログラツキー']
  ].forEach(function(r){ console.log('  ' + pad(r[0],28)+pad(r[1],12)+r[2]); });
  console.log('');
  console.log('  ★★ 何が起きていたか ── ★ 長方形の両端を ★ 別々の単位で測っていました。');
  console.log('      下端 −1/2：ワールブルグ ＝ インピーダンスの階数 β');
  console.log('      上端 +2  ：波動方程式  ＝ 方程式の階数 α（β では +1）');
  console.log('    ★ ワールブルグの β = −1/2 は ★ 端ではなく帯のまん中あたりです。');
  console.log('    ★ 端に見えたのは「手持ちで一番 負だった」から ── ★ 定理ではなく観測でした。');
  console.log('');
  console.log('  ★★ 書き直した帯：');
  console.log('');
  console.log('      ★ β ∈ [−1, +1]（＝ α ∈ [0, 2]）、虚部 ≈ 0');
  console.log('      ★ 両端は無損失（ばねと質量）、内側が散逸、外は物理ではない');
  console.log('      ★ 幅はちょうど 2 ── ★ 一階ぶん ずつ 両側。');
}

// ------------------------------------------------------------------
hr('8. 四階を落とすのは誰か ── オストログラツキーを数値で見る');

console.log('  α = 4 は無散逸でした。★ それでも禁止される理由は ★ 負エネルギーの部門です。');
console.log('');
console.log('  パイス＝ウーレンベック振動子（四階の代表）：');
console.log('');
console.log('      L = ½[ẍ² − (ω1²+ω2²)ẋ² + ω1²ω2² x²]');
console.log('      → x⁗ + (ω1²+ω2²)ẍ + ω1²ω2² x = 0     解は e^{±iω1 t}, e^{±iω2 t}');
console.log('');
console.log('  オストログラツキーのエネルギー：');
console.log('');
console.log('      H = ½ẍ² − ẋ·x⃛ − ½(ω1²+ω2²)ẋ² − ½ω1²ω2² x²');
console.log('');

{
  const w1=2.0, w2=1.0;
  function H(x,v,acc,jerk){
    return 0.5*acc*acc - v*jerk - 0.5*(w1*w1+w2*w2)*v*v - 0.5*w1*w1*w2*w2*x*x;
  }
  console.log('  ' + pad('状態',24) + pad('H（数値）',16) + pad('H（解析）',16) + '符号');
  console.log('  ' + '-'.repeat(66));
  [['モード1だけ A=1', 1,0],['モード1だけ A=2',2,0],['モード2だけ B=1',0,1],['モード2だけ B=2',0,2]]
  .forEach(function(p){
    const A=p[1], B=p[2], t=0.37;
    const x   =  A*Math.cos(w1*t) + B*Math.cos(w2*t);
    const v   = -A*w1*Math.sin(w1*t) - B*w2*Math.sin(w2*t);
    const acc = -A*w1*w1*Math.cos(w1*t) - B*w2*w2*Math.cos(w2*t);
    const jrk =  A*w1*w1*w1*Math.sin(w1*t) + B*w2*w2*w2*Math.sin(w2*t);
    const num = H(x,v,acc,jrk);
    const th  = 0.5*(w1*w1-w2*w2)*(A*A*w1*w1 - B*B*w2*w2);
    console.log('  ' + pad(p[0],24) + rpad(f(num,6),12) + pad('',4) + rpad(f(th,6),12) + pad('',4)
      + (th<0?'★★ 負':'正'));
  });
  console.log('');
  console.log('      解析式：★ H = ½(ω1²−ω2²)(A²ω1² − B²ω2²)');
  console.log('  ★★ モード 2 のエネルギーは ★ 負。★ B を大きくすれば H はいくらでも下がる。');
  console.log('    ★ 下に有界でない ── これがオストログラツキーの不安定性です。');
  console.log('');

  function mk(w1,w2,lam){
    function HH(x,v,a,j){ return 0.5*a*a - v*j - 0.5*(w1*w1+w2*w2)*v*v - 0.5*w1*w1*w2*w2*x*x; }
    function d(y){ return [y[1],y[2],y[3],
      -(w1*w1+w2*w2)*y[2] - w1*w1*w2*w2*y[0] - lam*y[0]*y[0]*y[0]]; }
    function rk4(y,h){ const k1=d(y),k2=d(y.map((v,i)=>v+0.5*h*k1[i])),
      k3=d(y.map((v,i)=>v+0.5*h*k2[i])),k4=d(y.map((v,i)=>v+h*k3[i]));
      return y.map((v,i)=>v+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6); }
    return {HH:HH, rk4:rk4};
  }

  console.log('  ★ まず λ = 0（結合なし）で、数値積分が信頼できることを確認：');
  {
    const m=mk(w1,w2,0);
    let y=[2,0,-w1*w1-w2*w2,0]; const h=1e-4; const H0=m.HH(y[0],y[1],y[2],y[3]);
    let mx=0;
    for(let n=0;n<2000000;n++){ y=m.rk4(y,h);
      const d=Math.abs(m.HH(y[0],y[1],y[2],y[3])-H0); if(d>mx) mx=d; }
    console.log('      200 秒 積分して H のずれ 最大 ' + e(mx,2) + '（H0 = ' + f(H0,4) + '）── 保存 OK');
  }
  console.log('');
  console.log('  ★ 次に λ x³ の結合を入れて、暴走するかを ★ 実際に探します。');
  console.log('    （A=B=1 から出発、400 秒 まで、|x| が 1e6 を超えたら「暴走」と判定）');
  console.log('');
  console.log('  ' + pad('ω1/ω2',14) + pad('λ=0.01',16) + pad('λ=0.1',16) + pad('λ=1',16));
  console.log('  ' + '-'.repeat(60));
  [[2.0,1.0],[1.5,1.0],[1.1,1.0],[1.01,1.0]].forEach(function(W){
    const cells=[0.01,0.1,1].map(function(lam){
      const m=mk(W[0],W[1],lam);
      let y=[2,0,-W[0]*W[0]-W[1]*W[1],0]; const h=2e-4;
      let blew=null; const n=Math.round(400/h);
      for(let i=1;i<=n;i++){
        y=m.rk4(y,h);
        if(!isFinite(y[0])||Math.abs(y[0])>1e6){ blew=i*h; break; }
      }
      return pad(blew===null?'— 起きない':('★ '+f(blew,1)+' 秒'),16);
    });
    console.log('  ' + pad(f(W[0],2)+' / '+f(W[1],2),14) + cells.join(''));
  });
  console.log('');
  console.log('  ★★ 結果は一様ではありませんでした ──');
  console.log('    ★ ω1/ω2 = 2 の弱結合（λ ≤ 0.1）では、400 秒 走らせても ★ 暴走しません。');
  console.log('    ★ ところが ω1 を ω2 に近づけると、弱い結合でも ★ 暴走します。');
  console.log('    ★ 縮退に近いほど危ない ── 正負の部門の周波数が近いと、やり取りが効くからです。');
  console.log('');
  console.log('  ★ ここは正直に書きます：★「四階は必ず即 暴走する」ではありません。');
  console.log('    ★ 確実に言えるのは ★ H が下に有界でないこと（解析・上の表）。');
  console.log('    ★ 実際に暴走するかは結合と周波数比しだいで、安定に見える島もあります。');
  console.log('    ── ★ それでも ★ 下に有界でない以上、★ 基礎理論としては使えません。');
  console.log('      ★ 「たまたま落ちないだけの椅子」に座り続ける理由がないからです。');
}

// ------------------------------------------------------------------
hr('9. まとめ');

{
  const rows = [
    ['一階（時間）では振動しない',    '◎ 解析', '★ ω = −iDk² は純虚数'],
    ['拡散の「無限速度」は観測外',    '◎ 数値', '1 ns 後の 1 m 先で 10^(−1.1e12)'],
    ['二階 ＝ 両方向',               '◎ 数値', '★ □=(∂t−c∂x)(∂t+c∂x)、山が 0.5 ずつに割れる'],
    ['一階で波にする代償がスピン',    '◎ 数値', '★ 2×2 では 3 本が限界、4×4 で誤差ゼロ'],
    ['三階は暴走する',               '◎ 数値', '★ τ0=6.27e-24 s、倍加 4.34e-24 s'],
    ['三階の暴走 ＝ sin(3π/2)<0',    '◎ 数値', '★ 一周期の仕事 W が負'],
    ['受動性 ⟺ cos(βπ/2) ≥ 0',    '◎ 解析', '★ ただし 4 おきに帯が並ぶ。一意ではない'],
    ['四階は受動性では落ちない',      '◎ 数値', '★ W = 0。落とすのはオストログラツキー'],
    ['H は下に有界でない',           '◎ 数値', '★ H = ½(ω1²−ω2²)(A²ω1²−B²ω2²)'],
    ['四階が必ず即 暴走はしない',     '★ 訂正', '★ ω1/ω2=2・λ≤0.1 では 400 秒 起きない'],
    ['第 15 回の長方形は単位が混在',  '★ 訂正', '★ 下端 −1/2 は β、上端 2 は α だった']
  ];
  console.log('  ' + pad('主張',30) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(92));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],30)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     二階とは「両方向」のことだった。');
  console.log('     そして帯の幅 2 は、★ 受動性とオストログラツキーが ★ 交互に決めていた。');
  console.log('     ── ★★ 奇数階は受動性が、偶数階はゴーストが落とす。');
  console.log('');
  console.log('  ★★ 本回は ★ このシリーズ自身の第 15 回を二か所 訂正しました。');
  console.log('    ① 長方形の両端は別々の単位で測られていた（β と α）。');
  console.log('    ② 下端の理由は因果律ではなく受動性。そもそも −1/2 は端ではない。');
  console.log('    ★ 反証可能だと宣言した以上、★ 自分の回も採点対象です。');
}

console.log('');
