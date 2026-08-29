# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">物理法則は、世界を短く書き直す装置です。ケプラーの三法則は惑星の位置表を数式に畳み、\(\Lambda\)CDM は 6 個の数で 600 万個の多重極を出します。<strong>では、圧縮率で理論を並べれば「良い理論」の順位が決まるのか。</strong> 今回はそれを本気で計算し、<em>途中で崩れるところまで見ます</em>。</p>

<h2><span class="n">01</span>まず、法則そのものの長さを測る</h2>

<p>式を LaTeX で書き下し、1 文字 = \(\log_2 95=6.57\) ビット（印字可能 ASCII 95 種）で数えます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>法則</th><th class="mid">文字数</th><th class="mid">ビット</th></tr></thead>
<tbody>
<tr class="hi"><th>c·t=一定（膨張則） \(a\propto t\)</th><td class="mid"><strong>10</strong></td><td class="mid"><strong>66</strong></td></tr>
<tr><th>ニュートン重力</th><td class="mid">13</td><td class="mid">85</td></tr>
<tr><th>シュレディンガー方程式</th><td class="mid">31</td><td class="mid">204</td></tr>
<tr><th>ディラック方程式</th><td class="mid">33</td><td class="mid">217</td></tr>
<tr><th>フリードマン方程式</th><td class="mid">63</td><td class="mid">414</td></tr>
<tr><th>マクスウェル方程式（テンソル形）</th><td class="mid">66</td><td class="mid">434</td></tr>
<tr><th>アインシュタイン方程式</th><td class="mid">78</td><td class="mid">512</td></tr>
<tr><th>標準模型ラグランジアン（展開）</th><td class="mid">約 5000</td><td class="mid">約 33000</td></tr>
</tbody>
</table>
</div>

<p><strong>最短は \(a\propto t\) の 66 ビット</strong>。宇宙の膨張の歴史全体が、ツイートの 1/40 に収まります。</p>

<h2><span class="n">02</span>次に、説明する数の個数を測る</h2>

<div class="calc">
<span class="tag">CMB を数える</span>
<p class="lbl">\(l=2\) から \(2500\) までの球面調和モード数</p>
$$\sum_{l=2}^{2500}(2l+1)=6{,}254{,}997\quad(\text{TT のみ})\qquad\times3=1.88\times10^7\quad(\text{TT+TE+EE})$$
<p class="lbl">\(\Lambda\)CDM のパラメータは 6 個なので</p>
$$\text{圧縮率}=\frac{6{,}254{,}997}{6}=1.0\times10^6\ \text{倍}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>理論</th><th class="mid">パラメータ</th><th class="mid">説明する数</th><th class="mid">圧縮率</th></tr></thead>
<tbody>
<tr><th>リュードベリ公式</th><td class="mid">1（\(R_\infty\)）</td><td class="mid">\(n\le100\) で 4,950 本</td><td class="mid">4,950 倍</td></tr>
<tr><th>\(\Lambda\)CDM</th><td class="mid">6</td><td class="mid">\(6.3\times10^6\) モード</td><td class="mid">\(1.0\times10^6\) 倍</td></tr>
<tr><th>標準模型</th><td class="mid">19</td><td class="mid">全散乱断面積</td><td class="mid">（数え方次第）</td></tr>
<tr class="hi"><th>一般相対論</th><td class="mid"><strong>0</strong></td><td class="mid">全ての時空</td><td class="mid"><strong>形式的に無限大</strong></td></tr>
</tbody>
</table>
</div>

<p>ここまでなら気持ちのいい話です。<em>パラメータが少ないほど良い理論</em>。ところが ──</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>崩れるところ ── 同じ計算で、勝敗がひっくり返る</h2>

<p>MDL（最小記述長）でまじめに総合します。総記述長は三つの和です。</p>

<div class="calc">
<span class="tag">MDL</span>
$$L=\underbrace{L(\text{法則})}_{\text{式の長さ}}+\underbrace{L(\text{パラメータ})}_{\tfrac12\log_2N\ \text{bit/個}}+\underbrace{L(\text{残差})}_{\Delta\chi^2/(2\ln2)}$$
<p class="lbl">第20回の値を再利用：\(N=1701\) で \(\tfrac12\log_2N=5.37\) bit/個、\(\Delta\chi^2=213\) で残差 153.6 bit</p>
</div>

<p>問題は、<strong>\(a\propto t\) を「フリードマン式に足す拘束」と数えるか、「フリードマン式を丸ごと置き換えるもの」と数えるか</strong>で、L(法則) が変わることです。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>書き方 A：足す拘束</th><th class="mid">L(法則)</th><th class="mid">L(param)</th><th class="mid">L(残差)</th><th class="mid">合計</th></tr></thead>
<tbody>
<tr><th>\(\Lambda\)CDM</th><td class="mid">414</td><td class="mid">32.2</td><td class="mid">0.0</td><td class="mid"><strong>446</strong></td></tr>
<tr><th>c·t=一定</th><td class="mid">414+66</td><td class="mid">26.8</td><td class="mid">153.6</td><td class="mid">660</td></tr>
</tbody>
</table>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>書き方 B：置き換える</th><th class="mid">L(法則)</th><th class="mid">L(param)</th><th class="mid">L(残差)</th><th class="mid">合計</th></tr></thead>
<tbody>
<tr><th>\(\Lambda\)CDM</th><td class="mid">414</td><td class="mid">32.2</td><td class="mid">0.0</td><td class="mid">446</td></tr>
<tr class="hi"><th>c·t=一定</th><td class="mid">66</td><td class="mid">26.8</td><td class="mid">153.6</td><td class="mid"><strong>246</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>同じモデル・同じデータで、結論が 214 ビット負け ⇄ 200 ビット勝ちにひっくり返りました。</strong><br>
動いたのは L(法則) の 414 ビットだけ。<em>そしてこの 414 ビットは「どの言語で式を書くか」で決まります。</em></p>
</div>

<p>これはコルモゴロフ複雑度の<strong>不変性定理</strong>そのものです ── 記述長は、記述言語に依る定数を除いてしか決まらない。教科書ではその定数は「大きな有限値だが、データを増やせば効かなくなる」と扱われます。ところが<em>理論を比べるという用途では、その定数が勝敗をひっくり返せる大きさを持っていました</em>。</p>

<div class="fig">
<p class="cap">図：MDL の三本の柱。ツマミで L(法則) を動かすと合計が入れ替わりますが、<strong>L(param) と L(残差) だけの比較（右の細い棒）は動きません</strong></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>c·t=一定 の L(法則) をどう数えるか [bit]<input id="sl" type="range" min="0" max="600" value="480" step="5"></label>
  <span class="val" id="vl">480</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3a2f5a"></i>L(法則)：言語依存</span>
  <span><i class="swatch" style="background:#b06a2a"></i>L(param)：不変</span>
  <span><i class="swatch" style="background:#8a7fa8"></i>L(残差)：データだけで決まる</span>
</div>
</div>

<h2><span class="n">04</span>では、圧縮率のどこが信用できるのか</h2>

<div class="seven">
<div class="row"><div class="mk">✕</div><div class="txt"><strong>L(法則) ── 使えない</strong><span>記述言語に依存する。今回の例で 414 ビット動いた。「式が短いから良い理論」は、情報理論の言葉では支えられない</span></div></div>
<div class="row hi"><div class="mk">○</div><div class="txt"><strong>L(パラメータ) ── 使える</strong><span>パラメータの個数は再パラメトライズで変わらない。5.37 bit/個</span></div></div>
<div class="row hi"><div class="mk">○</div><div class="txt"><strong>L(残差) ── 使える</strong><span>尤度はデータだけで決まる。153.6 bit</span></div></div>
</div>

<div class="calc">
<span class="tag">信用できる部分だけで比べる</span>
$$\Delta L=\underbrace{+5.37}_{\text{パラメータ 1 個ぶんの得}}-\underbrace{153.6}_{\text{当てはまりの損}}=-148.3\ \text{bit}$$
$$\text{オッズ比}\ 2^{148}=4.3\times10^{44}$$
</div>

<p>第3回の判決は、<strong>この二つの項にしか依存していません</strong>。式の短さという曖昧な部分を全部捨てても、結論は変わりません ── これは判決の蒸し返しではなく、<em>判決がどれだけ狭い土台の上に立っているかの確認</em>です。</p>

<h2><span class="n">05</span>種明かし ── 圧縮率は「良さ」ではなく「掛け金」</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>パラメータ数 \(k\)</th><th class="mid">持っている逃げ場</th></tr></thead>
<tbody>
<tr class="hi"><th>\(k=0\)</th><td class="mid"><strong>合わせにいくことが原理的にできない</strong></td></tr>
<tr><th>\(k=1\)</th><td class="mid">1 方向に逃げられる</td></tr>
<tr><th>\(k=6\)（\(\Lambda\)CDM）</th><td class="mid">6 方向</td></tr>
<tr><th>\(k=25\)（\(\Lambda\)CDM＋標準模型）</th><td class="mid">25 方向</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">05節の結論</p>
<p style="margin:6px 0 0">圧縮率が高い ⟺ パラメータが少ない ⟺ <strong>逃げ場がない</strong> ⟺ 反証されやすい。<br>
MDL の圧縮率と、ポパーの反証可能性は<em>同じ軸の裏表</em>でした。</p>
</div>

<p>だから \(a\propto t\) が「最短・パラメータ 0 個」であることは、<strong>良い知らせではなく、大きな賭けだったという知らせ</strong>です。掛け金が大きいから、外れたときに 148 ビットも取られました。<em>圧縮率が高すぎる理論に共通の弱点とは、これのことです</em> ── 吸収する余地がない。</p>

<div class="aside">
<span class="tag">それでも短さには使い道がある</span>
判定には使えない、と言いました。<strong>でも書き換えには使えます。</strong> このシリーズがずっとやってきたのは判定ではなく圧縮です ── \(H_0d_L/c=(1+z)\ln(1+z)\)（第9回、パラメータ 0 個）、\(\Omega/N=p\ln2/2\pi^2\)（第1回）、\(C\cdot t=N\)（第24回）。<em>これらは「短いから正しい」のではなく、「短いから見える構造がある」という主張です。</em> 見えた構造が本物かどうかを決めるのは、いつも L(残差) のほうでした。
</div>

<h2><span class="n">06</span>宇宙自身の圧縮率</h2>

<div class="calc">
<span class="tag">法則が圧縮していないもの</span>
<p class="lbl">実際に使われている情報（第6回・第23回）</p>
$$k=S/\ln2=4.47\times10^{104}\ \text{bit}$$
<p class="lbl">物理法則が使うパラメータ（\(\Lambda\)CDM＋標準模型）</p>
$$25\ \text{個}\approx134\ \text{bit}$$
</div>

<p>134 ビットの法則で \(4.5\times10^{104}\) ビットの世界を説明できているように見えますが、<strong>法則は初期条件を圧縮していません</strong>。この \(10^{104}\) ビットの内訳を持っているのは、法則ではなく<em>履歴</em>のほうです。第20回で「宇宙は 140 手のプログラム」と書いたのは、まさにその履歴のことでした。</p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 「1 文字 = 6.57 ビット」は、恣意的な数え方です。</strong> 実際、それがこの回の主題です。LaTeX ではなく別の記法を選べば、どの式も短くも長くもなります ── だから 01節の表は<em>順位を主張するものではなく、03節で崩すための材料</em>です。</p>
<p style="margin:0 0 10px"><strong>② 圧縮率（説明する数 ÷ パラメータ数）も、分子の数え方に依存します。</strong> \(\Lambda\)CDM の \(6.3\times10^6\) は「TT の全 \(a_{lm}\) モード」の数で、実際に独立な情報量はもっと少なく（Planck の binned \(C_l\) は 1701 点）、逆に TT+TE+EE や他の観測を足せば増えます。標準模型の欄を空けたのは同じ理由で、<em>誠実に数える方法が無かった</em>からです。</p>
<p style="margin:0 0 10px"><strong>③ \(\Delta\chi^2=213\) は第20回で使った値で、比較する観測セットに依存します。</strong> 数値そのものより、「残差の項がパラメータの項を 2 桁上回る」という構造のほうが頑健です。</p>
<p style="margin:0 0 10px"><strong>④ MDL の残差項に \(\Delta\chi^2/(2\ln2)\) を使うのはガウス近似です。</strong> 厳密には尤度比そのものを取るべきで、非ガウスな尤度では係数が変わります。</p>
<p style="margin:0 0 10px"><strong>⑤ 「一般相対論はパラメータ 0 個」は、\(\Lambda\) を含めない場合です。</strong> \(\Lambda\) を理論の一部と数えれば 1 個、\(G\) と \(c\) は単位換算なので数えません（第2回の規約）。</p>
<p style="margin:0"><strong>⑥ 第3回の判定は動かしていません。</strong> 04節は判決の再判定ではなく、<em>判決が L(法則) という曖昧な項に一切依存していないことの確認</em>です。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>\(\Lambda\)CDM の圧縮率を、TT+TE+EE で数えよ。
<details><summary>答えを見る</summary><div class="ans">\(3\times6{,}254{,}997/6=3.1\times10^6\) 倍。ただし分子は独立な情報量ではなくモード数なので、<strong>これは上限側の数え方</strong>です。</div></details></li>

<li>書き方 A と B で結論がひっくり返る理由を一言で述べよ。
<details><summary>答えを見る</summary><div class="ans">L(法則) が記述言語に依存するから。A と B の差はフリードマン方程式の 414 ビットで、<strong>それが 148 ビットの差を打ち消して余る</strong>。コルモゴロフ複雑度の不変性定理が言う「言語依存の定数」が、ここでは効いてしまっています。</div></details></li>

<li>パラメータ 1 個を足して \(\Delta\chi^2\) をいくつ下げれば元が取れるか（\(N=1701\)）。
<details><summary>答えを見る</summary><div class="ans">値段は \(\tfrac12\log_2 1701=5.37\) bit。\(\Delta\chi^2/(2\ln2)>5.37\) すなわち <strong>\(\Delta\chi^2>7.44\)</strong> 下がれば元が取れます。素朴な「\(\Delta\chi^2>1\)」よりずっと厳しい基準です。</div></details></li>

<li>「圧縮率が高い理論ほど良い」は正しいか。
<details><summary>答えを見る</summary><div class="ans">正しくありません。圧縮率が高い ⟺ パラメータが少ない ⟺ <strong>逃げ場がない</strong> ⟺ 反証されやすい。圧縮率は<em>良さ</em>ではなく<em>掛け金の大きさ</em>を測っています。\(a\propto t\) は最短・パラメータ 0 個で、だからこそ大きく外れました。</div></details></li>

<li>（やや難）法則 134 ビットで \(4.5\times10^{104}\) ビットの世界を説明できるのはなぜか。
<details><summary>答えを見る</summary><div class="ans"><strong>説明できていません。</strong> 法則は「時間発展の規則」を圧縮しますが、初期条件は圧縮しません。\(10^{104}\) ビットの内訳を持っているのは履歴のほうです ── 第20回の「140 手のプログラム」がそれで、法則はその実行規則にすぎません。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　圧縮率は、良さではなく掛け金</h2>
<p>法則の長さを LaTeX の文字数で数えると、最短は \(a\propto t\) の <strong>66 ビット</strong>、アインシュタイン方程式が 512 ビット、標準模型が約 33000 ビットでした。説明する数の個数で割った圧縮率は、\(\Lambda\)CDM で \(10^6\) 倍、一般相対論では形式的に無限大です。</p>
<p>ところが MDL でまじめに総合すると崩れました ── \(a\propto t\) を「フリードマン式に足す拘束」と数えるか「置き換えるもの」と数えるかで、<strong>同じモデル・同じデータの結論が 214 ビット負け ⇄ 200 ビット勝ちにひっくり返ります</strong>。動いたのは L(法則) の 414 ビットだけで、これは記述言語に依存する量です。コルモゴロフ複雑度の不変性定理が言う「言語依存の定数」が、理論の比較という用途では<em>勝敗を左右する大きさ</em>を持っていました。</p>
<p>信用できるのは残りの二つ ── パラメータの個数（再パラメトライズ不変、5.37 bit/個）と残差（データだけで決まる、153.6 bit）。この二つだけで比べると \(-148\) ビット、オッズ比 \(4.3\times10^{44}\)。<strong>第3回の判決は、この狭い土台の上にだけ立っています。</strong></p>
<p>そして種明かし ── 圧縮率が高い ⟺ パラメータが少ない ⟺ 逃げ場がない ⟺ 反証されやすい。<em>MDL の圧縮率と、ポパーの反証可能性は同じ軸の裏表でした。</em> \(a\propto t\) が最短でパラメータ 0 個であることは、良い知らせではなく<strong>大きな賭けだったという知らせ</strong>です。圧縮率が高すぎる理論の弱点とは、吸収する余地がないこと ── ただしそれは<em>判定</em>の話で、<em>書き換え</em>としての短さの価値は別に残ります。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第26回（第 III 部・完）</span>
第 III 部の最後は<strong>「情報として測る」の総決算</strong>です。第17回から今回まで、地平線・パラメータ・驚き・偶然・演算・符号・帯域・記述長と、<em>八つの物差しで宇宙を測ってきました</em>。それを一枚の表に並べると、<strong>同じ数が何度も出てきます</strong> ── \(1.5\times10^{-18}\) が三度、\(140\) が四度、\(0.035\) が二度。<em>物差しが違うのに同じ数が出るとき、それは発見なのか、それとも最初から同じものを測っていたのか。</em> 第19回の「驚きをビットで測る」手続きを、シリーズ自身に適用します。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sl=document.getElementById('sl'), vl=document.getElementById('vl'), ro=document.getElementById('ro');
  var LF=414.0, PA=32.2, PB=26.8, RES=153.6;
  var X0=70, X1=700, Y0=34, Y1=300;
  function draw(){
    var Lct=parseFloat(sl.value);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    var lcdm=[LF,PA,0], ct=[Lct,PB,RES];
    var tl=LF+PA, tc=Lct+PB+RES;
    var max=Math.max(tl,tc,700);
    function bar(x,w,parts,label,total,sub){
      var y=Y1;
      var cols=['#3a2f5a','#b06a2a','#8a7fa8'];
      for(var i=0;i<3;i++){
        var h=parts[i]/max*(Y1-Y0);
        g.fillStyle=cols[i];
        g.fillRect(x,y-h,w,h);
        if(h>16){
          g.fillStyle='#fff'; g.textAlign='center';
          g.fillText(parts[i].toFixed(0), x+w/2, y-h/2+4);
        }
        y-=h;
      }
      g.strokeStyle='#cfc7dd'; g.lineWidth=1; g.strokeRect(x,y,w,Y1-y);
      g.fillStyle='#3a2f5a'; g.textAlign='center';
      g.font='bold 13px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillText(total.toFixed(0)+' bit', x+w/2, y-9);
      g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillStyle='#5a4f78';
      g.fillText(label, x+w/2, Y1+20);
      if(sub){ g.fillStyle='#9088a8'; g.fillText(sub, x+w/2, Y1+37); }
    }
    bar(120,110,lcdm,'ΛCDM',tl,'（基準）');
    bar(275,110,ct,'c·t=一定',tc,'L(法則)を動かす');
    // 信用できる部分だけ
    g.strokeStyle='#e4dff0'; g.lineWidth=1; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(440,Y0-14); g.lineTo(440,Y1+44); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#8a7fa8'; g.textAlign='left'; g.font='12px sans-serif';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('L(法則) を捨てた比較 ── 動かない', 462, Y0-2);
    bar(500,64,[0,PA,0],'ΛCDM',PA,'');
    bar(600,64,[0,PB,RES],'c·t',PB+RES,'');
    g.strokeStyle='#c3b8d8'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();
    vl.textContent=Lct.toFixed(0)+' bit';
    var w = tc<tl ? 'c·t=一定 の勝ち' : 'ΛCDM の勝ち';
    ro.textContent='L(法則)='+Lct.toFixed(0)+'　→　合計 '+tc.toFixed(0)+' vs '+tl.toFixed(0)+
      '　'+w+'（差 '+Math.abs(tc-tl).toFixed(0)+' bit）'+
      '　／　L(法則)を捨てると差は常に '+(PB+RES-PA).toFixed(1)+' bit で ΛCDM の勝ち';
  }
  sl.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-25-mdl.html', acc='#3a2f5a', ops='#b06a2a',
      title='物理法則は圧縮アルゴリズムか ── わかる c·t=一定 第25回',
      ep='第 25 回 ／ 記述長で理論を並べると、どこで崩れるか',
      eyebrow='圧縮率は「良さ」ではなく「掛け金」でした',
      h1='物理法則は<br>圧縮アルゴリズムか',
      sub='\\(a\\propto t\\) は 66 ビット、アインシュタイン方程式は 512 ビット。<br><em>では短いほうが良い理論か ── まじめに計算すると、途中で崩れます。</em>',
      byline_l='必要な道具：MDL、\\(\\tfrac12\\log_2N\\)、掛け算',
      byline_r='圧縮率 ＝ 反証可能性',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第25回、物理好きの高校生・大学生向け読み物です。最小記述長原理（MDL, Rissanen）、コルモゴロフ複雑度の不変性定理、BIC の \\(\\tfrac12\\log_2N\\) はいずれも標準的です。<strong>「1 文字 = \\(\\log_2 95\\) ビット」という数え方は本稿の恣意的な規約であり、それ自体がこの回の主題です</strong> ── 01節の表は順位を主張するものではなく、03節で崩すための材料です。書き方 A / B の比較（214 bit 負け ⇄ 200 bit 勝ち）、および L(法則) を捨てた比較（\\(-148.3\\) bit）は本稿での計算です（kenshou/calc29.py）。圧縮率の分子（説明する数の個数）は数え方に強く依存し、\\(\\Lambda\\)CDM の \\(6.3\\times10^6\\) は TT の全 \\(a_{lm}\\) モード数（独立な情報量は Planck の binned \\(C_l\\) 1701 点程度）です。標準模型の欄を空けたのは、誠実に数える方法が無かったためです。\\(\\Delta\\chi^2=213\\) は第20回で用いた値で比較する観測セットに依存し、残差項の \\(\\Delta\\chi^2/(2\\ln2)\\) はガウス近似です。「一般相対論はパラメータ 0 個」は \\(\\Lambda\\) を含めない場合の数え方です。線形膨張（\\(c\\cdot t=\\)一定）は検証途上の少数派モデルで、その判定は第3回で扱いました ── 本稿はその判定を再検討するものではなく、判定が L(法則) に依存していないことの確認です。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで L(法則) を動かすと、勝敗がひっくり返る様子が見えます。「答えを見る」で解答が開きます。')
