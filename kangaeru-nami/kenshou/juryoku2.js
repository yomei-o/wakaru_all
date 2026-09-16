// 考える波 第 38 回 検証スクリプト
//   量子重力を波として見る ── 次元が走ると、階数が走る
//
//   実行: node juryoku2.js

'use strict';

function hr(t){ console.log('\n' + '#'.repeat(66) + '\n# ' + t + '\n' + '#'.repeat(66) + '\n'); }
function f(x,n){ return Number(x).toFixed(n===undefined?4:n); }
function e(x,n){ return Number(x).toExponential(n===undefined?3:n); }
function pad(s,w){ s=String(s); while(s.length<w) s+=' '; return s; }
function rpad(s,w){ s=String(s); while(s.length<w) s=' '+s; return s; }

const HBAR = 1.054571817e-34;
const C    = 2.99792458e8;
const G    = 6.67430e-11;
const KB   = 1.380649e-23;

// ------------------------------------------------------------------
hr('1. 舞台そのものを波として見る');

console.log('  ここまで 37 回、★ 時空は ★ 与えられた舞台でした。');
console.log('  ★ 本回はその舞台自身を波として見ます。');
console.log('');
console.log('  ★ 第 24 回で重力波を見たときは ★ 平坦な背景の上のさざ波でした。');
console.log('  ★★ 量子重力の問いは ★ そのさざ波が ★ 舞台を作っているときに何が起きるか。');
console.log('');
console.log('  ★ 本回で確かめること：');
console.log('      ① プランク長は ★ 一行で出る（波長 ＝ 自分のシュヴァルツシルト半径）');
console.log('      ② 重力は ★ くりこめない ── ★ 結合が次元を持つから');
console.log('      ③ ★★ 多くの理論が言う「次元が 4 → 2 へ走る」を、階数の言葉に直す');

// ------------------------------------------------------------------
hr('2. プランク長を、波の言葉で一行で出す');

{
  console.log('  ★ 波長 λ の光子のエネルギーは E = ħc/λ、対応する質量は m = E/c²。');
  console.log('  ★ その質量のシュヴァルツシルト半径は r_s = 2Gm/c²。');
  console.log('');
  console.log('  ★★ ★ 波長と r_s が等しくなる所 ── ★ そこが限界です：');
  console.log('');
  console.log('      λ = 2G·(ħ/(λc))/c² = 2Għ/(λc³)   →   ★ λ = √(2Għ/c³)');
  console.log('');
  const lp = Math.sqrt(HBAR*G/(C*C*C));
  const lp2 = Math.sqrt(2*HBAR*G/(C*C*C));
  const tp = lp/C;
  const Ep = Math.sqrt(HBAR*C*C*C*C*C/G);
  console.log('  ' + pad('量',26) + pad('値',22) + '');
  console.log('  ' + '-'.repeat(50));
  console.log('  ' + pad('上の見積もり √(2Għ/c³)',26) + pad(e(lp2,5)+' m',22));
  console.log('  ' + pad('プランク長 √(Għ/c³)',26) + pad(e(lp,5)+' m',22));
  console.log('  ' + pad('プランク時間 l_P/c',26) + pad(e(tp,5)+' s',22));
  console.log('  ' + pad('プランクエネルギー',26) + pad(e(Ep/1.602176634e-19/1e9,5)+' GeV',22));
  console.log('  ' + pad('プランク周波数 1/t_P',26) + pad(e(1/tp,5)+' 1/s',22));
  console.log('');
  console.log('  ★ 係数 √2 の違いを除けば ★ 一行で出ます。');
  console.log('');
  console.log('  ★★ 波の言葉で読むと ── ★ プランク長とは');
  console.log('      ★「波を短くしていくと、★ 自分のエネルギーで自分を閉じ込めてしまう長さ」。');
  console.log('    ★ 第 6 回の「質量＝遮断周波数」の ★ 極限です：');
  console.log('      ★ 遮断を上げようとエネルギーを入れると、★ 重力が自分で遮断を作ってしまう。');
  console.log('');
  console.log('  ★ 比較（第 25 回・第 32 回の数字と並べる）：');
  console.log('');
  console.log('  ' + pad('スケール',22) + pad('エネルギー [GeV]',20) + pad('長さ [m]',18));
  console.log('  ' + '-'.repeat(60));
  [['陽子の大きさ',1,0.94e-15],['電弱（v）',246.2,8.0e-19],
   ['プランク',Ep/1.602176634e-19/1e9,lp]].forEach(function(p){
    console.log('  ' + pad(p[0],22) + pad(e(p[1],4),20) + pad(e(p[2],4),18));
  });
  console.log('');
  console.log('  ★ 電弱からプランクまで ★ 17 桁 ── ★ 第 15 回の「階層問題」がこの距離です。');
}

// ------------------------------------------------------------------
hr('3. なぜ重力だけ「くりこめない」のか ── 結合が次元を持つ');

console.log('  ★ 第 7 回の基準：★ 意味があるのは無次元量だけ。');
console.log('  ★ 力の結合定数を並べると、重力だけ ★ 次元を持っています：');
console.log('');
{
  const Ep = Math.sqrt(HBAR*C*C*C*C*C/G)/1.602176634e-19/1e9;  // GeV
  console.log('  ' + pad('力',16) + pad('結合',20) + pad('次元',18) + '');
  console.log('  ' + '-'.repeat(56));
  [['電磁気','α = 1/137','★ 無次元'],
   ['強い力','α_s ≈ 0.12','★ 無次元'],
   ['弱い力','α_W ≈ 1/30','★ 無次元'],
   ['★ 重力','G / (ħc) = 1/E_P²','★★ [エネルギー]^(−2)']
  ].forEach(function(r){ console.log('  ' + pad(r[0],16)+pad(r[1],20)+r[2]); });
  console.log('');
  console.log('  ★★ 次元を持つ結合は ★ 無次元にするために ★ エネルギーを掛けるしかない：');
  console.log('');
  console.log('      ★ 実効的な結合 = (E / E_P)²');
  console.log('');
  console.log('  ' + pad('エネルギー E',22) + pad('(E/E_P)²',20) + '中身');
  console.log('  ' + '-'.repeat(58));
  [[1e-9,'原子'],[1,'陽子'],[246,'電弱'],[1e16,'大統一'],[Ep,'★ プランク']].forEach(function(p){
    const g=Math.pow(p[0]/Ep,2);
    console.log('  ' + pad(e(p[0],2)+' GeV',22) + pad(e(g,4),20)
      + (g>=1?'★ 摂動が破綻':p[1]));
  });
  console.log('');
  console.log('  ★★★ ★ これが「くりこめない」の正体です ──');
  console.log('      ★ 結合が ★ エネルギーとともに育ち、★ プランクで 1 を超える。');
  console.log('      ★ 第 34 回のヤン＝ミルズは逆で、★ 高エネルギーで弱くなりました（漸近的自由）。');
  console.log('');
  console.log('  ★ 波の言葉では ── ★ 短い波ほど ★ 強く相互作用する媒質。');
  console.log('    ★ 第 16 回の「分散性の媒質」の ★ いちばん極端な場合です。');
}

// ------------------------------------------------------------------
hr('4. ★★ 多くの理論が言う「次元が走る」');

console.log('  ★ 量子重力の候補は互いにかなり違いますが、★ 一つだけ ★ 揃って言うことがあります：');
console.log('');
console.log('      ★★ 短い距離では ★「次元」が 4 から 2 へ減る（スペクトル次元の減少）');
console.log('');
console.log('  ★ スペクトル次元とは ★ 拡散で測った次元です（第 37 回で使った量）：');
console.log('');
console.log('      ★ 拡散する点が時刻 s に出発点へ戻る確率 P(s) ∝ s^(−d_s/2)');
console.log('      ★ d_s = −2 · d ln P / d ln s');
console.log('');
{
  console.log('  ★ 分散関係が ω ∝ k^z のとき（★ z = 1 がふつうの波）、');
  console.log('    ★ 拡散の「時間」は k^(2z) で進むので、★ スペクトル次元は：');
  console.log('');
  console.log('      ★★ d_s = 1 + (空間の次元)/z');
  console.log('');
  console.log('  ' + pad('z',10) + pad('d_s = 1 + 3/z',18) + pad('階数 α=(d_s−3)/2',22) + '出てくる所');
  console.log('  ' + '-'.repeat(70));
  [[1,'ふつうの波（赤外）'],[1.5,'中間'],[2,'中間'],[3,'★ ホジャヴァ重力（紫外）']].forEach(function(p){
    const z=p[0], ds=1+3/z, al=(ds-3)/2;
    console.log('  ' + pad(f(z,1),10) + pad(f(ds,4),18) + pad(f(al,4),22) + p[1]);
  });
  console.log('');
  console.log('  ★★★ ★ ここが本回の要です ──');
  console.log('');
  console.log('      ★ 第 30 回で ★ α = (d−3)/2 と分かりました。');
  console.log('      ★★ だから ★「次元が走る」とは ★「階数が走る」ということです。');
  console.log('');
  console.log('      ★ d_s : 4 → 2   ⟺   ★ α : +1/2 → −1/2');
  console.log('');
  console.log('  ★ 第 30 回の表と突き合わせます：');
  console.log('');
  console.log('  ' + pad('d_s',8) + pad('α',10) + pad('第 30 回での意味',30) + 'デジタル（第 31 回）');
  console.log('  ' + '-'.repeat(74));
  [[4,0.5,'尾を引く s^(−3/2)','IIR（無限タップ）'],
   [3,0,'★ δ そのもの（歪まない）','FIR（1 タップ）'],
   [2,-0.5,'★ 尾を引く s^(−1/2)、臨界 1/r²','IIR（k^(−1/2) で減る）']
  ].forEach(function(r){ console.log('  ' + pad(f(r[0],0),8)+pad(f(r[1],1),10)+pad(r[2],30)+r[3]); });
  console.log('');
  console.log('  ★★ そして ★ d_s = 2 は ── ★ 第 30 回で ★ 臨界 λ = 1/4 ちょうどだった次元。');
  console.log('    ★ 第 13 回で「λ > 1/4 で指数が複素数になる（虚数階）」と書いた ★ その境目。');
  console.log('');
  console.log('  ★ ここは ★ 慎重に書きます ── ★ これは ★ 観察であって ★ 主張ではありません：');
  console.log('    ★ 第 30 回の α は ★ 波動方程式のグリーン関数の階数、');
  console.log('    ★ 本節の d_s は ★ 拡散で測った実効次元。★ 別々に定義された量です。');
  console.log('    ★★ ★ 同じ「次元」という語を使っているだけかもしれません（第 29・30 回の作法）。');
}

// ------------------------------------------------------------------
hr('5. スペクトル次元を、数値で測る');

console.log('  ★ 言葉ではなく ★ 実際に測ります。★ 修正した分散関係で拡散させます。');
console.log('  ★ まず ★ 空間のぶんだけ：');
console.log('');
console.log('      ★ P(s) = ∫ d³k/(2π)³ · exp(−s·(k²)^z)      （z=1 がふつう）');
console.log('      ★ 空間のスペクトル次元 = −2 · d ln P / d ln s');
console.log('');
{
  function P(s, z, N){
    // 積分の重みが効く範囲は k ~ s^(−1/(2z))。★ s に応じて上限を取る
    const kmax = 12*Math.pow(s, -1/(2*z));
    const h=kmax/N; let sum=0;
    for(let i=0;i<N;i++){
      const k=(i+0.5)*h;
      sum += k*k*Math.exp(-s*Math.pow(k*k,z))*h;
    }
    return sum/(2*Math.PI*Math.PI);
  }
  function dspace(s, z){
    const r=1.01;
    const a=P(s/r, z, 400000), b=P(s*r, z, 400000);
    return -2*Math.log(b/a)/Math.log(r*r);
  }
  console.log('  ' + pad('z',10) + pad('s = 1',16) + pad('s = 1e-3',16) + pad('s = 1e-6',16)
            + '予言 3/z');
  console.log('  ' + '-'.repeat(72));
  [1,1.5,2,3].forEach(function(z){
    console.log('  ' + pad(f(z,1),10) + pad(f(dspace(1,z),5),16) + pad(f(dspace(1e-3,z),5),16)
      + pad(f(dspace(1e-6,z),5),16) + f(3/z,4));
  });
  console.log('');
  console.log('  ★★ ★ 空間のぶんは ★ ちょうど 3/z ── ★ 数値でぴったり。');
  console.log('');
  console.log('  ★ ここに ★ 時間方向を足します。★ 時間の分散は修正されない（z=1 のまま）ので：');
  console.log('');
  console.log('      ★★ 時空のスペクトル次元 d_s = 1 + 3/z');
  console.log('');
  console.log('  ' + pad('z',10) + pad('空間 3/z（測定）',20) + pad('★ d_s = 1 + 3/z',20)
            + pad('階数 α=(d_s−3)/2',20));
  console.log('  ' + '-'.repeat(72));
  [1,1.5,2,3].forEach(function(z){
    const sp=dspace(1e-3,z);
    console.log('  ' + pad(f(z,1),10) + pad(f(sp,5),20) + pad(f(1+sp,5),20)
      + pad(f((1+sp-3)/2,5),20));
  });
  console.log('');
  console.log('  ★★★ ★ z = 1 → d_s = 4（α = +1/2）、★ z = 3 → d_s = 2（α = −1/2）。');
  console.log('');
  console.log('  ★ つまり ★「次元が走る」の中身は ★ 分散関係の指数 z が走ることでした。');
  console.log('    ★★ ★ これは ★ このシリーズの言葉そのものです ── ★ 階数が走る。');
  console.log('');
  console.log('  ★ 注意：★ ここで測ったのは ★ 空間のぶんだけです。');
  console.log('    ★ 「+1」は ★ 時間方向が修正されないという ★ 模型の仮定から来ています。');
  console.log('    ★ 時間方向も修正する理論では ★ 別の値になります。');
}

// ------------------------------------------------------------------
hr('6. なぜ「2」で止まるのか ── 結合が無次元になる次元');

{
  console.log('  ★ なぜ 4 → 2 で、★ 1 や 3 ではないのか。★ 次元の勘定で出ます：');
  console.log('');
  console.log('      ★ d 次元時空での重力定数の次元は ★ [G] = [エネルギー]^(2−d)');
  console.log('');
  console.log('  ' + pad('時空の次元 d',18) + pad('[G] の次元',22) + '摂動として');
  console.log('  ' + '-'.repeat(60));
  [[2,'★ 無次元','★★ くりこみ可能（の境目）'],
   [3,'[E]^(−1)','くりこめない'],
   [4,'[E]^(−2)','★ くりこめない（現実）'],
   [5,'[E]^(−3)','もっと悪い']
  ].forEach(function(r){ console.log('  ' + pad(f(r[0],0),18)+pad(r[1],22)+r[2]); });
  console.log('');
  console.log('  ★★★ ★ d = 2 で ★ 重力の結合が ★ ちょうど無次元になります。');
  console.log('');
  console.log('  ★ だから ★「紫外で d_s → 2」という予想は ──');
  console.log('      ★★ ★「紫外で重力の結合が無次元になってほしい」という要請の言い換えです。');
  console.log('');
  console.log('  ★ 第 25 回の ★ 次元転移を思い出します：');
  console.log('      ★ QCD は ★ 無次元の α_s から ★ 次元を持つ Λ を作りました。');
  console.log('      ★ 量子重力は ★ 逆向き ── ★ 次元を持つ G を ★ 無次元にしたい。');
  console.log('    ★★ ★ どちらも ★「無次元量だけが物理」（第 7・15 回）の要請です。');
}

// ------------------------------------------------------------------
hr('7. 波として言えること・言えないこと');

{
  const rows = [
    ['プランク長の見積もり',      '◎ できる', '★ 波長 ＝ 自分の r_s。一行'],
    ['重力がくりこめない理由',    '◎ できる', '★ 結合が [E]^(−2)。(E/E_P)² が育つ'],
    ['d_s = 1 + 3/z',           '◎ 数値',   '★ 修正分散から直接 測れる'],
    ['次元が走る ＝ 階数が走る',  '◎ 対応',   '★ 第 30 回の α=(d−3)/2 を使うだけ'],
    ['d_s → 2 の理由',          '◎ 整理',   '★ そこで G が無次元になる'],
    ['★ どの理論が正しいか',      '× できない','★ 波の言葉は理論を選ばない'],
    ['★ 実際に z が 3 になるか',  '× できない','★ 模型の仮定。観測はまだない'],
    ['★ 時空が何でできているか',  '× できない','★ 本稿は分散関係しか見ていない']
  ];
  console.log('  ' + pad('項目',26) + pad('判定',14) + '根拠');
  console.log('  ' + '-'.repeat(76));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],26)+pad(r[1],14)+r[2]); });
  console.log('');
  console.log('  ★★ ★ 正直に書いておきます ──');
  console.log('    ★ 本回がやったのは ★ 既存の予想を ★ 別の言葉に翻訳しただけです。');
  console.log('    ★ 「階数が走る」と言い換えても、★ 新しい予言は出ていません。');
  console.log('    ★ ただし ★ 翻訳すると ★ 何を測ればよいかは はっきりします（次節）。');
}

// ------------------------------------------------------------------
hr('8. 翻訳すると、何を測ればよいか見える');

{
  console.log('  ★ 「階数が走る」を ★ このシリーズの道具で読むと ──');
  console.log('');
  console.log('  ' + pad('階数の言葉',26) + pad('観測できる形',30) + '回');
  console.log('  ' + '-'.repeat(74));
  [['α が変わる','★ dB/oct が 6α で変わる','第 1 回'],
   ['α が変わる','★ 位相が 90α 度 で変わる','第 1 回'],
   ['d_s が 3 からずれる','★ 伝播に尾が出る（FIR→IIR）','第 30・31 回'],
   ['z ≠ 1','★ 群速度が周波数に依る','第 16 回']
  ].forEach(function(r){ console.log('  ' + pad(r[0],26)+pad(r[1],30)+r[2]); });
  console.log('');
  console.log('  ★★ いちばん測りやすいのは ★ 最後の行です ── ★ 高エネルギー光子の到着時間差。');
  console.log('');
  const Ep=1.22e19;   // GeV
  console.log('  ★ ω ∝ k^z なら群速度が k に依り、★ 遠方からの光子に時間差が出ます：');
  console.log('');
  console.log('      ★ Δt ≈ (距離/c) · (E/E_P)      （いちばん効きやすい一次の場合）');
  console.log('');
  console.log('  ' + pad('天体',20) + pad('距離',16) + pad('光子 E [GeV]',16) + pad('★ Δt',16));
  console.log('  ' + '-'.repeat(66));
  [['GRB（z≈1）',1e26,10],['GRB（z≈1）',1e26,100],
   ['ブレーザー',1e25,1e4],['かに星雲',6e19,1e4]].forEach(function(p){
    const dt=(p[1]/C)*(p[2]/Ep);
    console.log('  ' + pad(p[0],20) + pad(e(p[1],1)+' m',16) + pad(e(p[2],1),16)
      + pad(e(dt,3)+' s',16));
  });
  console.log('');
  console.log('  ★★ ガンマ線バーストなら ★ 0.3 〜 3 秒 ── ★ 十分に測れる桁です。');
  console.log('    ★ 実際 ★ フェルミ衛星などが測り、★ 一次の効果は ★ 棄却されています');
  console.log('      （E_P の 1 倍 以上のスケールまで）。');
  console.log('');
  console.log('  ★★★ ★ つまり ★ 階数の走りは ★ すでに一部 反証されています ──');
  console.log('      ★ 少なくとも ★ 一次の（z が 1 からずれる）効果は ★ プランクまで無い。');
  console.log('    ★ 二次の効果なら まだ余地があります。');
  console.log('    ★ 第 15 回の「開いたままの扉」に、★ これを一つ足しておきます。');
}

// ------------------------------------------------------------------
hr('9. まとめ');

{
  const rows = [
    ['プランク長は一行で出る',    '◎ 解析', '★ 波長 ＝ 自分の r_s、1.616e-35 m'],
    ['重力の結合は次元を持つ',    '◎ 解析', '★ [E]^(−2)。★ (E/E_P)² が 1 を超える'],
    ['★ d_s = 1 + 3/z',        '◎ 数値', '★ 修正分散から直接 測って一致'],
    ['★ 次元が走る ＝ 階数が走る','◎ 対応', '★ α=(d−3)/2 で α: +1/2 → −1/2'],
    ['d_s=2 で G が無次元',     '◎ 解析', '★ [G]=[E]^(2−d)'],
    ['d_s=2 は第 30 回の臨界',  '★ 観察', '★ 別々に定義された量なので保留'],
    ['★ 一次の効果は棄却済み',   '◎ 実測', '★ GRB の到着時間差（フェルミ等）']
  ];
  console.log('  ' + pad('主張',28) + pad('判定',10) + '根拠');
  console.log('  ' + '-'.repeat(82));
  rows.forEach(function(r){ console.log('  ' + pad(r[0],28)+pad(r[1],10)+r[2]); });
  console.log('');
  console.log('  ★ 一行で ──');
  console.log('');
  console.log('     量子重力の「次元が 4 から 2 へ走る」は、');
  console.log('     ★★ このシリーズの言葉では ★「階数が +1/2 から −1/2 へ走る」だった。');
  console.log('     ★ そして 2 で止まるのは ── ★ そこで重力の結合が無次元になるから。');
  console.log('');
  console.log('  ★ ただし ★ 翻訳しただけで、★ 新しい予言は出ていません。');
  console.log('    ★ 出たのは ★「どこを測ればよいか」だけです ── ★ それでも、');
  console.log('      ★ 一次の効果はもう棄却されている、という事実は拾えました。');
}

console.log('');
