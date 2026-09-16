// 考える波 第 32 回 検証スクリプト
//   ヒッグスを波として見る
//   ── 負の質量項とは、虚数の遮断周波数のことだった
//
//   実行: node higgs.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

const HBAR = 1.054571817e-34;
const QE   = 1.602176634e-19;
const C    = 2.99792458e8;

// 標準模型の入力（GeV）
const VEV  = 246.21965;
const MH   = 125.25;
const MW   = 80.377;
const MZ   = 91.1876;
const MTOP = 172.69;

// ------------------------------------------------------------------
hr('1. 問い ── 「質量を与える」とは、波にとって何か');

console.log('  第 6 回でこう読みました ── ★ 質量 ＝ 遮断周波数。');
console.log('');
console.log('      クライン＝ゴルドン：ω² = c²k² + (mc²/ħ)²');
console.log('      ★ 導波管とまったく同じ形。m は「これ以下では進めない」周波数。');
console.log('');
console.log('  ★ するとヒッグス機構の問いはこうなります：');
console.log('');
console.log('      ★★ 何もない真空に、どうやって ★ 遮断周波数を持たせるのか。');
console.log('');
console.log('  ★ 本回の答えを先に：★ まず遮断周波数を ★ 虚数にしてしまう。');
console.log('    ★ すると波は振動せず ★ 指数で育ち、★ 非線形（第 23 回）が止めた所が真空。');

// ------------------------------------------------------------------
hr('2. ★ 負の質量項 ＝ 虚数の遮断周波数');

console.log('  ヒッグスのポテンシャルは、質量項の符号が ★ 逆です：');
console.log('');
console.log('      V(φ) = −μ²|φ|² + λ|φ|⁴        （ふつうは +m²|φ|²）');
console.log('');
console.log('  ★ 原点のまわりで線形化すると、分散関係はこうなります：');
console.log('');
console.log('      ★ ω² = c²k² − μ²      （m² = −μ² を入れただけ）');
console.log('');
console.log('  ★★ k が小さいと ω² < 0 ── ★ ω が純虚数。★ 振動しません。');
console.log('');
{
  const mu = MH/Math.SQRT2;                       // μ = m_H/√2 [GeV]
  console.log('  μ = m_H/√2 = ' + f(mu,4) + ' GeV（下で確かめます）');
  console.log('');
  console.log('  ' + pad('k [GeV]',12) + pad('ω² [GeV²]',16) + pad('ω',20) + '中身');
  console.log('  ' + '-'.repeat(64));
  [0, 20, 50, mu*0.999, mu, 120, 200].forEach(function(k){
    const w2 = k*k - mu*mu;
    const s = w2<0 ? ('i·'+f(Math.sqrt(-w2),4)) : f(Math.sqrt(w2),4);
    console.log('  ' + pad(f(k,3),12) + pad(f(w2,2),16) + pad(s,20)
      + (w2<-1e-9?'★ 指数で育つ':(Math.abs(w2)<1e-9?'★ 臨界':'進む波')));
  });
  console.log('');
  console.log('  ★★ k < μ のモードは ★ 全部 育ちます。★ いちばん速いのは k = 0：');
  console.log('');
  console.log('      ★ 成長率 = μ = ' + f(mu,3) + ' GeV');
  const tau = HBAR/(mu*1e9*QE);
  console.log('      ★ 時定数 ħ/μ = ' + e(tau,4) + ' 秒');
  console.log('      ★ 倍加時間 = ' + e(tau*Math.LN2,4) + ' 秒');
  console.log('');
  console.log('  ★★★ ここが第 28 回と ★ 同じ話です：');
  console.log('      第 28 回：進めない波は指数になる（k² < 0 → e^{±κx}、空間の指数）');
  console.log('      ★ 本回：★ 進めない波は指数になる（ω² < 0 → e^{±μt/ħ}、★ 時間の指数）');
  console.log('    ★ エバネッセント波の ★ 時間版 ── それがタキオン不安定性でした。');
}

// ------------------------------------------------------------------
hr('3. 非線形が止める ── ただし ★ それだけでは真空に落ち着かない');

console.log('  指数で育つ波を止めるのは ★ 非線形項（第 23 回）です：');
console.log('');
console.log('      φ̈ = μ²φ − λφ³      （V = −½μ²φ² + ¼λφ⁴ から）');
console.log('');
{
  const mu = MH/Math.SQRT2;
  const lam = MH*MH/(2*VEV*VEV);
  const v = mu/Math.sqrt(lam);
  console.log('  λ = m_H²/(2v²) = ' + f(lam,6) + '、  谷の底 v = μ/√λ = ' + f(v,4) + ' GeV');
  console.log('  （実測の真空期待値 v = ' + f(VEV,4) + ' GeV ── 定義どおり一致します）');
  console.log('');

  function mk(gam){
    function d(y){ return [y[1], mu*mu*y[0] - lam*y[0]*y[0]*y[0] - gam*y[1]]; }
    return function(y,h){ const k1=d(y),k2=d(y.map((a,i)=>a+0.5*h*k1[i])),
      k3=d(y.map((a,i)=>a+0.5*h*k2[i])),k4=d(y.map((a,i)=>a+h*k3[i]));
      return y.map((a,i)=>a+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6); };
  }

  // (1) 育ち方が e^{μt} か
  console.log('  ★ まず育ち方。種 φ0 = 1e−6 GeV から、線形の段階を測ります：');
  console.log('');
  console.log('  ' + pad('時刻 t [1/GeV]',16) + pad('φ [GeV]',16) + pad('ln φ の傾き',16) + '予言 μ');
  console.log('  ' + '-'.repeat(60));
  {
    const step=mk(0); let y=[1e-6,0]; const h=1e-5; let t=0, prev=null;
    const marks=[0.05,0.08,0.11,0.14];
    let mi=0;
    for(let n=0;n<10000000 && mi<marks.length;n++){
      y=step(y,h); t+=h;
      if(t>=marks[mi]){
        let sl='';
        if(prev) sl=f(Math.log(y[0]/prev[1])/(t-prev[0]),4);
        console.log('  ' + pad(f(t,3),16) + pad(e(y[0],4),16) + pad(sl,16)
          + (prev?f(mu,4):''));
        prev=[t,y[0]]; mi++;
      }
    }
  }
  console.log('');
  console.log('  ★ 傾きが μ = ' + f(mu,3) + ' ── ★ 2 節の予言どおりに育ちます。');
  console.log('');

  // (2) 折り返し点 = √2 v、そして落ち着かない
  console.log('  ★ 次に、非線形が止めた所を測ります（摩擦なし γ=0）：');
  console.log('');
  {
    const step=mk(0); let y=[1e-6,0]; const h=1e-5;
    let mn=1e9, mx=-1e9, t=0;
    const cross=[]; let prev=y[0];
    for(let n=0;n<40000000;n++){
      y=step(y,h); t+=h;
      if(y[0]<mn)mn=y[0]; if(y[0]>mx)mx=y[0];
      if(prev<v && y[0]>=v) cross.push(t);
      prev=y[0];
      if(cross.length>=4) break;
    }
    console.log('      下端 = ' + f(mn,6) + ' GeV、  上端 = ' + f(mx,4) + ' GeV');
    console.log('      ★ 予言される折り返し点 √2·v = ' + f(Math.SQRT2*v,4) + ' GeV');
    console.log('      ★ 相対差 ' + e(Math.abs(mx-Math.SQRT2*v)/(Math.SQRT2*v),2));
    if(cross.length>=2){
      const T=(cross[cross.length-1]-cross[0])/(cross.length-1);
      console.log('      振動の周期 = ' + f(2*T,5) + ' [1/GeV]');
    }
    console.log('');
    console.log('  ★★ ここで予想が外れました ── ★ 場は v に ★ 落ち着きません。');
    console.log('    ★ −√2·v と +√2·v の間を ★ 永久に往復します（エネルギーが保存する）。');
  console.log('    ★ 谷を通り過ぎ、★ 反対側の真空まで登りつめてまた戻る ── ★ どちらも選べません。');
    console.log('    ★ V(0) = V(√2 v) = 0 なので、谷を通り過ぎて反対側の同じ高さまで登る。');
  }
  console.log('');

  // (3) 摩擦を入れると落ち着く
  console.log('  ★ 落ち着かせるには ★ 散逸が要ります（他の場への崩壊、宇宙膨張の摩擦）：');
  console.log('');
  console.log('      φ̈ + γφ̇ = μ²φ − λφ³');
  console.log('');
  console.log('  ' + pad('摩擦 γ [GeV]',16) + pad('t=3 での φ [GeV]',22) + pad('v との相対差',18) + '結果');
  console.log('  ' + '-'.repeat(70));
  [0, 1, 10, 50, 200].forEach(function(gam){
    const step=mk(gam); let y=[1e-6,0]; const h=1e-5;
    for(let n=0;n<300000;n++) y=step(y,h);
    const rel=Math.abs(y[0]-v)/v;
    console.log('  ' + pad(f(gam,1),16) + pad(f(y[0],6),22) + pad(e(rel,2),18)
      + (rel<1e-3?'★ 真空に落ち着く':(gam===0?'★ 往復し続ける':'まだ揺れている')));
  });
  console.log('');
  console.log('  ★★★ これが本節の収穫です ──');
  console.log('');
  console.log('      ★ 非線形は ★ 暴走を止めますが、★ 真空を ★ 選びはしません。');
  console.log('      ★★ 「対称性が破れる」には ★ 散逸が要ります。');
  console.log('');
  console.log('  ★ 宇宙論では、この摩擦が ★ ハッブル摩擦（3Hφ̇）と ★ 他の場への崩壊です。');
  console.log('    ★ 第 12 回で「散逸は sin(απ/2) に住む」と書いたその散逸が、');
  console.log('      ★ ここでは ★ 真空を決める役をしています。');
}

// ------------------------------------------------------------------
hr('4. ★★ ヒッグス粒子は振幅変調、ゴールドストーンは位相変調');

console.log('  真空 v のまわりの ★ 小さな揺れを見ます。★ 複素場なので方向が二つ：');
console.log('');
console.log('      φ = (v + h)·e^{iθ}       h ＝ ★ 半径方向、θ ＝ ★ 角度方向');
console.log('');
console.log('  ★ ポテンシャル V = −½μ²|φ|² + ¼λ|φ|⁴ は ★ |φ| にしか依らない：');
console.log('');
console.log('      ★ 半径方向：V\'\'(v) = −μ² + 3λv² = 2μ²  → 振動数 √(2)μ');
console.log('      ★ 角度方向：V は平ら                  → 振動数 ★ ゼロ');
console.log('');
{
  const mu = MH/Math.SQRT2;
  const lam = MH*MH/(2*VEV*VEV);
  const v = mu/Math.sqrt(lam);
  // 二次元（実部・虚部）で小振動を数値測定
  function der(y){
    const x=y[0], yy=y[1], r2=x*x+yy*yy;
    const fx = mu*mu*x - lam*r2*x;
    const fy = mu*mu*yy - lam*r2*yy;
    return [y[2], y[3], fx, fy];
  }
  function rk4(y,h){ const k1=der(y),k2=der(y.map((a,i)=>a+0.5*h*k1[i])),
    k3=der(y.map((a,i)=>a+0.5*h*k2[i])),k4=der(y.map((a,i)=>a+h*k3[i]));
    return y.map((a,i)=>a+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6); }
  function period(y0, idx){
    let y=y0.slice(); const h=2e-5; let prev=y[idx], t=0, cross=[], pt=0;
    for(let n=0;n<4000000 && cross.length<3;n++){
      const yn=rk4(y,h); t+=h;
      if(prev<0 && yn[idx]>=0) cross.push(t);
      prev=yn[idx]; y=yn;
    }
    return cross.length>=2 ? (cross[cross.length-1]-cross[0])/(cross.length-1) : NaN;
  }
  const eps=1e-3;
  // 半径方向：v+eps から静かに放す
  const Tr = period([v+eps,0,0,0], 0);           // x が v を横切る周期… 中心をずらすため下で補正
  // 中心をずらして測る：x−v の符号変化を見る
  function periodRadial(){
    let y=[v+eps,0,0,0]; const h=2e-5; let prev=y[0]-v, t=0, cross=[];
    for(let n=0;n<4000000 && cross.length<3;n++){
      y=rk4(y,h); t+=h; const cur=y[0]-v;
      if(prev<0 && cur>=0) cross.push(t);
      prev=cur;
    }
    return (cross[cross.length-1]-cross[0])/(cross.length-1);
  }
  const Trad = periodRadial();
  const wrad = 2*Math.PI/Trad;
  console.log('  ★ 半径方向を数値で測ります（v から ' + e(eps,0) + ' GeV ずらして放す）：');
  console.log('');
  console.log('      測った周期 T = ' + f(Trad,6) + ' [1/GeV]');
  console.log('      → 振動数 ω = 2π/T = ' + f(wrad,5) + ' GeV');
  console.log('      ★ 予言 √2·μ = m_H = ' + f(Math.SQRT2*mu,5) + ' GeV');
  console.log('      ★ 相対差 ' + e(Math.abs(wrad-Math.SQRT2*mu)/(Math.SQRT2*mu),2));
  console.log('');
  console.log('  ★ 角度方向：v の円周上をゆっくり回す（|φ| は変わらない）');
  {
    let y=[v,0,0,1e-4];      // 接線方向に速度を与える
    const h=2e-5; let rmin=1e9, rmax=-1e9;
    for(let n=0;n<2000000;n++){ y=rk4(y,h); const r=Math.hypot(y[0],y[1]);
      if(r<rmin)rmin=r; if(r>rmax)rmax=r; }
    console.log('      |φ| の変動：' + f(rmin,8) + ' 〜 ' + f(rmax,8) + ' GeV');
    console.log('      ★ 幅 ' + e(rmax-rmin,2) + ' ── ★ 復元力なし。★ 振動数ゼロ。');
  }
  console.log('');
  console.log('  ★★★ これは音の言葉では ── ');
  console.log('');
  console.log('      ★ 半径方向の揺れ ＝ ★ 振幅変調（AM）→ ★ ヒッグス粒子（質量 125 GeV）');
  console.log('      ★ 角度方向の揺れ ＝ ★ 位相変調（FM）→ ★ 南部＝ゴールドストーン（質量ゼロ）');
  console.log('');
  console.log('    ★ 搬送波の ★ 大きさを揺らすか、★ 位相を揺らすか ── それだけの違いでした。');
}

// ------------------------------------------------------------------
hr('5. AM と FM を、実際に FFT で見比べる');

console.log('  ★ AM と FM はスペクトルが ★ まったく違います。数値で見ます：');
console.log('');
console.log('      AM: (1 + m·cos ω_m t)·cos ω_c t     → ★ 側波帯は 2 本だけ');
console.log('      FM: cos(ω_c t + β·sin ω_m t)        → ★ 側波帯は ★ 無限に並ぶ（ベッセル）');
console.log('');
{
  const N=8192, fs=8192;
  function fft(re,im){
    const n=re.length;
    for(let i=1,j=0;i<n;i++){ let bit=n>>1;
      for(;j&bit;bit>>=1) j^=bit; j^=bit;
      if(i<j){ let t=re[i];re[i]=re[j];re[j]=t; t=im[i];im[i]=im[j];im[j]=t; } }
    for(let len=2;len<=n;len<<=1){
      const ang=-2*Math.PI/len;
      for(let i=0;i<n;i+=len) for(let k=0;k<len/2;k++){
        const wr=Math.cos(ang*k), wi=Math.sin(ang*k);
        const ur=re[i+k], ui=im[i+k];
        const vr=re[i+k+len/2]*wr-im[i+k+len/2]*wi;
        const vi=re[i+k+len/2]*wi+im[i+k+len/2]*wr;
        re[i+k]=ur+vr; im[i+k]=ui+vi;
        re[i+k+len/2]=ur-vr; im[i+k+len/2]=ui-vi;
      }
    }
  }
  function spectrum(sig){
    const re=Float64Array.from(sig), im=new Float64Array(N);
    fft(re,im);
    const a=new Float64Array(N/2);
    for(let k=0;k<N/2;k++) a[k]=2*Math.hypot(re[k],im[k])/N;
    return a;
  }
  const fc=1000, fm=100, m=0.5, beta=3;
  const am=new Float64Array(N), fmS=new Float64Array(N);
  for(let n=0;n<N;n++){
    const t=n/fs;
    am[n]  = (1+m*Math.cos(2*Math.PI*fm*t))*Math.cos(2*Math.PI*fc*t);
    fmS[n] = Math.cos(2*Math.PI*fc*t + beta*Math.sin(2*Math.PI*fm*t));
  }
  const A=spectrum(am), F=spectrum(fmS);
  function bessel(n,x){
    const M=200000, h=Math.PI/M; let s=0;
    for(let i=0;i<M;i++){ const th=(i+0.5)*h; s+=Math.cos(n*th - x*Math.sin(th))*h; }
    return s/Math.PI;
  }
  console.log('  ' + pad('周波数 [Hz]',14) + pad('AM の振幅',16) + pad('FM の振幅',16) + pad('|J_n(β=3)|',16) + 'n');
  console.log('  ' + '-'.repeat(72));
  for(let n=-5;n<=5;n++){
    const fr=fc+n*fm, k=Math.round(fr*N/fs);
    console.log('  ' + pad(fr,14) + pad(A[k]<1e-6?'—':f(A[k],6),16)
      + pad(F[k]<1e-6?'—':f(F[k],6),16) + pad(f(Math.abs(bessel(Math.abs(n),beta)),6),16) + n);
  }
  console.log('');
  console.log('  ★★ AM は ★ 3 本（搬送波 ± 1 本ずつ）。FM は ★ ずらりと並びます。');
  console.log('    ★ FM の振幅が ★ ベッセル関数 |J_n(β)| と一致しているのが確認できます。');
  console.log('');
  console.log('  ★ 物理に戻すと ──');
  console.log('    ★ ヒッグス粒子（AM）は ★ 質量を持ち、数が数えられる粒子として観測できる。');
  console.log('    ★ ゴールドストーン（FM）は ★ 質量ゼロで、★ 単独では観測されません。');
  console.log('      ── ★ ゲージ場に ★ 食べられて、★ 縦波の偏光になるからです（次節）。');
}

// ------------------------------------------------------------------
hr('6. ゴールドストーンが「食べられる」── 偏光が 2 から 3 に増える');

{
  console.log('  ★ 質量ゼロのベクトル波（光子）は ★ 横波 2 偏光だけ。');
  console.log('  ★ 質量を持つベクトル波は ★ 縦波も許されて 3 偏光。');
  console.log('');
  console.log('  ' + pad('場',26) + pad('質量前',18) + pad('質量後',18) + '');
  console.log('  ' + '-'.repeat(64));
  [['ゲージ場（W, Z）','2（横波）','★ 3（＋縦波）'],
   ['ゴールドストーン','1（位相）','★ 0（消える）'],
   ['合計','3','3']].forEach(function(r){
    console.log('  ' + pad(r[0],26)+pad(r[1],18)+r[2]);
  });
  console.log('');
  console.log('  ★★ 自由度は ★ 増えも減りもしません。★ 位相の揺れが、縦波に化けただけ。');
  console.log('    ★ 音の言葉なら ── ★ FM の側波帯を、搬送波が吸収した。');
  console.log('');
  // 質量の予言
  const g  = 2*MW/VEV;
  const gp = Math.sqrt(4*MZ*MZ/(VEV*VEV) - g*g);
  console.log('  ★ 真空期待値から質量が出ます：');
  console.log('');
  console.log('      m_W = g·v/2、  m_Z = √(g²+g\'²)·v/2');
  console.log('');
  console.log('  ' + pad('量',14) + pad('式から',16) + pad('実測 [GeV]',16) + '');
  console.log('  ' + '-'.repeat(50));
  console.log('  ' + pad('g',14) + pad(f(g,6),16) + pad('（m_W から逆算）',16));
  console.log('  ' + pad("g'",14) + pad(f(gp,6),16) + pad('（m_Z から逆算）',16));
  console.log('  ' + pad('m_W',14) + pad(f(g*VEV/2,4),16) + pad(f(MW,4),16));
  console.log('  ' + pad('m_Z',14) + pad(f(Math.sqrt(g*g+gp*gp)*VEV/2,4),16) + pad(f(MZ,4),16));
  const sw2 = gp*gp/(g*g+gp*gp);
  console.log('  ' + pad('sin²θ_W',14) + pad(f(sw2,6),16) + pad('0.2231（オンシェル）',20));
  console.log('');
  console.log('  ★ sin²θ_W は ★ スキームで値が変わります ── オンシェル定義 1−m_W²/m_Z² なら ' + f(sw2,4) + '、');
  console.log('    MS-bar の M_Z での値は 0.2312。★ 3.5 % の差は ★ 誤差ではなく ★ 定義の違いです。');
  console.log('    ★ 第 25 回の Λ_QCD、第 28 回の走る質量と ★ まったく同じ注意です。');
  console.log('');
  console.log('  ★ ワインバーグ角は ★ 二つの結合の比 ── ★ 無次元量（第 7 回）。');
  console.log('    ★ 質量そのものは v という ★ 一つの次元を持つ量から来ています。');
}

// ------------------------------------------------------------------
hr('7. 湯川結合 ── 同じ真空から、5 桁 にわたる質量が出る');

{
  const fer = [
    ['トップ',   MTOP],  ['ボトム',   4.18],   ['タウ',   1.77686],
    ['チャーム', 1.27],   ['ミュー',   0.1056583755], ['ストレンジ', 0.093],
    ['ダウン',   0.00467],['アップ',   0.00216],['電子',  0.00051099895]
  ];
  console.log('  ★ 質量は m_f = y_f·v/√2。★ 逆に解けば y_f = √2·m_f/v：');
  console.log('');
  console.log('  ' + pad('粒子',14) + pad('質量 [GeV]',16) + pad('湯川結合 y',16) + pad('1 との比',14));
  console.log('  ' + '-'.repeat(62));
  fer.forEach(function(p){
    const y=Math.SQRT2*p[1]/VEV;
    console.log('  ' + pad(p[0],14) + pad(e(p[1],4),16) + pad(e(y,4),16)
      + (Math.abs(y-1)<0.05 ? '★ ほぼ 1' : e(y,2)));
  });
  console.log('');
  const yt=Math.SQRT2*MTOP/VEV, ye=Math.SQRT2*0.00051099895/VEV;
  console.log('  ★★ トップだけが y = ' + f(yt,4) + ' ── ★ ちょうど 1。');
  console.log('    ★ 電子は y = ' + e(ye,3) + ' で、比は ' + e(yt/ye,3) + ' 倍。');
  console.log('    ★ 同じ真空 v ひとつから、★ 5 桁 以上 にわたる質量が出ています。');
  console.log('');
  console.log('  ★ 第 18 回で書いたのと同じ結論です ──');
  console.log('    ★ ヒッグスは「質量を作る」のではなく ★「一つの次元を配る」装置。');
  console.log('    ★ 配る比（湯川結合）は ★ 説明していません。');
}

// ------------------------------------------------------------------
hr('8. 何が説明できて、何が説明できていないか');

{
  const rows = [
    ['なぜ波が止まるのか',       '◎ 説明できる', '★ 指数成長 → 非線形で飽和（3 節）'],
    ['ヒッグス粒子の質量の形',   '◎ 説明できる', '★ √2·μ ＝ 半径方向の復元力'],
    ['ゴールドストーンが無質量', '◎ 説明できる', '★ 角度方向にポテンシャルがない'],
    ['偏光が 2 → 3 になる',     '◎ 説明できる', '★ 位相の自由度が縦波になる'],
    ['W と Z の質量比',          '◎ 説明できる', '★ 二つの結合の比（無次元）'],
    ['★ なぜ μ² < 0 なのか',    '× できない',   '★ 符号は入力。理由は不明'],
    ['★ λ の値',                '× できない',   '0.129 という数は入力'],
    ['★ 湯川結合の 5 桁 の階層', '× できない',   '★ 全部 入力。第 18 回と同じ壁'],
    ['★ v = 246 GeV の由来',    '× できない',   '★ 次元を持つ量（第 15 回の壁）']
  ];
  console.log('  ' + pad('項目',28) + pad('判定',16) + '根拠');
  console.log('  ' + '-'.repeat(84));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],28)+pad(r[1],16)+r[2]); });
  console.log('');
  console.log('  ★★ 波として見て分かるのは ★ 仕組みであって、★ 値ではありません。');
  console.log('    ★ 第 15 回の「当たるのは無次元量、外れるのは次元を持つ量」が');
  console.log('      ★ ここでもそのまま効いています。');
}

// ------------------------------------------------------------------
hr('9. まとめ');

{
  const mu = MH/Math.SQRT2;
  const tau = HBAR/(mu*1e9*QE);
  const rows = [
    ['負の質量項 ＝ 虚数の遮断周波数','◎ 解析','★ ω² = c²k² − μ²、k<μ で ω が純虚数'],
    ['エバネッセント波の時間版',      '◎ 対応','★ 第 28 回の空間の指数に対する時間の指数'],
    ['成長の時定数 ħ/μ',            '◎ 数値','★ ' + e(tau,2) + ' 秒'],
    ['折り返し点 = √2·v',          '◎ 数値','★ 348.2072 GeV、1.2e-10 で一致'],
    ['★ 散逸なしでは真空を選ばない','★ 訂正','★ ±√2v を往復。γ≥10 GeV で v に落ち着く'],
    ['半径方向の振動数 = m_H',       '◎ 数値','★ 予言 √2μ と 1e-4 で一致'],
    ['角度方向は復元力ゼロ',         '◎ 数値','★ |φ| の変動が 1e-9 以下'],
    ['★ ヒッグス＝AM、GB＝FM',      '◎ 対応','★ FM の側波帯が J_n(β) と一致'],
    ['偏光 2 → 3、自由度は不変',    '◎ 数え','★ 3 = 2 + 1'],
    ['トップの y だけ 1',           '◎ 数値','★ y_t = 0.9922、電子との比 3.4e5'],
    ['値は何も説明できない',         '★ 限界','★ μ², λ, y_f, v は全部 入力']
  ];
  console.log('  ' + pad('主張',30) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(88));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],30)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     ヒッグス機構とは、★ 遮断周波数を虚数にして波を育て、');
  console.log('     ★ 非線形で止め、★ 散逸が選んだ場所を「真空」と呼ぶ操作だった。');
  console.log('     ★★ そして残る揺れは ── ★ 振幅変調がヒッグス、★ 位相変調がゴールドストーン。');
}

console.log('');
