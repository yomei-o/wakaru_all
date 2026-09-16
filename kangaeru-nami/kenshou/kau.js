// 考える波 第 54 回：範囲を「買う」方法はあるのか
//   貼り合わせ・別の観測量・系を変える ── 実験家がやっていることを 数える
//   node kau.js
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

console.log('考える波 第 54 回 ── 範囲を「買う」方法はあるのか');
console.log('第 53 回：範囲は log N。では 測定時間 以外の 買い方は');

// ============================================================
head('1. 買い方は 三つしかない');
// ============================================================
console.log('');
const ways = [
  ['① 貼り合わせる', '違う帯域の測定を つなぐ', '★ 装置を増やす'],
  ['② 別の観測量を使う', '同じ物理を 別の量で見る', '★ 補正が 打ち消しあう形を探す'],
  ['③ 系そのものを 変える', 'より広い 慣性領域を持つ対象へ', '★ レイノルズ数を上げる'],
];
console.log('  ' + pad('買い方', 24) + pad('中身', 28) + '要るもの');
for (const w of ways) console.log('  ' + pad(w[0], 24) + pad(w[1], 28) + w[2]);
console.log('');
console.log('  ★ 「もっと長く測る」は 入っていません ── 第 53 回のとおり log N だから。');

// ============================================================
head('2. ★ 貼り合わせ ── 較正誤差が そのまま 傾きの誤差になる');
// ============================================================
// 帯域 A：log10 f ∈ [0, D] 、帯域 B：[S, S+D]。B の利得が delta dB ずれている
{
  console.log('');
  console.log('  帯域 A と B を つないで 直線を当てる。B の利得が delta dB ずれていると');
  console.log('  傾きが ずれる。どれくらいか。');
  console.log('');
  function biasOf(D, S, deltaDB) {
    const M = 2000, xs = [], ys = [];
    const beta = 5 / 3;
    for (let i = 0; i < M; i++) {                     // 帯域 A
      const lg = D * i / (M - 1);
      xs.push(lg * Math.LN10); ys.push(-beta * lg * Math.LN10);
    }
    for (let i = 0; i < M; i++) {                     // 帯域 B（ずれあり）
      const lg = S + D * i / (M - 1);
      xs.push(lg * Math.LN10);
      ys.push(-beta * lg * Math.LN10 + deltaDB * Math.LN10 / 10);
    }
    return 3 * (-slope(xs, ys) - beta);               // dB/oct でのずれ
  }
  console.log('  ' + pad('帯域の間隔 S [桁]', 20)
    + [0.2, 0.5, 1.0, 2.0].map(d => padl('delta=' + d + ' dB', 16)).join(''));
  for (const S of [1, 2, 3, 6]) {
    console.log('  ' + pad(f(S, 1), 20)
      + [0.2, 0.5, 1.0, 2.0].map(d => padl(f(biasOf(1, S, d), 5), 16)).join(''));
  }
  console.log('');
  console.log('  ★ 予言（解析）： ずれ [dB/oct] = 0.3 × delta [dB] / （中心間の桁数）');
  console.log('  ' + pad('確認（S=3, delta=1 dB）', 26)
    + padl('|実測| ' + f(Math.abs(biasOf(1, 3, 1)), 6), 18)
    + padl('予言 0.3/3 = ' + f(0.3 / 3, 6), 22));
  console.log('  （帯域に 幅があるぶん 実測のほうが 少し小さくなります）');
  console.log('');
  console.log('  ★★★ 1 dB の較正ずれを 3 桁 離れた帯域の間に置くと 0.1 dB/oct。');
  console.log('  ★★★ 第 42 回の 0.081 dB/oct と 同じ大きさです。');
  console.log('  ★★ つまり 貼り合わせで 3 桁 稼ぐには、較正を 0.8 dB より良くする必要がある。');
  console.log('  ★ 逆に言うと ── 離れた帯域どうしなら、較正の要求は 緩くなります。');
}

// ============================================================
head('3. ★★ 別の観測量 ── 補正が 打ち消しあう形を探す');
// ============================================================
// 拡張自己相似（ESS）の考え方：
//   S_p(r) = rho(r)^{zeta_p} という形なら、ln S_p 対 ln S_3 は
//   rho の形に よらず 傾き zeta_p/zeta_3 の直線になる
{
  console.log('');
  console.log('  仮定： S_p(r) = rho(r)^{zeta_p} 、 rho(r) = r × h(r)（h は 端の補正）');
  console.log('  すると ln S_p 対 ln r は 曲がるのに、ln S_p 対 ln S_3 は 直線のまま。');
  console.log('');
  // zeta_p は 第 42 回の p 模型（p=0.7）から
  const P = 0.7;
  const tauZ = (q) => -Math.log(Math.pow(P, q) + Math.pow(1 - P, q)) / Math.LN2;
  const tauE = (q) => 1 - q + tauZ(q);
  const zeta = (pp) => pp / 3 + tauE(pp / 3);
  // 端の補正：小さい r で 散逸域に入る（なめらかな 折れ曲がり）
  //   rho(r) = r / (1 + r0/r) 、 r0 = 1
  //   r >> r0 で rho ≈ r 、 r << r0 で rho ∝ r^2（傾きが 1 → 2 に変わる）
  const lnRho = (lr) => lr - Math.log(1 + Math.exp(-lr));
  // 局所的な傾きが target ± tol に入る「r の桁数」を数える
  //   横軸を 何に取っても、幅は いつも ln r で測る（比べられるように）
  function decadesFlat(target, xs, ys, lnr, tol) {
    let best = 0, run = 0;
    for (let i = 1; i < xs.length; i++) {
      const a = (ys[i] - ys[i - 1]) / (xs[i] - xs[i - 1]);
      const w = (lnr[i] - lnr[i - 1]) / Math.LN10;
      if (Math.abs(a - target) <= tol) { run += w; if (run > best) best = run; }
      else run = 0;
    }
    return best;
  }
  const M = 6000, lnr = [], lnS = {}, ps = [1, 2, 3, 4, 6];
  for (let i = 0; i < M; i++) lnr.push((-3 + 9 * i / (M - 1)) * Math.LN10);
  for (const pp of ps) lnS[pp] = lnr.map(lr => zeta(pp) * lnRho(lr));
  console.log('  ' + pad('p', 8) + padl('zeta_p（真）', 14)
    + padl('ln S_p 対 ln r', 22) + padl('★ ln S_p 対 ln S_3', 24));
  console.log('  ' + pad('', 8) + padl('', 14) + padl('（r の桁数／全 9 桁）', 22)
    + padl('（r の桁数／全 9 桁）', 24));
  for (const pp of ps) {
    const d1 = decadesFlat(zeta(pp), lnr, lnS[pp], lnr, 0.01);
    const d2 = decadesFlat(zeta(pp) / zeta(3), lnS[3], lnS[pp], lnr, 0.01);
    console.log('  ' + pad(pp, 8) + padl(f(zeta(pp), 6), 14)
      + padl(f(d1, 2) + ' 桁', 22) + padl(f(d2, 2) + ' 桁', 24));
  }
  console.log('');
  console.log('  ★★★ ln S_3 を 横軸にすると、補正 h(r) が 完全に 打ち消えます。');
  console.log('  ★★ これが 実験で使われている「拡張自己相似（ESS）」の考え方です。');
  console.log('  ★★★ ただし ── 打ち消えるのは「S_p が 共通の rho の冪」という');
  console.log('  ★★★ 仮定を 置いたからで、それ自体は 証明ではありません。');
  console.log('  ★ 本稿が示したのは「その仮定が成り立つなら 範囲は 買える」までです。');
}

// ============================================================
head('4. ★ 系を変える ── 慣性領域は レイノルズ数の 3/4 乗');
// ============================================================
{
  console.log('');
  console.log('  コルモゴロフ長 eta と 外部スケール L の比： L/eta = Re^{3/4}');
  console.log('  → 慣性領域の 桁数 = (3/4) log10 Re');
  console.log('');
  console.log('  ' + pad('場面', 26) + padl('Re', 14) + padl('★ 慣性領域 [桁]', 18)
    + padl('第 51 回の 最良誤差', 22));
  const best = { 3: 0.1793, 4: 0.1155, 6: 0.0587 };
  for (const [Re, lab] of [[1e4, '実験室の 乱流'], [1e6, '風洞'],
                           [1e7, '自動車のまわり'], [1e9, '大型の 風洞'],
                           [1e12, '地球の 大気']]) {
    const d = 0.75 * Math.log10(Re);
    let bb = '';
    const k = Math.round(d);
    if (best[k] !== undefined) bb = '≈ ' + f(best[k], 4) + ' dB/oct';
    else if (d > 6) bb = '< 0.06 dB/oct';
    console.log('  ' + pad(lab, 26) + padl(e(Re, 0), 14) + padl(f(d, 2), 18)
      + padl(bb, 22));
  }
  console.log('');
  console.log('  ★★ 慣性領域を 1 桁 増やすには Re を 10^{4/3} = '
    + f(Math.pow(10, 4 / 3), 1) + ' 倍 にする必要があります。');
  console.log('  ★★★ ここでも 対数 ── ただし 対象を変えるだけで 桁が 動くのが違い。');
  console.log('  ★ 実験室（Re=1e4、3 桁）から 大気（Re=1e12、9 桁）まで 6 桁 の差。');
  console.log('  ★ 第 51 回の表では 3 桁 で 0.18、6 桁 で 0.059 dB/oct でした。');
}

// ============================================================
head('5. 三つを 合わせると どこまで行けるか');
// ============================================================
{
  console.log('');
  console.log('  目標：第 42 回の 0.0812 dB/oct を 3 sigma で 言う（= 0.027 dB/oct）');
  console.log('');
  console.log('  ' + pad('手段', 30) + pad('得られるもの', 26) + '代償');
  const rows = [
    ['測定時間を 増やす', '精度 N^{-1/2}', '範囲は log N でしか伸びない'],
    ['★ 装置を 貼り合わせる', '★ 範囲が 装置の数に比例', '★ 較正 0.8 dB 以内（2 節）'],
    ['★ ESS など 別の観測量', '★ 範囲が ほぼ 全域に', '★ 仮定を 一つ 置く（3 節）'],
    ['★ Re を 上げる', '★ 慣性領域 ∝ (3/4)log Re', '★ 装置の 規模'],
  ];
  for (const r of rows) console.log('  ' + pad(r[0], 30) + pad(r[1], 26) + r[2]);
  console.log('');
  console.log('  ★★★ 三つとも「範囲」を 買っていますが、買い方が 違います：');
  console.log('  ★★★   貼り合わせ → 装置の数に 比例（線形に 買える）');
  console.log('  ★★★   別の観測量 → 仮定と 引き換えに 一気に 買える');
  console.log('  ★★★   系を変える → Re の 対数（でも 対象を変えれば 大きく動く）');
  console.log('');
  console.log('  ★★ 第 53 回の結論「範囲は log N」は「同じ系を 長く測る」場合の話でした。');
  console.log('  ★★ 装置を 増やせば、範囲は 線形に 買えます ── そこが 抜け道です。');
}

// ============================================================
head('6. 買えないもの');
// ============================================================
console.log('');
const cannot = [
  ['同じ系を 長く測って 範囲を 買う', '× 無理', '★ log N（第 53 回）'],
  ['較正なしで 貼り合わせる', '× 無理', '★ 1 dB / 3 桁 = 0.1 dB/oct（2 節）'],
  ['仮定なしで ESS を 使う', '× 無理', '★ 共通の rho を 仮定している（3 節）'],
  ['★ f(alpha) の 端に 届く', '× 無理', '★ 第 52 回。標本の 対数で 決まる'],
  ['系に 無い慣性領域を 作る', '× 無理', '★ Re が 決める（4 節）'],
];
console.log('  ' + pad('やりたいこと', 30) + pad('判定', 12) + '理由');
for (const c of cannot) console.log('  ' + pad(c[0], 30) + pad(c[1], 12) + c[2]);

// ============================================================
head('7. 本回のまとめ');
// ============================================================
const rows2 = [
  ['★ 貼り合わせの 較正要求', '◎ 数値', '★ 0.3 × delta[dB] / 桁 間隔'],
  ['1 dB / 3 桁 = 0.1 dB/oct', '◎ 数値', '★ 第 42 回の目標と 同じ大きさ'],
  ['★★ ESS は 補正を 打ち消す', '◎ 数値', '★ 4 桁 → 9 桁（全域）に伸びる'],
  ['ただし 仮定を 一つ置く', '◎ 明記', '★ 共通の rho の冪という形'],
  ['慣性領域 = (3/4) log10 Re', '◎ 数値', '実験室 3 桁、大気 9 桁'],
  ['★ 1 桁 増やすには Re を 21.5 倍', '◎ 数値', 'ここでも 対数'],
  ['★★ 装置の数には 線形', '◎ 論理', '★ 第 53 回の 抜け道'],
  ['★ 実データでの検証', '× 未着手', '★ 本稿も 合成データのみ'],
];
console.log('');
for (const r of rows2) console.log('  ' + pad(r[0], 32) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 範囲は 買えます。ただし 時間では 買えません。');
console.log('  ★ 買えるのは ── 装置の数（線形）、仮定（一気に）、対象の選択（Re の対数）。');
console.log('  ★★ 第 53 回の「範囲は log N」は、');
console.log('  ★★ 「同じ系を 同じ装置で 長く測る」場合に限った話でした。');
