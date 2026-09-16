// 考える波 第 55 回：手引きの改訂版と、「仮定つき」の洗い直し
//   第 51〜54 回で分かったことを 手引きに入れ、
//   本シリーズの数字が どれだけ 仮定に依っているかを 感度で測る
//   node kaitei.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

console.log('考える波 第 55 回 ── 手引きの改訂版と、「仮定つき」の洗い直し');
console.log('第 XVIII 部を 締める');

// ============================================================
head('1. 手引きの改訂版（第 49 回 → 第 55 回）');
// ============================================================
console.log('');
const steps = [
  ['① 対数対数で描く', '第 1 回', ''],
  ['② 局所的な階数を測る', '第 48 回', '★ 隣との差ではなく 窓での当てはめ（第 51 回）'],
  ['③ 何桁 一定か 数える', '第 27・48 回', '★ 報告できる上限は D - w（第 51 回）'],
  ['④ 曲がっている所を探す', '第 16 回', '★ 窓は 慣性領域の 真ん中に（第 51 回）'],
  ['⑤ 位相も測る', '第 1・8 回', '位相 = 90 alpha 度 か'],
  ['⑥ モーメントを変える', '第 42 回', '★ 先に q* を測る（第 52 回）'],
  ['⑦ 系の大きさと比べる', '第 5・48 回', ''],
  ['★ ⑧ 誤差を 二つに分ける', '★ 第 51 回', '★ 統計 5.57/sqrt(K) dB と 系統'],
  ['★ ⑨ 範囲が足りないなら 買う', '★ 第 54 回', '★ 貼り合わせ／別の観測量／系を変える'],
  ['★ ⑩ 仮定を 数える', '★ 本回', '★ 出した数字ごとに 感度を書く'],
];
console.log('  ' + pad('ステップ', 28) + pad('出どころ', 16) + '第 51〜55 回での 追記');
for (const s of steps) console.log('  ' + pad(s[0], 28) + pad(s[1], 16) + s[2]);
console.log('');
console.log('  ★ ①〜⑦ が 第 49 回、⑧〜⑩ が 第 XVIII 部で 増えた分です。');

// ============================================================
head('2. ★ 本シリーズの数字を 四つに分類する');
// ============================================================
console.log('');
const kinds = { A: '本稿の数値計算', B: '文献値', C: '★ 模型を仮定した値', D: '既存の式の翻訳' };
const items = [
  ['第 1 回', 'dB/oct = 6 alpha', 'D', '定義に近い恒等式'],
  ['第 2 回', '1/f は 半積分', 'A', '重ね合わせを 数値で'],
  ['第 13 回', 's = 1/2 ± sqrt(1/4-lambda)', 'D', '二次方程式'],
  ['第 30 回', 'alpha = (d-3)/2', 'A', '自由場のグリーン関数'],
  ['第 33 回', '小出の K = 0.666661', 'B', '★ 質量は 文献値'],
  ['第 37 回', '3 次元の帰還確率 0.340537', 'A', 'ワトソン積分'],
  ['第 38 回', 'd_s = 1 + 3/z', 'C', '★ 時間方向は 修正しない という模型'],
  ['第 39 回', 'alpha = 2 nu', 'C', '★ AdS/CFT 対応を 仮定'],
  ['第 40 回', '剛性の幅 eps < 0.12', 'C', '★ 古典スピン鎖という 模型'],
  ['第 42 回', 'K41 との差 0.0812 dB/oct', 'C', '★ p 模型で p=0.7 と 置いた'],
  ['第 45 回', 'カシミール圧 1.30e5 Pa', 'A', '完全導体の 理想化つき'],
  ['第 46 回', '測定帯域を出る 1.5 ms', 'A', '★ 帯域の 定義に依る'],
  ['第 47 回', 'n_s → -0.1053 dB/oct', 'B', '★ n_s は 観測値'],
  ['第 51 回', '周期図 1 本 5.57 dB', 'A', '★ 仮定が いちばん少ない'],
  ['第 52 回', 'q* ≈ 4（100 万箱）', 'C', '★ 判定基準 0.1 に依る'],
  ['第 54 回', '較正 1 dB / 3 桁 = 0.1', 'A', '幾何だけ'],
];
console.log('  ' + pad('回', 10) + pad('数字', 30) + pad('種別', 22) + '注');
for (const it of items) {
  console.log('  ' + pad(it[0], 10) + pad(it[1], 30) + pad(kinds[it[2]], 22) + it[3]);
}
const cnt = { A: 0, B: 0, C: 0, D: 0 };
for (const it of items) cnt[it[2]]++;
console.log('');
console.log('  ' + pad('内訳', 22) + Object.keys(kinds).map(k =>
  padl(k + ': ' + cnt[k], 10)).join(''));
console.log('');
console.log('  ★★ 「模型を仮定した値（C）」が ' + cnt.C + ' 件 ── いちばん注意が要る分類です。');
console.log('  ★ 本回は その ' + cnt.C + ' 件に 感度をつけます。');

// ============================================================
head('3. ★★ 感度 ── 仮定を動かすと 数字は どれだけ動くか');
// ============================================================
{
  console.log('');
  // (a) 第 42 回：p 模型の p
  const tauZ = (q, p) => -Math.log(Math.pow(p, q) + Math.pow(1 - p, q)) / Math.LN2;
  const tauE = (q, p) => 1 - q + tauZ(q, p);
  const zeta = (pp, p) => pp / 3 + tauE(pp / 3, p);
  const dBoct = (p) => 3 * (1 + zeta(2, p)) - 5;
  console.log('  (a) 第 42 回：K41 との差 [dB/oct] は p 模型の p に どれだけ依るか');
  console.log('  ' + pad('p', 10) + padl('zeta_6', 14) + padl('★ dB/oct の差', 18)
    + padl('文献の zeta_6 = 1.78 との差', 26));
  for (const p of [0.60, 0.65, 0.70, 0.75, 0.80]) {
    console.log('  ' + pad(f(p, 2), 10) + padl(f(zeta(6, p), 6), 14)
      + padl(f(dBoct(p), 6), 18) + padl(f(zeta(6, p) - 1.78, 4), 26));
  }
  console.log('  ★ zeta_6 を 文献値 1.78 に合わせると p ≈ 0.70。そのとき 0.0812。');
  console.log('  ★★ p を 0.65〜0.75 に振ると 0.0812 は '
    + f(dBoct(0.65), 4) + ' 〜 ' + f(dBoct(0.75), 4) + ' に動きます。');
  console.log('  ★★★ つまり 0.0812 の 有効数字は 2 桁 まで ── 「0.08 dB/oct 級」と書くべき。');
  console.log('');

  // (b) 第 47 回：n_s の観測誤差
  console.log('  (b) 第 47 回：n_s = 0.9649 ± 0.0042 を dB/oct に');
  console.log('  ' + pad('n_s', 14) + padl('3(n_s-1) [dB/oct]', 22));
  for (const ns of [0.9649 - 0.0042, 0.9649, 0.9649 + 0.0042]) {
    console.log('  ' + pad(f(ns, 4), 14) + padl(f(3 * (ns - 1), 6), 22));
  }
  console.log('  ★ -0.1053 ± 0.0126 ── 有効数字は 2 桁。「-0.11 dB/oct 級」。');
  console.log('');

  // (c) 第 46 回：帯域の定義
  console.log('  (c) 第 46 回：「測定帯域を出るまで 1.5 ms」は 帯域の定義に どれだけ依るか');
  const G = 6.67430e-11, c = 299792458, Msun = 1.98892e30;
  const kap = c * c * c * c / (4 * G * Msun) / c;   // 1/s
  const ageU = 13.8e9 * 3.155693e7;
  console.log('  ' + pad('上の周波数', 22) + padl('下の周波数', 22)
    + padl('e 倍の回数', 16) + padl('★ 時間 [ms]', 16));
  for (const [whi, wlo, lab] of [[5e14, 1 / ageU, '可視光 → 宇宙年齢'],
                                 [1e9, 1 / ageU, '電波 → 宇宙年齢'],
                                 [5e14, 1e-3, '可視光 → 1 mHz'],
                                 [5e14, 1, '可視光 → 1 Hz']]) {
    const n = Math.log(whi / wlo);
    console.log('  ' + pad(lab, 22) + padl('', 22) + padl(f(n, 1), 16)
      + padl(f(n / kap / 1e-3, 3), 16));
  }
  console.log('  ★★ 帯域の 下端を 1 Hz に取ると 0.68 ms、宇宙年齢に取ると 1.47 ms。');
  console.log('  ★★★ 2 倍 しか 動きません ── 対数だから、定義への感度が 低い。');
  console.log('  ★ これは 対数の 良い面です（第 53 回の裏返し）。');
  console.log('');

  // (d) 第 51 回：1 桁あたりの本数 n
  console.log('  (d) 第 51 回：最適な窓と 最良誤差は 1 桁あたりの本数 n に どれだけ依るか');
  const beta0 = 5 / 3;
  const logAsym = (R) => (lg) => -beta0 * lg * Math.LN10
    - Math.pow(10, lg - R / 2) - Math.log(1 + Math.pow(10, 2 * (-R / 2 - lg)));
  function slp(xs, ys) {
    const nn = xs.length; let sx = 0, sy = 0, sxx = 0, sxy = 0;
    for (let i = 0; i < nn; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
    return (nn * sxy - sx * sy) / (nn * sxx - sx * sx);
  }
  const biasOf = (R, D) => {
    const M = 3000, xs = [], ys = [], g = logAsym(R);
    for (let i = 0; i < M; i++) { const lg = -D / 2 + D * i / (M - 1);
      xs.push(lg * Math.LN10); ys.push(g(lg)); }
    return Math.abs(3 * (-slp(xs, ys) - beta0));
  };
  const statOf = (n, D) => 3 * (Math.PI / Math.sqrt(6))
    / (Math.sqrt(n * D) * (Math.LN10 / Math.sqrt(12)) * D);
  console.log('  ' + pad('R [桁]', 10) + [30, 100, 300, 1000].map(n =>
    padl('n=' + n, 16)).join(''));
  for (const R of [3, 4, 6]) {
    const row = [30, 100, 300, 1000].map(n => {
      let best = 1e9;
      for (let D = 0.2; D <= R - 0.001; D += 0.05) {
        const t = Math.hypot(statOf(n, D), biasOf(R, D));
        if (t < best) best = t;
      }
      return padl(f(best, 4), 16);
    }).join('');
    console.log('  ' + pad(f(R, 1), 10) + row);
  }
  console.log('  ★ n を 30 倍 にしても 最良誤差は 半分 以下には なりません（系統が残る）。');
  console.log('  ★★ R=3 桁 では n をいくら増やしても 0.13 dB/oct あたりで 頭打ち。');
}

// ============================================================
head('4. ★ 具体例 ── 小出の K は 実験誤差の内か');
// ============================================================
{
  console.log('');
  // 文献値（PDG 相当）と その誤差
  const me = 0.51099895000, dme = 1.5e-10;
  const mmu = 105.6583755, dmmu = 2.3e-6;
  const mtau = 1776.86, dmtau = 0.12;
  const K = (a, b, cc) => (a + b + cc) /
    Math.pow(Math.sqrt(a) + Math.sqrt(b) + Math.sqrt(cc), 2);
  const K0 = K(me, mmu, mtau);
  const dK = Math.abs(K(me, mmu, mtau + dmtau) - K(me, mmu, mtau - dmtau)) / 2;
  console.log('  ' + pad('量', 30) + padl('値', 20));
  console.log('  ' + pad('K（中心値）', 30) + padl(f(K0, 9), 20));
  console.log('  ' + pad('2/3', 30) + padl(f(2 / 3, 9), 20));
  console.log('  ' + pad('★ 差', 30) + padl(e(K0 - 2 / 3, 3), 20));
  console.log('  ' + pad('★ m_tau の誤差 ±0.12 MeV から', 30) + padl('±' + e(dK, 3), 20));
  console.log('  ' + pad('★ 差 / 誤差', 30) + padl(f(Math.abs(K0 - 2 / 3) / dK, 3), 20));
  console.log('');
  console.log('  ★★★ 差は 誤差の ' + f(Math.abs(K0 - 2 / 3) / dK, 1) + ' 倍 ──');
  if (Math.abs(K0 - 2 / 3) / dK < 1) {
    console.log('  ★★★ つまり 現在の測定では K = 2/3 と 区別がつきません。');
  } else {
    console.log('  ★★★ つまり 形式的には 2/3 から ずれています（ただし 2 sigma 未満なら 有意ではない）。');
  }
  console.log('  ★ 第 33 回は「K = 2/3 ⟺ A = sqrt2」と書きましたが、');
  console.log('  ★ 「2/3 ちょうど」かどうかは 上の比較で 判断すべきです。');
  console.log('  ★★ そして m_tau の誤差が 縮めば、この判定は 変わり得ます。');
  console.log('  ★ なお 上の誤差は m_tau のぶんだけ です（m_e, m_mu の誤差は');
  console.log('  ★ それぞれ ' + e(dme / me, 1) + ' 、 ' + e(dmmu / mmu, 1)
    + ' の相対精度で、効きません）。');
}

// ============================================================
head('5. 確からしさの 五段階');
// ============================================================
console.log('');
const ladder = [
  ['① 恒等式・定義', '動かない', 'dB/oct = 6 alpha（第 1 回）'],
  ['② 本稿の数値計算', '再現できる', '★ 周期図 5.57 dB（第 51 回）'],
  ['③ 文献値を使った計算', '文献に依る', 'n_s（第 47 回）、レプトン質量（第 33 回）'],
  ['★ ④ 模型を仮定した値', '★ 仮定に依る', '★ p 模型の 0.0812（第 42 回）'],
  ['★ ⑤ 対応を仮定した翻訳', '★ 前提ごと 仮定', '★ AdS/CFT（第 39 回）'],
];
console.log('  ' + pad('段', 24) + pad('性質', 16) + '例');
for (const l of ladder) console.log('  ' + pad(l[0], 24) + pad(l[1], 16) + l[2]);
console.log('');
console.log('  ★★ 本シリーズは ①〜③ を「◎」、④ を「△ 仮定つき」、');
console.log('  ★★ ⑤ を「翻訳」と 書き分けてきました ── 第 43・50 回の方針です。');
console.log('  ★★★ 本回で足したのは、④ と ⑤ に 感度の数字をつけたことです。');

// ============================================================
head('6. 本回のまとめ');
// ============================================================
const rows = [
  ['手引きが 7 → 10 手順に', '◎ 整理', '★ ⑧誤差の二分・⑨範囲を買う・⑩仮定を数える'],
  ['数字を 四つに分類', '◎ 整理', '★ 模型を仮定した値が ' + cnt.C + ' 件'],
  ['★ 第 42 回 0.0812 の感度', '◎ 数値', '★ p=0.65〜0.75 で 0.04〜0.13'],
  ['★ 第 47 回 -0.1053 の感度', '◎ 数値', '★ ±0.0126（観測の誤差から）'],
  ['★ 第 46 回 1.5 ms の感度', '◎ 数値', '★ 帯域の定義を変えても 2 倍 以内'],
  ['第 51 回 最良誤差の n 依存', '◎ 数値', '★ R=3 桁 では 0.13 で頭打ち'],
  ['★ 小出の K と 実験誤差', '◎ 数値', '★ 差 / 誤差 を 計算'],
  ['確からしさの 五段階', '◎ 整理', '★ ④⑤ に 感度をつけた'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 32) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 数字を出したら、その数字が「何に どれだけ 依るか」も 一緒に出す。');
console.log('  ★★ 第 42 回の 0.0812 は 有効数字 2 桁、第 47 回の -0.1053 も 2 桁 でした。');
console.log('  ★★★ 本シリーズは これまで 桁を 書きすぎていた ── そこを ここで 直します。');
