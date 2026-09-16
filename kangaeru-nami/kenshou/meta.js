// 考える波 第 44 回：メタマテリアル ── 媒質を自分で作る
//   負の屈折率、バンドギャップ、遅い光、そして「時間方向の周期構造」
//   node meta.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

// ---- 複素数（最低限） ----
const C = {
  add: (a, b) => [a[0] + b[0], a[1] + b[1]],
  sub: (a, b) => [a[0] - b[0], a[1] - b[1]],
  mul: (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]],
  div: (a, b) => { const d = b[0] * b[0] + b[1] * b[1];
    return [(a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d]; },
  abs: (a) => Math.hypot(a[0], a[1]),
  sqrtP: (a) => {                       // 主値（偏角を (-pi, pi] に取る）
    const r = Math.hypot(a[0], a[1]), th = Math.atan2(a[1], a[0]);
    return [Math.sqrt(r) * Math.cos(th / 2), Math.sqrt(r) * Math.sin(th / 2)];
  },
};

console.log('考える波 第 44 回 ── メタマテリアル');
console.log('媒質を自分で作る。ただし作ってよいものは決まっている');

// ============================================================
head('1. 負の屈折率 ── 符号を決めるのは「損があること」');
// ============================================================
// n^2 = eps mu 。 eps, mu がともに負のとき、n = +sqrt か -sqrt か
console.log('');
console.log('  n^2 = eps · mu。eps も mu も負なら n^2 > 0 なので、符号は 2 通りある。');
console.log('  決めるのは「損を入れたとき、波が 減衰する側」── つまり Im n > 0。');
console.log('');
console.log('  ' + pad('eps', 22) + pad('mu', 22) + padl('主値 sqrt(eps mu)', 22)
  + '  ★ 正しい n');
for (const [er, mr, g] of [[1, 1, 0.01], [-1, 1, 0.01], [1, -1, 0.01],
                           [-1, -1, 0.01], [-2, -0.5, 0.01], [-4, -1, 1e-4]]) {
  const eps = [er, g], mu = [mr, g];
  const n2 = C.mul(eps, mu);
  const np = C.sqrtP(n2);
  const nn = (np[1] >= 0) ? np : [-np[0], -np[1]];   // Im n > 0 の側を選ぶ
  const lab = (er < 0 && mr < 0) ? '★ Re n < 0（負屈折）'
    : (n2[0] < 0 ? 'エバネッセント（Re n ~ 0）' : '普通');
  console.log('  ' + pad(f(er, 2) + ' + ' + f(g, 4) + 'i', 22)
    + pad(f(mr, 2) + ' + ' + f(g, 4) + 'i', 22)
    + padl(f(np[0], 5) + ' + ' + f(np[1], 5) + 'i', 22) + '  '
    + f(nn[0], 5) + ' + ' + f(nn[1], 5) + 'i  ' + lab);
}
console.log('');
console.log('  ★★ eps<0 かつ mu<0 だけが Re n < 0 になる。片方だけなら n はほぼ純虚数');
console.log('  ★★ ＝ 第 28 回のエバネッセント（k^2 < 0 で進めない波）');
console.log('  ★ そして符号を決めたのは「損」── 第 8 回の因果律が効いている');

// ============================================================
head('2. 分散なしには作れない ── エネルギーが負になってしまう');
// ============================================================
// 分散性媒質のエネルギー密度： u ∝ d(omega eps)/d omega  |E|^2 + d(omega mu)/d omega |H|^2
// これが正でなければならない。 eps < 0 を分散なしで作ると u < 0。
function drude(w, wp) { return 1 - wp * wp / (w * w); }
{
  const wp = 1;
  console.log('');
  console.log('  ドルーデ： eps(w) = 1 - wp^2/w^2 （wp = 1）');
  console.log('  エネルギーの条件： d(w eps)/dw > 0');
  console.log('');
  console.log('  ' + pad('w/wp', 10) + padl('eps', 14) + padl('d(w eps)/dw', 18)
    + padl('分散なしなら', 16) + '  判定');
  for (const w of [0.3, 0.5, 0.8, 1.0, 1.5, 3.0]) {
    const eps = drude(w, wp);
    const h = 1e-6;
    const d = ((w + h) * drude(w + h, wp) - (w - h) * drude(w - h, wp)) / (2 * h);
    console.log('  ' + pad(f(w, 2), 10) + padl(f(eps, 6), 14) + padl(f(d, 6), 18)
      + padl(f(eps, 6), 16) + '  ' + (d > 0 ? 'OK' : '★ 禁止')
      + (eps < 0 ? '  （eps<0 だが d(w eps)/dw>0）' : ''));
  }
  console.log('');
  console.log('  ★ eps が負でも d(w eps)/dw = 1 + wp^2/w^2 は必ず正 ── 分散のおかげ');
  console.log('  ★★ 逆に言うと「分散のない負の eps」は作れない。');
  console.log('  ★★ 負屈折の媒質が必ず 狭帯域 なのは、これが理由');
}

// ============================================================
head('3. 総和則 ── 「全部の周波数で得をする」ことはできない');
// ============================================================
// f 総和則： ∫_0^inf w Im eps(w) dw = (pi/2) wp^2
// ローレンツ振動子で数値確認
function lorentzIm(w, wp, w0, g) {
  const d = (w0 * w0 - w * w), den = d * d + (g * w) * (g * w);
  return wp * wp * g * w / den;
}
{
  const wp = 1, w0 = 2, g = 0.1;
  const N = 4000000, wmax = 4000, h = wmax / N;
  let s = 0;
  for (let i = 0; i < N; i++) { const w = (i + 0.5) * h; s += w * lorentzIm(w, wp, w0, g) * h; }
  console.log('');
  console.log('  ローレンツ振動子（wp=1, w0=2, gamma=0.1）');
  console.log('  ' + pad('∫ w Im eps dw（数値）', 30) + padl(f(s, 8), 16));
  console.log('  ' + pad('(pi/2) wp^2（理論）', 30) + padl(f(Math.PI / 2, 8), 16));
  console.log('  ' + pad('比', 30) + padl(f(s / (Math.PI / 2), 8), 16));
  console.log('');
  console.log('  ★★ 右辺は w0 にも gamma にも依らない ── 共振をどこに置いても総量は同じ');
  console.log('  ★ 「ある周波数で強くしたら、別の周波数で弱くなる」が式で言えている');
  console.log('  ★ 第 8 回（クラマース＝クローニッヒ）の帰結。設計の上限そのもの');
}

// ============================================================
head('4. 一次元フォトニック結晶 ── バンドギャップと 遅い光');
// ============================================================
// 層 1（n1, d1）と層 2（n2, d2）の繰り返し。転送行列の trace でバンドを決める
function blochCos(w, n1, d1, n2, d2) {
  const k1 = w * n1, k2 = w * n2;
  const p1 = k1 * d1, p2 = k2 * d2;
  // tr M / 2
  return Math.cos(p1) * Math.cos(p2)
    - 0.5 * (n1 / n2 + n2 / n1) * Math.sin(p1) * Math.sin(p2);
}
{
  const d1 = 0.5, d2 = 0.5, L = d1 + d2;
  console.log('');
  console.log('  層 1（n1, 厚み 0.5）と層 2（n2, 厚み 0.5）の繰り返し');
  console.log('  |tr M / 2| > 1 の所がバンドギャップ（＝進めない ＝ エバネッセント）');
  console.log('');
  console.log('  ' + pad('n2/n1', 10) + padl('第 1 ギャップの下端', 20)
    + padl('上端', 14) + padl('★ 相対幅', 14));
  for (const n2 of [1.05, 1.2, 1.5, 2.0, 3.0]) {
    const n1 = 1;
    // w を上げていって |tr/2| が 1 を越える所と戻る所を探す
    let lo = null, hi = null;
    const N = 400000, wmax = 8;
    let prev = Math.abs(blochCos(1e-6, n1, d1, n2, d2));
    for (let i = 1; i <= N; i++) {
      const w = wmax * i / N;
      const v = Math.abs(blochCos(w, n1, d1, n2, d2));
      if (lo === null && prev <= 1 && v > 1) lo = w;
      else if (lo !== null && hi === null && prev > 1 && v <= 1) hi = w;
      prev = v;
    }
    const rel = (hi - lo) / ((hi + lo) / 2);
    console.log('  ' + pad(f(n2 / n1, 2), 10) + padl(f(lo, 6), 20) + padl(f(hi, 6), 14)
      + padl(f(rel, 6), 14));
  }
  console.log('');
  // バンド端での群速度
  const n1 = 1, n2 = 2;
  console.log('  第 1 バンドの上端（w = 1.68214）へ近づくと 群速度が 0 へ： n2 = 2');
  console.log('  ' + pad('w', 12) + padl('K L（ブロッホ位相）', 22) + padl('★ v_g / c', 14));
  const wl = [0.5, 1.0, 1.4, 1.6, 1.67, 1.680, 1.6820];
  for (const w of wl) {
    const c0 = blochCos(w, n1, d1, n2, d2);
    if (Math.abs(c0) > 1) { console.log('  ' + pad(f(w, 3), 12) + padl('ギャップの中', 22)
      + padl('-', 14)); continue; }
    const K = Math.acos(c0) / L;
    const h = 1e-7;
    const cp = blochCos(w + h, n1, d1, n2, d2), cm = blochCos(w - h, n1, d1, n2, d2);
    if (Math.abs(cp) > 1 || Math.abs(cm) > 1) continue;
    const Kp = Math.acos(cp) / L, Km = Math.acos(cm) / L;
    const vg = (2 * h) / (Kp - Km);
    console.log('  ' + pad(f(w, 3), 12) + padl(f(K * L, 8), 22) + padl(f(vg, 6), 14));
  }
  console.log('');
  console.log('  ★ ギャップの中は「進めない」── 第 28 回の k^2<0 と同じ状態');
  console.log('  ★ ギャップの端では v_g → 0 ── 遅い光。ただし帯域も 0 に近づく');
}

// ============================================================
head('5. 遅延と帯域は交換できない ── 遅い光の代償');
// ============================================================
// ローレンツ共振の群遅延と、その帯域の積
{
  const wp = 0.3, w0 = 1;
  console.log('');
  console.log('  ローレンツ媒質（長さ 1）の群遅延と、透過帯域の積');
  console.log('');
  console.log('  ' + pad('gamma', 10) + padl('最大群遅延 tau', 18)
    + padl('帯域 dw', 14) + padl('★ tau · dw', 14));
  for (const g of [0.4, 0.2, 0.1, 0.05, 0.025]) {
    // n(w) = sqrt(1 + wp^2/(w0^2 - w^2 - i g w)) の実部から群速度
    const nre = (w) => {
      const den = [w0 * w0 - w * w, -g * w];
      const chi = C.div([wp * wp, 0], den);
      const n = C.sqrtP([1 + chi[0], chi[1]]);
      return n[0];
    };
    const tau = (w) => { const h = 1e-5; return nre(w) + w * (nre(w + h) - nre(w - h)) / (2 * h); };
    // 共振の外側（w0 より少し下）で群遅延が最大になる所を探す
    let best = 0, bw = 0;
    for (let i = 1; i < 20000; i++) {
      const w = 0.2 + 0.8 * i / 20000;
      const t = tau(w);
      if (t > best) { best = t; bw = w; }
    }
    // 帯域は gamma で決まる
    console.log('  ' + pad(f(g, 4), 10) + padl(f(best, 6), 18) + padl(f(g, 6), 14)
      + padl(f(best * g, 6), 14));
  }
  console.log('');
  console.log('  ★ 遅延だけなら 1.11 → 15.92 と 14 倍 に伸ばせる（gamma を 16 分の 1 に）');
  console.log('  ★★ ところが 積は 0.44 → 0.22 → 0.40 と、2 倍の幅にしか動かない。');
  console.log('  ★ 正直に：単調ではありません（gamma=0.1 付近で最小）。');
  console.log('  ★ それでも「16 倍 変えて 積は 2 倍以内」── 遅延を稼げば帯域を失う。');
  console.log('  ★ これも第 8 回（因果律）と第 9 回（帯域幅定理）の帰結');

}

// ============================================================
head('6. ★ 時間方向に周期構造を作る ── 運動量のギャップ');
// ============================================================
// 空間が周期的 → 周波数のギャップ（4 節）
// 時間が周期的 → ★ 運動量（k）のギャップ。しかも中では 増幅する
// d^2E/dt^2 + c^2 k^2 / eps(t) · E = 0 、 1/eps(t) = 1 + h cos(Om t)
function floquetK(k, h, Om, c) {
  const T = 2 * Math.PI / Om, N = 200000, dt = T / N;
  const F = (t, x, v) => [v, -c * c * k * k * (1 + h * Math.cos(Om * t)) * x];
  const run = (x0, v0) => {
    let x = x0, v = v0, t = 0;
    for (let i = 0; i < N; i++) {
      const a = F(t, x, v);
      const b = F(t + dt / 2, x + dt / 2 * a[0], v + dt / 2 * a[1]);
      const cc = F(t + dt / 2, x + dt / 2 * b[0], v + dt / 2 * b[1]);
      const d = F(t + dt, x + dt * cc[0], v + dt * cc[1]);
      x += dt / 6 * (a[0] + 2 * b[0] + 2 * cc[0] + d[0]);
      v += dt / 6 * (a[1] + 2 * b[1] + 2 * cc[1] + d[1]);
      t += dt;
    }
    return [x, v];
  };
  const c1 = run(1, 0), c2 = run(0, 1);
  const tr = c1[0] + c2[1];
  const det = c1[0] * c2[1] - c2[0] * c1[1];
  let mu = 1;
  if (Math.abs(tr) > 2) mu = Math.abs(tr) / 2 + Math.sqrt(tr * tr / 4 - 1);
  return { tr: tr, det: det, mu: mu, rate: Math.log(mu) / T };
}
{
  const c = 1, Om = 2, h = 0.1;
  console.log('');
  console.log('  1/eps(t) = 1 + h cos(Om t) 、 h = 0.1 、 Om = 2 、 c = 1');
  console.log('  各 k について 一周期の単値行列を作り、|mu| > 1 なら「運動量ギャップ」');
  console.log('');
  console.log('  ' + pad('k', 10) + padl('det M', 12) + padl('tr M', 14)
    + padl('|mu|', 12) + padl('成長率', 14) + '  判定');
  for (const k of [0.7, 0.9, 0.95, 1.0, 1.05, 1.1, 1.3]) {
    const r = floquetK(k, h, Om, c);
    console.log('  ' + pad(f(k, 3), 10) + padl(f(r.det, 6), 12) + padl(f(r.tr, 6), 14)
      + padl(f(r.mu, 6), 12) + padl(f(r.rate, 6), 14) + '  '
      + (r.mu > 1 + 1e-9 ? '★ ギャップ（増幅）' : '通る'));
  }
  console.log('');
  console.log('  ★ ギャップの中心は k = Om/(2c) = ' + f(Om / (2 * c), 3)
    + '  ── 第 40 回のパラメトリックと同じ条件');
  console.log('  ★ 予言： 中心での成長率 = h c k / 4 = '
    + f(h * c * (Om / (2 * c)) / 4, 6));
  console.log('');
  console.log('  ' + pad('空間が周期的（4 節）', 30) + '周波数のギャップ。中では 減衰');
  console.log('  ' + pad('★ 時間が周期的（本節）', 30) + '★ 運動量のギャップ。中では 増幅');
  console.log('');
  console.log('  ★★ 減衰か増幅かの違いは、どちらの向きに「進めない」かの違い');
  console.log('  ★★ 空間で進めない ＝ 減る。時間で進めない ＝ 育つ。');
}

// ============================================================
head('7. 作ってはいけないもの ── 三つの門番');
// ============================================================
console.log('');
const gates = [
  ['受動性（第 17・18 回）', 'Re Z >= 0', '外から入れずに増幅はできない'],
  ['オストログラツキー（第 29 回）', '時間微分は 2 階まで', '3 階以上は 必ず不安定'],
  ['総和則（第 8 回・本回 3 節）', '∫ w Im eps dw 一定', 'どこかで強くすれば どこかで弱くなる'],
];
console.log('  ' + pad('門番', 30) + pad('条件', 24) + '意味');
for (const g of gates) console.log('  ' + pad(g[0], 30) + pad(g[1], 24) + g[2]);
console.log('');
console.log('  ★ メタマテリアルが「自由に作れる」のは、この三つの外側だけ。');
console.log('  ★★ 負屈折は 三つとも破っていません ── だから作れた。');
console.log('  ★★ 「完全レンズ」が難しいのは、損（Im eps）を 0 にできないから。');

// ============================================================
head('8. 本回のまとめ');
// ============================================================
const rows = [
  ['n の符号は損が決める', '◎ 数値', '★ eps<0 かつ mu<0 のときだけ Re n<0'],
  ['分散なしの eps<0 は禁止', '◎ 数値', 'd(w eps)/dw > 0'],
  ['総和則', '◎ 数値', '★ (pi/2) wp^2 と 4 桁一致'],
  ['バンドギャップ＝進めない帯', '◎ 数値', '|tr M/2| > 1'],
  ['バンド端で v_g → 0', '◎ 数値', '遅い光'],
  ['★ 遅延×帯域 の交換', '○ 数値', '★ gamma 16 倍 で 積は 2 倍以内'],
  ['★ 時間周期 → 運動量ギャップ', '◎ 数値', '★ しかも中では 増幅'],
  ['★ 実際の素子の設計', '× 扱えない', '★ 本稿は一次元の模型のみ'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 34) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ メタマテリアルとは「分散関係を設計すること」だった。');
console.log('  ★ 空間に周期を入れれば 周波数のギャップ、');
console.log('  ★ 時間に周期を入れれば 運動量のギャップ ── そして そこでは 育つ。');
