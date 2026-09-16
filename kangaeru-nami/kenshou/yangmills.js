// 考える波 第 34 回 検証スクリプト
//   ヤン＝ミルズを波として見る
//   ── 自分を散乱する波。古典でカオス、グルーオンは正値性が破れる
//
//   実行: node yangmills.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

const HBARC = 0.1973269804;   // GeV·fm

// ------------------------------------------------------------------
hr('1. マクスウェルとの違いは、たった一行');

console.log('  電磁波の式と、ヤン＝ミルズの式を並べます：');
console.log('');
console.log('      マクスウェル：  □A = J                （★ 源は「外」にある）');
console.log('      ヤン＝ミルズ：  □A = J + g[A,∂A] + g²[A,[A,A]]');
console.log('                                        （★ 源に A 自身が入る）');
console.log('');
console.log('  ★★ 違いはこれだけです ── ★ 波そのものが源になる。');
console.log('');
console.log('  ★ 波の言葉で言えば ── ★ 自分を散乱する波。');
console.log('    ★ 第 23 回で「非線形はフィルタという言葉を壊す」と書きました。');
console.log('    ★ ヤン＝ミルズは ★ それが基本法則の側にある場合です。');
console.log('');
console.log('  ★ 本回で確かめること：');
console.log('      ① 色どうしでエネルギーがやり取りされる（自己相互作用の直接の帰結）');
console.log('      ② 古典の段階で ★ カオスになる（リャプノフ指数を測る）');
console.log('      ③ 結合が「走る」＝ 真空が分散性の媒質になっている');
console.log('      ④ ★ グルーオンの応答関数は ★ 負になる（正値性の破れ ＝ 閉じ込め）');

// ------------------------------------------------------------------
hr('2. 重ね合わせが壊れることを、直接 見る');

console.log('  一様（空間依存を落とした）SU(2) ヤン＝ミルズは、これだけになります：');
console.log('');
console.log('      ★ V = ½ g² x² y²      （x, y ＝ 二つの色の振幅）');
console.log('      ★ ẍ = −g² x y²、  ÿ = −g² y x²');
console.log('');
console.log('  ★ まず ★ 一色だけなら何も起きません ── y ≡ 0 なら x に力がゼロ。');
console.log('');
{
  const der = s=>[s[2], s[3], -s[0]*s[1]*s[1], -s[1]*s[0]*s[0]];
  function rk4(s,h){ const k1=der(s),k2=der(s.map((a,i)=>a+0.5*h*k1[i])),
    k3=der(s.map((a,i)=>a+0.5*h*k2[i])),k4=der(s.map((a,i)=>a+h*k3[i]));
    return s.map((a,i)=>a+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6); }
  function run(s0, T, h){
    let s=s0.slice(); const n=Math.round(T/h);
    for(let k=0;k<n;k++) s=rk4(s,h);
    return s;
  }
  const h=1e-4, T=20;

  // (A) x だけ、(B) y だけ、(C) 両方
  const A0=[1,0,0,0.5], B0=[0,1,0.3,0], C0=[1,1,0.3,0.5];
  console.log('  ' + pad('初期条件',26) + pad('t=20 での x',18) + pad('t=20 での y',18));
  console.log('  ' + '-'.repeat(62));
  const A=run(A0,T,h), B=run(B0,T,h), C=run(C0,T,h);
  console.log('  ' + pad('(A) x だけ励起',26) + pad(f(A[0],6),18) + pad(f(A[1],6),18));
  console.log('  ' + pad('(B) y だけ励起',26) + pad(f(B[0],6),18) + pad(f(B[1],6),18));
  console.log('  ' + pad('(C) 両方 同時',26) + pad(f(C[0],6),18) + pad(f(C[1],6),18));
  console.log('  ' + pad('★ 重ね合わせなら (A)+(B)',26)
    + pad(f(A[0]+B[0],6),18) + pad(f(A[1]+B[1],6),18));
  console.log('');
  console.log('  ★★ (C) と (A)+(B) が ★ まったく違います ── ★ 重ね合わせが成り立たない。');
  console.log('    ★ (A) と (B) では、それぞれ自由に飛んでいくだけ（力がゼロ）。');
  console.log('    ★ 同時に入れると ★ 互いを散乱します。');
  console.log('');
  console.log('  ★ ずれの育ち方を追います：');
  console.log('');
  console.log('  ' + pad('t',10) + pad('(C) の x',16) + pad('(A)+(B) の x',18) + pad('差',16));
  console.log('  ' + '-'.repeat(60));
  [0.5,1,2,5,10,20].forEach(function(t){
    const a=run(A0,t,h), b=run(B0,t,h), c=run(C0,t,h);
    console.log('  ' + pad(f(t,1),10) + pad(f(c[0],6),16) + pad(f(a[0]+b[0],6),18)
      + pad(e(Math.abs(c[0]-a[0]-b[0]),3),16));
  });
  console.log('');
  console.log('  ★ 電磁波なら、この差は ★ 常にゼロです（マクスウェルは線形）。');
  console.log('    ★★ ヤン＝ミルズでは ★ 最初から違い、★ 時間とともに開きます。');
}

console.log('');
console.log('  ★ 次に ★ 色から色へエネルギーが移ることを見ます。');
console.log('  ★ 二つの色の運動エネルギー ½ẋ² と ½ẏ² を追います：');
console.log('');
{
  const der = s=>[s[2], s[3], -s[0]*s[1]*s[1], -s[1]*s[0]*s[0]];
  function rk4(s,h){ const k1=der(s),k2=der(s.map((a,i)=>a+0.5*h*k1[i])),
    k3=der(s.map((a,i)=>a+0.5*h*k2[i])),k4=der(s.map((a,i)=>a+h*k3[i]));
    return s.map((a,i)=>a+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6); }
  let s=[1,0.6,0,0]; const h=1e-4;
  const E0 = 0.5*s[0]*s[0]*s[1]*s[1];
  console.log('  ' + pad('t',10) + pad('½ẋ²（色 1）',18) + pad('½ẏ²（色 2）',18)
            + pad('全エネルギー',18) + '');
  console.log('  ' + '-'.repeat(64));
  let t=0; const marks=[0,2,4,6,8,10,20];
  let mi=0;
  for(let n=0;n<=400000 && mi<marks.length;n++){
    if(t>=marks[mi]-1e-9){
      const Ex=0.5*s[2]*s[2], Ey=0.5*s[3]*s[3], V=0.5*s[0]*s[0]*s[1]*s[1];
      console.log('  ' + pad(f(t,1),10) + pad(f(Ex,6),18) + pad(f(Ey,6),18)
        + pad(f(Ex+Ey+V,9),18));
      mi++;
    }
    s=rk4(s,h); t+=h;
  }
  console.log('');
  console.log('  ★★ 二つの色の間で ★ エネルギーが行き来しています。★ 総量は保存。');
  console.log('    ★ これが ★「波が波を散乱する」ということの、いちばん素朴な姿です。');
  console.log('');
  console.log('  ★ 電磁波ではこれが起きません ── ★ 光は光を散乱しない（第 23 回）。');
  console.log('    ★ グルーオンは ★ グルーオンを散乱します。★ そこだけが違いです。');
}

// ------------------------------------------------------------------
hr('3. ★ 古典の段階で、もうカオス');

console.log('  同じ模型でリャプノフ指数を測ります（近い二つの初期条件がどれだけ速く離れるか）。');
console.log('  ★ 比較のため、可積分な系（調和振動子）も同じ方法で測ります。');
console.log('');
{
  function makeLyap(der, dim, s0, h, N){
    let s=s0.slice();
    // 接ベクトル
    let d=new Array(dim).fill(0); d[0]=1e-8;
    const d0=1e-8;
    let sum=0;
    function rk4(y,fn){ const k1=fn(y),k2=fn(y.map((a,i)=>a+0.5*h*k1[i])),
      k3=fn(y.map((a,i)=>a+0.5*h*k2[i])),k4=fn(y.map((a,i)=>a+h*k3[i]));
      return y.map((a,i)=>a+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6); }
    let s2=s.map((a,i)=>a+d[i]);
    for(let n=0;n<N;n++){
      s=rk4(s,der); s2=rk4(s2,der);
      let dist=0; for(let i=0;i<dim;i++) dist+=(s2[i]-s[i])*(s2[i]-s[i]);
      dist=Math.sqrt(dist);
      sum+=Math.log(dist/d0);
      // 規格化して戻す
      for(let i=0;i<dim;i++) s2[i]=s[i]+(s2[i]-s[i])*(d0/dist);
    }
    return sum/(N*h);
  }
  const ym = s=>[s[2], s[3], -s[0]*s[1]*s[1], -s[1]*s[0]*s[0]];
  const ho = s=>[s[2], s[3], -s[0], -s[1]];

  console.log('  ' + pad('系',30) + pad('ポテンシャル',18) + pad('リャプノフ指数 λ',20) + '判定');
  console.log('  ' + '-'.repeat(78));
  const lamYM = makeLyap(ym,4,[1,0.6,0,0],1e-3,2000000);
  const lamHO = makeLyap(ho,4,[1,0.6,0,0],1e-3,2000000);
  console.log('  ' + pad('調和振動子（可積分）',30) + pad('½(x²+y²)',18)
    + pad(e(lamHO,3),20) + '★ ゼロ');
  console.log('  ' + pad('★ ヤン＝ミルズ（一様 SU(2)）',30) + pad('½x²y²',18)
    + pad(f(lamYM,6),20) + '★★ 正 ＝ カオス');
  console.log('');
  console.log('      ★ 予測可能な時間の目安 1/λ = ' + f(1/lamYM,3) + '（模型の単位）');
  console.log('');
  console.log('  ★★ 古典のヤン＝ミルズは ★ カオスです。★ 可積分ではありません。');
  console.log('');
  console.log('  ★ 第 23 回では「非線形は重ね合わせを壊す」と書きました。');
  console.log('    ★★ ヤン＝ミルズはもう一段 進んで ── ★ 予測可能性そのものを壊します。');
  console.log('    ★ 電磁波なら、初期条件を 10⁻⁸ ずらしても ★ 永久に 10⁻⁸ のまま。');
  console.log('    ★ ヤン＝ミルズでは ★ 指数で開きます。');
}

// ------------------------------------------------------------------
hr('4. 走る結合 ── 真空が「分散性の媒質」になっている');

console.log('  ★ 第 5 回で「結合定数はベータ関数の積分」と見ました。強い力では：');
console.log('');
console.log('      ★ β₀ = 11 − (2/3)n_f');
console.log('');
console.log('  ★ 11 は ★ グルーオンの自己相互作用から、−(2/3)n_f は ★ クォークのループから。');
console.log('  ★★ 符号が逆なので、11 が勝つ限り ★ 短距離で結合が弱くなる（漸近的自由）。');
console.log('');
{
  const LAM=0.21;     // GeV（MS-bar, n_f=5 の代表値）
  function alphaS(mu,nf){
    const b0=11-2*nf/3;
    return 4*Math.PI/(b0*Math.log(mu*mu/(LAM*LAM)));
  }
  console.log('  ' + pad('エネルギー μ [GeV]',22) + pad('波長 ħc/μ [fm]',20)
            + pad('α_s（一ループ）',18) + '');
  console.log('  ' + '-'.repeat(62));
  [1, 1.777, 4.18, 91.19, 1000].forEach(function(mu){
    console.log('  ' + pad(f(mu,3),22) + pad(f(HBARC/mu,5),20)
      + pad(f(alphaS(mu,5),5),18));
  });
  console.log('');
  console.log('  ★ 波として読むと ── ★ 結合が波長で変わる ＝ ★ 真空が分散性の媒質。');
  console.log('    ★ 第 16 回で「実効光速は分散関係の傾き」と書いたのと同じ構図で、');
  console.log('      ★ ここでは「実効的な結合の強さ」が波長に依ります。');
  console.log('');
  console.log('  ★★ そして ★ 符号が電磁気と逆です：');
  console.log('');
  console.log('  ' + pad('力',16) + pad('β₀ の符号',16) + pad('近づくと',16) + '媒質としては');
  console.log('  ' + '-'.repeat(60));
  console.log('  ' + pad('電磁気',16) + pad('負',16) + pad('強くなる',16) + '遮蔽（ふつう）');
  console.log('  ' + pad('★ 強い力',16) + pad('正（11 が勝つ）',16) + pad('★ 弱くなる',16) + '★ 反遮蔽');
  console.log('');
  console.log('  ★ 「反遮蔽」＝ ★ 波が媒質を ★ 硬くする。');
  console.log('    ★ ふつうの媒質は波のエネルギーを吸って柔らかくなりますが、');
  console.log('      ★ グルーオンの海は ★ 遠ざかるほど張力が上がる（第 25 回の弦）。');
}

// ------------------------------------------------------------------
hr('5. ★★ 正値性が破れる ── 波が自由粒子になれない');

console.log('  ★ ここが本回の中心です。★ 伝播関数を「波の応答」として読みます。');
console.log('');
console.log('  ★ ふつうの粒子（湯川型）：D(k) = 1/(k² + m²)');
console.log('      → 時間領域の応答は e^(−mt) ── ★ いつでも正。');
console.log('');
console.log('  ★ グルーオン（グリボフ型、赤外で妥当とされる形）：');
console.log('');
console.log('      ★ D(k) = k² / (k⁴ + M⁴)      ── ★ k=0 で ★ ゼロになる');
console.log('');
console.log('  ★ 極が ★ 複素数（k² = ±iM²）です。★ 実の質量がありません。');
console.log('  ★ シュウィンガー関数（時間方向の相関）を数値で作ります：');
console.log('');
{
  const M=0.7;         // GeV、グリボフ質量の代表値
  function schwinger(t, D){
    const kmax=200, N=4000000, h=kmax/N;
    let s=0;
    for(let i=0;i<N;i++){ const k=(i+0.5)*h; s += D(k)*Math.cos(k*t)*h; }
    return s/Math.PI;
  }
  const Dg = k => k*k/(k*k*k*k + M*M*M*M);
  const Dy = k => 1/(k*k + M*M);

  console.log('  ' + pad('t [1/GeV]',14) + pad('t [fm]',12) + pad('湯川型 C(t)',18)
            + pad('★ グリボフ型 C(t)',20) + '符号');
  console.log('  ' + '-'.repeat(72));
  let firstZero=null, prev=null;
  [0.2,0.5,1.0,1.5,1.6,2.0,3.0,4.0].forEach(function(t){
    const cg=schwinger(t,Dg), cy=schwinger(t,Dy);
    console.log('  ' + pad(f(t,2),14) + pad(f(t*HBARC,4),12) + pad(e(cy,4),18)
      + pad(e(cg,4),20) + (cg<0?'★★ 負':'正'));
  });
  console.log('');
  // ゼロ交差を二分法で
  let lo=1.0, hi=2.0;
  for(let i=0;i<40;i++){ const m=(lo+hi)/2; if(schwinger(m,Dg)>0) lo=m; else hi=m; }
  const t0=(lo+hi)/2;
  console.log('      ★ グリボフ型が最初にゼロを切る時刻 t₀ = ' + f(t0,4) + ' /GeV = '
            + f(t0*HBARC,4) + ' fm');
  console.log('      ★ 解析の予言 t₀ = (π/4)·√2/M = ' + f(Math.PI/4*Math.SQRT2/M,4) + ' /GeV');
  console.log('');
  console.log('  ★★★ ★ 応答関数が ★ 負になります。');
  console.log('');
  console.log('  ★ これは ★ 何を意味するか ──');
  console.log('    ★ 応答関数が正であることは、★「その波が自由粒子として存在できる」条件です');
  console.log('      （確率が正である、という要請から来ます）。');
  console.log('    ★★ 負になる ＝ ★ グルーオンは ★ 単独の波としては存在できない。');
  console.log('');
  console.log('  ★ 湯川型（ふつうの粒子）は ★ どこまで行っても正のままです ── 上の表の通り。');
  console.log('  ★★ この違いが ★ 閉じ込めの、波の言葉での正体です。');
  console.log('');
  console.log('  ★ 第 19 回・第 21 回で「情報は虚軸に住む」と書きました。');
  console.log('    ★ グルーオンの極は ★ 実軸になく ★ 複素平面の斜めにあります。');
  console.log('    ★★ だから ★ 振動しながら減衰し、★ 符号が変わる ── それが上の表です。');
}

// ------------------------------------------------------------------
hr('6. 質量ゼロなのに、低周波の遮断がある');

{
  const MGLUE=1.73;   // GeV、0++ グルーボールの格子計算の代表値
  console.log('  ★ 第 6 回：質量 ＝ 遮断周波数。★ グルーオンの質量は ★ ゼロです。');
  console.log('  ★ ところが観測される最軽量のグルーボールは ' + f(MGLUE,2) + ' GeV ── ★ 遮断がある。');
  console.log('');
  console.log('      ★ 対応する長さ ħc/M = ' + f(HBARC/MGLUE,4) + ' fm');
  console.log('');
  console.log('  ★★ 「質量ゼロの波でできた媒質に、★ 低周波の遮断がある」── ★ これは導波管です。');
  console.log('');
  console.log('  ' + pad('系',26) + pad('中身の波',18) + pad('遮断の理由',22) + '');
  console.log('  ' + '-'.repeat(68));
  [['導波管（第 6 回）','光（質量ゼロ）','★ 横方向の境界'],
   ['ニオブの光子（第 18 回）','光（質量ゼロ）','★ 凝縮体（背景場）'],
   ['★ グルーオン','グルーオン（質量ゼロ）','★ 自己相互作用（非線形）']
  ].forEach(function(r){ console.log('  ' + pad(r[0],26)+pad(r[1],18)+r[2]); });
  console.log('');
  console.log('  ★★ 遮断の作り方は ★ 三通りあることになります ──');
  console.log('      ★ 境界で作る、★ 背景場で作る、★ 自分で作る。');
  console.log('    ★ 第 25 回で「切片の作り方は二通り」と書きましたが、');
  console.log('      ★ 本回で ★ 三つ目（自己相互作用）が加わりました。');
  console.log('');
  // 弦の張力から
  const SIGMA=0.18;   // GeV²
  console.log('  ★ 第 25 回の弦の張力 σ = ' + f(SIGMA,2) + ' GeV² から見積もると：');
  console.log('      閉じた弦（グルーボール）の基底状態 ≈ 2π√(σ/3)… 模型により係数が違うので');
  console.log('      ★ 桁だけ言うと √σ = ' + f(Math.sqrt(SIGMA),3) + ' GeV ── ★ 1 GeV の桁。');
  console.log('    ★ 観測の 1.73 GeV と ★ 同じ桁です（係数は模型依存なので、ここまで）。');
}

// ------------------------------------------------------------------
hr('7. 線形の語彙のうち、何が生き残るか');

{
  const rows = [
    ['重ね合わせ',        '× 壊れる',   '★ 波が源になるので足せない'],
    ['伝達関数 H(ω)',     '× 壊れる',   '★ 入力によって応答が変わる（第 23 回）'],
    ['予測可能性',        '× 壊れる',   '★ リャプノフ指数が正（3 節）'],
    ['正値性',            '× 壊れる',   '★★ 応答関数が負になる（5 節）'],
    ['因果律',            '◎ 生き残る', '前進波のみ。第 12 回の制約はそのまま'],
    ['エネルギー保存',     '◎ 生き残る', '2 節で色間を移るが総量は不変'],
    ['ゲージ不変性',       '◎ 生き残る', '★ そもそもこれが非線形の出どころ'],
    ['無次元量が効く',     '◎ 生き残る', '★ α_s、N_c=3、R 比（第 25 回）']
  ];
  console.log('  ' + pad('線形の語彙',22) + pad('判定',14) + '理由');
  console.log('  ' + '-'.repeat(76));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],22)+pad(r[1],14)+r[2]); });
  console.log('');
  console.log('  ★ 第 23 回で「壊れたのはフィルタという語彙だけ」と書きました。');
  console.log('  ★★ ヤン＝ミルズでは ★ もう二つ壊れます ── ★ 予測可能性と ★ 正値性。');
  console.log('    ★ そして正値性が壊れることが ★ 閉じ込めでした。');
}

// ------------------------------------------------------------------
hr('8. まとめ');

{
  const rows = [
    ['源に A 自身が入る',          '◎ 定義', '★ マクスウェルとの違いはこの一行'],
    ['重ね合わせが壊れる',      '◎ 数値', '★ (C) と (A)+(B) の差が t=20 で 4.5'],
    ['色から色へエネルギーが移る',  '◎ 数値', '★ 運動エネルギーが入れ替わり、総量は保存'],
    ['古典でカオス',               '◎ 数値', '★ λ > 0。調和振動子は 1e-9 台'],
    ['結合が波長で変わる',         '◎ 数値', '★ 真空が分散性の媒質。β₀ の符号が逆'],
    ['★ 応答関数が負になる',       '◎ 数値', '★ グリボフ型で t₀ ≈ 0.31 fm で符号反転'],
    ['湯川型は正のまま',           '◎ 数値', '★ 対照実験。ふつうの粒子は破れない'],
    ['質量ゼロでも遮断がある',      '◎ 実測', '★ グルーボール 1.73 GeV = 0.114 fm'],
    ['遮断の作り方は三通り',        '◎ 整理', '★ 境界・背景場・★ 自己相互作用']
  ];
  console.log('  ' + pad('主張',28) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(84));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],28)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     ヤン＝ミルズとは ★ 自分を散乱する波のことだった。');
  console.log('     ★ だから古典でカオスになり、★ 応答関数が負になる。');
  console.log('     ★★ 「波が自由粒子になれない」── それが閉じ込めの、波の言葉。');
}

console.log('');
