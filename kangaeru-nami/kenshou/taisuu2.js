// 考える波 第 53 回：なぜ「測れる範囲」は いつも 対数で効くのか
//   桁数・e 倍の回数・q* ── 三つとも 対数だった。同じ根から来ているのか。
//   node taisuu2.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

console.log('考える波 第 53 回 ── なぜ「測れる範囲」は いつも 対数で効くのか');
console.log('第 51・52 回で、上限が どちらも「データの対数」だった');

// ============================================================
head('1. このシリーズに出てきた「対数」を 並べる');
// ============================================================
console.log('');
console.log('  ' + pad('出た所', 24) + pad('量', 26) + '中身');
const logs = [
  ['第 5 回', '宇宙年齢との比', 'ln(T_universe / T_signal)'],
  ['第 20 回', 'c·t=一定 の座標', '位相が ln t に比例'],
  ['第 21 回', '情報量', 'log2(状態の数)'],
  ['第 22 回', 'ウェーブレット平面', 'ln omega の軸で 等分解能'],
  ['第 39 回', 'AdS の 固有距離', '|ln(z2/z1)|'],
  ['第 45 回', 'リンドラー時間', 'a t = e^{a eta}'],
  ['第 46 回', '測定帯域を出るまで', 'e 倍 74.5 回'],
  ['第 47 回', '地平線問題', 'e 倍 63.6 回'],
  ['★ 第 51 回', '冪則の 桁数', 'log10(f_hi/f_lo)'],
  ['★ 第 52 回', '到達できる q*', 'log2(箱の数) に比例'],
];
for (const l of logs) console.log('  ' + pad(l[0], 24) + pad(l[1], 26) + l[2]);
console.log('');
console.log('  ★ 10 か所。偶然にしては 多すぎます。');

// ============================================================
head('2. 掛け算に対して 不変な測度は dx/x だけ');
// ============================================================
// ∫_a^b w(x) dx が x -> lambda x で不変か 数値で確かめる
{
  function integ(w, a, b, N) {
    const h = (b - a) / N; let s = 0;
    for (let i = 0; i < N; i++) s += w(a + (i + 0.5) * h) * h;
    return s;
  }
  console.log('');
  console.log('  区間 [a, b] を [lambda a, lambda b] に 伸ばしたとき、');
  console.log('  ∫ w(x) dx が 変わらない w は どれか');
  console.log('');
  const ws = [['w = 1', (x) => 1], ['★ w = 1/x', (x) => 1 / x], ['w = 1/x^2', (x) => 1 / (x * x)]];
  console.log('  ' + pad('lambda', 12) + ws.map(x => padl(x[0], 18)).join(''));
  for (const lam of [1, 2, 10, 100]) {
    console.log('  ' + pad(f(lam, 0), 12)
      + ws.map(x => padl(f(integ(x[1], lam * 1, lam * 3, 400000), 8), 18)).join(''));
  }
  console.log('');
  console.log('  ★★★ 1/x だけが 変わりません（いつでも ln 3 = ' + f(Math.log(3), 6) + '）。');
  console.log('  ★★ これが「掛け算の群（スケール変換）の 不変測度」です。');
  console.log('  ★ 不変測度が dx/x なら、自然な座標は ∫dx/x = ln x ── だから 対数。');
}

// ============================================================
head('3. 相対分解能が一定なら、区別できる目盛りの数は 対数');
// ============================================================
// 第 22 回の 定 Q 分析：Delta f / f = 一定
{
  console.log('');
  console.log('  Delta f / f = 1/Q が一定なら、f_lo から f_hi までに 入る目盛りの数は');
  console.log('    N = ln(f_hi/f_lo) / ln(1 + 1/Q)');
  console.log('');
  console.log('  ' + pad('Q', 10) + pad('意味', 26)
    + [2, 3, 6, 12].map(d => padl(d + ' 桁', 12)).join(''));
  for (const [Q, lab] of [[1, '1 オクターブごと'], [16.8, '★ 半音（第 22 回）'],
                          [100, '1 % 分解能'], [1000, '0.1 % 分解能']]) {
    const row = [2, 3, 6, 12].map(d =>
      padl(f(d * Math.LN10 / Math.log(1 + 1 / Q), 1), 12)).join('');
    console.log('  ' + pad(f(Q, 1), 10) + pad(lab, 26) + row);
  }
  console.log('');
  console.log('  ★★ 「区別できる目盛りの数」が 桁数に 比例します。');
  console.log('  ★★★ だから「何桁」が、そのまま「いくつ区別できたか」になる。');
  console.log('  ★ 第 51 回の 桁数も、第 52 回の q* も、この数え方の上に乗っていました。');
}

// ============================================================
head('4. ★★ 全部 同じ関数方程式から 来ている');
// ============================================================
// f(xy) = f(x) + f(y) の 連続解は c ln x だけ（コーシー）
{
  console.log('');
  console.log('  「掛け算を 足し算にする」関数 f：  f(x y) = f(x) + f(y)');
  console.log('  連続な解は  f(x) = c ln x  だけ（コーシーの関数方程式）。');
  console.log('');
  console.log('  数値で確かめる： f(2)=a, f(3)=b と置くと、2^p ≈ 3^q のとき');
  console.log('  p a ≈ q b でなければ 連続にならない → b/a = p/q → ln3/ln2');
  console.log('');
  console.log('  ' + pad('p', 8) + padl('q', 8) + padl('2^p / 3^q', 16)
    + padl('p/q', 14) + padl('ln3/ln2', 14) + padl('差', 12));
  // 2^p ≈ 3^q となる p, q を 連分数で探す
  const target = Math.log(3) / Math.log(2);
  let bestErr = 1e9;
  for (const q of [1, 2, 5, 12, 29, 41, 53, 306, 665]) {
    const p = Math.round(q * target);
    const ratio = Math.exp(p * Math.LN2 - q * Math.log(3));  // 桁あふれを避ける
    console.log('  ' + pad(p, 8) + padl(q, 8) + padl(f(ratio, 6), 16)
      + padl(f(p / q, 8), 14) + padl(f(target, 8), 14)
      + padl(e(Math.abs(p / q - target), 2), 12));
  }
  console.log('');
  console.log('  ★★★ 良い近似ほど p/q が ln3/ln2 に近づく ── 他の解はありません。');
  console.log('  ★★ つまり「掛け算を足し算にしたい」と決めた瞬間に、対数が 一意に決まる。');
  console.log('');
  console.log('  ★ 第 28 回で「指数関数が出る源のひとつは 足し算が掛け算になること」と');
  console.log('  ★ 整理しました。本回は その 裏返しです ──');
  console.log('  ★★★ 掛け算を 足し算に戻すと 対数。だから「数える」と 必ず 対数が出る。');
}

// ============================================================
head('5. それぞれの「対数」を この観点で 読み直す');
// ============================================================
console.log('');
console.log('  ' + pad('出た所', 20) + pad('何が 掛け算か', 26) + '何を 足したいか');
const reread = [
  ['第 5 回', '時間スケールの比', '「何桁 離れているか」'],
  ['第 21 回', '独立な系を 並べる', '★ 情報量（加法的にしたい）'],
  ['第 22 回', '周波数を 定 Q で刻む', '目盛りの数'],
  ['第 39 回', '動径方向の スケール変換', '固有距離（足し算になる）'],
  ['第 45 回', '加速で 時間が 伸び縮み', '固有時（足し算）'],
  ['★ 第 51 回', '周波数の比', '★ 冪則の 桁数'],
  ['★ 第 52 回', '箱の数が 2 倍 ずつ', '★ 到達できる q*'],
];
for (const r of reread) console.log('  ' + pad(r[0], 20) + pad(r[1], 26) + r[2]);
console.log('');
console.log('  ★★ どれも「掛け算で増えるものを、足し算で数えたい」という形でした。');
console.log('  ★ 情報量（第 21 回）だけは 少し違って見えますが ──');
console.log('  ★ 「独立な系を並べると 状態数は掛け算、情報量は足し算」なので 同じ形です。');

// ============================================================
head('6. ★ 第 52 回の q* は 本当に log N か ── 素朴な判定と比べる');
// ============================================================
{
  const P = 0.7;
  const tau = (q) => -Math.log(Math.pow(P, q) + Math.pow(1 - P, q)) / Math.LN2;
  const dtau = (q) => { const h = 1e-6; return (tau(q + h) - tau(q - h)) / (2 * h); };
  const fa = (q) => q * dtau(q) - tau(q);
  // 素朴な判定：f(alpha(q)) >= 0 なら 標本に 入るはず
  let qf = 0;
  for (let q = 0.1; q < 40; q += 0.01) { if (fa(q) < 0) break; qf = q; }
  console.log('');
  console.log('  素朴な判定：その q を支配する alpha の集合が 空でない（f(alpha) >= 0）なら');
  console.log('  標本に 入るはず。その上限は  q = ' + f(qf, 2));
  console.log('');
  console.log('  ' + pad('q', 8) + padl('f(alpha(q))', 16) + padl('第 52 回の実測 q*', 20));
  for (const q of [2, 4, 6, 8, 9, 10]) {
    console.log('  ' + pad(f(q, 1), 8) + padl(f(fa(q), 8), 16)
      + padl(q === 4 ? '★ ここまでしか 届かなかった' : '', 20));
  }
  console.log('');
  console.log('  ★★★ 素朴な判定は q ≈ ' + f(qf, 1) + ' まで許しますが、');
  console.log('  ★★★ 実測（第 52 回）は q* ≈ 4 ── 6 倍 以上 甘い。');
  console.log('  ★★ 理由：f(alpha) >= 0 は「平均すれば 1 個は入る」という条件で、');
  console.log('  ★★ 実際には その 1 個の ゆらぎが 傾きを 壊すからです。');
  console.log('  ★ 第 52 回の 実測のほうを 使うべきです（素朴な判定は 楽観的すぎる）。');
}

// ============================================================
head('7. ★★ 対数にならないもの ── 精度は 冪');
// ============================================================
{
  console.log('');
  console.log('  ここまで 対数だったのは すべて「どこまで 広く」でした。');
  console.log('  では「どこまで 細かく」は どうか ── 第 51 回の答えは 1/sqrt(M)。');
  console.log('');
  console.log('  ' + pad('問い', 30) + pad('N への依存', 20) + '出た回');
  const two = [
    ['どこまで 広い範囲を 見られるか', '★ log N', '第 51・52 回'],
    ['どこまで 精密に 測れるか', '★ N^{-1/2}', '第 51 回'],
    ['いくつ 目盛りを 区別できるか', 'log N', '第 22 回・本回 3 節'],
    ['雑音を どこまで 減らせるか', 'N^{-1/2}', '第 51 回 1 節'],
    ['どこまで 深い極値に 届くか', 'log N', '第 52 回'],
  ];
  for (const t of two) console.log('  ' + pad(t[0], 30) + pad(t[1], 20) + t[2]);
  console.log('');
  console.log('  ' + pad('データを 100 倍 にすると', 30) + padl('範囲', 14) + padl('精度', 14));
  for (const N of [100, 1e4, 1e6, 1e8]) {
    console.log('  ' + pad('N = ' + e(N, 0), 30)
      + padl('×' + f(Math.log(N) / Math.log(100), 2), 14)
      + padl('×' + f(Math.sqrt(N / 100), 1), 14));
  }
  console.log('');
  console.log('  ★★★ データを 100 万倍 にしても、範囲は 3 倍 にしかなりません。');
  console.log('  ★★★ 一方 精度は 1000 倍 よくなります。');
  console.log('  ★★ 「細かく測る」は 努力で届き、「広く測る」は ほとんど届かない ──');
  console.log('  ★★ これが 第 51・52 回で 出会った壁の 正体でした。');
}

// ============================================================
head('8. 本回のまとめ');
// ============================================================
const rows = [
  ['シリーズ中の 対数は 10 か所', '◎ 整理', '偶然にしては 多い'],
  ['★ 掛け算の不変測度は dx/x', '◎ 数値', '★ 1/x だけが スケール不変'],
  ['相対分解能一定 → 目盛りは 対数', '◎ 数値', '第 22 回の 定 Q'],
  ['★★ 根は f(xy)=f(x)+f(y)', '◎ 数値', '★ 連続解は c ln x だけ'],
  ['第 28 回の裏返し', '◎ 対応', '足し算↔掛け算'],
  ['★ 素朴な q* の判定は 甘い', '◎ 数値', '★ f>=0 は q≈26、実測は 4'],
  ['★★ 範囲は log N、精度は N^{-1/2}', '◎ 数値', '★ 100 万倍 で 範囲 3 倍、精度 1000 倍'],
  ['★ なぜ物理が スケール不変なのか', '× 扱えない', '★ 本稿は 結果から 遡っただけ'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 34) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 「測れる範囲が 対数で効く」のは、');
console.log('  ★ 掛け算で増えるものを 足し算で数えようとしているから ──');
console.log('  ★ そして そう数えられる関数は、対数 ただ一つ でした。');
console.log('');
console.log('  ★★★ だから 第 51 回の「桁数」と 第 52 回の「q*」は');
console.log('  ★★★ 別々の問題ではなく、同じ壁の 二つの顔でした。');
