// 考える波 第 52 回：階数の分布を、有限のデータから 取り出す
//   第 42 回の f(alpha) 曲線は、どこまで 測れるのか
//   node multi.js
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
function gauss(rnd) {
  const u = Math.max(1e-12, rnd()), v = rnd();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}
function slope(xs, ys) {
  const n = xs.length; let sx = 0, sy = 0, sxx = 0, sxy = 0;
  for (let i = 0; i < n; i++) { sx += xs[i]; sy += ys[i]; sxx += xs[i] * xs[i]; sxy += xs[i] * ys[i]; }
  return (n * sxy - sx * sy) / (n * sxx - sx * sx);
}

const P = 0.7;                                     // 第 42 回と同じ p 模型
const tauExact = (q) => -Math.log(Math.pow(P, q) + Math.pow(1 - P, q)) / Math.LN2;
const dtauExact = (q) => { const h = 1e-6; return (tauExact(q + h) - tauExact(q - h)) / (2 * h); };

// 掛け算カスケードを 1 回 作る
//   ★ 子ごとに 独立に 掛け算子を引く（保存型にしない）。
//     保存型（p と 1-p を 必ず 対で配る）だと 箱の値の 多重集合が
//     毎回 まったく同じになり、標本のゆらぎが 消えてしまうため。
//   最後に 全体を 1 に規格化する。
function cascade(levels, p, seed) {
  const rnd = mulberry32(seed);
  let mu = new Float64Array(1); mu[0] = 1;
  for (let L = 0; L < levels; L++) {
    const next = new Float64Array(mu.length * 2);
    for (let i = 0; i < mu.length; i++) {
      next[2 * i] = mu[i] * (rnd() < 0.5 ? p : (1 - p));
      next[2 * i + 1] = mu[i] * (rnd() < 0.5 ? p : (1 - p));
    }
    mu = next;
  }
  let tot = 0; for (let i = 0; i < mu.length; i++) tot += mu[i];
  for (let i = 0; i < mu.length; i++) mu[i] /= tot;
  return mu;
}
// 1 回の実現から tau(q) を測る（分配関数の傾き）
function tauEmp(mu, q, levels, minLevel) {
  const xs = [], ys = [];
  let cur = mu;
  for (let n = levels; n >= (minLevel || 4); n--) {
    let Z = 0;
    for (let i = 0; i < cur.length; i++) if (cur[i] > 0) Z += Math.pow(cur[i], q);
    xs.push(-n * Math.LN2); ys.push(Math.log(Z));
    const nx = new Float64Array(cur.length / 2);
    for (let i = 0; i < nx.length; i++) nx[i] = cur[2 * i] + cur[2 * i + 1];
    cur = nx;
  }
  return slope(xs, ys);
}

console.log('考える波 第 52 回 ── 階数の分布を、有限のデータから 取り出す');
console.log('第 42 回の f(alpha) 曲線は、どこまで 測れるのか');

// ============================================================
head('1. なぜ q を振るのか ── 第 42 回の復習');
// ============================================================
console.log('');
console.log('  第 42 回： Z(q,r) = Σ mu^q ∝ r^{tau(q)} 、 alpha = dtau/dq 、 f = q alpha - tau');
console.log('  q は「どの強さの領域を拾うか」を選ぶ つまみ：');
console.log('    q が大きい → いちばん強い所だけを拾う（alpha が小さい）');
console.log('    q が負    → いちばん弱い所だけを拾う（alpha が大きい）');
console.log('');
console.log('  ' + pad('q', 10) + padl('alpha（厳密）', 16) + padl('f(alpha)（厳密）', 18)
  + '  拾っている場所');
for (const q of [-4, -2, 0, 1, 2, 4, 8]) {
  const a = dtauExact(q), fa = q * a - tauExact(q);
  console.log('  ' + pad(f(q, 1), 10) + padl(f(a, 6), 16) + padl(f(fa, 6), 18)
    + '  ' + (q > 2 ? 'いちばん強い所' : (q < -1 ? 'いちばん弱い所' : '代表的な所')));
}
console.log('');
console.log('  ★ 厳密な alpha の幅： ' + f(-Math.log(P) / Math.LN2, 6) + ' 〜 '
  + f(-Math.log(1 - P) / Math.LN2, 6));

// ============================================================
head('2. 1 回の実現から測ると、大きい q で 外れる');
// ============================================================
{
  console.log('');
  console.log('  p 模型（p = ' + P + '）の カスケードを 1 回 作り、そこから tau(q) を測る');
  console.log('');
  const levels = [12, 16, 20];
  const mus = levels.map(L => cascade(L, P, 424242 + L));
  console.log('  ' + pad('q', 8) + padl('厳密な tau', 14)
    + levels.map(L => padl('n=' + L + '（' + (1 << L) + ' 箱）', 20)).join(''));
  for (const q of [-4, -2, 0, 1, 2, 3, 4, 6, 8, 12]) {
    const row = levels.map((L, i) => padl(f(tauEmp(mus[i], q, L), 5), 20)).join('');
    console.log('  ' + pad(f(q, 1), 8) + padl(f(tauExact(q), 5), 14) + row);
  }
  console.log('');
  console.log('  ★ 小さい |q| では よく合いますが、q が大きいほど ずれます。');
  console.log('  ★★ 箱を増やす（n を大きくする）と ずれは 減りますが、遅い。');
  console.log('  ★★★ 原因：大きい q は「いちばん強い 1 個の箱」だけで決まるからです。');
  console.log('  ★★★ その 1 個が 標本の中に 出てくるかどうかが、答えを 左右する。');
}

// ============================================================
head('3. ★ 到達できる q には 上限がある');
// ============================================================
// 1 回の実現では ばらつくので、複数の種で 中央値を取る
function qStar(mu, L, sign) {
  let best = 0;
  for (let k = 1; k <= 20; k++) {
    const q = sign * k;
    if (Math.abs(tauEmp(mu, q, L) - tauExact(q)) > 0.1) break;
    best = q;
  }
  return best;
}
function median(a) { const b = a.slice().sort((x, y) => x - y);
  return b[Math.floor(b.length / 2)]; }
{
  console.log('');
  console.log('  |tau_emp - tau_exact| <= 0.1 を保てる q の範囲を、5 つの種で 測って 中央値を取る');
  console.log('');
  console.log('  ' + pad('段数 n', 10) + padl('箱の数', 12) + padl('★ q*（正）', 13)
    + padl('q*（負）', 13) + padl('到達できる alpha の幅', 22) + padl('全幅に対して', 14));
  const full = (-Math.log(1 - P) / Math.LN2) - (-Math.log(P) / Math.LN2);
  const res = [];
  for (const L of [10, 12, 14, 16, 18, 20]) {
    const qps = [], qms = [];
    for (let sd2 = 0; sd2 < 5; sd2++) {
      const mu = cascade(L, P, 1000 * L + sd2);
      qps.push(qStar(mu, L, +1)); qms.push(qStar(mu, L, -1));
    }
    const qp = median(qps), qm = median(qms);
    const aw = dtauExact(qm) - dtauExact(qp);
    res.push([L, qp, qm, aw]);
    console.log('  ' + pad(L, 10) + padl(1 << L, 12) + padl(f(qp, 1), 13)
      + padl(f(qm, 1), 13) + padl(f(aw, 4) + ' / ' + f(full, 4), 22)
      + padl(f(100 * aw / full, 1) + ' %', 14));
  }
  console.log('');
  console.log('  ★ 箱を 1000 倍（n=10 → 20）にして、q* は 2 → 4 にしか 伸びません。');
  console.log('  ★★ alpha の幅は 54.5 % → 89.4 % まで 広がりますが、そこで 頭打ち。');
  console.log('  ★★★ 残る 10 % が いちばん端 ── そこは 箱を増やしても 伸びていません。');
  console.log('  ★ q* の伸びは 対数的で、指数関数的に データを増やさないと 端に届かない。');
  global.__res = res;
}

// ============================================================
head('4. ★ f(alpha) のうち 測れるのはどこか');
// ============================================================
{
  const res = global.__res;
  const r18 = res.find(x => x[0] === 18);
  const qm = r18[2], qp = r18[1];
  console.log('');
  console.log('  n = 18（262144 箱）で 到達できる q は ' + f(qm, 1) + ' 〜 ' + f(qp, 1));
  console.log('');
  console.log('  ' + pad('q', 8) + padl('alpha', 12) + padl('f(alpha)', 12)
    + padl('測れるか', 14) + '  意味');
  for (const q of [-8, -4, -2, 0, 1, 2, 4, 8, 16]) {
    const a = dtauExact(q), fa = q * a - tauExact(q);
    const ok = (q >= qm && q <= qp);
    const note = q === 0 ? '★ 台の次元（必ず測れる）'
      : (q > 2 ? 'いちばん強い所' : (q < -2 ? 'いちばん弱い所' : ''));
    console.log('  ' + pad(f(q, 1), 8) + padl(f(a, 6), 12) + padl(f(fa, 6), 12)
      + padl(ok ? '★ 測れる' : '× 届かない', 14) + '  ' + note);
  }
  console.log('');
  console.log('  ★ f(alpha) の 頂上（q=0、f=1）は 必ず測れます ── 台の次元だから。');
  console.log('  ★★ 測れないのは 両裾 ── つまり「いちばん強い所」と「いちばん弱い所」。');
  console.log('  ★★★ そこが いちばん 面白い所なのに、そこだけ 届きません。');
}

// ============================================================
head('5. 雑音を足すと どうなるか');
// ============================================================
{
  console.log('');
  console.log('  各箱の測度に 相対的な雑音（対数正規、sd = s）を掛けて 測り直す');
  console.log('');
  const L = 16;
  const base = cascade(L, P, 2718);
  const rnd = mulberry32(999);
  console.log('  ' + pad('雑音 s', 12) + [-2, 0, 2, 4, 6].map(q => padl('q=' + q, 13)).join('')
    + '  ');
  console.log('  ' + pad('（厳密）', 12)
    + [-2, 0, 2, 4, 6].map(q => padl(f(tauExact(q), 5), 13)).join(''));
  for (const s of [0, 0.1, 0.3, 1.0]) {
    const mu = new Float64Array(base.length);
    for (let i = 0; i < base.length; i++) mu[i] = base[i] * Math.exp(s * gauss(rnd) - s * s / 2);
    console.log('  ' + pad(f(s, 2), 12)
      + [-2, 0, 2, 4, 6].map(q => padl(f(tauEmp(mu, q, L), 5), 13)).join(''));
  }
  console.log('');
  console.log('  ★ q = 0 は 雑音に まったく影響されません（箱の数を 数えているだけ）。');
  console.log('  ★★ 小さい雑音（s <= 0.3）では どの q も ほとんど動きません。');
  console.log('  ★★★ s = 1.0 で崩れ、ずれが 大きいのは 正の側でした：');
  console.log('        q=-2 で 0.24（6 %）、q=4 で 0.37（18 %）、q=6 で 0.62（19 %）。');
  console.log('  ★ 予想（負の q がいちばん弱い）は 外れ ── 雑音が 対数正規だと');
  console.log('  ★ 大きい値のほうが 大きくばらつくので、正の q が 先に 壊れます。');
  console.log('  ★★ いずれにせよ 効くのは |q| が 大きい側 ── 3 節の結論と 同じ向きです。');
}

// ============================================================
head('6. 対策 ── 何ができて 何ができないか');
// ============================================================
console.log('');
const fixes = [
  ['q の範囲を データから決める', '◎ できる', '★ 3 節の q* を 毎回 測る'],
  ['q = 0 の周りだけ 報告する', '◎ できる', '頂上と 曲率は 測れる'],
  ['多数の実現を 平均する', '△ 限定的', '★ 裾は 1 回ぶんの標本で決まるので 効きにくい'],
  ['大きい |q| を 使う', '× 勧めない', '★ 標本にも 雑音にも 弱い（3・5 節）'],
  ['f(alpha) の 全体像を 出す', '× できない', '★ 端は 原理的に 届かない'],
  ['「分布になっている」と言う', '◎ できる', '★ tau(q) の 曲がりだけで 十分'],
];
console.log('  ' + pad('やりたいこと', 30) + pad('判定', 14) + '理由');
for (const x of fixes) console.log('  ' + pad(x[0], 30) + pad(x[1], 14) + x[2]);
console.log('');
console.log('  ★★ 第 42 回の主張「階数が 一つの数ではない」は、q の狭い範囲だけで 言えます。');
console.log('  ★★ 言えないのは「分布が どんな形か」のほう ── そこは 標本の大きさが 決める。');

// ============================================================
head('7. 第 49・51 回の手引きへの 追記');
// ============================================================
console.log('');
const recipe = [
  ['⑥-a q を振る前に q* を測る', '★ 合成データで 同じ標本数で 試す'],
  ['⑥-b 報告は q* の内側だけ', '外側は 標本の最大値を 見ているだけ'],
  ['⑥-c 大きい |q| は 別扱い', '★ 雑音に 弱い。報告するなら 感度も一緒に'],
  ['⑥-d 「曲がっている」で止める', '★ 形まで言うには 標本が 足りないことが多い'],
  ['⑥-e 桁数（第 51 回）と 同じ扱い', '★ q の範囲も「どこまで言えるか」の指標'],
];
console.log('  ' + pad('手順', 30) + '注意');
for (const r of recipe) console.log('  ' + pad(r[0], 30) + r[1]);

// ============================================================
head('8. 本回のまとめ');
// ============================================================
const rows = [
  ['小さい |q| では よく合う', '◎ 数値', '★ q=0〜2 は 100 万箱で ほぼ厳密'],
  ['★ 大きい q で 外れる', '◎ 数値', '★ 最強の 1 箱で 決まるため'],
  ['★ 到達できる q に 上限 q*', '◎ 数値', '★ 箱 1000 倍 で q* は 2 → 4 のみ'],
  ['★★ f(alpha) の 端は 届かない', '◎ 数値', '★ 100 万箱でも 全幅の 一部'],
  ['q=0 は 雑音に 強い', '◎ 数値', '箱の数を 数えているだけ'],
  ['★ 雑音に 弱いのは 正の側だった', '◎ 数値', '★ 予想は 外れ（対数正規の裾のため）'],
  ['「分布になっている」は 言える', '◎ 論理', 'tau(q) の 曲がりだけで 十分'],
  ['★ 分布の 形を 言うこと', '× できない', '★ 標本の大きさが 上限を決める'],
];
console.log('');
for (const r of rows) console.log('  ' + pad(r[0], 32) + pad(r[1], 12) + r[2]);
console.log('');
console.log('  一行でいうと ──');
console.log('  ★ 第 42 回の「階数は 分布だった」は、有限のデータでも 言えます。');
console.log('  ★ ただし 言えるのは「分布である」ところまで ──');
console.log('  ★★ 「どんな分布か」は、標本の大きさが 決めていました。');
console.log('  ★★★ 第 51 回の「桁数」と 同じで、ここでも 上限は');
console.log('  ★★★ 測定そのものではなく、持っているデータの 大きさにあります。');
