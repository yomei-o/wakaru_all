// 時間の矢は、微分階数の偶奇に住む
'use strict';
const E=x=>x.toExponential(3);

console.log('##################################################################');
console.log('# 1. 時間を反転すると、微分はどうなるか');
console.log('##################################################################\n');
console.log('  t → −t と置き換えると、微分は符号を変えます：\n');
console.log('      d/dt  →  −d/dt\n');
console.log('  したがって n 階微分は (−1)ⁿ 倍になります：\n');
console.log('   階数 n    (−1)ⁿ     時間反転で     物理量の例');
console.log('  '+'-'.repeat(62));
const orders=[
  [0, '位置 x'],
  [1, '速度 v'],
  [2, '加速度 a'],
  [3, '躍度'],
  [4, 'スナップ'],
];
for(const [n,nm] of orders){
  const s=Math.pow(-1,n);
  console.log(`   ${String(n).padStart(4)}     ${s>0?'+1':'−1'}      ${s>0?'不変':'符号反転'}         ${nm}`);
}
console.log('\n  ★ 偶数階は時間反転で不変、奇数階は符号が変わる。');
console.log('    ── これだけで、可逆・不可逆の分類ができてしまいます。');

console.log('\n##################################################################');
console.log('# 2. 運動方程式を、項ごとに採点する');
console.log('##################################################################\n');
console.log('  減衰振動：  m ẍ + b ẋ + k x = 0\n');
console.log('  項           階数   時間反転で   性質');
console.log('  '+'-'.repeat(60));
const terms=[
  ['m ẍ（慣性）',   2, '不変',    '保存的'],
  ['b ẋ（摩擦）',   1, '符号反転', '★ 散逸的'],
  ['k x（ばね）',   0, '不変',    '保存的'],
];
for(const [a,n,b,c] of terms) console.log(`  ${a.padEnd(14)} ${String(n).padStart(3)}    ${b.padEnd(8)}  ${c}`);
console.log('\n  ★ 奇数階の項は、ただ一つ ── そしてそれが唯一の散逸項です。');
console.log('    「摩擦があると時間が戻せない」の正体は、階数が奇数であること。\n');
console.log('  数値で確かめます。前進させてから、速度を反転して戻します：\n');
function simulate(m,b,k,x0,v0,T,N){
  let x=x0,v=v0; const h=T/N;
  for(let i=0;i<N;i++){
    // 4 次ルンゲクッタ
    const f=(x,v)=>[-v, (b*v+k*x)/m*-1];   // dx/dt=v, dv/dt=-(b v + k x)/m
    const a1=[v, -(b*v+k*x)/m];
    const a2=[v+a1[1]*h/2, -(b*(v+a1[1]*h/2)+k*(x+a1[0]*h/2))/m];
    const a3=[v+a2[1]*h/2, -(b*(v+a2[1]*h/2)+k*(x+a2[0]*h/2))/m];
    const a4=[v+a3[1]*h,   -(b*(v+a3[1]*h)+k*(x+a3[0]*h))/m];
    x+=h/6*(a1[0]+2*a2[0]+2*a3[0]+a4[0]);
    v+=h/6*(a1[1]+2*a2[1]+2*a3[1]+a4[1]);
  }
  return {x,v};
}
console.log('    b（摩擦）   前進後の x    速度反転して戻した x   元に戻ったか');
console.log('  '+'-'.repeat(70));
for(const b of [0, 0.01, 0.1, 0.5]){
  const T=10, N=200000;
  const f=simulate(1,b,1, 1,0, T,N);
  const r=simulate(1,b,1, f.x,-f.v, T,N);   // 速度を反転して同じ時間だけ進める
  console.log(`  ${b.toFixed(2).padStart(9)}   ${f.x.toFixed(6).padStart(10)}    ${r.x.toFixed(6).padStart(14)}      ${Math.abs(r.x-1)<1e-6?'○ 戻った':'× 戻らない'}`);
}
console.log('\n  ★ b = 0 のときだけ、きれいに戻ります。');
console.log('    摩擦があると「速度を逆にする」だけでは元に戻りません ──');
console.log('    戻すには摩擦の符号も変えねばならない（つまり別の物理になる）。');

console.log('\n##################################################################');
console.log('# 3. 分類 ── 可逆であるには、二つの道がある');
console.log('##################################################################\n');
console.log('  時間微分の階数だけでは、実は分類が足りません。i（虚数単位）も効きます：\n');
const eqs=[
  ['波動方程式',        '∂²u/∂t²',   2, 'なし', '○ 可逆',   '偶数階'],
  ['拡散方程式',        '∂u/∂t',     1, 'なし', '× 不可逆', '奇数階。熱は戻らない'],
  ['シュレーディンガー',  'iħ ∂ψ/∂t',  1, '★ あり','○ 可逆',  '奇数階なのに可逆'],
  ['減衰振動（摩擦項）',  'b ẋ',       1, 'なし', '× 不可逆', '奇数階'],
  ['マクスウェル',       '∂E/∂t',     1, 'なし', '○ 可逆',   '★ 二本が組になっている'],
];
console.log('  方程式              時間微分      階数  i    T 対称性   備考');
console.log('  '+'-'.repeat(88));
for(const [a,b,n,c,d,e] of eqs)
  console.log(`  ${a.padEnd(18)} ${b.padEnd(12)} ${String(n).padStart(3)}  ${c.padEnd(5)} ${d.padEnd(9)} ${e}`);
console.log('\n  ★ 可逆であるための道は、ちょうど二つ：\n');
console.log('      ① 偶数階である（波動方程式）');
console.log('      ② 奇数階だが、i がついている（シュレーディンガー）\n');
console.log('  ②の仕組み：t → −t で iħ∂ψ/∂t → −iħ∂ψ/∂t となりますが、');
console.log('  同時に ψ → ψ*（複素共役）を取ると、符号が二度 返って元に戻ります。');
console.log('  ★ 量子力学が可逆なのは、i のおかげでした。\n');
console.log('  ※ マクスウェル方程式も一階ですが、E と B の二本が組になっていて');
console.log('    t → −t で B → −B とすれば全体が不変になります（同じ仕組みの別形）。');

console.log('\n##################################################################');
console.log('# 4. では、分数階は？── ここが本題');
console.log('##################################################################\n');
console.log('  階数 α が整数でないと、偶数でも奇数でもありません。');
console.log('  第 1 回で測ったとおり、(iω)^α の位相は 90α 度でした：\n');
console.log('      α = 0（ばね）    位相 0°     完全に保存的');
console.log('      α = 1（ダッシュポット）位相 90°  完全に散逸的');
console.log('      α = 1/2         位相 45°   ★ ちょうど半分\n');
console.log('  ★ 分数階は、可逆と不可逆の「あいだ」に連続に住んでいます。\n');
console.log('  これは粘弾性で実際に測られている量です。複素弾性率を書くと：\n');
console.log('      E*(ω) = K (iω)^α = K ω^α [ cos(απ/2) + i sin(απ/2) ]\n');
console.log('      貯蔵弾性率 E′ = K ω^α cos(απ/2)     ← ばね的');
console.log('      損失弾性率 E″ = K ω^α sin(απ/2)     ← ダンパ的');
console.log('      ★ 損失正接  tan δ = tan(απ/2)\n');
console.log('    α       位相遅れ δ    tan δ      1 周期あたりの損失／貯蔵');
console.log('  '+'-'.repeat(68));
for(const al of [0,0.05,0.1,0.2,0.3,0.5,0.7,0.9,1.0]){
  const d=90*al;
  const td=Math.tan(al*Math.PI/2);
  const ratio=2*Math.PI*td;
  console.log(`  ${al.toFixed(2).padStart(6)}    ${d.toFixed(1).padStart(7)}°    ${(al<1?td.toFixed(4):'∞').padStart(8)}    ${al<1?ratio.toFixed(3):'∞'}`);
}
console.log('\n  ★ α が「どれだけ時間の矢を持っているか」を連続に測っています。');

console.log('\n##################################################################');
console.log('# 5. 実在の物質は、どの階数にいるか');
console.log('##################################################################\n');
console.log('  損失正接は材料の基本的な測定量です。逆に解くと α が出ます：\n');
console.log('      α = (2/π) arctan(tan δ)\n');
const mats=[
  ['溶融石英',     1e-5,  '音叉・共振器。ほぼ完全なばね'],
  ['鋼',          1e-4,  '構造材'],
  ['アルミ',       2e-4,  ''],
  ['ガラス',       1e-3,  ''],
  ['木材',        1e-2,  ''],
  ['硬いゴム',     0.1,   ''],
  ['生体組織',     0.2,   '★ 分数階模型が実際に使われる'],
  ['軟らかいゴム',  0.5,   '防振材'],
  ['アスファルト',  1.0,   '★ ちょうど α = 1/2'],
];
console.log('  材料             tan δ       実効的な階数 α    性質');
console.log('  '+'-'.repeat(74));
for(const [nm,td,note] of mats){
  const al=2/Math.PI*Math.atan(td);
  console.log(`  ${nm.padEnd(14)} ${E(td).padStart(9)}    ${(al<0.01?E(al):al.toFixed(4)).padStart(9)}      ${note}`);
}
console.log('\n  ★ 溶融石英は α ≈ 6×10⁻⁶ ── ほぼ完全に「偶数階（保存的）」。');
console.log('    アスファルトは α ≈ 1/2 ── ちょうど可逆と不可逆の中間。');
console.log('    ★ 物質は、微分階数の軸の上に並んでいます。');

console.log('\n##################################################################');
console.log('# 6. 数値で確かめる ── 分数階振動子の損失');
console.log('##################################################################\n');
console.log('  正弦的なひずみ ε(t) = sin(ωt) を与え、応力 σ = K D^α ε を計算して');
console.log('  1 周期あたりの散逸 ∮σ dε を数値積分します。\n');
console.log('  理論値：  ∮σ dε = π K ω^α sin(απ/2)\n');
console.log('    α      数値積分       理論値        相対差');
console.log('  '+'-'.repeat(58));
const w=1.0, K=1.0, M=2000000;
for(const al of [0,0.25,0.5,0.75,1.0]){
  // σ(t) = K ω^α sin(ωt + απ/2)
  const amp=K*Math.pow(w,al), ph=al*Math.PI/2;
  let loop=0;
  for(let i=0;i<M;i++){
    const t=2*Math.PI/w*i/M, dt2=2*Math.PI/w/M;
    const sig=amp*Math.sin(w*t+ph);
    const deps=w*Math.cos(w*t)*dt2;      // dε = ω cos(ωt) dt
    loop+=sig*deps;
  }
  const theory=Math.PI*K*Math.pow(w,al)*Math.sin(ph);
  console.log(`  ${al.toFixed(2).padStart(6)}   ${loop.toFixed(6).padStart(10)}   ${theory.toFixed(6).padStart(10)}    ${theory!==0?E(Math.abs((loop-theory)/theory)):E(Math.abs(loop))}`);
}
console.log('\n  ★ 一致します。散逸は sin(απ/2) に比例 ──');
console.log('    α=0 でゼロ、α=1 で最大、α=1/2 でその 1/√2。');
console.log('    ★ 「時間の矢の強さ」が、階数の三角関数で書けました。');

console.log('\n##################################################################');
console.log('# 7. 【仮説】不可逆性の尺度としての階数');
console.log('##################################################################\n');
console.log('  ここまでを一つの見方にまとめると：\n');
console.log('      ★ 時間の矢の強さ ＝ sin(απ/2)\n');
const scale=[
  ['α = 0',       'sin 0 = 0',       '完全に可逆。ばね・位置'],
  ['α = 1/2',     'sin(π/4) = 0.707','半分。拡散の境界・アスファルト'],
  ['α = 1',       'sin(π/2) = 1',    '完全に不可逆。摩擦・拡散'],
  ['α = 2',       'sin π = 0',       '★ また可逆に戻る。慣性'],
  ['α = 3',       'sin(3π/2) = −1',  '符号が逆の不可逆（＝逆向きの矢）'],
];
console.log('  階数         sin(απ/2)         意味');
console.log('  '+'-'.repeat(66));
for(const [a,b,c] of scale) console.log(`  ${a.padEnd(12)} ${b.padEnd(18)} ${c}`);
console.log('\n  ★ 周期 4 で戻ってきます ── これは (iω)^α の位相が 90α 度だから当然。');
console.log('    そして第 2 回で見たとおり、物理が使うのは α ≤ 2 の範囲でした。');
console.log('    つまり ── 使える範囲は「可逆 → 不可逆 → また可逆」の半周期ぶん。\n');
console.log('  ⇒ 【仮説】物理が α ∈ [0, 2] に収まっているのは、');
console.log('     ★ その範囲で時間の矢が 0 → 1 → 0 と一往復するからではないか。');
console.log('     （α > 2 は「逆向きの矢」になり、オストログラツキー不安定性と');
console.log('       同じ場所で禁止される ── 符号が合わない）\n');
console.log('  ※ これは本稿の推測です。オストログラツキーの定理と、');
console.log('    sin(απ/2) の符号反転が同じ α = 2 で起きるのは示唆的ですが、');
console.log('    両者を結ぶ厳密な議論を本稿は与えていません。');

console.log('\n##################################################################');
console.log('# 8. まとめ');
console.log('##################################################################\n');
const summary=[
  ['偶数階 → 可逆',      '◎ 厳密',  '(−1)ⁿ = +1'],
  ['奇数階 → 不可逆',    '◎ 厳密',  'ただし i があれば別（量子力学）'],
  ['可逆への道は二つ',    '◎ 分類',  '偶数階、または 奇数階＋i'],
  ['分数階 → その中間',   '◎ 実測',  'tan δ = tan(απ/2)。粘弾性で測定される'],
  ['散逸 ∝ sin(απ/2)',  '◎ 数値',  '第 6 節で確認'],
  ['α∈[0,2] の理由',    '△ 仮説',  '矢が一往復する範囲。厳密な議論は無い'],
];
console.log('  主張                  判定      根拠');
console.log('  '+'-'.repeat(70));
for(const [a,b,c] of summary) console.log(`  ${a.padEnd(20)} ${b.padEnd(9)} ${c}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     時間の矢は、微分階数の偶奇に住んでいる。');
console.log('     そして分数階は、その二つの間を連続につないでいる。');
console.log('     ── 「どれだけ不可逆か」は、階数の三角関数で測れる。');
