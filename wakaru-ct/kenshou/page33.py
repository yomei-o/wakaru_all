# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第 IV 部でいちばん紛らわしい二つを並べます ── <strong>ミルン宇宙</strong>と <strong>\(R_h=ct\)</strong>。どちらも「\(a\propto t\)」で、どちらも「減速も加速もしない」と言われます。ところが<em>まったく別物</em>です。第3回で「\(c\cdot t=\)一定 は座標変換ではなく共形変換」と書きましたが、その区別を<strong>いちばん紛らわしい相手</strong>に当てます。そして<em>見分ける手続き</em>を作ります。</p>

<h2><span class="n">01</span>どちらも \(a\propto t\)。違いは \(k\) と中身だけ</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">ミルン宇宙</th><th class="mid">\(R_h=ct\)</th></tr></thead>
<tbody>
<tr><th>スケール因子</th><td class="mid">\(a\propto t\)</td><td class="mid">\(a\propto t\)</td></tr>
<tr class="hi"><th>中身</th><td class="mid"><strong>空（\(\rho=0\)）</strong></td><td class="mid"><strong>物質が入っている</strong></td></tr>
<tr class="hi"><th>空間曲率</th><td class="mid"><strong>\(k=-1\)</strong></td><td class="mid"><strong>\(k=0\)</strong></td></tr>
<tr><th>全体の状態方程式</th><td class="mid">──</td><td class="mid">\(w=-1/3\)</td></tr>
</tbody>
</table>
</div>

<p>見た目の \(a(t)\) は同じです。違うのは \(k\) と中身だけ ── <strong>そしてそれが決定的でした。</strong></p>

<h2><span class="n">02</span>スカラー曲率を計算すると、決着がつく</h2>

<div class="calc">
<span class="tag">計算 ── 一行</span>
<p class="lbl">FLRW のスカラー曲率（\(c=1\)）</p>
$$R=6\left[\frac{\ddot a}{a}+\left(\frac{\dot a}{a}\right)^2+\frac{k}{a^2}\right]$$
<p class="lbl">\(a=t\) を入れると \(\ddot a=0\)、\(\dot a/a=1/t\) なので</p>
$$R=\frac{6(1+k)}{t^2}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(k\)</th><th class="mid">\(R\)</th><th class="mid">正体</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">\(-1\)</th><td class="mid"><strong>\(0\)</strong></td><td class="mid"><strong>ミルン ── 厳密に平坦</strong></td></tr>
<tr><th class="mid">\(0\)</th><td class="mid">\(6/t^2\)</td><td class="mid">\(R_h=ct\)</td></tr>
<tr><th class="mid">\(+1\)</th><td class="mid">\(12/t^2\)</td><td class="mid">（参考：閉じた場合）</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0"><strong>\(k=-1\) でちょうどゼロ。</strong> しかもスカラー曲率だけでなく、<em>リーマンテンソル全体が恒等的にゼロ</em>です。<br>
── <strong>ミルン宇宙は、座標を取り替えたミンコフスキー時空そのものでした。</strong></p>
</div>

<div class="calc">
<span class="tag">今日の値</span>
$$R_{h}=ct:\quad R=\frac{6}{(ct_0)^2}=3.52\times10^{-52}\ \mathrm{m^{-2}}\qquad\Longrightarrow\qquad \frac{1}{\sqrt R}=1.73\ \mathrm{Gpc}$$
$$\text{ミルン}:\quad R=0\ (\text{厳密に})$$
</div>

<h2><span class="n">03</span>核心 ── 三段の判定手続き</h2>

<p>この違いは、一般の時空に使える<strong>手続き</strong>になります。</p>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>リーマンテンソルは恒等的にゼロか？</strong><span>Yes → <em>座標変換だけで平坦時空に戻せる</em>。物理的な中身はゼロ</span></div></div>
<div class="row hi"><div class="mk">2</div><div class="txt"><strong>ゼロでないなら、ワイルテンソル \(C\) はゼロか？</strong><span>Yes → <em>共形変換でミンコフスキーにできる</em>。ただし質量が動く（第4回）</span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>\(C\) もゼロでないなら</strong><span>どちらでも消せない。第6回でいう「ワイル側」＝本物の重力場</span></div></div>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>時空</th><th class="mid">リーマン</th><th class="mid">ワイル \(C\)</th><th class="mid">何が要るか</th></tr></thead>
<tbody>
<tr><th>ミンコフスキー</th><td class="mid">\(0\)</td><td class="mid">\(0\)</td><td class="mid">何もしなくてよい</td></tr>
<tr class="hi"><th>ミルン</th><td class="mid">\(0\)</td><td class="mid">\(0\)</td><td class="mid"><strong>座標変換だけ（Step 1）</strong></td></tr>
<tr class="hi"><th>\(R_h=ct\)</th><td class="mid">\(\ne0\)</td><td class="mid">\(0\)</td><td class="mid"><strong>共形変換が要る（Step 2）</strong></td></tr>
<tr><th>\(\Lambda\)CDM</th><td class="mid">\(\ne0\)</td><td class="mid">\(0\)</td><td class="mid">共形変換が要る（Step 2）</td></tr>
<tr><th>シュヴァルツシルト</th><td class="mid">\(\ne0\)</td><td class="mid">\(\ne0\)</td><td class="mid">どちらでも消せない（Step 3）</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>すべての FLRW は Step 2 に入ります</strong>（ワイルがゼロ、リッチが非ゼロ）。<br>
── <em>このシリーズが第1回からずっといた場所が、この一行で特定されました。</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>光度距離を比べると、意外なことが起きる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(z\)</th><th class="mid">\(\Lambda\)CDM</th><th class="mid">ミルン</th><th class="mid">\(R_h=ct\)</th><th class="mid">\(\Delta\mu\) ミルン</th><th class="mid">\(\Delta\mu\) \(R_h=ct\)</th></tr></thead>
<tbody>
<tr><th class="mid">0.3</th><td class="mid">0.3613</td><td class="mid">0.3450</td><td class="mid">0.3411</td><td class="mid">−0.101</td><td class="mid">−0.125</td></tr>
<tr><th class="mid">0.5</th><td class="mid">0.6580</td><td class="mid">0.6250</td><td class="mid">0.6082</td><td class="mid">−0.112</td><td class="mid">−0.171</td></tr>
<tr class="hi"><th class="mid">1.0</th><td class="mid">1.5292</td><td class="mid"><strong>1.5000</strong></td><td class="mid">1.3863</td><td class="mid"><strong>−0.042</strong></td><td class="mid">−0.213</td></tr>
<tr><th class="mid">1.5</th><td class="mid">2.5188</td><td class="mid">2.6250</td><td class="mid">2.2907</td><td class="mid">+0.090</td><td class="mid">−0.206</td></tr>
<tr><th class="mid">2.0</th><td class="mid">3.6837</td><td class="mid">4.0000</td><td class="mid">3.2958</td><td class="mid">+0.179</td><td class="mid">−0.181</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0">驚くべきことに、\(z=1\) では <strong>ミルンのほうが \(\Lambda\)CDM に近い</strong>（1.500 対 1.529、ずれ 0.042 等）。<br>
<em>中身が空っぽの時空が、\(R_h=ct\) より良くハッブル図に合っています。</em><br>
── <strong>「ハッブル図に合う」は、モデルの検定として弱い。</strong></p>
</div>

<div class="fig">
<p class="cap">図：\(\Lambda\)CDM からのずれ（等級）。<strong>灰色の帯は超新星 1 本の内在的ばらつき（0.15 等）</strong>。ツマミで赤方偏移を動かすと、<em>その \(z\) で 5σ の区別に何本必要か</em>が読めます</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>赤方偏移 \(z\)<input id="sz" type="range" min="5" max="200" value="100" step="1"></label>
  <span class="val" id="vz">z = 1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a3a4a"></i>ミルン</span>
  <span><i class="swatch" style="background:#9a6a2a"></i>\(R_h=ct\)</span>
  <span><i class="swatch" style="background:#d5d9dd"></i>超新星 1 本のばらつき</span>
</div>
</div>

<h2><span class="n">05</span>それでもミルンは、完全に排除されている</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>観測</th><th class="mid">なぜ通らないか</th></tr></thead>
<tbody>
<tr><th>CMB の音響ピーク</th><td class="mid">バリオンが無いので、音波が立たない</td></tr>
<tr><th>元素合成</th><td class="mid">物質が無いので、\(^4\)He も D も作れない</td></tr>
<tr><th>構造形成</th><td class="mid">重力で集まる物質が無い</td></tr>
<tr class="hi"><th>\(\Omega_m\) の測定</th><td class="mid"><strong>\(\Omega_m=0.315\pm0.007\)</strong> ── \(\Omega_m=0\) とは 45σ 以上</td></tr>
</tbody>
</table>
</div>

<p><strong>幾何が良くても、中身が無ければ物理になりません。</strong> 第25回の言葉で言えば ── <em>\(L(\text{残差})\) はハッブル図だけで決まらない</em>。この一点だけ見れば「ミルンのほうがまし」に見えても、他のデータセットを入れた瞬間に消し飛びます（第29回で MOND について見たのと、同じ構造です）。</p>

<h2><span class="n">06</span>種明かし ── 混同の元と、その解き方</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">ミルン</th><th class="mid">\(R_h=ct\)</th></tr></thead>
<tbody>
<tr><th>言われ方</th><td class="mid">「\(a\propto t\)、減速も加速もしない」</td><td class="mid">同じ</td></tr>
<tr class="hi"><th>\(k\)</th><td class="mid">\(-1\)</td><td class="mid">\(0\)</td></tr>
<tr class="hi"><th>リーマン</th><td class="mid">\(0\)</td><td class="mid">\(\ne0\)</td></tr>
<tr class="hi"><th>要る操作</th><td class="mid"><strong>座標変換</strong></td><td class="mid"><strong>共形変換</strong></td></tr>
<tr><th>物理の中身</th><td class="mid">ゼロ</td><td class="mid">質量が動く</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">06節の結論</p>
<p style="margin:6px 0 0">見分け方は一つ ── <strong>\(k\) を見る。</strong><br>
\(k=-1\)（＋空）なら座標変換で済み、<em>物理の中身はゼロ</em>。<br>
\(k=0\)（＋物質）なら共形変換が要り、<em>質量が動く</em>。<br>
── <strong>第3回で「座標変換ではなく共形変換」と書いたことの、いちばん具体的な意味がこれです。</strong></p>
</div>

<h2><span class="n">07</span>このシリーズは、どこにいたのか</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>ミルンなら Step 1</strong><span>もともと平坦なので、<em>質量すら動かす必要がない</em></span></div></div>
<div class="row hi"><div class="mk">2</div><div class="txt"><strong>FLRW は全部 Step 2</strong><span>ワイル \(=0\)、リッチ \(\ne0\)。だから第4回で「消せるものを全部消したら質量ひとつ」ができた</span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>シュヴァルツシルトなら Step 3</strong><span>共形変換では平坦にできない ── ブラックホールが第6回で「動かない側」だったのは、これ</span></div></div>
</div>

<p><strong>このシリーズの道具が効く範囲は、Step 2 の行にぴったり一致します。</strong> 第13回で「共形変換は大きさにしか触れない」、第16回で「動かせるのは使われていない側だけ」と測りました ── <em>今回はそれを幾何学の言葉で言い直したことになります</em>。</p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① ミルン宇宙が平坦時空であることは、厳密な結果です。</strong> 座標変換 \(T=t\cosh\chi,\ R=ct\sinh\chi\) でミンコフスキー時空の（光円錐の内側の）一部分になります ── <em>「一部分」であることは重要で、ミルン座標はミンコフスキー時空全体を覆いません</em>。</p>
<p style="margin:0 0 10px"><strong>② 「すべての FLRW はワイル \(=0\)」は、等方一様性の帰結です。</strong> ゆらぎを入れれば \(C\ne0\) になり、Step 3 に移ります ── <strong>実際の宇宙は完全な FLRW ではなく、だから第6回の使用率が \(0\) ではありません</strong>（\(1.5\times10^{-18}\)）。02節・03節の表は<em>背景時空についての言明</em>です。</p>
<p style="margin:0 0 10px"><strong>③ 04節の \(\Lambda\)CDM は \(\Omega_m=0.315\)、\(\Omega_r=9.2\times10^{-5}\) による本稿の数値積分です。</strong> ミルンの \(H_0d_L/c=z(1+z/2)\) と \(R_h=ct\) の \((1+z)\ln(1+z)\) は閉じた式です。<em>実際の超新星解析では絶対等級（定数項）を自由にするので、ここでの \(\Delta\mu\) をそのまま有意性に直すことはできません</em> ── 図の「必要な本数」は<strong>定数項を固定した場合の目安</strong>です。</p>
<p style="margin:0 0 10px"><strong>④ 「ミルンのほうが \(\Lambda\)CDM に近い」は \(z\simeq1\) 付近での話です。</strong> \(z=0.5\) では \(R_h=ct\) と大差なく、\(z=2\) では逆にミルンのほうが遠い（\(+0.179\) 等）。<em>特定の \(z\) を選べば話が変わる</em>ので、桁と傾向として読んでください。</p>
<p style="margin:0"><strong>⑤ \(R_h=ct\) の判定は第3回で扱った通りです。</strong> 本稿は \(R_h=ct\) の是非を再検討するものではなく、<em>ミルンとの構造的な違い</em>だけを扱っています。学術的な標準は \(\Lambda\)CDM です。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>\(a=t\) の FLRW でスカラー曲率を求め、\(k=-1\) でゼロになることを示せ。
<details><summary>答えを見る</summary><div class="ans">\(R=6[\ddot a/a+(\dot a/a)^2+k/a^2]\) に \(a=t\) を入れると \(\ddot a=0\)、\(\dot a/a=1/t\)、\(k/a^2=k/t^2\) なので \(R=6(1+k)/t^2\)。<strong>\(k=-1\) でちょうどゼロ</strong>です。</div></details></li>

<li>ミルンと \(R_h=ct\) の、いちばん本質的な違いは何か。
<details><summary>答えを見る</summary><div class="ans"><strong>リーマンテンソルがゼロかどうか。</strong> ミルンは恒等的にゼロ（＝座標を取り替えたミンコフスキー時空）、\(R_h=ct\) は \(R=6/(ct)^2\ne0\)。<em>だからミルンは座標変換で済み、\(R_h=ct\) は共形変換が要ります。</em></div></details></li>

<li>三段の判定手続きを述べ、\(\Lambda\)CDM とシュヴァルツシルトを分類せよ。
<details><summary>答えを見る</summary><div class="ans">Step 1：リーマン \(=0\) → 座標変換で済む。Step 2：リーマン \(\ne0\) でワイル \(=0\) → 共形変換が要る。Step 3：ワイル \(\ne0\) → どちらでも消せない。<strong>\(\Lambda\)CDM は Step 2</strong>（すべての FLRW がそう）、<strong>シュヴァルツシルトは Step 3</strong>。</div></details></li>

<li>\(z=1\) で、\(\Lambda\)CDM に近いのはどちらか。
<details><summary>答えを見る</summary><div class="ans"><strong>ミルン</strong>（1.500 対 \(\Lambda\)CDM の 1.529、ずれ 0.042 等）。\(R_h=ct\) は 1.386 でずれ 0.213 等。<em>中身が空っぽの時空が、\(R_h=ct\) より良くハッブル図に合います</em> ── だから「ハッブル図に合う」はモデルの検定として弱い。</div></details></li>

<li>（やや難）このシリーズの道具が効く範囲を、三段の手続きの言葉で述べよ。
<details><summary>答えを見る</summary><div class="ans"><strong>Step 2 の行にぴったり一致します。</strong> Step 1（ミルン）ならもともと平坦で質量すら動かす必要がなく、Step 3（シュヴァルツシルト）なら共形変換で平坦にできません。<em>すべての FLRW が Step 2 にいるからこそ、第4回の「消せるものを全部消したら質量ひとつ」ができました</em> ── 第13回・第16回で測った道具の限界の、幾何学的な言い換えです。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　\(k\) を見れば、決着がつく</h2>
<p>ミルン宇宙と \(R_h=ct\) はどちらも \(a\propto t\) で、どちらも「減速も加速もしない」と言われます。違うのは \(k\) と中身だけ ── <strong>そしてスカラー曲率を計算すると、決着がつきます</strong>。\(a=t\) なら \(R=6(1+k)/t^2\) で、<em>\(k=-1\) でちょうどゼロ</em>。しかもリーマンテンソル全体が恒等的にゼロで、<strong>ミルンは座標を取り替えたミンコフスキー時空そのもの</strong>でした。\(R_h=ct\) は \(R=3.5\times10^{-52}\ \mathrm{m^{-2}}\)（曲率半径 1.73 Gpc）でゼロではありません。</p>
<p>ここから、一般に使える<strong>三段の判定手続き</strong>が作れます ── Step 1：リーマン \(=0\) なら座標変換で済み、物理の中身はゼロ。Step 2：ワイル \(=0\) なら共形変換が要り、質量が動く。Step 3：ワイル \(\ne0\) ならどちらでも消せない。<strong>すべての FLRW は Step 2 に入ります</strong> ── <em>このシリーズが第1回からずっといた場所が、この一行で特定されました。</em></p>
<p>光度距離を比べると、意外なことが起きます。\(z=1\) で <strong>ミルンのほうが \(\Lambda\)CDM に近い</strong>（ずれ 0.042 等 対 \(R_h=ct\) の 0.213 等）── <em>中身が空っぽの時空が、より良くハッブル図に合う</em>。それでもミルンは CMB・元素合成・構造形成・\(\Omega_m\) の測定（45σ 以上）で完全に排除されます。<strong>幾何が良くても、中身が無ければ物理になりません</strong> ── 第25回の \(L(\text{残差})\) はハッブル図だけで決まらない、第29回の「問いは一つではない」と、同じ構造です。</p>
<p>そして種明かし ── <strong>見分け方は \(k\) を見ること</strong>。\(k=-1\)（＋空）なら座標変換で済んで物理の中身はゼロ、\(k=0\)（＋物質）なら共形変換が要って質量が動く。<em>第3回で「\(c\cdot t=\)一定 は座標変換ではなく共形変換」と書いたことの、いちばん具体的な意味がこれです。</em></p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第34回</span>
次は<strong>共形重力（マンハイム）</strong>です。ここまで扱ってきた理論はどれも、共形変換を<em>後付けの書き換え</em>として使っていました。マンハイムは違います ── <strong>共形対称性そのものを、重力の基本原理に据える</strong>。作用をアインシュタイン＝ヒルベルトではなくワイルテンソルの二乗 \(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\) にすると、理論全体が最初から共形不変になります。<em>すると宇宙定数問題が構造的に消え、暗黒物質なしで回転曲線が出る</em> ── ただし代償があります。<strong>第 V 部で扱う予定だったゴーストが、ここで先に顔を出します。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sz=document.getElementById('sz'), vz=document.getElementById('vz'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=34, Y1=310;
  var xmin=0.05, xmax=2.0, ymin=-0.30, ymax=0.25;
  var SIG=0.15;
  var Om=0.315, Or=9.2e-5, OL=0.685;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function dlR(z){ return (1+z)*Math.log(1+z); }
  function dlM(z){ return z*(1+z/2); }
  function dlL(z){
    var n=600, s=0, dz=z/n;
    for(var i=0;i<=n;i++){
      var zz=i*dz;
      var E=Math.sqrt(Or*Math.pow(1+zz,4)+Om*Math.pow(1+zz,3)+OL);
      var w=(i===0||i===n)?0.5:1;
      s+=w/E;
    }
    return (1+z)*s*dz;
  }
  function dmu(f,z){ return 5*Math.log(f(z)/dlL(z))/Math.LN10; }

  function draw(){
    var z=parseInt(sz.value,10)/100;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    // 超新星 1 本のばらつき帯
    g.fillStyle='#eef0f2';
    g.fillRect(X0, py(SIG), X1-X0, py(-SIG)-py(SIG));
    g.fillStyle='#a6adb4'; g.textAlign='left';
    g.fillText('超新星 1 本の内在的ばらつき ±0.15 等', X0+10, py(SIG)-7);

    g.textAlign='right';
    for(var e=-0.3;e<=0.25;e+=0.1){
      var y=py(e);
      g.strokeStyle=(Math.abs(e)<1e-9?'#ccd2d8':'#f3f5f7'); g.lineWidth=(Math.abs(e)<1e-9?1.6:1);
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#96a0a8'; g.fillText(e.toFixed(1), X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0.5;q<=2.0;q+=0.5){
      var x=px(q);
      g.strokeStyle='#f8fafb'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#96a0a8'; g.fillText('z = '+q.toFixed(1), x, Y1+16);
    }
    g.strokeStyle='#c8d0d6'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    function curve(f,col){
      g.strokeStyle=col; g.lineWidth=3.2; g.beginPath();
      for(var i=0;i<=160;i++){
        var zz=xmin+(xmax-xmin)*i/160;
        var y=dmu(f,zz);
        if(i===0) g.moveTo(px(zz),py(Math.min(Math.max(y,ymin),ymax)));
        else g.lineTo(px(zz),py(Math.min(Math.max(y,ymin),ymax)));
      }
      g.stroke();
    }
    curve(dlM,'#2a3a4a');
    curve(dlR,'#9a6a2a');

    g.textAlign='left';
    g.fillStyle='#2a3a4a'; g.fillText('ミルン', px(1.75), py(dmu(dlM,1.75))-10);
    g.fillStyle='#9a6a2a'; g.fillText('R_h=ct', px(1.75), py(dmu(dlR,1.75))+18);

    // カーソル
    g.strokeStyle='#7a848c'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(z),Y0); g.lineTo(px(z),Y1); g.stroke();
    g.setLineDash([]);
    var ym=dmu(dlM,z), yr=dmu(dlR,z);
    [[ym,'#2a3a4a'],[yr,'#9a6a2a']].forEach(function(q){
      g.fillStyle=q[1];
      g.beginPath(); g.arc(px(z),py(Math.min(Math.max(q[0],ymin),ymax)),5,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=1.6;
      g.beginPath(); g.arc(px(z),py(Math.min(Math.max(q[0],ymin),ymax)),5,0,6.2832); g.stroke();
    });

    g.fillStyle='#7d868e'; g.textAlign='center';
    g.fillText('赤方偏移  z', (X0+X1)/2, Y1+38);
    g.save(); g.translate(19,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('ΛCDM からのずれ Δμ [等]', 0,0); g.restore();

    function need(d){ return d===0?Infinity:Math.pow(5*SIG/Math.abs(d),2); }
    vz.textContent='z = '+z.toFixed(2);
    ro.textContent='z = '+z.toFixed(2)+
      '　ミルン Δμ = '+ym.toFixed(3)+' 等（5σ に '+Math.ceil(need(ym))+' 本）'+
      '　／　R_h=ct Δμ = '+yr.toFixed(3)+' 等（5σ に '+Math.ceil(need(yr))+' 本）'+
      (Math.abs(ym)<Math.abs(yr) ? '　★ ミルンのほうが ΛCDM に近い' : '');
  }
  sz.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-33-milne.html', acc='#2a3a4a', ops='#9a6a2a',
      title='ミルン宇宙と R_h=ct ── わかる c·t=一定 第33回',
      ep='第 33 回 ／ 第 IV 部・いちばん紛らわしい二つを並べる',
      eyebrow='見分け方は一つ ── \\(k\\) を見ること',
      h1='ミルン宇宙と<br>\\(R_h=ct\\)',
      sub='どちらも \\(a\\propto t\\)。ところがミルンは座標変換で平坦時空に戻せ、\\(R_h=ct\\) は戻せません。<br><em>座標変換で済むのか、共形変換が要るのか ── 見分ける手続きを作ります。</em>',
      byline_l='必要な道具：FLRW のスカラー曲率、割り算',
      byline_r='\\(R=6(1+k)/t^2\\) ── \\(k=-1\\) でゼロ',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第33回、物理好きの高校生・大学生向け読み物です。ミルン宇宙（Milne 1935）が空の開いた FLRW（\\(\\rho=0\\)、\\(k=-1\\)、\\(a\\propto t\\)）であり、座標変換 \\(T=t\\cosh\\chi,\\ R=ct\\sinh\\chi\\) によってミンコフスキー時空の一部分になることは標準的な結果です ── <em>「一部分」であることは重要で、ミルン座標はミンコフスキー時空全体を覆いません</em>。FLRW のスカラー曲率 \\(R=6[\\ddot a/a+(\\dot a/a)^2+k/a^2]\\)、および FLRW が共形平坦（ワイルテンソルがゼロ）であることも標準的です。本稿の \\(R=6(1+k)/t^2\\)、\\(R_h=ct\\) の今日の値 \\(3.52\\times10^{-52}\\ \\mathrm{m^{-2}}\\)（曲率半径 1.73 Gpc）、および光度距離の比較表は本稿での計算です（kenshou/calc37.py）。<strong>「すべての FLRW はワイル \\(=0\\)」は等方一様な背景時空についての言明であり、ゆらぎを入れれば \\(C\\ne0\\) になります</strong> ── 実際の宇宙は完全な FLRW ではなく、だから第6回の使用率は \\(0\\) ではありません。\\(\\Lambda\\)CDM の値は \\(\\Omega_m=0.315\\)、\\(\\Omega_r=9.2\\times10^{-5}\\) による本稿の数値積分、ミルンの \\(H_0d_L/c=z(1+z/2)\\) と \\(R_h=ct\\) の \\((1+z)\\ln(1+z)\\) は閉じた式です。<strong>実際の超新星解析では絶対等級（定数項）を自由にするため、本稿の \\(\\Delta\\mu\\) をそのまま有意性に直すことはできません</strong> ── 図の「必要な本数」は定数項を固定した場合の目安です。「ミルンのほうが \\(\\Lambda\\)CDM に近い」は \\(z\\simeq1\\) 付近の話で、\\(z=2\\) では逆転します。\\(\\Omega_m=0.315\\pm0.007\\) は Planck による値です。\\(R_h=ct\\) の判定は第3回で扱っており、本稿はその再検討ではなく<em>ミルンとの構造的な違い</em>のみを扱います。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルで、学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで赤方偏移を動かし、5σ の区別に必要な超新星の本数が読めます。「答えを見る」で解答が開きます。')
