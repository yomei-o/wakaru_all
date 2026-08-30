# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">前回は「計算を増やせば精度が買える」でした。この回はその逆 ── <em>計算を減らす</em>方です。しかも新しい物理は一つも使いません。<strong>変数の取り替えだけで、1052 万枚のファインマン図が 1 項になります。</strong> そして同じことが、紙と鉛筆でスパコンに並ぶ例でも起きています。</p>

<h2><span class="n">01</span>グルーオンの散乱は、図が爆発する</h2>

<p>グルーオンが \(n\) 本、互いに散乱する。いちばん単純な（ツリーレベルの）計算をするのに、ファインマン図を何枚描くか ── その数は次のように増えます。</p>

<div class="calc">
<span class="tag">計算（kensho/calc01.py ⑤）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(n\)</th><th class="mid">図の数</th><th class="mid">\(\log_2\)</th><th class="mid">Parke–Taylor 公式では</th></tr></thead>
<tbody>
<tr><td class="mid">4</td><td class="mid">4</td><td class="mid">2.0</td><td class="mid"><strong>1 項</strong></td></tr>
<tr><td class="mid">5</td><td class="mid">25</td><td class="mid">4.6</td><td class="mid"><strong>1 項</strong></td></tr>
<tr><td class="mid">6</td><td class="mid">220</td><td class="mid">7.8</td><td class="mid"><strong>1 項</strong></td></tr>
<tr><td class="mid">7</td><td class="mid">2 485</td><td class="mid">11.3</td><td class="mid"><strong>1 項</strong></td></tr>
<tr><td class="mid">8</td><td class="mid">34 300</td><td class="mid">15.1</td><td class="mid"><strong>1 項</strong></td></tr>
<tr><td class="mid">9</td><td class="mid">559 405</td><td class="mid">19.1</td><td class="mid"><strong>1 項</strong></td></tr>
<tr class="hi"><td class="mid"><strong>10</strong></td><td class="mid"><strong>10 525 900</strong></td><td class="mid"><strong>23.3</strong></td><td class="mid"><strong>1 項</strong></td></tr>
</tbody>
</table>
</div>

<p>階乗より速く増えています。10 本で <em>1052 万枚</em>。一枚 1 秒で書き写しても 4 か月かかる量です。</p>

<h2><span class="n">02</span>ところが、答えは一行だった</h2>

<p>1986 年、パークとテイラーが、この和の答えを書きました。</p>

<div class="keybox">
<span class="lbl">Parke–Taylor 公式</span>
<p>\[A_n = \frac{\langle ij\rangle^4}{\langle 12\rangle\langle 23\rangle\cdots\langle n1\rangle}\]</p>
<p><strong>これで全部です。</strong> \(n\) が何本でも、項は一つ。</p>
</div>

<p>圧縮率は \(1.1\times10^{7}\) 倍、ビットで言えば <strong>23.3 ビット</strong>。前回のレート（計算 1 ビットで精度 2 ビット）で言えば、<em>46 ビット分の精度をタダで手に入れた</em>のと同じ効果です。</p>

<h2><span class="n">03</span>何をしたのか ── 変数を取り替えただけ</h2>

<p>ここが大事なところです。<strong>パークとテイラーは、新しい物理を一つも使っていません。</strong></p>

<p>やったのは、運動量ベクトル \(p^\mu\)（4 成分の実数）を、スピノルの組 \(\lambda_a, \tilde\lambda_{\dot a}\) に書き換えたことだけです。質量ゼロの粒子なら \(p^\mu\) は \(p^2=0\) という条件を持つので、実質 3 自由度。スピノルで書けばその条件が<em>自動的に満たされる</em>。だから条件を持ち回らなくて済む。</p>

<p>この取り替えを「スピノル・ヘリシティ形式」と言います。<strong>記法の変更です。</strong> ラグランジアンは同じ、粒子も同じ、予言も同じ。<em>変わったのは、書き方だけ。</em></p>

<div class="aside">
<span class="tag">なぜ効くのか</span>
<p>ファインマン図の一枚一枚は<strong>ゲージ不変ではありません</strong>。合計してはじめて意味のある量になる。つまり 1052 万枚のうち大半は、互いに打ち消し合うために書かれています。スピノル・ヘリシティは、<em>打ち消し合う項を最初から書かない</em>書き方です。</p>
</div>

<h2><span class="n">04</span>同じことが、質量の計算でも起きている</h2>

<p>もう一つ、もっと古くて、もっと極端な例があります。1961 年のゲルマン–大久保の質量公式です。</p>

<div class="keybox">
<span class="lbl">Gell-Mann–Okubo の質量公式</span>
<p>\[\frac{m_N + m_\Xi}{2} = \frac{3m_\Lambda + m_\Sigma}{4}\]</p>
</div>

<div class="calc">
<span class="tag">計算（kensho/calc01.py ⑥）</span>
<p>左辺 \(=(938.92+1318.3)/2 = \mathbf{1128.61}\) MeV<br>
右辺 \(=(3\times1115.68+1193.15)/4 = \mathbf{1135.05}\) MeV<br>
相対差 <strong>0.567 %</strong>　→　<strong>7.5 ビット</strong></p>
</div>

<p><strong>紙と鉛筆で 0.6 %。</strong> 格子 QCD がスパコンで 1 % を出すのに、こちらは筆算です。</p>

<p>そして使ったのは <em>SU(3) の表現論だけ</em> ── <strong>ダイナミクスを一切計算していません</strong>。「バリオンが 8 個で一組になる」という並べ方の性質だけから、質量の間の関係が出ています。</p>

<div class="keybox">
<span class="lbl">この回の要点</span>
<p><strong>対称性は、計算せずに答えの一部を先取りする装置です。</strong><br>Parke–Taylor も Gell-Mann–Okubo も、第1回の分類でいえば <em>記法の側</em>。物理を変えずに、計算だけを減らしています。</p>
</div>

<h2><span class="n">05</span>この二つは、同じ型の発見</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th>Parke–Taylor</th><th>Gell-Mann–Okubo</th></tr></thead>
<tbody>
<tr><th>使ったもの</th><td>スピノル・ヘリシティ</td><td>SU(3) の表現論</td></tr>
<tr><th>やったこと</th><td>変数の取り替え</td><td>並べ方の性質を読む</td></tr>
<tr><th>新しい物理</th><td class="mid"><strong>なし</strong></td><td class="mid"><strong>なし</strong></td></tr>
<tr><th>新しいパラメータ</th><td class="mid"><strong>ゼロ</strong></td><td class="mid"><strong>ゼロ</strong></td></tr>
<tr class="hi"><th><strong>減ったもの</strong></th><td class="mid"><strong>計算量 \(10^{7}\) 倍</strong></td><td class="mid"><strong>計算量（暗算になった）</strong></td></tr>
</tbody>
</table>
</div>

<p>どちらも<em>タダ</em>です。前回の帳簿でいうと、払いがゼロで買いだけがある。これが「記法で下げる」の実体で、<strong>第1回で「実績あり」と書いた欄の中身</strong>です。</p>

<div class="caveat">
<span class="tag">正直な線</span>
<p>Parke–Taylor 公式が使えるのは <strong>MHV（最大ヘリシティ違反）と呼ばれる特別なヘリシティ配位</strong>で、一般の配位には BCFW 漸化式などの追加の道具が要ります。「1 項」は最も鮮やかな場合の話です。<br>Gell-Mann–Okubo の 0.567 % は<em>厳密ではありません</em> ── SU(3) の破れの 1 次までの関係で、なぜ 0.6 % なのかはこの式からは出ません。この違いは第 III 部（第8〜9回）で正面から扱います。</p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>ここまでは「計算は安い」「記法で下がる」と良い話ばかりでした。次回は<strong>高いところ</strong>を測ります。摂動論が 2.03 ビット／ビットで儲かるのに対し、強結合の格子計算は <em>0.2〜0.33</em>。<strong>効率差は約 7 倍</strong>。そして「簡単」の二つの意味が、そこで完全に分離します。</p>
</div>'''

build(out='../butsuri-kantan-03-notation.html', acc='#1c3f63', ops='#a85a12',
      title='第3回：記法だけで、1052 万枚が 1 項になる ── 物理を簡単にする',
      ep='第 3 回 ／ 第 I 部「簡単」を測る',
      eyebrow='Parke–Taylor と Gell-Mann–Okubo ── どちらも払いがゼロ',
      h1='記法だけで、<br>1052 万枚が 1 項になる',
      sub='グルーオン 10 本の散乱、ファインマン図 1052 万枚。<br><em>答えは一行でした。しかも変数を取り替えただけ。</em>',
      byline_l='必要な予備知識：前回の「為替レート」',
      byline_r='検証：kensho/calc01.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第3回です。グルーオン散乱のツリー図の枚数と Parke–Taylor 公式、Gell-Mann–Okubo の質量公式はいずれも<strong>確立した標準的な内容</strong>で、本シリーズの主張ではありません。新しいのは<em>それらを「計算量の圧縮」という一つの物差しで並べたこと</em>だけです。数値は kensho/calc01.py で計算しました。<strong>Parke–Taylor が 1 項になるのは MHV 配位に限られます</strong>。<strong>Gell-Mann–Okubo は厳密な関係ではありません</strong>（SU(3) 破れの 1 次まで）── この区別は第 III 部で扱います。</p>')
