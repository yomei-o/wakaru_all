// 考える波 第 56 回：1/f に 戻る
//   第 2・27 回の主張を、第 51〜55 回の道具で 測り直す
//   node ichif.js
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

console.log('考える波 第 56 回 ── 1/f に 戻る');
console.log('第 2・27 回の主張を、第 51〜55 回の道具で 測り直す');

// ============================================================
head('1. 第 2 回の作り方を、そのまま 使う');
// ============================================================
// g(tau) ∝ tau^{-gamma} の 重ね合わせ
//   S(w) = ∫ g(tau) tau/(1+w^2 tau^2) dtau ∝ w^{gamma-2}
//   → パワーの傾き beta = 2 - gamma 。 gamma=1 で beta=1（1/f）
function makeS(logTlo, logThi, gamma, N) {
  const lts = [], ws = [];
  for (let i = 0; i < N; i++) {
    const lt = logTlo + (logThi - logTlo) * i / (N - 1);
    lts.push(Math.pow(10, lt));
    ws.push(Math.pow(Math.pow(10, lt), 1 - gamma));   // g(tau) dtau ∝ tau^{1-gamma} d(ln tau)
  }
  return (w) => {
    let s = 0;
    for (let i = 0; i < N; i++) {
      const t = lts[i];
      s += ws[i] * t / (1 + w * w * t * t);
    }
    return Math.log(s);                                // ln S（パワー）
  };
}
// 局所的な「パワーの傾き」beta（第 51 回の作法：窓での当てはめ）
function localBeta(logS, w, wdec, npts) {
  const xs = [], ys = [];
  for (let i = 0; i < npts; i++) {
    const lg = Math.log10(w) - wdec / 2 + wdec * i / (npts - 1);
    xs.push(lg * Math.LN10); ys.push(logS(Math.pow(10, lg)));
  }
  return -slope(xs, ys);
}
{
  const S = makeS(-6, 6, 1.0, 40000);   // tau が 12 桁
  console.log('');
  console.log('  g(tau) ∝ 1/tau 、 tau は 1e-6 〜 1e6（12 桁）');
  console.log('  → 予言： beta = 2 - gamma = 1（つまり 1/f）');
  console.log('');
  console.log('  ' + pad('w', 12) + padl('局所的な beta', 18) + padl('|beta - 1|', 16));
  for (const w of [1e-5, 1e-3, 1e-1, 1, 1e1, 1e3, 1e5]) {
    const b = localBeta(S, w, 0.4, 41);
    console.log('  ' + pad(e(w, 0), 12) + padl(f(b, 6), 18) + padl(e(Math.abs(b - 1), 2), 16));
  }
  console.log('');
  console.log('  ★ 真ん中では 1 にきれいに乗り、端で 外れます。');
}

// ============================================================
head('2. ★ 端で どれだけ 失うか ── 「tau の桁数 - c」');
// ============================================================
{
  console.log('');
  console.log('  tau が T 桁 にわたるとき、beta = 1 が ±0.05 に入るのは 何桁 か');
  console.log('');
  console.log('  ' + pad('tau の桁数 T', 16) + padl('★ 1/f の桁数', 18)
    + padl('★ 失った分 T - (1/f)', 24));
  const res = [];
  for (const T of [3, 4, 6, 8, 10, 12]) {
    const S = makeS(-T / 2, T / 2, 1.0, 40000);
    // 端まで 走査して ±0.05 に入る 最長の連続区間
    const N = 2000, lo = -T / 2 - 1, hi = T / 2 + 1;
    let best = 0, run = 0;
    for (let i = 0; i <= N; i++) {
      const lg = lo + (hi - lo) * i / N;
      const b = localBeta(S, Math.pow(10, lg), 0.2, 21);
      if (Math.abs(b - 1) <= 0.05) { run += (hi - lo) / N; if (run > best) best = run; }
      else run = 0;
    }
    res.push([T, best]);
    console.log('  ' + pad(f(T, 0), 16) + padl(f(best, 3) + ' 桁', 18)
      + padl(f(T - best, 3) + ' 桁', 24));
  }
  // 失う分は ほぼ一定か（線形回帰）
  const xs = res.map(r => r[0]), ys = res.map(r => r[1]);
  const k = slope(xs, ys);
  let c = 0; for (let i = 0; i < xs.length; i++) c += ys[i] - k * xs[i]; c /= xs.length;
  console.log('');
  console.log('  ★ 直線に当てると  1/f の桁数 = ' + f(k, 4) + ' × T + ' + f(c, 4));
  console.log('  ★★★ 傾きは ほぼ 1、切片は ' + f(c, 2) + ' ──');
  console.log('  ★★★ つまり「tau の桁数から 約 ' + f(-c, 1) + ' 桁 引いたぶん」が 1/f になります。');
  console.log('  ★★ 第 2 回は「多数の時定数の重ね合わせ」と言いましたが、');
  console.log('  ★★ その「多数」は 少なくとも ' + f(-c, 1) + ' 桁 + 見たい桁数 だけ 要ります。');
}

// ============================================================
head('3. 第 27 回の「beta を決める比」を 測り直す');
// ============================================================
{
  console.log('');
  console.log('  g(tau) ∝ tau^{-gamma} なら beta = 2 - gamma （解析）');
  console.log('  第 27 回は これを「D が変わる桁数 / tau が広がる桁数」と書きました。');
  console.log('');
  console.log('  ' + pad('gamma', 10) + padl('予言 beta = 2-gamma', 22)
    + padl('★ 実測 beta（中央で）', 24) + padl('差', 12));
  for (const g of [0.6, 0.8, 1.0, 1.2, 1.4]) {
    const S = makeS(-6, 6, g, 40000);
    const b = localBeta(S, 1, 0.4, 41);
    console.log('  ' + pad(f(g, 2), 10) + padl(f(2 - g, 6), 22)
      + padl(f(b, 6), 24) + padl(e(Math.abs(b - (2 - g)), 2), 12));
  }
  console.log('');
  console.log('  ★★ beta = 2 - gamma が 数値でも 確認できました。');
  console.log('  ★ 第 27 回の言い方に直すと ── D(E) が「1 桁の tau あたり どれだけ変わるか」が');
  console.log('  ★ gamma を決め、それが そのまま beta を決めます。');
  console.log('');
  console.log('  ★★★ そして これは 反証可能です ──');
  console.log('  ★★★ D(E) を 独立に 測れば、beta は 予言できる。');
}

// ============================================================
head('4. ★ 「1/f は どこまでも続く」は 測れる主張か');
// ============================================================
{
  console.log('');
  console.log('  低域の 折れ曲がりは tau_max のところに出ます。');
  console.log('  それを見るには 観測時間が tau_max より 長くなければならない ──');
  console.log('  第 5 回「宇宙年齢より長い周期は 定数と区別がつかない」と 同じ形。');
  console.log('');
  console.log('  ' + pad('観測時間', 18) + padl('見える 下端 [Hz]', 20)
    + padl('★ そこまでに 見える桁数', 26) + '  （上端 1 kHz として）');
  for (const [T, lab] of [[1, '1 秒'], [3600, '1 時間'], [86400, '1 日'],
                          [2.6e6, '1 か月'], [3.15e7, '1 年'], [3.15e8, '10 年']]) {
    const flo = 1 / T, fhi = 1e3;
    console.log('  ' + pad(lab, 18) + padl(e(flo, 2), 20)
      + padl(f(Math.log10(fhi / flo), 2) + ' 桁', 26));
  }
  console.log('');
  console.log('  ★ 10 年 測っても 11.5 桁。★ 実験で報告されるのは たいてい 6 桁 前後。');
  console.log('  ★★★ つまり「1/f に 下端は無い」という主張は、');
  console.log('  ★★★ 「観測時間より長い tau は 見えない」と 言っているだけかもしれません。');
  console.log('  ★★ 第 55 回の言葉では ── これは「測れない」であって「無い」ではない。');
}

// ============================================================
head('5. では 何を測れば 決着するか');
// ============================================================
console.log('');
const tests = [
  ['★ D(E) を 独立に測る', '◎ 決着する', '★ beta が 予言できる（3 節）'],
  ['観測時間を 伸ばす', '△ 対数でしか伸びない', '第 53 回。10 倍 で 1 桁'],
  ['tau_max を 別に見積もる', '◎ 有望', '★ 活性化エネルギーの上限から'],
  ['温度を 変える', '◎ 有望', '★ tau = tau0 exp(E/kT) なので 全体が ずれる'],
  ['★ 試料を 小さくする', '◎ 有望', '★ 欠陥の数が 減り、離散的になるはず'],
];
console.log('  ' + pad('やること', 28) + pad('判定', 22) + '理由');
for (const t of tests) console.log('  ' + pad(t[0], 28) + pad(t[1], 22) + t[2]);
console.log('');
console.log('  ★★ 「温度を変える」が いちばん強い ──');
console.log('  ★★ tau = tau0 exp(E/kT) なら、T を 2 倍 にすると');
console.log('  ★★ 同じ E の tau が  exp(E/kT) → exp(E/2kT) 、つまり 指数が 半分。');
{
  const kB = 8.617333e-5;   // eV/K
  console.log('');
  console.log('  ' + pad('E [eV]', 12) + [100, 200, 300, 400].map(T =>
    padl('T=' + T + 'K', 16)).join('') + '  （tau/tau0）');
  for (const E of [0.3, 0.5, 0.8, 1.0]) {
    console.log('  ' + pad(f(E, 2), 12) + [100, 200, 300, 400].map(T =>
      padl(e(Math.exp(E / (kB * T)), 2), 16)).join(''));
  }
  console.log('');
  console.log('  ★★★ 300 K で E=1.0 eV の tau は tau0 の 1e16 倍 ──');
  console.log('  ★★★ tau0 = 1e-13 s なら tau = 1e3 s。観測できる範囲です。');
  console.log('  ★ 温度を下げると この tau は 急に長くなり、1/f の下端が 下がるはず。');
  console.log('  ★★ そこが 動くかどうかが、第 2 回の「活性化の重ね合わせ」の 検証になります。');
}

// ============================================================
head('6. 本回のまとめ');
// ============================================================
const rows = [
  ['beta = 2 - gamma', '◎ 数値', '★ 1e-6 の精度で 一致'],
  ['★ 1/f の桁数 = tau の桁数 - c', '◎ 数値', '★ c ≈ 2.2 桁（±0.05 の基準で）'],
  ['第 27 回の比を 再確認', '◎ 数値', 'D(E) が beta を決める'],
  ['★ 「下端が無い」は 測れない主張', '◎ 論理', '★ 観測時間が tau_max を 超えないと 見えない'],
  ['10 年 測っても 11.5 桁', '◎ 数値', '★ 実験の報告は たいてい 6 桁 前後'],
  ['★ 温度を変えるのが いちばん強い', '○ 提案', '★ tau = tau0 exp(E/kT)'],
  ['★ 実データでの検証', '× 未着手', '★ 本稿も 合成データのみ'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 34) + pad(r[1], 22) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 第 2 回の「1/f は 多数の時定数の重ね合わせ」は 正しいが、');
console.log('  ★ その「多数」には 値段がついていました ──');
console.log('  ★★ 見たい桁数 ＋ 約 2 桁 の tau が 要る。');
console.log('  ★★★ そして「1/f に 下端は無い」は、');
console.log('  ★★★ 観測時間を 超えた所については 測れない主張でした（第 5 回）。');
