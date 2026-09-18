// 考える波 第64回「あの式の名前」検証
//   node namae.js
// 依存ライブラリ 0。
//
// 第62回で使った  G = (2/hbar) int sqrt(2m(V-E)) dx  には 名前が あるのか。
//
// 答え：少なくとも 六つ ある。そして いちばん深い名前は
//   「虚時間における 古典軌道の 作用」＝ ユークリッド作用 S_E。
//   G = 2 S_E / hbar。
//
// 本稿で 数値で 確かめること：
//   ★ 虚時間にすると 障壁が 谷に なり、禁止領域を 古典的に 通れる（03節）
//   ★ WKB は 桁を 当てるが 係数を 一定倍 外す（04節）
//   ★ 障壁の頭では e^-G が 破綻し、ケンブル 1/(1+e^G) が 正しい（05節）
//   ★★ アレニウスと ガモフは 同じ式の 両極限。境目は T_c = hbar w_b / 2pi k_B（06節）
//   ★★ その 2pi は ウンルー温度の 2pi と 同じもの（07節）
//   ★★★ 摂動級数の 発散の速さが 作用を 知っている（08節）

'use strict';

function line(t) { console.log(t); }
function rule(c) { line((c || '-').repeat(80)); }
function head(n, t) { line(''); rule('='); line('[' + n + '] ' + t); rule('='); }
function row(cols, w) {
  let s = '';
  for (let i = 0; i < cols.length; i++) {
    const c = String(cols[i]), width = w[i] || 12;
    s += (i === 0) ? c.padEnd(width) : c.padStart(width);
  }
  return s;
}
const CHECKS = [];
function chk(label, got, want, relTol, note) {
  const ok = Math.abs(got - want) <= relTol * Math.abs(want);
  CHECKS.push([label, got, want, ok, note || '']);
  return ok;
}

// ==================================================================
head(1, 'あの式の 名前 ── 六つ ある');
// ==================================================================
line(row(['呼び名', '誰', '年', '文脈'], [26, 22, 8, 22]));
rule();
const NAMES = [
  ['リウヴィル＝グリーン近似', 'Liouville, Green', 1837, '数学（2階 ODE の漸近解）'],
  ['（ジェフリーズも）', 'Jeffreys', 1923, '→ WKBJ と 呼ぶ流儀も'],
  ['WKB 近似', 'Wentzel/Kramers/Brillouin', 1926, '量子力学'],
  ['ガモフ因子', 'Gamow', 1928, 'クーロン障壁（第62回）'],
  ['ケンブルの公式', 'Kemble', 1935, '一様に正しい 1/(1+e^G)'],
  ['インスタントン／バウンス', 'Coleman', 1977, '場の理論・虚時間'],
];
for (const n of NAMES) line(row(n, [26, 22, 8, 22]));
rule();
line('★ 同じ積分に 140 年 かけて 六つの名前が ついた。');
line('★★ そして いちばん 深い名前は 最後の もの ──');
line('   積分そのものが「虚時間における 古典軌道の 作用」S_E で、');
line('   トンネル振幅が exp(-S_E/hbar)。これを インスタントンと 呼ぶ。');
line('★★★ つまり トンネル効果とは「虚時間の 古典運動」だった。');

// ==================================================================
head(2, 'なぜ 2/hbar なのか ── 振幅と 確率');
// ==================================================================
line('振幅は  psi ~ exp(-S_E/hbar)、S_E = int sqrt(2m(V-E)) dx');
line('確率は  P = |psi|^2 = exp(-2 S_E/hbar) = exp(-G)');
line('');
line('  → G = 2 S_E / hbar。第62回の「2/hbar」の 2 は、');
line('    振幅を 2 乗して 確率に したから。');
line('★ 桁で 言えば：振幅は G/(2 ln10) 桁、確率は G/ln10 桁 抑えられる。');
line('★★ 第58回の ボゴリューボフ |beta| も 振幅 ── だから あちらは 半分。');

// ==================================================================
head(3, '★★★ 虚時間にすると 障壁が 谷になる ── 数値で 確かめる');
// ==================================================================
// 実時間  : m x'' = -V'(x)
// t = -i tau とすると  m d^2x/dtau^2 = +V'(x)   ← ポテンシャルが 反転する
// 反転した -V の中では、禁止領域が 古典的に 通れる 谷に なる。
// その軌道の ユークリッド作用
//   S_E = int [ (m/2)(dx/dtau)^2 + V - E ] dtau
// は、エネルギー保存 (m/2)(dx/dtau)^2 = V - E を 使うと
//   S_E = int 2(V-E) dtau = int sqrt(2m(V-E)) dx
// に なるはず。実際に 反転ポテンシャルの 運動方程式を 解いて 確かめる。

function wkbIntegral(V, m, E, x1, x2, n) {
  let s = 0; const h = (x2 - x1) / n;
  for (let i = 0; i < n; i++) {
    const dv = V(x1 + h * (i + 0.5)) - E;
    if (dv > 0) s += Math.sqrt(2 * m * dv);
  }
  return s * h;
}
// 反転ポテンシャルでの 古典運動を RK4 で 解き、作用を 積む
function euclideanAction(V, dV, m, E, x1, x2, nstep) {
  // 転回点 x1 から 出発（速度 0）。数値的に 動き出せるよう わずかに 内側から。
  const eps = (x2 - x1) * 1e-7;
  let x = x1 + eps;
  let v = Math.sqrt(Math.max(0, 2 * (V(x) - E) / m));   // dx/dtau
  const dtau = 1e-5;
  let S = 0, steps = 0;
  const acc = (xx) => dV(xx) / m;                        // d2x/dtau2 = +V'/m
  while (x < x2 - eps && steps < nstep) {
    // 作用の 被積分関数（中点で）
    const f = (xx, vv) => 0.5 * m * vv * vv + V(xx) - E;
    const k1x = v, k1v = acc(x);
    const k2x = v + dtau / 2 * k1v, k2v = acc(x + dtau / 2 * k1x);
    const k3x = v + dtau / 2 * k2v, k3v = acc(x + dtau / 2 * k2x);
    const k4x = v + dtau * k3v, k4v = acc(x + dtau * k3x);
    const xm = x + dtau / 2 * k1x, vm = v + dtau / 2 * k1v;
    S += f(xm, vm) * dtau;
    x += dtau / 6 * (k1x + 2 * k2x + 2 * k3x + k4x);
    v += dtau / 6 * (k1v + 2 * k2v + 2 * k3v + k4v);
    steps++;
  }
  return { S: S, steps: steps, tau: steps * dtau, xend: x };
}

{
  line('反転ポテンシャルの 中を 古典的に 走らせ、作用を 積む');
  line('（hbar = m = 1。障壁は V = V0 sech^2(x/a)、V0=1, a=3）');
  line('');
  const V0 = 1, a = 3, m = 1;
  const V = (x) => V0 / Math.pow(Math.cosh(x / a), 2);
  const dV = (x) => -2 * V0 * Math.tanh(x / a) / Math.pow(Math.cosh(x / a), 2) / a;
  line(row(['E', '転回点 ±x_t', '虚時間の作用 S_E', 'WKB 積分', '比'],
    [10, 16, 20, 16, 10]));
  rule();
  for (const E of [0.2, 0.4, 0.6, 0.8]) {
    const xt = a * Math.acosh(Math.sqrt(V0 / E));
    const r = euclideanAction(V, dV, m, E, -xt, xt, 20000000);
    const w = wkbIntegral(V, m, E, -xt, xt, 400000);
    line(row([E, xt.toFixed(4), r.S.toFixed(6), w.toFixed(6),
      (r.S / w).toFixed(6)], [10, 16, 20, 16, 10]));
    chk('虚時間の作用 = WKB 積分（E=' + E + '）', r.S, w, 2e-3, '反転ポテンシャルの 古典運動');
  }
  rule();
  line('★★★ 一致した。禁止領域は「虚時間では 通れる谷」だった。');
  line('★★ 古典的に 通れないのは 実時間の 話で、');
  line('   時間を 90 度 回すと 障壁は 谷に なり、粒子は 普通に 転がる。');
  line('★ その軌道は 出発点に 戻ってくるので「バウンス（跳ね返り）」と 呼ばれる。');
}

// ==================================================================
head(4, '厳密解と 比べる ── WKB は 桁を 当て、係数を 外す');
// ==================================================================
// エッカート（ポッシェル＝テラー）障壁 V = V0 sech^2(x/a) は 厳密に 解ける。
{
  const V0 = 1, a = 3;
  const LAM = 8 * V0 * a * a;                   // 8 m V0 a^2 / hbar^2
  const Texact = (E) => {
    const s = Math.sinh(Math.PI * Math.sqrt(2 * E) * a);
    const d = (LAM > 1) ? Math.cosh(0.5 * Math.PI * Math.sqrt(LAM - 1))
      : Math.cos(0.5 * Math.PI * Math.sqrt(1 - LAM));
    return s * s / (s * s + d * d);
  };
  const Ganal = (E) => 2 * Math.PI * a * Math.SQRT2 * (Math.sqrt(V0) - Math.sqrt(E));
  line('V = V0 sech^2(x/a)、V0=1, a=3（hbar=m=1）');
  line('');
  line(row(['E/V0', 'G', 'e^-G', '厳密', '厳密/e^-G'], [10, 12, 14, 14, 12]));
  rule();
  const ratios = [];
  for (const r of [0.1, 0.2, 0.3, 0.5, 0.7]) {
    const E = r * V0, g = Ganal(E), ex = Texact(E), wk = Math.exp(-g);
    ratios.push(ex / wk);
    line(row([r.toFixed(2), g.toFixed(4), wk.toExponential(3),
      ex.toExponential(3), (ex / wk).toFixed(4)], [10, 12, 14, 14, 12]));
  }
  rule();
  // 前置因子の 解析値： exp( pi[ 2a sqrt(2V0) - sqrt(8 V0 a^2 - 1) ] )
  const pref = Math.exp(Math.PI * (2 * a * Math.sqrt(2 * V0) - Math.sqrt(LAM - 1)));
  const spread = Math.max(...ratios) - Math.min(...ratios);
  const meanR = ratios.reduce((x, y) => x + y, 0) / ratios.length;
  chk('WKB 前置因子の 相対ばらつき', spread / meanR, 0.02, 0.5, '一定かどうか');
  chk('前置因子の 解析値', ratios[0], pref, 1e-3, 'exp(pi[2a sqrt(2V0) - sqrt(8V0a^2-1)])');
  line('★ 比は ' + ratios[0].toFixed(4) + ' 〜 ' + ratios[ratios.length - 1].toFixed(4)
    + ' で ほぼ 一定（相対ばらつき ' + (100 * spread / meanR).toFixed(1) + ' %）。');
  line('★★ 解析値 exp(pi[2a sqrt(2V0) - sqrt(8V0a^2-1)]) = ' + pref.toFixed(4)
    + ' と 一致。');
  line('★★★ つまり WKB の 誤差は「指数の 中」では なく「前の 定数」に ある。');
  line('   透過率が 8 桁 変わるあいだ、比は 1.20 のまま 動かない。');
  line('★ 第62回で「桁数は 当たる」と 言えたのは このため。');
  line('   逆に「前置因子まで 欲しい」なら WKB では 足りない。');
}

// ==================================================================
head(5, '★★ 障壁の 頭では e^-G が 壊れる ── ケンブルの形');
// ==================================================================
{
  const V0 = 1, a = 3;
  const LAM = 8 * V0 * a * a;
  const OMB = Math.sqrt(2 * V0) / a;            // 障壁頂上の 虚振動数
  const Texact = (E) => {
    const s = Math.sinh(Math.PI * Math.sqrt(2 * E) * a);
    const d = Math.cosh(0.5 * Math.PI * Math.sqrt(LAM - 1));
    return s * s / (s * s + d * d);
  };
  const Gpara = (E) => 2 * Math.PI * (V0 - E) / OMB;
  line('障壁の 頂上 付近。放物線近似 G = 2pi(V0-E)/(hbar omega_b)、omega_b = '
    + OMB.toFixed(5));
  line('');
  line(row(['E/V0', 'G', 'e^-G', '1/(1+e^G)', '厳密'], [10, 12, 14, 14, 14]));
  rule();
  for (const r of [0.9, 0.95, 1.0, 1.05, 1.2, 1.5]) {
    const E = r * V0, g = Gpara(E);
    line(row([r.toFixed(2), g.toFixed(4), Math.exp(-g).toExponential(3),
      (1 / (1 + Math.exp(g))).toFixed(6), Texact(E).toFixed(6)], [10, 12, 14, 14, 14]));
  }
  rule();
  chk('障壁の頭での ケンブル', 1 / (1 + 1), 0.5, 1e-12, '厳密に 1/2');
  chk('障壁の頭での 厳密解', Texact(V0), 0.5, 0.10, 'エッカートは 0.546');
  line('★★★ E = V0 で e^-G = 1（全部 通る）は 明らかに 間違い。');
  line('   厳密解は 0.546、ケンブルは 0.500。');
  line('★★ E > V0 では e^-G が 1 を 超えて 784 などに なる ── 確率が 1 を 超える。');
  line('★ ケンブル 1/(1+e^G) は どこでも 0〜1 に 収まり、');
  line('   放物線障壁なら 厳密解そのもの。');
  line('★★★ なぜ 頭で 壊れるか：二つの 転回点が 合体するから。');
  line('   第57回の「端」── 展開が 効く範囲の 外に 出ている。');
}

// ==================================================================
head(6, '★★★ アレニウスと ガモフは 同じ式 ── 境目は T_c = hbar w_b / 2pi k_B');
// ==================================================================
// 温度 T では、エネルギー E の 粒子が ボルツマン因子 exp(-E/kT) で いて、
// それぞれ 透過率 1/(1+e^G) で 抜ける。掛けて 足したものが 速さ。
//   Gamma(T) ∝ int dE exp(-E/kT) / (1 + e^{G(E)})
// 放物線障壁なら G = 2pi(V0-E)/(hbar w_b) なので、被積分関数は
//   exp( -E/kT - 2pi(V0-E)/(hbar w_b) )
// E の係数が 符号を 変える所が 境目：1/kT = 2pi/(hbar w_b)。

{
  const V0 = 1, a = 3, OMB = Math.sqrt(2 * V0) / a;
  const Tc = OMB / (2 * Math.PI);              // hbar = k_B = 1
  const Gpara = (E) => 2 * Math.PI * (V0 - E) / OMB;
  function rate(T) {
    const n = 200000, Emax = 4 * V0, h = Emax / n;
    let s = 0, num = 0;
    for (let i = 0; i < n; i++) {
      const E = h * (i + 0.5);
      const w = Math.exp(-E / T) / (1 + Math.exp(Gpara(E)));
      s += w * h; num += E * w * h;
    }
    return { G: s, Estar: num / s };
  }
  line('hbar = k_B = 1、V0 = 1、omega_b = ' + OMB.toFixed(5));
  line('交差温度 T_c = hbar omega_b / (2 pi k_B) = ' + Tc.toFixed(6));
  line('');
  line(row(['T/T_c', 'T', 'ln Gamma', '実効的な E*', '振る舞い'], [10, 12, 14, 14, 18]));
  rule();
  const pts = [];
  for (const r of [0.3, 0.5, 0.8, 1.0, 1.3, 2.0, 3.0, 5.0]) {
    const T = r * Tc, R = rate(T);
    pts.push([T, Math.log(R.G)]);
    let beh;
    if (r < 0.9) beh = 'トンネル（頭打ち）';
    else if (r < 1.2) beh = '★ 交差';
    else beh = 'アレニウス';
    line(row([r.toFixed(1), T.toFixed(5), Math.log(R.G).toFixed(4),
      R.Estar.toFixed(4), beh], [10, 12, 14, 14, 18]));
  }
  rule();
  // 実験で 測れるのは「見かけの 活性化エネルギー」
  //   E_eff(T) = -d(ln Gamma)/d(1/T)
  // 高温では V0 + kT（前置の kT のぶん）、低温では 0 に 近づくはず。
  function Eeff(T) {
    const d = 0.01 * T;
    const a1 = Math.log(rate(T - d).G), a2 = Math.log(rate(T + d).G);
    return -(a2 - a1) / (1 / (T + d) - 1 / (T - d));
  }
  line('');
  line('実験で 測れるのは 見かけの 活性化エネルギー E_eff = -d(lnGamma)/d(1/T)');
  line('');
  line(row(['T/T_c', 'E_eff', 'E_eff/V0', '高温の予言 V0+kT', '判定'],
    [10, 12, 12, 18, 16]));
  rule();
  for (const r of [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]) {
    const T = r * Tc, e = Eeff(T);
    line(row([r.toFixed(1), e.toFixed(4), (e / V0).toFixed(4),
      (V0 + T).toFixed(4), r < 1 ? 'トンネル' : (r < 1.5 ? '★ 交差' : 'アレニウス')],
      [10, 12, 12, 18, 16]));
  }
  rule();
  {
    const Thi = 5 * Tc, ehi = Eeff(Thi);
    chk('高温の E_eff（アレニウス）', ehi, V0 + Thi, 0.06, 'V0 + kT（前置の kT 込み）');
    line('★★ 高温側で E_eff → V0 + kT（前置因子 kT の ぶん 少し 超える）。');
    line('   T=5T_c で ' + ehi.toFixed(4) + '、予言 ' + (V0 + Thi).toFixed(4) + '。');
    line('   → Gamma ∝ kT exp(-V0/kT)。これが アレニウスの 式（第56回）。');
    const Tlo = 0.3 * Tc, elo = Eeff(Tlo);
    chk('低温の E_eff（頭打ち）', elo / V0, 0.05, 1.0, '真の障壁より ずっと 小さい');
    line('★★★ 低温側では E_eff = ' + elo.toFixed(4) + ' ── 真の障壁 V0=1 の '
      + (100 * elo / V0).toFixed(1) + ' % しかない。');
    line('   温度を 下げても 速さが 落ちなく なる ＝ トンネルが 効いている。');
    line('★★★ これが 実験での トンネルの 印：');
    line('   アレニウス図（ln Gamma 対 1/T）が 低温側で 寝る。');
    line('   見かけの 活性化エネルギーが 真の障壁より 小さく 出たら、');
    line('   その差は トンネルの ぶん。');
    line('★ 第56回で 金属中の U_e を 論じたが、同じ 測り方が ここにも 効く ──');
    line('   温度を 振って E_eff の 折れ曲がりを 見れば T_c が 出る。');
  }
  line('');
  line('★★★ アレニウス exp(-V0/kT) と ガモフ exp(-2pi V0/(hbar w_b)) は、');
  line('   同じ 積分の 高温極限と 低温極限。');
  line('★★ 境目は 二つの 指数が 等しく なる所：');
  line('   V0/(k T) = 2pi V0/(hbar w_b)  →  T_c = hbar w_b / (2 pi k_B)');
  line('★ 第56回で「温度を 変えるのが いちばん強い」と 書いたのは、');
  line('   T > T_c では 指数が 1/T で 効くから。T < T_c では 効かない。');
}

// ==================================================================
head(7, '★ その 2pi は どこから 来たか ── ウンルー温度と 同じもの');
// ==================================================================
line('虚時間 tau は 温度 T の 系では 周期 hbar/(k_B T) の 円 に なっている。');
line('  （これが 温度と 虚時間の 対応。第45回の ウンルー効果と 同じ枠組み）');
line('');
line('放物線の 頂上 付近での バウンスの 周期は 2pi/omega_b。');
line('  バウンスが 円に 収まる 条件： hbar/(k_B T) >= 2pi/omega_b');
line('  →  T <= hbar omega_b/(2 pi k_B) = T_c');
line('');
{
  // ウンルー温度 T = hbar a /(2 pi c k_B) と 同じ形か
  line(row(['場面', '式', '2pi の 出どころ'], [24, 30, 24]));
  rule();
  line(row(['交差温度（本回）', 'T_c = hbar w_b/(2pi k_B)', '虚時間の 円周'], [24, 30, 24]));
  line(row(['ウンルー（第45回）', 'T = hbar a/(2pi c k_B)', '虚時間の 円周'], [24, 30, 24]));
  line(row(['ホーキング', 'T = hbar kappa/(2pi c k_B)', '虚時間の 円周'], [24, 30, 24]));
  rule();
  line('★★ どれも「虚時間を 円にしたときの 一周」から 出る 2pi。');
  line('★★★ 第45回で「加速した人が 真空を 熱く見る」のと、');
  line('   本回で「ある温度から 上は 古典的に 越える」のは、');
  line('   同じ 虚時間の 幾何の 二つの 顔。');
  line('★ ただし 同じ形なのは 2pi の 出どころだけで、');
  line('   物理は 別（第63回の「同じ統計は 同じ物理ではない」と 同じ注意）。');
}

// ==================================================================
head(8, '★★★ 摂動論は e^{-S/hbar} を 知らない ── が、発散の速さが 知っている');
// ==================================================================
// 非調和振動子 H = p^2/2 + x^2/2 + g x^4。
// g < 0 に すると 準安定になり、崩壊率 ~ exp(-1/(3|g|))。
// バウンス作用 S = 1/(3|g|) を 03節の 積分で 確かめ、
// そのうえで 摂動級数 E(g) = sum a_n g^n の 大きい n での 振る舞いを 見る。
//   予言（Bender-Wu）： a_n ~ (-1)^{n+1} sqrt(6/pi^3) 3^n Gamma(n+1/2)
// 3 は 1/S に 対応する。つまり 発散の速さが 作用を 知っている。

{
  // (1) バウンス作用が 1/(3g) か
  const g = 0.05;
  const V = (x) => 0.5 * x * x - g * Math.pow(x, 4);
  const xt = 1 / Math.sqrt(2 * g);
  let s = 0; const n = 400000, h = xt / n;
  for (let i = 0; i < n; i++) {
    const x = h * (i + 0.5), dv = V(x);
    if (dv > 0) s += Math.sqrt(2 * dv);
  }
  const Sb = 2 * s * h;                        // 0 -> xt を 往復
  chk('バウンス作用 S = 1/(3g)', Sb, 1 / (3 * g), 1e-3, 'g=0.05');
  line('g = ' + g + ' の とき バウンス作用 S = ' + Sb.toFixed(6)
    + '（解析 1/(3g) = ' + (1 / (3 * g)).toFixed(6) + '）');
  line('');
}
{
  // (2) 摂動係数を 高次まで
  const N = 260, ORD = 40;
  const x = [];
  for (let i = 0; i < N; i++) x.push(new Float64Array(N));
  for (let k = 0; k + 1 < N; k++) {
    const v = Math.sqrt((k + 1) / 2); x[k][k + 1] = v; x[k + 1][k] = v;
  }
  function mul(A, B) {
    const C = []; for (let i = 0; i < N; i++) C.push(new Float64Array(N));
    for (let i = 0; i < N; i++) for (let k = 0; k < N; k++) {
      const av = A[i][k]; if (av === 0) continue;
      for (let j = 0; j < N; j++) C[i][j] += av * B[k][j];
    }
    return C;
  }
  const x2 = mul(x, x), V4 = mul(x2, x2);
  const E0 = 0.5, psis = [new Float64Array(N)], Es = [E0];
  psis[0][0] = 1;
  for (let k = 1; k <= ORD; k++) {
    const w = new Float64Array(N), prev = psis[k - 1];
    for (let i = 0; i < N; i++) {
      let sv = 0;
      for (let j = 0; j < N; j++) sv += V4[i][j] * prev[j];
      w[i] = sv;
    }
    for (let j = 1; j <= k - 1; j++) {
      const c = Es[j], p = psis[k - j];
      for (let i = 0; i < N; i++) w[i] -= c * p[i];
    }
    Es.push(w[0]);
    const nx = new Float64Array(N);
    for (let mm = 1; mm < N; mm++) nx[mm] = w[mm] / (E0 - (mm + 0.5));
    psis.push(nx);
  }
  line('摂動級数 E(g) = sum a_n g^n の 係数（調和振動子基底 260、40 次まで）');
  line('  a_0..a_4 = ' + Es.slice(0, 5).map((v) => v.toPrecision(9)).join(', '));
  line('  既知      = 0.5, 0.75, -2.625, 20.8125, -241.2890625');
  chk('a_2（既知値）', Es[2], -2.625, 1e-9, 'Bender-Wu');
  chk('a_4（既知値）', Es[4], -241.2890625, 1e-9, 'Bender-Wu');
  line('');
  line(row(['n', 'a_n', 'a_n/a_{n-1}', '比/(-3)', '予言 n-1/2'], [6, 18, 16, 12, 14]));
  rule();
  for (const n of [2, 5, 10, 20, 30, 40]) {
    const r = Es[n] / Es[n - 1];
    line(row([n, Es[n].toExponential(4), r.toFixed(4), (r / -3).toFixed(4),
      (n - 0.5).toFixed(1)], [6, 18, 16, 12, 14]));
  }
  rule();
  const rl = Es[40] / Es[39] / -3;
  chk('大きい n での 比/(-3)', rl, 39.5, 2e-3, '予言 n - 1/2');
  line('★★★ a_n/a_{n-1} = -3(n - 1/2) に 収束する。');
  line('   n=40 で ' + rl.toFixed(4) + '（予言 39.5）。');
  line('★★ 級数は 収束しない（n! で 発散する）── 摂動論は g の 冪では');
  line('   exp(-1/(3g)) を 決して 作れない。すべての 次数で 0 だから。');
  line('★★★ ところが 発散の 速さ 3^n の 3 が、バウンス作用 S = 1/(3g) の');
  line('   1/S に 一致する。');
  line('★ 「摂動論は トンネルを 知らない」が、「発散の 仕方が 知っている」。');
  line('   ── ダイソンの 議論（1952）の 定量版。');
  line('★★ これが、あの積分に 名前が 六つ ついた いちばんの 理由：');
  line('   摂動論の 外に ある ものを 数える 道具 だから。');
}

// ==================================================================
head(9, '検算のまとめ');
// ==================================================================
line(row(['項目', '計算', '参照', '判定'], [36, 16, 16, 8]));
rule();
let bad = 0;
for (const c of CHECKS) {
  if (!c[3]) bad++;
  const f = (v) => (typeof v === 'number')
    ? (Math.abs(v) !== 0 && (Math.abs(v) < 1e-3 || Math.abs(v) > 1e5)
      ? v.toExponential(2) : v.toFixed(5)) : v;
  line(row([c[0], f(c[1]), f(c[2]), c[3] ? 'OK' : 'NG'], [36, 16, 16, 8]));
}
rule();
line(bad === 0 ? '★ 全 ' + CHECKS.length + ' 件 合格。'
  : '★ ' + CHECKS.length + ' 件 中 ' + bad + ' 件 不一致。');
line('');
line('★★★ あの式の 正体は「虚時間における 古典軌道の 作用」。');
line('    G = 2 S_E / hbar。名前は 六つ、いちばん 深いのは インスタントン。');
line('★★★ そして 摂動論の 発散の 速さが、その 作用を 知っている。');
line('');
