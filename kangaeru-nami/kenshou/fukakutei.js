// 不確定性原理は、帯域幅定理に ħ を掛けただけである
'use strict';
const E=x=>x.toExponential(3);
const hbar=1.054571817e-34, h=6.62607015e-34;
const eV=1.602176634e-19, c=2.99792458e8;

// ===== FFT =====
function fft(re,im,inv){
  const n=re.length;
  for(let i=1,j=0;i<n;i++){let b=n>>1;for(;j&b;b>>=1)j^=b;j^=b;
    if(i<j){[re[i],re[j]]=[re[j],re[i]];[im[i],im[j]]=[im[j],im[i]];}}
  for(let len=2;len<=n;len<<=1){
    const ang=2*Math.PI/len*(inv?1:-1), wr=Math.cos(ang), wi=Math.sin(ang);
    for(let i=0;i<n;i+=len){let cr=1,ci=0;
      for(let j=0;j<len/2;j++){
        const ur=re[i+j],ui=im[i+j];
        const vr=re[i+j+len/2]*cr-im[i+j+len/2]*ci, vi=re[i+j+len/2]*ci+im[i+j+len/2]*cr;
        re[i+j]=ur+vr;im[i+j]=ui+vi;re[i+j+len/2]=ur-vr;im[i+j+len/2]=ui-vi;
        const nc=cr*wr-ci*wi;ci=cr*wi+ci*wr;cr=nc;}}}
  if(inv)for(let i=0;i<n;i++){re[i]/=n;im[i]/=n;}
}

console.log('##################################################################');
console.log('# 1. 純粋にフーリエの定理 ── 量子力学はまだ出てこない');
console.log('##################################################################\n');
console.log('  どんな波でも、時間幅と周波数幅を同時に狭くはできません：\n');
console.log('      Δt · Δω  ≥  1/2          （ガボールの限界）\n');
console.log('  これは信号処理の定理で、物理とは何の関係もありません。');
console.log('  「短いパルスは、必ず広い帯域を持つ」というだけ。\n');
console.log('  実際に測ります。いろいろな波形を作って、標準偏差を計算します。');

// 標準偏差（強度 |f|² を重みとする）
function moments(arr, dx){
  let s=0, m1=0, m2=0;
  for(let i=0;i<arr.length;i++){ const w=arr[i]*arr[i]; s+=w; m1+=w*i*dx; }
  m1/=s;
  for(let i=0;i<arr.length;i++){ const w=arr[i]*arr[i]; m2+=w*Math.pow(i*dx-m1,2); }
  return Math.sqrt(m2/s);
}
const N=1<<16, dt=1e-3, T=N*dt;
const dw=2*Math.PI/T;
function spec(sig){
  const re=Float64Array.from(sig), im=new Float64Array(N);
  fft(re,im,false);
  // 角周波数を中心化した配列にする
  const a=new Float64Array(N);
  for(let k=0;k<N;k++){ const kk=k<N/2?k+N/2:k-N/2; a[kk]=Math.hypot(re[k],im[k]); }
  return a;
}
function sigmaW(sig){
  const a=spec(sig);
  return moments(a, dw);
}
const t0=N*dt/2;
const shapes=[
  ['ガウス（σ=1）',      i=>Math.exp(-Math.pow(i*dt-t0,2)/2)],
  ['ガウス（σ=3）',      i=>Math.exp(-Math.pow(i*dt-t0,2)/18)],
  ['方形（幅 4）',       i=>(Math.abs(i*dt-t0)<2?1:0)],
  ['両側指数（τ=1）',    i=>Math.exp(-Math.abs(i*dt-t0))],
  ['三角（幅 4）',       i=>Math.max(0,1-Math.abs(i*dt-t0)/2)],
];
console.log('\n  波形                  Δt          Δω          Δt·Δω     判定');
console.log('  '+'-'.repeat(72));
for(const [nm,f] of shapes){
  const sig=new Float64Array(N);
  for(let i=0;i<N;i++) sig[i]=f(i);
  const st=moments(sig, dt), sw=sigmaW(sig);
  const p=st*sw;
  console.log(`  ${nm.padEnd(20)} ${st.toFixed(4).padStart(8)}    ${sw.toFixed(4).padStart(8)}    ${p.toFixed(4).padStart(7)}   ${p<0.51?'★ 最小（ガウス）':''}`);
}
console.log('\n  ★ ガウス波形だけが 0.5 に達し、他は必ずそれより大きい。');
console.log('    これがガボールの限界です ── 波である限り、逃れられない。');
console.log('');
console.log('  ※ 方形パルスの 30.4 は、実は発散しています。');
console.log('    sinc スペクトルの裾が 1/ω でしか落ちないので、分散積分が収束しない ──');
console.log('    「角が立った波形は、帯域が無限に広がる」という、別の言い方の同じ事実です。');

console.log('\n##################################################################');
console.log('# 2. ここで ħ を掛ける');
console.log('##################################################################\n');
console.log('  量子力学が言うのは、たった二つの対応です：\n');
console.log('      E = ħω        （エネルギー ＝ 時間周波数 × ħ）');
console.log('      p = ħk        （運動量   ＝ 空間周波数 × ħ）\n');
console.log('  これを帯域幅定理に代入するだけで：\n');
console.log('      Δt·Δω ≥ 1/2    →    Δt·ΔE ≥ ħ/2');
console.log('      Δx·Δk ≥ 1/2    →    Δx·Δp ≥ ħ/2\n');
console.log('  ★ 不確定性原理の中身は、フーリエの定理です。');
console.log('    ħ がやっているのは「波の単位」を「粒子の単位」に換算することだけ。\n');
const rates=[
  ['c',   '空間 ↔ 時間',     'm/s',     '第 4 回。定義値'],
  ['ħ',   '波 ↔ 粒子',       'J·s',     '★ 本回。定義値（2019〜）'],
  ['k_B', '温度 ↔ エネルギー', 'J/K',     '定義値（2019〜）'],
];
console.log('  定数    何を換算するか       単位      備考');
console.log('  '+'-'.repeat(66));
for(const [a,b,d,e] of rates) console.log(`  ${a.padEnd(6)} ${b.padEnd(18)} ${d.padEnd(9)} ${e}`);
console.log('\n  ★ 三つとも「換算レート」で、三つとも定義値になりました。');
console.log('    第 4 回の「次元付きは帳簿」が、ここでも効いています。');

console.log('\n##################################################################');
console.log('# 3. よくある誤解 ── 測定の擾乱ではない');
console.log('##################################################################\n');
const myth=[
  ['測定が乱すから',      '×', 'ハイゼンベルクの顕微鏡は直感的説明だが、本質ではない'],
  ['装置が不完全だから',  '×', '完璧な装置でも、波である限り成り立つ'],
  ['★ 波だから',        '○', '第 1 節で、量子力学抜きに実測した'],
];
console.log('  説明                 正誤   理由');
console.log('  '+'-'.repeat(76));
for(const [a,b,d] of myth) console.log(`  ${a.padEnd(20)} ${b}     ${d}`);
console.log('\n  ★ 証拠：第 1 節の計算に ħ は一度も出てきません。');
console.log('    音でも水面波でも電波でも、同じ不等式が成り立ちます。');
console.log('    ── 量子力学が加えたのは「粒子もまた波である」という一点だけ。');

console.log('\n##################################################################');
console.log('# 4. 実測との照合 ── 自然幅');
console.log('##################################################################\n');
console.log('  励起状態の寿命 τ は、そのままスペクトル線の幅になります：\n');
console.log('      Γ = ħ/τ        （自然幅）\n');
console.log('  これは帯域幅定理そのものです ── 有限時間しか続かない波は、幅を持つ。\n');
const lines=[
  ['水素 2p → 1s',    1.6e-9,      10.2,      'ライマン α'],
  ['ナトリウム D 線',  16e-9,       2.1,       '黄色の街灯'],
  ['Fe-57（メスバウアー）', 141e-9,  14.4e3,   '★ 核の遷移'],
  ['ルビジウム時計',   30e-9,       1.6,       ''],
];
console.log('  遷移                  寿命 τ [s]    エネルギー [eV]   Γ [eV]        Γ/E');
console.log('  '+'-'.repeat(86));
for(const [nm,tau,Ee,note] of lines){
  const G=hbar/tau/eV;
  console.log(`  ${nm.padEnd(20)} ${E(tau)}    ${E(Ee).padStart(9)}    ${E(G)}   ${E(G/Ee)}   ${note}`);
}
console.log('\n  ★ Fe-57 の Γ/E = 3×10⁻¹³ ── これがメスバウアー効果の分解能です。');
console.log('    「反跳なしで γ 線を吸収させる」と、この幅がそのまま使える。\n');
const g=9.80665, hgt=22.5;
const zGrav=g*hgt/(c*c);
const Gfe=hbar/141e-9/eV/14.4e3;
console.log('  そして 1959 年、パウンド＝レブカはこれで重力赤方偏移を測りました：\n');
console.log(`    高さ ${hgt} m での重力赤方偏移 = gh/c² = ${E(zGrav)}`);
console.log(`    Fe-57 の自然幅（相対） = ${E(Gfe)}`);
console.log(`    → 線幅の ${(zGrav/Gfe*100).toFixed(2)} % のずれを検出する必要がある\n`);
console.log('  ★ 線幅より小さいずれでも、線の「中心」なら測れます。');
console.log('    （山の頂上の位置は、山の幅より精密に決められる）');
console.log('    ── 帯域幅定理が決めるのは幅であって、中心の精度ではない。');

console.log('\n##################################################################');
console.log('# 5. 交換関係も、フーリエ共役そのもの');
console.log('##################################################################\n');
console.log('  x で掛ける操作と、d/dx を取る操作の順番を入れ替えると：\n');
console.log('      [x, d/dx] f = x·f′ − (x f)′ = x f′ − f − x f′ = −f\n');
console.log('  つまり [x, d/dx] = −1。ここに p = −iħ d/dx を入れると：\n');
console.log('      [x, p] = iħ\n');
console.log('  ★ 交換関係は「位置と空間周波数はフーリエ共役」の言い換えでした。');
console.log('    ħ はここでも、単位を合わせているだけです。\n');
const pairs=[
  ['時間 t',   '角周波数 ω',  'エネルギー E = ħω',   'ΔtΔE ≥ ħ/2'],
  ['位置 x',   '波数 k',      '運動量 p = ħk',       'ΔxΔp ≥ ħ/2'],
  ['角度 φ',   '整数 m',      '角運動量 L = ħm',     'ΔφΔL ≥ ħ/2（周期性で微妙）'],
];
console.log('  変数        共役な変数     物理量               不等式');
console.log('  '+'-'.repeat(76));
for(const [a,b,d,e] of pairs) console.log(`  ${a.padEnd(10)} ${b.padEnd(12)} ${d.padEnd(20)} ${e}`);

console.log('\n##################################################################');
console.log('# 6. 「ΔEΔt」だけは、実は毛色が違う');
console.log('##################################################################\n');
console.log('  ★ ここは注意が要ります。');
console.log('    位置と運動量は両方とも「演算子」ですが、時間は演算子ではありません。\n');
const caveat=[
  ['ΔxΔp ≥ ħ/2',  '両方とも演算子',   '交換関係から厳密に導ける'],
  ['ΔEΔt ≥ ħ/2',  '時間は演算子でない','★ 意味を与えるには解釈が要る'],
];
console.log('  不等式            状況              性質');
console.log('  '+'-'.repeat(70));
for(const [a,b,d] of caveat) console.log(`  ${a.padEnd(16)} ${b.padEnd(18)} ${d}`);
console.log('\n  ΔEΔt の「Δt」が意味するのは、たとえば：');
console.log('    ・状態が変化するのにかかる時間（マンデルシュタム＝タム）');
console.log('    ・励起状態の寿命（第 4 節の自然幅）');
console.log('    ・測定に費やした時間\n');
console.log('  ★ 波の言葉（第 1 節）では、時間も周波数も対等な軸です。');
console.log('    量子力学に移すと、片方だけが演算子になって非対称が生まれる ──');
console.log('    これは「波として見る」視点が、量子力学より広いことの現れです。');

console.log('\n##################################################################');
console.log('# 7. 最小不確定の波形は、なぜガウスか');
console.log('##################################################################\n');
console.log('  第 1 節でガウスだけが 0.5 に達しました。理由は簡単です：\n');
console.log('      ガウス関数のフーリエ変換は、ガウス関数である\n');
console.log('  つまり時間側と周波数側で「同じ形」になる ── 対称性が最大。\n');
console.log('  実際に確かめます（σ を変えて、両側の幅を測る）：\n');
console.log('   σ_t（設定）   実測 Δt      実測 Δω      積      予言 1/2');
console.log('  '+'-'.repeat(66));
for(const s of [0.5,1,2,3,5]){
  const sig=new Float64Array(N);
  for(let i=0;i<N;i++) sig[i]=Math.exp(-Math.pow(i*dt-t0,2)/(2*s*s));
  const st=moments(sig,dt), sw=sigmaW(sig);
  console.log(`  ${s.toFixed(1).padStart(8)}   ${st.toFixed(5).padStart(9)}   ${sw.toFixed(5).padStart(9)}   ${(st*sw).toFixed(5)}   0.50000`);
}
console.log('\n  ★ σ をどう変えても、積はきっかり 0.5。');
console.log('    「片方を狭くすれば、必ず他方が同じだけ広がる」が数値で見えます。\n');
console.log('  ⇒ そして第 1 節に戻ると ── この 0.5 に ħ を掛けたものが、');
console.log('    ハイゼンベルクの不等式の右辺そのものでした。');

console.log('\n##################################################################');
console.log('# 8. まとめ');
console.log('##################################################################\n');
const summary=[
  ['ΔtΔω ≥ 1/2',     '◎ 実測',   'ガウスで 0.5、他は必ず大きい。量子力学 不要'],
  ['ΔtΔE ≥ ħ/2',     '○ 換算',   'E = ħω を代入するだけ'],
  ['ΔxΔp ≥ ħ/2',     '○ 換算',   'p = ħk を代入するだけ'],
  ['[x,p] = iħ',      '○ 同値',   'フーリエ共役の言い換え'],
  ['測定の擾乱が原因',  '× 誤解',   '第 1 節に ħ は出てこない'],
  ['ΔEΔt は特別',     '△ 注意',   '時間は演算子でない。解釈が要る'],
];
console.log('  主張                  判定       根拠');
console.log('  '+'-'.repeat(72));
for(const [a,b,d] of summary) console.log(`  ${a.padEnd(20)} ${b.padEnd(10)} ${d}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     不確定性原理は、波の性質に ħ という換算レートを掛けたものである。');
console.log('     驚くべきは不等式のほうではなく、');
console.log('     ★「粒子もまた波である」という一点のほうでした。');
