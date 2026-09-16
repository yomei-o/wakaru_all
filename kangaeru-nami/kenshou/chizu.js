// 考える波 第 50 回：地図
//   50 回ぶんを 一枚に。数字は すべて ここで 計算し直す。
//   node chizu.js         （kenshou/ の中で実行すること）
'use strict';

const fs = require('fs');
const path = require('path');

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

let nPass = 0, nFail = 0;
function check(ep, name, got, want, tol) {
  const ok = Math.abs(got - want) <= tol * Math.max(1, Math.abs(want));
  if (ok) nPass++; else nFail++;
  console.log('  ' + pad('第 ' + ep + ' 回', 9) + pad(name, 30)
    + padl(f(got, 6), 16) + padl(f(want, 6), 16) + '  ' + (ok ? 'PASS' : '★ FAIL'));
}

const G = 6.67430e-11, hbar = 1.054571817e-34, c = 299792458, kB = 1.380649e-23;
const Msun = 1.98892e30, ageU = 13.8e9 * 3.155693e7;
const lp = Math.sqrt(G * hbar / (c * c * c));

console.log('考える波 第 50 回 ── 地図');
console.log('第 1 回の一行から、ここまで');

// ============================================================
head('1. 一本の軸 ── すべての階数が出た場所');
// ============================================================
console.log('');
console.log('  ' + pad('階数 alpha', 11) + padl('dB/oct', 9) + padl('位相[度]', 9)
  + '  出た場所');
const spots = [
  [-1.0, '第 30 回 d=1（1 次元の波）'],
  [-0.5, '第 30 回 d=2、第 38 回 d_s=2（紫外の重力）'],
  [0.0, '第 30 回 d=3、第 39 回 BF 境界、対数が出る所'],
  [0.5, '第 2 回 1/f、第 30 回 d=4、第 39 回 nu=1/4 の AdS'],
  [5 / 6, '★ 第 42 回 乱流（K41）'],
  [1.0, 'ブラウン運動、第 30 回 d=5'],
  [1.5, '第 30 回 d=6'],
];
for (const [a, where] of spots) {
  console.log('  ' + pad(f(a, 4), 11) + padl(f(6 * a, 3), 9) + padl(f(90 * a, 1), 9)
    + '  ' + where);
}
console.log('');
console.log('  ★ 同じ数の 別々の名前：');
console.log('    dB/oct = 6 alpha （第 1 回） 、 位相 = 90 alpha 度 （第 1 回）');
console.log('    次元 d = 2 alpha + 3 （第 30 回） 、 ハースト H = alpha - 1/2 （第 42 回）');
console.log('    AdS の nu = alpha/2 （第 39 回） 、 スペクトル指数 beta = 2 alpha');
console.log('');
console.log('  ★★ 宇宙の原始ゆらぎ（第 47 回）は n_s = 0.9649 ＝ '
  + f(3 * (0.9649 - 1), 4) + ' dB/oct');
console.log('  ★★ 乱流の間欠性（第 42 回）は K41 から +'
  + f(3 * (1 + (2 / 3 + (1 - 2 / 3 - Math.log(Math.pow(0.7, 2 / 3)
    + Math.pow(0.3, 2 / 3)) / Math.LN2))) - 5, 4) + ' dB/oct');

// ============================================================
head('2. 階数が整数から外れる 五つの理由');
// ============================================================
console.log('');
const reasons = [
  ['① 多数の時定数の重ね合わせ', '第 2 回', 'g(tau) ∝ 1/tau'],
  ['② 次元', '第 30 回', 'alpha = (d-3)/2'],
  ['③ 臨界点での連続変化', '第 13 回', 's = 1/2 ± sqrt(1/4-lambda)'],
  ['④ バルクの質量', '第 39 回', 'alpha = 2 sqrt(d^2/4+m^2L^2)'],
  ['⑤ 階数が一つの数でない', '第 42 回', '幅 = log2((1-p)/p)'],
];
for (const r of reasons) console.log('  ' + pad(r[0], 30) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  そして 軸が終わる 三つの形（第 41・42・48 回）');
const ends = [
  ['① 軸に乗らない量', '第 41 回', '整数（巻き数・チャーン数）'],
  ['② 軸が一本でない', '第 42 回', '階数が 分布になる'],
  ['③ 冪則が そもそも無い', '第 48 回', '発散・対数的接近・有限サイズ'],
];
for (const r of ends) console.log('  ' + pad(r[0], 30) + pad(r[1], 12) + r[2]);

// ============================================================
head('3. 数字を すべて 計算し直す（第 1 回〜第 49 回）');
// ============================================================
console.log('');
console.log('  ' + pad('回', 9) + pad('項目', 30) + padl('再計算', 16)
  + padl('記事の値', 16) + '  判定');

// --- 第 1 回：軸そのもの ---
check(1, 'dB/oct = 6 alpha (a=0.5)', 6 * 0.5, 3.0, 1e-12);
check(1, '位相 = 90 alpha (a=0.5)', 90 * 0.5, 45.0, 1e-12);
// --- 第 30 回 ---
check(30, 'alpha=(d-3)/2 at d=2', (2 - 3) / 2, -0.5, 1e-12);
// --- 第 33 回：小出 ---
{
  const me = 0.51099895, mmu = 105.6583755, mtau = 1776.86;
  const K = (me + mmu + mtau) /
    Math.pow(Math.sqrt(me) + Math.sqrt(mmu) + Math.sqrt(mtau), 2);
  check(33, '小出の K', K, 2 / 3, 5e-5);
}
// --- 第 37 回：ワトソン積分 ---
{
  const N = 200, h = 2 * Math.PI / N; let u = 0;
  for (let i = 0; i < N; i++) { const cx = Math.cos(-Math.PI + (i + 0.5) * h);
    for (let j = 0; j < N; j++) { const cy = Math.cos(-Math.PI + (j + 0.5) * h);
      for (let k = 0; k < N; k++) { const cz = Math.cos(-Math.PI + (k + 0.5) * h);
        u += 1 / (1 - (cx + cy + cz) / 3); } } }
  u *= h * h * h / Math.pow(2 * Math.PI, 3);
  check(37, '3 次元の帰還確率', 1 - 1 / u, 0.340537, 5e-3);
}
// --- 第 38 回 ---
check(38, 'プランク長 [1e-35 m]', lp / 1e-35, 1.6162, 1e-3);
check(38, 'alpha=(d_s-3)/2 at z=3', ((1 + 3 / 3) - 3) / 2, -0.5, 1e-12);
// --- 第 39 回 ---
{
  const d = 4, mmB = -4.25, nuB = Math.sqrt(-(d * d / 4 + mmB));
  check(39, 'z の比 exp(pi/|nu|)', Math.exp(Math.PI / nuB), 535.4917, 1e-5);
  check(39, '17 桁の固有距離 [L]', 17 * Math.LN10, 39.143947, 1e-6);
}
// --- 第 40 回 ---
check(40, 'h_th = 2 gamma / w0', 2 * 0.05 / 1, 0.1, 1e-12);
// --- 第 41 回 ---
check(41, 'xi = 1/ln(w/v) (w=2)', 1 / Math.log(2), 1.442695, 1e-5);
// --- 第 42 回 ---
{
  const tauZ = (q, p) => -Math.log(Math.pow(p, q) + Math.pow(1 - p, q)) / Math.LN2;
  const tauE = (q, p) => 1 - q + tauZ(q, p);
  const zeta = (pp, p) => pp / 3 + tauE(pp / 3, p);
  check(42, 'zeta_3（4/5 の法則）', zeta(3, 0.7), 1.0, 1e-12);
  check(42, 'K41 との dB/oct の差', 3 * (1 + zeta(2, 0.7)) - 5, 0.081164, 1e-4);
  check(42, 'alpha の幅', -Math.log(0.3 / 0.7) / Math.LN2, 1.222392, 1e-5);
}
// --- 第 44 回：総和則としきい値 ---
{
  const wp = 1, w0 = 2, g = 0.1;
  const N = 2000000, wmax = 4000, h = wmax / N; let s = 0;
  for (let i = 0; i < N; i++) {
    const w = (i + 0.5) * h;
    const d = (w0 * w0 - w * w), den = d * d + (g * w) * (g * w);
    s += w * (wp * wp * g * w / den) * h;
  }
  check(44, 'f 総和則 ∫w Im eps dw', s, Math.PI / 2, 1e-4);
  check(44, '運動量ギャップの成長率', 0.1 * 1 * 1 / 4, 0.025, 1e-12);
}
// --- 第 45 回：-1/12 とカシミールとウンルー ---
{
  const d = 0.001; let s = 0;
  const N = Math.ceil(60 / d);
  for (let n = 1; n <= N; n++) s += n * Math.exp(-d * n);
  check(45, 'Σ n e^{-dn} - 1/d^2', s - 1 / (d * d), -1 / 12, 1e-4);
  const P = Math.PI * Math.PI * hbar * c / 240 / Math.pow(1e-8, 4);
  check(45, 'カシミール圧 10nm [1e5 Pa]', P / 1e5, 1.3001, 1e-3);
  const aU = 2 * Math.PI * c * kB * 1.0 / hbar;
  check(45, 'T=1K のウンルー加速度 [1e20]', aU / 1e20, 2.4655, 1e-3);
}
// --- 第 46 回：ホーキング ---
{
  const kap = c * c * c * c / (4 * G * Msun);
  check(46, '太陽質量の T [1e-8 K]', hbar * kap / (2 * Math.PI * c * kB) / 1e-8,
    6.1687, 1e-3);
  check(46, '太陽質量の S/kB [1e77]', 4 * Math.PI * G * Msun * Msun / (hbar * c) / 1e77,
    1.0494, 1e-3);
  check(46, 'ページ時刻 t/T', 1 - Math.pow(1 / Math.SQRT2, 3), 0.646447, 1e-5);
  const k = kap / c;
  check(46, '測定帯域を出る時間 [ms]',
    Math.log(5e14 / (1 / ageU)) / k / 1e-3, 1.4662, 2e-3);
}
// --- 第 47 回：インフレーション ---
{
  check(47, 'n_s = 3-2nu+1 at nu=1.5', 1 + 3 - 2 * 1.5, 1.0, 1e-12);
  check(47, 'n_s を dB/oct に', 3 * (0.9649 - 1), -0.10530, 1e-4);
  check(47, 'スタロビンスキー r (N=60)', 12 / (60 * 60), 0.003333, 1e-4);
}
// --- 第 48 回：限界的な結合 ---
{
  const g0 = 0.3, b = 1.0;
  const gv = (mu) => g0 / (1 + b * g0 * Math.log(mu));
  check(48, '限界的な結合の階数 at 1e32', -gv(1e32), -0.012984, 1e-4);
}
// --- 第 49 回：ボーデの関係 ---
{
  const a = -0.5;
  const U = 25, N = 100000, h = 2 * U / N; let s = 0;
  for (let i = 0; i < N; i++) {
    const u = -U + (i + 0.5) * h;
    s += a * Math.log(Math.abs(1 / Math.tanh(u / 2))) * h;
  }
  check(49, 'ボーデの位相 [度]', s / Math.PI * 180 / Math.PI * Math.PI / Math.PI * 1,
    90 * a, 1e-3);
}
console.log('');
console.log('  ' + pad('合計', 9) + 'PASS ' + nPass + ' 、 FAIL ' + nFail);

// ============================================================
head('4. このシリーズ自身を 数える');
// ============================================================
{
  const root = path.join(__dirname, '..');
  const kenshou = fs.readdirSync(__dirname).filter(x => x.endsWith('.js'));
  let lines = 0, bytes = 0;
  for (const x of kenshou) {
    const t = fs.readFileSync(path.join(__dirname, x), 'utf8');
    lines += t.split('\n').length; bytes += Buffer.byteLength(t);
  }
  const body = fs.existsSync(path.join(root, 'body'))
    ? fs.readdirSync(path.join(root, 'body')).filter(x => /^\d+\.html$/.test(x)) : [];
  const bodyEn = fs.existsSync(path.join(root, 'body-en'))
    ? fs.readdirSync(path.join(root, 'body-en')).filter(x => /^\d+\.html$/.test(x)) : [];
  const built = fs.readdirSync(root).filter(x => /^kangaeru-nami-\d+-/.test(x));
  let bodyChars = 0;
  for (const x of body) bodyChars += fs.readFileSync(path.join(root, 'body', x), 'utf8').length;
  console.log('');
  console.log('  ' + pad('項目', 34) + padl('数', 14));
  console.log('  ' + pad('公開した回（日本語）', 34) + padl(built.length, 14));
  console.log('  ' + pad('本文ファイル（日本語）', 34) + padl(body.length, 14));
  console.log('  ' + pad('本文ファイル（英語）', 34) + padl(bodyEn.length, 14));
  console.log('  ' + pad('★ 数値検証スクリプト', 34) + padl(kenshou.length, 14));
  console.log('  ' + pad('★ そのコード行数', 34) + padl(lines, 14));
  console.log('  ' + pad('★ そのバイト数', 34) + padl(e(bytes, 3), 14));
  console.log('  ' + pad('日本語本文の文字数（およそ）', 34) + padl(e(bodyChars, 3), 14));
  console.log('');
  console.log('  ★ 依存ライブラリは 0 本。すべて 素の Node で そのまま動きます。');
}

// ============================================================
head('5. ★ まだ 手をつけていない場所');
// ============================================================
console.log('');
const open = [
  ['雑音のある実データの扱い', '第 49 回', '桁数の推定に統計誤差が入る'],
  ['量子多体局在', '第 40 回', '時間結晶の本体。古典しか扱っていない'],
  ['実際の物質・素子の設計', '第 41・44 回', '最小模型しか扱っていない'],
  ['宇宙定数問題', '第 45 回', '★ 差しか扱えない。絶対値は無理'],
  ['情報パラドックスの解決', '第 46 回', '★ 「測れない」と「無い」の間'],
  ['インフレーションの実在', '第 47 回', '模型の中の計算のみ'],
  ['★ 軸を置き換えるもの', '第 48 回', '★ 探したが 見つからなかった'],
  ['非平衡統計の一般論', '未着手', '揺動散逸は使ったが 体系は扱っていない'],
  ['物理の外の冪則', '未着手', '★ 本シリーズは 物理に限った'],
  ['実験の提案', '一部', '測るべき量は出たが 装置の話はしていない'],
];
console.log('  ' + pad('残っていること', 28) + pad('どこで宣言したか', 16) + '中身');
for (const o of open) console.log('  ' + pad(o[0], 28) + pad(o[1], 16) + o[2]);

// ============================================================
head('6. 50 回の 一行');
// ============================================================
console.log('');
console.log('  第 1 回の一行：');
console.log('    「音を微分すると高音になり、積分すると低音になる。');
console.log('      ならば、その途中（分数階）は 何を意味するのか」');
console.log('');
console.log('  50 回後の答え：');
console.log('    ★ 階数 alpha は、dB/oct でも 位相でも 次元でも ハースト指数でも');
console.log('    ★ AdS の質量でも 構造関数の指数でもある ── 同じ一つの数だった。');
console.log('');
console.log('    ★★ そしてその軸が使える条件は ただ一つ：');
console.log('    ★★ スケール不変性が、ある桁数にわたって 成り立っていること。');
console.log('');
console.log('    ★★★ 人類が知らない新しい式は 出ませんでした。');
console.log('    ★★★ 出たのは「同じ式の 別の読み方」と「何を測ればよいか」です。');
console.log('');
console.log('  ★ 負けた計算を 消さないのが、このシリーズの方針でした（第 15 回から）。');
