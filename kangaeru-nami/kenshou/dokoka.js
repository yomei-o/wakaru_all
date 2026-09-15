// 質量はどこから来るのか ── 箱の最低周波数と、凝縮体との結合と、走り
'use strict';
const E=x=>x.toExponential(3);
const hbarc=197.3269804;        // MeV·fm
const v=246.21965e3;            // ヒッグスの真空期待値 [MeV]

console.log('##################################################################');
console.log('# 1. 陽子の質量の内訳 ── 99% はクォークの質量ではない');
console.log('##################################################################\n');
const mp=938.27208816, mn=939.56542052;
const mu=2.16, md=4.67;          // MS-bar, 2 GeV（PDG）
const sumq=2*mu+md;
console.log('   粒子          質量 [MeV]      備考');
console.log('  '+'-'.repeat(66));
console.log(`   陽子           ${mp.toFixed(4).padStart(10)}      uud`);
console.log(`   u クォーク     ${mu.toFixed(2).padStart(10)}      MS-bar, 2 GeV`);
console.log(`   d クォーク     ${md.toFixed(2).padStart(10)}      MS-bar, 2 GeV`);
console.log(`   u+u+d の和     ${sumq.toFixed(2).padStart(10)}      ★ 陽子の ${(sumq/mp*100).toFixed(2)} %`);
console.log(`   残り           ${(mp-sumq).toFixed(2).padStart(10)}      ★ ${((mp-sumq)/mp*100).toFixed(2)} %`);
console.log('\n  ★ 陽子の質量の 99 % は、クォークの質量ではありません。');
console.log('    では何なのか ── 閉じ込められた場のエネルギーです。\n');
console.log('  ★ 波の言葉ではこうなります：\n');
console.log('      箱に閉じ込めた波には、最低周波数がある。');
console.log('      その最低周波数が、質量として見える。\n');
console.log('  ── 第 6 回の「質量＝遮断周波数」が、そのまま出どころの説明になっています。');

console.log('\n##################################################################');
console.log('# 2. 箱に閉じ込めるだけで、質量が出る');
console.log('##################################################################\n');
console.log('  質量ゼロの波を、大きさ L の箱に閉じ込めます。');
console.log('  境界条件から波数が下から止まるので、エネルギーにも下限ができます：\n');
console.log('      一次元の箱   : k = π/L      →   E = πħc/L');
console.log('      球の箱（最低）: kR = 2.04    →   E = 2.04 ħc/R\n');
console.log(`      ħc = ${hbarc} MeV·fm\n`);
console.log('   閉じ込めの寸法      一次元 πħc/L      球 2.04ħc/R      比較');
console.log('  '+'-'.repeat(76));
for(const [L,note] of [[0.5,''],[0.84,'★ 陽子の電荷半径'],[1.0,'核子の目安'],[2.0,''],[5.0,'原子核（重い）']]){
  console.log(`  ${L.toFixed(2).padStart(10)} fm     ${(Math.PI*hbarc/L).toFixed(1).padStart(10)} MeV   ${(2.04*hbarc/L).toFixed(1).padStart(10)} MeV    ${note}`);
}
console.log('\n  ★ 1 fm に閉じ込めるだけで、数百 MeV が出ます。');
console.log('    陽子の 938 MeV と、同じ桁です。\n');
console.log('  逆に解いてみます ── 質量ゼロのクォーク 3 個が陽子の質量を全部 担うとしたら、');
console.log('  箱の大きさはいくつになるか：\n');
const Rpred=3*2.04*hbarc/mp;
console.log(`      3 × 2.04 ħc / R = ${mp.toFixed(1)} MeV     →     R = ${Rpred.toFixed(3)} fm`);
console.log(`      実測の電荷半径                              R = 0.841 fm`);
console.log(`      ずれ                                          ${(Rpred/0.841).toFixed(2)} 倍\n`);
console.log('  ★ 1.5 倍 のずれ。桁は合っています。');
console.log('    ── 模型がそれだけ粗いということで、それ以上のことは言えません。');
console.log('    ★ 判定：これは「閉じ込めで質量が出る」の桁の確認であって、');
console.log('      陽子質量の計算ではありません（本物は格子 QCD で 1 % 精度）。');

console.log('\n##################################################################');
console.log('# 3. もう一つの出どころ ── 凝縮体との結合');
console.log('##################################################################\n');
console.log('  第 17 回で、超伝導体の中の光子が質量を持つのを見ました。');
console.log('  素粒子でも同じことが起きています ── ヒッグス場という凝縮体。\n');
console.log('      m_f = y_f · v / √2,      v = 246.22 GeV\n');
console.log('  y は「結合の強さ」。質量から逆算してみます：\n');
const fer=[
  ['電子',       0.51099895],
  ['ミューオン',  105.6583755],
  ['タウ',        1776.86],
  ['u クォーク',  2.16],
  ['d クォーク',  4.67],
  ['s クォーク',  93.4],
  ['c クォーク',  1270],
  ['b クォーク',  4180],
  ['t クォーク',  172690],
];
console.log('   粒子            質量 [MeV]        湯川結合 y        電子の何倍');
console.log('  '+'-'.repeat(74));
const ye=Math.sqrt(2)*0.51099895/v;
for(const [nm,m] of fer){
  const y=Math.sqrt(2)*m/v;
  console.log(`  ${nm.padEnd(12)} ${E(m).padStart(12)}      ${E(y).padStart(12)}     ${E(y/ye)}`);
}
console.log('\n  ★ t クォークだけ y ≈ 1 ── ちょうど 1 です。');
console.log(`      y_top = ${(Math.sqrt(2)*172690/v).toFixed(4)}\n`);
console.log('  ★ そして電子からトップまで、結合の幅は 5 桁半：');
console.log(`      y_top / y_e = ${E(172690/0.51099895)}\n`);
console.log('  ── なぜこんなに開いているのか。誰も知りません。');
console.log('    ★ これが「フレーバーの階層問題」で、第 15 回の');
console.log('      「α の値の由来」と同じ種類の、開いたままの扉です。');

console.log('\n##################################################################');
console.log('# 4. 質量も走る ── ここは文字どおり積分値');
console.log('##################################################################\n');
console.log('  第 5 回で結合定数が ln μ について走りました。質量も走ります：\n');
console.log('      d ln m / d ln μ = −γ(α_s)        （γ は質量異常次元）\n');
console.log('  一ループでは、解が閉じた形で書けます：\n');
console.log('      m(μ) = m(μ₀) · [ α_s(μ)/α_s(μ₀) ]^(γ₀/2β₀),   γ₀ = 8, β₀ = 11 − 2n_f/3\n');
const mZ=91.1876, asZ=0.1179;
function b0(nf){ return 11-2*nf/3; }
function alphaS(mu,nf){
  // 一ループ：1/α_s(μ) = 1/α_s(m_Z) + (β₀/2π) ln(μ/m_Z)
  return 1/(1/asZ + b0(nf)/(2*Math.PI)*Math.log(mu/mZ));
}
function runMass(m0,mu0,mu,nf){
  return m0*Math.pow(alphaS(mu,nf)/alphaS(mu0,nf), 8/(2*b0(nf)));
}
console.log('   スケール μ [GeV]    α_s(μ)      m_b(μ) [GeV]     m_τ(μ) [GeV]    m_b/m_τ');
console.log('  '+'-'.repeat(84));
const mb0=4.18, mtau=1.77686;
for(const mu of [4.18, 10, mZ, 1000, 1e6, 1e10, 1e16]){
  const nf=mu<mZ?5:6;
  const as=alphaS(mu,nf);
  const mb=runMass(mb0,4.18,mu,nf);
  console.log(`  ${E(mu).padStart(14)}    ${as.toFixed(5)}    ${mb.toFixed(4).padStart(10)}      ${mtau.toFixed(4).padStart(10)}     ${(mb/mtau).toFixed(4)}`);
}
console.log(`\n  ★ m_b(m_Z) = ${runMass(mb0,4.18,mZ,5).toFixed(3)} GeV   （文献値 約 2.83 GeV、二ループ以上を入れた値）`);
console.log('    一ループなので 9 % ずれます。それでも「4.18 → 3.1」の走りは出ています。\n');
console.log('  ★ ここで注意が要ります ──');
console.log('    m_b(μ) は次元を持つ量です。第 7 回の結論からすると、これ自体は');
console.log('    「帳簿」のはず。観測にかかるのは比のほうです。\n');
console.log('  そこで m_b/m_τ を見ました。τ は QCD で走らないので、比が動きます。');
// m_b = m_tau になるスケールを探す
{
  let lo=Math.log(mZ), hi=Math.log(1e16);
  for(let i=0;i<200;i++){
    const md2=(lo+hi)/2, mu=Math.exp(md2);
    if(runMass(mb0,4.18,mu,6)>mtau) lo=md2; else hi=md2;
  }
  const muEq=Math.exp((lo+hi)/2);
  console.log(`\n  ★ m_b(μ) = m_τ になるスケール： μ = ${E(muEq)} GeV`);
  console.log(`      そこでの共通の質量 = ${runMass(mb0,4.18,muEq,6).toFixed(4)} GeV`);
}
console.log(`\n  ★ 大統一スケール 10^16 GeV では m_b/m_τ = ${(runMass(mb0,4.18,1e16,6)/mtau).toFixed(3)}`);
console.log('    ── 1 に近づきますが、一致はしません。');
console.log('    ★ これは既知の結果です（標準模型のままでは b-τ 統一は成立せず、');
console.log('      超対称性を入れると改善する、というのが定番の議論）。');
console.log('      判定：本稿は一ループで再現しただけで、新しい主張はありません。');

console.log('\n##################################################################');
console.log('# 5. 慣性質量と重力質量 ── 波として見ると同じもの');
console.log('##################################################################\n');
console.log('  質量には二つの顔があります：\n');
console.log('      慣性質量  : 押しても動きにくさ       ← 分散関係の曲率（第 17 回）');
console.log('      重力質量  : 引かれる強さ             ← 時計の進み方\n');
console.log('  この二つが等しいことは、実験で確かめられています：\n');
const eps=[
  ['エトヴェシュ（1908）',   5e-9],
  ['ディッケ（1964）',      1e-11],
  ['ブラギンスキー（1972）', 1e-12],
  ['Eöt-Wash（2008）',     2e-13],
  ['MICROSCOPE（2022）',   1e-15],
];
console.log('   実験                        η = 2|a₁−a₂|/(a₁+a₂) の上限');
console.log('  '+'-'.repeat(64));
for(const [nm,e] of eps) console.log(`  ${nm.padEnd(26)} ${E(e)}`);
console.log('\n  ★ 波の言葉では、等価原理はこう読めます ──\n');
console.log('      重力とは「場所によって時計の進み方が違う」こと（第 16 回の c_eff）。');
console.log('      そして分散関係は時計に対して書かれている。');
console.log('      ★ だから、どんな波も同じだけ影響を受ける ── 中身によらない。\n');
console.log('  これが「重力質量＝慣性質量」の、波としての言い方です。');
console.log('  ★ 逆に言えば、等価原理が破れるとしたら');
console.log('    「波の種類によって時計が違う」ときだけ ── だから探すのは第五の力。');

console.log('\n##################################################################');
console.log('# 6. 質量の階層 ── 何桁 あるのか');
console.log('##################################################################\n');
const hier=[
  ['ニュートリノ（上限）',     1e-7,       '宇宙論からの和の上限 ~0.1 eV'],
  ['電子',                  0.511,      ''],
  ['ミューオン',             105.7,      ''],
  ['陽子',                  938.3,      '★ 99% は閉じ込め'],
  ['タウ',                  1776.9,     ''],
  ['W ボソン',              80377,      ''],
  ['ヒッグス',               125250,     ''],
  ['t クォーク',             172690,     '★ y ≈ 1'],
  ['プランク質量',           1.22091e22, '★ ħc/G の平方根'],
];
console.log('   粒子                  質量 [MeV]         電子の何倍');
console.log('  '+'-'.repeat(66));
for(const [nm,m,note] of hier)
  console.log(`  ${nm.padEnd(20)} ${E(m).padStart(12)}      ${E(m/0.511).padStart(10)}   ${note}`);
console.log('\n  ★ ニュートリノからプランク質量まで、29 桁。');
console.log(`    そしてトップからプランクまでだけで ${E(1.22091e22/172690)} 倍 ──`);
console.log('    ★ これが「階層問題」です。第 15 回の開いた扉に、もう一つ加わります。');

console.log('\n##################################################################');
console.log('# 7. 出どころは三つ。そして二つは同じもの');
console.log('##################################################################\n');
const src=[
  ['① 閉じ込め',   '境界条件が最低周波数を作る', '陽子の 99 %',        '本回 2 節'],
  ['② 凝縮体',     '背景場との結合が切片を作る', 'クォーク・レプトン', '本回 3 節'],
  ['③ 走り',       'スケールによって変わる分',   'm_b: 4.18 → 3.0',   '本回 4 節'],
];
console.log('   出どころ        仕組み                       効くところ           節');
console.log('  '+'-'.repeat(84));
for(const [a,b,cc,d] of src) console.log(`  ${a.padEnd(14)} ${b.padEnd(28)} ${cc.padEnd(20)} ${d}`);
console.log('\n  ★ そして ① と ② は、波の言葉では同じことです ──\n');
console.log('      どちらも「分散関係に切片を作る」操作。');
console.log('      ① は境界条件で作り、② は背景場で作る。\n');
console.log('  ★ 第 6 回で「質量は遮断周波数」と書きました。本回で分かったのは、');
console.log('    ★ その遮断周波数の作り方が二通りある、ということでした。');
console.log('      ── 箱に入れるか、媒質に浸すか。');

console.log('\n##################################################################');
console.log('# 8. まとめ');
console.log('##################################################################\n');
const sm=[
  ['陽子の 99% は閉じ込め',  '◎ 文献',  `クォークの和 ${sumq.toFixed(2)} MeV / ${mp.toFixed(1)} MeV`],
  ['1 fm の箱 → 数百 MeV',  '◎ 計算',  'πħc/L = 620 MeV。桁が合う'],
  ['逆算で R = 1.29 fm',    '△ 粗い',  '実測 0.841 fm。1.5 倍 のずれ'],
  ['y_top = 0.992',        '◎ 計算',  '★ トップだけ結合が 1'],
  ['y の幅は 5 桁半',       '◎ 計算',  '階層問題。誰も説明できていない'],
  ['m_b: 4.18 → 3.08 GeV', '○ 計算',  '一ループ。文献値 2.83 に 9% で近い'],
  ['等価原理 η < 10⁻¹⁵',    '○ 実測',  'MICROSCOPE 2022'],
];
console.log('  主張                      判定      根拠');
console.log('  '+'-'.repeat(80));
for(const [a,b,cc] of sm) console.log(`  ${a.padEnd(24)} ${b.padEnd(9)} ${cc}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     質量とは、分散関係にできた切片のこと。');
console.log('     その切片は、箱に入れても作れるし、媒質に浸しても作れる。');
console.log('     ── 陽子は前者で 99%、クォークは後者で 100%。');
