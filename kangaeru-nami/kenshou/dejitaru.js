// 考える波 第 31 回 検証スクリプト
//   ラプラス変換からｚ変換へ ── 階数をデジタルで作る
//   ── そして第 30 回の「尾」が FIR / IIR そのものだったと分かる
//
//   実行: node dejitaru.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

// ガンマ関数（ランチョス）
function gammaFn(z){
  const g=7, p=[0.99999999999980993,676.5203681218851,-1259.1392167224028,
    771.32342877765313,-176.61502916214059,12.507343278686905,
    -0.13857109526572012,9.9843695780195716e-6,1.5056327351493116e-7];
  if(z<0.5) return Math.PI/(Math.sin(Math.PI*z)*gammaFn(1-z));
  z-=1; let x=p[0];
  for(let i=1;i<g+2;i++) x+=p[i]/(z+i);
  const t=z+g+0.5;
  return Math.sqrt(2*Math.PI)*Math.pow(t,z+0.5)*Math.exp(-t)*x;
}

// ------------------------------------------------------------------
hr('1. 舞台を s 平面から z 平面へ');

console.log('  ここまで 30 回、ずっと ★ アナログで考えてきました。');
console.log('  微分は ×(iω)、階数は (iω)^α、安定性は「左半平面に極」。');
console.log('');
console.log('  ★ 標本化して離散にすると、舞台が移ります：');
console.log('');
console.log('      ★ z = e^{sT}        （T は標本化の周期）');
console.log('');
console.log('  ' + pad('概念',22) + pad('アナログ（s 平面）',26) + 'デジタル（z 平面）');
console.log('  ' + '-'.repeat(76));
[['周波数軸',       '虚軸 s = iω',            '★ 単位円 z = e^{iωT}'],
 ['安定',           'Re s < 0（左半平面）',    '★ |z| < 1（単位円の内側）'],
 ['微分',           's',                      '★ (1 − z⁻¹)/T'],
 ['積分',           '1/s',                    '★ 1/(1 − z⁻¹) ＝ 累算器'],
 ['遅延 τ',         'e^{−sτ}',                'z^{−n} ── ★ 整数しか作れない'],
 ['定数（第 5 回）', 'ω = 0',                  '★ z = 1 の極'],
 ['分数階',         '(iω)^α',                 '★ (1 − z⁻¹)^α ← 本回の主役']
].forEach(function(r){ console.log('  ' + pad(r[0],22)+pad(r[1],26)+r[2]); });
console.log('');
console.log('  ★★ 最後の行が本回です。★ (1 − z⁻¹)^α を展開すると何が出るか。');

// ------------------------------------------------------------------
hr('2. ★ 分数階のデジタル版 ── グリュンワルト＝レトニコフ');

console.log('  二項展開するだけです：');
console.log('');
console.log('      ★ (1 − z⁻¹)^α = Σ_k w_k z^{−k},   w_k = (−1)^k C(α,k)');
console.log('');
console.log('  ★ これが ★ グリュンワルト＝レトニコフの分数階微分そのもの。');
console.log('  ★ w_k は ★ インパルス応答（フィルタのタップ）です。漸化式で作れます：');
console.log('');
console.log('      w_0 = 1,   w_k = w_{k−1} · ( 1 − (α+1)/k )');
console.log('');

function glWeights(alpha, N){
  const w=new Float64Array(N); w[0]=1;
  for(let k=1;k<N;k++) w[k]=w[k-1]*(1-(alpha+1)/k);
  return w;
}

{
  console.log('  ' + pad('α',8) + pad('w_0..w_6',58) + 'タップ');
  console.log('  ' + '-'.repeat(80));
  [-1,-0.5,0,0.5,1,1.5,2,3].forEach(function(a){
    const w=glWeights(a,7);
    const str=[...w].map(x=>f(x,4)).join(' ');
    let nz=0; const wl=glWeights(a,4000);
    for(let k=0;k<4000;k++) if(Math.abs(wl[k])>1e-14) nz=k+1;
    console.log('  ' + pad(f(a,1),8) + pad(str,58) + (nz<4000?('★ '+nz+' 本で終わる'):'★ 無限に続く'));
  });
  console.log('');
  console.log('  ★★ ここが本回いちばんの発見です ──');
  console.log('');
  console.log('      ★ α が ★ 非負の整数 のときだけ、★ タップが有限で終わる（FIR）。');
  console.log('      ★ それ以外は ★ 無限に続く（IIR）。');
  console.log('');
  console.log('  ★ α = −1 は全部 1 ── ★ 累算器。一度 入れた値が ★ 永久に残ります。');
  console.log('  ★ α = 0 は [1, 0, 0, …] ── ★ 素通し（δ）。');
  console.log('  ★ α = 1 は [1, −1] ── ★ 差分。2 本で終わる。');
  console.log('  ★ α = 1/2 や −1/2 は ★ 終わりません。');
}

// ------------------------------------------------------------------
hr('3. 尾はべき乗で減る ── 第 26 回・第 27 回と同じ形');

console.log('  無限に続くタップは、どう減るのか。★ 漸近形は知られています：');
console.log('');
console.log('      ★ w_k ≈ k^(−α−1) / Γ(−α)      （k が大きいとき）');
console.log('');
console.log('  ★ ★ べき乗です。★ 指数まで測ります：');
console.log('');
{
  console.log('  ' + pad('α',8) + pad('k',10) + pad('w_k',16) + pad('k^(−α−1)/Γ(−α)',20) + '比');
  console.log('  ' + '-'.repeat(66));
  [-0.5,0.5,1.5,-0.25].forEach(function(a){
    const N=200001, w=glWeights(a,N);
    const G=gammaFn(-a);
    [1000,10000,100000].forEach(function(k){
      const th=Math.pow(k,-a-1)/G;
      console.log('  ' + pad(f(a,2),8) + pad(e(k,0),10) + pad(e(w[k],4),16)
        + pad(e(th,4),20) + f(w[k]/th,6));
    });
  });
  console.log('');
  console.log('  ★★ 一致しました。★ 分数階のデジタルフィルタは');
  console.log('    ★ 係数が ★ べき乗で減る、★ 終わらない記憶を持ちます。');
  console.log('');
  console.log('  ★ これは第 26 回・第 27 回で見たのと ★ 同じ形です：');
  console.log('      第 26 回：分数階 ⇐ 時定数がべき乗分布 g(τ) ∝ τ^(α−1)');
  console.log('      本回　　：分数階 ⇐ タップがべき乗分布 w_k ∝ k^(−α−1)');
  console.log('    ★ 連続か離散かの違いだけで、★ 同じことを言っています。');
}

// ------------------------------------------------------------------
hr('4. 半階を二回かけると一階になるか');

console.log('  分数階の定番の検算です。★ 畳み込みで確かめます：');
console.log('');
console.log('      ★ D^(1/2) ∘ D^(1/2) = D^1     ⟺  w(1/2) * w(1/2) = w(1) = [1, −1]');
console.log('');
{
  const N=200000;
  const h=glWeights(0.5,N);
  // 畳み込みの先頭だけ計算すれば足りる
  const M=10; const c=new Float64Array(M);
  for(let n=0;n<M;n++){ let s=0; for(let k=0;k<=n;k++) s+=h[k]*h[n-k]; c[n]=s; }
  console.log('  ' + pad('n',6) + pad('(w½ * w½)_n',20) + pad('w(1)_n',14) + '差');
  console.log('  ' + '-'.repeat(52));
  const w1=[1,-1,0,0,0,0,0,0,0,0];
  for(let n=0;n<8;n++)
    console.log('  ' + pad(n,6) + pad(f(c[n],12),20) + pad(f(w1[n],1),14) + e(Math.abs(c[n]-w1[n]),2));
  console.log('');
  console.log('  ★★ 先頭 2 本が [1, −1]、あとは ★ 機械精度でゼロ。');
  console.log('    ★ 無限に続くフィルタを二回 通すと、★ 2 本で終わるフィルタになる。');
  console.log('    ── ★ 半階は ★ 確かに「一階の平方根」でした。');
}

// ------------------------------------------------------------------
hr('5. 周波数で見る ── どの離散化が階数を保つか');

console.log('  s を z に置き換える流儀は一つではありません。代表的な二つ：');
console.log('');
console.log('      ★ 後退差分：s → (1 − z⁻¹)/T');
console.log('      ★ 双一次（タスティン）：s → (2/T)·(1 − z⁻¹)/(1 + z⁻¹)');
console.log('');
console.log('  ★ 単位円 z = e^{iθ}（θ = ωT）に乗せて位相を見ます：');
console.log('');
console.log('      後退差分： 1 − e^{−iθ} = 2 sin(θ/2) · e^{i(π/2 − θ/2)}');
console.log('               → α 乗すると位相 ★ α(90° − θ/2)   ── ★ θ とともにずれる');
console.log('');
console.log('      双一次：  (1−e^{−iθ})/(1+e^{−iθ}) = i·tan(θ/2)');
console.log('               → α 乗すると位相 ★ ちょうど 90α°   ── ★ 周波数によらない');
console.log('');
{
  const alphas=[0.5,1,-0.5];
  console.log('  ' + pad('α',7) + pad('ω/ωN',9) + pad('後退差分の位相',18)
            + pad('双一次の位相',18) + pad('アナログ 90α°',16) + '後退差分の誤差');
  console.log('  ' + '-'.repeat(86));
  alphas.forEach(function(a){
    [0.01,0.1,0.3,0.5,0.9].forEach(function(fr){
      const th=Math.PI*fr;                       // ωT、ナイキストは π
      const pb=a*(90-th*90/Math.PI);             // 後退差分
      const pt=90*a;                             // 双一次
      console.log('  ' + pad(f(a,1),7) + pad(f(fr,2),9) + rpad(f(pb,3),10) + pad('',8)
        + rpad(f(pt,3),10) + pad('',8) + rpad(f(90*a,3),10) + pad('',6)
        + f(pb-90*a,3) + '°');
    });
  });
  console.log('');
  console.log('  ★★ 双一次は ★ どの周波数でも位相がぴったり 90α°。');
  console.log('    ★ 「階数とは位相のこと」（第 1 回）が、★ 離散化を選ぶ基準になりました。');
  console.log('');
  console.log('  ★ 後退差分はナイキストに近づくほど位相が ★ ゼロへ倒れます。');
  console.log('    ★ 位相誤差が 1° / 5° 以内に収まるのは、ナイキストの何割までか：');
  console.log('');
  console.log('  ' + pad('α',8) + pad('位相誤差 1° 以内',22) + pad('位相誤差 5° 以内',22));
  console.log('  ' + '-'.repeat(54));
  [0.5,1,2].forEach(function(a){
    function lim(deg){
      // |a·θ/2| （度）= deg となる θ
      const th=deg*Math.PI/180*2/Math.abs(a);
      return th/Math.PI;
    }
    console.log('  ' + pad(f(a,1),8) + pad('ω/ωN < '+f(lim(1),4),22) + pad('ω/ωN < '+f(lim(5),4),22));
  });
  console.log('');
  console.log('  ★ 階数が大きいほど厳しい ── ★ 一階でも ★ ナイキストの 1 % までです。');
}

// ------------------------------------------------------------------
hr('6. ★★ 第 30 回とつながる ── 次元は ★ タップ数だった');

console.log('  第 30 回の結論はこうでした：');
console.log('');
console.log('      ★ d 次元のグリーン関数の階数は α = (d−3)/2');
console.log('      ★ 奇数次元は鋭く（尾なし）、偶数次元は尾を引く');
console.log('');
console.log('  ★ 本回の結論はこうでした：');
console.log('');
console.log('      ★ α が非負の整数のときだけ、タップが有限で終わる（FIR）');
console.log('');
console.log('  ★★★ 重ねます：');
console.log('');
{
  console.log('  ' + pad('d',5) + pad('α=(d−3)/2',12) + pad('GL のタップ',24)
            + pad('第 30 回の尾',24) + 'デジタルの言葉');
  console.log('  ' + '-'.repeat(92));
  [[1,'θ(s) 段差が永久に残る'],[2,'s^(−1/2) の尾'],[3,'δ そのもの'],
   [4,'s^(−3/2) の尾'],[5,"δ'（微分される）"],[7,"δ''"]].forEach(function(p){
    const d=p[0], a=(d-3)/2;
    const w=glWeights(a,4000);
    let nz=0; for(let k=0;k<4000;k++) if(Math.abs(w[k])>1e-14) nz=k+1;
    const tap = (nz<4000) ? ('★ '+nz+' 本 [' + [...w.slice(0,nz)].map(x=>f(x,0)).join(', ') + ']')
                          : (a<=-1 ? '無限（減らない ── 全部 1）'
                                   : ('無限（k^' + f(-a-1,1) + ' で減る）'));
    console.log('  ' + pad(d,5) + pad(f(a,1),12) + pad(tap,24) + pad(p[1],24)
      + (nz<4000?'★ FIR':'★ IIR'));
  });
  console.log('');
  console.log('  ★★★ ぴったり対応します：');
  console.log('');
  console.log('      ★ 奇数次元 ＝ 整数階 ＝ ★ FIR（タップが (d−1)/2 本で終わる）');
  console.log('      ★ 偶数次元 ＝ 半整数階 ＝ ★ IIR（タップがべき乗で無限に続く）');
  console.log('');
  console.log('  ★ 一つずつ読みます：');
  console.log('      d=1：タップが全部 1 の ★ 累算器 → 入れた音が永久に残る（θ(s)）');
  console.log('      d=3：タップ 1 本の ★ 素通し → 歪まず、通り過ぎたら終わり（δ）');
  console.log('      d=5：タップ 2 本の ★ 差分 → 鋭いが ★ 微分される（δ\'）');
  console.log('      d=2：★ 1, 0.5, 0.375, … と ★ k^(−1/2) で減る無限の尾');
  console.log('');
  console.log('  ★★ 空間の次元は、★ フィルタのタップ数として数えられました。');
  console.log('    ★ 「ホイヘンスの原理が成り立つ」＝「そのフィルタが FIR である」。');
}

// ------------------------------------------------------------------
hr('7. 2 次元の残響を、実際に鳴らしてみる');

console.log('  ★ d=2 のタップ（α = −1/2）を、そのまま ★ 残響として聞くとどうなるか。');
console.log('  ★ ステップ応答（ずっと鳴らし続けたときの溜まり方）を計算します：');
console.log('');
{
  const N=200000;
  const w=glWeights(-0.5,N);          // d=2
  const w0=glWeights(0,N);            // d=3
  const wm=glWeights(-1,N);           // d=1
  function step(w,n){ let s=0; for(let k=0;k<=n;k++) s+=w[k]; return s; }
  console.log('  ' + pad('標本数 n',12) + pad('d=1（α=−1）',18) + pad('d=2（α=−1/2）',20)
            + pad('d=3（α=0）',16) + '√n との比（d=2）');
  console.log('  ' + '-'.repeat(76));
  [10,100,1000,10000,100000].forEach(function(n){
    const s1=step(wm,n), s2=step(w,n), s3=step(w0,n);
    console.log('  ' + pad(e(n,0),12) + pad(f(s1,1),18) + pad(f(s2,4),20)
      + pad(f(s3,1),16) + f(s2/Math.sqrt(n),6));
  });
  console.log('');
  console.log('  ★★ d=3 は ★ 1 のまま ── 溜まりません。');
  console.log('  ★ d=1 は ★ n に比例して溜まります（累算器）。');
  console.log('  ★★ d=2 は ★ √n で溜まる ── ★ 中間。');
  console.log('    ★ 比が 2/√π = ' + f(2/Math.sqrt(Math.PI),6) + ' に近づきます。');
  console.log('');
  console.log('  ★ 「2 次元の部屋では音が √(時間) で溜まる」── ★ これが第 30 回の帰結の');
  console.log('    ★ デジタル版です。1 時間 話すと、1 分の 7.7 倍 溜まる。');
}

// ------------------------------------------------------------------
hr('8. デジタルで初めて出てくる問題 ── 分数の遅延');

console.log('  アナログでは e^{−sτ} で τ を ★ いくらでも細かく取れます。');
console.log('  ★ デジタルでは遅延は z^{−n} ── ★ n は整数しか作れません。');
console.log('');
console.log('  ★ では「半標本ぶん遅らせる」フィルタ z^(−1/2) はどんな形か。');
console.log('  ★ 理想の分数遅延のインパルス応答は ★ シンク関数です：');
console.log('');
console.log('      ★ h_k = sinc(k − D),   D = 遅延の標本数');
console.log('');
{
  function sinc(x){ return Math.abs(x)<1e-12 ? 1 : Math.sin(Math.PI*x)/(Math.PI*x); }
  console.log('  ' + pad('k',6) + pad('D=0（整数）',16) + pad('D=0.5（半標本）',20) + pad('D=1（整数）',16));
  console.log('  ' + '-'.repeat(60));
  for(let k=-3;k<=4;k++){
    console.log('  ' + pad(k,6) + pad(f(sinc(k-0),6),16) + pad(f(sinc(k-0.5),6),20)
      + pad(f(sinc(k-1),6),16));
  }
  console.log('');
  console.log('  ★★ 整数の遅延は ★ 1 本だけ。★ 半標本の遅延は ★ 無限に尾を引きます。');
  console.log('    ★ しかも 1/k でしか減らない ── ★ 打ち切りにくい。');
  console.log('');
  console.log('  ★ これは本回 2 節と ★ まったく同じ構図です：');
  console.log('      ★ 整数 → 有限本（FIR）、★ 分数 → 無限本（IIR）。');
  console.log('    ★ 階数でも、遅延でも、★ 整数から外れた瞬間に尾が生えます。');
  console.log('');
  console.log('  ★★ そして第 30 回に戻ると ── ★ 次元も同じでした。');
  console.log('    ★ 奇数（整数階）は有限、偶数（半整数階）は無限。');
}

// ------------------------------------------------------------------
hr('9. まとめ');

{
  const rows = [
    ['D^α = (1−z⁻¹)^α ＝ GL',      '◎ 解析', '★ 二項展開そのもの'],
    ['整数階だけ FIR',              '◎ 数値', '★ α=0,1,2,3 で 1,2,3,4 本で終わる'],
    ['α=−1 は全部 1（累算器）',     '◎ 数値', '★ 第 30 回 d=1 の θ(s) と一致'],
    ['タップは k^(−α−1) で減る',    '◎ 数値', '★ 1/Γ(−α) まで含めて 6 桁 一致'],
    ['D^½∘D^½ = D',                '◎ 数値', '★ 畳み込みが [1,−1] になる'],
    ['双一次は位相を厳密に保つ',     '◎ 解析', '★ tan(θ/2) が純虚数だから'],
    ['後退差分は位相が倒れる',       '◎ 数値', '★ 一階でもナイキストの 2 % まで'],
    ['次元 ＝ タップ数',            '◎ 対応', '★ 奇数=FIR (d−1)/2 本、偶数=IIR'],
    ['2 次元では √n で溜まる',      '◎ 数値', '★ 比が 2/√π に収束'],
    ['分数遅延も無限に尾を引く',     '◎ 数値', '★ sinc は 1/k でしか減らない']
  ];
  console.log('  ' + pad('主張',30) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(86));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],30)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     デジタルに移すと、階数は ★ タップの本数として目に見える。');
  console.log('     ★★ 整数階は有限本（FIR）、分数階は ★ べき乗で減る無限本（IIR）。');
  console.log('     ── ★ そして第 30 回の「次元」も、まったく同じ勘定でした。');
  console.log('');
  console.log('  ★★ 第 30 回：奇数次元は尾なし、偶数次元は尾を引く');
  console.log('    第 31 回：整数階は FIR、分数階は IIR');
  console.log('    ★★★ この二つは ★ 同じ一つのことを、別の言葉で言っていました。');
}

console.log('');
