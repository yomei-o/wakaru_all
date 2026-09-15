// 重力波 ── 時空そのものが波。階数で数えると、電磁波より一つ上だった
'use strict';
const E=x=>x.toExponential(3);
const G=6.67430e-11;
const c=2.99792458e8;
const hbar=1.054571817e-34;
const Msun=1.98892e30;
const pc=3.085677581e16;
const yr=3.1557e7;
const eV=1.602176634e-19;

console.log('##################################################################');
console.log('# 1. 時空そのものが波 ── 測るのは無次元量');
console.log('##################################################################\n');
console.log('  この連載でずっと「何かが波である」と言ってきました。');
console.log('  ★ 重力波だけは、波打っているのが時空そのものです。\n');
console.log('  そして測る量は、長さの比：\n');
console.log('      h = ΔL / L        ★ 無次元\n');
console.log('  ── 第 7 回の「意味があるのは無次元量だけ」が、ここでは定義になっています。\n');
const L=4000;
console.log('   事象                   h               LIGO の腕 4 km での ΔL [m]     比較');
console.log('  '+'-'.repeat(92));
const evs=[
  ['GW150914（2015）',      1.0e-21, '★ 陽子の 1/1000'],
  ['GW170817（中性子星）',   1.0e-22, ''],
  ['連続波（パルサー）の上限', 1e-26,   ''],
  ['地面の振動（1 Hz）',      1e-9,    '★ 防振がなければ 12 桁 上'],
];
for(const [nm,hh,note] of evs){
  console.log(`  ${nm.padEnd(22)} ${E(hh).padStart(10)}      ${E(hh*L).padStart(12)}          ${note}`);
}
console.log('\n  ★ GW150914 で腕が伸びた量は 4×10⁻¹⁸ m ── 陽子の直径の 1/1000 です。');
console.log('    それを 4 km の腕で測った。★ 相対精度 10⁻²¹。');

console.log('\n##################################################################');
console.log('# 2. なぜ四重極なのか ── 階数で数える');
console.log('##################################################################\n');
console.log('  第 12 回で、放射には加速度（二階微分）が要ると見ました。');
console.log('  重力波では、さらに条件が厳しくなります：\n');
const multipoles=[
  ['単極子（質量）',   '∑m',        '質量保存',       '時間微分がゼロ → 放射しない'],
  ['双極子（質量中心）','∑m·r',      '運動量保存',     '★ 二階微分がゼロ → 放射しない'],
  ['★ 四重極',        '∑m·r_i r_j','保存則がない',   '★ ここから放射が出る'],
];
console.log('   多重極          モーメント      効く保存則      なぜ放射しないか');
console.log('  '+'-'.repeat(88));
for(const [a,b,cc,d] of multipoles) console.log(`  ${a.padEnd(14)} ${b.padEnd(14)} ${cc.padEnd(14)} ${d}`);
console.log('\n  ★ 電磁波では双極子が生き残ります（電荷保存はあるが「電荷中心の保存」はない）。');
console.log('    ★ 重力では質量中心の運動が保存されるので、双極子まで消える。\n');
console.log('  そこで放射の式を並べてみます：\n');
console.log('      電磁波（第 12 回）: P = (1/6πε₀c³)·⟨(d²p/dt²)²⟩      ★ 双極子の二階微分の二乗');
console.log('      重力波          : P = (G/5c⁵)·⟨(d³Q/dt³)²⟩         ★ 四重極の三階微分の二乗\n');
console.log('  ★★ 階数が一つ上がっています。');
console.log('    ── 第 12 回で「放射は二階微分から出る」と書きましたが、');
console.log('      ★ 重力波は「三階微分から出る」。空間の次数が一つ上がった分、時間も一つ上がる。');

console.log('\n##################################################################');
console.log('# 3. なぜこんなに弱いのか ── 基準になるパワー');
console.log('##################################################################\n');
console.log('  重力波の放射公式に出てくる係数は G/c⁵ です。その逆数を見ます：\n');
const Pplanck=Math.pow(c,5)/G;
console.log(`      c⁵/G = ${E(Pplanck)} W        ★ プランクパワー\n`);
console.log('  ★ これが「重力波が出せるパワーの基準」です。');
console.log('    ★ 質量・長さ・時間を含まない ── 純粋に G と c だけでできています。\n');
console.log('   事象                        パワー [W]        c⁵/G との比        比較');
console.log('  '+'-'.repeat(92));
const pows=[
  ['GW150914 のピーク',     3.6e49,  '★ 宇宙で最も明るい事象'],
  ['太陽の光度',            3.828e26,''],
  ['銀河系 全体の光',       5e36,    ''],
  ['観測可能な宇宙の星 全部', 1e49,   '★ 合体はこれと同程度'],
  ['プランクパワー',        Pplanck, '★ 理論的な上限'],
];
for(const [nm,P,note] of pows){
  console.log(`  ${nm.padEnd(24)} ${E(P).padStart(12)}      ${E(P/Pplanck).padStart(12)}      ${note}`);
}
console.log('\n  ★ GW150914 は、一瞬だけ「宇宙の星 全部」と同じ明るさで輝きました。');
console.log(`    ★ それでも c⁵/G の ${E(3.6e49/Pplanck)} 倍 にすぎません。\n`);
console.log('  ★ そして地球に届いた時点でのエネルギー流束を計算します：\n');
{
  const hh=1e-21, f=100;
  const hdot=2*Math.PI*f*hh;
  const F=Math.pow(c,3)/(16*Math.PI*G)*hdot*hdot;
  console.log(`      h = ${E(hh)}、f = ${f} Hz`);
  console.log(`      ḣ = 2πf·h = ${E(hdot)} /s`);
  console.log(`      F = (c³/16πG)·ḣ² = ${E(F)} W/m²\n`);
  console.log(`      ★ ${(F*1e3).toFixed(1)} mW/m² ── 満月の光（約 1 mW/m²）と同じ桁です。`);
}
console.log('\n  ★★ ここが重力波の逆説です ──');
console.log('    エネルギーとしては満月なみのものが降り注いだのに、');
console.log('    ★ 腕が陽子の 1/1000 しか動かない。');
console.log('    ── 流れているエネルギーは大きいのに、物質との結合が弱すぎる。');

console.log('\n##################################################################');
console.log('# 4. チャープ ── 合体までの時間が周波数を決める');
console.log('##################################################################\n');
console.log('  連星が近づくと、軌道が速くなり周波数が上がります：\n');
console.log('      df/dt = (96/5)·π^(8/3)·(GM_c/c³)^(5/3)·f^(11/3)\n');
console.log('  ★ M_c は「チャープ質量」── これだけが効きます：\n');
console.log('      M_c = (m₁m₂)^(3/5) / (m₁+m₂)^(1/5)\n');
function chirpMass(m1,m2){
  return Math.pow(m1*m2,0.6)/Math.pow(m1+m2,0.2);
}
function tauToMerge(f,Mc){
  const tau0=G*Mc/(c*c*c);
  return 5/256*Math.pow(tau0,-5/3)*Math.pow(Math.PI*f,-8/3);
}
console.log('   連星                    m₁ [M☉]  m₂ [M☉]   M_c [M☉]    35 Hz から合体まで [s]');
console.log('  '+'-'.repeat(88));
const bins=[
  ['GW150914',            36,   29],
  ['GW170817（中性子星）', 1.46, 1.27],
  ['等質量 10+10',        10,   10],
  ['等質量 100+100',      100,  100],
];
for(const [nm,m1,m2] of bins){
  const Mc=chirpMass(m1,m2);
  const tau=tauToMerge(35,Mc*Msun);
  console.log(`  ${nm.padEnd(22)} ${String(m1).padStart(7)}  ${String(m2).padStart(7)}   ${Mc.toFixed(3).padStart(8)}    ${tau.toFixed(3).padStart(14)}`);
}
console.log('\n  ★ GW150914 は 35 Hz から 0.19 秒 で合体 ── 実際の観測（約 0.2 秒）と一致します。');
console.log('    ★ 中性子星の合体は 35 Hz から 37 秒 ── だから長く追跡できた。\n');
console.log('  ★ チャープの形を解きます。df/dt の式を積分すると：\n');
console.log('      f(τ) ∝ τ^(−3/8),      τ = 合体までの残り時間\n');
{
  const Mc=chirpMass(36,29)*Msun;
  console.log('   合体まで τ [s]     f [Hz]      f·τ^(3/8)（一定なら −3/8 乗）');
  console.log('  '+'-'.repeat(68));
  let ref=null;
  for(const tau of [10,1,0.3,0.1,0.03,0.01]){
    // τ から f を逆に解く
    const tau0=G*Mc/(c*c*c);
    const f=Math.pow(tau/(5/256)/Math.pow(tau0,-5/3), -3/8)/Math.PI;
    const q=f*Math.pow(tau,3/8);
    if(ref===null) ref=q;
    console.log(`  ${E(tau).padStart(12)}   ${f.toFixed(2).padStart(9)}      ${q.toFixed(6)}   ${Math.abs(q/ref-1)<1e-9?'★ 一定':''}`);
  }
}
console.log('\n  ★ きっかり −3/8 乗です。第 13 回の双曲線チャープ（−1 乗）とは違う指数 ──');
console.log('    ★ 対数周期にはなりません。「合体までの時間」という特別な時刻があるからです。');
console.log('    ── スケール不変な世界（第 20 回）には特別な時刻がなく、だから 1/t だった。');

console.log('\n##################################################################');
console.log('# 5. 重力波の速さ ── 分散があるか');
console.log('##################################################################\n');
console.log('  GW170817 では、重力波とガンマ線が同時に届きました：\n');
const D=40e6*pc;         // 1.3 億光年 ≒ 40 Mpc
const dtObs=1.7;
console.log(`      距離 D = ${E(D)} m（約 40 Mpc = 1.3 億光年）`);
console.log(`      到着の時間差 Δt = ${dtObs} s（ガンマ線が後）\n`);
const T=D/c;
console.log(`      光の飛行時間 T = D/c = ${E(T)} s = ${(T/yr/1e6).toFixed(1)} 百万年`);
console.log(`      ★ |Δv|/c < Δt/T = ${E(dtObs/T)}\n`);
console.log('  ★ 重力波と光の速さは、10⁻¹⁵ の精度で同じでした。');
console.log('    ── これで「重力波が光より速い／遅い」とする多くの模型が一掃されました。\n');
console.log('  ★ 第 6 回の言葉に翻訳すると、重力子の質量に上限がつきます：\n');
console.log('      ω² = c²k² + (m_g c²/ħ)²      →      遮断周波数がある\n');
const mg=1.27e-23;    // eV（LIGO-Virgo の代表的な上限）
const wc=mg*eV/hbar;
console.log(`      m_g < ${E(mg)} eV（重力波の分散からの上限）`);
console.log(`      遮断周波数 f_c < ${E(wc/(2*Math.PI))} Hz`);
console.log(`      到達距離 λ = c/ω_c > ${E(c/wc)} m = ${(c/wc/pc).toFixed(2)} pc\n`);
console.log('  ★ 重力の到達距離は 0.5 pc 以上 ── 最寄りの恒星までの距離（1.3 pc）の半分弱。\n');
console.log('  ★ 第 17 回の光子の上限と並べてみます：\n');
{
  const mgam=1e-18;   // eV
  const lamG=c/(mgam*eV/hbar);
  console.log('   粒子      質量の上限 [eV]    到達距離の下限 [m]      たとえ');
  console.log('  '+'-'.repeat(76));
  console.log(`   光子      ${E(mgam).padStart(12)}      ${E(lamG).padStart(12)}       ${(lamG/1.496e11).toFixed(1)} AU（第 17 回）`);
  console.log(`   重力子    ${E(mg).padStart(12)}      ${E(c/wc).padStart(12)}       ${(c/wc/pc).toFixed(2)} pc`);
  console.log(`\n      ★ 長さで比べると、重力子の下限のほうが ${E((c/wc)/lamG)} 倍 長い。`);
}
console.log('\n  ★ 第 6 回の「質量があると遮断ができる」が、重力にも当てはまります。');
console.log('    いまのところ、どちらの遮断も見つかっていません。');

console.log('\n##################################################################');
console.log('# 6. 偏光が 45° ── スピンが階数を決める');
console.log('##################################################################\n');
console.log('  電磁波の二つの偏光は 90° で直交します。重力波は 45° です。\n');
console.log('  ★ 理由は「何階のテンソルか」だけ：\n');
const spins=[
  ['音波（縦波）',    0, '──',    '偏光がない'],
  ['電磁波',          1, '90°',   'ベクトル場。双極子放射'],
  ['★ 重力波',       2, '45°',   '★ 二階テンソル場。四重極放射'],
];
console.log('   波            スピン s   偏光の直交角   場の階数');
console.log('  '+'-'.repeat(72));
for(const [a,s,ang,d] of spins)
  console.log(`  ${a.padEnd(14)} ${String(s).padStart(6)}     ${ang.padEnd(10)}  ${d}`);
console.log('\n  ★ 一般に、スピン s の場では偏光が 90°/s で直交します：\n');
for(const s of [1,2]){
  console.log(`      s = ${s} → ${90/s}°`);
}
console.log('\n  ★ そして放射の最低次数も s で決まります ── 2^s 重極。');
console.log('    s=1 なら双極子（2¹）、s=2 なら四重極（2²）。');
console.log('    ★ 「スピン」「多重極の次数」「偏光の角度」は、同じ一つのことの三つの言い方でした。');

console.log('\n##################################################################');
console.log('# 7. 検出の限界 ── 第 22 回の標準量子限界と合流する');
console.log('##################################################################\n');
console.log('  第 22 回で、40 kg の鏡を 100 Hz で測る限界を計算しました：\n');
{
  const m=40, f=100, tau=1/(2*Math.PI*f);
  const dx=Math.sqrt(hbar*tau/m);
  const hSQL=dx/L;
  console.log(`      Δx_SQL = √(ħτ/m) = ${E(dx)} m`);
  console.log(`      h_SQL = Δx/L = ${E(hSQL)}        （腕 L = 4 km）\n`);
  console.log(`      LIGO の設計感度（100 Hz）≈ 4×10⁻²⁴ /√Hz`);
  console.log(`      ★ 同じ桁です ── LIGO はすでに標準量子限界の近くで動いています。\n`);
}
console.log('  ★ だから 2019 年からスクイーズド光を常用しています（第 22 回）。');
console.log('    ★ 「積は動かせないが、配分は選べる」を、重力波望遠鏡が実装している。\n');
console.log('  感度を上げる手立てを、波の言葉で並べます：\n');
const ways=[
  ['腕を長くする',        'L を増やす',      'h = Δx/L。LISA は 250 万 km'],
  ['鏡を重くする',        'm を増やす',      '★ SQL は √(ħτ/m)。40 kg → 100 kg'],
  ['光を強くする',        '散射雑音を下げる','ただし輻射圧雑音が増える'],
  ['★ スクイーズ',       '配分を変える',    '★ 6 dB で 2 倍（第 22 回）'],
  ['低周波へ行く',        'τ を伸ばす',      '★ 地面振動との戦い → 宇宙へ'],
];
console.log('   手立て            何を変えるか        中身');
console.log('  '+'-'.repeat(80));
for(const [a,b,cc] of ways) console.log(`  ${a.padEnd(16)} ${b.padEnd(18)} ${cc}`);

console.log('\n##################################################################');
console.log('# 8. 周波数帯の梯子 ── 第 3 回の観測窓に重力波を載せる');
console.log('##################################################################\n');
console.log('  第 3 回で「観測窓より長い周期は定数に見える」と書きました。');
console.log('  ★ 重力波にも、同じ梯子があります：\n');
const bands=[
  ['地上干渉計（LIGO）',    10,      5000,    '恒星質量のブラックホール合体'],
  ['宇宙干渉計（LISA）',    1e-4,    1e-1,    '超大質量ブラックホール、白色矮星'],
  ['パルサータイミング',     1e-9,    1e-7,    '★ 超大質量連星の背景'],
  ['宇宙背景放射（B モード）',1e-18,  1e-16,   '★ インフレーション起源'],
];
console.log('   手法                     下限 [Hz]   上限 [Hz]     周期          対象');
console.log('  '+'-'.repeat(96));
for(const [nm,lo,hi,tg] of bands){
  const per=1/lo;
  let ps;
  if(per<60) ps=per.toFixed(2)+' 秒';
  else if(per<yr) ps=(per/86400).toFixed(1)+' 日';
  else ps=(per/yr).toExponential(1)+' 年';
  console.log(`  ${nm.padEnd(24)} ${E(lo).padStart(9)}   ${E(hi).padStart(9)}     ${ps.padEnd(12)} ${tg}`);
}
console.log('\n  ★ 一番下の帯は周期 10¹⁸ 秒 ＝ 300 億年 ── 宇宙年齢より長い。');
console.log('    ★ だから直接は測れず、「偏光の模様」として痕跡を探します。');
console.log('    ── 第 3 回の「ω=0 には手が届かない」が、そのまま重力波にも当てはまる。\n');
console.log('  ★ そして 2023 年、パルサータイミングの帯（周期 数年）で');
console.log('    ★ 背景重力波の兆候が報告されました ── 超大質量ブラックホール連星の合唱。');
console.log('      判定：複数の観測チームが同様の結果を出していますが、起源はまだ確定していません。');

console.log('\n##################################################################');
console.log('# 9. まとめ');
console.log('##################################################################\n');
const sm=[
  ['h は無次元',              '◎ 定義',  '第 7 回がここでは定義になる'],
  ['四重極から出る',          '◎ 厳密',  '★ 単極子・双極子は保存則で消える'],
  ['P ∝ (三階微分)²',        '◎ 厳密',  '★ 電磁波より階数が一つ上'],
  ['基準は c⁵/G = 3.6×10⁵² W','◎ 計算',  'G と c だけでできている'],
  ['地球での流束 3 mW/m²',    '◎ 計算',  '★ 満月の光と同じ桁'],
  ['チャープは τ^(−3/8)',     '◎ 数値',  '第 13 回の 1/t とは違う'],
  ['35 Hz から 0.19 秒',      '◎ 計算',  'GW150914。観測（約 0.2 秒）と一致'],
  ['|Δv|/c < 4×10⁻¹⁶',      '○ 実測',  'GW170817。重力子質量の上限'],
  ['偏光は 45°',             '◎ 厳密',  '★ スピン 2 ＝ 二階テンソル'],
  ['LIGO は SQL の近く',      '◎ 計算',  '★ 第 22 回と合流'],
];
console.log('  主張                      判定      根拠');
console.log('  '+'-'.repeat(76));
for(const [a,b,cc] of sm) console.log(`  ${a.padEnd(24)} ${b.padEnd(9)} ${cc}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     重力波は、階数が一つ上の放射だった。');
console.log('     電磁波が双極子の二階微分なら、重力波は四重極の三階微分。');
console.log('     ── そして測る量は長さの比。無次元だけが物理、がここでは定義になっている。');
