// 測ることを波として見る ── 観測とは、どの基底に射影するかの選択だった
'use strict';
const E=x=>x.toExponential(3);
const hbar=1.054571817e-34;
const kB=1.380649e-23;
const h=6.62607015e-34;
const c=2.99792458e8;
const u=1.66053906660e-27;

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

console.log('##################################################################');
console.log('# 1. 「測る」とは、どの基底に射影するか');
console.log('##################################################################\n');
console.log('  第 1 回からずっと、波を二つの見方で書いてきました ──\n');
console.log('      時間の並び x(t)      と      周波数の並び X(ω)\n');
console.log('  ★ この二つは同じ情報の別表示です。どちらで「測る」かを選べる。\n');
const bases=[
  ['デルタ関数 δ(t−t₀)', '時刻',       '完全',  'なし',  'オシロスコープ'],
  ['正弦波 e^(iωt)',     '周波数',     'なし',  '完全',  'スペクトラムアナライザ'],
  ['窓つき正弦波',        '時刻と周波数','有限',  '有限',  '★ 短時間フーリエ変換'],
  ['ウェーブレット',      '時刻と対数周波数','ω に比例','ω に比例','★ 定 Q 分析'],
];
console.log('   基底                  何が見える      時間分解能  周波数分解能  道具');
console.log('  '+'-'.repeat(88));
for(const [a,b,cc,d,e] of bases)
  console.log(`  ${a.padEnd(20)} ${b.padEnd(14)} ${cc.padEnd(10)} ${d.padEnd(10)} ${e}`);
console.log('\n  ★ 「観測する」とは、この表のどの行を選ぶかという操作でした。');
console.log('    そして第 9 回の帯域幅定理が、選べる範囲を決めています。');

console.log('\n##################################################################');
console.log('# 2. 窓を変えると、分解能がどう動くか');
console.log('##################################################################\n');
console.log('  ガウス窓の幅 σ を変えて、時間分解能と周波数分解能を実測します。');
console.log('  （第 9 回と同じ定義：強度を重みとする標準偏差）\n');
const N=1<<14, fs=8000, dt=1/fs;
function widths(sigma){
  // ガウス窓 exp(-t²/2σ²) の Δt と Δω を数値で測る
  const re=new Float64Array(N), im=new Float64Array(N);
  for(let i=0;i<N;i++){
    const t=(i-N/2)*dt;
    re[i]=Math.exp(-t*t/(2*sigma*sigma));
  }
  let s=0,m1=0;
  for(let i=0;i<N;i++){const w=re[i]*re[i], t=(i-N/2)*dt; s+=w; m1+=w*t;}
  m1/=s;
  let m2=0;
  for(let i=0;i<N;i++){const w=re[i]*re[i], t=(i-N/2)*dt; m2+=w*(t-m1)*(t-m1);}
  const Dt=Math.sqrt(m2/s);
  fft(re,im,false);
  let s2=0,q2=0;
  for(let k=0;k<N;k++){
    const kk=k<=N/2?k:k-N;
    const w=re[k]*re[k]+im[k]*im[k];
    const om=2*Math.PI*kk*fs/N;
    s2+=w; q2+=w*om*om;
  }
  const Dw=Math.sqrt(q2/s2);
  return {Dt,Dw};
}
console.log('   窓の幅 σ [ms]    Δt [ms]     Δω [rad/s]    Δt·Δω      Δf [Hz]');
console.log('  '+'-'.repeat(76));
for(const sms of [0.5,1,2,5,10,20]){
  const r=widths(sms*1e-3);
  console.log(`  ${sms.toFixed(1).padStart(12)}   ${(r.Dt*1e3).toFixed(4).padStart(9)}   ${r.Dw.toFixed(2).padStart(11)}   ${(r.Dt*r.Dw).toFixed(6)}   ${(r.Dw/(2*Math.PI)).toFixed(2)}`);
}
console.log('\n  ★ 積はいつでも 0.5 ── 第 9 回のガボール限界にぴたりと乗っています。');
console.log('    ★ 「窓を広げれば周波数が細かく見え、時間がぼやける」が数値で見えます。');
console.log('      ── 観測者が選べるのは「どこに配るか」だけで、総量は動かせない。');

console.log('\n##################################################################');
console.log('# 3. ★ ウェーブレットは、対数周波数軸のフーリエ変換だった');
console.log('##################################################################\n');
console.log('  短時間フーリエ変換は、どの周波数でも同じ窓を使います。');
console.log('  ウェーブレット（定 Q 分析）は、周波数に比例して窓を縮めます：\n');
console.log('      短時間フーリエ : Δω = 一定        → 線形な周波数軸で等間隔');
console.log('      ウェーブレット : Δω/ω = 一定      → ★ 対数周波数軸で等間隔\n');
const Q=16.817;   // 12 平均律の隣どうしを分けるのに要る Q（後で計算します）
function morlet(f0,Qv){
  // 中心周波数 f0、品質係数 Q のモルレー窓：σ_t = Q/(2π f0)
  const sigma=Qv/(2*Math.PI*f0);
  const r=widths(sigma);
  return {sigma, Dt:r.Dt, Dw:r.Dw};
}
console.log('   中心周波数 [Hz]   σ_t [ms]    Δt [ms]    Δω [rad/s]   Δω/ω      Δt·Δω');
console.log('  '+'-'.repeat(84));
for(const f0 of [55,110,220,440,880,1760]){
  const m=morlet(f0,Q);
  console.log(`  ${String(f0).padStart(12)}   ${(m.sigma*1e3).toFixed(4).padStart(9)}  ${(m.Dt*1e3).toFixed(4).padStart(9)}   ${m.Dw.toFixed(2).padStart(10)}   ${(m.Dw/(2*Math.PI*f0)).toFixed(6)}   ${(m.Dt*m.Dw).toFixed(6)}`);
}
console.log('\n  ★ Δω/ω が一定、そして Δt·Δω も一定（＝0.5）。');
console.log('    ★ つまりウェーブレットは「ln ω の軸で等分解能」の分析です。\n');
console.log('  ── ここで第 13 回・第 20 回とつながります：\n');
console.log('      第 13 回：虚数階微分の位相は ln ω に比例（メリン変換）');
console.log('      第 20 回：c·t=一定 の座標系では位相が ln t に比例');
console.log('      本回　：ウェーブレットは ln ω について等間隔\n');
console.log('  ★★ 三つとも「対数軸が自然な世界」の道具でした。');
console.log('    ★ フーリエが時間並進の道具なら、ウェーブレットはスケール変換の道具です。');
console.log('      ── だから自己相似な信号（1/f 雑音、乱流、地震波）に強い。\n');
console.log('  音楽の例で Q を出しておきます。半音を分けるには：\n');
const ratio=Math.pow(2,1/12);
const Qneed=1/(ratio-1);
console.log(`      隣の半音との比 = 2^(1/12) = ${ratio.toFixed(6)}`);
console.log(`      要る Q = 1/(2^(1/12) − 1) = ${Qneed.toFixed(3)}`);
console.log(`      ★ Q = ${Qneed.toFixed(1)} ── だから音楽の分析は定 Q でやる。`);

console.log('\n##################################################################');
console.log('# 4. 第 4 回の宿題に決着をつける ── 階段状の変化は捕まえられるか');
console.log('##################################################################\n');
console.log('  第 4 回でこう書きました ──\n');
console.log('      「フーリエは定常性を仮定する。一度きりの跳びは');
console.log('        全周波数に薄く広がって、どの帯域の上限にもかからない」\n');
console.log('  ★ ではウェーブレット（時間局在した基底）に乗り換えればどうか。');
console.log('    信号を作って試します：途中で一度だけ振幅が跳ぶ正弦波。\n');
function stepSignal(){
  const x=new Float64Array(N);
  for(let i=0;i<N;i++){
    const t=i*dt;
    const amp=(i<N/2)?1.0:1.2;      // 中央で 20 % 跳ぶ
    x[i]=amp*Math.sin(2*Math.PI*440*t);
  }
  return x;
}
function stft(x,sigma,tc){
  // 時刻 tc を中心にガウス窓をかけて、440 Hz 成分の振幅を測る
  let sr=0,si=0,norm=0;
  for(let i=0;i<N;i++){
    const t=i*dt-tc;
    const w=Math.exp(-t*t/(2*sigma*sigma));
    const ph=2*Math.PI*440*(i*dt);
    sr+=x[i]*w*Math.cos(ph); si-=x[i]*w*Math.sin(ph);
    norm+=w;
  }
  return 2*Math.hypot(sr,si)/norm;
}
{
  const x=stepSignal();
  const Ttot=N*dt, tmid=Ttot/2;
  console.log('  窓を動かしながら 440 Hz 成分の振幅を測り、跳びが');
  console.log('  「1.02 から 1.18 に立ち上がるのにかかる時間」を遷移幅とします。\n');
  console.log('   窓 σ [ms]   Δf [Hz]    遷移幅 [ms]   Δt [ms]   遷移幅/Δt   時間と周波数の積');
  console.log('  '+'-'.repeat(88));
  for(const sms of [1,3,10,30,100]){
    const sigma=sms*1e-3;
    const w=widths(sigma);
    const df=w.Dw/(2*Math.PI);
    // 立ち上がりを走査
    let t10=null,t90=null;
    const span=8*sigma, step=span/400;
    for(let t=tmid-span;t<=tmid+span;t+=step){
      const a2=stft(x,sigma,t);
      if(t10===null && a2>=1.02) t10=t;
      if(t90===null && a2>=1.18) t90=t;
    }
    if(t10===null||t90===null){ console.log(`  ${sms.toFixed(0).padStart(9)}   ${df.toFixed(2).padStart(7)}     （窓が広すぎて読めません）`); continue; }
    const rise=(t90-t10)*1e3;
    console.log(`  ${sms.toFixed(0).padStart(9)}   ${df.toFixed(2).padStart(7)}   ${rise.toFixed(3).padStart(10)}   ${(w.Dt*1e3).toFixed(3).padStart(8)}   ${(rise/(w.Dt*1e3)).toFixed(3).padStart(8)}   ${(rise*1e-3*w.Dw).toFixed(3)}`);
  }
}
console.log('\n  ★ 遷移幅は Δt にきれいに比例します（比が一定）。');
console.log('    窓を狭くすれば「いつ跳んだか」が鋭く出る ── でも Δf が 100 倍 広がる。');
console.log('    ★ 遷移幅 × Δω も一定 ── 配分を変えているだけです。\n');
console.log('  ★ 結論（第 4 回への回答）：\n');
console.log('      定常性の仮定は外せる。不確定性は外せない。\n');
console.log('  ── 階段状の変化はウェーブレットで捕まります。');
console.log('    でも「いつ」と「どの周波数で」を同時に細かくはできない。');
console.log('    ★ 第 4 回の限界①（定常性）は克服でき、第 9 回の限界（帯域幅定理）は残る。');

console.log('\n##################################################################');
console.log('# 5. 測ると、なぜ干渉が消えるのか ── デコヒーレンスは位相の拡散');
console.log('##################################################################\n');
console.log('  二つの経路の位相差が φ なら、干渉の可視度は\n');
console.log('      V = |⟨e^(iφ)⟩|\n');
console.log('  φ が分散 σ_φ² のガウス分布なら、きれいな形になります：\n');
console.log('      ★ V = exp(−σ_φ²/2)\n');
console.log('   位相のばらつき σ_φ [rad]    可視度 V        様子');
console.log('  '+'-'.repeat(64));
for(const sp of [0,0.1,0.5,1,2,3,5]){
  const V=Math.exp(-sp*sp/2);
  let st='';
  if(V>0.9) st='ほぼ完全な干渉';
  else if(V>0.1) st='干渉が見える';
  else if(V>1e-3) st='ほぼ消えた';
  else st='★ 古典的';
  console.log(`  ${sp.toFixed(1).padStart(16)}          ${V.toExponential(3).padStart(10)}     ${st}`);
}
console.log('\n  ★ σ_φ が 1 rad を超えたあたりで、干渉は急速に消えます。');
console.log('    ── 「観測した」とは、環境が位相を 1 rad 以上 かき混ぜたということ。\n');
console.log('  ★ ここで第 19 回・第 21 回とつながります：\n');
console.log('      可視度 V は単調に減る。振動しない。');
console.log('      ★ つまりデコヒーレンスは虚軸の現象です。だから戻らない。');

console.log('\n##################################################################');
console.log('# 6. デコヒーレンスの速さ ── なぜ大きいものは干渉しないか');
console.log('##################################################################\n');
console.log('  熱的な環境では、重ね合わせの間隔 Δx が広いほど速く壊れます：\n');
console.log('      τ_D / τ_relax ≈ (λ_dB / Δx)²,      λ_dB = ħ/√(2m k_B T)\n');
console.log('  ★ 熱的ド・ブロイ波長より広い重ね合わせは、一瞬で壊れる。\n');
const T=300;
console.log('   対象                質量 [kg]      λ_dB [m]      Δx=1 μm での');
console.log('                                                    τ_D/τ_relax');
console.log('  '+'-'.repeat(76));
const objs=[
  ['電子',            9.1093837015e-31],
  ['水素原子',        1.008*u],
  ['C60 分子',        720*u],
  ['大きなウイルス',   1e-20],
  ['塵（1 μm）',      1e-15],
  ['砂粒（1 mm）',    1e-6],
];
for(const [nm,m] of objs){
  const lam=hbar/Math.sqrt(2*m*kB*T);
  const r=Math.pow(lam/1e-6,2);
  console.log(`  ${nm.padEnd(18)} ${E(m).padStart(12)}   ${E(lam).padStart(11)}   ${E(r)}`);
}
console.log('\n  ★ 電子と塵で 15 桁 違います。');
console.log('    ★ 「大きいものが干渉しない」のは量子力学が効かないからではなく、');
console.log('      ★ デコヒーレンスが速すぎて見えないからでした。\n');
console.log('  実際に干渉させた実験の記録：\n');
const exps=[
  ['電子（1927）',           9.1093837015e-31, 1e7],
  ['中性子（1970年代）',      1.675e-27,        2000],
  ['ヘリウム原子',           4.003*u,          1000],
  ['C60 分子（1999）',       720*u,            200],
  ['★ 大きな分子（2019）',   25000*u,          100],
];
console.log('   実験                   質量 [kg]     速さ [m/s]   ド・ブロイ波長 [m]');
console.log('  '+'-'.repeat(76));
for(const [nm,m,v] of exps){
  const lam=h/(m*v);
  console.log(`  ${nm.padEnd(22)} ${E(m).padStart(11)}   ${E(v).padStart(9)}    ${E(lam)}`);
}
console.log('\n  ★ C60 の波長は 2.8 pm ── 分子そのもの（直径 1 nm）の 1/360 です。');
console.log('    ★ 自分より 360 倍 小さい波長で、自分自身と干渉している。');

console.log('\n##################################################################');
console.log('# 7. 測定そのものの限界 ── 標準量子限界');
console.log('##################################################################\n');
console.log('  自由質量 m の位置を、時間 τ かけて測るときの限界：\n');
console.log('      Δx ≥ √(ħτ/m)        ★ 標準量子限界（SQL）\n');
console.log('  ★ 由来は第 9 回です ── 位置を精密に測ると運動量が乱れ、');
console.log('    その運動量が τ のあいだに位置をぼかす。\n');
console.log('   系                     質量 [kg]     時間 τ [s]     SQL [m]');
console.log('  '+'-'.repeat(76));
const sqls=[
  ['LIGO の鏡（100 Hz）',  40,     1/(2*Math.PI*100)],
  ['LIGO の鏡（1 kHz）',   40,     1/(2*Math.PI*1000)],
  ['1 g の振動子',         1e-3,   1e-3],
  ['原子 1 個（1 ms）',    87*u,   1e-3],
];
for(const [nm,m,tau] of sqls){
  console.log(`  ${nm.padEnd(22)} ${E(m).padStart(10)}   ${E(tau).padStart(11)}   ${E(Math.sqrt(hbar*tau/m))}`);
}
console.log('\n  ★ LIGO の鏡（40 kg）を 100 Hz で測るときの SQL は 6.5×10⁻²⁰ m。');
console.log('    ── 陽子の大きさの 1 万分の 1 より小さい。\n');
console.log('  ★ そして LIGO は、この限界を実際に押しています ──');
console.log('    スクイーズド光で片方の揺らぎを圧縮し、もう片方に押しつける。');
console.log('    ★ 第 9 回の「積は動かせないが、配分は選べる」を、そのまま使っています。\n');
console.log('   スクイージング [dB]   雑音の低減率     実効的な感度向上');
console.log('  '+'-'.repeat(60));
for(const db of [0,3,6,10]){
  const f=Math.pow(10,-db/20);
  console.log(`  ${String(db).padStart(14)}        ${f.toFixed(4)}          ${(1/f).toFixed(2)} 倍`);
}
console.log('\n  ★ 6 dB で 2 倍。観測できる宇宙の体積は 2³ = 8 倍 になります。');

console.log('\n##################################################################');
console.log('# 8. 測定を、情報の言葉で');
console.log('##################################################################\n');
console.log('  第 21 回で「情報は虚軸に住む」と書きました。測定も同じです：\n');
const meas=[
  ['測定の前',    '重ね合わせ',   '位相が定まっている', '可逆'],
  ['測定の最中',  '環境と相関',   '位相が環境へ漏れる', '★ ここで虚軸に乗る'],
  ['測定の後',    '確定した値',   '位相が失われた',     '不可逆'],
];
console.log('   段階          状態            位相                 可逆性');
console.log('  '+'-'.repeat(76));
for(const [a,b,cc,d] of meas) console.log(`  ${a.padEnd(12)} ${b.padEnd(14)} ${cc.padEnd(20)} ${d}`);
console.log('\n  ★ 「測定が不可逆」なのは、位相を環境に捨てるからでした。');
console.log('    ── 第 21 回のランダウアーと同じ構造です。捨てた分だけ熱が出る。\n');
console.log('  1 ビット 得るのに要る最小のエネルギー（室温）：\n');
console.log(`      k_B T ln2 = ${E(kB*300*Math.LN2)} J = ${(kB*300*Math.LN2/1.602176634e-19).toFixed(4)} eV\n`);
console.log('  ★ ただし「測定」自体は原理的に無料にできます（可逆測定）。');
console.log('    払わねばならないのは ★ 記録を消すとき ── これがランダウアーの主張です。');

console.log('\n##################################################################');
console.log('# 9. まとめ');
console.log('##################################################################\n');
const sm=[
  ['測定＝基底の選択',        '◎ 整理',  '時刻か周波数か、その中間か'],
  ['窓の Δt·Δω = 0.5',      '◎ 数値',  'ガウス窓。第 9 回と一致'],
  ['ウェーブレット＝対数軸',  '◎ 数値',  '★ Δω/ω 一定。第 13・20 回と同族'],
  ['階段状の変化は捕まる',    '◎ 数値',  '★ 第 4 回の限界①は克服できる'],
  ['でも不確定性は残る',      '◎ 厳密',  '第 9 回の限界は外せない'],
  ['V = exp(−σ_φ²/2)',      '◎ 厳密',  'σ_φ ~ 1 rad で干渉が消える'],
  ['デコヒーレンスは虚軸',    '◎ 整理',  '★ 単調に減る。だから戻らない'],
  ['電子と塵で 15 桁',       '◎ 計算',  '大きいものは速く壊れるだけ'],
  ['LIGO の SQL 6.5×10⁻²⁰ m','◎ 計算', 'スクイーズド光で押している'],
];
console.log('  主張                      判定      根拠');
console.log('  '+'-'.repeat(76));
for(const [a,b,cc] of sm) console.log(`  ${a.padEnd(24)} ${b.padEnd(9)} ${cc}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     「観測する」とは、どの基底に射影するかを選ぶことだった。');
console.log('     選べるのは配分だけで、総量（ΔtΔω ≥ 1/2）は動かせない。');
console.log('     ── そして測定が不可逆なのは、位相を虚軸に捨てるからだった。');
