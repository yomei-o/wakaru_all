// 非線形 ── この連載がずっと置いてきた仮定を、正面から壊す
'use strict';
const E=x=>x.toExponential(3);

// ===== FFT =====
function fft(re,im,inv){
  const n=re.length;
  for(let i=1,j=0;i<n;i++){let b=n>>1;for(;j&b;b>>=1)j^=b;j^=b;
    if(i<j){[re[i],re[j]]=[re[j],re[i]];[im[i],im[j]]=[im[j],im[i]];}}
  for(let len=2;len<=n;len<<=1){
    const ang=2*Math.PI/len*(inv?1:-1), wr=Math.cos(ang), wi=Math.sin(ang);
    for(let i=0;i<n;i+=len){let cr=1,ci=0;
      for(let j=0;j<len/2;j++){
        const ur=re[i+j],ui=im[i+j];
        const vr=re[i+j+len/2]*cr-im[i+j+len/2]*ci, vi=re[i+j+len/2]*ci+im[i+j+len/2]*cr;
        re[i+j]=ur+vr;im[i+j]=ui+vi;re[i+j+len/2]=ur-vr;im[i+j+len/2]=ui-vi;
        const nc=cr*wr-ci*wi;ci=cr*wi+ci*wr;cr=nc;}}}
  if(inv)for(let i=0;i<n;i++){re[i]/=n;im[i]/=n;}
}
const N=1<<14, fs=16384, df=fs/N;   // df = 1 Hz ちょうど

console.log('##################################################################');
console.log('# 1. この連載が置いてきた仮定');
console.log('##################################################################\n');
console.log('  第 1 回から第 22 回まで、ずっと同じ言葉を使ってきました ──');
console.log('  「フィルタ」「伝達関数」「スペクトルを傾ける」。\n');
console.log('  ★ これらは全部、線形性を前提にしています：\n');
console.log('      重ね合わせ : L[a·x + b·y] = a·L[x] + b·L[y]\n');
console.log('  ★ 重ね合わせが効くから、正弦波ごとに分けて考えられた。');
console.log('    ★ 効かないなら、「周波数応答」という概念そのものが成り立ちません。\n');
const linear=[
  ['重ね合わせ',        '成り立つ',  '★ 壊れる',   '入力を分けて考えられない'],
  ['伝達関数 H(ω)',     '定義できる','★ 定義できない','応答が入力の大きさに依る'],
  ['周波数の保存',      '保たれる',  '★ 混ざる',   '入れていない周波数が出る'],
  ['フーリエ分解の意味', '完全',      '限定的',     '分けても独立に扱えない'],
];
console.log('   性質                線形では      非線形では     中身');
console.log('  '+'-'.repeat(80));
for(const [a,b,c,d] of linear) console.log(`  ${a.padEnd(18)} ${b.padEnd(12)} ${c.padEnd(12)} ${d}`);

console.log('\n##################################################################');
console.log('# 2. いちばん簡単な非線形 ── 新しい周波数が生まれる');
console.log('##################################################################\n');
console.log('  出力に二乗の項を足すだけ：\n');
console.log('      y = x + ε x²\n');
console.log('  そこに二つの正弦波を入れます（1000 Hz と 1100 Hz）：\n');
function spectrum(y){
  const re=Float64Array.from(y), im=new Float64Array(N);
  fft(re,im,false);
  const out=[];
  for(let k=0;k<N/2;k++){
    const a=2*Math.hypot(re[k],im[k])/N;
    if(a>1e-6) out.push([k*df, a]);
  }
  out.sort((p,q)=>q[1]-p[1]);
  return out;
}
{
  const x=new Float64Array(N);
  for(let i=0;i<N;i++){
    const t=i/fs;
    x[i]=Math.sin(2*Math.PI*1000*t)+Math.sin(2*Math.PI*1100*t);
  }
  const eps=0.1;
  const y=new Float64Array(N);
  for(let i=0;i<N;i++) y[i]=x[i]+eps*x[i]*x[i];
  const sp=spectrum(y);
  console.log('   周波数 [Hz]     振幅        正体');
  console.log('  '+'-'.repeat(60));
  const names={0:'★ 直流（整流された分）',100:'★ 差 f₂−f₁',1000:'入力 f₁',1100:'入力 f₂',
               2000:'★ 二倍音 2f₁',2100:'★ 和 f₁+f₂',2200:'★ 二倍音 2f₂'};
  for(const [f,a] of sp.slice(0,8)){
    console.log(`  ${f.toFixed(0).padStart(10)}   ${a.toFixed(6)}    ${names[Math.round(f)]||''}`);
  }
}
console.log('\n  ★ 入れていない周波数が、七つも出てきました。');
console.log('    ★ 線形フィルタには絶対にできないことです ──');
console.log('      線形なら「入れた周波数を強めるか弱めるか」しかできない。\n');
console.log('  差の 100 Hz に注目してください。★ 入力より低い周波数が生まれています。');
console.log('    ── これが混変調（相互変調）で、オーディオでは最も嫌われる歪みです。');
console.log('      高調波は倍音なので音楽的ですが、差音は不協和になるから。');

console.log('\n##################################################################');
console.log('# 3. 歪みを数値で測る ── どのくらい小さければよいか');
console.log('##################################################################\n');
console.log('  純音 1000 Hz を入れて、y = x + a₂x² + a₃x³ の高調波歪み率を測ります：\n');
function thd(a2,a3){
  const x=new Float64Array(N), y=new Float64Array(N);
  for(let i=0;i<N;i++){
    const t=i/fs;
    x[i]=Math.sin(2*Math.PI*1000*t);
    y[i]=x[i]+a2*x[i]*x[i]+a3*x[i]*x[i]*x[i];
  }
  const re=Float64Array.from(y), im=new Float64Array(N);
  fft(re,im,false);
  const amp=k=>2*Math.hypot(re[k],im[k])/N;
  const f0=amp(1000);
  let h=0;
  for(let n=2;n<=8;n++) h+=Math.pow(amp(1000*n),2);
  return Math.sqrt(h)/f0*100;
}
console.log('   a₂        a₃        THD [%]      たとえ');
console.log('  '+'-'.repeat(70));
const cases=[
  [0,      0,       '完全に線形'],
  [1e-4,   0,       '高級オーディオ'],
  [1e-3,   0,       'ふつうのアンプ'],
  [0,      1e-3,    '奇数次だけ（対称な歪み）'],
  [0.01,   0,       '安物のスピーカー'],
  [0.1,    0,       '★ 2 節で使った値'],
  [0.3,    0.3,     '★ ギターの歪みエフェクタ'],
];
for(const [a2,a3,note] of cases){
  console.log(`  ${a2.toExponential(0).padStart(8)}  ${a3.toExponential(0).padStart(8)}   ${thd(a2,a3).toFixed(4).padStart(9)}    ${note}`);
}
console.log('\n  ★ 人間が歪みに気づくのは、おおよそ 1 % 以上 からと言われます。');
console.log('    ★ つまり日常の「線形な世界」は、0.1 % 程度の非線形を無視した近似。');
console.log('      ── 線形性は自然の性質ではなく、小ささの結果でした。');

console.log('\n##################################################################');
console.log('# 4. 伝達関数が定義できなくなる ── ダフィング振動子');
console.log('##################################################################\n');
console.log('  ばねを少しだけ硬くします（振幅が大きいほど硬い）：\n');
console.log('      ẍ + 2γẋ + ω₀²x + βx³ = F cos(ωt)\n');
console.log('  ★ β=0 なら線形 ── 共鳴曲線は入力の大きさによらず同じ形。');
console.log('    β≠0 だと、共鳴の山が傾きます。\n');
function duffing(w,beta,F,x0,v0,nCyc){
  const gam=0.05, w0=1;
  let x=x0,v=v0,t=0;
  const dt=2*Math.PI/w/400;
  const nStep=Math.round(nCyc*400);
  const f=(t,x,v)=>[v, -2*gam*v - w0*w0*x - beta*x*x*x + F*Math.cos(w*t)];
  for(let i=0;i<nStep;i++){
    const k1=f(t,x,v);
    const k2=f(t+dt/2, x+dt/2*k1[0], v+dt/2*k1[1]);
    const k3=f(t+dt/2, x+dt/2*k2[0], v+dt/2*k2[1]);
    const k4=f(t+dt,   x+dt*k3[0],   v+dt*k3[1]);
    x+=dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]);
    v+=dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]);
    t+=dt;
  }
  // 最後の 20 周期で振幅を測る
  let amax=0;
  for(let i=0;i<8000;i++){
    const k1=f(t,x,v);
    const k2=f(t+dt/2, x+dt/2*k1[0], v+dt/2*k1[1]);
    const k3=f(t+dt/2, x+dt/2*k2[0], v+dt/2*k2[1]);
    const k4=f(t+dt,   x+dt*k3[0],   v+dt*k3[1]);
    x+=dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]);
    v+=dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]);
    t+=dt;
    if(Math.abs(x)>amax) amax=Math.abs(x);
  }
  return {amp:amax, x, v};
}
function sweep(beta,F,up){
  const ws=[];
  for(let i=0;i<=70;i++) ws.push(0.6+i*0.02);
  if(!up) ws.reverse();
  let x=0,v=0;
  const out=[];
  for(const w of ws){
    const r=duffing(w,beta,F,x,v,60);
    x=r.x; v=r.v;
    out.push([w,r.amp]);
  }
  return out;
}
console.log('  周波数をゆっくり上げたときと、下げたときの応答を比べます。');
console.log('  （線形なら同じ。非線形だと違う経路を通ります）\n');
{
  const beta=0.3, F=0.3;
  const up=sweep(beta,F,true);
  const dn=sweep(beta,F,false);
  const dnMap=new Map(dn.map(([w,a])=>[w.toFixed(2),a]));
  console.log('   ω        上げたとき   下げたとき    差');
  console.log('  '+'-'.repeat(56));
  let maxGap=0, gapW=0;
  for(const [w,a] of up){
    const b=dnMap.get(w.toFixed(2));
    const gap=Math.abs(a-b);
    if(gap>maxGap){maxGap=gap; gapW=w;}
    if(Math.abs(w-Math.round(w*10)/10)<1e-9 || gap>0.1)
      console.log(`  ${w.toFixed(2)}     ${a.toFixed(5).padStart(9)}    ${b.toFixed(5).padStart(9)}    ${gap.toFixed(5)}`);
  }
  console.log(`\n  ★ 最大の差は ω = ${gapW.toFixed(2)} で ${maxGap.toFixed(4)}`);
}
console.log('\n  ★ 同じ周波数・同じ入力なのに、答えが二つあります。');
console.log('    どちらになるかは「そこへ至った経路」で決まる ── ヒステリシス。\n');
console.log('  ★ これが決定的です ──\n');
console.log('      伝達関数 H(ω) は「周波数を入れたら応答が決まる」という関数。');
console.log('      ★ 答えが二つある以上、関数として定義できません。\n');
console.log('  ── 第 1 回から使ってきた「フィルタ」という言葉は、ここで使えなくなります。');

console.log('\n##################################################################');
console.log('# 5. 何が壊れ、何が生き残るか ── ここが本題');
console.log('##################################################################\n');
const survive=[
  ['重ね合わせ',              '第 1 回',  '★ 壊れる',  '非線形の定義そのもの'],
  ['伝達関数・フィルタ描像',   '第 1 回',  '★ 壊れる',  '4 節のヒステリシス'],
  ['スペクトルを傾ける描像',   '第 1 回',  '△ 限定的',  '周波数が混ざるため'],
  ['★ 因果律',               '第 8 回',  '◎ 生き残る','出力が入力より先に出ないのは変わらない'],
  ['★ 帯域幅定理',           '第 9 回',  '◎ 生き残る','フーリエ変換自体の性質だから'],
  ['★ 時間の矢（階数の偶奇）', '第 10 回', '◎ 生き残る','t→−t の性質は非線形でも同じ'],
  ['★ 次元解析',             '第 14 回', '◎ 生き残る','むしろ非線形でこそ主役（乱流）'],
  ['★ 情報は虚軸に住む',      '第 21 回', '◎ 生き残る','第二法則は非線形でも成り立つ'],
];
console.log('   道具                     出た回      非線形では   理由');
console.log('  '+'-'.repeat(92));
for(const [a,b,c,d] of survive)
  console.log(`  ${a.padEnd(24)} ${b.padEnd(10)} ${c.padEnd(12)} ${d}`);
console.log('\n  ★★ ここが本回いちばんの発見です ──\n');
console.log('      壊れるのは第 I 部の「フィルタ」という描像だけ。');
console.log('      第 IV 部で見つけた三つの制約（因果律・帯域幅・時間の矢）は、');
console.log('      ★ 全部 生き残ります。\n');
console.log('  理由も明確です ──');
console.log('    「フィルタ」は線形性の言葉ですが、');
console.log('    ★ 因果律・帯域幅・時間の矢は、線形性ではなく');
console.log('      ★「時間が一方向にしか進まない」ことから来ているから。');

console.log('\n##################################################################');
console.log('# 6. 非線形の強さを測る ── 全部 同じ形の無次元量');
console.log('##################################################################\n');
console.log('  どの分野でも、非線形の強さは「非線形項 / 線形項」で測ります：\n');
const nl=[
  ['流体',       'レイノルズ数 Re',   '(u·∇)u / ν∇²u',    'UL/ν'],
  ['非線形光学', '非線形位相 φ_NL',   'n₂I / n₀',          'γPL'],
  ['重力',       'コンパクト性',      'GM/(rc²)',          '第 15 回'],
  ['音響',       '非線形パラメータ',  'B/A · (u/c)',       '音の大きさに比例'],
  ['場の理論',   '結合定数',          '相互作用項 / 自由項', 'α, α_s'],
];
console.log('   分野          量                   中身                     記号');
console.log('  '+'-'.repeat(84));
for(const [a,b,c,d] of nl) console.log(`  ${a.padEnd(12)} ${b.padEnd(20)} ${c.padEnd(24)} ${d}`);
console.log('\n  ★ 全部「非線形項を線形項で割った無次元量」です。');
console.log('    ── 第 7 回の「意味があるのは無次元量だけ」が、ここでも効いています。\n');
console.log('  レイノルズ数を数値で並べます（Re = UL/ν）：\n');
const re=[
  ['精子の遊泳',        1e-5,   5e-5,  1e-6],
  ['毛細血管の血流',    1e-3,   8e-6,  3e-6],
  ['水道の蛇口',        1,      0.01,  1e-6],
  ['泳ぐ人',            1,      2,     1e-6],
  ['自動車（100 km/h）',27.8,   4,     1.5e-5],
  ['旅客機',            250,    60,    1.5e-5],
  ['★ 地球の大気',      10,     1e7,   1.5e-5],
];
console.log('   場面                     U [m/s]    L [m]      ν [m²/s]      Re          流れ');
console.log('  '+'-'.repeat(92));
for(const [nm,U,L,nu] of re){
  const R=U*L/nu;
  let st;
  if(R<1) st='★ 完全に線形（粘性が支配）';
  else if(R<2300) st='層流';
  else st='★ 乱流（非線形が支配）';
  console.log(`  ${nm.padEnd(22)} ${E(U).padStart(9)}  ${E(L).padStart(9)}  ${E(nu).padStart(9)}   ${E(R).padStart(10)}   ${st}`);
}
console.log('\n  ★ 精子の世界は Re ~ 10⁻⁴ ── 完全に線形です。');
console.log('    ★ だから「慣性で滑る」ことができず、鞭毛を止めた瞬間に止まる。');
console.log('      ── ★ 線形な世界に住むと、時間反転対称な泳ぎ方では前に進めません');
console.log('        （ホタテ貝定理）。第 10 回の時間の矢が、生物の形を決めています。');

console.log('\n##################################################################');
console.log('# 7. 非線形が作るもの ── ソリトン');
console.log('##################################################################\n');
console.log('  非線形は壊すだけではありません。★ 分散と釣り合うと、形が保たれます。\n');
console.log('      分散：波は広がろうとする（第 16 回の群速度分散）');
console.log('      非線形：強いところほど位相が遅れる（自己位相変調）');
console.log('      ★ この二つが釣り合うと、崩れない波 ── ソリトンができる\n');
console.log('  光ファイバでの釣り合いの条件（基本ソリトン）：\n');
console.log('      N² = γP₀T₀²/|β₂| = 1\n');
const gamma=1.3e-3, beta2=-20e-27;   // /(W·m), s²/m
console.log('   パルス幅 T₀ [ps]   必要なピーク電力 P₀ [mW]    分散長 L_D [km]');
console.log('  '+'-'.repeat(76));
for(const T0ps of [1,5,10,20,50]){
  const T0=T0ps*1e-12;
  const P0=Math.abs(beta2)/(gamma*T0*T0);
  const LD=T0*T0/Math.abs(beta2);
  console.log(`  ${T0ps.toFixed(0).padStart(14)}      ${(P0*1e3).toFixed(3).padStart(14)}          ${(LD/1e3).toFixed(2)}`);
}
console.log('\n  ★ 10 ps のパルスなら 15 mW ── 実用的な値です。');
console.log('    ★ 実際、ソリトン伝送は長距離光通信で検討され、一部で使われました。\n');
console.log('  ★ 波の言葉でまとめると ──\n');
console.log('      線形な分散だけなら、パルスは必ず広がる（第 16 回）。');
console.log('      非線形だけなら、波形は歪んで壊れる（2 節）。');
console.log('      ★ 二つが釣り合うと、どちらも起きない ── これがソリトン。');

console.log('\n##################################################################');
console.log('# 8. 摂動論はいつまで効くか');
console.log('##################################################################\n');
console.log('  非線形を「小さな補正」として扱えるのは、展開パラメータが 1 より小さいとき：\n');
const pert=[
  ['QED（電子の g−2）',    1/137.036,     '◎ 5 ループまで計算済み'],
  ['QCD（高エネルギー）',   0.118,         '○ 3〜4 ループ'],
  ['QCD（低エネルギー）',   1.0,           '× 摂動論が使えない → 格子計算'],
  ['★ グラフェン（裸）',    2.19,          '× 第 17 回。机の上の強結合'],
  ['重力（地表）',          7e-10,         '◎ 線形近似で 10 桁'],
  ['重力（中性子星表面）',  0.345,         '△ 非線形が効く'],
  ['重力（地平面）',        0.5,           '× 枠組みごと使えない'],
];
console.log('   系                        展開パラメータ    摂動論');
console.log('  '+'-'.repeat(76));
for(const [a,b,c] of pert) console.log(`  ${a.padEnd(24)} ${E(b).padStart(12)}    ${c}`);
console.log('\n  ★ 第 15 回で「地球上では 10 桁 の精度で線形」と書きました。');
console.log('    ★ だから「波の言葉」がこれほどよく効いた ── それは幸運であって、');
console.log('      ★ 自然の性質ではありませんでした。');

console.log('\n##################################################################');
console.log('# 9. まとめ');
console.log('##################################################################\n');
const sm=[
  ['新しい周波数が生まれる',  '◎ 数値',  '★ 二つ入れて七つ出た'],
  ['線形性は近似だった',      '◎ 整理',  '日常は 0.1 % の非線形を無視'],
  ['伝達関数が定義できない',  '◎ 数値',  '★ ダフィングのヒステリシス'],
  ['フィルタ描像は壊れる',    '◎ 厳密',  '第 I 部の言葉が使えなくなる'],
  ['★ 三つの制約は生き残る',  '◎ 整理',  '★ 因果律・帯域幅・時間の矢'],
  ['非線形の強さ ＝ 無次元量','◎ 整理',  'Re、n₂I/n₀、GM/rc²'],
  ['精子の世界は Re ~ 10⁻⁴', '◎ 計算',  '完全に線形。ホタテ貝定理'],
  ['ソリトン ＝ 釣り合い',    '◎ 計算',  '20 ps なら 38 mW'],
];
console.log('  主張                      判定      根拠');
console.log('  '+'-'.repeat(76));
for(const [a,b,c] of sm) console.log(`  ${a.padEnd(24)} ${b.padEnd(9)} ${c}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     非線形になると「フィルタ」という言葉が使えなくなる。');
console.log('     でも因果律・帯域幅・時間の矢は生き残る。');
console.log('     ── 壊れるのは線形性の言葉で、残るのは時間の一方向性から来たものだった。');
