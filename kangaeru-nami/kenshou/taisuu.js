// 考える波 第 27 回 検証スクリプト
//   対数一様な時定数分布は、どこから来るのか
//   第 26 回が残した最後の問いに答える
//
//   実行: node taisuu.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

// ------------------------------------------------------------------
hr('1. 第 26 回が残した問い');

console.log('  第 26 回の結論はこうでした ──');
console.log('');
console.log('      分数階が現れるのは、粗視化した自由度が');
console.log('      ★ スケール不変に（べき乗で）分布しているときである。');
console.log('');
console.log('  そして 1/f 雑音だけが、問いの形を変えて残りました：');
console.log('');
console.log('      ★ なぜ自然には、対数一様な時定数分布がこれほど多いのか。');
console.log('');
console.log('  本回で答えます。結論を先に言うと ──');
console.log('  ★★ 「指数の中に平らなものがあれば、それでいい」。');

// ------------------------------------------------------------------
hr('2. まず確認 ── 対数一様な τ から、本当に 1/f が出るか');

console.log('  時定数 τ の一階緩和のスペクトルは 2τ/(1+ω²τ²)（ローレンツ型）。');
console.log('  これを重み g(τ) で重ね合わせます：');
console.log('');
console.log('      S(ω) = ∫ g(τ)·2τ/(1+ω²τ²) dτ');
console.log('');
console.log('  ★ 対数一様 ＝ ln τ について一様 ＝ g(τ) ∝ 1/τ。');
console.log('  この場合、積分は手で解けます：');
console.log('');
console.log('      ∫ (A/τ)·2τ/(1+ω²τ²) dτ = (2A/ω)[arctan ωτ]');
console.log('      ★ ωτ1 ≪ 1 ≪ ωτ2 の帯では → πA/ω ── ぴったり 1/f。');
console.log('');

// 数値：ln τ を等分して足す
function spectrumLogUniform(w, lnt1, lnt2, N){
  const h = (lnt2-lnt1)/N;
  let s = 0;
  for(let i=0;i<N;i++){
    const lt = lnt1 + (i+0.5)*h;
    const tau = Math.exp(lt);
    s += 2*tau/(1+w*w*tau*tau) * h;   // g dτ = (A/τ)·τ d(lnτ) = A d(lnτ)
  }
  return s;
}

{
  const lnt1 = Math.log(1e-6), lnt2 = Math.log(1e6);  // 12 桁
  console.log('  数値で確かめます。τ ∈ [1e−6, 1e+6] 秒（12 桁）を対数等分：');
  console.log('');
  console.log('  ' + pad('ω [rad/s]',14) + pad('S(ω)',16) + pad('傾き [/dec]',14) + '予言');
  console.log('  ' + '-'.repeat(64));
  let prevW=null, prevS=null;
  const exact = [];
  for(let k=-4;k<=4;k++){
    const w = Math.pow(10,k);
    const S = spectrumLogUniform(w, lnt1, lnt2, 200000);
    let sl = '';
    if(prevS!==null) sl = f(Math.log10(S/prevS)/Math.log10(w/prevW),4);
    exact.push([w,S]);
    console.log('  ' + pad(e(w,0),14) + pad(e(S,6),16) + pad(sl,14) + (k>=-3&&k<=3?'−1':'（帯の外）'));
    prevW=w; prevS=S;
  }
  console.log('');
  // 帯の中央での振幅を理論値 π/ω と比べる
  const S1 = spectrumLogUniform(1, lnt1, lnt2, 200000);
  console.log('  ω=1 での理論値 πA/ω = ' + f(Math.PI,6) + '、数値 = ' + f(S1,6)
              + '（相対誤差 ' + e(Math.abs(S1-Math.PI)/Math.PI,2) + '）');
  console.log('');
  console.log('  ★ 帯の中で傾きがちょうど −1 ── 対数一様 ⇒ 1/f は確かです。');
  console.log('  ★ そして帯の外（1/τ2 より下、1/τ1 より上）では平らに寝ます。');
  console.log('    ── ★ 1/f には必ず上下の折れ点があります。無限には続きません。');
}

// ------------------------------------------------------------------
hr('3. ★ 本題 ── 対数一様はどこから来るのか');

console.log('  ここが第 26 回の残した謎でした。');
console.log('  g(τ) ∝ 1/τ は、τ を直接 見ると「特別な形」に見えます。');
console.log('  ところが ── ★ 変数を一つ替えるだけで、いちばんありふれた形になります。');
console.log('');
console.log('      ★ τ = τ0 · exp(E/kT)        （活性化過程。E は障壁の高さ）');
console.log('');
console.log('  このとき ln τ = ln τ0 + E/kT ── ★ ln τ は E の一次関数です。');
console.log('  だから：');
console.log('');
console.log('      ★★ E が一様分布 ⟺ ln τ が一様分布 ⟺ g(τ) ∝ 1/τ');
console.log('');
console.log('  ヤコビアンで書けば g(τ)dτ = D(E)dE、dE = kT·dτ/τ なので');
console.log('');
console.log('      ★ g(τ) = kT·D(E)/τ ── D が平らなら、そのまま 1/τ。');
console.log('');
console.log('  ★ べき乗分布を用意する必要はありません。');
console.log('    ★ 「指数の中身が平らである」だけでいい ── これはごく普通の状況です。');
console.log('');

const kB = 8.617333262e-5;      // eV/K
function decadesOfTau(E1,E2,T){ return (E2-E1)/(kB*T*Math.LN10); }

{
  console.log('  どれくらい桁が稼げるか（τ0 = 1e−13 s、室温 T = 300 K）：');
  console.log('');
  console.log('  ' + pad('障壁 E の幅 [eV]',20) + pad('τ の広がり [桁]',18) + pad('τ_max',14) + '');
  console.log('  ' + '-'.repeat(62));
  const T=300, tau0=1e-13;
  [[0.3,0.4],[0.3,0.6],[0.3,1.0],[0.3,1.3]].forEach(function(p){
    const dec = decadesOfTau(p[0],p[1],T);
    const tmax = tau0*Math.exp(p[1]/(kB*T));
    console.log('  ' + pad(f(p[0],2)+' 〜 '+f(p[1],2)+'（幅 '+f(p[1]-p[0],2)+'）',20)
      + pad(f(dec,2),18) + pad(e(tmax,2)+' s',14));
  });
  console.log('');
  console.log('  ★ kT ln10 = ' + f(kB*300*Math.LN10,5) + ' eV が「1 桁あたりの障壁」。');
  console.log('  ★★ 障壁の幅 0.36 eV で、時定数は 6 桁 に広がります ── 安すぎます。');
  console.log('    ★ 1/f が 6 桁 続くのに必要なのは、0.36 eV ぶんの障壁のばらつきだけ。');
  console.log('');
  const tmax1 = 1e-13*Math.exp(1.0/(kB*300));
  console.log('  そして E_max = 1.0 eV なら τ_max = ' + e(tmax1,3) + ' s = ' + f(tmax1/3600,2) + ' 時間');
  console.log('  ── ★ 1/f はここで折れるはず（' + e(1/(2*Math.PI*tmax1),2) + ' Hz 以下）。');
  console.log('    実験で 1e−6 Hz まで折れないなら、障壁は 1.3 eV 以上まで伸びている。');
}

// ------------------------------------------------------------------
hr('4. 数値で ── 一様な障壁分布から 1/f を作る');

function spectrumFromBarriers(w, E1, E2, T, tau0, slopeDecades, N){
  // D(E) ∝ exp(c E) で、E1→E2 の間に slopeDecades 桁 変化する
  const c = slopeDecades*Math.LN10/(E2-E1);
  const h = (E2-E1)/N;
  let s = 0, norm = 0;
  for(let i=0;i<N;i++){
    const E = E1 + (i+0.5)*h;
    const D = Math.exp(c*(E-E1));
    const tau = tau0*Math.exp(E/(kB*T));
    s += D * 2*tau/(1+w*w*tau*tau) * h;
    norm += D*h;
  }
  return s/norm;
}

{
  const T=300, tau0=1e-13, E1=0.3, E2=1.0;
  console.log('  障壁が E ∈ [0.3, 1.0] eV に分布（τ0=1e−13 s、T=300 K）。');
  console.log('  ★ D(E) を平らにした場合と、10 倍・1000 倍 傾けた場合を比べます。');
  console.log('');
  console.log('  ' + pad('D(E) の変化',16) + pad('f = 1 Hz 近傍の傾き β',24) + pad('予言 β = 1 + kT·dlnD/dE',26));
  console.log('  ' + '-'.repeat(70));
  [0,1,3].forEach(function(dec){
    const w1 = 2*Math.PI*0.3, w2 = 2*Math.PI*3;
    const S1 = spectrumFromBarriers(w1,E1,E2,T,tau0,dec,400000);
    const S2 = spectrumFromBarriers(w2,E1,E2,T,tau0,dec,400000);
    const beta = -Math.log(S2/S1)/Math.log(w2/w1);
    const c = dec*Math.LN10/(E2-E1);
    const pred = 1 + kB*T*c;
    console.log('  ' + pad((dec===0?'平ら':Math.pow(10,dec)+' 倍')+'',16)
      + rpad(f(beta,5),10) + pad('',14) + rpad(f(pred,5),10));
  });
  console.log('');
  console.log('  ★★ これが 1/f の「1」が動かない理由です：');
  console.log('');
  console.log('      ★ β − 1 = kT · dlnD/dE');
  console.log('              = （D が変化する桁数）/（τ が広がる桁数）');
  console.log('');
  const decTau = decadesOfTau(E1,E2,T);
  console.log('  この例では τ が ' + f(decTau,1) + ' 桁 広がるので：');
  console.log('      D が 10 倍（1 桁）変化しても β − 1 = 1/' + f(decTau,1) + ' = ' + f(1/decTau,3));
  console.log('      D が 1000 倍（3 桁）でも β − 1 = ' + f(3/decTau,3));
  console.log('');
  console.log('  ★★ 分母が大きいので、β は勝手に 1 の近くに釘づけされます。');
  console.log('    ★ 実測の 1/f が β = 0.8〜1.4 に散らばるのは、まさにこの比です。');
  console.log('    ── ★ 1/f は微調整の結果ではありません。★ 避けるほうが難しい。');
}

// ------------------------------------------------------------------
hr('5. 実例① α 崩壊 ── 指数写像のいちばん極端な例');

console.log('  第 19 回で「崩壊定数は虚数の周波数」と見ました。');
console.log('  ★ その崩壊定数こそ、指数写像の教科書的な例です。');
console.log('');
console.log('      ★ λ ∝ exp(−G)、G ＝ ガモフ因子 ∝ Z/√Q');
console.log('');
console.log('  Q 値（放出エネルギー）は「ふつうの量」で、せいぜい 2 倍しか違いません。');
console.log('  ところが半減期は ──');
console.log('');

const alphas = [
  // 核種, 娘核の Z, Q [MeV], 半減期 [s]
  ['232Th', 88, 4.0816, 1.405e10*3.1557e7],
  ['238U ', 90, 4.2700, 4.468e9 *3.1557e7],
  ['235U ', 90, 4.6780, 7.040e8 *3.1557e7],
  ['230Th', 88, 4.7700, 7.538e4 *3.1557e7],
  ['226Ra', 86, 4.8710, 1600    *3.1557e7],
  ['222Rn', 84, 5.5900, 3.8235*86400],
  ['218Po', 82, 6.1150, 3.098*60],
  ['214Po', 82, 7.8340, 164.3e-6],
  ['212Po', 82, 8.9540, 0.299e-6]
];

{
  console.log('  ' + pad('核種',8) + rpad('Q [MeV]',10) + rpad('半減期 [s]',14)
            + rpad('log10 T½',11) + rpad('Z/√Q',9) + rpad('直線の予言',12));
  console.log('  ' + '-'.repeat(66));
  // 最小二乗 log10 T = a·(Z/√Q) + b
  let sx=0, sy=0, sxx=0, sxy=0, n=alphas.length;
  alphas.forEach(function(r){
    const x = r[1]/Math.sqrt(r[2]);
    const y = Math.log10(r[3]);
    sx+=x; sy+=y; sxx+=x*x; sxy+=x*y;
  });
  const a = (n*sxy - sx*sy)/(n*sxx - sx*sx);
  const b = (sy - a*sx)/n;
  let ssr=0, sst=0; const ybar = sy/n;
  alphas.forEach(function(r){
    const x = r[1]/Math.sqrt(r[2]);
    const y = Math.log10(r[3]);
    const p = a*x+b;
    ssr += (y-p)*(y-p); sst += (y-ybar)*(y-ybar);
    console.log('  ' + pad(r[0],8) + rpad(f(r[2],4),10) + rpad(e(r[3],2),14)
      + rpad(f(y,3),11) + rpad(f(x,3),9) + rpad(f(p,3),12));
  });
  console.log('');
  console.log('      最小二乗: log10 T½ = ' + f(a,4) + '·(Z/√Q) ' + (b<0?'−':'+') + ' ' + f(Math.abs(b),3));
  console.log('      決定係数 R² = ' + f(1-ssr/sst,6) + '、残差の標準偏差 = ' + f(Math.sqrt(ssr/n),3) + ' 桁');
  console.log('');
  const qr = alphas[alphas.length-1][2]/alphas[0][2];
  const tr = Math.log10(alphas[0][3]/alphas[alphas.length-1][3]);
  console.log('  ★★ Q は ' + f(qr,2) + ' 倍 しか違わないのに、半減期は ' + f(tr,1) + ' 桁 違います。');
  console.log('    ★ これがガイガー＝ナタルの法則 ── ★ 指数写像そのものです。');
  console.log('');
  console.log('  ★ 第 19 回との接続：あそこでは「崩壊定数は虚数の周波数だから');
  console.log('    観測窓の壁が効かない」と書きました。本回ではもう一段 深く ──');
  console.log('    ★ 崩壊定数が宇宙年齢から μ 秒まで連続に埋まっているのは、');
  console.log('      ★ Q という「ふつうの量」が指数の中に入っているからです。');
}

// ------------------------------------------------------------------
hr('6. 実例② 離散スケール不変性 ── 第 13 回の梯子が戻ってくる');

console.log('  対数一様には、もう一つの作り方があります ── ★ 等比数列。');
console.log('');
console.log('      τ_n = τ0 · λ^n     （ln τ_n が等間隔）');
console.log('');
console.log('  これは「連続に一様」ではなく「離散的に一様」です。');
console.log('  ★ 第 13 回のエフィモフ状態（λ = e^(π/s0) = 22.69）がまさにこれ。');
console.log('  ★ 1/f は出るのか、出るならどう違うのか。');
console.log('');

function spectrumLadder(w, tau0, lam, nmin, nmax){
  let s=0;
  for(let n=nmin;n<=nmax;n++){
    const t = tau0*Math.pow(lam,n);
    s += 2*t/(1+w*w*t*t);
  }
  return s;
}

{
  // メリン再和で出る予言：相対リップル r = 2/cosh(π²/lnλ)（k=1 の項）
  function rippleDb(lam){
    const r = 2/Math.cosh(Math.PI*Math.PI/Math.log(lam));
    return 20*Math.log10((1+r)/(1-r));
  }
  console.log('  ' + pad('比 λ',12) + pad('1 桁あたりの段数',18) + pad('リップル [dB p-p]',20) + '予言 2/cosh(π²/lnλ)');
  console.log('  ' + '-'.repeat(76));
  [2, 3, 10, 22.69, 100].forEach(function(lam){
    // ω を 1 周期ぶん（λ 倍）走査してリップルを測る
    const tau0=1e-6, nmin=0, nmax=Math.ceil(12*Math.LN10/Math.log(lam));
    let mn=Infinity, mx=-Infinity;
    const K=2000;
    for(let i=0;i<K;i++){
      const w = 1.0*Math.pow(lam, i/K);
      const S = spectrumLadder(w,tau0,lam,nmin,nmax);
      const norm = S*w;                        // 1/f を割り落とす
      if(norm<mn) mn=norm; if(norm>mx) mx=norm;
    }
    const ripple = 20*Math.log10(mx/mn);
    console.log('  ' + pad(f(lam,2),12) + pad(f(1/Math.log10(lam),3),18)
      + rpad(f(ripple,5),9) + pad('',11) + rpad(f(rippleDb(lam),5),12));
  });
  console.log('');
  console.log('  ★ どの λ でも 1/f 自体は出ます（段数を増やせば必ず）。');
  console.log('  ★★ 違いは ★ 対数周期のリップル ── λ が大きいほど大きい。');
  console.log('    ★ しかも予言 2/cosh(π²/lnλ) と、λ ≤ 22.7 では 3 桁 で合います。');
  console.log('');
  console.log('  ★★ ここで予想が外れました。');
  console.log('    λ = 22.69（エフィモフ）のリップルは ' + f(rippleDb(22.69),2) + ' dB ──');
  console.log('    ★ 第 13 回の「対数周期性は見つけにくい」とは、逆の結論です。');
  console.log('');
  console.log('    ★ 第 13 回で消えていたのは ★ 虚数階フィルタのインパルス応答（e^(−βπ) で潰れる）。');
  console.log('    ★ 本回で残るのは ★ 離散した時定数の梯子がスペクトルに刻むリップル。');
  console.log('    ── ★ 「離散スケール不変性」と「虚数階」は、別の見え方をします。');
  console.log('');
  // 実測の 1/f がリップルなしに見えることから λ に上限がつく
  function lamForDb(target){
    let lo=1.0001, hi=1000;
    for(let i=0;i<200;i++){ const m=Math.sqrt(lo*hi); if(rippleDb(m)<target) lo=m; else hi=m; }
    return Math.sqrt(lo*hi);
  }
  console.log('  ★ これは ★ 検証可能な予言になります：');
  console.log('    実測の 1/f スペクトルが対数周期リップルを見せないなら、梯子の比は小さいはず。');
  console.log('');
  console.log('  ' + pad('リップルの検出限界',22) + '許される最大の λ');
  console.log('  ' + '-'.repeat(44));
  [1.0, 0.3, 0.1, 0.03].forEach(function(d){
    console.log('  ' + pad(f(d,2)+' dB 以下',22) + f(lamForDb(d),2));
  });
  console.log('');
  console.log('  ★★ 1/f が 0.1 dB の平坦さで測れているなら、時定数の梯子の比は ' + f(lamForDb(0.1),1) + ' 倍 以下。');
  console.log('    ── ★ つまり 1/f の背後にあるのは ★ 連続（密）な分布であって、');
  console.log('      ★ エフィモフ型の粗い梯子ではありません。★ 活性化過程（§3）と整合します。');
}

// ------------------------------------------------------------------
hr('7. 対照実験 ── 対数一様「でない」分布は何を出すか');

function spectrumLogNormal(w, lnTauMean, sigma, N){
  const lo = lnTauMean - 6*sigma, hi = lnTauMean + 6*sigma;
  const h = (hi-lo)/N;
  let s=0, norm=0;
  for(let i=0;i<N;i++){
    const lt = lo + (i+0.5)*h;
    const D = Math.exp(-(lt-lnTauMean)*(lt-lnTauMean)/(2*sigma*sigma));
    const t = Math.exp(lt);
    s += D*2*t/(1+w*w*t*t)*h;
    norm += D*h;
  }
  return s/norm;
}

{
  console.log('  ln τ がガウス分布（幅 σ 桁）の場合 ── ★ 対数一様の「なまった」版です。');
  console.log('  これは掛け算的なランダム過程（中心極限定理の対数版）から自然に出ます。');
  console.log('');
  console.log('  ★ 測るのは「傾き」ではありません ── ω τ=1 では単一のローレンツでも傾きは');
  console.log('    ちょうど −1 になってしまうからです（肩の点）。★ 測るべきは ★ 幅：');
  console.log('    ★ 傾きが −1 ± 0.1 に収まる ω の範囲が何桁あるか。');
  console.log('');
  function decadesOf1f(sigDec){
    const sigma = Math.max(sigDec,1e-6)*Math.LN10;
    const m = 0;
    let lo=null, hi=null;
    const step = 0.02;   // 桁
    for(let k=-8;k<=8;k+=step){
      const w1 = Math.pow(10,k-0.005), w2 = Math.pow(10,k+0.005);
      const S1 = spectrumLogNormal(w1,m,sigma,40000);
      const S2 = spectrumLogNormal(w2,m,sigma,40000);
      const sl = Math.log(S2/S1)/Math.log(w2/w1);
      if(sl>-1.1 && sl<-0.9){ if(lo===null) lo=k; hi=k; }
    }
    return (lo===null)?0:(hi-lo+step);
  }
  console.log('  ' + pad('σ [桁]',12) + pad('1/f に見える幅 [桁]',24) + '判定');
  console.log('  ' + '-'.repeat(58));
  [0.0000001, 0.5, 1, 2, 4].forEach(function(sigDec){
    const d = decadesOf1f(sigDec);
    let v;
    if(sigDec<0.01) v = '★ 単一 τ ── ほぼ幅なし（ローレンツの肩）';
    else if(d>1.5) v = '★ 1/f と区別がつかない';
    else v = '中間';
    console.log('  ' + pad(sigDec<0.01?'≈0':f(sigDec,1),12) + rpad(f(d,2),10) + pad('',14) + v);
  });
  console.log('');
  console.log('  ★ 単一の τ では、1/f に見える幅はわずか 0.10 桁 ── ★ 肩の一点だけです。');
  console.log('  ★★ σ を広げると、幅はほぼ σ に比例して伸びます。');
  console.log('  ── ★ 「対数一様」である必要はありません。★ 対数軸で広ければ、それで 1/f に見える。');
    console.log('    ★ 自然が用意すべきものは、さらに緩かった。');
}

// ------------------------------------------------------------------
hr('8. 仕組みを並べて採点する');

{
  const rows = [
    ['活性化（アレニウス）','τ=τ0 e^{E/kT}','★ 障壁 E が平らに散らばる','◎ ほぼ自動'],
    ['トンネル効果',        'τ∝e^{2κd}',    '★ 距離 d が平らに散らばる','◎ ほぼ自動'],
    ['α 崩壊（第 19 回）',  'λ∝e^{−G}',     '★ Q が並ぶだけ（24 桁）',   '◎ 実測'],
    ['掛け算的ランダム過程', '対数正規',      'σ が 2 桁 超で十分',        '○ 条件つき'],
    ['離散スケール不変性',   'τ_n=τ0 λ^n',  '★ 第 13 回の梯子',          '◎ ただし 3 dB のリップルが残る'],
    ['臨界現象',            'τ∝ξ^z',       '相関長が発散するとき',       '○ 微調整が要る'],
    ['一様なばね鎖（第 26 回）','τ が一定',   '── ',                      '× 整数階のまま']
  ];
  console.log('  ' + pad('仕組み',22) + pad('形',16) + pad('必要な条件',28) + '対数一様が出るか');
  console.log('  ' + '-'.repeat(92));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],22)+pad(r[1],16)+pad(r[2],28)+r[3]); });
  console.log('');
  console.log('  ★★ 上から三つは、どれも ★「指数の中に、ふつうの量が入っている」だけ。');
  console.log('    ★ べき乗分布を用意する必要も、臨界点に微調整する必要もありません。');
  console.log('');
  console.log('  ★ 対して臨界現象は、温度をぴったり Tc に合わせないとスケール不変になりません。');
  console.log('    ── ★ 自己組織化臨界（SOC）が注目されたのは、この微調整を');
  console.log('      系が勝手にやってくれる仕組みだったからです。');
  console.log('    ★ でも 1/f の説明としては、活性化のほうがずっと安上がりです。');
}

// ------------------------------------------------------------------
hr('9. まとめ');

{
  const rows = [
    ['対数一様 ⇒ 1/f',            '◎ 数値', '★ 傾き −1、πA/ω と 1e−6 で一致'],
    ['1/f には必ず上下の折れ点',   '◎ 数値', '帯の外は平ら'],
    ['指数写像で対数一様が出る',   '◎ 解析', '★ g(τ)=kT·D(E)/τ'],
    ['β − 1 ＝ 桁数の比',          '◎ 数値', '★ D が 1000 倍でも β−1=0.25'],
    ['α 崩壊は 24 桁（Q は 2 倍）','◎ 実測', '★ R²=0.99 の直線'],
    ['離散版は 3 dB のリップル',    '◎ 数値', '★ 実測の平坦さが λ<4.5 を課す'],
    ['幅 σ 桁 ⇒ 1/f が σ 桁',      '◎ 数値', '★ 単一 τ では幅ゼロ']
  ];
  console.log('  ' + pad('主張',30) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(84));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],30)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     1/f は微調整の結果ではなく、★ 避けるほうが難しい現象だった。');
  console.log('     速さが「ふつうの量の指数」で決まる系なら、勝手に対数一様になる。');
  console.log('     ── ★ 自然が用意していたのは、べき乗分布ではなく指数写像だった。');
  console.log('');
  console.log('  ★ そして第 26 回の扉が、ここで閉じます：');
  console.log('      第 26 回「分数階 ⇐ スケール不変な自由度」');
  console.log('      第 27 回「スケール不変な自由度 ⇐ 指数写像」');
  console.log('    ★★ 分数階の起源は、指数関数だった。');
}

console.log('');
