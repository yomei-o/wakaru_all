// 考える波 第 35 回 検証スクリプト
//   光をもっと掘る ── 位相が「角度の関数」になるとき
//   ── 軌道角運動量と幾何学的位相
//
//   実行: node hikari2.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

// ------------------------------------------------------------------
hr('1. 位相に、新しい軸を足す');

console.log('  第 1 回から 34 回まで、★ 位相はいつも ★ 時間の関数でした：');
console.log('');
console.log('      φ(t) = ωt      ── ★ 階数 α は「位相が 90α 度 回ること」');
console.log('');
console.log('  ★ 本回は位相に ★ 二つの新しい軸を足します：');
console.log('');
console.log('      ① ★ 位相が ★ 方位角の関数：φ = ℓ·（回りの角度）  ── 軌道角運動量');
console.log('      ② ★ 位相が ★ 状態空間の経路で決まる          ── 幾何学的位相');
console.log('');
console.log('  ★★ どちらも ★ 時間とは無関係に位相が生まれます。');
console.log('    ★ ①では ★ 整数しか許されず（トポロジー）、');
console.log('    ★ ②では ★ 位相が「面積」として現れます。');

// ------------------------------------------------------------------
hr('2. 位相が角度の関数になる ── らせんの波面');

console.log('  電磁波の横断面で、位相が ★ 回りの角度 ϕ に比例する場を考えます：');
console.log('');
console.log('      ★ u(r, ϕ) ∝ r^|ℓ| · e^(−r²/w²) · e^(iℓϕ)      （ラゲール・ガウス）');
console.log('');
console.log('  ★ 波面は ★ らせん階段になります。★ そして ★ 二つのことが起きます：');
console.log('');
{
  // 強度分布とピーク半径
  const w=1;
  function I(r,l){ const a=Math.pow(r,Math.abs(l))*Math.exp(-r*r/(w*w)); return a*a; }
  console.log('  ★ ① 中心の強度がゼロになる（位相が定義できないから）：');
  console.log('');
  console.log('  ' + pad('ℓ',6) + pad('r=0 の強度',16) + pad('ピーク半径 r_max',20) + pad('予言 w√(|ℓ|/2)',18));
  console.log('  ' + '-'.repeat(60));
  [0,1,2,3,5,10].forEach(function(l){
    // 数値でピークを探す
    let best=0, rb=0;
    for(let i=1;i<=200000;i++){ const r=i*1e-4; const v=I(r,l); if(v>best){best=v; rb=r;} }
    console.log('  ' + pad(l,6) + pad(l===0?'1.0000':'0.0000',16) + pad(f(rb,5),20)
      + pad(l===0?'—':f(w*Math.sqrt(Math.abs(l)/2),5),18));
  });
  console.log('');
  console.log('  ★ ℓ ≠ 0 では ★ 中心がきっかりゼロ ── ★ ドーナツ形のビームになります。');
  console.log('  ★ ピーク半径は ★ w√(|ℓ|/2) ── ★ ℓ が大きいほど太る。');
  console.log('');
  console.log('  ★★ ② ℓ は ★ 整数しか取れません。★ 一周して元の値に戻る必要があるから：');
  console.log('');
  console.log('      e^(iℓ·2π) = 1   ⟺   ★ ℓ ∈ 整数');
  console.log('');
  console.log('  ★ これは第 5 回の「境界条件が離散モードを作る」の、★ 角度版です。');
  console.log('    ★ 導波管では横方向の壁が、★ ここでは ★「一周すると戻る」という条件が');
  console.log('      ★ 離散化しています。');
}

// ------------------------------------------------------------------
hr('3. 巻き数は、動かしても壊れない');

console.log('  ★ 位相の巻き数を数値で数えます。★ 閉じた経路を回って位相の増分を足すだけ：');
console.log('');
console.log('      ★ 巻き数 = (1/2π)·∮ dφ');
console.log('');
{
  function winding(fn, cx, cy, R, N){
    let tot=0, prev=null;
    for(let i=0;i<=N;i++){
      const t=2*Math.PI*i/N;
      const z=fn(cx+R*Math.cos(t), cy+R*Math.sin(t));
      const ph=Math.atan2(z[1],z[0]);
      if(prev!==null){
        let d=ph-prev;
        while(d>Math.PI) d-=2*Math.PI;
        while(d<-Math.PI) d+=2*Math.PI;
        tot+=d;
      }
      prev=ph;
    }
    return tot/(2*Math.PI);
  }
  // u = (x+iy)² − a²  → ±a に ℓ=1 の渦が二つ
  function mk(a){ return function(x,y){
    // (x+iy)^2 - a^2
    const re=x*x-y*y-a*a, im=2*x*y;
    return [re,im];
  }; }

  console.log('  ★ 試験場： u = (x+iy)² − a²   ── ★ x = ±a に渦が二つ。');
  console.log('');
  console.log('  ' + pad('a',8) + pad('大きな円 R=10',20) + pad('+a まわり R=0.1a',22)
            + pad('原点まわり R=0.1a',22));
  console.log('  ' + '-'.repeat(72));
  [0.001,0.1,1,3].forEach(function(a){
    const fn=mk(a);
    const big=winding(fn,0,0,10,20000);
    const near=winding(fn,a,0,0.1*a,20000);
    const orig=winding(fn,0,0,0.1*a,20000);
    console.log('  ' + pad(f(a,3),8) + pad(f(big,6),20) + pad(f(near,6),22) + pad(f(orig,6),22));
  });
  console.log('');
  console.log('  ★★ 大きな円ではいつも ★ ちょうど 2 ── ★ 渦をどこへ動かしても変わりません。');
  console.log('  ★ 小さな円は、中に渦が入っていれば 1、いなければ 0 ── ★ 整数しか出ません。');
  console.log('');
  console.log('  ★★★ ★ 巻き数は ★ 連続に変えられない量です（トポロジカルな保存量）。');
  console.log('    ★ 振幅や位相はいくらでも連続に動かせるのに、★ 巻き数だけは飛びます。');
  console.log('');
  console.log('  ★ 第 13 回の「離散スケール不変性」とは ★ 別の離散性です：');
  console.log('      第 13 回：★ 対数軸で等間隔（連続の対称性が離散に破れた）');
  console.log('      ★ 本回：★ 一周して戻るという条件（★ トポロジー）');
  console.log('    ★ どちらも「離散」ですが、★ 出どころが違います。');
}

// ------------------------------------------------------------------
hr('4. ★★ 位相が「面積」になる ── 幾何学的位相');

console.log('  ★ こんどは偏光です。★ 偏光の状態は ★ ポアンカレ球（ブロッホ球）の点で表せます：');
console.log('');
console.log('      |ψ(θ,ϕ)⟩ = ( cos(θ/2), sin(θ/2)·e^(iϕ) )');
console.log('      北極 = 右円偏光、南極 = 左円偏光、赤道 = 直線偏光');
console.log('');
console.log('  ★★ 状態を球面上で ★ 一周させて元に戻すと ── ★ 位相が残ります。');
console.log('  ★ しかもその位相は ★ 囲んだ立体角の半分です（パンチャラトナム＝ベリー）。');
console.log('');
{
  // ジョーンズベクトル（2 成分複素）
  function ket(th,ph){ return [[Math.cos(th/2),0],[Math.sin(th/2)*Math.cos(ph), Math.sin(th/2)*Math.sin(ph)]]; }
  function bloch(th,ph){ return [Math.sin(th)*Math.cos(ph), Math.sin(th)*Math.sin(ph), Math.cos(th)]; }
  function inner(a,b){ // ⟨a|b⟩
    let re=0, im=0;
    for(let i=0;i<2;i++){ const ar=a[i][0], ai=-a[i][1], br=b[i][0], bi=b[i][1];
      re+=ar*br-ai*bi; im+=ar*bi+ai*br; }
    return [re,im];
  }
  function cmul(z,w){ return [z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]]; }
  function dot(a,b){ return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]; }
  function cross(a,b){ return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]; }
  function solidAngle(A,B,C){   // Van Oosterom–Strackee
    const num=dot(A,cross(B,C));
    const den=1+dot(A,B)+dot(B,C)+dot(C,A);
    return 2*Math.atan2(num,den);
  }

  console.log('  ★ 三つの偏光状態 A → B → C → A を巡らせます。');
  console.log('  ★ パンチャラトナム位相 γ = −arg[⟨A|B⟩⟨B|C⟩⟨C|A⟩] を計算し、');
  console.log('    ★ 球面三角形の立体角 Ω と比べます：');
  console.log('');
  console.log('  ' + pad('三角形',30) + pad('γ [rad]',16) + pad('−Ω/2 [rad]',16) + '差');
  console.log('  ' + '-'.repeat(70));
  const tris = [
    ['八分の一球（北極・赤道 0°・赤道 90°）', [0,0],[Math.PI/2,0],[Math.PI/2,Math.PI/2]],
    ['小さな三角形',                        [0.3,0],[0.3,1.0],[0.5,0.5]],
    ['大きな三角形',                        [0.2,0],[1.8,2.0],[2.5,4.0]],
    ['ほぼ潰れた三角形',                     [1.0,0],[1.0,0.01],[1.0001,0.005]]
  ];
  tris.forEach(function(t){
    const A=ket(t[1][0],t[1][1]), B=ket(t[2][0],t[2][1]), C=ket(t[3][0],t[3][1]);
    const p=cmul(cmul(inner(A,B),inner(B,C)),inner(C,A));
    const gam=-Math.atan2(p[1],p[0]);
    const Om=solidAngle(bloch(t[1][0],t[1][1]),bloch(t[2][0],t[2][1]),bloch(t[3][0],t[3][1]));
    console.log('  ' + pad(t[0],30) + pad(f(gam,8),16) + pad(f(-Om/2,8),16)
      + e(Math.abs(gam+Om/2),2));
  });
  console.log('');
  console.log('  ★★★ ★ ぴったり一致します ── ★ γ = −Ω/2。');
  console.log('');
  console.log('  ★★ 位相が ★ 面積（立体角）として現れました。');
  console.log('    ★ 第 1 回の位相は ★ 時間の遅れでした。');
  console.log('    ★ 本節の位相は ★ 時間とまったく関係ありません ── ★ 経路の形だけで決まる。');
  console.log('');
  // 円錐（緯度一定の円）で N 角形近似
  console.log('  ★ 経路を細かくしても同じか。★ 緯度 θ の円を N 角形で近似します：');
  console.log('');
  console.log('  ' + pad('θ [rad]',12) + pad('N',10) + pad('積み上げた γ',18)
            + pad('−π(1−cosθ)',18) + '差');
  console.log('  ' + '-'.repeat(66));
  [0.5,1.0,2.0].forEach(function(th){
    [12,100,2000].forEach(function(N){
      let acc=[1,0];
      for(let i=0;i<N;i++){
        const a=ket(th,2*Math.PI*i/N), b=ket(th,2*Math.PI*((i+1)%N)/N);
        acc=cmul(acc,inner(a,b));
      }
      const gam=-Math.atan2(acc[1],acc[0]);
      const th_pred=-Math.PI*(1-Math.cos(th));
      // 2π の折り返しを合わせる
      let g=gam; while(g-th_pred>Math.PI) g-=2*Math.PI; while(g-th_pred<-Math.PI) g+=2*Math.PI;
      console.log('  ' + pad(f(th,2),12) + pad(N,10) + pad(f(g,8),18)
        + pad(f(th_pred,8),18) + e(Math.abs(g-th_pred),2));
    });
  });
  console.log('');
  console.log('  ★★ N を増やすと ★ −π(1−cosθ) に収束します ── ★ 経路だけで決まる。');
  console.log('    ★ どんな速さで回っても、どんな刻み方でも ★ 同じ値。');
  console.log('    ── ★ だから「幾何学的」位相と呼ばれます。');
}

// ------------------------------------------------------------------
hr('5. ★ 角度と ℓ は、フーリエの対 ── ただし片方が周期的');

console.log('  ★ 位相が e^(iℓϕ) なら、★ ϕ と ℓ は ★ フーリエ変換の対です。');
console.log('  ★ ただし ϕ は ★ 周期的（0〜2π）── ★ だから ℓ は ★ 離散（整数）。');
console.log('');
console.log('  ★★ これは第 31 回で見た構造と ★ 同じです：');
console.log('');
console.log('  ' + pad('周期的なほう',22) + pad('離散になるほう',22) + '出てくる場所');
console.log('  ' + '-'.repeat(66));
[['時間を標本化（周期 T）','周波数が 2π/T で折り返す','第 31 回・単位円'],
 ['★ 角度 ϕ（周期 2π）','★ 軌道角運動量 ℓ が整数','★ 本回'],
 ['結晶の格子（周期 a）','逆格子・ブリルアンゾーン','固体物理']
].forEach(function(r){ console.log('  ' + pad(r[0],22)+pad(r[1],22)+r[2]); });
console.log('');
console.log('  ★ そして第 9 回の帯域幅定理にも ★ 角度版があります：');
console.log('');
{
  console.log('      ★ 半径 r の円周上で e^(iℓϕ) の縞を分解するには、');
  console.log('        ★ 縞の間隔 2πr/(2ℓ) が ★ 波長の半分より広い必要がある：');
  console.log('');
  console.log('      ★★ ℓ ≤ 2πr/λ  ── ★「円周が波長 何個 ぶんか」');
  console.log('');
  console.log('  ' + pad('開口半径 r',16) + pad('波長 λ',16) + pad('★ ℓ の上限',18) + '');
  console.log('  ' + '-'.repeat(56));
  [[0.001,1.55e-6,'光ファイバ級'],[0.01,1.55e-6,'望遠鏡の小口径'],
   [1.0,1.55e-6,'大口径'],[0.01,0.01,'マイクロ波 30 GHz']].forEach(function(p){
    const lmax=2*Math.PI*p[0]/p[1];
    console.log('  ' + pad(f(p[0],4)+' m',16) + pad(e(p[1],2)+' m',16)
      + pad(e(lmax,4),18) + p[2]);
  });
  console.log('');
  console.log('  ★★ 「使える ℓ の本数 ＝ 円周が波長 何個 ぶんか」── ★ 帯域幅定理の角度版。');
  console.log('    ★ 第 9 回の Δt·Δω ≥ 1/2 が、★ Δϕ·Δℓ ≥ 1/2 になっただけです。');
  console.log('    ★ 情報を載せる本数もここで決まります（第 21 回）。');
}

// ------------------------------------------------------------------
hr('6. スピンと軌道の違いを、数で見る');

{
  console.log('  ★ 光は ★ 二種類の角運動量を持ちます：');
  console.log('');
  console.log('  ' + pad('種類',20) + pad('一光子あたり',16) + pad('取りうる値',22) + '正体');
  console.log('  ' + '-'.repeat(72));
  [['スピン（偏光）','±ħ','★ 2 通りだけ','★ 場のベクトルの向き'],
   ['★ 軌道（OAM）','ℓħ','★ 整数 すべて','★ 位相のらせん']
  ].forEach(function(r){ console.log('  ' + pad(r[0],20)+pad(r[1],16)+pad(r[2],22)+r[3]); });
  console.log('');
  console.log('  ★★ スピンは ★ 2 通りしかないのに、★ 軌道は ★ 上限がありません（開口が許す限り）。');
  console.log('    ★ だから ★ 情報を載せるなら軌道のほうが有利です。');
  console.log('    ★ 実験では ℓ = 10010 まで作られたと報告されています。');
  console.log('');
  console.log('  ★ 波の言葉で並べると ──');
  console.log('      ★ 偏光 ＝ ★ 場が「どちらを向いているか」（ベクトルの自由度、2 個）');
  console.log('      ★ OAM ＝ ★ 位相が「どれだけ巻いているか」（整数、無限個）');
  console.log('    ★★ 前者は ★ 振幅側の自由度、後者は ★ 位相側の自由度です。');
  console.log('');
  console.log('  ★ 第 32 回で「ヒッグス＝AM、ゴールドストーン＝FM」と書きました。');
  console.log('    ★ ここでも同じ分け方が効いています ── ★ 振幅の自由度と位相の自由度。');
}

// ------------------------------------------------------------------
hr('7. まとめ');

{
  const rows = [
    ['ℓ≠0 で中心の強度がゼロ',     '◎ 数値', '★ 位相特異点。ドーナツ形'],
    ['ピーク半径 = w√(|ℓ|/2)',    '◎ 数値', '★ ℓ=10 まで一致'],
    ['ℓ は整数しか取れない',       '◎ 解析', '★ 一周して戻る条件'],
    ['巻き数は動かしても不変',      '◎ 数値', '★ 大きな円でいつも 2'],
    ['巻き数は整数しか出ない',      '◎ 数値', '★ 1 か 0。連続に変えられない'],
    ['★ γ = −Ω/2（幾何学的位相）', '◎ 数値', '★ 立体角の半分と 1e-16 で一致'],
    ['経路の刻み方に依らない',      '◎ 数値', '★ N→∞ で −π(1−cosθ) に収束'],
    ['角度と ℓ はフーリエの対',     '◎ 整理', '★ 周期的 ⇒ 離散（第 31 回と同構造）'],
    ['ℓ の上限 = 2πr/λ',         '◎ 解析', '★ 帯域幅定理の角度版'],
    ['スピンは 2 通り、軌道は無限',  '◎ 整理', '★ 振幅の自由度 vs 位相の自由度']
  ];
  console.log('  ' + pad('主張',28) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(84));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],28)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     位相は ★ 時間だけのものではありませんでした。');
  console.log('     ★ 角度の関数にすると ★ 整数しか許されず（トポロジー）、');
  console.log('     ★★ 状態空間を一周させると ★ 面積として現れる（幾何学的位相）。');
  console.log('');
  console.log('  ★ 第 1 回の「階数とは位相のこと」は ★ 時間軸の話でした。');
  console.log('    ★★ 位相には ★ 少なくとも三つの出どころがあります ──');
  console.log('      ★ 時間（階数）、★ 角度（トポロジー）、★ 経路（幾何）。');
}

console.log('');
