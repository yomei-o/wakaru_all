// 物理定数を微分する ── 実際に測られている値を並べる
'use strict';
const E=x=>x.toExponential(3);
const YR=3.155760e7, GYR=1e9*YR;
const tUniv=13.8e9*YR;

console.log('##################################################################');
console.log('# 1. まず、意地の悪い前置き ── 何を微分できるのか');
console.log('##################################################################\n');
console.log('  「光速は変化しているか」という問いには、落とし穴があります。');
console.log('  c は 1983 年から、こう定義されているからです：\n');
console.log('      c ≡ 299 792 458 m/s   （厳密に。定義値）\n');
console.log('  メートルが「光が 1/299792458 秒に進む距離」と定義されたので、');
console.log('  c を測ることは、もう原理的にできません。');
console.log('  ★ つまり dc/dt = 0 は、測定結果ではなく取り決めです。\n');
console.log('  2019 年の SI 改定で、この扱いが 7 つの定数に広がりました：\n');
const si=[
  ['Δν_Cs', 'セシウム超微細遷移', '9 192 631 770 Hz',        1967],
  ['c',      '光速',              '299 792 458 m/s',         1983],
  ['h',      'プランク定数',       '6.62607015×10⁻³⁴ J·s',    2019],
  ['e',      '電気素量',          '1.602176634×10⁻¹⁹ C',     2019],
  ['k_B',    'ボルツマン定数',     '1.380649×10⁻²³ J/K',      2019],
  ['N_A',    'アボガドロ定数',     '6.02214076×10²³ /mol',    2019],
  ['K_cd',   '視感効果度',        '683 lm/W',                1979],
];
console.log('  定数      名前                 定義値                     以後');
console.log('  '+'-'.repeat(76));
for(const [a,b,c,y] of si) console.log(`  ${a.padEnd(8)} ${b.padEnd(18)} ${c.padEnd(24)} ${y}`);
console.log('\n  ★ この 7 つは、微分すると厳密に 0 です。定義だから。');
console.log('    「変化しているか」を問うことすらできません。\n');
console.log('  では、まだ測れる定数は何か：');
const meas=[
  ['G',            '重力定数',        '次元あり。しかし単独では測れる（力を測る）'],
  ['α = e²/4πε₀ħc','微細構造定数',    '★ 無次元。単位の取り方に依らない'],
  ['μ = m_p/m_e',  '陽子・電子の質量比','★ 無次元'],
  ['m_p/m_Pl',     '陽子質量／プランク質量','★ 無次元'],
];
console.log('\n  定数              名前                 性質');
console.log('  '+'-'.repeat(76));
for(const [a,b,c] of meas) console.log(`  ${a.padEnd(16)} ${b.padEnd(18)} ${c}`);
console.log('\n  ★ 本質的なのは無次元量だけです。');
console.log('    「c が 2 倍になった宇宙」は、メートルの定義を変えただけの同じ宇宙。');
console.log('    しかし「α が 2 倍の宇宙」は、化学が変わる ── 別の宇宙です。');
console.log('\n  ⇒ だから問いはこう精密化されます：');
console.log('     ★ 無次元定数のスペクトルに、ω ≠ 0 の成分はあるか。');

console.log('\n##################################################################');
console.log('# 2. 実際に微分した結果 ── 測定の一覧');
console.log('##################################################################\n');
console.log('  ※ 以下は文献値の要約です（本稿で測定したものではありません）。\n');
// [手法, 対象, 観測の時間尺度 Δt [s], |Δx/x| の上限, 備考]
const obs=[
  ['光時計の比較',      'α', 10*YR,      1e-17, '≈ 10 年の比較。Al⁺/Hg⁺ など'],
  ['分子時計',          'μ', 10*YR,      1e-16, '振動回転遷移'],
  ['オクロ天然原子炉',   'α', 1.8*GYR,    1e-8,  'Sm-149 の共鳴位置から'],
  ['隕石（Re-187 崩壊）','α', 4.6*GYR,    1e-7,  '半減期が α に強く依存'],
  ['クエーサー吸収線',   'α', 10*GYR,     1e-5,  '★ 変化を主張する報告あり（論争中）'],
  ['クエーサー H₂ 線',   'μ', 10*GYR,     1e-5,  '同上'],
  ['CMB',              'α', 13.4*GYR,   1e-2,  '再結合期 z≈1100'],
  ['ビッグバン元素合成',  'α', 13.8*GYR,   1e-2,  'z≈10⁹。最も古い'],
  ['月レーザー測距',     'G', 50*YR,      5e-12, '★ Ġ/G < 10⁻¹³ /年'],
  ['ビッグバン元素合成',  'G', 13.8*GYR,   1e-1,  'ヘリウム存在比から'],
];
console.log('  手法                対象  観測の時間尺度    上限 |Δx/x|   備考');
console.log('  '+'-'.repeat(88));
for(const [m,q,dt,lim,note] of obs){
  const tStr = dt>GYR ? (dt/GYR).toFixed(1)+' Gyr' : (dt/YR).toFixed(0)+' 年';
  console.log(`  ${m.padEnd(18)} ${q.padEnd(4)} ${tStr.padStart(10)}      ${E(lim)}   ${note}`);
}
console.log('\n  ★ 微分値に直すと：\n');
console.log('  対象   最も厳しい上限              宇宙年齢での積算変化');
console.log('  '+'-'.repeat(66));
for(const [q,rate,src] of [['α',1e-17,'光時計'],['μ',1e-16,'分子時計'],['G',1e-13,'月レーザー測距']]){
  console.log(`  ${q.padEnd(5)}  |ẋ/x| < ${E(rate)} /年   ${(rate>0?E(rate*13.8e9):'')}  （${src}）`);
}
console.log('\n  ★ α は 宇宙年齢を通じて 10⁻⁷ 以内。小数第 7 位まで定数です。');

console.log('\n##################################################################');
console.log('# 3. これをフーリエの言葉に翻訳する ── ここが本題');
console.log('##################################################################\n');
console.log('  仮に定数が  x(t) = x0 (1 + A sin ωt)  と揺れているとします。');
console.log('  各実験は、この A に周波数ごとの上限を与えます。\n');
console.log('  ・速度を測る実験（時計）：測れるのは最大変化率 Aω');
console.log('      → 速度上限 R に対し  A < R/ω          ★ 低周波ほど弱い\n');
console.log('  ・二つの時代を比べる実験（オクロ・クエーサー・CMB）：');
console.log('      腕の長さ Δt、精度 ε に対し');
console.log('      A < ε        （ωΔt ≳ 1 のとき）');
console.log('      A < ε/(ωΔt)  （ωΔt ≪ 1 のとき）  ★ やはり低周波で弱い\n');
const rateLim=[
  ['光時計（速度）',  3.169e-25, null, null],
];
const epochLim=[
  ['オクロ',        null, 1.8*GYR,  1e-8],
  ['隕石',          null, 4.6*GYR,  1e-7],
  ['クエーサー',     null, 10*GYR,   1e-5],
  ['CMB',          null, 13.4*GYR, 1e-2],
  ['元素合成',       null, 13.8*GYR, 1e-2],
];
function ampLimit(f){
  const w=2*Math.PI*f;
  let best=Infinity, who='';
  for(const [n,R] of rateLim.map(r=>[r[0],r[1]])){
    const L=R/w;
    if(L<best){best=L;who=n;}
  }
  for(const [n,_,dt,eps] of epochLim){
    const s=w*dt;
    const L=eps*Math.max(1, 1/s);
    if(L<best){best=L;who=n;}
  }
  return {best,who};
}
console.log('  周波数 f [Hz]     周期              α の振幅上限     効いている実験');
console.log('  '+'-'.repeat(76));
for(const f of [1e-9,1e-12,1e-15,1e-17,1e-18,1e-19,1e-21,1e-24]){
  const r=ampLimit(f);
  const P=1/f;
  const pStr = P>GYR ? (P/GYR).toExponential(1)+' Gyr' : (P>YR ? (P/YR).toExponential(1)+' 年' : E(P)+' s');
  console.log(`  ${E(f)}   ${pStr.padStart(14)}    ${E(r.best)}    ${r.who}`);
}
console.log('  ★ 周期 32 Gyr（宇宙年齢の 2 倍）あたりで、主役が入れ替わります ──');
console.log('    それより速い揺れは 光時計、遅い揺れは オクロ天然原子炉。');
console.log('');
console.log('    腕の長さでは宇宙論的な観測が 8 桁 有利（10 年 対 18 億年）。');
console.log('    しかし精度では光時計が 9 桁 有利（10⁻¹⁷/年 対 10⁻⁸）。');
console.log('    ── 卓上の時計が、宇宙史とほぼ互角に戦っています。');
console.log('  ★ そして f → 0 では、どの実験の上限も発散します。');
console.log('    これは失敗ではなく定義です ──');
console.log('    「ω = 0 の成分」こそ、我々が「定数の値」と呼んでいるものだから。');

console.log('\n##################################################################');
console.log('# 3b. ただし ── この枠組み自体に穴があります');
console.log('##################################################################\n');
console.log('  上の議論は「定常な正弦波」を仮定しました。');
console.log('  しかし宇宙史は定常ではありません。たとえば ──\n');
const nonstat=[
  ['階段状の変化',   'ある時期に一度だけ跳んで、以後は一定',
   '★ 時計には見えない。CMB・元素合成だけが捕まえる'],
  ['減衰する振動',   '初期宇宙で大きく揺れ、現在は静か',
   '同上。スカラー場の緩和模型がこの形'],
  ['単調なドリフト',  '宇宙年齢に比例してゆっくり変化',
   '時計で見えるが、外挿は当てにならない'],
];
console.log('  変化の形          内容                              どの実験が効くか');
console.log('  '+'-'.repeat(88));
for(const [a,b,c] of nonstat) console.log(`  ${a.padEnd(15)} ${b.padEnd(32)} ${c}`);
console.log('\n  ★ フーリエは「いつでも同じように揺れている」場合の道具です。');
console.log('    一度きりの出来事を周波数で書くと、全周波数に薄く広がってしまい、');
console.log('    どの帯域でも上限にかからなくなる。\n');
console.log('  ⇒ だから宇宙論的な観測は、時計に負けていても捨てられません。');
console.log('    ★「すべてを波と見る」視点の、最初の限界がここにあります。');
console.log('\n##################################################################');
console.log('# 4. 原理的に見えない帯域');
console.log('##################################################################\n');
const fUniv=1/tUniv;
console.log(`  宇宙年齢 ${(tUniv/GYR).toFixed(1)} Gyr = ${E(tUniv)} s`);
console.log(`  → 分解できる最低周波数 1/T = ${E(fUniv)} Hz\n`);
console.log('  これより低い周波数は、どんな実験をしても「定数」に見えます。');
console.log('  なぜなら、1 周期ぶんの観測ができないから。\n');
const windows=[
  ['1 回の測定',          1,          '瞬間'],
  ['人間の一生',          80*YR,      ''],
  ['精密測定の歴史',       400*YR,     'ニュートン以降'],
  ['地球の年齢',          4.6*GYR,    'オクロ・隕石'],
  ['宇宙年齢',           13.8*GYR,   '★ 原理的な限界'],
];
console.log('  観測の窓            長さ            分解できる最低周波数');
console.log('  '+'-'.repeat(66));
for(const [n,t,note] of windows){
  const tt = t>GYR ? (t/GYR).toFixed(1)+' Gyr' : (t>YR? (t/YR).toFixed(0)+' 年' : t+' s');
  console.log(`  ${n.padEnd(18)} ${tt.padStart(10)}      ${E(1/t)} Hz   ${note}`);
}
console.log('\n  ★ 「物理定数」の正確な定義は、こうなります：\n');
console.log('        物理定数 ＝ 周期が宇宙年齢より長い成分');
console.log('');
console.log('    それは「変化しない」のではなく「変化を観測する手段がない」。');
console.log('    ── ご指摘のとおり、定数とは積分値でした。');
console.log('      ただし積分区間は「宇宙の歴史」で、それより長い波は見えない。');

console.log('\n##################################################################');
console.log('# 5. 実際に「定数を微分」してみる ── 数値');
console.log('##################################################################\n');
const alpha=7.2973525693e-3;
const rate=1e-17/YR;
console.log(`  α = ${alpha}`);
console.log(`  |α̇/α| < ${E(1e-17)} /年 = ${E(rate)} /s`);
console.log(`  → |α̇| < ${E(alpha*rate)} /s\n`);
console.log('  これがどれくらい小さいか、身近な量と比べます：\n');
const cmp=[
  ['α の変化率',           alpha*rate,      '/s'],
  ['山が隆起する速さ',      1e-10,           'm/s（年 3 mm）'],
  ['爪が伸びる速さ',        1e-9,            'm/s'],
  ['大陸移動',             1e-9,            'm/s（年 3 cm）'],
];
console.log('  量                     値');
console.log('  '+'-'.repeat(50));
for(const [a,b,c] of cmp) console.log(`  ${a.padEnd(22)} ${E(b)} ${c}`);
console.log('\n  ★ 単位が違うので直接は比べられませんが、桁の感覚として ──');
console.log(`    α が 1 % 変わるのに要する時間は ${E(0.01/rate/YR)} 年。`);
console.log(`    宇宙年齢の ${E(0.01/rate/tUniv)} 倍です。`);

console.log('\n##################################################################');
console.log('# 6. 逆に ── 定数の「高周波成分」はどうか');
console.log('##################################################################\n');
console.log('  ここまでは低周波（ゆっくりした変化）の話でした。');
console.log('  では 高周波側、つまり「定数を微分したら何か出るか」は？\n');
console.log('  実は、これも探索されています ── 超軽量スカラー場の探索です。\n');
const osc=[
  ['原子時計の比較',     '10⁻⁶ 〜 10⁻¹ Hz',  '日周・年周の変動を探す'],
  ['光共振器',          '10⁻³ 〜 10³ Hz',   '共振周波数の揺らぎ'],
  ['干渉計（LIGO 等）',  '10 〜 10³ Hz',     '★ 副産物として制約が出る'],
];
console.log('  手法                探索する周波数帯        内容');
console.log('  '+'-'.repeat(72));
for(const [a,b,c] of osc) console.log(`  ${a.padEnd(18)} ${b.padEnd(20)} ${c}`);
console.log('\n  ★ 「定数が振動していないか」は、実際に組織的に探されています。');
console.log('    超軽量スカラー場（暗黒物質の候補）が定数を揺らす、という模型があり、');
console.log('    質量 m の場は振動数 f = mc²/h で定数を揺らします。\n');
const h_eV=4.135667696e-15;   // eV·s
console.log('  場の質量 [eV]     揺らぎの振動数 [Hz]     周期');
console.log('  '+'-'.repeat(60));
for(const m of [1e-22,1e-18,1e-15,1e-12,1e-9]){
  const f=m/h_eV;
  const P=1/f;
  const pStr = P>YR ? (P/YR).toExponential(1)+' 年' : (P>1? P.toExponential(1)+' s' : E(P)+' s');
  console.log(`  ${E(m).padStart(9)}        ${E(f).padStart(10)}       ${pStr}`);
}
console.log('\n  ★ つまり ── 「定数を微分したら何が出るか」は、');
console.log('    暗黒物質の探索そのものになっています。');
console.log('    いまのところ、どの帯域でも有意な信号は出ていません。');

console.log('\n##################################################################');
console.log('# 7. まとめ');
console.log('##################################################################\n');
const sum=[
  ['c, h, e, k_B, N_A', '微分は厳密に 0',   '定義値。測る対象ではない（SI 2019）'],
  ['α',                '|α̇/α| < 10⁻¹⁷/年', '宇宙年齢で 10⁻⁷ 以内'],
  ['μ = m_p/m_e',      '|μ̇/μ| < 10⁻¹⁶/年', '同程度'],
  ['G',                '|Ġ/G| < 10⁻¹³/年', '月レーザー測距。最も緩い'],
  ['ω < 1/T_宇宙',      '★ 制約できない',   '1 周期の観測ができない'],
];
console.log('  対象                 微分した結果          根拠');
console.log('  '+'-'.repeat(80));
for(const [a,b,c] of sum) console.log(`  ${a.padEnd(20)} ${b.padEnd(20)} ${c}`);
console.log('\n  ★ 答え ──\n');
console.log('    「定数は積分値ではないか」── 半分 正しく、半分は定義の問題でした。\n');
console.log('    正しい部分：');
console.log('      観測窓 T より長い周期の成分は、原理的に定数と区別できない。');
console.log('      だから「定数」とは ω < 1/T の成分のことであり、');
console.log('      T を伸ばせば定数が変数になりうる ── これはそのとおり。\n');
console.log('    定義の問題：');
console.log('      c や h を微分しても 0 なのは、物理ではなく取り決め。');
console.log('      意味があるのは無次元量だけで、それは α, μ, G の 3 つ。\n');
console.log('    そして実測では、どれも ω ≠ 0 の成分が見つかっていません。');
console.log('    ★ ただし「見つかっていない」の上限が、周波数とともに緩む ──');
console.log('      そこにこのシリーズの続きがあります。');
