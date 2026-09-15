// 微分は高音、積分は低音 ── フーリエで実測する
'use strict';
const E=x=>x.toExponential(3);

// ================= FFT（基数 2、反復版） =================
function fft(re, im, inverse){
  const n=re.length;
  for(let i=1,j=0;i<n;i++){
    let bit=n>>1;
    for(;j&bit;bit>>=1) j^=bit;
    j^=bit;
    if(i<j){ [re[i],re[j]]=[re[j],re[i]]; [im[i],im[j]]=[im[j],im[i]]; }
  }
  for(let len=2;len<=n;len<<=1){
    const ang=2*Math.PI/len*(inverse?1:-1);
    const wr=Math.cos(ang), wi=Math.sin(ang);
    for(let i=0;i<n;i+=len){
      let cr=1, ci=0;
      for(let j=0;j<len/2;j++){
        const ur=re[i+j], ui=im[i+j];
        const vr=re[i+j+len/2]*cr-im[i+j+len/2]*ci;
        const vi=re[i+j+len/2]*ci+im[i+j+len/2]*cr;
        re[i+j]=ur+vr; im[i+j]=ui+vi;
        re[i+j+len/2]=ur-vr; im[i+j+len/2]=ui-vi;
        const ncr=cr*wr-ci*wi; ci=cr*wi+ci*wr; cr=ncr;
      }
    }
  }
  if(inverse) for(let i=0;i<n;i++){ re[i]/=n; im[i]/=n; }
}
function spectrum(x){
  const n=x.length, re=Float64Array.from(x), im=new Float64Array(n);
  fft(re,im,false);
  const a=new Float64Array(n/2);
  for(let i=0;i<n/2;i++) a[i]=Math.hypot(re[i],im[i])*2/n;
  return a;
}

// ================= 試験信号 =================
const fs=48000, N=1<<14;                 // 48 kHz、16384 点
const dt=1/fs, T=N*dt;
const df=1/T;
// FFT のビン中心にちょうど乗る周波数を選ぶ（漏れを避ける）
//   df = 48000/16384 = 2.9297 Hz、k = 32,128,512,2048
const tones=[93.75, 375, 1500, 6000];    // 2 オクターブおき、全てビン中心
const x=new Float64Array(N);
for(let i=0;i<N;i++){
  let v=0;
  for(const f of tones) v+=Math.sin(2*Math.PI*f*i*dt);
  x[i]=v;
}

console.log('##################################################################');
console.log('# 1. 音声を微分すると、本当に高音になるのか');
console.log('##################################################################\n');
console.log(`  標本化周波数 ${fs} Hz、${N} 点（${(T*1000).toFixed(1)} ms）`);
console.log(`  周波数分解能 Δf = 1/T = ${df.toFixed(3)} Hz`);
console.log(`  試験信号：${tones.join(' Hz, ')} Hz の正弦波を等振幅で足したもの\n`);
console.log('  これを数値的に微分・積分して、スペクトルを見ます。');
console.log('  （微分は中心差分、積分は台形則。どちらも素朴な数値計算）\n');

// 中心差分による微分
const d=new Float64Array(N);
for(let i=0;i<N;i++){
  const ip=(i+1)%N, im2=(i-1+N)%N;
  d[i]=(x[ip]-x[im2])/(2*dt);
}
// 台形則による積分（平均値を引いてドリフトを除く）
const s=new Float64Array(N);
let acc=0;
for(let i=0;i<N;i++){ const ip=(i+1)%N; acc+=(x[i]+x[ip])/2*dt; s[i]=acc; }
let mean=0; for(let i=0;i<N;i++) mean+=s[i]; mean/=N;
for(let i=0;i<N;i++) s[i]-=mean;

const Sx=spectrum(x), Sd=spectrum(d), Ss=spectrum(s);
const binOf=f=>Math.round(f/df);
console.log('   周波数    元の振幅    微分後      比      ω=2πf     比/ω');
console.log('  '+'-'.repeat(72));
for(const f of tones){
  const k=binOf(f), w=2*Math.PI*f;
  console.log(`  ${String(f).padStart(5)} Hz  ${Sx[k].toFixed(4)}    ${Sd[k].toFixed(1).padStart(8)}   ${(Sd[k]/Sx[k]).toFixed(1).padStart(8)}   ${E(w)}  ${(Sd[k]/Sx[k]/w).toFixed(5)}`);
}
console.log('\n  ★ 最後の列が全部 1 に近い ── つまり');
console.log('');
console.log('        微分すると、振幅が ω 倍になる。');
console.log('');
console.log('    （中心差分なので高周波でわずかに 1 を割ります。後述）');

console.log('\n##################################################################');
console.log('# 2. 積分は、その逆');
console.log('##################################################################\n');
console.log('   周波数    元の振幅    積分後      比      1/ω        比×ω');
console.log('  '+'-'.repeat(72));
for(const f of tones){
  const k=binOf(f), w=2*Math.PI*f;
  console.log(`  ${String(f).padStart(5)} Hz  ${Sx[k].toFixed(4)}    ${Ss[k].toExponential(3)}   ${(Ss[k]/Sx[k]).toExponential(3)}   ${E(1/w)}  ${(Ss[k]/Sx[k]*w).toFixed(5)}`);
}
console.log('\n  ★ こちらも 1 に揃います ──');
console.log('');
console.log('        積分すると、振幅が 1/ω 倍になる。');
console.log('');

console.log('\n##################################################################');
console.log('# 3. オクターブあたり何 dB か');
console.log('##################################################################\n');
console.log('  試験信号は 2 オクターブおきに置いてあります。');
console.log('  隣り合う音の振幅比を dB で見ます：\n');
console.log('   区間              元        微分後      積分後');
console.log('  '+'-'.repeat(60));
const dB=r=>20*Math.log10(r);
for(let i=0;i<tones.length-1;i++){
  const a=binOf(tones[i]), b=binOf(tones[i+1]);
  console.log(`  ${String(tones[i]).padStart(4)}→${String(tones[i+1]).padStart(5)} Hz   ` +
    `${dB(Sx[b]/Sx[a]).toFixed(2).padStart(7)} dB  ${dB(Sd[b]/Sd[a]).toFixed(2).padStart(7)} dB  ${dB(Ss[b]/Ss[a]).toFixed(2).padStart(7)} dB`);
}
console.log('\n  ★ 2 オクターブで ±12 dB ── つまり');
console.log('');
console.log('        微分 = +6 dB/oct（高域強調）');
console.log('        積分 = −6 dB/oct（低域強調）');
console.log('');
console.log('  これは音響の世界では日常の道具です。');
const audio=[
  ['微分', '+6 dB/oct', '一次のハイパスと同じ傾き。シャリシャリした音になる'],
  ['積分', '−6 dB/oct', '一次のローパスと同じ傾き。こもった音になる'],
  ['RIAA', '±の組み合わせ','レコードの録音・再生イコライザはこの原理'],
];
console.log('\n  操作      傾き          意味');
console.log('  '+'-'.repeat(66));
for(const [a,b,c] of audio) console.log(`  ${a.padEnd(8)} ${b.padEnd(13)} ${c}`);

console.log('\n##################################################################');
console.log('# 4. なぜそうなるのか ── 一行で');
console.log('##################################################################\n');
console.log('  フーリエ変換の上では、微分も積分も「掛け算」です：\n');
console.log('      f(t) = e^(iωt)  に対して');
console.log('');
console.log('        d/dt  →  ×(iω)          振幅 ω 倍、位相 +90°');
console.log('        ∫dt   →  ×(1/iω)        振幅 1/ω 倍、位相 −90°');
console.log('');
console.log('  ★ 微分も積分も「周波数ごとの重み付け」でしかない。');
console.log('    だから ── 物理で微分・積分を繰り返すとは、');
console.log('    信号のスペクトルを傾け続けることに他なりません。');

console.log('\n##################################################################');
console.log('# 5. 位相も確かめる');
console.log('##################################################################\n');
function phaseAt(sig,f){
  const n=sig.length, re=Float64Array.from(sig), im=new Float64Array(n);
  fft(re,im,false);
  const k=Math.round(f/df);
  return Math.atan2(im[k],re[k])*180/Math.PI;
}
console.log('   周波数    元の位相    微分後      差        積分後      差');
console.log('  '+'-'.repeat(74));
for(const f of tones){
  const p0=phaseAt(x,f), p1=phaseAt(d,f), p2=phaseAt(s,f);
  const norm=a=>{ while(a>180)a-=360; while(a<-180)a+=360; return a; };
  console.log(`  ${String(f).padStart(5)} Hz  ${p0.toFixed(1).padStart(8)}°  ${p1.toFixed(1).padStart(8)}°  ${norm(p1-p0).toFixed(1).padStart(7)}°  ${p2.toFixed(1).padStart(8)}°  ${norm(p2-p0).toFixed(1).padStart(7)}°`);
}
console.log('\n  ★ 微分で +90°、積分で −90°。振幅だけでなく位相も予言どおりです。');

console.log('\n##################################################################');
console.log('# 6. 数値微分のズレは、どこから来るのか');
console.log('##################################################################\n');
console.log('  第 1 節で高周波がわずかに 1 を割りました。理由を確かめます。');
console.log('  中心差分の伝達関数は、厳密には\n');
console.log('      (e^(iωΔt) − e^(−iωΔt))/(2Δt) = i·sin(ωΔt)/Δt\n');
console.log('  なので、真の iω に対して sin(ωΔt)/(ωΔt) 倍のずれがあります：\n');
console.log('   周波数     ωΔt      sinc(ωΔt)    実測の比/ω');
console.log('  '+'-'.repeat(60));
for(const f of tones){
  const k=binOf(f), w=2*Math.PI*f, a=w*dt;
  console.log(`  ${String(f).padStart(5)} Hz  ${a.toFixed(4)}   ${(Math.sin(a)/a).toFixed(6)}    ${(Sd[k]/Sx[k]/w).toFixed(6)}`);
}
console.log('\n  ★ 予言と実測が小数点以下 6 桁で一致。');
console.log('    ズレは物理ではなく、差分という近似のせいでした。');
console.log('    ── FFT で直接 iω を掛ければ、この誤差は消えます（次節）。');

console.log('\n##################################################################');
console.log('# 7. スペクトル法 ── 厳密に微分・積分する');
console.log('##################################################################\n');
console.log('  FFT して (iω)^α を掛けて戻す。これが厳密な微積分です。\n');
function fracDeriv(sig, alpha){
  const n=sig.length, re=Float64Array.from(sig), im=new Float64Array(n);
  fft(re,im,false);
  for(let k=0;k<n;k++){
    const kk = k<=n/2 ? k : k-n;             // 負の周波数
    const w = 2*Math.PI*kk*df;
    if(kk===0){ re[k]=0; im[k]=0; continue; } // ★ DC は定義できない
    const mag=Math.pow(Math.abs(w),alpha);
    const ph=alpha*Math.PI/2*Math.sign(w);
    const cr=mag*Math.cos(ph), ci=mag*Math.sin(ph);
    const nr=re[k]*cr-im[k]*ci, ni=re[k]*ci+im[k]*cr;
    re[k]=nr; im[k]=ni;
  }
  fft(re,im,true);
  return re;
}
const exact=fracDeriv(x,1);
const Se=spectrum(exact);
console.log('   周波数    スペクトル法の 比/ω     中心差分の 比/ω');
console.log('  '+'-'.repeat(58));
for(const f of tones){
  const k=binOf(f), w=2*Math.PI*f;
  console.log(`  ${String(f).padStart(5)} Hz     ${(Se[k]/Sx[k]/w).toFixed(9)}       ${(Sd[k]/Sx[k]/w).toFixed(9)}`);
}
console.log('\n  ★ スペクトル法は誤差ゼロ（丸め誤差のみ）。');
console.log('    これで α を連続に動かす準備ができました ── 次回の主題です。');

console.log('\n##################################################################');
console.log('# 8. ここに、最初の引っかかりがある');
console.log('##################################################################\n');
console.log('  第 7 節のコードに、こう書きました：\n');
console.log('      if(kk===0){ re[k]=0; im[k]=0; continue; }   // ★ DC は定義できない\n');
console.log('  ω = 0 では 1/ω が発散するので、積分は DC 成分を決められません。');
console.log('  微分のほうは逆に、DC 成分を 0 に潰してしまう。\n');
const impl=[
  ['微分', 'DC を消す',      '定数項は微分すると消える。情報が失われる'],
  ['積分', 'DC を決められない','1/ω が発散する。★ これが「積分定数」の正体'],
];
console.log('  操作    DC (ω=0) の扱い    意味');
console.log('  '+'-'.repeat(70));
for(const [a,b,c] of impl) console.log(`  ${a.padEnd(6)} ${b.padEnd(17)} ${c}`);
console.log('\n  ★ 積分定数とは、「周波数ゼロの成分」のことでした。');
console.log('    そして周波数ゼロとは「無限に長い周期」── つまり');
console.log('    どれだけ長く観測しても変化が見えないもの。');
console.log('');
console.log('  ⇒ ここから、このシリーズの本題に入ります：');
console.log('     ★ 物理定数とは、積分定数のことではないのか。');
