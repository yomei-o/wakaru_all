// 考える波 第 46 回：地平線を波として見る
//   ホーキング温度は ウンルーと同じ式。情報は 消えたのではなく 赤方偏移した。
//   node bh.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

const G = 6.67430e-11, hbar = 1.054571817e-34, c = 299792458, kB = 1.380649e-23;
const Msun = 1.98892e30, Mearth = 5.9722e24;
const yr = 3.155693e7, ageU = 13.8e9 * yr;
const lp = Math.sqrt(G * hbar / (c * c * c));

console.log('考える波 第 46 回 ── 地平線を波として見る');
console.log('情報は 消えたのではなく、測れない所まで 赤方偏移した');

// ============================================================
head('1. ホーキング温度は、第 45 回のウンルーと 同じ式');
// ============================================================
// 表面重力 kappa = c^4/(4GM) 、 T = hbar kappa / (2 pi c kB)
function rs(M) { return 2 * G * M / (c * c); }
function kappa(M) { return c * c * c * c / (4 * G * M); }      // [m/s^2]
function Thawk(M) { return hbar * kappa(M) / (2 * Math.PI * c * kB); }
console.log('');
console.log('  第 45 回： T = hbar a / (2 pi c kB)');
console.log('  本回　 ： T = hbar kappa / (2 pi c kB) 、 kappa = c^4/(4GM)');
console.log('  ★ a を kappa（表面重力）に置き換えただけ');
console.log('');
console.log('  ' + pad('質量', 22) + padl('r_s [m]', 16) + padl('kappa [m/s^2]', 16)
  + padl('★ T [K]', 16));
for (const [M, lab] of [[Msun, '太陽質量'], [1e6 * Msun, '10^6 太陽質量'],
                        [Mearth, '地球質量'], [1e12, '10^12 kg'],
                        [1e8, '10^8 kg']]) {
  console.log('  ' + pad(lab, 22) + padl(e(rs(M), 4), 16) + padl(e(kappa(M), 4), 16)
    + padl(e(Thawk(M), 4), 16));
}
// 宇宙背景放射と同じ温度になる質量
{
  const Tcmb = 2.72548;
  const M = hbar * c * c * c / (8 * Math.PI * G * Tcmb * kB);
  console.log('');
  console.log('  ★ T = 2.725 K（宇宙背景放射）と釣り合う質量 = ' + e(M, 4) + ' kg'
    + '（月の ' + e(M / 7.342e22, 3) + ' 倍）');
  console.log('  ★ これより軽ければ 蒸発、重ければ 背景放射を吸って 成長する');
}

// ============================================================
head('2. エントロピー ── 面積で数える（第 39 回のホログラフィー）');
// ============================================================
function Sbh(M) { return 4 * Math.PI * G * M * M / (hbar * c); }   // S/kB
console.log('');
console.log('  S/kB = A c^3/(4 G hbar) = 4 pi G M^2/(hbar c) = A/(4 l_p^2)');
console.log('  プランク長 l_p = ' + e(lp, 4) + ' m');
console.log('');
console.log('  ' + pad('質量', 22) + padl('面積 A [m^2]', 16) + padl('A/(4 l_p^2)', 16)
  + padl('4 pi G M^2/(hbar c)', 20));
for (const [M, lab] of [[Msun, '太陽質量'], [Mearth, '地球質量'], [1e12, '10^12 kg']]) {
  const A = 4 * Math.PI * rs(M) * rs(M);
  console.log('  ' + pad(lab, 22) + padl(e(A, 4), 16) + padl(e(A / (4 * lp * lp), 4), 16)
    + padl(e(Sbh(M), 4), 20));
}
console.log('');
console.log('  ★ 二通りの数え方が一致 ── 「面積 ÷ プランク面積」がそのまま自由度の数');
console.log('  ★★ 第 39 回の (L/eps)^{d-1} と同じ数え方。地平線が その eps を決めている');
// 太陽の熱的エントロピーと比べる
{
  const Ssun = 1e58;   // 文献値のおよそ（太陽の熱的エントロピー / kB）
  console.log('');
  console.log('  ' + pad('太陽（ふつうの星）の熱的 S/kB', 34) + padl('~ ' + e(Ssun, 1), 14)
    + '  （文献値のおよそ）');
  console.log('  ' + pad('★ 太陽質量のブラックホールの S/kB', 34)
    + padl(e(Sbh(Msun), 4), 14) + '  ★ ' + e(Sbh(Msun) / Ssun, 2) + ' 倍');
  console.log('');
  console.log('  ★★ 同じ質量でも、ブラックホールにすると エントロピーが 19 桁 増える');
  console.log('  ★★ 「重力が最も乱雑な配置」── これが第 21 回の情報の話に効いてくる');
}

// ============================================================
head('3. 蒸発 ── 熱容量が負なので、終わりが加速する');
// ============================================================
// dM/dt = - K / M^2 、 t_evap = 5120 pi G^2 M^3/(hbar c^4)
function tevap(M) { return 5120 * Math.PI * G * G * M * M * M / (hbar * c * c * c * c); }
console.log('');
console.log('  dT/dM < 0 ── 軽くなるほど 熱くなる ＝ 熱容量が負');
console.log('  t_evap = 5120 pi G^2 M^3 / (hbar c^4)');
console.log('');
console.log('  ' + pad('質量', 22) + padl('t_evap [s]', 16) + padl('[年]', 16)
  + padl('宇宙年齢との比', 18));
for (const [M, lab] of [[Msun, '太陽質量'], [Mearth, '地球質量'],
                        [1e12, '10^12 kg'], [1e11, '10^11 kg'], [1e8, '10^8 kg']]) {
  const t = tevap(M);
  console.log('  ' + pad(lab, 22) + padl(e(t, 4), 16) + padl(e(t / yr, 4), 16)
    + padl(e(t / ageU, 3), 18));
}
// 宇宙年齢で ちょうど蒸発しきる質量
{
  const M = Math.pow(ageU * hbar * c * c * c * c / (5120 * Math.PI * G * G), 1 / 3);
  console.log('');
  console.log('  ★ 宇宙年齢で ちょうど蒸発しきる質量 = ' + e(M, 4) + ' kg');
  console.log('    （そのときの r_s = ' + e(rs(M), 3) + ' m 、 T = ' + e(Thawk(M), 3) + ' K）');
  console.log('  ★ 宇宙初期にこの質量のものができていれば、いま 最後の閃光が見えるはず');
}
// 終わりの加速
{
  const M0 = 1e12;
  const T0 = tevap(M0);
  console.log('');
  console.log('  終わりの加速（M0 = 10^12 kg、全寿命 ' + e(T0 / yr, 3) + ' 年）');
  console.log('  ' + pad('残り時間', 16) + padl('残る質量 [kg]', 18) + padl('T [K]', 16)
    + padl('r_s [m]', 14));
  for (const left of [T0 / 2, 1e7, 1, 1e-3]) {
    // M(t) = M0 (1 - t/T0)^{1/3} 、 残り時間 left なら M = M0 (left/T0)^{1/3}
    const M = M0 * Math.pow(left / T0, 1 / 3);
    console.log('  ' + pad(e(left, 2) + ' s', 16) + padl(e(M, 4), 18)
      + padl(e(Thawk(M), 4), 16) + padl(e(rs(M), 3), 14));
  }
  console.log('');
  console.log('  ★ 最後の 1 秒で ' + e(M0 * Math.pow(1 / T0, 1 / 3) * c * c, 3)
    + ' J ── 広島型原爆 ' + e(M0 * Math.pow(1 / T0, 1 / 3) * c * c / 6.3e13, 2) + ' 個ぶん');
  console.log('  ★★ 熱容量が負だから、放っておくと 必ず暴走して終わる');
}

// ============================================================
head('4. ページ曲線 ── 上がってから 下がる');
// ============================================================
// 粗視化：放射のエントロピーは min( 出したぶん , 残っているぶん )
{
  console.log('');
  console.log('  放射のもつれエントロピーの模型（ページ）：');
  console.log('    S_rad = min( S_BH(M0) - S_BH(M) ,  S_BH(M) )');
  console.log('  S_BH ∝ M^2 、 M(t) = M0 (1 - t/T)^{1/3}');
  console.log('');
  console.log('  ' + pad('t / T', 10) + padl('M/M0', 12) + padl('出したぶん', 16)
    + padl('残っているぶん', 18) + padl('★ S_rad', 14) + '  ');
  const S0 = 1;
  for (const x of [0, 0.1, 0.3, 0.5, 0.6464, 0.8, 0.95, 1.0]) {
    const m = Math.pow(1 - x, 1 / 3);
    const out = S0 * (1 - m * m), rem = S0 * m * m;
    const srad = Math.min(out, rem);
    const mark = Math.abs(x - 0.6464) < 1e-4 ? '  ★ ページ時刻' : '';
    console.log('  ' + pad(f(x, 4), 10) + padl(f(m, 6), 12) + padl(f(out, 6), 16)
      + padl(f(rem, 6), 18) + padl(f(srad, 6), 14) + mark);
  }
  // ページ時刻を解析で
  const mPage = 1 / Math.SQRT2;
  const xPage = 1 - Math.pow(mPage, 3);
  console.log('');
  console.log('  ★ ページ時刻： S_BH(M) = S_BH(M0)/2 、つまり M = M0/sqrt(2) = '
    + f(mPage, 6) + ' M0');
  console.log('  ★ 時刻にすると t/T = 1 - 2^{-3/2} = ' + f(xPage, 6)
    + ' ── 寿命の 64.6 %');
  console.log('  ★★ そこまでは上がり、そこから下がる。最後に 0 に戻れば 情報は出ている。');
}

// ============================================================
head('5. ★ 情報は どこへ行ったか ── 赤方偏移の話として読む');
// ============================================================
// 地平線の近くの外向きモードは omega(t) = omega0 e^{-kappa t / c}
// （kappa/c が 1/秒 の次元になる）
{
  console.log('');
  console.log('  第 45 回： 加速する観測者の時間は 対数になる（a t = e^{a eta}）');
  console.log('  同じ形が 地平線の近くでも出る：外向きモードの周波数は');
  console.log('    omega(t) = omega0 exp( - (kappa/c) t )   ← ★ 指数的に 赤くなる');
  console.log('');
  console.log('  ' + pad('質量', 20) + padl('kappa/c [1/s]', 16)
    + padl('e 倍 の時間 [s]', 18) + padl('★ 74 回 分 [s]', 18));
  for (const [M, lab] of [[Msun, '太陽質量'], [1e6 * Msun, '10^6 太陽質量'],
                          [Mearth, '地球質量'], [1e12, '10^12 kg']]) {
    const k = kappa(M) / c;
    console.log('  ' + pad(lab, 20) + padl(e(k, 4), 16) + padl(e(1 / k, 4), 18)
      + padl(e(74.4 / k, 4), 18));
  }
  const wOpt = 5e14, wAge = 1 / ageU;
  console.log('');
  console.log('  可視光 ' + e(wOpt, 1) + ' Hz から、宇宙年齢の逆数 ' + e(wAge, 2)
    + ' Hz まで下がるのに必要な e 倍の回数 = ' + f(Math.log(wOpt / wAge), 1));
  const k = kappa(Msun) / c;
  console.log('  ★★★ 太陽質量なら ' + e(Math.log(wOpt / wAge) / k, 3) + ' 秒');
  console.log('');
  console.log('  ★★★ つまり 1.5 ミリ秒 で、可視光の情報は');
  console.log('  ★★★ 「宇宙年齢かけても 1 周期 観測できない」周波数まで 落ちる。');
  console.log('  ★ 第 5 回：「宇宙年齢より長い周期は 定数と区別がつかない」');
  console.log('  ★ 情報は 消えたのではなく、測れない帯域へ 移された。');
}

// ============================================================
head('6. 「毛が三本」を、フィルタとして読む');
// ============================================================
console.log('');
console.log('  外から見えるのは 質量・電荷・角運動量 の 三つだけ（無毛定理）。');
console.log('');
console.log('  ' + pad('落ちる前', 30) + pad('落ちた後', 22) + '波の言葉');
const rows = [
  ['本 1 冊（10^7 ビット）', '質量が増えただけ', '★ 極端な低域通過'],
  ['同じ質量の石', '区別がつかない', '★ 出力が同じ'],
  ['電荷を持つもの', '電荷も増える', '通る成分は 3 つ'],
];
for (const r of rows) console.log('  ' + pad(r[0], 30) + pad(r[1], 22) + r[2]);
console.log('');
console.log('  ★ 「無毛」は 情報が消えたという意味ではなく、');
console.log('  ★ 「外の観測者の帯域では 3 成分しか残らない」という意味。');
console.log('  ★★ 5 節のとおり、残りは 指数的に低い周波数へ移っただけ ── ただし');
console.log('  ★★ それが「原理的に取り出せる」かどうかは 本稿では決着しません。');

// ============================================================
head('7. 何が未解決のまま残るか');
// ============================================================
console.log('');
const open = [
  ['★ 蒸発が終わったあと何が残るか', '× 本稿では扱えない', '量子重力の問題（第 38 回）'],
  ['★ ページ曲線が実際に下がるか', '△ 模型の仮定', '本稿は ランダムな一様性を仮定した'],
  ['★ 情報が 取り出せるか', '× 未解決', '赤方偏移＝取り出せない、ではない'],
  ['エントロピーが面積なのはなぜか', '△ 数えただけ', '第 39 回と同じ「翻訳」'],
  ['ホーキング温度そのもの', '◎ 式は一行', '第 45 回のウンルーと同じ'],
];
console.log('  ' + pad('問い', 34) + pad('判定', 22) + '根拠');
for (const o of open) console.log('  ' + pad(o[0], 34) + pad(o[1], 22) + o[2]);
console.log('');
console.log('  ★★ 本回も「翻訳」です。情報パラドックスは 解いていません。');
console.log('  ★★ 言えたのは ── 「消えた」ではなく「測れない所へ行った」まで。');

// ============================================================
head('8. 本回のまとめ');
// ============================================================
const rows2 = [
  ['ホーキング温度 = ウンルー温度', '◎ 解析', '★ a → kappa に置き換えるだけ'],
  ['T=2.725 K と釣り合う質量', '◎ 数値', '★ 4.5e22 kg（月の 0.6 倍）'],
  ['S = A/(4 l_p^2)', '◎ 数値', '二通りの数え方が一致'],
  ['★ BH にすると S が 19 桁 増える', '◎ 数値', '★ 重力が最も乱雑'],
  ['蒸発時間 ∝ M^3', '◎ 数値', '宇宙年齢で 1.73e11 kg'],
  ['熱容量が負 → 終わりが加速', '◎ 数値', '最後の 1 秒で 10^22 J 級'],
  ['ページ時刻 = 寿命の 64.6 %', '◎ 解析', '★ M = M0/sqrt(2)'],
  ['★ 1.5 ms で測定帯域の外へ', '◎ 数値', '★ 第 5 回と同じ構図'],
  ['★ 情報パラドックスの解決', '× 扱えない', '★ 本稿は翻訳のみ'],
];
console.log('');
for (const r of rows2) console.log('  ' + pad(r[0], 34) + pad(r[1], 14) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 地平線は「情報を消す装置」ではなく、');
console.log('  ★ 「周波数を指数的に下げる装置」でした。');
console.log('  ★ そして下げきった先は、第 5 回で見た「定数と区別がつかない」領域です。');
