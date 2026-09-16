// 考える波 第 39 回：ホログラフィーを波として見る
//   余分な次元 ＝ 対数スケール軸（第 22 回のウェーブレット平面）
//   AdS の Δ = d/2 ± sqrt(d^2/4 + m^2 L^2) と
//   第 13 回の s = 1/2 ± sqrt(1/4 - lambda) は同じ二次方程式
//
//   node horo.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

// ---- ランチョスのガンマ関数（負の引数も反射公式で） ----
const LG = [676.5203681218851, -1259.1392167224028, 771.32342877765313,
  -176.61502916214059, 12.507343278686905, -0.13857109526572012,
  9.9843695780195716e-6, 1.5056327351493116e-7];
function gamma(z) {
  if (z < 0.5) return Math.PI / (Math.sin(Math.PI * z) * gamma(1 - z));
  z -= 1;
  let x = 0.99999999999980993;
  for (let i = 0; i < 8; i++) x += LG[i] / (z + i + 1);
  const t = z + 7.5;
  return Math.sqrt(2 * Math.PI) * Math.pow(t, z + 0.5) * Math.exp(-t) * x;
}

console.log('考える波 第 39 回 ── ホログラフィーを波として見る');
console.log('余分な次元は、対数スケールの軸だった');

// ============================================================
head('1. 同じ二次方程式が、二回出てくる');
// ============================================================
// 第 13 回：u'' + lambda u / r^2 = 0   →  u ~ r^s,  s(s-1) + lambda = 0
//           s = 1/2 +- sqrt(1/4 - lambda)
// AdS   ：phi'' - (d-1)/z phi' - m^2L^2/z^2 phi = 0  →  phi ~ z^Delta
//           Delta(Delta-1) - (d-1)Delta - m^2L^2 = 0
//           Delta^2 - d Delta - m^2L^2 = 0
//           Delta = d/2 +- sqrt(d^2/4 + m^2 L^2)
console.log('');
console.log('  第 13 回   u\'\' + L u/r^2 = 0        s = 1/2 +- sqrt(1/4 - L)');
console.log('  AdS      phi\'\' - (d-1)/z phi\' - m^2L^2/z^2 phi = 0');
console.log('                                     D = d/2 +- sqrt(d^2/4 + m^2L^2)');
console.log('');
console.log('  d -> 1 、 m^2L^2 -> -lambda と置くと ★ 文字どおり同じ式');
console.log('');
console.log('  ' + pad('m^2L^2', 10) + padl('d', 4) + padl('nu=sqrt(d^2/4+m^2L^2)', 24)
  + padl('Delta+', 10) + padl('Delta-', 10) + '  判定');
const BFs = [[0, 4], [-1, 4], [-3.75, 4], [-4, 4], [-4.25, 4], [-5, 4]];
for (const [mm, d] of BFs) {
  const disc = d * d / 4 + mm;
  let nu, dp, dm, judge;
  if (disc >= 0) {
    nu = Math.sqrt(disc); dp = d / 2 + nu; dm = d / 2 - nu;
    judge = (disc === 0) ? '★ BF 境界ちょうど（重根）' : '安定';
    console.log('  ' + pad(f(mm, 2), 10) + padl(d, 4) + padl(f(nu, 6), 24)
      + padl(f(dp, 4), 10) + padl(f(dm, 4), 10) + '  ' + judge);
  } else {
    nu = Math.sqrt(-disc);
    console.log('  ' + pad(f(mm, 2), 10) + padl(d, 4) + padl(f(nu, 6) + ' i', 24)
      + padl('複素', 10) + padl('複素', 10) + '  ★ BF 違反 → 不安定');
  }
}
console.log('');
console.log('  ★ BF 境界 m^2L^2 = -d^2/4 は、第 13 回の臨界 lambda = 1/4 そのもの');
console.log('  ★ そこを越えると指数が複素になる ── 第 13 回の「虚数階」');

// ============================================================
head('2. AdS の波動方程式を実際に解いて、境界の振る舞いを測る');
// ============================================================
// phi'' - (d-1)/z phi' - (k^2 + m^2L^2/z^2) phi = 0
// t = ln z と置くと  dphi/dt = psi,  dpsi/dt = d*psi + (k^2 e^{2t} + m^2L^2) phi
// 正解は phi = z^{d/2} K_nu(k z)
function solve(d, mm, k, tHi, tLo, N) {
  const nu = Math.sqrt(d * d / 4 + mm);
  // 大きい z での漸近： phi ~ z^{(d-1)/2} e^{-kz}
  let t = tHi, z = Math.exp(t);
  let phi = 1.0;
  let psi = ((d - 1) / 2 - k * z) * phi;   // psi = z phi'
  const h = (tLo - tHi) / N;
  const F = function (t, p, q) {
    const z2 = Math.exp(2 * t);
    return [q, d * q + (k * k * z2 + mm) * p];
  };
  for (let i = 0; i < N; i++) {
    const a = F(t, phi, psi);
    const b = F(t + h / 2, phi + h / 2 * a[0], psi + h / 2 * a[1]);
    const c = F(t + h / 2, phi + h / 2 * b[0], psi + h / 2 * b[1]);
    const dd = F(t + h, phi + h * c[0], psi + h * c[1]);
    phi += h / 6 * (a[0] + 2 * b[0] + 2 * c[0] + dd[0]);
    psi += h / 6 * (a[1] + 2 * b[1] + 2 * c[1] + dd[1]);
    t += h;
    // 発散を抑える（線形なので任意に規格化してよい）
    if (Math.abs(phi) > 1e100) { phi *= 1e-100; psi *= 1e-100; }
  }
  // phi = A z^{Dm} + B z^{Dp} として A, B を取り出す
  z = Math.exp(t);
  const Dp = d / 2 + nu, Dm = d / 2 - nu;
  const zp = Math.pow(z, Dp), zm = Math.pow(z, Dm);
  const phid = psi / z;
  // [zm zp; Dm zm/z  Dp zp/z] [A;B] = [phi; phid]
  const det = zm * (Dp * zp / z) - zp * (Dm * zm / z);
  const A = (phi * (Dp * zp / z) - zp * phid) / det;
  const B = (zm * phid - phi * (Dm * zm / z)) / det;
  return { A: A, B: B, nu: nu, Dp: Dp, Dm: Dm };
}

const d4 = 4, mm4 = -3.75;          // nu = 0.5（整数でないので対数項が出ない）
const nu4 = Math.sqrt(d4 * d4 / 4 + mm4);
const exact = gamma(-nu4) / gamma(nu4);   // B/A = [G(-nu)/G(nu)] (k/2)^{2nu}
console.log('');
console.log('  d = ' + d4 + ' 、 m^2L^2 = ' + mm4 + '  →  nu = ' + f(nu4, 6)
  + ' 、 Delta+ = ' + f(d4 / 2 + nu4, 3) + ' 、 Delta- = ' + f(d4 / 2 - nu4, 3));
console.log('  解析解： B/A = [Gamma(-nu)/Gamma(nu)] (k/2)^{2nu} 、係数 = ' + f(exact, 6));
console.log('');
console.log('  ' + pad('k', 10) + padl('B/A（数値）', 18) + padl('B/A（解析）', 18)
  + padl('比', 10));
const ks = [0.25, 0.5, 1, 2, 4, 8];
const BA = [];
for (const k of ks) {
  const tHi = Math.log(40 / k), tLo = Math.log(1e-5 / k);
  const r = solve(d4, mm4, k, tHi, tLo, 200000);
  const num = r.B / r.A;
  const ana = exact * Math.pow(k / 2, 2 * nu4);
  BA.push(num);
  console.log('  ' + pad(f(k, 3), 10) + padl(f(num, 8), 18) + padl(f(ana, 8), 18)
    + padl(f(num / ana, 6), 10));
}
// 傾きを測る
let sl = 0, n = 0;
for (let i = 1; i < ks.length; i++) {
  sl += Math.log(Math.abs(BA[i] / BA[i - 1])) / Math.log(ks[i] / ks[i - 1]); n++;
}
console.log('');
console.log('  ★ ln|B/A| 対 ln k の傾き（数値）= ' + f(sl / n, 6)
  + '   予言 2nu = ' + f(2 * nu4, 6));
console.log('  ★ これが境界の 2 点関数 <O O>(k) ∝ k^{2nu} ── 階数 alpha = 2nu');

// ============================================================
head('3. ★ 階数は、平方根そのものだった');
// ============================================================
console.log('');
console.log('  <O O>(k) ∝ k^{2nu} 、 nu = sqrt(d^2/4 + m^2L^2)');
console.log('  第 1 回の言葉では  alpha = 2nu  ── dB/oct = 6 alpha 、 位相 = 90 alpha 度');
console.log('');
console.log('  ' + pad('m^2L^2 (d=4)', 14) + padl('nu', 12) + padl('alpha=2nu', 12)
  + padl('dB/oct', 10) + padl('位相[度]', 12));
for (const mm of [4, 0, -2, -3, -3.75, -4, -4.25]) {
  const disc = d4 * d4 / 4 + mm;
  if (disc >= 0) {
    const nu = Math.sqrt(disc);
    console.log('  ' + pad(f(mm, 2), 14) + padl(f(nu, 6), 12) + padl(f(2 * nu, 6), 12)
      + padl(f(12 * nu, 3), 10) + padl(f(180 * nu, 2), 12));
  } else {
    const nu = Math.sqrt(-disc);
    console.log('  ' + pad(f(mm, 2), 14) + padl(f(nu, 6) + ' i', 12)
      + padl(f(2 * nu, 4) + ' i', 12) + padl('★ 虚数', 10) + padl('★ 虚数', 12));
  }
}
console.log('');
console.log('  ★★ BF 境界 = 階数がゼロになる点 = 対数の点');
console.log('  ★★ その下では階数が虚数 ── 第 13 回とまったく同じ構図');

// ============================================================
head('4. BF 境界を越えると、対数周期が出る（第 13 回のエフィモフと同型）');
// ============================================================
// d=4, m^2L^2 = -4.25  →  nu = 0.5 i 、 phi = z^2 cos(0.5 ln z + delta)
const mmB = -4.25, nuB = Math.sqrt(-(d4 * d4 / 4 + mmB));
console.log('');
console.log('  d = 4 、 m^2L^2 = ' + mmB + '  →  nu = ' + f(nuB, 6) + ' i');
console.log('  予言： phi = z^{d/2} cos(nu ln z + delta) 、 零点の間隔 = pi/nu = '
  + f(Math.PI / nuB, 6) + '（ln z で）');
// k=0 の純冪方程式を数値で解いて零点を探す
{
  let t = 0, phi = 1, psi = 0;
  const h = -1e-4; const zeros = [];
  const F = (p, q) => [q, d4 * q + mmB * p];
  let prev = phi;
  for (let i = 0; i < 400000; i++) {
    const a = F(phi, psi);
    const b = F(phi + h / 2 * a[0], psi + h / 2 * a[1]);
    const c = F(phi + h / 2 * b[0], psi + h / 2 * b[1]);
    const dd = F(phi + h * c[0], psi + h * c[1]);
    const np = phi + h / 6 * (a[0] + 2 * b[0] + 2 * c[0] + dd[0]);
    const nq = psi + h / 6 * (a[1] + 2 * b[1] + 2 * c[1] + dd[1]);
    if (prev * np < 0) zeros.push(t + h * (prev / (prev - np)));
    phi = np; psi = nq; prev = np; t += h;
    if (Math.abs(phi) > 1e100) { phi *= 1e-100; psi *= 1e-100; prev *= 1e-100; }
  }
  console.log('');
  console.log('  ' + pad('零点 #', 8) + padl('ln z', 14) + padl('前との差', 14)
    + padl('z の比', 16));
  for (let i = 0; i < Math.min(6, zeros.length); i++) {
    const dlt = i ? zeros[i] - zeros[i - 1] : NaN;
    console.log('  ' + pad(i + 1, 8) + padl(f(zeros[i], 6), 14)
      + padl(i ? f(dlt, 6) : '-', 14) + padl(i ? f(Math.exp(-dlt), 4) : '-', 16));
  }
  if (zeros.length > 1) {
    const dlt = Math.abs(zeros[1] - zeros[0]);
    console.log('');
    console.log('  ★ 測定した間隔 = ' + f(dlt, 6) + ' 、 予言 pi/nu = '
      + f(Math.PI / nuB, 6) + ' 、 差 ' + e(Math.abs(dlt - Math.PI / nuB), 2));
    console.log('  ★ z の比 = ' + f(Math.exp(dlt), 4)
      + ' ── 第 13 回のエフィモフ比 22.7 と同じ「対数周期」');
  }
}

// ============================================================
head('5. ★★ 余分な次元は、ウェーブレット平面そのものだった');
// ============================================================
// AdS ポアンカレ計量  ds^2 = L^2 (dx^2 + dz^2)/z^2
// 第 22 回のウェーブレット平面 (b, a) のアフィン群の不変計量も
//                     ds^2 = (db^2 + da^2)/a^2
// → 文字どおり同じ（双曲上半平面）。z = 1/omega 。
console.log('');
console.log('  AdS（ポアンカレ座標）  ds^2 = L^2 (dx^2 + dz^2) / z^2');
console.log('  ウェーブレット平面    ds^2 =     (db^2 + da^2) / a^2');
console.log('  ★ 同じ計量。z（動径）＝ a（スケール）＝ 1/omega');
console.log('');
console.log('  不変性の確認：(b,a) -> (lambda b + c, lambda a) で ds^2 が変わらないか');
function ds2(db, da, a) { return (db * db + da * da) / (a * a); }
console.log('  ' + pad('lambda', 10) + padl('ds^2（変換後）', 20) + padl('比', 12));
const b0 = 0.3, a0 = 0.7, db0 = 1e-4, da0 = 2e-4;
const base = ds2(db0, da0, a0);
for (const lam of [1, 2, 10, 1e3, 1e6]) {
  const v = ds2(lam * db0, lam * da0, lam * a0);
  console.log('  ' + pad(e(lam, 1), 10) + padl(e(v, 8), 20) + padl(f(v / base, 8), 12));
}
console.log('');
console.log('  ★ スケール変換が「等長変換」── だから対数スケール軸が距離を持つ');
console.log('');
// 固有距離 = |ln(z2/z1)|
console.log('  動径方向の固有距離（x 固定）= L |ln(z2/z1)| ── 数値で確認');
function radial(z1, z2, N) {
  const h = (Math.log(z2) - Math.log(z1)) / N; let s = 0;
  for (let i = 0; i < N; i++) { s += Math.abs(h); }   // dz/z = d(ln z)
  return s;
}
console.log('  ' + pad('z1 -> z2', 22) + padl('数値', 14) + padl('|ln(z2/z1)|', 14));
for (const [z1, z2] of [[1, 10], [1, 1e3], [1e-3, 1], [1, 1e17]]) {
  console.log('  ' + pad(e(z1, 0) + ' -> ' + e(z2, 0), 22)
    + padl(f(radial(z1, z2, 100000), 6), 14)
    + padl(f(Math.abs(Math.log(z2 / z1)), 6), 14));
}
console.log('');
console.log('  ★ 1 桁（10 倍）＝ ln 10 = ' + f(Math.LN10, 6) + ' × L');
console.log('  ★ 第 38 回の「電弱からプランクまで 17 桁」＝ 固有距離 '
  + f(17 * Math.LN10, 3) + ' L');
console.log('  ★ 階層問題は、ホログラフィーでは「余分な次元の長さ」になる');

// ============================================================
head('6. もつれのエントロピーが対数になる ── 臨界＝階数ゼロ');
// ============================================================
// AdS3 の測地線：境界の 2 点 (x=0, x=l) を結ぶ半円
//   x = (l/2)(1 + cos th), z = (l/2) sin th
//   長さ = ∫ sqrt(dx^2+dz^2)/z = ∫ dth / sin th = 2 ln(l/eps)
function geodesic(l, eps, N) {
  // th0 は z = eps となる角（sin th0 = 2 eps / l）
  const th0 = Math.asin(Math.min(1, 2 * eps / l));
  // 端点で 1/sin th が発散するので th = th0 e^w と置いて対数的に刻む
  // 対称なので [th0, pi/2] を 2 倍する
  const wmax = Math.log((Math.PI / 2) / th0);
  const h = wmax / N; let s = 0;
  for (let i = 0; i < N; i++) {
    const w = (i + 0.5) * h;
    const th = th0 * Math.exp(w);
    s += 2 * h * th / Math.sin(th);    // dth = th dw
  }
  return s;
}
console.log('');
console.log('  ' + pad('l', 8) + pad('eps', 12) + padl('測地線長（数値）', 20)
  + padl('2 ln(l/eps)', 16) + padl('差', 12));
for (const [l, eps] of [[1, 1e-2], [1, 1e-4], [1, 1e-6], [10, 1e-6]]) {
  const g = geodesic(l, eps, 2000000);
  const p = 2 * Math.log(l / eps);
  console.log('  ' + pad(f(l, 1), 8) + pad(e(eps, 0), 12) + padl(f(g, 8), 20)
    + padl(f(p, 8), 16) + padl(e(Math.abs(g - p), 2), 12));
}
console.log('');
console.log('  S = 測地線長 /(4G) = (c/3) ln(l/eps)   （c = 3L/2G）');
console.log('  ★ 対数 ── これは「階数ゼロ」の場合です（第 2 回の 1/f と同じ）');
console.log('  ★ 冪ではなく対数になるのが 1+1 次元の臨界の印');

// ============================================================
head('7. 自由度の数え上げ ── 面積と格子');
// ============================================================
// z = eps の切断面の面積 / (プランク面積) ∝ (R/eps)^{d-1}
console.log('');
console.log('  AdS_{d+1} で z = eps に切ると、境界の体積要素は (L/eps)^{d-1}');
console.log('  ── 間隔 eps の格子のセル数そのもの（UV 切断 = 動径の切断）');
console.log('');
console.log('  ' + pad('d', 5) + pad('R', 8) + pad('eps', 10) + padl('(R/eps)^{d-1}', 18)
  + padl('意味', 24));
for (const [dd, R, ep] of [[2, 1, 1e-3], [3, 1, 1e-3], [4, 1, 1e-3], [4, 1, 1e-6]]) {
  console.log('  ' + pad(dd, 5) + pad(f(R, 0), 8) + pad(e(ep, 0), 10)
    + padl(e(Math.pow(R / ep, dd - 1), 4), 18) + padl('格子のセル数', 24));
}
console.log('');
console.log('  ★ 「面積で数える」は、第 6 回のホログラフィック限界と同じ数え方');
console.log('  ★ 動径を切ること = 周波数を切ること（第 22 回の窓）');

// ============================================================
head('8. くりこみ群の流れ ＝ 動径方向の運動');
// ============================================================
// 境界の結合 g(mu) の走りが、バルクの場の z 依存になる
// 一ループ：dg/d ln mu = -b g^3 → 動径方向の「運動方程式」
console.log('');
console.log('  ln mu = -ln z なので、第 5 回の「走る結合」は動径方向の流れ');
console.log('');
const b0c = 7 / (16 * Math.PI * Math.PI);   // 適当な一ループ係数（例示）
console.log('  ' + pad('z', 12) + padl('mu = 1/z', 14) + padl('g^2(mu)', 14)
  + padl('固有距離', 14));
let g2 = 0.3;
let zprev = 1;
for (const z of [1, 1e-1, 1e-2, 1e-3, 1e-4]) {
  // dg^2/dln mu = -2 b0 g^4
  const dl = Math.log(zprev / z);
  g2 = g2 / (1 + 2 * b0c * g2 * dl);
  console.log('  ' + pad(e(z, 0), 12) + padl(e(1 / z, 0), 14) + padl(f(g2, 8), 14)
    + padl(f(Math.abs(Math.log(z)), 6), 14));
  zprev = z;
}
console.log('');
console.log('  ★ 「エネルギースケールを上げる」＝「境界に近づく」');
console.log('  ★ 第 5 回で見た走りは、余分な次元では ── ただの移動でした');

// ============================================================
head('9. 本回のまとめ');
// ============================================================
const rows = [
  ['Delta の式 = 第 13 回の式', '◎ 解析', '★ d->1, m^2L^2->-lambda で一致'],
  ['BF 境界 = 臨界 lambda=1/4', '◎ 解析', '★ 階数がゼロになる点'],
  ['★ <O O> ∝ k^{2nu} を数値で', '◎ 数値', '★ 傾き ' + f(sl / n, 4) + '（予言 ' + f(2 * nu4, 4) + '）'],
  ['★ 階数 alpha = 2 sqrt(d^2/4+m^2L^2)', '◎ 対応', '★ 階数は平方根そのもの'],
  ['BF 違反 → 対数周期', '◎ 数値', '★ 間隔 pi/nu を実測'],
  ['★ 余分な次元 = ウェーブレット平面', '◎ 解析', '★ 計量が文字どおり同じ'],
  ['もつれ = 測地線長 = 対数', '◎ 数値', '★ 2 ln(l/eps) と一致'],
  ['自由度 = (L/eps)^{d-1}', '◎ 解析', '第 6 回のホログラフィック限界'],
  ['くりこみ群 = 動径方向の運動', '◎ 対応', '第 5 回の走りが「移動」になる'],
  ['★ 重力の量子論が出るか', '× 出ない', '★ 対応は仮定。本稿は検証していない'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 36) + pad(r[1], 10) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 第 22 回で引いた ln omega の軸は、');
console.log('  ★ ホログラフィーでは「余分な次元」と呼ばれていた。');
console.log('  ★ そして境界の階数は alpha = 2 sqrt(d^2/4 + m^2L^2) ──');
console.log('  ★ 質量が階数を決め、BF 境界でそれがゼロになり、その下で虚数になる。');
console.log('');
console.log('  ★ ただし「重力＝場の理論」という対応自体は仮定で、本稿は検証していません。');
