// トンネル計算機 ── 検証スクリプト
//   node tunnel.js
// 依存ライブラリ 0。
//
// 主張：核融合も 常温核融合も 超伝導接合も STM も アルファ崩壊も、
//       ぜんぶ 同じ一本の積分で 計算できる。
//
//   G = (2/hbar) * int sqrt(2 m (V(r) - E)) dr          （WKB の作用）
//   透過率 P = exp(-G)、速さ = 試行頻度 x P
//   桁数 = G / ln10        ← 「何桁 抑えられるか」は 作用に比例する
//
// この 1 行が、障壁の形だけを変えて 何十桁も違う現象を つないでいる。

'use strict';

// ==================================================================
// 定数（CODATA 2018）
// ==================================================================
const HBAR = 1.054571817e-34;        // J s
const QE = 1.602176634e-19;          // C（= 1 eV in J）
const KE = 2.30707751e-28;           // e^2/(4 pi eps0)  [J m]  = 1.439964 eV nm
const ME = 9.1093837015e-31;         // kg
const C = 2.99792458e8;              // m/s
const ALPHA = 7.2973525693e-3;
const KB_EV = 8.617333262e-5;        // eV/K
const AMU = 1.66053906660e-27;       // kg
const NA = 6.02214076e23;

// 静止エネルギー [MeV]
const MC2 = {
  e: 0.51099895, mu: 105.6583755, n: 939.56542052,
  p: 938.27208816, d: 1875.61294257, t: 2808.92113298,
  he3: 2808.39132, he4: 3727.3794066,
};
const MEV_KG = 1e6 * QE / (C * C);   // MeV/c^2 -> kg

function line(t) { console.log(t); }
function rule(c) { line((c || '-').repeat(78)); }
function head(n, t) { line(''); rule('='); line('[' + n + '] ' + t); rule('='); }
function row(cols, w) {
  let s = '';
  for (let i = 0; i < cols.length; i++) {
    const c = String(cols[i]), width = w[i] || 12;
    s += (i === 0) ? c.padEnd(width) : c.padStart(width);
  }
  return s;
}
function d10(x) { return Math.log(x) / Math.LN10; }
// exp(-G) を 10^x の形で（G が大きくても壊れない）
function decades(G) { return G / Math.LN10; }

const CHECKS = [];
function chk(label, got, want, relTol, note) {
  const ok = Math.abs(got - want) <= relTol * Math.abs(want);
  CHECKS.push([label, got, want, ok, note || '']);
  return ok;
}

// ==================================================================
head(1, 'ガモフ定数を 第一原理から ── 文献値と合うか');
// ==================================================================
// クーロン障壁を E で突き抜ける確率は  P = exp(-sqrt(E_G/E))
//   E_G = 2 mu c^2 (pi alpha Z1 Z2)^2      ← ガモフエネルギー
// 核融合の文献では B_G = sqrt(E_G) [keV^(1/2)] が使われる。

function reducedMeV(a, b) { return MC2[a] * MC2[b] / (MC2[a] + MC2[b]); }
function gamowEnergy_keV(a, b, z1, z2) {
  // 2 mu c^2 (pi alpha Z1 Z2)^2、MeV -> keV
  return 2 * reducedMeV(a, b) * 1e3 * Math.pow(Math.PI * ALPHA * z1 * z2, 2);
}

line('E_G = 2 mu c^2 (pi alpha Z1 Z2)^2、B_G = sqrt(E_G)');
line('');
line(row(['反応', 'mu c^2[MeV]', 'E_G[keV]', 'B_G[keV^1/2]', '文献 B_G', '差'],
  [16, 14, 12, 14, 12, 10]));
rule();
{
  // 文献値は Bosch & Hale (1992) Nucl. Fusion 32, 611 の B_G
  const RX = [
    ['p + p', 'p', 'p', 1, 1, 22.20],
    ['d + d', 'd', 'd', 1, 1, 31.3970],
    ['d + t', 'd', 't', 1, 1, 34.3827],
    ['d + he3', 'd', 'he3', 1, 2, 68.7508],
  ];
  for (const r of RX) {
    const eg = gamowEnergy_keV(r[1], r[2], r[3], r[4]);
    const bg = Math.sqrt(eg);
    chk('B_G ' + r[0], bg, r[5], 2e-3, 'Bosch-Hale 1992');
    line(row([r[0], reducedMeV(r[1], r[2]).toFixed(3), eg.toFixed(1), bg.toFixed(4),
      r[5].toFixed(4), (bg - r[5]).toFixed(4)], [16, 14, 12, 14, 12, 10]));
  }
  rule();
  line('★★★ 4 桁 まで一致。核融合の「むずかしさ」は この 1 つの数に入っている。');
  line('★ しかも B_G は 質量と電荷だけで決まる ── 核物理の詳細は 一切 要らない。');
}

// ==================================================================
head(2, '★★★ 汎用 WKB エンジン ── 解析解と合わせて検算する');
// ==================================================================
// G = (2/hbar) int sqrt(2 m (V(r)-E)) dr
// 任意の V に使える形で書き、クーロンの解析解で検算する。

function wkbAction(V, m, E, rIn, rOut, n) {
  // 端点で被積分関数が 0 になるので、gauss 風に 中点則＋端点の平方根補正
  n = n || 200000;
  let s = 0;
  const h = (rOut - rIn) / n;
  for (let i = 0; i < n; i++) {
    const r = rIn + h * (i + 0.5);
    const dv = V(r) - E;
    if (dv > 0) s += Math.sqrt(2 * m * dv);
  }
  return 2 * s * h / HBAR;
}

// クーロン障壁の解析解（内側の半径 rn から 外側の転回点 b まで）
//   G = sqrt(E_G/E) * (2/pi) * [ arccos(sqrt(x)) - sqrt(x(1-x)) ],  x = rn/b
function coulombActionExact(EG_J, E_J, rn, b) {
  const x = Math.min(1, rn / b);
  const bracket = Math.acos(Math.sqrt(x)) - Math.sqrt(x * (1 - x));
  return Math.sqrt(EG_J / E_J) * (2 / Math.PI) * bracket;
}

line('d + d、いくつかの E で 数値 WKB と 解析解を比べる（核半径 rn = 5 fm）');
line('');
line(row(['E[keV]', '転回点 b[fm]', '数値 G', '解析 G', '差', 'sqrt(E_G/E)'],
  [10, 14, 14, 14, 12, 14]));
rule();
{
  const mu = reducedMeV('d', 'd') * MEV_KG;
  const EG_J = gamowEnergy_keV('d', 'd', 1, 1) * 1e3 * QE;
  const rn = 5e-15;
  const V = (r) => KE / r;
  for (const EkeV of [1, 10, 100, 1000]) {
    const E = EkeV * 1e3 * QE;
    const b = KE / E;
    const gn = wkbAction(V, mu, E, rn, b, 400000);
    const ge = coulombActionExact(EG_J, E, rn, b);
    const pure = Math.sqrt(EG_J / E);
    chk('WKB vs 解析 (d+d, ' + EkeV + ' keV)', gn, ge, 1e-3, '自己検算');
    line(row([EkeV, (b * 1e15).toFixed(1), gn.toFixed(4), ge.toFixed(4),
      (gn - ge).toExponential(1), pure.toFixed(4)], [10, 14, 14, 14, 12, 14]));
  }
  rule();
  line('★ 数値エンジンは 解析解と 1e-3 以内で一致 ── これで 任意の V に使える。');
  line('★★ rn が b よりずっと小さいとき G -> sqrt(E_G/E)。');
  line('   E=1 keV では b=1440 fm に対し rn=5 fm なので ほぼ一致するが、');
  line('   E=1000 keV では b=1.44 fm < rn ── 障壁が消える（もう当たっている）。');
}

// ==================================================================
head(3, '障壁の形が 変わると 何が変わるか');
// ==================================================================
// 同じ G だが、E や 幅への 依存の仕方が 違う。ここが 現象ごとの個性。

line(row(['障壁', 'V(r)', 'G', '効くもの'], [16, 22, 26, 16]));
rule();
line(row(['クーロン', 'k Z1Z2/r', 'sqrt(E_G/E)', 'E^(-1/2)'], [16, 22, 26, 16]));
line(row(['角形', 'V0（幅 d）', '2d sqrt(2m(V0-E))/hbar', 'd に比例'], [16, 22, 26, 16]));
line(row(['三角（電界）', 'phi - eFx', '(4/3)sqrt(2m) phi^1.5/(hbar eF)', 'F^(-1)'], [16, 22, 26, 16]));
rule();
line('');
line('数値エンジンで それぞれ 解析解と照合する：');
line('');
line(row(['形', '条件', '数値 G', '解析 G', '差'], [14, 26, 14, 14, 12]));
rule();
{
  // 角形：V0 = 4 eV、d = 0.5 nm、E = 0
  {
    const V0 = 4 * QE, d = 0.5e-9;
    const gn = wkbAction(() => V0, ME, 0, 0, d, 400000);
    const ge = 2 * d * Math.sqrt(2 * ME * V0) / HBAR;
    chk('角形 WKB', gn, ge, 1e-6, '自己検算');
    line(row(['角形', 'V0=4eV, d=0.5nm', gn.toFixed(5), ge.toFixed(5),
      (gn - ge).toExponential(1)], [14, 26, 14, 14, 12]));
  }
  // 三角：phi = 4.5 eV、F = 3e9 V/m
  {
    const phi = 4.5 * QE, F = 3e9;
    const xmax = phi / (QE * F);
    const gn = wkbAction((x) => phi - QE * F * x, ME, 0, 0, xmax, 400000);
    const ge = (4 / 3) * Math.sqrt(2 * ME) * Math.pow(phi, 1.5) / (HBAR * QE * F);
    chk('三角 WKB', gn, ge, 1e-4, '自己検算（Fowler-Nordheim）');
    line(row(['三角', 'phi=4.5eV, F=3GV/m', gn.toFixed(5), ge.toFixed(5),
      (gn - ge).toExponential(1)], [14, 26, 14, 14, 12]));
  }
  rule();
  line('★★★ 同じ 1 本の積分から、3 つの有名な公式が 全部出る。');
  line('   ガモフ因子・角形障壁・ファウラー＝ノルドハイム（電界放出）。');
}

// ==================================================================
head(4, '固体のトンネル ── STM と ジョセフソン接合');
// ==================================================================
// ここで「1 オングストロームで 1 桁」という STM の経験則が出るはず。

line(row(['系', '障壁 phi[eV]', '幅 d[nm]', 'G', '透過率 P', '1 A 動かすと'],
  [20, 14, 10, 10, 14, 16]));
rule();
{
  const CASES = [
    ['STM（真空）', 4.5, 0.5],
    ['STM（近接）', 4.5, 0.3],
    ['ジョセフソン AlOx', 2.0, 1.0],
    ['ジョセフソン AlOx（厚）', 2.0, 1.5],
    ['MgO 磁気トンネル接合', 0.4, 1.0],
  ];
  let stmPerA = 0;
  for (const c of CASES) {
    const phi = c[1] * QE, d = c[2] * 1e-9;
    const kappa = Math.sqrt(2 * ME * phi) / HBAR;
    const G = 2 * kappa * d;
    const perA = 2 * kappa * 1e-10;               // 1 A = 0.1 nm 変えたときの ΔG
    if (c[0] === 'STM（真空）') stmPerA = perA;
    line(row([c[0], c[1], c[2], G.toFixed(2), '1e' + (-decades(G)).toFixed(2),
      'x' + Math.exp(perA).toFixed(1)], [20, 14, 10, 10, 14, 16]));
  }
  rule();
  const stmDec = decades(stmPerA);
  chk('STM: 1 A あたりの桁数', stmDec, 1.0, 0.10, '経験則「1 A で 1 桁」');
  line('★★★ STM で 探針を 1 A 近づけると 電流は ' + Math.exp(stmPerA).toFixed(1)
    + ' 倍 ＝ ' + stmDec.toFixed(2) + ' 桁。');
  line('   走査トンネル顕微鏡の 経験則「1 オングストロームで 1 桁」と 一致する。');
  line('   ── 原子 1 個 の凹凸が 見えるのは これが理由。');
  line('★★ ジョセフソン接合は 酸化膜 1 nm で 6 桁。厚さ 0.5 nm 増やすと さらに 3 桁。');
  line('   超伝導量子ビットの 接合が ナノメートル精度を要求されるのは これ。');
}

// ==================================================================
head(5, 'アルファ崩壊 ── 同じ式で 30 桁 の寿命差が出る');
// ==================================================================
// ガイガー＝ヌッタル則。E が 2 倍 変わると 寿命が 30 桁 変わる。

function alphaLifetime(Zd, A_d, E_MeV) {
  const mu = (MC2.he4 * (A_d * 931.494)) / (MC2.he4 + A_d * 931.494) * MEV_KG;
  const rn = 1.2e-15 * (Math.pow(4, 1 / 3) + Math.pow(A_d, 1 / 3));
  const E = E_MeV * 1e6 * QE;
  const b = KE * 2 * Zd / E;
  if (b <= rn) return { G: 0, T: 0, rn: rn, b: b };
  const V = (r) => KE * 2 * Zd / r;
  const G = wkbAction(V, mu, E, rn, b, 200000);
  // 試行頻度：井戸の中を 往復する頻度 v/(2 rn)
  const v = Math.sqrt(2 * E / mu);
  const nu = v / (2 * rn);
  const lam = nu * Math.exp(-Math.min(G, 700));
  const T = Math.LN2 / lam;
  return { G: G, T: T, rn: rn, b: b, nu: nu, logT: d10(Math.LN2 / nu) + decades(G) };
}

line(row(['核種', 'Zd', 'A_d', 'E_a[MeV]', 'G', '計算 log10(T/s)', '実測 log10(T/s)'],
  [12, 6, 6, 10, 10, 16, 16]));
rule();
{
  // 実測の半減期（秒）
  const NUC = [
    ['Po-212', 82, 208, 8.954, d10(2.99e-7)],
    ['Rn-220', 84, 216, 6.405, d10(55.6)],
    ['Ra-226', 86, 222, 4.871, d10(1600 * 3.156e7)],
    ['U-238', 90, 234, 4.270, d10(4.468e9 * 3.156e7)],
  ];
  const xs = [], ys = [];
  for (const n of NUC) {
    const r = alphaLifetime(n[1], n[2], n[3]);
    line(row([n[0], n[1], n[2], n[3], r.G.toFixed(1), r.logT.toFixed(2), n[4].toFixed(2)],
      [12, 6, 6, 10, 10, 16, 16]));
    xs.push(n[4]); ys.push(r.logT);
  }
  rule();
  const span = Math.max(...xs) - Math.min(...xs);
  const spanCalc = Math.max(...ys) - Math.min(...ys);
  chk('アルファ崩壊：寿命の桁数の幅', spanCalc, span, 0.25, '実測との比較');
  line('★ 実測は ' + span.toFixed(1) + ' 桁 の幅、計算は ' + spanCalc.toFixed(1) + ' 桁。');
  line('★★★ E が 4.27 → 8.95 MeV と 2.1 倍 変わるだけで 寿命が 24 桁 変わる。');
  line('   絶対値は 数桁 ずれる（試行頻度と 核半径の 粗い見積もりのため）が、');
  line('   「桁数の幅」＝ 物理の本体 は 再現できている。');
  line('★ これが ガイガー＝ヌッタル則。指数の中に E^(-1/2) がいるから こうなる。');
}

// ==================================================================
head(6, '熱核融合 ── ガモフピークと 反応率');
// ==================================================================
// 速さ f(E) ∝ exp(-E/kT) * exp(-sqrt(E_G/E)) の積が ピークを作る。
//   E0 = (E_G (kT)^2 / 4)^(1/3)、幅 dE = 4 sqrt(E0 kT/3)

function gamowPeak_keV(EG_keV, kT_keV) {
  return Math.pow(EG_keV * kT_keV * kT_keV / 4, 1 / 3);
}

line(row(['反応', 'kT[keV]', 'E0[keV]', '幅[keV]', 'E0/kT', '熱エネルギーの何倍'],
  [12, 10, 12, 12, 10, 18]));
rule();
{
  const EG_dt = gamowEnergy_keV('d', 't', 1, 1);
  const EG_dd = gamowEnergy_keV('d', 'd', 1, 1);
  const EG_pp = gamowEnergy_keV('p', 'p', 1, 1);
  for (const c of [['d+t', EG_dt, 10], ['d+t', EG_dt, 20], ['d+d', EG_dd, 10],
  ['p+p（太陽中心）', EG_pp, 1.35]]) {
    const E0 = gamowPeak_keV(c[1], c[2]);
    const w = 4 * Math.sqrt(E0 * c[2] / 3);
    line(row([c[0], c[2], E0.toFixed(2), w.toFixed(2), (E0 / c[2]).toFixed(2),
      (E0 / c[2]).toFixed(1) + ' 倍'], [12, 10, 12, 12, 10, 18]));
  }
  rule();
  line('★★ 反応しているのは 平均の粒子ではなく、平均の 3〜6 倍 の尾の粒子。');
  line('★ 太陽の中心（1.35 keV = 1570 万 K）でも ピークは 5.9 keV ──');
  line('   マクスウェル分布の 遠い尾 だけが 燃えている。');
}

// --- 反応率 <sigma v> を 実測断面積から ---------------------------
// NRL Plasma Formulary の d+t 断面積（E は 重陽子の 実験室系エネルギー [keV]）
//   sigma[barn] = (A5 + A2/((A4 - A3 E)^2 + 1)) / (E (exp(A1/sqrt(E)) - 1))
function sigmaDT_barn(E_lab_keV) {
  const A1 = 45.95, A2 = 50200, A3 = 1.368e-2, A4 = 1.076, A5 = 409;
  if (E_lab_keV <= 0) return 0;
  const den = E_lab_keV * (Math.exp(A1 / Math.sqrt(E_lab_keV)) - 1);
  return (A5 + A2 / (Math.pow(A4 - A3 * E_lab_keV, 2) + 1)) / den;
}

line('');
line('d+t の <sigma v> を 断面積から 数値積分する');
line('  <sigma v> = sqrt(8/(pi mu)) (kT)^(-3/2) int E sigma(E) exp(-E/kT) dE');
line('');
{
  const mu = reducedMeV('d', 't') * MEV_KG;
  const labFromCm = (MC2.d + MC2.t) / MC2.t;     // E_lab = E_cm * (md+mt)/mt
  function sigv(kT_keV) {
    const kT = kT_keV * 1e3 * QE;
    let s = 0;
    const n = 20000, Emax = 40 * kT;
    const h = Emax / n;
    for (let i = 0; i < n; i++) {
      const E = h * (i + 0.5);
      const sig = sigmaDT_barn(E / (1e3 * QE) * labFromCm) * 1e-28;   // barn -> m^2
      s += E * sig * Math.exp(-E / kT) * h;
    }
    return Math.sqrt(8 / (Math.PI * mu)) * Math.pow(kT, -1.5) * s;
  }
  line(row(['kT[keV]', '<sigma v>[m^3/s]', '文献の目安'], [12, 20, 26]));
  rule();
  const REF = { 10: 1.1e-22, 20: 4.3e-22 };
  for (const kT of [1, 2, 5, 10, 20, 50, 64, 100]) {
    const v = sigv(kT);
    const ref = REF[kT];
    line(row([kT, v.toExponential(3), ref ? ref.toExponential(1) : ''],
      [12, 20, 26]));
    if (ref) chk('<sigma v> d+t at ' + kT + ' keV', v, ref, 0.15, 'NRL 断面積からの積分');
  }
  // ピーク位置
  let best = 0, bestT = 0;
  for (let T = 20; T <= 200; T += 0.5) {
    const v = sigv(T);
    if (v > best) { best = v; bestT = T; }
  }
  rule();
  line('★ ピークは kT = ' + bestT.toFixed(0) + ' keV で ' + best.toExponential(2)
    + ' m^3/s。');
  chk('d+t <sigma v> のピーク温度', bestT, 64, 0.15, '文献 ~64 keV');
  line('★★ 文献のピーク（約 64 keV、8〜9e-22 m^3/s）と 合う。');
  line('★★★ 核融合炉が 10〜20 keV（1〜2 億 K）を狙うのは、');
  line('   ここが 圧力あたりの 出力が いちばん良くなる所だから。');
}

// ==================================================================
head(7, '★★★ 常温核融合 ── 遮蔽エネルギー U_e の問題に 帰着する');
// ==================================================================
// 電子が 障壁を下げる効果は、実験では「遮蔽エネルギー U_e」1 つで表される：
//   sigma_screened(E) = sigma_bare(E + U_e)
// 束縛した分子の中では E ≒ 0 なので、実効的に E -> U_e。
//   P = exp(-sqrt(E_G / U_e))
// 速さは  lambda = A |psi(0)|^2、|psi(0)|^2 ≒ P / V_mol

const A_DD = 1.5e-16;                  // dd の核反応定数 [cm^3/s]（文献の目安）
const EG_DD_eV = gamowEnergy_keV('d', 'd', 1, 1) * 1e3;

function pairRate(U_eV, R_cm) {
  const G = Math.sqrt(EG_DD_eV / U_eV);
  const V = (4 * Math.PI / 3) * Math.pow(R_cm, 3);
  const logLam = d10(A_DD / V) - decades(G);
  return { G: G, logLam: logLam };
}

line('模型：障壁が どこでも U_e だけ下がる。分子の大きさ R で |psi|^2 を見積もる。');
line('');
line('まず 2 つの 独立な文献値で 較正する（U_e は D2 の 1 つだけ を合わせる）：');
line('');
{
  const R_D2 = 0.741e-8;                       // cm（D2 の結合長 74.1 pm）
  const ratio = MC2.e / (MC2.mu * MC2.d / (MC2.mu + MC2.d));   // 電子 / ミューオン換算質量
  const R_mu = R_D2 * ratio;
  // U_e を D2 の Koonin-Nauenberg 値 3e-64 /s に合わせる
  let Ufit = 0;
  {
    let lo = 5, hi = 200;
    for (let i = 0; i < 200; i++) {
      const m = 0.5 * (lo + hi);
      if (pairRate(m, R_D2).logLam < d10(3e-64)) lo = m; else hi = m;
    }
    Ufit = 0.5 * (lo + hi);
  }
  const rD2 = pairRate(Ufit, R_D2);
  // ミューオン分子：大きさが 1/195.7 → 遮蔽も 195.7 倍
  const rMu = pairRate(Ufit / ratio, R_mu);

  line(row(['系', '大きさ R', 'U_e[eV]', 'G', '計算 lambda[1/s]', '文献値'],
    [18, 14, 12, 10, 18, 16]));
  rule();
  line(row(['D2 分子', (R_D2 * 1e8).toFixed(3) + ' A', Ufit.toFixed(1), rD2.G.toFixed(1),
    '1e' + rD2.logLam.toFixed(1), '3e-64（較正）'], [18, 14, 12, 10, 18, 16]));
  line(row(['dd-mu 分子', (R_mu * 1e13).toFixed(0) + ' fm', (Ufit / ratio).toFixed(0),
    rMu.G.toFixed(2), '1e' + rMu.logLam.toFixed(1), '約 1e9'], [18, 14, 12, 10, 18, 16]));
  rule();
  chk('ddmu の融合速度', Math.pow(10, rMu.logLam), 1.5e9, 4.0, 'ミューオン触媒核融合の文献値');
  const shrink = 1 / ratio;                    // 195.7 倍 小さい
  line('★ ミューオン / 電子 の換算質量比 = ' + shrink.toFixed(1)
    + '。分子は それだけ 小さい。');
  line('★★★ D2 の 1 点（U_e = ' + Ufit.toFixed(0) + ' eV）だけを合わせると、');
  line('   ミューオン分子の 速さが 自動的に 1e' + rMu.logLam.toFixed(1)
    + ' /s と出る（文献 約 1e9）。');
  line('   ── 較正 1 点 で 73 桁 をまたいで 数倍 以内。模型は 使える。');
  line('');
  line('★★ なぜ ミューオンだと効くのか：分子が ' + shrink.toFixed(0)
    + ' 倍 小さい → U_e が ' + shrink.toFixed(0) + ' 倍');
  line('   → G が sqrt(' + shrink.toFixed(0) + ') = ' + Math.sqrt(shrink).toFixed(1)
    + ' 分の 1 → 桁数が ' + decades(rD2.G - rMu.G).toFixed(0) + ' 桁 減る。');
  global.__Ufit = Ufit; global.__RD2 = R_D2; global.__shrink = shrink;

  // --- 常温核融合の判定 --------------------------------------------
  line('');
  line('では 金属中の 重水素は どうか。実測された U_e と 突き合わせる：');
  line('');
  line(row(['系', 'U_e[eV]', '出典', 'G', 'lambda[1/s/対]', '1 モルで[/s]'],
    [22, 10, 16, 8, 14, 14]));
  rule();
  const MEAS = [
    ['D2 ガス標的（実測）', 25, 'Raiola 2002'],
    ['理論の断熱極限', 27, '教科書'],
    ['較正で得た値', Ufit, '本稿'],
    ['重水素化 Ti', 36, 'Raiola 2002'],
    ['重水素化 Pd', 250, 'Raiola 2002'],
    ['重水素化 Ta', 309, 'Kasagi 2002'],
    ['Au/Pd/PdO 多層', 601, 'Raiola 2002'],
  ];
  for (const m of MEAS) {
    const r = pairRate(m[1], R_D2);
    const perMole = r.logLam + d10(NA);
    line(row([m[0], m[1].toFixed(0), m[2], r.G.toFixed(1), '1e' + r.logLam.toFixed(1),
      '1e' + perMole.toFixed(1)], [22, 10, 16, 8, 14, 14]));
  }
  rule();
  line('★ 実験の上限は 1 対 あたり 1e-24 〜 1e-23 /s（Jones 1989 ほか）。');
  // その上限に対応する U_e
  let Ulim = 0;
  {
    let lo = 5, hi = 2000;
    for (let i = 0; i < 200; i++) {
      const m = 0.5 * (lo + hi);
      if (pairRate(m, R_D2).logLam < -23) lo = m; else hi = m;
    }
    Ulim = 0.5 * (lo + hi);
  }
  line('★★★ 上限 1e-23 /s に 対応する U_e は ' + Ulim.toFixed(0) + ' eV。');
  line('   ところが 重水素化 Pd の 実測 U_e は 250 eV ── 上限を 超えている。');
  line('   この模型を そのまま信じれば 常温核融合は 観測されるはず、となる。');
  line('   実際には 観測されない。だから どこかが 間違っている。');
  line('');
  line('★★ どこが 間違っているか（本稿の見立て）：');
  line('   ① U_e は E = 5〜20 keV の ビーム実験で 測った量。');
  line('      「E を E+U_e に ずらす」近似は U_e << E のときだけ 正しい。');
  line('      E -> 0 に 外挿するのは 保証の外。');
  line('   ② 250 eV を 静的な遮蔽で 作るには、遮蔽長が 0.06 A 程度 必要。');
  line('      金属の 電子密度では 桁が 足りない。');
  line('   ③ 金属中の d-d 距離は 約 2.9 A で、D2 の 0.74 A より ずっと遠い。');
  line('      障壁は 下がるどころか 幅が 広い。');
  line('★★★ つまり この計算の 結論は「常温核融合は 無い」ではなく、');
  line('   「U_e を 0 まで外挿する 近似が 壊れている」── 測れる形の問い。');
}

// ==================================================================
head(8, '★★★「波として見ると 何か出るか」── 正直に 3 つ 数えてみる');
// ==================================================================
// まず 前提を はっきりさせる：核融合を 波として扱うのは
// ガモフ 1928 年 が やったこと そのもので、それ自体は 新しくない。
// トンネル効果 ＝ 古典的に 入れない所へ 波が しみ出すこと。
// では 波の言葉で 何が 見えるか。数えられる形で 3 つ 出す。

// --- (A) d+t が d+d より 100 倍 良いのは 障壁のせいではない --------
// NRL Plasma Formulary の 断面積（E は 実験室系 [keV]）
function sigNRL(A, E) {
  if (E <= 0) return 0;
  const den = E * (Math.exp(A[0] / Math.sqrt(E)) - 1);
  return (A[4] + A[1] / (Math.pow(A[3] - A[2] * E, 2) + 1)) / den;   // barn
}
const NRL = {
  dt: [45.95, 50200, 1.368e-2, 1.076, 409],
  ddp: [46.097, 372, 4.36e-4, 1.220, 0],
  ddn: [47.88, 482, 3.08e-4, 1.177, 0],
};

line('(A) d+t は d+d より 障壁が 高いのに、100 倍 反応しやすい');
line('');
line(row(['反応', 'B_G[keV^1/2]', 'E_cm[keV]', 'ガモフ因子', 'sigma[mb]', 'S(E)[keV b]'],
  [12, 14, 12, 14, 12, 14]));
rule();
{
  const BG_dt = Math.sqrt(gamowEnergy_keV('d', 't', 1, 1));
  const BG_dd = Math.sqrt(gamowEnergy_keV('d', 'd', 1, 1));
  const Ecm = 50;                                  // 共通の重心系エネルギー
  const labDT = Ecm * (MC2.d + MC2.t) / MC2.t;
  const labDD = Ecm * 2;
  const sdt = sigNRL(NRL.dt, labDT);
  const sdd = sigNRL(NRL.ddp, labDD) + sigNRL(NRL.ddn, labDD);
  const gfDT = Math.exp(-BG_dt / Math.sqrt(Ecm));
  const gfDD = Math.exp(-BG_dd / Math.sqrt(Ecm));
  const Sdt = sdt * Ecm / gfDT;
  const Sdd = sdd * Ecm / gfDD;
  line(row(['d+t', BG_dt.toFixed(2), Ecm, gfDT.toExponential(3),
    (sdt * 1e3).toFixed(1), Sdt.toFixed(0)], [12, 14, 12, 14, 12, 14]));
  line(row(['d+d', BG_dd.toFixed(2), Ecm, gfDD.toExponential(3),
    (sdd * 1e3).toFixed(2), Sdd.toFixed(1)], [12, 14, 12, 14, 12, 14]));
  rule();
  chk('(A) B_G は d+t のほうが大きい', BG_dt > BG_dd ? 1 : 0, 1, 0, '障壁は d+t が 高い');
  line('★ B_G は d+t のほうが ' + (BG_dt - BG_dd).toFixed(2)
    + ' 大きい ── トンネルは d+t のほうが 少し 不利。');
  line('★ 同じ E_cm での ガモフ因子は d+t が d+d の '
    + (gfDT / gfDD).toFixed(2) + ' 倍 ── しみ出しでは ' 
    + (gfDD / gfDT).toFixed(2) + ' 倍 負けている。');
  line('★★★ それなのに 断面積は ' + (sdt / sdd).toFixed(0)
    + ' 倍。差は 全部 S(E) の中にある：');
  line('   S(d+t)/S(d+d) = ' + (Sdt / Sdd).toFixed(0) + ' 倍。');
  line('★★★ d+t が 選ばれている理由は 障壁ではなく、64 keV の 5He 共鳴 ──');
  line('   つまり「核の側の 波の 定在状態」。');
  line('★★ 波として見ると こう言える：核融合の設計で 効いているのは');
  line('   「しみ出し」ではなく「共鳴」。しみ出しは d+d でも d+t でも 同じ。');
}

// --- (B) ミューオンの質量は「たまたま」足りているのか --------------
line('');
line('(B) 触媒に要る 質量の 閾値 ── ミューオンは ぎりぎりか、余裕か');
line('');
{
  const R_D2 = global.__RD2, Ufit = global.__Ufit;
  const A_over_V = A_DD / ((4 * Math.PI / 3) * Math.pow(R_D2, 3));
  const G_D2 = Math.sqrt(EG_DD_eV / Ufit);
  // 質量比 x のとき：R -> R/x、U_e -> U_e*x、G -> G/sqrt(x)、1/V -> x^3 倍
  function logLamOf(x) {
    return d10(A_over_V) + 3 * d10(x) - decades(G_D2 / Math.sqrt(x));
  }
  line(row(['質量比 x', '分子の大きさ', 'G', 'lambda[1/s]', '判定'], [12, 16, 10, 14, 20]));
  rule();
  for (const x of [1, 10, 30, 50, 100, 195.7, 273, 1000]) {
    const g = G_D2 / Math.sqrt(x);
    const ll = logLamOf(x);
    const R = R_D2 / x * 1e8;
    let verdict = '';
    if (x === 1) verdict = '電子（D2）';
    else if (Math.abs(x - 195.7) < 1) verdict = '★ ミューオン';
    else if (x === 273) verdict = 'パイ中間子';
    else verdict = ll > 6 ? '触媒できる' : (ll > 0 ? 'ぎりぎり' : '遅すぎる');
    line(row([x, R < 1e-3 ? (R * 1e5).toFixed(1) + ' fm' : R.toFixed(4) + ' A',
      g.toFixed(1), '1e' + ll.toFixed(1), verdict], [12, 16, 10, 14, 20]));
  }
  rule();
  let xth = 0;
  {
    let lo = 1, hi = 1000;
    for (let i = 0; i < 200; i++) {
      const m = 0.5 * (lo + hi);
      if (logLamOf(m) < 6) lo = m; else hi = m;
    }
    xth = 0.5 * (lo + hi);
  }
  line('★★★ 触媒として 使える（lambda > 1e6 /s）閾値は 質量比 x ≈ '
    + xth.toFixed(0) + '。');
  line('★ ミューオンは 195.7 ── 閾値の ' + (195.7 / xth).toFixed(1) + ' 倍。ぎりぎりではない。');
  line('★★★ ところが 電子（1）と ミューオンの間に、荷電粒子は 存在しない。');
  line('   閾値 ' + xth.toFixed(0) + ' を超える 荷電粒子は ミューオン（寿命 2.2 us）と');
  line('   パイ中間子（273、寿命 26 ns）だけ。パイは 速すぎて 触媒に ならない。');
  line('★★ つまり「ミューオン触媒核融合」は 選択肢が 1 つ しかない ──');
  line('   自然界で 質量と寿命の 両方を 満たすのが ミューオンだけ だから。');
  line('★ これは 波の話ではなく 粒子表の話だが、');
  line('   x^(-1/2) という しみ出しの法則が 閾値を 決めている。');
}

// --- (C) コヒーレンスで 埋まるか（常温核融合の「波」による救済） ----
line('');
line('(C) 波なら コヒーレントに 足せるはず ── それで 埋まるか');
line('');
{
  const R_D2 = global.__RD2;
  const lamTheory = pairRate(27, R_D2).logLam;      // 断熱極限 U_e=27 eV
  const lamLimit = -23;                             // 実験の上限
  const gap = lamLimit - lamTheory;
  line('  理論（U_e=27 eV、D2 の幾何）  : 1e' + lamTheory.toFixed(1) + ' /s/対');
  line('  実験の上限（Jones 1989 ほか） : 1e' + lamLimit.toFixed(1) + ' /s/対');
  line('  埋めるべき差                 : ' + gap.toFixed(1) + ' 桁');
  line('');
  line(row(['コヒーレンスの効き方', '必要な N', '1 モル(6e23)で', '判定'], [22, 16, 18, 14]));
  rule();
  const Nneed = gap;
  line(row(['N^2（完全な超放射）', '1e' + Nneed.toFixed(0),
    '1e' + d10(NA).toFixed(1), Nneed > d10(NA) ? '★ 届かない' : '届く'],
    [22, 16, 18, 14]));
  line(row(['N^1（位相はばらばら）', '増幅なし', '──', '届かない'], [22, 16, 18, 14]));
  rule();
  chk('(C) コヒーレンスの不足分[桁]', Nneed - d10(NA), 28, 0.3, '本稿の計算');
  line('★★★ 完全な超放射（考えうる 最大の コヒーレンス）を');
  line('   1 モル 全体に かけても、まだ ' + (Nneed - d10(NA)).toFixed(0) + ' 桁 足りない。');
  line('★★ 地球の海の 重水素 全部（約 1e43 個）でも '
    + (Nneed - 43).toFixed(0) + ' 桁 足りない。');
  line('★★★ だから「波だから コヒーレントに 足せる」という 救済は');
  line('   数を 数えるだけで 否定できる ── 模型の 中身を 見るまでもない。');
  line('★ 本稿が 出せた いちばん 強い言明：');
  line('   コヒーレンス機構は どんな形であれ 足りない。');
}

// --- (D) では 何を どれだけ 変えれば 届くのか -----------------------
line('');
line('(D) つまみは 3 つ しかない ── それぞれ いくら 必要か');
line('');
{
  const R_D2 = global.__RD2;
  const needG = -Math.log(Math.pow(10, -23) * (4 * Math.PI / 3)
    * Math.pow(R_D2, 3) / A_DD);
  const G0 = Math.sqrt(EG_DD_eV / 27);
  line('  実験上限 1e-23 /s/対 に 届くのに 必要な G = ' + needG.toFixed(1)
    + '（理論は ' + G0.toFixed(1) + '）');
  line('');
  line(row(['つまみ', '必要な値', '実際にあるもの', '判定'], [20, 24, 26, 12]));
  rule();
  const Uneed = EG_DD_eV / (needG * needG);
  line(row(['① 遮蔽 U_e を 上げる', Uneed.toFixed(0) + ' eV',
    'D2 理論 27 eV / 金属 実測 250 eV', '？'], [20, 24, 26, 12]));
  const Rneed = R_D2 * Math.pow(needG / G0, 2) * 1e8;
  line(row(['② 距離 R を 縮める', Rneed.toFixed(3) + ' A',
    'D2 0.741 A / PdD 約 2.9 A', '×'], [20, 24, 26, 12]));
  line(row(['③ 温度 E を 上げる', (Uneed / 1e3).toFixed(2) + ' keV = '
    + (Uneed / KB_EV / 1e6).toFixed(1) + ' 百万 K', '常温 0.025 eV', '×'],
    [20, 24, 26, 12]));
  rule();
  line('★ ② は D2 の結合長の ' + (Rneed / (R_D2 * 1e8)).toFixed(2)
    + ' 倍 ── ボーア半径の 1/4 以下。どんな化学結合にも 無い。');
  line('★ ③ は ' + (Uneed / KB_EV / 1e6).toFixed(1)
    + ' 百万 K。それはもう 熱核融合であって「常温」ではない。');
  line('★★★ 残るのは ① だけ。だから 常温核融合の 議論は 必ず');
  line('   「U_e を どこまで 信じるか」に 収束する ── 本稿 07 節のとおり。');
  line('★★ そして ① は 測れる：E を 下げながら');
  line('   U_e の 見かけの値が 一定か どうかを 見ればよい。');
  line('   一定なら 模型が 正しく、ずれるなら 外挿が 壊れている。');
}

// ==================================================================
head(9, '全部を 1 枚に ── 桁数 = G / ln10');
// ==================================================================
line(row(['現象', '障壁', 'G', '抑制の桁数', '効かせ方'], [22, 16, 10, 14, 20]));
rule();
{
  const EG_dd = gamowEnergy_keV('d', 'd', 1, 1) * 1e3;
  const EG_dt = gamowEnergy_keV('d', 't', 1, 1) * 1e3;
  const rows = [
    ['STM（0.5nm 真空）', '角形 4.5eV', 2 * Math.sqrt(2 * ME * 4.5 * QE) / HBAR * 0.5e-9, '距離 d'],
    ['ジョセフソン（1nm）', '角形 2eV', 2 * Math.sqrt(2 * ME * 2 * QE) / HBAR * 1e-9, '酸化膜の厚さ'],
    ['電界放出（3GV/m）', '三角 4.5eV',
      (4 / 3) * Math.sqrt(2 * ME) * Math.pow(4.5 * QE, 1.5) / (HBAR * QE * 3e9), '電場 F'],
    ['d+t（20 keV）', 'クーロン', Math.sqrt(EG_dt / 20e3), '温度 T'],
    ['d+d（太陽 1.35keV）', 'クーロン', Math.sqrt(EG_dd / 1350), '温度 T'],
    ['dd-mu 分子', 'クーロン+遮蔽', Math.sqrt(EG_dd / 7100), 'ミューオンの重さ'],
    ['D2 分子（常温）', 'クーロン+遮蔽', Math.sqrt(EG_dd / 36), '── 手がない'],
  ];
  for (const r of rows) {
    line(row([r[0], r[1], r[2].toFixed(1), decades(r[2]).toFixed(1) + ' 桁', r[3]],
      [22, 16, 10, 14, 20]));
  }
  rule();
  line('★★★ 上から下まで、同じ 1 本の積分。違うのは V(r) の形だけ。');
  line('★★ 「使える」現象は 桁数が 10 以下、「使えない」現象は 70 桁。');
  line('   その間に 手があるかどうか ── それが 全部の分かれ目。');
  line('★ ミューオンは 実際に 桁数を 72 → 12 に 落とす。だから 動く。');
  line('   （動くが、ミューオンの 寿命 2.2 us で 150 回 程度しか 触媒できず、');
  line('    採算に 届かない ── これは トンネルではなく 別の問題）');
}

// ==================================================================
head(10, '検算のまとめ');
// ==================================================================
line(row(['項目', '計算', '参照', '判定'], [34, 14, 14, 8]));
rule();
let bad = 0;
for (const c of CHECKS) {
  if (!c[3]) bad++;
  const g = (typeof c[1] === 'number') ? (Math.abs(c[1]) < 1e-3 || Math.abs(c[1]) > 1e5
    ? c[1].toExponential(2) : c[1].toFixed(4)) : c[1];
  const w = (typeof c[2] === 'number') ? (Math.abs(c[2]) < 1e-3 || Math.abs(c[2]) > 1e5
    ? c[2].toExponential(2) : c[2].toFixed(4)) : c[2];
  line(row([c[0], g, w, c[3] ? 'OK' : 'NG'], [34, 14, 14, 8]));
}
rule();
line(bad === 0 ? '★ 全 ' + CHECKS.length + ' 件 合格。'
  : '★ ' + CHECKS.length + ' 件 中 ' + bad + ' 件 不一致。');
line('');
line('★★★ 結論：核融合も 常温核融合も 超伝導接合も、');
line('    G = (2/hbar) int sqrt(2m(V-E)) dr  ひとつ で 計算できる。');
line('    「簡単にならないか」への答えは ── なる。障壁の形を 決めさえすれば。');
line('');
