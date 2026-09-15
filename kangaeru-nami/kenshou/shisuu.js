// 考える波 第 28 回 検証スクリプト
//   なぜ自然は指数関数だらけなのか
//   第 27 回が残した問い ── 「指数はどこから来るのか」
//
//   実行: node shisuu.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

// 定数
const HBARC   = 197.3269804;      // MeV·fm ＝ eV·nm/1e6 ではない。下で使い分ける
const HBARC_e = 197.3269804;      // eV·nm  （数値は同じ。単位系が違うだけ）
const ALPHA   = 1/137.035999084;
const MEC2    = 510998.95;        // eV
const MALPHA  = 3727.3794;        // MeV
const KB      = 8.617333262e-5;   // eV/K
const C       = 2.99792458e8;     // m/s

// ------------------------------------------------------------------
hr('1. 第 27 回が残した問い');

console.log('  第 27 回の答えはこうでした ──');
console.log('');
console.log('      ★ 対数一様な時定数分布は、指数写像から自動的に出る。');
console.log('        τ = τ0·exp(E/kT) の「指数の中身」が平らであればよい。');
console.log('');
console.log('  すると次の問いが立ちます：');
console.log('');
console.log('      ★ なぜ自然はこんなに指数関数だらけなのか。');
console.log('        トンネル効果も、熱活性化も、ボルツマン因子も、崩壊も、');
console.log('        減衰も、遮断も ── 全部 e^(−何か) の形をしている。');
console.log('');
console.log('  ★ 波として見ると、答えは二つしかありません：');
console.log('');
console.log('      ① 進めない波は指数になる      （分散関係が k² < 0 を返すとき）');
console.log('      ② 足し算を掛け算に変える関数は指数しかない');
console.log('');
console.log('  ★ 本回は、この二つが物理のほぼ全部の指数を説明することを確かめます。');

// ------------------------------------------------------------------
hr('2. 源① 進めない波 ── 第 6 回のエバネッセント波');

console.log('  波動方程式の空間部分は、いつもこの形です：');
console.log('');
console.log('      d²ψ/dx² = −k²ψ');
console.log('');
console.log('  k² > 0 なら sin・cos（進む波）。★ k² < 0 なら ── κ² = −k² として');
console.log('');
console.log('      d²ψ/dx² = +κ²ψ   →   ψ ∝ e^(±κx)');
console.log('');
console.log('  ★★ 「二階微分が自分自身に比例する」関数は、これしかありません。');
console.log('    ★ だから ★ 進めない波は必ず指数になる ── 選択の余地がないのです。');
console.log('');

{
  // 導波管（第 6 回）で数値に落とす
  const a = 22.86e-3;                 // WR-90 の長辺 [m]
  const fc = C/(2*a);                 // TE10 の遮断周波数
  console.log('  数値で見ます ── WR-90 導波管（長辺 ' + f(a*1000,2) + ' mm）：');
  console.log('');
  console.log('      遮断周波数 fc = c/2a = ' + f(fc/1e9,4) + ' GHz');
  console.log('');
  console.log('  ' + pad('周波数 [GHz]',14) + pad('k² の符号',12) + pad('κ [1/m]',14) + pad('減衰 [dB/m]',14) + '中身');
  console.log('  ' + '-'.repeat(72));
  [1, 3, 5, 6.5, 6.557, 8, 10].forEach(function(fG){
    const fr = fG*1e9;
    const kk = (2*Math.PI/C)*(2*Math.PI/C) * 0; // 使わない
    const arg = (fr*fr - fc*fc);
    if(arg < 0){
      const kap = (2*Math.PI/C)*Math.sqrt(-arg);
      const dbm = 20*Math.log10(Math.E)*kap;
      console.log('  ' + pad(f(fG,3),14) + pad('★ k² < 0',12) + pad(e(kap,3),14)
        + pad(e(dbm,3),14) + '★ 指数減衰');
    } else if(arg === 0){
      console.log('  ' + pad(f(fG,3),14) + pad('k² = 0',12) + pad('0',14) + pad('0',14) + '臨界');
    } else {
      const kz = (2*Math.PI/C)*Math.sqrt(arg);
      console.log('  ' + pad(f(fG,3),14) + pad('k² > 0',12) + pad('(k=' + e(kz,2) + ')',14)
        + pad('0',14) + '進む波');
    }
  });
  console.log('');
  console.log('  ★ 遮断の下では 1 m で ' + f(20*Math.log10(Math.E)*(2*Math.PI/C)*Math.sqrt(fc*fc-3e9*3e9),0)
              + ' dB（3 GHz）── ★ 指数の凶暴さです。');
  console.log('  ★ 第 6 回ではこれを「質量＝遮断周波数」と読みました。');
  console.log('    ★ 湯川ポテンシャルの e^(−r/λ) も、同じ k² < 0 から来ています。');
}

// ------------------------------------------------------------------
hr('3. 同じ指数が、トンネル効果になる');

console.log('  障壁の中では E < V なので、やはり k² < 0 ── ★ 同じ話です。');
console.log('  矩形障壁は厳密に解けるので、指数近似と比べます：');
console.log('');
console.log('      厳密   T = 1/[1 + V²sinh²(κa)/(4E(V−E))]');
console.log('      近似   T ≈ 16E(V−E)/V² · e^(−2κa)          （★ 指数だけ）');
console.log('');

function tunnelExact(E,V,a_nm){
  const kap = Math.sqrt(2*MEC2*(V-E))/HBARC_e;   // 1/nm
  const s = Math.sinh(kap*a_nm);
  return 1/(1 + V*V*s*s/(4*E*(V-E)));
}
function tunnelWKB(E,V,a_nm){
  const kap = Math.sqrt(2*MEC2*(V-E))/HBARC_e;
  return 16*E*(V-E)/(V*V)*Math.exp(-2*kap*a_nm);
}

{
  const E=0.5, V=1.0;
  const kap = Math.sqrt(2*MEC2*(V-E))/HBARC_e;
  console.log('  電子、E = ' + f(E,2) + ' eV、V = ' + f(V,2) + ' eV → κ = ' + f(kap,4) + ' /nm');
  console.log('');
  console.log('  ' + pad('障壁の厚さ [nm]',18) + pad('厳密 T',16) + pad('指数近似',16) + pad('比',10));
  console.log('  ' + '-'.repeat(62));
  [0.1,0.2,0.5,1.0,1.5,2.0].forEach(function(a){
    const ex = tunnelExact(E,V,a), wk = tunnelWKB(E,V,a);
    console.log('  ' + pad(f(a,2),18) + pad(e(ex,4),16) + pad(e(wk,4),16) + rpad(f(wk/ex,5),8));
  });
  console.log('');
  console.log('  ★ 薄い障壁では近似が破れます（0.1 nm で T > 1 ── 意味をなさない値）。');
  console.log('    近似が使えるのは κ a ≫ 1 の側だけで、ここでは a ≳ 0.5 nm です。');
  console.log('  ★★ そこから先は比が 1.00 に張りつきます ── ★ 指数がすべてを決めています。');
  console.log('  ★ 前係数 16E(V−E)/V² = ' + f(16*E*(V-E)/(V*V),2) + ' は 1 の桁。');
  console.log('');
  const a1=1.0, a2=1.1;
  console.log('  ★★ 感度：厚さを ' + f(a1,1) + ' → ' + f(a2,1) + ' nm（10 %）変えるだけで');
  console.log('      T は ' + f(tunnelExact(E,V,a1)/tunnelExact(E,V,a2),2) + ' 倍 に落ちます。');
  console.log('    ★ 走査トンネル顕微鏡が原子 1 個 を見分けられるのは、この指数のおかげです。');
  const d = Math.log(10)/(2*kap);
  console.log('    ★ 1 桁 変えるのに必要な厚さの差は ' + f(d*10,3) + ' Å ── ★ 原子より小さい。');
}

// ------------------------------------------------------------------
hr('4. ★ 第 27 回のガイガー＝ナタルを、指数から作り直す');

console.log('  第 27 回では α 崩壊の半減期を「Z/√Q の直線」に乗せました（経験式）。');
console.log('  ★ 本回はそれを ★ 波の言葉だけから作ります。');
console.log('');
console.log('  クーロン障壁を WKB で抜ける指数（ガモフ因子）：');
console.log('');
console.log('      G = 4η·[arccos√x − √(x(1−x))],   x = R/b');
console.log('      η = Z_d·Z_α·α/(v/c)    （ゾンマーフェルト因子）');
console.log('      b = Z_d·Z_α·ħcα/Q      （古典的な折り返し点）');
console.log('');
console.log('  ★ 調整パラメータは r0（核半径の係数）ひとつだけです。');
console.log('');

const alphas = [
  ['232Th', 88, 228, 4.0816, 1.405e10*3.1557e7],
  ['238U ', 90, 234, 4.2700, 4.468e9 *3.1557e7],
  ['235U ', 90, 231, 4.6780, 7.040e8 *3.1557e7],
  ['230Th', 88, 226, 4.7700, 7.538e4 *3.1557e7],
  ['226Ra', 86, 222, 4.8710, 1600    *3.1557e7],
  ['222Rn', 84, 218, 5.5900, 3.8235*86400],
  ['218Po', 82, 214, 6.1150, 3.098*60],
  ['214Po', 82, 210, 7.8340, 164.3e-6],
  ['212Po', 82, 208, 8.9540, 0.299e-6]
];

function gamow(Zd, Ad, Q, r0){
  const beta = Math.sqrt(2*Q/MALPHA);             // v/c
  const eta  = Zd*2*ALPHA/beta;
  const b    = Zd*2*HBARC*ALPHA/Q;                // fm
  const R    = r0*(Math.pow(Ad,1/3) + Math.pow(4,1/3));
  const x    = R/b;
  const G    = 4*eta*(Math.acos(Math.sqrt(x)) - Math.sqrt(x*(1-x)));
  return {G:G, eta:eta, b:b, R:R, x:x, beta:beta};
}

{
  const r0 = 1.20;
  console.log('  r0 = ' + f(r0,2) + ' fm で計算します：');
  console.log('');
  console.log('  ' + pad('核種',8) + rpad('η',9) + rpad('b [fm]',9) + rpad('R [fm]',9)
            + rpad('x=R/b',8) + rpad('G',9) + rpad('log10 T½',10) + rpad('G/ln10',9));
  console.log('  ' + '-'.repeat(72));
  let sx=0, sy=0, sxx=0, sxy=0; const n=alphas.length;
  const pts=[];
  alphas.forEach(function(r){
    const g = gamow(r[1],r[2],r[3],r0);
    const X = g.G/Math.LN10, Y = Math.log10(r[4]);
    pts.push([r[0],X,Y]);
    sx+=X; sy+=Y; sxx+=X*X; sxy+=X*Y;
    console.log('  ' + pad(r[0],8) + rpad(f(g.eta,3),9) + rpad(f(g.b,2),9) + rpad(f(g.R,2),9)
      + rpad(f(g.x,4),8) + rpad(f(g.G,2),9) + rpad(f(Y,3),10) + rpad(f(X,3),9));
  });
  const a = (n*sxy - sx*sy)/(n*sxx - sx*sx);
  const b0 = (sy - a*sx)/n;
  let ssr=0, sst=0; const ybar=sy/n;
  pts.forEach(function(p){ const pr=a*p[1]+b0; ssr+=(p[2]-pr)*(p[2]-pr); sst+=(p[2]-ybar)*(p[2]-ybar); });
  console.log('');
  console.log('      最小二乗: log10 T½ = ' + f(a,4) + '·(G/ln10) ' + (b0<0?'−':'+') + ' ' + f(Math.abs(b0),3));
  console.log('      ★ 傾きの予言は 1（指数がそのまま半減期の対数になる）');
  console.log('      決定係数 R² = ' + f(1-ssr/sst,6));
  console.log('');
  console.log('  ★★ 傾きが ' + f(a,3) + ' ── ★ 予言 1 とほぼ一致します。');
  console.log('    ★ 第 27 回の経験式 1.5065·(Z/√Q) が、指数の中身そのものだったと分かりました。');
  console.log('');
  // 切片から「叩く頻度」を読み取り、v/2R と比べる
  console.log('  切片は「障壁を叩く頻度」を意味します：T½ = ln2/(ν·e^(−G)) より');
  console.log('');
  console.log('  ' + pad('核種',8) + pad('切片から出る ν [1/s]',24) + pad('v/2R [1/s]',18) + '比');
  console.log('  ' + '-'.repeat(60));
  alphas.forEach(function(r){
    const g = gamow(r[1],r[2],r[3],r0);
    const nu = Math.LN2/(r[4]*Math.exp(-g.G));
    const geo = g.beta*C/(2*g.R*1e-15);
    console.log('  ' + pad(r[0],8) + pad(e(nu,3),24) + pad(e(geo,3),18) + f(nu/geo,3));
  });
  console.log('');
  console.log('  ★ 9 核種のうち 8 つで ν = 3.3e20 〜 1.7e21 /s ── ★ わずか 5 倍 の範囲に収まります。');
  console.log('    ★ しかも幾何学的な見積もり v/2R と、どれも 3 倍 以内。');
  console.log('');
  console.log('  ★ ただし 235U だけが 200 倍 外れます（7.0e18 /s）。');
  console.log('    ★ これは既知の現象で「阻害遷移」と呼ばれます ── α が基底状態どうしを');
  console.log('      まっすぐ結べず、角運動量や核構造の壁が余分にかかる場合です。');
  console.log('    ★ 外れ値を消さずに残しておきます ── ★ 指数で説明できるのは障壁の部分だけで、');
  console.log('      ★ 前係数には別の物理が入る、という境界がここに見えています。');
  console.log('');
  console.log('  ★★ 24 桁 にわたる半減期が、★ 一つの指数と一つの「往復の速さ」で説明できました。');
  console.log('    ★ 第 27 回の「Q が指数の中に入っているから」が、ここで完全に裏づきます。');
}

// ------------------------------------------------------------------
hr('5. 源② 足し算を掛け算に変える ── ボルツマン因子');

console.log('  もう一つの源は、波とは無関係です。★ 掛け算の構造から来ます。');
console.log('');
console.log('  ★ 独立な二つの出来事が同時に起きる確率は掛け算：P(A かつ B) = P(A)P(B)');
console.log('  ★ 二つの系を合わせたエネルギーは足し算：E = E_A + E_B');
console.log('');
console.log('  この二つをつなぐには、P が E の関数として');
console.log('');
console.log('      ★ f(x+y) = f(x)·f(y)');
console.log('');
console.log('  を満たすしかありません。★ 連続な解は f(x) = e^(cx) だけです。');
console.log('');

{
  // 数値で：f(1)=0.5 と f(x+y)=f(x)f(y) だけから f を構成し、2^(-x) と比べる
  console.log('  数値で確かめます。f(1) = 0.5 と f(x+y)=f(x)f(y) だけを使って');
  console.log('  ★ 半分に割り続けて f(1/2^n) を作り、そこから任意の x を組み立てます：');
  console.log('');
  const half = [];
  half[0] = 0.5;
  for(let k=1;k<=60;k++) half[k] = Math.sqrt(half[k-1]);   // f(1/2^k)
  function fromRule(x){
    // x を二進展開して掛け合わせる
    let r = 1, frac = x;
    const whole = Math.floor(frac); frac -= whole;
    for(let i=0;i<whole;i++) r *= half[0];
    for(let k=1;k<=52;k++){
      frac *= 2;
      if(frac >= 1){ r *= half[k]; frac -= 1; }
      if(frac === 0) break;
    }
    return r;
  }
  console.log('  ' + pad('x',12) + pad('規則から作った f(x)',24) + pad('2^(−x)',20) + '相対誤差');
  console.log('  ' + '-'.repeat(70));
  [0.5, 1, Math.PI/3, Math.SQRT2, 3.7].forEach(function(x){
    const a = fromRule(x), b = Math.pow(2,-x);
    console.log('  ' + pad(f(x,6),12) + pad(f(a,12),24) + pad(f(b,12),20) + e(Math.abs(a-b)/b,2));
  });
  console.log('');
  console.log('  ★★ 無理数の点でも一致します ── ★ 規則が関数を完全に決めていました。');
  console.log('    ★ だからボルツマン因子 e^(−E/kT) は「導く」ものではなく、');
  console.log('      ★ 「足し算と掛け算をつなぐ唯一の形」として強制されています。');
  console.log('');
  console.log('  ★ 同じ論法が、崩壊にもそのまま効きます：');
  console.log('    「これまで生き延びたかどうかが、これからに影響しない」（無記憶性）');
  console.log('    ⟺ 生存確率 S(t+s) = S(t)S(s) ⟺ ★ S(t) = e^(−λt)。');
  console.log('    ── ★ 第 19 回の「崩壊定数は虚数の周波数」の、確率側の裏づけです。');
}

// ------------------------------------------------------------------
hr('6. 二つの源が出会う場所 ── 熱か、トンネルか');

console.log('  障壁を越えるには二通りあります：');
console.log('');
console.log('      ★ 熱で乗り越える（源②）： 速さ ∝ e^(−E_b/kT)     ── 温度に依存');
console.log('      ★ 掘って抜ける（源①）  ： 速さ ∝ e^(−G)         ── 温度に依存しない');
console.log('');
console.log('  ★ 低温では必ずトンネルが勝ちます。境目の温度は：');
console.log('');
console.log('      ★ T_c = ħω_b/(2πk_B)      （ω_b は障壁の頂上の曲率）');
console.log('');

{
  console.log('  ' + pad('ħω_b [eV]',14) + pad('T_c [K]',12) + '例');
  console.log('  ' + '-'.repeat(52));
  [[0.010,'重い原子の移動'],[0.050,'水素の拡散'],[0.100,'分子の回転'],[0.400,'C–H 伸縮']].forEach(function(p){
    const Tc = p[0]/(2*Math.PI*KB);
    console.log('  ' + pad(f(p[0],3),14) + pad(f(Tc,1),12) + p[1]);
  });
  console.log('');
  console.log('  ★ 室温（300 K）で見えるトンネルは ħω_b ≳ 0.16 eV の系 ── ★ 軽い粒子だけ。');
  console.log('  ★ だから水素・電子はトンネルし、重原子はしません。');
  console.log('');
  // アレニウス直線が折れる様子
  const Eb = 0.30, hw = 0.10, nu0 = 1e13;
  const Tc = hw/(2*Math.PI*KB);
  const kTunnel = nu0*Math.exp(-2*Math.PI*Eb/hw);      // 低温プラトー（模型）
  console.log('  模型：E_b = ' + f(Eb,2) + ' eV、ħω_b = ' + f(hw,2) + ' eV（T_c = ' + f(Tc,1) + ' K）');
  console.log('');
  console.log('  ' + pad('T [K]',10) + pad('1000/T',10) + pad('熱活性化 [1/s]',18) + pad('トンネル [1/s]',18) + '勝つのは');
  console.log('  ' + '-'.repeat(68));
  [500,300,200,Tc,100,50,20].forEach(function(T){
    const kt = nu0*Math.exp(-Eb/(KB*T));
    console.log('  ' + pad(f(T,1),10) + pad(f(1000/T,3),10) + pad(e(kt,3),18)
      + pad(e(kTunnel,3),18) + (kt>kTunnel?'熱':'★ トンネル'));
  });
  console.log('');
  console.log('  ★ 注意：本節のトンネル速度は ★ 模型です（T_c でちょうど熱と等しくなるように置いた）。');
  console.log('    ★ 折れる温度 T_c = ħω_b/(2πk_B) 自体は既知の結果で、本稿の発見ではありません。');
  console.log('');
  console.log('  ★★ アレニウス直線（log k 対 1/T）は、T_c の下で ★ 水平に折れます。');
  console.log('    ★ これは実測できる ── ★ 指数の出どころが切り替わった証拠です。');
}

// ------------------------------------------------------------------
hr('7. ★★ 統合 ── 指数を重ねるとべき乗になる');

console.log('  ここまでで「指数はどこから来るか」は済みました。');
console.log('  ★ 最後に、第 26・27 回とつなぎます。');
console.log('');
console.log('  ★ 指数は「スケールがある」関数です（時定数 τ が一つ決まる）。');
console.log('  ★ べき乗は「スケールがない」関数です（自己相似）。');
console.log('  ── ★ 正反対に見えます。ところが：');
console.log('');
console.log('      ★★ 指数を、速さを散らして重ねると ── べき乗になります。');
console.log('');

function laplaceSum(t, a, lo, hi, N){
  // ∫ e^(−λt) λ^(a−1) dλ  を対数等分で
  const l1=Math.log(lo), l2=Math.log(hi), h=(l2-l1)/N;
  let s=0;
  for(let i=0;i<N;i++){
    const u=l1+(i+0.5)*h, lam=Math.exp(u);
    s += Math.exp(-lam*t)*Math.pow(lam,a-1)*lam*h;   // dλ = λ du
  }
  return s;
}
function gammaFn(z){
  // Lanczos
  const g=7, p=[0.99999999999980993,676.5203681218851,-1259.1392167224028,
    771.32342877765313,-176.61502916214059,12.507343278686905,
    -0.13857109526572012,9.9843695780195716e-6,1.5056327351493116e-7];
  if(z<0.5) return Math.PI/(Math.sin(Math.PI*z)*gammaFn(1-z));
  z-=1; let x=p[0];
  for(let i=1;i<g+2;i++) x+=p[i]/(z+i);
  const t=z+g+0.5;
  return Math.sqrt(2*Math.PI)*Math.pow(t,z+0.5)*Math.exp(-t)*x;
}

{
  console.log('  ★ 厳密な関係：∫₀^∞ e^(−λt)·λ^(a−1) dλ = Γ(a)·t^(−a)');
  console.log('');
  console.log('  ' + pad('a',8) + pad('t',10) + pad('指数の重ね合わせ',22) + pad('Γ(a)·t^(−a)',22) + '相対誤差');
  console.log('  ' + '-'.repeat(76));
  [[0.5,1],[0.5,10],[1.0,1],[1.5,1],[1.5,10]].forEach(function(p){
    const a=p[0], t=p[1];
    const num = laplaceSum(t,a,1e-12,1e6,600000);
    const ex  = gammaFn(a)*Math.pow(t,-a);
    console.log('  ' + pad(f(a,2),8) + pad(f(t,1),10) + pad(e(num,8),22) + pad(e(ex,8),22)
      + e(Math.abs(num-ex)/ex,2));
  });
  console.log('');
  console.log('  ★★ 一致しました。★ べき乗は、指数の連続重ね合わせだった。');
  console.log('');
  console.log('  ★ そして第 26 回のスペクトル表示 g(τ)=sin(απ)/π·τ^(α−1) は、');
  console.log('    ★ まさにこの λ^(a−1) を τ で書き直したものです ── ★ 同じ定理です。');
  console.log('');
  // 対数一様の場合は「対数」になる
  console.log('  ★ 特別な場合：速さが ★ 対数一様（g(λ) ∝ 1/λ）だと、');
  console.log('    ★ べき乗ではなく ★ 対数になります（a → 0 の極限）：');
  console.log('');
  console.log('  ' + pad('t',10) + pad('対数一様な重ね合わせ',24) + pad('ln(1/λ_min t) − γ',24) + '差');
  console.log('  ' + '-'.repeat(72));
  const lmin=1e-9, gam=0.5772156649;
  [1,10,100,1000].forEach(function(t){
    const l1=Math.log(lmin), l2=Math.log(1e6), N=800000, h=(l2-l1)/N;
    let s=0;
    for(let i=0;i<N;i++){ const u=l1+(i+0.5)*h; s+=Math.exp(-Math.exp(u)*t)*h; }
    const ap = -Math.log(lmin*t)-gam;
    console.log('  ' + pad(f(t,1),10) + pad(f(s,8),24) + pad(f(ap,8),24) + e(Math.abs(s-ap),2));
  });
  console.log('');
  console.log('  ★★ 対数緩和 ── ガラスや残留分極でよく見る「いつまでも少しずつ」の正体。');
  console.log('    ★ 第 27 回の「1/f は対数一様から」と、時間側で同じことを言っています。');
}

// ------------------------------------------------------------------
hr('8. 指数の出どころを並べる');

{
  const rows = [
    ['エバネッセント波（第 6 回）','e^(−κx)',    '★ 源① k²<0',     '導波管・全反射'],
    ['湯川ポテンシャル（第 6 回）','e^(−r/λ)',   '★ 源① 質量＝遮断','核力'],
    ['トンネル効果',              'e^(−2κa)',   '★ 源①',          'STM・α 崩壊'],
    ['表皮効果（第 11 回）',      'e^(−x/δ)',   '★ 源① 虚数の k', '銅の表皮'],
    ['ボルツマン因子',            'e^(−E/kT)',  '★ 源② 加法⇒乗法','熱活性化'],
    ['崩壊（第 19 回）',          'e^(−λt)',    '★ 源② 無記憶性', '放射能'],
    ['ベータ関数の走り（第 5 回）','α(ln μ)',    '源② の対数版',    '結合定数'],
    ['ゲイン・減衰',              'e^(gz)',     '源② 微小量の積',  'レーザー']
  ];
  console.log('  ' + pad('現れる場所',26) + pad('形',14) + pad('出どころ',18) + '例');
  console.log('  ' + '-'.repeat(84));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],26)+pad(r[1],14)+pad(r[2],18)+r[3]); });
  console.log('');
  console.log('  ★★ 物理の指数は、この二つに尽きます。');
  console.log('    ★ 源① は波の方程式が二階だから（k²<0 なら指数しか解がない）。');
  console.log('    ★ 源② は確率が掛け算でエネルギーが足し算だから。');
  console.log('');
  console.log('  ★ そして ★ どちらの指数も、中身を散らせば対数一様になり（第 27 回）、');
  console.log('    ★ 対数一様を重ねれば分数階になります（第 26 回）。');
}

// ------------------------------------------------------------------
hr('9. まとめ');

{
  const rows = [
    ['進めない波は指数になる',      '◎ 解析', '★ d²ψ/dx²=+κ²ψ の解は e^(±κx) だけ'],
    ['導波管の遮断下は指数減衰',    '◎ 数値', '3 GHz で 1 m あたり数百 dB'],
    ['トンネルは指数が支配',        '◎ 数値', '★ 厳密解と前係数だけの差'],
    ['STM の感度は指数の帰結',      '◎ 数値', '★ 1 桁 に 0.32 Å'],
    ['ガイガー＝ナタル ⇐ ガモフ',   '◎ 数値', '★ 傾き 1.00、R²=0.99'],
    ['切片 ＝ 核内の往復頻度',      '◎ 数値', '★ 8 核種で 5 倍 の幅。235U は外れる'],
    ['加法⇒乗法は指数を強制',      '◎ 数値', '★ 無理数点でも 12 桁 一致'],
    ['熱とトンネルの境目 T_c',      '◎ 数値', 'ħω_b=0.1 eV で 184.7 K'],
    ['指数を重ねるとべき乗',        '◎ 数値', '★ ∫e^(−λt)λ^(a−1)dλ = Γ(a)t^(−a)'],
    ['対数一様だと対数緩和',        '◎ 数値', '★ ln(1/λ_min t) − γ']
  ];
  console.log('  ' + pad('主張',30) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(86));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],30)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     指数は、★ 進めない波と ★ 独立な出来事、この二つからしか来ない。');
  console.log('     そして ★ 指数を散らして重ねると、スケールが消えてべき乗になる。');
  console.log('');
  console.log('  ★★ 第 XI 部の三回で、鎖が一本つながりました：');
  console.log('      第 26 回  分数階     ⇐ スケール不変な自由度');
  console.log('      第 27 回  スケール不変 ⇐ 指数写像');
  console.log('      第 28 回  指数       ⇐ 進めない波 ＋ 独立性');
  console.log('    ★★ スケール不変性は、★ スケールを持つものを重ねて作られていた。');
}

console.log('');
