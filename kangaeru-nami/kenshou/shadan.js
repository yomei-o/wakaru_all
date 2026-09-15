// 質量は遮断周波数である ── 波として見たときの、質量の正体
'use strict';
const E=x=>x.toExponential(3);
const c=2.99792458e8, hbar=1.054571817e-34;
const eV=1.602176634e-19;
const hbarc=197.3269804;            // MeV·fm

console.log('##################################################################');
console.log('# 1. 波動方程式は、フィルタの仕様書である');
console.log('##################################################################\n');
console.log('  平面波 exp(i(kx − ωt)) を方程式に入れると、ω と k の関係が出ます。');
console.log('  それが分散関係 ── どの (ω, k) が通れるかを決める「伝達関数」です。\n');
const eqs=[
  ['波動方程式',        '∂²ψ/∂t² = c²∂²ψ/∂x²',        'ω = ck',                'すべての ω が通る'],
  ['クライン＝ゴルドン',  '(□ + (mc/ħ)²)ψ = 0',         'ω² = c²k² + (mc²/ħ)²',  '★ 下に遮断がある'],
  ['シュレーディンガー',  'iħ∂ψ/∂t = −(ħ²/2m)∂²ψ/∂x²', 'ω = ħk²/2m',            '非相対論。二次'],
  ['拡散方程式',        '∂u/∂t = D∂²u/∂x²',           'ω = −iDk²',             '虚数 ── 伝わらず減衰'],
];
console.log('  方程式              式                            分散関係                 性質');
console.log('  '+'-'.repeat(96));
for(const [a,b,d,e] of eqs) console.log(`  ${a.padEnd(18)} ${b.padEnd(28)} ${d.padEnd(22)} ${e}`);
console.log('\n  ★ 二行目を、もう一度 見てください。');

console.log('\n##################################################################');
console.log('# 2. クライン＝ゴルドンの分散関係を、音響の目で読む');
console.log('##################################################################\n');
console.log('      ω² = c²k² + ω_c²,      ω_c ≡ mc²/ħ\n');
console.log('  この形に見覚えがあるはずです。導波管とまったく同じ式です：\n');
const analog=[
  ['自由な波（真空中の光）', 'ω = ck',              '遮断なし。どんな低い ω も通る'],
  ['導波管',              'ω² = c²k² + ω_c²',    '★ ω_c 以下は通らない'],
  ['質量 m の場',          'ω² = c²k² + (mc²/ħ)²','★ 同じ形。ω_c = mc²/ħ'],
];
console.log('  系                    分散関係                性質');
console.log('  '+'-'.repeat(74));
for(const [a,b,d] of analog) console.log(`  ${a.padEnd(20)} ${b.padEnd(22)} ${d}`);
console.log('\n  ★ つまり ──\n');
console.log('        質量とは、真空という導波管の「遮断周波数」である。\n');
console.log('  静止した粒子（k = 0）は、ω = ω_c でその場で振動しています。');
console.log('  それ以下の周波数では、波が伝わりません。\n');
const parts=[
  ['電子',       0.51099895],
  ['ミュー粒子',   105.6583755],
  ['パイ中間子',   139.57039],
  ['陽子',       938.27208816],
  ['W ボソン',   80379],
  ['ヒッグス',    125250],
];
console.log('  粒子          質量 [MeV]      遮断周波数 ω_c [rad/s]    遮断振動数 [Hz]');
console.log('  '+'-'.repeat(76));
for(const [n,m] of parts){
  const wc=m*1e6*eV/hbar;
  console.log(`  ${n.padEnd(12)} ${m.toFixed(3).padStart(10)}      ${E(wc)}          ${E(wc/(2*Math.PI))}`);
}
console.log('\n  ★ 電子の遮断周波数は 7.8×10²⁰ rad/s。');
console.log('    可聴音の最高が 2×10⁵ rad/s なので、その 10¹⁶ 倍です。');

console.log('\n##################################################################');
console.log('# 3. 遮断より下では、どうなるか ── ここが決定的');
console.log('##################################################################\n');
console.log('  ω < ω_c では、分散関係を満たす実数の k がありません：\n');
console.log('      k² = (ω² − ω_c²)/c² < 0     →     k = iκ（純虚数）\n');
console.log('  波数が虚数ということは、exp(ikx) = exp(−κx) ── 指数関数的に減衰する。');
console.log('  導波管の用語では「エバネッセント波」、遮断以下のモードです。\n');
console.log('  ★ そして ω = 0（静的な場）では：\n');
console.log('      κ = ω_c/c = mc/ħ    →    減衰長 = ħ/(mc)\n');
console.log('  これは何かというと ── 湯川ポテンシャルです：\n');
console.log('      V(r) ∝ exp(−r/λ)/r,     λ = ħ/(mc)\n');
console.log('  粒子          質量 [MeV]      到達距離 ħ/mc [fm]     備考');
console.log('  '+'-'.repeat(78));
for(const [n,m] of parts){
  const lam=hbarc/m;
  let note='';
  if(n==='パイ中間子') note='★ 核力の到達距離。湯川の予言';
  if(n==='W ボソン') note='★ 弱い力が「弱い」理由';
  if(n==='電子') note='電子のコンプトン波長';
  console.log(`  ${n.padEnd(12)} ${m.toFixed(3).padStart(10)}      ${lam.toExponential(3).padStart(10)}       ${note}`);
}
console.log('\n  ★ 力の到達距離とは、遮断周波数以下でのエバネッセント減衰長でした。');
console.log('    パイ中間子の 1.41 fm は、まさに原子核の大きさの尺度です。');
console.log('    （前シリーズ「金を作る」で使った核半径 1.2 A^(1/3) fm を思い出してください）');

console.log('\n##################################################################');
console.log('# 4. 力が光速無限遠まで届くかどうかも、遮断で決まる');
console.log('##################################################################\n');
const forces=[
  ['電磁気',   '光子',      0,        '∞',        '遮断ゼロ → 無限遠まで'],
  ['重力',     '重力子',    0,        '∞',        '同上'],
  ['弱い力',   'W/Z',       80379,    null,       '★ 遮断が高い → 届かない'],
  ['強い力',   'グルーオン',  0,        '1 fm 程度', '遮断ゼロだが閉じ込めで別の話'],
];
console.log('  力          媒介粒子      質量 [MeV]   到達距離        理由');
console.log('  '+'-'.repeat(80));
for(const [a,b,m,r,note] of forces){
  const rr = r!==null ? r : (hbarc/m).toExponential(2)+' fm';
  console.log(`  ${a.padEnd(10)} ${b.padEnd(12)} ${String(m).padStart(8)}   ${String(rr).padEnd(14)} ${note}`);
}
console.log('\n  ★ 「なぜ電磁気は遠くまで届き、弱い力は届かないのか」の答えは');
console.log('    「光子には遮断が無く、W ボソンには 1.2×10²⁶ rad/s の遮断があるから」。');
console.log('    質量があるかないか、ただそれだけでした。');

console.log('\n##################################################################');
console.log('# 5. 速度も、スペクトルの微分で出る');
console.log('##################################################################\n');
console.log('  分散関係 ω(k) から、二つの速度が定義できます：\n');
console.log('      位相速度  v_p = ω/k        （比）');
console.log('      群速度    v_g = dω/dk      （★ 微分）\n');
console.log('  クライン＝ゴルドンで計算すると：\n');
console.log('      ω² = c²k² + ω_c²  を k で微分して  2ω(dω/dk) = 2c²k');
console.log('      → v_g = c²k/ω,   v_p = ω/k');
console.log('      → ★ v_p · v_g = c²\n');
console.log('  粒子の速度 v に対して：\n');
console.log('   v/c      v_g/c      v_p/c      v_p·v_g/c²');
console.log('  '+'-'.repeat(50));
for(const b of [0.1,0.5,0.9,0.99,0.999]){
  const vg=b, vp=1/b;
  console.log(`  ${b.toFixed(3)}    ${vg.toFixed(4)}     ${vp.toFixed(4)}     ${(vp*vg).toFixed(6)}`);
}
console.log('\n  ★ 位相速度は光速を超えます（v_p = c²/v > c）。しかし情報は運びません。');
console.log('    運ぶのは群速度 ── つまり「スペクトルの微分」のほうです。\n');
console.log('  ⇒ ここでも微分が効いています。');
console.log('    「速さ」とは、分散関係というスペクトルを微分した量でした。');

console.log('\n##################################################################');
console.log('# 6. 静止エネルギー E = mc² を、波の言葉で読む');
console.log('##################################################################\n');
console.log('  遮断周波数に ħ を掛けるだけです：\n');
console.log('      ħω_c = ħ · (mc²/ħ) = mc²\n');
console.log('  ★ E = mc² とは「遮断周波数のエネルギー」でした。');
console.log('    アインシュタインの式が、フィルタの仕様に書き直せる。\n');
console.log('  そして k ≠ 0 のとき：\n');
console.log('      (ħω)² = (ħck)² + (mc²)²     ⟺     E² = (pc)² + (mc²)²\n');
console.log('  ★ 相対論のエネルギー・運動量関係は、分散関係そのものです。');
console.log('    ピタゴラスの定理に見えるのは、導波管の分散関係だったから。\n');
console.log('  確かめます（電子、いろいろな運動量で）：\n');
const me=0.51099895;
console.log('   p [MeV/c]    E=√(p²+m²)   ħω [MeV]   一致');
console.log('  '+'-'.repeat(54));
for(const p of [0,0.1,0.511,1,10,100]){
  const Erel=Math.sqrt(p*p+me*me);
  const k=p/hbarc;                                  // fm^-1
  const wc=me/hbarc;                                 // fm^-1
  const w=Math.sqrt(k*k+wc*wc)*hbarc;                // MeV（ħω）
  console.log(`  ${p.toFixed(3).padStart(9)}   ${Erel.toFixed(6).padStart(10)}   ${w.toFixed(6).padStart(9)}   ${Math.abs(Erel-w)<1e-9?'○':'×'}`);
}
console.log('\n  ★ 完全に同じ式です。');

console.log('\n##################################################################');
console.log('# 7. まとめ ── 波として見たときの質量');
console.log('##################################################################\n');
const sum=[
  ['質量 m',          '遮断周波数 ω_c = mc²/ħ',   '真空を導波管と見たときの仕様'],
  ['静止エネルギー',    'ħω_c',                   'E = mc² はこれ'],
  ['E²=(pc)²+(mc²)²', '分散関係 ω²=c²k²+ω_c²',   '相対論 ＝ 導波管の式'],
  ['力の到達距離',      'ħ/(mc)',                 '遮断以下のエバネッセント減衰長'],
  ['粒子の速さ',        'dω/dk',                  '★ スペクトルの微分'],
  ['位相速度',          'ω/k = c²/v',             '光速を超えるが情報は運ばない'],
];
console.log('  物理量               波の言葉では                意味');
console.log('  '+'-'.repeat(80));
for(const [a,b,d] of sum) console.log(`  ${a.padEnd(18)} ${b.padEnd(24)} ${d}`);
console.log('\n  ★ 「質量を波として見る」は、完全に成功します ──');
console.log('    ただし答えは「積分値」ではなく「遮断周波数」でした。\n');
console.log('    前回、質量を重力の積分と見る道は否定されました（ブランス＝ディッケ）。');
console.log('    しかし波として見る道は、そのまま相対論と量子論になります。');
console.log('');
console.log('    ⇒ 質量は、積分ではなくフィルタの特性です。');
