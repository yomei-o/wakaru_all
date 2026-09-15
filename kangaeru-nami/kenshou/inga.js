// 因果律 ── フィルタは未来を知らない。その一言が、実部と虚部を縛る
'use strict';
const E=x=>x.toExponential(3);

console.log('##################################################################');
console.log('# 1. 「すべてはフィルタ」と言うなら、制約があるはず');
console.log('##################################################################\n');
console.log('  第 1 回で、微分も積分もフィルタだと分かりました。');
console.log('  では、物理が許すフィルタには条件があるのか ── あります。ただ一つ：\n');
console.log('      ★ 応答関数 h(t) は、t < 0 でゼロでなければならない。\n');
console.log('  入力より先に出力が出ることはない。それだけです。');
console.log('  ところがこの一言が、周波数領域に恐ろしく強い制約を課します。');

console.log('\n##################################################################');
console.log('# 2. まず、禁止されるものを見る ── 理想フィルタは作れない');
console.log('##################################################################\n');
console.log('  「遮断周波数までは全部 通し、その上は全部 止める」── 理想的な低域通過。');
console.log('  この伝達関数を逆フーリエ変換すると：\n');
console.log('      h(t) = 2 f_c · sinc(2 f_c t)\n');
console.log('  sinc は t < 0 でもゼロではありません。つまり ── 未来を使っている。\n');
const fc=1000;
console.log('  実際に値を見ます（f_c = 1000 Hz）：\n');
console.log('    t [ms]      h(t)/h(0)      判定');
console.log('  '+'-'.repeat(50));
for(const tms of [-2,-1,-0.5,-0.25,0,0.25,0.5,1,2]){
  const t=tms/1000;
  const x=2*Math.PI*fc*t;
  const s=(t===0)?1:Math.sin(x)/x;
  console.log(`  ${tms.toFixed(2).padStart(7)}    ${s.toFixed(6).padStart(10)}     ${tms<0?(Math.abs(s)>1e-9?'★ 未来を使っている':''):''}`);
}
console.log('\n  ★ 理想フィルタは、物理的に実現できません。');
console.log('    「遷移帯域が要る」のは技術の限界ではなく、因果律の帰結でした。');

console.log('\n##################################################################');
console.log('# 3. 一般則 ── クラマース＝クローニッヒ関係');
console.log('##################################################################\n');
console.log('  h(t) が片側（t<0 でゼロ）なら、その変換 χ(ω) = χ′ + iχ″ は');
console.log('  上半平面で解析的になります。コーシーの積分定理から：\n');
console.log('      χ′(ω) = (1/π) P∫ χ″(ω′)/(ω′−ω) dω′');
console.log('      χ″(ω) = −(1/π) P∫ χ′(ω′)/(ω′−ω) dω′\n');
console.log('  ★ 実部と虚部は、独立ではない。片方から他方が決まる。\n');
console.log('  実際に確かめます。ローレンツ振動子（減衰調和振動子）で：\n');
console.log('      χ(ω) = 1 / (ω₀² − ω² − iγω)\n');
const w0=1.0, gam=0.2;
function chi(w){
  const re=w0*w0-w*w, im=-gam*w;
  const d=re*re+im*im;
  return {re: re/d, im: -im/d};   // 1/(re+i·im) の実部・虚部
}
// K-K 積分（主値）。特異点を引き算して正則化する：
//   P∫g(ω')/(ω'²−ω²)dω' = ∫[g(ω')−g(ω)]/(ω'²−ω²)dω' + g(ω)·(1/2ω)ln|(W−ω)/(W+ω)|
function kkRe(w, N=2000000, W=4000){
  const dw=W/N;
  const g=wp=>wp*chi(wp).im;
  const gw=g(w);
  let s=0;
  for(let i=1;i<=N;i++){
    const wp=(i-0.5)*dw;                    // 中点則。格子点が ω に当たらない
    const den=wp*wp-w*w;
    if(Math.abs(den)<1e-14) continue;
    s += (g(wp)-gw)/den*dw;                 // 被積分関数は ω′=ω で正則
  }
  s += gw*(1/(2*w))*Math.log(Math.abs((W-w)/(W+w)));   // 引いた分を解析的に戻す
  return 2/Math.PI*s;
}
console.log('    ω        χ′（直接）      χ′（K-K 積分）     相対差');
console.log('  '+'-'.repeat(64));
for(const w of [0.3,0.6,0.9,1.2,1.5,2.0]){
  const direct=chi(w).re;
  const viaKK=kkRe(w);
  console.log(`  ${w.toFixed(2)}    ${direct.toFixed(6).padStart(10)}    ${viaKK.toFixed(6).padStart(10)}     ${E(Math.abs((viaKK-direct)/direct))}`);
}
console.log('\n  ★ 一致します。虚部（吸収）だけから、実部（分散）が再現できました。');

console.log('\n##################################################################');
console.log('# 4. 物理的な意味 ── 吸収なしに分散なし');
console.log('##################################################################\n');
const conseq=[
  ['吸収がゼロなら',        'χ″ ≡ 0 → χ′ = 定数',   '★ 屈折率が振動数によらない ＝ 分散なし'],
  ['どこかで吸収があれば',   'χ′ が振動数依存',        '必ず分散する'],
  ['逆も真',              '分散があれば吸収がある',   '透明で分散する媒質は存在しない'],
];
console.log('  条件                  帰結                        意味');
console.log('  '+'-'.repeat(84));
for(const [a,b,c] of conseq) console.log(`  ${a.padEnd(20)} ${b.padEnd(26)} ${c}`);
console.log('\n  ★ ガラスが色を分けるのは、紫外で吸収があるからです。');
console.log('    可視光では透明なのに、遠くの吸収線が分散を作っている ──');
console.log('    これは「わかる屈折」の「屈折と吸収は同じ関数」と同じ話です。\n');
console.log('  そして第 5 回で使った Δα_had も、この関係で得られていました：');
console.log('    e⁺e⁻ → ハドロン の断面積（虚部）を測り、分散関係で実部に変換する。');
console.log('    ★ 計算できない量を、測定と因果律で埋めている。');

console.log('\n##################################################################');
console.log('# 5. 総和則 ── 積分すると、電子の数が出る');
console.log('##################################################################\n');
console.log('  K-K からもう一歩 進めると、総和則（f-sum rule）が出ます：\n');
console.log('      ∫₀^∞ ω ε″(ω) dω = (π/2) ω_p²,     ω_p² = n e²/(ε₀ m)\n');
console.log('  ★ 吸収スペクトルを全周波数で積分すると、電子の数密度が出る。\n');
// 数値確認：ローレンツ振動子の総和則
const eps0=1.0;
function epsIm(w){ return gam*w/((w0*w0-w*w)*(w0*w0-w*w)+gam*gam*w*w); }
let sum=0;
const Wmax=2000, Nn=4000000;
for(let i=1;i<=Nn;i++){ const w=i*Wmax/Nn; sum+=w*epsIm(w)*(Wmax/Nn); }
console.log(`  ローレンツ振動子（ω₀=${w0}, γ=${gam}、振動子強度 1）で数値積分：`);
console.log(`    ∫ω ε″dω = ${sum.toFixed(6)}`);
console.log(`    予言値 π/2 = ${(Math.PI/2).toFixed(6)}`);
console.log(`    相対差 ${E(Math.abs(sum-Math.PI/2)/(Math.PI/2))}\n`);
console.log('');
console.log('  本当に ω₀ にも γ にもよらないか、振って確かめます：');
console.log('');
console.log('    ω₀      γ       ∫ω ε″dω      π/2 からの相対差');
console.log('  '+'-'.repeat(58));
for(const [a,b] of [[0.5,0.1],[1.0,0.2],[2.0,0.5],[5.0,1.0],[1.0,0.02]]){
  function im(w){ return b*w/((a*a-w*w)*(a*a-w*w)+b*b*w*w); }
  let t=0; const M=2000000, WW=20000;
  for(let i=1;i<=M;i++){ const w=(i-0.5)*WW/M; t+=w*im(w)*(WW/M); }
  console.log(`  ${a.toFixed(1).padStart(5)}   ${b.toFixed(2).padStart(5)}   ${t.toFixed(6).padStart(10)}     ${E(Math.abs(t-Math.PI/2)/(Math.PI/2))}`);
}
console.log('');
console.log('  ★ 位置も幅も変えたのに、全部 π/2。');
console.log('  ★ 振動子の位置 ω₀ にも幅 γ にもよらず、π/2 になります。');
console.log('    ── 総和則は「何個あるか」だけを数えていて、');
console.log('      どんな形で吸収するかには依らない。強力な検算になります。');

console.log('\n##################################################################');
console.log('# 6. 微分・積分は、因果的か');
console.log('##################################################################\n');
console.log('  第 1〜2 回で使った操作を、因果律で採点します：\n');
const ops=[
  ['微分 d/dt',        '○ ぎりぎり因果的', 'h(t)=δ′(t)。t=0 に集中しており、t<0 には無い'],
  ['積分 ∫₀ᵗ',         '○ 因果的',        'h(t)=ステップ関数。過去だけを見る'],
  ['両側積分 ∫₋∞^∞',    '× 非因果的',      '未来も見る'],
  ['分数階（前進）',      '○ 因果的',       '記憶核 (t−τ)^(−α) は過去のみ'],
  ['理想低域通過',       '× 非因果的',      '★ sinc が両側に広がる（第 2 節）'],
  ['ヒルベルト変換',      '× 非因果的',      '位相を 90° 回すだけの操作も、実は未来が要る'],
];
console.log('  操作                 判定             理由');
console.log('  '+'-'.repeat(84));
for(const [a,b,c] of ops) console.log(`  ${a.padEnd(20)} ${b.padEnd(16)} ${c}`);
console.log('\n  ★ 面白いのは最後の二つです。');
console.log('    「振幅は変えず位相だけ 90° 回す」という、一見 無害な操作が非因果的。');
console.log('    ── 因果律は「何を通すか」ではなく「実部と虚部の関係」を縛っています。');

console.log('\n##################################################################');
console.log('# 7. ペイリー＝ウィーナーの条件 ── どこまで急に切れるか');
console.log('##################################################################\n');
console.log('  因果的な応答が持てる「切れ味」には上限があります：\n');
console.log('      ∫ |ln|χ(ω)|| / (1+ω²) dω < ∞\n');
console.log('  ★ これを満たさない ＝ 減衰が速すぎる ＝ 因果的に実現できない。\n');
const decay=[
  ['1/ω（一次のフィルタ）',  '○', 'ln は対数的にしか増えない'],
  ['exp(−ω/ω_c)',         '○', 'ln が線形。∫ln/(1+ω²) は収束する'],
  ['exp(−ω²/ω_c²)（ガウス）','×', '★ ln が ω² で増える。発散 ── 実現できない'],
  ['ある周波数から厳密に 0',  '×', 'ln が −∞。理想フィルタ（第 2 節）'],
];
console.log('  減衰の形                   可否   理由');
console.log('  '+'-'.repeat(72));
for(const [a,b,c] of decay) console.log(`  ${a.padEnd(26)} ${b}     ${c}`);
console.log('\n  ★ ガウシアンフィルタは、厳密には因果的でない。');
console.log('    画像処理で使えるのは、時間方向でなく空間方向だからです。');
console.log('    （空間には「未来」が無いので、因果律の制約がかからない）');

console.log('\n##################################################################');
console.log('# 8. まとめ ── 一行が、全部を縛っていた');
console.log('##################################################################\n');
const summary=[
  ['因果律',            'h(t) = 0 (t<0)',       '入力より先に出力は出ない'],
  ['⇒ 解析性',          'χ(ω) が上半平面で正則',  'コーシーの定理が使える'],
  ['⇒ K-K 関係',        'χ′ と χ″ が互いを決める', '★ 実測で確認（第 3 節）'],
  ['⇒ 吸収なしに分散なし', '透明で分散する媒質は無い', 'ガラスの色分けは紫外の吸収のせい'],
  ['⇒ 総和則',          '∫ωε″dω = πω_p²/2',     '形によらず個数だけを数える'],
  ['⇒ 理想フィルタは禁止', '遷移帯域が必ず要る',     '技術ではなく原理の限界'],
];
console.log('  段階                  内容                        意味');
console.log('  '+'-'.repeat(84));
for(const [a,b,c] of summary) console.log(`  ${a.padEnd(20)} ${b.padEnd(24)} ${c}`);
console.log('\n  ★ 「すべてはフィルタ」という見方に、物理が課す条件はただ一つ ──');
console.log('    未来を使うな。');
console.log('    そしてその一言から、分散も、総和則も、フィルタ設計の限界も出ます。');
