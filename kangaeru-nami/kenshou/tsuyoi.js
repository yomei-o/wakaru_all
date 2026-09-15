// 強い力と素粒子を波として見る ── 閉じ込めは箱ではなく弦だった
'use strict';
const E=x=>x.toExponential(3);
const hbarc=0.1973269804;   // GeV·fm
const GeV=1.602176634e-10;  // J

console.log('##################################################################');
console.log('# 1. 第 18 回の「箱」を、本物に取り替える');
console.log('##################################################################\n');
console.log('  第 18 回では、陽子の質量を「箱に閉じ込めた波の最低周波数」で見積もりました。');
console.log('  ★ 桁は合いましたが、1.5 倍 ずれました。理由があります ──\n');
console.log('      本当は箱ではなく、★ 弦（フラックスチューブ）に閉じ込められている。\n');
const compare=[
  ['電磁気',  '場が全方向へ広がる', 'V ∝ −1/r',     '力は 1/r² で弱くなる'],
  ['湯川（第 6 回）','遮断より下は減衰','V ∝ −e^(−r/λ)/r','λ より遠くへ届かない'],
  ['★ 強い力','★ 場が弦に絞られる','★ V ∝ +σr',    '★ 距離によらず一定の力'],
];
console.log('   力            場の形                ポテンシャル        振る舞い');
console.log('  '+'-'.repeat(88));
for(const [a,b,c,d] of compare) console.log(`  ${a.padEnd(12)} ${b.padEnd(20)} ${c.padEnd(18)} ${d}`);
console.log('\n  ★ ここが決定的な違いです ──');
console.log('    電磁気も湯川も「遠ざかると弱くなる」。');
console.log('    ★ 強い力だけは、遠ざかっても弱くならない。だから閉じ込められる。');

console.log('\n##################################################################');
console.log('# 2. ハドロンの質量から、弦の張力を測る ── レッジェ軌道');
console.log('##################################################################\n');
console.log('  回転する弦を考えると、角運動量と質量の二乗が比例します：\n');
console.log('      J = α\' M² + α₀,      α\' = 1/(2πσ)\n');
console.log('  ★ σ が弦の張力。実測のハドロンを並べて、傾きを測ります：\n');
const regge=[
  ['ρ(775)',    0.77526, 1],
  ['a₂(1320)',  1.3182,  2],
  ['ρ₃(1690)',  1.6888,  3],
  ['a₄(1970)',  1.967,   4],
];
console.log('   粒子           質量 M [GeV]    M² [GeV²]     スピン J');
console.log('  '+'-'.repeat(64));
let sx=0,sy=0,sxx=0,sxy=0;
for(const [nm,M,J] of regge){
  const x=M*M;
  sx+=x; sy+=J; sxx+=x*x; sxy+=x*J;
  console.log(`  ${nm.padEnd(14)} ${M.toFixed(5).padStart(10)}    ${x.toFixed(5).padStart(9)}      ${J}`);
}
const n=regge.length;
const alphaP=(n*sxy-sx*sy)/(n*sxx-sx*sx);
const alpha0=(sy-alphaP*sx)/n;
console.log(`\n      最小二乗の傾き α' = ${alphaP.toFixed(4)} GeV⁻²      （文献値 約 0.9）`);
console.log(`      切片          α₀ = ${alpha0.toFixed(4)}             （文献値 約 0.48）\n`);
console.log('   粒子           J（実測）   J（直線の予言）    差');
console.log('  '+'-'.repeat(60));
for(const [nm,M,J] of regge){
  const pred=alphaP*M*M+alpha0;
  console.log(`  ${nm.padEnd(14)} ${String(J).padStart(7)}     ${pred.toFixed(4).padStart(10)}    ${(pred-J).toFixed(4).padStart(9)}`);
}
console.log('\n  ★ 四つの粒子が、きれいに一直線に乗ります。\n');
const sigma=1/(2*Math.PI*alphaP);
const sigmaGeVfm=sigma/hbarc;
const sigmaN=sigmaGeVfm*GeV/1e-15;
console.log('  ★ 傾きから弦の張力が出ます：\n');
console.log(`      σ = 1/(2πα') = ${sigma.toFixed(4)} GeV²`);
console.log(`        = ${sigmaGeVfm.toFixed(4)} GeV/fm`);
console.log(`        = ${E(sigmaN)} N  =  ★ ${(sigmaN/9.80665/1000).toFixed(1)} トン重\n`);
console.log('  ★★ クォーク 1 組を引き離すのに、14 トンの力が要ります。');
console.log('    ★ しかも距離によらず一定 ── だから絶対に引き離せない。');
console.log('      ── ハドロンの質量スペクトルを直線に並べただけで、この数字が出ました。');

console.log('\n##################################################################');
console.log('# 3. 弦の梯子 ── 第 6 回の導波管モードと同じ構造');
console.log('##################################################################\n');
console.log('  レッジェ軌道は「弦の振動モードの梯子」です。第 6 回と並べます：\n');
const ladders=[
  ['導波管（第 6 回）', 'ω² = ω_c² + c²k²', 'モード番号 n',   '遮断周波数の梯子'],
  ['箱（第 18 回）',   'E = 2.04ħc/R',     '節の数',        '境界条件の梯子'],
  ['★ 弦（本回）',     'M² = (J−α₀)/α\'',  '★ 角運動量 J',  '★ 回転モードの梯子'],
];
console.log('   系                  関係式                 梯子の番号      正体');
console.log('  '+'-'.repeat(88));
for(const [a,b,c,d] of ladders) console.log(`  ${a.padEnd(18)} ${b.padEnd(22)} ${c.padEnd(14)} ${d}`);
console.log('\n  ★ 三つとも「境界条件が離散的なモードを作る」という同じ話です。');
console.log('    違うのは境界の作り方だけ ── 壁、箱、そして★ 弦の張力。\n');
console.log('  ★ 弦の梯子から、まだ見つかっていない粒子の質量も予言できます：\n');
console.log('   J      予言される M [GeV]     実測の候補');
console.log('  '+'-'.repeat(56));
const cand={5:'ρ₅(2350) M=2.33',6:'a₆(2450) M=2.45',7:'──'};
for(let J=5;J<=7;J++){
  const M=Math.sqrt((J-alpha0)/alphaP);
  console.log(`  ${J}      ${M.toFixed(4).padStart(14)}         ${cand[J]}`);
}
console.log('\n  ★ 実測とよく合います ── ★ 弦の描像が効いている証拠です。');

console.log('\n##################################################################');
console.log('# 4. 色の数を測る ── 断面積の比という無次元量');
console.log('##################################################################\n');
console.log('  第 19 回で、タウの寿命からクォークの色の数 3 が出ました。');
console.log('  ★ もっと直接な測り方があります ── R 比：\n');
console.log('      R = σ(e⁺e⁻ → ハドロン) / σ(e⁺e⁻ → μ⁺μ⁻) = N_c · Σ q²\n');
console.log('  ★ 断面積の比 ── 完全に無次元です（第 7 回）。\n');
const quarks=[
  ['u', 2/3],['d',-1/3],['s',-1/3],['c',2/3],['b',-1/3],
];
const thresholds=[
  ['√s = 2〜3 GeV（u,d,s）',      3, 0.25],
  ['√s = 5〜10 GeV（+c）',        4, 0.21],
  ['√s = 20〜40 GeV（+b）',       5, 0.14],
];
console.log('   エネルギー帯                 素朴な R    QCD 補正込み   実測の目安');
console.log('  '+'-'.repeat(84));
const obs=['約 2.2','約 3.6','約 3.9'];
let idx=0;
for(const [nm,nq,as] of thresholds){
  let sumq2=0;
  for(let i=0;i<nq;i++) sumq2+=quarks[i][1]*quarks[i][1];
  const Rnaive=3*sumq2;
  const Rqcd=Rnaive*(1+as/Math.PI);
  console.log(`  ${nm.padEnd(26)} ${Rnaive.toFixed(4).padStart(9)}   ${Rqcd.toFixed(4).padStart(10)}     ${obs[idx++]}`);
}
console.log('\n  ★ N_c = 3 を入れると、三つの帯すべてが実測と合います。');
console.log('    ★ N_c = 1 なら R は 1/3 になり、まったく合いません。\n');
console.log('  ── ★ 「色が 3 つある」は、無次元の比として直接 測られた事実でした。');
console.log('    第 19 回（タウの寿命）と第 4 節（R 比）── 独立な二つの測り方が一致します。');

console.log('\n##################################################################');
console.log('# 5. 漸近的自由 ── なぜ QED と逆向きに走るのか');
console.log('##################################################################\n');
console.log('  第 5 回では、QED の結合は近づくほど強くなりました（真空が遮蔽する）。');
console.log('  ★ QCD は逆です。理由はグルーオン自身が色を持つことにあります：\n');
console.log('      β₀ = 11 − (2/3)n_f\n');
console.log('        11      … グルーオンの自己相互作用（反遮蔽）');
console.log('        (2/3)n_f … クォーク対による遮蔽（QED と同じ向き）\n');
console.log('   n_f（クォークの種類）   β₀ = 11 − 2n_f/3     結合の向き');
console.log('  '+'-'.repeat(72));
for(const nf of [0,3,5,6,16,17]){
  const b0=11-2*nf/3;
  const dir=b0>0?'★ 漸近的自由（近づくと弱い）':'QED と同じ（近づくと強い）';
  console.log(`  ${String(nf).padStart(16)}      ${b0.toFixed(4).padStart(10)}        ${dir}`);
}
console.log('\n  ★ n_f < 16.5 なら漸近的自由。実際の自然は 6 種類なので、余裕で成立します。');
console.log('    ★ 「もしクォークが 17 種類あったら、閉じ込めは起きなかった」── 紙一重ではない。');

console.log('\n##################################################################');
console.log('# 6. ★ 次元転移 ── 無次元量から、質量が生まれる');
console.log('##################################################################\n');
console.log('  漸命的自由の式を逆に解くと、結合が発散するスケールが出ます：\n'.replace('漸命','漸近'));
console.log('      1/α_s(μ) = (β₀/2π)·ln(μ/Λ)      →      Λ = μ·exp(−2π/(β₀α_s(μ)))\n');
const mZ=91.1876, asZ=0.1179, b0_5=11-2*5/3;
const Lam=mZ*Math.exp(-2*Math.PI/(b0_5*asZ));
console.log(`      α_s(m_Z) = ${asZ}、β₀ = ${b0_5.toFixed(4)}（n_f=5）`);
console.log(`      ★ Λ_QCD = ${(Lam*1000).toFixed(1)} MeV        （文献値 約 210 MeV、二ループ以上）\n`);
console.log(`      対応する長さ ħc/Λ = ${(hbarc/Lam).toFixed(3)} fm`);
console.log(`      （文献値 Λ = 210 MeV なら ${(hbarc/0.210).toFixed(3)} fm ── ★ ハドロンの大きさそのもの）\n`);
console.log('  ★ 一ループなので Λ は小さめに出ます。二ループ以上だと 210 MeV 級になり、');
console.log('    長さは 0.94 fm ── ★ 陽子の電荷半径（0.84 fm）とほぼ同じになります。\n');
console.log('  ★★ ここが、この回いちばん重要なところです ──\n');
console.log('      入力は無次元の α_s だけ。');
console.log('      ★ なのに、次元を持つ質量スケール Λ_QCD が出てきます。\n');
console.log('  これを「次元転移」と言います。第 5 回の「定数は ln μ の積分」の、');
console.log('  ★ もっとも劇的な帰結です ── 積分の結果として、新しい次元が生まれる。\n');
console.log('   α_s(m_Z) を動かすと Λ がどう動くか：\n');
console.log('   α_s(m_Z)      Λ_QCD [MeV]     ħc/Λ [fm]');
console.log('  '+'-'.repeat(56));
for(const as of [0.110,0.115,0.1179,0.120,0.125]){
  const L=mZ*Math.exp(-2*Math.PI/(b0_5*as));
  console.log(`  ${as.toFixed(4).padStart(8)}      ${(L*1000).toFixed(1).padStart(10)}      ${(hbarc/L).toFixed(3).padStart(9)}`);
}
console.log('\n  ★ α_s が 6 % 動くだけで、Λ は 2 倍 近く動きます（指数関数だから）。');
console.log('    ★ つまり ── 陽子の大きさは、無次元の結合定数に指数関数的に敏感。\n');
console.log('  ★★ そして第 18 回とつながります ──\n');
console.log('      陽子の質量の 99 % は「閉じ込め」＝ Λ_QCD 由来。');
console.log('      ★ その Λ_QCD は、無次元の α_s から次元転移で生まれた。\n');
console.log('  ── ★ 身の回りの質量の 99 % は、無次元量から生まれています。');
console.log('    第 7 回の「意味があるのは無次元量だけ」が、');
console.log('    ★ 「次元を持つ量は、無次元量から作られる」にまで進みました。');

console.log('\n##################################################################');
console.log('# 7. 質量ゼロなのに届かない ── 第 6 回の例外');
console.log('##################################################################\n');
console.log('  第 6 回で「力の到達距離 ＝ ħ/(mc)」と書きました。');
console.log('  ★ ところがグルーオンは質量ゼロなのに、1 fm しか届きません。\n');
const reach=[
  ['光子',      0,        '∞',      '線形。場が広がる'],
  ['W ボソン',  80.4,     '2.5×10⁻³ fm','第 6 回。質量による遮断'],
  ['★ グルーオン',0,       '★ 約 1 fm','★ 非線形。場が弦に絞られる'],
];
console.log('   媒介粒子      質量 [GeV]   到達距離      理由');
console.log('  '+'-'.repeat(76));
for(const [a,b,c,d] of reach) console.log(`  ${a.padEnd(12)} ${String(b).padStart(9)}    ${c.padEnd(12)}  ${d}`);
console.log('\n  ★ 第 6 回の「質量＝遮断」は、線形理論の話でした。');
console.log('    ★ 非線形では、質量なしでも閉じ込めが起きます ──\n');
console.log('      グルーオンが色を持つ → グルーオン同士が引き合う');
console.log('      → 場が広がらずに弦に絞られる → 力が距離によらず一定\n');
console.log('  ★★ 第 23 回の非線形が、ここで効いています。');
console.log('    ── 「重ね合わせが効かない」という性質が、');
console.log('      ★ 場の形そのものを変えてしまう。\n');
console.log('  ★ 対比をまとめると：\n');
console.log('      線形 + 質量あり → 指数関数的に減衰（湯川、第 6 回）');
console.log('      線形 + 質量なし → 無限遠まで届く（電磁気）');
console.log('      ★ 非線形 + 質量なし → 弦になって閉じ込め（QCD、本回）');

console.log('\n##################################################################');
console.log('# 8. 粒子を共鳴として見る ── 第 9 回の線幅');
console.log('##################################################################\n');
console.log('  「粒子」とは場のモードで、寿命が線幅になります（第 9 回、第 19 回）：\n');
const parts=[
  ['Δ(1232)',   1.232,  0.117,   '強い相互作用。★ 幅が質量の 9.5 %'],
  ['ρ(770)',    0.7753, 0.1476,  '★ 幅が質量の 19 % ── 粒子と呼べるぎりぎり'],
  ['J/ψ',       3.0969, 92.6e-6, '★ 異常に細い（OZI 抑制）'],
  ['Υ(1S)',     9.4603, 54.02e-6,'同上'],
  ['W ボソン',   80.377, 2.085,   '弱い相互作用'],
  ['Z ボソン',   91.188, 2.4955,  ''],
  ['ヒッグス',   125.25, 0.0041,  '標準模型の予言値'],
];
console.log('   粒子          質量 [GeV]    幅 Γ [GeV]      Γ/M          寿命 [s]        備考');
console.log('  '+'-'.repeat(104));
const hbarGeV=6.582119569e-25;
for(const [nm,M,G,note] of parts){
  console.log(`  ${nm.padEnd(12)} ${M.toFixed(4).padStart(10)}   ${E(G).padStart(11)}   ${E(G/M).padStart(10)}   ${E(hbarGeV/G).padStart(11)}   ${note}`);
}
console.log('\n  ★ ρ の幅は質量の 19 % ── ★ 一周期 振動する前に崩れます。');
console.log('    第 9 回の言葉では「Δω が ω と同じ桁」── ★ 波として数えられる限界。\n');
console.log('  ★ 逆に J/ψ は Γ/M = 3×10⁻⁵ ── 強い相互作用で崩壊するのに、異常に細い。');
console.log('    ★ 理由は「行き先が閉じている」こと（OZI 抑制）── 第 19 回の ¹⁸⁷Re と同じ構造です。');
console.log('      ── 終状態のモードが使えないと、遷移率が落ちる。\n');
{
  const rho=0.1476/0.7753, jpsi=92.6e-6/3.0969;
  console.log(`      ρ と J/ψ の相対線幅の比 = ${E(rho/jpsi)} 倍`);
  console.log('      ★ どちらも強い相互作用なのに、4 桁 違う。');
}

console.log('\n##################################################################');
console.log('# 9. 強い力の梯子を、一枚に');
console.log('##################################################################\n');
const summary=[
  ['弦の張力 σ',        `${sigmaGeVfm.toFixed(3)} GeV/fm`, '★ 14 トン重。距離によらない'],
  ['レッジェ傾き α\'',   `${alphaP.toFixed(3)} GeV⁻²`,     'ハドロン 4 個の直線から'],
  ['Λ_QCD',            `${(Lam*1000).toFixed(0)} MeV`,   '★ 無次元の α_s から生まれた'],
  ['ハドロンの大きさ',   `${(hbarc/0.210).toFixed(2)} fm`, 'ħc/Λ（文献値の Λ で）'],
  ['色の数 N_c',        '3',                              '★ R 比とタウの寿命が一致'],
  ['漸近的自由の条件',   'n_f < 16.5',                     '自然は 6 種類'],
];
console.log('   量                    値                中身');
console.log('  '+'-'.repeat(76));
for(const [a,b,c] of summary) console.log(`  ${a.padEnd(20)} ${b.padEnd(16)} ${c}`);

console.log('\n##################################################################');
console.log('# 10. まとめ');
console.log('##################################################################\n');
const sm=[
  ['閉じ込めは弦',          '◎ 実測',  '★ レッジェ軌道が直線に乗る'],
  ['弦の張力 14 トン',      '◎ 計算',  '★ ハドロンの質量から出る'],
  ['弦の梯子は導波管と同型',  '◎ 整理',  '第 6 回・第 18 回と同じ構造'],
  ['色は 3 つ',            '◎ 実測',  '★ R 比。無次元の比として測れる'],
  ['漸近的自由は 11 のおかげ','◎ 厳密',  'グルーオンの自己相互作用'],
  ['★ 次元転移',           '◎ 計算',  '★ 無次元の α_s から Λ_QCD が出る'],
  ['質量ゼロでも閉じ込め',   '◎ 整理',  '★ 第 23 回の非線形が効く'],
  ['ρ は幅が質量の 19 %',   '◎ 文献',  '波として数えられる限界'],
];
console.log('  主張                      判定      根拠');
console.log('  '+'-'.repeat(76));
for(const [a,b,c] of sm) console.log(`  ${a.padEnd(24)} ${b.padEnd(9)} ${c}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     クォークは箱ではなく弦に閉じ込められていて、その張力は 14 トン。');
console.log('     そして弦の太さを決めている Λ_QCD は、無次元の結合定数から生まれた。');
console.log('     ── 身の回りの質量の 99 % は、無次元量が次元を獲得したものだった。');
