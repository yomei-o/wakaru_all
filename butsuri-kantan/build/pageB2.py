# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第9回で「厳密値を全部集めたら、<strong>整数と \(\pi\) しかなかった</strong>」と書きました。そのとき「網羅的な調査ではない」と断りましたが ── <em>実際に反例がありました</em>。しかも例外ではなく、<strong>一つの族</strong>でした。ただし、境目そのものは動きませんでした。</p>

<h2><span class="n">01</span>反例その一 ── 黒体輻射に \(\zeta(3)\) が出る</h2>

<p>空洞の中の光子の<em>数</em>密度は、厳密に次の形をしています。</p>

<div class="keybox">
<span class="lbl">黒体輻射の光子数密度</span>
<p>\[n_\gamma = \frac{2\zeta(3)}{\pi^2}\left(\frac{k_BT}{\hbar c}\right)^3\]</p>
</div>

<p>\(\zeta(3) = \sum_n 1/n^3\)。自由場のボーズ積分から出る、<strong>まぎれもない厳密値</strong>です。近似は一つも入っていません。</p>

<div class="calc">
<span class="tag">計算（kensho/calc09.py ②）</span>
<p>\(\sum 1/n^3\) を 400 万項： \(\zeta(3) = \mathbf{1.202056903}\)（参考値と \(5\times10^{-11}\) 一致）</p>
</div>

<p>ところが \(\zeta(3)\) は、<strong>\(\pi\) の有理数倍ではありません</strong>。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid"></th><th class="mid">値</th><th class="mid">閉じた形</th></tr></thead>
<tbody>
<tr><th class="mid">\(\zeta(2)\)</th><td class="mid">1.644934067</td><td class="mid">\(\pi^2/6\)</td></tr>
<tr class="hi"><th class="mid">\(\zeta(3)\)</th><td class="mid"><strong>1.202056903</strong></td><td class="mid"><strong>\(\pi\) では書けない</strong></td></tr>
<tr><th class="mid">\(\zeta(4)\)</th><td class="mid">1.082323234</td><td class="mid">\(\pi^4/90\)</td></tr>
</tbody>
</table>
</div>

<p><strong>偶数だけが \(\pi\) の冪になります。</strong> 奇数は名前つきの新しい定数で、\(\zeta(3)\)（アペリーの定数）が無理数であることは 1978 年に証明されましたが、<em>\(\pi\) との閉じた関係は知られていません</em>。</p>

<h2><span class="n">02</span>反例その二 ── 2 次元イジングにカタラン定数</h2>

<p>第9回では「2 次元イジングの臨界指数は \(\nu=1\)、\(\beta=1/8\)、\(\eta=1/4\) ── 全部きれいな有理数」と書きました。ところが<strong>自由エネルギーそのもの</strong>を見ると、話が変わります。</p>

<div class="keybox">
<span class="lbl">オンサーガーの厳密解（正方格子、臨界点）</span>
<p>\[-\beta f = \ln 2 + \frac{1}{8\pi^2}\iint \ln\!\left[2-\cos\theta_1-\cos\theta_2\right]d\theta_1 d\theta_2\]</p>
<p>この積分の値は \(\;\dfrac{\ln 2}{2} + \dfrac{2G}{\pi}\;\) ── \(G\) は<strong>カタラン定数</strong>。</p>
</div>

<div class="calc">
<span class="tag">計算（kensho/calc09.py ③）</span>
<p>数値積分（\(3000\times3000\) 点）　　\(-\beta f = \mathbf{0.929695}\)<br>
\(\ln2/2 + 2G/\pi\)　　　　　　　　\(-\beta f = \mathbf{0.929695}\)<br>
差 \(= 3.9\times10^{-8}\)　── <strong>7 桁一致</strong></p>
<p>カタラン定数 \(G = \mathbf{0.915965594}\)</p>
</div>

<p>カタラン定数も \(\pi\) の有理数倍ではありません。それどころか ── <strong>無理数かどうかすら証明されていません</strong>。</p>

<h2><span class="n">03</span>これは例外ではなく、族だった</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">厳密値</th><th class="mid">含む定数</th><th>出どころ</th></tr></thead>
<tbody>
<tr class="hi"><th>黒体の光子数</th><td class="mid">\(2\zeta(3)/\pi^2\)</td><td class="mid"><strong>\(\zeta(3)\)</strong></td><td>自由場のボーズ積分</td></tr>
<tr><th>黒体のエントロピー</th><td class="mid">\(\propto \zeta(4)=\pi^4/90\)</td><td class="mid">\(\pi\) の冪</td><td>同上（偶数なので \(\pi\)）</td></tr>
<tr class="hi"><th>2 次元イジング臨界自由エネルギー</th><td class="mid">\(\ln2/2 + 2G/\pi\)</td><td class="mid"><strong>カタラン \(G\)</strong></td><td>可解模型</td></tr>
<tr><th>2 次元イジング自発磁化</th><td class="mid">\((1-k^2)^{1/8}\)</td><td class="mid">有理数の冪</td><td>可解模型</td></tr>
<tr><th>デバイ模型の低温比熱</th><td class="mid">\(\propto \pi^4/5\)</td><td class="mid">\(\pi\) の冪</td><td>自由場</td></tr>
<tr class="hi"><th>3 ループの \(\beta\) 関数係数</th><td class="mid">\(\zeta(3)\) を含む</td><td class="mid"><strong>\(\zeta(3)\)</strong></td><td><strong>多ループ積分</strong></td></tr>
</tbody>
</table>
</div>

<p>最後の行が示唆的です。<strong>多ループのファインマン積分には \(\zeta(3)\)、\(\zeta(5)\) が普通に出ます</strong>（多重ゼータ値と呼ばれる族）。つまり反例は珍しいものではなく、<em>ある高さから上では標準的</em>でした。</p>

<div class="aside">
<span class="tag">第15回とつながる</span>
<p>第15回で「\(\beta\) 関数の係数 \(b_0=9\)、\(b_1=64\) は整数」と驚きました。<strong>ところが 3 ループの \(b_2\) には \(\zeta(3)\) が入ります。</strong><br>「結合定数の走り方は単純な整数で決まる」は、<em>2 ループまでの話</em>でした。ここも第15回の記述を一段細かくする必要があります。</p>
</div>

<h2><span class="n">04</span>主張を、正しく書き直す</h2>

<div class="record">
<h2>訂正</h2>
<p>× 「厳密値は<strong>整数・有理数・\(\pi\) の有理数倍</strong>しかない」</p>
<p>○ <strong>「厳密値は必ず<em>閉じた形</em>を持つ」</strong></p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>値の型</th><th>出どころ</th><th>例</th></tr></thead>
<tbody>
<tr><th>整数・有理数</th><td>数え上げ・群論・位相</td><td>\(N_c=3\), \(C_F=4/3\), \(b_0=9\)</td></tr>
<tr><th>\(\pi\) の有理数倍</th><td>自由場のガウス積分</td><td>\(A/4\), \(-\pi/12\), \(\pi^2/60\)</td></tr>
<tr class="hi"><th><strong>名前つきの定数</strong></th><td><strong>自由場でも高次／可解模型</strong></td><td><strong>\(\zeta(3)\)、カタラン \(G\)</strong></td></tr>
<tr><th>代数的数</th><td>可解模型の指数</td><td>\((1-k^2)^{1/8}\)</td></tr>
<tr><td colspan="3" class="mid">────── ここから先 ──────</td></tr>
<tr class="hi"><th><strong>閉じた形なし</strong></th><td><strong>相互作用を実際に解いた答え</strong></td><td><strong>\(m_p/\sqrt\sigma\)、3 次元イジング \(\nu\)</strong></td></tr>
</tbody>
</table>
</div>

<h2><span class="n">05</span>境目は、動かなかった</h2>

<div class="keybox">
<span class="lbl">反例が広げたのは、境目の「上側」だけ</span>
<p>\(\zeta(3)\) もカタラン \(G\) も、<strong>式で書けます</strong> ── 無限級数として定義されている。数値がいくらでも欲しい桁まで出せる。</p>
<p>一方 \(m_p/\sqrt\sigma = 2.13\dots\) は、<strong>数値でしか知られていません</strong>。級数も積分も、それを与える式が一つも書かれていない。</p>
</div>

<p>つまり第9回の<strong>分類の境目 ── 相互作用を実際に解いたかどうか ── は、そのまま生きています</strong>。直すべきだったのは「整数と \(\pi\) しかない」という<em>言い方</em>の方でした。</p>

<p>そして第9回の実務的な結論 ── <strong>「量はいくつか」ではなく「いくつあるか」と問え</strong> ── も変わりません。整数を狙う理由は、\(\pi\) しか出ないからではなく、<em>整数が数え上げから来るから</em>でした。</p>

<h2><span class="n">06</span>この訂正から持ち帰るもの</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>やったこと</th><th>効果</th></tr></thead>
<tbody>
<tr><th>「例外なく」と書いた箇所を疑う</th><td>網羅していない主張は、<strong>必ず反例が出る</strong></td></tr>
<tr class="hi"><th><strong>反例を探しにいく</strong></th><td><strong>2 件見つかり、しかも族だった</strong></td></tr>
<tr><th>境目が動いたか確かめる</th><td>動いていない ── <em>言い方だけが誤り</em>だった</td></tr>
</tbody>
</table>
</div>

<p>番外編①（\(\tau\) 質量の誤差）と合わせて、<strong>本編には二箇所の上振れがありました</strong>。どちらも<em>結論は変わらず、根拠の言い方が誤っていた</em>という型です。</p>

<div class="caveat">
<span class="tag">正直な線</span>
<p>\(\zeta(3)\) が \(\pi\) の冪で書けないことは、<strong>証明されていません</strong>（無理数であることは証明済みですが、\(\pi\) との関係は未解決）。250 年探して見つかっていない、という状況証拠があるだけです。<br>02節の数値積分は対数特異点を含むため収束が遅く、<em>主張しているのは 7 桁の一致</em>です。<br>04節の「閉じた形を持つ」にも<strong>厳密な定義はありません</strong>（何を「閉じた」と呼ぶかは規約）。ただし \(\zeta(3)\) と \(m_p/\sqrt\sigma\) の間には<em>「定義する式があるか」という明確な差</em>があります。<br>そして ── <strong>この番外編もまた網羅的ではありません</strong>。「閉じた形を持つ」に対する反例が将来出る可能性は残っています。</p>
</div>

<div class="next">
<span class="lbl">この先</span>
<p>03節の最後の行 ── <strong>3 ループの \(\beta\) 関数に \(\zeta(3)\) が入る</strong> ── は、第15回の「境目は一本」をもう一段細かくします。<em>群論・位相からは整数、自由場の低次からは \(\pi\)、高次からは \(\zeta\)、そして相互作用を解くと閉じた形が消える。</em> 境目は一本ではなく、<strong>階段</strong>だったのかもしれません。</p>
</div>'''

build(out='../butsuri-kantan-b2-zeta.html', acc='#5a3a6a', ops='#8a5a1a',
      title='番外編②：厳密値に、π 以外の定数が出る ── 物理を簡単にする',
      ep='番外編 ② ／ 第9回の訂正',
      eyebrow='ζ(3) とカタラン定数 ── 反例は例外ではなく族だった',
      h1='厳密値に、<br>\\(\\pi\\) 以外の定数が出る',
      sub='第9回の「整数と \\(\\pi\\) しかない」には反例がありました。<br><em>ただし境目そのものは、動きませんでした。</em>',
      byline_l='必要な予備知識：第9回（厳密値のフィルタ）',
      byline_r='検証：kensho/calc09.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ番外編②です。<strong>本編第9回の記述（「厳密値は整数と \\(\\pi\\) しかない」）の訂正を含みます</strong>。黒体輻射の光子数密度に \\(\\zeta(3)\\) が現れること、オンサーガーの臨界自由エネルギーにカタラン定数が現れること、多ループ積分に多重ゼータ値が現れることは、いずれも<strong>確立した標準的な内容</strong>です ── 本シリーズが見落としていました。数値確認は kensho/calc09.py で行いました。<strong>\\(\\zeta(3)\\) が \\(\\pi\\) の冪で書けないことは証明されていません</strong>。<strong>「閉じた形」にも厳密な定義はありません</strong>。この番外編も網羅的ではなく、さらなる反例の可能性は残ります。</p>')
