// 考える波 第 48 回：階数という軸の 端を探す
//   冪則が成り立たない場所。対数が冪を置き換える場所。
//   node hate.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

// 局所的な階数： alpha(w) = d ln|H| / d ln w
// 指数関数などで H が桁落ちしないよう、ln|H| を直接 与える形にする
function localAlpha(logH, w) {
  const h = 1e-6;
  return (logH(w * (1 + h)) - logH(w * (1 - h))) / Math.log((1 + h) / (1 - h));
}

console.log('考える波 第 48 回 ── 階数という軸の 端を探す');
console.log('第 43 回で予告した「三度目の試練」を、自分で探しに行く');

// ============================================================
head('1. まず、軸がうまく働く場合を確認する');
// ============================================================
{
  console.log('');
  console.log('  局所的な階数 alpha(w) = d ln|H| / d ln w を、いろいろな H で測る');
  console.log('  冪則 H = w^a なら alpha(w) = a で一定のはず');
  console.log('');
  console.log('  ' + pad('w', 12) + padl('H=w^0.5', 14) + padl('H=w^{-5/6}', 16)
    + padl('★ 一定か', 14));
  const p1 = (w) => 0.5 * Math.log(w), p2 = (w) => (-5 / 6) * Math.log(w);
  for (const w of [1e-3, 1e-1, 1, 1e1, 1e3, 1e6]) {
    console.log('  ' + pad(e(w, 0), 12) + padl(f(localAlpha(p1, w), 8), 14)
      + padl(f(localAlpha(p2, w), 8), 16) + padl('★ はい', 14));
  }
  console.log('');
  console.log('  ★ ここでは「階数」は 良い座標です。どの周波数で測っても 同じ値。');
}

// ============================================================
head('2. ★ 端 その 1 ── 局所的な階数が 周波数の関数になる');
// ============================================================
{
  console.log('');
  console.log('  冪則でない H を並べて、alpha(w) がどう振る舞うかを見る');
  console.log('');
  const fns = [
    ['ローレンツ 1/(1+w^2)', (w) => -Math.log(1 + w * w)],
    ['対数 ln(1+1/w)', (w) => Math.log(Math.log(1 + 1 / w))],
    ['指数 e^{-w}', (w) => -w],
    ['伸びた指数 e^{-sqrt(w)}', (w) => -Math.sqrt(w)],
  ];
  console.log('  ' + pad('w', 12) + fns.map(x => padl(x[0].slice(0, 12), 16)).join(''));
  for (const w of [1e-3, 1e-2, 1e-1, 1, 1e1, 1e2, 1e3]) {
    console.log('  ' + pad(e(w, 0), 12)
      + fns.map(x => padl(f(localAlpha(x[1], w), 5), 16)).join(''));
  }
  console.log('');
  console.log('  ★ ローレンツ：0 から -2 へ 連続に動く（両端では 冪則に戻る）');
  console.log('  ★★ 対数：どこまでも 0 に近づくが、決して 0 にならない');
  console.log('  ★★★ 指数：alpha = -w なので 上限が無い ── 階数が 発散する');
  console.log('  ★★★ ＝ 軸に乗らないのではなく、軸の 目盛りを振り切る。');
}

// ============================================================
head('3. どれくらいの範囲なら「冪則」と言ってよいか');
// ============================================================
{
  console.log('');
  console.log('  第 27 回で使った測り方： alpha(w) が ある値の ±0.1 に入る 桁数');
  console.log('');
  function decades(H, target, wlo, whi) {
    const N = 20000; let cnt = 0;
    const l0 = Math.log10(wlo), l1 = Math.log10(whi);
    for (let i = 0; i < N; i++) {
      const w = Math.pow(10, l0 + (l1 - l0) * i / N);
      if (Math.abs(localAlpha(H, w) - target) <= 0.1) cnt++;
    }
    return (l1 - l0) * cnt / N;
  }
  console.log('  ' + pad('H', 28) + pad('目標の階数', 14) + padl('±0.1 に入る 桁数', 20));
  const tests = [
    ['w^0.5', (w) => 0.5 * Math.log(w), 0.5],
    ['ローレンツ（低域側）', (w) => -Math.log(1 + w * w), 0],
    ['ローレンツ（高域側）', (w) => -Math.log(1 + w * w), -2],
    ['対数 ln(1+1/w)', (w) => Math.log(Math.log(1 + 1 / w)), 0],
    ['指数 e^{-w}', (w) => -w, -1],
  ];
  for (const [lab, H, t] of tests) {
    console.log('  ' + pad(lab, 28) + pad(f(t, 2), 14)
      + padl(f(decades(H, t, 1e-6, 1e6), 3) + ' 桁', 20));
  }
  console.log('');
  console.log('  ★ 12 桁 のうち何桁で「冪則」と言えるか、という測り方');
  console.log('  ★★ 指数関数は どの階数でも ほとんど桁を稼げない ── 冪則ではない');
  console.log('  ★★ 対数は 0 の近くに 長く居るが、いつまでも 0 にならない');
}

// ============================================================
head('4. ★ 端 その 2 ── くりこみ群の「限界的」な場合');
// ============================================================
// beta(g) = a g  → g ∝ mu^a （冪）
// beta(g) = -b g^2 → g(mu) = g0/(1 + b g0 ln(mu/mu0)) （対数）
{
  console.log('');
  console.log('  固定点の近くで beta(g) = a g なら g ∝ mu^a ── 階数 a の冪則');
  console.log('  ところが a = 0（限界的）だと 二次の項が効いて');
  console.log('    g(mu) = g0 / (1 + b g0 ln(mu/mu0))   ← ★ 対数。冪則ではない');
  console.log('');
  const g0 = 0.3, b = 1.0;
  const gval = (mu) => g0 / (1 + b * g0 * Math.log(mu));
  const g = (mu) => Math.log(gval(mu));
  console.log('  ' + pad('mu', 14) + padl('g(mu)', 14) + padl('★ 局所的な階数', 18)
    + padl('alpha × ln(mu)', 18));
  for (const mu of [1e1, 1e2, 1e4, 1e8, 1e16, 1e32]) {
    const a = localAlpha(g, mu);
    console.log('  ' + pad(e(mu, 0), 14) + padl(f(gval(mu), 8), 14) + padl(f(a, 8), 18)
      + padl(f(a * Math.log(mu), 6), 18));
  }
  console.log('');
  console.log('  ★★ 局所的な階数は 0 に向かうが、その速さは 1/ln(mu) ── とても遅い');
  console.log('  ★★ 32 桁 走っても まだ -0.0130。「冪則で階数 0」とは言えない。');
  console.log('  ★ alpha × ln(mu) が -1/b = -1 に近づく ── これが 1/ln の形の印');
  console.log('  ★★★ これが「限界的」の正体 ── 階数が 0 なのではなく、0 に 対数的に近づく。');
}

// ============================================================
head('5. ★ 端 その 3 ── 有限サイズ。一つの指数すら 定義できなくなる');
// ============================================================
// 1 次元イジング（周期境界、サイズ L）： <s_0 s_r> = (t^r + t^{L-r})/(1 + t^L)
{
  const K = 1.0, t = Math.tanh(K);
  console.log('');
  console.log('  1 次元イジング（周期境界）： <s_0 s_r> = (t^r + t^{L-r})/(1 + t^L) 、 t = tanh K');
  console.log('  無限鎖なら t^r ── 純粋な指数。有限だと 後半で 折り返す。');
  console.log('');
  const corr = (r, L) => (Math.pow(t, r) + Math.pow(t, L - r)) / (1 + Math.pow(t, L));
  console.log('  ' + pad('r/L', 10) + [8, 16, 32, 64].map(L => padl('L=' + L, 16)).join(''));
  for (const x of [0.1, 0.2, 0.3, 0.4, 0.5]) {
    console.log('  ' + pad(f(x, 2), 10)
      + [8, 16, 32, 64].map(L => padl(e(corr(Math.round(x * L), L), 4), 16)).join(''));
  }
  console.log('');
  console.log('  ★ r/L で揃えても 値は揃わない（指数関数なので 素直には崩れない）');
  console.log('');
  // 局所的な「減衰率」を測る
  console.log('  局所的な減衰率 -d ln<ss>/dr （無限鎖なら -ln t = ' + f(-Math.log(t), 6) + ' 一定）');
  console.log('  ' + pad('r', 10) + [16, 32, 64].map(L => padl('L=' + L, 16)).join('')
    + padl('無限鎖', 14));
  for (const r of [2, 4, 8, 12, 15]) {
    const row = [16, 32, 64].map(L => {
      if (r >= L - 1) return padl('-', 16);
      const a = corr(r - 1, L), b2 = corr(r + 1, L);
      return padl(f(-Math.log(b2 / a) / 2, 6), 16);
    }).join('');
    console.log('  ' + pad(r, 10) + row + padl(f(-Math.log(t), 6), 14));
  }
  console.log('');
  console.log('  ★★ L=16 では r=8 を過ぎると 減衰率が 0 に近づき、やがて 負になる');
  console.log('  ★★ ＝ 有限の系では「一つの指数」も「一つの階数」も 定義できない');
  console.log('  ★ 第 5 回「宇宙年齢より長いものは 定数と区別がつかない」の 空間版');
}

// ============================================================
head('6. 臨界指数を 階数として読む ── そして イプシロン展開の精度');
// ============================================================
{
  console.log('');
  console.log('  d = 4 - eps でのイジング（n=1）：');
  console.log('    nu = 1/2 + (n+2)/(4(n+8)) eps + ... = 1/2 + eps/12 + ...');
  console.log('    eta = (n+2)/(2(n+8)^2) eps^2 + ... = eps^2/54 + ...');
  console.log('');
  console.log('  ' + pad('eps（＝4-d）', 14) + padl('nu（1 次まで）', 16)
    + padl('eta（2 次まで）', 16) + padl('文献の 3 次元値', 18));
  for (const eps of [0.0, 0.25, 0.5, 0.75, 1.0]) {
    const nu = 0.5 + eps / 12, eta = eps * eps / 54;
    const ref = (eps === 1.0) ? 'nu=0.6300, eta=0.0363' : '';
    console.log('  ' + pad(f(eps, 2), 14) + padl(f(nu, 6), 16) + padl(f(eta, 6), 16)
      + padl(ref, 18));
  }
  console.log('');
  console.log('  ★ eps = 1（3 次元）での ずれ：');
  console.log('    nu : ' + f(0.5 + 1 / 12, 4) + ' 対 0.6300 → '
    + f(100 * Math.abs(0.5 + 1 / 12 - 0.63) / 0.63, 1) + ' %');
  console.log('    eta: ' + f(1 / 54, 4) + ' 対 0.0363 → '
    + f(100 * Math.abs(1 / 54 - 0.0363) / 0.0363, 1) + ' %');
  console.log('');
  console.log('  ★★ 「階数が連続に変わる」は d=4 の近くでは 良い近似だが、');
  console.log('  ★★ 3 次元まで来ると 1 次では 7 % ずれる（eta は 49 % ずれる）。');
  console.log('  ★ 第 30 回の alpha=(d-3)/2 は 自由場の話。相互作用があると こうなる。');
}

// ============================================================
head('7. 軸が終わる 三つの形 ── まとめて並べる');
// ============================================================
console.log('');
console.log('  ' + pad('終わり方', 26) + pad('どこで出たか', 20) + '何が起きているか');
const ends = [
  ['① 軸に乗らない量が出る', '第 41 回', '整数（巻き数・チャーン数）'],
  ['② 軸が一本でなくなる', '第 42 回', '階数が分布になる'],
  ['★ ③ 冪則が そもそも無い', '★ 本回', '★ alpha(w) が w の関数になる'],
  ['★ ③a 目盛りを振り切る', '★ 本回 2 節', '★ 指数関数：alpha が発散'],
  ['★ ③b 0 に対数的に近づく', '★ 本回 4 節', '★ 限界的な結合：1/ln(mu)'],
  ['★ ③c 系が有限', '★ 本回 5 節', '★ 折り返して 指数すら定義できない'],
];
for (const x of ends) console.log('  ' + pad(x[0], 26) + pad(x[1], 20) + x[2]);
console.log('');
console.log('  ★★★ 三つとも「軸が間違っている」わけではありません。');
console.log('  ★★★ 「軸が使える条件」が はっきりしただけです ──');
console.log('  ★★★ スケール不変性が、ある桁数にわたって 成り立っていること。');

// ============================================================
head('8. 本回のまとめ');
// ============================================================
const rows = [
  ['冪則なら alpha は一定', '◎ 数値', '第 1 回の軸が働く場合'],
  ['★ 指数関数では alpha が発散', '◎ 数値', '★ alpha = -w 、上限なし'],
  ['ローレンツは 0 → -2 に連続', '◎ 数値', '両端でだけ 冪則に戻る'],
  ['★ 限界的な結合は 1/ln(mu)', '◎ 数値', '★ 32 桁 走っても -0.0130'],
  ['★ 有限サイズで指数も定義不能', '◎ 数値', '★ 1 次元イジングで実演'],
  ['イプシロン展開の精度', '◎ 数値', '★ 3 次元で nu は 7 %、eta は 49 % ずれ'],
  ['★ 軸が終わる三つの形', '◎ 整理', '★ 第 41・42 回 ＋ 本回'],
  ['★ 軸を置き換えるもの', '× 出ない', '★ 本稿では見つからなかった'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 34) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 「階数」という軸は 間違っていませんが、万能でもありません。');
console.log('  ★ 使える条件は ただ一つ ── スケール不変性が 何桁か 続いていること。');
console.log('  ★★ そして物理で冪則がよく出るのは、その条件が よく成り立つからでした。');
