// 分数階微分 ── 微分と積分のあいだには、何があるのか
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
const N=1<<14, fs=48000, dt=1/fs, df=fs/N;
function fracOp(sig,alpha){
  const n=sig.length,re=Float64Array.from(sig),im=new Float64Array(n);
  fft(re,im,false);
  for(let k=0;k<n;k++){
    const kk=k<=n/2?k:k-n, w=2*Math.PI*kk*df;
    if(kk===0){re[k]=0;im[k]=0;continue;}
    const mag=Math.pow(Math.abs(w),alpha), ph=alpha*Math.PI/2*Math.sign(w);
    const cr=mag*Math.cos(ph), ci=mag*Math.sin(ph);
    const nr=re[k]*cr-im[k]*ci, ni=re[k]*ci+im[k]*cr;
    re[k]=nr;im[k]=ni;
  }
  fft(re,im,true);
  return re;
}
function ampAt(sig,f){
  const n=sig.length,re=Float64Array.from(sig),im=new Float64Array(n);
  fft(re,im,false);
  const k=Math.round(f/df);
  return {a:Math.hypot(re[k],im[k])*2/n, p:Math.atan2(im[k],re[k])*180/Math.PI};
}

console.log('##################################################################');
console.log('# 1. 微分と積分を、連続につなぐ');
console.log('##################################################################\n');
console.log('  第 1 回で見たとおり、フーリエ上では\n');
console.log('      微分 = ×(iω)^1,     積分 = ×(iω)^(−1)\n');
console.log('  ならば、指数を整数に限る理由はありません：\n');
console.log('      D^α  =  ×(iω)^α  =  ×|ω|^α · exp(i α π/2 · sgn ω)\n');
console.log('  ★ α は連続に動かせます。これが分数階微分です。');
console.log('    α = 1/2 なら「半分だけ微分する」── 意味を持ちます。\n');
const tones=[93.75,375,1500,6000];
const x=new Float64Array(N);
for(let i=0;i<N;i++){let v=0;for(const f of tones)v+=Math.sin(2*Math.PI*f*i*dt);x[i]=v;}
console.log('  α を動かして、実際に測ります（93.75 Hz と 375 Hz、2 オクターブ差）：\n');
console.log('    α      振幅比（375/93.75）   dB/oct    位相の進み');
console.log('  '+'-'.repeat(60));
for(const al of [-1,-0.5,0,0.25,0.5,0.75,1,1.5,2]){
  const y=fracOp(x,al);
  const a1=ampAt(y,93.75), a2=ampAt(y,375);
  const ratio=a2.a/a1.a;
  const dbOct=20*Math.log10(ratio)/2;
  const p0=ampAt(x,93.75).p;
  let dp=a1.p-p0; while(dp>180)dp-=360; while(dp<-180)dp+=360;
  console.log(`  ${al.toFixed(2).padStart(6)}   ${ratio.toFixed(4).padStart(12)}      ${dbOct.toFixed(2).padStart(6)}    ${dp.toFixed(1).padStart(7)}°`);
}
console.log('\n  ★ きれいに連続です：');
console.log('      dB/oct = 6α,     位相の進み = 90α 度');
console.log('    α = 1/2 なら +3 dB/oct、位相 +45°。');

console.log('\n##################################################################');
console.log('# 2. 半微分は実在するのか ── します。毎日 測られています');
console.log('##################################################################\n');
console.log('  「半分だけ微分する」は数学の遊びに見えますが、実験室の日常です。\n');
console.log('  ★ ワールブルグ・インピーダンス\n');
console.log('      半無限の媒質に物質が拡散するとき、境界でのインピーダンスは');
console.log('');
console.log('          Z(ω) ∝ 1/√(iω)          ★ これは「半積分」そのもの');
console.log('');
console.log('  電池・燃料電池・電気化学の測定で、必ず出てきます。');
console.log('  ナイキスト線図で 45° の直線として現れるのが、この α = −1/2 です。\n');
const frac=[
  ['ワールブルグ拡散',  -0.5,  '電気化学。半無限拡散の境界条件',       '★ 日常的に測定される'],
  ['異常拡散',        null,  '⟨x²⟩ ∝ t^α。α≠1 で分数階',          '生体内・多孔質媒体'],
  ['粘弾性（スプリングポット）', null, '応力 ∝ D^α(ひずみ)、0<α<1',   'ゴム・生体組織・アスファルト'],
  ['コール＝コール緩和',  null,  '誘電率 ε(ω) = ε∞ + Δε/(1+(iωτ)^α)', '液体・高分子の誘電測定'],
];
console.log('  現象                     階数 α    式・内容                             状況');
console.log('  '+'-'.repeat(96));
for(const [a,al,b,d] of frac)
  console.log(`  ${a.padEnd(24)} ${(al!==null?al.toFixed(1):'0〜1').padStart(6)}   ${b.padEnd(34)} ${d}`);
console.log('\n  ★ 分数階が出るのは、どれも「境界」か「乱れた媒質」です。');

console.log('\n##################################################################');
console.log('# 3. なぜ物理はふつう整数階なのか ── これは深い');
console.log('##################################################################\n');
console.log('  整数階の微分は、その瞬間の値だけで決まります（局所的）。');
console.log('  ところが分数階の微分は、こう書けます：\n');
console.log('      D^α f(t) = (1/Γ(1−α)) d/dt ∫₀ᵗ f(τ)/(t−τ)^α dτ\n');
console.log('  ★ 積分が入っています ── つまり 過去 全部を見ている。記憶があるのです。\n');
const loc=[
  ['整数階（α = 0,1,2…）', '局所',   '記憶なし。マルコフ的',  '通常の運動方程式'],
  ['分数階（α が非整数）',   '非局所', '★ 過去の重み付き和',   'べき乗の記憶核 (t−τ)^(−α)'],
];
console.log('  階数                  性質    意味                  例');
console.log('  '+'-'.repeat(76));
for(const [a,b,d,e] of loc) console.log(`  ${a.padEnd(20)} ${b.padEnd(6)} ${d.padEnd(20)} ${e}`);
console.log('\n  ⇒ 【仮説】物理法則がほぼ整数階なのは、');
console.log('     ★ 自然が局所的（記憶を持たない）だからではないか。\n');
console.log('     逆に言えば ── 分数階が現れる場所は、');
console.log('     必ず「自由度を積分で消した後」です。');
console.log('     ワールブルグなら媒質全体の拡散を境界に押し込めた結果、');
console.log('     粘弾性なら高分子の内部自由度を消した結果。\n');
console.log('  ※ これは本稿の推測です。ただし検証可能な形にはなっています ──');
console.log('     「分数階の系は、必ず隠れた自由度の粗視化で説明できるはず」。');

console.log('\n##################################################################');
console.log('# 4. 雑音のスペクトル ── 自然はどの階数を使っているか');
console.log('##################################################################\n');
console.log('  白色雑音を積分すると、スペクトルの傾きが −20 dB/decade 変わります。');
console.log('  実際に確かめます（乱数列を作って、階数を変えて測る）：\n');
// 白色雑音（再現性のため簡易 LCG）
let seed=12345;
const rnd=()=>{seed=(seed*1103515245+12345)&0x7fffffff; return seed/0x7fffffff-0.5;};
const w=new Float64Array(N);
for(let i=0;i<N;i++) w[i]=rnd();
function slope(sig){
  const n=sig.length,re=Float64Array.from(sig),im=new Float64Array(n);
  fft(re,im,false);
  // 対数ビンで平均してから両対数の傾きを最小二乗
  const pts=[];
  for(let k=8;k<n/8;k*=1.3){
    const k0=Math.floor(k), k1=Math.min(Math.floor(k*1.3),n/2-1);
    let s=0,c2=0;
    for(let j=k0;j<=k1;j++){ s+=re[j]*re[j]+im[j]*im[j]; c2++; }
    if(c2>0) pts.push([Math.log10(k0*df), Math.log10(s/c2)]);
  }
  let sx=0,sy=0,sxx=0,sxy=0;
  for(const [a,b] of pts){sx+=a;sy+=b;sxx+=a*a;sxy+=a*b;}
  const m=(pts.length*sxy-sx*sy)/(pts.length*sxx-sx*sx);
  return m;    // 出力は log10(power) / log10(f) = −β
}
console.log('    α        スペクトル指数 β        名前              備考');
console.log('  '+'-'.repeat(76));
const names={0:'白色雑音',0.5:'★ ピンク雑音（1/f）',1:'ブラウン雑音（1/f²）',1.5:'黒色雑音（1/f³）'};
for(const al of [0,-0.25,-0.5,-0.75,-1,-1.5]){
  const y = al===0 ? w : fracOp(w,al);
  const b=-slope(y);
  const key=(-al);
  console.log(`  ${al.toFixed(2).padStart(6)}   β = ${b.toFixed(3).padStart(6)}          ${(names[key]||'').padEnd(20)} ${key===0.5?'★ 半積分':''}`);
}
console.log('\n  ★ 積分の階数 α と、スペクトル指数 β の関係は  β = −2α。');
console.log('    整数階の積分は β を 2 ずつ動かすので、');
console.log('    ★ β = 1（1/f 雑音）には、整数階では到達できません。');

console.log('\n##################################################################');
console.log('# 5. 【仮説】1/f 雑音は、自然の半積分ではないか');
console.log('##################################################################\n');
console.log('  1/f 雑音（ピンク雑音）は、あらゆる場所に現れます：\n');
const pink=[
  ['半導体素子の雑音',   '電流の揺らぎ'],
  ['水晶発振器の位相',   '時計の精度を制限する'],
  ['心拍の間隔',        '健康な心臓ほど 1/f に近い'],
  ['音楽の音量変化',     'バッハもビートルズも 1/f'],
  ['河川の流量',        'ハースト指数'],
  ['交通量・株価',       '経済にも現れる'],
];
console.log('  現れる場所');
console.log('  '+'-'.repeat(50));
for(const [a,b] of pink) console.log(`  ${a.padEnd(20)} ${b}`);
console.log('\n  ★ そして 1/f 雑音の起源は、いまだに統一的な説明がありません。');
console.log('    白色雑音（β=0）とブラウン雑音（β=2）は素直に説明できるのに、');
console.log('    ちょうど真ん中の β=1 だけが謎として残っている。\n');
console.log('  ⇒ 【仮説】β=1 が特別なのは、それが「半積分」だからではないか。\n');
console.log('     現在の標準的な説明は「緩和時間の広い分布の重ね合わせ」です。');
console.log('     時定数 τ が 1/τ の密度で分布していると、確かに 1/f が出ます。');
console.log('     ── しかしそれは「なぜ 1/τ 分布なのか」を問い直しただけ。\n');
console.log('  検算：時定数分布から 1/f が出ることを確かめます。\n');
console.log('  ローレンツ型 S(f) = Σ_i A/(1+(f/f_i)²)、f_i を対数一様に配置：\n');
console.log('   周波数 [Hz]     重ね合わせた S(f)     f·S(f)（一定なら 1/f）');
console.log('  '+'-'.repeat(66));
function pinkSum(f){
  let s=0;
  for(let e=-3;e<=3;e+=0.05){ const fi=Math.pow(10,e); s+=1/(1+Math.pow(f/fi,2))/fi; }
  return s;
}
for(const f of [0.01,0.1,1,10,100]){
  const S=pinkSum(f);
  console.log(`  ${E(f).padStart(10)}     ${E(S).padStart(12)}      ${E(f*S)}`);
}
console.log('\n  ★ f·S(f) がほぼ一定 ── 確かに 1/f になります。');
console.log('    つまり「時定数が対数一様に分布していれば 1/f」は正しい。');
console.log('    残る問いは ── なぜ自然はそんな分布を好むのか。\n');
console.log('  ※ ここから先は未解決です。本稿の立場は「半積分という見方を');
console.log('    加えると、少なくとも問いの形が変わる」という程度のものです。');

console.log('\n##################################################################');
console.log('# 6. 【仮説】微分階数を、物理量の「もう一つの次元」と見る');
console.log('##################################################################\n');
console.log('  力学の量を、位置からの微分階数で並べてみます：\n');
const ladder=[
  [-2, '位置の二重積分', '(あまり使われない)'],
  [-1, '位置の積分',     'absement（実際に名前がある）'],
  [ 0, '位置',          'x'],
  [ 1, '速度',          'v = dx/dt'],
  [ 2, '加速度',        'a ── ★ ニュートンの法則はここ'],
  [ 3, '躍度（ジャーク）','乗り心地の指標。実用される'],
  [ 4, 'スナップ',       'ほぼ使われない'],
];
console.log('   階数 α   名前                 備考');
console.log('  '+'-'.repeat(60));
for(const [a,b,d] of ladder) console.log(`  ${String(a).padStart(5)}    ${b.padEnd(18)} ${d}`);
console.log('\n  ★ 物理が実際に使うのは α = 0, 1, 2 にほぼ限られます。');
console.log('    なぜ 2 で止まるのか ── これには答えがあります：\n');
console.log('    ① 3 階以上だと、初期条件が 3 つ要る（位置・速度・加速度）。');
console.log('       しかし実験では 2 つしか指定できない。');
console.log('    ② 高階の運動方程式は、オストログラツキー不安定性を持つ。');
console.log('       ★ エネルギーが下に非有界になり、系が壊れる。\n');
console.log('  ⇒ つまり「なぜ F = ma なのか（F = m·躍度 ではないのか）」の答えは、');
console.log('     ★ 3 階以上は不安定で存在できないから、でした。');
console.log('     微分階数のスペクトルには、上限があるのです。\n');
console.log('  ※ オストログラツキーの定理は厳密な結果です（1850 年）。');
console.log('    ただし「だから自然は 2 階まで」という推論は本稿の整理であり、');
console.log('    高階理論を退ける議論には他の形もあります。');

console.log('\n##################################################################');
console.log('# 7. まとめ');
console.log('##################################################################\n');
const sum=[
  ['α は連続に動かせる',    '◎ 実測',   'dB/oct = 6α、位相 = 90α 度'],
  ['半微分は実在する',      '◎ 実測',   'ワールブルグ・インピーダンス（α=−1/2）'],
  ['整数階＝記憶なし',      '○ 厳密',   '分数階には必ず記憶核が入る'],
  ['1/f は半積分',         '△ 仮説',   'β=−2α は厳密。起源は未解決'],
  ['α ≤ 2 の理由',        '○ 定理',   'オストログラツキー不安定性'],
];
console.log('  主張                  判定       根拠');
console.log('  '+'-'.repeat(72));
for(const [a,b,d] of sum) console.log(`  ${a.padEnd(20)} ${b.padEnd(10)} ${d}`);
console.log('\n  ★ 微分階数 α を連続変数として扱うと、');
console.log('    物理の「使っている帯域」が見えてきます ──');
console.log('    下は α = −1/2（拡散の境界）、上は α = 2（ニュートン）。');
console.log('    その外は、記憶か不安定性のどちらかに阻まれている。');
