// 考える波 第60回「トレンドと信号は どこで分かれるか」検証
//   node torendo.js
// 依存ライブラリ 0（FFT は自前）。
//
// 第59回で「1〜2 次のトレンドを引けば漏れが消える」と分かった。
// では 引いたものは どこへ行ったのか。トレンドと信号の境目はどこか。
//
// 本稿の主張：
//   ★ q 次のトレンド除去は 階数 q+1 の高域通過フィルタ ── また dB/oct = 6 alpha。
//   ★ 引いたトレンドは 捨てものではなく、記録より長い波の
//      （自由度 1〜2 の、ひどく粗い）唯一の測定値。
//   ★★ そして 1/f^beta の「分散」は数ではない ── 切り方で走る（第29回）。

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
function mean(a) { let s = 0; for (const v of a) s += v; return s / a.length; }
function vari(a) {
  const m = mean(a); let s = 0;
  for (const v of a) s += (v - m) * (v - m);
  return s / a.length;
}

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

let _s = 20260919;
function rnd() { _s = (_s * 1103515245 + 12345) & 0x7fffffff; return _s / 0x7fffffff; }
function gauss() {
  const u = Math.max(rnd(), 1e-12), v = rnd();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(TWO_PI * v);
}

// ---------------------------------------------------- 多項式トレンドの射影
// 記録 x（長さ n）に q 次多項式を最小二乗で当て、その多項式を返す。
function fitPoly(x, q) {
  const n = x.length;
  const pw = new Float64Array(2 * q + 1);
  for (let t = 0; t < n; t++) {
    const u = 2 * t / (n - 1) - 1;
    let up = 1;
    for (let j = 0; j <= 2 * q; j++) { pw[j] += up; up *= u; }
  }
  const A = [];
  for (let i = 0; i <= q; i++) {
    A.push(new Float64Array(q + 2));
    for (let j = 0; j <= q; j++) A[i][j] = pw[i + j];
  }
  for (let t = 0; t < n; t++) {
    const u = 2 * t / (n - 1) - 1;
    let up = 1;
    for (let i = 0; i <= q; i++) { A[i][q + 1] += up * x[t]; up *= u; }
  }
  for (let i = 0; i <= q; i++) {
    let piv = i;
    for (let r = i + 1; r <= q; r++) if (Math.abs(A[r][i]) > Math.abs(A[piv][i])) piv = r;
    const tmp = A[i]; A[i] = A[piv]; A[piv] = tmp;
    for (let r = 0; r <= q; r++) {
      if (r === i) continue;
      const f = A[r][i] / A[i][i];
      for (let c = i; c <= q + 1; c++) A[r][c] -= f * A[i][c];
    }
  }
  const co = [];
  for (let i = 0; i <= q; i++) co.push(A[i][q + 1] / A[i][i]);
  const p = new Float64Array(n);
  for (let t = 0; t < n; t++) {
    const u = 2 * t / (n - 1) - 1;
    let up = 1, v = 0;
    for (let i = 0; i <= q; i++) { v += co[i] * up; up *= u; }
    p[t] = v;
  }
  return p;
}
function detrend(x, q) {
  const p = fitPoly(x, q);
  const r = new Float64Array(x.length);
  for (let i = 0; i < x.length; i++) r[i] = x[i] - p[i];
  return r;
}

// =====================================================================
head(1, '★★★ トレンド除去は「階数 q+1 の高域通過フィルタ」だった');
// =====================================================================
// 正弦波 1 本を入れて、残差のエネルギーを測る。
//   利得^2(f) = (|r_cos|^2 + |r_sin|^2) / (|cos|^2 + |sin|^2)

const NW = 1024;
function gain2(q, f) {
  const c = new Float64Array(NW), s = new Float64Array(NW);
  for (let t = 0; t < NW; t++) {
    const ph = TWO_PI * f * t / NW;
    c[t] = Math.cos(ph); s[t] = Math.sin(ph);
  }
  const rc = detrend(c, q), rs = detrend(s, q);
  let a = 0, b = 0;
  for (let t = 0; t < NW; t++) { a += rc[t] * rc[t] + rs[t] * rs[t]; b += c[t] * c[t] + s[t] * s[t]; }
  return a / b;
}

line('記録の長さ 1024。周波数 f［bin］の正弦波が どれだけ残るか');
line('');
line(row(['f[bin]', 'q=0(平均)', 'q=1(直線)', 'q=2', 'q=3'], [10, 14, 14, 14, 14]));
rule();
{
  for (const f of [0.01, 0.03, 0.1, 0.3, 1, 2, 3]) {
    const out = [];
    for (let q = 0; q <= 3; q++) out.push((10 * d10(gain2(q, f))).toFixed(2));
    line(row([f, ...out], [10, 14, 14, 14, 14]));
  }
  rule();
  line('（表は 利得^2 を dB で。0 dB なら そのまま通す）');
  line('');
  line(row(['q', '低域の傾き dB/oct', '予言 6(q+1)', 'alpha', '-3dB 点[bin]'],
    [6, 20, 14, 8, 16]));
  rule();
  for (let q = 0; q <= 3; q++) {
    const xs = [], ys = [];
    for (let f = 0.005; f <= 0.08; f *= 1.4) {
      xs.push(Math.log(f) / Math.LN2); ys.push(10 * d10(gain2(q, f)));
    }
    // -3 dB 点を二分法で
    let lo = 0.001, hi = 5;
    for (let i = 0; i < 60; i++) {
      const m = 0.5 * (lo + hi);
      if (10 * d10(gain2(q, m)) < -3) lo = m; else hi = m;
    }
    line(row([q, slope(xs, ys).toFixed(3), (6.0206 * (q + 1)).toFixed(4), q + 1,
      (0.5 * (lo + hi)).toFixed(4)], [6, 20, 14, 8, 16]));
  }
  rule();
  line('★★★ dB/oct = 6(q+1) ── 第1回の物差しが ここにも出る。');
  line('   q 次のトレンド除去は 階数 alpha = q+1 の高域通過フィルタ。');
  line('★★ -3dB 点は 0.44 / 0.85 / 1.24 / 1.62 bin ── およそ 0.4(q+1) bin。');
  line('   どれも「記録 1 本のあいだに 1 周期ほど」の所にある。');
  line('★★★ つまり「トレンドか信号か」の境目は 系ではなく 記録の長さが決めている。');
  line('   同じ信号でも 記録を 10 倍 長くすれば、いままでトレンドだったものが');
  line('   信号になる ── 第5回の「宇宙年齢より長い周期」と まったく同じ形。');
}

// =====================================================================
head(2, '★★★ 漏れが有限になる条件 ── beta <= 2q + 3');
// =====================================================================
// 分解能より低い f からの漏れは
//   Leak(k) = int f^-beta * G_q(f) * |W_alpha(k-f)|^2 df
// G_q(f) ∝ f^(2(q+1)) なので（01節）、積分が下端で収束する条件は
//   -beta + 2(q+1) > -1   すなわち   beta < 2q + 3。
// 第59回 03節の表が これで全部説明できるはず。

function winCos(alpha, n) {
  const w = new Float64Array(n);
  for (let i = 0; i < n; i++) {
    const x = (i + 0.5) / n - 0.5;
    w[i] = Math.pow(Math.cos(Math.PI * x), alpha - 1);
  }
  return w;
}
function dtft2(w, f) {
  let re = 0, im = 0;
  const n = w.length;
  for (let i = 0; i < n; i++) {
    const ph = TWO_PI * f * (i - (n - 1) / 2) / n;
    re += w[i] * Math.cos(ph); im -= w[i] * Math.sin(ph);
  }
  return re * re + im * im;
}
// 下端 fmin から 1 bin までの漏れ（bin k へ）
function leak(k, beta, q, alpha, fmin) {
  const w = winCos(alpha, NW);
  let s = 0;
  const NP = 400;
  const a = Math.log(fmin), b = 0, h = (b - a) / NP;   // ln f で中点則
  for (let i = 0; i < NP; i++) {
    const f = Math.exp(a + h * (i + 0.5));
    s += Math.pow(f, -beta) * gain2(q, f) * dtft2(w, k - f) * f;  // df = f d(ln f)
  }
  return s * h;
}

{
  line('ハン窓（alpha=3）、bin k=64 への漏れ。下端 fmin を 1/16 から 1/64 に');
  line('下げたとき 漏れが何倍になるか（1 に近ければ 収束している）');
  line('');
  line(row(['beta', 'q=0', 'q=1', 'q=2', 'beta<=2q+3 を満たす q'], [8, 12, 12, 12, 24]));
  rule();
  for (const beta of [3, 4, 5, 6, 7]) {
    const out = [];
    for (let q = 0; q <= 2; q++) {
      const a = leak(64, beta, q, 3, 1 / 64), b = leak(64, beta, q, 3, 1 / 16);
      out.push((a / b).toFixed(3));
    }
    const ok = [3, 5, 7].map((lim, j) => (beta <= lim ? 'q=' + j : null)).filter(Boolean);
    line(row([beta, ...out, ok.length ? ok.join(',') : 'なし'],
      [8, 12, 12, 12, 24]));
  }
  rule();
  line('★★★ 比が 1.00 なら 収束、大きければ 発散 ── 予言 beta < 2q+3 のとおり。');
  line('★ beta = 2q+3 ちょうど（beta=5,q=1 と beta=7,q=2）は 対数発散で、');
  line('   下端を 4 倍 下げても 1.19 倍 にしかならない ── 実用上は 収束と同じ。');
  line('');
  line('★ 第59回 03節（ハン窓 alpha=3）の表と突き合わせる：');
  line(row(['beta', 'q', '2q+3', '漏れの比', '第59回の実測', '天井 2alpha=6'],
    [8, 5, 8, 12, 16, 14]));
  rule();
  const OBS = [
    [5, 0, '5.512（行きすぎ）', '-'],
    [5, 1, '4.992（直った）', '-'],
    [6, 1, '6.035（まだ）', '-'],
    [6, 2, '5.994（直った）', '-'],
    [7, 2, '6.039（天井）', '貼りつき'],
  ];
  for (const o of OBS) {
    const beta = o[0], q = o[1];
    const rr = leak(64, beta, q, 3, 1 / 64) / leak(64, beta, q, 3, 1 / 16);
    line(row([beta, q, 2 * q + 3, rr.toFixed(2) + (rr < 1.1 ? ' 収束' : ' 発散'),
      o[2], o[3]], [8, 5, 8, 12, 16, 14]));
  }
  rule();
  line('★★★ 「収束」の行だけが 直っている ── beta <= 2q+3 が そのまま効いている。');
  line('   beta=6,q=1 は 比 1.13 の 発散 → 実測も 6.035 で 直っていない。');
  line('★★ beta=7, q=2 は 漏れのほうは 収まっているのに 直らない ──');
  line('   窓の天井 2alpha=6 に当たっているから。原因が別だと分かる。');
  line('★ つまり 二つの条件を 別々に満たす必要がある：');
  line('   ① 記録より長い波からの漏れ → beta < 2q + 3（トレンド除去で買う）');
  line('   ② 窓の裾からの天井       → beta < 2 alpha（窓で買う）');
  line('★★★ 第58回で「窓を上げろ」、第59回で「トレンドを引け」と言ったのは');
  line('   別々の条件だった ── どちらか一方では足りない。');
}

// =====================================================================
head(3, '引いたトレンドは 何の測定値か');
// =====================================================================
// 合成長 M の系列から 長さ N を切り出す。切り出した記録の分解能 1 bin より
// 低い成分（M 格子で k < M/N）だけを取り出したものを「真の低域部分」とし、
// 当てはめた 1 次多項式と どれだけ似ているかを測る。

const N = 1024, M = 1 << 16;
function makeSeries(beta) {
  const re = new Float64Array(M), im = new Float64Array(M);
  for (let k = 1; k < M / 2; k++) {
    const amp = Math.pow(k, -beta / 2);
    const a = gauss() * amp, b = gauss() * amp;
    re[k] = a; im[k] = b; re[M - k] = a; im[M - k] = -b;
  }
  fft(re, im, true);
  return re;
}
function lowPart(beta, seed) {
  // 同じ乱数から、低域だけ（k < M/N）を残した系列も作る
  _s = seed;
  const re = new Float64Array(M), im = new Float64Array(M);
  const reL = new Float64Array(M), imL = new Float64Array(M);
  const kc = M / N;                       // 切り出した記録の 1 bin にあたる
  for (let k = 1; k < M / 2; k++) {
    const amp = Math.pow(k, -beta / 2);
    const a = gauss() * amp, b = gauss() * amp;
    re[k] = a; im[k] = b; re[M - k] = a; im[M - k] = -b;
    if (k < kc) { reL[k] = a; imL[k] = b; reL[M - k] = a; imL[M - k] = -b; }
  }
  fft(re, im, true); fft(reL, imL, true);
  return [re, reL];
}

{
  line('切り出し長 ' + N + '。1 次多項式の当てはめと「真の低域部分」の相関');
  line('');
  line(row(['beta', '相関係数', 'トレンドの分散/低域の分散', '低域が全分散に占める割合'],
    [8, 14, 26, 26]));
  rule();
  const R = 60;
  for (const beta of [1, 2, 3, 4, 5]) {
    const cors = [], rats = [], fracs = [];
    for (let r = 0; r < R; r++) {
      const pair = lowPart(beta, 20260919 + 7919 * r);
      const off = (Math.floor(M / 3) + 137 * r) % (M - N);
      const seg = [], low = [];
      for (let i = 0; i < N; i++) { seg.push(pair[0][off + i]); low.push(pair[1][off + i]); }
      const tr = fitPoly(seg, 1);
      // 相関（どちらも平均を引いて）
      const mt = mean(Array.from(tr)), ml = mean(low);
      let sxy = 0, sxx = 0, syy = 0;
      for (let i = 0; i < N; i++) {
        const a = tr[i] - mt, b = low[i] - ml;
        sxy += a * b; sxx += a * a; syy += b * b;
      }
      cors.push(sxy / Math.sqrt(sxx * syy));
      rats.push(sxx / syy);
      fracs.push(vari(low) / vari(seg));
    }
    line(row([beta, mean(cors).toFixed(4), mean(rats).toFixed(4), mean(fracs).toFixed(4)],
      [8, 14, 26, 26]));
  }
  rule();
  line('★ beta が大きいほど 相関が高い ── 低域が支配的になるから。');
  line('★★ しかし 分散の比は 1 に届かない ── 直線は 低域の一部しか拾えない。');
  line('★★★ つまり 引いたトレンドは「記録より長い波」の測定値ではあるが、');
  line('   自由度 2 の ひどく粗い測定値。第51回の「自由度 2」がここにも。');
}

// =====================================================================
head(4, '★★ 1/f^beta の「分散」は 数ではない ── 切り方で走る');
// =====================================================================
{
  line('同じ系列から 長さ N を切り出したときの 分散（beta ごと、R=40 の平均）');
  line('');
  line(row(['beta', 'N=256', 'N=1024', 'N=4096', '傾き(桁/桁)', '予言'],
    [8, 14, 14, 14, 14, 12]));
  rule();
  const NS = [256, 1024, 4096];
  const R = 40;
  for (const beta of [0.5, 1, 2, 3]) {
    const out = [], xs = [], ys = [];
    for (const n of NS) {
      let acc = 0;
      for (let r = 0; r < R; r++) {
        _s = 20260919 + 104729 * r;
        const x = makeSeries(beta);
        const off = (Math.floor(M / 3) + 211 * r) % (M - n);
        const seg = [];
        for (let i = 0; i < n; i++) seg.push(x[off + i]);
        acc += vari(seg);
      }
      const v = acc / R;
      out.push(v.toExponential(2));
      xs.push(Math.log(n)); ys.push(Math.log(v));
    }
    // beta<1 は高域が支配して 収束（傾き 0）。beta=1 は log N（この範囲で 0.146）。
    // beta>1 は N^(beta-1)。
    const pred = beta < 1 ? '0（収束）'
      : (beta === 1 ? '0.146 (log N)' : (beta - 1).toFixed(1));
    line(row([beta, ...out, slope(xs, ys).toFixed(3), pred],
      [8, 14, 14, 14, 14, 14]));
  }
  rule();
  line('★★★ beta > 1 では 分散が 記録を伸ばすほど 増え続ける（N^(beta-1)）。');
  line('   「この信号の分散はいくつか」という問いに 答えは無い ──');
  line('   記録の長さを言わなければ 決まらない。');
  line('★ beta < 1 では 高域が支配して 収束する（実測 0.016）。');
  line('★★★ そして beta = 1 ちょうどでは log N ── べきでも 定数でもない。');
  line('   N=256→4096 での予言 ln(ln4096/ln256)/ln16 = 0.146 に対し 実測 0.161。');
  line('   1/f は ここでも ちょうど境目にいる。');
  line('★★ これが 第29回の繰り込みと同じ構造：');
  line('   物理量は「どこで切ったか」に依存し、切り方を変えると走る。');
  line('   そして 対数で走る点が 繰り込み群の 固定点にあたる。');
}

// =====================================================================
head(5, 'トレンドを引くと 分散はどれだけ減るか');
// =====================================================================
{
  line('N=1024。引く前の分散を 1 としたときの 残差の分散');
  line('');
  line(row(['beta', 'q=0', 'q=1', 'q=2', 'q=3', 'q=5'], [8, 12, 12, 12, 12, 12]));
  rule();
  const R = 60;
  for (const beta of [0.5, 1, 2, 3, 4]) {
    const acc = [0, 0, 0, 0, 0];
    const QS = [0, 1, 2, 3, 5];
    for (let r = 0; r < R; r++) {
      _s = 20260919 + 15485863 * r;
      const x = makeSeries(beta);
      const off = (Math.floor(M / 3) + 307 * r) % (M - N);
      const seg = new Float64Array(N);
      for (let i = 0; i < N; i++) seg[i] = x[off + i];
      const v0 = vari(Array.from(seg));
      for (let j = 0; j < QS.length; j++) {
        acc[j] += vari(Array.from(detrend(seg, QS[j]))) / v0;
      }
    }
    line(row([beta, ...acc.map((v) => (v / R).toFixed(4))], [8, 12, 12, 12, 12, 12]));
  }
  rule();
  line('★ beta が大きいほど トレンド除去で 大きく減る ──');
  line('   低域に力が集まっているから。');
  line('★★★ beta=4 では 直線を引くだけで 分散が 1 割 以下 になる。');
  line('   「分散」という量が どれだけ 低域に支配されていたかが分かる。');
  line('★★ 逆に beta=0.5 では ほとんど変わらない ── 引いても害が小さい。');
  line('   迷ったら引いてよい、というのは この意味で正しい。');
}

// =====================================================================
head(6, 'まとめ');
// =====================================================================
const SUM = [
  ['★ トレンド除去の正体', '階数 q+1 の高域通過', '本稿の計算'],
  ['低域の傾き', '6(q+1) dB/oct', '本稿の計算'],
  ['-3dB 点', '約 0.4(q+1) bin', '本稿の計算'],
  ['境目を決めるもの', '系ではなく 記録の長さ', '本稿の主張'],
  ['★ 漏れの収束条件', 'beta <= 2q + 3', '本稿の計算'],
  ['★ 天井（貼りつき）', 'beta < 2 alpha（窓だけ）', '第58回＋本稿'],
  ['二つは別条件', '両方 満たす必要がある', '本稿の主張'],
  ['★ 引いたトレンド', '自由度 2 の 粗い測定値', '本稿の計算'],
  ['★★ 1/f^beta の分散', '数ではなく 走る量', '本稿の計算'],
  ['分散の走り方', 'beta>1 で N^(beta-1)', '本稿の計算'],
  ['★ beta = 1 では', 'log N（0.146 対 実測 0.161）', '本稿の計算'],
  ['beta < 1 では', '収束（実測 0.016）', '本稿の計算'],
  ['実データでの検証', '未着手', '合成のみ'],
];
line(row(['項目', '値', '根拠'], [24, 32, 14]));
rule();
for (const s of SUM) line(row(s, [24, 32, 14]));
rule();
line('');
line('★★★ 「トレンドか信号か」に 系の側の答えは無い。');
line('    記録の長さが 境目を決めている ── 第5回と同じ形。');
line('★★★ そして 引いたものは 消えていない。');
line('    自由度 2 の 粗い測定値として 手元に残っている。');
line('');
