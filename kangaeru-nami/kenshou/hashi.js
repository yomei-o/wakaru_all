// 考える波 第57回「端で何が起きるか」検証
//   node hashi.js
// 依存ライブラリ 0。
//
// 第56回で「重ね合わせの端で 2.2 桁 失う」という数字が出た。
// その 2.2 はどこから来るのか。そして第16回の分散、第44回のバンド端、
// 第51回の窓の端は、同じ「端」なのか。
//
// 結論（本稿の主張）：
//   ★ どの端も「最低次の補正項」で決まり、
//      失う桁数 = (1/n) log10(1/eps) + const
//      n は最低次の補正のべき。
//   ★ 第56回の 2.2 桁 は n=1 の端が両側にある場合の解析値
//      2 log10(2/(pi eps)) = 2.2098（eps=0.05）に一致する。

'use strict';

const L10 = Math.LN10;
function d10(x) { return Math.log(x) / L10; }

function line(t) { console.log(t); }
function rule(c) { line((c || '-').repeat(72)); }
function head(n, t) { line(''); rule('='); line('[' + n + '] ' + t); rule('='); }

// 表示用：列をそろえる
function row(cols, w) {
  let s = '';
  for (let i = 0; i < cols.length; i++) {
    const c = String(cols[i]);
    const width = w[i] || 12;
    s += (i === 0) ? c.padEnd(width) : c.padStart(width);
  }
  return s;
}

// 最小二乗の傾き
function slope(xs, ys) {
  const n = xs.length;
  let sx = 0, sy = 0, sxx = 0, sxy = 0;
  for (let i = 0; i < n; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
  return (n * sxy - sx * sy) / (n * sxx - sx * sx);
}

// 単調な条件 cond(x) が true → false に変わる x を二分法で
function bisect(cond, lo, hi, iter) {
  iter = iter || 200;
  for (let i = 0; i < iter; i++) {
    const m = 0.5 * (lo + hi);
    if (cond(m)) lo = m; else hi = m;
  }
  return 0.5 * (lo + hi);
}

const EPS = [0.2, 0.1, 0.05, 0.02, 0.01, 0.005];
// 傾きは漸近形に入った小さい eps だけで測る（大きい eps では補正の高次項が残る）
const EPSFIT = [0.002, 0.001, 5e-4, 2e-4, 1e-4];

// =====================================================================
head(1, 'ローレンツ 1 個の「曲がりの幅」 ── 端はどこから始まるか');
// =====================================================================
// S(w) = tau/(1+w^2 tau^2)。tau=1 とする。
// log-log の傾き： dlnS/dlnw = -2x^2/(1+x^2),  x = w tau
//   平ら（傾き 0 から eps 以内）： 2x^2/(1+x^2) < eps  →  x < sqrt(eps/(2-eps))
//   -2 から eps 以内            ： 2/(1+x^2)   < eps  →  x > sqrt(2/eps - 1)
// 曲がりの幅 = log10( sqrt(2/eps-1) / sqrt(eps/(2-eps)) )  ≈ log10(2/eps)

function lorSlope(x) { return -2 * x * x / (1 + x * x); }

line('S = tau/(1+w^2tau^2) の log-log 傾きが 0 → -2 に変わる幅');
line('');
line(row(['eps', 'x_flat', 'x_steep', '幅[桁]', 'log10(2/eps)', '差'], [10, 14, 14, 12, 14, 12]));
rule();
{
  const xs = [], ys = [];
  for (const eps of EPS) {
    const xf = bisect((x) => Math.abs(lorSlope(x)) < eps, 1e-12, 1e12);
    const xs2 = bisect((x) => Math.abs(lorSlope(x) + 2) >= eps, 1e-12, 1e12);
    const w = d10(xs2 / xf);
    const pred = d10(2 / eps);
    line(row([eps, xf.toFixed(6), xs2.toFixed(4), w.toFixed(4), pred.toFixed(4),
      (w - pred).toExponential(1)], [10, 14, 14, 12, 14, 12]));
  }
  for (const eps of EPSFIT) {
    const xf = bisect((x) => Math.abs(lorSlope(x)) < eps, 1e-12, 1e12);
    const xs2 = bisect((x) => Math.abs(lorSlope(x) + 2) >= eps, 1e-12, 1e12);
    xs.push(d10(1 / eps)); ys.push(d10(xs2 / xf));
  }
  rule();
  line('★ 曲がりの幅 = log10(2/eps) ── 解析値と一致。');
  line('★ 幅 vs log10(1/eps) の傾き = ' + slope(xs, ys).toFixed(6) + '（予言 1、eps<=0.002 で測定）');
  line('   ＝ 両側とも最低次の補正が x^2（n=2）で、各側 1/2 桁ずつ、合計 1。');
}

// =====================================================================
head(2, '重ね合わせの端 ── 第56回の「2.2 桁」の正体');
// =====================================================================
// gamma=1 のとき厳密に積分できる：
//   S(w) = [ atan(w tmax) - atan(w tmin) ] / w
//   beta(w) = 1 - w A'/A,  A = atan(w tmax)-atan(w tmin),
//             A' = tmax/(1+w^2 tmax^2) - tmin/(1+w^2 tmin^2)

function betaExact(w, tmin, tmax) {
  const A = Math.atan(w * tmax) - Math.atan(w * tmin);
  const Ap = tmax / (1 + w * w * tmax * tmax) - tmin / (1 + w * w * tmin * tmin);
  return 1 - w * Ap / A;
}

line('gamma=1 の厳密解  S(w) = [atan(w tmax) - atan(w tmin)]/w');
line('');
{
  const T = 12, tmin = 1e-6, tmax = 1e6;
  line(row(['eps', '下端 w_lo', '上端 w_hi', '1/f[桁]', '失った[桁]', '2log10(2/pi eps)'],
    [10, 14, 14, 12, 12, 18]));
  rule();
  const xs = [], ys = [];
  for (const eps of EPS) {
    // 中央 w=1 から外へ
    const wlo = bisect((w) => Math.abs(betaExact(w, tmin, tmax) - 1) >= eps, 1 / tmax * 1e-3, 1);
    const whi = bisect((w) => Math.abs(betaExact(w, tmin, tmax) - 1) < eps, 1, 1 / tmin * 1e3);
    const dec = d10(whi / wlo);
    const lost = T - dec;
    const pred = 2 * d10(2 / (Math.PI * eps));
    line(row([eps, wlo.toExponential(4), whi.toExponential(4), dec.toFixed(4),
      lost.toFixed(4), pred.toFixed(4)], [10, 14, 14, 12, 12, 18]));
  }
  for (const eps of EPSFIT) {
    const wlo = bisect((w) => Math.abs(betaExact(w, tmin, tmax) - 1) >= eps, 1 / tmax * 1e-3, 1);
    const whi = bisect((w) => Math.abs(betaExact(w, tmin, tmax) - 1) < eps, 1, 1 / tmin * 1e3);
    xs.push(d10(1 / eps)); ys.push(T - d10(whi / wlo));
  }
  rule();
  line('★ 失う桁数 vs log10(1/eps) の傾き = ' + slope(xs, ys).toFixed(6) + '（予言 2、eps<=0.002 で測定）');
  line('   ＝ 両側とも最低次の補正が 1/x（n=1）で、各側 1 桁ずつ、合計 2。');
  line('');
  line('★★ eps=0.05 のとき 解析値 2 log10(2/(pi*0.05)) = '
    + (2 * d10(2 / (Math.PI * 0.05))).toFixed(4) + ' 桁');
  line('   第56回の実測（T=8 で 2.255、T=12 で 2.249）と一致。');
  line('   ── あの 2.2 は、両端の atan の裾 2/(pi x) から来ていた。');
}

// =====================================================================
head(3, 'gamma を変えても同じか');
// =====================================================================
// 一般の gamma では閉じた形にならないので数値積分（ln tau で Simpson）。
//   S(w)    = int tau^{1-gamma}/(1+w^2tau^2) dtau
//   beta(w) = int 2w^2 tau^{3-gamma}/(1+w^2tau^2)^2 dtau / S(w)

function simpsonLog(f, lo, hi, n) {
  // int f(tau) dtau を u=ln tau で Simpson（n は偶数）
  const a = Math.log(lo), b = Math.log(hi), h = (b - a) / n;
  let s = 0;
  for (let i = 0; i <= n; i++) {
    const u = a + h * i, t = Math.exp(u);
    const wgt = (i === 0 || i === n) ? 1 : (i % 2 ? 4 : 2);
    s += wgt * f(t) * t;
  }
  return s * h / 3;
}

function betaNum(w, g, tmin, tmax, n) {
  const den = simpsonLog((t) => Math.pow(t, 1 - g) / (1 + w * w * t * t), tmin, tmax, n);
  const num = simpsonLog((t) => 2 * w * w * Math.pow(t, 3 - g) /
    Math.pow(1 + w * w * t * t, 2), tmin, tmax, n);
  return num / den;
}

// 端の漸近形（解析）：
//   低域側 ─ tau^max で切ったことの効き目は (w tmax)^{-gamma}   → n = gamma
//   高域側 ─ tau^min で切ったことの効き目は (w tmin)^{2-gamma}  → n = 2-gamma
//     （tau -> 1/tau の裏返しで gamma -> 2-gamma になるため）
//   よって 失う桁数の傾き = 1/gamma + 1/(2-gamma) = 2/(gamma(2-gamma))
//   これは gamma=1 で最小値 2 をとる。

const EPSFIT3 = [0.01, 0.005, 0.002, 0.001];

{
  const tmin = 1e-12, tmax = 1e12, T = 24, N = 20000;
  line(row(['gamma', 'beta(中央)', '予言 2-g', 'eps=.05 で失う', '傾き(実測)', '予言 2/(g(2-g))'],
    [8, 12, 10, 16, 12, 16]));
  rule();
  for (const g of [0.6, 0.8, 1.0, 1.2, 1.4]) {
    const b0 = betaNum(1, g, tmin, tmax, N);
    const target = 2 - g;
    const xs = [], ys = [];
    let lost05 = 0;
    for (const eps of EPS) {
      const wlo = bisect((w) => Math.abs(betaNum(w, g, tmin, tmax, 3000) - target) >= eps,
        1e-15, 1, 60);
      const whi = bisect((w) => Math.abs(betaNum(w, g, tmin, tmax, 3000) - target) < eps,
        1, 1e15, 60);
      if (eps === 0.05) lost05 = T - d10(whi / wlo);
    }
    for (const eps of EPSFIT3) {
      const wlo = bisect((w) => Math.abs(betaNum(w, g, tmin, tmax, 3000) - target) >= eps,
        1e-15, 1, 60);
      const whi = bisect((w) => Math.abs(betaNum(w, g, tmin, tmax, 3000) - target) < eps,
        1, 1e15, 60);
      xs.push(d10(1 / eps)); ys.push(T - d10(whi / wlo));
    }
    const pred = 2 / (g * (2 - g));
    line(row([g, b0.toFixed(6), target.toFixed(3), lost05.toFixed(4),
      slope(xs, ys).toFixed(4), pred.toFixed(4)], [8, 12, 10, 16, 12, 16]));
  }
  rule();
  line('★★★ 傾きは 2 ではなかった ── gamma に依存して 2/(gamma(2-gamma))。');
  line('★★ そしてこれは gamma=1、つまり ちょうど 1/f のとき 最小値 2 をとる。');
  line('   ── 1/f は「端がいちばん安い」スペクトルでもある。');
}

// =====================================================================
head(4, '別の端 ── 第16回・第44回の「分散の端」');
// =====================================================================
// 離散化した弦（第16回）：  w(k) = (2c/a) sin(ka/2)
// 直線 w=ck からのずれ： sin(x)/x = 1 - x^2/6 + ...   x = ka/2
//   |1 - sin x/x| < eps  →  x ~ sqrt(6 eps)     ← べき（n=2）

line('離散弦の分散 w = (2c/a) sin(ka/2)。直線からのずれが eps 以内の範囲');
line('');
line(row(['eps', 'x_max', 'sqrt(6eps)', '差', 'log10 x_max'], [10, 14, 14, 12, 14]));
rule();
{
  const xs = [], ys = [];
  for (const eps of EPS) {
    const xm = bisect((x) => Math.abs(1 - Math.sin(x) / x) < eps, 1e-9, 3.14);
    const pred = Math.sqrt(6 * eps);
    line(row([eps, xm.toFixed(6), pred.toFixed(6), (xm - pred).toExponential(1),
      d10(xm).toFixed(4)], [10, 14, 14, 12, 14]));
    xs.push(d10(1 / eps)); ys.push(-d10(xm));
  }
  for (const eps of EPSFIT) {
    const xm = bisect((x) => Math.abs(1 - Math.sin(x) / x) < eps, 1e-9, 3.14);
    xs.push(d10(1 / eps)); ys.push(-d10(xm));
  }
  rule();
  line('★ 失う桁数 vs log10(1/eps) の傾き = ' + slope(xs, ys).toFixed(6)
    + '（予言 1/2）');
  line('★★ 失う桁数は (1/2) log10(1/eps) ── 重ね合わせの端（1 桁/桁）の 半分。');
}

// =====================================================================
head(5, '第51回の「窓の端」');
// =====================================================================
// 窓当てはめの偏り。対称な窓＋対称な曲率では偏りが消える（第51回 04節）。
// 3 次項 d*u^3 が残るとき、半幅 h の中央窓での最小二乗傾きの偏りは
//   bias = d * <u^4>/<u^2> = d * (3/5) h^2      ← べき（n=2）

function fitBiasCubic(h, d, npts) {
  const us = [], ys = [];
  for (let i = 0; i < npts; i++) {
    const u = -h + 2 * h * i / (npts - 1);
    us.push(u); ys.push(d * u * u * u);   // 真の傾きは u=0 で 0
  }
  return slope(us, ys);
}

line('真の曲線 y = d u^3（中央での真の傾き 0）を半幅 h の窓で当てはめる');
line('');
line(row(['h', '実測の偏り', '(3/5) d h^2', '比'], [10, 16, 16, 12]));
rule();
{
  const d = 1.0;
  for (const h of [0.1, 0.2, 0.5, 1.0, 2.0]) {
    const b = fitBiasCubic(h, d, 4001);
    const pred = 0.6 * d * h * h;
    line(row([h, b.toFixed(8), pred.toFixed(8), (b / pred).toFixed(6)], [10, 16, 16, 12]));
  }
  rule();
  line('★ 偏り ∝ h^2。よって偏りを eps 以内に収める窓幅は h ∝ sqrt(eps)。');

  const xs = [], ys = [];
  for (const eps of EPS) {
    const h = Math.sqrt(eps / 0.6);
    xs.push(d10(1 / eps)); ys.push(-d10(h));
  }
  line('★ 失う桁数 vs log10(1/eps) の傾き = ' + slope(xs, ys).toFixed(6)
    + '（予言 1/2）── 第44回の端と同じ族。');
}

// =====================================================================
head(6, '★★★ 一般化 ── 端は「最低次の補正のべき」で決まる');
// =====================================================================
// 観測量が  Q(x) = Q0 (1 + A x^n + ...)  と書けるとき、
//   |A x^n| < eps  →  x < (eps/A)^{1/n}
//   失う桁数 = (1/n) log10(1/eps) + (1/n) log10 A

line('Q(x) = 1 + A x^n。|Q-1| < eps となる x の上限の、log10(1/eps) に対する傾き');
line('');
line(row(['n', 'A', '実測の傾き', '予言 1/n', '差'], [8, 8, 14, 12, 12]));
rule();
{
  for (const n of [1, 2, 3, 4, 6]) {
    for (const A of [1, 0.1]) {
      const xs = [], ys = [];
      for (const eps of EPS) {
        const xm = bisect((x) => A * Math.pow(x, n) < eps, 1e-12, 1e6);
        xs.push(d10(1 / eps)); ys.push(-d10(xm));
      }
      const sl = slope(xs, ys);
      line(row([n, A, sl.toFixed(6), (1 / n).toFixed(6),
        (sl - 1 / n).toExponential(1)], [8, 8, 14, 12, 12]));
    }
  }
  rule();
  line('★★★ 失う桁数 = (1/n) log10(1/eps) + const。');
  line('   A（補正の大きさ）は切片だけを動かし、傾きは n だけで決まる。');
}

// =====================================================================
head(7, 'シリーズに出てきた「端」を分類する');
// =====================================================================

line(row(['端', '最低次の補正', 'n', '桁/桁', '出典'], [24, 16, 5, 9, 14]));
rule();
const CAT = [
  ['重ね合わせの下端', '(w tmax)^-g', 1, 1.0, '第 2, 56 回'],
  ['重ね合わせの上端', '(w tmin)^(2-g)', 1, 1.0, '第 2, 56 回'],
  ['ローレンツ 1 個の端', 'x^2', 2, 0.5, '第 5, 48 回'],
  ['離散弦の分散', 'x^2/6', 2, 0.5, '第 16 回'],
  ['バンド端', '(k-kc)^2', 2, 0.5, '第 44 回'],
  ['窓当てはめ', '(3/5)h^2', 2, 0.5, '第 51 回'],
  ['周期の分解能', '1/N', 1, 1.0, '第 51, 53 回'],
];
for (const c of CAT) line(row([c[0], c[1], c[2], c[3].toFixed(1), c[4]], [24, 16, 5, 9, 14]));
rule();
line('（重ね合わせの n は gamma=1 の場合。一般には 低域 n=gamma、高域 n=2-gamma）');
line('');
line('★ 端は「種類」ではなく、n という連続の量で並んでいた。');
line('★★ n=1（重ね合わせの 1/f・分解能）は eps を 10 倍 きびしくすると 1 桁 失う。');
line('★★ n=2（テイラー展開・窓）は 10 倍 で 0.5 桁 しか失わない ── 端としては安い。');
line('★★★ ただし n が小さいほど「その端の外側の情報が遠くまで効く」ことでもある。');

// =====================================================================
head(8, '第53回との関係 ── どちらも log だが、係数が違う');
// =====================================================================

line(row(['買い方', '桁数の伸び方', '10 倍 の投資で', '出典'], [22, 22, 16, 12]));
rule();
const BUY = [
  ['観測時間 T', 'log10 T', '+1.0 桁', '第 53 回'],
  ['標本数 N（精度）', '-(1/2)log10 N', '精度 3.2 倍', '第 53 回'],
  ['許容 eps（n=1 の端）', 'log10(1/eps)', '-1.0 桁', '本回'],
  ['許容 eps（n=2 の端）', '(1/2)log10(1/eps)', '-0.5 桁', '本回'],
  ['1/f の両端（g=1）', '2 log10(1/eps)', '-2.0 桁', '本回'],
  ['温度（活性化）', 'E/kT を直接', '桁違い', '第 56 回'],
];
for (const b of BUY) line(row(b, [22, 22, 16, 12]));
rule();
line('★ 「範囲は対数でしか買えない」（第53回）は端でも成り立つ。');
line('★★ ただし係数が 1/n ── 端の種類を知らないと、必要な精度を'
  + ' 2 倍 見誤る。');

// =====================================================================
head(9, 'まとめ');
// =====================================================================

const SUM = [
  ['第56回の 2.2 桁 の解析値', (2 * d10(2 / (Math.PI * 0.05))).toFixed(4) + ' 桁', '厳密解'],
  ['ローレンツ 1 個の曲がりの幅', 'log10(2/eps)', '厳密解'],
  ['重ね合わせの端の n', 'gamma と 2-gamma', '本稿の計算'],
  ['テイラー展開の端の n', '2', '本稿の計算'],
  ['★ 一般法則', '失う桁 = (1/n)log10(1/eps)+c', '本稿の主張'],
  ['★ 重ね合わせの傾き', '2/(g(2-g))、g=1 で最小', '本稿の計算'],
  ['実データでの検証', '未着手', '合成のみ'],
];
line(row(['項目', '値', '根拠'], [30, 28, 14]));
rule();
for (const s of SUM) line(row(s, [30, 28, 14]));
rule();
line('');
line('★★★ 端はどれも「最低次の補正項」だった。');
line('    失う桁数 = (1/n) log10(1/eps) + const。');
line('    第56回の 2.2 桁 は n=1 が両側にある場合の 2 log10(2/(pi eps)) = 2.2098。');
line('★★★ そして 2/(gamma(2-gamma)) は gamma=1 で最小 ──');
line('    1/f は「端の代金がいちばん安い」スペクトルでもあった。');
line('');
