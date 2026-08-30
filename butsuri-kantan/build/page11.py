# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">前回、「QCD は可積分になりえない」と分かりました。では厳密なのは整数だけなのか ── <strong>いいえ。「関係」があります。</strong> どれも値については何も言わず、量と量の<em>間</em>だけを言う。そして驚くことに、<strong>関係だけで数値が 7 桁決まる</strong>例が実際にあります。</p>

<h2><span class="n">01</span>QCD で厳密に成り立つ「関係」</h2>

<div class="calc">
<span class="tag">計算（kensho/calc05.py ⑥）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>厳密な関係</th><th>中身</th><th>出どころ</th></tr></thead>
<tbody>
<tr><th>くりこみ群方程式</th><td>\(\mu\,dG/d\mu = \beta(G)\) ── <strong>全次数で厳密</strong></td><td>スケール不変性</td></tr>
<tr><th>ワード–高橋恒等式</th><td>厳密</td><td>ゲージ対称性</td></tr>
<tr><th>ユニタリ性（光学定理）</th><td>\(\mathrm{Im}\,f(0) = (k/4\pi)\sigma\) ── 厳密</td><td>確率の保存</td></tr>
<tr><th>交叉対称性</th><td>厳密</td><td>解析性</td></tr>
<tr><th>分散関係</th><td>厳密</td><td>因果律</td></tr>
<tr><th>Adler–Bardeen 定理</th><td>アノマリーは<strong>1 ループで完全</strong></td><td>位相</td></tr>
<tr class="hi"><th>'t Hooft のアノマリー整合</th><td><strong>強結合のスペクトルを厳密に縛る</strong></td><td>位相</td></tr>
<tr><th>Vafa–Witten 定理</th><td>ベクトル的対称性は<strong>自発的に破れない</strong></td><td>正定値性</td></tr>
<tr><th>Weingarten 不等式</th><td>\(m_\pi \le m_N\) など ── 厳密</td><td>正定値性</td></tr>
<tr><th>演算子積展開（OPE）</th><td>漸近的に厳密</td><td>スケール分離</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">共通点</span>
<p><strong>どれも、値については何も言いません。関係だけを言います。</strong></p>
<p>QCD の厳密な内容は、<em>量ではなく、量と量の間にありました。</em></p>
</div>

<p>とくに 't Hooft のアノマリー整合は驚くべきものです。<strong>何も解かずに、強結合領域のスペクトルに条件を課します</strong> ── 高エネルギー側のアノマリー係数と低エネルギー側のそれが一致しなければならない、というだけで、「閉じ込めが起きているなら、こういう粒子がなければおかしい」が出る。</p>

<h2><span class="n">02</span>関係だけで、数値が決まることがある</h2>

<p>共形ブートストラップという方法があります。<strong>ラグランジアンを使いません。</strong></p>

<div class="keybox">
<span class="lbl">入力はこれだけ</span>
<p><strong>交叉対称性 ＋ ユニタリ性 ＋ 演算子が有限個</strong></p>
<p>粒子の一覧も、結合定数も、作用も要りません。</p>
</div>

<div class="calc">
<span class="tag">計算（kensho/calc05.py ⑦）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">値</th><th class="mid">誤差</th><th>検算</th></tr></thead>
<tbody>
<tr class="hi"><th>3 次元イジング \(\nu\)</th><td class="mid"><strong>0.6299709</strong></td><td class="mid">\(4\times10^{-7}\)</td><td>格子 0.63002 と一致</td></tr>
<tr><th>3 次元イジング \(\eta\)</th><td class="mid">0.0362978</td><td class="mid">\(2\times10^{-7}\)</td><td>同上</td></tr>
<tr><th>3 次元イジング \(\omega\)</th><td class="mid">0.8303</td><td class="mid">\(1\times10^{-3}\)</td><td>同上</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">この回のいちばん重要な点</span>
<p><strong>模型ゼロ、パラメータゼロ、近似ゼロで 7 桁。</strong></p>
<p>しかも誤差は<em>近似の誤差ではありません</em> ── <strong>厳密な不等式の幅</strong>です。値が厳密な区間に閉じ込められている。</p>
</div>

<p>これが「近似ではなく厳密に」のいちばん近い実現です。<em>量そのものは閉じた形を持たないが、厳密に囲い込める。</em></p>

<h2><span class="n">03</span>経験による裏づけ ── 厳密な主張ほど、よく検証されている</h2>

<p>「厳密を狙え」という直感には、数字の裏づけがあります。<strong>厳密な主張は、計算した実数より桁違いに厳しい試験に通されています。</strong></p>

<div class="calc">
<span class="tag">計算（kensho/calc05.py ⑧）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>検証された主張</th><th class="mid">精度</th><th>種類</th><th class="mid">ビット</th></tr></thead>
<tbody>
<tr class="hi"><th>光子質量 \(m_\gamma/m_e\)</th><td class="mid">\(&lt;2\times10^{-24}\)</td><td><strong>厳密（ゼロ）</strong></td><td class="mid"><strong>79</strong></td></tr>
<tr class="hi"><th>電荷の中性 \(|q_p+q_e|/e\)</th><td class="mid">\(&lt;10^{-21}\)</td><td><strong>厳密（整数）</strong></td><td class="mid"><strong>70</strong></td></tr>
<tr class="hi"><th>CPT：\(|m_K - m_{\bar K}|/m_K\)</th><td class="mid">\(&lt;6\times10^{-19}\)</td><td><strong>厳密（対称性）</strong></td><td class="mid"><strong>61</strong></td></tr>
<tr><th>電子 \(g-2\)（理論 対 実験）</th><td class="mid">\(10^{-10}\)</td><td>計算した実数（摂動）</td><td class="mid">33</td></tr>
<tr><th>\(\mu\) の \(g-2\) のハドロン部分</th><td class="mid">\(10^{-9}\)</td><td>計算した実数（強結合込み）</td><td class="mid">30</td></tr>
<tr><th>格子のハドロン質量</th><td class="mid">\(10^{-2}\)</td><td>計算した実数（強結合）</td><td class="mid">7</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">きれいな三段</span>
<p>厳密な主張（整数・ゼロ）　　<strong>70 ビット</strong><br>
摂動で計算した実数　　　　<strong>33 ビット</strong><br>
強結合で計算した実数　　　<strong>7 ビット</strong></p>
<p><strong>厳密なものは、計算した実数より 37 ビット（11 桁）よく検証されています。</strong></p>
</div>

<h2><span class="n">04</span>第 III 部のまとめ ── 目標への道筋</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">段</th><th>やること</th><th>得られるもの</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">1</th><td><strong>整数かゼロに落とす</strong>（「いくつあるか」「消えるか」に問いを変える）</td><td><strong>厳密。20 桁で検証できる</strong></td></tr>
<tr class="hi"><th class="mid">2</th><td><strong>厳密な関係を積む</strong>（値ではなく拘束を書く）</td><td><strong>厳密。値を知らなくても成り立つ</strong></td></tr>
<tr class="hi"><th class="mid">3</th><td><strong>関係で囲い込む</strong>（ブートストラップ）</td><td><strong>厳密な区間。7 桁</strong></td></tr>
<tr><th class="mid">4</th><td>制御された近似で詰める</td><td>任意精度。1 桁 \(=\) 1000 倍</td></tr>
<tr><th class="mid">5</th><td>制御されていない近似</td><td><strong>改良できない</strong></td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>第 III 部の結論</h2>
<p><strong>第 II 部は 5 段目から始めていました。</strong> 「これだと単なる近似だ」という不満は、もっともでした。</p>
<p>そして <strong>1〜3 段目は、計算機を一台も使わずにできます。</strong></p>
<p>残された厳密性は二種類だけ ── <em>(a) 答えが整数かゼロになる問い、(b) 値を言わない、量どうしの関係。</em></p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>02節のブートストラップの「誤差」は厳密な区間ですが、<strong>数値的に得た区間</strong>です。区間が閉じることの証明は、計算の中身に依存しています。<br>03節の精度の比較は、<em>測っているものが違います</em>（対称性の破れの上限 対 値の一致）。三段の順序は頑健ですが、ビット数を直接比べるのは乱暴です。<br>4 次元の \(S\) 行列ブートストラップは<strong>いま進行中の前線</strong>で、QCD の質量比を 7 桁で囲い込めているわけではありません。</p>
</div>

<div class="next">
<span class="lbl">次回から第 IV 部</span>
<p>「全部を単純な整数の比で書きたい」── この願いには、<strong>物理でいちばん長い実績</strong>があります。そして成功例を並べると、驚くことに<em>全部が「距離の比」</em>でした。</p>
</div>'''

build(out='../butsuri-kantan-11-relations.html', acc='#4a2f52', ops='#8a5a1a',
      title='第11回：厳密なのは、値ではなく関係 ── 物理を簡単にする',
      ep='第 11 回 ／ 第 III 部 厳密とは何か（部の終わり）',
      eyebrow='関係だけで 7 桁決まる ── しかも誤差は厳密な区間の幅',
      h1='厳密なのは、<br>値ではなく関係',
      sub='QCD の厳密な内容は、量ではなく量と量の間にありました。<br><em>そして厳密な主張は、計算した実数より 11 桁よく検証されています。</em>',
      byline_l='必要な予備知識：第10回（コールマン–マンデュラ）',
      byline_r='検証：kensho/calc05.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第11回（第 III 部の終わり）です。くりこみ群方程式、ワード–高橋恒等式、\'t Hooft のアノマリー整合、Vafa–Witten 定理、共形ブートストラップの 3 次元イジング結果、および 03節の実験上限はいずれも<strong>確立した標準的な内容</strong>です。<em>「厳密なのは値ではなく関係」という整理と、03節の三段の並べ方は本シリーズのもの</em>です（kensho/calc05.py）。<strong>03節は測っているものが違う量を同じ単位で並べており</strong>、順序は頑健ですがビット数の直接比較は乱暴です。<strong>4 次元の \\(S\\) 行列ブートストラップは進行中の研究</strong>で、QCD の質量比を高精度で囲い込めているわけではありません。</p>')
