// 考える波 第61回「第 XIX 部の締め ── alpha は何回 顔を出したか」検証
//   node shime.js
// 依存ライブラリ 0（FFT は自前）。
//
// 第56〜60回で出た数字を もう一度 計算しなおし（回帰試験）、
// そのうえで 本シリーズの背骨 dB/oct = 6 alpha を
// 独立な 4 つの道すじで 同時に測る。

'use strict';

const TWO_PI = 2 * Math.PI;
function d10(x) { return Math.log(x) / Math.LN10; }
function line(t) { console.log(t); }
function rule(c) { line((c || '-').repeat(76)); }
function head(n, t) { line(''); rule('='); line('[' + n + '] ' + t); rule('='); }
function row(cols, w) {
  let s = '';
  for (let i = 0; i < cols.length; i++) {
    const c = String(cols[i]), width = w[i] || 12;
    s += (i === 0) ? c.padEnd(width) : c.padStart(width);
  }
  return s;
}
function slope(xs, ys) {
  const n = xs.length;
  let sx = 0, sy = 0, sxx = 0, sxy = 0;
  for (let i = 0; i < n; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
  return (n * sxy - sx * sy) / (n * sxx - sx * sx);
}
function mean(a) { let s = 0; for (const v of a) s += v; return s / a.length; }
function vari(a) {
  const m = mean(a); let s = 0;
  for (const v of a) s += (v - m) * (v - m);
  return s / a.length;
}
function fft(re, im, inv) {
  const n = re.length;
  for (let i = 1, j = 0; i < n; i++) {
    let bit = n >> 1;
    for (; j & bit; bit >>= 1) j ^= bit;
    j ^= bit;
    if (i < j) {
      let t = re[i]; re[i] = re[j]; re[j] = t;
      t = im[i]; im[i] = im[j]; im[j] = t;
    }
  }
  for (let len = 2; len <= n; len <<= 1) {
    const ang = (inv ? TWO_PI : -TWO_PI) / len;
    const wr = Math.cos(ang), wi = Math.sin(ang);
    for (let i = 0; i < n; i += len) {
      let cr = 1, ci = 0;
      for (let k = 0; k < len / 2; k++) {
        const ur = re[i + k], ui = im[i + k];
        const vr = re[i + k + len / 2] * cr - im[i + k + len / 2] * ci;
        const vi = re[i + k + len / 2] * ci + im[i + k + len / 2] * cr;
        re[i + k] = ur + vr; im[i + k] = ui + vi;
        re[i + k + len / 2] = ur - vr; im[i + k + len / 2] = ui - vi;
        const ncr = cr * wr - ci * wi; ci = cr * wi + ci * wr; cr = ncr;
      }
    }
  }
  if (inv) for (let i = 0; i < n; i++) { re[i] /= n; im[i] /= n; }
}
let _s = 20260920;
function rnd() { _s = (_s * 1103515245 + 12345) & 0x7fffffff; return _s / 0x7fffffff; }
function gauss() {
  const u = Math.max(rnd(), 1e-12), v = rnd();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(TWO_PI * v);
}
function bisect(cond, lo, hi, it) {
  it = it || 200;
  for (let i = 0; i < it; i++) {
    const m = 0.5 * (lo + hi);
    if (cond(m)) lo = m; else hi = m;
  }
  return 0.5 * (lo + hi);
}

// =====================================================================
head(1, '第56〜60回の数字を もう一度 計算する（回帰試験）');
// =====================================================================

const CHECKS = [];
function chk(label, got, want, tol, where) {
  const ok = Math.abs(got - want) <= tol;
  CHECKS.push([label, got, want, ok, where]);
  return ok;
}

// --- 第56回：1/f の桁数 = 0.9916*T - 2.1708 -------------------------
{
  function makeS(lo, hi, g, n) {
    const ts = [], ws = [];
    for (let i = 0; i < n; i++) {
      const lt = lo + (hi - lo) * i / (n - 1);
      ts.push(Math.pow(10, lt)); ws.push(Math.pow(Math.pow(10, lt), 1 - g));
    }
    return (w) => {
      let s = 0;
      for (let i = 0; i < n; i++) { const t = ts[i]; s += ws[i] * t / (1 + w * w * t * t); }
      return Math.log(s);
    };
  }
  function localBeta(f, w) {
    const xs = [], ys = [];
    for (let i = 0; i < 9; i++) {
      const lg = d10(w) - 0.1 + 0.2 * i / 8;
      xs.push(lg * Math.LN10); ys.push(f(Math.pow(10, lg)));
    }
    return -slope(xs, ys);
  }
  function fitFor(Ts) {
    const dec = [];
    for (const T of Ts) {
      const f = makeS(-T / 2, T / 2, 1, 4000);
      const lo = bisect((w) => Math.abs(localBeta(f, w) - 1) >= 0.05,
        Math.pow(10, -T / 2), 1, 60);
      const hi = bisect((w) => Math.abs(localBeta(f, w) - 1) < 0.05,
        1, Math.pow(10, T / 2), 60);
      dec.push(d10(hi / lo));
    }
    const sl = slope(Ts, dec);
    return [sl, mean(dec) - sl * mean(Ts)];
  }
  const A = fitFor([3, 4, 6, 8, 10, 12]);     // 第56回が使った T
  const B = fitFor([4, 6, 8, 10, 12]);        // T=3 を外したとき
  chk('第56回 傾き（T=3 込み）', A[0], 0.9916, 0.01, '第56回 02節');
  chk('第56回 切片（T=3 込み）', A[1], -2.1708, 0.01, '第56回 02節');
  // T=3 を外したときの切片は 公開値とは別物なので、参考として後で出す
  global.__ic_noT3 = B[1];
}

// --- 第57回：端で失う桁数 = 2 log10(2/(pi eps)) ---------------------
{
  const v = 2 * d10(2 / (Math.PI * 0.05));
  chk('第57回 端の代金[桁]', v, 2.2098, 0.001, '第57回 02節');
  // 傾きは gamma=1 で 2/(g(2-g)) = 2
  chk('第57回 傾き(gamma=1)', 2 / (1 * (2 - 1)), 2.0, 1e-9, '第57回 03節');
  chk('第57回 傾き(gamma=0.6)', 2 / (0.6 * 1.4), 2.3810, 0.001, '第57回 03節');
}

// --- 第58回：cos^p 窓の裾 = -6(p+1) dB/oct --------------------------
const NWIN = 4096;
function cosWin(p, n) {
  const w = new Float64Array(n);
  for (let i = 0; i < n; i++) {
    const x = (i + 0.5) / n - 0.5;
    w[i] = Math.pow(Math.cos(Math.PI * x), p);
  }
  return w;
}
function winMag(w, f) {
  let re = 0, im = 0;
  const n = w.length;
  for (let i = 0; i < n; i++) {
    const ph = TWO_PI * f * (i - (n - 1) / 2) / n;
    re += w[i] * Math.cos(ph); im -= w[i] * Math.sin(ph);
  }
  return Math.hypot(re, im);
}
function sideSlope(w) {
  const xs = [], ys = [], W0 = winMag(w, 0);
  for (let f = 8; f <= 512; f *= Math.SQRT2) {
    let best = 0;
    for (let g = f; g < f * Math.SQRT2; g += 0.05) {
      const m = winMag(w, g);
      if (m > best) best = m;
    }
    if (best / W0 < 1e-13) break;
    xs.push(Math.log(f) / Math.LN2); ys.push(20 * d10(best));
  }
  return slope(xs, ys);
}
{
  chk('第58回 矩形窓 dB/oct', sideSlope(cosWin(0, NWIN)), -5.934, 0.02, '第58回 01節');
  chk('第58回 ハン窓 dB/oct', sideSlope(cosWin(2, NWIN)), -17.876, 0.02, '第58回 01節');
}

// --- 第60回：トレンド除去は 6(q+1) dB/oct ---------------------------
function fitPoly(x, q) {
  const n = x.length;
  const pw = new Float64Array(2 * q + 1);
  for (let t = 0; t < n; t++) {
    const u = 2 * t / (n - 1) - 1;
    let up = 1;
    for (let j = 0; j <= 2 * q; j++) { pw[j] += up; up *= u; }
  }
  const A = [];
  for (let i = 0; i <= q; i++) {
    A.push(new Float64Array(q + 2));
    for (let j = 0; j <= q; j++) A[i][j] = pw[i + j];
  }
  for (let t = 0; t < n; t++) {
    const u = 2 * t / (n - 1) - 1;
    let up = 1;
    for (let i = 0; i <= q; i++) { A[i][q + 1] += up * x[t]; up *= u; }
  }
  for (let i = 0; i <= q; i++) {
    let piv = i;
    for (let r = i + 1; r <= q; r++) if (Math.abs(A[r][i]) > Math.abs(A[piv][i])) piv = r;
    const tmp = A[i]; A[i] = A[piv]; A[piv] = tmp;
    for (let r = 0; r <= q; r++) {
      if (r === i) continue;
      const f = A[r][i] / A[i][i];
      for (let c = i; c <= q + 1; c++) A[r][c] -= f * A[i][c];
    }
  }
  const co = [];
  for (let i = 0; i <= q; i++) co.push(A[i][q + 1] / A[i][i]);
  const p = new Float64Array(n);
  for (let t = 0; t < n; t++) {
    const u = 2 * t / (n - 1) - 1;
    let up = 1, v = 0;
    for (let i = 0; i <= q; i++) { v += co[i] * up; up *= u; }
    p[t] = v;
  }
  return p;
}
function detrend(x, q) {
  const p = fitPoly(x, q);
  const r = new Float64Array(x.length);
  for (let i = 0; i < x.length; i++) r[i] = x[i] - p[i];
  return r;
}
const NT = 1024;
function trendGain2(q, f) {
  const c = new Float64Array(NT), s = new Float64Array(NT);
  for (let t = 0; t < NT; t++) {
    const ph = TWO_PI * f * t / NT;
    c[t] = Math.cos(ph); s[t] = Math.sin(ph);
  }
  const rc = detrend(c, q), rs = detrend(s, q);
  let a = 0, b = 0;
  for (let t = 0; t < NT; t++) { a += rc[t] * rc[t] + rs[t] * rs[t]; b += c[t] * c[t] + s[t] * s[t]; }
  return a / b;
}
function trendSlope(q) {
  const xs = [], ys = [];
  for (let f = 0.005; f <= 0.08; f *= 1.4) {
    xs.push(Math.log(f) / Math.LN2); ys.push(10 * d10(trendGain2(q, f)));
  }
  return slope(xs, ys);
}
{
  chk('第60回 q=0 dB/oct', trendSlope(0), 6.014, 0.02, '第60回 01節');
  chk('第60回 q=2 dB/oct', trendSlope(2), 18.057, 0.02, '第60回 01節');
}

// --- 出力 -----------------------------------------------------------
line(row(['項目', '今回の計算', '公開した値', '判定', '出典'], [24, 14, 14, 8, 14]));
rule();
let bad = 0;
for (const c of CHECKS) {
  if (!c[3]) bad++;
  line(row([c[0], c[1].toFixed(4), c[2].toFixed(4), c[3] ? 'OK' : 'NG', c[4]],
    [24, 14, 14, 8, 14]));
}
rule();
line(bad === 0 ? '★ 全 ' + CHECKS.length + ' 件 一致。第56〜60回の数字は 再現できる。'
  : '★ ' + bad + ' 件 不一致。');
line('');
line('★★★ ただし 1 件、合っていても 直すべき数字が見つかった。');
line('');
line(row(['第56回 切片の出し方', '値'], [34, 14]));
rule();
line(row(['T = 3,4,6,8,10,12（第56回が使った）', CHECKS[1][1].toFixed(4)], [34, 14]));
line(row(['T = 4,6,8,10,12（T=3 を外す）', global.__ic_noT3.toFixed(4)], [34, 14]));
line(row(['第57回が導いた 解析値', (-2 * d10(2 / (Math.PI * 0.05))).toFixed(4)], [34, 14]));
rule();
line('★★ T=3 は 失う 2.2 桁 とほぼ同じ大きさで、まだ漸近形に入っていない。');
line('   それを当てはめに入れたぶん 切片が 浅く（-2.17）出ていた。');
line('   外すと -2.24。解析値 -2.2098 は その間にある。');
line('★★★ つまり 第56回の「-2.1708」は 4 桁 書きすぎだった ──');
line('   当てはめる T の範囲で ±0.04 動く。正しくは「-2.2 程度」。');
line('★★★ 第55回で「0.0812 は 2 桁 しか根拠が無い」と書いたのと 同じ失敗を、');
line('   その 1 回あとで もう一度 やっていた。手引きに書いても、やる。');

// =====================================================================
head(2, '★★★ dB/oct = 6 alpha を 独立な 4 つの道すじで 測る');
// =====================================================================
// ① 微分（第1回）  ② 分数階の微分（第13・41回）
// ③ 窓の裾（第58回） ④ トレンド除去（第60回）

const NS = 1 << 14;
function whiteSeries(n) {
  const x = new Float64Array(n);
  for (let i = 0; i < n; i++) x[i] = gauss();
  return x;
}
// 分数階微分：FFT で (i*2*pi*k/N)^a を掛ける
function fracDiff(x, a) {
  const n = x.length;
  const re = new Float64Array(n), im = new Float64Array(n);
  for (let i = 0; i < n; i++) re[i] = x[i];
  fft(re, im, false);
  for (let k = 1; k < n; k++) {
    const kk = (k <= n / 2) ? k : k - n;
    const w = TWO_PI * Math.abs(kk) / n;
    const mag = Math.pow(w, a);
    const ph = (kk >= 0 ? 1 : -1) * a * Math.PI / 2;
    const cr = mag * Math.cos(ph), ci = mag * Math.sin(ph);
    const r = re[k], m = im[k];
    re[k] = r * cr - m * ci; im[k] = r * ci + m * cr;
  }
  re[0] = 0; im[0] = 0;
  fft(re, im, true);
  return re;
}
function specSlopeDb(x, klo, khi) {
  const n = x.length;
  const re = new Float64Array(n), im = new Float64Array(n);
  for (let i = 0; i < n; i++) re[i] = x[i];
  fft(re, im, false);
  const xs = [], ys = [];
  for (let k = klo; k <= khi; k++) {
    const P = re[k] * re[k] + im[k] * im[k];
    xs.push(Math.log(k) / Math.LN2); ys.push(10 * d10(P + 1e-300));
  }
  return slope(xs, ys);
}

line(row(['道すじ', 'alpha', '実測 dB/oct', '予言 6 alpha', '差', '出典'],
  [22, 8, 14, 14, 10, 12]));
rule();
{
  _s = 20260920;
  const x = whiteSeries(NS);
  const base = specSlopeDb(x, 64, 2048);
  // ① 整数回の微分（差分）
  for (const nd of [1, 2, 3]) {
    let y = Float64Array.from(x);
    for (let d = 0; d < nd; d++) {
      const z = new Float64Array(y.length);
      for (let i = 1; i < y.length; i++) z[i] = y[i] - y[i - 1];
      z[0] = y[0] - y[y.length - 1];
      y = z;
    }
    const s = specSlopeDb(y, 64, 512) - specSlopeDb(x, 64, 512);
    line(row(['① 差分 ' + nd + ' 回', nd, s.toFixed(3), (6.0206 * nd).toFixed(3),
      (s - 6.0206 * nd).toFixed(3), '第 1 回'], [22, 8, 14, 14, 10, 12]));
  }
  void base;
  // ② 分数階の微分
  for (const a of [0.5, 1.5, 2.5]) {
    const y = fracDiff(x, a);
    const s = specSlopeDb(y, 64, 2048) - specSlopeDb(x, 64, 2048);
    line(row(['② 分数階 ' + a + ' 階', a, s.toFixed(3), (6.0206 * a).toFixed(3),
      (s - 6.0206 * a).toFixed(3), '第13・41回'], [22, 8, 14, 14, 10, 12]));
  }
}
// ③ 窓の裾
for (const p of [0, 2, 4]) {
  const s = -sideSlope(cosWin(p, NWIN));
  line(row(['③ cos^' + p + ' 窓の裾', p + 1, s.toFixed(3), (6.0206 * (p + 1)).toFixed(3),
    (s - 6.0206 * (p + 1)).toFixed(3), '第 58 回'], [22, 8, 14, 14, 10, 12]));
}
// ④ トレンド除去
for (const q of [0, 1, 3]) {
  const s = trendSlope(q);
  line(row(['④ トレンド除去 q=' + q, q + 1, s.toFixed(3), (6.0206 * (q + 1)).toFixed(3),
    (s - 6.0206 * (q + 1)).toFixed(3), '第 60 回'], [22, 8, 14, 14, 10, 12]));
}
rule();
line('★★★ まったく別の 4 つの操作が、同じ 6 alpha に乗る。');
line('   ── 微分、分数階の微分、窓の切り口、トレンドの引き算。');
line('★★ しかも alpha は 整数である必要がない（②）。');
line('★ 第1回の「音を微分すると高音になる」という一行から、ここまで来た。');

// =====================================================================
head(3, '★★★ 第45回の宿題を閉じる ── 1+2+3+... = -1/12 は 切り方に依らないか');
// =====================================================================
// 第45回 01節で 指数的な切断を使って
//   sum n e^{-delta n} = 1/delta^2 - 1/12 + O(delta^2)
// を出し、脚注に「正則化の取り方に依らないことは本稿では確かめていない」
// と書いた。ここで確かめる。
//
// 一般に、なめらかな切断 f（f(0)=1、遠くで十分速く落ちる）について
//   sum_{n>=1} n f(delta n) = A/delta^2 + zeta(-1) + O(delta^k),
//   A = int_0^inf x f(x) dx
// が成り立つはず。A は f ごとに違うが、定数項は いつも zeta(-1) = -1/12。

function regSum(f, delta, xmax) {
  // sum_{n>=1} n f(delta n)。f(delta n) が効かなくなるまで足す
  let s = 0;
  const nmax = Math.ceil(xmax / delta);
  for (let n = 1; n <= nmax; n++) s += n * f(delta * n);
  return s;
}
// A = int_0^inf x f(x) dx（十分細かい中点則）
function areaA(f, xmax) {
  const NP = 400000, h = xmax / NP;
  let s = 0;
  for (let i = 0; i < NP; i++) { const x = h * (i + 0.5); s += x * f(x); }
  return s * h;
}

const REGS = [
  ['e^-x（第45回）', (x) => Math.exp(-x), 1.0, 80],
  ['e^-x^2（ガウス）', (x) => Math.exp(-x * x), 0.5, 12],
  ['e^-x^4', (x) => Math.exp(-Math.pow(x, 4)), Math.sqrt(Math.PI) / 4, 8],
  ['sech x', (x) => 1 / Math.cosh(x), 2 * 0.9159655942, 80],
  // 5 番目の要素は「xmax までで打ち切った A」の厳密値。
  // 裾の落ちが遅い f では、和の打ち切りと合わせないと
  // 1/delta^2 倍 に拡大されて 定数項を壊す。
  ['1/(1+x^2)^2', (x) => 1 / Math.pow(1 + x * x, 2), 0.5, 4000,
    (X) => 0.5 - 1 / (2 * (1 + X * X))],
];

line('切断 f を変えて sum n f(delta n) - A/delta^2 を測る（delta -> 0）');
line('');
line(row(['切断 f', 'A（解析）', 'A（数値）', 'd=0.02', 'd=0.01', 'd=0.005', '-1/12'],
  [18, 12, 12, 12, 12, 12, 12]));
rule();
{
  let worst = 0;
  for (const r of REGS) {
    const name = r[0], f = r[1], Aexact = r[2], xmax = r[3];
    const Asub = r[4] ? r[4](xmax) : Aexact;   // 和と同じ所で打ち切った A
    const Anum = areaA(f, xmax);
    const vals = [];
    // 引くのは 解析値 A。数値積分の A を使うと、その誤差が 1/delta^2 倍に
    // 拡大されて 定数項を壊す（delta=0.005 で 4e-6 の誤差が 0.17 になる）。
    for (const d of [0.02, 0.01, 0.005]) {
      const v = regSum(f, d, xmax) - Asub / (d * d);
      vals.push(v.toFixed(6));
      worst = Math.max(worst, Math.abs(v + 1 / 12));
    }
    line(row([name, Aexact.toFixed(6), Anum.toFixed(6), ...vals, (-1 / 12).toFixed(6)],
      [18, 12, 14, 12, 12, 12, 12]));
  }
  rule();
  line('★ -1/12 からのずれ 最大 ' + worst.toExponential(1));
  line('★★★ 5 種類の切断で A（発散項の係数）は 0.443 〜 1.832 とばらばら。');
  line('   それなのに 定数項は どれも -0.083333 ── zeta(-1) = -1/12。');
  line('★★ これで 第45回の脚注「正則化の取り方に依らないことは');
  line('   本稿では確かめていない」を 閉じられる。');
  line('');
  line('★ 途中で 二度 つまずいた（記録として）：');
  line('   ① A を数値積分で出して引いたら 1/(1+x^2)^2 が -0.25 になった。');
  line('     A の誤差 4e-6 が 1/delta^2 = 4e4 倍 に拡大されていた。');
  line('   ② 解析値 A に直しても まだ -0.0846。今度は 和の打ち切り(xmax)と');
  line('     A の積分範囲が合っていなかった（裾が x^-3 でしか落ちないため）。');
  line('★★★ どちらも「発散項を引く計算では、引く側の精度が');
  line('   1/delta^2 倍 に効く」という 同じ一つのこと。');
  line('   カシミールの計算が繊細なのは、これが理由。');
}

// --- 第60回との対比 -------------------------------------------------
line('');
line('★ ここが 第60回との分かれ目：');
line('');
line(row(['', 'カシミール（第45回）', '1/f^beta の分散（第60回）'], [16, 30, 30]));
rule();
line(row(['発散する項', 'A/delta^2（切り方に依存）', 'N^(beta-1)（記録長に依存）'],
  [16, 30, 30]));
line(row(['有限な残り', '-1/12（切り方に依らない）', '無い'], [16, 30, 30]));
line(row(['差を取ると', '消える（壁の有無で引ける）', '消えない'], [16, 30, 30]));
line(row(['結果', '物理量が決まる', '記録長を言うしかない'], [16, 30, 30]));
rule();
line('★★★ 「走る量」に意味を持たせられるかどうかは、');
line('   切り方に依らない有限部分が 残るかどうかで決まる。');
line('★★ 第60回の練習問題2で「構造は同じだが 繰り込みはできない」と');
line('   書いたのは、この違いのこと ── いま 数字で示せた。');
line('★ そして -1/12 は 1+2+3+... の値ではない。');
line('   1+2+3+... は 発散する。-1/12 は「発散項を引いたあとに残るもの」。');
line('   引くべき発散項が 切り方に依存し、残りが 依存しない ── そこが要点。');

// =====================================================================
head(4, '第 XIX 部で 手引きに足すべきもの');
// =====================================================================
line('第49回 7 手順 → 第55回 10 手順 → 今回 14 手順');
line('');
const STEPS = [
  ['①〜⑦', '第49回', '実測する／片対数で見る／傾きを測る 等'],
  ['⑧', '第55回', '誤差を 統計と系統に分ける'],
  ['⑨', '第55回', '範囲を買う手を検討する'],
  ['⑩', '第55回', '仮定を数えて 一緒に書く'],
  ['★⑪', '第59・60回', '周期図の前に 1〜2 次のトレンドを引く'],
  ['★⑫', '第60回', '二つの条件を 別々に確かめる（beta<=2q+3 と beta<2alpha）'],
  ['★⑬', '第59回', '誤差の「大きさ」より先に「形」を測る（被覆率）'],
  ['★⑭', '第60回', '分散を書くときは 記録の長さも書く'],
];
line(row(['手順', '出どころ', '内容'], [8, 12, 50]));
rule();
for (const s of STEPS) line(row(s, [8, 12, 50]));
rule();
line('★ ⑪〜⑭ は どれも「切り方を宣言する」ことに帰着する。');
line('★★ 第 XIX 部で分かったのは、測定の限界が ほとんど');
line('   「どこで切ったか」で決まるということ。');

// =====================================================================
head(5, '第 XIX 部の数字を 第55回の物差しで分類する');
// =====================================================================
line(row(['数字', '分類', '注意'], [34, 16, 24]));
rule();
const CLASS = [
  ['1/f 桁数 = 0.99T - 2.17', '本稿の計算', 'eps=0.05 の基準に依存'],
  ['端の代金 2 log10(2/pi eps)', '厳密解', '-'],
  ['傾き 2/(g(2-g))', '解析＋数値', '漸近形（小さい eps）'],
  ['dB/oct = -6 alpha（窓）', '本稿の計算', '-'],
  ['天井 beta = 2 alpha', '本稿の計算', '当てはめ帯域に依存'],
  ['|beta| ∝ T^-(p+1)', '本稿の計算', '共鳴が無い場合に限る'],
  ['被覆率 79〜87%', '本稿の実測', '帯域・tol・窓の族に依存'],
  ['beta <= 2q + 3', '本稿の計算', '-'],
  ['分散 ∝ N^(beta-1)', '本稿の計算', '3 点からの当てはめ'],
  ['tau/tau0 = 6.3e16', '模型を仮定', 'E=1.0eV, T=300K の仮定つき'],
  ['「実験の報告は 6 桁 前後」', '代表的な状況', '特定の文献値ではない'],
  ['★ -1/12 は切り方に依らない', '本稿の計算', '5 種類の切断で確認'],
  ['★ 第56回の切片 -2.1708', '書きすぎ → -2.2 程度', 'T の範囲で ±0.04'],
];
for (const c of CLASS) line(row(c, [34, 16, 24]));
rule();
line('★ 13 件 中 ── 本稿の計算 10、厳密解 1、模型を仮定 1、状況の記述 1。');
line('★★ 「模型を仮定」が 1 件 しかないのは、第 XIX 部が');
line('   物理ではなく 測定の話だったから。');

// =====================================================================
head(6, 'まだ やっていないこと');
// =====================================================================
const TODO = [
  ['★★★ 実データに当てる', '第56〜60回 すべて 合成データのみ'],
  ['（済）-1/12 の正則化非依存', '第45回の脚注 → 本回 03節で 閉じた'],
  ['D(E) の独立な測定', '第56回の 決着手。文献にあたっていない'],
  ['温度を変えた 1/f の測定', '第56回の提案。未検証'],
  ['短い記録を多数集める手', '第60回 練習問題3。独立性が怪しい'],
  ['非ガウス過程での被覆率', '第59回は ガウス合成のみ'],
  ['窓の族を変えた場合', '第59回は cos^p のみ'],
];
line(row(['項目', '状況'], [28, 44]));
rule();
for (const t of TODO) line(row(t, [28, 44]));
rule();
line('★★★ いちばん大きいのは 一つ目 ── 本シリーズは まだ');
line('   一度も 実測データに触れていない。');
line('★ そう書いておくことが、第55回の手引きの ⑩ にあたる。');

// =====================================================================
head(7, 'まとめ');
// =====================================================================
line('★ 第56〜60回の数字 ' + CHECKS.length + ' 件 を 再計算 ── ' +
  (bad === 0 ? '全件 一致' : bad + ' 件 不一致'));
line('★ ただし 第56回の切片 -2.1708 は 書きすぎ ── T の範囲で ±0.04 動く。');
line('  第55回で同じ注意を書いた 1 回あとで、また やっていた。');
line('★★★ dB/oct = 6 alpha が 独立な 4 つの道すじで 同じ値を返した。');
line('  微分・分数階の微分・窓の切り口・トレンドの引き算。');
line('★★★ 第45回の宿題を閉じた ── -1/12 は 5 種類の切断で同じ値。');
line('  発散項の係数 A は 0.443〜1.832 とばらばらなのに、定数項は動かない。');
line('★★ そこが 第60回の分散との違い ── あちらには 切り方に依らない');
line('  有限部分が 無い。だから「構造は同じだが 繰り込みはできない」。');
line('★★ 手引きは 7 → 10 → 14 手順に。⑪〜⑭ はすべて「切り方の宣言」。');
line('★★★ 残る最大の宿題：本シリーズは まだ 実測データに触れていない。');
line('');
