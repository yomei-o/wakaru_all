// 虚数階微分 ── 振幅を変えず、位相を log ω で回す。スケール変換の生成子だった
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

// ===== 複素数とガンマ関数（ランチョス近似） =====
const LG=[676.5203681218851,-1259.1392167224028,771.32342877765313,
-176.61502916214059,12.507343278686905,-0.13857109526572012,
9.9843695780195716e-6,1.5056327351493116e-7];
const cmul=(a,b)=>[a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]];
const cdiv=(a,b)=>{const d=b[0]*b[0]+b[1]*b[1];return [(a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d];};
const cexp=a=>{const e=Math.exp(a[0]);return [e*Math.cos(a[1]),e*Math.sin(a[1])];};
const clog=a=>[0.5*Math.log(a[0]*a[0]+a[1]*a[1]), Math.atan2(a[1],a[0])];
const cpow=(a,b)=>cexp(cmul(clog(a),b));
function cgamma(z){
  let xr=0.99999999999980993, xi=0;
  const zz=[z[0]-1,z[1]];
  for(let i=0;i<8;i++){const q=cdiv([LG[i],0],[zz[0]+i+1,zz[1]]); xr+=q[0]; xi+=q[1];}
  const t=[zz[0]+7.5, zz[1]];
  return cmul(cmul([Math.sqrt(2*Math.PI),0],cpow(t,[zz[0]+0.5,zz[1]])),cmul(cexp([-t[0],-t[1]]),[xr,xi]));
}
function simpC(f,a,b,M){
  const h=(b-a)/M; let sr=0,si=0;
  for(let k=0;k<=M;k++){
    const w=(k===0||k===M)?1:(k%2?4:2);
    const v=f(a+k*h); sr+=w*v[0]; si+=w*v[1];
  }
  return [sr*h/3, si*h/3];
}
// I(ε) = ∫₀^∞ x^(iβ) e^(ix−εx) dx。x<1 は x=e^u に置換（位相が u について線形になる）
function quadI(b,eps){
  const f1=u=>{const x=Math.exp(u); const ph=b*u+x; const e=Math.exp(u-eps*x); return [e*Math.cos(ph), e*Math.sin(ph)];};
  const A=simpC(f1,-60,0,600000);
  const X=Math.max(60/eps,50);
  const f2=x=>{const ph=b*Math.log(x)+x; const e=Math.exp(-eps*x); return [e*Math.cos(ph), e*Math.sin(ph)];};
  const B=simpC(f2,1,X,Math.ceil(X*2000));
  return [A[0]+B[0], A[1]+B[1]];
}

console.log('##################################################################');
console.log('# 1. 指数を虚数にすると、何が起きるか');
console.log('##################################################################\n');
console.log('  第 2 回で (iω)^α の α を実数で動かしました。虚数にしてみます：\n');
console.log('      (iω)^(iβ) = exp( iβ · ln(iω) )');
console.log('               = exp( iβ · [ ln ω + iπ/2 ] )');
console.log('               = exp(−βπ/2) · exp( i β ln ω )\n');
console.log('  ★ 二つに分かれました：\n');
console.log('      振幅 : exp(−βπ/2)     ← ω に依らない定数！');
console.log('      位相 : β ln ω          ← 周波数の「対数」に比例\n');
console.log('  つまり ── 虚数階微分は「全域通過フィルタ」です。');
console.log('  どの周波数も同じだけ通し、位相だけを log ω で回す。\n');
console.log('   β      振幅 exp(−βπ/2)    ω=1 での位相   ω=10 での位相   ω=100 での位相');
console.log('  '+'-'.repeat(82));
for(const b of [-1,-0.5,0,0.5,1,2]){
  const amp=Math.exp(-b*Math.PI/2);
  const p=w=>(b*Math.log(w)*180/Math.PI).toFixed(1)+'°';
  console.log(`  ${b.toFixed(1).padStart(5)}   ${E(amp).padStart(12)}      ${p(1).padStart(8)}     ${p(10).padStart(9)}     ${p(100).padStart(9)}`);
}
console.log('\n  ★ 10 倍 ごとに同じだけ位相が回る ── これがすべての鍵です。');

console.log('\n##################################################################');
console.log('# 2. 音で考える ── クリックが「チャープ」になる');
console.log('##################################################################\n');
console.log('  第 2 回では「α を上げると高音が強くなる」でした。');
console.log('  虚数階では振幅が変わらないので、音色は変わりません。');
console.log('  変わるのは ── 時間的な並び方です。\n');
console.log('  実信号に施すときの流儀を先に決めます。(iω)^(iβ) は');
console.log('  そのままでは H(−ω) = H*(ω) を満たさない（出力が複素になる）ので、');
console.log('  正の周波数で (iω)^(iβ) を定義し、負側は共役で埋めます。');
console.log('  ── ヒルベルト変換と同じ作法です。すると：\n');
console.log('      |H(ω)| = exp(−βπ/2)   （全周波数で同じ）');
console.log('      arg H(ω) = β ln ω     （正の周波数側）\n');
const N=1<<15, fs=48000, dt=1/fs, df=fs/N;
function imagOrder(sig, beta){
  const re=Float64Array.from(sig), im=new Float64Array(N);
  fft(re,im,false);
  for(let k=0;k<N;k++){
    const kk=k<=N/2?k:k-N;
    if(kk===0||Math.abs(kk)===N/2){re[k]=0;im[k]=0;continue;} // DC とナイキストは実数でないと困る
    const w=2*Math.PI*Math.abs(kk)*df;
    const sg=Math.sign(kk);
    const mag=Math.exp(-beta*Math.PI/2);
    const ph=sg*beta*Math.log(w);
    const cr=mag*Math.cos(ph), ci=mag*Math.sin(ph);
    const nr=re[k]*cr-im[k]*ci, ni=re[k]*ci+im[k]*cr;
    re[k]=nr; im[k]=ni;
  }
  fft(re,im,true);
  return re;
}
// (a) 全域通過の確認
console.log('  【確認 1】本当に全域通過か ── 白色雑音を通して実効値を比べます。\n');
let seed=12345; const rnd=()=>{seed=(seed*1103515245+12345)&0x7fffffff; return seed/0x7fffffff*2-1;};
const noise=new Float64Array(N); for(let i=0;i<N;i++)noise[i]=rnd();
let nm=0; for(let i=0;i<N;i++)nm+=noise[i]; nm/=N; for(let i=0;i<N;i++)noise[i]-=nm;
const rms=a=>{let s=0;for(let i=0;i<N;i++)s+=a[i]*a[i];return Math.sqrt(s/N);};
const r0=rms(noise);
console.log('   β      実測 出力/入力       理論 exp(−βπ/2)     相対誤差');
console.log('  '+'-'.repeat(66));
for(const b of [-1,-0.5,0.5,1,2]){
  const y=imagOrder(noise,b);
  const meas=rms(y)/r0, th=Math.exp(-b*Math.PI/2);
  console.log(`  ${b.toFixed(1).padStart(5)}   ${meas.toFixed(9).padStart(14)}   ${th.toFixed(9).padStart(14)}    ${E(Math.abs(meas/th-1))}`);
}
console.log('\n  ★ 一致しました。振幅スペクトルには指一本触れていません。');
// (b) 群遅延
console.log('\n  【確認 2】では何が変わるのか ── 群遅延を測ります。\n');
console.log('      位相 φ(ω) = β ln ω     →     群遅延 τ_g = −dφ/dω = −β/ω\n');
console.log('  ★ 遅れが 1/ω に比例する ── 低い音ほど大きくずれる。');
console.log('    ガウス窓をかけた純音（トーンバースト）を入れて、重心の移動を測ります。\n');
function burst(f0, t0, sigma){
  const x=new Float64Array(N);
  for(let i=0;i<N;i++){const t=i*dt-t0; x[i]=Math.exp(-t*t/(2*sigma*sigma))*Math.cos(2*Math.PI*f0*t);}
  return x;
}
function centroid(y){ // エネルギー重心 [s]
  let s=0,m=0; for(let i=0;i<N;i++){const w=y[i]*y[i]; s+=w; m+=w*i;} return m/s*dt;
}
const T0=N*dt/2, SG=0.010;
console.log('   f [Hz]    β     実測ずれ [ms]    理論 −β/ω [ms]    差 [μs]');
console.log('  '+'-'.repeat(68));
for(const f0 of [200,400,800,1600]){
  const x=burst(f0,T0,SG), c0=centroid(x);
  const b=3;
  const y=imagOrder(x,b), c1=centroid(y);
  const meas=(c1-c0)*1000, th=-b/(2*Math.PI*f0)*1000;
  console.log(`  ${String(f0).padStart(6)}   ${b.toFixed(1)}   ${meas.toFixed(4).padStart(12)}   ${th.toFixed(4).padStart(13)}     ${((meas-th)*1000).toFixed(2).padStart(7)}`);
}
console.log('\n  ★ 1/f に比例してずれる ── 理論どおりです。');
console.log('    周波数が 2 倍になるごとに、ずれは半分。');
console.log('    ★ だからクリック（全周波数が同時）を入れると、');
console.log('      出てくるのは双曲線チャープ ── 音程がすーっと滑る音になります。');
// (c) クリックの実効長
// (c) インパルス応答の閉じた形
console.log('\n  【確認 3】では時間の波形そのものは、どんな形なのか。\n');
console.log('  クリックを入れたときの出力 h(t) を、手で積分してみます。');
console.log('  x = ωt と置くと、t が積分の外に出ます：\n');
console.log('      h(t) = (e^(−βπ/2)/π) Re ∫₀^∞ ω^(iβ) e^(iωt) dω');
console.log('           = (e^(−βπ/2)/π) Re [ t^(−1−iβ) ∫₀^∞ x^(iβ) e^(ix) dx ]\n');
console.log('  ★ 残った積分は t に依らない、ただの複素数です。値は\n');
console.log('      ∫₀^∞ x^(iβ) e^(ix) dx = Γ(1+iβ) · e^(iπ(1+iβ)/2)\n');
console.log('  これを代入して整理すると：\n');
console.log('      ★ t·h(t) = A(β) · sin( β ln t − arg Γ(1+iβ) )');
console.log('         A(β) = e^(−βπ) · |Γ(1+iβ)| / π');
console.log('         |Γ(1+iβ)| = √( πβ / sinh(πβ) )\n');
console.log('  ── t を掛けると、ln t についてのきれいな正弦波になる。');
console.log('     ★ 時間軸を対数目盛りで見ると、周期 2π/β の振動です。\n');
console.log('  まず Γ の値を確かめます（ランチョス近似 vs 厳密式）：\n');
console.log('   β      |Γ(1+iβ)| 数値       √(πβ/sinh πβ)        arg Γ [rad]');
console.log('  '+'-'.repeat(70));
for(const b of [0.5,1,2,3,5]){
  const g=cgamma([1,b]);
  const num=Math.hypot(g[0],g[1]), th=Math.sqrt(Math.PI*b/Math.sinh(Math.PI*b));
  console.log(`  ${b.toFixed(1).padStart(4)}   ${num.toExponential(8)}    ${th.toExponential(8)}     ${Math.atan2(g[1],g[0]).toFixed(6).padStart(10)}`);
}
console.log('\n  次に、問題の積分そのものを数値で確かめます。');
console.log('  x→0 で位相 β ln x が無限に速く回るので、そこだけ x = e^u に置換して');
console.log('  積分します。収束因子 e^(−εx) を入れ、閉じた式 Γ(1+iβ)/(ε−i)^(1+iβ) と比べます：\n');
console.log('   β    ε        数値積分（実部, 虚部）              相対誤差');
console.log('  '+'-'.repeat(70));
for(const b of [1,2,3]){
  for(const eps of [0.05,0.01]){
    const num=quadI(b,eps);
    const cf=cdiv(cgamma([1,b]),cpow([eps,-1],[1,b]));
    const err=Math.hypot(num[0]-cf[0],num[1]-cf[1])/Math.hypot(cf[0],cf[1]);
    console.log(`  ${b}   ${eps.toFixed(2)}   ${num[0].toExponential(7).padStart(15)}  ${num[1].toExponential(7).padStart(15)}     ${E(err)}`);
  }
}
console.log('\n  ★ 11〜13 桁一致。閉じた形は正しいと見てよさそうです。\n');
console.log('  そこで裾の大きさ A(β) を並べます：\n');
console.log('   β      A(β) = e^(−βπ)|Γ(1+iβ)|/π      対数目盛りの周期 2π/β');
console.log('  '+'-'.repeat(70));
for(const b of [0.1,0.5,1,2,3,5]){
  const A=Math.exp(-b*Math.PI)*Math.sqrt(Math.PI*b/Math.sinh(Math.PI*b))/Math.PI;
  console.log(`  ${b.toFixed(1).padStart(4)}   ${E(A).padStart(14)}                  ${(2*Math.PI/b).toFixed(3).padStart(10)}`);
}
console.log('\n  ★ ここに落とし穴があります ──');
console.log('    β を大きくすると振動は速くなりますが、裾の振幅は e^(−βπ) で潰れる。');
console.log('    β = 3 で既に 10^−6。数値の FFT では丸め誤差に埋もれて見えません。');
console.log('    ★ 「対数周期性を実測する」のが難しいのは、まさにこれが理由です。');
console.log('      ── 第 6 節で「地震や金融の対数周期は論争中」と書くのも、');
console.log('        振幅が小さすぎて統計的に分離しにくいから。\n');
console.log('  ここで起きていることを、もう一度言い直します：\n');
console.log('    ・振幅スペクトルは一切変わっていない（全域通過）');
console.log('    ・なのに波形は 1/t の裾を引いて広がる');
console.log('    ・その裾は、時間を e^(2π/β) 倍するごとに同じ形に戻る\n');
console.log('  ★ これは純粋な分散です。吸収ゼロで、位相だけが動いている。');
console.log('    第 8 回で「吸収なしに分散なし」と書きましたが、あれは');
console.log('    因果的な応答の話でした。この全域通過フィルタは非因果的');
console.log('    （τ_g < 0 ＝ 先に出る）なので、その縛りの外にいます。');

console.log('\n##################################################################');
console.log('# 3. 何の生成子なのか ── スケール変換');
console.log('##################################################################\n');
console.log('  位相が ln ω に比例する、という性質を言い換えます。');
console.log('  周波数を λ 倍に伸ばしてみると：\n');
console.log('      φ(λω) = β ln(λω) = β ln ω + β ln λ\n');
console.log('  ★ 位相が「一定だけ」ずれる。形は変わらない。\n');
console.log('  つまり虚数階微分は、スケール変換に対して不変な操作です。');
console.log('  実数階との対比：\n');
const contrast=[
  ['実数階 α',  '(iω)^α',   'ω^α',          'απ/2（一定）',  '時間並進', 'フーリエ変換'],
  ['虚数階 iβ', '(iω)^(iβ)','定数',         'β ln ω',       '★ スケール変換', '★ メリン変換'],
];
console.log('  階数        記号          振幅        位相         対応する対称性   自然な変換');
console.log('  '+'-'.repeat(92));
for(const [a,b,c,d,e,f] of contrast)
  console.log(`  ${a.padEnd(10)} ${b.padEnd(12)} ${c.padEnd(10)} ${d.padEnd(12)} ${e.padEnd(14)} ${f}`);
console.log('\n  ★ これが今回いちばんの発見です ──\n');
console.log('      実数階微分は「時間をずらす」世界の道具');
console.log('      虚数階微分は「スケールを変える」世界の道具\n');
console.log('  フーリエ変換の核 e^(iωt) が時間並進の固有関数であるのと同じく、');
console.log('  メリン変換の核 t^(iβ) はスケール変換の固有関数です。');
console.log('  ★ 虚数階微分は、そのメリン核そのものでした。');

console.log('\n##################################################################');
console.log('# 4. 物理はどこで虚数階を使っているか ── 1/r² ポテンシャル');
console.log('##################################################################\n');
console.log('  引力の 1/r² ポテンシャルを考えます（3 次元、s 波）：\n');
console.log('      −(ħ²/2m)u″ − (λħ²/2m)u/r² = E u\n');
console.log('  r → 0 では E が効かないので、u ∝ r^s と置くと：\n');
console.log('      s(s−1) + λ = 0     →     s = 1/2 ± √(1/4 − λ)\n');
console.log('  ★ λ > 1/4 で、平方根の中が負 ── 指数が複素数になります：\n');
console.log('      s = 1/2 ± i s₀,     s₀ = √(λ − 1/4)');
console.log('      u ∝ √r · cos( s₀ ln r + δ )      ★ 対数周期振動\n');
console.log('   λ（引力の強さ）   √(1/4−λ)        s₀        振る舞い');
console.log('  '+'-'.repeat(72));
for(const lam of [0,0.1,0.2,0.25,0.5,1.0,2.0]){
  const d=0.25-lam;
  if(d>0) console.log(`  ${lam.toFixed(2).padStart(9)}      ${Math.sqrt(d).toFixed(4).padStart(8)}        ──        安定。基底状態がある`);
  else if(d===0) console.log(`  ${lam.toFixed(2).padStart(9)}      ${Math.sqrt(d).toFixed(4).padStart(8)}        ──        ★ ちょうど臨界`);
  else console.log(`  ${lam.toFixed(2).padStart(9)}      ${'虚数'.padStart(8)}     ${Math.sqrt(-d).toFixed(4).padStart(6)}    ★ 対数周期。中心へ落ちる`);
}
console.log('\n  ★ λ = 1/4 が臨界点。これを超えると「中心への落下」が起きます。');
console.log('    そして波動関数は ln r について周期的 ──');
console.log('    ★ 空間が「対数目盛りで周期的」になる ＝ 離散的スケール不変性。');

console.log('\n##################################################################');
console.log('# 5. 実際に観測されている ── エフィモフ状態');
console.log('##################################################################\n');
console.log('  三体問題で、これが本当に起きます（エフィモフ 1970）。');
console.log('  同種ボソン 3 個が共鳴的に相互作用すると、超半径 R について\n');
console.log('      有効ポテンシャル ∝ −(s₀² + 1/4)/R²,     s₀ = 1.00624\n');
console.log('  ★ ちょうど臨界を超えた 1/R² ── つまり虚数階の世界です。\n');
const s0=1.00624;
const scale=Math.exp(Math.PI/s0);
console.log(`  s₀ = ${s0}`);
console.log(`  → 束縛状態の大きさの比 = exp(π/s₀) = ${scale.toFixed(3)}`);
console.log(`  → エネルギーの比       = exp(2π/s₀) = ${(scale*scale).toFixed(1)}\n`);
console.log('  ★ 22.7 倍 ごとに、同じ形の束縛状態が無限に並ぶ ──');
console.log('    これが「エフィモフの梯子」です。\n');
console.log('   n     大きさ（第0準位を 1 として）    エネルギー比');
console.log('  '+'-'.repeat(60));
for(let n=0;n<5;n++){
  console.log(`  ${n}     ${E(Math.pow(scale,n)).padStart(12)}              ${E(Math.pow(scale,-2*n))}`);
}
console.log('\n  ★ 2006 年、超低温セシウム原子で実際に観測されました。');
console.log('    ── 対数周期性が、実験室で確認された数少ない例です。');
console.log('\n  そして位相の言葉に戻すと：');
console.log(`    大きさが 22.7 倍になるごとに、位相 s₀ ln R が π 進む。`);
console.log(`    ★ 第 1 節の「10 倍ごとに ${(s0*Math.log(10)*180/Math.PI).toFixed(0)}° 回る」と同じ勘定です。`);

console.log('\n##################################################################');
console.log('# 6. 第 5 回とつながる ── 複素次元と繰り込み群');
console.log('##################################################################\n');
console.log('  第 5 回で、結合定数は ln μ について走ると見ました：\n');
console.log('      dα/d ln μ = β(α)\n');
console.log('  ★ 「ln（スケール）についての微分」── まさに虚数階の舞台です。\n');
console.log('  ある量が O(μ) ∝ μ^(−Δ) と振る舞うとき、Δ を「次元」と呼びます。');
console.log('  Δ が複素数 Δ = Δ_R + i Δ_I になると：\n');
console.log('      μ^(−Δ) = μ^(−Δ_R) · exp(−i Δ_I ln μ)\n');
console.log('  ★ べき乗に、対数周期の振動が掛かる。');
console.log('    ── これが「離散的スケール不変性」です。\n');
const dsi=[
  ['エフィモフ状態',    '○ 実測',   '超低温原子（2006）。比 22.7'],
  ['1/r² 落下',       '○ 厳密',   '臨界 λ=1/4 を超えると必ず'],
  ['臨界現象の対数補正', '△ 場合による','離散的な格子では出ることがある'],
  ['拡散律速凝集（DLA）','△ 数値',   '対数周期の報告があるが議論がある'],
  ['地震・金融の対数周期','× 論争中',  '★ 主張されているが、統計的に確立していない'],
];
console.log('  現象                  状況        備考');
console.log('  '+'-'.repeat(76));
for(const [a,b,c] of dsi) console.log(`  ${a.padEnd(20)} ${b.padEnd(11)} ${c}`);
console.log('\n  ★ 確実なのは上の二つだけです。下の三つは主張の段階。');
console.log('    ── 対数周期性は「見つけたくなる」パターンなので、');
console.log('      統計的な扱いに注意が要る領域です。');

console.log('\n##################################################################');
console.log('# 7. 複素階数の全体像 ── 二つの独立なつまみ');
console.log('##################################################################\n');
console.log('  一般の複素階数 α + iβ をまとめます：\n');
console.log('      (iω)^(α+iβ) = ω^α e^(−βπ/2) · exp( i[ απ/2 + β ln ω ] )\n');
console.log('  ★ 実部 α と虚部 β は、まったく違う仕事をしています：\n');
const knobs=[
  ['実部 α', '振幅の傾き',   'ω^α → 6α dB/oct',  '第 1〜2 回'],
  ['実部 α', '一定の位相',   'απ/2 度',          '第 10 回（時間の矢）'],
  ['虚部 β', '振幅の定数倍', 'e^(−βπ/2)',        '全体の大きさだけ'],
  ['虚部 β', '対数周期の位相','β ln ω',           '★ 本回（スケール不変性）'],
];
console.log('  つまみ    効く先          式                  出てきた回');
console.log('  '+'-'.repeat(76));
for(const [a,b,c,d] of knobs) console.log(`  ${a.padEnd(9)} ${b.padEnd(14)} ${c.padEnd(20)} ${d}`);
console.log('\n  ★ 実部 ＝ 時間の矢の向きと強さ');
console.log('    虚部 ＝ スケールの周期性\n');
console.log('  この二つは独立です。だから「複素階数の平面」を描けます：\n');
console.log('       β（虚部）');
console.log('        ↑  対数周期・スケール不変');
console.log('        │');
console.log('   ─────┼─────→ α（実部）');
console.log('        │  保存 ↔ 散逸（時間の矢）');
console.log('        │');
console.log('\n  ★ 物理が使っているのは、この平面のごく狭い領域です：');
console.log('      α ∈ [0, 2]（第 2 回・第 10 回）、β はほぼ 0。');
console.log('      β ≠ 0 が出るのは、臨界的な 1/r² が現れる特殊な場合だけ。');

console.log('\n##################################################################');
console.log('# 8. まとめ');
console.log('##################################################################\n');
const summary=[
  ['虚数階＝全域通過',     '◎ 厳密',  '振幅 e^(−βπ/2) は ω に依らない'],
  ['位相が β ln ω',       '◎ 厳密',  '10 倍ごとに一定角度'],
  ['クリック→チャープ',    '◎ 数値',  '群遅延 −β/ω。第 2 節で実測'],
  ['スケール変換の生成子',  '◎ 対応',  '★ メリン変換の核そのもの'],
  ['1/r² の臨界超え',     '◎ 厳密',  'λ>1/4 で指数が複素数。対数周期'],
  ['エフィモフ状態',      '○ 実測',  '比 22.7。2006 年に観測'],
  ['複素次元＝離散スケール不変','○ 既知','第 5 回の繰り込み群とつながる'],
];
console.log('  主張                    判定      根拠');
console.log('  '+'-'.repeat(76));
for(const [a,b,c] of summary) console.log(`  ${a.padEnd(22)} ${b.padEnd(9)} ${c}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     実数階微分は「時間をずらす」世界の道具、');
console.log('     虚数階微分は「スケールを変える」世界の道具だった。');
console.log('     ── 音で言えば、前者は音色を変え、後者は音色を変えずに時間を伸ばす。');
