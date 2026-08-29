# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">前回、終期の側が<strong>第 3 段</strong>（道具が届かない）だと分かりました。今回はそこへ入っていきます ── <strong>ブラックホールの内部</strong>。結論を先に言うと、<em>事象の地平面はウェイト 0 で、共形変換では作れも消せもしません</em>。ところが<strong>見かけの地平面のほうは動きます</strong>。そして中に入っても、\(1.5\times10^{77}\) ビットは<em>読めません</em>。</p>

<h2><span class="n">01</span>地平面は、共形変換で消せるか</h2>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>共形変換 \(g\to\Omega^2g\) は、光円錐を動かさない</strong><span>\(\Omega>0\) がなめらかなら、ヌル測地線の集合は変わらない ── <em>因果構造はそのまま</em></span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>事象の地平面の定義は、因果構造だけで決まる</strong><span>「未来のヌル無限遠の因果的過去の境界」── 距離も時間も出てこない</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>したがって、事象の地平面はウェイト 0</strong><span><em>共形変換では作れも消せもしません</em> ── このシリーズの道具が、ブラックホールを消せない理由</span></div></div>
</div>

<h2><span class="n">02</span>ところが、見かけの地平面は共形不変ではない</h2>

<div class="calc">
<span class="tag">見かけの地平面は「外向きヌル束の膨張 \(\theta=0\)」で決まる ── 局所的な量</span>
$$\theta\;\to\;\Omega^{-1}\left(\theta+2\,l^\mu\partial_\mu\ln\Omega\right)$$
<p class="lbl">\(\theta=0\) は保たれない ── <strong>見かけの地平面は動く</strong></p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>地平面</th><th class="mid">決め方</th><th class="mid">ウェイト</th><th class="mid">共形変換</th></tr></thead>
<tbody>
<tr class="hi"><th>事象の地平面</th><td class="mid">因果構造（大域的）</td><td class="mid"><strong>\(0\)</strong></td><td class="mid"><strong>動かない</strong></td></tr>
<tr><th>見かけの地平面</th><td class="mid">\(\theta=0\)（局所的）</td><td class="mid">\(\ne0\)</td><td class="mid"><strong>動く</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0">二つの地平面の違いが、そのまま<strong>ウェイトの違い</strong>になっています。<br>
ただし事象の地平面を実際に見つけるには<em>未来を全部知る必要があります</em> ──<br>
<strong>動かない方は測れず、測れる方は動く。</strong></p>
</div>

<h2><span class="n">03</span>ペンローズ図 ── 記法が仕事をする場所</h2>

<div class="seven">
<div class="row"><div class="mk">＝</div><div class="txt"><strong>ペンローズ図は、共形変換そのもの</strong><span>\(\Omega\) を選んで、無限遠を有限の距離に引き寄せる</span></div></div>
<div class="row"><div class="mk">変</div><div class="txt"><strong>変わるもの：紙の上の距離</strong><span>帳簿 ── 何の主張でもない</span></div></div>
<div class="row hi"><div class="mk">不</div><div class="txt"><strong>変わらないもの：光円錐の傾き</strong><span>＝ 因果構造 ＝ <em>物理</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">03節の結論</p>
<p style="margin:6px 0 0">第1回の主張「\(c\cdot t=\)一定 は記法であってモデルではない」の<strong>双子</strong>です ──<br>
ペンローズ図もモデルではありません。<em>それでも相対論で最も有用な道具の一つ</em>。<br>
── <strong>記法は無価値ではありません。ただ、主張ではないだけです。</strong></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>核心 ── 中に入っても、中身は読めない</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>ブラックホール</th><th class="mid">地平面での潮汐 [g]</th><th class="mid">地平面→特異点 [s]</th></tr></thead>
<tbody>
<tr><th>太陽質量</th><td class="mid">\(2.10\times10^{9}\)</td><td class="mid">\(1.55\times10^{-5}\)</td></tr>
<tr><th>いて座 A\(^*\)（\(4.3\times10^6M_\odot\)）</th><td class="mid">\(1.14\times10^{-4}\)</td><td class="mid">\(66.6\)</td></tr>
<tr class="hi"><th>M87\(^*\)（\(6.5\times10^9M_\odot\)）</th><td class="mid"><strong>\(4.97\times10^{-11}\)</strong></td><td class="mid">\(1.01\times10^{5}\)</td></tr>
</tbody>
</table>
</div>

<p>太陽質量では \(2\times10^9\) g ── <em>原子ごと引き裂かれます</em>。ところが <strong>M87\(^*\) では \(5\times10^{-11}\) g、まったく感じません</strong>。<em>地平面は「何かが起きる場所」ではありません</em> ── 大きいブラックホールでは、通過に気づかないのです。</p>

<div class="calc">
<span class="tag">では、中で情報は読めるか（第24回のチャンネル容量を 70 kg の観測者に当てる）</span>
$$C=\frac{2\pi mc^2}{\hbar\ln2}=5.41\times10^{53}\ \text{bit/s}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>ブラックホール</th><th class="mid">読める [bit]</th><th class="mid">BH の \(S\) [bit]</th><th class="mid">足りない [bit]</th></tr></thead>
<tbody>
<tr><th>太陽質量</th><td class="mid">\(8.37\times10^{48}\)</td><td class="mid">\(1.51\times10^{77}\)</td><td class="mid">\(93.9\)</td></tr>
<tr><th>いて座 A\(^*\)</th><td class="mid">\(3.60\times10^{55}\)</td><td class="mid">\(2.80\times10^{90}\)</td><td class="mid">\(115.9\)</td></tr>
<tr class="hi"><th>M87\(^*\)</th><td class="mid">\(5.44\times10^{58}\)</td><td class="mid">\(6.40\times10^{96}\)</td><td class="mid"><strong>\(126.5\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>どの場合も、桁違いに足りません。</strong><br>
── 情報が「失われる」かどうか以前に、<em>取り出す時間がありません</em>。<br>
<strong>大きいブラックホールほど中にいる時間は長いのに、足りなさは大きくなります</strong>（93.9 → 126.5 ビット）。</p>
</div>

<div class="fig">
<p class="cap">図：ブラックホールの質量を動かしたときの、<strong>地平面での潮汐（感じるか）</strong>と<strong>中で読める情報の足りなさ</strong>。ツマミを動かすと、<em>大きいほど痛くないのに、大きいほど読めない</em>ことが見えます</p>
<canvas id="cv" width="720" height="370"></canvas>
<div class="controls">
  <label>ブラックホールの質量 \(\log_{10}(M/M_\odot)\)<input id="sm" type="range" min="0" max="100" value="0" step="1"></label>
  <span class="val" id="vm">0.0</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#4a3a6a"></i>地平面での潮汐 [g]（対数）</span>
  <span><i class="swatch" style="background:#2a6a4a"></i>読めない量 [bit]</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>人が耐えられる目安（10 g）</span>
</div>
</div>

<h2><span class="n">05</span>蒸発の時計</h2>

<div class="calc">
<span class="tag">ホーキング蒸発</span>
$$t_{\rm evap}=\frac{5120\pi G^2M^3}{\hbar c^4}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>ブラックホール</th><th class="mid">\(t_{\rm evap}\) [年]</th><th class="mid">宇宙年齢の何倍</th></tr></thead>
<tbody>
<tr><th>太陽質量</th><td class="mid">\(2.10\times10^{67}\)</td><td class="mid">\(1.5\times10^{57}\)</td></tr>
<tr><th>M87\(^*\)</th><td class="mid">\(5.76\times10^{96}\)</td><td class="mid">\(4.2\times10^{86}\)</td></tr>
<tr class="hi"><th>いま蒸発し終わる質量</th><td class="mid" colspan="2"><strong>\(M=1.73\times10^{11}\) kg（地球の山ひとつぶん）</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>恒星質量以上のブラックホールは、宇宙年齢の \(10^{57}\) 倍以上かかります</strong> ── 実質、蒸発しません。いま蒸発し終わる質量帯（\(10^{11}\) kg）は、<em>原始ブラックホールとして探されている</em>ところです。</p>

<h2><span class="n">06</span>ページ時間 ── 情報が出てくるとしたら、いつか</h2>

<div class="calc">
<span class="tag">面積が半分になるのは \(M/M_0=1/\sqrt2\) のとき</span>
$$\frac{t}{t_{\rm evap}}=1-\left(\frac1{\sqrt2}\right)^3=0.6464\qquad\text{── 蒸発時間の 65 パーセント}$$
</div>

<p>ページ曲線では、放射のエンタングルメント・エントロピーがブラックホールのエントロピーと等しくなる時点で折り返します。<em>よく引かれる「0.54」は別の規約による値</em>で、ここでは面積が半分になる時点を採りました。<strong>どちらにせよ蒸発の中盤</strong> ── 情報が出てくるとしたら、そこから後。太陽質量なら \(1.4\times10^{67}\) 年後です。</p>

<h2><span class="n">07</span>ウェイト表で確かめる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">ウェイト</th><th class="mid">理由</th></tr></thead>
<tbody>
<tr><th>事象の地平面があるかどうか</th><td class="mid">\(0\)</td><td class="mid">因果構造だけで決まる</td></tr>
<tr><th>\(S=A/4\ell_P^2\)</th><td class="mid">\(0\)</td><td class="mid">第40回①</td></tr>
<tr><th>潮汐加速度を \(g\) で測った値</th><td class="mid">\(0\)</td><td class="mid">加速度 ÷ 加速度</td></tr>
<tr><th>\(t_{\rm evap}/t_0\)</th><td class="mid">\(0\)</td><td class="mid">時間 ÷ 時間</td></tr>
<tr><th>ページ時間の割合</th><td class="mid">\(0\)</td><td class="mid">時間 ÷ 時間</td></tr>
<tr class="hi"><th><strong>見かけの地平面の位置</strong></th><td class="mid"><strong>\(\ne0\)</strong></td><td class="mid"><strong>ここだけが例外</strong></td></tr>
</tbody>
</table>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p style="margin:0 0 10px"><strong>① 01節の「共形変換が因果構造を保つ」には条件があります。</strong> \(\Omega\) が<em>どこでも正でなめらか</em>であることが必要で、\(\Omega\) がゼロになったり発散したりする点（ペンローズ図で無限遠を持ってくる境界がまさにそれ）では、話が別になります ── <strong>境界の扱いこそが共形幾何のいちばん微妙なところ</strong>で、第31回の CCC も第41回のワイル仮説も、その微妙な場所での要請でした。</p>
<p style="margin:0 0 10px"><strong>② 04節の「読める情報」は、上限の上限です。</strong> 第24回のチャンネル容量（マルゴラス–レヴィティン限界）は<em>理想的な量子計算の速度上限</em>で、実在の観測者がその速度で情報を取り込めるという意味ではありません ── <strong>「足りない」という結論は、この最も甘い見積もりでさえ足りない、という形で強くなります</strong>が、数値そのものは目安です。</p>
<p style="margin:0 0 10px"><strong>③ 04節の潮汐と落下時間は、シュヴァルツシルト解での値です。</strong> 実在のブラックホールは回転しており（第39回）、内部構造も違います ── <em>桁を見るための計算</em>と読んでください。また、静止状態から自由落下した場合の最大固有時であって、落ち方によっては短くなります。</p>
<p style="margin:0 0 10px"><strong>④ 06節のページ曲線は、まだ完全には決着していない話題です。</strong> 近年の「島（island）」の計算はページ曲線を再現しますが、<em>情報がどのように出てくるかの機構は未解決</em>です。本稿は「いつ折り返すか」の時刻だけを扱い、<strong>情報が実際に出てくるかどうかについては何も主張しません</strong>。</p>
<p style="margin:0"><strong>⑤ 05節の蒸発時間は、周囲から何も落ちてこない理想の場合です。</strong> 実際には CMB（2.7 K）のほうが恒星質量ブラックホールのホーキング温度（\(10^{-8}\) K 程度）より高いので、<em>現在の宇宙ではこれらのブラックホールは蒸発せず、むしろ吸収して成長しています</em> ── 蒸発が始まるのは、宇宙が十分冷えたずっと先です。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>共形変換で事象の地平面を消せるか。理由も。
<details><summary>答えを見る</summary><div class="ans"><strong>消せません</strong>。共形変換は光円錐を動かさず、事象の地平面は<em>因果構造だけで決まる</em>（「未来のヌル無限遠の因果的過去の境界」）からです ── <strong>ウェイト 0</strong>。ただし①のとおり、\(\Omega\) がどこでも正でなめらかであることが条件です。</div></details></li>

<li>見かけの地平面はどうか。
<details><summary>答えを見る</summary><div class="ans"><strong>動きます</strong>。\(\theta=0\) という<em>局所的</em>な条件で決まり、共形変換のもとで \(\theta\to\Omega^{-1}(\theta+2l^\mu\partial_\mu\ln\Omega)\) なので \(\theta=0\) は保たれません。── <em>動かない方（事象）は未来を全部知らないと測れず、測れる方（見かけ）は動く</em>。</div></details></li>

<li>M87\(^*\) の地平面を通過すると、どれくらい痛いか。
<details><summary>答えを見る</summary><div class="ans"><strong>まったく感じません</strong> ── \(5\times10^{-11}\) g。太陽質量なら \(2\times10^9\) g で原子ごと引き裂かれますが、潮汐は \(1/M^2\) で落ちます。<em>地平面は「何かが起きる場所」ではありません</em>。</div></details></li>

<li>中に入れば、ブラックホールの情報を読めるか。
<details><summary>答えを見る</summary><div class="ans"><strong>読めません</strong>。第24回のチャンネル容量で最も甘く見積もっても、太陽質量で <strong>93.9 ビット</strong>、M87\(^*\) で <strong>126.5 ビット</strong>足りません ── <em>情報が「失われる」かどうか以前に、取り出す時間がありません</em>。しかも<strong>大きいほど中にいる時間は長いのに、足りなさは増えます</strong>。</div></details></li>

<li>（やや難）ペンローズ図と \(c\cdot t=\)一定 の共通点は。
<details><summary>答えを見る</summary><div class="ans"><strong>どちらも記法であって、モデルではない</strong>ことです。ペンローズ図は共形変換そのもので、変わるのは紙の上の距離（帳簿）、変わらないのは光円錐の傾き（物理）。<em>それでも相対論で最も有用な道具の一つ</em> ── <strong>記法は無価値ではありません。ただ、主張ではないだけです。</strong></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　動かない方は測れず、測れる方は動く</h2>
<p>共形変換 \(g\to\Omega^2g\) は光円錐を動かしません。そして事象の地平面は<em>因果構造だけで決まります</em>から ── <strong>事象の地平面はウェイト 0、共形変換では作れも消せもしません</strong>。このシリーズの道具が、ブラックホールを消せない理由です。</p>
<p>ところが<strong>見かけの地平面は動きます</strong>。\(\theta=0\) という局所的な条件で決まり、\(\theta\to\Omega^{-1}(\theta+2l^\mu\partial_\mu\ln\Omega)\) だからです。<em>二つの地平面の違いが、そのままウェイトの違いになっていました</em> ── そして<strong>動かない方は未来を全部知らないと測れず、測れる方は動く</strong>。</p>
<p>ペンローズ図は共形変換そのものです。変わるのは紙の上の距離（帳簿）、変わらないのは光円錐の傾き（物理）── <em>第1回の「\(c\cdot t=\)一定 は記法であってモデルではない」の双子</em>で、それでも相対論で最も有用な道具の一つです。<strong>記法は無価値ではありません。ただ、主張ではないだけです。</strong></p>
<p>中に入るとどうなるか。太陽質量なら地平面で \(2\times10^9\) g、原子ごと引き裂かれますが、<strong>M87\(^*\) なら \(5\times10^{-11}\) g でまったく感じません</strong> ── 地平面は「何かが起きる場所」ではありません。では中で情報は読めるか。第24回のチャンネル容量で最も甘く見積もっても、<strong>太陽質量で 93.9 ビット、M87\(^*\) で 126.5 ビット足りません</strong>。<em>情報が「失われる」かどうか以前に、取り出す時間がないのです</em> ── しかも大きいほど中にいる時間は長いのに、足りなさは増えます。</p>
<p>外で待つのはどうか。恒星質量ブラックホールの蒸発は<strong>宇宙年齢の \(10^{57}\) 倍以上</strong>、情報が出てくるとしたらページ時間（蒸発の 65 パーセント）から後 ── 太陽質量なら \(1.4\times10^{67}\) 年後です。<em>ブラックホールの話は、見かけの地平面を除いて全部 0 の列にありました。</em></p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第43回</span>
今回、ブラックホールの話がほぼ全部<strong>ウェイト 0 の列</strong>にあることを見ました。次回は<strong>プランクスケール</strong>へ行きます ── 第18回で「1 ビット \(\leftrightarrow\) 1.96 fm」を出しましたが、<em>プランク長そのものは何なのか</em>。ウェイト表で \(\ell_P\) はどこにいるのか。そして<strong>「長さに最小単位がある」は、共形変換と両立するのか</strong> ── <em>ここで、このシリーズの道具は本当に壊れます。</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sm=document.getElementById('sm'), vm=document.getElementById('vm'), ro=document.getElementById('ro');
  var X0=80, X1=690, Y0=36, Y1=270;
  var G=6.6743e-11, c=2.99792458e8, hbar=1.054571817e-34, Ms=1.98892e30, g0=9.80665, LN2=Math.LN2;

  function px(l){ return X0+l/10*(X1-X0); }
  function tidal(l){ var M=Math.pow(10,l)*Ms; return 2*Math.pow(c,6)/(4*G*G*M*M)/g0; }
  function shortfall(l){
    var M=Math.pow(10,l)*Ms;
    var tau=Math.PI*G*M/(c*c*c);
    var read=2*Math.PI*70*c*c/(hbar*LN2)*tau;
    var S=4*Math.PI*G*M*M/(hbar*c)/LN2;
    return Math.log(S/read)/LN2;
  }
  function pyT(v){ return Y1-(Math.log(v)/Math.LN10+12)/24*(Y1-Y0); }   // log10 tidal: -12..12
  function pyS(v){ return Y1-(v-80)/60*(Y1-Y0); }                        // 80..140 bit

  function draw(){
    var l=parseInt(sm.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    // 耐えられる目安 10 g
    g.strokeStyle='#c8c2d0'; g.lineWidth=1.6; g.setLineDash([5,4]);
    g.beginPath(); g.moveTo(X0,pyT(10)); g.lineTo(X1,pyT(10)); g.stroke(); g.setLineDash([]);
    g.fillStyle='#a89fae'; g.textAlign='left';
    g.fillText('人が耐えられる目安（10 g）', X0+8, pyT(10)-7);

    g.textAlign='center'; g.fillStyle='#9c96a4';
    for(var t=0;t<=10;t+=2){
      var X=px(t);
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X,Y0); g.lineTo(X,Y1); g.stroke();
      g.fillText('10^'+t, X, Y1+20);
    }

    g.strokeStyle='#4a3a6a'; g.lineWidth=2.8; g.beginPath();
    for(var i=0;i<=200;i++){ var v=i/20, X2=px(v), Y2=pyT(tidal(v)); if(i===0)g.moveTo(X2,Y2); else g.lineTo(X2,Y2); }
    g.stroke();
    g.strokeStyle='#2a6a4a'; g.lineWidth=2.4; g.beginPath();
    for(var j=0;j<=200;j++){ var v3=j/20, X3=px(v3), Y3=pyS(shortfall(v3)); if(j===0)g.moveTo(X3,Y3); else g.lineTo(X3,Y3); }
    g.stroke();

    g.textAlign='left';
    g.fillStyle='#4a3a6a'; g.fillText('地平面での潮汐 [g]（1/M² で落ちる）', px(0.3), pyT(tidal(0.3))-10);
    g.fillStyle='#2a6a4a'; g.fillText('読めない量 [bit]（大きいほど増える）', px(3.4), pyS(shortfall(3.4))-10);

    var Xc=px(l);
    g.strokeStyle='#5a5262'; g.lineWidth=1.8; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(Xc,Y0); g.lineTo(Xc,Y1); g.stroke(); g.setLineDash([]);
    g.fillStyle='#4a3a6a'; g.beginPath(); g.arc(Xc,pyT(tidal(l)),4.6,0,6.29); g.fill();
    g.fillStyle='#2a6a4a'; g.beginPath(); g.arc(Xc,pyS(shortfall(l)),4.6,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('ブラックホールの質量 M / M☉', (X0+X1)/2, Y1+44);

    vm.textContent=l.toFixed(1);
    var M=Math.pow(10,l)*Ms, tau=Math.PI*G*M/(c*c*c);
    ro.textContent='M = 10^'+l.toFixed(1)+' M☉　→　地平面の潮汐 '+tidal(l).toExponential(2)+
      ' g　／　地平面から特異点まで '+tau.toExponential(2)+' s　／　読めない量 '+shortfall(l).toFixed(1)+' bit'+
      (tidal(l)<10?'　★ もう痛くない ── それでも読めない量は増えている':'');
  }
  sm.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-42-inside.html', acc='#4a3a6a', ops='#2a6a4a',
      title='ブラックホールの内部 ── わかる c·t=一定 第42回（第V部）',
      ep='第 42 回 ／ 第 V 部・道具が壊れる場所',
      eyebrow='動かない方は測れず、測れる方は動く',
      h1='地平面は、<br>共形変換では消せない',
      sub='事象の地平面はウェイト 0 ── 因果構造だけで決まるからです。<br><em>ところが見かけの地平面は動きます。そして中に入っても、中身は読めません。</em>',
      byline_l='必要な道具：第1回の記法論、第24回のチャンネル容量、第39回、第40回、第41回',
      byline_r='M87\\(^*\\) の地平面は \\(5\\times10^{-11}\\) g ── 気づかない',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第42回（第 V 部の 6 回目）、物理好きの高校生・大学生向け読み物です。共形変換が因果構造を保つこと、事象の地平面と見かけの地平面の性質の違い、ペンローズ図、ホーキング蒸発、ページ曲線はいずれも標準的な内容で、本稿に新しい主張はありません ── 数値は kenshou/calc46.py で計算しています。<strong>01節の「共形変換が因果構造を保つ」には \\(\\Omega\\) がどこでも正でなめらかであることが必要で</strong>、\\(\\Omega\\) がゼロになったり発散したりする点（ペンローズ図で無限遠を持ってくる境界がまさにそれ）では話が別です ── 境界の扱いこそが共形幾何のいちばん微妙なところです。<strong>04節の「読める情報」は上限の上限で</strong>、第24回のチャンネル容量（マルゴラス–レヴィティン限界）は理想的な量子計算の速度上限であり、実在の観測者がその速度で情報を取り込めるという意味ではありません ── <em>「最も甘い見積もりでさえ足りない」という形で結論は強くなりますが、数値そのものは目安</em>です。04節の潮汐と落下時間はシュヴァルツシルト解での値で（実在のブラックホールは回転しています）、静止状態から自由落下した場合の最大固有時です。<strong>06節のページ曲線はまだ完全には決着していない話題で</strong>、近年の「島」の計算はページ曲線を再現しますが情報がどう出てくるかの機構は未解決です ── 本稿は折り返しの時刻だけを扱い、<em>情報が実際に出てくるかどうかについては何も主張しません</em>。<strong>05節の蒸発時間は周囲から何も落ちてこない理想の場合で</strong>、実際には CMB（2.7 K）のほうが恒星質量ブラックホールのホーキング温度より高いため、<em>現在の宇宙ではこれらは蒸発せず吸収して成長しています</em>。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで質量を動かすと、痛くなくなるのに読めなくなることが見えます。「答えを見る」で解答が開きます。')
