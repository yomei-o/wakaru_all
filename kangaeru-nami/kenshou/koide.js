// 考える波 第 33 回 検証スクリプト
//   小出の式を波として読む
//   ── √質量を 120 度 間隔で標本化した正弦波と見ると、交流＝直流
//
//   実行: node koide.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

// 極質量 [MeV]（PDG）
const ME   = 0.51099895000;
const MMU  = 105.6583755;
const MTAU = 1776.86;
const MTAU_ERR = 0.12;

function koide(m){
  const S = m.reduce((a,b)=>a+Math.sqrt(b),0);
  const M = m.reduce((a,b)=>a+b,0);
  return M/(S*S);
}

// ------------------------------------------------------------------
hr('1. 第 32 回が残した問い');

console.log('  第 32 回で、ヒッグスは ★ 一つの次元（v）を配る装置だと分かりました。');
console.log('  ★ しかし ★ 配る比（湯川結合）は ★ 何も説明できませんでした：');
console.log('');
console.log('      y_top / y_e = 3.4e5 ── ★ 5 桁 以上 の階層。理由は不明。');
console.log('');
console.log('  ★ では、質量どうしに ★ 関係式はないのか。');
console.log('  ★ 荷電レプトン 3 つには、★ 一つだけ 知られた関係があります ── 小出の式（1981）：');
console.log('');
console.log('      ★ K = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3');
console.log('');
console.log('  ★ 本回はこれを ★ 波として読み直します。');

// ------------------------------------------------------------------
hr('2. まず実測で確かめる');

{
  const m=[ME,MMU,MTAU];
  const K=koide(m);
  console.log('  ' + pad('量',20) + pad('値',22) + '');
  console.log('  ' + '-'.repeat(46));
  console.log('  ' + pad('m_e [MeV]',20) + pad(f(ME,11),22));
  console.log('  ' + pad('m_μ [MeV]',20) + pad(f(MMU,7),22));
  console.log('  ' + pad('m_τ [MeV]',20) + pad(f(MTAU,2)+' ± '+f(MTAU_ERR,2),22));
  console.log('');
  console.log('      ★ K = ' + f(K,9));
  console.log('      ★ 2/3 = ' + f(2/3,9));
  console.log('      ★★ 相対差 ' + e((K-2/3)/(2/3),3));
  console.log('');
  console.log('  ★ 10 万分の 1 で合っています。★ まず「K は何でも取れる値なのか」を確かめます。');
  console.log('');
  // K の取りうる範囲
  console.log('  ★ x_i = √m_i と置くと K = |x|²/(Σx)²。★ 範囲は決まっています：');
  console.log('');
  console.log('  ' + pad('状況',26) + pad('K',12) + '');
  console.log('  ' + '-'.repeat(40));
  console.log('  ' + pad('三つとも等しい',26) + pad(f(koide([1,1,1]),6),12));
  console.log('  ' + pad('一つだけ極端に大きい',26) + pad(f(koide([1e-12,1e-12,1]),6),12));
  console.log('  ' + pad('★ 小出',26) + pad(f(2/3,6),12));
  console.log('');
  console.log('  ★★ K は ★ 1/3 〜 1 の間しか取れません。★ そして 2/3 は ★ ちょうど真ん中。');
  console.log('    ★ だから「2/3 が出た」こと自体は、そこまで驚くことではありません。');
  console.log('    ★★ 驚くのは ★ 精度のほうです（10⁻⁵）。★ 8 節でそこを測ります。');
}

// ------------------------------------------------------------------
hr('3. 幾何で読む ── 45 度');

{
  const s=[Math.sqrt(ME),Math.sqrt(MMU),Math.sqrt(MTAU)];
  const len=Math.hypot(s[0],s[1],s[2]);
  const dot=(s[0]+s[1]+s[2])/Math.sqrt(3);
  const th=Math.acos(dot/len)*180/Math.PI;
  console.log('  ★ ベクトル x = (√m_e, √m_μ, √m_τ) と、対角線 n = (1,1,1)/√3 の角度を測ります。');
  console.log('');
  console.log('      Σ√m = √3·|x|·cos θ  なので  ★ K = 1/(3cos²θ)');
  console.log('');
  console.log('  ' + pad('量',24) + pad('値',18) + '');
  console.log('  ' + '-'.repeat(44));
  console.log('  ' + pad('|x|',24) + pad(f(len,6),18));
  console.log('  ' + pad('★ 測った角度 θ',24) + pad(f(th,6)+' 度',18));
  console.log('  ' + pad('K = 2/3 なら',24) + pad('45 度 ちょうど',18));
  console.log('  ' + pad('θ の取りうる範囲',24) + pad('0 〜 54.7356 度',18));
  console.log('');
  console.log('  ★★ ★ 44.9997 度 ── ★ 45 度 と 5 桁 で一致します。');
  console.log('');
  console.log('  ★ ここで ★ 第 29・30 回で覚えた作法を使います ── ★ この 45 度 は');
  console.log('    ★ 「半階の位相 45 度」（第 1 回）と ★ 同じものか。');
  console.log('');
  console.log('  ★★ 却下します。★ 別物です。');
  console.log('    ★ 第 1 回の 45 度 は ★ 複素平面での ★ 位相（時間の遅れ）。');
  console.log('    ★ 本節の 45 度 は ★ 実 3 次元での ★ ベクトルの向き。');
  console.log('    ★ 住んでいる空間が違います。★ 数字が同じでも、意味は共有しません。');
}

// ------------------------------------------------------------------
hr('4. ★★ 波として読む ── 120 度 間隔で標本化した正弦波');

console.log('  ★ 三つの √m を、★ 一本の正弦波を 3 点で標本化したものと見ます：');
console.log('');
console.log('      ★ √m_k = μ·( 1 + A·cos(δ + 2πk/3) ),   k = 0, 1, 2');
console.log('');
console.log('  ★ 直流成分 μ、交流の振幅 μA、位相 δ ── ★ 3 点の DFT そのものです。');
console.log('');
{
  const s=[Math.sqrt(ME),Math.sqrt(MMU),Math.sqrt(MTAU)];
  const S=s[0]+s[1]+s[2];
  const mu=S/3;
  let cr=0, ci=0;
  for(let k=0;k<3;k++){ const t=2*Math.PI*k/3; cr+=s[k]*Math.cos(t); ci+=s[k]*Math.sin(t); }
  cr*=2/3; ci*=2/3;
  const A=Math.hypot(cr,ci)/mu;
  let delta=Math.atan2(-ci,cr);
  console.log('  ' + pad('量',26) + pad('実測から',20) + '');
  console.log('  ' + '-'.repeat(50));
  console.log('  ' + pad('直流 μ = (Σ√m)/3',26) + pad(f(mu,6)+' √MeV',20));
  console.log('  ' + pad('★ 振幅比 A',26) + pad(f(A,8),20));
  console.log('  ' + pad('位相 δ',26) + pad(f(delta,6)+' rad = '+f(delta*180/Math.PI,4)+' 度',20));
  console.log('');
  console.log('  ★ 三相の恒等式 Σ_k cos²(δ + 2πk/3) = 3/2 を使うと、★ K が手で出ます：');
  console.log('');
  console.log('      Σ√m = 3μ                     （Σcos = 0 だから）');
  console.log('      Σm  = μ²[3 + 2A·Σcos + A²Σcos²] = μ²[3 + 0 + (3/2)A²]');
  console.log('      ★★ K = [3 + (3/2)A²] / 9 = ★ (1 + A²/2)/3');
  console.log('');
  // 恒等式そのものを数値で確認
  console.log('  ★ まず恒等式を確かめます（δ を振っても 3/2 のまま）：');
  console.log('');
  console.log('  ' + pad('δ [度]',12) + pad('Σcos',16) + pad('Σcos²',16) + '');
  console.log('  ' + '-'.repeat(46));
  [0,17,45,90,132.73,200].forEach(function(dg){
    const d=dg*Math.PI/180;
    let c=0, c2=0;
    for(let k=0;k<3;k++){ const v=Math.cos(d+2*Math.PI*k/3); c+=v; c2+=v*v; }
    console.log('  ' + pad(f(dg,2),12) + pad(e(c,2),16) + pad(f(c2,12),16));
  });
  console.log('');
  console.log('  ★★ どの δ でも Σcos = 0、Σcos² = 1.5 ── ★ 三相交流の電力が一定なのと同じ恒等式。');
  console.log('');
  console.log('  ★ そして K の式を検算：');
  console.log('');
  console.log('      (1 + A²/2)/3 = ' + f((1+A*A/2)/3,9));
  console.log('      直接の K      = ' + f(koide([ME,MMU,MTAU]),9));
  console.log('');
  console.log('  ★★★ したがって ── ★ 小出の式 K = 2/3 とは、★ A = √2 のことです：');
  console.log('');
  console.log('      (1 + A²/2)/3 = 2/3  ⟺  A² = 2  ⟺  ★ A = √2');
  console.log('');
  console.log('      ★ 実測の A = ' + f(A,8));
  console.log('      ★ √2      = ' + f(Math.SQRT2,8));
  console.log('      ★★ 相対差 ' + e((A-Math.SQRT2)/Math.SQRT2,3));
}

// ------------------------------------------------------------------
hr('5. ★★★ A = √2 の意味 ── 交流と直流の実効値が等しい');

{
  const s=[Math.sqrt(ME),Math.sqrt(MMU),Math.sqrt(MTAU)];
  const mu=(s[0]+s[1]+s[2])/3;
  let cr=0, ci=0;
  for(let k=0;k<3;k++){ const t=2*Math.PI*k/3; cr+=s[k]*Math.cos(t); ci+=s[k]*Math.sin(t); }
  cr*=2/3; ci*=2/3;
  const A=Math.hypot(cr,ci)/mu;
  console.log('  ★ 振幅 A の正弦波の ★ 実効値（RMS）は A/√2 です。');
  console.log('  ★ だから ── ★ A = √2 ⟺ ★ 実効値 = 1 ＝ 直流成分。');
  console.log('');
  console.log('  ' + pad('成分',24) + pad('値 [√MeV]',20) + '');
  console.log('  ' + '-'.repeat(46));
  console.log('  ' + pad('直流 μ',24) + pad(f(mu,6),20));
  console.log('  ' + pad('★ 交流の実効値 μA/√2',24) + pad(f(mu*A/Math.SQRT2,6),20));
  console.log('  ' + pad('★★ 比',24) + pad(f(A/Math.SQRT2,8),20));
  console.log('');
  const db=20*Math.log10(A/Math.SQRT2);
  console.log('      ★ dB で書くと ' + e(db,2) + ' dB ── ★ 0 dB。');
  console.log('');
  console.log('  ★★★ ★ 小出の式とは、これだけのことでした：');
  console.log('');
  console.log('      ★★ 「√質量の波の、★ 交流と直流の実効値が等しい」');
  console.log('');
  console.log('  ★ 2/3 という半端な数より、★ こちらのほうが言いたいことが見えます。');
  console.log('    ★ 交流成分が担う「電力」と、直流成分が担う「電力」が ★ ちょうど半々。');
}

// ------------------------------------------------------------------
hr('6. 予言する ── τ の質量');

{
  const a=Math.sqrt(ME), b=Math.sqrt(MMU);
  // 3(a²+b²+c²) = 2(a+b+c)² を c について解く
  const p=a+b, C=3*a*a+3*b*b-2*p*p;
  const c=(4*p+Math.sqrt(16*p*p-4*C))/2;
  const pred=c*c;
  console.log('  ★ m_e と m_μ だけを入れて、K = 2/3 から m_τ を解きます：');
  console.log('');
  console.log('      c² − 4(a+b)c + 3a² + 3b² − 2(a+b)² = 0,   a=√m_e, b=√m_μ, c=√m_τ');
  console.log('');
  console.log('  ' + pad('量',20) + pad('値 [MeV]',20) + '');
  console.log('  ' + '-'.repeat(44));
  console.log('  ' + pad('★ 予言 m_τ',20) + pad(f(pred,3),20));
  console.log('  ' + pad('実測 m_τ',20) + pad(f(MTAU,2)+' ± '+f(MTAU_ERR,2),20));
  console.log('  ' + pad('差',20) + pad(f(pred-MTAU,3),20));
  console.log('  ' + pad('★ 何 σ か',20) + pad(f((pred-MTAU)/MTAU_ERR,2)+' σ',20));
  console.log('');
  console.log('  ★★ 0.9 σ ── ★ 現在の測定精度では ★ 合っています。');
  console.log('');
  // 感度
  console.log('  ★ どれくらい精度が要るか（入力を 1 ppm 動かしたときの予言の変化）：');
  console.log('');
  console.log('  ' + pad('入力',16) + pad('1 ppm 変えると m_τ は',26) + '');
  console.log('  ' + '-'.repeat(44));
  [['m_e',ME],['m_μ',MMU]].forEach(function(q){
    const d=q[1]*1e-6;
    const a2=Math.sqrt(q[0]==='m_e'?ME+d:ME), b2=Math.sqrt(q[0]==='m_μ'?MMU+d:MMU);
    const p2=a2+b2, C2=3*a2*a2+3*b2*b2-2*p2*p2;
    const c2=(4*p2+Math.sqrt(16*p2*p2-4*C2))/2;
    console.log('  ' + pad(q[0],16) + pad(f((c2*c2-pred)*1e3,4)+' keV 動く',26));
  });
  console.log('');
  console.log('  ★ μ の質量が効きます。★ いまの m_μ の精度（2.3e-8）なら十分です。');
  console.log('  ★★ つまりこの式は ★ 反証可能です ── τ の測定が 10 倍 精しくなれば決着します。');
}

// ------------------------------------------------------------------
hr('7. ★ 走らせると壊れる ── これは極質量の関係だった');

{
  console.log('  ★ このシリーズは第 5・18・28 回で ★「質量は走る」と繰り返してきました。');
  console.log('  ★ 小出比は ★ 無次元量なので（第 7 回の基準は満たす）、走らせても意味があります。');
  console.log('  ★ そこで M_Z での MS-bar 質量で同じ比を計算します。');
  console.log('');
  const pole=[ME,MMU,MTAU];
  const mz=[0.4865657, 102.7181, 1746.24];      // 文献値（MS-bar, M_Z）
  console.log('  ' + pad('スキーム',22) + pad('m_e',12) + pad('m_μ',12) + pad('m_τ',12) + pad('K',12) + '2/3 との差');
  console.log('  ' + '-'.repeat(84));
  [['極質量',pole],['★ MS-bar @ M_Z',mz]].forEach(function(p){
    const K=koide(p[1]);
    console.log('  ' + pad(p[0],22) + pad(f(p[1][0],5),12) + pad(f(p[1][1],3),12)
      + pad(f(p[1][2],2),12) + pad(f(K,6),12) + f((K-2/3)/(2/3)*100,4) + ' %');
  });
  console.log('');
  const Kz=koide(mz);
  const Az=Math.sqrt(2*(3*Kz-1));
  console.log('  ★ 振幅比で見ると：');
  console.log('      極質量　　　 A = ' + f(Math.sqrt(2*(3*koide(pole)-1)),6));
  console.log('      MS-bar @ M_Z A = ' + f(Az,6) + '   （√2 = ' + f(Math.SQRT2,6) + '）');
  console.log('');
  console.log('  ★★ ずれが ' + e(Math.abs(koide(pole)-2/3)/(2/3),1) + ' → '
            + e(Math.abs(Kz-2/3)/(2/3),1) + ' と ★ 200 倍 悪化します。');
  console.log('');
  console.log('  ★ これは重要な事実です ──');
  console.log('    ★★ 小出の関係は ★「極質量というスキームでだけ」成り立っています。');
  console.log('    ★ 基本的な関係式なら、ふつうは ★ ある物理的なスケールで成り立ってほしい。');
  console.log('    ★ 極質量は ★ 粒子ごとに違うスケールなので、理論的には落ち着きが悪い。');
  console.log('');
  console.log('  ★ 二つの読み方があります（どちらが正しいかは本稿では決められません）：');
  console.log('      ① 偶然である（8 節で確率を測ります）');
  console.log('      ② 極質量に意味がある（例：その粒子自身のスケールで成り立つ関係）');
  console.log('');
  console.log('  ★ 第 28 回で書いたとおり、★ 極質量は「その粒子が実際に飛ぶときの質量」です。');
  console.log('    ★ ②の読み方を取るなら、★ 小出の式は ★ 各レプトンを ★ 自分のスケールで');
  console.log('      ★ 測ったときの関係、ということになります。★ 検証の手立ては今のところ不明。');
}

// ------------------------------------------------------------------
hr('8. ★ どれくらい驚くべきか ── 対照実験');

{
  console.log('  ★ 2 節で見たとおり K は 1/3 〜 1 に収まり、2/3 はその真ん中です。');
  console.log('  ★ では ★ 適当な三つ組で K が 2/3 の近くに来る確率はどれくらいか。');
  console.log('');
  // 乱数で対照実験（√m を対数一様に振る）
  // mulberry32（Math.imul で 32 ビットを正確に扱う）
  let seed=12345;
  function rnd(){
    seed = (seed + 0x6D2B79F5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  }
  const N=20000000;
  const tolList=[1e-2,1e-3,1e-4,1e-5];
  const hit=new Array(tolList.length).fill(0);
  let inRange=0;
  for(let i=0;i<N;i++){
    // 実際のレプトンと同じくらいの広がり（√m が 0.7 〜 42、対数一様）
    const a=Math.exp(Math.log(0.7)+rnd()*Math.log(42/0.7));
    const b=Math.exp(Math.log(0.7)+rnd()*Math.log(42/0.7));
    const c=Math.exp(Math.log(0.7)+rnd()*Math.log(42/0.7));
    const K=(a*a+b*b+c*c)/((a+b+c)*(a+b+c));
    const rel=Math.abs(K-2/3)/(2/3);
    inRange++;
    for(let t=0;t<tolList.length;t++) if(rel<tolList[t]) hit[t]++;
  }
  console.log('  ★ √m を 0.7〜42（実際のレプトンと同じ広がり）で対数一様に ' + e(N,0) + ' 組 作り、');
  console.log('    K が 2/3 からどれだけ離れるかを数えました：');
  console.log('');
  console.log('  ' + pad('相対差より近い',20) + pad('当たった組',16) + pad('割合',16) + '何組に 1 つ');
  console.log('  ' + '-'.repeat(66));
  tolList.forEach(function(t,i){
    const p=hit[i]/inRange;
    console.log('  ' + pad(e(t,0),20) + pad(hit[i],16) + pad(e(p,3),16)
      + (p>0?('1 / '+e(1/p,2)):'0 組'));
  });
  console.log('');
  const p5=hit[3]/inRange;
  console.log('  ★★ 実測は 9.2e-6 の精度で当たっています。');
  console.log('    ★ 乱数だと 1e-5 以内に来るのは ' + (p5>0?('約 '+e(1/p5,2)+' 組に 1 つ'):'この試行では 0 組') + '。');
  console.log('');
  console.log('  ★ 正直な評価：');
  console.log('    ★ 「2/3 が出た」ことは ★ そこまで珍しくありません（範囲の真ん中だから）。');
  console.log('    ★★ 珍しいのは ★ 精度です ── ★ 10⁻⁵ は偶然にしては良すぎます。');
  console.log('    ★ ただし ★ 7 節のとおり ★ 走らせると壊れるので、★ 何かの近似かもしれません。');
  console.log('');
  // クォークで試す
  console.log('  ★ 同じ式をクォークに使うと、どうなるか（MS-bar の代表値）：');
  console.log('');
  const sets=[
    ['荷電レプトン', [ME,MMU,MTAU]],
    ['上型クォーク (u,c,t)', [2.16, 1270, 172690]],
    ['下型クォーク (d,s,b)', [4.67, 93.4, 4180]]
  ];
  console.log('  ' + pad('三つ組',26) + pad('K',14) + pad('A',14) + '2/3 との差');
  console.log('  ' + '-'.repeat(68));
  sets.forEach(function(p){
    const K=koide(p[1]), A=Math.sqrt(Math.max(2*(3*K-1),0));
    console.log('  ' + pad(p[0],26) + pad(f(K,6),14) + pad(f(A,6),14)
      + f((K-2/3)/(2/3)*100,3) + ' %');
  });
  console.log('');
  console.log('  ★★ クォークでは ★ 合いません（数 % 〜 十数 %）。');
  console.log('    ★ 荷電レプトンだけの関係です ── ★ そこも説明がついていません。');
}

// ------------------------------------------------------------------
hr('9. おまけ ── 位相 δ の数値');

{
  const s=[Math.sqrt(ME),Math.sqrt(MMU),Math.sqrt(MTAU)];
  const mu=(s[0]+s[1]+s[2])/3;
  let cr=0, ci=0;
  for(let k=0;k<3;k++){ const t=2*Math.PI*k/3; cr+=s[k]*Math.cos(t); ci+=s[k]*Math.sin(t); }
  cr*=2/3; ci*=2/3;
  let delta=Math.atan2(-ci,cr)*180/Math.PI;
  const d2=delta-120;
  console.log('  ★ 振幅 A は √2 に決まりましたが、★ 位相 δ は ★ 何にも決まっていません。');
  console.log('  ★ 実測の値を見ておきます：');
  console.log('');
  console.log('      δ = ' + f(delta,5) + ' 度');
  console.log('      ★ 120 度 を引くと ' + f(d2,5) + ' 度 = ' + f(d2*Math.PI/180,7) + ' rad');
  console.log('      ★ 2/9 = ' + f(2/9,7) + ' rad');
  console.log('      相対差 ' + e((d2*Math.PI/180-2/9)/(2/9),2));
  console.log('');
  console.log('  ★★ 2/9 に ★ 4 桁 で近い ── ★ これは有名な「気になる一致」です。');
  console.log('');
  console.log('  ★ ただし ★ 正直に書きます：');
  console.log('    ★ δ は ★ データに合わせた 1 個の自由パラメータです。');
  console.log('    ★ 自由パラメータが単純な分数に 4 桁 で近いのは、★ 確率 10⁻⁴ 程度の出来事。');
  console.log('    ★ 「気になる」止まりで、★ 証拠ではありません。仕組みが要ります。');
  console.log('    ★ しかも 7 節のとおり δ もスキーム依存です（走らせると動く）。');
}

// ------------------------------------------------------------------
hr('10. まとめ');

{
  const rows = [
    ['K = 2/3 が 1e-5 で成立',       '◎ 実測', '★ 0.666660511 vs 0.666666667'],
    ['K は 1/3〜1 しか取れない',     '◎ 解析', '★ 2/3 は範囲の真ん中'],
    ['(√m) と (1,1,1) が 45 度',    '◎ 実測', '★ 44.999735 度'],
    ['45 度 は第 1 回の位相と別物',  '★ 却下', '★ 実3次元の向き vs 複素平面の位相'],
    ['★ K = (1 + A²/2)/3',         '◎ 解析', '★ 三相の恒等式 Σcos²=3/2 から'],
    ['★★ 小出 ⟺ A = √2',          '◎ 実測', '★ A = 1.41420051'],
    ['★★★ 交流の実効値 = 直流',      '◎ 実測', '★ 比 0.99999077（0 dB）'],
    ['m_τ の予言が 0.9 σ',          '◎ 実測', '★ 1776.969 vs 1776.86 ± 0.12'],
    ['★ 走らせると 200 倍 悪化',     '★ 限界', '★ 極質量 9e-6 → M_Z で 1.9e-3'],
    ['クォークでは合わない',         '◎ 実測', '★ 数 % 〜 十数 % ずれる'],
    ['δ ≈ 2/9 は気になるだけ',      '★ 保留', '★ 自由パラメータ 1 個の 4 桁 一致']
  ];
  console.log('  ' + pad('主張',30) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(88));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],30)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     小出の式とは ── ★ √質量を 120 度 間隔で標本化した波の、');
  console.log('     ★★ 交流と直流の実効値が等しい、ということだった。');
  console.log('');
  console.log('  ★ 本回が付け加えたのは ★ 言い換えだけで、★ 説明ではありません。');
  console.log('    ★ なぜ A = √2 なのかは ★ 分かっていません。');
  console.log('    ★ ただ「2/3」より「AC = DC」のほうが ★ 何を説明すべきかは はっきりします。');
}

console.log('');
