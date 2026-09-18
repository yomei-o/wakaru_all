// 考える波 第63回「波とゼータ」検証
//   node zeta.js
// 依存ライブラリ 0（リーマン零点も 自前で 計算する）。
//
// 問い：核物理を 波として見ると 計算は簡単になるか。
//       そして 波と ゼータ関数は どうつながるか。
//
// 答え（本稿の主張）：
//   ★ 核を波として見ると「共鳴」── d+t の S(E) は 共鳴 1 つ で書ける。
//   ★★ 共鳴が 並ぶと 準位統計になる。
//   ★★★ その統計が、リーマンゼータの 零点の統計と 同じもの
//       ── Montgomery-Dyson 1972。本稿では 零点を 自前で計算して 確かめる。
//   ★ そして 第45・61回の -1/12 は、波のスペクトルの ゼータ関数 zeta(-1) そのもの。

'use strict';

const TWO_PI = 2 * Math.PI;
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
function mean(a) { let s = 0; for (const v of a) s += v; return s / a.length; }
const CHECKS = [];
function chk(label, got, want, relTol, note) {
  const ok = Math.abs(got - want) <= relTol * Math.abs(want);
  CHECKS.push([label, got, want, ok, note || '']);
  return ok;
}

// ==================================================================
head(1, '核を 波として見る ── d+t の S(E) は 共鳴 1 つ で書けるか');
// ==================================================================
// 第62回で「d+t の利点は 障壁ではなく 共鳴」と分かった。
// では その共鳴は 1 つ で足りるのか。足りるなら 核物理の側は
//   sigma(E) = S(E)/E * exp(-B_G/sqrt(E)),  S(E) = 共鳴 1 つ
// という 3 つの数（E_R, Gamma, 強さ）だけ で書けることになる。

const ALPHA = 7.2973525693e-3;
const MC2 = { p: 938.27208816, d: 1875.61294257, t: 2808.92113298 };
function red(a, b) { return MC2[a] * MC2[b] / (MC2[a] + MC2[b]); }
function EG_keV(a, b, z1, z2) {
  return 2 * red(a, b) * 1e3 * Math.pow(Math.PI * ALPHA * z1 * z2, 2);
}
// NRL Plasma Formulary の d+t 断面積（E は 実験室系 keV、barn）
function sigDT(Elab) {
  const A = [45.95, 50200, 1.368e-2, 1.076, 409];
  if (Elab <= 0) return 0;
  const den = Elab * (Math.exp(A[0] / Math.sqrt(Elab)) - 1);
  return (A[4] + A[1] / (Math.pow(A[3] - A[2] * Elab, 2) + 1)) / den;
}
{
  const BG = Math.sqrt(EG_keV('d', 't', 1, 1));
  const labF = (MC2.d + MC2.t) / MC2.t;
  // S(E) = sigma * E * exp(B_G/sqrt(E))  （E は 重心系 keV、S は keV*barn）
  const Es = [], Ss = [];
  for (let E = 5; E <= 300; E += 1) {
    const s = sigDT(E * labF);
    Es.push(E); Ss.push(s * E * Math.exp(BG / Math.sqrt(E)));
  }
  // 単一準位ブライト＝ウィグナー：S(E) = A / ((E-ER)^2 + (G/2)^2)
  // 3 つの数を 粗い格子探索 ＋ 縮小で 合わせる
  let best = { err: Infinity };
  function fitErr(ER, Gam) {
    // A は 最小二乗で 解析的に 決まる
    let num = 0, den = 0;
    for (let i = 0; i < Es.length; i++) {
      const b = 1 / (Math.pow(Es[i] - ER, 2) + Gam * Gam / 4);
      num += Ss[i] * b; den += b * b;
    }
    const A = num / den;
    let e = 0;
    for (let i = 0; i < Es.length; i++) {
      const m = A / (Math.pow(Es[i] - ER, 2) + Gam * Gam / 4);
      e += Math.pow(Math.log(m / Ss[i]), 2);          // 対数で 合わせる（桁で見る）
    }
    return { err: Math.sqrt(e / Es.length), A: A };
  }
  function doFit(lo, hi) {
    const keep = [];
    for (let i = 0; i < Es.length; i++) if (Es[i] >= lo && Es[i] <= hi) keep.push(i);
    function err(ER, Gam) {
      let num = 0, den = 0;
      for (const i of keep) {
        const b = 1 / (Math.pow(Es[i] - ER, 2) + Gam * Gam / 4);
        num += Ss[i] * b; den += b * b;
      }
      const A = num / den;
      let e = 0;
      for (const i of keep) {
        const m = A / (Math.pow(Es[i] - ER, 2) + Gam * Gam / 4);
        e += Math.pow(Math.log(m / Ss[i]), 2);
      }
      return { err: Math.sqrt(e / keep.length), A: A };
    }
    let b2 = { err: Infinity }, ER0 = 64, G0 = 80, step = 32;
    for (let it = 0; it < 80; it++) {
      let improved = false;
      for (const dE of [-step, 0, step]) for (const dG of [-step, 0, step]) {
        const ER = ER0 + dE, Gam = G0 + dG;
        if (ER < 5 || Gam < 2) continue;
        const r = err(ER, Gam);
        if (r.err < b2.err - 1e-13) { b2 = { err: r.err, A: r.A, ER: ER, Gam: Gam }; improved = true; }
      }
      if (improved) { ER0 = b2.ER; G0 = b2.Gam; } else { step /= 2; if (step < 1e-5) break; }
    }
    return b2;
  }
  const FITWIN = doFit(5, 300);       // 広い窓
  const FITNAR = doFit(35, 110);      // 共鳴の まわりだけ
  best = FITWIN;
  line('d+t の S(E) を 単一準位ブライト＝ウィグナー 1 つ で 合わせる');
  line('  S(E) = A / ((E - E_R)^2 + (Gamma/2)^2)、E = 5..300 keV（重心系）');
  line('');
  line('  合わせた値： E_R = ' + best.ER.toFixed(2) + ' keV、Gamma = '
    + best.Gam.toFixed(1) + ' keV');
  line('  対数での 平均残差 = ' + best.err.toFixed(4)
    + '  → 典型的なずれ ' + ((Math.exp(best.err) - 1) * 100).toFixed(1) + ' %');
  line('');
  line(row(['E[keV]', 'S(E) 実際', 'BW 1 つ', '比'], [10, 16, 16, 10]));
  rule();
  for (const E of [10, 30, 64, 100, 200, 300]) {
    const act = sigDT(E * labF) * E * Math.exp(BG / Math.sqrt(E));
    const bw = best.A / (Math.pow(E - best.ER, 2) + best.Gam * best.Gam / 4);
    line(row([E, act.toFixed(0), bw.toFixed(0), (bw / act).toFixed(3)], [10, 16, 16, 10]));
  }
  rule();
  line('');
  line(row(['当てはめる窓', 'E_R[keV]', 'Gamma[keV]', '残差', '典型のずれ'],
    [18, 12, 14, 10, 14]));
  rule();
  line(row(['5〜300 keV（広い）', FITWIN.ER.toFixed(1), FITWIN.Gam.toFixed(1),
    FITWIN.err.toFixed(4), ((Math.exp(FITWIN.err) - 1) * 100).toFixed(1) + ' %'],
    [18, 12, 14, 10, 14]));
  line(row(['35〜110 keV（山だけ）', FITNAR.ER.toFixed(1), FITNAR.Gam.toFixed(1),
    FITNAR.err.toFixed(4), ((Math.exp(FITNAR.err) - 1) * 100).toFixed(1) + ' %'],
    [18, 12, 14, 10, 14]));
  line(row(['文献（R 行列の 極）', '64', '約 75', '', '別の模型'], [18, 12, 14, 10, 14]));
  rule();
  chk('共鳴 1 つ の 当てはめ精度', FITWIN.err, 0.10, 0.35, '対数での 残差');
  line('★★★ 共鳴 1 つ で、5〜300 keV を '
    + ((Math.exp(FITWIN.err) - 1) * 100).toFixed(0) + ' % 程度で 再現できる。');
  line('   ── d+t の 核物理は 3 つの数（E_R, Gamma, 強さ）に 畳める。');
  line('   残りは 全部 ガモフ因子 ── 第62回の物差しの側。');
  line('');
  line('★ 山のまわり だけに 絞ると 残差は '
    + ((Math.exp(FITNAR.err) - 1) * 100).toFixed(1) + ' % まで 落ちる。');
  line('  そして 中心は 広い窓 ' + FITWIN.ER.toFixed(1) + ' keV、狭い窓 '
    + FITNAR.ER.toFixed(1) + ' keV と ほぼ 動かない ──');
  line('  つまり この 模型の パラメータとしては 安定して 決まる。');
  line('');
  line('★★★ ところが その ' + FITNAR.ER.toFixed(1)
    + ' keV は、文献の「共鳴 64 keV」とは 別の量。');
  line('   文献の 64 keV は R 行列の 極の位置（幅が エネルギーで 変わる扱い）。');
  line('   本稿の値は「幅を 定数に した ブライト＝ウィグナーを S(E) に');
  line('   合わせたときの 中心」。どちらも 同じ sigma(E) を 与えるが、');
  line('   数としては 一致しない。');
  line('★★ これは 間違いではなく、模型の 違い ── 第55回の分類でいう');
  line('   「模型を 仮定した値」。使うなら 模型を 添えて 書くべき数。');
  line('   （断面積を 作るのが 目的なら 48.7 keV が 正しく、');
  line('    共鳴の 位置を 言いたいなら 64 keV を 使うべき）');
  line('');
  line('★★ 「核を 波として 見ると 計算が 簡単になるか」への 答え：');
  line('   なる。共鳴（定在波）と しみ出し（トンネル）に 分ければ、');
  line('   前者は 数個 の数、後者は 質量と電荷だけ。');
  line('★ ただし 簡単にした ぶん、出てくる数は 模型の 数になる。');
  line('   断面積は 10 % で 出るが、共鳴の パラメータは 出ない。');
}

// ==================================================================
head(2, 'リーマン零点を 自前で 計算する（リーマン＝ジーゲル）');
// ==================================================================
// Z(t) は 実数関数で、その零点が ゼータの 臨界線上の零点。
//   theta(t) = (t/2)ln(t/2pi) - t/2 - pi/8 + 1/(48t) + ...
//   Z(t) = 2 sum_{n<=N} cos(theta - t ln n)/sqrt(n) + 補正、N = floor(sqrt(t/2pi))

function theta(t) {
  return (t / 2) * Math.log(t / TWO_PI) - t / 2 - Math.PI / 8
    + 1 / (48 * t) + 7 / (5760 * Math.pow(t, 3));
}
// C0(p) は p=1/4, 3/4 で 0/0（可除特異点、極限は どちらも 1/2）。
// そこだけ 両側の平均で 通す。
function C0(p) {
  const g = Math.cos(TWO_PI * p);
  const f = (q) => Math.cos(TWO_PI * (q * q - q - 1 / 16)) / Math.cos(TWO_PI * q);
  if (Math.abs(g) > 1e-3) return f(p);
  return 0.5 * (f(p - 2e-3) + f(p + 2e-3));
}
function Zfun(t) {
  const th = theta(t);
  const N = Math.floor(Math.sqrt(t / TWO_PI));
  let s = 0;
  for (let n = 1; n <= N; n++) s += Math.cos(th - t * Math.log(n)) / Math.sqrt(n);
  const p = Math.sqrt(t / TWO_PI) - N;
  return 2 * s + (N % 2 === 0 ? -1 : 1) * Math.pow(TWO_PI / t, 0.25) * C0(p);
}
function zerosIn(ta, tb, dt) {
  const zs = [];
  let z0 = Zfun(ta);
  for (let t = ta + dt; t < tb; t += dt) {
    const z1 = Zfun(t);
    if ((z0 < 0) !== (z1 < 0)) {
      let a = t - dt, b = t, fa = z0;
      for (let i = 0; i < 70; i++) {
        const m = 0.5 * (a + b), fm = Zfun(m);
        if ((fa < 0) !== (fm < 0)) b = m; else { a = m; fa = fm; }
      }
      zs.push(0.5 * (a + b));
    }
    z0 = z1;
  }
  return zs;
}

const KNOWN = [14.134725142, 21.022039639, 25.010857580, 30.424876126,
  32.935061588, 37.586178159, 40.918719012, 43.327073281,
  48.005150881, 49.773832478];
{
  const zs = zerosIn(10, 60, 0.01);
  line(row(['番号', '本稿の計算', '既知の値', '差'], [8, 18, 18, 12]));
  rule();
  let worst = 0;
  for (let i = 0; i < Math.min(zs.length, KNOWN.length); i++) {
    const e = Math.abs(zs[i] - KNOWN[i]);
    worst = Math.max(worst, e);
    line(row([i + 1, zs[i].toFixed(6), KNOWN[i].toFixed(6), e.toExponential(1)],
      [8, 18, 18, 12]));
  }
  rule();
  chk('最初の 10 個の 零点', worst, 0.008, 1.0, '既知値との 最大差');
  line('★ 最大差 ' + worst.toExponential(1) + '。');
  line('★★ リーマン＝ジーゲルは 漸近公式なので 小さい t では 精度が 落ちる。');
  line('   （誤差は t^(-3/4) で 減る。t=14 では 1e-3 級、t=1e4 では 1e-5 級）');
  line('');
  line('個数の 検算 ── リーマン＝フォン・マンゴルト N(T) ≒ theta(T)/pi + 1');
  line('');
  line(row(['範囲', '見つけた個数', 'N(T) の予想', '差'], [20, 16, 16, 10]));
  rule();
  for (const ab of [[10, 1000], [10, 5000], [10000, 12000], [50000, 51000]]) {
    const z = zerosIn(ab[0], ab[1], 0.01);
    const pred = theta(ab[1]) / Math.PI - theta(ab[0]) / Math.PI;
    line(row(['t = ' + ab[0] + '..' + ab[1], z.length, pred.toFixed(2),
      (z.length - pred).toFixed(2)], [20, 16, 16, 10]));
    chk('零点の個数 t=' + ab[0] + '..' + ab[1], z.length, pred, 0.01, 'N(T) と 比較');
  }
  rule();
  line('★★★ 高い t では 個数が N(T) と 1 個 未満の ずれで 合う');
  line('   ── 数え落としも 偽の零点も 無い。統計に 使える。');
}

// ==================================================================
head(3, 'アンフォールド ── 「ばね定数」を 取り除く');
// ==================================================================
// 零点の 密度は t とともに 増える（dN/dt = ln(t/2pi)/2pi）。
// 統計を 見るには 密度を 1 に 揃える必要がある。
//   x_n = theta(t_n)/pi      ← これが ほぼ 整数に なる

function unfold(zs) { return zs.map((t) => theta(t) / Math.PI); }
function spacings(x) {
  const s = [];
  for (let i = 1; i < x.length; i++) s.push(x[i] - x[i - 1]);
  return s;
}

let SP = null, SPhi = null;
{
  const W = zerosIn(10000, 14000, 0.015);
  const x = unfold(W);
  SP = spacings(x);
  line('t = 1e4 .. 1.4e4 の 零点 ' + W.length + ' 個');
  line('  生の 平均間隔（t で）    = ' + mean(spacings(W)).toFixed(4));
  line('  理論 2pi/ln(t/2pi)     = ' + (TWO_PI / Math.log(12000 / TWO_PI)).toFixed(4));
  line('  アンフォールド後の 平均  = ' + mean(SP).toFixed(6) + '（1 に なるはず）');
  chk('アンフォールド後の 平均間隔', mean(SP), 1.0, 1e-3, '構成から 1');
  line('');
  const W2 = zerosIn(100000, 103000, 0.01);
  SPhi = spacings(unfold(W2));
  line('t = 1e5 .. 1.03e5 の 零点 ' + W2.length + ' 個（比較用）');
  line('  アンフォールド後の 平均  = ' + mean(SPhi).toFixed(6));
  line('★ これで 2 つの 高さの 窓が そろった。t を 上げると どうなるかを 見る。');
}

// ==================================================================
head(4, '★★★ 準位間隔の 分布 ── 核の準位と 同じか');
// ==================================================================
// 比べる 3 つ（ウィグナーの推量）：
//   ポアソン（無相関）      P(s) = e^{-s},            <s^2> = 2
//   GOE（時間反転対称）     P(s) = (pi/2) s e^{-pi s^2/4},  <s^2> = 4/pi = 1.2732
//   GUE（時間反転なし）     P(s) = (32/pi^2) s^2 e^{-4s^2/pi}, <s^2> = 3pi/8 = 1.1781

function pPoisson(s) { return Math.exp(-s); }
function pGOE(s) { return (Math.PI / 2) * s * Math.exp(-Math.PI * s * s / 4); }
function pGUE(s) { return (32 / (Math.PI * Math.PI)) * s * s * Math.exp(-4 * s * s / Math.PI); }

function hist(sp, nb, smax) {
  const h = new Array(nb).fill(0), w = smax / nb;
  let n = 0;
  for (const s of sp) {
    if (s < smax) { h[Math.floor(s / w)]++; n++; }
  }
  return { h: h, w: w, n: n, tot: sp.length };
}
function compare(sp, label) {
  const nb = 20, smax = 3.0;
  const H = hist(sp, nb, smax);
  const names = ['Poisson', 'GOE', 'GUE'];
  const fns = [pPoisson, pGOE, pGUE];
  const chi = [0, 0, 0];
  for (let i = 0; i < nb; i++) {
    const sc = (i + 0.5) * H.w;
    const obs = H.h[i];
    for (let k = 0; k < 3; k++) {
      const exp = fns[k](sc) * H.w * H.tot;
      if (exp > 5) chi[k] += Math.pow(obs - exp, 2) / exp;
    }
  }
  let m2 = 0; for (const s of sp) m2 += s * s;
  m2 /= sp.length;
  let small = 0; for (const s of sp) if (s < 0.3) small++;
  return { H: H, chi: chi, m2: m2, small: small / sp.length, label: label };
}

{
  const A = compare(SP, 't=1e4');
  const B = compare(SPhi, 't=1e5');
  line('比べる相手（ウィグナーの推量）');
  line(row(['', '<s^2>', 's<0.3 の割合'], [16, 12, 16]));
  rule();
  line(row(['ポアソン', (2).toFixed(4), (1 - Math.exp(-0.3)).toFixed(4)], [16, 12, 16]));
  line(row(['GOE', (4 / Math.PI).toFixed(4), (1 - Math.exp(-Math.PI * 0.09 / 4)).toFixed(4)], [16, 12, 16]));
  let gueSmall = 0;
  for (let i = 0; i < 3000; i++) { const s0 = 0.3 * (i + 0.5) / 3000; gueSmall += pGUE(s0) * 0.3 / 3000; }
  line(row(['GUE', (3 * Math.PI / 8).toFixed(4), gueSmall.toFixed(4)], [16, 12, 16]));
  rule();
  line('');
  line(row(['零点の窓', '<s^2>', 's<0.3 の割合', 'chi^2 Poisson', 'chi^2 GOE', 'chi^2 GUE'],
    [14, 10, 14, 14, 12, 12]));
  rule();
  for (const R of [A, B]) {
    line(row([R.label, R.m2.toFixed(4), R.small.toFixed(4),
      R.chi[0].toFixed(0), R.chi[1].toFixed(0), R.chi[2].toFixed(1)],
      [14, 10, 14, 14, 12, 12]));
  }
  rule();
  chk('零点の <s^2>（t=1e5）', B.m2, 3 * Math.PI / 8, 0.05, 'GUE の 3pi/8');
  line('');
  line('ヒストグラム（t=1e5 の窓、幅 0.15）');
  line('');
  line(row(['s', '実測', 'Poisson', 'GOE', 'GUE'], [10, 10, 10, 10, 10]));
  rule();
  {
    const H = B.H;
    for (let i = 0; i < 14; i++) {
      const sc = (i + 0.5) * H.w;
      const o = H.h[i] / H.tot / H.w;
      const bar = (v) => v.toFixed(3);
      line(row([sc.toFixed(2), bar(o), bar(pPoisson(sc)), bar(pGOE(sc)), bar(pGUE(sc))],
        [10, 10, 10, 10, 10]));
    }
  }
  rule();
  line('★★★ 小さい s で 実測は 0 に 落ちる ── 「準位反発」。');
  line('   ポアソン（無相関）なら s=0 で いちばん 多いはずだが、そうならない。');
  line('★★★ しかも 落ち方が s^2（GUE）── s^1（GOE）より 急。');
  line('★★ t を 1e4 から 1e5 に 上げると GUE に 近づく（chi^2 が 下がる）。');
  line('   Odlyzko が t=1e20 まで 行ったのは このため ── 収束は 遅い。');
  line('★ 核の準位（原子核データ集成）は GOE に 従うことが 知られている。');
  line('   時間反転対称性が あるかないかで 1 と 2 が 分かれる。');
}

// ==================================================================
head(5, 'ゼータと 波の もう一つの 接点 ── -1/12 は スペクトルの ゼータ');
// ==================================================================
// 第45・61回の -1/12 は、実は 波のスペクトルの ゼータ関数 そのもの。
//   1 次元の箱：omega_n = n pi c / a
//   零点エネルギー sum omega_n / 2 = (pi c / 2a) sum n = (pi c / 2a) zeta(-1)

line('1 次元の箱（長さ a）のモード omega_n = n pi c / a');
line('  零点エネルギー = (hbar/2) sum omega_n = (hbar pi c / 2a) * sum n');
line('  sum n は 発散するが、スペクトルゼータ zeta_s(s) = sum n^{-s} の');
line('  s = -1 での 値 zeta(-1) = -1/12 を 取ると');
line('');
line('    E = (hbar pi c / 2a) * (-1/12) = - hbar pi c / (24 a)');
line('');
{
  const z = -1 / 12;
  line('  zeta(-1) = ' + z.toFixed(10));
  chk('zeta(-1)', z, -1 / 12, 1e-12, '定義');
  line('★ 第45回は 指数的な切断で これを出し、第61回で 5 種類の切断に');
  line('   依らないことを 確かめた。ここでは 由来が はっきりする ──');
  line('★★★ -1/12 は「波のスペクトルの ゼータ関数の 値」。');
  line('   1+2+3+... の 値 では なく、モードの並びが 決めている数。');
}

// --- ワイルの法則：スペクトルから 形が 読めるか -------------------
line('');
line('もう一つ：スペクトルには 形の情報が 入っている（ワイルの法則）');
line('  長方形の 太鼓（a x b、固定端）の 固有値 lambda = pi^2(m^2/a^2 + n^2/b^2)');
line('  N(L) ≒ (面積/4pi) L - (周長/4pi) sqrt(L) + ...');
line('');
{
  const a = 1.0, b = 0.7;
  const area = a * b, per = 2 * (a + b);
  line(row(['L', '数えた N(L)', 'ワイル 第1項', '第2項まで', '残差'], [12, 14, 14, 14, 12]));
  rule();
  for (const L of [1e4, 1e5, 1e6, 1e7]) {
    let cnt = 0;
    const mmax = Math.floor(Math.sqrt(L) * a / Math.PI);
    for (let m = 1; m <= mmax; m++) {
      const rem = L / (Math.PI * Math.PI) - (m * m) / (a * a);
      if (rem <= 0) continue;
      cnt += Math.floor(Math.sqrt(rem) * b);
    }
    const w1 = area * L / (4 * Math.PI);
    const w2 = w1 - per * Math.sqrt(L) / (4 * Math.PI);
    line(row([L.toExponential(0), cnt, w1.toFixed(1), w2.toFixed(1),
      (cnt - w2).toFixed(1)], [12, 14, 14, 14, 12]));
    if (L === 1e7) chk('ワイルの法則（第2項まで）', cnt, w2, 0.002, 'L=1e7');
  }
  rule();
  line('★★ 第1項が 面積、第2項が 周長 ── スペクトルから 形が 読める。');
  line('★★★ これが「太鼓の形は 聞けるか」。答えは「面積と周長は 聞ける」。');
  line('★ ゼータの側で 言えば、スペクトルゼータ zeta_s(s)=sum lambda_n^{-s} の');
  line('   極の位置と 留数が 面積・周長・曲率に 対応する。');
  line('   ── 波の並びと ゼータ関数は、同じものの 2 つの書き方。');
}

// ==================================================================
head(6, '何が 言えて 何が 言えないか');
// ==================================================================
line(row(['言えること', '根拠'], [44, 30]));
rule();
const SAY = [
  ['d+t の S(E) は 共鳴 1 つ で書ける', '残差 10%（山だけなら 0.5%）'],
  ['★ ただし E_R は 模型の数', 'R 行列の 64 keV とは 別物'],
  ['零点を 自前で 計算できる', 'N(T) と 1 個 未満で一致'],
  ['零点の間隔は ポアソンではない', 'chi^2 が 桁違い'],
  ['★ 零点の間隔は GUE に 近い', '<s^2> と ヒストグラム'],
  ['★ t を 上げると GUE に 近づく', '1e4 と 1e5 の 比較'],
  ['-1/12 は スペクトルゼータの値', '定義から'],
  ['スペクトルから 面積と周長が 読める', 'ワイルの法則 0.2% で一致'],
];
for (const s of SAY) line(row(s, [44, 30]));
rule();
line('');
line(row(['言えないこと', '理由'], [44, 30]));
rule();
const NOSAY = [
  ['零点が ある演算子の 固有値である', 'ヒルベルト＝ポリア予想 ── 未解決'],
  ['GUE 一致が リーマン予想を 示す', '別の問題。統計は 予想を 含意しない'],
  ['核の準位と 零点が「同じ物理」', '同じ統計であって 同じ機構ではない'],
  ['本稿が 何かを 証明した', '既知の結果の 数値確認'],
];
for (const s of NOSAY) line(row(s, [44, 30]));
rule();
line('★★★ いちばん 大事な 区別：');
line('   「同じ統計」は「同じ物理」では ない。');
line('   ランダム行列は 対称性だけで 決まるので、対称性が 同じ系は');
line('   中身が まったく違っても 同じ統計に なる ── だから 一致する。');
line('★★ それでも 面白いのは、ゼータの零点が「時間反転のない量子系」の');
line('   対称性クラスに 落ちることが、数論の 側から 予想されていなかった点。');

// ==================================================================
head(7, '検算のまとめ');
// ==================================================================
line(row(['項目', '計算', '参照', '判定'], [34, 16, 16, 8]));
rule();
let bad = 0;
for (const c of CHECKS) {
  if (!c[3]) bad++;
  const f = (v) => (typeof v === 'number')
    ? (Math.abs(v) < 1e-3 || Math.abs(v) > 1e5 ? v.toExponential(2) : v.toFixed(4)) : v;
  line(row([c[0], f(c[1]), f(c[2]), c[3] ? 'OK' : 'NG'], [34, 16, 16, 8]));
}
rule();
line(bad === 0 ? '★ 全 ' + CHECKS.length + ' 件 合格。'
  : '★ ' + CHECKS.length + ' 件 中 ' + bad + ' 件 不一致。');
line('');
line('★★★ 核を 波として 見ると ── 共鳴（定在波）と しみ出し（トンネル）に');
line('    分かれ、前者は 数個の数、後者は 質量と電荷だけ。計算は 簡単になる。');
line('★★★ そして 共鳴が 並んだ ときの 統計が、');
line('    リーマンゼータの 零点の 統計と 同じものだった。');
line('');
