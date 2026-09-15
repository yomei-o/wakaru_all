// 情報の微積分 ── ビットレートを積分すると情報量。そして情報は虚軸に住んでいる
'use strict';
const E=x=>x.toExponential(3);
const c=2.99792458e8;
const h=6.62607015e-34;
const hbar=1.054571817e-34;
const kB=1.380649e-23;
const eV=1.602176634e-19;
const lP=1.616255e-35;
const ln2=Math.LN2;
const yr=3.1557e7;
const Tuniv=13.787e9*yr;
const Rhor=c*Tuniv;

console.log('##################################################################');
console.log('# 1. 情報にも、階数の梯子がある');
console.log('##################################################################\n');
console.log('  ビットレート [bit/s] を積分すると、情報量 [bit] になります。');
console.log('  ── 速さを積分すると距離になるのと、まったく同じ形です。\n');
console.log('  ★ 第 1 回の梯子に、情報を載せてみます：\n');
const ladder=[
  ['階数 0','情報量 I','bit',     '★ 定数に見える量（第 3 回）'],
  ['階数 1','ビットレート dI/dt','bit/s','通信速度、エントロピー生成率'],
  ['階数 2','d²I/dt²','bit/s²',   '情報生成の加速'],
  ['階数 −1','∫I dt','bit·s',     '★ あまり使われない（後で出てきます）'],
];
console.log('   階数      量                  単位       中身');
console.log('  '+'-'.repeat(76));
for(const [a,b,cc,d] of ladder) console.log(`  ${a.padEnd(8)} ${b.padEnd(18)} ${cc.padEnd(10)} ${d}`);
console.log('\n  ★ そして第 3 回の「積分定数」も、そのまま効きます ──');
console.log('    情報量の積分定数 ＝ 初期情報量。');
console.log('    ★ 「宇宙は最初に何ビット 持っていたか」は、');
console.log('      ビットレートをいくら積分しても決まりません。');

console.log('\n##################################################################');
console.log('# 2. シャノンの公式は「帯域幅 × 時間」だった');
console.log('##################################################################\n');
console.log('  情報理論の基本式：\n');
console.log('      C = B · log₂(1 + S/N)        [bit/s]\n');
console.log('  ★ ビットレートは帯域幅 B に比例します。だから積分すると：\n');
console.log('      I = C·T = B·T · log₂(1 + S/N)        [bit]\n');
console.log('  ★ 情報量 ＝ （帯域幅 × 時間） × （1 サンプルあたりのビット数）\n');
console.log('  ── 第 9 回の帯域幅定理 ΔtΔω ≥ 1/2 が、そのまま出てきます。');
console.log('    ★ ナイキストの標本化定理では、帯域 B・時間 T の信号の自由度は 2BT。');
console.log('      ★ 「1 ビット送るには、時間 × 帯域 が要る」── これが本質でした。\n');
console.log('   通信路               帯域 B        S/N [dB]    容量 C          実際の値');
console.log('  '+'-'.repeat(88));
const links=[
  ['電話回線（音声帯域）', 3100,   30, 'ダイヤルアップ 56 kbps の壁'],
  ['4G LTE（20 MHz）',   2e7,    20, '150 Mbps 級'],
  ['Wi-Fi（80 MHz）',    8e7,    35, '実測 数百 Mbps'],
  ['5G（100 MHz）',      1e8,    20, '1 Gbps 級'],
  ['光ファイバ C+L 帯',   1e13,   20, '実用 10〜100 Tbps'],
];
for(const [nm,B,snrdb,note] of links){
  const snr=Math.pow(10,snrdb/10);
  const C=B*Math.log2(1+snr);
  console.log(`  ${nm.padEnd(20)} ${E(B).padStart(10)} Hz    ${String(snrdb).padStart(4)}     ${E(C).padStart(10)} bit/s   ${note}`);
}
console.log('\n  ★ 電話回線の 30.9 kbps ── これがダイヤルアップの理論限界でした。');
console.log('    56k モデムが 56k で止まったのは、この式が理由です。');
console.log('    ★ 帯域を増やすしかない。だから光ファイバは 10 桁 速い。');

console.log('\n##################################################################');
console.log('# 3. 情報とエネルギーの為替レート ── ランダウアー');
console.log('##################################################################\n');
console.log('  1 ビット 消すのに要るエネルギーには、下限があります：\n');
console.log('      E ≥ k_B T ln2\n');
console.log('  ★ 第 7 回で ħ・c・k_B を「為替レート」と呼びました。');
console.log('    ここでは k_B が、情報とエネルギーの為替レートです。\n');
console.log('   温度                        1 ビットの値段 [J]      [eV]');
console.log('  '+'-'.repeat(72));
const temps=[
  ['宇宙背景放射 2.725 K',  2.725],
  ['液体窒素 77 K',         77],
  ['室温 300 K',            300],
  ['太陽表面 5772 K',       5772],
  ['太陽中心 1.5×10⁷ K',    1.5e7],
];
for(const [nm,T] of temps){
  const e=kB*T*ln2;
  console.log(`  ${nm.padEnd(26)} ${E(e).padStart(12)}      ${E(e/eV)}`);
}
console.log('\n  ★ 室温では 1 ビット = 2.87×10⁻²¹ J = 0.0179 eV。\n');
console.log('  実際の計算機は、どれだけ余分に使っているか：\n');
const CV=0.1e-15, V=0.8;
const swE=0.5*CV*V*V;
const land=kB*300*ln2;
console.log(`      トランジスタ 1 回 のスイッチング ≈ ½CV² = ${E(swE)} J`);
console.log(`      （C = 0.1 fF、V = 0.8 V の目安）`);
console.log(`      ランダウアー限界（300 K）      = ${E(land)} J`);
console.log(`      ★ 比 = ${E(swE/land)} 倍\n`);
console.log('  ★ 現代の半導体は、まだ 1 万倍 ほど余裕があります。');
console.log('    ── 2012 年に、実験でランダウアー限界そのものが確認されました。');
console.log('    ★ 判定：スイッチングエネルギーは代表的な目安で、世代や設計で変わります。');

console.log('\n##################################################################');
console.log('# 4. ビットレートの上限 ── ブレーメルマンとマルゴラス＝レヴィティン');
console.log('##################################################################\n');
console.log('  第 9 回の帯域幅定理を、情報に適用します。');
console.log('  エネルギー E の系が変化できる速さには上限があります：\n');
console.log('      演算速度 ν ≤ 2E/(πħ)        （マルゴラス＝レヴィティン）');
console.log('      ビットレート ≤ mc²/h        （ブレーメルマン）\n');
console.log(`      ブレーメルマン定数 c²/h = ${E(c*c/h)} bit/(s·kg)\n`);
console.log('   系                     質量／エネルギー      演算速度の上限 [/s]');
console.log('  '+'-'.repeat(76));
const sys=[
  ['電子 1 個',       9.109e-31],
  ['陽子 1 個',       1.673e-27],
  ['1 ng',           1e-12],
  ['1 g',            1e-3],
  ['★ 1 kg（究極のノート PC）', 1],
  ['地球',           5.972e24],
];
for(const [nm,m] of sys){
  const Ee=m*c*c;
  console.log(`  ${nm.padEnd(22)} ${E(m).padStart(12)} kg     ${E(2*Ee/(Math.PI*hbar))}`);
}
console.log('\n  ★ 1 kg の物質は、毎秒 5.4×10⁵⁰ 回 まで状態を変えられます。');
console.log('    現代の CPU は 10¹⁰ 回/秒 ── ★ 40 桁 の余裕があります。\n');
console.log('  ★ ここでも第 9 回がそのまま効いています ──');
console.log('    「速く変わるには、広い帯域が要る。広い帯域には、高いエネルギーが要る」。');

console.log('\n##################################################################');
console.log('# 5. 情報量の上限 ── ベケンシュタインとホログラフィー');
console.log('##################################################################\n');
console.log('  持てる情報量にも上限があります：\n');
console.log('      I ≤ 2πER/(ħc ln2)        （ベケンシュタイン限界）\n');
const bek=(m,R)=>2*Math.PI*(m*c*c)*R/(hbar*c*ln2);
console.log('   対象                 質量 [kg]      半径 [m]      情報量の上限 [bit]');
console.log('  '+'-'.repeat(80));
const objs=[
  ['1 ビットの磁性体',  1e-18,   1e-8],
  ['USB メモリ（10 g）',0.01,    0.02],
  ['人間',             70,      0.5],
  ['地球',             5.972e24,6.371e6],
  ['太陽',             1.989e30,6.957e8],
];
for(const [nm,m,R] of objs){
  console.log(`  ${nm.padEnd(20)} ${E(m).padStart(10)}    ${E(R).padStart(10)}     ${E(bek(m,R))}`);
}
console.log('\n  ★ 人間 1 人 で 9×10⁴⁴ ビット ── 実際に使っているのは何桁 下でしょうか。\n');
console.log('  そして宇宙全体は、第 7 回で計算したホログラフィック限界です：\n');
console.log('      I = A/(4 l_P² ln2),      A = 4π(ct)²\n');
const Ihol=Math.PI*Rhor*Rhor/(lP*lP*ln2);
console.log(`      I = ${E(Ihol)} bit     （第 7 回の 3.3×10¹²² と同じ桁）\n`);

console.log('##################################################################');
console.log('# 6. ★ 宇宙のビットレートを、微分してみる');
console.log('##################################################################\n');
console.log('  ホログラフィック限界は面積に比例し、面積は (ct)² です。つまり：\n');
console.log('      I(t) = π c²t² / (l_P² ln2)        ★ 時間の二乗に比例\n');
console.log('  ★ ならば微分できます ──\n');
const dI=2*Ihol/Tuniv;
const d2I=2*Math.PI*c*c/(lP*lP*ln2);
console.log(`      dI/dt  = 2I/t = ${E(dI)} bit/s        ← 宇宙のビットレート`);
console.log(`      d²I/dt² = 2πc²/(l_P² ln2) = ${E(d2I)} bit/s²   ★ 一定！\n`);
console.log('  ★ 「宇宙の情報加速度は一定」── 面白い言い方になりました。');
console.log('    ── 第 1 回で「等加速度運動は x ∝ t²」と書いたのと、同じ形です。\n');
console.log('   時刻                    ct [m]          情報量 I [bit]     ビットレート [bit/s]');
console.log('  '+'-'.repeat(88));
for(const [nm,t] of [['プランク時間',5.391e-44],['1 秒',1],['元素合成 3 分',180],['晴れ上がり 38 万年',3.8e5*yr],['現在',Tuniv]]){
  const R=c*t, I=Math.PI*R*R/(lP*lP*ln2);
  console.log(`  ${nm.padEnd(22)} ${E(R).padStart(10)}     ${E(I).padStart(12)}      ${E(2*I/t)}`);
}
console.log('\n  ★ プランク時間には 4.5 ビット しかありませんでした（π/ln2）。');
console.log('    いま 3×10¹²² ビット ── ★ 122 桁 増えています。\n');
console.log('  ★ そして第 20 回とつながります ──\n');
console.log('      I ∝ (c t)²  なので、  c·t = 一定 の座標系では I が一定。\n');
console.log('  ★★ つまり「c·t = 一定 の座標系」とは、');
console.log('    ★ 「宇宙の情報量を一定に保つ座標系」でもありました。');
console.log('    ── 第 20 回で「時間を対数目盛りで測ること」と分かりましたが、');
console.log('      情報の言葉では「情報量を目盛りにすること」だった。');

console.log('\n##################################################################');
console.log('# 7. ★ 情報は虚軸に住んでいる');
console.log('##################################################################\n');
console.log('  第 19 回で、実軸（振動）と虚軸（減衰）を分けました。');
console.log('  ★ 情報量・エントロピーは、どちらでしょうか。\n');
console.log('      エントロピーは振動しない。単調に増えるだけ。\n');
console.log('  ★ つまり虚軸です。── これが熱力学第二法則の、波としての言い方でした。\n');
const axis=[
  ['振動する量',   '実軸 ω',  'エネルギー、位相、振幅', '可逆。時間反転で戻る'],
  ['単調に増える量','虚軸 iλ', '★ エントロピー、情報量', '★ 不可逆。時間の矢'],
  ['単調に減る量',  '虚軸 iλ', '放射性核種の数、自由エネルギー','同上'],
];
console.log('   種類            軸        例                        性質');
console.log('  '+'-'.repeat(84));
for(const [a,b,cc,d] of axis) console.log(`  ${a.padEnd(14)} ${b.padEnd(9)} ${cc.padEnd(24)} ${d}`);
console.log('\n  ★ そして第 10 回の「時間の矢は階数の偶奇に住む」と、');
console.log('    第 19 回の「崩壊定数は虚数の周波数」と、ここで合流します：\n');
console.log('      奇数階の微分 → 時間反転で符号が変わる → 不可逆');
console.log('      虚軸の周波数 → 単調に増減する         → 不可逆');
console.log('      情報量の増加 → 熱力学第二法則         → 不可逆\n');
console.log('  ★ 三つとも同じことを言っています。');
console.log('    ★ 「時間の矢」とは、複素周波数平面の虚軸のことでした。');

console.log('\n##################################################################');
console.log('# 8. 位相空間のセルを数える ── 1 ビットの大きさ');
console.log('##################################################################\n');
console.log('  第 9 回のガボール限界 ΔtΔω ≥ 1/2 は、');
console.log('  情報の言葉では「1 モードの大きさ」でした：\n');
console.log('      位相空間のセル : Δx Δp ≥ ħ/2');
console.log('      時間 × 帯域    : Δt Δω ≥ 1/2\n');
console.log('  ★ どちらも「これ以上 細かく区別できない単位」を決めています。\n');
console.log('  帯域 B・時間 T の信号に入るモードの数は 2BT（ナイキスト）。');
console.log('  1 モードあたり log₂(1+S/N) ビット。掛けるとシャノンの式に戻ります：\n');
console.log('      I = 2BT × ½log₂(1+S/N) = BT log₂(1+S/N)     ✓\n');
console.log('   信号                  帯域 [Hz]   時間 [s]    モード数 2BT     情報量 [bit]');
console.log('  '+'-'.repeat(88));
for(const [nm,B,T,snrdb] of [['電話 1 分',3100,60,30],['CD 1 曲（ステレオ）',2e4*2,240,96],['4K 動画 1 秒',1e7,1,40]]){
  const snr=Math.pow(10,snrdb/10);
  const modes=2*B*T;
  const I=modes*0.5*Math.log2(1+snr);
  console.log(`  ${nm.padEnd(22)} ${E(B).padStart(9)}   ${E(T).padStart(8)}    ${E(modes).padStart(10)}     ${E(I)}`);
}
console.log('\n  ★ 「情報量 ＝ モードの数 × 1 モードあたりのビット数」。');
console.log('    ★ モードの数を決めているのは、帯域幅定理 ── つまり第 9 回でした。');

console.log('\n##################################################################');
console.log('# 9. まとめ');
console.log('##################################################################\n');
const sm=[
  ['情報量 ＝ ビットレートの積分','◎ 定義','★ 階数 0 と 1 の関係'],
  ['シャノン ＝ 帯域幅 × 時間',  '◎ 厳密','★ 第 9 回がそのまま効く'],
  ['電話回線 30.9 kbps',        '◎ 計算','56k モデムの壁の正体'],
  ['ランダウアー 0.0179 eV',    '◎ 計算','300 K。実測で確認済み'],
  ['半導体はまだ 1 万倍 上',     '○ 概算','½CV² の目安から'],
  ['1 kg で 5.4×10⁵⁰ 回/秒',   '◎ 計算','マルゴラス＝レヴィティン'],
  ['人間は 9×10⁴⁴ ビットまで',  '◎ 計算','ベケンシュタイン限界'],
  ['宇宙の情報加速度は一定',     '◎ 計算','★ d²I/dt² = 3.1×10⁸⁷ bit/s²'],
  ['c·t=一定 ＝ 情報量一定',    '◎ 整理','★ 第 20 回とつながる'],
  ['情報は虚軸に住む',          '◎ 整理','★ 第二法則 ＝ 時間の矢'],
];
console.log('  主張                          判定      根拠');
console.log('  '+'-'.repeat(80));
for(const [a,b,cc] of sm) console.log(`  ${a.padEnd(28)} ${b.padEnd(9)} ${cc}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     情報量はビットレートの積分で、ビットレートは帯域幅に比例する。');
console.log('     だから情報の限界は、全部 帯域幅定理の言い換えだった。');
console.log('     ── そして情報は虚軸に住んでいる。だから戻らない。');
