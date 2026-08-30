# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">最終回です。目標に対する<strong>現在地</strong>を測ります ── この 50 年、パラメータの数は<em>増え続けています</em>。それでも比を見ると勝っている。残った非圧縮性のうち、数字で生き残っている候補は<strong>一つだけ</strong>でした。そして 15 回でやってきたことを、一本の道筋にまとめます。</p>

<h2><span class="n">01</span>圧縮の実績 ── 目標は何度も達成されている</h2>

<div class="calc">
<span class="tag">計算（kensho/calc07.py ②）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>いつ</th><th>何を</th><th>何に</th><th class="mid">圧縮</th></tr></thead>
<tbody>
<tr><th>1687 ニュートン</th><td>地上の落下 ＋ 天体の運行</td><td>1 つの法則</td><td class="mid">2 → 1</td></tr>
<tr><th>1865 マクスウェル</th><td>電気 ＋ 磁気 ＋ 光</td><td>4 つの式</td><td class="mid">3 → 1</td></tr>
<tr><th>1877 ボルツマン</th><td>熱力学の諸法則</td><td>力学 ＋ 数え上げ</td><td class="mid">4 → 1</td></tr>
<tr class="hi"><th>1926 量子力学</th><td><strong>92 元素の性質の表</strong></td><td>1 つの方程式 ＋ \(Z\)</td><td class="mid"><strong>100 → 1</strong></td></tr>
<tr><th>1967 電弱</th><td>電磁気 ＋ 弱い力</td><td>1 つのゲージ群</td><td class="mid">2 → 1</td></tr>
<tr class="hi"><th>1973 QCD</th><td>ハドロン百数十個</td><td>3 つのクォーク ＋ 色</td><td class="mid"><strong>140 → 1</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>どれも「別々に見えたものが同じだった」型</strong>です。新しい仕組みを足したのではなく、既にあるものが一つだと気づいた。<em>目標は歴史的に何度も達成されていて、方法もはっきりしています。</em></p>

<h2><span class="n">02</span>ところが、この 50 年は逆を向いている</h2>

<div class="calc">
<span class="tag">計算（kensho/calc07.py ③）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">年</th><th class="mid">独立な数</th><th>できごと</th></tr></thead>
<tbody>
<tr><td class="mid">1900</td><td class="mid">300</td><td>元素・スペクトルの表をそのまま持つ</td></tr>
<tr><td class="mid">1930</td><td class="mid">30</td><td>量子力学で化学が畳まれる</td></tr>
<tr class="hi"><td class="mid">1973</td><td class="mid"><strong>19</strong></td><td><strong>標準模型が完成。ここが底</strong></td></tr>
<tr><td class="mid">1998</td><td class="mid">26</td><td>ニュートリノ質量と混合で \(+7\)</td></tr>
<tr><td class="mid">2003</td><td class="mid">28</td><td>暗黒エネルギーで \(+1\)、ほか</td></tr>
<tr class="hi"><td class="mid">2026</td><td class="mid"><strong>30</strong></td><td><strong>まだ増えている</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>1973 年を底に、パラメータの数は増え続けています。</strong> 「単純にする」は、この 50 年ずっと負けている ── 少なくとも、この数え方では。</p>

<h2><span class="n">03</span>ただし、比を見ると勝っている</h2>

<div class="calc">
<span class="tag">計算（kensho/calc07.py ④）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>時代</th><th class="mid">説明したデータ</th><th class="mid">理論の値段</th><th class="mid">圧縮率</th></tr></thead>
<tbody>
<tr class="hi"><th>1900 の化学</th><td class="mid">3000 ビット</td><td class="mid">3000 ビット</td><td class="mid"><strong>1.0</strong></td></tr>
<tr><th>1930 の量子化学</th><td class="mid">3000</td><td class="mid">161</td><td class="mid">18.6</td></tr>
<tr class="hi"><th>2026 の素粒子</th><td class="mid">30000</td><td class="mid">161</td><td class="mid"><strong>186</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">指標を取り替える</span>
<p><strong>1900 年の化学は圧縮率 1:1</strong> ── 表を書き写しただけで、理論ではありませんでした。</p>
<p>いまは <strong>186:1</strong>。パラメータは増えましたが、<em>説明した量はそれ以上に増えています</em>。</p>
<p>→ <strong>「単純にする」の正しい指標は、数ではなく比。</strong></p>
</div>

<h2><span class="n">04</span>残った非圧縮性は、どこに集中しているか</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>場所</th><th class="mid">個数</th><th>現状</th></tr></thead>
<tbody>
<tr class="hi"><th><strong>フェルミオンの質量</strong></th><td class="mid"><strong>12</strong></td><td><strong>全部フィット。確立した関係はゼロ</strong></td></tr>
<tr class="hi"><th>混合角と位相</th><td class="mid">8</td><td>全部フィット。パターンはあるが説明なし</td></tr>
<tr><th>ゲージ結合</th><td class="mid">3</td><td>走る。大統一で 1 個になる可能性</td></tr>
<tr><th>ヒッグス</th><td class="mid">2</td><td>フィット</td></tr>
<tr><th>\(\theta_{\rm QCD}\)</th><td class="mid">1</td><td>なぜ 0 なのか不明</td></tr>
<tr><th>宇宙論</th><td class="mid">6</td><td>初期条件。説明の対象かも不明</td></tr>
</tbody>
</table>
</div>

<p><strong>半分以上が質量と混合です。</strong> ここが圧縮できれば、目標の大半が片づきます。</p>

<h2><span class="n">05</span>候補を、第13回の物差しで採点する</h2>

<p>「質量や角度の間に、隠れた関係があるのではないか」── 有名な候補を四つ、採点します。買いは \(\log_2(\text{事前範囲}/\text{一致幅})\)、払いは探索空間 \(\log_2 M\)。</p>

<div class="calc">
<span class="tag">計算（kensho/calc07.py ⑥）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>候補</th><th class="mid">買い</th><th class="mid">払い</th><th class="mid">差引</th><th>中身</th></tr></thead>
<tbody>
<tr class="hi"><th><strong>小出の関係</strong>（荷電レプトン）</th><td class="mid"><strong>16.7</strong></td><td class="mid">10.0</td><td class="mid"><strong>\(+6.8\)</strong></td><td>\((\sum m)/(\sum\sqrt{m})^2 = 2/3\)、ずれ \(9.2\times10^{-6}\)</td></tr>
<tr><th>\(b\)–\(\tau\) 統一</th><td class="mid">3.9</td><td class="mid">4.9</td><td class="mid">\(-1.0\)</td><td>大統一で \(m_b/m_\tau \to 1\)、10 % 以内</td></tr>
<tr><th>量子レプトン相補性</th><td class="mid">4.9</td><td class="mid">6.6</td><td class="mid">\(-1.7\)</td><td>\(\theta_C+\theta_{12} = 46.5^\circ\)（\(45^\circ\) から \(1.5^\circ\)）</td></tr>
<tr><th>\(\theta_{13} \approx \theta_C/\sqrt2\)</th><td class="mid">6.1</td><td class="mid">8.2</td><td class="mid">\(-2.1\)</td><td>予言 \(9.22^\circ\)、実測 \(8.57^\circ\)</td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>採点の結果</h2>
<p><strong>生き残るのは、小出の関係だけでした。</strong> 5〜6 桁合っていて、探索空間を引いても黒字。</p>
<p><em>角度の関係は、全部が探索の値段で消えます。</em>「それっぽく見える」のは、候補が多すぎるからです（第13回）。</p>
<p>→ <strong>圧縮を探すなら、まず荷電レプトンの質量。</strong> ここだけが数字で残っています。</p>
</div>

<h2><span class="n">06</span>三本の道</h2>

<p>第1回で「三つの軸」を作りました。目標に対して、それぞれが道になります。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>道</th><th>やること</th><th>手がかり</th><th>見込み</th></tr></thead>
<tbody>
<tr><th>A 記述長を下げる</th><td>荷電レプトン質量の関係を説明する</td><td><strong>小出の関係だけが残っている</strong></td><td>難しい。50 年誰もできていない</td></tr>
<tr><th>B 計算量を下げる</th><td>強結合領域の新しい記法を探す</td><td>ブートストラップ、大 \(N\)、AdS/CFT</td><td>専門家が大勢いる</td></tr>
<tr class="hi"><th><strong>C 前提概念を下げる</strong></th><td><strong>既知の物理を、少ない前提で組み直す</strong></td><td><strong>三つの通貨、三つのふるい、厳密性のフィルタ</strong></td><td><strong>空いている。一人でできる</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">道の選び方</span>
<p><strong>A は運が要ります。B は設備と人数が要ります。C は要りません。</strong></p>
<p>そして C の成果は、<em>A と B の両方を助けます</em> ── 前提が少ないほど、探しやすくなるから。</p>
</div>

<h2><span class="n">07</span>15 回でやったのは、C の道だった</h2>

<p>このシリーズ自体が、第三の軸の実例になっています。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>回</th><th>置き換えた前提概念</th><th>新しい前提</th></tr></thead>
<tbody>
<tr><th>第1〜4回</th><td>「簡単」をめぐる議論</td><td><strong>三つの通貨（記述長・計算量・前提概念）</strong></td></tr>
<tr><th>第7回</th><td>「意味不明な定数」をめぐる議論</td><td><strong>三つのふるい（純粋な数か・\(O(1)\) 倍か・無次元か）</strong></td></tr>
<tr><th>第8〜9回</th><td>「近似 対 厳密」の議論</td><td><strong>三分類 ＋「答えが整数かゼロか」</strong></td></tr>
<tr><th>第10回</th><td>「なぜ解けないのか」の議論</td><td><strong>コールマン–マンデュラの四つの仮定</strong></td></tr>
<tr class="hi"><th>第12〜15回</th><td>「整数比は見つかるか」の議論</td><td><strong>「閉じた道を数えているか」の一言</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>新しい物理は一つも使っていません。順序と記法だけです。</strong></p>

<h2><span class="n">08</span>15 回を、一枚に</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">部</th><th class="mid">回</th><th>結論</th></tr></thead>
<tbody>
<tr><th class="mid">第 I 部</th><td class="mid">1〜4</td><td>「簡単」は三つあり、独立。計算がいちばん安い通貨</td></tr>
<tr><th class="mid">第 II 部</th><td class="mid">5〜7</td><td>強い力は四層に切れる。持ち込んだ定数 12 個は全部落ちる</td></tr>
<tr><th class="mid">第 III 部</th><td class="mid">8〜11</td><td>厳密値は整数と \(\pi\) しかない。解けないのは定理の帰結</td></tr>
<tr class="hi"><th class="mid">第 IV 部</th><td class="mid">12〜15</td><td><strong>整数は「閉じた道を数える」ところにだけある</strong></td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>一文にすると</h2>
<p><strong>物理を簡単にする道は三本あって、そのうち二本は塞がっている。</strong></p>
<p>残る一本 ── <em>前提概念を減らすこと</em> ── は、新しい物理も設備も要らず、まだ誰も最適化していません。</p>
<p>そして<strong>厳密が欲しいなら、問いを「いくつあるか」に書き換えること。</strong> 閉じた道を数えているところにだけ、整数と厳密があります。</p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>02節のパラメータ数の推移は<strong>数え方に幅があります</strong>（マヨラナ位相、宇宙論の従属パラメータ）。ただし「1973 年が底で、その後増えた」という向きは変わりません。<br>03節の圧縮率は「PDG の約 3000 項目」という粗い見積もりで、桁の話としてだけ読んでください。<br>05節の払い \(\log_2 M\) は<strong>筆者の見積もり</strong>です。小出の 1000 通りを 10 万通りにすれば黒字は消えます ── <em>この一点で結論がひっくり返る</em>ことを明記しておきます。<br>そして 07節は<strong>自画自賛の危険があります</strong>。本シリーズの道具が実際に前提を減らしたかは、<em>読者にしか判定できません</em>。筆者が測ると必ず良く出ます。</p>
</div>

<div class="next">
<span class="lbl">この先</span>
<p>04節の 12 個 ── フェルミオンの質量 ── が、残った最大の的です。<strong>そこに関係が「在る」か「無い」かは、まだ誰も知りません。</strong> 探すときは第13回の採点を先にかけてください。それが、このシリーズから持ち帰れるいちばん実用的な道具です。</p>
</div>'''

build(out='../butsuri-kantan-16-where-we-are.html', acc='#2a3a5a', ops='#7a5a3a',
      title='第16回：現在地と、三本の道 ── 物理を簡単にする',
      ep='第 16 回 ／ 最終回',
      eyebrow='パラメータは増え続けている。それでも比では勝っている',
      h1='現在地と、<br>三本の道',
      sub='残った非圧縮性の半分以上は、フェルミオンの質量と混合。<br><em>数字で生き残っている候補は、一つだけでした。</em>',
      byline_l='必要な予備知識：第1〜15回',
      byline_r='検証：kensho/calc07.py（および calc01〜06）',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第16回（最終回）です。01節の統一の歴史、04節のパラメータの内訳、05節の四つの候補（小出の関係、\\(b\\)–\\(\\tau\\) 統一、量子レプトン相補性、\\(\\theta_{13}\\approx\\theta_C/\\sqrt2\\)）はいずれも<strong>よく知られた事実</strong>です。<em>「三つの軸」「三本の道」「探索空間を引いてから採点する」という枠組みは本シリーズのもの</em>で、教科書の主張ではありません（kensho/calc07.py）。<strong>02節の数え方には幅があり</strong>、03節は粗い見積もりです。<strong>05節の \\(\\log_2 M\\) は筆者の見積もりで、この一点で結論が変わります</strong>。07節は自己評価であり、読者の判断に委ねます。<strong>本シリーズは既存の物理に新しい主張を加えるものではありません</strong> ── 扱った物理はすべて確立した標準的な内容で、新しいのは測り方だけです。</p>')
