// 放射は二階微分から出る ── 空が青い理由まで、階数で説明できる
'use strict';
const E=x=>x.toExponential(3);
const e=1.602176634e-19, eps0=8.8541878128e-12, c=2.99792458e8;
const me=9.1093837015e-31, hbar=1.054571817e-34;
const a0=5.29177210903e-11;
const re=e*e/(4*Math.PI*eps0*me*c*c);   // 古典電子半径

console.log('##################################################################');
console.log('# 1. 遠方場だけが、二階微分を拾う');
console.log('##################################################################\n');
console.log('  電荷が作る場を距離で展開すると、三つの項が出ます：\n');
console.log('   項        距離依存   何に比例するか        階数   エネルギーを運ぶか');
console.log('  '+'-'.repeat(76));
const terms=[
  ['静電場',   '1/r²',  '電荷 q',          0, '×'],
  ['誘導場',   '1/r²',  '電流 ＝ q̇',        1, '×'],
  ['放射場',   '1/r',   '★ 加速度 ＝ q̈',    2, '★ ○'],
];
for(const [a,b,d,n,f] of terms)
  console.log(`  ${a.padEnd(9)} ${b.padEnd(9)} ${d.padEnd(18)} ${String(n).padStart(3)}    ${f}`);
console.log('\n  ★ なぜ 1/r の項だけがエネルギーを運ぶのか ── 数えれば分かります：\n');
console.log('      エネルギー流束 ∝ E²、球の面積 ∝ r²');
console.log('      → 全放射パワー ∝ E² r²\n');
console.log('   場の型     E ∝        E²r² ∝      無限遠で');
console.log('  '+'-'.repeat(52));
for(const [nm,p] of [['静電・誘導','1/r²'],['放射','1/r']]){
  const n = p==='1/r²'?2:1;
  console.log(`  ${nm.padEnd(10)} ${p.padEnd(10)} r^${2-2*n}${2-2*n===0?'（一定）':''}      ${2-2*n<0?'ゼロになる':'★ 残る'}`);
}
console.log('\n  ★ 1/r より速く落ちる場は、無限遠に届きません。');
console.log('    そして 1/r の項は、二階微分（加速度）にしか現れない ──');
console.log('    ★ だから「放射には加速度が要る」のです。階数の問題でした。');

console.log('\n##################################################################');
console.log('# 2. ラーモアの公式 ── 加速度の二乗');
console.log('##################################################################\n');
console.log('      P = q² a² / (6π ε₀ c³)\n');
console.log('  ★ 加速度の「二乗」── つまり二階微分を取って、二乗する。');
console.log('    第 1 回の言葉では：スペクトルを +12 dB/oct 傾けて、パワーにする。\n');
function larmor(q,a){ return q*q*a*a/(6*Math.PI*eps0*Math.pow(c,3)); }
console.log('  場面                     加速度 a [m/s²]    放射パワー [W]');
console.log('  '+'-'.repeat(68));
const cases=[
  ['重力加速度で落ちる電子',   9.8],
  ['家庭用電源の電子（60Hz, 1mm振幅）', Math.pow(2*Math.PI*60,2)*1e-3],
  ['水素原子の基底状態の電子',  Math.pow(2.187691e6,2)/a0],
  ['LHC の陽子（曲率半径 2.8km）', Math.pow(c,2)/2804],
];
for(const [nm,a] of cases) console.log(`  ${nm.padEnd(24)} ${E(a)}      ${E(larmor(e,a))}`);
console.log('\n  ★ 加速度が 10 桁 違えば、放射は 20 桁 違う ── 二乗だから。');

console.log('\n##################################################################');
console.log('# 3. 古典原子は、なぜ潰れるのか ── 時間を計算する');
console.log('##################################################################\n');
console.log('  水素原子の電子は円運動しています。円運動は加速度運動 ──');
console.log('  だから古典電磁気学によれば、放射してエネルギーを失うはずです。\n');
const v0=2.187691e6;                      // ボーア半径での速度 [m/s]
const acc=v0*v0/a0;
const P0=larmor(e,acc);
const Etot=e*e/(8*Math.PI*eps0*a0);       // 全エネルギーの大きさ（13.6 eV）
console.log(`  ボーア半径 a₀ = ${E(a0)} m`);
console.log(`  電子の速さ v = ${E(v0)} m/s  （= αc）`);
console.log(`  向心加速度 a = v²/a₀ = ${E(acc)} m/s²`);
console.log(`  → 放射パワー P = ${E(P0)} W\n`);
console.log(`  全エネルギー |E| = ${E(Etot)} J = ${(Etot/e).toFixed(2)} eV`);
console.log(`  素朴な見積もり  |E|/P = ${E(Etot/P0)} s\n`);
console.log('  ★ ただし半径が縮むと加速度が上がり、放射が加速します。');
console.log('    きちんと積分すると：\n');
console.log('      t = a₀³ / (4 r_e² c),      r_e = 古典電子半径\n');
const tFall=Math.pow(a0,3)/(4*re*re*c);
console.log(`  r_e = ${E(re)} m`);
console.log(`  → t = ${E(tFall)} s\n`);
console.log('  ★ 約 16 ピコ秒で、電子は原子核に落ちます。');
console.log('    ── 古典物理では、原子は存在できません。');
console.log('    これが量子力学が必要になった理由の一つでした。\n');
console.log('  半径の縮み方も見ておきます（r³ が線形に減る）：\n');
console.log('   経過時間 [s]     半径 r/a₀      加速度の比    放射パワーの比');
console.log('  '+'-'.repeat(70));
for(const frac of [0,0.5,0.9,0.99,0.999]){
  const r3=Math.pow(a0,3)*(1-frac);
  const r=Math.pow(r3,1/3);
  const ratio=r/a0;
  // a ∝ 1/r², P ∝ a² ∝ 1/r⁴
  console.log(`  ${E(tFall*frac).padStart(11)}    ${ratio.toFixed(4).padStart(8)}     ${E(1/(ratio*ratio))}    ${E(1/Math.pow(ratio,4))}`);
}
console.log('\n  ★ 最後の 0.1 % の時間で、放射パワーが 10⁴ 倍 になります。');

console.log('\n##################################################################');
console.log('# 4. 振動する電荷は、ω⁴ で放射する ── ここが効く');
console.log('##################################################################\n');
console.log('  双極子 p = p₀ sin(ωt) が放射するパワーは：\n');
console.log('      P ∝ ⟨p̈²⟩ = ω⁴ p₀²/2\n');
console.log('  ★ 二階微分で ω²、それを二乗して ω⁴。');
console.log('    ── 「階数 2 を二乗する」だけで、四乗則が出ます。\n');
console.log('  これがレイリー散乱です。散乱断面積が ω⁴ ∝ 1/λ⁴ に比例する。\n');
console.log('   色         波長 [nm]    (1/λ⁴) の比（赤を 1 として）');
console.log('  '+'-'.repeat(60));
const colors=[['紫',400],['青',450],['緑',550],['黄',580],['赤',650]];
for(const [nm,lam] of colors){
  const r=Math.pow(650/lam,4);
  console.log(`  ${nm.padEnd(10)} ${String(lam).padStart(6)}       ${r.toFixed(2).padStart(6)}${nm==='青'?'   ★ 赤の 4.4 倍 散乱される':''}`);
}
console.log('\n  ★ 空が青いのは、二階微分を二乗したから。');
console.log('    ── 大気の分子が光で揺さぶられ、加速度に比例して再放射する。');
console.log('      その強さが ω⁴ なので、短波長ほど強く散乱される。\n');
console.log('  そして夕焼けが赤いのも、同じ式の裏返しです：');
console.log('  太陽が低いと大気を長く通るので、青が先に散らされ、赤だけが残る。');

console.log('\n##################################################################');
console.log('# 5. 放射のスペクトル ＝ 加速度のスペクトル');
console.log('##################################################################\n');
console.log('  第 1 回の見方を使うと、放射スペクトルの正体が分かります：\n');
console.log('      放射の振幅 ∝ a(ω) = (iω)² x(ω) = −ω² x(ω)\n');
console.log('  ★ 放射スペクトルは「軌道のスペクトルを +12 dB/oct 傾けたもの」。\n');
const spectra=[
  ['単振動する電荷',      '線スペクトル',   'その振動数だけ。原子スペクトル'],
  ['制動放射',           '広いスペクトル', '急な減速 ＝ 短いパルス ＝ 広帯域（第 9 回）'],
  ['シンクロトロン放射',   '高調波の櫛',    '円運動だが相対論的で、高次高調波まで出る'],
  ['熱運動（黒体放射）',   '連続スペクトル', '乱雑な加速度の重ね合わせ'],
];
console.log('  加速度の形             放射スペクトル     理由');
console.log('  '+'-'.repeat(80));
for(const [a,b,d] of spectra) console.log(`  ${a.padEnd(20)} ${b.padEnd(16)} ${d}`);
console.log('\n  ★ 制動放射が広帯域なのは、第 9 回の帯域幅定理そのものです ──');
console.log('    「短時間で急に止まる」＝「短いパルス」＝「広い帯域」。\n');
const tStop=1e-18;
console.log(`  例：電子が ${E(tStop)} 秒 で止まるとすると`);
console.log(`     帯域 Δω ≳ 1/(2Δt) = ${E(1/(2*tStop))} rad/s`);
console.log(`     光子エネルギーに直すと ħΔω = ${(hbar/(2*tStop)/e/1e3).toFixed(1)} keV`);
console.log('\n  ★ X 線の帯域が出ました。制動放射が X 線源になる理由です。');

console.log('\n##################################################################');
console.log('# 6. 階数の梯子を、電磁気で並べ直す');
console.log('##################################################################\n');
const ladder=[
  [0, 'q（電荷）',         '静電場 ∝ 1/r²',        'クーロン'],
  [1, 'q̇（電流）',          '磁場・誘導 ∝ 1/r²',    'ビオ＝サバール、ファラデー'],
  [2, 'q̈（加速度）',        '★ 放射 ∝ 1/r',         'ラーモア、レイリー、制動放射'],
  [3, '⃛q（躍度）',          'アブラハム＝ローレンツ力', '★ 反作用。因果律を壊す'],
];
console.log('   階数   量                 生じる場              名前');
console.log('  '+'-'.repeat(80));
for(const [n,a,b,d] of ladder)
  console.log(`   ${String(n).padStart(3)}    ${a.padEnd(18)} ${b.padEnd(22)} ${d}`);
console.log('\n  ★ 三階まで行くと、有名な困りごとが出ます ──');
console.log('    放射の反作用（アブラハム＝ローレンツ力）は F = (q²/6πε₀c³) ⃛x。\n');
console.log('  この式は三階微分なので：');
console.log('    ・第 2 回のオストログラツキー不安定性にかかる');
console.log('    ・実際、力が加わる「前」に加速が始まる解が出る（前加速）');
console.log('    ★ 第 8 回の因果律を破ります。\n');
const tau0=2*re/(3*c);
console.log(`  前加速の時間尺度 τ = 2r_e/(3c) = ${E(tau0)} s`);
console.log(`  （光が古典電子半径を横切る時間の程度）\n`);
console.log('  ★ 「階数を上げすぎると因果律が壊れる」が、');
console.log('    古典電磁気学の中で実際に起きています。');
console.log('    ── これは古典論の破綻であって、量子電磁力学では解消します。');

console.log('\n##################################################################');
console.log('# 7. まとめ');
console.log('##################################################################\n');
const summary=[
  ['放射は二階微分から',   '◎ 厳密',  '1/r の項だけが加速度に比例し、エネルギーを運ぶ'],
  ['P ∝ a²',           '◎ 厳密',  'ラーモアの公式'],
  ['古典原子は 16 ps',   '◎ 計算',  't = a₀³/(4r_e²c)。量子力学が必要な理由'],
  ['空が青いのは ω⁴',    '◎ 計算',  '二階微分を二乗するだけ。青は赤の 4.4 倍'],
  ['制動放射が広帯域',   '○ 帯域幅', '第 9 回の定理そのもの'],
  ['三階は因果律を壊す',  '○ 既知',  'アブラハム＝ローレンツ力の前加速'],
];
console.log('  主張                  判定      根拠');
console.log('  '+'-'.repeat(76));
for(const [a,b,d] of summary) console.log(`  ${a.padEnd(20)} ${b.padEnd(9)} ${d}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     放射とは、二階微分を二乗したものである。');
console.log('     だから加速度が要り、だから ω⁴ になり、だから空は青い。');
console.log('     ── そして三階まで行くと、因果律が壊れる。');
