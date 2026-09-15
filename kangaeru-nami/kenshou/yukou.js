// 有効質量 ── 分散関係をテイラー展開すると、0次が質量、1次が速度、2次がまた質量
'use strict';
const E=x=>x.toExponential(3);
const c=2.99792458e8;
const hbar=1.054571817e-34;
const me=9.1093837015e-31;
const e_=1.602176634e-19;
const alpha=7.2973525693e-3;
const eV=e_;

console.log('##################################################################');
console.log('# 1. 分散関係をテイラー展開する ── これが本回の骨格');
console.log('##################################################################\n');
console.log('  第 6 回で質量は遮断周波数でした。第 16 回で光速は傾きでした。');
console.log('  ★ どちらも同じ曲線 ω(k) の、違う場所を見ていただけです。\n');
console.log('  k = 0 のまわりで展開してみます：\n');
console.log('      ω(k) = ω₀ + (dω/dk)·k + (1/2)(d²ω/dk²)·k² + …\n');
console.log('   次数   テイラー係数        物理的な意味              出てきた回');
console.log('  '+'-'.repeat(76));
const terms=[
  ['0 次','ω₀',           '★ 静止質量（遮断周波数 mc²/ħ）', '第 6 回'],
  ['1 次','dω/dk',        '★ 群速度（実効光速）',           '第 16 回'],
  ['2 次','d²ω/dk²',      '★ 有効質量の逆数 ħ/m*',          '本回'],
  ['4 次','d⁴ω/dk⁴',      '相対論的補正、非放物線性',        '本回 2 節'],
];
for(const [a,b,cc,d] of terms) console.log(`  ${a.padEnd(6)} ${b.padEnd(18)} ${cc.padEnd(28)} ${d}`);
console.log('\n  ★ つまり ──\n');
console.log('      質量 → 速度 → 質量\n');
console.log('  展開の 0 次と 2 次が、どちらも「質量」と呼ばれています。');
console.log('  ── 同じ言葉が、曲線の違う特徴を指している。\n');
console.log('  有効質量の定義を書き下すと：\n');
console.log('      1/m* = (1/ħ²)·d²E/dk²        （E = ħω）\n');
console.log('  ★ 質量の逆数 ＝ 分散関係の曲率。');

console.log('\n##################################################################');
console.log('# 2. クライン＝ゴルドンで確かめる ── 0 次と 2 次');
console.log('##################################################################\n');
console.log('  相対論的な分散関係を展開します：\n');
console.log('      E = √((mc²)² + (pc)²)');
console.log('        = mc² + p²/(2m) − p⁴/(8m³c²) + …\n');
console.log('  ★ 0 次が静止エネルギー、2 次が古典的な運動エネルギー、');
console.log('    4 次が最初の相対論的補正。数値で確かめます（電子）：\n');
const mc2=me*c*c;
function Eexact(beta){ const g=1/Math.sqrt(1-beta*beta); return g*mc2; }
function Eseries(beta,n){
  const p=me*c*beta/Math.sqrt(1-beta*beta);   // 相対論的運動量
  let s=mc2;
  if(n>=2) s+=p*p/(2*me);
  if(n>=4) s-=Math.pow(p,4)/(8*me*me*me*c*c);
  return s;
}
console.log('   v/c        厳密 E [keV]     2 次まで       誤差        4 次まで      誤差');
console.log('  '+'-'.repeat(86));
for(const b of [0.001,0.01,0.05,0.1,0.3,0.5]){
  const ex=Eexact(b), e2=Eseries(b,2), e4=Eseries(b,4);
  console.log(`  ${b.toFixed(3).padStart(6)}   ${(ex/eV/1e3).toFixed(4).padStart(12)}   ${(e2/eV/1e3).toFixed(4).padStart(12)}  ${E(Math.abs(e2/ex-1)).padStart(10)}  ${(e4/eV/1e3).toFixed(4).padStart(12)}  ${E(Math.abs(e4/ex-1))}`);
}
console.log('\n  ★ v/c = 0.1 までは 2 次だけで 10⁻⁴ の精度。');
console.log('    ── ふつうの物理が「質量は定数」で済むのは、この放物線近似が効くから。\n');
console.log('  逆に言えば ── ★ 有効質量が「定数でなくなる」のは、放物線から外れたとき。');
console.log('    半導体では、これが高い電界で実際に起きます（非放物線性）。');

console.log('\n##################################################################');
console.log('# 3. 固体の中の電子 ── 有効質量は「跳び移りにくさ」');
console.log('##################################################################\n');
console.log('  もっとも簡単な固体の模型（強束縛近似）：\n');
console.log('      E(k) = −2t cos(ka)        t: 隣へ跳び移る強さ、a: 格子間隔\n');
console.log('  k = 0 のまわりで展開すると：\n');
console.log('      E ≈ −2t + t a² k²     →     m* = ħ²/(2ta²)\n');
console.log('  ★ 跳び移りやすい（t が大きい）ほど、軽い。');
console.log('    ── 有効質量とは「動きにくさ」そのものでした。\n');
function tbMass(t_eV,a_nm){
  const t=t_eV*eV, a=a_nm*1e-9;
  // 数値微分で確かめる
  const Ek=k=>-2*t*Math.cos(k*a);
  const h=1e6;   // k の刻み [1/m]
  const d2=(Ek(h)-2*Ek(0)+Ek(-h))/(h*h);
  return {ana:hbar*hbar/(2*t*a*a), num:hbar*hbar/d2};
}
console.log('   t [eV]   a [nm]    m*/m_e（解析）   m*/m_e（数値微分）   差');
console.log('  '+'-'.repeat(74));
for(const [t,a] of [[0.1,0.3],[0.5,0.3],[1.0,0.3],[3.0,0.3],[1.0,0.5]]){
  const r=tbMass(t,a);
  console.log(`  ${t.toFixed(1).padStart(6)}   ${a.toFixed(2).padStart(5)}    ${(r.ana/me).toFixed(6).padStart(12)}   ${(r.num/me).toFixed(6).padStart(16)}   ${E(Math.abs(r.num/r.ana-1))}`);
}
console.log('\n  ★ バンドの「てっぺん」ではどうなるか ── k = π/a で展開します：\n');
{
  const t=1.0*eV, a=0.3e-9, kTop=Math.PI/a;
  const Ek=k=>-2*t*Math.cos(k*a);
  const h=1e6;
  const d2top=(Ek(kTop+h)-2*Ek(kTop)+Ek(kTop-h))/(h*h);
  const mTop=hbar*hbar/d2top;
  console.log(`      バンド底 k=0     : m*/m_e = ${(hbar*hbar/((Ek(h)-2*Ek(0)+Ek(-h))/(h*h))/me).toFixed(4)}`);
  console.log(`      バンド頂 k=π/a   : m*/m_e = ${(mTop/me).toFixed(4)}      ★ 負！`);
}
console.log('\n  ★ バンドの頂上では、有効質量が負になります。');
console.log('    押すと逆に戻る ── これが「正孔（ホール）」の正体です。');
console.log('    ★ 第 10 回で「階数の偶奇が時間の矢を決める」と書きましたが、');
console.log('      ここでは「二階微分の符号が力の向きを決める」。');

console.log('\n##################################################################');
console.log('# 4. 実在の材料 ── 3 桁 にわたる有効質量');
console.log('##################################################################\n');
const mats=[
  ['自由電子（真空）',      1.0,     '基準'],
  ['シリコン（伝導帯）',    0.26,    '集積回路'],
  ['ゲルマニウム',          0.12,    '初期のトランジスタ'],
  ['ガリウムヒ素 GaAs',     0.067,   '高速デバイス・レーザー'],
  ['インジウムアンチモン',  0.014,   '★ 自由電子の 1/70'],
  ['重い電子系（UPt₃ など）',200,    '★ 自由電子の 200 倍'],
];
console.log('   材料                    m*/m_e      サイクロトロン周波数 @1T    用途');
console.log('  '+'-'.repeat(86));
for(const [nm,r,use] of mats){
  const f=e_*1/(r*me)/(2*Math.PI);
  console.log(`  ${nm.padEnd(22)} ${String(r).padStart(7)}     ${E(f).padStart(10)} Hz          ${use}`);
}
console.log('\n  ★ 4 桁 以上 の幅があります。そして重い電子系では 200 倍 ──');
console.log('    ★ 「質量」は材料のパラメータになっている。');
console.log('      第 4 回で「c は定義値だから微分できない」と書きましたが、');
console.log('      有効質量は材料を変えれば変わる ── 微分どころか、自由に設計できます。');

console.log('\n##################################################################');
console.log('# 5. グラフェン ── 質量ゼロ・光速 c/300 の世界');
console.log('##################################################################\n');
console.log('  グラフェンの分散関係は、原点で「円錐」になります：\n');
console.log('      E = ± ħ v_F |k|,      v_F ≈ 1.0×10⁶ m/s\n');
const vF=1.0e6;
console.log(`  ★ これは「質量ゼロの粒子」の分散関係そのものです（E = pc の c を v_F に）。`);
console.log(`      v_F/c = 1/${(c/vF).toFixed(0)}      ── 実効光速が 300 分の 1 の世界\n`);
console.log('  ここで面白いことが起きます。微細構造定数を計算してみると：\n');
console.log('      α = e²/(4πε₀ ħ c)   →   α_graphene = e²/(4πε₀ ħ v_F) = α·(c/v_F)\n');
const ag=alpha*c/vF;
console.log(`      α_graphene = ${alpha.toFixed(8)} × ${(c/vF).toFixed(1)} = ${ag.toFixed(4)}\n`);
console.log('  ★ 2.2 ── 1 より大きい。');
console.log('    ★ グラフェンの中は「強結合の QED」です。');
console.log('      第 5 回で走らせた α は真空で 1/137 でしたが、');
console.log('      ここでは 2.2 ── ★ 摂動論が使えない領域が、机の上にある。\n');
console.log('  質量ゼロなのに「サイクロトロン質量」は定義できます：\n');
console.log('      m_c = E_F/v_F²        ★ エネルギーに依存する質量\n');
console.log('   フェルミ準位 E_F [eV]    m_c/m_e        備考');
console.log('  '+'-'.repeat(62));
for(const ef of [0.01,0.05,0.1,0.3]){
  const mc=ef*eV/(vF*vF);
  console.log(`  ${ef.toFixed(3).padStart(14)}      ${(mc/me).toFixed(6).padStart(10)}      ${ef===0.1?'★ よくある実験条件':''}`);
}
console.log('\n  ★ 質量がエネルギーに比例する ── これは相対論的な分散関係の特徴です。');
console.log('    静止質量ゼロの粒子に「質量」を感じさせているのは、運動エネルギーだけ。');
console.log('    ★ 次回の主題（陽子の質量の 99% は運動エネルギー）の、机上版です。');

console.log('\n##################################################################');
console.log('# 6. 光子に質量を持たせる ── 超伝導体の中');
console.log('##################################################################\n');
console.log('  第 6 回で「質量＝遮断周波数」と書きました。逆をやります ──');
console.log('  ★ 遮断周波数を作ってやれば、光子に質量が生えます。\n');
console.log('  超伝導体の中では磁場が λ_L で減衰します（マイスナー効果）。');
console.log('  第 6 回の言葉では、これはエバネッセント減衰そのもの：\n');
console.log('      減衰長 λ_L = ħ/(m_γ c)      →      m_γ = ħ/(λ_L c)\n');
const supers=[
  ['アルミニウム',    16e-9],
  ['鉛',              37e-9],
  ['ニオブ',          39e-9],
  ['YBCO（高温超伝導）',150e-9],
];
console.log('   物質                  λ_L [nm]    光子の質量 [kg]     エネルギー [eV]');
console.log('  '+'-'.repeat(80));
for(const [nm,lam] of supers){
  const m=hbar/(lam*c);
  console.log(`  ${nm.padEnd(20)} ${(lam*1e9).toFixed(0).padStart(7)}     ${E(m).padStart(12)}     ${(m*c*c/eV).toFixed(3).padStart(10)}`);
}
console.log('\n  ★ ニオブの中では、光子は 5.06 eV の質量を持ちます。\n');
console.log('  ── これはヒッグス機構の、そのままの縮小版です。');
console.log('    超伝導の凝縮体が光子に質量を与える／ヒッグス場が W・Z に質量を与える。\n');
const MW=80.377e9;   // eV
const lamW=hbar/(MW*eV/(c*c)*c);
console.log(`   W ボソン    質量 ${(MW/1e9).toFixed(3)} GeV    到達距離 ħ/(M_W c) = ${E(lamW)} m`);
console.log(`   ニオブの光子 質量 5.06 eV        到達距離            = ${E(39e-9)} m\n`);
const rMass=MW/5.06, rLen=39e-9/lamW;
console.log(`   質量の比 = ${E(rMass)}        長さの比 = ${E(rLen)}        比の比 = ${(rMass/rLen).toFixed(6)}`);
console.log('\n  ★ ぴったり一致します ── 同じ式だから当然ですが、');
console.log('    ★ 「弱い力が弱い」と「超伝導体が磁場を締め出す」が、');
console.log('      まったく同じ一本の式で結ばれていることの確認になっています。');

console.log('\n##################################################################');
console.log('# 7. 真空の光子質量 ── 上限はどこまで');
console.log('##################################################################\n');
console.log('  では真空の光子には、質量がないと言い切れるのか。上限があります：\n');
const mg=1e-18;    // eV（代表的な上限）
const wg=mg*eV/hbar;
console.log(`      m_γ < ${E(mg)} eV     （惑星磁場などからの代表的な上限）\n`);
console.log('  第 6 回の言葉に翻訳すると、これは「真空の遮断周波数」の上限です：\n');
console.log(`      ω_c = m_γc²/ħ < ${E(wg)} rad/s`);
console.log(`      f_c < ${E(wg/(2*Math.PI))} Hz          周期 > ${E(2*Math.PI/wg)} s = ${(2*Math.PI/wg/60).toFixed(0)} 分`);
console.log(`      到達距離 λ = c/ω_c > ${E(c/wg)} m = ${(c/wg/1.496e11).toFixed(2)} AU\n`);
console.log('  ★ つまり ── 真空は「周期 1 時間 より長いところで遮断があるかもしれない」');
console.log('    導波管かもしれない、という状態です。それ以上は分からない。\n');
console.log('  ★ そして第 3・4 回の話とつながります ──');
console.log('    低周波側は、いつでも「まだ見えていない」。');
console.log('    質量ゼロという主張は、「遮断周波数が観測窓より下」という主張でした。');

console.log('\n##################################################################');
console.log('# 8. 「質量」という言葉が指しているもの');
console.log('##################################################################\n');
const kinds=[
  ['静止質量',        'ω₀ = mc²/ħ',        '分散関係の切片',     '第 6 回'],
  ['有効質量 m*',     'ħ/(d²ω/dk²)',       '★ 分散関係の曲率',   '本回'],
  ['サイクロトロン質量','ħk/(dω/dk)',        '傾きと位置の比',     '本回 5 節'],
  ['光子の質量（媒質）','ħ/(λ c)',           '減衰長の逆数',       '本回 6 節'],
  ['縦質量・横質量',   '方向で違う曲率',      '異方性のある結晶',   '──'],
];
console.log('   呼び名                 定義                  正体                出たところ');
console.log('  '+'-'.repeat(84));
for(const [a,b,cc,d] of kinds)
  console.log(`  ${a.padEnd(20)} ${b.padEnd(20)} ${cc.padEnd(20)} ${d}`);
console.log('\n  ★ 全部 同じ曲線 ω(k) の特徴量です。');
console.log('    ── 「質量」は一つの量ではなく、分散関係の読み方の名前でした。');

console.log('\n##################################################################');
console.log('# 9. まとめ');
console.log('##################################################################\n');
const sm=[
  ['0次=質量、1次=速度、2次=質量','◎ 厳密','テイラー展開そのもの'],
  ['1/m* = d²E/dk²/ħ²',        '◎ 定義','有効質量の定義'],
  ['強束縛 m* = ħ²/(2ta²)',     '◎ 数値','解析式と数値微分が 10⁻⁵ 一致'],
  ['バンド頂上で m* < 0',       '◎ 数値','正孔の正体'],
  ['α_graphene = 2.19',        '◎ 計算','★ 机の上の強結合 QED'],
  ['ニオブの光子 5.06 eV',      '◎ 計算','マイスナー＝ヒッグスの縮小版'],
  ['真空の遮断周期 > 1 時間',    '○ 上限','光子質量の上限の翻訳'],
];
console.log('  主張                          判定      根拠');
console.log('  '+'-'.repeat(80));
for(const [a,b,cc] of sm) console.log(`  ${a.padEnd(28)} ${b.padEnd(9)} ${cc}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     質量の逆数は、分散関係の曲率だった。');
console.log('     0 次の質量は「切片」、2 次の質量は「曲がり具合」。');
console.log('     ── 同じ言葉が、同じ曲線の違う特徴を指していた。');
