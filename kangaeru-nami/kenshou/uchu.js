// 考える波 第 47 回：宇宙そのものを波として見る
//   インフレーション ── 第 13 回の 1/tau^2 が、また出てくる
//   node uchu.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }
function slope(xs, ys) {
  const n = xs.length; let sx = 0, sy = 0, sxx = 0, sxy = 0;
  for (let i = 0; i < n; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
  return (n * sxy - sx * sy) / (n * sxx - sx * sx);
}

console.log('考える波 第 47 回 ── 宇宙そのものを波として見る');
console.log('インフレーションの式は、第 13 回の 1/tau^2 そのものだった');

// ============================================================
head('1. ★ ムカノフ＝ササキ方程式は、第 13 回の式だった');
// ============================================================
// v'' + (k^2 - z''/z) v = 0 、 デシッターでは z''/z = (nu^2 - 1/4)/tau^2
// x = -k tau と置くと  v_xx + [1 - (nu^2-1/4)/x^2] v = 0  ← ★ k が消える
console.log('');
console.log('  ムカノフ＝ササキ： v\'\' + (k^2 - z\'\'/z) v = 0');
console.log('  デシッター背景： z\'\'/z = (nu^2 - 1/4)/tau^2 、 nu = 3/2 が厳密なデシッター');
console.log('');
console.log('  x = -k tau と置くと  v_xx + [ 1 - (nu^2 - 1/4)/x^2 ] v = 0');
console.log('  ★ k が式から消える ── 「どの波長でも同じ形」がスケール不変性の正体');
console.log('');
console.log('  x が小さいところ（地平線の外）では 1 が効かなくなり');
console.log('    v_xx - (nu^2-1/4)/x^2 v = 0  ← ★★ 第 13 回の 1/r^2 ポテンシャルそのもの');
console.log('    v ~ x^s 、 s(s-1) = nu^2 - 1/4  →  s = 1/2 ± nu');
console.log('');
console.log('  ' + pad('nu', 10) + padl('s = 1/2 ± nu', 22) + padl('第 13 回の lambda', 20)
  + padl('第 39 回の m^2L^2', 20));
for (const nu of [0.5, 1.0, 1.5, 2.0]) {
  // 第 13 回： s = 1/2 ± sqrt(1/4 - lambda) なので lambda = 1/4 - nu^2
  const lam = 0.25 - nu * nu;
  // 第 39 回： nu = sqrt(d^2/4 + m^2L^2) 、 d=3 とすると m^2L^2 = nu^2 - 9/4
  const mm = nu * nu - 2.25;
  console.log('  ' + pad(f(nu, 2), 10) + padl(f(0.5 + nu, 3) + ' , ' + f(0.5 - nu, 3), 22)
    + padl(f(lam, 4), 20) + padl(f(mm, 4) + '（d=3）', 20));
}
console.log('');
console.log('  ★★★ 第 13 回（臨界ポテンシャル）・第 39 回（AdS）・本回（インフレーション）が');
console.log('  ★★★ 同じ二次方程式の 三つの顔でした。');

// ============================================================
head('2. 実際に解いて、スペクトル指数を測る');
// ============================================================
// x = X（地平線の内側）から BD 初期条件で始めて、x = k|tau_end| まで積分
function solveV(nu, xStart, xEnd) {
  const A = nu * nu - 0.25;
  // BD： v = e^{i x}/sqrt(2k) 相当（k は外に出したので 1/sqrt(2) は共通）
  let vr = Math.cos(xStart), vi = Math.sin(xStart);
  let pr = -Math.sin(xStart), pi = Math.cos(xStart);   // dv/dx
  let x = xStart;
  const F = (x, v, p) => [p, -(1 - A / (x * x)) * v];
  while (x > xEnd) {
    let h = Math.min(0.002, x / 4000);
    if (x - h < xEnd) h = x - xEnd;
    // 実部
    let a = F(x, vr, pr);
    let b = F(x - h / 2, vr - h / 2 * a[0], pr - h / 2 * a[1]);
    let c = F(x - h / 2, vr - h / 2 * b[0], pr - h / 2 * b[1]);
    let d = F(x - h, vr - h * c[0], pr - h * c[1]);
    const nvr = vr - h / 6 * (a[0] + 2 * b[0] + 2 * c[0] + d[0]);
    const npr = pr - h / 6 * (a[1] + 2 * b[1] + 2 * c[1] + d[1]);
    // 虚部
    a = F(x, vi, pi);
    b = F(x - h / 2, vi - h / 2 * a[0], pi - h / 2 * a[1]);
    c = F(x - h / 2, vi - h / 2 * b[0], pi - h / 2 * b[1]);
    d = F(x - h, vi - h * c[0], pi - h * c[1]);
    const nvi = vi - h / 6 * (a[0] + 2 * b[0] + 2 * c[0] + d[0]);
    const npi = pi - h / 6 * (a[1] + 2 * b[1] + 2 * c[1] + d[1]);
    vr = nvr; pr = npr; vi = nvi; pi = npi;
    x -= h;
  }
  return Math.sqrt(vr * vr + vi * vi);
}
{
  console.log('');
  console.log('  |tau_end| = 1 に固定し、k を変えて P(k) = k^2 |v(x=k)|^2 を測る');
  console.log('  予言： P(k) ∝ k^{3-2nu} 、 つまり n_s - 1 = 3 - 2 nu');
  console.log('');
  console.log('  ' + pad('nu', 10) + padl('傾き（実測）', 18) + padl('3 - 2 nu', 14)
    + padl('差', 12) + padl('n_s', 10));
  const ks = [1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3];
  for (const nu of [1.5, 1.45, 1.4, 1.6]) {
    const xs = [], ys = [];
    for (const k of ks) {
      const v = solveV(nu, 400, k);
      xs.push(Math.log(k)); ys.push(Math.log(k * k * v * v));
    }
    const sl = slope(xs, ys);
    console.log('  ' + pad(f(nu, 3), 10) + padl(f(sl, 8), 18) + padl(f(3 - 2 * nu, 6), 14)
      + padl(e(Math.abs(sl - (3 - 2 * nu)), 2), 12) + padl(f(1 + 3 - 2 * nu, 5), 10));
  }
  console.log('');
  console.log('  ★ nu = 3/2 ちょうどで n_s = 1（完全なスケール不変）');
  console.log('  ★ nu を 3/2 から ほんの少しずらすと、n_s が 1 から少しずれる');
}

// ============================================================
head('3. 地平線を出ると、凍りつく');
// ============================================================
// zeta = v/z 、 z ∝ (-tau)^{1/2-nu} なので |zeta| ∝ |v| x^{nu-1/2}
{
  const nu = 1.5;
  console.log('');
  console.log('  曲率ゆらぎ zeta = v/z 、 z ∝ (-tau)^{1/2-nu}');
  console.log('  → |zeta| ∝ |v(x)| · x^{nu - 1/2}   （nu = 1.5）');
  console.log('');
  console.log('  ' + pad('x = k|tau|', 14) + padl('|v(x)|', 16) + padl('★ |zeta| ∝ |v| x^{nu-1/2}', 28)
    + '  状態');
  for (const x of [10, 3, 1, 0.3, 0.1, 0.03, 0.01]) {
    const v = solveV(nu, 400, x);
    const z = v * Math.pow(x, nu - 0.5);
    console.log('  ' + pad(f(x, 3), 14) + padl(f(v, 8), 16) + padl(f(z, 10), 28)
      + '  ' + (x > 1 ? '地平線の内側（振動）' : '★ 地平線の外（凍る）'));
  }
  console.log('');
  console.log('  ★★ x < 1 になると |zeta| が 一定になる ── これが「凍りつく」');
  console.log('  ★ 地平線を出たゆらぎは、もう変化しない。だから 38 万年後まで残る。');
  console.log('  ★ 波の言葉では「進めなくなった波」── 第 28 回のエバネッセントの親戚');
}

// ============================================================
head('4. 模型ごとの n_s と r ── 観測と比べる');
// ============================================================
// V ∝ phi^p のとき（M_pl = 1）： eps = p/(4N) 、 eta = (p-1)/(2N)
//   n_s - 1 = -6 eps + 2 eta = -(p+2)/(2N) 、 r = 16 eps = 4p/N
{
  console.log('');
  console.log('  観測（プランク衛星ほか）： n_s = 0.9649 ± 0.0042 、 r < 0.036');
  console.log('');
  console.log('  ' + pad('模型', 24) + pad('N', 6) + padl('n_s', 12) + padl('r', 12)
    + '  判定');
  const rows = [];
  for (const [p, lab] of [[2, 'V ∝ phi^2'], [4, 'V ∝ phi^4'], [1, 'V ∝ phi^1']]) {
    for (const N of [50, 60]) {
      const ns = 1 - (p + 2) / (2 * N), r = 4 * p / N;
      rows.push([lab, N, ns, r]);
    }
  }
  // スタロビンスキー型（R^2）： n_s - 1 = -2/N 、 r = 12/N^2
  for (const N of [50, 60]) rows.push(['スタロビンスキー (R^2)', N, 1 - 2 / N, 12 / (N * N)]);
  for (const [lab, N, ns, r] of rows) {
    const okns = Math.abs(ns - 0.9649) < 3 * 0.0042;
    const okr = r < 0.036;
    console.log('  ' + pad(lab, 24) + pad(N, 6) + padl(f(ns, 6), 12) + padl(f(r, 6), 12)
      + '  ' + (okns ? 'n_s ◎' : 'n_s ×') + ' / ' + (okr ? 'r ◎' : '★ r 棄却'));
  }
  console.log('');
  console.log('  ★★ n_s だけ見ると phi^2 も通るが、r で棄却される');
  console.log('  ★★ 「指数が一つ合った」だけでは足りない ── 第 42 回と同じ教訓');
}

// ============================================================
head('5. ★ n_s を dB/oct に直す ── 宇宙の「傾き」の大きさ');
// ============================================================
{
  console.log('');
  console.log('  P(k) ∝ k^{n_s-1} 。 振幅は k^{(n_s-1)/2} なので');
  console.log('    dB/oct = 6 × (n_s-1)/2 = 3 (n_s - 1)');
  console.log('');
  console.log('  ' + pad('量', 34) + padl('値', 16) + padl('dB/oct', 14));
  const ns = 0.9649, dns = 0.0042;
  console.log('  ' + pad('n_s（観測）', 34) + padl(f(ns, 4) + ' ± ' + f(dns, 4), 16)
    + padl(f(3 * (ns - 1), 5), 14));
  console.log('  ' + pad('誤差', 34) + padl('± ' + f(dns, 4), 16)
    + padl('± ' + f(3 * dns, 5), 14));
  console.log('  ' + pad('n_s = 1（完全スケール不変）', 34) + padl('1.0000', 16)
    + padl('0.00000', 14));
  console.log('');
  console.log('  ★★★ 宇宙の原始ゆらぎは 傾き ' + f(3 * (ns - 1), 4)
    + ' dB/oct（誤差 ±' + f(3 * dns, 4) + '）');
  console.log('  ★★★ 第 42 回の「乱流の間欠性は 0.081 dB/oct」と 同じ桁！');
  console.log('');
  console.log('  ' + pad('物理', 30) + padl('傾きのずれ [dB/oct]', 22) + '  何からのずれか');
  console.log('  ' + pad('★ 宇宙の原始ゆらぎ', 30) + padl(f(3 * (ns - 1), 4), 22)
    + '  ★ 完全スケール不変（n_s=1）から');
  console.log('  ' + pad('★ 乱流の間欠性', 30) + padl('+0.0812', 22)
    + '  ★ コルモゴロフ（-5/3）から');
  console.log('');
  console.log('  ★★ 物理でいちばん精密に測られた「傾きのずれ」が、どちらも 0.1 dB/oct 級。');
  console.log('  ★ そして どちらも「ずれていること」自体が 理論の中身を語っている：');
  console.log('  ★ 宇宙では「インフレーションが 有限時間で終わったこと」、');
  console.log('  ★ 乱流では「カスケードが 掛け算であること」。');
}

// ============================================================
head('6. 何 e 倍 必要か ── 地平線問題');
// ============================================================
{
  console.log('');
  console.log('  いま見える宇宙が、インフレーション開始時に 地平線の内側に入っていた条件');
  console.log('');
  console.log('  ' + pad('項目', 30) + padl('値', 20));
  const Trh = 1e15;               // 再加熱温度 [GeV]（例）
  const T0 = 2.35e-13;            // いまの CMB 温度 [GeV]
  const Nmin = Math.log(Trh / T0) + Math.log(1);   // ざっくり
  console.log('  ' + pad('再加熱温度（例）', 30) + padl(e(Trh, 2) + ' GeV', 20));
  console.log('  ' + pad('いまの CMB 温度', 30) + padl(e(T0, 3) + ' GeV', 20));
  console.log('  ' + pad('★ 必要な e 倍の回数（およそ）', 30) + padl(f(Nmin, 1), 20));
  console.log('');
  console.log('  ★ 60 回 ほど ── よく言われる「N ≈ 60」はこの数です');
  console.log('  ★ 第 46 回では「74.5 回の e 倍で測定帯域の外へ」と出ました。');
  console.log('  ★★ 地平線は 60〜75 回の e 倍で「見える／見えない」を切り替える装置。');
}

// ============================================================
head('7. インフレーションは、第 44・45 回の パラメトリック そのもの');
// ============================================================
console.log('');
console.log('  ' + pad('第 44 回（メタマテリアル）', 30) + '媒質の eps(t) を揺らす → 運動量ギャップで増幅');
console.log('  ' + pad('第 45 回（動的カシミール）', 30) + '境界を揺らす → 真空から光子が出る');
console.log('  ' + pad('★ 本回（インフレーション）', 30) + '★ 宇宙が膨張する → 真空から ゆらぎが出る');
console.log('');
console.log('  どれも同じ形： v\'\' + omega^2(t) v = 0 で omega が時間に依る');
console.log('  ★★ CMB のゆらぎは、膨張する宇宙の「動的カシミール光子」でした。');
console.log('  ★ ボゴリューボフ係数も同じ： |alpha|^2 - |beta|^2 = 1（第 36・45 回）');
console.log('');
console.log('  ★★★ 違いは ただ一つ ── 揺すった人が居ないこと。');
console.log('  ★★★ 揺らしているのは 宇宙自身の膨張で、そのエネルギー源は インフラトンの位置エネルギー。');

// ============================================================
head('8. 本回のまとめ');
// ============================================================
const rows2 = [
  ['★ MS 方程式 = 第 13 回の 1/tau^2', '◎ 解析', '★ s = 1/2 ± nu'],
  ['x=-k tau で k が消える', '◎ 解析', '★ スケール不変性の正体'],
  ['P(k) ∝ k^{3-2nu} を数値で', '◎ 数値', '★ 傾きが 3-2nu と一致'],
  ['地平線の外で zeta が凍る', '◎ 数値', 'x<1 で一定'],
  ['n_s だけでは模型を選べない', '◎ 数値', '★ phi^2 は r で棄却'],
  ['★ n_s → -0.105 dB/oct', '◎ 解析', '★ 乱流の 0.081 と同じ桁'],
  ['N ≈ 60 の由来', '○ 数値', 'ざっくりの見積もり'],
  ['★ インフレ = パラメトリック', '◎ 対応', '★ 第 44・45 回と同じ式'],
  ['★ インフレーションの実在', '× 扱えない', '★ 本稿は模型の中の計算のみ'],
];
console.log('');
for (const r of rows2) console.log('  ' + pad(r[0], 36) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 宇宙の原始ゆらぎは、第 13 回の 1/tau^2 が作った 階数 でした。');
console.log('  ★ 完全なスケール不変（n_s=1）からの ずれは わずか 0.105 dB/oct ──');
console.log('  ★ そしてその わずかなずれが「インフレーションは いつか終わった」と言っている。');
