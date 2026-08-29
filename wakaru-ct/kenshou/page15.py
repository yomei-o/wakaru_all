# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第 II 部の最後は、いちばん遠いところへ行きます ── <strong>化学と生物</strong>。結合エネルギー ÷ \(k_BT\)、アレニウス因子、pH、クライバー則の指数、一生の心拍数、DNA の情報量。<em>ひとつ残らず無次元</em>なので、この絵で一文字も変わりません。そこから出る結論はかなり強いものです ── <strong>生命は、宇宙が「膨張している」のか「質量が育っている」のかを、原理的に知ることができない。</strong></p>

<h2><span class="n">01</span>化学は、まるごと無傷</h2>

<p>化学反応の起きやすさを決めるのは、アレニウス因子です。</p>

<div class="calc">
<span class="tag">指数の中身は、無次元</span>
$$k\ \propto\ \exp\!\left(-\frac{E_a}{k_BT}\right)$$
<p class="lbl">\(E_a\) も \(k_BT\) もウェイト \(-1\) なので、比は不変</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>化学の量</th><th class="mid">中身</th><th class="mid">この絵で</th></tr></thead>
<tbody>
<tr class="hi"><th>アレニウス因子</th><td class="mid">\(e^{-E_a/k_BT}\)</td><td class="mid"><strong>不変</strong></td></tr>
<tr><th>平衡定数</th><td class="mid">\(e^{-\Delta G/RT}\)</td><td class="mid"><strong>不変</strong></td></tr>
<tr><th>pH</th><td class="mid">濃度の比の対数</td><td class="mid"><strong>不変</strong></td></tr>
<tr><th>結合エネルギー ÷ 熱エネルギー</th><td class="mid">\(E_b/k_BT\)</td><td class="mid"><strong>不変</strong></td></tr>
<tr><th>反応速度どうしの比</th><td class="mid">──</td><td class="mid"><strong>不変</strong></td></tr>
</tbody>
</table>
</div>

<p>第8回でトンネル透過率が不変だったのと、まったく同じ理由です ── <em>指数の中身が無次元だから</em>。だから太陽が燃える速さも、酵素反応の速さも、この絵で一切変わりません。</p>

<h2><span class="n">02</span>クライバー則を、分解してみる</h2>

<p>生物学でいちばん有名なスケーリング則です ── <strong>代謝率は体重の 3/4 乗に比例する</strong>。ネズミからゾウまで、6 桁にわたって成り立ちます。</p>

<div class="calc">
<span class="tag">計算 ── 部品ごとのウェイト</span>
<p class="lbl">代謝率 \(B\)（エネルギー／時間 ＝ \(ML^2/T^3\)）</p>
$$w(B)=-1+2\cdot1-3\cdot1\cdot(-1)\ \Longrightarrow\ w=-2\qquad(\times a^2)$$
<p class="lbl">体重 \(M\)</p>
$$w(M)=-1\qquad(\times a)$$
<p class="lbl">\(B=CM^{3/4}\) が形を保つには</p>
$$w(C)=-2-\tfrac34(-1)=-\tfrac54\qquad(\times a^{5/4})$$
</div>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0"><strong>指数 3/4 は不変。係数 \(C\) は \(\times a^{5/4}\) で動きます。</strong><br>
係数は次元付き ── つまり帳簿。<em>ゲージ不変な言い方は「二匹の代謝率の比 ＝（体重比）\(^{3/4}\)」</em>で、これは比どうしなので動きません。</p>
</div>

<p>第3回でシリーズの題名に、第9回で原子に、第12回で宇宙定数にやった手術が、ここでも同じ形で当たります ── <strong>「代謝率は体重の 3/4 乗」の 3/4 は物理、係数は帳簿。</strong></p>

<h2><span class="n">03</span>一生の心拍数は、無次元だった</h2>

<p>クライバー則からもう一つ、有名な帰結が出ます。</p>

<div class="calc">
<span class="tag">掛けると、体重が消える</span>
$$\text{心拍数}\ \propto M^{-1/4},\qquad \text{寿命}\ \propto M^{+1/4}$$
<p class="lbl">積は</p>
$$\text{一生の心拍数}\ \propto M^{0}\ \simeq\ 1.5\times10^{9}\ \text{回}$$
</div>

<p>ネズミもゾウも、一生におよそ 15 億回。<strong>体重に依らない ── つまり無次元</strong>です。だからこの絵でも、まったく同じ 15 億回。</p>

<div class="aside">
<span class="tag">生きている時間は、何で測るか</span>
この絵では、寿命（時間）はウェイト \(+1\) なので \(\div a\) で縮みます。ネズミもゾウも、時代とともに<em>短命になっていく</em>。ところが心拍数も同じだけ速くなるので、<strong>一生の拍数は変わらない</strong>。<em>生きている長さを「秒」で測れば縮み、「心拍」で測れば不変</em> ── 第9回の「ボーア半径は縮むが比べる相手がいない」と、同じ構図です。
</div>

<h2><span class="n">04</span>生命が測れるものを、全部並べる</h2>

<div class="fig">
<p class="cap">図：上段は<strong>次元付きの量</strong>（体重・体長・代謝率・寿命）── ツマミで時代を遡ると、めちゃくちゃに動きます。下段は<strong>生命が実際に測れる量</strong> ── <em>一本残らず、1 に貼りついたまま</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>いつの時代で見るか \(\log_{10}a\)（右端が今日）<input id="sa" type="range" min="-2000" max="0" value="-700" step="1"></label>
  <span class="val" id="va">a = 0.200</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6b4a7a"></i>次元付きの量（動く）</span>
  <span><i class="swatch" style="background:#a06020"></i>生命が測れる量（動かない）</span>
</div>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>生命が測れるもの</th><th class="mid">中身</th><th class="mid">この絵で</th></tr></thead>
<tbody>
<tr><th>濃度の比</th><td class="mid">個数 ÷ 個数</td><td class="mid">不変</td></tr>
<tr><th>反応速度の比</th><td class="mid">時間 ÷ 時間</td><td class="mid">不変</td></tr>
<tr class="hi"><th>一生の心拍数</th><td class="mid">回数</td><td class="mid"><strong>不変（\(1.5\times10^9\)）</strong></td></tr>
<tr><th>世代数</th><td class="mid">回数</td><td class="mid">不変</td></tr>
<tr class="hi"><th>遺伝情報</th><td class="mid">ビット</td><td class="mid"><strong>不変（\(6.2\times10^9\) bit ＝ 775 MB）</strong></td></tr>
<tr><th>体長 ÷ 細胞の大きさ</th><td class="mid">長さ ÷ 長さ</td><td class="mid">不変</td></tr>
<tr><th>代謝率の比</th><td class="mid">──</td><td class="mid">不変</td></tr>
<tr><th>温度差 ÷ 温度</th><td class="mid">──</td><td class="mid">不変</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>生命が測れるものは、ひとつ残らず無次元です。</strong><br>
だから生命は、宇宙が「膨張している」のか「質量が育っている」のかを、<br>
<em>原理的に知ることができない。</em></p>
</div>

<p>第9回で「原子は比較相手を持たない」と書きました。今回はそれを<strong>生物のスケールまで押し上げた</strong>ことになります。細胞も、心臓も、遺伝子も、比較相手を原子に置いている限り、絵の違いに気づけません。</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">05</span>おまけ ── 二つの「歩数」</h2>

<p>このシリーズは、無次元の「回数」をいくつも数えてきました。並べてみます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>何の歩数か</th><th class="mid">回数</th><th class="mid">出どころ</th></tr></thead>
<tbody>
<tr><th>宇宙の対数クロック</th><td class="mid">140.2</td><td class="mid">第2回</td></tr>
<tr><th>宇宙のプランクティック</th><td class="mid">\(8.08\times10^{60}\)</td><td class="mid">第1回</td></tr>
<tr class="hi"><th>人間の一生の心拍</th><td class="mid">\(1.5\times10^{9}\)</td><td class="mid">今回</td></tr>
<tr><th>ヒトゲノムの情報</th><td class="mid">\(6.2\times10^{9}\) bit</td><td class="mid">今回</td></tr>
<tr><th>宇宙のメモリ</th><td class="mid">\(2.96\times10^{122}\) bit</td><td class="mid">第1回</td></tr>
</tbody>
</table>
</div>

<p>面白いのは三行目です ── <strong>宇宙は 140 手しか指していないのに、人間は一生に 15 億回、心臓を打つ</strong>。もちろん数え方の単位が違います（片方は倍々の回数、もう片方は拍の回数）。それでも、<em>どちらも無次元で、どちらも絵の取り替えでは動かない</em>ことに変わりはありません。</p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① クライバー則の指数 3/4 には論争があります。</strong> 2/3（表面積則）を支持する解析もあり、分類群や体重域によって実効的な指数は変わります。本稿が使っているのは「<em>指数が何であれ、それは無次元なので不変</em>」という点だけで、3/4 という値そのものを主張してはいません。</p>
<p style="margin:0 0 10px"><strong>② 「一生の心拍 \(1.5\times10^9\) 回」は哺乳類の大まかな目安です。</strong> 実際には種によって数倍のばらつきがあり、ヒトは（医療のおかげもあって）この値より大きい側にいます。ここで効いているのは<em>「体重に依らない＝無次元」という構造</em>であって、数値の精度ではありません。</p>
<p style="margin:0 0 10px"><strong>③ 化学・生物の量が「一緒に変換される」ことを前提にしています。</strong> 第8回①・第13回①と同じ注意で、実験室で固定された条件（決まった温度の恒温槽など）を置くと話が変わります ── 本稿が扱うのは<em>宇宙全体をまとめて書き換える</em>操作です。</p>
<p style="margin:0 0 10px"><strong>④ 「生命は原理的に知ることができない」は、本シリーズの判定手続きの帰結です。</strong> より正確には「<em>無次元量だけを測る限り、区別できない</em>」── これは生命に固有の制限ではなく、あらゆる観測者に等しくかかる制限です（前シリーズ最終回）。</p>
<p style="margin:0"><strong>⑤ ヒトゲノム 3.1×10⁹ 塩基対 × 2 bit は、配列を素朴に符号化した場合の上限です。</strong> 実際の情報量（圧縮後、あるいは機能的に意味のある量）はこれより小さく、その見積もりには議論があります。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>アレニウス因子がこの絵で不変なのはなぜか。
<details><summary>答えを見る</summary><div class="ans">指数の中身 \(E_a/k_BT\) が、エネルギー ÷ エネルギー ＝ 無次元だから。<em>第8回のトンネル透過率とまったく同じ理由</em>で、化学反応の起きやすさは一切変わりません。</div></details></li>

<li>代謝率 \(B\)（次元 \(ML^2/T^3\)）のウェイトを求めよ。
<details><summary>答えを見る</summary><div class="ans">\(M\) が \(-1\)、\(L^2\) が \(+2\)、\(T^{-3}\) が \(-3\) なので、\(-1+2-3=-2\)。よって \(\tilde B=a^2B\)。<em>この絵では、昔の生き物ほど代謝が遅い</em>ことになります ── ただし比べる相手も同じだけ遅い。</div></details></li>

<li>クライバー則 \(B=CM^{3/4}\) で、係数 \(C\) はどう動くか。
<details><summary>答えを見る</summary><div class="ans">\(w(C)=w(B)-\tfrac34w(M)=-2-\tfrac34(-1)=-\tfrac54\)、つまり \(\times a^{5/4}\)。<strong>指数 3/4 は不変、係数は動く</strong> ── 次元付きだから帳簿です。ゲージ不変な言い方は「二匹の代謝率の比 ＝（体重比）\(^{3/4}\)」。</div></details></li>

<li>一生の心拍数が体重に依らないことを示し、この絵でどうなるか答えよ。
<details><summary>答えを見る</summary><div class="ans">心拍数 \(\propto M^{-1/4}\)、寿命 \(\propto M^{+1/4}\) なので、積は \(M^0\)。<strong>体重に依らない＝無次元</strong>なので、この絵でも同じ \(1.5\times10^9\) 回。<em>寿命は \(\div a\) で縮み、心拍数も同じだけ速くなるので、拍数は変わりません。</em></div></details></li>

<li>（やや難）「生命は絵の違いを知ることができない」は、生命に固有の制限か。
<details><summary>答えを見る</summary><div class="ans">いいえ。<strong>あらゆる観測者に等しくかかる制限</strong>です ── 測れるのは無次元量だけ、というのは前シリーズ最終回の判定手続きそのもの。生物を出したのは、<em>細胞や心臓や遺伝子という、宇宙論からいちばん遠いものでも同じ結論になる</em>ことを見るためです。第9回（原子）を、生物のスケールまで押し上げた形になります。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　生命は、どちらの絵にいるか知りようがない</h2>
<p>化学はまるごと無傷でした ── アレニウス因子、平衡定数、pH、結合エネルギー ÷ \(k_BT\)。<em>指数の中身が無次元</em>なので、反応の起きやすさは一切変わりません（第8回のトンネル効果と同じ理由）。</p>
<p>生物では、クライバー則を分解しました。代謝率のウェイトは \(-2\)（\(\times a^2\)）、体重は \(-1\)（\(\times a\)）。だから \(B=CM^{3/4}\) の<strong>係数は \(\times a^{5/4}\) で動き、指数 3/4 は不変</strong>。ゲージ不変な言い方は「二匹の代謝率の比 ＝（体重比）\(^{3/4}\)」── 第3回・第9回・第12回とまったく同じ手術です。</p>
<p>そして一生の心拍数。心拍数 \(\propto M^{-1/4}\)、寿命 \(\propto M^{1/4}\) なので積は \(M^0\)、<strong>体重に依らないおよそ 15 億回</strong>。無次元なので、この絵でも同じ値です。<em>生きている長さを「秒」で測れば縮み、「心拍」で測れば不変</em> ── 第9回のボーア半径と、同じ構図でした。</p>
<p>生命が測れるものを全部並べると ── 濃度比、反応速度の比、心拍数、世代数、遺伝情報のビット、体長 ÷ 細胞の大きさ、代謝率の比、温度差 ÷ 温度。<strong>ひとつ残らず無次元</strong>です。だから<em>生命は、宇宙が「膨張している」のか「質量が育っている」のかを、原理的に知ることができない</em>。第9回の「原子は比較相手を持たない」を、生物のスケールまで押し上げたことになります。おまけに ── 宇宙は 140 手しか指していないのに、人間は一生に 15 億回、心臓を打っています。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第16回（第 II 部・最終回）</span>
第 II 部の 10 本を、一枚の表に畳みます。重力・量子力学・原子・熱・光・真空・流体・相転移・化学生物 ── どこに入れても、<strong>動いたのはいつも一つだけ</strong>でした。そして動かなかったものを全部並べると、それがそのまま<em>「物理とは何か」の一覧</em>になります。最後に、この記法が<strong>本当に役に立つ場所</strong>と<strong>まったく無力な場所</strong>を、はっきり線引きします ── 答えは第13回で半分出ていました。<em>次元付きの量が主役の場所だけ。</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sa=document.getElementById('sa'), va=document.getElementById('va'), ro=document.getElementById('ro');
  var X0=88, X1=690;
  var TOP=[['体重 M',-1],['体長 L',1],['代謝率 B',-2],['寿命 τ',1]];
  var BOT=['一生の心拍数','遺伝情報（bit）','代謝率の比','pH・濃度比'];

  function draw(){
    var la=parseInt(sa.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);

    var Y1=118, Y2=300;      // 上段・下段のゼロ線
    var scale=Math.min(52, 96/Math.max(2*Math.abs(la),1));

    ['上段：次元付きの量（この絵で動く）','下段：生命が実際に測れる量（動かない）'].forEach(function(t,i){
      g.font='bold 12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillStyle=(i===0?'#6b4a7a':'#a06020'); g.textAlign='left';
      g.fillText(t, X0-8, (i===0?Y1-92:Y2-64));
    });
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    [[Y1,'#e2d6e8'],[Y2,'#efe0cf']].forEach(function(q){
      g.strokeStyle=q[1]; g.lineWidth=1.6;
      g.beginPath(); g.moveTo(X0-8,q[0]); g.lineTo(X1,q[0]); g.stroke();
      g.fillStyle='#a08fa8'; g.textAlign='right';
      g.fillText('×1', X0-14, q[0]+4);
    });

    var n=4, w=88, gap=(X1-X0-n*w)/(n+1);
    // 上段
    for(var i=0;i<n;i++){
      var ex=-TOP[i][1]*la;
      var x=X0+gap+(w+gap)*i, h=ex*scale;
      g.fillStyle='#6b4a7a'; g.globalAlpha=0.85;
      g.fillRect(x, h>=0? Y1-h : Y1, w, Math.abs(h));
      g.globalAlpha=1;
      g.fillStyle='#4a3255'; g.textAlign='center';
      g.fillText(TOP[i][0], x+w/2, Y1+20);
      g.fillStyle='#7d6a88';
      g.fillText('×10'+(ex>=0?'+':'')+ex.toFixed(1), x+w/2, Y1+36);
    }
    // 下段（全部ゼロ）
    for(var i=0;i<n;i++){
      var x=X0+gap+(w+gap)*i;
      g.fillStyle='#a06020'; g.globalAlpha=0.9;
      g.fillRect(x, Y2-3, w, 6);
      g.globalAlpha=1;
      g.fillStyle='#6d4416'; g.textAlign='center';
      g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillText(BOT[i], x+w/2, Y2+22);
      g.fillStyle='#9a7a52';
      g.fillText('×1.000', x+w/2, Y2+38);
    }

    var a=Math.pow(10,la);
    va.textContent='a = '+(a<0.01? a.toExponential(2) : a.toFixed(3));
    ro.textContent='a = '+va.textContent+'（z = '+(1/a-1).toPrecision(3)+'）　'+
      '体重 ×10'+(la>=0?'+':'')+(la).toFixed(1)+'　'+
      '体長 ×10'+(-la>=0?'+':'')+(-la).toFixed(1)+'　'+
      '代謝率 ×10'+(2*la>=0?'+':'')+(2*la).toFixed(1)+'　'+
      '寿命 ×10'+(-la>=0?'+':'')+(-la).toFixed(1)+
      '　→　生命が測れる量は、すべて ×1.000 のまま';
  }
  sa.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-15-life.html', acc='#6b4a7a', ops='#a06020',
      title='化学と生物に入れてみる ── わかる c·t=一定 第15回',
      ep='第 15 回 ／ 第 II 部・いちばん遠いところへ',
      eyebrow='生命が測れるものは、ひとつ残らず無次元でした',
      h1='化学と生物に、<br>入れてみる',
      sub='アレニウス因子も、クライバー則の指数も、一生の心拍数も、DNA の情報量も不変。<br><em>だから生命は、自分がどちらの絵にいるか知りようがない。</em>',
      byline_l='必要な道具：ウェイトの足し算、指数の読み方',
      byline_r='一生の心拍 \\(1.5\\times10^9\\) 回 ── 体重に依らない',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第15回、物理好きの高校生・大学生向け読み物です。共形変換のもとで無次元量が不変であること、および次元の分解からウェイトが決まることは標準的です（第13回）。本稿の代謝率のウェイト \\(-2\\)、クライバー則の係数のウェイト \\(-5/4\\) は本稿での計算です（kenshou/calc20.py）。<strong>クライバー則の指数 3/4 には論争があり</strong>、2/3（表面積則）を支持する解析もあり、分類群や体重域で実効的な指数は変わります ── 本稿が使っているのは「指数が何であれ無次元なので不変」という点だけです。「一生の心拍 \\(1.5\\times10^9\\) 回」は哺乳類の大まかな目安で、種による数倍のばらつきがあり、ヒトはこの値より大きい側にいます ── 効いているのは<em>体重に依らない＝無次元</em>という構造であって、数値の精度ではありません。ヒトゲノム \\(3.1\\times10^9\\) 塩基対 × 2 bit \\(=6.2\\times10^9\\) bit は素朴な符号化での上限で、実際の情報量（圧縮後・機能的な量）はこれより小さく、その見積もりには議論があります。化学・生物の量が一緒に変換されることを前提にしており、実験室で固定された条件には適用されません（第8回①・第13回①と同じ注意）。「生命は原理的に知ることができない」はより正確には「無次元量だけを測る限り区別できない」であり、生命に固有の制限ではなく、あらゆる観測者に等しくかかる制限です（前シリーズ最終回）。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルで、初期宇宙まで外挿した場合は元素合成と矛盾します（Lewis, Barnes &amp; Kaushik 2016）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで時代を変え、上段だけが動く様子が見えます。「答えを見る」で解答が開きます。')
