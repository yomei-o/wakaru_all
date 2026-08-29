# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第18回で「体積セルには、はじめから番地が振られていない」と数えました。では地平面に書かれた \(10^{122}\) ビットは、<em>どうやって守られているのか</em>。今回は<strong>符号の言葉</strong>で読み直します。すると第6回の「使用率 \(1.5\times10^{-18}\)」が、まったく違う顔で出てきます ── <strong>冗長度 \(6.6\times10^{17}\)</strong>。<em>空いているのではなく、同じ情報が何度も書かれている</em>という読み方です。</p>

<h2><span class="n">01</span>符号として読む</h2>

<p>誤り訂正符号は、二つの数で特徴づけられます ── <strong>物理ビット \(n\)</strong>（実際に使う記憶素子の数）と <strong>論理ビット \(k\)</strong>（守りたい情報の量）。宇宙に当てはめます。</p>

<div class="calc">
<span class="tag">二つの数を入れる</span>
<p class="lbl">物理ビット（地平面に書ける量、第1回）</p>
$$n=2.96\times10^{122}$$
<p class="lbl">論理ビット（実際に使われているエントロピー、第6回）</p>
$$k=\frac{S_{\rm obs}/k_B}{\ln2}=\frac{3.1\times10^{104}}{0.693}=4.47\times10^{104}$$
<p class="lbl">符号化率と冗長度</p>
$$R=\frac{k}{n}=1.51\times10^{-18},\qquad \frac{n}{k}=6.61\times10^{17}$$
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0">第6回の「使用率 \(1.5\times10^{-18}\)」は、符号の言葉では <strong>「冗長度 \(6.6\times10^{17}\)」</strong>。<br>
<em>同じ数字を、まったく逆向きに読んだことになります。</em></p>
</div>

<h2><span class="n">02</span>現実の符号と比べる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>符号</th><th class="mid">冗長度 \(n/k\)</th><th class="mid">備考</th></tr></thead>
<tbody>
<tr><th>QR コード（最高水準）</th><td class="mid">1.4</td><td class="mid">30% の汚れまで復元</td></tr>
<tr><th>RAID6</th><td class="mid">1.5</td><td class="mid">ディスク 2 台まで故障可</td></tr>
<tr><th>低符号化率の通信路符号</th><td class="mid">10</td><td class="mid">深宇宙通信など</td></tr>
<tr><th>量子誤り訂正・表面符号</th><td class="mid">\(10^{3}\)</td><td class="mid">論理 1 量子ビットに物理 1000 個</td></tr>
<tr class="hi"><th>宇宙の地平面</th><td class="mid"><strong>\(6.6\times10^{17}\)</strong></td><td class="mid"><strong>表面符号の \(6.6\times10^{14}\) 倍</strong></td></tr>
</tbody>
</table>
</div>

<p>人間が作るどんな符号よりも、<strong>14 桁ぶん冗長</strong>です。量子誤り訂正が「論理 1 量子ビットに物理 1000 個も要る」と嘆かれるところ、宇宙は \(10^{18}\) 個使っています。</p>

<h2><span class="n">03</span>訂正能力の上限を見積もる</h2>

<p>符号化率がこれだけ低いと、原理上どこまで壊れても復元できるのでしょうか。シングルトン限界（符号の距離 \(d\) の上限）で見積もります。</p>

<div class="calc">
<span class="tag">上限</span>
<p class="lbl">古典符号</p>
$$d\le n-k+1=2.96\times10^{122}\qquad(\text{ほぼ }n\text{ そのもの})$$
<p class="lbl">量子符号</p>
$$d\le\frac{n-k}{2}+1=1.48\times10^{122}=\frac{n}{2}$$
</div>

<div class="keybox">
<p class="lbl">03節の結論</p>
<p style="margin:6px 0 0">原理上は ── <strong>地平面のビットの約半分が壊れても、中身は復元できる。</strong><br>
（ただしこれは<em>上限</em>であって、実際にそういう符号になっている保証はありません）</p>
</div>

<div class="fig">
<p class="cap">図：冗長度の比較（対数）。人間の符号は左端に固まり、宇宙だけが桁違いに右です。ツマミは<strong>使われているエントロピーの見積もり</strong>を動かします ── \(S_{\rm obs}\) には桁の不確かさがあるので、冗長度もそのぶん動きます</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>使われているエントロピー \(\log_{10}(S_{\rm obs}/k_B)\)（既定は 104.5）<input id="ss" type="range" min="1000" max="1100" value="1045" step="1"></label>
  <span class="val" id="vs">10^104.5</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a4a"></i>人間が作る符号</span>
  <span><i class="swatch" style="background:#8a4a2a"></i>宇宙の地平面</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>核心 ── 空きなのか、冗長なのか</h2>

<p>ここが今回の要です。<strong>まったく同じ \(1.5\times10^{-18}\) を、二通りに読めます。</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>読み方</th><th>何を言っているか</th><th class="mid">出どころ</th></tr></thead>
<tbody>
<tr><th>① 空いている</th><td>容量の \(1.5\times10^{-18}\) しか使っていない</td><td class="mid">第6回</td></tr>
<tr class="hi"><th>② 冗長である</th><td>同じ情報が \(6.6\times10^{17}\) 回ぶん重ねて書かれている</td><td class="mid">今回</td></tr>
</tbody>
</table>
</div>

<p>観測でこの二つを区別できるでしょうか。── <strong>第3回の手続きが、そのまま効きます。</strong></p>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>「空き」と「冗長」は、比較相手を言うまで区別できません。</strong><br>
<em>容量と比べれば空き、情報と比べれば冗長</em> ── 同じ一つの比の、二つの読み方です。</p>
</div>

<p>第3回では「\(c\cdot t\) が一定」に、第9回では「原子が縮む」に、第12回では「宇宙定数」に、同じ手術を当てました。今回は<strong>このシリーズが自分で出した数字</strong>に当てています ── <em>比較相手を言わないまま「空っぽだ」と言うのは、まだ文になっていない。</em></p>

<h2><span class="n">05</span>ホログラフィック符号という前例</h2>

<p>「境界の情報でバルクを守る」という構造は、思いつきではありません。AdS/CFT には<strong>量子誤り訂正符号としての読み方</strong>があります（アルムヘイリ＝ドン＝ハーロウ 2015）。</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>バルクの局所演算子は、境界の部分領域から再構成できる</strong><span>境界の一部を失っても、バルクの中心の情報は残っている</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>それは誤り訂正符号の定義そのもの</strong><span>「符号空間の情報が、部分系の消去に耐える」── 数学的に同じ構造</span></div></div>
<div class="row hi"><div class="mk">✗</div><div class="txt"><strong>ただし、宇宙論的地平面では確立していない</strong><span>AdS 境界と宇宙の地平面は別物。de Sitter / FLRW のホログラフィーは未解決 ── <em>今回の話は類推まで</em></span></div></div>
</div>

<p>だから今回できるのは<strong>「数を符号の言葉に翻訳すること」まで</strong>で、「宇宙が実際に誤り訂正符号である」とは言えません。この線は、はっきり引いておきます。</p>

<h2><span class="n">06</span>自制する ── 論理 1 ビットの大きさ</h2>

<p>第18回では「物理 1 ビットあたりの体積の一辺が 1.96 fm ＝ 陽子の大きさ」という一致が出ました。同じことを<em>論理ビット</em>でやってみます。</p>

<div class="calc">
<span class="tag">論理 1 ビットが占める面積</span>
$$\frac{A}{k}=\frac{2.14\times10^{53}}{4.47\times10^{104}}=4.79\times10^{-52}\ \mathrm{m^2}\qquad\Longrightarrow\qquad \text{一辺}\ 2.19\times10^{-26}\ \mathrm{m}$$
</div>

<p>第19回の作法で、何かに一致するか確かめます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>相手</th><th class="mid">長さ</th><th class="mid">比</th></tr></thead>
<tbody>
<tr><th>陽子</th><td class="mid">\(10^{-15}\) m</td><td class="mid">\(2.2\times10^{-11}\)</td></tr>
<tr><th>電弱スケール</th><td class="mid">\(2.5\times10^{-18}\) m</td><td class="mid">\(8.8\times10^{-9}\)</td></tr>
<tr><th>大統一スケール</th><td class="mid">\(2\times10^{-32}\) m</td><td class="mid">\(1.1\times10^{6}\)</td></tr>
<tr class="hi"><th>プランク長</th><td class="mid">\(1.6\times10^{-35}\) m</td><td class="mid">\(1.4\times10^{9}\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">06節の結論</p>
<p style="margin:6px 0 0"><strong>何とも一致しません。だから、何も言うことがない。</strong><br>
── 第18回の 1.96 fm と違って、この数は近い相手を持たない。<em>沈黙が正解です。</em></p>
</div>

<p>第19回で仕分けの手続きを作ったのは、まさにこのためでした。<strong>計算して出た数がすべて意味を持つわけではない</strong> ── 近い相手がないなら、驚きは 0 ビットで、語ることは何もありません。</p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 「宇宙が誤り訂正符号である」とは言っていません。</strong> やったのは、第1回と第6回の二つの数を<em>符号の言葉に翻訳した</em>だけです。AdS/CFT の量子誤り訂正としての読み方（Almheiri, Dong &amp; Harlow 2015）は AdS 境界についてのもので、<strong>宇宙論的地平面に同じ構造があるかは未解決</strong>です（de Sitter/FLRW のホログラフィー自体が確立していません）。</p>
<p style="margin:0 0 10px"><strong>② \(k=S_{\rm obs}/\ln2\) と置くのは、粗い同一視です。</strong> 熱力学的エントロピーを「守るべき論理ビット」と読むのは自明ではありません ── むしろエントロピーは<em>失われた情報</em>の量なので、逆向きに読むべきだという立場もありえます。図のツマミが示すとおり、\(S_{\rm obs}\) 自体にも桁の不確かさがあります（第6回①）。</p>
<p style="margin:0 0 10px"><strong>③ シングルトン限界は上限であって、達成可能性は別問題です。</strong> 「地平面の半分が壊れても復元できる」は<em>そういう符号が存在しうる</em>という意味で、宇宙がその符号であるという主張ではありません。</p>
<p style="margin:0 0 10px"><strong>④ 表面符号の \(10^3\) は目安です。</strong> 誤り率と要求する論理誤り率によって \(10^2\)〜\(10^4\) と動きます。</p>
<p style="margin:0"><strong>⑤ 04節の「空きか冗長か」は、本シリーズの読み方です。</strong> 二つの読みが観測的に等価だと厳密に示したわけではありません ── <em>比較相手を明示しないと区別が立たない</em>、という手続き上の指摘までです。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>宇宙の地平面を符号として読んだときの、符号化率と冗長度を求めよ。
<details><summary>答えを見る</summary><div class="ans">物理ビット \(n=2.96\times10^{122}\)、論理ビット \(k=3.1\times10^{104}/\ln2=4.47\times10^{104}\)。符号化率 \(R=k/n=1.51\times10^{-18}\)、冗長度 \(n/k=\) <strong>\(6.6\times10^{17}\)</strong>。<em>第6回の使用率と、同じ数の裏表</em>です。</div></details></li>

<li>量子誤り訂正の表面符号と比べて、何倍冗長か。
<details><summary>答えを見る</summary><div class="ans">表面符号は \(10^3\) 程度なので、\(6.6\times10^{17}/10^3=\) <strong>\(6.6\times10^{14}\) 倍</strong>。人間が作るどんな符号より 14 桁ぶん冗長です。</div></details></li>

<li>同じ \(1.5\times10^{-18}\) の二つの読み方を述べ、区別できるか答えよ。
<details><summary>答えを見る</summary><div class="ans">①「容量の \(1.5\times10^{-18}\) しか使っていない（空き）」、②「同じ情報が \(6.6\times10^{17}\) 回重ねて書かれている（冗長）」。<strong>比較相手を言うまで区別できません</strong> ── 容量と比べれば空き、情報と比べれば冗長。第3回の手術が、シリーズ自身の数字に当たった形です。</div></details></li>

<li>論理 1 ビットが占める面積の一辺を求め、何かに一致するか調べよ。
<details><summary>答えを見る</summary><div class="ans">\(A/k=4.79\times10^{-52}\ \mathrm{m^2}\)、一辺 \(2.19\times10^{-26}\) m。陽子より 11 桁小さく、プランク長より 9 桁大きい ── <strong>何とも一致しません</strong>。第19回の作法に従えば、驚きは 0 ビットで<em>語ることは何もない</em>。計算して出た数がすべて意味を持つわけではありません。</div></details></li>

<li>（やや難）「宇宙は誤り訂正符号だ」と言えるか。
<details><summary>答えを見る</summary><div class="ans">言えません。AdS/CFT を量子誤り訂正符号として読む定式化は<strong>AdS 境界についてのもの</strong>で、宇宙論的地平面に同じ構造があるかは未解決です（de Sitter/FLRW のホログラフィー自体が確立していない）。<em>本稿がやったのは、二つの数を符号の言葉に翻訳したところまで</em>です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　同じ数を、裏返して読む</h2>
<p>地平面を符号として読みました ── 物理ビット \(n=2.96\times10^{122}\)、論理ビット \(k=4.47\times10^{104}\)、符号化率 \(R=1.51\times10^{-18}\)。裏返すと <strong>冗長度 \(6.6\times10^{17}\)</strong>。第6回の「使用率 \(1.5\times10^{-18}\)」と、同じ数の裏表です。人間が作るどんな符号よりも 14 桁ぶん冗長で、量子誤り訂正の表面符号（\(10^3\)）が霞みます。シングルトン限界で見れば、原理上は<em>地平面のビットの半分が壊れても復元できる</em>（あくまで上限として）。</p>
<p>核心は読み方でした。<strong>同じ \(1.5\times10^{-18}\) を「空き」とも「冗長」とも読める</strong> ── 容量と比べれば空き、情報と比べれば冗長。<em>比較相手を言うまで、この二つは区別できません。</em> 第3回で \(c\cdot t\) に、第9回で原子に、第12回で宇宙定数に当てた同じ手術が、今回は<strong>このシリーズが自分で出した数字</strong>に当たりました。</p>
<p>前例はあります ── AdS/CFT には量子誤り訂正符号としての読み方があり、「境界の一部を失ってもバルクの中心は復元できる」という構造は符号の定義そのものです。<strong>ただし宇宙論的地平面で同じことが言えるかは未解決</strong>で、今回できたのは<em>数を符号の言葉に翻訳するところまで</em>。この線ははっきり引きました。</p>
<p>最後に一つ、自制しました。論理 1 ビットが占める面積の一辺は \(2.19\times10^{-26}\) m ── 第19回の作法で確かめると、<strong>何とも一致しません</strong>。第18回の 1.96 fm と違って、近い相手を持たない。<em>計算して出た数がすべて意味を持つわけではなく、近い相手がないなら語ることは何もない</em> ── 仕分けの手続きを作ったのは、このためでした。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第24回</span>
次は<strong>通信路容量</strong>です。第17回で「合意に必要だった情報は 20 KB、問題はチャネルが無かったこと」と数えました。ではチャネルはどれだけの太さなのか ── <em>地平面を、毎秒何ビットが渡れるのか</em>。第1回で \(dN/dt=1.36\times10^{105}\) bit/s と数えましたが、あれは<strong>容量が増える速さ</strong>であって、通信速度ではありません。ブレーメルマン限界とベケンシュタイン境界から、<em>実際に情報が渡れる帯域</em>を見積もります。そして「宇宙は 140 手しか指していない」という第2回の結論に、<strong>帯域という制約</strong>を足します。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=210, X1=690, Y0=40;
  var n=2.9556e122, ln2=Math.log(2);
  var CODES=[['QR コード',1.4286],['RAID6',1.5],['通信路符号',10],['表面符号',1e3]];
  var XMAX=20;   // log10 冗長度

  function px(v){ return X0+Math.min(Math.max(v,0),XMAX)/XMAX*(X1-X0); }

  function draw(){
    var lS=parseInt(ss.value,10)/10;
    var k=Math.pow(10,lS)/ln2;
    var red=n/k;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='center';
    for(var b=0;b<=20;b+=4){
      var x=px(b);
      g.strokeStyle=(b===0?'#c2d2cc':'#eef4f1'); g.lineWidth=(b===0?1.6:1);
      g.beginPath(); g.moveTo(x,Y0-8); g.lineTo(x,Y0+5*46+8); g.stroke();
      g.fillStyle='#93a89f'; g.fillText(b===0?'1倍':'10'+b, x, Y0+5*46+24);
    }

    for(var i=0;i<CODES.length;i++){
      var v=Math.log(CODES[i][1])/Math.LN10;
      var y=Y0+i*46+10;
      g.fillStyle='#2a5a4a'; g.globalAlpha=0.85;
      g.fillRect(X0, y, Math.max(px(v)-X0,3), 26);
      g.globalAlpha=1;
      g.fillStyle='#2b3d36'; g.textAlign='right';
      g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillText(CODES[i][0], X0-14, y+18);
      g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.textAlign='left'; g.fillStyle='#4a6a5c';
      g.fillText(CODES[i][1]<100?CODES[i][1].toFixed(1)+'倍':CODES[i][1].toExponential(0)+'倍', px(v)+8, y+18);
    }
    // 宇宙
    var vu=Math.log(red)/Math.LN10, yu=Y0+4*46+10;
    g.fillStyle='#8a4a2a'; g.globalAlpha=0.9;
    g.fillRect(X0, yu, Math.max(px(vu)-X0,3), 26);
    g.globalAlpha=1;
    g.fillStyle='#6d3a1e'; g.textAlign='right';
    g.font='bold 12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('宇宙の地平面', X0-14, yu+18);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.textAlign='left';
    g.fillText(red.toExponential(2)+'倍', px(vu)+8, yu+18);

    g.fillStyle='#7d9188'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('冗長度  n / k （物理ビット ÷ 論理ビット）', (X0+X1)/2, Y0+5*46+48);

    vs.textContent='10^'+lS.toFixed(1);
    ro.textContent='S_obs/k_B = 10^'+lS.toFixed(1)+
      '　→　論理ビット k = '+k.toExponential(2)+
      '　冗長度 '+red.toExponential(2)+'　符号化率 '+(1/red).toExponential(2)+
      '　／　表面符号の '+(red/1e3).toExponential(2)+' 倍'+
      (Math.abs(lS-104.5)<0.06?'　★ 既定値（Egan & Lineweaver 2010）':'');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-23-code.html', acc='#2a5a4a', ops='#8a4a2a',
      title='誤り訂正としての地平面 ── わかる c·t=一定 第23回',
      ep='第 23 回 ／ 同じ数を、裏返して読む',
      eyebrow='使用率 \\(10^{-18}\\) は、符号の言葉では冗長度 \\(10^{18}\\) でした',
      h1='誤り訂正としての、<br>地平面',
      sub='空いているのか、それとも同じ情報が何度も書かれているのか。<br><em>比較相手を言うまで、この二つは区別できません。</em>',
      byline_l='必要な道具：割り算、符号化率の定義',
      byline_r='冗長度 \\(n/k=6.6\\times10^{17}\\)',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第23回、物理好きの高校生・大学生向け読み物です。誤り訂正符号の符号化率 \\(R=k/n\\)、シングルトン限界（古典 \\(d\\le n-k+1\\)、量子 \\(d\\le(n-k)/2+1\\)）は標準的です。本稿の \\(n=2.96\\times10^{122}\\)（第1回）、\\(k=S_{\\rm obs}/\\ln2=4.47\\times10^{104}\\)（第6回、Egan &amp; Lineweaver 2010 による \\(S_{\\rm obs}=3.1\\times10^{104}k_B\\)）、符号化率 \\(1.51\\times10^{-18}\\)、冗長度 \\(6.61\\times10^{17}\\)、および論理 1 ビットあたりの面積 \\(4.79\\times10^{-52}\\ \\mathrm{m^2}\\)（一辺 \\(2.19\\times10^{-26}\\) m）は本稿での計算です（kenshou/calc27.py）。<strong>本稿は「宇宙が誤り訂正符号である」とは主張していません</strong> ── AdS/CFT を量子誤り訂正符号として読む定式化は Almheiri, Dong &amp; Harlow (2015) による AdS 境界についてのもので、<em>宇宙論的地平面に同じ構造があるかは未解決です</em>（de Sitter/FLRW のホログラフィー自体が確立していません）。\\(k=S_{\\rm obs}/\\ln2\\) と置くのは粗い同一視で、熱力学的エントロピーを「守るべき論理ビット」と読むことの妥当性は自明ではありません（エントロピーはむしろ失われた情報の量だ、という立場もありえます）。\\(S_{\\rm obs}\\) 自体に桁の不確かさがあり、図のツマミはそれを示すためのものです。シングルトン限界は上限であって達成可能性とは別問題であり、「半分が壊れても復元できる」はそういう符号が存在しうるという意味です。表面符号の \\(10^3\\) は目安で、要求する論理誤り率により \\(10^2\\)〜\\(10^4\\) と動きます。04節の「空きか冗長か」は本シリーズの読み方であり、二つの読みが観測的に等価だと厳密に示したものではありません。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルです。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーでエントロピーの見積もりを変え、冗長度が動く様子が見えます。「答えを見る」で解答が開きます。')
