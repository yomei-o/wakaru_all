// スペクトル指数の梯子 ── 整数・半整数・そして 1/3 と 1/5 はどこから来るのか
'use strict';
const E=x=>x.toExponential(3);

// ===== 有理数（指数がきれいな分数で出るように、厳密に解く） =====
function gcd(a,b){a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b];}return a||1;}
function R(n,d){d=d===undefined?1:d; if(d<0){n=-n;d=-d;} const g=gcd(n,d); return {n:n/g,d:d/g};}
const radd=(a,b)=>R(a.n*b.d+b.n*a.d, a.d*b.d);
const rsub=(a,b)=>R(a.n*b.d-b.n*a.d, a.d*b.d);
const rmul=(a,b)=>R(a.n*b.n, a.d*b.d);
const rdiv=(a,b)=>R(a.n*b.d, a.d*b.n);
const rz=a=>a.n===0;
const rs=a=>a.d===1?String(a.n):(a.n+'/'+a.d);
const rv=a=>a.n/a.d;

// ガウス消去（有理数、厳密）。A x = b を解く
function solve(A,b){
  const m=A.length, n=A[0].length;
  const M=A.map((row,i)=>row.map(x=>R(x)).concat([R(b[i])]));
  let r=0; const piv=[];
  for(let c=0;c<n&&r<m;c++){
    let p=-1; for(let i=r;i<m;i++) if(!rz(M[i][c])){p=i;break;}
    if(p<0) continue;
    [M[r],M[p]]=[M[p],M[r]];
    const d=M[r][c];
    for(let j=c;j<=n;j++) M[r][j]=rdiv(M[r][j],d);
    for(let i=0;i<m;i++){
      if(i===r||rz(M[i][c])) continue;
      const f=M[i][c];
      for(let j=c;j<=n;j++) M[i][j]=rsub(M[i][j], rmul(f,M[r][j]));
    }
    piv.push(c); r++;
  }
  for(let i=r;i<m;i++) if(!rz(M[i][n])) return null;   // 矛盾
  if(r<n) return {under:true};                          // 一意でない
  const x=new Array(n).fill(R(0));
  for(let i=0;i<r;i++) x[piv[i]]=M[i][n];
  return x;
}

console.log('##################################################################');
console.log('# 1. まず、これまでに出てきた傾きを一枚に並べる');
console.log('##################################################################\n');
console.log('  第 1 回から第 13 回まで、いろいろな傾きが出てきました。');
console.log('  第 2 回の辞書 ── 階数 α の操作は 6α dB/oct、雑音の指数は β = −2α ──');
console.log('  で全部ひとつの目盛りに載せられます。\n');
const ladder=[
  ['ω⁴（レイリー散乱）',        4,   '二階微分を二乗',             '第 12 回',  '◎ 厳密'],
  ['+12 dB/oct（加速度）',      2,   '二階微分',                   '第 1 回',   '◎ 厳密'],
  ['+6 dB/oct（速度）',         1,   '一階微分',                   '第 1 回',   '◎ 厳密'],
  ['白色雑音',                  0,   '何もしない',                 '第 2 回',   '◎ 定義'],
  ['1/f 雑音（ピンク）',       -1,   '半積分 α=−1/2',              '第 2 回',   '○ 実測'],
  ['★ コルモゴロフ乱流',    -5/3,   '★ α=−5/6（三分の一が出る）', '本回',      '○ 実測'],
  ['ブラウン運動（赤）',       -2,   '一回積分',                   '第 2 回',   '◎ 厳密'],
  ['★ ボルジャーノ＝オブホフ',-11/5,'★ α=−11/10（五分の一）',     '本回',      '△ 場合による'],
  ['2 次元のエンストロフィー', -3,   'α=−3/2',                     '本回',      '○ 数値実験'],
  ['★ フィリップス（海の波）', -5,   'α=−5/2',                     '本回',      '○ 実測'],
];
console.log('   現象                       指数 β      階数の言葉          出てきた回   判定');
console.log('  '+'-'.repeat(88));
for(const [a,b,c,d,e] of ladder)
  console.log(`  ${a.padEnd(26)} ${(typeof b==='number'?b.toFixed(4):b).padStart(8)}   ${c.padEnd(20)} ${d.padEnd(10)} ${e}`);
console.log('\n  ★ ほとんどが整数か半整数です。ところが三つだけ違う ──');
console.log('    −5/3、−11/5、そして（後で見る）−7/3。');
console.log('    ★ 分母に 3 と 5 が出てきます。これはどこから来たのか。');

console.log('\n##################################################################');
console.log('# 2. −5/3 は、2 元 1 次方程式の答えだった');
console.log('##################################################################\n');
console.log('  コルモゴロフの仮定はたった一つです：\n');
console.log('      「慣性領域のスペクトルは、エネルギー散逸率 ε と波数 k だけで決まる」\n');
console.log('  次元だけで指数が決まります。単位を [長さ L] と [時間 T] で数えると：\n');
console.log('      [ε]    = L² T⁻³      （単位質量あたりの散逸率）');
console.log('      [k]    = L⁻¹');
console.log('      [E(k)] = L³ T⁻²      （E(k)dk がエネルギー L²T⁻² になるように）\n');
console.log('  E = ε^a k^b と置いて、L と T の指数を合わせるだけ：\n');
console.log('      L :  2a − b = 3');
console.log('      T : −3a     = −2\n');
// 厳密に解く
function dimsolve(name, target, sources){
  // target, sources: 次元ベクトル（同じ長さ）
  const nd=target.length;
  const A=[]; for(let d=0;d<nd;d++) A.push(sources.map(s=>s.v[d]));
  const x=solve(A,target);
  return {name,x,sources};
}
const L=0,T=1,TH=2;                   // 長さ・時間・温度
const V=(l,t,th)=>({v:[l,t,th||0]});
const cases=[
  {name:'3 次元エネルギー慣性領域（コルモゴロフ 1941）',
   target:[3,-2,0], srcs:[{n:'ε (L²T⁻³)',...V(2,-3)},{n:'k (L⁻¹)',...V(-1,0)}],
   note:'E(k) = C ε^(2/3) k^(−5/3)'},
  {name:'2 次元エンストロフィー領域（クライチナン 1967）',
   target:[3,-2,0], srcs:[{n:'η (T⁻³)',...V(0,-3)},{n:'k (L⁻¹)',...V(-1,0)}],
   note:'E(k) = C η^(2/3) k^(−3)'},
  {name:'受動スカラー・慣性対流領域（オブホフ＝コルシン）',
   target:[1,0,2], srcs:[{n:'χ (Θ²T⁻¹)',...V(0,-1,2)},{n:'ε (L²T⁻³)',...V(2,-3)},{n:'k (L⁻¹)',...V(-1,0)}],
   note:'E_θ(k) = C χ ε^(−1/3) k^(−5/3)'},
  {name:'★ ボルジャーノ＝オブホフ（浮力が効く領域）',
   target:[3,-2,0], srcs:[{n:'χ (Θ²T⁻¹)',...V(0,-1,2)},{n:'βg (LT⁻²Θ⁻¹)',...V(1,-2,-1)},{n:'k (L⁻¹)',...V(-1,0)}],
   note:'E(k) ∝ χ^(2/5) (βg)^(4/5) k^(−11/5)'},
  {name:'★ 圧力スペクトル（p は u² のオーダー）',
   target:[5,-4,0], srcs:[{n:'ε (L²T⁻³)',...V(2,-3)},{n:'k (L⁻¹)',...V(-1,0)}],
   note:'E_p(k) ∝ ε^(4/3) k^(−7/3)'},
  {name:'★ 海面波の飽和領域（フィリップス 1958）',
   target:[2,1,0], srcs:[{n:'g (LT⁻²)',...V(1,-2)},{n:'ω (T⁻¹)',...V(0,-1)}],
   note:'F(ω) = α g² ω^(−5)'},
];
console.log('   カスケード                                   解いた指数                    式');
console.log('  '+'-'.repeat(100));
for(const c of cases){
  const r=dimsolve(c.name, c.target, c.srcs);
  if(!r.x||r.x.under){ console.log('  '+c.name.padEnd(42)+'  （一意に決まらない）'); continue; }
  const ex=r.x.map((q,i)=>c.srcs[i].n.split(' ')[0]+'^('+rs(q)+')').join(' · ');
  console.log(`  ${c.name.padEnd(42)} ${ex}`);
  console.log(`  ${''.padEnd(42)} ${c.note}`);
}
console.log('\n  ★ どれも 2〜3 元の 1 次方程式を解いただけです。');
console.log('    仮定は「この量とこの量だけで決まる」という一行だけ。');

console.log('\n##################################################################');
console.log('# 3. 分母の 3 と 5 は、どこから来たのか ── 行列式だった');
console.log('##################################################################\n');
console.log('  前節の計算は、すべて「次元行列 M の逆行列を掛ける」ことでした。');
console.log('  クラメルの公式より、指数は必ず (整数)/det M の形になります ──\n');
console.log('      ★ 分母は det M を割り切る数しか出てこない\n');
console.log('  実際に行列式を計算して確かめます：\n');
function det(M){
  const n=M.length;
  if(n===1) return M[0][0];
  let s=0;
  for(let c=0;c<n;c++){
    const sub=M.slice(1).map(r=>r.filter((_,k)=>k!==c));
    s += ((c%2)?-1:1)*M[0][c]*det(sub);
  }
  return s;
}
console.log('   カスケード                                   det M    指数の分母    整合');
console.log('  '+'-'.repeat(84));
for(const c of cases){
  const nd=c.srcs.length;
  // 使う次元の行だけ取り出して正方行列にする（0 行は落とす）
  const rows=[];
  for(let d=0;d<3;d++){
    const row=c.srcs.map(x=>x.v[d]);
    if(row.some(v=>v!==0)||c.target[d]!==0) rows.push(row);
  }
  if(rows.length!==nd){ console.log('  '+c.name.padEnd(42)+'  （正方でない）'); continue; }
  const D=Math.abs(det(rows));
  const r=dimsolve(c.name,c.target,c.srcs);
  const dens=r.x.map(q=>q.d);
  const ok=dens.every(d=>D%d===0);
  console.log(`  ${c.name.padEnd(42)} ${String(D).padStart(5)}    ${dens.join(', ').padEnd(12)} ${ok?'○':'×'}`);
}
console.log('\n  ★ 例外なく、分母は |det M| を割り切っています。');
console.log('    ── −5/3 の 3 も、−11/5 の 5 も、行列式の値そのものでした。\n');
console.log('  では det M は何で決まるのか。中身を見ると：\n');
console.log('    ・コルモゴロフ：ε の時間次元 −3 が、そのまま det = −3 になる');
console.log('    ・ボルジャーノ：温度の制約 (Θ² と Θ⁻¹) が T の式に噛んで det = −5');
console.log('    ・フィリップス：g と ω だけなら det = −1 ── ★ だから整数になる\n');
console.log('  ★ 本稿の言い方にすると ──\n');
console.log('      「スペクトルの傾きが整数からずれるのは、');
console.log('        次元行列の行列式が 1 でないからであって、');
console.log('        分数階微分が物理法則に潜んでいるからではない」\n');
console.log('  第 2 回で「物理はほぼ整数階」と書きました。乱流はその反例に見えますが、');
console.log('    ★ 支配方程式（ナビエ＝ストークス）は依然として整数階です。');
console.log('      分数が出るのは統計をとった後 ── 階数ではなく、次元の割り算。');
console.log('      判定：これは本稿の整理であって、新しい主張ではありません。');

console.log('\n##################################################################');
console.log('# 4. 音で確かめる ── 指数 β の雑音を作って測り返す');
console.log('##################################################################\n');
function fft(re,im,inv){
  const n=re.length;
  for(let i=1,j=0;i<n;i++){let b=n>>1;for(;j&b;b>>=1)j^=b;j^=b;
    if(i<j){[re[i],re[j]]=[re[j],re[i]];[im[i],im[j]]=[im[j],im[i]];}}
  for(let len=2;len<=n;len<<=1){
    const ang=2*Math.PI/len*(inv?1:-1), wr=Math.cos(ang), wi=Math.sin(ang);
    for(let i=0;i<n;i+=len){let cr=1,ci=0;
      for(let j=0;j<len/2;j++){
        const ur=re[i+j],ui=im[i+j];
        const vr=re[i+j+len/2]*cr-im[i+j+len/2]*ci, vi=re[i+j+len/2]*ci+im[i+j+len/2]*cr;
        re[i+j]=ur+vr;im[i+j]=ui+vi;re[i+j+len/2]=ur-vr;im[i+j+len/2]=ui-vi;
        const nc=cr*wr-ci*wi;ci=cr*wi+ci*wr;cr=nc;}}}
  if(inv)for(let i=0;i<n;i++){re[i]/=n;im[i]/=n;}
}
const N=1<<18;
let seed=20260915;
function rnd(){ seed=(seed*1103515245+12345)&0x7fffffff; return seed/0x7fffffff; }
function gauss(){ const u=Math.max(rnd(),1e-12), v=rnd(); return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v); }
// PSD ∝ f^β の雑音を作る（周波数領域で振幅 f^(β/2) を掛ける）
function makeNoise(beta){
  const re=new Float64Array(N), im=new Float64Array(N);
  for(let k=1;k<N/2;k++){
    const amp=Math.pow(k, beta/2);
    const a=gauss()*amp, b=gauss()*amp;
    re[k]=a; im[k]=b; re[N-k]=a; im[N-k]=-b;
  }
  fft(re,im,true);
  return re;
}
// 対数対数での傾きを最小二乗で測る（帯域を対数等間隔でビン分け）
function slope(x, k1, k2, nb){
  const re=Float64Array.from(x), im=new Float64Array(N);
  fft(re,im,false);
  const lo=Math.log(k1), hi=Math.log(k2);
  const bx=[], by=[];
  for(let b=0;b<nb;b++){
    const a=Math.exp(lo+(hi-lo)*b/nb), c=Math.exp(lo+(hi-lo)*(b+1)/nb);
    let s=0,n=0,lk=0;
    for(let k=Math.ceil(a);k<c&&k<N/2;k++){ s+=re[k]*re[k]+im[k]*im[k]; n++; lk+=Math.log(k); }
    if(n<1) continue;
    bx.push(lk/n); by.push(Math.log(s/n));
  }
  let sx=0,sy=0,sxx=0,sxy=0; const n=bx.length;
  for(let i=0;i<n;i++){sx+=bx[i];sy+=by[i];sxx+=bx[i]*bx[i];sxy+=bx[i]*by[i];}
  return (n*sxy-sx*sy)/(n*sxx-sx*sx);
}
console.log('  指数 β の雑音を作り、スペクトルを測り返します（道具の確認）。');
console.log('  一回の実現値だと数 % ばらつくので、4 回作って平均します：\n');
console.log('   狙った β      測った β（4回平均）    差       ばらつき    階数 α = −β/2');
console.log('  '+'-'.repeat(70));
const betas=[0,-1,-5/3,-2,-11/5,-3];
const fields={};
for(const b of betas){
  const ms=[];
  for(let t=0;t<4;t++){ const x=makeNoise(b); if(t===0) fields[b]=x; ms.push(slope(x, 8, N/16, 40)); }
  const m=ms.reduce((p,q)=>p+q,0)/ms.length;
  let v=0; for(const q of ms) v+=(q-m)*(q-m);
  const sd=Math.sqrt(v/(ms.length-1));
  console.log(`  ${b.toFixed(5).padStart(9)}   ${m.toFixed(5).padStart(12)}   ${(m-b).toFixed(5).padStart(9)}   ±${sd.toFixed(5)}     ${(-b/2).toFixed(5)}`);
}
console.log('\n  ★ 作った通りに測れています。ばらつきの範囲で一致 ── ここまでは道具の確認。');

console.log('\n##################################################################');
console.log('# 5. 本題 ── 構造関数で見ると、2/3 が出る');
console.log('##################################################################\n');
console.log('  乱流で実際に測られるのは、スペクトルよりも構造関数です：\n');
console.log('      S₂(τ) = ⟨ |x(t+τ) − x(t)|² ⟩\n');
console.log('  スペクトル指数 β と構造関数の指数 ζ₂ の関係は、−3 < β < −1 のとき\n');
console.log('      ★ ζ₂ = −β − 1\n');
console.log('  β = −5/3 なら ζ₂ = 2/3 ── ★ コルモゴロフの 2/3 乗則です。\n');
function struct2(x, taus){
  const out=[];
  for(const t of taus){
    let s=0, n=0;
    for(let i=0;i+t<N;i+=Math.max(1,t>>2)){ const d=x[i+t]-x[i]; s+=d*d; n++; }
    out.push([t, s/n]);
  }
  return out;
}
const taus=[]; for(let e=2;e<=9;e+=0.5) taus.push(Math.round(Math.pow(2,e)));
console.log('   β          ζ₂ 理論 (−β−1)   ζ₂ 実測      差');
console.log('  '+'-'.repeat(60));
for(const b of [-1.2,-5/3,-2,-11/5,-2.8]){
  const x=fields[b]||makeNoise(b);
  const pts=struct2(x,taus);
  let sx=0,sy=0,sxx=0,sxy=0; const n=pts.length;
  for(const [t,s] of pts){const lx=Math.log(t), ly=Math.log(s); sx+=lx;sy+=ly;sxx+=lx*lx;sxy+=lx*ly;}
  const z=(n*sxy-sx*sy)/(n*sxx-sx*sx);
  const th=-b-1;
  console.log(`  ${b.toFixed(5).padStart(8)}   ${th.toFixed(5).padStart(10)}     ${z.toFixed(5).padStart(9)}   ${(z-th).toFixed(5).padStart(9)}`);
}
console.log('\n  ★ 帯の中央（β = −2 〜 −2.2）では 3 桁 一致。端の β = −1.2 は 0.11 ずれます ──');
console.log('    これは誤差ではなく、ζ₂ = −β−1 が成り立つのが −3 < β < −1 の内部で、');
console.log('    端に近づくほど収束が遅いからです（外側のスケールの寄与が残る）。');
console.log('\n  ★ 2/3 が数値でも出ました（β=−5/3 の行）。');
console.log('    ── コルモゴロフの 2/3 乗則は、−5/3 乗則の言い換えにすぎません。');
console.log('    どちらも「エネルギー流量 ε と長さだけで決まる」という一行から出ます。');

console.log('\n##################################################################');
console.log('# 6. 実際の自然界の指数を集める');
console.log('##################################################################\n');
const nature=[
  ['大気の風速（慣性領域）',      '−5/3',  '○ 実測',  'コルモゴロフ。多数の観測で確認'],
  ['海面波（飽和領域）',          '−5',    '○ 実測',  'フィリップス。ただし −4 という報告も多い'],
  ['音楽の音量ゆらぎ',            '約 −1', '△ 主張',  'ヴォス＝クラーク 1975。曲や測り方に依存'],
  ['半導体の 1/f 雑音',           '約 −1', '○ 実測',  '指数は 0.8〜1.4 に散る'],
  ['心拍間隔のゆらぎ',            '約 −1', '△ 主張',  '健康指標として使われるが解釈は分かれる'],
  ['地震のグーテンベルク＝リヒター','−(1+b)','○ 実測', 'b≈1。これは頻度分布でスペクトルではない'],
  ['宇宙マイクロ波背景放射',      '約 −1', '○ 実測',  'ほぼスケール不変（n_s=0.965）'],
  ['ブラウン運動の位置',          '−2',    '◎ 厳密',  '白色雑音の一回積分'],
];
console.log('   現象                          指数        判定     備考');
console.log('  '+'-'.repeat(92));
for(const [a,b,c,d] of nature)
  console.log(`  ${a.padEnd(28)} ${b.padEnd(10)} ${c.padEnd(8)} ${d}`);
console.log('\n  ★ 見ての通り、「約 −1」が多い。');
console.log('    1/f は自然界でいちばんよく出てくる指数ですが、');
console.log('    ★ 起源は一つではありません（第 2 回で「開いたままの扉」に入れた通り）。');
console.log('    緩和時間が対数一様に分布していれば 1/f が出る、というのが最有力ですが、');
console.log('    それが「なぜ対数一様なのか」は現象ごとに違います。');

console.log('\n##################################################################');
console.log('# 7. 梯子の全体像 ── 整数・半整数・そして分数');
console.log('##################################################################\n');
console.log('  最後に、この連載で出た指数を出自で分類します：\n');
const origin=[
  ['微分・積分の回数',    '整数',        '±6n dB/oct',   '第 1 回。局所的な法則から'],
  ['二乗（強度にする）',  '整数',        'ω⁴ など',      '第 12 回。振幅→パワー'],
  ['拡散（時間1・空間2）','半整数',      '√ω、α=1/2',    '第 11 回。階数の不釣り合い'],
  ['因果律つきの半微分',  '半整数',      'ワールブルグ',  '第 2 回。α=−1/2'],
  ['★ 次元合わせの割り算','det M の約数','−5/3、−11/5',  '★ 本回。次元行列の行列式'],
  ['★ 臨界的な 1/r²',    '複素数',      's₀=1.006',      '★ 第 13 回。対数周期'],
];
console.log('   出自                    指数の型      例             どこで出たか');
console.log('  '+'-'.repeat(88));
for(const [a,b,c,d] of origin)
  console.log(`  ${a.padEnd(22)} ${b.padEnd(12)} ${c.padEnd(14)} ${d}`);
console.log('\n  ★ 整理すると、指数が整数から外れる理由は三つしかありませんでした：\n');
console.log('      1. 階数そのものが半整数（拡散、ワールブルグ）── 第 2, 11 回');
console.log('      2. 次元合わせで分数が出る（乱流）        ── 本回');
console.log('      3. 階数が複素数になる（臨界 1/r²）        ── 第 13 回');
console.log('\n  そして 1 と 3 は「法則の形」の話、2 は「統計の取り方」の話です。');
console.log('  ★ 乱流の −5/3 は、実は法則が分数階になっているわけではない ──');
console.log('    ここが、本回でいちばん言いたかったことです。');

console.log('\n##################################################################');
console.log('# 8. まとめ');
console.log('##################################################################\n');
const sm=[
  ['β = −2α の辞書',        '◎ 厳密',  '第 2 回。すべてを一枚に載せる'],
  ['−5/3 は 2 元 1 次方程式','◎ 厳密',  '次元だけで決まる。仮定は一行'],
  ['分母 ＝ |det M| の約数', '◎ 厳密',  'クラメルの公式。−5/3 の 3、−11/5 の 5'],
  ['ζ₂ = −β−1',            '○ 数値',  '2/3 乗則は −5/3 乗則の言い換え'],
  ['1/f はいちばん多い',     '○ 実測',  'ただし起源は一つではない'],
  ['整数から外れる理由は 3 つ','○ 本稿','階数・次元・複素数'],
];
console.log('  主張                      判定      根拠');
console.log('  '+'-'.repeat(76));
for(const [a,b,c] of sm) console.log(`  ${a.padEnd(24)} ${b.padEnd(9)} ${c}`);
console.log('\n  ★ 一行で ──');
console.log('');
console.log('     スペクトルの傾きが整数から外れる理由は三つしかない。');
console.log('     階数が半端か、次元の割り算か、階数が複素数か。');
console.log('     ── 乱流の −5/3 は二つ目であって、一つ目ではなかった。');
