// 考える波 第 41 回：トポロジカルな波
//   一方向にしか進めない波 ── 巻き数・チャーン数・端の枝
//   node topo.js
'use strict';

function f(x, n) { return Number(x).toFixed(n === undefined ? 6 : n); }
function e(x, n) { return Number(x).toExponential(n === undefined ? 4 : n); }
function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
function padl(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
function head(t) { console.log('\n' + '='.repeat(72) + '\n' + t + '\n' + '='.repeat(72)); }

function mulberry32(a) {
  return function () {
    a |= 0; a = a + 0x6D2B79F5 | 0;
    let t = Math.imul(a ^ a >>> 15, 1 | a);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}

// ---- 実対称行列のヤコビ法（固有値と固有ベクトル） ----
function jacobi(Ain, maxSweep) {
  const n = Ain.length;
  const A = Ain.map(r => r.slice());
  const V = [];
  for (let i = 0; i < n; i++) { V.push(new Array(n).fill(0)); V[i][i] = 1; }
  for (let sweep = 0; sweep < (maxSweep || 60); sweep++) {
    let off = 0;
    for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) off += A[i][j] * A[i][j];
    if (off < 1e-26) break;
    for (let p = 0; p < n; p++) for (let q = p + 1; q < n; q++) {
      if (Math.abs(A[p][q]) < 1e-18) continue;
      const theta = (A[q][q] - A[p][p]) / (2 * A[p][q]);
      const t = Math.sign(theta || 1) / (Math.abs(theta) + Math.sqrt(theta * theta + 1));
      const c = 1 / Math.sqrt(t * t + 1), s = t * c;
      for (let k = 0; k < n; k++) {
        const akp = A[k][p], akq = A[k][q];
        A[k][p] = c * akp - s * akq; A[k][q] = s * akp + c * akq;
      }
      for (let k = 0; k < n; k++) {
        const apk = A[p][k], aqk = A[q][k];
        A[p][k] = c * apk - s * aqk; A[q][k] = s * apk + c * aqk;
      }
      for (let k = 0; k < n; k++) {
        const vkp = V[k][p], vkq = V[k][q];
        V[k][p] = c * vkp - s * vkq; V[k][q] = s * vkp + c * vkq;
      }
    }
  }
  const idx = [];
  for (let i = 0; i < n; i++) idx.push(i);
  idx.sort((a, b) => A[a][a] - A[b][b]);
  return { val: idx.map(i => A[i][i]), vec: idx.map(i => V.map(r => r[i])) };
}

console.log('考える波 第 41 回 ── トポロジカルな波');
console.log('一方向にしか進めない波は、乱れても止まらない');

// ============================================================
head('1. 巻き数は整数しか取れない ── SSH 模型');
// ============================================================
// h(k) = (v + w cos k , w sin k) 。原点の周りを何周するか
function winding(v, w, N) {
  let tot = 0, prev = Math.atan2(w * Math.sin(0), v + w * Math.cos(0));
  for (let i = 1; i <= N; i++) {
    const k = 2 * Math.PI * i / N;
    const th = Math.atan2(w * Math.sin(k), v + w * Math.cos(k));
    let d = th - prev; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI;
    tot += d; prev = th;
  }
  return tot / (2 * Math.PI);
}
console.log('');
console.log('  h(k) = (v + w cos k , w sin k) が原点の周りを回る回数');
console.log('');
console.log('  ' + pad('v', 8) + pad('w', 8) + padl('巻き数（数値積分）', 22)
  + padl('ギャップ |v-w|', 16) + '  相');
for (const [v, w] of [[1, 0.2], [1, 0.9], [1, 0.999], [1, 1.001], [1, 1.1], [1, 5], [1, 1]]) {
  const W = winding(v, w, 200000);
  const gap = Math.abs(v - w);
  const phase = (gap < 1e-9) ? '★ ギャップが閉じている（巻き数が定義できない）'
    : (w > v ? '★ トポロジカル' : '自明');
  console.log('  ' + pad(f(v, 3), 8) + pad(f(w, 3), 8) + padl(f(W, 9), 22)
    + padl(e(gap, 2), 16) + '  ' + phase);
}
console.log('');
console.log('  ★ v と w をどれだけ細かく変えても、巻き数は 0 か 1 しか取らない');
console.log('  ★ 変わるのは ギャップが閉じる v = w だけ ── 連続変形では跨げない');

// ============================================================
head('2. 巻き数が 1 なら、端に状態が出る ── バルク＝端対応');
// ============================================================
function sshChain(N, v, w, siteDis, hopDis, seed) {
  const rnd = mulberry32(seed);
  const n = 2 * N;
  const H = []; for (let i = 0; i < n; i++) H.push(new Array(n).fill(0));
  for (let i = 0; i < n - 1; i++) {
    const base = (i % 2 === 0) ? v : w;
    const t = base * (1 + hopDis * (rnd() * 2 - 1));
    H[i][i + 1] = t; H[i + 1][i] = t;
  }
  for (let i = 0; i < n; i++) H[i][i] = siteDis * (rnd() * 2 - 1);
  return jacobi(H);
}
console.log('');
console.log('  有限の鎖（N = 40 単位胞、80 サイト）の固有値。E = 0 付近を見る');
console.log('');
console.log('  ' + pad('v', 8) + pad('w', 8) + padl('|E| が最小の 4 個', 46) + '  端状態');
for (const [v, w] of [[1, 0.5], [1, 0.9], [1, 1.1], [1, 2.0]]) {
  const r = sshChain(40, v, w, 0, 0, 1);
  const s = r.val.slice().sort((a, b) => Math.abs(a) - Math.abs(b)).slice(0, 4);
  console.log('  ' + pad(f(v, 2), 8) + pad(f(w, 2), 8)
    + padl(s.map(x => e(Math.abs(x), 1)).join('  '), 46)
    + '  ' + (w > v ? '★ 2 個ある' : 'なし'));
}
// 端状態の局在長
console.log('');
console.log('  端状態の局在長（理論 1 / ln(w/v)）');
console.log('  ' + pad('w/v', 10) + padl('実測 xi', 16) + padl('1/ln(w/v)', 16) + padl('比', 10));
for (const w of [1.5, 2.0, 3.0, 5.0]) {
  const r = sshChain(60, 1, w, 0, 0, 1);
  // E=0 に最も近い状態
  let bi = 0, bv = Infinity;
  for (let i = 0; i < r.val.length; i++) if (Math.abs(r.val[i]) < bv) { bv = Math.abs(r.val[i]); bi = i; }
  const psi = r.vec[bi];
  // 左端からの減衰を対数の傾きで測る（偶サイトのみ。奇サイトは振幅ゼロ）
  const xs = [], ys = [];
  for (let i = 0; i < 40; i += 2) {
    const a = Math.abs(psi[i]);
    if (a > 1e-12) { xs.push(i / 2); ys.push(Math.log(a)); }
  }
  let sx = 0, sy = 0, sxx = 0, sxy = 0, m = xs.length;
  for (let i = 0; i < m; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
  const slope = (m * sxy - sx * sy) / (m * sxx - sx * sx);
  const xi = -1 / slope;
  const th = 1 / Math.log(w);
  console.log('  ' + pad(f(w, 2), 10) + padl(f(xi, 6), 16) + padl(f(th, 6), 16)
    + padl(f(xi / th, 5), 10));
}

// ============================================================
head('3. ★ 守られているのは何か ── 乱れの種類で答えが変わる');
// ============================================================
console.log('');
console.log('  同じ鎖（v=1, w=2）に二種類の乱れを入れて、E=0 の状態がどうなるか');
console.log('');
console.log('  ' + pad('乱れ', 26) + padl('|E| が最小の 2 個', 34) + '  判定');
for (const [lab, sd, hd] of [
  ['乱れなし', 0, 0],
  ['ホッピングに 30 %', 0, 0.3],
  ['ホッピングに 60 %', 0, 0.6],
  ['サイトに 0.05', 0.05, 0],
  ['サイトに 0.3', 0.3, 0],
]) {
  const r = sshChain(40, 1, 2, sd, hd, 99);
  const s = r.val.slice().sort((a, b) => Math.abs(a) - Math.abs(b)).slice(0, 2);
  const ok = Math.abs(s[1]) < 1e-9;
  console.log('  ' + pad(lab, 26) + padl(s.map(x => e(Math.abs(x), 2)).join('   '), 34)
    + '  ' + (ok ? '★ E=0 のまま' : '★ E=0 から外れた'));
}
console.log('');
console.log('  ★★ 守っているのは「対称性」です ── ホッピングだけの乱れは');
console.log('  ★★ 副格子対称性（カイラル対称性）を壊さないので E=0 が動かない。');
console.log('  ★★ サイトの乱れはその対称性を壊すので、すぐに動く。');
console.log('  ★ 「トポロジカルだから何にでも強い」わけではない ── 何に強いかが決まっている');

// ============================================================
head('4. 二次元のチャーン数 ── 球面を何回覆うか');
// ============================================================
// QWZ 模型： d(k) = (sin kx , sin ky , m + cos kx + cos ky)
function dvec(kx, ky, m) {
  return [Math.sin(kx), Math.sin(ky), m + Math.cos(kx) + Math.cos(ky)];
}
function chern(m, N) {
  const h = 2 * Math.PI / N; let C = 0;
  for (let i = 0; i < N; i++) for (let j = 0; j < N; j++) {
    const kx = -Math.PI + (i + 0.5) * h, ky = -Math.PI + (j + 0.5) * h;
    const d = dvec(kx, ky, m);
    const dx = dvec(kx + h / 2, ky, m), dxm = dvec(kx - h / 2, ky, m);
    const dy = dvec(kx, ky + h / 2, m), dym = dvec(kx, ky - h / 2, m);
    const nrm = (v) => { const L = Math.hypot(v[0], v[1], v[2]); return [v[0] / L, v[1] / L, v[2] / L]; };
    const n0 = nrm(d);
    const a = nrm(dx), b = nrm(dxm), c = nrm(dy), e2 = nrm(dym);
    const px = [(a[0] - b[0]) / h, (a[1] - b[1]) / h, (a[2] - b[2]) / h];
    const py = [(c[0] - e2[0]) / h, (c[1] - e2[1]) / h, (c[2] - e2[2]) / h];
    const cr = [px[1] * py[2] - px[2] * py[1], px[2] * py[0] - px[0] * py[2],
                px[0] * py[1] - px[1] * py[0]];
    C += (n0[0] * cr[0] + n0[1] * cr[1] + n0[2] * cr[2]) * h * h;
  }
  return C / (4 * Math.PI);
}
function gapMin(m, N) {
  let g = Infinity;
  for (let i = 0; i < N; i++) for (let j = 0; j < N; j++) {
    const kx = -Math.PI + 2 * Math.PI * i / N, ky = -Math.PI + 2 * Math.PI * j / N;
    const d = dvec(kx, ky, m);
    g = Math.min(g, 2 * Math.hypot(d[0], d[1], d[2]));
  }
  return g;
}
console.log('');
console.log('  d(k) = (sin kx , sin ky , m + cos kx + cos ky)');
console.log('  チャーン数 = (1/4pi) ∫ n·(∂x n × ∂y n) dkx dky ── 球面を覆う回数');
console.log('');
console.log('  ' + pad('m', 8) + padl('チャーン数（数値積分）', 24) + padl('最小ギャップ', 16) + '  相');
for (const m of [-3, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]) {
  const C = chern(m, 900), g = gapMin(m, 400);
  const lab = (g < 1e-3) ? '★ ギャップが閉じる' : (Math.abs(C) > 0.5 ? '★ トポロジカル' : '自明');
  console.log('  ' + pad(f(m, 1), 8) + padl(f(C, 9), 24) + padl(f(g, 6), 16) + '  ' + lab);
}
console.log('');
console.log('  ★ チャーン数も整数しか取らない。変わるのは ギャップが閉じる m = -2, 0, 2 だけ');

// ============================================================
head('5. 端のバンド ── ギャップを横切る枝の数');
// ============================================================
// y 方向を開放（Ny 段）、x 方向に kx。実対称行列になる
function stripH(kx, Ny, m) {
  const n = 2 * Ny;
  const H = []; for (let i = 0; i < n; i++) H.push(new Array(n).fill(0));
  const on = [[m + Math.cos(kx), Math.sin(kx)], [Math.sin(kx), -(m + Math.cos(kx))]];
  const T = [[0.5, -0.5], [0.5, -0.5]];   // y -> y+1
  for (let y = 0; y < Ny; y++) {
    for (let a = 0; a < 2; a++) for (let b = 0; b < 2; b++) H[2 * y + a][2 * y + b] += on[a][b];
    if (y + 1 < Ny) {
      for (let a = 0; a < 2; a++) for (let b = 0; b < 2; b++) {
        H[2 * y + a][2 * (y + 1) + b] += T[a][b];
        H[2 * (y + 1) + b][2 * y + a] += T[a][b];
      }
    }
  }
  return H;
}
{
  const Ny = 24, m = -1.0;
  console.log('');
  console.log('  m = ' + m + '（チャーン数 ' + f(chern(m, 900), 3) + '）、y 方向 ' + Ny + ' 段');
  console.log('  バルクのバンドは |E| >= 1。ギャップの中（|E| < 0.9）の状態を端で分けて数える');
  console.log('');
  console.log('  ' + pad('kx/pi', 10) + padl('左端の状態の E', 20) + padl('右端の状態の E', 20));
  const KX = [];
  for (let i = 0; i <= 120; i++) KX.push(-Math.PI + 2 * Math.PI * i / 120);
  const leftE = [], rightE = [];
  for (const kx of KX) {
    const r = jacobi(stripH(kx, Ny, m));
    let le = null, re = null;
    for (let i = 0; i < r.val.length; i++) {
      if (Math.abs(r.val[i]) > 0.9) continue;
      const p = r.vec[i];
      let com = 0, tot = 0;
      for (let y = 0; y < Ny; y++) {
        const wgt = p[2 * y] * p[2 * y] + p[2 * y + 1] * p[2 * y + 1];
        com += y * wgt; tot += wgt;
      }
      com /= tot;
      if (com < Ny / 3) { if (le === null || Math.abs(r.val[i]) < Math.abs(le)) le = r.val[i]; }
      else if (com > 2 * Ny / 3) { if (re === null || Math.abs(r.val[i]) < Math.abs(re)) re = r.val[i]; }
    }
    leftE.push(le); rightE.push(re);
  }
  for (let i = 0; i <= 120; i += 8) {
    console.log('  ' + pad(f(KX[i] / Math.PI, 3), 10)
      + padl(leftE[i] === null ? '-' : f(leftE[i], 6), 20)
      + padl(rightE[i] === null ? '-' : f(rightE[i], 6), 20));
  }

  // 群速度の符号を数える
  head('6. ★ 同じ端では、群速度が一方向しかない');
  let pos = 0, neg = 0, cnt = 0;
  for (let i = 1; i < KX.length; i++) {
    if (leftE[i] === null || leftE[i - 1] === null) continue;
    const dv = (leftE[i] - leftE[i - 1]) / (KX[i] - KX[i - 1]);
    if (Math.abs(dv) < 1e-6) continue;
    cnt++; if (dv > 0) pos++; else neg++;
  }
  console.log('');
  console.log('  左端の枝の群速度 dE/dkx の符号（ギャップ内の ' + cnt + ' 点で測定）');
  console.log('  ' + pad('正（右へ進む）', 22) + padl(pos, 8));
  console.log('  ' + pad('負（左へ進む）', 22) + padl(neg, 8));
  console.log('');
  if (pos === 0 || neg === 0) {
    console.log('  ★★★ 片方しかない ── 左端の波は 一方向にしか進めない');
  } else {
    console.log('  ★ 両方あった（' + pos + ' 対 ' + neg + '）── 一方向ではない');
  }
  let posR = 0, negR = 0;
  for (let i = 1; i < KX.length; i++) {
    if (rightE[i] === null || rightE[i - 1] === null) continue;
    const dv = (rightE[i] - rightE[i - 1]) / (KX[i] - KX[i - 1]);
    if (Math.abs(dv) < 1e-6) continue;
    if (dv > 0) posR++; else negR++;
  }
  console.log('  右端： 正 ' + posR + ' 、 負 ' + negR + '  ── 左端と逆向き');
  console.log('');
  console.log('  ★ 後方散乱するには「同じ端・同じエネルギーで逆向きの状態」が要る。');
  console.log('  ★ それが存在しないので、乱れがあっても跳ね返れない。');
}

// ============================================================
head('7. 第 37 回の局在と、どう折り合うか');
// ============================================================
console.log('');
console.log('  第 37 回：1 次元ではどんなに弱い乱れでも必ず局在する（後方散乱の重ね合わせ）');
console.log('  本回　 ：端の枝には逆向きの状態が無い → 後方散乱そのものが起きない');
console.log('');
console.log('  ★ 矛盾しません。第 37 回の前提は「前と後ろの両方に進める」ことでした。');
console.log('  ★ 片方向しか無い波は、その前提の外に居ます。');
console.log('');
console.log('  ★ ただし 03 節で見たとおり ── 守られる乱れの種類は決まっています。');
console.log('  ★ 「端の枝を別の端へ繋いでしまう」ほど強い乱れなら、やはり止まります。');

// ============================================================
head('8. 本回のまとめ');
// ============================================================
const rows = [
  ['巻き数は整数しか取らない', '◎ 数値', '★ 0 か 1。v=w でしか変わらない'],
  ['巻き数 1 → 端に E=0 が 2 個', '◎ 数値', 'バルク＝端対応'],
  ['端状態の局在長 1/ln(w/v)', '◎ 数値', '実測と一致'],
  ['★ 守るのは対称性', '◎ 数値', '★ ホッピングの乱れ○、サイト×'],
  ['チャーン数も整数', '◎ 数値', '0, ±1。m=-2,0,2 で跳ぶ'],
  ['★ 端の枝は一方向のみ', '◎ 数値', '★ 群速度の符号が片側だけ'],
  ['だから後方散乱できない', '◎ 論理', '第 37 回の前提が成り立たない'],
  ['★ 実際の物質で何が起きるか', '× 扱えない', '★ 本稿は模型のみ'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 32) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 「乱れても止まらない波」の正体は、強い波ではなく');
console.log('  ★ 「後ろに進む道が無い」波だった。');
console.log('  ★ そして道の数を数えているのが、整数（巻き数・チャーン数）。');
