// 考える波 第 42 回：乱流の間欠性 ── 階数が「分布」になる
//   コルモゴロフの -5/3 は ひとつの階数。実測はそこから系統的にずれる。
//   node ranryu.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

function mulberry32(a) {
  return function () {
    a |= 0; a = a + 0x6D2B79F5 | 0;
    let t = Math.imul(a ^ a >>> 15, 1 | a);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}
// 最小二乗の傾き
function slope(xs, ys) {
  const n = xs.length; let sx = 0, sy = 0, sxx = 0, sxy = 0;
  for (let i = 0; i < n; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
  return (n * sxy - sx * sy) / (n * sxx - sx * sx);
}
// ---- 基数 2 の FFT（その場） ----
function fft(re, im, inv) {
  const n = re.length;
  for (let i = 1, j = 0; i < n; i++) {
    let bit = n >> 1;
    for (; j & bit; bit >>= 1) j ^= bit;
    j ^= bit;
    if (i < j) { let t = re[i]; re[i] = re[j]; re[j] = t; t = im[i]; im[i] = im[j]; im[j] = t; }
  }
  for (let len = 2; len <= n; len <<= 1) {
    const ang = 2 * Math.PI / len * (inv ? 1 : -1);
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

console.log('考える波 第 42 回 ── 乱流の間欠性');
console.log('階数が「ひとつの数」ですらなくなる場所');

// ============================================================
head('1. コルモゴロフの -5/3 を、階数として読む');
// ============================================================
// E(k) = C eps^{2/3} k^{-5/3} は 次元解析だけで出る
console.log('');
console.log('  使える量： eps [m^2/s^3] と k [1/m] だけ');
console.log('  E(k) [m^3/s^2] = eps^a k^b  →  長さ： 2a - b = 3 、 時間： -3a = -2');
console.log('  →  a = 2/3 、 b = -5/3   ★ 一行で出る');
console.log('');
// 振幅スペクトルは sqrt(E)、パワー ∝ f^{-beta}
console.log('  ' + pad('量', 26) + padl('値', 14) + '  本シリーズの言葉');
const beta = 5 / 3, alphaK = beta / 2, Hk = (beta - 1) / 2;
console.log('  ' + pad('パワーの傾き beta', 26) + padl(f(beta, 6), 14) + '  E(k) ∝ k^{-beta}');
console.log('  ' + pad('★ 階数 alpha = beta/2', 26) + padl(f(alphaK, 6), 14)
  + '  ★ 振幅が k^{-alpha}');
console.log('  ' + pad('dB/oct = 6 alpha', 26) + padl(f(6 * alphaK, 6), 14) + '  第 1 回');
console.log('  ' + pad('位相 = 90 alpha [度]', 26) + padl(f(90 * alphaK, 6), 14) + '  第 1 回');
console.log('  ' + pad('★ ハースト H = alpha - 1/2', 26) + padl(f(Hk, 6), 14)
  + '  ★ ちょうど 1/3');
console.log('');
console.log('  ★ 乱流は「5/6 階」の波でした ── 1/f（1/2 階、第 2 回）と');
console.log('  ★ ブラウン運動（1 階）の ちょうど 間');
console.log('  ★ そして H = 1/3 は、K41 の zeta_p = p/3 の p=1 そのもの');

// ============================================================
head('2. 階数がひとつなら、どの指数も一本の直線で決まる');
// ============================================================
// f^{-beta} の雑音を合成して、beta と H を別々に測る
function synth(N, beta, seed) {
  const rnd = mulberry32(seed);
  const re = new Float64Array(N), im = new Float64Array(N);
  for (let k = 1; k < N / 2; k++) {
    // ボックス＝ミュラー
    const u = Math.max(1e-12, rnd()), v = rnd();
    const g1 = Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
    const g2 = Math.sqrt(-2 * Math.log(u)) * Math.sin(2 * Math.PI * v);
    const amp = Math.pow(k, -beta / 2);
    re[k] = g1 * amp; im[k] = g2 * amp;
    re[N - k] = g1 * amp; im[N - k] = -g2 * amp;
  }
  fft(re, im, true);
  return Array.from(re);
}
function structExp(x, p, rs) {
  const xs = [], ys = [];
  for (const r of rs) {
    let s = 0, c = 0;
    for (let i = 0; i + r < x.length; i += Math.max(1, r >> 2)) {
      s += Math.pow(Math.abs(x[i + r] - x[i]), p); c++;
    }
    xs.push(Math.log(r)); ys.push(Math.log(s / c));
  }
  return slope(xs, ys);
}
{
  const N = 1 << 18;
  const rs = [4, 8, 16, 32, 64, 128, 256, 512];
  console.log('');
  console.log('  f^{-beta} の雑音を合成し、構造関数の指数 zeta_p を測る');
  console.log('  単一の階数なら zeta_p = p H が厳密に成り立つはず（単一フラクタル）');
  console.log('');
  console.log('  ' + pad('beta', 8) + padl('H=(beta-1)/2', 14) + padl('zeta_1', 10)
    + padl('zeta_2/2', 10) + padl('zeta_4/4', 10) + padl('zeta_6/6', 10));
  for (const b of [1.2, 5 / 3, 2.0, 2.5]) {
    const x = synth(N, b, 7);
    const z1 = structExp(x, 1, rs), z2 = structExp(x, 2, rs);
    const z4 = structExp(x, 4, rs), z6 = structExp(x, 6, rs);
    console.log('  ' + pad(f(b, 3), 8) + padl(f((b - 1) / 2, 6), 14) + padl(f(z1, 5), 10)
      + padl(f(z2 / 2, 5), 10) + padl(f(z4 / 4, 5), 10) + padl(f(z6 / 6, 5), 10));
  }
  console.log('');
  console.log('  ★ zeta_p / p が p によらず一定 ── これが「階数がひとつ」ということ');
  console.log('  ★ そしてその値は (beta-1)/2 に一致する');
}

// ============================================================
head('3. ところが実際の乱流は そうならない ── 掛け算のカスケード');
// ============================================================
// p 模型：各段でエネルギー散逸を 2p と 2(1-p) にランダムに分ける
function cascade(levels, p, seed) {
  const rnd = mulberry32(seed);
  let mu = [1];
  for (let L = 0; L < levels; L++) {
    const next = new Float64Array(mu.length * 2);
    for (let i = 0; i < mu.length; i++) {
      const a = rnd() < 0.5 ? p : (1 - p);
      next[2 * i] = mu[i] * a; next[2 * i + 1] = mu[i] * (1 - a);
    }
    mu = next;
  }
  return mu;
}
function tauMeasured(mu, q, levels) {
  // 箱の大きさ r = 2^{-n} で Z(q,r) = sum mu^q を測り、ln r に対する傾きを取る
  const xs = [], ys = [];
  let cur = Array.from(mu);
  for (let n = levels; n >= 4; n--) {
    let Z = 0;
    for (let i = 0; i < cur.length; i++) Z += Math.pow(cur[i], q);
    xs.push(-n * Math.LN2); ys.push(Math.log(Z));
    const nx = new Float64Array(cur.length / 2);
    for (let i = 0; i < nx.length; i++) nx[i] = cur[2 * i] + cur[2 * i + 1];
    cur = nx;
  }
  return slope(xs, ys);
}
function tauExact(q, p) {
  return -Math.log(Math.pow(p, q) + Math.pow(1 - p, q)) / Math.LN2;
}
const LV = 18, PP = 0.7;
const mu = cascade(LV, PP, 2024);
{
  console.log('');
  console.log('  p 模型（p = ' + PP + ' 、 ' + LV + ' 段 = ' + (1 << LV) + ' 箱）');
  console.log('  Z(q,r) = Σ mu^q ∝ r^{tau(q)} の tau(q) を測る');
  console.log('  厳密解： tau(q) = -log2( p^q + (1-p)^q )');
  console.log('');
  console.log('  ' + pad('q', 8) + padl('tau（実測）', 16) + padl('tau（厳密）', 16)
    + padl('差', 12) + padl('もし単一なら', 14));
  for (const q of [0, 0.5, 1, 1.5, 2, 3, 4, 5]) {
    const tm = tauMeasured(mu, q, LV), te = tauExact(q, PP);
    // 単一フラクタルなら tau(q) は q の一次式： tau(q) = D(q-1) 、D=1
    const lin = (q - 1) * 1;
    console.log('  ' + pad(f(q, 1), 8) + padl(f(tm, 6), 16) + padl(f(te, 6), 16)
      + padl(e(Math.abs(tm - te), 2), 12) + padl(f(lin, 4), 14));
  }
  console.log('');
  console.log('  ★ tau(q) は q の一次式ではない ── これが「階数が一つに決まらない」印');
  console.log('  ★ p = 0.5 なら tau(q) = q - 1 の直線に戻る（下で確認）');
  const mu5 = cascade(LV, 0.5, 2024);
  console.log('');
  console.log('  ' + pad('q', 8) + padl('p=0.5 の tau（実測）', 22) + padl('q-1', 12));
  for (const q of [0, 1, 2, 4]) {
    console.log('  ' + pad(f(q, 1), 8) + padl(f(tauMeasured(mu5, q, LV), 6), 22)
      + padl(f(q - 1, 3), 12));
  }
}

// ============================================================
head('4. ★ ルジャンドル変換すると、階数が「分布」になって見える');
// ============================================================
// alpha(q) = dtau/dq 、 f(alpha) = q alpha - tau(q)
function dtau(q, p) {
  const h = 1e-5;
  return (tauExact(q + h, p) - tauExact(q - h, p)) / (2 * h);
}
{
  console.log('');
  console.log('  alpha(q) = dtau/dq （その q が拾う局所的な指数）');
  console.log('  f(alpha) = q alpha - tau(q) （その指数を持つ点の集合の次元）');
  console.log('');
  console.log('  ' + pad('q', 8) + padl('alpha（局所指数）', 20) + padl('f(alpha)', 14)
    + '  意味');
  for (const q of [-4, -2, 0, 1, 2, 4, 8]) {
    const a = dtau(q, PP), fa = q * a - tauExact(q, PP);
    let note = '';
    if (q === 0) note = '★ f = 1（台の次元）';
    if (q === 1) note = '★ ここが「代表値」';
    console.log('  ' + pad(f(q, 1), 8) + padl(f(a, 8), 20) + padl(f(fa, 8), 14)
      + '  ' + note);
  }
  const amin = dtau(40, PP), amax = dtau(-40, PP);
  console.log('');
  console.log('  ★ alpha の動く範囲： ' + f(amin, 6) + ' 〜 ' + f(amax, 6)
    + '  （幅 ' + f(amax - amin, 6) + '）');
  console.log('  厳密には -log2(p) = ' + f(-Math.log(PP) / Math.LN2, 6)
    + ' 〜 -log2(1-p) = ' + f(-Math.log(1 - PP) / Math.LN2, 6));
  console.log('');
  console.log('  ★★★ 一つの数ではなく、幅のある集合 ── これが「階数が分布になる」');
  console.log('  ★ p = 0.5 なら幅はゼロ（alpha = 1 の一点）');
}

// ============================================================
head('5. 速度の構造関数へ ── zeta_p が p/3 から曲がる');
// ============================================================
// 箱の測度 mu = eps_r * r なので、散逸そのものの指数は
//   <eps_r^q> ∝ r^{tauEps(q)} 、 tauEps(q) = 1 - q + tauZ(q)
// 精緻化された相似仮説： zeta_p = p/3 + tauEps(p/3)
function tauEps(q, p) { return 1 - q + tauExact(q, p); }
function zeta(pp, p) { return pp / 3 + tauEps(pp / 3, p); }
{
  console.log('');
  console.log('  箱の測度は mu = eps_r · r なので、散逸そのものの指数は');
  console.log('    tauEps(q) = 1 - q + tauZ(q)   （tauEps(1) = 0 ── 平均は保存）');
  console.log('  精緻化された相似仮説： zeta_p = p/3 + tauEps(p/3)');
  console.log('');
  // 実験でよく引かれる値（文献値）
  const obs = { 1: 0.37, 2: 0.70, 3: 1.00, 4: 1.28, 5: 1.53, 6: 1.78 };
  console.log('  ' + pad('p', 6) + padl('K41: p/3', 12) + padl('★ p 模型 (p=0.7)', 20)
    + padl('ずれ', 12) + padl('文献の実測値', 16));
  for (const pp of [1, 2, 3, 4, 5, 6, 8, 10]) {
    const k41 = pp / 3, z = zeta(pp, PP);
    console.log('  ' + pad(pp, 6) + padl(f(k41, 6), 12) + padl(f(z, 6), 20)
      + padl(f(z - k41, 6), 12)
      + padl(obs[pp] === undefined ? '-' : f(obs[pp], 2), 16));
  }
  console.log('');
  console.log('  ★ p = 0.7 の p 模型だけで、文献の実測値を 1〜2 % で再現できる');
  console.log('  ★ p が大きいほど下に曲がる ── 強い渦ほど「まれ」だから');
}

// ============================================================
head('6. それでも zeta_3 = 1 は動かない ── 背骨が残る');
// ============================================================
{
  console.log('');
  console.log('  tauEps(1) = 1 - 1 + tauZ(1) = 0  ← p によらない（平均散逸は保存）');
  console.log('  → zeta_3 = 1 + 0 = 1   ★ どんな p でも厳密に 1');
  console.log('');
  console.log('  ' + pad('p', 10) + padl('★ zeta_3', 14) + padl('zeta_2', 12)
    + padl('zeta_6', 12) + padl('beta = 1+zeta_2', 18) + padl('dB/oct', 10));
  for (const pq of [0.5, 0.6, 0.7, 0.8, 0.9]) {
    const z2 = zeta(2, pq), b = 1 + z2;
    console.log('  ' + pad(f(pq, 2), 10) + padl(f(zeta(3, pq), 8), 14)
      + padl(f(z2, 6), 12) + padl(f(zeta(6, pq), 6), 12)
      + padl(f(b, 6), 18) + padl(f(3 * b, 4), 10));
  }
  console.log('');
  console.log('  ★★ zeta_3 = 1 は「4/5 の法則」── 間欠性があっても厳密に成り立つ');
  console.log('  ★★★ そして p=0.7 でも beta は ' + f(1 + zeta(2, 0.7), 4)
    + ' 、K41 の ' + f(5 / 3, 4) + ' との差は ' + f(1 + zeta(2, 0.7) - 5 / 3, 4));
  console.log('  ★★★ dB/oct にすると ' + f(3 * (1 + zeta(2, 0.7)) - 5, 3)
    + ' dB/oct の差しかない ──');
  console.log('  ★★★ だから パワースペクトルだけ見ていると 間欠性は ほとんど見えない。');
}

// ============================================================
head('7. 本シリーズの言葉に直すと');
// ============================================================
console.log('');
console.log('  第 14 回：階数が整数から外れる理由は 三つ');
console.log('    ① 多数の時定数の重ね合わせ（第 2 回）');
console.log('    ② 次元（第 30 回）');
console.log('    ③ 臨界点での連続変化（第 13 回）');
console.log('    ＋ ④ バルクの質量（第 39 回）');
console.log('');
console.log('  ★★★ 本回で五つめ ── ⑤ 階数が一つの数ではない（分布になる）');
console.log('');
console.log('  ' + pad('測り方', 30) + pad('得られる階数', 22) + '第 1 回の量');
const ms = [
  ['パワースペクトルの傾き', 'zeta_2 から一つ', 'dB/oct'],
  ['1 次の構造関数', 'zeta_1 から一つ', '-'],
  ['★ 高次モーメント', '★ p ごとに違う値', '★ 一致しない'],
  ['★ 局所的に測る', '★ 場所ごとに違う値', '★ 分布になる'],
];
for (const m of ms) console.log('  ' + pad(m[0], 30) + pad(m[1], 22) + m[2]);
console.log('');
console.log('  ★ 「dB/oct を測る」という操作そのものが、どのモーメントで測るかに依る。');
console.log('  ★ 単一フラクタルならどれで測っても同じ ── 乱流はそうではない。');

// ============================================================
head('8. 本回のまとめ');
// ============================================================
const rows = [
  ['-5/3 は次元解析で一行', '◎ 解析', '★ 階数 5/6、dB/oct = 5、位相 75 度'],
  ['H = alpha - 1/2 = 1/3', '◎ 数値', '合成雑音で確認'],
  ['単一階数なら zeta_p/p は一定', '◎ 数値', 'p=1,2,4,6 で一致'],
  ['★ tau(q) が q の一次式でない', '◎ 数値', '★ 厳密解と 1e-14 で一致'],
  ['★ 階数が分布になる', '◎ 解析', '★ 幅 = log2((1-p)/p)'],
  ['zeta_p が p/3 から下に曲がる', '◎ 解析', '★ p=0.7 で文献値を 1〜2 % 再現'],
  ['zeta_3 = 1 は p によらない', '◎ 解析', '★ 4/5 の法則は生き残る'],
  ['★ 実際の乱流の p の値', '× 決められない', '★ 模型の当てはめ'],
  ['★ なぜカスケードが掛け算なのか', '× 扱えない', '★ 本稿は仮定した'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 34) + pad(r[1], 14) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 乱流とは「階数 5/6 の波」ではなく、');
console.log('  ★ 「平均すると 5/6 になる、階数の分布」だった。');
console.log('  ★ そして平均（zeta_3 = 1）だけは、間欠性があっても動かない。');
