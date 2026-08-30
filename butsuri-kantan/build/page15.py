# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">整数がある場所と無い場所の境目を、QCD の中で全部並べます。<strong>境目は一本しかありませんでした</strong> ── 群論・位相から来たか、動力学から来たか。そして驚くべきことに、<em>結合定数の走り方は、単純な整数で決まっています</em>。「強い力は汚い」のは、走り方ではなくスペクトルの話でした。</p>

<h2><span class="n">01</span>全部並べる</h2>

<div class="calc">
<span class="tag">計算（kensho/calc06.py ⑨）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">値</th><th class="mid">型</th><th>出どころ</th></tr></thead>
<tbody>
<tr><th>色の数 \(N_c\)</th><td class="mid">\(3\)</td><td class="mid"><strong>整数</strong></td><td>群論</td></tr>
<tr><th>カシミール \(C_A\)</th><td class="mid">\(3\)</td><td class="mid"><strong>整数</strong></td><td>群論</td></tr>
<tr><th>カシミール \(C_F\)</th><td class="mid">\(4/3\)</td><td class="mid"><strong>有理数</strong></td><td>群論</td></tr>
<tr><th>\(T_F\)</th><td class="mid">\(1/2\)</td><td class="mid"><strong>有理数</strong></td><td>群論</td></tr>
<tr class="hi"><th>\(\beta\) 関数 \(b_0\)（\(n_f=3\)）</th><td class="mid">\(11-2 = \mathbf{9}\)</td><td class="mid"><strong>整数</strong></td><td>1 ループの計算</td></tr>
<tr class="hi"><th>\(\beta\) 関数 \(b_1\)（\(n_f=3\)）</th><td class="mid">\(102-38 = \mathbf{64}\)</td><td class="mid"><strong>整数</strong></td><td>2 ループの計算</td></tr>
<tr><th>\(\langle \mathbf{S}_i\cdot\mathbf{S}_j\rangle\)</th><td class="mid">\(-3/4, +1/4\)</td><td class="mid"><strong>有理数</strong></td><td>スピンの合成</td></tr>
<tr><th>アノマリー係数</th><td class="mid">\(1\)</td><td class="mid"><strong>整数</strong></td><td>位相</td></tr>
<tr><th>アドラー和則</th><td class="mid">\(2\)</td><td class="mid"><strong>整数</strong></td><td>カレント代数</td></tr>
<tr><td colspan="4" class="mid">──────────</td></tr>
<tr><th>\(m_p/m_\rho\)</th><td class="mid">\(1.211\dots\)</td><td class="mid"><strong>生の実数</strong></td><td><strong>動力学</strong></td></tr>
<tr><th>\(m_p/\sqrt{\sigma}\)</th><td class="mid">\(2.13\dots\)</td><td class="mid"><strong>生の実数</strong></td><td><strong>動力学</strong></td></tr>
<tr><th>グルーボール\(/\sqrt{\sigma}\)</th><td class="mid">\(3.405\dots\)</td><td class="mid"><strong>生の実数</strong></td><td><strong>動力学</strong></td></tr>
<tr><th>レッジェ傾き \(\alpha'\)</th><td class="mid">\(0.88\dots\) GeV\(^{-2}\)</td><td class="mid"><strong>生の実数</strong></td><td><strong>動力学</strong></td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>境目は一本だけ</h2>
<p><strong>群論・位相から来たもの → 例外なく厳密な整数か有理数。</strong><br>
<strong>動力学から来たもの → 例外なく生の実数。</strong></p>
<p>中間はありません。</p>
</div>

<h2><span class="n">02</span>いちばん驚いてよいのは、\(b_0 = 9\)</h2>

<p>\(\beta\) 関数の係数は、結合定数がエネルギーとともにどう走るかを決めます。<em>これは力学的な量に見えます</em> ── 実際、量子補正の計算から出てくる。</p>

<div class="keybox">
<span class="lbl">それでも整数だった</span>
<p>\[b_0 = 11 - \frac{2n_f}{3},\qquad b_1 = 102 - \frac{38 n_f}{3}\]</p>
<p>\(n_f = 3\) なら \(b_0 = \mathbf{9}\)、\(b_1 = \mathbf{64}\)。</p>
</div>

<p>グルーオンのループから \(11\)、クォークのループから \(-2n_f/3\)。どちらも<strong>群論の因子と、有限個の積分の組み合わせ</strong>で、答えは有理数になります。</p>

<div class="keybox">
<span class="lbl">つまり</span>
<p><strong>結合定数の走り方は、単純な整数で決まっています。</strong></p>
<p>「強い力は汚い」のは、走り方ではなく<em>スペクトル</em>の話でした。</p>
</div>

<p>第5回を思い出してください。\(\Lambda = \mu\exp(-2\pi/(b_0\alpha_s))\) で、原子核のスケールが決まりました。<strong>その指数の中身は整数 9 です。</strong> 汚いのは \(\alpha_s\) の値の方 ── そしてそれは第7回で見たとおり、<em>単位の選択</em>です。</p>

<h2><span class="n">03</span>なぜ、動力学だと駄目なのか</h2>

<p>第10回とつながります。整数比が出るには、答えが<strong>代数的な構造</strong>から出てこなければなりません。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>答えの出どころ</th><th>答えの型</th><th>なぜ</th></tr></thead>
<tbody>
<tr><th>数え上げ・位相</th><td><strong>整数</strong></td><td>個数だから</td></tr>
<tr><th>群の表現論</th><td><strong>有理数</strong></td><td>カシミールは有理数</td></tr>
<tr><th>有限個の積分</th><td><strong>有理数 × \(\pi^n\)</strong></td><td>ガウス積分は解ける</td></tr>
<tr><th>可解な固有値問題</th><td><strong>有理数</strong></td><td>水素の \(1/n^2\)</td></tr>
<tr class="hi"><th><strong>可積分でない系の固有値</strong></th><td><strong>生の実数</strong></td><td><strong>代数的な関係を持たない</strong></td></tr>
</tbody>
</table>
</div>

<p>いちばん下が QCD のスペクトルです。<strong>第10回の定理により、QCD は可積分になりえません。</strong> だから固有値が代数的な関係を持つ理由が無い。</p>

<div class="aside">
<span class="tag">第10回と第12回がここで合流する</span>
<p>第10回：<em>QCD は可積分になりえない</em>（コールマン–マンデュラ）。<br>第12回：<em>整数が出るのは閉じたものを数えているとき</em>。<br>この回：<em>だから QCD のスペクトルには整数比が無い</em>。</p>
<p><strong>三つは同じ一つのことを、別の側から言っています。</strong></p>
</div>

<h2><span class="n">04</span>第 IV 部のまとめ ── 実行手順</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>手順</th><th>中身</th><th>得られるもの</th></tr></thead>
<tbody>
<tr class="hi"><th>① 閉じた道を探す</th><td>一周して戻るもの（位相、回転、巻きつき）</td><td><strong>そこに必ず整数がある</strong></td></tr>
<tr class="hi"><th>② 数える対象に言い換える</th><td>「量はいくつか」→「何個入るか」</td><td><strong>整数比が出る</strong></td></tr>
<tr class="hi"><th>③ 混合を疑う</th><td>汚い数は、きれいな数の平均かもしれない</td><td><strong>分解できれば整数に戻る</strong></td></tr>
<tr class="hi"><th>④ 群論・位相の量を選ぶ</th><td>カシミール、\(\beta\) 係数、アノマリー</td><td><strong>厳密な有理数</strong></td></tr>
<tr><th><strong>⑤ 動力学の値には手を出さない</strong></th><td>ハミルトニアンの固有値</td><td><strong>整数比になった前例がゼロ</strong></td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>第 IV 部の結論</h2>
<p><strong>①〜④だけで、驚くほど広い範囲が整数比で書けます。</strong> しかも計算機は一台も要りません。</p>
<p>そして⑤ ── <em>動力学の値が整数比にならないのは、第10回の定理の帰結です。</em></p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>01節の「動力学は例外なく生の実数」は、<strong>知られている限り</strong>の主張です。2 次元や超対称の系では、動力学の値も厳密になります（第10回①）。<br>02節で \(b_0, b_1\) が整数になるのは \(n_f=3\) のときで、\(n_f=5\) なら \(b_0 = 23/3\)（有理数）です。<em>整数か有理数かは \(n_f\) に依りますが、「有理数である」ことは変わりません</em>。<br>03節の表の「なぜ」は<strong>説明であって証明ではありません</strong> ── 可積分でない系の固有値が代数的関係を持たないことは、証明された定理ではなく観察です。</p>
</div>

<div class="next">
<span class="lbl">次回・最終回</span>
<p>目標に対する<strong>現在地</strong>を測ります。この 50 年、パラメータの数は<em>増え続けています</em>。それでも比を見ると勝っている。そして残った非圧縮性のうち、<strong>数字で生き残っている候補は一つだけ</strong>でした。</p>
</div>'''

build(out='../butsuri-kantan-15-the-line.html', acc='#7a3a2a', ops='#3a5a7a',
      title='第15回：境目は一本 ── 群論・位相 か 動力学 か ── 物理を簡単にする',
      ep='第 15 回 ／ 第 IV 部 整数比の探し方（部の終わり）',
      eyebrow='結合定数の走り方は、単純な整数で決まっている',
      h1='境目は一本<br>── 群論・位相 か 動力学 か',
      sub='\\(\\beta\\) 関数の係数は \\(b_0 = 9\\)、\\(b_1 = 64\\)。<br><em>「強い力は汚い」のは、走り方ではなくスペクトルの話でした。</em>',
      byline_l='必要な予備知識：第10回（定理）、第12〜14回',
      byline_r='検証：kensho/calc06.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第15回（第 IV 部の終わり）です。カシミール、\\(\\beta\\) 関数係数、アノマリー係数、アドラー和則、および格子で求められた質量比はいずれも<strong>確立した標準的な内容</strong>です。<em>「境目は群論・位相か動力学かの一本」という整理と、第10回・第12回との合流の読み方は本シリーズのもの</em>です（kensho/calc06.py）。<strong>「動力学は例外なく生の実数」は知られている限りの主張</strong>で、2 次元や超対称系では成り立ちません。<strong>03節の表は説明であって証明ではありません</strong>。\\(b_0, b_1\\) が整数になるのは \\(n_f=3\\) の場合です。</p>')
