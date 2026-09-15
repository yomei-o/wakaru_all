// 宇宙年齢のそばの時定数 ── 崩壊定数は「虚数の周波数」だから、待たずに測れる
'use strict';
const E=x=>x.toExponential(3);
const hbar=1.054571817e-34;
const hbarGeV=6.582119569e-25;   // GeV·s
const eV=1.602176634e-19;
const NA=6.02214076e23;
const yr=3.1557e7;               // ユリウス年 [s]
const Tuniv=13.787e9*yr;         // 宇宙年齢 [s]

console.log('##################################################################');
console.log('# 1. 第 3 回の観測窓を、もう一度');
console.log('##################################################################\n');
console.log('  第 3 回・第 4 回でこう書きました：\n');
console.log('      「周期が観測窓より長い成分は、定数と区別がつかない」\n');
console.log(`      宇宙年齢 T = ${E(Tuniv)} s`);
console.log(`      対応する周波数 1/T = ${E(1/Tuniv)} Hz\n`);
console.log('  ★ ここで当然の疑問が出ます ──\n');
console.log('      では、時定数が「ちょうど宇宙年齢のあたり」にあるものは、どうなるのか。\n');
console.log('  実は、たくさんあります：\n');
const near=[
  ['²³⁵U',    0.7040e9],
  ['⁴⁰K',     1.248e9],
  ['²³⁸U',    4.468e9],
  ['★ 宇宙年齢', 13.787e9],
  ['²³²Th',   14.05e9],
  ['¹⁷⁶Lu',   37.6e9],
  ['¹⁸⁷Re',   41.6e9],
  ['⁸⁷Rb',    49.7e9],
  ['¹⁴⁷Sm',   106e9],
];
console.log('   核種            半減期 [年]       宇宙年齢との比');
console.log('  '+'-'.repeat(60));
for(const [nm,t] of near){
  console.log(`  ${nm.padEnd(12)} ${E(t).padStart(12)}      ${(t/13.787e9).toFixed(3)}`);
}
console.log('\n  ★ ²³²Th の半減期 140.5 億年 と、宇宙年齢 137.9 億年 は');
console.log('    1.02 倍 ── ほとんど ぴったり重なっています。');
console.log('\n  では、これらは「定数と区別がつかない」のか？');
console.log('  ★ 答えは ── 区別がつきます。しかも 1 秒 で。');

console.log('\n##################################################################');
console.log('# 2. 核心 ── 崩壊定数は「虚数の周波数」だった');
console.log('##################################################################\n');
console.log('  振動と減衰を、同じ形で書いてみます：\n');
console.log('      振動 : e^(iωt)        ω は実数');
console.log('      減衰 : e^(−λt) = e^(i(iλ)t)     ★ ω = iλ ── 純虚数\n');
console.log('  ★ 崩壊定数は、複素周波数平面の「虚軸の上」にいます。\n');
console.log('  これは第 11 回の拡散（ω = −iDk²）と、同じ家族です。');
console.log('  そして第 13 回で見たとおり、実軸と虚軸では性質がまったく違う。\n');
console.log('   軸        振る舞い      測り方                    必要な観測時間');
console.log('  '+'-'.repeat(84));
const axes=[
  ['実軸 ω',   '振動する',   '位相が一周するのを見る',     '★ 周期の程度'],
  ['虚軸 iλ',  '単調に減る', '傾き（＝崩壊の回数）を数える','★ いくらでも短くてよい'],
];
for(const [a,b,c,d] of axes) console.log(`  ${a.padEnd(9)} ${b.padEnd(12)} ${c.padEnd(26)} ${d}`);
console.log('\n  ★ ここが決定的です ──\n');
console.log('      振動の周波数は、一周期 待たないと分からない。');
console.log('      減衰の速さは、一瞬でも分かる。数えればいいから。\n');
console.log('  実際に計算します。²³²Th を 1 グラム 用意します：\n');
const A232=232.0381, T232=14.05e9*yr;
const lam232=Math.LN2/T232;
const N232=NA/A232;
const act=lam232*N232;
console.log(`      原子の数 N = ${E(N232)} 個/g`);
console.log(`      崩壊定数 λ = ln2/T½ = ${E(lam232)} /s`);
console.log(`      放射能 A = λN = ${act.toFixed(0)} Bq/g      ★ 毎秒 ${act.toFixed(0)} 回\n`);
console.log('  ★ 半減期が宇宙年齢より長い物質が、1 グラムで毎秒 4000 回 崩壊します。');
console.log('    ── 1 秒 測れば、崩壊定数は 1.6 % の精度で決まる（√4057/4057）。');
console.log('    ★ 1 日 測れば 0.017 %。宇宙年齢を待つ必要は、まったくありません。\n');
console.log('  比較のために、同じ「周波数」の振動を測ることを考えます：\n');
console.log(`      周期 ${E(T232)} s = ${(T232/yr/1e9).toFixed(1)} 億年 の振動`);
console.log('      ★ これは 140 億年 待たないと、一周期すら見えません。\n');
console.log('  ★ 同じ「1.6×10⁻¹⁸ /s」という数字なのに、');
console.log('    実軸にあれば測れず、虚軸にあれば 1 秒 で測れる。\n');
console.log('  ── 第 3 回の「ω=0 には手が届かない」は、');
console.log('    ★ 周期的な成分についての話でした。単調な減衰には当てはまりません。');

console.log('\n##################################################################');
console.log('# 3. なぜ測れるのか ── アボガドロ数が効いている');
console.log('##################################################################\n');
console.log('  種明かしは「数が多い」ことです。1 個 の原子核なら、');
console.log('  ²³²Th が崩壊するのを見るのに、平均 203 億年 待つことになります。\n');
console.log('  ★ でも 1 モル 集めれば、待ち時間は 6×10²³ 分の 1 になる。\n');
console.log('   試料                原子数          崩壊/秒       1 回 待つ時間');
console.log('  '+'-'.repeat(76));
for(const [nm,g] of [['原子 1 個',A232/NA],['1 ng',1e-9],['1 mg',1e-3],['1 g',1],['1 kg',1e3]]){
  const n=g/A232*NA, a=lam232*n;
  const wait=a>0?1/a:Infinity;
  let ws;
  if(wait>yr) ws=(wait/yr).toExponential(2)+' 年';
  else if(wait>1) ws=wait.toFixed(1)+' 秒';
  else if(wait>1e-3) ws=(wait*1e3).toFixed(3)+' ミリ秒';
  else ws=(wait*1e6).toFixed(3)+' マイクロ秒';
  console.log(`  ${nm.padEnd(16)} ${E(n).padStart(12)}    ${E(a).padStart(12)}    ${ws}`);
}
console.log('\n  ★ これは第 9 回の帯域幅定理の「裏返し」です。');
console.log('    一つの系を長く見る代わりに、たくさんの系を一度に見る ──');
console.log('    ★ 時間平均を集団平均で置き換えた。');
console.log('      振動ではこれができません（位相がばらばらだから）。');
console.log('      ★ 崩壊で できるのは、各原子核が独立で、向きを持たないからです。');

console.log('\n##################################################################');
console.log('# 4. 半減期の梯子 ── 65 桁');
console.log('##################################################################\n');
const ladder=[
  ['Δ(1232) 共鳴',   5.63e-24,  '強い相互作用'],
  ['π⁰',            8.43e-17,  '電磁相互作用'],
  ['μ',             2.1969811e-6,'弱い相互作用'],
  ['中性子',         878.4,     '★ 弱い。宇宙初期に効く'],
  ['³H（トリチウム）', 12.32*yr,  ''],
  ['¹⁴C',           5700*yr,   '考古学の時計'],
  ['²³⁸U',          4.468e9*yr,'★ 地質の時計'],
  ['²³²Th',         14.05e9*yr,'★ 宇宙年齢とほぼ同じ'],
  ['¹⁴⁷Sm',         1.06e11*yr,''],
  ['¹³⁰Te（2νββ）',  7.9e20*yr, '二重ベータ崩壊'],
  ['¹²⁸Te（2νββ）',  2.2e24*yr, '★ 測定された最長の半減期'],
  ['陽子崩壊（下限）',  1.6e34*yr, '★ まだ一度も見ていない'],
];
console.log('   崩壊                半減期 [s]        Γ = ħ/τ [eV]      宇宙年齢との比');
console.log('  '+'-'.repeat(84));
for(const [nm,t,note] of ladder){
  const tau=t/Math.LN2;
  const G=hbar/tau/eV;
  console.log(`  ${nm.padEnd(16)} ${E(t).padStart(12)}      ${E(G).padStart(12)}      ${E(t/Tuniv).padStart(10)}   ${note}`);
}
console.log('\n  ★ 半減期で 65 桁、線幅でも 65 桁。');
console.log('    第 9 回で「Fe-57 の自然幅 4.7×10⁻⁹ eV は極端に鋭い」と書きましたが、');
console.log(`    ²³²Th の線幅は ${E(hbar/(T232/Math.LN2)/eV)} eV ── さらに 24 桁 鋭い。\n`);
{
  const Q=4.0816e6;   // ²³²Th の α 崩壊 Q 値 [eV]
  const G=hbar/(T232/Math.LN2)/eV;
  console.log(`      ²³²Th の相対線幅 Γ/Q = ${E(G/Q)}`);
  console.log(`      Fe-57（第 9 回）      = 3.24×10⁻¹³`);
  console.log(`      ★ 比 = ${E(G/Q/3.24e-13)} ── 27 桁 鋭い\n`);
}
console.log('  ★ ただし、この鋭さは使えません。');
console.log('    共鳴として叩くには、それだけ精密な励起源が要るからです。');
console.log('    ── だから数えるほうを使う。★ 虚軸は「数える」、実軸は「叩く」。');

console.log('\n##################################################################');
console.log('# 5. 宇宙年齢のそばにあるものだけが、時計になれる');
console.log('##################################################################\n');
console.log('  年代測定に使える核種には、はっきりした条件があります：\n');
console.log('      速すぎると → もう残っていない');
console.log('      遅すぎると → まだ減っていない\n');
console.log('  宇宙年齢 138 億年 のあいだの残存率を計算します：\n');
console.log('   核種        半減期 [億年]    残存率        使えるか');
console.log('  '+'-'.repeat(70));
for(const [nm,t] of [['²³⁵U',0.704e9],['⁴⁰K',1.248e9],['²³⁸U',4.468e9],['²³²Th',14.05e9],['⁸⁷Rb',49.7e9],['¹⁴⁷Sm',106e9],['¹²⁸Te',2.2e24]]){
  const f=Math.pow(2,-13.787e9/t);
  let j;
  if(f<1e-4) j='△ ほぼ枯渇';
  else if(f>0.99) j='△ ほぼ減らない';
  else j='★ よい時計';
  const ts=(t/1e8>1e6)?(t/1e8).toExponential(2):(t/1e8).toFixed(2);
  console.log(`  ${nm.padEnd(10)} ${ts.padStart(12)}     ${E(f).padStart(10)}    ${j}`);
}
console.log('\n  ★ では「最適な半減期」はいくつか。計算してみます。\n');
console.log('  残った数 N を数えて年代 t を出すとき、ポアソン誤差 √N が効くので：\n');
console.log('      δt = (1/λ)·(1/√N) = e^(λt/2)/(λ√N₀)\n');
console.log('  これを λ について最小化すると：\n');
console.log('      d/dλ [ λt/2 − ln λ ] = 0     →     λ = 2/t     →     T½ = (ln2)·t/2\n');
const Topt=Math.LN2*13.787e9/2;
console.log(`      最適な半減期 = ln2 × 137.9億年 / 2 = ${(Topt/1e8).toFixed(2)} 億年 = ${E(Topt)} 年\n`);
console.log('   核種        半減期 [億年]     最適値との比');
console.log('  '+'-'.repeat(52));
for(const [nm,t] of [['²³⁵U',0.704e9],['⁴⁰K',1.248e9],['²³⁸U',4.468e9],['²³²Th',14.05e9],['⁸⁷Rb',49.7e9]]){
  console.log(`  ${nm.padEnd(10)} ${(t/1e8).toFixed(2).padStart(12)}     ${(t/Topt).toFixed(3)}`);
}
console.log('\n  ★ ²³⁸U（44.68 億年）が、最適値 47.8 億年 の 0.935 倍。');
console.log('    ── 7 % 以内 で、理想の時計です。\n');
console.log('  ★ もちろん偶然です。自然が我々のために選んだわけではない。');
console.log('    ★ でも「なぜ地質学が ²³⁸U を使うのか」の理由にはなっています ──');
console.log('      使えるものが、たまたまそこにあった。');
console.log('    ★ 判定：この最適化は本稿の計算で、理想化されています');
console.log('      （実際の年代測定は娘核種との比を質量分析で測るので、条件が違う）。');

console.log('\n##################################################################');
console.log('# 6. 崩壊定数は、本当に定数か');
console.log('##################################################################\n');
console.log('  第 4 回で α の時間変化を調べました。崩壊定数はどうか。\n');
const claims=[
  ['季節変動の主張（2008〜）',  '× ほぼ否定', '地下実験・恒温実験で再現せず。環境効果が有力'],
  ['⁷Be の電子捕獲',          '○ 本物',     '化学環境で 0.1〜1 % 変わる（C60 内包など）'],
  ['★ 完全電離した ¹⁸⁷Re',    '◎ 本物',     '★ 416 億年 → 32.9 年（10⁹ 倍）'],
  ['圧力・温度依存',           '○ 小さい',   '電子捕獲でのみ。α 崩壊はほぼ不変'],
  ['α（微細構造定数）依存',     '◎ 理論',     '★ α 崩壊は指数関数的に効く（次の節）'],
];
console.log('   主張／現象                判定          中身');
console.log('  '+'-'.repeat(86));
for(const [a,b,c] of claims) console.log(`  ${a.padEnd(24)} ${b.padEnd(13)} ${c}`);
console.log('\n  ★ いちばん強烈なのは ¹⁸⁷Re です。');
console.log('    中性原子なら半減期 416 億年。ところが電子を全部 剥がすと 32.9 年。');
console.log(`    ★ ${E(41.6e9/32.9)} 倍 の変化 ──`);
console.log('      束縛状態へのベータ崩壊が開くからです。\n');
console.log('  ★ つまり「崩壊定数」は、原子核だけの性質ではありません。');
console.log('    周りの電子の状態まで含めた、系全体の性質。');
console.log('    ── 第 6 回の言葉では、★ 終状態の「モード密度」が変わると遷移率が変わる。');
console.log('      これはパーセルの効果（共振器で自然放出が変わる）と同じ理屈です。');

console.log('\n##################################################################');
console.log('# 7. α 崩壊は、微細構造定数の超高感度センサー');
console.log('##################################################################\n');
console.log('  α 崩壊はトンネル効果です。ガモフ因子が効きます：\n');
console.log('      λ ∝ exp(−2πη),      η = Z_d Z_α α c/v\n');
console.log('  α を少し動かすと、λ がどれだけ動くか（障壁の部分だけ）：\n');
console.log('      d ln λ / d ln α = −2πη\n');
const alpha=7.2973525693e-3, mAlpha=3727.379;   // MeV
console.log('   親核        娘核 Z     Q [MeV]     v/c        η        −2πη');
console.log('  '+'-'.repeat(76));
for(const [nm,Zd,Q] of [['²³⁸U',90,4.270],['²³²Th',88,4.0816],['²²⁶Ra',86,4.871],['²¹⁰Po',82,5.407]]){
  const beta=Math.sqrt(2*Q/mAlpha);
  const eta=Zd*2*alpha/beta;
  console.log(`  ${nm.padEnd(10)} ${String(Zd).padStart(6)}    ${Q.toFixed(3).padStart(7)}    ${beta.toFixed(5)}   ${eta.toFixed(3).padStart(7)}   ${(-2*Math.PI*eta).toFixed(1).padStart(8)}`);
}
console.log('\n  ★ ²³⁸U で −172。つまり α が 0.1 % 変わると、崩壊率が 17 % 変わる。');
console.log('    ★ 第 4 回で「α の変化は 10⁻¹⁷/年 以下」と書きましたが、');
console.log('      α 崩壊はその制限を得るための、もっとも感度の高い道具の一つです。\n');
console.log('  ── ただし Q 値自体も α に依存する（クーロンエネルギー）ので、');
console.log('    実際の感度はもっと大きく、文献では 10³ 程度とされます。');
console.log('    ★ 判定：上の −172 は障壁の寄与だけを計算したもので、全体ではありません。');

console.log('\n##################################################################');
console.log('# 8. 弱い力はなぜ弱いのか ── 結合ではなく遮断のせい');
console.log('##################################################################\n');
console.log('  弱い相互作用の「弱さ」の正体を、第 6 回の言葉で見ます。\n');
const s2w=0.23122, aem=1/127.951;
const aW=aem/s2w;
console.log(`      α_em(m_Z) = 1/${(1/aem).toFixed(2)} = ${aem.toFixed(6)}`);
console.log(`      α_W       = α_em/sin²θ_W = ${aW.toFixed(6)} = 1/${(1/aW).toFixed(1)}\n`);
console.log(`  ★ 弱い相互作用の結合は、電磁気より ${(aW/aem).toFixed(2)} 倍 強い。\n`);
console.log('  では何が弱いのか ── プロパゲータです：\n');
console.log('      振幅 ∝ g²/(q² − M_W²)      低エネルギーでは ∝ g²/M_W²\n');
const MW=80.377;
console.log('   運動量移行 q         弱/電磁 の比        どこ');
console.log('  '+'-'.repeat(70));
for(const [q,wh] of [[0.001,'原子核のベータ崩壊（MeV）'],[0.1,'核子の内部'],[1,'1 GeV'],[10,'10 GeV'],[MW,'★ M_W ── 同じ強さに'],[1000,'1 TeV']]){
  const r=(aW/aem)*q*q/(q*q+MW*MW);
  console.log(`  ${E(q).padStart(10)} GeV    ${E(r).padStart(12)}      ${wh}`);
}
console.log('\n  ★ 1 MeV では 10⁻⁹、M_W では 2 倍 ── ★ これが電弱統一です。');
console.log('    「弱い力が弱い」は、低エネルギーでだけ成り立つ話でした。\n');
console.log('  ★ 第 6 回の言葉に翻訳すると ──\n');
console.log(`      M_W は遮断周波数。到達距離 ħ/(M_W c) = ${E(hbarGeV*2.99792458e8/MW*1e15)} fm`);
console.log('      遮断より下ではエバネッセントになり、指数関数的に減衰する。\n');
console.log('  ★ そして第 18 回で見たとおり、その遮断を作っているのはヒッグス凝縮です。');
console.log('    ── ★ 「弱い力が弱い」「超伝導体が磁場を締め出す」「陽子が重い」は、');
console.log('      全部 同じ「分散関係に切片ができる」話でした。');

console.log('\n##################################################################');
console.log('# 9. G_F から、ミューオンの寿命を出す');
console.log('##################################################################\n');
console.log('  弱い崩壊定数が本当に効いていることを、数値で確かめます：\n');
console.log('      Γ_μ = G_F² m_μ⁵ / (192π³)\n');
const GF=1.1663787e-5, mmu=0.1056583755;
const Gmu=GF*GF*Math.pow(mmu,5)/(192*Math.pow(Math.PI,3));
const taumu=hbarGeV/Gmu;
console.log(`      G_F = ${GF} GeV⁻²,   m_μ = ${mmu} GeV`);
console.log(`      Γ_μ = ${E(Gmu)} GeV`);
console.log(`      τ_μ = ħ/Γ = ${E(taumu)} s`);
console.log(`      実測  τ_μ = 2.1969811e-6 s`);
console.log(`      ★ 比 = ${(taumu/2.1969811e-6).toFixed(5)}   ── ${((1-taumu/2.1969811e-6)*100).toFixed(2)} % 一致\n`);
console.log('  ★ 3 桁 合いました。残りの 0.5 % は位相空間と輻射補正です。\n');
console.log('  ★ τ ∝ 1/m⁵ という強い依存に注目してください。');
console.log('    タウ粒子で試します：\n');
const mtau=1.77686;
const scale=Math.pow(mtau/mmu,5);
const tauPred=2.1969811e-6/scale;
const tauObs=2.903e-13;
console.log(`      (m_τ/m_μ)⁵ = ${E(scale)}`);
console.log(`      予言 τ_τ = ${E(tauPred)} s      （崩壊路が 1 本 なら）`);
console.log(`      実測 τ_τ = ${E(tauObs)} s`);
console.log(`      ★ 比 = ${(tauPred/tauObs).toFixed(2)}\n`);
console.log('  ★ 5.6 倍 速く崩壊している ── 崩壊路が 5.6 本 あるということ。');
console.log('    数えてみます：\n');
console.log('      τ → e ν ν     : 1 本');
console.log('      τ → μ ν ν     : 1 本');
console.log('      τ → ハドロン   : u d̄ の組。★ 色が 3 つ あるので 3 本\n');
const asTau=0.33;
const expect=2+3*(1+asTau/Math.PI);
console.log(`      合計 = 2 + 3×(1 + α_s/π) = 2 + 3×${(1+asTau/Math.PI).toFixed(3)} = ${expect.toFixed(2)}`);
console.log(`      実測から出た本数                        = ${(tauPred/tauObs).toFixed(2)}\n`);
console.log('  ★ 5.3 対 5.6 ── 6 % の一致です。');
console.log('    ★ タウの寿命から、クォークの色の数 3 が出てきました。');
console.log('      判定：これは既知の古典的な議論の再現で、新しい主張ではありません');
console.log('      （カビボ角やカットの扱いを省いているので、この精度が限界）。');

console.log('\n##################################################################');
console.log('# 10. 中性子の寿命が、宇宙の組成を決めた');
console.log('##################################################################\n');
console.log('  最後に、弱い崩壊定数が宇宙に残した跡を見ます。\n');
console.log('  ビッグバン元素合成の筋書き：\n');
console.log('      ① T ≈ 0.7 MeV（t ≈ 1 秒）で弱い反応が凍結 → n/p ≈ 1/6');
console.log('      ② そこから数百秒、中性子が崩壊し続ける（τ_n = 878 秒）');
console.log('      ③ 重水素の関門が開くと、残った中性子が全部 ⁴He になる\n');
const tn=878.4;              // 中性子の平均寿命 [s]
console.log('   τ_n [秒]     t_nuc=250 秒 後の n/p     ヘリウム質量比 Y_p');
console.log('  '+'-'.repeat(66));
for(const t of [tn/4,tn/2,tn,tn*2,tn*4,1e9]){
  const x=(1/6)*Math.exp(-250/t);
  const Y=2*x/(1+x);
  console.log(`  ${E(t).padStart(10)}      ${x.toFixed(5).padStart(12)}          ${Y.toFixed(4)}`);
}
console.log(`\n      実測の τ_n = ${tn} 秒 → Y_p = ${(2*((1/6)*Math.exp(-250/tn))/(1+(1/6)*Math.exp(-250/tn))).toFixed(4)}`);
console.log('      観測された Y_p = 0.245\n');
console.log('  ★ 粗い見積もりで 0.223。観測は 0.245 ── 1 割 の差です。');
console.log('    （凍結温度と t_nuc を丸めているため。本物の計算は 0.5 % で合います）\n');
console.log('  ★ 大事なのは感度のほうです ──');
console.log('    中性子の寿命が 4 分の 1 なら Y_p = 0.17、4 倍 なら 0.28。');
console.log('    ★ 弱い崩壊定数が、宇宙のヘリウム量を直接 決めている。\n');
console.log('  ── そして中性子の寿命 878 秒 と、元素合成の時刻 ~250 秒 が');
console.log('    同じ桁である ★ のは、この物語が成立するための条件でした。');
console.log('    寿命が 10 倍 短ければ中性子は全部 消え、水素だけの宇宙になっていた。');

console.log('\n##################################################################');
console.log('# 11. まとめ');
console.log('##################################################################\n');
const sm=[
  ['崩壊定数 ＝ 虚数の周波数',  '◎ 厳密',  '★ e^(−λt) = e^(i(iλ)t)'],
  ['虚軸は一周期 待たなくてよい','◎ 計算',  '★ ²³²Th 1 g で 4057 Bq'],
  ['半減期の梯子は 65 桁',     '◎ 文献',  'Δ 共鳴から陽子崩壊まで'],
  ['最適な時計は T½ = 47.8 億年','○ 本稿',  '★ ²³⁸U が 0.935 倍'],
  ['¹⁸⁷Re は電離で 10⁹ 倍',    '◎ 実測',  '崩壊定数は系全体の性質'],
  ['α 崩壊の α 感度 −172',    '◎ 計算',  '障壁部分のみ。全体は 10³ 級'],
  ['α_W > α_em（4.3 倍）',    '◎ 計算',  '★ 弱いのは結合ではなく遮断'],
  ['τ_μ = 2.187 μs',        '◎ 計算',  '実測と 0.45 % 一致'],
  ['タウの寿命から色数 3',      '○ 計算',  '5.6 対 5.3'],
  ['Y_p は τ_n で決まる',     '△ 粗い',  '0.223 対 観測 0.245'],
];
console.log('  主張                        判定      根拠');
console.log('  '+'-'.repeat(80));
for(const [a,b,c] of sm) console.log(`  ${a.padEnd(26)} ${b.padEnd(9)} ${c}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     「宇宙年齢より長いものは定数と区別がつかない」は、');
console.log('     振動についての話だった。');
console.log('     ── 崩壊は虚軸に住んでいるので、一周期 待たずに測れる。');
