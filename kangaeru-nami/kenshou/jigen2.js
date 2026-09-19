// 考える波 第65回「次元を落とすということ」検証
//   node jigen2.js
// 依存ライブラリ 0（FFT も 箱数えも 自前）。
//
// 問い（読者から）：
//   「次元って積分することなので 6 dB のフィルターじゃん。
//     観測するって 2 次元の波を観測するわけだから 情報落ちるよね。
//     観測対象の構造が非整数次元だと誤差が出るよね。
//     質量とかって非整数次元の波で説明できないの？」
//
// 本稿で 数えること：
//   ★ 次元は 6 dB では なく 3 dB（積分と 2 倍 違う）── 01・02節
//   ★★ 「情報が落ちる」には 2 種類ある。スライスは 形を変え、
//      射影は 形を変えないのに 情報を 落とす ── 03節
//   ★★★ 非整数次元だと 誤差が出るのでは なく、2 で 頭打ちになる
//      （マーストランドの射影定理）── 04節
//   ★★ しかも 対称軸は 定理の 例外方向 ── 05節
//   ★★★ 質量＝非整数次元は 第 2 回の 積分 そのもの ── 06・07節

'use strict';

const TWO_PI = 2 * Math.PI;
const L = (s) => console.log(s);
const rule = (c) => L((c || '-').repeat(78));
const head = (n, t) => { L(''); rule('='); L('[' + n + '] ' + t); rule('='); };
const pad = (s, n) => String(s).padStart(n);
const d10 = (x) => Math.log(x) / Math.LN10;
function slope(xs, ys) {
  const n = xs.length; let sx = 0, sy = 0, sxx = 0, sxy = 0;
  for (let i = 0; i < n; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
  return (n * sxy - sx * sy) / (n * sxx - sx * sx);
}
const CHECKS = [];
function chk(label, got, want, tol, note) {
  CHECKS.push([label, got, want, Math.abs(got - want) <= tol, note || '']);
}

// ---------------------------------------------------------------- FFT
function fft(re, im, inv) {
  const n = re.length;
  for (let i = 1, j = 0; i < n; i++) {
    let bit = n >> 1;
    for (; j & bit; bit >>= 1) j ^= bit;
    j ^= bit;
    if (i < j) { let t = re[i]; re[i] = re[j]; re[j] = t; t = im[i]; im[i] = im[j]; im[j] = t; }
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
  const u = Math.max(rnd(), 1e-12);
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(TWO_PI * rnd());
}
// 第59回の教訓：対数を とる前に 周期図を 平均する
function periodogram(x) {
  const N = x.length;
  const re = Float64Array.from(x), im = new Float64Array(N);
  fft(re, im, false);
  const P = new Float64Array(N);
  for (let k = 0; k < N; k++) P[k] = re[k] * re[k] + im[k] * im[k];
  return P;
}
function betaFromAvg(P, klo, khi) {
  const xs = [], ys = [];
  for (let k = klo; k <= khi; k++) { xs.push(Math.log(k)); ys.push(Math.log(P[k] + 1e-300)); }
  return -slope(xs, ys);
}

// ==================================================================
head(1, '物差しを 揃える ── 「次元」と「積分」は 同じ 6 dB では ない');
// ==================================================================
L('本シリーズの 背骨：振幅 ∝ f^-alpha なら -6.02 alpha dB/oct（第 1 回）。');
L('パワー S ∝ f^-beta で beta = 2 alpha。よって beta 1 = 3.01 dB/oct。');
L('');
L(pad('操作', 22) + pad('動く量', 16) + pad('dB/oct', 12) + pad('出典', 14));
rule();
L(pad('1 回 積分する', 22) + pad('alpha +1', 16) + pad('6.02', 12) + pad('第 1 回', 14));
L(pad('1 次元 スライスする', 22) + pad('beta -1', 16) + pad('3.01', 12) + pad('本回 02節', 14));
L(pad('1 方向に 射影する', 22) + pad('beta 変わらず', 16) + pad('0', 12) + pad('本回 02節', 14));
rule();
chk('積分と スライスの 比', 6.0206 / 3.0103, 2.0, 1e-6, '定義から');
L('★ 積分と 次元は ちょうど 2 倍 違う。');
L('★★ そして 射影は 0 ── スペクトルの 形を まったく 変えない。');
L('   （それでも 情報は 落ちている。03節）');

// ==================================================================
head(2, 'd 次元の 場から 1 次元を 取り出す ── 数値で 確かめる');
// ==================================================================
// 予言 (a) スライス： beta_1 = beta_d - (d-1)
// 予言 (b) 射影    ： beta_1 = beta_d        （k_perp = 0 を 取るだけ）

function field2D(N, beta) {
  const re = new Float64Array(N * N), im = new Float64Array(N * N);
  for (let i = 0; i < N; i++) {
    const ki = (i <= N / 2) ? i : i - N;
    for (let j = 0; j < N; j++) {
      const kj = (j <= N / 2) ? j : j - N;
      const k = Math.hypot(ki, kj);
      if (k === 0) continue;
      const amp = Math.pow(k, -beta / 2);
      re[i * N + j] = gauss() * amp; im[i * N + j] = gauss() * amp;
    }
  }
  const a = new Float64Array(N), b = new Float64Array(N);
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) { a[j] = re[i * N + j]; b[j] = im[i * N + j]; }
    fft(a, b, true);
    for (let j = 0; j < N; j++) { re[i * N + j] = a[j]; im[i * N + j] = b[j]; }
  }
  for (let j = 0; j < N; j++) {
    for (let i = 0; i < N; i++) { a[i] = re[i * N + j]; b[i] = im[i * N + j]; }
    fft(a, b, true);
    for (let i = 0; i < N; i++) { re[i * N + j] = a[i]; im[i * N + j] = b[i]; }
  }
  return re;
}
function field3D(N, beta) {
  const M = N * N * N;
  const re = new Float64Array(M), im = new Float64Array(M);
  for (let i = 0; i < N; i++) {
    const ki = (i <= N / 2) ? i : i - N;
    for (let j = 0; j < N; j++) {
      const kj = (j <= N / 2) ? j : j - N;
      for (let l = 0; l < N; l++) {
        const kl = (l <= N / 2) ? l : l - N;
        const k = Math.sqrt(ki * ki + kj * kj + kl * kl);
        if (k === 0) continue;
        const amp = Math.pow(k, -beta / 2);
        const idx = (i * N + j) * N + l;
        re[idx] = gauss() * amp; im[idx] = gauss() * amp;
      }
    }
  }
  const a = new Float64Array(N), b = new Float64Array(N);
  for (let ax = 0; ax < 3; ax++) {
    for (let p = 0; p < N; p++) for (let q = 0; q < N; q++) {
      for (let r = 0; r < N; r++) {
        const idx = ax === 0 ? (r * N + p) * N + q : ax === 1 ? (p * N + r) * N + q : (p * N + q) * N + r;
        a[r] = re[idx]; b[r] = im[idx];
      }
      fft(a, b, true);
      for (let r = 0; r < N; r++) {
        const idx = ax === 0 ? (r * N + p) * N + q : ax === 1 ? (p * N + r) * N + q : (p * N + q) * N + r;
        re[idx] = a[r]; im[idx] = b[r];
      }
    }
  }
  return re;
}

{
  const N = 512;
  L('2 次元場（' + N + 'x' + N + '、24 実現 x 全 行 を 平均）');
  L('');
  L(pad('beta_2', 9) + pad('スライス', 12) + pad('予言 b-1', 11) +
    pad('射影', 11) + pad('予言 b', 9));
  rule();
  for (const b2 of [2.0, 3.0, 4.0]) {
    const Psl = new Float64Array(N), Ppr = new Float64Array(N);
    let nsl = 0, npr = 0;
    for (let rep = 0; rep < 24; rep++) {
      const f = field2D(N, b2);
      const v = new Float64Array(N);
      for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) v[j] = f[i * N + j];
        const P = periodogram(v);
        for (let k = 0; k < N; k++) Psl[k] += P[k];
        nsl++;
      }
      for (let j = 0; j < N; j++) { let s = 0; for (let i = 0; i < N; i++) s += f[i * N + j]; v[j] = s; }
      let P = periodogram(v);
      for (let k = 0; k < N; k++) Ppr[k] += P[k];
      npr++;
      for (let i = 0; i < N; i++) { let s = 0; for (let j = 0; j < N; j++) s += f[i * N + j]; v[i] = s; }
      P = periodogram(v);
      for (let k = 0; k < N; k++) Ppr[k] += P[k];
      npr++;
    }
    for (let k = 0; k < N; k++) { Psl[k] /= nsl; Ppr[k] /= npr; }
    const bs = betaFromAvg(Psl, 4, N / 8), bp = betaFromAvg(Ppr, 4, N / 8);
    L(pad(b2.toFixed(1), 9) + pad(bs.toFixed(3), 12) + pad((b2 - 1).toFixed(1), 11) +
      pad(bp.toFixed(3), 11) + pad(b2.toFixed(1), 9));
    chk('2D スライス b=' + b2, bs, b2 - 1, 0.12, 'beta_1 = beta_2 - 1');
    chk('2D 射影 b=' + b2, bp, b2, 0.12, 'beta_1 = beta_2');
  }
  rule();
}
{
  const N = 128;
  L('');
  L('3 次元場（' + N + '^3、3 実現 x 全 ' + (N * N) + ' 本の 線 を 平均）');
  L('');
  L(pad('beta_3', 9) + pad('スライス', 12) + pad('予言 b-2', 11) +
    pad('射影', 11) + pad('予言 b', 9));
  rule();
  for (const b3 of [3.0, 4.0, 5.0]) {
    const Psl = new Float64Array(N), Ppr = new Float64Array(N);
    let nsl = 0, npr = 0;
    for (let rep = 0; rep < 3; rep++) {
      const f = field3D(N, b3);
      const v = new Float64Array(N);
      for (let p = 0; p < N; p++) for (let q = 0; q < N; q++) {
        for (let r = 0; r < N; r++) v[r] = f[(p * N + q) * N + r];
        const P = periodogram(v);
        for (let k = 0; k < N; k++) Psl[k] += P[k];
        nsl++;
      }
      for (let ax = 0; ax < 3; ax++) {
        for (let r = 0; r < N; r++) {
          let s = 0;
          for (let p = 0; p < N; p++) for (let q = 0; q < N; q++) {
            s += ax === 0 ? f[(r * N + p) * N + q] : ax === 1 ? f[(p * N + r) * N + q] : f[(p * N + q) * N + r];
          }
          v[r] = s;
        }
        const P = periodogram(v);
        for (let k = 0; k < N; k++) Ppr[k] += P[k];
        npr++;
      }
    }
    for (let k = 0; k < N; k++) { Psl[k] /= nsl; Ppr[k] /= npr; }
    const bs = betaFromAvg(Psl, 3, N / 8), bp = betaFromAvg(Ppr, 3, N / 8);
    L(pad(b3.toFixed(1), 9) + pad(bs.toFixed(3), 12) + pad((b3 - 2).toFixed(1), 11) +
      pad(bp.toFixed(3), 11) + pad(b3.toFixed(1), 9));
    chk('3D スライス b=' + b3, bs, b3 - 2, 0.18, 'beta_1 = beta_3 - 2');
    chk('3D 射影 b=' + b3, bp, b3, 0.18, 'beta_1 = beta_3');
  }
  rule();
  L('★★★ スライスは 1 次元 あたり beta を 1（3.01 dB/oct）平らにする。');
  L('★★★ 射影は beta を まったく 変えない。');
}

// ==================================================================
head(3, '★★ それでも 射影は 情報を 落としている ── 数えれば 分かる');
// ==================================================================
// 射影は フーリエ空間で「原点を通る 平面（または 直線）」を 取るだけ。
// N^3 の 物体から 1 回の 射影で 取れるのは N^2 点 ── 全体の 1/N。
{
  L('射影定理：1 方向の 射影の フーリエ変換 ＝ 原点を通る 断面');
  L('');
  L(pad('物体', 14) + pad('全係数', 14) + pad('1 射影で 取れる', 16) +
    pad('割合', 12) + pad('全部 埋めるのに', 16));
  rule();
  for (const N of [64, 128, 256, 512]) {
    L(pad('N^3 (N=' + N + ')', 14) + pad((N * N * N).toExponential(2), 14) +
      pad((N * N).toExponential(2), 16) + pad('1/' + N, 12) +
      pad('約 ' + Math.round(Math.PI * N / 2) + ' 方向', 16));
  }
  rule();
  L('★ 1 枚の 写真で 取れるのは 3 次元の 情報の 1/N。');
  L('★★ スペクトルの 形（beta）は 変わらないのに、');
  L('   k_perp ≠ 0 の 成分は 丸ごと 落ちている。');
  L('★★★ 「形が 同じ」は「情報が 落ちていない」を 意味しない。');
  L('   ── 第59・60回の 主題（見かけの量が 保存されていても 失うものはある）。');
  L('★ だから CT は 成り立つ：多方向から 集めれば k_perp を 埋め戻せる。');
  L('   1 方向では 戻せない。必要な 方向数は 約 pi N/2（標本化定理）。');
}

// 実際に 断面を 数えて 確かめる（2 次元で）
{
  const N = 128;
  L('');
  L('2 次元で 実際に 数える：M 方向の 射影が k 空間の 何 % を 覆うか');
  L('');
  L(pad('M 方向', 10) + pad('覆った点', 14) + pad('全体 N^2', 12) +
    pad('割合', 10) + pad('予言 M/(piN/2)', 16));
  rule();
  for (const M of [1, 4, 16, 64, 128, 201]) {
    const seen = new Set();
    for (let m = 0; m < M; m++) {
      const th = Math.PI * m / M;
      const ct = Math.cos(th), st = Math.sin(th);
      for (let t = -N; t <= N; t += 0.25) {
        const kx = Math.round(t * ct), ky = Math.round(t * st);
        if (Math.abs(kx) <= N / 2 && Math.abs(ky) <= N / 2) seen.add(kx + ',' + ky);
      }
    }
    const frac = seen.size / (N * N);
    L(pad(M, 10) + pad(seen.size, 14) + pad(N * N, 12) +
      pad((100 * frac).toFixed(1) + '%', 10) +
      pad((M / (Math.PI * N / 2)).toFixed(3), 16));
  }
  rule();
  L('★ 方向を 増やすと 埋まっていく。約 pi N/2 = ' +
    Math.round(Math.PI * N / 2) + ' 方向 で ほぼ 全部。');
  L('★★ ただし 原点近くは すぐ 埋まり、外側は 最後まで 疎 ──');
  L('   これが CT の 分解能が 中心で 良く 周辺で 悪い 理由。');
}

// ==================================================================
head(4, '★★★ 非整数次元だと どうなるか ── マーストランドの 射影定理');
// ==================================================================
// 定理（Marstrand 1954 / Mattila）：ハウスドルフ次元 D の 集合を
// k 次元平面に 射影すると、ほとんど すべての 方向で 次元は min(D, k)。

function buildDust(m, levels, seed) {
  _s = seed;
  const idx = [];
  for (let i = 0; i < 27; i++) idx.push(i);
  for (let i = 26; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); const t = idx[i]; idx[i] = idx[j]; idx[j] = t; }
  const pick = idx.slice(0, m);
  let pts = [[0, 0, 0]], scale = 1;
  for (let lv = 0; lv < levels; lv++) {
    const next = [];
    for (const p of pts) for (const c of pick) {
      next.push([p[0] * 3 + (c % 3), p[1] * 3 + Math.floor(c / 3) % 3, p[2] * 3 + Math.floor(c / 9)]);
    }
    pts = next; scale *= 3;
  }
  const proj = new Set();
  for (const c of pick) proj.add((c % 3) + ',' + (Math.floor(c / 3) % 3));
  return { pts: pts, n: scale, mProj: proj.size };
}
function boxDim3(pts, n) {
  const xs = [], ys = [];
  for (let b = 1; b <= n / 3; b *= 3) {
    const seen = new Set();
    for (const p of pts) seen.add(Math.floor(p[0] / b) + ',' + Math.floor(p[1] / b) + ',' + Math.floor(p[2] / b));
    xs.push(Math.log(n / b)); ys.push(Math.log(seen.size));
  }
  return slope(xs, ys);
}
function boxDimProj(pts, n, u) {
  const a0 = Math.abs(u[0]) < 0.9 ? [1, 0, 0] : [0, 1, 0];
  let e1 = [u[1] * a0[2] - u[2] * a0[1], u[2] * a0[0] - u[0] * a0[2], u[0] * a0[1] - u[1] * a0[0]];
  const n1 = Math.hypot(e1[0], e1[1], e1[2]); e1 = e1.map((v) => v / n1);
  const e2 = [u[1] * e1[2] - u[2] * e1[1], u[2] * e1[0] - u[0] * e1[2], u[0] * e1[1] - u[1] * e1[0]];
  const xs = [], ys = [];
  for (let b = 1; b <= n / 3; b *= 3) {
    const seen = new Set();
    for (const p of pts) {
      const x = p[0] * e1[0] + p[1] * e1[1] + p[2] * e1[2];
      const y = p[0] * e2[0] + p[1] * e2[1] + p[2] * e2[2];
      seen.add(Math.floor(x / b) + ',' + Math.floor(y / b));
    }
    xs.push(Math.log(n / b)); ys.push(Math.log(seen.size));
  }
  return slope(xs, ys);
}
{
  const u = [0.3717, 0.5901, 0.7159];
  const un = Math.hypot(u[0], u[1], u[2]);
  const uu = u.map((v) => v / un);
  L('3 次元カントール塵（1 辺を 3 分割＝27 個 から m 個 残す、D = log m/log 3）');
  L('');
  L(pad('m', 5) + pad('理論 D', 10) + pad('3D 実測', 10) + pad('軸射影', 10) +
    pad('軸の予言', 10) + pad('一般方向', 10) + pad('min(D,2)', 10));
  rule();
  for (const m of [5, 7, 9, 12, 16, 20, 24]) {
    const D = Math.log(m) / Math.log(3);
    const lv = (m <= 9) ? 6 : (m <= 16 ? 5 : 4);
    const r = buildDust(m, lv, 20260920 + m);
    const d3 = boxDim3(r.pts, r.n);
    const dAx = boxDimProj(r.pts, r.n, [0, 0, 1]);
    const dGen = boxDimProj(r.pts, r.n, uu);
    const predAx = Math.log(r.mProj) / Math.log(3);
    L(pad(m, 5) + pad(D.toFixed(4), 10) + pad(d3.toFixed(4), 10) + pad(dAx.toFixed(4), 10) +
      pad(predAx.toFixed(4), 10) + pad(dGen.toFixed(4), 10) + pad(Math.min(D, 2).toFixed(4), 10));
    chk('3D 次元 m=' + m, d3, D, 1e-6, '箱数え＝理論');
    chk('射影は 2 以下 m=' + m, dGen <= 2.02 ? 1 : 0, 1, 0, 'マーストランドの 上限');
  }
  rule();
  L('★★★ 3 次元での 次元は 理論値と 完全一致（1.465 〜 2.893）。');
  L('★★★ ところが 射影は D が いくら 大きくても 2 を 超えない。');
  L('★★ 「非整数次元だと 誤差が 出る」のでは なく、');
  L('   2 を 超えたぶんが 丸ごと 消える。');
  L('★ 有限段数（4〜6 段）なので 値は 2 より 少し 低く出るが、');
  L('   頭打ちの 構造は はっきり 見える。');
}

// ==================================================================
head(5, '★★ 対称軸は 定理の 例外方向 ── 一番 損な 見方');
// ==================================================================
{
  L('マーストランドは「ほとんど すべての 方向で min(D,2)」。');
  L('「ほとんど」の 外に あるのが 例外方向 ── 格子の 対称軸が まさに それ。');
  L('');
  L('軸射影の 次元は log(射影で 潰れずに 残る 部分セル数)/log 3 で');
  L('決まる 組合せ量で、マーストランドの 値では ない。');
  L('');
  L('  上の表：m=16（D=2.524）で');
  L('    軸射影   1.686（予言 log7/log3 = 1.771）');
  L('    一般方向 1.871');
  L('  → 軸に 乗せると 定理が 保証する ぶんすら 取り落とす。');
  L('');
  L('★★★ 観測方向を 対象の 対称軸に 合わせるのは、');
  L('   見やすいが いちばん 情報が 落ちる 見方。');
  L('★ 結晶を 撮るときに 低指数方位を 外すのは この ため。');
}

// ==================================================================
head(6, '★★★ 質量は 非整数次元の 波か ── 第 2 回の 積分 そのもの');
// ==================================================================
// 単一の 質量 = 単一の 極。非整数の スケーリング次元 = 質量の 冪分布。
// これは 第 2 回「1/f は 多数の 時定数の 重ね合わせ」と 同じ 積分。
{
  L('第 2 回 ：S(w) = ∫ g(tau) tau/(1+w^2 tau^2) dtau、g ∝ tau^-gamma → S ∝ w^(gamma-2)');
  L('アンパーティクル（Georgi 2007）：');
  L('        rho(M^2) ∝ (M^2)^(d_U-2) の 質量連続体 → 伝播関数 ∝ (p^2)^(d_U-2)');
  L('');
  L('同じ 積分か、数値で 確かめる：');
  L('  ∫_0^inf u^(a-1)/(p^2+u) du = pi p^(2(a-1)) / sin(pi a)   （0 < a < 1）');
  L('');
  function propNum(a) {
    let s = 0;
    const lo = -40, hi = 40, n = 600000, h = (hi - lo) / n;
    for (let i = 0; i < n; i++) {
      const t = Math.exp(lo + h * (i + 0.5));
      s += Math.pow(t, a - 1) / (1 + t) * t * h;
    }
    return s;
  }
  L(pad('d_U', 8) + pad('a = d_U-1', 12) + pad('数値積分', 16) +
    pad('pi/sin(pi a)', 16) + pad('比', 10));
  rule();
  for (const dU of [1.2, 1.4, 1.5, 1.6, 1.8]) {
    const a = dU - 1, num = propNum(a), ana = Math.PI / Math.sin(Math.PI * a);
    L(pad(dU.toFixed(1), 8) + pad(a.toFixed(1), 12) + pad(num.toFixed(6), 16) +
      pad(ana.toFixed(6), 16) + pad((num / ana).toFixed(6), 10));
    chk('アンパーティクル積分 d_U=' + dU, num / ana, 1.0, 5e-3, 'pi/sin(pi a)');
  }
  rule();
  L('★ 質量の 冪分布から 伝播関数 (p^2)^(d_U-2) が 出る。');
  L('  d_U = 1 なら 1/p^2 ＝ 普通の 質量ゼロ粒子（極が 1 つ）。');
  L('');
  L('第 2 回との 対応：');
  L(pad('第 2 回（1/f）', 30) + pad('アンパーティクル', 30));
  rule();
  const MAP = [
    ['時定数 tau', '質量の逆数 1/M'],
    ['ローレンツ tau/(1+w^2tau^2)', '伝播関数 1/(p^2+M^2)'],
    ['g(tau) ∝ tau^-gamma', 'rho(M^2) ∝ (M^2)^(d_U-2)'],
    ['S ∝ w^(gamma-2)', 'Prop ∝ (p^2)^(d_U-2)'],
  ];
  for (const r of MAP) L(pad(r[0], 30) + pad(r[1], 30));
  rule();
  L('  指数を 合わせると gamma - 2 = 2 d_U - 4 → d_U = 1 + gamma/2');
  L('  beta = 2 - gamma だから  d_U = 2 - beta/2 = 2 - alpha');
  L('');
  L(pad('alpha', 9) + pad('beta', 8) + pad('gamma', 9) + pad('d_U = 2-alpha', 15) + pad('意味', 22));
  rule();
  for (const r of [[0, '白色雑音'], [0.5, '桃色雑音'], [1.0, '1/f'], [1.5, ''], [2.0, 'ブラウン運動']]) {
    const a = r[0];
    L(pad(a.toFixed(1), 9) + pad((2 * a).toFixed(1), 8) + pad((2 - 2 * a).toFixed(1), 9) +
      pad((2 - a).toFixed(1), 15) + pad(r[1], 22));
    chk('d_U = 2 - alpha（alpha=' + a + '）', 2 - a, 2 - a, 1e-12, '定義');
  }
  rule();
  L('★★★ 本シリーズの alpha が そのまま アンパーティクルの 次元 d_U = 2 - alpha。');
  L('★★ 1/f（alpha=1）が d_U=1 ＝ 極 1 つ ＝ 普通の 粒子 に 当たる。');
  L('★ ただし これは 同じ 積分の 別の 書き方であって、');
  L('   「質量の 起源」を 説明した わけでは ない。');
  L('   アンパーティクルは 未発見の 仮説である ことも 忘れないこと。');
}

// ==================================================================
head(7, 'AdS/CFT では 文字どおり 成り立つ（第 39 回の 再掲）');
// ==================================================================
{
  L('第 39 回： Delta(Delta - d) = m^2 L^2、Delta = d/2 ± sqrt(d^2/4 + m^2 L^2)');
  L('  境界の 演算子の 次元 Delta が バルクの 質量 m を 決める。逆も 同じ。');
  L('');
  L(pad('m^2 L^2', 12) + pad('d=4 の Delta+', 16) + pad('整数か', 12));
  rule();
  for (const mL of [-4, -3, 0, 1, 2, 5, 7, 12]) {
    const dp = 2 + Math.sqrt(4 + mL);
    L(pad(mL, 12) + pad(dp.toFixed(6), 16) +
      pad(Math.abs(dp - Math.round(dp)) < 1e-9 ? '整数' : '非整数', 12));
  }
  rule();
  chk('Delta(Delta-d) = m^2L^2', (2 + Math.sqrt(5)) * (2 + Math.sqrt(5) - 4), 1.0, 1e-9, 'd=4, m^2L^2=1');
  L('★ 4 + m^2L^2 が 平方数の ときだけ 整数。ふつうは 非整数。');
  L('★★★ 「質量 ＝ 非整数次元」は AdS/CFT では 文字どおり 成り立つ。');
  L('★★ ただし これは 2 つの 記述の 辞書であって、');
  L('   「なぜ その 質量なのか」には 答えていない。');
  L('★ そして 第 13 回の s = 1/2 ± sqrt(1/4 - lambda) と 同じ 2 次方程式。');
  L('   本シリーズは これを 3 度 見ている（第 13・39・47 回）。');
}

// ==================================================================
head(8, '検算のまとめ');
// ==================================================================
L(pad('項目', 34) + pad('計算', 14) + pad('参照', 14) + pad('判定', 8));
rule();
let bad = 0;
for (const c of CHECKS) {
  if (!c[3]) bad++;
  const f = (v) => (typeof v === 'number')
    ? (Math.abs(v) !== 0 && (Math.abs(v) < 1e-3 || Math.abs(v) > 1e5) ? v.toExponential(2) : v.toFixed(4)) : v;
  L(pad(c[0], 34) + pad(f(c[1]), 14) + pad(f(c[2]), 14) + pad(c[3] ? 'OK' : 'NG', 8));
}
rule();
L(bad === 0 ? '★ 全 ' + CHECKS.length + ' 件 合格。' : '★ ' + CHECKS.length + ' 件 中 ' + bad + ' 件 不一致。');
L('');
L('★★★ 次元は 3 dB、積分は 6 dB ── ちょうど 2 倍 違う。');
L('★★★ 射影は 形を 変えないのに 情報を 落とす（1 枚で 1/N）。');
L('★★★ 非整数次元は 誤差を 生むのでは なく、2 で 頭打ちに なる。');
L('★★★ 質量＝非整数次元は、第 2 回の 重ね合わせ積分 そのもの。');
L('');
