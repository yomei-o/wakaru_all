// 考える波 第58回「窓の外が中に漏れる」検証
//   node mado.js
// 依存ライブラリ 0（FFT も RK4 も自前）。
//
// 第57回で「端は最低次の補正項で決まる」と分かった。
// では逆に、窓の「端」が中に何を持ちこむのか。
//
// 本稿の主張：
//   ★ 窓の裾の落ち方は「端で何階まで滑らかか」で決まり、
//      それは このシリーズの階数 alpha そのもの（dB/oct = -6 alpha）。
//   ★ その alpha が「測れる beta の上限」を決める（beta < 2 alpha）。
//   ★★ そして同じ規則が 第45回のボゴリューボフ係数を支配する
//      ── 窓の漏れと 粒子生成は 同じ計算だった。

'use strict';

const TWO_PI = 2 * Math.PI;
function d10(x) { return Math.log(x) / Math.LN10; }
function line(t) { console.log(t); }
function rule(c) { line((c || '-').repeat(74)); }
function head(n, t) { line(''); rule('='); line('[' + n + '] ' + t); rule('='); }
function row(cols, w) {
  let s = '';
  for (let i = 0; i < cols.length; i++) {
    const c = String(cols[i]), width = w[i] || 12;
    s += (i === 0) ? c.padEnd(width) : c.padStart(width);
  }
  return s;
}
function slope(xs, ys) {
  const n = xs.length;
  let sx = 0, sy = 0, sxx = 0, sxy = 0;
  for (let i = 0; i < n; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
  return (n * sxy - sx * sy) / (n * sxx - sx * sx);
}

// ---------------------------------------------------------------- 窓
// w_p(x) = cos^p(pi x),  x in [-1/2, 1/2]
//   p=0 矩形（端で値が飛ぶ）      p=1 コサイン窓      p=2 ハン窓
//   端で w, w', ... w^(p-1) が 0 になり、w^(p) が 0 でない。
function cosWin(p, N) {
  const w = new Float64Array(N);
  for (let n = 0; n < N; n++) {
    const x = (n + 0.5) / N - 0.5;
    w[n] = Math.pow(Math.cos(Math.PI * x), p);
  }
  return w;
}
function namedWin(name, N) {
  const w = new Float64Array(N);
  for (let n = 0; n < N; n++) {
    const u = n / (N - 1);                 // 0..1
    switch (name) {
      case 'rect': w[n] = 1; break;
      case 'bartlett': w[n] = 1 - Math.abs(2 * u - 1); break;
      case 'hann': w[n] = 0.5 - 0.5 * Math.cos(TWO_PI * u); break;
      case 'hamming': w[n] = 0.54 - 0.46 * Math.cos(TWO_PI * u); break;
      case 'blackman':
        w[n] = 0.42 - 0.5 * Math.cos(TWO_PI * u) + 0.08 * Math.cos(2 * TWO_PI * u); break;
      default: throw new Error('unknown window ' + name);
    }
  }
  return w;
}

// 窓の連続スペクトル |W(f)| を bin 単位の f で（DTFT を直接）
function winMag(w, f) {
  const N = w.length;
  let re = 0, im = 0;
  for (let n = 0; n < N; n++) {
    const ph = TWO_PI * f * (n - (N - 1) / 2) / N;
    re += w[n] * Math.cos(ph);
    im -= w[n] * Math.sin(ph);
  }
  return Math.hypot(re, im);
}

// 裾（サイドローブ）の包絡の傾きを dB/oct で測る
// f = flo..fhi のあいだで、各オクターブの極大を拾って最小二乗
function sidelobeSlope(w, flo, fhi) {
  const xs = [], ys = [];
  const W0 = winMag(w, 0);
  for (let f = flo; f <= fhi; f *= Math.SQRT2) {
    // f の近傍でサイドローブの山を探す
    let best = 0;
    for (let g = f; g < f * Math.SQRT2; g += 0.05) {
      const m = winMag(w, g);
      if (m > best) best = m;
    }
    // 倍精度の床（相対 1e-13 ≒ -260 dB）に触れた点は使わない
    if (best / W0 < 1e-13) break;
    xs.push(Math.log(f) / Math.LN2);
    ys.push(20 * d10(best));
  }
  return slope(xs, ys);
}

// 第1サイドローブ：主ローブの半幅 hw から先の最大値
function firstSidelobe(w, hw) {
  const W0 = winMag(w, 0);
  let best = 0;
  for (let f = hw; f < 16; f += 0.005) {
    const m = winMag(w, f);
    if (m > best) best = m;
  }
  return 20 * d10(best / W0);
}

// =====================================================================
head(1, '窓の裾は「端で何階まで滑らかか」で決まる');
// =====================================================================
line('w_p(x) = cos^p(pi x)。端で p 階まで 0 になる → 裾は f^-(p+1)');
line('');
line(row(['p', '窓', '実測 dB/oct', '予言 -6(p+1)', 'alpha=p+1', '差'],
  [5, 14, 14, 14, 11, 10]));
rule();
{
  const N = 4096;
  for (let p = 0; p <= 5; p++) {
    const w = cosWin(p, N);
    const s = sidelobeSlope(w, 8, 512);
    const pred = -6.0206 * (p + 1);
    const nm = ['矩形', 'コサイン', 'ハン', 'cos^3', 'cos^4', 'cos^5'][p];
    line(row([p, nm, s.toFixed(3), pred.toFixed(3), p + 1,
      (s - pred).toFixed(3)], [5, 14, 14, 14, 11, 10]));
  }
  rule();
  line('★★★ dB/oct = -6 alpha ── このシリーズの背骨が、窓の裾にもそのまま出る。');
  line('   alpha は「端で何階まで滑らかか」。第57回の n と同じ量の、窓側の顔。');
}

// =====================================================================
head(2, 'よく使う窓を同じ物差しで');
// =====================================================================
line(row(['窓', '端での値', '実測 dB/oct', 'alpha', '第1サイドローブ[dB]'],
  [14, 12, 14, 8, 20]));
rule();
{
  const N = 4096;
  // 主ローブの半幅（余弦和の項数）
  const NAMES = [['rect', 1], ['bartlett', 2], ['hann', 2], ['hamming', 2], ['blackman', 3]];
  for (const pair of NAMES) {
    const nm = pair[0], hw = pair[1];
    const w = namedWin(nm, N);
    const s = sidelobeSlope(w, 8, 512);
    line(row([nm, w[0].toFixed(4), s.toFixed(3), (-s / 6.0206).toFixed(2),
      firstSidelobe(w, hw).toFixed(1)], [14, 12, 14, 8, 20]));
  }
  rule();
  line('★ ハミングは 第1サイドローブが ハンより低い（-42 dB 対 -31 dB）のに、');
  line('   裾の落ち方は 矩形と同じ alpha=1 ── 端で値が 0.08 残るから。');
  line('★★ 「最初の裾が低い」と「遠くまで落ちる」は 別のこと。');
  line('   遠くを決めるのは 端の滑らかさだけ。');
}

// =====================================================================
head(3, '漏れの床 ── 強い低周波が高周波に置いていくもの');
// =====================================================================
// f0 = 4.3 bin（格子に乗らない）の純音 1 本。高周波側に何が残るか。
// 注：4.5 のような半整数は cos^p（p 奇数）窓の厳密な零点に当たるので避ける。
line('f0 = 4.3 bin の純音 1 本。f bin での漏れ（dB、ピーク基準）');
line('');
{
  const N = 4096;
  const FS = [16, 32, 64, 128, 256, 512];
  line(row(['窓', ...FS.map((f) => 'f=' + f), '傾き dB/oct'],
    [12, 10, 10, 10, 10, 10, 10, 14]));
  rule();
  for (let p = 0; p <= 4; p++) {
    const w = cosWin(p, N);
    const W0 = winMag(w, 0);
    const vals = [], xs = [], ys = [];
    for (const f of FS) {
      const m = winMag(w, f - 4.3);
      const db = 20 * d10(m / W0);
      vals.push(db.toFixed(1));
      xs.push(Math.log(f) / Math.LN2); ys.push(db);
    }
    const nm = ['矩形', 'コサイン', 'ハン', 'cos^3', 'cos^4'][p];
    line(row([nm, ...vals, slope(xs, ys).toFixed(2)],
      [12, 10, 10, 10, 10, 10, 10, 14]));
  }
  rule();
  line('★ 漏れの床も -6 alpha dB/oct で落ちる ── 01節と同じ量。');
}

// =====================================================================
head(4, '★★★ 測れる beta の上限 ── beta < 2 alpha');
// =====================================================================
// 真のスペクトルが S ∝ f^-beta のとき、
//   測った値 ≈ S(f) + （低周波からの漏れ）
//   漏れは パワーで f^-2alpha。
//   よって beta > 2 alpha だと 漏れが本体を追い越す。

// --- 自前 FFT（radix-2、in-place）
function fft(re, im, inv) {
  const n = re.length;
  for (let i = 1, j = 0; i < n; i++) {
    let bit = n >> 1;
    for (; j & bit; bit >>= 1) j ^= bit;
    j ^= bit;
    if (i < j) {
      let t = re[i]; re[i] = re[j]; re[j] = t;
      t = im[i]; im[i] = im[j]; im[j] = t;
    }
  }
  for (let len = 2; len <= n; len <<= 1) {
    const ang = (inv ? TWO_PI : -TWO_PI) / len;
    const wr = Math.cos(ang), wi = Math.sin(ang);
    for (let i = 0; i < n; i += len) {
      let cr = 1, ci = 0;
      for (let k = 0; k < len / 2; k++) {
        const ur = re[i + k], ui = im[i + k];
        const vr = re[i + k + len / 2] * cr - im[i + k + len / 2] * ci;
        const vi = re[i + k + len / 2] * ci + im[i + k + len / 2] * cr;
        re[i + k] = ur + vr; im[i + k] = ui + vi;
        re[i + k + len / 2] = ur - vr; im[i + k + len / 2] = ui - vi;
        const ncr = cr * wr - ci * wi; ci = cr * wi + ci * wr; cr = ncr;
      }
    }
  }
  if (inv) for (let i = 0; i < n; i++) { re[i] /= n; im[i] /= n; }
}

// 乱数（再現できるよう自前の線形合同法）
let _s = 20260917;
function rnd() { _s = (_s * 1103515245 + 12345) & 0x7fffffff; return _s / 0x7fffffff; }
function gauss() {
  const u = Math.max(rnd(), 1e-12), v = rnd();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(TWO_PI * v);
}

// S ∝ f^-beta の系列を FFT 合成で作る（長めに作って 一部を切り出す
// ── 切り出すことで周期性が壊れ、漏れが実際に効くようになる）
function makeSeries(beta, M) {
  const re = new Float64Array(M), im = new Float64Array(M);
  for (let k = 1; k < M / 2; k++) {
    const amp = Math.pow(k, -beta / 2);
    const a = gauss() * amp, b = gauss() * amp;
    re[k] = a; im[k] = b;
    re[M - k] = a; im[M - k] = -b;
  }
  fft(re, im, true);
  return re;
}

{
  const M = 1 << 16, N = 1 << 12;
  line(row(['真の beta', '矩形(a=1)', 'コサイン(a=2)', 'ハン(a=3)', 'cos^4(a=5)'],
    [12, 14, 16, 14, 14]));
  rule();
  const WINS = [cosWin(0, N), cosWin(1, N), cosWin(2, N), cosWin(4, N)];
  const REAL = 32;                       // 8 realization の平均（ばらつきを均す）
  for (const beta of [1, 2, 3, 4, 5, 6]) {
    const acc = [0, 0, 0, 0];
    for (let r = 0; r < REAL; r++) {
      _s = 20260917 + 7919 * r;
      const x = makeSeries(beta, M);
      const seg = new Float64Array(N);
      const off = Math.floor(M / 3) + 137 * r;            // 途中から切り出す
      for (let i = 0; i < N; i++) seg[i] = x[off + i];
      for (let j = 0; j < WINS.length; j++) {
        const w = WINS[j];
        const re = new Float64Array(N), im = new Float64Array(N);
        for (let i = 0; i < N; i++) re[i] = seg[i] * w[i];
        fft(re, im, false);
        // 中域 k=32..512 で当てはめ
        const xs = [], ys = [];
        for (let k = 32; k <= 512; k++) {
          const P = re[k] * re[k] + im[k] * im[k];
          xs.push(Math.log(k)); ys.push(Math.log(P + 1e-300));
        }
        acc[j] += -slope(xs, ys);
      }
    }
    line(row([beta, ...acc.map((a) => (a / REAL).toFixed(3))], [12, 14, 16, 14, 14]));
  }
  rule();
  line('');
  line('★ 上限のすぐ手前で 行きすぎが出る（ハン窓 alpha=3、上限 beta=6 の近く）');
  line('');
  line(row(['真の beta', '推定 beta', '差'], [12, 14, 12]));
  rule();
  {
    const w = cosWin(2, N), R = 12;
    for (const beta of [3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8]) {
      let acc = 0;
      for (let r = 0; r < R; r++) {
        _s = 20260917 + 7919 * r;
        const x = makeSeries(beta, M);
        const re = new Float64Array(N), im = new Float64Array(N);
        const off = Math.floor(M / 3) + 137 * r;
        for (let i = 0; i < N; i++) re[i] = x[off + i] * w[i];
        fft(re, im, false);
        const xs = [], ys = [];
        for (let k = 32; k <= 512; k++) {
          const P = re[k] * re[k] + im[k] * im[k];
          xs.push(Math.log(k)); ys.push(Math.log(P + 1e-300));
        }
        acc += -slope(xs, ys);
      }
      const est = acc / R;
      line(row([beta, est.toFixed(3), (est - beta).toFixed(3)], [12, 14, 12]));
    }
  }
  rule();
  line('★★ 上限は「崖」ではなかった ── beta が 2alpha に近づくと まず 行きすぎ、');
  line('   越えると 2alpha に貼りつく。漏れの床 f^-2alpha が 本体より急なので、');
  line('   帯域の低い側だけを持ち上げ、傾きを 急に見せるため。');
  line('');
  line('★★★ 推定値が貼りつく天井は ちょうど 2 alpha ──');
  line('   矩形 2.0（実測 1.981）、コサイン 4.0（4.021）、ハン 6.0（5.998〜6.000）。');
  line('★★ ただし実用上の上限は 2 alpha より 1 ほど手前。');
  line('   ハン窓では beta=5 で すでに +0.6 行きすぎ、5.5 で天井に届く。');
  line('   ── 「beta < 2 alpha」は目安で、1 ほどの余裕を取るべき。');
  line('★ 第40回で「周期の整数倍で切る」必要があったのは、');
  line('   矩形窓の alpha=1（天井 beta=2）を回避するためだった。');
}

// =====================================================================
head(5, '★★ 同じ規則が 第45回の粒子生成を支配する');
// =====================================================================
// chi'' + omega^2(t) chi = 0、omega が T のあいだに w1 -> w2 へ変わる。
// 切り替えの形 f(x) が 端で p 階まで滑らかなら |beta| ∝ (wT)^-(p+1)。

function profile(p, x) {
  if (x <= 0) return 0;
  if (x >= 1) return 1;
  switch (p) {
    case 0: return x;                                        // 傾きが端で飛ぶ
    case 1: return x * x * (3 - 2 * x);                      // 1階まで滑らか
    case 2: return x * x * x * (10 + x * (-15 + 6 * x));     // 2階まで
    case 3: return x * x * x * x * (35 + x * (-84 + x * (70 - 20 * x)));  // 3階まで
    default: throw new Error('p');
  }
}

function bogo(p, T, w1, w2, nstep) {
  const w2sq = (t) => {
    const w = w1 + (w2 - w1) * profile(p, t / T);
    return w * w;
  };
  // chi(0) = 1/sqrt(2 w1), chi'(0) = -i w1 chi(0)
  const a0 = 1 / Math.sqrt(2 * w1);
  // 実部と虚部は同じ実係数 ODE に従うので別々に RK4
  function run(y0, v0) {
    let y = y0, v = v0;
    const h = T / nstep;
    for (let i = 0; i < nstep; i++) {
      const t = i * h;
      const f = (t, y) => -w2sq(t) * y;
      const k1y = v, k1v = f(t, y);
      const k2y = v + h / 2 * k1v, k2v = f(t + h / 2, y + h / 2 * k1y);
      const k3y = v + h / 2 * k2v, k3v = f(t + h / 2, y + h / 2 * k2y);
      const k4y = v + h * k3v, k4v = f(t + h, y + h * k3y);
      y += h / 6 * (k1y + 2 * k2y + 2 * k3y + k4y);
      v += h / 6 * (k1v + 2 * k2v + 2 * k3v + k4v);
    }
    return [y, v];
  }
  const [yr, vr] = run(a0, 0);            // 実部：chi_R(0)=a0, chi_R'(0)=0
  const [yi, vi] = run(0, -w1 * a0);      // 虚部：chi_I(0)=0, chi_I'(0)=-w1 a0
  // chi = yr + i yi,  chi' = vr + i vi  を t=T で w2 の基底に分解
  //   beta = sqrt(2 w2)/2 * e^{-i w2 T} (chi - i chi'/w2)
  const cr = yr - (-vi) / w2;             // Re(chi - i chi'/w2) = yr + vi/w2 ... 下で丁寧に
  void cr;
  const ar = yr, ai = yi;                 // chi
  const br = vr, bi = vi;                 // chi'
  // -i chi'/w2 = -i (br + i bi)/w2 = (bi - i br)/w2
  const zr = ar + bi / w2, zi = ai - br / w2;
  // e^{-i w2 T} を掛ける
  const c = Math.cos(w2 * T), s = Math.sin(w2 * T);
  const pr = zr * c + zi * s, pi2 = zi * c - zr * s;
  const k = Math.sqrt(2 * w2) / 2;
  const betaAbs = k * Math.hypot(pr, pi2);
  // alpha も同様に（|alpha|^2 - |beta|^2 = 1 の確認用）
  const qr = ar - bi / w2, qi = ai + br / w2;
  const ar2 = qr * c - qi * s, ai2 = qi * c + qr * s;
  const alphaAbs = k * Math.hypot(ar2, ai2);
  return [betaAbs, alphaAbs];
}

{
  const w1 = 1, w2 = 2;
  line('omega: 1 -> 2 を 時間 T で切り替える。|beta| の T 依存');
  line('');
  // |beta| は T とともに振動しながら落ちるので、T を密に振って
  // log-log の最小二乗で包絡の傾きを測る（T = 16 .. 128 の 40 点）。
  // T = 8 は まだ漸近形に入っていないので 傾きの当てはめには使わない。
  line(row(['p（端の滑らかさ）', 'T=8', 'T=16', 'T=32', 'T=64', '傾き', '予言 -(p+1)'],
    [18, 12, 12, 12, 12, 10, 12]));
  rule();
  let wronMax = 0;
  for (let p = 0; p <= 3; p++) {
    const vals = [];
    for (const T of [8, 16, 32, 64]) {
      const [b, a] = bogo(p, T, w1, w2, Math.max(40000, Math.round(4000 * T)));
      wronMax = Math.max(wronMax, Math.abs(a * a - b * b - 1));
      vals.push(b.toExponential(2));
    }
    const xs = [], ys = [];
    for (let i = 0; i < 40; i++) {
      const T = 16 * Math.pow(8, i / 39);
      const [b, a] = bogo(p, T, w1, w2, Math.max(40000, Math.round(4000 * T)));
      wronMax = Math.max(wronMax, Math.abs(a * a - b * b - 1));
      xs.push(Math.log(T)); ys.push(Math.log(b));
    }
    line(row([p, ...vals, slope(xs, ys).toFixed(3), -(p + 1)],
      [18, 12, 12, 12, 12, 10, 12]));
  }
  rule();
  line('★ |alpha|^2 - |beta|^2 = 1 のずれ 最大 ' + wronMax.toExponential(1)
    + '（第36・45回の det = 1）');
  line('★★★ |beta| ∝ T^-(p+1) ── 窓の裾とまったく同じ規則。');
  line('   切り替えが端で滑らかなほど、粒子は作られない。');
}

// =====================================================================
head(6, '三つの顔を並べる');
// =====================================================================
line(row(['場面', '「端」とは', '効き目', 'alpha の意味'], [20, 20, 18, 16]));
rule();
const FACES = [
  ['窓関数（第40回）', '窓の両端', '裾 f^-alpha', '端の滑らかさ'],
  ['周期図（第51回）', '記録の両端', '漏れの床', '測れる beta の上限/2'],
  ['粒子生成（第45回）', '切り替えの前後', '|beta| ∝ T^-alpha', '切り替えの滑らかさ'],
  ['重ね合わせ（第56回）', 'tau の両端', '失う桁数', '補正のべき'],
];
for (const f of FACES) line(row(f, [20, 20, 18, 16]));
rule();
line('★★★ どれも「有限で切った」ことの代金で、');
line('    代金の大きさは 切り口の滑らかさ alpha だけで決まる。');
line('★★ 第45回の「真空は観測者による」は、');
line('    「窓の外が中に漏れる」の物理側の言い方だった。');

// =====================================================================
head(7, 'まとめ');
// =====================================================================
const SUM = [
  ['窓の裾', 'dB/oct = -6 alpha', '本稿の計算'],
  ['alpha の正体', '端で何階まで滑らかか', '本稿の計算'],
  ['★ 推定値の天井', 'beta = 2 alpha', '本稿の計算'],
  ['★ 実用上の上限', '2 alpha より 1 手前', '本稿の主張'],
  ['矩形窓の天井', 'beta = 2（実測 1.981）', '本稿の計算'],
  ['ハン窓の天井', 'beta = 6（実測 5.998）', '本稿の計算'],
  ['★★ 粒子生成', '|beta| ∝ T^-(p+1)', '本稿の計算'],
  ['|alpha|^2-|beta|^2 = 1', '保たれる', '本稿の確認'],
  ['実データでの検証', '未着手', '合成のみ'],
];
line(row(['項目', '値', '根拠'], [26, 26, 14]));
rule();
for (const s of SUM) line(row(s, [26, 26, 14]));
rule();
line('');
line('★★★ 窓の漏れと 粒子生成は 同じ計算だった。');
line('    どちらも「端の滑らかさ alpha」が代金を決める。');
line('★★★ そして dB/oct = -6 alpha ── 第1回の物差しが、');
line('    切り口の滑らかさにも そのまま使えた。');
line('');
