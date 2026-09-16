// 考える波 第 45 回：真空を揺らす
//   ゼロ点の海 ── カシミール、動的カシミール、ウンルー
//   node shinku.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

// ---- 複素数 ----
const cadd = (a, b) => [a[0] + b[0], a[1] + b[1]];
const cmul = (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
const cdiv = (a, b) => { const d = b[0] * b[0] + b[1] * b[1];
  return [(a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d]; };
const cabs2 = (a) => a[0] * a[0] + a[1] * a[1];
const cexp = (a) => [Math.exp(a[0]) * Math.cos(a[1]), Math.exp(a[0]) * Math.sin(a[1])];
const clog = (a) => [0.5 * Math.log(a[0] * a[0] + a[1] * a[1]), Math.atan2(a[1], a[0])];
const cpow = (a, b) => cexp(cmul(b, clog(a)));

// ---- 複素ガンマ関数（ランチョス） ----
const LG = [676.5203681218851, -1259.1392167224028, 771.32342877765313,
  -176.61502916214059, 12.507343278686905, -0.13857109526572012,
  9.9843695780195716e-6, 1.5056327351493116e-7];
function cgamma(z) {
  if (z[0] < 0.5) {
    // 反射公式： Gamma(z) = pi / (sin(pi z) Gamma(1-z))
    const pz = [Math.PI * z[0], Math.PI * z[1]];
    const sn = [Math.sin(pz[0]) * Math.cosh(pz[1]), Math.cos(pz[0]) * Math.sinh(pz[1])];
    return cdiv([Math.PI, 0], cmul(sn, cgamma([1 - z[0], -z[1]])));
  }
  const zz = [z[0] - 1, z[1]];
  let x = [0.99999999999980993, 0];
  for (let i = 0; i < 8; i++) x = cadd(x, cdiv([LG[i], 0], [zz[0] + i + 1, zz[1]]));
  const t = [zz[0] + 7.5, zz[1]];
  return cmul(cmul(cpow(t, [zz[0] + 0.5, zz[1]]), cexp([-t[0], -t[1]])),
              cmul([Math.sqrt(2 * Math.PI), 0], x));
}

const hbar = 1.054571817e-34, c = 299792458, kB = 1.380649e-23;

console.log('考える波 第 45 回 ── 真空を揺らす');
console.log('「何もない」を波として見ると、ゼロ点の海だった');

// ============================================================
head('1. 無限を引き算する ── 一次元のカシミール');
// ============================================================
// 間隔 a の 2 枚の壁の間のモード： omega_n = n pi c / a
// E = (hbar/2) sum omega_n は発散する。切断 e^{-delta n} を入れて分ける。
//   sum n e^{-delta n} = 1/(4 sinh^2(delta/2)) = 1/delta^2 - 1/12 + O(delta^2)
console.log('');
console.log('  壁の間のモード： omega_n = n pi c / a 。 E = (hbar/2) Σ omega_n');
console.log('  切断 e^{-delta n} を入れると  Σ n e^{-delta n} = 1/(4 sinh^2(delta/2))');
console.log('  = 1/delta^2 - 1/12 + O(delta^2)  ── 第 1 項は a に比例する「体積の項」');
console.log('');
console.log('  ' + pad('delta', 12) + padl('Σ n e^{-delta n}（数値）', 26)
  + padl('1/delta^2', 16) + padl('★ 差', 14) + padl('-1/12', 12));
for (const d of [0.1, 0.03, 0.01, 0.003, 0.001]) {
  let s = 0;
  const N = Math.ceil(60 / d);
  for (let n = 1; n <= N; n++) s += n * Math.exp(-d * n);
  console.log('  ' + pad(f(d, 4), 12) + padl(f(s, 8), 26) + padl(f(1 / (d * d), 8), 16)
    + padl(f(s - 1 / (d * d), 8), 14) + padl(f(-1 / 12, 8), 12));
}
console.log('');
console.log('  ★★ 発散する項は 1/delta^2 ＝ 壁が無くても同じ（体積に比例）。');
console.log('  ★★ 引き算して残るのは -1/12 ── 有限で、しかも 負。');
console.log('');
// E/L = -(hbar c pi)/(24 a^2)  （1 次元スカラー、単位長さあたり）
console.log('  → E(a) = (hbar c pi / 2a) · (-1/12) = - hbar c pi / (24 a)');
console.log('  → 力 F = -dE/da = - hbar c pi / (24 a^2)   ★ 引力');

// ============================================================
head('2. 三次元の電磁場 ── 実際の大きさ');
// ============================================================
// P = - pi^2 hbar c / (240 a^4)
{
  console.log('');
  console.log('  平行平板（完全導体）の圧力： P = - pi^2 hbar c / (240 a^4)');
  console.log('');
  console.log('  ' + pad('間隔 a', 14) + padl('|P| [Pa]', 18) + padl('大気圧との比', 18)
    + '  たとえ');
  const K = Math.PI * Math.PI * hbar * c / 240;
  for (const [a, note] of [[1e-3, '1 mm'], [1e-5, '10 um'], [1e-6, '1 um'],
                           [1e-7, '100 nm'], [1e-8, '10 nm']]) {
    const P = K / Math.pow(a, 4);
    console.log('  ' + pad(note, 14) + padl(e(P, 4), 18) + padl(e(P / 101325, 3), 18)
      + '  ' + (P > 101325 ? '★ 大気圧より大きい' : ''));
  }
  console.log('');
  console.log('  ★ 10 nm まで詰めると 大気圧（1.28 倍）を超える ── 「何もない」の圧力');
  console.log('  ★ a^{-4} なので、1 桁 縮めると 10000 倍');
}

// ============================================================
head('3. 動的カシミール ── 揺すると 光子が出る');
// ============================================================
// モードの周波数を揺らす： x'' + w0^2 (1 + h cos(Om t)) x = 0
// 一周期の単値行列 M（det M = 1）から ボゴリューボフ係数を取る：
//   alpha = (M11+M22)/2 - i (M12-M21)/2
//   beta  = (M11-M22)/2 + i (M12+M21)/2
//   |alpha|^2 - |beta|^2 = det M = 1 ← ★ 第 36 回の det M = 1 そのもの
//   生成された光子数 n = |beta|^2
function mono(w0, h, Om, N) {
  const T = 2 * Math.PI / Om, dt = T / N;
  const F = (t, x, v) => [v, -w0 * w0 * (1 + h * Math.cos(Om * t)) * x];
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
  // 位置と「p/w0」を基底に取る（det = 1 になるように）
  const c1 = run(1, 0), c2 = run(0, w0);
  return [[c1[0], c2[0] / w0], [c1[1] / w0, c2[1] / w0]];
}
function bogo(M) {
  const ar = (M[0][0] + M[1][1]) / 2, ai = -(M[0][1] - M[1][0]) / 2;
  const br = (M[0][0] - M[1][1]) / 2, bi = (M[0][1] + M[1][0]) / 2;
  return { a2: ar * ar + ai * ai, b2: br * br + bi * bi };
}
{
  const w0 = 1, Om = 2;
  console.log('');
  console.log('  モードの周波数を揺らす： x\'\' + w0^2 (1 + h cos(Om t)) x = 0');
  console.log('  一周期の単値行列 M から ボゴリューボフ係数 alpha, beta を取る');
  console.log('  ★ |alpha|^2 - |beta|^2 = det M = 1 （第 36 回）');
  console.log('  ★ 生成された光子数 n = |beta|^2');
  console.log('');
  console.log('  ' + pad('h', 8) + padl('det M', 12) + padl('|alpha|^2', 14)
    + padl('|beta|^2 = n', 14) + padl('差', 12));
  for (const h of [0.0, 0.05, 0.1, 0.2, 0.4]) {
    const M = mono(w0, h, Om, 200000);
    const det = M[0][0] * M[1][1] - M[0][1] * M[1][0];
    const b = bogo(M);
    console.log('  ' + pad(f(h, 3), 8) + padl(f(det, 8), 12) + padl(f(b.a2, 8), 14)
      + padl(f(b.b2, 8), 14) + padl(f(b.a2 - b.b2, 8), 12));
  }
  console.log('');
  console.log('  ★★ 揺すらなければ（h=0）n = 0 ── 真空のまま');
  console.log('  ★★ 揺すると n > 0 ── 何もない所から 光子が出る');
  console.log('');
  // 周期を重ねると指数的に増える
  console.log('  周期を重ねたとき（h = 0.1）');
  console.log('  ' + pad('周期の数', 12) + padl('n = |beta|^2', 18)
    + padl('|alpha|^2-|beta|^2', 22));
  let M = mono(w0, 0.1, Om, 200000);
  let A = [[1, 0], [0, 1]];
  for (let k = 1; k <= 60; k++) {
    A = [[A[0][0] * M[0][0] + A[0][1] * M[1][0], A[0][0] * M[0][1] + A[0][1] * M[1][1]],
         [A[1][0] * M[0][0] + A[1][1] * M[1][0], A[1][0] * M[0][1] + A[1][1] * M[1][1]]];
    if (k === 1 || k === 10 || k === 20 || k === 40 || k === 60) {
      const b = bogo(A);
      console.log('  ' + pad(k, 12) + padl(f(b.b2, 6), 18) + padl(f(b.a2 - b.b2, 9), 22));
    }
  }
  console.log('');
  console.log('  ★ 指数的に増える。ただし |alpha|^2-|beta|^2 = 1 は ずっと保たれる');
  console.log('  ★★ ＝ 第 36 回の「det M = 1 は不確定性の保存」の、粒子数版');
}

// ============================================================
head('4. ウンルー ── 加速すると 真空が温かく見える');
// ============================================================
// T = hbar a / (2 pi c kB)
{
  console.log('');
  console.log('  T = hbar a / (2 pi c kB)');
  console.log('');
  console.log('  ' + pad('加速度 a [m/s^2]', 20) + padl('T [K]', 18) + '  たとえ');
  const K = hbar / (2 * Math.PI * c * kB);
  for (const [a, note] of [[9.8, '地上の重力'], [1e10, '強い電場中の電子'],
                           [1e20, ''], [2.47e20, '★ T = 1 K'],
                           [1e26, '★ T = 300 K（室温）']]) {
    console.log('  ' + pad(e(a, 2), 20) + padl(e(K * a, 4), 18) + '  ' + note);
  }
  console.log('');
  console.log('  ★ 1 K を出すのに 2.5e20 m/s^2 ── だから 直接は 測られていない');
  console.log('  ★ 逆に言うと「日常では真空は冷たい」ことの定量的な理由');
}

// ============================================================
head('5. ★ なぜ「熱」になるのか ── 対数時間と 指数写像');
// ============================================================
// 加速する観測者の時間 eta と ミンコフスキー時間 t： a t = e^{a eta}
// → 平面波 e^{-i w t} は e^{-i (w/a) e^{a eta}} になる
// → eta で フーリエ変換すると ガンマ関数が出て、|beta/alpha|^2 = e^{-2 pi Om/a}
{
  console.log('');
  console.log('  加速する観測者の固有時 eta と ミンコフスキー時間 t： a t = e^{a eta}');
  console.log('  ★ 第 20 回の「対数時間」そのもの。第 28 回の「足し算 → 掛け算」');
  console.log('');
  console.log('  ∫ d eta e^{i Om eta} e^{∓ i (w/a) e^{a eta}}');
  console.log('    = (1/a) Gamma(i Om/a) (±i a/w)^{i Om/a}');
  console.log('  (±i)^{i Om/a} = e^{∓ pi Om/(2a)}  ← ★ ここで 指数が出る');
  console.log('');
  console.log('  ' + pad('Om/a', 10) + padl('|beta/alpha|^2（式）', 22)
    + padl('e^{-2 pi Om/a}', 18) + padl('★ n = 1/(e^x - 1)', 20));
  for (const y of [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]) {
    const r = Math.exp(-2 * Math.PI * y);
    const n = 1 / (Math.exp(2 * Math.PI * y) - 1);
    console.log('  ' + pad(f(y, 3), 10) + padl(e(r, 6), 22) + padl(e(r, 6), 18)
      + padl(e(n, 6), 20));
  }
  console.log('');
  // ガンマ関数の恒等式を数値で確認： |Gamma(i y)|^2 = pi / (y sinh(pi y))
  console.log('  ガンマ関数の恒等式を数値で確認： |Gamma(i y)|^2 = pi / (y sinh(pi y))');
  console.log('  ' + pad('y', 10) + padl('|Gamma(i y)|^2（数値）', 24)
    + padl('pi/(y sinh(pi y))', 22) + padl('比', 10));
  for (const y of [0.1, 0.3, 1.0, 2.0]) {
    const g = cgamma([0, y]);
    const lhs = cabs2(g);
    const rhs = Math.PI / (y * Math.sinh(Math.PI * y));
    console.log('  ' + pad(f(y, 2), 10) + padl(e(lhs, 8), 24) + padl(e(rhs, 8), 22)
      + padl(f(lhs / rhs, 6), 10));
  }
  console.log('');
  console.log('  ★★★ sinh が出れば、それを開いて 1/(e^x - 1) ── プランク分布');
  console.log('  ★★★ つまり「熱」の正体は、時間が対数になったことでした。');
  console.log('  ★ 温度 T = a/(2 pi) は、この e^{-2 pi Om/a} の肩そのもの');
}

// ============================================================
head('6. 温度が「見る人による」ということ');
// ============================================================
{
  console.log('');
  console.log('  同じ真空を、静止した人は T=0、加速する人は T=a/(2 pi) と見る。');
  console.log('');
  console.log('  ' + pad('立場', 26) + pad('見える状態', 22) + '本シリーズの言葉');
  const rows = [
    ['静止している', '真空（n=0）', '第 9 回：ゼロ点だけ'],
    ['★ 一定加速している', '★ 熱浴（T=a/2pi）', '★ 対数時間で見ている'],
    ['★ 鏡を揺らしている', '★ 光子が出る', '★ 第 40・44 回の パラメトリック'],
  ];
  for (const r of rows) console.log('  ' + pad(r[0], 26) + pad(r[1], 22) + r[2]);
  console.log('');
  console.log('  ★★ 「粒子が何個あるか」は 座標の取り方に依る量でした。');
  console.log('  ★★ 波として見れば当たり前です ── どの基底で展開するかの問題だから。');
  console.log('  ★ 第 7・15 回の「無次元量だけが物理」と同じ注意：');
  console.log('  ★ 座標に依る量を、物理だと思ってはいけない。');
}

// ============================================================
head('7. それでも ただでは取り出せない');
// ============================================================
console.log('');
console.log('  ' + pad('門番', 28) + '本回での効き方');
const gates = [
  ['受動性（第 17・18 回）', '鏡を揺らす仕事が、光子のエネルギー源'],
  ['det M = 1（第 36 回）', '★ |alpha|^2-|beta|^2=1 ── 増える分は必ず対で出る'],
  ['総和則（第 44 回）', 'ある周波数で得れば 別の周波数で損する'],
];
for (const g of gates) console.log('  ' + pad(g[0], 28) + g[1]);
console.log('');
console.log('  ★ カシミール力は「引き出せるエネルギー」ではなく、位置の関数の 勾配。');
console.log('  ★ 一度 板をくっつけたら、離すのに同じだけの仕事が要ります。');
console.log('  ★★ 動的カシミールの光子も、揺すった人の仕事がそのまま出ているだけ。');

// ============================================================
head('8. 本回のまとめ');
// ============================================================
const rows = [
  ['発散は体積に比例（引き算できる）', '◎ 数値', '★ 1/delta^2 を引くと -1/12'],
  ['カシミール圧 ∝ a^{-4}', '◎ 数値', '10 nm で 大気圧の 1.28 倍'],
  ['★ 揺すると n=|beta|^2 の光子', '◎ 数値', '★ h=0 では n=0'],
  ['★ |alpha|^2-|beta|^2 = det M = 1', '◎ 数値', '★ 第 36 回の粒子数版'],
  ['ウンルー温度', '◎ 数値', '1 K に 2.5e20 m/s^2'],
  ['★ 熱の正体は 対数時間', '◎ 解析', '★ ガンマ関数 → sinh → 1/(e^x-1)'],
  ['|Gamma(iy)|^2 の恒等式', '◎ 数値', 'pi/(y sinh(pi y)) と一致'],
  ['★ ただでエネルギーは出ない', '◎ 論理', '受動性・det M=1・総和則'],
  ['★ 実験での検出', '△ 扱えない', '★ 動的カシミールは超伝導回路で報告あり'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 36) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 「何もない」は、波の言葉では ゼロ点の海でした。');
console.log('  ★ 境界を動かせば さざ波が立ち（動的カシミール）、');
console.log('  ★ 時間を対数で測れば その海は 熱く見える（ウンルー）。');
console.log('  ★ どちらも 新しいエネルギー源ではなく、見方と 仕事の話です。');
