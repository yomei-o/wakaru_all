// 実効光速 ── 定義値でも、微分はできる。測れるのは無次元量のほうだった
'use strict';
const E=x=>x.toExponential(3);
const c=2.99792458e8;
const G=6.67430e-11;
const hbar=1.054571817e-34;
const me=9.1093837015e-31;
const alpha=7.2973525693e-3;
const AU=1.495978707e11;
const GMsun=1.32712440018e20;     // 太陽の重力定数（GM は G や M より精度が高い）
const Rsun=6.957e8;

console.log('##################################################################');
console.log('# 1. 光速は定義値。では何が測れるのか');
console.log('##################################################################\n');
console.log('  第 4 回で見たとおり、1983 年以降 c は定義値です。');
console.log('  dc/dt = 0 は測定結果ではなく、取り決め。\n');
console.log('  でも「光が実際に進む速さ」は、場所や媒質で変わります。');
console.log('  ★ 波の言葉では、光速とはこれのことでした ──\n');
console.log('      位相速度 v_p = ω/k        （波の山が進む速さ）');
console.log('      群速度   v_g = dω/dk      ★ 分散関係の「傾き」\n');
console.log('  つまり「光速を微分する」とは、分散関係を二階微分することです。');
console.log('  ── 定数を微分するのではなく、曲線の曲がり具合を測る。\n');
const disp=[
  ['真空',              'ω = ck',                 'c',      'c',       '傾き一定。曲がらない'],
  ['導波管・プラズマ',   'ω² = ω_c² + c²k²',       '> c',    '< c',     '★ v_p·v_g = c²（第 6 回）'],
  ['クライン＝ゴルドン', 'ω² = (mc²/ħ)² + c²k²',   '> c',    '< c',     '同じ式。質量が遮断周波数'],
  ['媒質（分散あり）',   'ω = ck/n(ω)',            'c/n',    'c/n_g',   '★ n_g = n + ω dn/dω'],
  ['拡散（第 11 回）',   'ω = −iDk²',              '純虚数',  '──',      '伝播しない'],
];
console.log('   系                 分散関係                  v_p      v_g      備考');
console.log('  '+'-'.repeat(92));
for(const r of disp) console.log(`  ${r[0].padEnd(18)} ${r[1].padEnd(24)} ${r[2].padEnd(8)} ${r[3].padEnd(8)} ${r[4]}`);

console.log('\n##################################################################');
console.log('# 2. 媒質 ── ここは本物。しかも二階微分が効く');
console.log('##################################################################\n');
console.log('  石英ガラスの屈折率を、セルマイヤーの式から計算します：\n');
console.log('      n²(λ) = 1 + Σ B_i λ² / (λ² − C_i)      （λ は μm）\n');
const B=[0.6961663,0.4079426,0.8974794];
const C=[0.0684043**2,0.1162414**2,9.896161**2];
function nSil(lam){ let s=1; for(let i=0;i<3;i++) s+=B[i]*lam*lam/(lam*lam-C[i]); return Math.sqrt(s); }
const d1=(f,x,h)=>(f(x+h)-f(x-h))/(2*h);
const d2=(f,x,h)=>(f(x+h)-2*f(x)+f(x-h))/(h*h);
// 群屈折率 n_g = n − λ dn/dλ
const ng=lam=>nSil(lam)-lam*d1(nSil,lam,1e-5);
console.log('   波長 [nm]   n        n_g       v_g [m/s]       用途');
console.log('  '+'-'.repeat(76));
const uses={'486':'水素 F 線','589':'ナトリウム D 線','633':'He-Ne レーザー','850':'短距離光通信','1310':'★ 零分散に近い','1550':'★ 長距離光通信（損失最小）'};
for(const nm of [486,589,633,850,1310,1550]){
  const lam=nm/1000;
  console.log(`  ${String(nm).padStart(8)}   ${nSil(lam).toFixed(5)}  ${ng(lam).toFixed(5)}   ${E(c/ng(lam))}   ${uses[String(nm)]||''}`);
}
console.log('\n  ★ 材料分散が消えるのは d²n/dλ² = 0 のところです。二分法で探します：\n');
let a=1.0,b=1.6;
for(let i=0;i<200;i++){ const m=(a+b)/2; if(d2(nSil,a,1e-4)*d2(nSil,m,1e-4)<=0) b=m; else a=m; }
const lam0=(a+b)/2;
console.log(`      零材料分散波長 = ${(lam0*1000).toFixed(1)} nm      （文献値 約 1270 nm）`);
console.log(`      そこでの n = ${nSil(lam0).toFixed(5)}、n_g = ${ng(lam0).toFixed(5)}\n`);
console.log('  ★ 光ファイバ通信が 1310 nm と 1550 nm を使う理由がここにあります ──');
console.log('    1310 nm は分散が消える波長、1550 nm は損失が最小の波長。');
console.log('    ★ そして「分散が消える」とは、n の二階微分がゼロということ。');
console.log('      ── 光速の「変化率の変化率」を、通信インフラが使っています。');

console.log('\n##################################################################');
console.log('# 3. 重力 ── 実効光速が場所で変わる');
console.log('##################################################################\n');
console.log('  弱い重力場では、座標で測った光速がこうなります：\n');
console.log('      c_eff = c ( 1 + 2Φ/c² ),      Φ = −GM/r  （負）\n');
console.log('  ★ これは微分できます：\n');
console.log(`      dc_eff/dΦ = 2/c = ${E(2/c)} s/m\n`);
console.log('  ── 定数を微分できないはずが、できてしまった。');
console.log('    種明かしは簡単で、変えているのは c ではなく無次元量 2Φ/c² です。\n');
const bodies=[
  ['地表',           5.9722e24*G, 6.371e6],
  ['太陽表面',       GMsun,       Rsun],
  ['白色矮星（表面）',GMsun*0.6,   7e6],
  ['中性子星（表面）',GMsun*1.4,   1.2e4],
];
console.log('   場所                 2GM/(rc²)        c_eff/c          遅れ [ns/m]');
console.log('  '+'-'.repeat(76));
for(const [nm,gm,r] of bodies){
  const x=2*gm/(r*c*c);
  console.log(`  ${nm.padEnd(18)} ${E(x).padStart(12)}   ${(1-x).toFixed(9)}    ${E(x/c*1e9)}`);
}
console.log('\n  ★ 弱い場では 10⁻⁶ 以下。でも積分すると測れる大きさになります ──');
console.log('    シャピロ遅延です。\n');
function shapiro(r1,r2,b){ return 2*GMsun/(c*c*c)*Math.log(4*r1*r2/(b*b)); }
console.log('   経路                              衝突径数 b     片道の遅れ    往復の遅れ');
console.log('  '+'-'.repeat(84));
const paths=[
  ['地球 → 金星（上合、太陽を掠める）', AU, 0.723*AU, Rsun*1.0],
  ['地球 → 火星（バイキング 1976）',    AU, 1.524*AU, Rsun*1.2],
  ['地球 → カッシーニ（2002 上合）',    AU, 8.43*AU,  Rsun*1.6],
];
for(const [nm,r1,r2,bb] of paths){
  const t=shapiro(r1,r2,bb);
  console.log(`  ${nm.padEnd(32)} ${(bb/Rsun).toFixed(1)} R_sun      ${(t*1e6).toFixed(1)} μs     ${(2*t*1e6).toFixed(1)} μs`);
}
console.log('\n  ★ カッシーニの往復 262 μs ── これを 10⁻⁵ の精度で測ったのが');
console.log('    第 7 回で出てきた「カッシーニの制限 γ−1 = (2.1±2.3)×10⁻⁵」です。');
console.log('    ★ 実効光速の変化は、すでに 5 桁 の精度で測られている。\n');
console.log('  ただし注意：これは座標で測った速さです。');
console.log('  ★ その場で測れば、いつでもぴったり c ── 局所的には何も変わりません。');
console.log('    「遅れ」として観測できるのは、離れた二点を結んだときだけ。');

console.log('\n##################################################################');
console.log('# 4. 真空そのものを変える ── 二つの本物の効果');
console.log('##################################################################\n');
console.log('  【その 1】強い磁場の真空複屈折（オイラー＝ハイゼンベルク）\n');
console.log('  磁場のある真空は、複屈折します。偏光の向きで屈折率が違う：\n');
console.log('      Δn = (3/2)·(α/45π)·(B/B_c)²,      B_c = m_e²c²/(eħ)\n');
const Bc=me*me*c*c/(1.602176634e-19*hbar);   // B_c = m_e²c²/(eħ)
const kCM=1.5*(alpha/(45*Math.PI))/(Bc*Bc);
console.log(`      臨界磁場 B_c = ${E(Bc)} T`);
console.log(`      係数     k   = ${E(kCM)} T⁻²      （文献値 4.0×10⁻²⁴ T⁻²）\n`);
console.log('   磁場 B [T]           Δn              どこ');
console.log('  '+'-'.repeat(66));
for(const [Bv,wh] of [[1,'ふつうの電磁石'],[5,'PVLAS 実験'],[45,'定常強磁場の世界記録級'],[1e8,'中性子星'],[1e11,'マグネター']]){
  console.log(`  ${E(Bv).padStart(10)}      ${E(kCM*Bv*Bv).padStart(12)}      ${wh}`);
}
console.log('\n  ★ 実験室では 10⁻²² ── まだ検出されていません（PVLAS が挑戦中）。');
console.log('    マグネターでは Δn ~ 0.04 ── ★ 真空が方解石なみに複屈折します。\n');
console.log('  【その 2】シャルンホルスト効果 ── カシミール板の間で c が増える\n');
console.log('  平行板の間では真空のモードが減るので、光がわずかに速くなります：\n');
console.log('      Δc/c = (11π²/8100)·α²·(ħ/(m_e c d))⁴        （d は板の間隔）\n');
const lamC=hbar/(me*c);
console.log('   板の間隔 d      (ħ/m_e c d)⁴        Δc/c');
console.log('  '+'-'.repeat(60));
for(const d of [1e-6,1e-7,1e-8,1e-9]){
  const q=Math.pow(lamC/d,4);
  console.log(`  ${E(d)} m    ${E(q).padStart(12)}     ${E(11*Math.PI*Math.PI/8100*alpha*alpha*q)}`);
}
console.log('\n  ★ 1 μm で 10⁻³² ── 測れる見込みはありません。');
console.log('    でも「真空の性質を変えれば光速は変わる」ことの、理論的な例です。');
console.log('    ★ 判定：式に代入しただけの値です。実験による確認はありません。');

console.log('\n##################################################################');
console.log('# 5. 群速度は c を超える。でも情報は超えない');
console.log('##################################################################\n');
console.log('  第 8 回のローレンツ振動子を、もう一度使います：\n');
console.log('      χ(ω) = ω_p² / (ω₀² − ω² − iγω)\n');
const wp=0.1, w0=1, gam=0.02;
function nOf(w){
  const den={re:w0*w0-w*w, im:-gam*w};
  const d2v=den.re*den.re+den.im*den.im;
  const chre=wp*wp*den.re/d2v, chim=-wp*wp*den.im/d2v;
  // n = sqrt(1+χ)
  const r=Math.hypot(1+chre,chim), th=Math.atan2(chim,1+chre);
  return {re:Math.sqrt(r)*Math.cos(th/2), im:Math.sqrt(r)*Math.sin(th/2)};
}
console.log('  共鳴のすぐ内側（異常分散領域）を見ます。n_g = n + ω dn/dω：\n');
console.log('   ω/ω₀      n（実部）     n_g          v_g/c        様子');
console.log('  '+'-'.repeat(72));
for(const w of [0.90,0.98,0.995,1.000,1.005,1.02,1.10,5.0,50.0]){
  const n=nOf(w).re;
  const dn=(nOf(w+1e-6).re-nOf(w-1e-6).re)/2e-6;
  const nG=n+w*dn;
  let s='通常';
  if(nG<1&&nG>0) s='★ v_g > c';
  if(nG<0) s='★ v_g < 0（負の群速度）';
  console.log(`  ${w.toFixed(3).padStart(7)}   ${n.toFixed(6).padStart(10)}  ${nG.toFixed(6).padStart(11)}  ${(1/nG).toFixed(6).padStart(11)}   ${s}`);
}
{
  const step=0.00002;
  const runs=[]; let cur=null;
  for(let w=0.95;w<1.12;w+=step){
    const n=nOf(w).re, dn=(nOf(w+1e-6).re-nOf(w-1e-6).re)/2e-6;
    const nG=n+w*dn;
    if(nG>0&&nG<1){ if(!cur){cur={a:w,b:w};runs.push(cur);} else cur.b=w; }
    else cur=null;
  }
  console.log('\n  0 < n_g < 1（つまり v_g > c）になる帯を、細かく探します：\n');
  if(!runs.length) console.log('      見つかりませんでした');
  for(const r of runs){
    const wm=(r.a+r.b)/2;
    const n=nOf(wm).re, dn=(nOf(wm+1e-6).re-nOf(wm-1e-6).re)/2e-6;
    const nG=n+wm*dn;
    console.log('      ω/ω₀ = '+r.a.toFixed(5)+' 〜 '+r.b.toFixed(5)+
      '   中央で n_g = '+nG.toFixed(6)+'、v_g = '+(1/nG).toFixed(4)+' c');
  }
  console.log('\n  ★ 共鳴の両脇に、v_g > c の細い帯が二本あります。');
  console.log('    その内側（共鳴のど真ん中）では n_g < 0 ── 群速度が負になります。');
}
console.log('  ── どちらも実験で確認されている本物の現象です（異常分散）。'+String.fromCharCode(10));
console.log('  では因果律は破れているのか ── 破れていません。');
console.log('  ★ 信号の「前面」が進む速さは、いつでもきっかり c です：\n');
console.log('      前面速度 = c / n(∞),      そして n(∞) = 1\n');
console.log('   ω/ω₀         n(ω) − 1        −ω_p²/(2ω²) との比');
console.log('  '+'-'.repeat(60));
for(const w of [10,100,1000,10000]){
  const dn=nOf(w).re-1;
  const asy=-wp*wp/(2*w*w);
  console.log(`  ${E(w).padStart(10)}    ${E(dn).padStart(12)}      ${(dn/asy).toFixed(8)}`);
}
console.log('\n  ★ 高周波では n → 1 に、きっちり −ω_p²/(2ω²) で近づきます（8 桁 一致）。');
console.log('    どんな媒質でも、十分高い周波数では真空と同じ ──');
console.log('    ★ だから「最初の一波」は必ず c で届く。');
console.log('      群速度が何をしようと、情報は c を超えません（第 8 回の帰結）。');

console.log('\n##################################################################');
console.log('# 6. 実効光速の一覧 ── 何桁 変えられるか');
console.log('##################################################################\n');
const all=[
  ['BEC 中の光（ハウ 1999）',    17,              '○ 実測',  '★ n_g = 1.8×10⁷。自転車より遅い'],
  ['冷却原子気体',              1.7e4,           '○ 実測',  '電磁誘導透明化'],
  ['水（群速度）',              c/1.34,          '◎ 厳密',  'n_g ≈ 1.34'],
  ['石英ガラス 1550 nm',        c/1.4625,        '◎ 計算',  '光ファイバの実効速度'],
  ['真空',                      c,               '◎ 定義',  '基準'],
  ['太陽表面（座標）',           c*(1-4.245e-6),  '○ 実測',  'シャピロ遅延として測定済み'],
  ['カシミール板間（1 nm）',     c*(1+1.6e-20),   '× 未検証','シャルンホルスト効果'],
];
console.log('   状況                        実効光速 [m/s]    c_eff/c            判定      備考');
console.log('  '+'-'.repeat(104));
for(const [a,v,j,note] of all){
  const rt=v/c;
  const rs=(rt<0.99||rt>1.01)?E(rt):rt.toFixed(14);
  console.log(`  ${a.padEnd(26)} ${E(v).padStart(12)}   ${rs.padStart(16)}   ${j.padEnd(8)}  ${note}`);
}
console.log('\n  ★ 実効光速は 7 桁 以上 遅くできます（BEC で 17 m/s）。');
console.log('    でも速くするほうは、いまのところ 10⁻²⁰ 程度が理論の限界。');
console.log('    ★ この非対称性は偶然ではありません ──');
console.log('      遅くするのは「共鳴を置く」だけ、速くするには「真空を薄くする」必要がある。');

console.log('\n##################################################################');
console.log('# 7. では、結局 光速は微分できたのか');
console.log('##################################################################\n');
const verdict=[
  ['dc/dt',            '× できない', 'c は定義値（第 4 回）。0 は取り決め'],
  ['dc_eff/dΦ = 2/c',  '○ できる',   '★ ただし中身は無次元量 2Φ/c² の微分'],
  ['dn/dω',            '◎ できる',   '無次元。分散そのもの。毎日 測られている'],
  ['d²n/dλ²',          '◎ できる',   '★ 零分散波長 1270 nm。通信インフラが使う'],
  ['dv_g/dω',          '◎ できる',   '群速度分散。パルスが広がる速さ'],
];
console.log('   何を微分するか        判定        中身');
console.log('  '+'-'.repeat(80));
for(const [a,b,cc] of verdict) console.log(`  ${a.padEnd(20)} ${b.padEnd(11)} ${cc}`);
console.log('\n  ★ 答え ──\n');
console.log('     光速そのものは微分できない。でも屈折率は微分できる。');
console.log('     そして「実効光速が変わる」と言うとき、変わっているのは');
console.log('     いつでも無次元量のほうでした。\n');
console.log('  ── 第 7 回の結論「当たるのは無次元量、外れるのは次元を持つ量」が、');
console.log('    ここでもそのまま効いています。');
console.log('    ★ 「実効」という言葉は、次元を持つ量を無次元量で書き直す合図でした。');

console.log('\n##################################################################');
console.log('# 8. まとめ');
console.log('##################################################################\n');
const sm=[
  ['光速 ＝ 分散関係の傾き',   '◎ 定義',  'v_p=ω/k、v_g=dω/dk'],
  ['零分散波長 1270 nm',      '◎ 計算',  'セルマイヤーの d²n/dλ²=0'],
  ['シャピロ遅延 262 μs',     '○ 実測',  'カッシーニ。γ−1 を 10⁻⁵ で'],
  ['真空複屈折 4.0×10⁻²⁴ B²','◎ 計算',  '文献値と一致。未検出'],
  ['シャルンホルスト 10⁻³²',  '× 未検証','式に代入しただけ'],
  ['群速度 > c でも情報は c', '◎ 数値',  'n(∞)=1 を 8 桁 で確認'],
  ['変わるのは無次元量',      '◎ 整理',  '★ 第 7 回の結論がそのまま効く'],
];
console.log('  主張                      判定      根拠');
console.log('  '+'-'.repeat(76));
for(const [a,b,cc] of sm) console.log(`  ${a.padEnd(24)} ${b.padEnd(9)} ${cc}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     光速は微分できない。屈折率は微分できる。');
console.log('     「実効光速」とは、次元を持つ量を無次元量に書き直した姿だった。');
console.log('     ── そして次回、同じことを質量でやります。');
