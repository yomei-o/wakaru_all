// 考える波 第 51 回：桁数に 誤差棒をつける
//   雑音のある実データから「何桁の冪則か」を言うには、何が必要か
//   node gosa.js
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
function gauss(rnd) {
  const u = Math.max(1e-12, rnd()), v = rnd();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}
function slope(xs, ys) {
  const n = xs.length; let sx = 0, sy = 0, sxx = 0, sxy = 0;
  for (let i = 0; i < n; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
  return (n * sxy - sx * sy) / (n * sxx - sx * sx);
}
function sd(a) {
  const n = a.length; let m = 0; for (const x of a) m += x; m /= n;
  let s = 0; for (const x of a) s += (x - m) * (x - m);
  return { mean: m, sd: Math.sqrt(s / (n - 1)) };
}

const EULER = 0.5772156649015329;

console.log('考える波 第 51 回 ── 桁数に 誤差棒をつける');
console.log('第 49 回の手引きは 雑音のない関数でしか試していなかった');

// ============================================================
head('1. 対数ペリオドグラムの 雑音は いつでも同じ大きさ');
// ============================================================
// 周期図の 1 本は 真のスペクトル × (chi^2_2 / 2)
//   ln(chi^2_2/2) の 平均 = -gamma 、 分散 = pi^2/6
{
  const rnd = mulberry32(20260917);
  const N = 400000; const v = [];
  for (let i = 0; i < N; i++) {
    const a = gauss(rnd), b = gauss(rnd);
    v.push(Math.log((a * a + b * b) / 2));         // chi^2_2 / 2
  }
  const s = sd(v);
  console.log('');
  console.log('  周期図の 1 本 ＝ 真のスペクトル × (chi^2_2 / 2)');
  console.log('  → ln をとると 加法的な雑音になる');
  console.log('');
  console.log('  ' + pad('量', 34) + padl('モンテカルロ', 16) + padl('理論', 16));
  console.log('  ' + pad('平均 E[ln(chi^2_2/2)]', 34) + padl(f(s.mean, 6), 16)
    + padl(f(-EULER, 6), 16));
  console.log('  ' + pad('標準偏差', 34) + padl(f(s.sd, 6), 16)
    + padl(f(Math.PI / Math.sqrt(6), 6), 16));
  const dB = Math.PI / Math.sqrt(6) * 10 / Math.LN10;
  console.log('  ' + pad('★ 同じものを dB で', 34) + padl(f(s.sd * 10 / Math.LN10, 4) + ' dB', 16)
    + padl(f(dB, 4) + ' dB', 16));
  console.log('');
  console.log('  ★★★ 周期図 1 本の ばらつきは ' + f(dB, 2) + ' dB。');
  console.log('  ★★★ これは 信号の強さにも 周波数にも 測定器にも よりません。');
  console.log('  ★ 平均が -0.5772（＝ -2.51 dB）ずれるのは 切片に効くだけで、傾きには効かない。');
}

// ============================================================
head('2. 傾きの誤差は 1.2825 / sqrt(M)');
// ============================================================
// ln S = c - beta ln f + eps 、 sd(eps) = pi/sqrt(6) = 1.2825
// 周波数が 0〜F に一様なら ln f の分散は ちょうど 1 なので
//   sd(beta) = 1.2825 / sqrt(M)
{
  const rnd = mulberry32(7);
  console.log('');
  console.log('  ln S = c - beta ln f + eps 、 sd(eps) = pi/sqrt(6) = '
    + f(Math.PI / Math.sqrt(6), 4));
  console.log('  周波数が 0〜F に一様なら Var(ln f) = 1 ちょうど');
  console.log('  → 予言： sd(beta) = 1.2825 / sqrt(M)');
  console.log('');
  console.log('  ' + pad('M（周期図の本数）', 20) + padl('sd(beta)（実測）', 18)
    + padl('1.2825/sqrt(M)', 18) + padl('比', 10));
  for (const M of [50, 200, 1000, 5000, 20000]) {
    const est = [];
    for (let trial = 0; trial < 400; trial++) {
      const xs = [], ys = [];
      for (let i = 1; i <= M; i++) {
        const fr = i / M;                       // 0〜1 に一様
        const a = gauss(rnd), b = gauss(rnd);
        ys.push(-1.6667 * Math.log(fr) + Math.log((a * a + b * b) / 2));
        xs.push(Math.log(fr));
      }
      est.push(-slope(xs, ys));
    }
    const s = sd(est);
    const pred = (Math.PI / Math.sqrt(6)) / Math.sqrt(M);
    console.log('  ' + pad(M, 20) + padl(f(s.sd, 6), 18) + padl(f(pred, 6), 18)
      + padl(f(s.sd / pred, 4), 10));
  }
  console.log('');
  console.log('  ★ Var(ln f) = 1 は「線形に並んだ周波数」の性質です。');
  console.log('  ★ 桁数を広げても Var(ln f) は 1 のまま ── 効くのは 本数 M だけ。');
}

// ============================================================
head('3. ★ 第 42・47 回の「ずれ」を 測るのに 何本 要るか');
// ============================================================
{
  console.log('');
  console.log('  dB/oct = 3 beta なので sd(dB/oct) = 3 × 1.2825 / sqrt(M) = 3.85 / sqrt(M)');
  console.log('');
  console.log('  ' + pad('測りたい差', 30) + padl('1σ に要る M', 16)
    + padl('3σ に要る M', 16) + padl('試料長 N', 14));
  const K = 3 * Math.PI / Math.sqrt(6);
  for (const [d, lab] of [[0.0812, '★ 乱流の間欠性（第 42 回）'],
                          [0.1053, '★ 宇宙の n_s のずれ（第 47 回）'],
                          [0.5, '1/f と 1/f^{1.17} の差'],
                          [3.0, '1 階ぶんの差（α=0.5）']]) {
    const m1 = Math.pow(K / d, 2), m3 = Math.pow(3 * K / d, 2);
    console.log('  ' + pad(lab, 30) + padl(e(m1, 2), 16) + padl(e(m3, 2), 16)
      + padl(e(2 * m3, 2), 14));
  }
  console.log('');
  console.log('  ★ 0.081 dB/oct を 3σ で言うには 周期図 2 万本 ＝ 4 万点 の試料。');
  console.log('  ★★ 意外に 少ない。統計だけなら 手が届きます。');
  console.log('  ★★★ ところが ── 実際に難しいのは そこではありません（次節）。');
}

// ============================================================
head('4. 系統誤差 ── まず 打ち消しあうことに 気づく');
// ============================================================
{
  const beta0 = 5 / 3;
  // (a) 対称な模型：両端とも 同じ形の曲がり
  const logSym = (R) => (lg) => -beta0 * lg * Math.LN10
    - Math.log(1 + Math.pow(10, 2 * (lg - R / 2)))
    - Math.log(1 + Math.pow(10, 2 * (-R / 2 - lg)));
  // (b) 非対称な模型：高域は 指数的な切断（散逸域）、低域は 冪の曲がり
  const logAsym = (R) => (lg) => -beta0 * lg * Math.LN10
    - Math.pow(10, lg - R / 2)
    - Math.log(1 + Math.pow(10, 2 * (-R / 2 - lg)));
  const fitBias = (logS, lo, hi) => {
    const M = 4000, xs = [], ys = [];
    for (let i = 0; i < M; i++) {
      const lg = lo + (hi - lo) * i / (M - 1);
      xs.push(lg * Math.LN10); ys.push(logS(lg));
    }
    return 3 * (-slope(xs, ys) - beta0);
  };
  console.log('');
  console.log('  (a) 対称な模型： S = f^{-5/3} / [(1+(f/f_hi)^2)(1+(f_lo/f)^2)]');
  console.log('      慣性領域の 真ん中に 幅 D の窓を置く');
  console.log('');
  console.log('  ' + pad('R [桁]', 14) + [0.5, 1, 2, 3].map(d => padl('D=' + d, 14)).join(''));
  for (const R of [3, 4, 6]) {
    console.log('  ' + pad(f(R, 1), 14) + [0.5, 1, 2, 3].map(D =>
      padl(D > R ? '-' : e(Math.abs(fitBias(logSym(R), -D / 2, D / 2)), 1), 14)).join(''));
  }
  console.log('');
  console.log('  ★★★ ほぼ 完全に 0 ── 両端の曲がりが 傾きに 逆向きに効いて 打ち消しあいます。');
  console.log('  ★★ つまり「窓を 慣性領域の 真ん中に 置く」だけで 主要な系統誤差は消える。');
  console.log('  ★ これは 実務でいちばん 効く注意でした。');
  console.log('');
  console.log('  (b) 非対称な模型： 高域は 指数的な切断、低域は 冪の曲がり');
  console.log('      （実際の乱流に 近い。散逸域の落ち方は 急）');
  console.log('');
  console.log('  ' + pad('R [桁]', 14) + [0.5, 1, 2, 3].map(d => padl('D=' + d, 14)).join(''));
  for (const R of [3, 4, 6]) {
    console.log('  ' + pad(f(R, 1), 14) + [0.5, 1, 2, 3].map(D =>
      padl(D > R ? '-' : f(fitBias(logAsym(R), -D / 2, D / 2), 4), 14)).join(''));
  }
  console.log('');
  console.log('  ★★ 打ち消しが 効かなくなり、D = 3 桁 では 0.1 dB/oct を 超えます。');
  console.log('');
  console.log('  (c) 窓を 真ん中から ずらすと どうなるか（対称な模型、R=4、D=2）');
  console.log('  ' + pad('中心のずれ [桁]', 18) + padl('★ 系統誤差 [dB/oct]', 22));
  for (const sh of [0, 0.25, 0.5, 0.75, 1.0]) {
    console.log('  ' + pad(f(sh, 2), 18)
      + padl(f(fitBias(logSym(4), -1 + sh, 1 + sh), 5), 22));
  }
  console.log('');
  console.log('  ★★★ 0.5 桁 ずらすだけで 0.03 dB/oct 級 ── 打ち消しは すぐ壊れます。');
  global.__biasAsym = (R, D) => fitBias(logAsym(R), -D / 2, D / 2);
}

// ============================================================
head('5. ★★★ 窓の幅には 最適値がある');
// ============================================================
{
  const biasOf = global.__biasAsym;
  console.log('');
  console.log('  非対称な模型（4 節 (b)）で、統計と系統を 合わせる。');
  console.log('  対数等間隔に 1 桁あたり n 本の 独立な推定値があるとして');
  console.log('    統計誤差 [dB/oct] = 3 × 1.2825 / ( sqrt(nD) × (ln10/sqrt12) × D )');
  console.log('');
  const statOf = (n, D) => 3 * (Math.PI / Math.sqrt(6))
    / (Math.sqrt(n * D) * (Math.LN10 / Math.sqrt(12)) * D);
  for (const R of [3, 4, 6]) {
    console.log('  慣性領域 R = ' + R + ' 桁 （n = 100 本/桁）');
    console.log('  ' + pad('窓 D [桁]', 12) + padl('統計', 14)
      + padl('系統', 14) + padl('★ 合計', 14));
    let best = { D: 0, tot: 1e9 };
    for (let D = 0.2; D <= R - 0.001; D += 0.05) {
      const st = statOf(100, D), sy = Math.abs(biasOf(R, D));
      const tot = Math.sqrt(st * st + sy * sy);
      if (tot < best.tot) best = { D: D, tot: tot, st: st, sy: sy };
    }
    for (const D of [0.5, 1, 1.5, 2, 2.5, 3].filter(x => x < R)) {
      const st = statOf(100, D), sy = Math.abs(biasOf(R, D));
      const tot = Math.sqrt(st * st + sy * sy);
      console.log('  ' + pad(f(D, 2), 12) + padl(f(st, 5), 14) + padl(f(sy, 5), 14)
        + padl(f(tot, 5), 14) + (Math.abs(D - best.D) < 0.03 ? '  ★ 最適' : ''));
    }
    console.log('  ' + pad('★ 最適', 12) + padl('D = ' + f(best.D, 2) + ' 桁', 14)
      + padl('統計 ' + f(best.st, 4), 14) + padl('系統 ' + f(best.sy, 4), 14)
      + padl('合計 ' + f(best.tot, 4) + ' dB/oct', 26));
    console.log('');
  }
  console.log('  ★★★ 最適点では 統計誤差と 系統誤差が 同じくらいになります。');
  console.log('  ★★ 慣性領域が 広いほど 最良の誤差は 小さくなる ──');
  console.log('  ★★ 「長く測る」より「広い慣性領域を持つ系を選ぶ」ほうが 効きます。');
}

// ============================================================
head('6. ★ 桁数そのものに 誤差棒をつける');
// ============================================================
// 第 49 回の「局所的な階数が平坦な桁数」を 雑音つきで やると どうなるか
{
  const rnd = mulberry32(99);
  console.log('');
  console.log('  第 49 回の手順（局所的な階数が ±0.1 の窓）を 雑音つきで やってみる');
  console.log('  真の信号： 6 桁 にわたる 冪則（beta = 1、つまり 1/f）');
  console.log('');
  console.log('  ' + pad('平均本数 K', 14) + padl('1 点あたりの sd [dB]', 22)
    + padl('★ 測れた「平坦な桁数」', 24) + padl('真の値', 12));
  for (const K of [1, 10, 100, 1000, 10000]) {
    // 対数等間隔に 60 点（6 桁）、各点は K 本の平均
    const trials = 60; const got = [];
    for (let t = 0; t < trials; t++) {
      const lf = [], ly = [];
      for (let i = 0; i < 60; i++) {
        const lg = -3 + 6 * i / 59;
        let s = 0;
        for (let k = 0; k < K; k++) { const a = gauss(rnd), b = gauss(rnd); s += (a * a + b * b) / 2; }
        lf.push(lg * Math.LN10);
        ly.push(-1 * lg * Math.LN10 + Math.log(s / K));
      }
      // 隣り合う点から 局所的な階数を作り、±0.1 に入る区間の 最長を数える
      const al = [];
      for (let i = 1; i < 60; i++) al.push((ly[i] - ly[i - 1]) / (lf[i] - lf[i - 1]));
      let best = 0, run = 0;
      for (let i = 0; i < al.length; i++) {
        if (Math.abs(-al[i] - 1) <= 0.1) { run++; if (run > best) best = run; }
        else run = 0;
      }
      got.push(best * 6 / 59);
    }
    const s = sd(got);
    const sdb = (Math.PI / Math.sqrt(6)) / Math.sqrt(K) * 10 / Math.LN10;
    console.log('  ' + pad(K, 14) + padl(f(sdb, 3), 22)
      + padl(f(s.mean, 3) + ' ± ' + f(s.sd, 3) + ' 桁', 24) + padl('6.0 桁', 12));
  }
  console.log('');
  console.log('  ★★★ 平均を 1 万本 取っても、素朴な手順では 6 桁 を復元できません。');
  console.log('  ★★★ 隣同士の差で階数を作ると、雑音が 差で 増幅されるからです。');
  console.log('  ★ 第 49 回の手引きは、このままでは 実データに使えない。');
}

// ============================================================
head('7. ★ 直し方 ── 差ではなく、窓ごとの当てはめで測る');
// ============================================================
{
  const rnd = mulberry32(12345);
  console.log('');
  console.log('  局所的な階数を「隣との差」ではなく「幅 w の窓での最小二乗」で作る');
  console.log('  → 雑音が sqrt(本数) で 減り、桁数が 復元できる');
  console.log('');
  console.log('  ' + pad('窓の幅 [桁]', 14) + padl('階数の sd', 16)
    + padl('★ 測れた「平坦な桁数」', 24) + padl('真の値', 12));
  const K = 100;
  for (const wdec of [0.1, 0.3, 0.6, 1.0, 1.5]) {
    const trials = 60; const got = []; const sds = [];
    for (let t = 0; t < trials; t++) {
      const lf = [], ly = [];
      const NP = 300;
      for (let i = 0; i < NP; i++) {
        const lg = -3 + 6 * i / (NP - 1);
        let s = 0;
        for (let k = 0; k < K; k++) { const a = gauss(rnd), b = gauss(rnd); s += (a * a + b * b) / 2; }
        lf.push(lg); ly.push(-1 * lg * Math.LN10 + Math.log(s / K));
      }
      const half = Math.max(1, Math.round(wdec / 2 / (6 / (NP - 1))));
      const al = [], pos = [];
      for (let i = half; i < NP - half; i++) {
        const xs = [], ys = [];
        for (let j = i - half; j <= i + half; j++) { xs.push(lf[j] * Math.LN10); ys.push(ly[j]); }
        al.push(-slope(xs, ys)); pos.push(lf[i]);
      }
      const s2 = sd(al); sds.push(s2.sd);
      let best = 0, run = 0;
      for (let i = 0; i < al.length; i++) {
        if (Math.abs(al[i] - 1) <= 0.1) { run++; if (run > best) best = run; }
        else run = 0;
      }
      got.push(best * (6 / (NP - 1)));
    }
    const s = sd(got), ss = sd(sds);
    console.log('  ' + pad(f(wdec, 2), 14) + padl(f(ss.mean, 5), 16)
      + padl(f(s.mean, 3) + ' ± ' + f(s.sd, 3) + ' 桁', 24) + padl('6.0 桁', 12));
  }
  console.log('');
  console.log('  ★★ 窓を広げるほど 階数は静かになり、桁数が 6 に近づきます。');
  console.log('  ★★★ ただし 幅 w の窓は 両端で w/2 ずつ 使えなくなるので、');
  console.log('  ★★★ 報告できる桁数の 上限は 6 - w に下がります。');
  console.log('  ★ 実際 w=1.0 で 5.017（上限 5.0）、w=1.5 で 4.535（上限 4.5）── 端で頭打ち。');
  console.log('  ★★ つまり 狭すぎると 雑音で 途切れ、広すぎると 端を失う。');
  console.log('  ★★★ 窓の幅そのものが、第 49 回の「分解能の配分」でした（第 9・22 回）。');
}

// ============================================================
head('8. 最短の手順（第 49 回の手引きへの追記）');
// ============================================================
console.log('');
const recipe = [
  ['③-a 1 点の誤差を 5.57 dB と置く', '周期図なら いつでもこの値'],
  ['③-b K 本 平均したら 5.57/sqrt(K) dB', '平均は 周波数方向でも 試行方向でもよい'],
  ['③-c 局所的な階数は 窓での当てはめで', '★ 隣との差は 使わない（6 節）'],
  ['③-d 窓の幅は 0.5〜1 桁 から始める', '広げると静かになるが 曲がりも消える'],
  ['③-e 系統誤差を 別に見積もる', '★ 窓の端を 曲がりから 1 桁 以上 離す'],
  ['③-f 統計と系統が 釣り合う M で止める', 'それ以上 測っても 精度は上がらない'],
];
console.log('  ' + pad('手順', 34) + '注意');
for (const r of recipe) console.log('  ' + pad(r[0], 34) + r[1]);

// ============================================================
head('9. 本回のまとめ');
// ============================================================
const rows = [
  ['★ 周期図 1 本の ばらつき', '◎ 数値', '★ 5.57 dB（何によらず一定）'],
  ['平均のずれ -0.5772', '◎ 数値', '切片に効くだけ、傾きには効かない'],
  ['sd(beta) = 1.2825/sqrt(M)', '◎ 数値', '★ 桁数ではなく 本数で決まる'],
  ['★ 0.081 dB/oct に要る試料長', '◎ 数値', '★ 3σ で 4 万点'],
  ['★ 対称な窓では 系統誤差が 打ち消す', '◎ 数値', '★ 真ん中に置くだけで消える'],
  ['ずらすと すぐ壊れる', '◎ 数値', '0.5 桁 で 0.03 dB/oct 級'],
  ['★★ 窓の幅に 最適値がある', '◎ 数値', '★ そこで 統計と系統が 同じ大きさ'],
  ['★ 素朴な桁数推定は 破綻する', '◎ 数値', '★ 1 万本 平均しても 復元できず'],
  ['★ 窓での当てはめで 直る', '◎ 数値', '★ 窓 1 桁 で 6 桁 に近づく'],
  ['★ 実データでの検証', '× 未着手', '★ 本稿も 合成データのみ'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 34) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 「何桁 の冪則か」に 誤差棒はつけられます。');
console.log('  ★ ただし その誤差棒は、長く測れば縮む部分（統計）と');
console.log('  ★ 窓の取り方でしか縮まない部分（系統）に 分かれていました。');
console.log('  ★★ そして 第 42・47 回の 0.1 dB/oct 級の ずれは、');
console.log('  ★★ 窓を 慣性領域の 真ん中に置けば 主要な系統誤差は 打ち消しますが、');
console.log('  ★★ 0.5 桁 ずらすだけで 0.03 dB/oct 級 ── そこが 難しさの正体でした。');
