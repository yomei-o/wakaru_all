# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">「計算量」は測れます。しかも、<em>精度と交換できる通貨</em>として測れます。電子の \(g-2\) を使うと、「ファインマン図を何枚描くと、精度が何桁上がるか」がきれいな直線に乗りました。そしてその<strong>為替レート</strong>を、パラメータの値段と比べると ── <em>計算はいちばん安い通貨</em>でした。</p>

<h2><span class="n">01</span>電子の \(g-2\) は、計算の値段が分かる唯一の題材</h2>

<p>電子の磁気能率は、ディラック方程式が \(g=2\) ちょうどを要求します。実際には少しずれていて、そのずれ \(a_e = (g-2)/2\) が量子電磁力学の計算で出ます。</p>

<p>この計算が特別なのは、<strong>次数ごとに「何枚の図を描いたか」が数えられている</strong>ことです。1 ループなら 1 枚、2 ループなら 7 枚、…と、はっきりした整数がついている。<em>計算の量が数字になる、めずらしい例です。</em></p>

<div class="calc">
<span class="tag">計算（kensho/calc01.py ②）</span>
<p class="lbl">次数ごとの図の数と、到達した精度</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">ループ</th><th class="mid">図の数</th><th class="mid">累積の図</th><th class="mid">相対誤差</th><th class="mid">精度ビット</th></tr></thead>
<tbody>
<tr><td class="mid">1</td><td class="mid">1</td><td class="mid">1</td><td class="mid">\(1.5\times10^{-3}\)</td><td class="mid">9.4</td></tr>
<tr><td class="mid">2</td><td class="mid">7</td><td class="mid">8</td><td class="mid">\(1.3\times10^{-5}\)</td><td class="mid">16.3</td></tr>
<tr><td class="mid">3</td><td class="mid">72</td><td class="mid">80</td><td class="mid">\(4.8\times10^{-8}\)</td><td class="mid">24.3</td></tr>
<tr><td class="mid">4</td><td class="mid">891</td><td class="mid">971</td><td class="mid">\(3.9\times10^{-10}\)</td><td class="mid">31.3</td></tr>
<tr class="hi"><td class="mid">5</td><td class="mid"><strong>12672</strong></td><td class="mid">13643</td><td class="mid">\(8.1\times10^{-12}\)</td><td class="mid"><strong>36.8</strong></td></tr>
</tbody>
</table>
</div>

<p>「精度ビット」は、相対誤差の \(-\log_2\) です。誤差が半分になると 1 ビット増える、という数え方。第 III 部までずっとこの単位を使います。</p>

<h2><span class="n">02</span>まず驚くのは、一枚目です</h2>

<div class="keybox">
<span class="lbl">1 ループ ＝ 図 1 枚 ＝ 紙 1 行</span>
<p>\(a_e \simeq \dfrac{\alpha}{2\pi} = 0.001161410\)　　実測 \(0.001159652\)</p>
<p><strong>3 桁合います。</strong> 図 1 枚、掛け算 1 回、それで <strong>9.4 ビット</strong>。</p>
</div>

<p>残りの 12,671 枚が買うのは、そこから先の 27 ビットです。<em>最初の一枚がいちばん儲かる</em> ── これは後で効いてきます。</p>

<h2><span class="n">03</span>直線に乗る</h2>

<p>「累積の図の数」の \(\log_2\) を横軸、精度ビットを縦軸に取ると、五つの点がきれいに並びます。最小二乗で直線を引くと：</p>

<div class="keybox">
<span class="lbl">為替レート</span>
<p>\[\text{精度ビット} = 10.24 + \mathbf{2.03}\times \log_2(\text{図の数})\]</p>
<p><strong>計算コスト 1 ビットにつき、精度が 2.03 ビット買える。</strong></p>
</div>

<p>つまり<em>計算は儲かります</em>。1 払って 2 返ってくる。図の枚数を倍にすると、精度は 4 倍良くなる計算です。</p>

<h2><span class="n">04</span>パラメータの値段と比べる</h2>

<p>比べる相手が要ります。「パラメータを 1 個増やす」ことの値段は、記述長側の標準的な数え方（BIC）で決まります ── データ点が \(N\) 個あるとき \(\tfrac12\log_2 N\) ビット。素粒子物理の標準的なデータ数（\(N \simeq 1700\)）なら：</p>

<div class="calc">
<span class="tag">計算（kensho/calc01.py ③）</span>
<p>パラメータ 1 個の値段 \(= \tfrac12\log_2 1701 = \mathbf{5.37}\) ビット</p>
</div>

<p>これで二つの通貨が並びました。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>買い方</th><th>払い</th><th>買えるもの</th><th>ほかの量は</th></tr></thead>
<tbody>
<tr><th>パラメータで買う</th><td class="mid">5.37 ビット</td><td>合わせた <strong>1 個の量だけ</strong></td><td>何も当たらない</td></tr>
<tr class="hi"><th><strong>計算で買う</strong></th><td class="mid"><strong>1 ビット</strong></td><td><strong>2.03 ビットの精度</strong></td><td><strong>全部同時に当たる</strong></td></tr>
</tbody>
</table>
</div>

<p>右端の欄が決定的です。パラメータを増やして合わせても、<em>合わせた量が当たるだけ</em>で、他は何も良くならない。計算を進めると、<strong>同じ理論から出てくる全部の量が同時に良くなる</strong>。</p>

<h2><span class="n">05</span>10 桁が欲しいときの見積もり</h2>

<p>電子の \(g-2\) は 10 桁（約 44 ビット）合っています。それを買うのに要る計算量は、さっきの直線から逆算できます。</p>

<div class="calc">
<span class="tag">計算（kensho/calc01.py ③）</span>
<p>\((44.0 - 10.24) / 2.03 = \mathbf{16.7}\) ビットの計算コスト<br>
\(= 2^{16.7} \simeq\) <strong>10 万枚</strong>の図に相当</p>
<p>フィットで買うなら 5.37 ビット（<em>安い</em>）。ただし<strong>予言はゼロ</strong>。</p>
</div>

<p>フィットの方が圧倒的に安いのです。それでも計算する理由は、④の右端の欄しかありません ── <em>計算だけが、払った以上のものを返す</em>。</p>

<div class="keybox">
<span class="lbl">この回の要点</span>
<p><strong>「わけのわからない計算」は、パラメータを増やさずに精度を買う唯一の方法です。</strong><br>計算を簡単にすると、その分は<em>必ずパラメータで払う</em>ことになります。</p>
</div>

<h2><span class="n">06</span>実際に、そうやって払っている</h2>

<p>この交換は、比喩ではありません。強い力の計算では、はっきりそうなっています。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>方法</th><th class="mid">追加パラメータ</th><th class="mid">計算量</th><th class="mid">精度</th></tr></thead>
<tbody>
<tr><th>格子 QCD</th><td class="mid"><strong>0 個</strong></td><td class="mid">\(10^{19}\) flops</td><td class="mid">1 %</td></tr>
<tr><th>カイラル摂動論 NLO</th><td class="mid">10 個</td><td class="mid">手計算</td><td class="mid">数 %</td></tr>
<tr><th>クォーク模型</th><td class="mid">4 個</td><td class="mid">暗算</td><td class="mid">10 %</td></tr>
<tr><th>次元解析</th><td class="mid">1 個</td><td class="mid">暗算</td><td class="mid">桁が合う</td></tr>
</tbody>
</table>
</div>

<p>上から下へ行くほど計算は楽になり、<strong>そのぶんパラメータが増えていきます</strong>。カイラル摂動論の 10 個（\(10\times5.37 = 54\) ビット）を払って、格子の \(10^{19}\) flops を回避している ── これが交換の実体です。</p>

<div class="caveat">
<span class="tag">正直な線</span>
<p>02〜03節の回帰は<strong>5 点</strong>で、しかも量子電磁力学という<em>いちばん行儀のいい例</em>です。QCD の摂動級数は係数の増え方が速く、同じレートは出ません。また「図の数 ＝ 計算量」は乱暴で、実際は 1 枚あたりの積分が次数とともに重くなるので、<strong>2.03 は上限寄りの見積もり</strong>です。</p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>計算量は、<strong>記法を変えるだけで劇的に下がることがあります</strong>。グルーオン 10 本の散乱は、ファインマン図で <em>1052 万枚</em>。それが <strong>1 項</strong>になります。しかもやったことは変数の取り替えだけで、物理は一つも変わっていません。</p>
</div>'''

build(out='../butsuri-kantan-02-cheapest-currency.html', acc='#1c3f63', ops='#a85a12',
      title='第2回：計算は、いちばん安い通貨 ── 物理を簡単にする',
      ep='第 2 回 ／ 第 I 部「簡単」を測る',
      eyebrow='電子の g−2 で、精度と計算量の為替レートを測る',
      h1='計算は、<br>いちばん安い通貨',
      sub='計算コスト 1 ビットにつき、精度が 2.03 ビット買える。<br><em>パラメータは 5.37 ビット払って、1 個しか買えない。</em>',
      byline_l='必要な予備知識：\\(\\log_2\\) が「桁」の数え方であること',
      byline_r='検証：kensho/calc01.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第2回です。ファインマン図の枚数（1, 7, 72, 891, 12672）と \\(a_e\\) の摂動係数は公表値、<strong>回帰と為替レート 2.03 は本シリーズの計算</strong>です（kensho/calc01.py）。<strong>「計算量 ＝ 図の数」は粗い代用</strong>で、実際の計算コストはこれより急に増えます。パラメータ 1 個 \\(=5.37\\) ビットは \\(N=1701\\) を仮定した BIC の値で、データ数の取り方に依存します。<em>「計算は儲かる」という結論は量子電磁力学という最良の例での話</em>で、強結合領域では成り立ちません（第4回で測ります）。</p>')
