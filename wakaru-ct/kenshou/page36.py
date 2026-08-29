# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第 IV 部の九つを、一枚の手術台に並べます ── インフレーション、VSL、MOND、定数の測定、CCC、コスモン、ミルン、共形重力、漸近安全性。<strong>すべてに同じ手術を当てて、分かれ目がどこにあったかを一覧にします。</strong> そして、この部で分かったいちばん大事なことを書きます ── <em>良い理論は、第3回の手術を最初から済ませてある。</em> <strong>済ませていなかったのは、一つだけでした。</strong></p>

<h2><span class="n">01</span>九つを、一枚の表に</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">回</th><th>理論</th><th class="mid">(A) 記法</th><th class="mid">(B) 観測にかかる主張</th><th class="mid">手術</th></tr></thead>
<tbody>
<tr><th class="mid">27</th><td>インフレーション</td><td class="mid">因果的に繋げる</td><td class="mid">\(n_s\approx1-2/N\)</td><td class="mid">済</td></tr>
<tr class="hi"><th class="mid">28</th><td><strong>VSL</strong></td><td class="mid">単位の取り替え</td><td class="mid">\(\alpha\) が動く</td><td class="mid"><strong>✗</strong></td></tr>
<tr><th class="mid">29</th><td>MOND</td><td class="mid">\(a_0\) を置く</td><td class="mid">力学が \(g/a_0\) で決まる</td><td class="mid">済</td></tr>
<tr><th class="mid">30</th><td>定数の測定</td><td class="mid">（記法ではない）</td><td class="mid">\(\alpha\) の不変性（26 ビット）</td><td class="mid">──</td></tr>
<tr><th class="mid">31</th><td>CCC</td><td class="mid">共形の貼り合わせ</td><td class="mid">前の宇宙が続く</td><td class="mid">済</td></tr>
<tr><th class="mid">32</th><td>コスモン</td><td class="mid">膨張しない絵</td><td class="mid">\(w(z)\ne-1\)</td><td class="mid">済</td></tr>
<tr><th class="mid">33</th><td>ミルン</td><td class="mid">座標変換</td><td class="mid">（中身が空）</td><td class="mid">──</td></tr>
<tr><th class="mid">34</th><td>共形重力</td><td class="mid">ゲージ対称性</td><td class="mid">回転曲線、\(\alpha_g\)</td><td class="mid">切るものが無い</td></tr>
<tr><th class="mid">35</th><td>漸近安全性</td><td class="mid">\(G\) の無次元化</td><td class="mid">\(m_H\)、予言の個数</td><td class="mid">済</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>(A) と (B) を区別できていなかったのは、VSL ただ一つ。</strong><br>
── <em>良い理論は、第3回の手術を最初から済ませてあります。</em></p>
</div>

<h2><span class="n">02</span>分かれ目は、名前ではなかった</h2>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>「名前が (A) を指しているか」ではない</strong><span>コスモンの論文題は「膨張しない宇宙」で (A) 側。VSL も (A) 側。<em>そこまでは同じ</em></span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>「理論の側が (A) と (B) を区別できているか」だった</strong><span>ヴェッテリヒは二つの絵が Weyl 変換で等価だと明示し、ペンローズは貼り合わせで物差しが無いと明言した</span></div></div>
<div class="row"><div class="mk">✗</div><div class="txt"><strong>VSL だけが区別しなかった</strong><span>結果、「光速が変わる」が中身（\(\alpha\) が変わる）を隠し、<em>26 ビットの制約が正面から見えなくなった</em></span></div></div>
</div>

<h2><span class="n">03</span>予言は、例外なく無次元量に置かれていた</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>理論</th><th class="mid">予言の置き場所</th><th class="mid">次元</th></tr></thead>
<tbody>
<tr><th>インフレーション</th><td class="mid">\(n_s\)</td><td class="mid">無次元</td></tr>
<tr><th>VSL</th><td class="mid">\(\Delta\alpha/\alpha\)</td><td class="mid">無次元</td></tr>
<tr><th>MOND</th><td class="mid">\(g/a_0\)</td><td class="mid">無次元</td></tr>
<tr><th>CCC</th><td class="mid">ホーキング点の統計</td><td class="mid">無次元</td></tr>
<tr><th>コスモン</th><td class="mid">\(w\)</td><td class="mid">無次元</td></tr>
<tr><th>共形重力</th><td class="mid">回転曲線の形</td><td class="mid">無次元</td></tr>
<tr class="hi"><th>漸近安全性</th><td class="mid">\(m_H/v\)</td><td class="mid"><strong>無次元</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">03節の結論</p>
<p style="margin:6px 0 0"><strong>例外はありませんでした。</strong> 第3回の判定手続きの、いちばん強い確認です。<br>
── <em>次元付きの量に主張を置いた理論は、そもそも判定の土俵に乗りません。</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>核心 ── 偶然の帯</h2>

<p>もう一つ、並べてはじめて見えたことがあります。第19回で作った「驚きのビット数」で、この部に出てきた一致を全部並べます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>一致</th><th class="mid">驚き</th><th class="mid">分類</th></tr></thead>
<tbody>
<tr><th>\(\rho_\Lambda^{1/4}\) と \(m_\nu\)（前・番外編⑤）</th><td class="mid">4.7 bit</td><td class="mid">偶然</td></tr>
<tr class="hi"><th>インフレーションの \(N\) の一致（第27回）</th><td class="mid">4.8 bit</td><td class="mid">説明あり→物理</td></tr>
<tr class="hi"><th>漸近安全性のヒッグス予言（第35回）</th><td class="mid">5.3 bit</td><td class="mid">説明あり→物理</td></tr>
<tr class="hi"><th>共形重力の \(\gamma_0\simeq1/25R_H\)（第34回）</th><td class="mid">5.4 bit</td><td class="mid">偶然</td></tr>
<tr class="hi"><th>MOND の \(a_0\simeq cH_0/2\pi\)（第29回）</th><td class="mid">5.9 bit</td><td class="mid">偶然</td></tr>
<tr><th>1 ビット ↔ 1.96 fm（第18回）</th><td class="mid">7.4 bit</td><td class="mid">偶然</td></tr>
<tr><th>小出の関係式（前・番外編④）</th><td class="mid">15.7 bit</td><td class="mid">経験式</td></tr>
<tr><th>CMB の一様性（第17回）</th><td class="mid">\(1.6\times10^5\) bit</td><td class="mid">本物の問題</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>4〜7.5 ビットの帯に、6 件が集まっています</strong>（平均 5.6、幅 2.7 ビット）。<br>
まったく独立な理論から出てきた一致が、なぜ同じ狭い帯に落ちるのか。</p>
</div>

<div class="fig">
<p class="cap">図：このシリーズが測ってきた「驚き」を、一本の軸に並べたもの。<strong>4〜7.5 ビットの帯に集中しています</strong>。ツマミで「気に留める閾値」を動かすと、何件が残るかが読めます ── <em>帯の正体は、たぶん選択効果です</em></p>
<canvas id="cv" width="720" height="390"></canvas>
<div class="controls">
  <label>「気に留める」閾値（ビット）<input id="sb" type="range" min="0" max="180" value="40" step="1"></label>
  <span class="val" id="vb">4.0 bit</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#38343f"></i>偶然と判定したもの</span>
  <span><i class="swatch" style="background:#8a6a3a"></i>説明があるもの（物理）</span>
  <span><i class="swatch" style="background:#d8d2dc"></i>閾値より下（気に留められない）</span>
</div>
</div>

<div class="seven">
<div class="row"><div class="mk">↓</div><div class="txt"><strong>4 ビット未満（1/16 より緩い）</strong><span>誰も気に留めない ── 記録にすら残らない</span></div></div>
<div class="row hi"><div class="mk">◆</div><div class="txt"><strong>4〜7 ビット</strong><span><em>論文にはなるが、合意にはならない</em> ── 「面白いが決定的でない」が住む場所</span></div></div>
<div class="row"><div class="mk">↑</div><div class="txt"><strong>15 ビット超（小出の関係式）</strong><span>有名になり、説明を要求される ── 40 年たっても導出が無いことが問題になる</span></div></div>
</div>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0">帯の正体は、たぶん<strong>選択効果</strong>です ── <em>緩すぎれば誰も見ず、きつすぎれば説明されてしまう。</em><br>
── <strong>第19回で作った目盛りが、物理学の営みそのものを測っていた</strong>ことになります。</p>
</div>

<h2><span class="n">05</span>帳簿の総まとめ</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>理論</th><th class="mid">パラメータ</th><th class="mid">買うもの</th><th class="mid">差し引き [bit]</th></tr></thead>
<tbody>
<tr><th>インフレーション（第27回）</th><td class="mid">\(+2\)</td><td class="mid">\(n_s\) ほか多数</td><td class="mid">\(-6.5\)（過小評価）</td></tr>
<tr class="hi"><th>c·t=一定（第25回）</th><td class="mid">\(-1\)</td><td class="mid">地平線問題が消える</td><td class="mid"><strong>\(-148.3\)</strong></td></tr>
<tr class="hi"><th>MOND（回転曲線のみ、第29回）</th><td class="mid">\(+4\)</td><td class="mid">バリオンから回転曲線</td><td class="mid"><strong>\(+1971\)</strong></td></tr>
<tr class="hi"><th>共形重力（回転曲線のみ、第34回）</th><td class="mid">\(+3\)</td><td class="mid">同上 ＋ \(\Lambda\) 項が禁じられる</td><td class="mid"><strong>\(+1977\)</strong></td></tr>
<tr><th>コスモン（第32回）</th><td class="mid">\(+2\)</td><td class="mid">\(\rho_\Lambda\) の大きさ（最大 408）</td><td class="mid">大きく黒字</td></tr>
<tr><th>漸近安全性（第35回）</th><td class="mid">\(+3\)</td><td class="mid">\(m_H\)、紫外の有限性</td><td class="mid">評価未確定</td></tr>
</tbody>
</table>
</div>

<p>単位は第5回の天秤（パラメータ 1 個 = 5.37 ビット）です。<strong>ただしデータセットが違うので、直接比較はできません</strong> ── 第29回で見たとおり、<em>どのデータセットで測るかで勝敗が変わります</em>。この表は「同じ通貨で書けること」を示すものであって、順位表ではありません。</p>

<h2><span class="n">06</span>種明かし ── 四つとも、一つの手続きの帰結だった</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>良い理論は、第3回の手術を最初から済ませてある</strong><span>済ませていなかったのは VSL だけ（01・02節）</span></div></div>
<div class="row"><div class="mk">2</div><div class="txt"><strong>予言は例外なく無次元量に置かれる</strong><span>次元付きに置いた主張は、判定の土俵に乗らない（03節）</span></div></div>
<div class="row hi"><div class="mk">3</div><div class="txt"><strong>面白い一致は 4〜7 ビットの帯に集まる</strong><span>それは選択効果 ── 緩すぎれば見られず、きつすぎれば説明される（04節）</span></div></div>
<div class="row"><div class="mk">4</div><div class="txt"><strong>勝敗はデータセットに依存する</strong><span>「暗黒物質か MOND か」は一つの問いではなかった（05節、第29回）</span></div></div>
</div>

<div class="keybox">
<p class="lbl">06節の結論</p>
<p style="margin:6px 0 0"><strong>四つとも、第3回で作った一つの手続きの帰結でした。</strong><br>
<em>「次元付きは帳簿、無次元が物理。比較相手を言わなければ、まだ文になっていない」</em> ──<br>
それだけで、九つの理論の分かれ目が全部説明できます。</p>
</div>

<div class="aside">
<span class="tag">第 I〜IV 部を、一行ずつ</span>
<strong>第 I 部</strong>：\(c\cdot t=\)一定 は記法であって、モデルではない。<br>
<strong>第 II 部</strong>：どこに入れても、動くのは一つだけ。触れるのは大きさだけ。<br>
<strong>第 III 部</strong>：情報として測ると、同じ数を八つの言語で言い直していた。<br>
<strong>第 IV 部</strong>：同じ手術を他の理論に当てると、<em>良い理論は最初から済ませてあった</em>。
</div>

<div class="caveat">
<span class="tag">正直な線 ── 第 IV 部全体について</span>
<p style="margin:0 0 10px"><strong>① 「手術が済んでいるか」の判定は、本シリーズの読み方です。</strong> 各理論の提唱者がどこまで意識していたかは、論文の書き方から推し量ったもので、<em>本人の意図を確かめたわけではありません</em>。VSL についても、名前が中身を隠したという指摘は Ellis &amp; Uzan (2005) の整理に基づくものであって、VSL の研究者がその区別を理解していなかったという意味ではありません。</p>
<p style="margin:0 0 10px"><strong>② 04節の「偶然の帯」は、8 件という小さな標本に基づく観察です。</strong> しかも<em>このシリーズが取り上げた一致だけ</em>を集めたもので、選び方そのものにバイアスがあります ── <strong>「選択効果だ」という説明自体が、選択効果を受けた標本から出ています</strong>。定量的な主張ではなく、<em>目に付いたパターンの記録</em>として読んでください。</p>
<p style="margin:0 0 10px"><strong>③ 各回の驚きのビット数は、事前範囲の取り方に依存します</strong>（第19回①）。4.7〜7.4 という値は数ビット動きうるので、「帯」の幅もそのぶん曖昧です。</p>
<p style="margin:0 0 10px"><strong>④ 05節の帳簿は、データセットが揃っていません。</strong> 第25回は超新星、第29回・第34回は銀河の回転曲線、第27回は CMB ── <em>同じ通貨で書けることを示すための表であって、順位表ではありません</em>。パラメータ数の見積もりもそれぞれ粗いものです。</p>
<p style="margin:0"><strong>⑤ 本稿は第 IV 部で扱った理論のどれも支持・否定しません。</strong> インフレーションを除いてすべて少数派の仮説であり、学術的な標準はインフレーションを含む \(\Lambda\)CDM モデルと、修正のない一般相対論です。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（第 IV 部の総まとめ）</p>
<ol>
<li>九つの理論のうち、手術が済んでいなかったのはどれか。
<details><summary>答えを見る</summary><div class="ans"><strong>VSL（第28回）ただ一つ</strong>。(B)「\(\alpha\) が動く」を主張しながら (A)「単位の取り替え」の名前を残したので、<em>\(\alpha\) の 26 ビットの制約が正面から見えなくなりました</em>。</div></details></li>

<li>分かれ目は「名前が (A) を指しているか」だったか。
<details><summary>答えを見る</summary><div class="ans">違います。コスモンの論文題「膨張しない宇宙」も VSL も、名前は (A) 側です。<strong>分かれ目は「理論の側が (A) と (B) を区別できているか」</strong>でした ── ヴェッテリヒは二つの絵が Weyl 変換で等価だと明示しています。</div></details></li>

<li>七つの理論の予言に共通する性質は何か。
<details><summary>答えを見る</summary><div class="ans"><strong>例外なく無次元量に置かれていること</strong> ── \(n_s\)、\(\Delta\alpha/\alpha\)、\(g/a_0\)、\(w\)、\(m_H/v\) など。第3回の判定手続きのいちばん強い確認で、<em>次元付きに置いた主張は判定の土俵に乗りません</em>。</div></details></li>

<li>「偶然の帯」とは何か。その説明は。
<details><summary>答えを見る</summary><div class="ans">このシリーズが扱った一致のうち 6 件が <strong>4〜7.5 ビット</strong>に集まっていること（平均 5.6）。説明はたぶん<strong>選択効果</strong> ── <em>4 ビット未満は誰も気に留めず、15 ビット超は有名になって説明を要求される。4〜7 ビットは「論文にはなるが合意にはならない」場所</em>です。ただし②のとおり、標本が小さくバイアスもあります。</div></details></li>

<li>（やや難）第 IV 部の四つの発見は、何から出てきたか。
<details><summary>答えを見る</summary><div class="ans"><strong>第3回で作った一つの手続き</strong>です ── 「次元付きは帳簿、無次元が物理。比較相手を言わなければ、まだ文になっていない」。①手術が済んでいるか、②予言がどこに置かれるか、③一致の驚きをどう測るか、④勝敗がデータセットに依存すること ── <em>四つとも、この一つの手続きの帰結でした</em>。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　良い理論は、手術を済ませてある</h2>
<p>第 IV 部の九つを一枚の表に並べました。<strong>(A) 記法と (B) 観測にかかる主張を区別できていなかったのは、VSL ただ一つ</strong>です。そして分かれ目は「名前が (A) を指しているか」ではありませんでした ── コスモンの論文題も VSL も (A) 側で、そこまでは同じ。<em>分かれ目は「理論の側が区別できているか」</em>でした。</p>
<p>予言の置き場所も並べました ── \(n_s\)、\(\Delta\alpha/\alpha\)、\(g/a_0\)、ホーキング点の統計、\(w\)、回転曲線の形、\(m_H/v\)。<strong>例外なく無次元量</strong>です。第3回の判定手続きの、いちばん強い確認でした ── <em>次元付きに主張を置いた理論は、そもそも判定の土俵に乗りません</em>。</p>
<p>並べてはじめて見えたこともありました。第19回の「驚きのビット数」で一致を全部並べると、<strong>4〜7.5 ビットの帯に 6 件が集まっています</strong>（平均 5.6）。まったく独立な理論から出てきた一致が、同じ狭い帯に落ちる ── 正体はたぶん<strong>選択効果</strong>です。<em>4 ビット未満は誰も気に留めず、15 ビット超（小出の関係式）は有名になって説明を要求される。4〜7 ビットは「論文にはなるが、合意にはならない」場所</em>。<strong>第19回で作った目盛りが、物理学の営みそのものを測っていた</strong>ことになります。</p>
<p>そして種明かし ── ①手術が済んでいるか、②予言がどこに置かれるか、③一致がどの帯に落ちるか、④勝敗がデータセットに依存すること。<strong>四つとも、第3回で作った一つの手続きの帰結でした</strong>。<em>「次元付きは帳簿、無次元が物理。比較相手を言わなければ、まだ文になっていない」</em> ── それだけで、九つの理論の分かれ目が全部説明できます。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第37回（第 V 部のはじまり）</span>
第 V 部は、<strong>この道具が壊れる場所を、正面から探しにいく部</strong>です。第 IV 部で二度、<em>ゴースト</em>に出会いました ── 前シリーズ第9回でアインシュタイン重力の共形因子が、第34回で共形重力のスピン 2 が。第 V 部はその源へ行きます。最初は<strong>量子アノマリー</strong> ── 第11回で「光には何も起きていない」と数えたのは<em>古典の範囲</em>の話でした。量子にすると細かさの基準 \(\mu\) が持ち込まれ、共形対称性が破れます。<strong>その破れを、ビットで測ります。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sb=document.getElementById('sb'), vb=document.getElementById('vb'), ro=document.getElementById('ro');
  var X0=290, X1=690, Y0=44;
  var D=[
    ['ρ_Λ と m_ν', 4.7, 0],
    ['インフレーションの N', 4.8, 1],
    ['漸近安全性のヒッグス', 5.3, 1],
    ['共形重力の γ_0', 5.4, 0],
    ['MOND の a_0', 5.9, 0],
    ['1ビット ↔ 1.96 fm', 7.4, 0],
    ['小出の関係式', 15.7, 0],
    ['CMB の一様性', 20.0, 2]      // 目盛りの外（1.6e5）
  ];
  var XMAX=20;

  function px(b){ return X0+Math.min(b,XMAX)/XMAX*(X1-X0); }

  function draw(){
    var th=parseInt(sb.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    // 4〜7.5 の帯
    g.fillStyle='#f2eef4';
    g.fillRect(px(4.0), Y0-14, px(7.5)-px(4.0), 8*40+18);
    g.fillStyle='#9a8fa4'; g.textAlign='center';
    g.fillText('4〜7.5 ビットの帯', (px(4.0)+px(7.5))/2, Y0-20);

    g.textAlign='center';
    for(var b=0;b<=20;b+=5){
      var x=px(b);
      g.strokeStyle=(b===0?'#cdc8d2':'#f4f2f6'); g.lineWidth=(b===0?1.6:1);
      g.beginPath(); g.moveTo(x,Y0-14); g.lineTo(x,Y0+8*40+6); g.stroke();
      g.fillStyle='#9c96a4'; g.fillText(b+' bit', x, Y0+8*40+22);
    }

    var cnt=0;
    for(var i=0;i<D.length;i++){
      var b=D[i][1], kind=D[i][2];
      var below=(b<th);
      if(!below) cnt++;
      var y=Y0+i*40+8;
      var col = below ? '#d8d2dc' : (kind===1 ? '#8a6a3a' : '#38343f');
      g.fillStyle=col; g.globalAlpha=0.9;
      g.fillRect(X0, y, Math.max(px(b)-X0,3), 22);
      g.globalAlpha=1;
      g.fillStyle= below ? '#b0a8b6' : '#3a3640';
      g.textAlign='right';
      g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillText(D[i][0], X0-12, y+16);
      g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.textAlign='left'; g.fillStyle=col;
      if(kind===2) g.fillText('→ 1.6×10⁵ bit（桁が違う）', px(b)-160, y+16);
      else g.fillText(b.toFixed(1)+' bit', px(b)+6, y+16);
    }

    // 閾値の線
    g.strokeStyle='#7a6a84'; g.lineWidth=1.8; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(th),Y0-14); g.lineTo(px(th),Y0+8*40+6); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('驚き ＝ −log₂( 落ちた幅 ÷ 事前に許された範囲 )', (X0+X1)/2-70, Y0+8*40+46);

    vb.textContent=th.toFixed(1)+' bit';
    ro.textContent='閾値 '+th.toFixed(1)+' ビット　→　気に留められるのは '+cnt+' 件／8 件'+
      '　／　4〜7.5 の帯には 6 件（平均 5.6、幅 2.7）'+
      (th<4?'　★ ここを下げても、拾えるものが増えない ── 帯の下は空いている':'');
  }
  sb.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-36-partIV.html', acc='#38343f', ops='#8a6a3a',
      title='手術台の上に並べる ── わかる c·t=一定 第36回（第IV部・総括）',
      ep='第 36 回 ／ 第 IV 部・総括',
      eyebrow='済ませていなかったのは、一つだけでした',
      h1='手術台の上に、<br>並べる',
      sub='九つの理論に同じ手術を当てて、分かれ目を一覧にします。<br><em>そして「偶然の帯」という、並べてはじめて見えたものがありました。</em>',
      byline_l='必要な道具：第 IV 部の九回、第19回の目盛り、第5回の天秤',
      byline_r='4〜7 ビット ── 面白いが決定的でない場所',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第36回（第 IV 部・総括）、物理好きの高校生・大学生向け読み物です。本回は第27〜35回の結果をまとめたもので、新しい計算は 04節の集計のみです（kenshou/calc40.py）── 各回の数値と出典は、それぞれの回の巻末を参照してください。<strong>「手術が済んでいるか」の判定は本シリーズの読み方であり</strong>、各理論の提唱者がどこまで意識していたかは論文の書き方から推し量ったもので、本人の意図を確かめたものではありません ── VSL について「名前が中身を隠した」という指摘は Ellis &amp; Uzan (2005) の整理に基づくもので、VSL の研究者がその区別を理解していなかったという意味ではありません。<strong>04節の「偶然の帯」は 8 件という小さな標本に基づく観察であり、しかもこのシリーズが取り上げた一致だけを集めたものです</strong> ── 「選択効果だ」という説明自体が選択効果を受けた標本から出ており、<em>定量的な主張ではなく、目に付いたパターンの記録</em>として読んでください。各回の驚きのビット数は事前範囲の取り方に依存します（第19回①）。05節の帳簿はデータセットが揃っておらず（第25回は超新星、第29回・第34回は銀河の回転曲線、第27回は CMB）、<em>同じ通貨で書けることを示すための表であって順位表ではありません</em>。<strong>本稿は第 IV 部で扱った理論のどれも支持・否定しません</strong> ── インフレーションを除いてすべて少数派の仮説であり、学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルと、修正のない一般相対論です。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで閾値を動かし、帯の下が空いている様子が見えます。「答えを見る」で解答が開きます。')
