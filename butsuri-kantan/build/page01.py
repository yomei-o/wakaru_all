# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">「物理をもっと簡単にしたい」── 誰もが一度は思うことです。ところがこの願いを実行しようとすると、すぐに困ります。<em>何を減らせば「簡単」になったことになるのか</em>が決まっていないからです。この回では、まずそこを決めます。答えは <strong>三つあって、しかも互いに独立</strong> でした。</p>

<h2><span class="n">01</span>同じ言葉で、三つの別のことを言っている</h2>

<p>標準模型のラグランジアンは、<em>マグカップに印刷できます</em>。実際に売っています。式は短い。それなのに誰も「標準模型は簡単だ」とは言いません。</p>

<p>逆に、\(F=ma\) は短くて、しかも簡単です。式の長さは似たようなものなのに、片方は簡単で片方は簡単でない。<strong>ということは「簡単」は式の長さのことではない</strong>、少なくともそれだけではない。</p>

<p>分けてみると、三つになりました。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>軸</th><th>何を減らすか</th><th>実例</th></tr></thead>
<tbody>
<tr><th>記述長</th><td>法則と定数の<strong>数</strong></td><td>統一。マクスウェル、電弱理論</td></tr>
<tr><th>計算量</th><td><strong>解ける</strong>ようにする</td><td>Parke–Taylor 公式、ブートストラップ</td></tr>
<tr class="hi"><th><strong>前提概念</strong></th><td><strong>人が一度に抱える数</strong></td><td><strong>？</strong></td></tr>
</tbody>
</table>
</div>

<p>三つ目の欄が空いているのは、書き忘れではありません。<em>この軸には、まだ名前のついた実例がないのです。</em></p>

<h2><span class="n">02</span>三つが独立であることを、数字で確かめる</h2>

<p>「独立」というのは、片方を減らしても他方が減るとは限らない、という意味です。それを確かめるには、同じものを三つの物差しで測ればよい。物理の代表的な法則を、そうやって並べます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>法則</th><th class="mid">記号の数</th><th class="mid">計算量</th><th class="mid">前提概念の数</th></tr></thead>
<tbody>
<tr><th>\(F=ma\)</th><td class="mid">3</td><td class="mid">1 演算</td><td class="mid">3</td></tr>
<tr><th>\(F=Gm_1m_2/r^2\)</th><td class="mid">5</td><td class="mid">3 演算</td><td class="mid">4</td></tr>
<tr><th>マクスウェル 4 式</th><td class="mid">20</td><td class="mid">偏微分方程式</td><td class="mid">8</td></tr>
<tr><th>シュレーディンガー方程式</th><td class="mid">8</td><td class="mid">偏微分方程式</td><td class="mid">10</td></tr>
<tr><th>一般相対論の場の方程式</th><td class="mid">12</td><td class="mid">非線形 PDE</td><td class="mid">16</td></tr>
<tr class="hi"><th><strong>標準模型のラグランジアン</strong></th><td class="mid">100</td><td class="mid"><strong>摂動展開／格子</strong></td><td class="mid"><strong>40</strong></td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">計算（kensho/calc01.py・calc07.py）</span>
<p class="lbl">\(F=ma\) から標準模型までの伸び</p>
<p>記号の数　： \(3 \to 100\)　（<strong>33 倍</strong>）<br>
前提概念　： \(3 \to 40\)　（<strong>13 倍</strong>）<br>
計算量　　： 1 演算 \(\to\) \(10^{19}\) flops　（<strong>\(10^{19}\) 倍</strong>）</p>
</div>

<p><strong>三つの倍率が、まったく違います。</strong> 33 倍、13 倍、\(10^{19}\) 倍。もしこれらが同じものを測っているなら、倍率はそろうはずでした。そろっていないので、<em>三つは別の量です</em>。</p>

<div class="keybox">
<span class="lbl">この回の要点</span>
<p><strong>標準模型がわかりにくいのは、式が長いからではありません。</strong> 記号は 33 倍にしかなっていないのに、前提概念は 13 倍、計算量は \(10^{19}\) 倍。<em>「わかりにくい」の中身は、記号の数ではなく、前提概念の数の方にあります。</em></p>
</div>

<h2><span class="n">03</span>前提概念とは何か</h2>

<p>「前提概念」を、はっきりさせておきます。<strong>その式を読むために、先に知っていなければならない考えの数</strong>のことです。</p>

<p>\(F=ma\) を読むのに要るのは、力・質量・加速度の三つ。どれも日常語で説明を始められます。</p>

<p>標準模型のラグランジアンを読むのに要るのは ── ゲージ群、表現、スピノル、ディラック共役、共変微分、場の強さ、非可換性、くりこみ、走る結合、自発的対称性の破れ、ヒッグス機構、湯川結合、CKM 行列、カイラリティ、アノマリー、ゴースト、ゲージ固定、経路積分、…。数え方に幅はありますが、<em>四十個前後</em>です。</p>

<div class="caveat">
<span class="tag">正直な線</span>
<p>この「四十個」は<strong>筆者が数えたもの</strong>で、標準的な定義はありません。何を一つと数えるかで簡単に上下します。ただし <em>倍率が三つの軸でまったく違う</em> という結論は、多少の数え方の違いでは動きません（13 倍と 33 倍と \(10^{19}\) 倍の差は、数え方の幅よりずっと大きい）。</p>
</div>

<h2><span class="n">04</span>三つの軸は、下げやすさが違う</h2>

<p>ここからがこのシリーズの本題です。<strong>三つの軸は、下げるのに要るものが違います。</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>軸</th><th>下げるには</th><th>実績</th><th>いまの状況</th></tr></thead>
<tbody>
<tr><th>記述長</th><td><strong>新しい物理が要る</strong></td><td>統一が起きるまで下がらない</td><td>50 年停滞中</td></tr>
<tr><th>計算量</th><td><strong>記法で下がる</strong></td><td>Parke–Taylor で \(10^{7}\) 倍</td><td>実績あり</td></tr>
<tr class="hi"><th><strong>前提概念</strong></th><td><strong>記法と順序で下がる</strong></td><td><strong>誰もやっていない</strong></td><td><strong>空いている</strong></td></tr>
</tbody>
</table>
</div>

<p>記述長を下げるには、新しい発見を待つしかありません。実際 1973 年以来、待ち続けています（第16回で数えます）。</p>

<p>計算量は記法で下がります。実際に \(10^{7}\) 倍下がった例があります（第3回でやります）。</p>

<p>そして<strong>前提概念も記法で下がるはずなのに、誰も測っていないし、最適化していない</strong>。だから空いています。</p>

<div class="aside">
<span class="tag">このシリーズがやること</span>
<p>三つの軸を、実際の物理に当てて測ります。第 I 部で物差しを作り、第 II 部で強い力に当て、第 III 部で「厳密とは何か」を決め、第 IV 部で「全部を整数の比にできないか」を検定します。<em>数字はすべて、書く前にスクリプトを走らせて出しました。</em></p>
</div>

<h2><span class="n">05</span>なぜ、この分け方が要るのか</h2>

<p>分けないと、議論がすれ違うからです。</p>

<p>「格子 QCD は陽子の質量を 1 % で出す」と言われて、「でも \(10^{19}\) 回も計算するのは簡単じゃない」と思う。これは <em>記述長では簡単、計算量では大変</em> という話で、両方正しい。</p>

<p>「構成子クォーク模型なら暗算で 1 % に届く」と言われて、「でも構成子質量なんて意味不明な定数を持ち込んでいる」と思う。これは <em>計算量では簡単、記述長では高い</em> という話で、これも両方正しい。</p>

<p><strong>三つの軸を分けておけば、どちらが正しいかを争わずに済みます。</strong> 何と何を交換したのかを、そのまま書けばよい。</p>

<div class="next">
<span class="lbl">次回</span>
<p>三つの軸のうち、<strong>計算量</strong>から測ります。電子の \(g-2\) を使うと、「計算を 1 ビット増やすと精度が何ビット買えるか」という<em>為替レート</em>が実際に出ます。そしてそれをパラメータの値段と比べると、<strong>計算がいちばん安い通貨</strong>だと分かります。</p>
</div>'''

build(out='../butsuri-kantan-01-three-axes.html', acc='#1c3f63', ops='#a85a12',
      title='第1回：「簡単」には三つある ── 物理を簡単にする',
      ep='第 1 回 ／ 第 I 部「簡単」を測る',
      eyebrow='記述長・計算量・前提概念 ── 三つは互いに独立でした',
      h1='「簡単」には、<br>三つある',
      sub='標準模型はマグカップに印刷できるのに、わかりにくい。<br><em>差は記号の数ではなく、前提概念の数にありました。</em>',
      byline_l='必要な予備知識：なし',
      byline_r='検証：kensho/calc01.py, calc07.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第1回、物理好きの高校生・大学生向けの読み物です。<strong>「前提概念の数」は本シリーズの独自の物差しであって、標準的な用語ではありません</strong> ── 数え方には恣意性があり、絶対値は当てになりません。要点は<em>三つの軸の倍率が違うこと</em>で、それは数え方の幅より大きい差です。02節の表の数値は kensho/calc01.py と calc07.py で計算しました。<strong>本シリーズは既存の物理に新しい主張を加えるものではありません</strong> ── 扱う物理はすべて確立した標準的な内容で、新しいのは<em>測り方の方</em>です。</p>')
