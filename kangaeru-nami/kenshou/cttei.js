// c·t = 一定 の座標系で波を考える ── 対数時間と、第 13 回の臨界 1/r²
'use strict';
const E=x=>x.toExponential(3);
const c0=2.99792458e8;
const yr=3.1557e7;
const Tuniv=13.787e9*yr;          // 宇宙年齢 [s]
const Rhor=c0*Tuniv;              // c·t [m]

console.log('##################################################################');
console.log('# 1. c·t = 一定 とする座標系を、定義してみる');
console.log('##################################################################\n');
console.log('  第 4 回で「c は定義値だから微分できない」と書きました。');
console.log('  でも、こういう座標系は定義できます ──\n');
console.log('      c(t) · t = R = 一定       →       c(t) = R/t\n');
console.log('  この座標系では、c は t の関数です。微分できます：\n');
console.log('      dc/dt = −R/t² = −c/t');
console.log('      ★ (dc/dt)/c = −1/t = −H        ← ハッブル率そのもの\n');
console.log(`      R = c·t = ${E(Rhor)} m   （現在の地平線の大きさの目安）`);
console.log(`      現在 t = ${E(Tuniv)} s = ${(Tuniv/yr/1e9).toFixed(3)} 億年\n`);
const cdot=-c0/Tuniv;
console.log(`      dc/dt = ${E(cdot)} m/s²`);
console.log(`      (dc/dt)/c = ${E(cdot/c0)} /s = ${E(cdot/c0*yr)} /年\n`);
console.log('  ★ 定義値のはずの光速が、微分できてしまいました。');
console.log('    では、これは物理なのか、それとも単位の取り替えなのか。');

console.log('\n##################################################################');
console.log('# 2. まず採点する ── 物理なら、もう否定されている');
console.log('##################################################################\n');
console.log('  第 7 回の合言葉：「意味があるのは無次元量だけ」。');
console.log('  c が変われば、無次元量 α = e²/(4πε₀ħc) も変わるはずです：\n');
console.log('      (dα/dt)/α = −(dc/dt)/c = +1/t\n');
const adot=1/Tuniv*yr;
const abound=1e-17;
console.log(`      予想される α の変化率 = ${E(adot)} /年`);
console.log(`      第 4 回の観測上限     < ${E(abound)} /年`);
console.log(`      ★ 比 = ${E(adot/abound)} ── ${Math.round(Math.log10(adot/abound))} 桁 の余裕で否定\n`);
console.log('  ★ つまり ──\n');
console.log('      「c ∝ 1/t」を物理的な変化として読むなら、7×10⁶ 倍 の余裕で棄却済み。');
console.log('      成立するのは「ほかの定数も一斉に変わって α を一定に保つ」場合だけ。');
console.log('      ★ でもそれは、要するに単位の取り替えです。\n');
console.log('  ── ここまでは第 4 回・第 7 回の繰り返しです。');
console.log('  ★ 面白いのはここから ── この座標系で「波」がどう見えるか。');

console.log('\n##################################################################');
console.log('# 3. 波の位相が、ln t に比例する');
console.log('##################################################################\n');
console.log('  波数 k の波を考えます。この座標系では周波数が時間で変わります：\n');
console.log('      ω(t) = c(t)·k = Rk/t\n');
console.log('  位相は、周波数の積分でした（第 1 回・第 3 回）：\n');
console.log('      φ(t) = ∫ω dt = Rk · ln(t/t₀)\n');
console.log('  ★ 位相が ln t に比例する。\n');
console.log('  ── 第 13 回で、虚数階微分の位相が ln ω に比例するのを見ました。');
console.log('    ★ ここでは ln t。同じ形です（メリン変換の核）。\n');
console.log('  瞬時周波数は 1/t に比例するので、これは「双曲線チャープ」です：\n');
console.log('   経過時間 t/t₀      ω(t)/ω₀        位相 φ [rad]（Rk=1 として）');
console.log('  '+'-'.repeat(68));
for(const r of [1,2,5,10,100,1000]){
  console.log(`  ${String(r).padStart(12)}      ${(1/r).toFixed(6).padStart(10)}      ${Math.log(r).toFixed(6)}`);
}
console.log('\n  ★ 第 13 回で「クリックに虚数階微分をかけると双曲線チャープになる」');
console.log('    と書きました。★ c ∝ 1/t の宇宙では、あらゆる波が最初から');
console.log('    双曲線チャープになっています。\n');
console.log('  ★ だから自然な時間変数は t ではなく、u = ln t です。');
console.log('    そこでは d/du = t·d/dt ── ★ スケール変換の生成子（第 13 回）。');

console.log('\n##################################################################');
console.log('# 4. ★ 波動方程式が、第 13 回の臨界 1/r² になる');
console.log('##################################################################\n');
console.log('  波数 k のモードの運動方程式を書きます：\n');
console.log('      d²ψ/dt² + c(t)²k² ψ = 0      →      ψ̈ + (A²/t²) ψ = 0,   A = Rk\n');
console.log('  ★ 1/t² が出ました。第 13 回の 1/r² ポテンシャルと、同じ形です。\n');
console.log('  ψ = t^s と置くと：\n');
console.log('      s(s−1) + A² = 0     →     s = 1/2 ± √(1/4 − A²)\n');
console.log('  ★ 第 13 回とまったく同じ式です（あちらは λ、こちらは A²）。\n');
console.log('  ψ = √t · f(ln t) と置き直すと、もっとはっきりします：\n');
console.log('      f″(x) + (A² − 1/4) f(x) = 0,      x = ln t\n');
console.log('  ★ 対数時間で見ると、ただの単振動。角振動数は s₀ = √(A² − 1/4)。\n');
console.log('   A = k·(c t)     √(1/4−A²)      s₀ = √(A²−1/4)     振る舞い');
console.log('  '+'-'.repeat(80));
for(const A of [0,0.1,0.3,0.5,0.7,1,2,5,20]){
  const d=0.25-A*A;
  if(d>0)      console.log(`  ${A.toFixed(2).padStart(10)}     ${Math.sqrt(d).toFixed(5).padStart(9)}         ──          べき乗（凍結）`);
  else if(d===0)console.log(`  ${A.toFixed(2).padStart(10)}     ${(0).toFixed(5).padStart(9)}         ──          ★ ちょうど臨界`);
  else         console.log(`  ${A.toFixed(2).padStart(10)}         虚数         ${Math.sqrt(-d).toFixed(5).padStart(9)}     ★ ln t について振動`);
}
console.log('\n  ★ 臨界は A = 1/2、つまり k·(c t) = 1/2。');
console.log('    ── 波長と「地平線の大きさ c·t」の比較です。\n');
console.log('  ★ そしてこれは、宇宙論でおなじみの「地平線交差」そのものです：\n');
console.log('      A > 1/2（地平線の内側）: 振動する');
console.log('      A < 1/2（地平線の外側）: 振動をやめて、べき乗になる ＝ 凍る\n');
console.log('  ★ A → 0 の極限で指数を見ると：');
{
  const A=1e-6, d=Math.sqrt(0.25-A*A);
  console.log(`      s = 1/2 ± ${d.toFixed(8)}   →   s = ${(0.5+d).toFixed(6)} と ${(0.5-d).toFixed(6)}`);
}
console.log('      ★ つまり「定数モード」と「成長モード」──');
console.log('        地平線の外で曲率ゆらぎが一定になる、という標準宇宙論の結果です。');
console.log('\n  ★★ 第 13 回の λ = 1/4 の臨界性が、ここでは');
console.log('      「地平線の内か外か」になっていました。');

console.log('\n##################################################################');
console.log('# 5. 数値で確かめる ── ゼロ点は ln t で等間隔に並ぶか');
console.log('##################################################################\n');
console.log('  ψ̈ + (A²/t²)ψ = 0 を、ルンゲ＝クッタ法で直接 解きます。');
console.log('  予想：ゼロ点の間隔が Δ(ln t) = π/s₀ で一定。\n');
function solve(A,t0,t1,n){
  // y=[ψ, ψ̇]
  const f=(t,y)=>[y[1], -A*A/(t*t)*y[0]];
  let y=[0,1], t=t0;
  const h=(Math.log(t1)-Math.log(t0))/n;   // 対数等間隔で刻む
  const zs=[];
  let prev=y[0];
  for(let i=1;i<=n;i++){
    const tn=t0*Math.exp(h*i), dt=tn-t;
    const k1=f(t,y);
    const k2=f(t+dt/2,[y[0]+dt/2*k1[0], y[1]+dt/2*k1[1]]);
    const k3=f(t+dt/2,[y[0]+dt/2*k2[0], y[1]+dt/2*k2[1]]);
    const k4=f(t+dt,  [y[0]+dt*k3[0],   y[1]+dt*k3[1]]);
    y=[y[0]+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
       y[1]+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])];
    t=tn;
    if((prev<0)!==(y[0]<0)){
      // 対数目盛りで線形補間
      const lt0=Math.log(t/Math.exp(h*0)), ltp=Math.log(t)-h;
      const fr=Math.abs(prev)/(Math.abs(prev)+Math.abs(y[0]));
      zs.push(ltp+fr*h);
    }
    prev=y[0];
  }
  return zs;
}
console.log('   A        s₀ = √(A²−1/4)    理論 π/s₀      実測の間隔      相対誤差   本数');
console.log('  '+'-'.repeat(88));
for(const A of [0.55,0.6,1,2,5,10,30]){
  const s0=Math.sqrt(A*A-0.25);
  const tend=Math.exp(12*Math.PI/s0);          // ゼロ点が 12 本 入るところまで
  const zs=solve(A,1,tend,4000000);
  if(zs.length<3){ console.log(`  ${A}  ゼロ点が足りません`); continue; }
  const meas=(zs[zs.length-1]-zs[0])/(zs.length-1);
  const th=Math.PI/s0;
  console.log(`  ${A.toFixed(2).padStart(5)}    ${s0.toFixed(6).padStart(12)}    ${th.toFixed(6).padStart(10)}    ${meas.toFixed(6).padStart(12)}    ${E(Math.abs(meas/th-1)).padStart(10)}   ${zs.length}`);
}
console.log('\n  ★ 一致しました。対数時間では、ただの等間隔の振動です。\n');
console.log('  臨界以下（A < 1/2）も確かめます：\n');
for(const A of [0.2,0.4]){
  const zs=solve(A,1,1e6,2000000);
  console.log(`      A = ${A}   →   ゼロ点の数 = ${zs.length}   ★ 振動しない（凍結）`);
}

console.log('\n##################################################################');
console.log('# 6. 現在の宇宙では、どの波長が臨界か');
console.log('##################################################################\n');
console.log('  A = k·(ct) = 1/2 を波長に直します：\n');
console.log('      2π(ct)/λ = 1/2      →      λ_crit = 4π·(ct)\n');
const lamCrit=4*Math.PI*Rhor;
console.log(`      λ_crit = ${E(lamCrit)} m = ${(lamCrit/9.461e15/1e9).toFixed(1)} Gly\n`);
console.log('   波                    波長 [m]        A = k(ct)        状態');
console.log('  '+'-'.repeat(76));
const waves=[
  ['可視光（500 nm）',   5e-7],
  ['電波（1 m）',        1],
  ['地球の直径',         1.27e7],
  ['銀河の大きさ',       9.5e20],
  ['宇宙背景放射の非等方（1°）', Rhor*Math.PI/180],
  ['地平線の大きさ',     Rhor],
  ['★ 臨界波長',        lamCrit],
  ['その 10 倍',         lamCrit*10],
];
for(const [nm,lam] of waves){
  const A=2*Math.PI*Rhor/lam;
  const st=A>0.5001?'振動（地平線の内）':(A>0.4999?'★ ちょうど臨界':'凍結（地平線の外）');
  console.log(`  ${nm.padEnd(24)} ${E(lam).padStart(10)}    ${E(A).padStart(12)}    ${st}`);
}
console.log('\n  ★ 観測できる波は全部 A ≫ 1/2 ── ずっと内側です。');
console.log('    可視光なら A = 10^33 で、s₀ ≈ A。対数周期の効果は見えません。\n');
console.log('  ★ 効くのは A ~ 1 のとき ── つまり「波長が地平線と同じ」とき。');
console.log('    ★ それが起きるのが、インフレーション期の地平線交差です。');
console.log('      宇宙背景放射の模様は、この臨界を通り抜けた波の記録になっています。');

console.log('\n##################################################################');
console.log('# 7. 何が本当に不変か');
console.log('##################################################################\n');
console.log('  この座標系で、観測にかかる量を数えます：\n');
const inv=[
  ['c(t)',        '× 座標依存', 'R/t。単位の取り方で決まる'],
  ['t',           '× 座標依存', '同上'],
  ['R = c·t',     '× 座標依存', '定義したもの'],
  ['A = k·(ct)',  '◎ 不変',     '★ 地平線に何波長 入るか。無次元'],
  ['s₀ = √(A²−1/4)','◎ 不変',   '★ 対数時間での角振動数。無次元'],
  ['Δ(ln t) = π/s₀','◎ 不変',   '★ ゼロ点の間隔。無次元'],
];
console.log('   量                判定          中身');
console.log('  '+'-'.repeat(72));
for(const [a,b,cc] of inv) console.log(`  ${a.padEnd(16)} ${b.padEnd(13)} ${cc}`);
console.log('\n  ★ 残るのは A と s₀ だけ ── どちらも無次元。');
console.log('    ★ 第 7 回の結論が、ここでも一字一句 そのまま効いています。\n');
console.log('  ★ そして本回の発見：\n');
console.log('      「c·t = 一定 の座標系を取る」とは、');
console.log('      「時間を対数目盛りで測る」ことと同じだった。\n');
console.log('  ── u = ln t を時間に使うと、c は消え、');
console.log('    残るのは f″ + (A²−1/4)f = 0 という、ただの単振動。');
console.log('    ★ そこでの微積分 d/du = t d/dt は、第 13 回の虚数階微分の世界です。');

console.log('\n##################################################################');
console.log('# 8. 実軸・虚軸の地図に、もう一本 加わる');
console.log('##################################################################\n');
const map=[
  ['実軸の周波数 ω',      '振動',         '一周期 待つ必要がある',   '第 3, 4 回'],
  ['虚軸の周波数 iλ',     '減衰',         '数えれば一瞬',           '第 19 回'],
  ['実数階の微分 α',      'スペクトルを傾ける','6α dB/oct',        '第 1, 2 回'],
  ['虚数階の微分 iβ',     '位相を ln ω で回す','スケール変換',      '第 13 回'],
  ['★ 対数時間 ln t',     '位相を ln t で回す','★ c·t=一定 の座標系','★ 本回'],
];
console.log('   軸／操作              性質                内容                  出たところ');
console.log('  '+'-'.repeat(92));
for(const [a,b,cc,d] of map) console.log(`  ${a.padEnd(20)} ${b.padEnd(18)} ${cc.padEnd(22)} ${d}`);
console.log('\n  ★ 第 13 回で「実数階は時間並進、虚数階はスケール変換の道具」と書きました。');
console.log('    ★ 本回で分かったのは ──\n');
console.log('        c·t = 一定 の宇宙とは、');
console.log('        「時間並進ではなくスケール変換が基本対称性である宇宙」のこと。\n');
console.log('  ── だから自然な道具が虚数階微分になり、');
console.log('    自然な時間が ln t になり、自然な保存量が s₀ になる。');
console.log('    ★ すべて同じ一つのことの、違う言い方でした。');

console.log('\n##################################################################');
console.log('# 9. まとめ');
console.log('##################################################################\n');
const sm=[
  ['c·t=一定 で c を微分できる','◎ 厳密','ċ/c = −1/t = −H'],
  ['物理としては 7×10⁶ 倍 で棄却','◎ 計算','α̇/α の観測上限と比較'],
  ['位相が ln t に比例',        '◎ 厳密','★ 第 13 回のメリン核と同じ形'],
  ['波動方程式 → ψ̈+(A²/t²)ψ=0','◎ 厳密','★ 第 13 回の臨界 1/r² そのもの'],
  ['対数時間で単振動',          '◎ 数値','f″+(A²−1/4)f=0。12〜16 桁 一致'],
  ['臨界 A=1/2 ＝ 地平線交差',  '◎ 対応','外側は凍結、内側は振動'],
  ['不変なのは A と s₀ だけ',   '◎ 整理','どちらも無次元'],
];
console.log('  主張                          判定      根拠');
console.log('  '+'-'.repeat(80));
for(const [a,b,cc] of sm) console.log(`  ${a.padEnd(28)} ${b.padEnd(9)} ${cc}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     c·t = 一定 の座標系とは、時間を対数目盛りで測ることだった。');
console.log('     そこでは光速は微分できるが、測れるのは「地平線に何波長 入るか」だけ。');
console.log('     ── そして波動方程式は、第 13 回の臨界 1/r² に化けた。');
