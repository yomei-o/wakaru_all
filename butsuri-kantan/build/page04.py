# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">「もっと簡単に計算できないのか」── その答えは、<em>できる所ではもうやっている</em>でした。残っているのは一箇所だけで、そこだけが桁違いに高い。この回でその場所を特定し、ついでに<strong>「簡単」の二つの意味が完全に分離する例</strong>を見ます。そして第 I 部の結論 ── <em>三つの通貨</em> ── にたどり着きます。</p>

<h2><span class="n">01</span>領域ごとに、為替レートが違う</h2>

<p>第2回で測った「精度ビット ÷ 計算コストビット」を、領域ごとに出します。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>領域</th><th class="mid">精度／コスト</th><th class="mid">収支</th><th>例</th></tr></thead>
<tbody>
<tr><th>摂動論が効く（\(\alpha\) 小）</th><td class="mid"><strong>2.03</strong></td><td class="mid"><strong>儲かる</strong></td><td>量子電磁力学、電弱、高エネルギー QCD</td></tr>
<tr><th>対称性で決まる</th><td class="mid">\(\infty\)</td><td class="mid"><strong>タダ</strong></td><td>Gell-Mann–Okubo、アノマリー、指数定理</td></tr>
<tr class="hi"><th><strong>強結合（\(\alpha \sim 1\)）</strong></th><td class="mid"><strong>0.2〜0.33</strong></td><td class="mid"><strong>大損</strong></td><td><strong>陽子質量、ハドロン、閉じ込め</strong></td></tr>
</tbody>
</table>
</div>

<p>いちばん下の行が、この分野で「わけのわからない計算」と呼ばれているものの正体です。</p>

<h2><span class="n">02</span>格子計算の値段を、実際に見積もる</h2>

<p>格子 QCD は、時空を格子に切って数値的に解きます。格子の間隔を \(a\) とすると：</p>

<div class="calc">
<span class="tag">計算（kensho/calc01.py ⑦）</span>
<p>離散化の誤差 \(\sim a^2\)、計算コスト \(\sim a^{-6}\)</p>
<p>→ 誤差を半分にする（精度 \(+1\) ビット）のにコストは \(2^3 = 8\) 倍 ＝ <strong>3 ビット</strong><br>
→ 統計誤差ぶん（誤差 \(\sim N^{-1/2}\)、コスト \(\sim N\) ＝ <strong>2 ビット</strong>）も乗る<br>
→ 実効レート <strong>精度 1 ビットあたりコスト 3〜5 ビット</strong></p>
</div>

<div class="keybox">
<span class="lbl">効率の差</span>
<p>摂動論　<strong>2.03</strong> ビット／ビット　（1 払って 2 返る）<br>
格子　　<strong>0.2〜0.33</strong> ビット／ビット　（3〜5 払って 1 返る）</p>
<p><strong>効率差は約 7 倍。</strong></p>
</div>

<p>だから、摂動論が使えるところでは誰も格子を使いません。<em>使えないところだけが残っている</em>。</p>

<h2><span class="n">03</span>だから、答えはこうなる</h2>

<div class="keybox">
<span class="lbl">「もっと簡単に計算できないのか」への答え</span>
<p><strong>できる所では、もうやっています。</strong><br>残っているのは \(\alpha_s \sim 1\) の領域だけで、そこだけが桁違いに高い。</p>
</div>

<p>これは怠慢の話ではありません。摂動論が使える場所では、人類はすでに 12,672 枚の図を描いています（第2回）。記法で圧縮できる場所では、1052 万枚を 1 項にしています（第3回）。<em>残ったのは、そのどちらも効かない場所です。</em></p>

<h2><span class="n">04</span>高いところを安くする道が、三つある</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>道</th><th>何を使うか</th><th>何を犠牲にするか</th><th class="mid">実績</th></tr></thead>
<tbody>
<tr><th>ブートストラップ</th><td>整合性（交叉対称性＋ユニタリ性）だけ</td><td>ラグランジアンも図も使わない</td><td class="mid">\(\nu\) を 7 桁</td></tr>
<tr><th>有効理論の階層</th><td>測った定数でループを置き換える</td><td><strong>パラメータで払う</strong></td><td class="mid">数 %</td></tr>
<tr><th>大 \(N\) 展開</th><td>\(1/N_c = 1/3\) を小さいと見なす</td><td><strong>強結合を弱結合に化かす</strong></td><td class="mid">30 %</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">05</span>そして、ここで「簡単」が二つに割れる</h2>

<p>一番上のブートストラップが、この回でいちばん面白いところです。</p>

<div class="keybox">
<span class="lbl">ブートストラップの奇妙さ</span>
<p><strong>記述長は極端に短いのに、計算量は重い。</strong></p>
<p>使う仮定は「クロッシング対称性とユニタリ性」の<em>2 語</em>。ラグランジアンも、粒子の一覧も、結合定数も要らない。</p>
<p>ところが実際に解くのは、<strong>数万本の制約を持つ半正定値計画</strong>です。</p>
</div>

<p>第1回で「三つの軸は独立」と言いました。<strong>ここでそれが完全に分離します。</strong> 短く言えることと、速く解けることは、別の資源です。ブートストラップは片方が極小で、もう片方が極大。</p>

<div class="aside">
<span class="tag">第 III 部への伏線</span>
<p>ブートストラップが特別なのは、値段の話だけではありません。<em>これは「近似」ではない</em> ── 出てくる誤差は、近似の誤差ではなく<strong>厳密な不等式の幅</strong>です。この違いが何を意味するかは、第 III 部（第8〜11回）で正面から扱います。</p>
</div>

<h2><span class="n">06</span>第 I 部のまとめ ── 通貨は三つあった</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>通貨</th><th class="mid">レート</th><th>性質</th></tr></thead>
<tbody>
<tr><th>パラメータ</th><td class="mid">5.37 ビット／個</td><td>増やせば予言が減る</td></tr>
<tr class="hi"><th><strong>計算量</strong></th><td class="mid"><strong>2.03 ビット／ビット</strong></td><td><strong>増やしても予言は減らない</strong></td></tr>
<tr><th>対称性</th><td class="mid">タダ</td><td>使える所が限られる</td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>第 I 部の結論</h2>
<p><strong>第5回の天秤（記述長＋ずれ）には、通貨が一つ足りませんでした。</strong>「パラメータいくつ」しか数えていなくて、「計算いくら」を数えていない。</p>
<p>同じ精度を出す二つの理論でも、<em>片方が \(10^{19}\) flops 要るなら同じではありません</em>。</p>
<p>そして ── <strong>計算が「わけのわからない」ものになるのは、それがいちばん安い通貨だからです。</strong> 簡単にした分は、必ずパラメータか精度で払うことになります。</p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>格子のスケーリング指数（\(a^{-6}\)）は作用とアルゴリズムに依り、\(a^{-5}\)〜\(a^{-7}\) の幅があります。また過去 30 年でアルゴリズムの改良が \(10^{6}\) 倍あった事実は、この見積もりに入っていません ── <strong>「壁」は動きうる</strong>ということです。<br>そして最大の留保：<em>計算量まで込みの記述長理論を、本シリーズは作れていません</em>。コルモゴロフ複雑さと計算量の関係は、それ自体が未解決の分野です。</p>
</div>

<div class="next">
<span class="lbl">次回から第 II 部</span>
<p>物差しができたので、実際の物理に当てます。<strong>強い力</strong>を四つの層に切ってみると ── <em>数 % までは全部が単純な計算で届き、格子 QCD が要るのは最後の数 % だけ</em>でした。</p>
</div>'''

build(out='../butsuri-kantan-04-where-expensive.html', acc='#1c3f63', ops='#a85a12',
      title='第4回：高いのはどこか ── 物理を簡単にする',
      ep='第 4 回 ／ 第 I 部「簡単」を測る（部の終わり）',
      eyebrow='摂動は儲かり、強結合は大損する ── 効率差は 7 倍',
      h1='高いのは、<br>どこか',
      sub='「もっと簡単にできないのか」の答えは、<em>できる所ではもうやっている</em>。<br>残っているのは \\(\\alpha_s \\sim 1\\) の一箇所だけでした。',
      byline_l='必要な予備知識：第2回の為替レート、第3回の記法圧縮',
      byline_r='検証：kensho/calc01.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第4回（第 I 部の終わり）です。格子 QCD のコストスケーリング（\\(a^{-6}\\)）と摂動論の収束は<strong>標準的な内容</strong>ですが、<em>それらを同じ「ビット／ビット」という単位で比べたのは本シリーズの整理</em>で、教科書の主張ではありません。数値は kensho/calc01.py で計算しました。<strong>「三つの通貨」という言い方も本シリーズの独自の枠組み</strong>です。計算量を含む形式的な記述長理論は本シリーズでは作れていません。</p>')
