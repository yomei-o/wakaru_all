// 考える波 第 49 回：手引き ── 測定データを渡されたら、どう読むか
//   これまで 48 回で作った手順を、そのまま プログラムにする
//   node tebiki.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

// ---- 道具 1：局所的な階数（第 48 回） ----
function localAlpha(logA, w) {
  const h = 1e-6;
  return (logA(w * (1 + h)) - logA(w * (1 - h))) / Math.log((1 + h) / (1 - h));
}
// ---- 道具 2：ボーデの 利得位相関係（第 1・8 回） ----
//   phi(w0) = (1/pi) ∫ (dA/du) ln|coth(u/2)| du 、 u = ln(w/w0)
function bodePhase(logA, w0) {
  const U = 25, N = 200000, h = 2 * U / N; let s = 0;
  for (let i = 0; i < N; i++) {
    const u = -U + (i + 0.5) * h;
    if (Math.abs(u) < 1e-9) continue;
    const a = localAlpha(logA, w0 * Math.exp(u));
    s += a * Math.log(Math.abs(1 / Math.tanh(u / 2))) * h;
  }
  return s / Math.PI;           // ラジアン
}
// ---- 道具 3：±0.1 に入る桁数（第 27・48 回） ----
function flatDecades(logA, target, wlo, whi) {
  const N = 4000; let cnt = 0;
  const l0 = Math.log10(wlo), l1 = Math.log10(whi);
  for (let i = 0; i < N; i++) {
    const w = Math.pow(10, l0 + (l1 - l0) * i / N);
    if (Math.abs(localAlpha(logA, w) - target) <= 0.1) cnt++;
  }
  return (l1 - l0) * cnt / N;
}
// ---- 道具 4：「階数の振れ幅が tol 以内」でいちばん長い窓を探す ----
//   目標値を人が決めずに済むよう、窓の中の max-min で判定する
function longestFlat(logA, wlo, whi, tol) {
  const N = 900, l0 = Math.log10(wlo), l1 = Math.log10(whi);
  const ls = [], as = [];
  for (let i = 0; i <= N; i++) {
    const l = l0 + (l1 - l0) * i / N;
    ls.push(l); as.push(localAlpha(logA, Math.pow(10, l)));
  }
  let best = { dec: 0, mean: 0, lo: 0, hi: 0 };
  for (let i = 0; i <= N; i++) {
    let mn = as[i], mx = as[i];
    for (let j = i + 1; j <= N; j++) {
      if (as[j] < mn) mn = as[j];
      if (as[j] > mx) mx = as[j];
      if (mx - mn > tol) break;
      const dec = ls[j] - ls[i];
      if (dec > best.dec) {
        let sum = 0; for (let k = i; k <= j; k++) sum += as[k];
        best = { dec: dec, mean: sum / (j - i + 1),
                 lo: Math.pow(10, ls[i]), hi: Math.pow(10, ls[j]) };
      }
    }
  }
  return best;
}
// ---- 道具 5：曲がっている所（特徴的な周波数）を探す ----
//   階数が 1 桁あたり 0.5 を超えて動いている区間の 中心を拾う
function corners(logA, wlo, whi) {
  const N = 900, l0 = Math.log10(wlo), l1 = Math.log10(whi);
  const dl = (l1 - l0) / N;
  const out = []; let run = null;
  let prev = localAlpha(logA, Math.pow(10, l0));
  for (let i = 1; i <= N; i++) {
    const l = l0 + dl * i;
    const a = localAlpha(logA, Math.pow(10, l));
    const rate = Math.abs(a - prev) / dl;
    if (rate > 0.5) { if (run === null) run = [l, l]; else run[1] = l; }
    else if (run !== null) { out.push(Math.pow(10, (run[0] + run[1]) / 2)); run = null; }
    prev = a;
  }
  if (run !== null) out.push(Math.pow(10, (run[0] + run[1]) / 2));
  return out;
}

console.log('考える波 第 49 回 ── 手引き');
console.log('48 回で作った手順を、そのままプログラムにする');

// ============================================================
head('1. 手引き ── 七つのステップ');
// ============================================================
console.log('');
const steps = [
  ['① 対数対数で描く', '第 1 回', 'まずこれ。線形軸では 何も見えない'],
  ['② 局所的な階数を測る', '第 48 回', 'alpha(w) = d ln|H| / d ln w'],
  ['③ 何桁 一定か 数える', '第 27・48 回', '★ 「冪則か」を 桁数で答える'],
  ['④ 曲がっている所を探す', '第 16 回', '★ 特徴的な周波数（時定数）が居る'],
  ['⑤ 位相も測る', '第 1・8 回', '★ 位相 = 90 alpha 度 か？ ずれたら 余分な遅延'],
  ['⑥ モーメントを変える', '第 42 回', '★ 高次で指数が動けば 分布'],
  ['⑦ 系の大きさと比べる', '第 5・48 回', '★ 観測窓より長いものは 定数と同じ'],
];
console.log('  ' + pad('ステップ', 26) + pad('出どころ', 18) + '何のために');
for (const s of steps) console.log('  ' + pad(s[0], 26) + pad(s[1], 18) + s[2]);
console.log('');
console.log('  ★ ①〜④ は 振幅だけで できる。⑤ が入ると 一気に強くなる。');

// ============================================================
head('2. ステップ ⑤ の道具を 数値で確かめる');
// ============================================================
// 冪則 |H| = w^a なら 位相は a pi/2（最小位相系）
{
  console.log('');
  console.log('  ボーデの 利得位相関係： phi(w0) = (1/pi) ∫ (dA/du) ln|coth(u/2)| du');
  console.log('  冪則なら phi = a pi/2 になるはず（＝ 第 1 回の「位相 = 90 alpha 度」）');
  console.log('');
  console.log('  ' + pad('階数 a', 10) + padl('位相（数値）[度]', 20)
    + padl('90 a [度]', 16) + padl('差', 12));
  for (const a of [-2, -1, -0.5, 0, 0.5, 1]) {
    const logA = (w) => a * Math.log(w);
    const ph = bodePhase(logA, 1) * 180 / Math.PI;
    console.log('  ' + pad(f(a, 2), 10) + padl(f(ph, 6), 20) + padl(f(90 * a, 4), 16)
      + padl(e(Math.abs(ph - 90 * a), 2), 12));
  }
  console.log('');
  console.log('  ★★ 振幅の傾きだけから 位相が出る ── 第 8 回の因果律の実用形');
  console.log('  ★★★ だから「位相が 90 alpha からずれていたら、余分な遅延がある」と言える');
  console.log('  ★ 振幅だけ見ていては 決して分からないことが、位相で分かる。');
}

// ============================================================
head('3. 六つの「未知のデータ」に 手順を当てる');
// ============================================================
// 中身を知らないつもりで ①〜④ を走らせる
const WLO = 1e-4, WHI = 1e4;

// A: 多数の時定数の重ね合わせ（第 2 回の 1/f）
function makeSuper(tlo, thi, n) {
  const ts = [];
  for (let i = 0; i < n; i++) ts.push(Math.pow(10, Math.log10(tlo)
    + (Math.log10(thi) - Math.log10(tlo)) * i / (n - 1)));
  return (w) => {
    let s = 0;
    for (const t of ts) s += t / (1 + w * w * t * t);   // g(tau) ∝ 1/tau の重み
    return 0.5 * Math.log(s);                          // |H| = sqrt(S)
  };
}
// F: 狭い対数正規分布（半桁ぶん）── 冪則に「見える」が 冪則ではない
function makeNarrow(tc, widthDec, n) {
  const ts = [], ws = [];
  for (let i = 0; i < n; i++) {
    const x = -3 + 6 * i / (n - 1);
    const t = tc * Math.pow(10, widthDec * x);
    ts.push(t); ws.push(Math.exp(-x * x / 2));
  }
  return (w) => {
    let s = 0;
    for (let i = 0; i < n; i++) s += ws[i] * ts[i] / (1 + w * w * ts[i] * ts[i]);
    return 0.5 * Math.log(s);
  };
}

const data = [
  ['A  重ね合わせ（広い）', makeSuper(1e-4, 1e4, 4000)],
  ['B  単一ローレンツ', (w) => -0.5 * Math.log(1 + w * w)],
  ['C  冪則 w^{-5/6}', (w) => (-5 / 6) * Math.log(w)],
  ['D  指数 e^{-w}', (w) => -w],
  ['E  冪則＋高域の切断', (w) => -0.5 * Math.log(w) - Math.pow(w / 100, 2)],
  ['F  狭い分布（0.5 桁）', makeNarrow(1, 0.5, 2001)],
];
console.log('');
console.log('  ステップ ②〜④ を 機械的に回す（「階数の振れ幅 0.1 以内」で最長の窓）');
console.log('');
console.log('  ' + pad('データ', 24) + padl('★ 平均の階数', 16)
  + padl('★ 続く桁数', 14) + padl('その範囲', 22) + padl('曲がり', 10));
const diag = [];
for (const [lab, logA] of data) {
  const b = longestFlat(logA, WLO, WHI, 0.1);
  const c = corners(logA, WLO, WHI);
  diag.push({ lab: lab, logA: logA, b: b, c: c });
  console.log('  ' + pad(lab, 24) + padl(f(b.mean, 4), 16)
    + padl(f(b.dec, 2) + ' 桁', 14)
    + padl(e(b.lo, 1) + ' 〜 ' + e(b.hi, 1), 22) + padl(c.length, 10));
}
console.log('');
console.log('  ★ 「最長の平坦な窓」は 低域の平らな部分を拾うことがあります（D, F）。');
console.log('  ★ それも正しい読みです ── e^{-w} は 低域では たしかに 定数。');
console.log('  ★★ 大事なのは「知りたい階数のところで 何桁 続くか」を 別に測ること。');

// ============================================================
head('4. ★ 山場 ── A と F を 見分ける');
// ============================================================
{
  console.log('');
  console.log('  A（広い重ね合わせ）と F（狭い分布）は、どちらも 途中で 1/f 風に見える。');
  console.log('  |H| の階数で言えば 1/f は -0.5（パワーが -1）。そこで何桁 続くかを測る。');
  console.log('');
  console.log('  ' + pad('データ', 26) + padl('★ 階数 -0.5 が ±0.1 で続く桁数', 32));
  for (const d of diag) {
    if (!d.lab.startsWith('A') && !d.lab.startsWith('F')) continue;
    console.log('  ' + pad(d.lab, 26) + padl(f(flatDecades(d.logA, -0.5, WLO, WHI), 3) + ' 桁', 32));
  }
  console.log('');
  const dF = diag.find(x => x.lab.startsWith('F'));
  console.log('  F の 局所的な階数（詳しく）');
  console.log('  ' + pad('w', 12) + padl('alpha(w)', 14));
  for (const w of [1e-2, 1e-1, 0.3, 1, 3, 1e1, 1e2]) {
    console.log('  ' + pad(e(w, 0), 12) + padl(f(localAlpha(dF.logA, w), 5), 14));
  }
  console.log('');
  console.log('  ★★★ F は -0.5 の近くを 素通りするだけで、平坦な区間を持ちません。');
  console.log('  ★★★ ステップ ③（桁数を数える）が 無ければ、F を 1/f と 誤判定します。');
  console.log('  ★★ A は 6 桁 以上 続く ── ここで初めて「単一の時定数では無理」と言える。');
}

// ============================================================
head('4b. 判定を 書く ── 言ってよいことの範囲');
// ============================================================
console.log('');
console.log('  ' + pad('データ', 24) + pad('判定', 28) + '言ってよいこと');
const verdicts = {
  'A  重ね合わせ（広い）': ['★ 冪則 -0.5 が 6 桁 以上', '機構を絞れる：単一の時定数では無理'],
  'B  単一ローレンツ': ['冪則 2 本＋曲がり 1 つ', '特徴的な周波数が 1 つ ある'],
  'C  冪則 w^{-5/6}': ['★ 冪則（窓の全域）', '窓の中に 特徴的な長さが 無い'],
  'D  指数 e^{-w}': ['低域は定数、以後 冪則でない', '★ 階数でなく 時定数で要約すべき'],
  'E  冪則＋高域の切断': ['冪則＋切断 1 つ', '切断の位置が 物理を語る'],
  'F  狭い分布（0.5 桁）': ['★ 判定保留（桁が足りない）', '★ 1/f と 言ってはいけない'],
};
for (const d of diag) {
  const v = verdicts[d.lab];
  console.log('  ' + pad(d.lab, 24) + pad(v[0], 28) + v[1]);
}

// ============================================================
head('5. ステップ ⑤ で さらに分かること ── 余分な遅延を見破る');
// ============================================================
{
  console.log('');
  console.log('  同じ振幅でも、位相が違えば 中身が違う。');
  console.log('  |H| = w^{-0.5}（階数 -0.5）に、遅延 e^{-i w T} を足した場合：');
  console.log('');
  console.log('  ' + pad('w', 12) + padl('ボーデの予言 [度]', 20)
    + padl('遅延 T=0.1 の実際 [度]', 24) + padl('差 = -w T [度]', 18));
  const logA = (w) => -0.5 * Math.log(w);
  const pred = bodePhase(logA, 1) * 180 / Math.PI;
  for (const w of [0.1, 0.3, 1, 3, 10]) {
    const p = bodePhase(logA, w) * 180 / Math.PI;
    const extra = -w * 0.1 * 180 / Math.PI;
    console.log('  ' + pad(f(w, 2), 12) + padl(f(p, 4), 20)
      + padl(f(p + extra, 4), 24) + padl(f(extra, 4), 18));
  }
  console.log('');
  console.log('  ★★ 振幅は まったく同じ。位相だけが w に比例して ずれる。');
  console.log('  ★★ ＝ 「振幅から予言した位相」との差が、そのまま 遅延時間になる。');
  console.log('  ★ 第 8 回（クラマース＝クローニッヒ）の いちばん実用的な使い方です。');
}

// ============================================================
head('6. やってはいけないこと ── 48 回で見た失敗から');
// ============================================================
console.log('');
const nos = [
  ['1 桁 の冪則を「冪則」と呼ぶ', '第 48 回', '指数関数でも 0.087 桁は稼げる'],
  ['一つの指数が合ったら満足する', '第 42・47 回', '★ K41 も phi^2 も それで通ってしまう'],
  ['鈍感な量で 理論を検証する', '第 42 回', '★ 間欠性は dB/oct を 0.081 しか動かさない'],
  ['観測窓より長い周期を語る', '第 5 回', '定数と 区別がつかない'],
  ['座標に依る量を 物理だと思う', '第 45 回', '★ 粒子数は 基底の取り方に依る'],
  ['整理を 発見と呼ぶ', '第 43 回', '★ 本シリーズがいちばん気をつけた点'],
];
console.log('  ' + pad('やってはいけない', 30) + pad('出どころ', 16) + '理由');
for (const n of nos) console.log('  ' + pad(n[0], 30) + pad(n[1], 16) + n[2]);

// ============================================================
head('7. 本回のまとめ');
// ============================================================
const rows = [
  ['七つのステップ', '◎ 整理', '48 回ぶんの手順を 一枚に'],
  ['★ ボーデの関係を数値で確認', '◎ 数値', '★ 位相 = 90 alpha を 0.01 度 以内で'],
  ['六つのデータを自動で判定', '◎ 数値', '★ 平坦な階数と桁数を 自動で探す'],
  ['★ 手引きが救った例（F）', '◎ 数値', '★ A は 6 桁 以上、F は 桁が足りない'],
  ['★ 位相で遅延を見破る', '◎ 数値', '★ 振幅だけでは 絶対に分からない'],
  ['やってはいけないこと 6 つ', '◎ 整理', '過去の失敗から'],
  ['★ 機構を一つに決めること', '× できない', '★ 手引きは 候補を絞るだけ'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 34) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 「傾きを測る」だけでは 足りません。');
console.log('  ★ 「何桁 続くか」と「位相はどうか」を 必ず一緒に見ること ──');
console.log('  ★ この二つが、48 回で いちばん役に立った道具でした。');
