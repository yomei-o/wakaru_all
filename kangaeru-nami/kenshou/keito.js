// 考える波 第59回「系統誤差を測る」検証
//   node keito.js
// 依存ライブラリ 0（FFT は自前）。
//
// 第58回で「窓を変えると beta の推定値が動く」＝符号の決まった系統誤差が出た。
// 今回はそれを逆手に取る ── 窓を何種類も変えて測り、動き方から真の値を推定する。
//
// 本稿の主張：
//   ★ 「行きすぎ」は 雑音ゼロでも出る ── 統計ではなく 漏れの形。
//      その主役は 記録の分解能より低い周波数（＝記録の中では傾きに見える成分）。
//   ★ だから 1〜2 次のトレンドを引くだけで 消える。
//   ★ beta-hat(alpha) には 平らな区間ができ、そこが答え。
//   ★★ 平らさの幅を系統誤差として報告する手続きを作り、
//      200 realization で「当たり具合」を実測する（名目 68% に対して何 %か）。

'use strict';

const TWO_PI = 2 * Math.PI;
function d10(x) { return Math.log(x) / Math.LN10; }
function line(t) { console.log(t); }
function rule(c) { line((c || '-').repeat(76)); }
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
function sd(a) {
  const m = mean(a); let s = 0;
  for (const v of a) s += (v - m) * (v - m);
  return Math.sqrt(s / (a.length - 1));
}

// ---------------------------------------------------------------- FFT
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

// ---------------------------------------------------------------- 乱数
let _s = 20260918;
function rnd() { _s = (_s * 1103515245 + 12345) & 0x7fffffff; return _s / 0x7fffffff; }
function gauss() {
  const u = Math.max(rnd(), 1e-12), v = rnd();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(TWO_PI * v);
}

// ---------------------------------------------------------------- 設定
const N = 4096;          // 記録の長さ
const M = 1 << 16;       // 合成の長さ（ここから切り出すので 周期的でなくなる）
const KLO = 32, KHI = 512;   // 当てはめ帯域
const AMAX = 8;          // 窓の階数 alpha = 1..8

// alpha 次の窓（cos^(alpha-1)）。alpha=1 が矩形、3 がハン。
function win(alpha) {
  const w = new Float64Array(N);
  for (let n = 0; n < N; n++) {
    const x = (n + 0.5) / N - 0.5;
    w[n] = Math.pow(Math.cos(Math.PI * x), alpha - 1);
  }
  return w;
}
const WINS = [];
for (let a = 1; a <= AMAX; a++) WINS.push(win(a));

function makeSeries(beta) {
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

function estimate(seg, w) {
  const re = new Float64Array(N), im = new Float64Array(N);
  for (let i = 0; i < N; i++) re[i] = seg[i] * w[i];
  fft(re, im, false);
  const xs = [], ys = [];
  for (let k = KLO; k <= KHI; k++) {
    const P = re[k] * re[k] + im[k] * im[k];
    xs.push(Math.log(k)); ys.push(Math.log(P + 1e-300));
  }
  return -slope(xs, ys);
}

function cutSeg(x, off) {
  const o = Math.abs(off) % (M - N);     // 配列の外に出ないよう畳む
  const seg = new Float64Array(N);
  for (let i = 0; i < N; i++) seg[i] = x[o + i];
  return seg;
}

// =====================================================================
head(1, 'beta-hat を alpha について走らせると 平らな区間が出る');
// =====================================================================
line('真の beta ごとに、窓の階数 alpha = 1..8 で推定（32 realization の平均）');
line('');
{
  line(row(['真の beta', ...Array.from({ length: AMAX }, (_, i) => 'a=' + (i + 1))],
    [10, 8, 8, 8, 8, 8, 8, 8, 8]));
  rule();
  for (const beta of [1, 2, 3, 4, 5, 6, 7]) {
    const acc = new Array(AMAX).fill(0), R = 32;
    for (let r = 0; r < R; r++) {
      _s = 20260918 + 7919 * r;
      const x = makeSeries(beta);
      const seg = cutSeg(x, Math.floor(M / 3) + 137 * r);
      for (let a = 0; a < AMAX; a++) acc[a] += estimate(seg, WINS[a]);
    }
    line(row([beta, ...acc.map((v) => (v / R).toFixed(3))],
      [10, 8, 8, 8, 8, 8, 8, 8, 8]));
  }
  rule();
  line('★ 小さい alpha では 漏れで頭打ち（第58回の天井 2 alpha）。');
  line('★ 天井の すぐ手前では 行きすぎる（beta=6, a=4 で 7.62／beta=7, a=4 で 8.00）。');
  line('★★ 大きい alpha に行くと 落ち着き、どの beta でも 真値より 0.01 ほど低い');
  line('   一定の値に並ぶ ── ここが 平らな区間。');
  line('★★★ 手続きの骨：この「平らな区間」を自動で見つけ、その幅を');
  line('   系統誤差として報告する（06節）。');
}

// =====================================================================
head(2, '雑音を消して 偏りだけを見る ── 「行きすぎ」は本物か');
// =====================================================================
// 雑音を除いた「期待される周期図」を直接たたみこみで作る：
//   E[P(k)] = int S(f) |W(k-f)|^2 df    （負の周波数からの寄与も足す）
// これを当てはめれば、統計誤差ゼロの 純粋な偏りが出る。

const LPAD = 1 << 18;                    // 1/64 bin の細かさで |W|^2 を作る
function winPower(w) {
  const re = new Float64Array(LPAD), im = new Float64Array(LPAD);
  for (let i = 0; i < N; i++) re[i] = w[i];
  fft(re, im, false);
  const p = new Float64Array(LPAD);
  for (let i = 0; i < LPAD; i++) p[i] = re[i] * re[i] + im[i] * im[i];
  return p;                              // 添字 i は f = i * N/LPAD [bin]
}
const SUB = LPAD / N;                    // 1 bin あたりの格子点数（=64）

function expectedP(wp, k, beta, fminBin) {
  // f を 1/SUB bin 刻みで、合成の最低周波数 N/M bin から N/2 bin まで。
  // 注意：切り出した記録の分解能 1 bin より下（N/M .. 1 bin）にも
  // 大きな力があり、そこが漏れの主役になる。1 bin から始めてはいけない。
  let s = 0;
  const fminI = Math.max(1, Math.round((fminBin === undefined ? N / M : fminBin) * SUB));
  const fmaxI = Math.round(N / 2 * SUB);
  for (let fi = fminI; fi <= fmaxI; fi++) {
    const f = fi / SUB;
    const S = Math.pow(f, -beta);
    const d1 = Math.abs(Math.round((k - f) * SUB)) % LPAD;
    const d2 = Math.abs(Math.round((k + f) * SUB)) % LPAD;
    s += S * (wp[d1] + wp[d2]);
  }
  return s / SUB;
}

{
  line('雑音ゼロの「期待される周期図」から出した 偏りだけ（真値との差）');
  line('');
  line(row(['真の beta', ...Array.from({ length: AMAX }, (_, i) => 'a=' + (i + 1))],
    [10, 8, 8, 8, 8, 8, 8, 8, 8]));
  rule();
  const WPS = WINS.map(winPower);
  const KS = [];
  for (let k = KLO; k <= KHI; k *= 1.3) KS.push(Math.round(k));
  for (const beta of [1, 3, 5, 7]) {
    const out = [];
    for (let a = 0; a < AMAX; a++) {
      const xs = [], ys = [];
      for (const k of KS) {
        xs.push(Math.log(k)); ys.push(Math.log(expectedP(WPS[a], k, beta)));
      }
      out.push((-slope(xs, ys) - beta).toFixed(3));
    }
    line(row([beta, ...out], [10, 8, 8, 8, 8, 8, 8, 8, 8]));
  }
  rule();
  line('★ 漏れの偏りは まず 負（緩く見える）── 天井 2 alpha に貼りつくため。');
  line('★ その手前に 正の「行きすぎ」がある（beta=5, a=3 で +0.625）。');
  line('★★★ これは 雑音ゼロの計算でも出る ── つまり 統計の効果ではなく、');
  line('   期待されるスペクトルそのものの形。第58回で見た +0.61 と一致する。');
  line('★★ 予想が外れた：大きい alpha で 主ローブの平滑化による 偏りが');
  line('   育つはずと思っていたが、+0.002 〜 +0.008 しかない。無視できる。');
  line('   → 大きい alpha 側を止めているのは 偏りではなく ばらつき（04節）。');
  line('');
  line('★ どこから漏れているのか ── 積分の下端を変えて調べる（beta=5, a=3）');
  {
    const wp = winPower(WINS[2]);
    for (const fmin of [N / M, 0.25, 0.5, 1.0]) {
      const xs = [], ys = [];
      for (const k of KS) { xs.push(Math.log(k)); ys.push(Math.log(expectedP(wp, k, 5, fmin))); }
      line('   下端 f = ' + fmin.toFixed(4) + ' bin → 推定 beta = '
        + (-slope(xs, ys)).toFixed(3));
    }
  }
  line('★★★ 記録の分解能 1 bin より下（0.0625〜1 bin）を入れたときだけ');
  line('   行きすぎが出る ── 漏れの主役は「記録の中では傾きにしか見えない成分」。');
}

// =====================================================================
head(3, '★★★ ならば 傾きを引けばよい ── トレンド除去');
// =====================================================================
// 02節で 漏れの主役は「記録の分解能より低い周波数」だと分かった。
// それは 記録の中では 定数・傾き・ゆるい曲がりにしか見えない。
// なら 当てはめて引いてしまえばよい。q 次多項式を最小二乗で引く。

function detrend(seg, q) {
  const n = seg.length;
  // ヴァンデルモンド行列の正規方程式をガウス消去で（q は小さいので十分）
  const A = [], b = [];
  for (let i = 0; i <= q; i++) {
    A.push(new Float64Array(q + 2));
    b.push(0);
  }
  const pw = new Float64Array(2 * q + 1);
  for (let t = 0; t < n; t++) {
    const u = 2 * t / (n - 1) - 1;
    let up = 1;
    for (let j = 0; j <= 2 * q; j++) { pw[j] += up; up *= u; }
  }
  for (let i = 0; i <= q; i++) for (let j = 0; j <= q; j++) A[i][j] = pw[i + j];
  for (let t = 0; t < n; t++) {
    const u = 2 * t / (n - 1) - 1;
    let up = 1;
    for (let i = 0; i <= q; i++) { b[i] += up * seg[t]; up *= u; }
  }
  for (let i = 0; i <= q; i++) A[i][q + 1] = b[i];
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
  const out = new Float64Array(n);
  for (let t = 0; t < n; t++) {
    const u = 2 * t / (n - 1) - 1;
    let up = 1, v = 0;
    for (let i = 0; i <= q; i++) { v += co[i] * up; up *= u; }
    out[t] = seg[t] - v;
  }
  return out;
}

{
  const R = 32;
  line('窓の階数 a=3（ハン）。q 次多項式を引いてから測る');
  line('');
  line(row(['真の beta', '引かない', 'q=0(平均)', 'q=1(直線)', 'q=2', 'q=3'],
    [10, 12, 12, 12, 10, 10]));
  rule();
  for (const beta of [3, 4, 5, 6, 7]) {
    const acc = [0, 0, 0, 0, 0];
    for (let r = 0; r < R; r++) {
      _s = 20260918 + 7919 * r;
      const x = makeSeries(beta);
      const seg = cutSeg(x, Math.floor(M / 3) + 137 * r);
      acc[0] += estimate(seg, WINS[2]);
      for (let q = 0; q <= 3; q++) acc[q + 1] += estimate(detrend(seg, q), WINS[2]);
    }
    line(row([beta, ...acc.map((v) => (v / R).toFixed(3))], [10, 12, 12, 12, 10, 10]));
  }
  rule();
  line('★★★ 直線を引くだけで 行きすぎが消える ── beta=5 で 5.512 → 4.992。');
  line('   第58回では「窓の階数を上げろ」と書いたが、もっと安い手があった。');
  line('★ beta=6 は q=2 で 5.994 まで直る。');
  line('★★ ただし 天井は動かない ── beta=7 は a=3（天井 6）のままでは');
  line('   どの q でも直らない（6.04〜6.57）。トレンド除去は');
  line('   「行きすぎ」を消すが、「貼りつき」は消さない。');
  line('★★ 引きすぎも害になる（beta=7 で q=3 にすると 6.57 と悪化）。');
  line('★ 手引きに足すべき手順：周期図を取る前に 1〜2 次のトレンドを引く。');
  line('   そのうえで 2 alpha >= beta + 2 になるよう 窓を選ぶ。');
}

// =====================================================================
head(4, 'ばらつきは alpha とともに増える');
// =====================================================================
// 窓をかけると 独立な点が減る（等価雑音帯域 ENBW が広がる）。
//   ENBW = N * sum(w^2) / (sum w)^2   [bin]
{
  line(row(['alpha', 'ENBW[bin]', '実測 sd(beta)', '1.2825/sqrt(M/ENBW)', '比'],
    [8, 14, 16, 22, 10]));
  rule();
  const R = 200, beta = 3;
  const est = Array.from({ length: AMAX }, () => []);
  for (let r = 0; r < R; r++) {
    _s = 20260918 + 104729 * r;
    const x = makeSeries(beta);
    const seg = cutSeg(x, Math.floor(M / 3) + 211 * r);
    for (let a = 0; a < AMAX; a++) est[a].push(estimate(seg, WINS[a]));
  }
  const Mpts = KHI - KLO + 1;
  // 対数周波数での当てはめなので、有効点数は sum((x-xbar)^2) で決まる
  let sxx = 0;
  {
    const xs = [];
    for (let k = KLO; k <= KHI; k++) xs.push(Math.log(k));
    const mx = mean(xs);
    for (const v of xs) sxx += (v - mx) * (v - mx);
  }
  for (let a = 0; a < AMAX; a++) {
    const w = WINS[a];
    let s1 = 0, s2 = 0;
    for (let i = 0; i < N; i++) { s1 += w[i]; s2 += w[i] * w[i]; }
    const enbw = N * s2 / (s1 * s1);
    const pred = 1.2825 / Math.sqrt(sxx / enbw);
    const obs = sd(est[a]);
    line(row([a + 1, enbw.toFixed(3), obs.toFixed(4), pred.toFixed(4),
      (obs / pred).toFixed(3)], [8, 14, 16, 22, 10]));
  }
  rule();
  line('★ 予言は 第51回の sd = 1.2825 / sqrt(有効点数)、有効点数 = Sxx/ENBW。');
  line('★ a=1,2 は beta=3 では まだ偏っているので、この sd は意味を持たない。');
  line('★★ 偏りの無い a>=3 では 比が 0.79〜0.88 ── 予言は 15〜20% 大きめ。');
  line('   （周期図の点が 窓のせいで相関しており、ENBW だけでは');
  line('    その相関を過大に見積もるため）使うなら 上限として。');
  line('★★★ alpha を上げると ばらつきは 単調に増える ── ただ上げればよくない。');
}

// =====================================================================
head(5, '偏りと ばらつきを足すと、最良の alpha が決まる');
// =====================================================================
{
  line(row(['真の beta', ...Array.from({ length: AMAX }, (_, i) => 'a=' + (i + 1)), '最良'],
    [10, 8, 8, 8, 8, 8, 8, 8, 8, 8]));
  rule();
  const R = 64;
  for (const beta of [1, 2, 3, 4, 5, 6, 7]) {
    const est = Array.from({ length: AMAX }, () => []);
    for (let r = 0; r < R; r++) {
      _s = 20260918 + 15485863 * r;
      const x = makeSeries(beta);
      const seg = cutSeg(x, Math.floor(M / 3) + 307 * r);
      for (let a = 0; a < AMAX; a++) est[a].push(estimate(seg, WINS[a]));
    }
    const rms = [];
    for (let a = 0; a < AMAX; a++) {
      let s = 0;
      for (const v of est[a]) s += (v - beta) * (v - beta);
      rms.push(Math.sqrt(s / est[a].length));
    }
    let best = 0;
    for (let a = 1; a < AMAX; a++) if (rms[a] < rms[best]) best = a;
    line(row([beta, ...rms.map((v) => v.toFixed(3)), 'a=' + (best + 1)],
      [10, 8, 8, 8, 8, 8, 8, 8, 8, 8]));
  }
  rule();
  line('★ 大筋では 最良の alpha は beta とともに上がる。');
  line('★★★ ただし beta=4 の a=2（0.026）や beta=6 の a=3（0.008）は');
  line('   「偏りが たまたま打ち消し合った」だけ ── beta を知らなければ');
  line('   狙って当てられない。この最小値に乗ってはいけない。');
  line('★★ 安全な目安は 2 alpha >= beta + 2（beta=4 なら a>=3、beta=6 なら a>=4）。');
  line('   beta を知らないと選べないので、01節の走査が要る。');
}

// =====================================================================
head(6, '★★ 手続きにする ── 平らな区間を探し、その幅を系統誤差とする');
// =====================================================================
// 手順：
//   ① alpha = 1..8 で beta-hat を測る
//   ② 隣り合う差が tol 以下で続く いちばん長い区間を探す
//   ③ 値はその平均、系統誤差はその半値幅
//   ④ 統計誤差は 第51回の式（ENBW 込み）
//   ⑤ 二つを二乗和で足して報告する

function procedure(seg, tol) {
  const b = [];
  for (let a = 0; a < AMAX; a++) b.push(estimate(seg, WINS[a]));
  let bi = 0, bj = 0;
  for (let i = 0; i < AMAX; i++) {
    for (let j = i; j < AMAX; j++) {
      let lo = Infinity, hi = -Infinity;
      for (let k = i; k <= j; k++) { lo = Math.min(lo, b[k]); hi = Math.max(hi, b[k]); }
      if (hi - lo <= tol && j - i >= bj - bi) { bi = i; bj = j; }
    }
  }
  let lo = Infinity, hi = -Infinity, s = 0;
  for (let k = bi; k <= bj; k++) { lo = Math.min(lo, b[k]); hi = Math.max(hi, b[k]); s += b[k]; }
  const val = s / (bj - bi + 1);
  const sys = (hi - lo) / 2;
  // 統計誤差は 区間の真ん中の alpha で
  const amid = Math.round((bi + bj) / 2);
  const w = WINS[amid];
  let s1 = 0, s2 = 0;
  for (let i = 0; i < N; i++) { s1 += w[i]; s2 += w[i] * w[i]; }
  const enbw = N * s2 / (s1 * s1);
  let sxx = 0;
  {
    const xs = [];
    for (let k = KLO; k <= KHI; k++) xs.push(Math.log(k));
    const mx = mean(xs);
    for (const v of xs) sxx += (v - mx) * (v - mx);
  }
  const stat = 1.2825 / Math.sqrt(sxx / enbw);
  return { val: val, sys: sys, stat: stat, err: Math.hypot(sys, stat), a0: bi + 1, a1: bj + 1 };
}

{
  const TOL = 0.15, R = 200;
  line('tol = ' + TOL + '、200 realization。名目 68% の区間が 何 % 当たるか');
  line('');
  line(row(['真の beta', '平均の推定', '合計誤差', '|誤差|中央', '|誤差|68%',
    '|誤差|95%', '実測sd', '被覆率[%]'], [10, 11, 10, 11, 11, 11, 10, 11]));
  rule();
  for (const beta of [1, 2, 3, 4, 5, 6, 7]) {
    const vals = [], syss = [], stats = [], errs = [];
    let cover = 0;
    const aLo = [], aHi = [];
    for (let r = 0; r < R; r++) {
      _s = 20260918 + 32452843 * r;
      const x = makeSeries(beta);
      const seg = cutSeg(x, Math.floor(M / 3) + 401 * r);
      const p = procedure(seg, TOL);
      vals.push(p.val); syss.push(p.sys); stats.push(p.stat); errs.push(p.err);
      aLo.push(p.a0); aHi.push(p.a1);
      if (Math.abs(p.val - beta) <= p.err) cover++;
    }
    const obs = sd(vals);
    const ae = vals.map((v) => Math.abs(v - beta)).sort((a, b) => a - b);
    const q = (f) => ae[Math.min(ae.length - 1, Math.floor(f * ae.length))];
    line(row([beta, mean(vals).toFixed(3), mean(errs).toFixed(3),
      q(0.5).toFixed(3), q(0.68).toFixed(3), q(0.95).toFixed(3),
      obs.toFixed(3), (100 * cover / R).toFixed(1)],
      [10, 11, 10, 11, 11, 11, 10, 11]));
  }
  rule();
  line('★ 名目 68% に対して 実測の被覆率は 79〜87% ── 少し 大きめの誤差。');
  line('★★★ ところが 実測 sd は 合計誤差より ずっと大きい（beta=1 で 0.32 対 0.13）。');
  line('   矛盾ではない ── 誤差の分布が 正規分布ではないから。');
  line('★★ |誤差| の 68% 点は 0.08〜0.11 で、報告する合計誤差 0.13 より小さい。');
  line('   ── だから 被覆率が 68% を超える（誤差を 1.4 倍 ほど大きめに出している）。');
  line('★★ 95% 点は 0.18〜0.22（68% 点の 2 倍 ほど）。芯は細いのに、');
  line('   まれに もっと大きく外す ── その稀な外れが sd を 0.2〜0.4 に膨らませている。');
  line('★★★ だから この手続きの誤差は sd で書いてはいけない。');
  line('   「68% がこの幅に入る」と 被覆率で書くのが正しい ──');
  line('   第51回の ln(chi^2_2/2) が 非対称だったのと 同じ理由。');
}

// =====================================================================
head(7, '手続きが破れるところ');
// =====================================================================
{
  line('当てはめ帯域を狭くする（k=64..256）と どうなるか');
  line('');
  const KL0 = KLO, KH0 = KHI;
  const saved = [KLO, KHI];
  void saved;
  line(row(['帯域', '真の beta', '推定', '合計誤差', '被覆率[%]'], [16, 12, 12, 12, 12]));
  rule();
  const bands = [[32, 512], [64, 256], [16, 1024]];
  for (const bd of bands) {
    // KLO/KHI を一時的に差し替える代わりに、局所の estimate を作る
    const est2 = (seg, w) => {
      const re = new Float64Array(N), im = new Float64Array(N);
      for (let i = 0; i < N; i++) re[i] = seg[i] * w[i];
      fft(re, im, false);
      const xs = [], ys = [];
      for (let k = bd[0]; k <= bd[1]; k++) {
        const P = re[k] * re[k] + im[k] * im[k];
        xs.push(Math.log(k)); ys.push(Math.log(P + 1e-300));
      }
      return -slope(xs, ys);
    };
    const proc2 = (seg) => {
      const b = [];
      for (let a = 0; a < AMAX; a++) b.push(est2(seg, WINS[a]));
      let bi = 0, bj = 0;
      for (let i = 0; i < AMAX; i++) for (let j = i; j < AMAX; j++) {
        let lo = Infinity, hi = -Infinity;
        for (let k = i; k <= j; k++) { lo = Math.min(lo, b[k]); hi = Math.max(hi, b[k]); }
        if (hi - lo <= 0.15 && j - i >= bj - bi) { bi = i; bj = j; }
      }
      let lo = Infinity, hi = -Infinity, s = 0;
      for (let k = bi; k <= bj; k++) { lo = Math.min(lo, b[k]); hi = Math.max(hi, b[k]); s += b[k]; }
      const w = WINS[Math.round((bi + bj) / 2)];
      let s1 = 0, s2 = 0;
      for (let i = 0; i < N; i++) { s1 += w[i]; s2 += w[i] * w[i]; }
      const enbw = N * s2 / (s1 * s1);
      const xs = [];
      for (let k = bd[0]; k <= bd[1]; k++) xs.push(Math.log(k));
      const mx = mean(xs);
      let sxx = 0; for (const v of xs) sxx += (v - mx) * (v - mx);
      const stat = 1.2825 / Math.sqrt(sxx / enbw);
      const sys = (hi - lo) / 2;
      return { val: s / (bj - bi + 1), err: Math.hypot(sys, stat) };
    };
    for (const beta of [3, 6]) {
      const vals = [], errs = [];
      let cover = 0;
      const R = 200;
      for (let r = 0; r < R; r++) {
        _s = 20260918 + 32452843 * r;
        const x = makeSeries(beta);
        const seg = cutSeg(x, Math.floor(M / 3) + 401 * r);
        const p = proc2(seg);
        vals.push(p.val); errs.push(p.err);
        if (Math.abs(p.val - beta) <= p.err) cover++;
      }
      line(row(['k=' + bd[0] + '..' + bd[1], beta, mean(vals).toFixed(3),
        mean(errs).toFixed(3), (100 * cover / R).toFixed(1)], [16, 12, 12, 12, 12]));
    }
  }
  rule();
  void KL0; void KH0;
  line('★ 帯域を変えると 被覆率も動く ── 手続きは帯域の選び方に依存する。');
  line('★★ つまり この手続きも「仮定つき」（第55回）。');
  line('   仮定は ①当てはめ帯域 ②tol ③窓の族 の三つ。');
}

// =====================================================================
head(8, 'まとめ');
// =====================================================================
const SUM = [
  ['★ 行きすぎの正体', '分解能より低い周波数の漏れ', '本稿の計算'],
  ['★★ 対策', '1〜2 次のトレンドを引く', '本稿の提案'],
  ['平滑化の偏り', '+0.002〜0.008（無視できる）', '予想外れ'],
  ['大きい alpha を止めるもの', '偏りでなく ばらつき', '本稿の計算'],
  ['ばらつきの予言', '0.79〜0.88 倍（予言が大きめ）', '第51回＋本稿'],
  ['安全な alpha', '2 alpha >= beta + 2', '本稿の主張'],
  ['★★ 手続き', '平らな区間の半値幅を系統誤差に', '本稿の提案'],
  ['手続きの被覆率', '79〜87%（名目 68%）', '本稿の実測'],
  ['★ 誤差の分布', '芯は細く 裾は重い', '本稿の計算'],
  ['報告の仕方', 'sd ではなく 被覆率で', '本稿の主張'],
  ['手続きの仮定', '帯域・tol・窓の族 の 3 つ', '本稿の確認'],
  ['実データでの検証', '未着手', '合成のみ'],
];
line(row(['項目', '値', '根拠'], [22, 32, 14]));
rule();
for (const s of SUM) line(row(s, [22, 32, 14]));
rule();
line('');
line('★★★ 系統誤差は「見積もる」ものではなく「測る」ものにできた。');
line('    窓を変えて動かし、動かない区間を探せばよい。');
line('★★★ そして いちばん効いたのは 窓ではなく トレンド除去だった ──');
line('    漏れの主役は「記録の中では傾きにしか見えない成分」。');
line('★★ ただし この手続き自体が 仮定つき ── 第55回の言うとおり、');
line('    仮定を数えて 一緒に書く必要がある。');
line('');
