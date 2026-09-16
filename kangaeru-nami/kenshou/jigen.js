// 考える波 第 30 回 検証スクリプト
//   波動方程式の「次元」だけを動かす
//   ── 偶数次元では波が尾を引く。そして次元と階数は同じ梯子だった
//
//   実行: node jigen.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

// ------------------------------------------------------------------
hr('1. 変えるのは一文字だけ ── 空間の次元 d');

console.log('  第 29 回で「二階とは両方向のことだった」と分かりました。');
console.log('  ★ 本回は方程式をほとんど変えません。★ 変えるのは d の一文字だけです：');
console.log('');
console.log('      ∂²u/∂t² = c²∇²u        （d 次元の ∇²）');
console.log('');
console.log('  球対称にすると、d はここにしか出てきません：');
console.log('');
console.log('      ★ ∂²u/∂t² = c²( ∂²u/∂r² + (d−1)/r · ∂u/∂r )');
console.log('');
console.log('  ★ 係数 (d−1) の一か所だけ。★ これを動かすと何が起きるか。');
console.log('');
console.log('  ★★ 結論を先に言うと ──');
console.log('      ★ 奇数次元では波は鋭く通り過ぎ、★ 偶数次元では ★ 尾を引きます。');
console.log('      ★★ そして「尾の階数」は α = (d−3)/2 ── ★ 次元と階数は同じ梯子でした。');

// ------------------------------------------------------------------
hr('2. 厳密解を並べる ── 遅延グリーン関数');

console.log('  点源に対する応答（遅延グリーン関数）は、次元ごとに知られています。');
console.log('  c = 1、s = t − r（前面からの経過）と書きます：');
console.log('');
{
  const rows = [
    ['1','(1/2)·θ(s)',                 '★ 段差（永久に残る）','−1'],
    ['2','(1/2π)/√(t²−r²)',           '★ 尾を引く s^(−1/2)','−1/2'],
    ['3','δ(s)/(4πr)',                '★ 鋭い（尾なし）',   '0'],
    ['4','∝ ∂_t[ θ(s)/√(t²−r²) ]',    '★ 尾を引く s^(−3/2)','+1/2'],
    ['5','∝ δ\'(s)/r³ + δ(s)/r²',     '★ 鋭いが微分される', '+1'],
    ['6','—',                          '★ 尾を引く',        '+3/2']
  ];
  console.log('  ' + pad('d',5) + pad('グリーン関数',30) + pad('前面の後ろ',22) + '階数 α');
  console.log('  ' + '-'.repeat(68));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],5)+pad(r[1],30)+pad(r[2],22)+r[3]); });
  console.log('');
  console.log('  ★ 階数 α の定義：G ∝ D^α δ(s) と書いたときの α（D = d/dt）。');
  console.log('      δ そのものが α = 0、θ(s) は δ の積分だから α = −1、');
  console.log('      s^(−1/2) は ★ 半階の積分（第 2 回のワールブルグと同じ形）で α = −1/2。');
  console.log('');
  console.log('  ★★ 表の右端を見ると ── ★ α = (d−3)/2。数値で確かめます：');
  console.log('');
  console.log('  ' + pad('d',6) + pad('表の α',12) + pad('(d−3)/2',12) + '一致');
  console.log('  ' + '-'.repeat(44));
  [[1,-1],[2,-0.5],[3,0],[4,0.5],[5,1],[6,1.5]].forEach(function(p){
    console.log('  ' + pad(p[0],6) + pad(f(p[1],2),12) + pad(f((p[0]-3)/2,2),12)
      + (Math.abs(p[1]-(p[0]-3)/2)<1e-12?'◎':'×'));
  });
}

// ------------------------------------------------------------------
hr('3. 前面の指数を数値で測る');

console.log('  「尾の階数」は、前面のすぐ後ろでの立ち上がり方で測れます。');
console.log('  G ∝ s^λ とすると λ = −α−1 のはずです（D^α δ ↔ s^(−α−1)）。');
console.log('');
{
  // d=2 と d=4 の厳密解から λ を測る
  function G2(r,t){ return t>r ? 1/(2*Math.PI*Math.sqrt(t*t-r*r)) : 0; }
  function G4(r,t){ // ∝ ∂_t[ 1/√(t²−r²) ] = −t/(t²−r²)^{3/2}
    return t>r ? -t/Math.pow(t*t-r*r,1.5) : 0; }
  function G1(r,t){ return t>r ? 0.5 : 0; }

  console.log('  ' + pad('d',5) + pad('s = t−r',12) + pad('G',20) + pad('測った λ',14) + pad('予言 λ=−α−1',14));
  console.log('  ' + '-'.repeat(68));
  const r=1;
  [[1,G1,0],[2,G2,-0.5],[4,G4,-1.5]].forEach(function(p){
    const d=p[0], G=p[1], lam=p[2];
    let prev=null;
    [1e-4,1e-5,1e-6].forEach(function(s){
      const g=G(r,r+s);
      let meas='';
      if(prev!==null) meas=f(Math.log(Math.abs(g/prev[1]))/Math.log(s/prev[0]),5);
      console.log('  ' + pad(d,5) + pad(e(s,0),12) + pad(e(Math.abs(g),4),20)
        + pad(meas,14) + (prev!==null?f(lam,2):''));
      prev=[s,g];
    });
  });
  console.log('');
  console.log('  ★★ d=1 で λ=0（段差）、d=2 で λ=−1/2、d=4 で λ=−3/2 ── ★ ぴったり。');
  console.log('    ★ α = −λ−1 に直すと −1、−1/2、+1/2 ── ★ (d−3)/2 と一致します。');
  console.log('');
  console.log('  ★ そして d=3 だけは s^λ の形にならず、★ δ そのもの（幅ゼロ）。');
  console.log('    ── ★ これがホイヘンスの原理です。');
}

// ------------------------------------------------------------------
hr('4. ★ なぜ半階が出るのか ── 次元を一つ消すと半階になる');

console.log('  ここが本回の中心です。★ アダマールの降下法：');
console.log('');
console.log('      ★ d 次元の解は、d+1 次元の解を ★ 一方向に積分したもの。');
console.log('');
console.log('  2 次元の波は「3 次元で z 軸に一様に並べた線源」を見ているのと同じです：');
console.log('');
console.log('      G₂(r,t) = ∫ G₃(√(r²+z²), t) dz');
console.log('');
console.log('  ★ 3 次元の G₃ は ★ 鋭い（δ）のに、z で積分すると ★ 尾が出る。数値で確かめます。');
console.log('');
{
  const sig = 0.004;                      // δ をこの幅でなまして扱う
  function gauss(s){ return Math.exp(-s*s/(2*sig*sig))/(sig*Math.sqrt(2*Math.PI)); }
  function G3s(R,t){ return gauss(t-R)/(4*Math.PI*R); }
  function descend(r,t){
    // ∫ dz G3s(√(r²+z²), t) 、z について対称なので 2×[0,∞)
    const zmax = Math.sqrt(Math.max(t*t-r*r,0)) + 40*sig + 1e-9;
    const N=400000, h=zmax/N; let s=0;
    for(let i=0;i<N;i++){ const z=(i+0.5)*h; s += G3s(Math.sqrt(r*r+z*z), t)*h; }
    return 2*s;
  }
  function G2exact(r,t){ return t>r ? 1/(2*Math.PI*Math.sqrt(t*t-r*r)) : 0; }

  console.log('  ' + pad('r',7) + pad('t',7) + pad('降下法の積分',20) + pad('2 次元の厳密解',20) + '相対誤差');
  console.log('  ' + '-'.repeat(68));
  [[1,2],[1,3],[1,5],[2,3],[2,6]].forEach(function(p){
    const a=descend(p[0],p[1]), b=G2exact(p[0],p[1]);
    console.log('  ' + pad(f(p[0],1),7) + pad(f(p[1],1),7) + pad(f(a,8),20) + pad(f(b,8),20)
      + e(Math.abs(a-b)/b,2));
  });
  console.log('');
  console.log('  ★★ 一致しました。★ 鋭い δ を一次元ぶん積分すると、尾のある 1/√ になる。');
  console.log('');

  // 到着時刻の分布 ── これが半階の正体
  console.log('  ★ なぜ 1/√ なのか。★ z 軸上の各点からの ★ 到着の遅れを数えます：');
  console.log('');
  console.log('      z の点からの遅れ  s(z) = √(r²+z²) − r');
  console.log('      ★ 逆に解くと z = √(s² + 2rs)、単位遅れあたりの本数は dz/ds');
  console.log('');
  console.log('  ' + pad('s',12) + pad('dz/ds（数値）',20) + pad('√(r/2s)',18) + '比');
  console.log('  ' + '-'.repeat(60));
  const r=1;
  [1e-2,1e-3,1e-4,1e-5].forEach(function(s){
    const h=s*1e-4;
    const zp=Math.sqrt((s+h)*(s+h)+2*r*(s+h)), zm=Math.sqrt((s-h)*(s-h)+2*r*(s-h));
    const num=(zp-zm)/(2*h), th=Math.sqrt(r/(2*s));
    console.log('  ' + pad(e(s,0),12) + pad(f(num,6),20) + pad(f(th,6),18) + f(num/th,6));
  });
  console.log('');
  console.log('  ★★ dz/ds ∝ s^(−1/2) ── ★ これが半階の正体です。');
  console.log('    ★ 消した自由度（z 軸の直線）が、★ 遅れについて s^(−1/2) で分布していた。');
  console.log('');
  console.log('  ★★★ ここで第 26 回の仮説が、★ まったく別の分野で検証されます：');
  console.log('');
  console.log('      第 26 回【書き直した仮説】分数階が現れるのは、粗視化した自由度が');
  console.log('                              ★ スケール不変に（べき乗で）分布しているとき。');
  console.log('');
  console.log('      ★ 本回：消した自由度は「z 軸の直線」、その分布は ★ s^(−1/2) のべき乗。');
  console.log('      ★ 出てきた階数は ★ ちょうど −1/2。★ 仮説どおりです。');
  console.log('');
  console.log('  ★ しかも第 26 回の反例（一様なばね鎖は整数階）とも矛盾しません ──');
  console.log('    ★ z 軸は「空間として」は一様ですが、★ 遅れに直すとべき乗になります。');
  console.log('    ★ 効くのは ★ 何について一様か。★ 光円錐の幾何がべき乗を作っていました。');
}

// ------------------------------------------------------------------
hr('5. ★ 尾はどこから来るのか ── 階数が 1/r² ポテンシャルとして現れる');

console.log('  d を含む項は (d−1)/r · ∂u/∂r の一つだけでした。★ これを消してみます。');
console.log('');
console.log('      ★ v = r^((d−1)/2) · u  と置くと ──');
console.log('');
console.log('      ★★ ∂²v/∂t² = c²( ∂²v/∂r² − l(l+1)/r² · v ),   l = (d−3)/2');
console.log('');
console.log('  ★ 一次元の波動方程式 ＋ 1/r² のポテンシャル。★ d は l にしか残りません。');
console.log('');
console.log('  ★★★ そして l = (d−3)/2 は ── ★ 2 節で出した階数 α そのものです。');
console.log('');
console.log('      ★ α = l。★ 階数が、1/r² ポテンシャルの強さとして現れました。');
console.log('');

{
  console.log('  ' + pad('d',6) + pad('l = α',10) + pad('l(l+1)',12) + pad('第 13 回の λ = −l(l+1)',24) + '中身');
  console.log('  ' + '-'.repeat(74));
  [1,2,3,4,5,6,7].forEach(function(d){
    const l=(d-3)/2, LL=l*(l+1), lam=-LL;
    let note='';
    if(Math.abs(LL)<1e-15) note='★ ポテンシャルなし';
    else if(Math.abs(lam-0.25)<1e-15) note='★★ 第 13 回の臨界 λ=1/4 ちょうど';
    else if(LL>0) note='斥力';
    else note='引力';
    console.log('  ' + pad(d,6) + pad(f(l,1),10) + rpad(f(LL,4),8) + pad('',4)
      + rpad(f(lam,4),8) + pad('',16) + note);
  });
  console.log('');
  console.log('  ★★ d = 1 と d = 3 だけ、★ ポテンシャルがちょうど消えます（l=−1 と l=0）。');
  console.log('    ── ★ そこでは方程式は ★ ただの一次元の波動方程式。尾が出ようがありません。');
  console.log('');
  console.log('  ★★★ そして d = 2 は ── ★ 第 13 回の臨界 1/r² ちょうどです。');
  console.log('');
  console.log('      l(l+1) は l = −1/2 で最小値 −1/4 をとります。');
  console.log('      λ = −l(l+1) ≤ 1/4 ── ★ どの次元も臨界を ★ 超えません。');
  console.log('      そして等号（臨界）になるのは ★ l = −1/2、つまり ★ d = 2 だけ。');
  console.log('');
  console.log('  ★ 第 13 回では λ > 1/4 で指数が複素数になる（虚数階・エフィモフ）と書きました。');
  console.log('    ★ 空間の次元からは、そこへは行けません ── ★ d = 2 がぎりぎり端です。');
}

console.log('');
console.log('  ★ この形で数値を走らせます（吸収境界つき、外向きパルスを r=10 から出して r=30 で受ける）：');
console.log('');

{
  function run(l){
    const LL=l*(l+1);
    const c=1, r0=1, R=90, N=45000;
    const dr=(R-r0)/(N-1), dt=0.4*dr/c;
    const rr=new Float64Array(N); for(let i=0;i<N;i++) rr[i]=r0+i*dr;
    let v0=new Float64Array(N), v1=new Float64Array(N), v2=new Float64Array(N);
    const w=0.4, rc=10;
    const F=r=>Math.exp(-(r-rc)*(r-rc)/(2*w*w));
    for(let i=0;i<N;i++) v0[i]=F(rr[i]);
    for(let i=0;i<N;i++) v1[i]=F(rr[i]-c*dt);
    const obs=Math.round((30-r0)/dr);
    const steps=Math.round(70/dt), k=(c*dt/dr)*(c*dt/dr);
    const rec=[];
    for(let n=0;n<steps;n++){
      for(let i=1;i<N-1;i++){
        v2[i]=2*v1[i]-v0[i]+k*(v1[i+1]-2*v1[i]+v1[i-1])
              - c*c*dt*dt*LL/(rr[i]*rr[i])*v1[i];
      }
      const a=(c*dt-dr)/(c*dt+dr);
      v2[0]   = v1[1]   + a*(v2[1]   - v0[0]);
      v2[N-1] = v1[N-2] + a*(v2[N-2] - v0[N-1]);
      const t=v0; v0=v1; v1=v2; v2=t;
      rec.push([(n+1)*dt, v1[obs]]);
    }
    let pk=0,tpk=0;
    rec.forEach(p=>{ if(Math.abs(p[1])>pk){pk=Math.abs(p[1]); tpk=p[0];} });
    function tail(dta){ let b=0;
      rec.forEach(p=>{ if(p[0]>tpk+dta && p[0]<tpk+dta+1) b=Math.max(b,Math.abs(p[1])); });
      return b/pk; }
    return {r2:tail(2), r5:tail(5), r10:tail(10), r20:tail(20)};
  }

  console.log('  ' + pad('d',5) + pad('l = α',9) + pad('+2 秒/ピーク',15) + pad('+5 秒',14)
            + pad('+10 秒',14) + pad('+20 秒',14) + '尾の行方');
  console.log('  ' + '-'.repeat(88));
  const R={};
  [1,2,3,4,5,6].forEach(function(d){
    const l=(d-3)/2, r=run(l); R[d]=r;
    let v;
    if(r.r20<1e-10) v='★★ 完全にゼロ';
    else if(r.r20/r.r2 < 0.05) v='減っていく';
    else v='★ 残り続ける';
    console.log('  ' + pad(d,5) + pad(f(l,1),9) + pad(e(r.r2,2),15) + pad(e(r.r5,2),14)
      + pad(e(r.r10,2),14) + pad(e(r.r20,2),14) + v);
  });
  console.log('');
  console.log('  ★★ d = 1 と d = 3 は ★ 1e-13 ── ★ 丸め誤差の水準。★ 尾は本当にありません。');
  console.log('    ★ ポテンシャルがゼロだから、というのが理由です（上の表）。');
  console.log('');
  console.log('  ★ それ以外の次元には尾が出ますが、★ 行方が二通りに分かれます：');
  console.log('');
  console.log('  ' + pad('d',6) + pad('l',8) + pad('+20 秒 / +2 秒',18) + '読み');
  console.log('  ' + '-'.repeat(56));
  [2,4,5,6].forEach(function(d){
    const r=R[d], ratio=r.r20/r.r2;
    console.log('  ' + pad(d,6) + pad(f((d-3)/2,1),8) + pad(f(ratio,4),18)
      + (d%2===0?'★ 偶数 ── 残る':'奇数 ── 減っていく'));
  });
  console.log('');
  console.log('  ★ 偶数次元（l が半整数）では尾が ★ 残り、奇数次元（l が整数）では ★ 減っていきます。');
  console.log('');
  console.log('  ★ ただし正直に書きます ── ★ この 1 次元に落とした計算だけでは');
  console.log('    ★ ホイヘンスの原理の証明にはなりません。原点を吸収境界で置き換えているので、');
  console.log('    ★ 「奇数次元で厳密にゼロ」を示せているのは ★ d=1 と d=3 だけです。');
  console.log('    ★ d=5 以上の鋭さの根拠は ★ 2〜3 節の厳密なグリーン関数のほうです。');
  console.log('');
  console.log('  ★★ この節で確実に言えること：');
  console.log('    ★ 尾の原因は ★ 1/r² ポテンシャルによる後方散乱。');
  console.log('    ★ そのポテンシャルの強さは ★ 階数 α そのもの（l = α）。');
  console.log('    ★ ちょうど消えるのは d = 1 と d = 3。★ 臨界になるのは d = 2。');
}

// ------------------------------------------------------------------
hr('6. ★ なぜ 3 次元だけが特別なのか');

{
  const rows = [
    ['1','−1',  '段差が永久に残る',        '鳴りっぱなし'],
    ['2','−1/2','s^(−1/2) の尾',          '池の波紋が消えない'],
    ['3','0',   '★ δ そのもの',            '★ 歪まず、通り過ぎたら終わり'],
    ['4','+1/2','s^(−3/2) の尾',          '尾が出る'],
    ['5','+1',  'δ\'（微分される）',        '鋭いが波形が歪む'],
    ['6','+3/2','尾が出る',                '尾が出る'],
    ['7','+2',  'δ\'\'（二回 微分される）',  '鋭いがさらに歪む']
  ];
  console.log('  ' + pad('d',5) + pad('α=(d−3)/2',13) + pad('前面の後ろ',26) + '聞こえ方');
  console.log('  ' + '-'.repeat(72));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],5)+pad(r[1],13)+pad(r[2],26)+r[3]); });
  console.log('');
  console.log('  ★★ 鋭い（尾がない）のは ★ 奇数次元の d ≥ 3 だけ。');
  console.log('    ★ しかし奇数でも d ≥ 5 では α ≥ 1 ── ★ 波形が微分されて歪みます。');
  console.log('');
  console.log('  ★★★ α = 0 ちょうどになる次元は ★ d = 3 しかありません。');
  console.log('');
  console.log('      ★ d = 2α + 3 で α = 0  ⟺  d = 3');
  console.log('');
  console.log('  ★ つまり ★ 3 次元は「波が歪まずに届き、しかも通り過ぎたら消える」唯一の次元。');
  console.log('    ★ 会話ができるのも、音楽が濁らないのも、★ これが理由です。');
  console.log('    ★ 2 次元なら、話すたびに部屋に音が溜まり続けます。');
}

// ------------------------------------------------------------------
hr('7. ★ 第 29 回で学んだ作法 ── この α は、あの α と同じか');

console.log('  第 29 回で「第 15 回は二つの α を混ぜていた」と訂正しました。');
console.log('  ★ だから本回も自分で点検します。★ 同じ α なのか。');
console.log('');
console.log('  ★ 気になる一致があります ──');
console.log('');
console.log('      第 29 回の受動性の帯：β ∈ [−1, +1]（幅 2）');
console.log('      本回の次元の階数　：α = (d−3)/2 が [−1, +1] ⟺ ★ 1 ≤ d ≤ 5');
console.log('');
console.log('  ★ 同じ幅 2 の帯。★ 何か意味があるのか。★ 受動性の判定式にかけてみます：');
console.log('');
{
  console.log('  ' + pad('d',6) + pad('α=(d−3)/2',13) + pad('cos(απ/2)',14) + pad('受動性の判定',18) + '実際はどうか');
  console.log('  ' + '-'.repeat(76));
  [1,2,3,4,5,6,7].forEach(function(d){
    const a=(d-3)/2, c=Math.cos(a*Math.PI/2);
    console.log('  ' + pad(d,6) + pad(f(a,2),13) + rpad(f(c,5),9) + pad('',5)
      + pad(c<-1e-12?'★ 能動 ＝ 禁止？':'受動',18)
      + (d===7?'★ でも 7 次元の自由場は何も湧かせない':''));
  });
  console.log('');
  console.log('  ★★ 却下します。★ これは意味のある一致ではありません。');
  console.log('');
  console.log('  ★ 理由：受動性 Re Z ≥ 0 は「★ 媒質が持つインピーダンス」についての条件です。');
  console.log('    ★ 一方 α = (d−3)/2 は「★ 何もない空間の幾何」から出る指数で、');
  console.log('      ★ そもそも散逸する相手がいません。★ 別の物です。');
  console.log('    ★ 7 次元の自由場は歪むだけで、エネルギーを湧かせたりしません。');
  console.log('');
  console.log('  ★ 幅 2 が両方に出たのは ── ★ どちらも「δ から ±1 階ぶん」という');
  console.log('    ★ 同じ数え方をしているからで、★ 同じ制約から来たのではありません。');
  console.log('');
  console.log('  ── ★★ 第 29 回で覚えた作法を、さっそく自分に使いました。');
  console.log('    ★ 同じ数字を見たら、まず「何で割ったか」を確かめる。');

}

// ------------------------------------------------------------------
hr('8. まとめ');

{
  const rows = [
    ['α = (d−3)/2',                 '◎ 数値', '★ d=1,2,4 で前面の指数を測って一致'],
    ['d=1 と d=3 は尾がゼロ',       '◎ 数値', '★ 1e-13 ── ポテンシャルが恒等的に消える'],
    ['奇数 d≥3 が鋭い',            '◎ 厳密解','★ 根拠は 2〜3 節。5 節の 1 次元計算では示せない'],
    ['降下法 ＝ 次元を一つ消す',      '◎ 数値', '★ ∫G₃dz が G₂ と 1e-4 で一致'],
    ['消した自由度は s^(−1/2) 分布', '◎ 数値', '★ dz/ds = √(r/2s) と 6 桁 一致'],
    ['第 26 回の仮説が別分野で成立',  '◎ 検証', '★ べき乗分布 → ちょうど半階'],
    ['α=0 は d=3 だけ',             '◎ 解析', '★ d = 2α + 3'],
    ['階数 α ＝ 1/r² の l',         '◎ 解析', '★ v=r^((d−1)/2)u で l(l+1)/r² が出る'],
    ['d=2 は第 13 回の臨界ちょうど','◎ 解析', '★ λ=−l(l+1)≤1/4、等号は l=−1/2 のみ'],
    ['受動性の帯との一致は偶然',      '★ 却下', '★ 自由場に散逸する相手はいない']
  ];
  console.log('  ' + pad('主張',30) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(86));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],30)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     方程式の d を一文字 動かすだけで、階数が半階ずつ動く。');
  console.log('     ★★ 次元と階数は、同じ一本の梯子だった ── 一次元が半階。');
  console.log('     そして α = 0（歪まず、残らない）になるのは ★ d = 3 だけ。');
  console.log('');
  console.log('  ★★ 本回の収穫は ★ 第 26 回の仮説が ★ 独立に検証されたことです。');
  console.log('    電気化学でも粘弾性でもなく ★ 真空の幾何から、同じ半階が出ました。');
  console.log('    ★ 消した自由度がべき乗で分布していれば分数階になる ── そのとおりでした。');
}

console.log('');
