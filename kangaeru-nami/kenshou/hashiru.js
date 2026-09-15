// 走る結合定数 ── 「定数は積分値」が、文字どおり正しい場所
'use strict';
const E=x=>x.toExponential(3);

const alpha0=7.2973525693e-3;      // α(0)、微細構造定数
const mZ=91187.6;                  // MeV
const leptons=[
  ['電子 e',   0.51099895],
  ['ミュー粒子 μ', 105.6583755],
  ['タウ粒子 τ',  1776.86],
];

console.log('##################################################################');
console.log('# 1. 「定数は積分値ではないか」── ここでは、文字どおり正しい');
console.log('##################################################################\n');
console.log('  これまでの回では、定数の時間微分を探して「見つからない」でした。');
console.log('  しかし ── 探す軸を間違えていました。\n');
console.log('  結合定数は、時間ではなく「エネルギー」について走ります。\n');
console.log('      α は定数ではない。α(μ) という関数である。');
console.log('      そして α(μ) は、ベータ関数の積分そのもの：\n');
console.log('        d α / d ln μ = β(α)');
console.log('        α(μ) = α(μ₀) + ∫ β(α) d ln μ        ★ 定数 ＝ 積分値\n');
console.log('  これは仮説ではなく、測定されている事実です。実際に計算します。');

console.log('\n##################################################################');
console.log('# 2. 一ループの真空偏極 ── なぜ走るのか');
console.log('##################################################################\n');
console.log('  電荷のまわりでは、真空が電子・陽電子対に分極します。');
console.log('  遠くから見ると遮蔽されて弱く、近づくほど裸の電荷が見えて強くなる。\n');
console.log('  QED の一ループの結果（レプトンのみ）：\n');
console.log('      Δα_lep(μ) = (α/3π) Σ_l [ ln(μ²/m_l²) − 5/3 ]\n');
console.log('      α(μ) = α(0) / (1 − Δα)\n');
const pref=alpha0/(3*Math.PI);
console.log(`  係数 α/3π = ${E(pref)}\n`);
console.log('  粒子           質量 [MeV]    ln(m_Z²/m_l²)   −5/3 込み    寄与 Δα');
console.log('  '+'-'.repeat(74));
let sumLog=0;
for(const [n,m] of leptons){
  const L=2*Math.log(mZ/m);
  const Lc=L-5/3;
  sumLog+=Lc;
  console.log(`  ${n.padEnd(14)} ${m.toFixed(4).padStart(11)}    ${L.toFixed(3).padStart(8)}      ${Lc.toFixed(3).padStart(8)}    ${E(pref*Lc)}`);
}
const dAlphaLep=pref*sumLog;
console.log('  '+'-'.repeat(74));
console.log(`  ${'合計'.padEnd(14)} ${''.padStart(11)}    ${''.padStart(8)}      ${sumLog.toFixed(3).padStart(8)}    ${E(dAlphaLep)}`);
console.log(`\n  ★ Δα_lep(m_Z) = ${dAlphaLep.toFixed(6)}`);
console.log('    文献値 0.031498 ── 一ループでここまで合います。');

console.log('\n##################################################################');
console.log('# 3. ハドロンの寄与 ── ここは計算できない');
console.log('##################################################################\n');
console.log('  クォークの寄与は、低エネルギーで強い相互作用が効くため');
console.log('  摂動論では計算できません。実験（e⁺e⁻ → ハドロン）から求めます。\n');
const dAlphaHad=0.02766;    // 文献値（5 フレーバー）
console.log(`  Δα_had⁽⁵⁾(m_Z) = ${dAlphaHad}   （実測。文献値）\n`);
const dAlpha=dAlphaLep+dAlphaHad;
console.log(`  合計 Δα = ${dAlphaLep.toFixed(6)} + ${dAlphaHad} = ${dAlpha.toFixed(6)}`);
const alphaZ=alpha0/(1-dAlpha);
console.log(`\n  α(m_Z) = ${alpha0.toExponential(6)} / (1 − ${dAlpha.toFixed(6)}) = ${alphaZ.toExponential(6)}`);
console.log(`  → 1/α(m_Z) = ${(1/alphaZ).toFixed(3)}`);
console.log(`\n  文献値（5 フレーバー QED）: 1/α(m_Z) ≈ 128.95`);
console.log(`  ★ 一致しました。`);

console.log('\n##################################################################');
console.log('# 4. これが答えです ── 定数が動いている');
console.log('##################################################################\n');
console.log('   エネルギー         1/α        α');
console.log('  '+'-'.repeat(50));
console.log(`  0（無限遠）        ${(1/alpha0).toFixed(3)}    ${E(alpha0)}`);
console.log(`  m_Z = 91.2 GeV    ${(1/alphaZ).toFixed(3)}    ${E(alphaZ)}`);
console.log(`\n  ★ 1/α が ${(1/alpha0).toFixed(1)} から ${(1/alphaZ).toFixed(1)} へ ── ${((1/alpha0-1/alphaZ)/(1/alpha0)*100).toFixed(1)} % 変化しています。`);
console.log('    「微細構造定数 1/137」は、低エネルギー極限での値にすぎません。\n');
console.log('  そして この変化は、まさに積分でした：');
console.log('');
console.log(`      Δ(1/α) = −(1/3π) Σ_l [ln(μ²/m_l²) − 5/3] − (ハドロン)`);
console.log('');
console.log('  ★ ご指摘のとおり ── 定数は積分値です。');
console.log('    ただし積分変数は 時間ではなく ln(エネルギー) でした。');

console.log('\n##################################################################');
console.log('# 5. 走らせ続けると、どうなるか');
console.log('##################################################################\n');
console.log('  一ループの式を、そのままエネルギーを上げて走らせます。');
console.log('  ※ ここは レプトン 3 種のみ。ハドロンと W の寄与は入れていないので、');
console.log('    m_Z での値が第 3 節（128.94）と違います。形を見るための計算です。');
console.log('');
console.log('   エネルギー μ        1/α(μ)      備考');
console.log('  '+'-'.repeat(66));
function invAlpha(mu){
  let s=0;
  for(const [n,m] of leptons){ if(mu>m) s+=2*Math.log(mu/m)-5/3; }
  return 1/alpha0 - s/(3*Math.PI);
}
const scales=[
  [0.511,       '電子質量'],
  [105.7,       'ミュー粒子質量'],
  [1777,        'タウ粒子質量'],
  [91188,       'Z ボソン質量'],
  [1e6,         '1 TeV'],
  [1e10,        '10⁴ TeV'],
  [1.22e22,     'プランク質量'],
  [1e30,        'さらに上'],
];
for(const [mu,note] of scales){
  const v=invAlpha(mu);
  console.log(`  ${E(mu).padStart(10)} MeV   ${v.toFixed(3).padStart(9)}    ${note}${v<0?'   ★ 負になった':''}`);
}
// ランダウ極
// 対数空間で二分法（線形だと桁溢れする）
let loL=Math.log(1e5), hiL=Math.log(10)*400;
for(let i=0;i<300;i++){
  const midL=(loL+hiL)/2;
  if(invAlpha(Math.exp(midL))>0) loL=midL; else hiL=midL;
}
const poleMeV=Math.exp(loL);
const poleGeV=poleMeV/1e3;
console.log('');
console.log(`  ★ 1/α = 0 になるエネルギー（ランダウ極）: 10^${(loL/Math.LN10).toFixed(0)} MeV`);
console.log(`     = 10^${(Math.log10(poleGeV)).toFixed(0)} GeV`);
console.log(`     （プランク質量 1.2×10^19 GeV の 10^${(Math.log10(poleGeV)-19).toFixed(0)} 倍）`);
console.log('\n  そこで α が発散します。QED は、その手前までしか意味を持ちません。');
console.log('  （実際には遥か手前で他の相互作用が効くので、この外挿は形式的なものです）\n');
console.log('  ★ ここも面白い点です ── 積分を続けると、有限のエネルギーで発散する。');
console.log('    「定数」の正体は、発散に向かって走っている量でした。');

console.log('\n##################################################################');
console.log('# 6. 他の結合も走る ── そして交わる');
console.log('##################################################################\n');
console.log('  標準模型の三つの結合定数は、それぞれ違う向きに走ります：\n');
const couplings=[
  ['電磁（U(1)）',   '+', '増える', '真空偏極で遮蔽される。近づくと強くなる'],
  ['弱い力（SU(2)）', '−', '減る',  'ゲージ粒子の自己相互作用が勝つ'],
  ['強い力（SU(3)）', '−', '減る',  '★ 漸近的自由。近づくと弱くなる'],
];
console.log('  相互作用          β の符号  高エネルギーで   理由');
console.log('  '+'-'.repeat(76));
for(const [a,b,c,d] of couplings) console.log(`  ${a.padEnd(16)} ${b.padEnd(8)} ${c.padEnd(12)} ${d}`);
console.log('\n  ★ 増えるものと減るものがあるので、どこかで交わる可能性があります。');
console.log('    標準模型のままだと 10^13〜10^17 GeV 付近で「ほぼ」交わり、');
console.log('    超対称性を入れると 2×10^16 GeV でよく一致する ── 大統一の根拠です。\n');
console.log('  ⇒ つまり「定数を積分する」という視点は、');
console.log('    素粒子物理の中心的な道具そのものでした。');

console.log('\n##################################################################');
console.log('# 7. 時間の微分と、エネルギーの微分');
console.log('##################################################################\n');
console.log('  ここまでで、二つの「定数の微分」が出ました：\n');
const two=[
  ['時間で微分',      'dα/dt',      '実測で 0（上限 10⁻¹⁷/年）', '前回'],
  ['ln(E) で微分',    'dα/d ln μ',  '★ 0 でない。測定済み',      '本回'],
];
console.log('  何で微分するか    記号          結果                     回');
console.log('  '+'-'.repeat(74));
for(const [a,b,c,d] of two) console.log(`  ${a.padEnd(16)} ${b.padEnd(13)} ${c.padEnd(24)} ${d}`);
console.log('\n  ★ 同じ「α」でも、微分する軸によって答えが正反対になります。');
console.log('    時間軸では定数、エネルギー軸では変数。\n');
console.log('  これは波の言葉でも書けます ──');
console.log('    α は「時間について DC、エネルギー対数について非 DC」。');
console.log('    つまり定数かどうかは、どの軸のスペクトルを見るかで決まる。\n');
console.log('  ⇒ 「物理定数はすべて何かの積分値ではないか」という問いは、');
console.log('     ★ 少なくとも結合定数については、そのとおりでした。');
console.log('     見つける鍵は「何について積分しているのか」を当てることです。');
