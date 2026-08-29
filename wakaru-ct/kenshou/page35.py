# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第7回で「\(G\) は次元付きだから帳簿」と数え、第34回で「\(\alpha_g\) は無次元だから物理」と数えました。<strong>漸近安全性は、その両方をつなぐ立場です</strong> ── \(G\) をスケールと組んで<em>無次元化して走らせる</em>。すると紫外で固定点に落ち着き、重力が量子論として成立する。そして第14回の<strong>異常次元</strong>が、いよいよ重力そのものに現れます ── <em>しかも、想像より遥かに大きい値で。</em></p>

<h2><span class="n">01</span>\(G\) を、無次元にする</h2>

<div class="calc">
<span class="tag">このシリーズの手続きを、重力の結合に当てる</span>
<p class="lbl">4 次元では \([G]=\)長さ\(^2\)（\(\hbar=c=1\) で \(G=\ell_P^2\)）── 次元付き＝帳簿</p>
$$g(k)=G\,k^2=(\ell_P k)^2\qquad\text{← これが物理の側（ウェイト 0）}$$
</div>

<p>第3回で「無次元だけが物理」と決め、第16回で地図を作りました。<strong>漸近安全性は、その判定手続きを重力の結合そのものに当てた立場です</strong> ── \(G\) 単独では意味がないので、スケール \(k\) と組んで無次元にする。</p>

<h2><span class="n">02</span>実際に走らせてみる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>スケール</th><th class="mid">\(k\) [1/m]</th><th class="mid">\(g=(\ell_Pk)^2\)</th></tr></thead>
<tbody>
<tr><th>実験室（\(1\ \mathrm{m^{-1}}\)）</th><td class="mid">\(1.0\)</td><td class="mid">\(2.6\times10^{-70}\)</td></tr>
<tr><th>陽子（1 GeV）</th><td class="mid">\(5.1\times10^{15}\)</td><td class="mid">\(6.7\times10^{-39}\)</td></tr>
<tr><th>LHC（10 TeV）</th><td class="mid">\(5.1\times10^{19}\)</td><td class="mid">\(6.7\times10^{-31}\)</td></tr>
<tr><th>大統一（\(10^{16}\) GeV）</th><td class="mid">\(5.1\times10^{31}\)</td><td class="mid">\(6.7\times10^{-7}\)</td></tr>
<tr class="hi"><th>プランク（\(1.22\times10^{19}\) GeV）</th><td class="mid">\(6.2\times10^{34}\)</td><td class="mid"><strong>\(1.0\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">傾きを測る</span>
$$\frac{38.2\ \text{桁}\ (g)}{19.1\ \text{桁}\ (E)}=2.00$$
</div>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0">傾きは<strong>ちょうど 2</strong> ── \(g=Gk^2\) の古典次元そのものです。<br>
── <em>プランク以下では、ウェイト表がぴったり正しい（異常次元ゼロ）。</em></p>
</div>

<p>ついでに、有名な「重力は \(10^{-38}\) 倍弱い」という数字の正体もここにあります ── <em>陽子スケールで \(g=6.7\times10^{-39}\)</em>。弱いのではなく、<strong>見ているスケールが小さいだけ</strong>です。</p>

<h2><span class="n">03</span>紫外で、固定点に落ち着く</h2>

<div class="calc">
<span class="tag">漸近安全性の主張</span>
$$\beta_g=2g-b\,g^2\qquad\Longrightarrow\qquad g^*=\frac{2}{b}\ne0\quad(\text{非ガウス固定点})$$
<p class="lbl">ロイター系の代表値（<strong>切り捨て・スキーム依存</strong>）</p>
$$g^*\simeq0.71,\qquad \lambda^*\simeq0.19$$
</div>

<p>\(g\) がここで止まるので \(G(k)\propto1/k^2\) となり、<strong>重力は紫外で弱くなります</strong>。これが「漸近安全（asymptotically safe）」という名前の意味です ── 発散する代わりに、有限の値に落ち着く。</p>

<div class="fig">
<p class="cap">図：無次元化した重力の結合 \(g=Gk^2\) の走り。<strong>プランク以下は傾き 2 の直線（古典次元そのもの）、その上で固定点に平らになります</strong>。ツマミで \(g^*\) を変えると、折れ曲がる場所が動きます</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>固定点の値 \(g^*\)（切り捨てで変わる）<input id="sg" type="range" min="10" max="150" value="71" step="1"></label>
  <span class="val" id="vg">g* = 0.71</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a5a"></i>\(g=Gk^2\) の走り</span>
  <span><i class="swatch" style="background:#8a3a3a"></i>固定点 \(g^*\)</span>
  <span><i class="swatch" style="background:#c2cfcf"></i>プランクエネルギー</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>核心 ── 固定点では、ウェイト表が 100% 外れる</h2>

<p>ここが今回の要です。\(g=Gk^2\) が定数になるには、\(G\) の走りが \(k^{-2}\) でなければなりません。つまり ──</p>

<div class="calc">
<span class="tag">ニュートン結合の異常次元</span>
$$\eta_N=-2\qquad(\text{固定点で、ちょうど})$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>演算子</th><th class="mid">古典次元</th><th class="mid">異常次元</th><th class="mid">誤差の割合</th></tr></thead>
<tbody>
<tr><th>3 次元イジングのスピン演算子（第14回）</th><td class="mid">0.5</td><td class="mid">0.0181</td><td class="mid">3.6%</td></tr>
<tr class="hi"><th>重力の結合（固定点）</th><td class="mid">2.0</td><td class="mid"><strong>2.0</strong></td><td class="mid"><strong>100%</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0">第14回で「帳簿の数字に誤差棒が付く」と書きました。3 次元イジングでは <strong>3.6%</strong> のずれでした。<br>
重力の固定点では <strong>100%</strong> ── <em>古典次元が丸ごと打ち消されます。</em><br>
── <strong>誤差棒どころではありません。ウェイト表そのものが、そこでは意味を失う。</strong></p>
</div>

<p>第14回で「ウェイトは決まった数ではなく、理論が決め、実験が測る量だった」と結論しました。<em>重力の紫外では、その「理論が決める」が極限まで効きます</em> ── 次元解析の予想が、まるごと消える。</p>

<h2><span class="n">05</span>何を買うのか ── 予言の個数</h2>

<p>漸近安全性の売りは、<strong>紫外臨界面の次元＝自由パラメータの個数が有限</strong>であることです。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">内容</th></tr></thead>
<tbody>
<tr><th>relevant な方向</th><td class="mid"><strong>2〜3 個</strong>（切り捨ての取り方で変わる）</td></tr>
<tr><th>もし 3 個なら</th><td class="mid">紫外の物理が 3 個で決まる ── 第5回の値段で 16.1 ビット</td></tr>
<tr class="hi"><th>弱点</th><td class="mid"><strong>個数が切り捨て依存で定まらない</strong>こと自体</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">06</span>実際に当たった予言 ── ヒッグス質量</h2>

<div class="calc">
<span class="tag">2010 年の予言と、2012 年の発見</span>
$$\text{シャポシニコフ＝ヴェッテリヒ（2010）}:\quad m_H\simeq126\ \mathrm{GeV}$$
$$\text{実測}:\quad m_H=125.25\pm0.17\ \mathrm{GeV}\qquad(\text{ずれ }0.6\%)$$
</div>

<p><em>発見より前に出された予言です。</em> 第19回の手続きで驚きを測ります。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>事前範囲の取り方</th><th class="mid">驚き</th></tr></thead>
<tbody>
<tr><th>当時の LEP＋精密電弱が示唆した幅（90〜160 GeV）</th><td class="mid">4.5 bit</td></tr>
<tr><th>もっと広く 100〜300 GeV と取る場合</th><td class="mid">6.1 bit</td></tr>
</tbody>
</table>
</div>

<p><strong>4〜6 ビット</strong> ── 第19回の目盛りでは<em>偶然</em>の帯（第29回の MOND が 5.9、第34回の \(\gamma_0\) が 5.4）。ただし<strong>説明（固定点条件）がある</strong>ので、第27回のインフレーションと同じく<em>物理</em>へ移ります ── 当たっていれば。<em>この予言は物質セクターについての仮定に依存し、頑健性には議論があります。</em></p>

<h2><span class="n">07</span>種明かし ── 第34回と同じ入口</h2>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>共形重力（第34回）</strong><span>\(\alpha_g\) が<em>構成上</em>無次元 ── 最初から物理の列にいる</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>漸近安全性（今回）</strong><span>\(G\) をスケールと組んで<em>無次元化する</em> ── 走らせて固定点を探す</span></div></div>
<div class="row"><div class="mk">◆</div><div class="txt"><strong>同じ要求の、別の実装</strong><span>どちらも「物理は無次元の結合にある」から出発している</span></div></div>
</div>

<div class="keybox">
<p class="lbl">07節の結論</p>
<p style="margin:6px 0 0">第3回で作った判定手続き（<em>次元付きは帳簿、無次元が物理</em>）が、<br>
<strong>重力の量子化そのものの設計に効いています。</strong><br>
── 二つの理論が、同じ入口から入って、別々の場所で代償を払っている。</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>理論</th><th class="mid">無次元の結合</th><th class="mid">主な負債</th><th class="mid">未解決</th></tr></thead>
<tbody>
<tr><th>共形重力（第34回）</th><td class="mid">\(\alpha_g\)（構成上）</td><td class="mid">ゴースト</td><td class="mid">CMB 予言が未確立</td></tr>
<tr class="hi"><th>漸近安全性</th><td class="mid">\(g=Gk^2\)（走る）</td><td class="mid">切り捨て依存</td><td class="mid">予言の個数が定まらない</td></tr>
</tbody>
</table>
</div>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 固定点の値 \(g^*\simeq0.71\)、\(\lambda^*\simeq0.19\) は切り捨てとスキームに依存します。</strong> 汎関数繰り込み群の計算では作用の切り捨て方を選ぶ必要があり、<em>値は数割動きます</em>。固定点の<strong>存在</strong>は多くの切り捨てで確認されていますが、それが真の非摂動的な結果であることの厳密な証明はありません。</p>
<p style="margin:0 0 10px"><strong>② \(\eta_N=-2\) は「固定点で \(g\) が定数になる」ことの言い換えです。</strong> 定義上そうなる、という側面が強く ── <em>第19回の分類でいえば恒等式に近い</em>。ただし「そのような固定点が実在するか」は恒等式ではなく物理の主張です。04節が言っているのは、<strong>もし固定点があるなら、ウェイト表の誤差が最大になる</strong>ということです。</p>
<p style="margin:0 0 10px"><strong>③ 「relevant な方向が 2〜3 個」は切り捨て計算による見積もりです。</strong> 数が確定していないこと自体が、この理論の予言力に対する主要な批判の一つです。</p>
<p style="margin:0 0 10px"><strong>④ ヒッグス質量の予言（Shaposhnikov &amp; Wetterich 2010）は、物質セクターの仮定（特に「プランクスケールで量子効果が \(\lambda\) と \(\beta_\lambda\) を同時にゼロにする」という条件）に依存します。</strong> 予言の頑健性、およびトップクォーク質量の不定性の扱いには議論があります ── <em>本稿は当たったという事実と、その驚きの大きさを記録するに留めます</em>。</p>
<p style="margin:0"><strong>⑤ 漸近安全性は有力な候補の一つですが、確立した量子重力理論ではありません。</strong> 弦理論・ループ量子重力・因果的動的三角形分割など他の候補があり、どれも決着していません。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>\(G\) を無次元にする方法と、その理由を述べよ。
<details><summary>答えを見る</summary><div class="ans">\([G]=\)長さ\(^2\) なので、スケール \(k\)（逆長さ）と組んで \(g=Gk^2=(\ell_Pk)^2\) とすれば無次元。<strong>次元付きは帳簿、無次元が物理</strong>（第3回・第16回）なので、<em>物理はこの \(g\) の側にあります</em>。</div></details></li>

<li>陽子スケールでの \(g\) を求め、「重力は \(10^{-38}\) 倍弱い」の正体を説明せよ。
<details><summary>答えを見る</summary><div class="ans">1 GeV は \(k=5.07\times10^{15}\ \mathrm{m^{-1}}\) なので \(g=(\ell_Pk)^2=6.7\times10^{-39}\)。<strong>重力が本質的に弱いのではなく、見ているスケールが小さいだけ</strong>です ── プランクスケールでは \(g=1\) になります。</div></details></li>

<li>プランク以下で \(g\) の傾きが 2 になるのはなぜか。
<details><summary>答えを見る</summary><div class="ans">\(g=Gk^2\) で \(G\) が定数なら \(g\propto k^2\) だから。<strong>古典次元そのもの</strong>で、<em>異常次元がゼロ</em>ということ ── プランク以下ではウェイト表がぴったり正しい。</div></details></li>

<li>固定点での異常次元を求め、第14回と比べよ。
<details><summary>答えを見る</summary><div class="ans">\(g=Gk^2\) が定数になるには \(G\propto k^{-2}\)、つまり <strong>\(\eta_N=-2\) ちょうど</strong>。3 次元イジングは古典次元 0.5 に対し異常次元 0.018（<em>3.6%</em>）でしたが、重力は 2 に対し 2 ── <strong>100%</strong>。<em>古典次元が丸ごと打ち消されます。</em></div></details></li>

<li>（やや難）第34回の共形重力と、漸近安全性の関係を述べよ。
<details><summary>答えを見る</summary><div class="ans">どちらも<strong>「物理は無次元の結合にある」という同じ要求</strong>から出発しています ── 共形重力は \(\alpha_g\) が<em>構成上</em>無次元、漸近安全性は \(G\) を \(k\) と組んで<em>無次元化して走らせる</em>。<em>第3回の判定手続きが、重力の量子化そのものの設計に効いている</em>ということです。代償の場所は違います（ゴースト 対 切り捨て依存）。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　重力では、ウェイト表が丸ごと消える</h2>
<p>漸近安全性は、このシリーズの判定手続きを重力の結合そのものに当てた立場です ── \(G\) は次元付きなので単独では意味がなく、スケールと組んで <strong>\(g=Gk^2=(\ell_Pk)^2\)</strong> を作る。走らせてみると、実験室で \(2.6\times10^{-70}\)、陽子スケールで \(6.7\times10^{-39}\)、プランクで \(1.0\) ── <em>傾きはちょうど 2 で、古典次元そのもの</em>。「重力は \(10^{-38}\) 倍弱い」の正体も、これでした（<strong>弱いのではなく、見ているスケールが小さいだけ</strong>）。</p>
<p>紫外では固定点 \(g^*\simeq0.71\) に落ち着き、\(G(k)\propto1/k^2\) となって<strong>重力が紫外で弱くなります</strong>。そして核心 ── \(g\) が定数になるには \(G\) が \(k^{-2}\) で走らねばならず、ニュートン結合の異常次元は <strong>\(\eta_N=-2\) ちょうど</strong>。第14回で「帳簿の数字に誤差棒が付く」と書き、3 次元イジングで <strong>3.6%</strong> と測りましたが、重力の固定点では <strong>100%</strong> ── <em>古典次元が丸ごと打ち消されます。誤差棒どころではありません。</em></p>
<p>買うのは<strong>予言の個数</strong>です（relevant な方向 2〜3 個、第5回の値段で 16.1 ビット）── ただし<em>個数が切り捨て依存で定まらない</em>ことが弱点。実際に当たった予言もあります ── シャポシニコフ＝ヴェッテリヒ（2010）のヒッグス質量 126 GeV に対し、実測 125.25 GeV。第19回の手続きで <strong>4〜6 ビット</strong>の驚きで、説明があるので<em>物理</em>の側です（ただし物質セクターの仮定に依存）。</p>
<p>そして種明かし ── <strong>第34回の共形重力と、同じ入口から入っています</strong>。共形重力は \(\alpha_g\) が構成上無次元、漸近安全性は \(G\) を無次元化して走らせる。<em>第3回で作った「次元付きは帳簿、無次元が物理」という判定手続きが、重力の量子化そのものの設計に効いている</em> ── そして二つは、別々の場所で代償を払っています（ゴースト 対 切り捨て依存）。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第36回（第 IV 部・完）</span>
第 IV 部の九つの理論を、一枚の手術台に並べます ── インフレーション、VSL、MOND、定数の測定、CCC、コスモン、ミルン、共形重力、漸近安全性。<strong>すべてに同じ手術を当てて、分かれ目がどこにあったかを一覧にします。</strong> そして<em>この部で分かったいちばん大事なこと</em>を書きます ── <strong>良い理論は、第3回の手術を最初から済ませてある。</strong> 済ませていなかったのは一つだけでした。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sg=document.getElementById('sg'), vg=document.getElementById('vg'), ro=document.getElementById('ro');
  var X0=78, X1=700, Y0=34, Y1=310;
  var lP=1.616255e-35, hbarc=1.973269804e-16, Epl=1.220890e19;
  var xmin=-3, xmax=25;        // log10(E/GeV)
  var ymin=-46, ymax=2;        // log10 g

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function lgG(lE){                    // 古典の走り log10 g = 2 log10(lP k)
    var k=Math.pow(10,lE)/hbarc;
    return 2*Math.log(lP*k)/Math.LN10;
  }

  function draw(){
    var gs=parseInt(sg.value,10)/100;
    var lgs=Math.log(gs)/Math.LN10;
    // 折れ曲がる位置：古典の走りが g* に達するエネルギー
    var lEs=(lgs/2)+Math.log(hbarc/lP)/Math.LN10;

    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right';
    for(var e=-45;e<=0;e+=15){
      var y=py(e);
      g.strokeStyle='#eef3f3'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#95a8a8'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=24;q+=6){
      var x=px(q);
      g.strokeStyle='#f6faf9'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#95a8a8'; g.fillText('10'+q+' GeV', x, Y1+16);
    }
    g.strokeStyle='#c5d4d4'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // プランクエネルギー
    var lPl=Math.log(Epl)/Math.LN10;
    g.strokeStyle='#c2cfcf'; g.lineWidth=1.6; g.setLineDash([5,4]);
    g.beginPath(); g.moveTo(px(lPl),Y0); g.lineTo(px(lPl),Y1); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#8ea0a0'; g.textAlign='center';
    g.fillText('プランク', px(lPl), Y0-8);

    // 固定点の水平線
    g.strokeStyle='#8a3a3a'; g.lineWidth=2.2; g.setLineDash([7,5]);
    g.beginPath(); g.moveTo(X0,py(lgs)); g.lineTo(X1,py(lgs)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#7a3232'; g.textAlign='left';
    g.fillText('固定点 g* = '+gs.toFixed(2), X0+10, py(lgs)-8);

    // 走り
    g.strokeStyle='#2a5a5a'; g.lineWidth=3.4;
    g.beginPath();
    var first=true;
    for(var i=0;i<=300;i++){
      var lE=xmin+(xmax-xmin)*i/300;
      var y=(lE<lEs)? lgG(lE) : lgs;
      if(y<ymin||y>ymax){ first=true; continue; }
      if(first){ g.moveTo(px(lE),py(y)); first=false; } else g.lineTo(px(lE),py(y));
    }
    g.stroke();

    // 折れ点
    if(lEs>xmin&&lEs<xmax){
      g.fillStyle='#2a5a5a';
      g.beginPath(); g.arc(px(lEs),py(lgs),6,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=2;
      g.beginPath(); g.arc(px(lEs),py(lgs),6,0,6.2832); g.stroke();
    }

    g.fillStyle='#2a5a5a'; g.textAlign='left';
    g.fillText('傾き 2（古典次元）', px(8), py(lgG(8))-10);
    g.fillStyle='#7a3232';
    g.fillText('傾き 0（異常次元 −2 が相殺）', px(lEs)+14, py(lgs)+18);

    g.fillStyle='#7d9090'; g.textAlign='center';
    g.fillText('エネルギースケール  k', (X0+X1)/2, Y1+38);
    g.save(); g.translate(19,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('無次元の結合 g = G k²', 0,0); g.restore();

    vg.textContent='g* = '+gs.toFixed(2);
    ro.textContent='g* = '+gs.toFixed(2)+
      '　→　折れ曲がるのは '+Math.pow(10,lEs).toExponential(2)+' GeV（プランクの '+
      (Math.pow(10,lEs)/Epl).toFixed(2)+' 倍）'+
      '　／　その上では η_N = −2 が古典次元 +2 をちょうど打ち消す ── ウェイト表の誤差 100%';
  }
  sg.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-35-asymptotic-safety.html', acc='#2a5a5a', ops='#8a3a3a',
      title='漸近安全性と、走る G ── わかる c·t=一定 第35回',
      ep='第 35 回 ／ 第 IV 部・第14回の異常次元が、重力に届く',
      eyebrow='イジングは 3.6%、重力の固定点は 100%',
      h1='漸近安全性と、<br>走る \\(G\\)',
      sub='\\(G\\) をスケールと組んで無次元化し、走らせて固定点を探す。<br><em>すると第14回のウェイト表の誤差が、重力では 100% になります。</em>',
      byline_l='必要な道具：第3回の判定手続き、第14回の異常次元、第19回の作法',
      byline_r='\\(\\eta_N=-2\\) ── 古典次元が丸ごと消える',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第35回、物理好きの高校生・大学生向け読み物です。漸近安全性は Weinberg (1979) の提案と Reuter (1998) 以降の汎関数繰り込み群による研究によります。4 次元で \\([G]=\\)長さ\\(^2\\) であること、\\(g=Gk^2\\) が無次元であること、非ガウス固定点で \\(\\eta_N=-2\\) となることは、いずれも標準的です。本稿の \\(g\\) の値（陽子スケールで \\(6.7\\times10^{-39}\\)、プランクで \\(1.0\\)）、傾き 2.00、および第14回との比較（イジング 3.6%、重力 100%）は本稿での計算です（kenshou/calc39.py）。<strong>固定点の値 \\(g^*\\simeq0.71\\)、\\(\\lambda^*\\simeq0.19\\) は切り捨てとスキームに依存し、値は数割動きます</strong> ── 固定点の存在は多くの切り捨てで確認されていますが、真の非摂動的な結果であることの厳密な証明はありません。<strong>\\(\\eta_N=-2\\) は「固定点で \\(g\\) が定数になる」ことの言い換えであり、定義上そうなるという側面が強い</strong>（第19回の分類では恒等式に近い）── 04節の主張は「もし固定点があるなら、ウェイト表の誤差が最大になる」という点です。「relevant な方向が 2〜3 個」は切り捨て計算による見積もりで、<strong>個数が確定していないこと自体がこの理論の予言力に対する主要な批判の一つ</strong>です。ヒッグス質量の予言は Shaposhnikov &amp; Wetterich (2010, Phys. Lett. B683, 196) によるもので、<strong>物質セクターの仮定に依存し、頑健性には議論があります</strong> ── 本稿は当たったという事実とその驚きの大きさを記録するに留めます。実測値 \\(m_H=125.25\\pm0.17\\) GeV は PDG による値です。漸近安全性は有力な候補の一つですが確立した量子重力理論ではなく、弦理論・ループ量子重力・因果的動的三角形分割など他の候補と並んで決着していません。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルと、修正のない一般相対論です。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで固定点の値を変え、折れ曲がる場所が動く様子が見えます。「答えを見る」で解答が開きます。')
