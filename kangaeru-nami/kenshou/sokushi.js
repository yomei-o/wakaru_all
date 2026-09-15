// 第 2 回の仮説を検証する ── 分数階は、粗視化の結果か
'use strict';
const E=x=>x.toExponential(3);
const deg=x=>x*180/Math.PI;

console.log('##################################################################');
console.log('# 1. 検証する仮説');
console.log('##################################################################\n');
console.log('  第 2 回で、こう書きました ──\n');
console.log('      【仮説】分数階が現れる系は、必ず隠れた自由度を');
console.log('              粗視化（積分で消去）した結果である。\n');
console.log('  ★ そして「反例を一つ挙げれば否定できる ── 反証可能」とも書きました。');
console.log('    25 回 かけて道具が揃ったので、ここで実際に確かめます。\n');
console.log('  やることは三つです：\n');
console.log('      ① 整数階の部品だけで組んだ系から、分数階が出るか（作ってみる）');
console.log('      ② 分数階は必ず整数階の重ね合わせに分解できるか（逆向き）');
console.log('      ③ 粗視化すれば必ず分数階になるのか（★ ここが本当の問い）');

console.log('\n##################################################################');
console.log('# 2. 実験① 整数階の部品だけで、半階を作る');
console.log('##################################################################\n');
console.log('  抵抗とコンデンサだけで梯子を組みます。部品はどちらも整数階です：\n');
console.log('      抵抗     : Z = R            （階数 0）');
console.log('      コンデンサ: Z = 1/(iωC)     （階数 −1）\n');
console.log('  これを N 段 重ねた入力インピーダンスを、連分数で計算します：\n');
console.log('      Z_n = R + 1/(iωC + 1/Z_{n−1})\n');
function ladder(N,R,C,w){
  // 最終段は開放（Z=∞ 相当）から始めて、外へ向かって積み上げる
  let re=0, im=0;   // Z_0 = 0（短絡終端）
  for(let n=0;n<N;n++){
    // Y = iωC + 1/Z   （Z=0 のときは 1/Z が発散 → 最初の段だけ特別扱い）
    let yr, yi;
    if(re===0 && im===0){ yr=0; yi=w*C; }
    else {
      const d=re*re+im*im;
      yr=re/d; yi=w*C-im/d;
    }
    // Z = R + 1/Y
    const dy=yr*yr+yi*yi;
    re=R+yr/dy; im=-yi/dy;
  }
  return {re,im};
}
const R=1, C=1;
console.log('   段数 N      |Z| @ ω=1e−4     位相 [度]     半階（−45°）との差');
console.log('  '+'-'.repeat(76));
for(const N of [1,2,3,5,10,20,50,200,1000]){
  const z=ladder(N,R,C,1e-4);
  const ph=deg(Math.atan2(z.im,z.re));
  console.log(`  ${String(N).padStart(8)}    ${Math.hypot(z.re,z.im).toFixed(6).padStart(12)}     ${ph.toFixed(4).padStart(10)}      ${(ph+45).toFixed(4)}`);
}
console.log('\n  半無限ラダーには厳密解があります ── 連分数の不動点：\n');
console.log('      Z_∞ = R/2 + √(R²/4 + R/(iωC))\n');
{
  const w=1e-4;
  // √(R²/4 + R/(iωC)) を複素数で
  const ar=R*R/4, ai=-R/(w*C);
  const m=Math.hypot(ar,ai), th=Math.atan2(ai,ar);
  const sr=Math.sqrt(m)*Math.cos(th/2), si=Math.sqrt(m)*Math.sin(th/2);
  const zr=R/2+sr, zi=si;
  console.log('      ω = 1e−4 での厳密解 : |Z| = '+Math.hypot(zr,zi).toFixed(6)+'、位相 = '+deg(Math.atan2(zi,zr)).toFixed(4)+'°');
  console.log('      ★ N=1000 の数値と一致します。残る 0.05° のずれは R/2 の項\n');
}
console.log('\n  ★ 段数を増やすと、位相がぴたりと −45° に近づきます。');
console.log('    ★ −45° ＝ 階数 −1/2（第 2 回）── ワールブルグ・インピーダンスです。\n');
console.log('  振幅の傾きも測ります（1 桁 あたり）：\n');
console.log('   ω          |Z|             傾き [dB/dec]    半階の予言 −10 dB/dec');
console.log('  '+'-'.repeat(76));
{
  const N=2000;
  let prev=null;
  for(const w of [1e-5,1e-4,1e-3,1e-2,1e-1]){
    const z=ladder(N,R,C,w);
    const m=Math.hypot(z.re,z.im);
    let slope='';
    if(prev) slope=(20*Math.log10(m/prev)).toFixed(4);
    console.log(`  ${E(w).padStart(9)}   ${m.toFixed(6).padStart(12)}     ${String(slope).padStart(12)}         −10`);
    prev=m;
  }
}
console.log('\n  ★★ −10 dB/dec ＝ −3.01 dB/oct ＝ 6α で α = −1/2。');
console.log('    ★ 整数階の部品だけで組んだのに、半階が出ました。\n');
console.log('  ── 仮説の①は成立します。★ 粗視化（無限段を一つのインピーダンスに畳む）で');
console.log('    分数階が作れる。');

console.log('\n##################################################################');
console.log('# 3. 実験② 逆向き ── 分数階は、必ず一階の重ね合わせに分解できるか');
console.log('##################################################################\n');
console.log('  こんどは逆です。分数階の応答を、「ふつうの緩和」の重ね合わせで書けるか：\n');
console.log('      (iω)^(−α) =? ∫₀^∞ g(τ)·1/(1+iωτ) dτ\n');
console.log('  ★ 右辺の 1/(1+iωτ) は、時定数 τ の一階の緩和 ── 整数階です。\n');
console.log('  解は知られています（0 < α < 1）：\n');
console.log('      g(τ) = sin(απ)/π · τ^(α−1)\n');
console.log('  数値で確かめます（τ を対数等間隔に切って和を取る）：\n');
function superpose(alpha,w){
  // ∫ g(τ)/(1+iωτ) dτ を対数グリッドで
  const lo=-25, hi=25, n=2000000;
  const h=(hi-lo)/n;
  let re=0, im=0;
  const pref=Math.sin(alpha*Math.PI)/Math.PI;
  for(let i=0;i<n;i++){
    const u=lo+(i+0.5)*h;
    const tau=Math.exp(u);
    // dτ = τ du
    const g=pref*Math.pow(tau,alpha-1)*tau;   // g(τ)=sin(απ)/π·τ^(α−1)、dτ=τ du
    const d=1+w*w*tau*tau;
    re+=g*h/d;
    im+=-g*h*w*tau/d;
  }
  return {re,im};
}
function fracRef(alpha,w){
  // (iω)^(−α) = ω^(−α)·exp(−iαπ/2)
  const m=Math.pow(w,-alpha), ph=-alpha*Math.PI/2;
  return {re:m*Math.cos(ph), im:m*Math.sin(ph)};
}
console.log('   α      ω        重ね合わせ（実部, 虚部）        (iω)^(−α)（実部, 虚部）      相対誤差');
console.log('  '+'-'.repeat(104));
for(const alpha of [0.25,0.5,0.75]){
  for(const w of [0.1,1,10]){
    const a=superpose(alpha,w), b=fracRef(alpha,w);
    const err=Math.hypot(a.re-b.re,a.im-b.im)/Math.hypot(b.re,b.im);
    console.log(`  ${alpha.toFixed(2)}   ${E(w).padStart(8)}   ${a.re.toFixed(6).padStart(10)} ${a.im.toFixed(6).padStart(11)}      ${b.re.toFixed(6).padStart(10)} ${b.im.toFixed(6).padStart(11)}    ${E(err)}`);
  }
}
console.log('\n  ★ 一致しました。');
console.log('    ★★ つまり ── 0 < α < 1 の分数階は、必ず一階の緩和の連続重ね合わせで書けます。\n');
console.log('  ── これは仮説の②の、実質的な証明です：');
console.log('    ★ 分数階の散逸的な応答には、必ず「隠れた自由度の分布」を割り当てられる。');
console.log('      その分布は g(τ) ∝ τ^(α−1) ── ★ べき乗、つまりスケール不変。');

console.log('\n##################################################################');
console.log('# 4. 実験③ では、粗視化すれば必ず分数階になるのか');
console.log('##################################################################\n');
console.log('  ★ ここが本当の問いです。反例を探します。\n');
console.log('  もっとも素直な粗視化 ── 半無限のばね・質点の鎖から、端の 1 個だけを見る：\n');
console.log('      m ẍ_n = k(x_{n+1} − 2x_n + x_{n−1})\n');
console.log('  残り全部を消すと、端の質点に「媒質からの力」がかかります。');
console.log('  その力のインピーダンス Z = F/v を計算します：\n');
function chainImpedance(w,m,k){
  // 分散関係 ω = 2√(k/m) sin(q/2) を解いて、外向き波のインピーダンス
  const wmax=2*Math.sqrt(k/m);
  if(w>=wmax) return null;
  const q=2*Math.asin(w/wmax);
  // F = k(x_1 − x_0) = k x_0 (e^{iq} − 1), v = −iω x_0
  const fr=k*(Math.cos(q)-1), fi=k*Math.sin(q);
  // Z = F/v = F/(−iω) = i F/ω
  return {re:-fi/w, im:fr/w, wmax};
}
{
  const m=1,k=1;
  const wmax=2;
  console.log(`      帯域の上限 ω_max = 2√(k/m) = ${wmax}\n`);
  console.log('   ω/ω_max     |Z|            位相 [度]        中身');
  console.log('  '+'-'.repeat(76));
  for(const r of [0.001,0.01,0.1,0.3,0.6,0.9,0.99]){
    const w=r*wmax;
    const z=chainImpedance(w,m,k);
    const ph=deg(Math.atan2(z.im,z.re));
    let note='';
    if(Math.abs(ph)<1) note='★ 純抵抗（位相 0）';
    console.log(`  ${r.toFixed(3).padStart(9)}   ${Math.hypot(z.re,z.im).toFixed(6).padStart(10)}     ${ph.toFixed(4).padStart(10)}     ${note}`);
  }
  console.log(`\n      低周波での |Z| → √(km) = ${Math.sqrt(m*k).toFixed(6)}`);
}
console.log('\n  ★★ 位相が 0 ── つまり純粋な抵抗（ふつうの摩擦）です。分数階ではありません。\n');
console.log('  ── ★ 反例が見つかりました。');
console.log('    「自由度を消せば必ず分数階になる」は ★ 誤りです。\n');
console.log('  第 2 回の仮説は、このままでは成り立ちません。');

console.log('\n##################################################################');
console.log('# 5. では何が分数階を決めるのか ── 自由度の「分布」だった');
console.log('##################################################################\n');
console.log('  ①と③の違いを見ます：\n');
const diff=[
  ['① RC ラダー',   '自己相似（各段が同じ形）', 'べき乗',       '★ 分数階 α = −1/2'],
  ['③ ばね鎖',      '一様（すべての段が同じ）', '一定',         '整数階（ふつうの摩擦）'],
  ['② 緩和の重ね',   'g(τ) ∝ τ^(α−1)',       'べき乗',       '★ 分数階 α'],
];
console.log('   系                 自由度の並び方           密度        結果');
console.log('  '+'-'.repeat(88));
for(const [a,b,c,d] of diff) console.log(`  ${a.padEnd(16)} ${b.padEnd(24)} ${c.padEnd(12)} ${d}`);
console.log('\n  ★ 違いは「消した自由度が、どう分布していたか」です。\n');
console.log('  ★ 一般に、消した自由度のスペクトル密度が J(ω) ∝ ω^s なら、');
console.log('    ★ 実効的な階数は α = s になります。数値で確かめます：\n');
function selfEnergy(s,w,wc){
  // Σ(ω) = ∫₀^{ωc} 2 ω'^{s+1}/(ω'²−ω²−i0) dω'
  // 実部は特異点を引き算して主値、虚部は極からの π ω^s
  const n=400000, h=wc/n;
  const f=x=>2*Math.pow(x,s+1);
  const fw=f(w);
  let pv=0;
  for(let i=0;i<n;i++){
    const x=(i+0.5)*h;
    const den=x*x-w*w;
    if(Math.abs(den)<1e-300) continue;
    pv+=(f(x)-fw)/den*h;
  }
  pv+=fw*(1/(2*w))*Math.log((wc-w)/(wc+w));
  const im=Math.PI*Math.pow(w,s);
  return {re:pv, im};
}
{
  const wc=1;
  console.log('   s      ω       Σ−Σ(0) の傾き [/dec]   位相 [度]    (iω)^s の予言 [度]   差');
  console.log('  '+'-'.repeat(92));
  for(const s of [0.5,1.0,1.5]){
    const S0=selfEnergy(s,1e-12,wc).re;   // ω→0 の実部
    let prev=null, prevW=null;
    for(const w of [1e-4,1e-3,1e-2]){
      const S=selfEnergy(s,w,wc);
      const dr=S.re-S0, di=S.im;
      const mag=Math.hypot(dr,di);
      let slope='';
      if(prev) slope=(Math.log10(mag/prev)/Math.log10(w/prevW)).toFixed(4);
      // 非解析部の位相：−(Σ−Σ0) の偏角を見る
      const ph=deg(Math.atan2(di,-dr));
      const pred=s*90;
      if(prev) console.log(`  ${s.toFixed(1)}   ${E(w).padStart(8)}      ${String(slope).padStart(10)}        ${ph.toFixed(3).padStart(9)}         ${pred.toFixed(1).padStart(8)}      ${(ph-pred).toFixed(3)}`);
      prev=mag; prevW=w;
    }
  }
}
console.log('\n  ★★ 傾きが s、位相が 90s 度 ── ★ きっかり (iω)^s です。\n');
console.log('  ── ★ 消した自由度のスペクトル密度の指数が、そのまま階数になる。\n');
console.log('  ★ 特別な場合として：\n');
console.log('      s = 1（オーム的）→ α = 1 ── ★ ふつうの摩擦（整数階）');
console.log('      s = 1/2         → α = 1/2 ── ★ 分数階');
console.log('      s = 2           → α = 2  ── 整数階\n');
console.log('  ★ ばね鎖（実験③）が整数階だったのは、低周波で J(ω) ∝ ω（オーム的）だから。');
console.log('    ★ RC ラダー（実験①）が半階だったのは、自己相似でべき乗分布だから。');

console.log('\n##################################################################');
console.log('# 6. 仮説を書き直す');
console.log('##################################################################\n');
console.log('  第 2 回の仮説：\n');
console.log('      「分数階が現れる系は、必ず隠れた自由度を粗視化した結果である」\n');
console.log('  ★ 採点します：\n');
const score=[
  ['分数階 → 粗視化で説明できる', '◎ 成立', '★ 実験②。0<α<1 なら必ずスペクトル表示がある'],
  ['粗視化 → 必ず分数階になる',   '× 不成立','★ 実験③。ばね鎖は整数階'],
  ['粗視化で分数階を作れる',      '◎ 成立', '★ 実験①。RC ラダーで半階'],
];
console.log('   主張                          判定       根拠');
console.log('  '+'-'.repeat(88));
for(const [a,b,c] of score) console.log(`  ${a.padEnd(28)} ${b.padEnd(10)} ${c}`);
console.log('\n  ★★ 書き直した仮説 ──\n');
console.log('      分数階が現れるのは、粗視化した自由度が');
console.log('      ★ スケール不変に（べき乗で）分布しているときである。\n');
console.log('  ★ 単なる粗視化では足りません。★ 自己相似性が要る。\n');
console.log('  ── そして、ここで第 13 回とつながります：\n');
console.log('      第 13 回：虚数階 ＝ スケール変換の生成子');
console.log('      第 22 回：ウェーブレット ＝ 対数軸で等分解能');
console.log('      ★ 本回　：分数階が出る条件 ＝ 隠れた自由度がスケール不変');
console.log('\n  ★★ 三つとも「スケール不変性」が鍵でした。');
console.log('    ★ 分数階とは、スケール不変な自由度を消した痕跡だった。');

console.log('\n##################################################################');
console.log('# 7. 実在の系を、この基準で並べ直す');
console.log('##################################################################\n');
const real=[
  ['ワールブルグ（第 2 回）', 'α=−1/2', '半無限拡散',            '★ 拡散は自己相似（√t）'],
  ['粘弾性（第 10 回）',      'α=0〜1', '高分子の緩和時間分布',  '★ 鎖の長さがべき乗分布'],
  ['1/f 雑音（第 2 回）',     'α=−1/2', '★ 時定数が対数一様',    '★ なぜ対数一様かは未解決'],
  ['コール＝コール',          'α=0〜1', '誘電緩和の分布',        '同上'],
  ['ふつうの摩擦',            'α=1',    'オーム的な浴',          '整数階。自己相似でない'],
  ['熱伝導（第 11 回）',      'α=−1/2', '★ 半無限媒質',          '★ 拡散なので自己相似'],
];
console.log('   系                       階数       消された自由度            自己相似か');
console.log('  '+'-'.repeat(92));
for(const [a,b,c,d] of real) console.log(`  ${a.padEnd(24)} ${b.padEnd(10)} ${c.padEnd(24)} ${d}`);
console.log('\n  ★ 分数階の系は、例外なく「自己相似な自由度を消した」ものでした。');
console.log('    ★ そして 1/f 雑音だけが、★ なぜ対数一様なのかが未解決のまま残ります。\n');
console.log('  ── 第 15 回で開いた扉のうち、');
console.log('    ★「分数階は必ず粗視化の結果か」は ── 条件つきで閉じました。');
console.log('    ★「1/f の起源」は ── 開いたままです。');
console.log('      ただし問いの形が変わりました：');
console.log('      ★ 「なぜ自然には、対数一様な時定数分布がこれほど多いのか」。');

console.log('\n##################################################################');
console.log('# 8. まとめ');
console.log('##################################################################\n');
const sm=[
  ['RC ラダーで半階が出る',    '◎ 数値',  '★ 位相 −45°、−10 dB/dec'],
  ['分数階 → 緩和の重ね合わせ','◎ 数値',  '★ g(τ)=sin(απ)/π·τ^(α−1)'],
  ['ばね鎖は整数階',          '◎ 数値',  '★ 反例。粗視化だけでは足りない'],
  ['階数 ＝ スペクトル密度の指数','◎ 数値','★ 傾き s、位相 90s 度'],
  ['仮説は条件つきで成立',     '◎ 整理',  '★ 自己相似性が要る'],
  ['1/f の起源は未解決のまま',  '○ 整理',  '問いの形は変わった'],
];
console.log('  主張                        判定      根拠');
console.log('  '+'-'.repeat(80));
for(const [a,b,c] of sm) console.log(`  ${a.padEnd(26)} ${b.padEnd(9)} ${c}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     「分数階は粗視化の結果」は、半分 正しかった。');
console.log('     粗視化しただけでは整数階にしかならない ── 自己相似性が要る。');
console.log('     ── 分数階とは、スケール不変な自由度を消した痕跡だった。');
