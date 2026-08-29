# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">この絵では、温度が動きません。\(\tilde T=aT\) で、標準の絵の \(T\propto1/a\) とちょうど打ち消し合うからです ── <strong>宇宙は 2.7255 K のまま、永遠に冷えない</strong>。すると、1 ビットを消すのに要るエネルギー（ランダウアーの限界 \(k_BT\ln2\)）が、宇宙の全歴史を通じて一定になります。標準の絵では \(1/a\) で下がっていく量が、ここでは固定される。<em>どちらが「本当の消去コスト」なのか。</em> ── 例によって、その問いはまだ文になっていません。</p>

<h2><span class="n">01</span>温度が動かないので、値段が固定される</h2>

<div class="calc">
<span class="tag">この絵でのランダウアー限界</span>
$$\tilde T=aT=\text{一定}=2.7255\ \mathrm{K}$$
$$k_B\tilde T\ln2=2.61\times10^{-23}\ \mathrm{J}=1.63\times10^{-4}\ \mathrm{eV}\qquad(\text{永遠に不変})$$
</div>

<p>標準の絵では、この量は昔ほど大きく、\(1/a\) で下がってきました。この絵では最初から今日までずっと \(1.63\times10^{-4}\) eV。<strong>まったく同じ宇宙について、正反対のことを言っています。</strong></p>

<h2><span class="n">02</span>第3回の手術を、値段にかける</h2>

<p>\(k_BT\ln2\) はエネルギー ── <em>次元付き</em>です。判定手続きにかければ左の列、帳簿。だから「1 ビット消すのに \(1.63\times10^{-4}\) eV かかる」は、それだけでは主張になっていません。<strong>何と比べて</strong>その値段なのかを言う必要があります。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>消去コストを、何と比べるか</th><th class="mid">今日の値</th><th class="mid">時間変化</th></tr></thead>
<tbody>
<tr><th>電子の静止質量 \(m_ec^2\)</th><td class="mid">\(4.6\times10^{-10}\)</td><td class="mid">\(\propto1/t\)（<strong>安くなる</strong>）</td></tr>
<tr><th>CMB 光子 1 個のエネルギー</th><td class="mid">\(\sim1\)</td><td class="mid">一定</td></tr>
<tr><th>プランクエネルギー</th><td class="mid">\(1.9\times10^{-32}\)</td><td class="mid">時代とともに変わる</td></tr>
<tr class="hi"><th>何とも比べない</th><td class="mid">──</td><td class="mid"><strong>主張が存在しない</strong></td></tr>
</tbody>
</table>
</div>

<p>粒子の質量と比べれば、情報消去は<em>時代とともに相対的に安くなっていきます</em>。光子 1 個と比べれば、永遠に同じ。── どちらも正しい。<strong>比較相手が違うだけです。</strong></p>

<div class="aside">
<span class="tag">「共形不変」と「時間変化しない」は別</span>
プランクエネルギーとの比 \(k_BT/E_P\) は<em>共形不変</em>です（分子も分母もウェイト \(-1\)）。でも<em>時間変化はします</em>。これは第8回の練習問題5と同じ落とし穴で、シリーズを通していちばん間違えやすいところです ── <strong>ゲージで動かないことと、時間で動かないことは、別のこと</strong>。前者は「物理か帳簿か」、後者は「宇宙で何が起きているか」の話です。
</div>

<h2><span class="n">03</span>もう一つ、言わなければいけないもの</h2>

<p>ところが、比較相手を決めてもまだ足りません。ランダウアーの限界には \(T\) が入っています ── <strong>どの熱浴に捨てるのか</strong>を言わないと、値段が決まらないのです。これは共形変換とは無関係の、熱力学そのものの要求です。</p>

<p>そこで、宇宙で使える熱浴を全部並べて、同じ問いを当ててみます ── <em>宇宙の全エネルギーを使ったら、何ビット消せるか。</em></p>

<div class="calc">
<span class="tag">計算 ── 割るだけ</span>
<p class="lbl">地平面内の全エネルギー（第1回で使った恒等式）</p>
$$E=\frac{c^4R_H}{2G}=7.90\times10^{69}\ \mathrm{J}$$
<p class="lbl">消せるビット数</p>
$$N_{\rm erase}=\frac{E}{k_BT\ln2}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>どの温度で消すか</th><th class="mid">\(T\)</th><th class="mid">1 ビットの値段</th><th class="mid">消せるビット数</th><th class="mid">メモリ \(N\) との比</th></tr></thead>
<tbody>
<tr class="hi"><th>ハッブル（地平面）温度</th><td class="mid">\(2.79\times10^{-30}\) K</td><td class="mid">\(2.67\times10^{-53}\) J</td><td class="mid"><strong>\(2.96\times10^{122}\)</strong></td><td class="mid"><strong>1.0000</strong></td></tr>
<tr><th>CMB 温度</th><td class="mid">2.7255 K</td><td class="mid">\(2.61\times10^{-23}\) J</td><td class="mid">\(3.03\times10^{92}\)</td><td class="mid">\(1.0\times10^{-30}\)</td></tr>
<tr><th>室温</th><td class="mid">300 K</td><td class="mid">\(2.87\times10^{-21}\) J</td><td class="mid">\(2.75\times10^{90}\)</td><td class="mid">\(9.3\times10^{-33}\)</td></tr>
<tr><th>プランク温度</th><td class="mid">\(1.42\times10^{32}\) K</td><td class="mid">\(1.36\times10^{9}\) J</td><td class="mid">\(5.83\times10^{60}\)</td><td class="mid">\(2.0\times10^{-62}\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0">宇宙の全エネルギーを使っても、<strong>CMB 温度で消すならメモリの \(10^{-30}\) しか消せません。</strong><br>
書ける量は \(10^{122}\) ビット、消せる量は \(10^{92}\) ビット ── <em>30 桁足りない。</em></p>
</div>

<p>第1回で「宇宙は 28.5 ビットに 1 回しか演算しない」と数えました。今回はもっと極端です ── <strong>宇宙は、自分が書ける量のうち \(10^{-30}\) しか消せない</strong>。書き込み専用に近い媒体です。</p>

<div class="fig">
<p class="cap">図：横軸は「どの温度の熱浴に捨てるか」、縦軸は宇宙の全エネルギーで消せるビット数。<strong>灰色の水平線が、書けるビット数 \(N=2.96\times10^{122}\)</strong>。二本が交わるのは、ただ一点 ── <em>ハッブル温度</em>だけです</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>捨てる先の温度 \(T\)（対数）<input id="st" type="range" min="0" max="1000" value="484" step="1"></label>
  <span class="val" id="vt">2.73 K</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6b5320"></i>消せるビット数 \(E/k_BT\ln2\)</span>
  <span><i class="swatch" style="background:#9aa0a8"></i>書けるビット数 \(N\)</span>
  <span><i class="swatch" style="background:#2f5f6b"></i>目印（地平面・CMB・室温・プランク）</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>種明かし ── 「ランダウアー限界ぴったり」の正体</h2>

<p>前シリーズ番外編②に、シリーズでいちばん印象的な数字がありました ── <strong>宇宙の 1 ビットあたりのエネルギーが、ランダウアーの限界と比 1.000000 で一致する</strong>。</p>

<div class="calc">
<span class="tag">あの一致</span>
$$\frac{E}{N}=2.672\times10^{-53}\ \mathrm{J},\qquad k_BT_H\ln2=2.672\times10^{-53}\ \mathrm{J}$$
</div>

<p>表の一行目が、まさにこれです。そして今回はっきりします ── <strong>あれは恒等式でした</strong>。\(E=T_HS\) は任意の FLRW で成り立つ関係で、「宇宙が限界ぎりぎりで走っている」という<em>物理的な主張ではありません</em>。地平面のエネルギーを、地平面の温度で、地平面のエントロピーで割っただけ。</p>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0">「宇宙はランダウアー限界ぴったり」は、<strong>恒等式を読んだだけ</strong>。<br>
意味が出るのは <em>別の温度を選んだとき</em> ── そして選んだ瞬間、\(10^{-30}\) という<strong>本物の数</strong>が出ます。</p>
</div>

<p>前シリーズの判定手続きを、今度は「美しい一致」に当てたことになります。<em>恒等式は物理ではない</em> ── 番外編③でディラックの大数に対して下した判定と、まったく同じ形です。</p>

<h2><span class="n">05</span>実機と比べておく</h2>

<div class="calc">
<span class="tag">地上の計算機</span>
<p class="lbl">室温のランダウアー限界</p>
$$k_B\!\cdot\!300\,\mathrm{K}\cdot\ln2=2.87\times10^{-21}\ \mathrm{J}=0.0179\ \mathrm{eV}$$
<p class="lbl">現代の CPU の 1 演算あたり（おおよそ）</p>
$$\sim10^{-15}\ \mathrm{J}\qquad\Longrightarrow\qquad \text{限界の約 }3.5\times10^{5}\ \text{倍}$$
</div>

<p>人間の計算機は、まだ限界から 5 桁半ほど離れています。宇宙のほうは（地平面温度で測れば）ぴったり限界に乗っている ── <em>ただしそれが恒等式であることは、いま見たとおり</em>。</p>

<h2><span class="n">06</span>エントロピーそのものは、動かない</h2>

<p>最後に確認しておきます。\(S/k_B\) は<strong>ビット数</strong>、つまり無次元です。だから共形変換で一切動きません。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">ウェイト</th><th class="mid">この絵で</th></tr></thead>
<tbody>
<tr class="hi"><th>エントロピー \(S/k_B\)</th><td class="mid">\(0\)</td><td class="mid"><strong>不変</strong></td></tr>
<tr class="hi"><th>熱力学第二法則</th><td class="mid">──</td><td class="mid"><strong>そのまま</strong></td></tr>
<tr><th>温度 \(T\)</th><td class="mid">\(-1\)</td><td class="mid">\(\times a\)（この絵では一定になる）</td></tr>
<tr><th>ランダウアーのコスト \(k_BT\ln2\)</th><td class="mid">\(-1\)</td><td class="mid">\(\times a\)（同上）</td></tr>
<tr><th>ボルツマン因子 \(e^{-E/k_BT}\)</th><td class="mid">\(0\)</td><td class="mid"><strong>不変</strong></td></tr>
</tbody>
</table>
</div>

<p>第6回で数えた \(3.1\times10^{104}\) も、第4回で使った再結合の \(52.6\) も、この絵で一文字も変わりません。<strong>熱力学は、無次元で書かれている限り、まるごと無傷です。</strong></p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① ランダウアーの限界は「論理的に不可逆な操作 1 回あたり」の下限です。</strong> 可逆計算なら原理的にゼロにできます。本稿の「消せるビット数」は、すべての消去を不可逆に行った場合の見積もりであって、宇宙が実際にそう動いているという主張ではありません。</p>
<p style="margin:0 0 10px"><strong>② \(E=c^4R_H/2G\) は平坦 FLRW の恒等式です</strong>（第1回・前シリーズ番外編③）。地平面内の「全エネルギー」をこう定義するのは自然ですが、一般相対論で系のエネルギーを定義する仕方は一意ではありません ── 準局所エネルギーの定義は複数あり、値も変わります。</p>
<p style="margin:0 0 10px"><strong>③ 表の「消せるビット数」は、エネルギーを全部消去に使えると仮定した上限です。</strong> 実際にはエネルギーを取り出して熱浴に捨てる機構が要り、その効率は含めていません。桁の議論として読んでください。</p>
<p style="margin:0 0 10px"><strong>④ ハッブル温度 \(T_H=\hbar H/2\pi k_B\) をランダウアーの \(T\) に使うのは、比喩の域を出ません。</strong> これはド・ジッター地平面のギボンズ＝ホーキング温度に対応する量で、一般の FLRW でそれが熱浴として振る舞うかは自明ではありません。<em>一行目が「ぴったり」なのは恒等式のためであって、物理的な機構によるものではない</em> ── これが 04節の主眼です。</p>
<p style="margin:0"><strong>⑤ CPU の \(10^{-15}\) J/演算は桁の目安です。</strong> 演算の定義（論理ゲート 1 個か、命令 1 個か）で何桁も変わります。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>この絵でランダウアーのコストが一定になるのはなぜか。
<details><summary>答えを見る</summary><div class="ans">温度がウェイト \(-1\) なので \(\tilde T=aT\)。標準の絵では \(T\propto1/a\) なので、掛けると打ち消して \(\tilde T=\)一定。よって \(k_B\tilde T\ln2\) も一定（\(1.63\times10^{-4}\) eV）。<em>標準の絵では \(1/a\) で下がる同じ量です。</em></div></details></li>

<li>「1 ビット消すのに \(1.63\times10^{-4}\) eV」は、それだけで主張になっているか。
<details><summary>答えを見る</summary><div class="ans">なっていません。エネルギーは次元付き＝帳簿なので、<strong>何と比べるか</strong>を言わないと意味が出ない。電子質量と比べれば \(4.6\times10^{-10}\) で時代とともに安くなり、CMB 光子 1 個と比べれば一定。第3回でシリーズの題名に当てた手術と、同じです。</div></details></li>

<li>宇宙の全エネルギーで、CMB 温度なら何ビット消せるか。メモリと比べよ。
<details><summary>答えを見る</summary><div class="ans">\(E/(k_BT_0\ln2)=7.90\times10^{69}/2.61\times10^{-23}=3.03\times10^{92}\) ビット。メモリ \(2.96\times10^{122}\) の <strong>\(10^{-30}\)</strong>。<em>書ける量の 10 億分の 1 の 10 億分の 1 の 10 億分の 1 しか消せません。</em></div></details></li>

<li>「宇宙はランダウアー限界ぴったりで走っている」は、物理的な主張か。
<details><summary>答えを見る</summary><div class="ans">いいえ、<strong>恒等式</strong>です。\(E=T_HS\) は任意の FLRW で成り立つので、\(E/N=k_BT_H\ln2\) は自動的に 1.000000 になります。<em>意味が出るのは別の温度を選んだとき</em>で、CMB 温度なら \(10^{-30}\) という本物の数が出ます。前シリーズ番外編③がディラックの大数に下した判定（恒等式は物理ではない）と、同じ形です。</div></details></li>

<li>（やや難）エントロピーは共形変換で不変なのに、温度は動く。矛盾しないか。
<details><summary>答えを見る</summary><div class="ans">しません。\(S/k_B\) は<strong>ビット数＝無次元</strong>なので動きようがなく、\(T\) は<strong>エネルギー＝次元付き</strong>なので動く。両方が同時に成り立ちます。実際 \(E=TS\) の左辺 \(E\) もウェイト \(-1\) なので、\(T\)（\(-1\)）\(\times S\)（\(0\)）でつじつまが合っています。<em>エントロピーが情報の量だという事実そのものが、それを帳簿から守っています。</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　値段は、温度を言うまで決まらない</h2>
<p>この絵では温度が動きません（\(\tilde T=aT=\)一定 \(=2.7255\) K）。だからランダウアーの限界 \(k_BT\ln2=1.63\times10^{-4}\) eV が、宇宙の全歴史を通じて<strong>一定</strong>になります ── 標準の絵では \(1/a\) で下がっていく、同じ量です。どちらが本当か、という問いは<em>まだ文になっていません</em>。エネルギーは次元付きなので、比較相手を言うまで主張が立たない。電子質量と比べれば時代とともに安くなり、CMB 光子 1 個と比べれば永遠に同じ。</p>
<p>そして今回は、比較相手のほかにもう一つ言うべきものがありました ── <strong>どの熱浴に捨てるか</strong>。宇宙の全エネルギー \(E=7.90\times10^{69}\) J で何ビット消せるかを温度ごとに数えると、ハッブル温度で \(2.96\times10^{122}\)、CMB 温度で \(3.03\times10^{92}\)、室温で \(2.75\times10^{90}\)、プランク温度で \(5.83\times10^{60}\)。<em>選ぶ温度で 60 桁動きます。</em></p>
<p>いちばん効くのは二行目です ── <strong>CMB 温度で消すなら、宇宙は自分が書ける量の \(10^{-30}\) しか消せません。</strong> 書ける \(10^{122}\)、消せる \(10^{92}\)。第1回の「28.5 ビットに 1 回しか演算しない」より、はるかに極端な非対称です。<em>宇宙は、ほとんど書き込み専用の媒体だった。</em></p>
<p>そして種明かし。前シリーズ番外編②のいちばん印象的な数字「1 ビットあたりのエネルギーがランダウアー限界と比 1.000000 で一致」は、表の一行目そのもので ── <strong>恒等式でした</strong>。\(E=T_HS\) は任意の FLRW で成り立つので、地平面温度で測れば必ずぴったりになる。<em>意味が出るのは、別の温度を選んだときだけ。</em> 恒等式は物理ではない ── ディラックの大数（第7回）に下したのと、同じ判定です。エントロピーそのものは無次元なので、この絵でも一切動きません。熱力学は、無次元で書かれている限り、まるごと無傷です。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第11回</span>
次は<strong>光</strong>です。ここまで「光は共形変換を素通りする」と何度も書いてきましたが、正面から扱ったことはありませんでした。この絵で光子ガスを見ると ── <em>数密度も、エネルギー密度も、温度も、全部が一定</em>。<strong>完全に静止しています。</strong> 宇宙の歴史を通じて、光には何も起きていない。育っているのは物質のほうだけ。4 次元のマクスウェル作用が \(\Omega^{D-4}\) でぴったり共形不変になるという前シリーズ第7回の結果が、いちばん露骨な形で見えます。そして赤方偏移が「光が伸びた」のではなく「<strong>受け取る側が育った</strong>」に完全に置き換わる瞬間を、数字で見ます。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var st=document.getElementById('st'), vt=document.getElementById('vt'), ro=document.getElementById('ro');
  var X0=78, X1=700, Y0=30, Y1=318;
  var kB=1.380649e-23, ln2=Math.log(2);
  var E=7.8980e69, N=2.9556e122;
  var xmin=-31, xmax=33;      // log10(T/K)
  var ymin=55, ymax=126;      // log10(消せるビット数)
  var MARKS=[[-29.554,'地平面'],[0.435,'CMB'],[2.477,'室温'],[32.151,'プランク']];

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function lg(v){ return Math.log(v)/Math.LN10; }

  function draw(){
    var f=parseInt(st.value,10)/1000;
    var T=Math.pow(10, xmin+ (xmax-xmin)*f);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right';
    for(var e=60;e<=125;e+=10){
      var y=py(e);
      g.strokeStyle='#f2efe6'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a49a86'; g.fillText('10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-30;q<=30;q+=10){
      var x=px(q);
      g.strokeStyle='#f8f6f1'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a49a86'; g.fillText('10'+q, x, Y1+16);
    }
    g.strokeStyle='#cdc6b5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // 書けるビット数
    g.strokeStyle='#9aa0a8'; g.lineWidth=2.4; g.setLineDash([7,5]);
    g.beginPath(); g.moveTo(X0,py(lg(N))); g.lineTo(X1,py(lg(N))); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#7f858c'; g.textAlign='right';
    g.fillText('書けるビット数 N = 2.96×10¹²²', X1-8, py(lg(N))-8);

    // 消せるビット数（傾き -1）
    g.strokeStyle='#6b5320'; g.lineWidth=3.4; g.beginPath();
    var first=true;
    for(var i=0;i<=300;i++){
      var lx=xmin+(xmax-xmin)*i/300;
      var y=lg(E/(kB*Math.pow(10,lx)*ln2));
      if(y<ymin||y>ymax){ first=true; continue; }
      if(first){ g.moveTo(px(lx),py(y)); first=false; } else g.lineTo(px(lx),py(y));
    }
    g.stroke();

    // 目印
    MARKS.forEach(function(m){
      var y=lg(E/(kB*Math.pow(10,m[0])*ln2));
      if(y<ymin||y>ymax) return;
      g.fillStyle='#2f5f6b';
      g.beginPath(); g.arc(px(m[0]),py(y),4.5,0,6.2832); g.fill();
      g.fillStyle='#2f5f6b'; g.textAlign='left';
      g.fillText(m[1], px(m[0])+8, py(y)-7);
    });

    // カーソル
    var yc=lg(E/(kB*T*ln2));
    g.strokeStyle='#6b5320'; g.lineWidth=1.5; g.setLineDash([3,3]);
    g.beginPath(); g.moveTo(px(lg(T)),Y0); g.lineTo(px(lg(T)),Y1); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#8a8272'; g.textAlign='center';
    g.fillText('捨てる先の温度  T [K]', (X0+X1)/2, Y1+36);

    var nb=E/(kB*T*ln2);
    vt.textContent = (T<1e-3||T>1e5) ? T.toExponential(2)+' K' : T.toPrecision(3)+' K';
    ro.textContent='T = '+vt.textContent+
      '　1ビットの値段 '+(kB*T*ln2).toExponential(2)+' J'+
      '　→　消せるビット数 '+nb.toExponential(3)+
      '　／　書ける量の '+(nb/N).toExponential(2)+' 倍'+
      (Math.abs(nb/N-1)<0.02 ? '　★ ちょうど一致（恒等式）' : '');
  }
  st.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-10-erase.html', acc='#6b5320', ops='#2f5f6b',
      title='熱と情報に入れてみる ── わかる c·t=一定 第10回',
      ep='第 10 回 ／ 冷えない宇宙で、1ビット消すといくらか',
      eyebrow='「ランダウアー限界ぴったり」は、恒等式を読んだだけでした',
      h1='熱と情報に、<br>入れてみる',
      sub='この絵では温度が動きません ── 宇宙は 2.7255 K のまま永遠に冷えない。<br>すると1ビットの消去コストが固定されます。<em>では、それは高いのか安いのか。</em>',
      byline_l='必要な道具：割り算、ランダウアーの限界',
      byline_r='書ける \\(10^{122}\\)、消せる \\(10^{92}\\)',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第10回、物理好きの高校生・大学生向け読み物です。ランダウアーの原理（論理的に不可逆な 1 ビットの消去に少なくとも \\(k_BT\\ln2\\) の散逸が伴う）、エントロピーが無次元量であること、および共形変換のもとで温度がウェイト \\(-1\\) であることは、いずれも標準的です。可逆計算では消去コストを原理的にゼロにできます ── 本稿の「消せるビット数」はすべての操作を不可逆と仮定した上限であり、宇宙が実際にそう動いているという主張ではありません。\\(E=c^4R_H/2G\\) は平坦 FLRW の恒等式で（前シリーズ番外編③）、一般相対論における準局所エネルギーの定義は一意ではありません。ハッブル温度 \\(T_H=\\hbar H/2\\pi k_B\\) はド・ジッター地平面の Gibbons–Hawking 温度に対応する量で、一般の FLRW でそれが熱浴として振る舞うかは自明ではなく、本稿の一行目の「ぴったり一致」は \\(E=T_HS\\) という恒等式の帰結であって物理的機構によるものではありません（これが 04節の主眼です）。表の数値（\\(k_BT_0\\ln2=2.61\\times10^{-23}\\) J \\(=1.63\\times10^{-4}\\) eV、\\(E=7.90\\times10^{69}\\) J、消せるビット数 \\(2.96\\times10^{122}\\)／\\(3.03\\times10^{92}\\)／\\(2.75\\times10^{90}\\)／\\(5.83\\times10^{60}\\)、CMB 温度でメモリの \\(1.0\\times10^{-30}\\)）は本稿での計算です。エネルギー取り出しと排熱の機構・効率は含めていません。CPU の \\(10^{-15}\\) J/演算 は桁の目安で、演算の定義により何桁も変わります。前シリーズ番外編②の「1 ビットあたりのエネルギーがランダウアー限界と比 1.0000 で一致」は同所でも恒等式と明記されています。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルで、初期宇宙まで外挿した場合は元素合成と矛盾します（Lewis, Barnes &amp; Kaushik 2016）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで捨てる先の温度を変え、二本が交わるのが地平面温度だけであることが見えます。「答えを見る」で解答が開きます。')
