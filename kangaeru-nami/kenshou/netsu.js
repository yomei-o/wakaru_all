// 熱は波として伝わらない ── 拡散の分散関係と、周波数で決まる深さ
'use strict';
const E=x=>x.toExponential(3);
const YR=3.155760e7, DAY=86400;
const mu0=4*Math.PI*1e-7;

console.log('##################################################################');
console.log('# 1. 拡散方程式の分散関係は、純虚数である');
console.log('##################################################################\n');
console.log('      ∂u/∂t = D ∂²u/∂x²\n');
console.log('  平面波 exp(i(kx − ωt)) を入れると：\n');
console.log('      −iω = −D k²      →      ω = −i D k²\n');
console.log('  ★ ω が純虚数。第 6 回で見た波の分散関係とは、根本的に違います。\n');
const comp=[
  ['波動方程式',      'ω = ck',            '実数',   '伝わる。減衰しない'],
  ['クライン＝ゴルドン','ω² = c²k² + ω_c²',  '実数（遮断以上）','伝わる'],
  ['拡散方程式',      'ω = −iDk²',         '★ 純虚数','伝わらない。その場で減衰する'],
];
console.log('  方程式              分散関係            ω の型        振る舞い');
console.log('  '+'-'.repeat(80));
for(const [a,b,c,d] of comp) console.log(`  ${a.padEnd(18)} ${b.padEnd(18)} ${c.padEnd(12)} ${d}`);
console.log('\n  ★ 「熱が伝わる」という日常語は、物理的には正しくありません。');
console.log('    熱は伝播しません。ただ、時間とともに広がって薄まるだけです。');

console.log('\n##################################################################');
console.log('# 2. ただし「周期的に温める」なら、話が変わる');
console.log('##################################################################\n');
console.log('  表面を ω で振動させると（昼夜・季節・交流電流）、');
console.log('  ω を実数に固定して k を解くことになります：\n');
console.log('      k² = iω/D      →      k = (1+i)/δ,      δ = √(2D/ω)\n');
console.log('  実部と虚部が同じ大きさ ── つまり\n');
console.log('      T(x,t) = T₀ e^(−x/δ) cos(ωt − x/δ)\n');
console.log('  ★ 深さ δ で振幅が 1/e に落ち、同時に位相が 1 ラジアン遅れる。');
console.log('    「減衰」と「遅れ」が、常に同じ長さで起きます。\n');
console.log('  ★ この δ を「浸透深さ」と呼びます。周波数で決まる ── ');
console.log('    つまり土も金属も、周波数ごとに違う厚さの「フィルタ」です。');

console.log('\n##################################################################');
console.log('# 3. 地面の温度 ── 昼夜の波と、季節の波');
console.log('##################################################################\n');
const Dsoil=5e-7;      // m²/s（典型的な土壌）
console.log(`  土壌の熱拡散率 D = ${E(Dsoil)} m²/s\n`);
console.log('  周期          ω [rad/s]      浸透深さ δ [m]    位相遅れ 1 rad の日数');
console.log('  '+'-'.repeat(76));
const periods=[
  ['1 時間',   3600],
  ['1 日',     DAY],
  ['1 か月',   30*DAY],
  ['1 年',     YR],
  ['100 年',   100*YR],
];
for(const [nm,P] of periods){
  const w=2*Math.PI/P;
  const d=Math.sqrt(2*Dsoil/w);
  console.log(`  ${nm.padEnd(10)} ${E(w)}    ${d.toFixed(3).padStart(9)}        ${(P/(2*Math.PI)/DAY).toFixed(2)} 日`);
}
console.log('\n  ★ 昼夜の波は 12 cm、季節の波は 2.2 m。');
console.log('    ── 地下 1 m では昼夜の変動が e^(−8.5) ≈ 0.02 % に落ち、');
console.log('      季節の変動だけが残ります。\n');
const dAnn=Math.sqrt(2*Dsoil/(2*Math.PI/YR));
console.log('  そして位相の遅れが、面白いことを起こします：\n');
console.log('   深さ [m]   振幅（地表比）   位相遅れ [rad]   遅れ [日]   何が起きるか');
console.log('  '+'-'.repeat(84));
for(const z of [0,1,2,dAnn,5,7,Math.PI*dAnn,10]){
  const amp=Math.exp(-z/dAnn);
  const ph=z/dAnn;
  const days=ph/(2*Math.PI)*365.25;
  let note='';
  if(Math.abs(z-dAnn)<0.01) note='★ 振幅 1/e、遅れ 58 日';
  if(Math.abs(z-Math.PI*dAnn)<0.01) note='★★ 遅れが半年 ── 冬に最も暖かい';
  console.log(`  ${z.toFixed(2).padStart(7)}    ${amp.toFixed(4).padStart(9)}      ${ph.toFixed(3).padStart(9)}     ${days.toFixed(1).padStart(7)}    ${note}`);
}
console.log('\n  ★ 深さ πδ = 7.0 m で、季節が半年 ずれます。');
console.log('    地下 7 m は「冬に最も暖かく、夏に最も冷たい」。');
console.log('    ── 昔の氷室や地下貯蔵庫が効くのは、この位相遅れのおかげです。');

console.log('\n##################################################################');
console.log('# 4. まったく同じ式が、電磁気に出る ── 表皮効果');
console.log('##################################################################\n');
console.log('  良導体の中では、マクスウェル方程式が拡散方程式になります：\n');
console.log('      ∂B/∂t = (1/μσ) ∇²B        D_em = 1/(μσ)\n');
console.log('  ★ 熱伝導と一字一句 同じ形。D が違うだけです。\n');
const metals=[
  ['銅',      1.68e-8],
  ['アルミ',   2.65e-8],
  ['鉄',      9.71e-8],
  ['ステンレス',6.9e-7],
];
console.log('  金属        抵抗率 [Ω·m]    D_em = ρ/μ [m²/s]   土壌の熱 D の何倍');
console.log('  '+'-'.repeat(76));
for(const [nm,rho] of metals){
  const D=rho/mu0;
  console.log(`  ${nm.padEnd(10)} ${E(rho)}     ${E(D)}        ${E(D/Dsoil)}`);
}
console.log('\n  ★ 電磁場の「拡散率」は、土の熱の 10⁴ 倍。だから浅く速く効きます。\n');
const rhoCu=1.68e-8;
console.log('  銅の表皮深さ δ = √(2ρ/μω)：\n');
console.log('   周波数        ω [rad/s]       δ [m]           δ');
console.log('  '+'-'.repeat(68));
for(const [nm,f] of [['50 Hz（商用）',50],['1 kHz',1e3],['1 MHz',1e6],['1 GHz',1e9],['10 GHz',1e10]]){
  const w=2*Math.PI*f;
  const d=Math.sqrt(2*rhoCu/(mu0*w));
  const s = d>1e-3 ? (d*1e3).toFixed(2)+' mm' : (d>1e-6 ? (d*1e6).toFixed(2)+' μm' : (d*1e9).toFixed(1)+' nm');
  console.log(`  ${nm.padEnd(14)} ${E(w)}    ${E(d)}     ${s}`);
}
console.log('\n  ★ 50 Hz で 9.2 mm、1 GHz で 2.1 μm。');
console.log('    ── 高周波の電線が「中空でよい」のも、金メッキが効くのも、これです。');
console.log('    そして地面の温度と、まったく同じ数式から出ています。');

console.log('\n##################################################################');
console.log('# 5. 微積分の言葉では、何が起きているのか');
console.log('##################################################################\n');
console.log('  第 1 回の見方で拡散方程式を読むと：\n');
console.log('      時間について 1 階（奇数）  →  ★ 不可逆（第 10 回）');
console.log('      空間について 2 階（偶数）  →  空間反転では対称\n');
console.log('  ★ 時間と空間で階数が違う ── これが拡散の本質です。\n');
const orders=[
  ['波動方程式',   2, 2, '同じ',   '○ 可逆。伝播する'],
  ['拡散方程式',   1, 2, '★ 違う', '× 不可逆。伝播しない'],
  ['シュレーディンガー', 1, 2, '違う', '○ 可逆（i のおかげ）'],
];
console.log('  方程式              時間の階数  空間の階数   階数   性質');
console.log('  '+'-'.repeat(80));
for(const [a,t,x,c,d] of orders)
  console.log(`  ${a.padEnd(18)} ${String(t).padStart(6)}      ${String(x).padStart(6)}     ${c.padEnd(6)} ${d}`);
console.log('\n  ★ 時間 1 階・空間 2 階だと、ω ∝ k² となって ω が純虚数になる。');
console.log('    「伝わらない」の起源は、階数の不釣り合いでした。\n');
console.log('  そして シュレーディンガー方程式は、まったく同じ階数の組み合わせなのに');
console.log('  i が一つ入るだけで可逆になり、波として伝播します ──');
console.log('  ★ 拡散方程式は「虚時間のシュレーディンガー方程式」と呼ばれる所以です。');
console.log(`    実際、t → −i t と置くと二つは移り合います。`);

console.log('\n##################################################################');
console.log('# 6. では、熱を「波として」伝えることはできるのか ── できます');
console.log('##################################################################\n');
console.log('  拡散方程式に時間 2 階の項を足すと、双曲型になります（カッタネオ）：\n');
console.log('      τ ∂²T/∂t² + ∂T/∂t = D ∇²T\n');
console.log('  分散関係は  −τω² − iω = −Dk²  となり、\n');
console.log('      ωτ ≫ 1 なら  ω ≈ ± k√(D/τ)     ★ 実数 ── 波として伝わる');
console.log('      ωτ ≪ 1 なら  ω ≈ −iDk²          いつもの拡散\n');
console.log('  ★ 遮断周波数 ω_c = 1/τ を境に、拡散から波へ切り替わります。');
console.log('    第 6 回の質量とは逆で、こちらは「高域通過」です。\n');
const cattaneo=[
  ['金属（電子）',    1e-11,  1e-4],
  ['半導体',        1e-11,  1e-5],
  ['誘電体',        1e-12,  1e-6],
  ['超流動ヘリウム',  1e-5,   1e-7],
];
console.log('  物質            緩和時間 τ [s]   D [m²/s]    遮断 1/τ [Hz]   第二音の速さ √(D/τ) [m/s]');
console.log('  '+'-'.repeat(92));
for(const [nm,tau,D] of cattaneo){
  const fc=1/tau/(2*Math.PI);
  const v=Math.sqrt(D/tau);
  console.log(`  ${nm.padEnd(14)} ${E(tau)}    ${E(D)}   ${E(fc)}      ${v.toFixed(1).padStart(8)}`);
}
console.log('\n  ★ ふつうの物質では遮断が 10^10〜10^11 Hz ── 日常では届きません。');
console.log('    だから熱は「拡散するもの」に見えます。\n');
console.log('  ★ しかし超流動ヘリウムでは τ が 10⁶ 倍 長く、遮断が 10 kHz 級。');
console.log('    そこでは熱が本当に波として伝わります ── 第二音（1944 年に観測）。');
console.log('    音速は 20 m/s 程度で、通常の音（240 m/s）よりずっと遅い。');

console.log('\n##################################################################');
console.log('# 7. まとめ');
console.log('##################################################################\n');
const summary=[
  ['ω = −iDk²',        '◎ 厳密',  '純虚数 ── 伝播せず、その場で減衰'],
  ['浸透深さ δ=√(2D/ω)','◎ 厳密',  '減衰と位相遅れが、同じ長さで起きる'],
  ['地面：昼夜 12 cm',  '◎ 計算',  '季節は 2.2 m。7 m で半年ずれる'],
  ['表皮効果は同じ式',   '◎ 同型',  'D = ρ/μ に置き換えるだけ'],
  ['不可逆の起源',      '◎ 分類',  '時間 1 階・空間 2 階という不釣り合い'],
  ['熱も波にできる',    '○ 実測',  'カッタネオ。超流動 He の第二音'],
];
console.log('  主張                  判定      根拠');
console.log('  '+'-'.repeat(70));
for(const [a,b,c] of summary) console.log(`  ${a.padEnd(20)} ${b.padEnd(9)} ${c}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     熱は波として伝わらない。時間 1 階・空間 2 階だから。');
console.log('     ところが時間 2 階の項を足すと、遮断周波数の上で波に変わる。');
console.log('     ── 「伝わるか、薄まるか」は、階数の組み合わせで決まっていた。');
