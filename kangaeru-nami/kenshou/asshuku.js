// 考える波 第 36 回 検証スクリプト
//   圧搾光 ── AM 雑音と FM 雑音を交換する
//
//   実行: node asshuku.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

// ------------------------------------------------------------------
hr('1. 位相の自由度の次は、位相の雑音');

console.log('  第 35 回で ★ 位相の自由度（角度・経路）を見ました。');
console.log('  ★ 本回は ★ 位相の ★ 雑音です。');
console.log('');
console.log('  ★ 単色の光を、二つの直交成分に分けます（第 32 回の AM / FM と同じ分け方）：');
console.log('');
console.log('      E(t) = X₁·cos ω₀t + X₂·sin ω₀t');
console.log('');
console.log('      ★ X₁ ＝ 振幅側（AM に対応）   ★ X₂ ＝ 位相側（FM に対応）');
console.log('');
console.log('  ★★ 量子力学は、この二つに ★ 同時にゼロにできない揺らぎを課します：');
console.log('');
console.log('      ★ ΔX₁ · ΔX₂ ≥ 1/4     （真空ゆらぎの規格化）');
console.log('');
console.log('  ★ 第 9 回の Δt·Δω ≥ 1/2 と ★ 同じ形です ── ★ フーリエ対だから。');
console.log('');
console.log('  ★★★ ★ すると当然、こう考えます ──');
console.log('      ★ 積が一定なら、★ 片方を減らして ★ もう片方に押しつけられるのでは？');
console.log('      ★ それが ★ 圧搾光（スクイーズド光）です。');

// ------------------------------------------------------------------
hr('2. 圧搾の量を数える');

console.log('  ★ 圧搾は一つの実数 r（スクイーズ・パラメータ）で書けます：');
console.log('');
console.log('      ★ ΔX₁ = ½e^(−r)、  ΔX₂ = ½e^(+r)     → ★ 積はいつも 1/4');
console.log('');
{
  console.log('  ' + pad('r',10) + pad('ΔX₁',14) + pad('ΔX₂',14) + pad('積',14)
            + pad('圧搾 [dB]',14) + '反対側 [dB]');
  console.log('  ' + '-'.repeat(78));
  [0,0.5,1.0,1.151,1.5,1.727,2.303].forEach(function(r){
    const x1=0.5*Math.exp(-r), x2=0.5*Math.exp(r);
    const db=20*Math.log10(x1/0.5);
    console.log('  ' + pad(f(r,3),10) + pad(f(x1,6),14) + pad(f(x2,6),14)
      + pad(f(x1*x2,8),14) + pad(f(db,2),14) + f(-db,2));
  });
  console.log('');
  console.log('  ★ 積はどこでも ★ 0.25 ── ★ 不確定性は破っていません。★ 配分を変えただけ。');
  console.log('');
  console.log('  ★ 実測の目安：');
  console.log('      ★ LIGO（2019〜）  ── ★ 約 3 dB');
  console.log('      ★ LIGO（最近）    ── ★ 約 6 dB');
  console.log('      ★ 研究室の最高記録 ── ★ 約 15 dB（r = 1.73）');
  console.log('');
  console.log('  ★★ 音の言葉では ── ★ 雑音を「イコライザで動かした」のと同じ。');
  console.log('    ★ 総量は変えられないが、★ どの直交成分に乗せるかは選べる。');
}

// ------------------------------------------------------------------
hr('3. ★★ AM 側波帯と FM 側波帯 ── 第 32 回の続き');

console.log('  ★ 直交成分は、側波帯の言葉に直せます。');
console.log('  ★ 搬送波 ω₀ の上下に、Ω 離れた側波帯が一対 あるとします：');
console.log('');
console.log('      E(t) = cos ω₀t + a·cos((ω₀+Ω)t + θ₊) + a·cos((ω₀−Ω)t + θ₋)');
console.log('');
console.log('  ★ 搬送波を基準にした複素表示で書くと、摂動はこうまとまります：');
console.log('');
console.log('      ★ P(t) = 2a·e^(iθ)·cos(Ωt + δ),   θ = (θ₊+θ₋)/2、δ = (θ₊−θ₋)/2');
console.log('');
console.log('  ★★ つまり ★ 二つの側波帯の位相の ★ 平均 θ だけが、AM か FM かを決めます：');
console.log('      ★ θ = 0   → P が実 → ★ 振幅が揺れる（AM）');
console.log('      ★ θ = π/2 → P が虚 → ★ 位相が揺れる（FM）');
console.log('      ★ δ は ★ 揺れる「タイミング」を決めるだけ。');
console.log('');
{
  function analyze(a, tp, tm, N){
    const Om=1, T=2*Math.PI/Om;
    let amin=1e9, amax=-1e9, pmin=1e9, pmax=-1e9;
    for(let i=0;i<N;i++){
      const t=T*i/N;
      const re=1+a*Math.cos(Om*t+tp)+a*Math.cos(-Om*t+tm);
      const im=  a*Math.sin(Om*t+tp)+a*Math.sin(-Om*t+tm);
      const A=Math.hypot(re,im), Ph=Math.atan2(im,re);
      if(A<amin)amin=A; if(A>amax)amax=A;
      if(Ph<pmin)pmin=Ph; if(Ph>pmax)pmax=Ph;
    }
    return {dA:(amax-amin)/2, dP:(pmax-pmin)/2};
  }
  const a=0.05;
  console.log('  ' + pad('θ₊',10) + pad('θ₋',10) + pad('θ=平均',10)
            + pad('振幅の振れ',16) + pad('位相の振れ',16) + '中身');
  console.log('  ' + '-'.repeat(74));
  [[0,0,'★ 純 AM'],
   [Math.PI/2,-Math.PI/2,'★ 純 AM（δ だけ違う）'],
   [Math.PI/2,Math.PI/2,'★ 純 FM'],
   [Math.PI,0,'★ 純 FM（δ だけ違う）'],
   [Math.PI/4,Math.PI/4,'45 度 の混合']].forEach(function(p){
    const r=analyze(a,p[0],p[1],400000);
    console.log('  ' + pad(f(p[0],3),10) + pad(f(p[1],3),10) + pad(f((p[0]+p[1])/2,3),10)
      + pad(f(r.dA,6),16) + pad(f(r.dP,6),16) + p[2]);
  });
  console.log('');
  console.log('  ★★ 平均 θ が 0 なら ★ 振幅だけ、π/2 なら ★ 位相だけが揺れます。');
  console.log('    ★ 側波帯の ★ 差 δ を変えても、AM か FM かは ★ 変わりません（タイミングだけ）。');
  console.log('');
  console.log('  ★★★ ★ 圧搾光とは ──');
  console.log('      ★ 側波帯の対に ★ 相関をつけて、★ AM 側の雑音を FM 側へ寄せること。');
  console.log('');
  console.log('  ★ 第 32 回では ★ ヒッグス＝AM、ゴールドストーン＝FM と見ました。');
  console.log('    ★ 同じ分け方が ★ ここでは「雑音をどちらに置くか」の設計になっています。');
}

// ------------------------------------------------------------------
hr('4. ★ 何が圧搾するのか ── 位相に依存する増幅');

console.log('  ★ 圧搾を作るのは ★ 非線形（第 23 回）です。');
console.log('  ★ 二倍の周波数でばね定数を揺すります（パラメトリック励振）：');
console.log('');
console.log('      ★ ẍ + ω₀²(1 + h·cos 2ω₀t)·x = 0');
console.log('');
console.log('  ★ 増幅と減衰を ★ きちんと分けるには ★ 一周期の写像（フロケ行列）を見ます：');
console.log('      ★ 初期条件 (1,0) と (0,1) をそれぞれ一周期 走らせて 2×2 行列 M を作り、');
console.log('      ★ その固有値を見る。★ |μ| > 1 が増幅、< 1 が減衰。');
console.log('');
{
  const w0=1;
  function monodromy(h){
    const Td=Math.PI/w0;              // 駆動の周期 2π/(2ω₀)
    const dt=Td/2000000;
    function der(s,t){ return [s[1], -w0*w0*(1+h*Math.cos(2*w0*t))*s[0]]; }
    function run(s0){
      let s=s0.slice(), t=0;
      for(let n=0;n<2000000;n++){
        const k1=der(s,t);
        const k2=der([s[0]+0.5*dt*k1[0],s[1]+0.5*dt*k1[1]],t+0.5*dt);
        const k3=der([s[0]+0.5*dt*k2[0],s[1]+0.5*dt*k2[1]],t+0.5*dt);
        const k4=der([s[0]+dt*k3[0],s[1]+dt*k3[1]],t+dt);
        s=[s[0]+dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6,
           s[1]+dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6];
        t+=dt;
      }
      return s;
    }
    const c1=run([1,0]), c2=run([0,1]);
    // M = [[c1[0], c2[0]],[c1[1], c2[1]]]
    const tr=c1[0]+c2[1], det=c1[0]*c2[1]-c2[0]*c1[1];
    const disc=tr*tr/4-det;
    let mu1, mu2;
    if(disc>=0){ mu1=tr/2+Math.sqrt(disc); mu2=tr/2-Math.sqrt(disc);
      if(Math.abs(mu1)<Math.abs(mu2)){ const t0=mu1; mu1=mu2; mu2=t0; } }
    else { mu1=NaN; mu2=NaN; }
    return {tr:tr, det:det, mu1:mu1, mu2:mu2, Td:Td};
  }
  console.log('  ' + pad('h',10) + pad('det M',14) + pad('|μ₊|',14) + pad('|μ₋|',14)
            + pad('積',12) + pad('成長率 ln|μ₊|/T',18) + '予言 hω₀/4');
  console.log('  ' + '-'.repeat(94));
  [0, 0.02, 0.05, 0.1, 0.2].forEach(function(h){
    const r=monodromy(h);
    if(isNaN(r.mu1)){
      console.log('  ' + pad(f(h,3),10) + pad(f(r.det,10),14) + pad('（複素）',14)
        + pad('（複素）',14) + pad('1',12) + pad('0（安定）',18) + f(h*w0/4,6));
    } else {
      const rate=Math.log(Math.abs(r.mu1))/r.Td;
      console.log('  ' + pad(f(h,3),10) + pad(f(r.det,10),14) + pad(f(Math.abs(r.mu1),8),14)
        + pad(f(Math.abs(r.mu2),8),14) + pad(f(Math.abs(r.mu1*r.mu2),6),12)
        + pad(f(rate,6),18) + f(h*w0/4,6));
    }
  });
  console.log('');
  console.log('  ★★ ★ 固有値が ★ 一つは 1 より大きく、★ もう一つは小さい。');
  console.log('    ★ そして ★ 積はいつも ★ ちょうど 1（det M = 1）。');
  console.log('');
  console.log('  ★★★ ここが本回の要です ──');
  console.log('      ★ det M = 1 ＝ ★ 面積が保存する ＝ ★ ΔX₁·ΔX₂ が保存する。');
  console.log('      ★ だから ★ 片方を e^(−r) に縮めると、もう片方は ★ 必ず e^(+r) に伸びる。');
  console.log('      ★ 不確定性が破れないのは、★ 力学が面積を保つからでした。');
  console.log('');
  console.log('  ★ 成長率は ★ hω₀/4 とよく合います（h が小さいほど良い）。');
  console.log('');
  console.log('  ★ 第 34 回では ★ 揺すりの周波数が合っていなかったので育ちませんでした。');
  console.log('    ★★ ★ パラメトリック増幅は ★ ちょうど二倍でないと効きません ── 共鳴条件。');
  console.log('    ★ ブランコの立ち漕ぎが「一往復に二回しゃがむ」のと同じ理由です。');
}

// ------------------------------------------------------------------
hr('5. 重力波にどれだけ効くか');

{
  console.log('  ★ 第 22 回で ★ LIGO の標準量子限界を見ました。');
  console.log('  ★ ショット雑音に支配される帯では、感度は ★ 雑音の振幅に比例します。');
  console.log('');
  console.log('  ' + pad('圧搾 [dB]',14) + pad('雑音の振幅',16) + pad('到達距離',16)
            + pad('★ 観測体積',16) + '事象率');
  console.log('  ' + '-'.repeat(74));
  [0,3,6,10,15].forEach(function(db){
    const amp=Math.pow(10,-db/20);
    const range=1/amp;
    console.log('  ' + pad(f(db,0),14) + pad(f(amp,5),16) + pad(f(range,4)+' 倍',16)
      + pad(f(range*range*range,3)+' 倍',16) + f(range*range*range,2) + ' 倍');
  });
  console.log('');
  console.log('  ★★ 6 dB の圧搾で ★ 到達距離が 2 倍、★ 観測体積が 8 倍。');
  console.log('    ★ 「見える宇宙が 8 倍 になる」── ★ 鏡もレーザーも変えずに。');
  console.log('');
  console.log('  ★ ただし ★ ただではありません（第 22 回の標準量子限界）：');
  console.log('      ★ 位相の雑音を減らすと ★ 振幅の雑音が増え、');
  console.log('      ★ その振幅の雑音が ★ 鏡を蹴ります（輻射圧雑音）。');
  console.log('    ★ 低周波では輻射圧が、高周波ではショット雑音が効くので、');
  console.log('      ★★ ★ 周波数ごとに圧搾の向きを変える必要があります（周波数依存圧搾）。');
}

// ------------------------------------------------------------------
hr('6. ★ 限界は「損失」── 減衰が真空を混ぜる');

console.log('  ★ 圧搾光の最大の敵は ★ 損失です。');
console.log('  ★ 透過率 η の素子を通すと、圧搾は ★ こう薄まります：');
console.log('');
console.log('      ★ S = η·e^(−2r) + (1 − η)');
console.log('');
console.log('  ★ 第二項が ★ 混ざってきた真空ゆらぎ ── ★ 失った光の代わりに入ってくる。');
console.log('');
{
  console.log('  ' + pad('透過率 η',14) + pad('損失',12) + pad('r=1.5 のとき [dB]',22)
            + pad('★ r→∞ の限界 [dB]',22));
  console.log('  ' + '-'.repeat(70));
  [1.0,0.99,0.95,0.90,0.80,0.50].forEach(function(eta){
    const r=1.5;
    const S=eta*Math.exp(-2*r)+(1-eta);
    const lim=(1-eta);
    console.log('  ' + pad(f(eta,3),14) + pad(f((1-eta)*100,1)+' %',12)
      + pad(f(10*Math.log10(S),3),22)
      + pad(eta===1?'（無限に圧搾できる）':f(10*Math.log10(lim),2),22));
  });
  console.log('');
  console.log('  ★★ ★ 損失 5 % で ★ どんなに頑張っても 13 dB が上限。');
  console.log('    ★ 損失 10 % なら 10 dB。★ これが実験の壁です。');
  console.log('');
  console.log('  ★ 波の言葉で言うと ── ★ 減衰は ★ 真空ゆらぎを混ぜる操作です。');
  console.log('    ★ 第 22 回で「デコヒーレンスは V = e^(−σ²/2) で単調に減る」と書きました。');
  console.log('    ★★ 圧搾も同じで、★ 一度 薄まったら ★ 戻せません（虚軸の現象）。');
  console.log('');
  console.log('  ★ だから圧搾光の実験は ★ 損失との戦いになります ──');
  console.log('      ★ 光学素子を減らす、反射率を上げる、検出器の量子効率を上げる。');
  console.log('    ★ 「増幅して信号を大きくする」では解決しません ── 増幅も雑音を足すからです。');
}

// ------------------------------------------------------------------
hr('7. まとめ');

{
  const rows = [
    ['ΔX₁·ΔX₂ = 1/4 は不変',     '◎ 数値', '★ r を振っても積は 0.25'],
    ['圧搾は配分の変更',           '◎ 解析', '★ 総量は変えられない'],
    ['側波帯 同相 → AM',          '◎ 数値', '★ 振幅だけ揺れる'],
    ['側波帯 逆相 → FM',          '◎ 数値', '★ 位相だけ揺れる'],
    ['★ 圧搾＝側波帯の相関',       '◎ 対応', '★ 第 32 回の AM/FM と同じ分け方'],
    ['位相依存増幅で作れる',       '◎ 数値', '★ 増幅率 hω₀/4 と一致'],
    ['★ 共鳴条件は「ちょうど二倍」', '◎ 数値', '★ 第 34 回の失敗の理由'],
    ['6 dB で観測体積 8 倍',      '◎ 数値', '★ 鏡もレーザーも変えずに'],
    ['★ 損失 5 % で 13 dB が上限', '◎ 数値', '★ 実験の壁。減衰は真空を混ぜる']
  ];
  console.log('  ' + pad('主張',28) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(82));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],28)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     不確定性は ★ 総量の話であって、★ 配分の話ではなかった。');
  console.log('     ★★ だから ★ AM の雑音を FM へ寄せられる ── それが圧搾光。');
  console.log('     ★ そして ★ 損失だけは ★ 取り返せません。');
  console.log('');
  console.log('  ★ 第 32 回：ヒッグスは AM、ゴールドストーンは FM（★ 場の自由度）');
  console.log('  ★ 第 35 回：偏光は振幅側、OAM は位相側（★ 光の自由度）');
  console.log('  ★ 本回　　：雑音も AM 側と FM 側に分かれる（★ 揺らぎの自由度）');
  console.log('    ★★ ★ 同じ二分法が、★ 三つの階層で効いていました。');
}

console.log('');
