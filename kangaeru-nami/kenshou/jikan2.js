// 考える波 第 40 回：時間結晶を波として見る
//   揺すった周期の「半分」で答える波 ── 分数調波と、その剛性
//   node jikan2.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

// ---- 素朴な DFT（必要な周波数だけ拾う） ----
function dftMag(x, fr) {          // fr は「1 サンプルあたりの回転数」
  let re = 0, im = 0;
  for (let i = 0; i < x.length; i++) {
    const p = 2 * Math.PI * fr * i;
    re += x[i] * Math.cos(p); im -= x[i] * Math.sin(p);
  }
  return Math.sqrt(re * re + im * im) / x.length;
}
function peakFreq(x, f0, f1, N) { // [f0,f1] を N 分割して最大を探し、放物線で補間
    let best = -1, bi = 0; const h = (f1 - f0) / N; const m = [];
  for (let i = 0; i <= N; i++) { m.push(dftMag(x, f0 + i * h)); }
  for (let i = 0; i <= N; i++) if (m[i] > best) { best = m[i]; bi = i; }
  if (bi > 0 && bi < N) {
    const a = m[bi - 1], b = m[bi], c = m[bi + 1];
    const d = (a - c) / (2 * (a - 2 * b + c));
    return { f: f0 + (bi + d) * h, mag: b };
  }
  return { f: f0 + bi * h, mag: best };
}

console.log('考える波 第 40 回 ── 時間結晶を波として見る');
console.log('揺すった周期の「半分」で答える波');

// ============================================================
head('1. 線形で時不変な系からは、分数調波は絶対に出ない');
// ============================================================
// 一次の IIR フィルタに cos(2 pi f0 n) を入れて、f0/2 の成分を測る
{
  const N = 1 << 14, f0 = 0.1, a = 0.9;
  const y = new Array(N); let prev = 0;
  for (let i = 0; i < N; i++) {
    const u = Math.cos(2 * Math.PI * f0 * i);
    prev = a * prev + (1 - a) * u; y[i] = prev;
  }
  // 過渡を捨てる。窓は f0 と f0/2 の周期の整数倍（= 20 サンプル）に揃える
  const z = y.slice(2000, 2000 + 12000);
  const m1 = dftMag(z, f0), mh = dftMag(z, f0 / 2), m2 = dftMag(z, 2 * f0);
  console.log('');
  console.log('  一次 IIR（線形・時不変）に f0 = 0.1 を入れる');
  console.log('  ' + pad('成分', 16) + padl('振幅', 16) + padl('dB（f0 比）', 16));
  console.log('  ' + pad('f0（入力）', 16) + padl(e(m1, 4), 16) + padl('0.0', 16));
  console.log('  ' + pad('f0/2（分数調波）', 16) + padl(e(mh, 4), 16)
    + padl(f(20 * Math.log10(mh / m1), 1), 16));
  console.log('  ' + pad('2 f0（高調波）', 16) + padl(e(m2, 4), 16)
    + padl(f(20 * Math.log10(m2 / m1), 1), 16));
  console.log('');
  console.log('  ★ 窓を周期の整数倍に取ると、分数調波も高調波も丸め誤差の底まで落ちる');
  console.log('  ★ 第 1 回の「線形時不変は周波数を作れない」── 時間結晶はここには居ない');
}

// ============================================================
head('2. 係数の側を揺らすと出る ── マシュー方程式');
// ============================================================
// x'' + w0^2 (1 + h cos(w t)) x = 0 、 w = 2 w0 が最強の不安定舌
function mathieu(w0, h, w, T, dt, x0, v0) {
  let x = x0, v = v0, t = 0;
  const n = Math.round(T / dt);
  const A = (t) => -w0 * w0 * (1 + h * Math.cos(w * t));
  for (let i = 0; i < n; i++) {
    const k1x = v, k1v = A(t) * x;
    const k2x = v + dt / 2 * k1v, k2v = A(t + dt / 2) * (x + dt / 2 * k1x);
    const k3x = v + dt / 2 * k2v, k3v = A(t + dt / 2) * (x + dt / 2 * k2x);
    const k4x = v + dt * k3v, k4v = A(t + dt) * (x + dt * k3x);
    x += dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x);
    v += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v);
    t += dt;
  }
  return [x, v];
}
{
  const w0 = 1.0;
  console.log('');
  console.log('  x\'\' + w0^2 (1 + h cos(w t)) x = 0 、 w0 = 1 、 w = 2（＝ 2 w0）');
  console.log('  解析：成長率 s = h w0 / 4');
  console.log('');
  console.log('  ' + pad('h', 10) + padl('成長率（実測）', 18) + padl('h w0/4', 14)
    + padl('比', 10));
  for (const h of [0.02, 0.05, 0.1, 0.2, 0.4]) {
    // 一周期の単値行列から厳密に取る（長時間積分より精度が高い）
    const T = Math.PI;                       // 2 pi / w 、 w = 2
    const dt = T / 200000;
    const c1 = mathieu(w0, h, 2 * w0, T, dt, 1, 0);
    const c2 = mathieu(w0, h, 2 * w0, T, dt, 0, 1);
    const tr = c1[0] + c2[1];
    const mu = Math.abs(tr) / 2 + Math.sqrt(tr * tr / 4 - 1);
    const s = Math.log(mu) / T;
    console.log('  ' + pad(f(h, 3), 10) + padl(f(s, 8), 18) + padl(f(h * w0 / 4, 8), 14)
      + padl(f(s / (h * w0 / 4), 5), 10));
  }
  console.log('  （成長率は一周期の単値行列 M の固有値から s = ln|mu| / T として取った）');
  console.log('');
  console.log('  ★ 揺すりは w = 2 、 答えは w0 = 1 ── ちょうど半分');
  console.log('  ★ 「係数が時間の関数」＝ パラメトリック。ここで初めて半分が出る');
}

// ============================================================
head('3. フロケ乗数で見る ── 周期倍分岐は mu = -1 を通る');
// ============================================================
// 一周期の単値行列 M。det M = 1（第 36 回）。tr M < -2 が周期倍の不安定
function monodromy(w0, h, w) {
  const T = 2 * Math.PI / w, dt = T / 200000;
  const c1 = mathieu(w0, h, w, T, dt, 1, 0);
  const c2 = mathieu(w0, h, w, T, dt, 0, 1);
  return [[c1[0], c2[0]], [c1[1], c2[1]]];
}
{
  const w0 = 1;
  console.log('');
  console.log('  ' + pad('h', 8) + pad('w', 8) + padl('det M', 14) + padl('tr M', 14)
    + padl('|mu| 最大', 14) + '  判定');
  for (const [h, w] of [[0.1, 1.6], [0.1, 1.9], [0.1, 2.0], [0.1, 2.1], [0.1, 2.4], [0.3, 2.0]]) {
    const M = monodromy(w0, h, w);
    const det = M[0][0] * M[1][1] - M[0][1] * M[1][0];
    const tr = M[0][0] + M[1][1];
    let mu, judge;
    if (Math.abs(tr) <= 2) { mu = 1; judge = '安定（|mu|=1）'; }
    else {
      const d = Math.sqrt(tr * tr / 4 - det);
      const m1 = Math.abs(tr / 2 + d), m2 = Math.abs(tr / 2 - d);
      mu = Math.max(m1, m2);
      judge = (tr < -2) ? '★ 周期倍（mu < -1）' : '不安定（mu > 1）';
    }
    console.log('  ' + pad(f(h, 2), 8) + pad(f(w, 2), 8) + padl(f(det, 9), 14)
      + padl(f(tr, 8), 14) + padl(f(mu, 8), 14) + '  ' + judge);
  }
  console.log('');
  console.log('  ★ det M = 1（第 36 回と同じ。ハミルトン系なので面積が保存）');
  console.log('  ★ tr M が -2 を下回る所で mu = -1 を通る ── これが「周期が 2 倍になる」');
  console.log('  ★ mu = -1 ＝ 一周期で符号が反転 ＝ 二周期で元に戻る');
}

// ============================================================
head('4. 破れた対称性は、二つの状態として見える');
// ============================================================
// 散逸つきパラメトリック発振：x'' + g x' + w0^2(1 + h cos 2w0 t) x + b x^3 = 0
function pardamp(g, w0, h, b, T, dt, x0, v0) {
  let x = x0, v = v0, t = 0;
  const n = Math.round(T / dt);
  const F = (t, x, v) => -g * v - w0 * w0 * (1 + h * Math.cos(2 * w0 * t)) * x - b * x * x * x;
  for (let i = 0; i < n; i++) {
    const k1x = v, k1v = F(t, x, v);
    const k2x = v + dt / 2 * k1v, k2v = F(t + dt / 2, x + dt / 2 * k1x, v + dt / 2 * k1v);
    const k3x = v + dt / 2 * k2v, k3v = F(t + dt / 2, x + dt / 2 * k2x, v + dt / 2 * k2v);
    const k4x = v + dt * k3v, k4v = F(t + dt, x + dt * k3x, v + dt * k3v);
    x += dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x);
    v += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v);
    t += dt;
  }
  return [x, v, t];
}
{
  const g = 0.05, w0 = 1, b = 1.0;
  const hth = 2 * g / w0;
  console.log('');
  console.log('  x\'\' + g x\' + w0^2(1 + h cos 2w0 t) x + b x^3 = 0');
  console.log('  しきい値 h_th = 2 g / w0 = ' + f(hth, 4) + '（これ以下では立ち上がらない）');
  console.log('');
  console.log('  ' + pad('h', 8) + pad('x0=+0.01 の終状態', 30) + pad('x0=-0.01 の終状態', 30)
    + '位相差');
  for (const h of [0.05, 0.15, 0.3]) {
    const T = 2000, dt = 2e-3;
    const A = pardamp(g, w0, h, b, T, dt, +0.01, 0);
    const B = pardamp(g, w0, h, b, T, dt, -0.01, 0);
    const amp = Math.sqrt(A[0] * A[0] + A[1] * A[1] / (w0 * w0));
    let ph = '-';
    if (amp > 1e-3) {
      const pa = Math.atan2(A[1] / w0, A[0]), pb = Math.atan2(B[1] / w0, B[0]);
      let dd = Math.abs(pa - pb); if (dd > Math.PI) dd = 2 * Math.PI - dd;
      ph = f(dd, 6) + ' rad';
    }
    console.log('  ' + pad(f(h, 3), 8) + pad('x=' + f(A[0], 5) + ' v=' + f(A[1], 5), 30)
      + pad('x=' + f(B[0], 5) + ' v=' + f(B[1], 5), 30) + ph);
  }
  console.log('');
  console.log('  ★ h > h_th で振動が立ち、位相は pi 違う二つのどちらかに落ちる');
  console.log('  ★ 「二つある」＝ 離散時間並進対称性 Z2 が破れている ということ');
  console.log('  ★ そして立ち上がるには散逸を越える必要がある ── 第 32 回と同じ構図');
}

// ============================================================
head('5. ★ 剛性 ── 蹴り角をずらしても、応答は 1/2 に居座るか');
// ============================================================
// 古典スピン鎖：各周期 (a) 近接相互作用による z 軸回り歳差、(b) x 軸回り角 pi(1-eps) の蹴り
function mulberry32(a) {
  return function () {
    a |= 0; a = a + 0x6D2B79F5 | 0;
    let t = Math.imul(a ^ a >>> 15, 1 | a);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}
function rotX(n, th) {
  const c = Math.cos(th), s = Math.sin(th);
  return [n[0], c * n[1] - s * n[2], s * n[1] + c * n[2]];
}
function rotZ(n, th) {
  const c = Math.cos(th), s = Math.sin(th);
  return [c * n[0] - s * n[1], s * n[0] + c * n[1], n[2]];
}
function run(N, steps, eps, J, seed) {
  const rnd = mulberry32(seed);
  const sp = [];
  for (let i = 0; i < N; i++) {
    // ほぼ +z 、わずかに乱す
    const a = (rnd() - 0.5) * 0.3, b = (rnd() - 0.5) * 0.3;
    const v = [a, b, 1]; const L = Math.hypot(v[0], v[1], v[2]);
    sp.push([v[0] / L, v[1] / L, v[2] / L]);
  }
  const Jl = [];
  for (let i = 0; i < N; i++) Jl.push(J * (0.6 + 0.8 * rnd()));  // 乱れた結合
  const th = Math.PI * (1 - eps);
  const M = [];
  for (let t = 0; t < steps; t++) {
    // (a) イジング歳差（同時更新）
    const z = sp.map(s => s[2]);
    const ns = [];
    for (let i = 0; i < N; i++) {
      const zl = z[(i - 1 + N) % N], zr = z[(i + 1) % N];
      ns.push(rotZ(sp[i], Jl[i] * (zl + zr)));
    }
    // (b) 蹴り
    for (let i = 0; i < N; i++) sp[i] = rotX(ns[i], th);
    let m = 0; for (let i = 0; i < N; i++) m += sp[i][2];
    M.push(m / N);
  }
  return M;
}
{
  const N = 40, steps = 4096;
  console.log('');
  console.log('  各周期： (a) 乱れたイジング結合で z 軸回り歳差 → (b) x 軸回り pi(1-eps) の蹴り');
  console.log('  自由なら M_z のピークは (1-eps)/2 にずれるはず。相互作用があるとどうか。');
  console.log('');
  console.log('  ' + pad('eps', 10) + padl('J=0（相互作用なし）', 22)
    + padl('J=0.6（あり）', 20) + padl('ずれ（J=0.6）', 16));
  for (const eps of [0.0, 0.02, 0.05, 0.10, 0.15, 0.25]) {
    const M0 = run(N, steps, eps, 0.0, 12345);
    const M1 = run(N, steps, eps, 0.6, 12345);
    const p0 = peakFreq(M0.slice(512), 0.30, 0.50, 800);
    const p1 = peakFreq(M1.slice(512), 0.30, 0.50, 800);
    console.log('  ' + pad(f(eps, 3), 10) + padl(f(p0.f, 6), 22) + padl(f(p1.f, 6), 20)
      + padl(e(Math.abs(p1.f - 0.5), 2), 16));
  }
  console.log('');
  console.log('  予言（相互作用なし）： (1-eps)/2 = 0.5, 0.49, 0.475, 0.45, 0.425, 0.375');
}

// ============================================================
head('6. 剛性の幅 ── どこまでずらすと外れるか');
// ============================================================
{
  const N = 40, steps = 4096;
  console.log('');
  console.log('  ' + pad('eps', 10) + padl('ピーク位置', 16) + padl('|f-0.5|', 14)
    + padl('1/2 の振幅', 16) + '  判定');
  let lock = 0;
  for (const eps of [0, 0.02, 0.05, 0.08, 0.12, 0.18, 0.25, 0.35, 0.5]) {
    const M = run(N, steps, eps, 0.6, 777).slice(512);
    const p = peakFreq(M, 0.25, 0.50, 1000);
    const amp = dftMag(M, 0.5);
    const locked = Math.abs(p.f - 0.5) < 2e-3 && amp > 0.02;
    if (locked) lock = eps;
    console.log('  ' + pad(f(eps, 3), 10) + padl(f(p.f, 6), 16)
      + padl(e(Math.abs(p.f - 0.5), 2), 14) + padl(f(amp, 6), 16)
      + '  ' + (locked ? '★ ロック' : '外れ'));
  }
  console.log('');
  console.log('  ★ ロックが保たれた最大の eps = ' + f(lock, 3)
    + '  ── これが「剛性」の幅');
}

// ============================================================
head('7. なぜ平衡では作れないか ── 受動性の言葉で');
// ============================================================
console.log('');
console.log('  第 17・18 回：受動的な系は Re Z >= 0。エネルギーを出せない。');
console.log('  自発的に振動が立つには、どこかに Re Z < 0（負性抵抗）が要る。');
console.log('  負性抵抗は外からエネルギーを入れないと作れない ── つまり平衡では無理。');
console.log('');
// 04 節のしきい値がまさにそれ：h > 2 g / w0
console.log('  ' + pad('減衰 g', 12) + padl('しきい値 h_th = 2g/w0', 24)
  + padl('意味', 28));
for (const g of [0.01, 0.05, 0.1, 0.3]) {
  console.log('  ' + pad(f(g, 3), 12) + padl(f(2 * g, 6), 24)
    + padl('これ以下では立たない', 28));
}
console.log('');
console.log('  ★ 散逸が大きいほど、強く揺すらないと立たない');
console.log('  ★ 「揺すり（外部）」と「散逸」が両方 要る ── だから平衡時間結晶は不可能');
console.log('  ★ 第 32 回「対称性の破れには散逸が要る」の、時間方向での繰り返し');

// ============================================================
head('8. 周波数を作れるのは誰か ── 三段の整理');
// ============================================================
console.log('');
console.log('  ' + pad('系', 30) + pad('出る周波数', 26) + '回');
const tiers = [
  ['線形・時不変（LTI）', '入力の周波数のみ', '第 1 回'],
  ['非線形・時不変', 'n w （整数倍）と混変調', '第 23 回'],
  ['線形・時間周期（パラメトリック）', 'w/2 、 w の有理数倍', '★ 第 36・40 回'],
  ['非線形＋時間周期＋散逸', '★ w/n が「剛く」立つ', '★ 本回'],
];
for (const t of tiers) console.log('  ' + pad(t[0], 30) + pad(t[1], 26) + t[2]);
console.log('');
console.log('  ★ 時間結晶が「新しい相」と呼ばれるのは、最下段だけが');
console.log('  ★ 「ずらしても戻ってくる」＝ 剛性 を持つから。');

// ============================================================
head('9. 本回のまとめ');
// ============================================================
const rows = [
  ['LTI から分数調波は出ない', '◎ 数値', '★ 丸め誤差の底まで落ちる'],
  ['★ パラメトリックなら出る', '◎ 数値', '成長率 = h w0/4 と一致'],
  ['det M = 1 、周期倍は mu=-1', '◎ 数値', '第 36 回の続き'],
  ['破れた対称性 = 二つの状態', '◎ 数値', '位相差ちょうど pi'],
  ['★ 剛性（ずらしても 1/2）', '◎ 数値', '★ 相互作用がある時だけ'],
  ['剛性の幅を実測', '◎ 数値', '★ アーノルドの舌の幅'],
  ['平衡では不可能', '◎ 解析', 'Re Z >= 0（第 17・18 回）'],
  ['★ 量子の時間結晶そのもの', '× 扱えない', '★ 本稿は古典のみ'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 32) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 時間結晶とは、「半分の周波数」が出ることではなく、');
console.log('  ★ 「半分の周波数が ずらしても戻ってくる」ことだった。');
console.log('  ★ 半分を出すだけならマシュー方程式で足りる。剛性が要る。');
