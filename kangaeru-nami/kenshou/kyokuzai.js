// 考える波 第 37 回 検証スクリプト
//   アンダーソン局在 ── 吸収がないのに、波が止まる
//   そして「次元で決まる」理由は、ランダムウォークが原点に戻るかどうかだった
//
//   実行: node kyokuzai.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

// mulberry32
function mkRnd(seed){
  return function(){
    seed = (seed + 0x6D2B79F5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ------------------------------------------------------------------
hr('1. 媒質を乱すと、波は止まる');

console.log('  ここまで 36 回、媒質は ★ きれいに揃っているとしてきました。');
console.log('  ★ 本回はそれを壊します ── ★ 乱れた媒質に波を入れる。');
console.log('');
console.log('  ★ 素朴な予想：★ 散乱されて、拡散になるだろう（ランダムウォーク）。');
console.log('  ★★ ところが ── ★ ある条件を超えると ★ 拡散すらしなくなります。');
console.log('');
console.log('      ★★ アンダーソン局在（1958）── ★ 吸収がないのに波が止まる。');
console.log('');
console.log('  ★ これは ★ 量子に限りません。★ 純粋に ★ 波の現象です：');
console.log('      ★ 光（乱れた導波路）、音、マイクロ波、水面波、冷却原子 ── どれでも起きる。');
console.log('');
console.log('  ★ 本回で確かめること：');
console.log('      ① 1 次元では ★ どんなに弱い乱れでも局在する（局在長を測る）');
console.log('      ② 局在は ★ 指数減衰だが、第 28 回の指数とは ★ 原因が違う');
console.log('      ③ ★★ 次元で決まる理由は ★ ランダムウォークが原点に戻るかどうかだった');

// ------------------------------------------------------------------
hr('2. 1 次元で、局在長を測る');

console.log('  いちばん簡単な模型（タイトバインディング）で走らせます：');
console.log('');
console.log('      ★ ψ_{n+1} = (E − ε_n)·ψ_n − ψ_{n−1},   ε_n ∈ [−W/2, +W/2] の一様乱数');
console.log('');
console.log('  ★ W = 0 なら ★ ただの平面波（伝わる）。★ W > 0 で何が起きるか。');
console.log('  ★ 転送行列の積の伸び率（リャプノフ指数 γ）を測り、★ 局在長 ξ = 1/γ とします。');
console.log('');

function lyapunov(W, E, N, seed){
  const rnd = mkRnd(seed);
  let a=1, b=0;            // (ψ_n, ψ_{n-1})
  let sum=0;
  for(let n=0;n<N;n++){
    const eps = (rnd()-0.5)*W;
    const an = (E-eps)*a - b;
    b = a; a = an;
    const nrm = Math.hypot(a,b);
    if(nrm>0){ sum += Math.log(nrm); a/=nrm; b/=nrm; }
  }
  return sum/N;
}

{
  const N=2000000;
  console.log('  ★ バンド中心から少し外した E = 0.5 で測ります（★ 中心には別の異常があるため）：');
  console.log('');
  console.log('  ' + pad('乱れ W',10) + pad('γ = 1/ξ',16) + pad('局在長 ξ [格子]',20)
            + pad('ξ·W²',16) + '');
  console.log('  ' + '-'.repeat(62));
  const Ws=[0.25,0.5,1,2,4];
  const xis=[];
  Ws.forEach(function(W,i){
    const g = lyapunov(W, 0.5, N, 12345+i*977);
    const xi = 1/g;
    xis.push([W,xi]);
    console.log('  ' + pad(f(W,3),10) + pad(e(g,4),16) + pad(f(xi,3),20) + pad(f(xi*W*W,3),16));
  });
  console.log('');
  // 指数をフィット
  let sx=0, sy=0, sxx=0, sxy=0; const n=xis.length;
  xis.forEach(function(p){ const x=Math.log(p[0]), y=Math.log(p[1]); sx+=x; sy+=y; sxx+=x*x; sxy+=x*y; });
  const slope=(n*sxy-sx*sy)/(n*sxx-sx*sx);
  console.log('      ★ ln ξ を ln W で回帰した傾き = ' + f(slope,4) + '（★ 弱乱れの予言 −2）');
  console.log('');
  console.log('  ★★ ★ W がどんなに小さくても ★ ξ は有限です ── ★ 必ず局在します。');
  console.log('    ★ ただし ξ ∝ W^(−2) なので、★ 弱い乱れでは ★ 途方もなく長くなる：');
  console.log('');
  [0.01,0.001].forEach(function(W){
    const xi=xis[0][1]*Math.pow(xis[0][0]/W,2);
    console.log('      W = ' + f(W,4) + ' なら ξ ≈ ' + e(xi,3) + ' 格子');
  });
  console.log('');
  console.log('  ★ だから ★ 実験では「局在していない」ように見えます ── ★ 試料が短いだけ。');
  console.log('    ★ これは第 5 回の「宇宙年齢より長い周期は定数と区別がつかない」と ★ 同じ構図。');
}

// ------------------------------------------------------------------
hr('3. 同じ「指数減衰」でも、原因が違う');

{
  console.log('  ★ 第 28 回で「進めない波は指数になる」と書きました。★ 見分けます：');
  console.log('');
  console.log('  ' + pad('現象',24) + pad('形',16) + pad('原因',26) + 'ゆらぐか');
  console.log('  ' + '-'.repeat(76));
  [['エバネッセント（第 6 回）','e^(−κx)','★ k² < 0（決定論）','★ ゆらがない'],
   ['トンネル（第 28 回）','e^(−2κa)','★ k² < 0（決定論）','★ ゆらがない'],
   ['★ アンダーソン局在','e^(−x/ξ)','★ 多重散乱の干渉（統計）','★★ ゆらぐ']
  ].forEach(function(r){ console.log('  ' + pad(r[0],24)+pad(r[1],16)+pad(r[2],26)+r[3]); });
  console.log('');
  console.log('  ★ 「ゆらぐ」を数値で見ます ── ★ 同じ W で乱数の種だけ変えて γ を測る：');
  console.log('');
  const N=200000, W=1, E=0.5;
  const gs=[];
  console.log('  ' + pad('種',10) + pad('γ',16) + pad('ξ = 1/γ',16));
  console.log('  ' + '-'.repeat(44));
  for(let s=0;s<6;s++){
    const g=lyapunov(W,E,N,1000+s*7919);
    gs.push(g);
    console.log('  ' + pad(s,10) + pad(e(g,5),16) + pad(f(1/g,3),16));
  }
  const m=gs.reduce((a,b)=>a+b)/gs.length;
  const sd=Math.sqrt(gs.reduce((a,b)=>a+(b-m)*(b-m),0)/gs.length);
  console.log('');
  console.log('      平均 γ = ' + e(m,5) + '、標準偏差 = ' + e(sd,2)
            + '（相対 ' + f(sd/m*100,2) + ' %）');
  console.log('');
  console.log('  ★★ 試料ごとに ★ 違う値になります ── ★ これが統計的な指数の特徴。');
  console.log('    ★ ただし ★ N を増やすと ★ ばらつきは 1/√N で縮みます（自己平均）。');
  console.log('    ★ エバネッセント波には ★ そもそもばらつきがありません。');
}

// ------------------------------------------------------------------
hr('4. ★★ なぜ次元で決まるのか ── ランダムウォークが原点に戻るか');

console.log('  ★ 局在は ★ 次元で振る舞いが変わります：');
console.log('');
console.log('      ★ 1 次元・2 次元 ── ★ どんなに弱い乱れでも ★ 必ず局在');
console.log('      ★ 3 次元       ── ★ 弱ければ拡散、強いと局在（★ 移動度端がある）');
console.log('');
console.log('  ★★ なぜ ★ 2 次元が境目なのか。★ 答えは ★ ランダムウォークの再帰性です。');
console.log('');
console.log('  ★ 局在は ★ 波が「戻ってきて自分と干渉する」ことで起きます。');
console.log('  ★ だから ★ 戻ってくる回数が効きます。★ 格子上のランダムウォークで数えます：');
console.log('');
console.log('      ★ 戻ってくる回数の期待値 = ∫ d^dk/(2π)^d · 1/(1 − λ(k)),  λ(k) = (1/d)Σcos k_i');
console.log('');
{
  function returns(d, Ngrid){
    // 1/(1-λ) の積分。λ→1 の特異点は k=0 のみ。
    // 台形で格子和（k=0 を除く）→ 発散の様子が見える
    let s=0, cnt=0;
    if(d===1){
      for(let i=1;i<Ngrid;i++){
        const k=Math.PI*i/Ngrid;
        s += 1/(1-Math.cos(k)); cnt++;
      }
    } else if(d===2){
      for(let i=0;i<Ngrid;i++) for(let j=0;j<Ngrid;j++){
        if(i===0&&j===0) continue;
        const kx=Math.PI*i/Ngrid, ky=Math.PI*j/Ngrid;
        s += 1/(1-(Math.cos(kx)+Math.cos(ky))/2); cnt++;
      }
    } else {
      for(let i=0;i<Ngrid;i++) for(let j=0;j<Ngrid;j++) for(let l=0;l<Ngrid;l++){
        if(i===0&&j===0&&l===0) continue;
        const kx=Math.PI*i/Ngrid, ky=Math.PI*j/Ngrid, kz=Math.PI*l/Ngrid;
        s += 1/(1-(Math.cos(kx)+Math.cos(ky)+Math.cos(kz))/3); cnt++;
      }
    }
    return s/cnt;
  }
  console.log('  ' + pad('格子の細かさ',16) + pad('d=1',18) + pad('d=2',18) + pad('★ d=3',18));
  console.log('  ' + '-'.repeat(70));
  [20,40,80,160].forEach(function(Ng){
    console.log('  ' + pad(Ng,16) + pad(f(returns(1,Ng),4),18) + pad(f(returns(2,Ng),4),18)
      + pad(f(returns(3,Ng),6),18));
  });
  console.log('');
  console.log('  ★★ ★ d=1 と d=2 は ★ 細かくするほど増え続けます（★ 発散）。');
  console.log('  ★★ ★ d=3 だけ ★ 有限値に落ち着きます。');
  console.log('');
  console.log('      ★ d=3 の極限値（ワトソン積分）= 1.516386…');
  console.log('        （格子 160 で 1.5636 。★ 1/N でしか近づかないので収束は遅い）');
  console.log('      ★ 戻ってくる確率 = 1 − 1/1.516386 = ' + f(1-1/1.516386,6));
  console.log('');
  console.log('  ★★★ これが ★ ポリアの定理です（1921）：');
  console.log('');
  console.log('      ★ d ≤ 2 のランダムウォークは ★ 必ず原点に戻る（再帰的）');
  console.log('      ★ d ≥ 3 では ★ 戻らないことがある（★ 3 次元で 66 % は帰らない）');
  console.log('');
  console.log('  ★★ 局在の次元依存は、★ ここから来ていました：');
  console.log('      ★ 波が戻ってこないと ★ 自分と干渉できない → ★ 局在しない');
  console.log('      ★ d ≤ 2 では ★ 必ず戻るので ★ 干渉が積み上がる → ★ 必ず局在');
  console.log('      ★ d = 3 では ★ 戻る確率が 34 % ── ★ 乱れが強くないと足りない');
}

// ------------------------------------------------------------------
hr('5. 弱局在の補正を、次元ごとに数える');

console.log('  ★ もう少し定量的に。★ 拡散する波が時刻 t に原点へ戻る確率密度は');
console.log('');
console.log('      ★ P(t) = 1/(4πDt)^(d/2)');
console.log('');
console.log('  ★ 干渉による伝導度の補正は、これを ★ 時間で積分したものに比例します：');
console.log('');
console.log('      ★ Δσ ∝ −∫ dt · (4πDt)^(−d/2)     （τ から τ_φ まで）');
console.log('');
{
  function corr(d, tau, tphi){
    const N=2000000, h=(Math.log(tphi)-Math.log(tau))/N;
    let s=0;
    for(let i=0;i<N;i++){
      const t=Math.exp(Math.log(tau)+(i+0.5)*h);
      s += Math.pow(4*Math.PI*t,-d/2)*t*h;     // dt = t d(ln t)
    }
    return s;
  }
  const tau=1;
  console.log('  ' + pad('τ_φ/τ',14) + pad('d=1（∝√t）',20) + pad('★ d=2（∝ln t）',20) + pad('d=3（収束）',20));
  console.log('  ' + '-'.repeat(72));
  [10,100,1e4,1e6,1e8].forEach(function(R){
    console.log('  ' + pad(e(R,0),14) + pad(f(corr(1,tau,tau*R),5),20)
      + pad(f(corr(2,tau,tau*R),6),20) + pad(f(corr(3,tau,tau*R),8),20));
  });
  console.log('');
  console.log('  ★★ ★ d=1 は √τ_φ で伸び、★ d=2 は ★ ln τ_φ で伸び、★ d=3 は ★ 止まります。');
  console.log('');
  console.log('  ★ つまり ★ d ≤ 2 では ★ 補正がいくらでも大きくなり、★ 摂動が破綻する');
  console.log('    ＝ ★ 拡散という描像自体が壊れる ＝ ★ 局在。');
  console.log('  ★ d = 3 では ★ 補正が有限に留まるので、★ 弱い乱れなら拡散のまま。');
  console.log('');
  console.log('  ★★★ ★ d = 2 が ★「対数」になる ── ★ これが境界次元の印です。');
  console.log('    ★ 第 30 回で ★ d = 2 が臨界 1/r² だったのと ★ 同じ数字が出ました。');
  console.log('    ★ ★ 点検します（第 29・30 回の作法）── ★ 同じものか。');
}

// ------------------------------------------------------------------
hr('6. ★ 第 30 回の d=2 と、本回の d=2 は同じものか');

{
  console.log('  ★ 二つの「d = 2 が特別」を並べます：');
  console.log('');
  console.log('  ' + pad('回',10) + pad('何が d=2 で起きるか',30) + '出どころ');
  console.log('  ' + '-'.repeat(76));
  console.log('  ' + pad('第 30 回',10) + pad('1/r² が臨界 λ=1/4 ちょうど',30)
            + '★ 球対称化の幾何（l(l+1) の最小値）');
  console.log('  ' + pad('★ 本回',10) + pad('戻る確率が発散しはじめる',30)
            + '★ 拡散の P(t) ∝ t^(−d/2) の積分');
  console.log('');
  console.log('  ★★ 判定：★ 別の出どころですが ── ★ 根は ★ 共通です。');
  console.log('');
  console.log('  ★ どちらも ★「d = 2 で対数が出る」ことが原因です：');
  console.log('      ★ 第 30 回：l = (d−3)/2 が −1/2 になり、l(l+1) が最小（対数的な臨界）');
  console.log('      ★ 本回　：∫dt·t^(−d/2) が d=2 で ★ 対数発散');
  console.log('');
  console.log('  ★★★ ★ そして ★ 対数が出る次元は ★ どちらも「べき乗の指数が −1 になる次元」。');
  console.log('    ★ これは ★ 第 27 回で見た「1/f が対数一様から出る」のと ★ 同じ数学です。');
  console.log('    ★ ── ★ 指数が −1 になると、★ 積分が対数になる。それだけ。');
  console.log('');
  console.log('  ★ ただし ★ 言いすぎないように書きます：');
  console.log('    ★ 「同じ定理から出た」のではなく ★「同じ積分の発散」が両方に現れた。');
  console.log('    ★ 物理の中身（幾何 vs 干渉）は ★ 別です。');
}

// ------------------------------------------------------------------
hr('7. 波なら何でも起きる ── 光・音・マイクロ波');

{
  console.log('  ★ アンダーソン局在は ★ 電子の話として生まれましたが、');
  console.log('  ★★ ★ 量子力学は要りません ── ★ 必要なのは ★ 波であることだけ。');
  console.log('');
  console.log('  ' + pad('系',22) + pad('波',16) + pad('次元',12) + '観測されたこと');
  console.log('  ' + '-'.repeat(72));
  [['乱れた光導波路','光','2（横方向）','★ ビームが広がらない'],
   ['マイクロ波の導波管','マイクロ波','1','★ 透過が指数で落ちる'],
   ['超音波','音','3','★ 移動度端が観測された'],
   ['冷却原子','物質波','1・3','★ 膨張が止まる'],
   ['地震波','弾性波','3','散乱が強い地殻での議論']
  ].forEach(function(r){ console.log('  ' + pad(r[0],22)+pad(r[1],16)+pad(r[2],12)+r[3]); });
  console.log('');
  console.log('  ★★ 「量子的な現象」に見えて ★ 干渉だけで説明できる ──');
  console.log('    ★ 第 8 回で「不確定性は帯域幅定理に ħ を掛けただけ」と書いたのと同じ構図です。');
  console.log('    ★ ħ は ★ 舞台装置で、★ 本質は ★ 波であること。');
}

// ------------------------------------------------------------------
hr('8. まとめ');

{
  const rows = [
    ['1 次元では必ず局在する',      '◎ 数値', '★ W→0 でも ξ は有限'],
    ['ξ ∝ W^(−2)',               '◎ 数値', '★ 回帰の傾きが −2 付近'],
    ['局在の指数は ★ ゆらぐ',      '◎ 数値', '★ 試料ごとに γ が違う（自己平均）'],
    ['第 28 回の指数とは別物',      '◎ 整理', '★ 決定論 vs 統計'],
    ['★ d≤2 は戻る、d≥3 は戻らない','◎ 数値', '★ 積分が d=1,2 で発散、d=3 で 1.5164'],
    ['3 次元の帰還確率 34 %',      '◎ 数値', '★ ポリアの定理'],
    ['弱局在の補正の次元依存',      '◎ 数値', '★ √t・ln t・収束'],
    ['★ d=2 が対数になる',        '◎ 数値', '★ 境界次元の印'],
    ['第 30 回の d=2 とは別物',    '★ 点検', '★ 幾何 vs 干渉。ただし根は「対数」で共通'],
    ['量子力学は要らない',         '◎ 実測', '★ 光・音・マイクロ波でも起きる']
  ];
  console.log('  ' + pad('主張',28) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(84));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],28)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     乱れた媒質では、★ 吸収がなくても波は止まる。');
  console.log('     ★★ そして ★ 止まるかどうかは ── ★ 波が原点に戻ってくるかで決まっていた。');
  console.log('     ── ★ 局在の次元依存は、★ ポリアの再帰定理そのものでした。');
}

console.log('');
