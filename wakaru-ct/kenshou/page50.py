# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">最終回です。50 回でやってきたことを、<em>一つの文</em>にまとめます ── 六つの部、九つの理論、八つの壊れる場所、16 の開いた扉、四度の圧縮。<strong>それらが全部、第3回で作った一つの手続きの帰結だったこと</strong>を、最後にもう一度だけ確かめます。そして題の意味を書きます ── <em>動くのは、一つだけだった。</em></p>

<h2><span class="n">01</span>六つの部を、一行ずつ</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">部</th><th class="mid">回</th><th>結論</th></tr></thead>
<tbody>
<tr><th class="mid">第 I 部</th><td class="mid">1〜9</td><td>\(c\cdot t=\)一定 は記法であって、モデルではない</td></tr>
<tr><th class="mid">第 II 部</th><td class="mid">10〜16</td><td>どこに入れても、動くのは一つだけ。触れるのは大きさだけ</td></tr>
<tr><th class="mid">第 III 部</th><td class="mid">17〜26</td><td>情報として測ると、同じ数を八つの言語で言い直していた</td></tr>
<tr><th class="mid">第 IV 部</th><td class="mid">27〜36</td><td>同じ手術を他の理論に当てると、良い理論は最初から済ませてあった</td></tr>
<tr><th class="mid">第 V 部</th><td class="mid">37〜45</td><td>道具が触れるのは世界のちょうど半分。残りの半分に時間の矢がある</td></tr>
<tr class="hi"><th class="mid">第 VI 部</th><td class="mid">46〜50</td><td><strong>手続きそのものを検査した ── 扉には四種類しかなかった</strong></td></tr>
</tbody>
</table>
</div>

<h2><span class="n">02</span>50 回で、何をやったか</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>項目</th><th class="mid">数</th><th class="mid">備考</th></tr></thead>
<tbody>
<tr><th>部</th><td class="mid">\(6\)</td><td class="mid"></td></tr>
<tr><th>回</th><td class="mid">\(50\)</td><td class="mid">日本語・英語の両方</td></tr>
<tr class="hi"><th>検証スクリプト（\(\texttt{calcNN.py}\)）</th><td class="mid"><strong>\(53\)</strong></td><td class="mid"><strong>すべての数字はここで計算した</strong></td></tr>
<tr><th>正面から扱った理論</th><td class="mid">\(9\)</td><td class="mid">第 IV 部</td></tr>
<tr><th>道具が壊れた／届かなかった場所</th><td class="mid">\(8\)</td><td class="mid">第 V 部</td></tr>
<tr><th>開いたままの扉</th><td class="mid">\(16\)</td><td class="mid">第49回</td></tr>
<tr class="hi"><th>圧縮に成功した回数</th><td class="mid"><strong>\(4\)</strong></td><td class="mid">第26・40・41・46回</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">03</span>四度の圧縮を、並べる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">回</th><th class="mid">入り</th><th class="mid">出</th><th>何に圧縮されたか</th></tr></thead>
<tbody>
<tr><th class="mid">26</th><td class="mid">24 の見出しの数字</td><td class="mid">\(12\)</td><td>独立な入力</td></tr>
<tr><th class="mid">40</th><td class="mid">三つの \(10^{122}\)</td><td class="mid">\(1\)</td><td>同じ数（ハッブル球 ＝ 自分の \(r_s\)）</td></tr>
<tr class="hi"><th class="mid">41</th><td class="mid">四つの \(10^{122}\)</td><td class="mid">\(1\)</td><td><strong>ペンローズの \(10^{10^{123}}\) も同じ数</strong></td></tr>
<tr><th class="mid">46</th><td class="mid">12 の \(a\propto t\) の言い方</td><td class="mid">\(3\)</td><td>膨張則・力学・幾何</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">03節の結論</p>
<p style="margin:6px 0 0"><strong>四度とも、同じことが起きました ── 別々に見えた数が、一つだった。</strong><br>
そして毎回、第19回の分類では <strong>0 ビット（恒等式）</strong>。<br>
── <em>驚くべきことが起きていたのではなく、同じことを別の言葉で言っていたのです。</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>核心 ── 道具は、いくつあったか</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">初出</th><th>道具</th><th class="mid">由来</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">3</th><td><strong>次元付きは帳簿、無次元が物理</strong></td><td class="mid">判定の手続き</td></tr>
<tr><th class="mid">5</th><td>記述長の天秤（パラメータの値段と当てはまり）</td><td class="mid">ビットで測る</td></tr>
<tr><th class="mid">16</th><td>共形ウェイトの地図</td><td class="mid">第3回の道具化</td></tr>
<tr><th class="mid">19</th><td>驚きの目盛り（\(-\log_2\) の作法）</td><td class="mid">ビットで測る</td></tr>
<tr><th class="mid">24</th><td>チャンネル容量（情報を数える）</td><td class="mid">ビットで測る</td></tr>
<tr><th class="mid">33</th><td>リーマン／ワイルの三段判定</td><td class="mid">幾何の道具化</td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">この 6 個を、自分の手続きで圧縮する</span>
$$\underbrace{6\ \text{の道具}}_{\text{第16・33回は第3回の適用、第5・19・24回は「ビットで測る」}}\;\longrightarrow\;\underbrace{2\ \text{の考え}}_{\text{圧縮 3.0 倍}}$$
</div>

<div class="seven">
<div class="row"><div class="mk">i</div><div class="txt"><strong>次元付きと無次元を分けること</strong><span>第3回 ── 判定の手続き</span></div></div>
<div class="row"><div class="mk">ii</div><div class="txt"><strong>全部をビットで測ること</strong><span>第5・19・24回 ── 検査の仕方</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>そしてもう一段：(ii) は (i) を検査するための道具だった</strong><span>第47回で SI が (i) を宣言し、第48回で (ii) が「美しさ」を分解し、第49回で (ii) が扉を四種類に分けた</span></div></div>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>50 回でやったのは、一つの考えと、その検査の仕方でした。</strong></p>
</div>

<div class="fig">
<p class="cap">図：50 回でやったことを、圧縮していったもの。<strong>50 の回 → 6 の道具 → 2 の考え → 1 つ</strong>。ツマミで圧縮の段階を進めてください ── <em>四度やった圧縮を、最後にシリーズ自身に当てています</em></p>
<canvas id="cv" width="720" height="340"></canvas>
<div class="controls">
  <label>圧縮の段階<input id="sc" type="range" min="0" max="3" value="0" step="1"></label>
  <span class="val" id="vc">0</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a3a5a"></i>残っているもの</span>
  <span><i class="swatch" style="background:#d8d2dc"></i>圧縮で消えたもの</span>
</div>
</div>

<h2><span class="n">05</span>判定 ── 変わらなかったもの</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>\(c\cdot t=\)一定 は記法であって、新しい物理ではない</strong><span>第3回で証明、第46回で再確認</span></div></div>
<div class="row"><div class="mk">2</div><div class="txt"><strong>初期宇宙まで額面で外挿すると元素合成と矛盾する</strong><span>前シリーズの判決、動かない</span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>短さでは買い、当てはまりでは大きく払う</strong><span>第25・46・48回</span></div></div>
<div class="row hi"><div class="mk">4</div><div class="txt"><strong>\(q=0\) は 13\(\sigma\)、\(w=-1/3\) は 23\(\sigma\) で外れる</strong><span>第46回</span></div></div>
</div>

<div class="keybox">
<p class="lbl">05節の結論</p>
<p style="margin:6px 0 0"><strong>50 回かけても、判定は一度も動きませんでした。</strong><br>
── 動いたのは判定ではなく、<em>なぜそう判定できるのかの理解</em>でした。</p>
</div>

<h2><span class="n">06</span>持ち帰れる三行</h2>

<div class="seven">
<div class="row hi"><div class="mk">1</div><div class="txt"><strong>次元付きは帳簿、無次元が物理。</strong><span>単位を変えて動く量は、それだけでは何も主張していない</span></div></div>
<div class="row hi"><div class="mk">2</div><div class="txt"><strong>比較相手を言わなければ、まだ文になっていない。</strong><span>「一定」「大きい」「小さい」は、何に対してかを言って初めて文になる</span></div></div>
<div class="row hi"><div class="mk">3</div><div class="txt"><strong>驚きは、ビットで測れる。</strong><span>0 ビットは恒等式、4〜7 ビットは偶然の帯、それ以上は本物</span></div></div>
</div>

<p><strong>この三行だけで、50 回ぶんの判定がやり直せます。</strong></p>

<h2><span class="n">07</span>最後に、題の意味</h2>

<div class="aside">
<span class="tag">「動くのは、一つだけだった」</span>
<strong>一つ目の意味：</strong>共形変換をどこに入れても、動くのは<em>大きさだけ</em>（第 II 部）。<br>
<strong>二つ目の意味：</strong>50 回を動かしていたのは、<em>一つの考えだけ</em>（04節）。<br>
── <strong>二つは同じことを言っています。動くものと動かないものを分けること、それがこのシリーズの全部でした。</strong>
</div>

<div class="caveat">
<span class="tag">正直な線 ── シリーズ全体について</span>
<p style="margin:0 0 10px"><strong>① このシリーズは、\(c\cdot t=\)一定 を支持していません。</strong> 第3回で「記法であってモデルではない」と結論し、前シリーズの判決（初期宇宙まで額面で外挿すると元素合成と矛盾する）は一度も動いていません ── <em>50 回かけて扱ったのは「短さ」であって「正しさ」ではありませんでした</em>。<strong>学術的な標準は、インフレーションを含む \(\Lambda\)CDM モデルと、修正のない一般相対論です。</strong></p>
<p style="margin:0 0 10px"><strong>② 本シリーズが紹介した物理は、ほぼすべてが確立した標準的な内容です。</strong> 共形変換、くりこみ群、ブラックホール熱力学、量子アノマリー、宇宙論の標準模型 ── <em>これらに新しい主張はありません</em>。一方で<strong>「良い理論は手術を済ませてある」（第36回）、「壊れる場所は移動する」（第38回）、「道具が触れるのはちょうど半分」（第45回）、「扉は四種類」（第49回）は、本シリーズが並べて見つけた読み方</strong>であって、教科書に書いてある主張ではありません。</p>
<p style="margin:0 0 10px"><strong>③ 数え上げには、すべて数え方の恣意性があります。</strong> 「9 つの理論」「8 つの場所」「16 の扉」「6 つの道具」── <em>どれも分け方次第で増減します</em>（第46回③、第49回①）。<strong>要点は構造のほうで、個数ではありません。</strong></p>
<p style="margin:0 0 10px"><strong>④ ビットという単位は、同じ通貨で書けることを示すだけです。</strong> 驚き・余白・隔たり・獲得・記述長 ── <em>これらは足したり順位をつけたりできる量ではありません</em>（第36回⑤、第45回③）。</p>
<p style="margin:0"><strong>⑤ 測れなかったものがあります。</strong> 第48回で書いたとおり、<em>感覚的な美しさは本シリーズの道具の外</em>にあります ── 測れないことは無いことではありません。そして<strong>「測れないものを判定に使わない」のが、第3回以来の作法でした。</strong></p>
</div>

<div class="prob">
<p class="lbl">練習問題（最終回）</p>
<ol>
<li>四度の圧縮に共通していたことは何か。
<details><summary>答えを見る</summary><div class="ans"><strong>別々に見えた数が、一つだった</strong>ということです ── 第26回（24→12）、第40回（三つの \(10^{122}\)→1）、第41回（四つ→1）、第46回（12→3）。そして毎回、第19回の分類では <strong>0 ビット（恒等式）</strong>。<em>驚くべきことが起きていたのではなく、同じことを別の言葉で言っていました。</em></div></details></li>

<li>このシリーズの道具は、圧縮するといくつになるか。
<details><summary>答えを見る</summary><div class="ans"><strong>2 個</strong>（6 個から 3.0 倍の圧縮）── (i) <em>次元付きと無次元を分けること</em>、(ii) <em>全部をビットで測ること</em>。第16・33回は第3回の適用、第5・19・24回はどれも「ビットで測る」でした。</div></details></li>

<li>その 2 個の関係は。
<details><summary>答えを見る</summary><div class="ans"><strong>(ii) は (i) を検査するための道具</strong>でした ── 第47回で SI が (i) を宣言し、第48回で (ii) が「美しさ」を分解し、第49回で (ii) が扉を四種類に分けました。<em>50 回でやったのは、一つの考えと、その検査の仕方だった</em>のです。</div></details></li>

<li>50 回のあいだに、判定は動いたか。
<details><summary>答えを見る</summary><div class="ans"><strong>動いていません。</strong> \(c\cdot t=\)一定 は記法であって新しい物理ではなく、初期宇宙まで外挿すれば元素合成と矛盾し、短さでは買い当てはまりでは大きく払う ── <em>動いたのは判定ではなく、なぜそう判定できるのかの理解でした</em>。</div></details></li>

<li>（最終問題）題「動くのは、一つだけだった」の二つの意味は。
<details><summary>答えを見る</summary><div class="ans">①共形変換をどこに入れても、動くのは<strong>大きさだけ</strong>（第 II 部）。②50 回を動かしていたのは、<strong>一つの考えだけ</strong>（04節）。<em>そして二つは同じことを言っています</em> ── <strong>動くものと動かないものを分けること。それがこのシリーズの全部でした。</strong></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　動くのは、一つだけだった</h2>
<p>50 回、六つの部でした。\(c\cdot t=\)一定 は記法であってモデルではないこと（第 I 部）、どこに入れても動くのは大きさだけであること（第 II 部）、情報として測ると同じ数を八つの言語で言い直していたこと（第 III 部）、同じ手術を他の理論に当てると良い理論は最初から済ませてあったこと（第 IV 部）、道具が触れるのは世界のちょうど半分で残りの半分に時間の矢があること（第 V 部）、そして手続きそのものを検査すると扉には四種類しかなかったこと（第 VI 部）。</p>
<p>四度、圧縮に成功しました ── 24 の数字が 12 の入力に、三つの \(10^{122}\) が一つに、四つ目のペンローズの \(10^{10^{123}}\) も同じ数に、12 の \(a\propto t\) の言い方が 3 個の入力に。<strong>四度とも、別々に見えた数が一つでした</strong>。そして毎回 <em>0 ビット</em> ── 驚くべきことが起きていたのではなく、<em>同じことを別の言葉で言っていた</em>のです。</p>
<p>最後に、その圧縮をシリーズ自身に当てました。道具は 6 個ありましたが、第16・33回は第3回の適用で、第5・19・24回はどれも「ビットで測る」── <strong>独立なのは 2 個でした</strong>。(i) 次元付きと無次元を分けること、(ii) 全部をビットで測ること。そしてもう一段 ── <strong>(ii) は (i) を検査するための道具でした。</strong> <em>50 回でやったのは、一つの考えと、その検査の仕方だったのです。</em></p>
<p>判定は、一度も動きませんでした。\(c\cdot t=\)一定 は記法であって新しい物理ではなく、初期宇宙まで外挿すれば元素合成と矛盾し、\(q=0\) は 13\(\sigma\)、\(w=-1/3\) は 23\(\sigma\) で外れます。<em>動いたのは判定ではなく、なぜそう判定できるのかの理解でした。</em></p>
<p>持ち帰れるのは三行です ── <strong>次元付きは帳簿、無次元が物理。比較相手を言わなければ、まだ文になっていない。驚きは、ビットで測れる。</strong> この三行だけで、50 回ぶんの判定がやり直せます。</p>
<p>そして題の意味。<strong>「動くのは、一つだけだった」</strong> ── 共形変換をどこに入れても動くのは大きさだけで、50 回を動かしていたのも一つの考えだけでした。<em>二つは同じことを言っています。</em> <strong>動くものと動かないものを分けること。それが、このシリーズの全部でした。</strong></p>
</div>

<div class="next">
<span class="lbl">おわりに</span>
ここまで読んでくださって、ありがとうございました。<br>
このシリーズの数字はすべて <span style="font-family:ui-monospace,monospace">kenshou/calcNN.py</span>（53 本）で計算し、<em>書く前に走らせています</em>。式や数値に誤りを見つけたら、それは<strong>直すべきもの</strong>です ── 第3回以来、<em>間違いは消さずに、印をつけて残す</em>のがこのシリーズの作法でした。<br>
そして最後にもう一度だけ ── <strong>次元付きは帳簿、無次元が物理。比較相手を言わなければ、まだ文になっていない。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sc=document.getElementById('sc'), vc=document.getElementById('vc'), ro=document.getElementById('ro');
  var X0=60, X1=690, Y0=50;

  var STAGE=[
    {n:50, lab:'50 の回', note:'第1回から第50回まで'},
    {n:6,  lab:'6 の道具', note:'第3・5・16・19・24・33回'},
    {n:2,  lab:'2 の考え', note:'(i) 次元で分ける　(ii) ビットで測る'},
    {n:1,  lab:'1 つ', note:'一つの考えと、その検査の仕方'}
  ];

  function draw(){
    var s=parseInt(sc.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    var N=50, cols=10, cw=(X1-X0)/cols, ch=24;
    var keep=STAGE[s].n;
    for(var i=0;i<N;i++){
      var r=Math.floor(i/cols), c=i%cols;
      var x=X0+c*cw, y=Y0+r*ch;
      var alive=(i<keep);
      g.fillStyle = alive ? '#2a3a5a' : '#d8d2dc';
      g.globalAlpha = alive ? 0.92 : 1;
      g.fillRect(x+3, y, cw-7, ch-7);
      g.globalAlpha=1;
    }

    g.textAlign='center';
    g.fillStyle='#2a3a5a';
    g.font='22px "Hiragino Mincho ProN","Yu Mincho",serif';
    g.fillText(STAGE[s].lab, (X0+X1)/2, Y0+5*ch+42);
    g.fillStyle='#7d7686';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText(STAGE[s].note, (X0+X1)/2, Y0+5*ch+66);

    // 段階の目盛り
    for(var k=0;k<4;k++){
      var xx=X0+40+k*((X1-X0-80)/3);
      g.fillStyle = (k<=s) ? '#2a3a5a' : '#ddd8e2';
      g.beginPath(); g.arc(xx, Y0+5*ch+92, 5, 0, 6.29); g.fill();
    }

    vc.textContent=String(s);
    var comp = (s===0) ? '' : '　／　ここまでの圧縮 '+(50/STAGE[s].n).toFixed(1)+' 倍';
    ro.textContent='段階 '+s+'：'+STAGE[s].lab+'　（'+STAGE[s].note+'）'+comp+
      (s===3?'　★ 動くのは、一つだけだった':'');
  }
  sc.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-50-final.html', acc='#2a3a5a', ops='#7a5a3a',
      title='最終回：動くのは、一つだけだった ── わかる c·t=一定 第50回',
      ep='第 50 回 ／ 最終回',
      eyebrow='50 回でやったのは、一つの考えと、その検査の仕方でした',
      h1='動くのは、<br>一つだけだった',
      sub='六つの部、九つの理論、八つの壊れる場所、16 の開いた扉、四度の圧縮。<br><em>全部が、第3回で作った一つの手続きの帰結でした。</em>',
      byline_l='必要な道具：第3回の判定、第5回の天秤、第19回の目盛り ── この三つだけ',
      byline_r='53 本の検証スクリプト、すべて走らせてから書きました',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第50回（最終回）、物理好きの高校生・大学生向け読み物です。本回は第1〜49回のまとめで、新しい計算は 02〜04節の集計のみです（kenshou/calc54.py）── 各回の数値と出典は、それぞれの回の巻末を参照してください。<strong>このシリーズは \\(c\\cdot t=\\)一定 を支持していません</strong> ── 第3回で「記法であってモデルではない」と結論し、前シリーズの判決（初期宇宙まで額面で外挿すると元素合成と矛盾する）は一度も動いていません。<em>50 回かけて扱ったのは「短さ」であって「正しさ」ではありませんでした</em> ── <strong>学術的な標準は、インフレーションを含む \\(\\Lambda\\)CDM モデルと、修正のない一般相対論です。</strong> 本シリーズが紹介した物理はほぼすべてが確立した標準的な内容で（共形変換、くりこみ群、ブラックホール熱力学、量子アノマリー、宇宙論の標準模型）<em>これらに新しい主張はありません</em>。一方で<strong>「良い理論は手術を済ませてある」（第36回）、「壊れる場所は移動する」（第38回）、「道具が触れるのはちょうど半分」（第45回）、「扉は四種類」（第49回）は、本シリーズが並べて見つけた読み方</strong>であって教科書の主張ではありません。<strong>数え上げにはすべて数え方の恣意性があり</strong>（「9 つの理論」「8 つの場所」「16 の扉」「6 つの道具」）、要点は構造のほうで個数ではありません。<strong>ビットという単位は「同じ通貨で書ける」ことを示すだけ</strong>で、驚き・余白・隔たり・獲得・記述長は足したり順位をつけたりできる量ではありません。<strong>そして測れなかったものがあります</strong> ── 感覚的な美しさは本シリーズの道具の外にあり、<em>測れないことは無いことではありません</em>。「測れないものを判定に使わない」のが、第3回以来の作法でした。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで圧縮の段階を進められます。「答えを見る」で解答が開きます。')
