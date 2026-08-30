# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">「全部を単純な整数の比で書きたい」── この願いには、<strong>物理でいちばん長い実績</strong>があります。200 年、勝ち続けている。そして成功例を並べたら、驚くことに<em>全部が同じ形</em>をしていました ── <strong>閉じた道に、いくつ入るか</strong>。つまり、長さと長さの比です。</p>

<h2><span class="n">01</span>戦績</h2>

<div class="calc">
<span class="tag">計算（kensho/calc06.py ①）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>いつ</th><th>何の比</th><th class="mid">答え</th><th class="mid">ずれ</th></tr></thead>
<tbody>
<tr><th>倍数比例の法則 (1803)</th><td>CO : CO\(_2\) の酸素</td><td class="mid"><strong>1 : 2</strong></td><td class="mid">厳密</td></tr>
<tr class="hi"><th>バルマー (1885)</th><td>H\(\alpha\) / H\(\beta\) の波長比</td><td class="mid"><strong>27/20</strong></td><td class="mid"><strong>\(5\times10^{-6}\)</strong></td></tr>
<tr><th>ブラッグ (1913)</th><td>\(n\lambda = 2d\sin\theta\)</td><td class="mid">\(n\) は整数</td><td class="mid">厳密</td></tr>
<tr><th>ボーア (1913)</th><td>\(2\pi r = n\lambda\)</td><td class="mid">\(n\) は整数</td><td class="mid">厳密</td></tr>
<tr><th>角運動量</th><td>\(\hbar/2\) の整数倍</td><td class="mid">整数</td><td class="mid">厳密</td></tr>
<tr class="hi"><th>電荷</th><td>\(e/3\) の整数倍</td><td class="mid">整数</td><td class="mid"><strong>\(&lt;10^{-21}\)</strong></td></tr>
<tr><th>磁束量子</th><td>\(\Phi = n\,h/2e\)</td><td class="mid">整数</td><td class="mid">\(&lt;10^{-9}\)</td></tr>
<tr class="hi"><th>ジョセフソン効果</th><td>\(V = n\,(h/2e)f\)</td><td class="mid">整数</td><td class="mid"><strong>\(&lt;10^{-19}\)</strong></td></tr>
<tr><th>整数量子ホール効果</th><td>\(\sigma = \nu\,e^2/h\)</td><td class="mid">\(\nu\) は整数</td><td class="mid">\(&lt;10^{-10}\)</td></tr>
<tr><th>分数量子ホール効果</th><td>\(\nu = 1/3, 2/5, \dots\)</td><td class="mid"><strong>単純な有理数</strong></td><td class="mid">厳密</td></tr>
</tbody>
</table>
</div>

<p>バルマーを実際に検算しておきます。水素のスペクトルは \(\lambda \propto 1/(1/4 - 1/n^2)\) なので、\(n=3\) と \(n=4\) の比は純粋な分数になるはずです。</p>

<div class="calc">
<span class="tag">計算（kensho/calc06.py ①）</span>
<p>予言　\(\lambda_\alpha/\lambda_\beta = (36/5)\div(16/3) = 27/20 = \mathbf{1.350000}\)<br>
実測　\(656.279 / 486.135 = \mathbf{1.349993}\)<br>
ずれ　\(\mathbf{5.0\times10^{-6}}\)</p>
</div>

<div class="keybox">
<span class="lbl">この方針の強さ</span>
<p><strong>整数比を探すのは、物理でいちばん実績のある方針です。</strong></p>
<p>しかも第9〜11回で見たとおり、<em>整数の主張は 20 桁で検証できます</em>。0.57 % で止まる関係とは、桁が違う。</p>
</div>

<h2><span class="n">02</span>勝った例に、共通するもの</h2>

<p>10 個並べて眺めると、全部が同じことをしています。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>例</th><th>何を数えているか</th></tr></thead>
<tbody>
<tr><th>倍数比例</th><td><strong>原子の個数</strong></td></tr>
<tr><th>バルマー</th><td><strong>軌道に波が何個入るか</strong></td></tr>
<tr><th>ブラッグ</th><td><strong>面と面の間に波長が何個入るか</strong></td></tr>
<tr><th>ボーア</th><td><strong>円周に波長が何個入るか</strong></td></tr>
<tr><th>角運動量</th><td><strong>一周したときの位相の回転数</strong></td></tr>
<tr><th>量子ホール</th><td><strong>チャーン数 ＝ 位相の巻きつき回数</strong></td></tr>
<tr><th>磁束量子</th><td><strong>輪を通る磁束が波動関数を何回まわすか</strong></td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>この回の中心</h2>
<p><strong>例外なく、「閉じた道に、いくつ入るか」を数えています。</strong></p>
<p>整数はどれも \(n = 2L/\lambda\) の形 ── <em>長さと長さの比</em>です。</p>
</div>

<p>「整数比は距離と関係があるのではないか」という直感は、<strong>成功例については 100 % 当たっています</strong>。整数が出るとき、必ずどこかに<em>一周して戻る道</em>があって、そこに何かが何個入るかを数えている。</p>

<h2><span class="n">03</span>「閉じている」が本質</h2>

<p>なぜ閉じていると整数になるのか。閉じていない場合と並べると、はっきりします。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>何の対称性か</th><th>閉じているか</th><th class="mid">スペクトル</th><th class="mid">整数比</th></tr></thead>
<tbody>
<tr><th>回転 SO(3)</th><td><strong>閉じている</strong>（一周して戻る）</td><td class="mid">離散</td><td class="mid"><strong>\(J = 0, 1/2, 1, \dots\)</strong></td></tr>
<tr><th>U(1) 電荷</th><td><strong>閉じている</strong></td><td class="mid">離散</td><td class="mid"><strong>\(e/3\) の整数倍</strong></td></tr>
<tr><th>箱の中の並進</th><td><strong>閉じている</strong>（周期境界）</td><td class="mid">離散</td><td class="mid"><strong>\(n = 2L/\lambda\)</strong></td></tr>
<tr><th>巻きつき数</th><td><strong>閉じている</strong>（円周）</td><td class="mid">整数</td><td class="mid"><strong>トポロジカル電荷</strong></td></tr>
<tr class="hi"><th>自由空間の並進</th><td><strong>閉じていない</strong></td><td class="mid">連続</td><td class="mid"><strong>整数なし</strong></td></tr>
<tr class="hi"><th>エネルギーの値そのもの</th><td><strong>閉じていない</strong></td><td class="mid">連続</td><td class="mid"><strong>整数なし</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">探すときの指針</span>
<p><strong>整数が出るのは、閉じたものを数えているときだけです。</strong></p>
<p>時計（一周して戻る）は数えられる。ロープ（どこまでも伸びる）は数えられない。</p>
<p>→ <em>閉じた道を見つけたら、そこに整数があります。</em></p>
</div>

<h2><span class="n">04</span>言い換えると、こうなる</h2>

<p>「一周して戻る」という言い方を、もう少し使いやすくしておきます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>問いの形</th><th class="mid">整数が出るか</th><th>例</th></tr></thead>
<tbody>
<tr class="hi"><th>「一周したら、何回まわったか」</th><td class="mid"><strong>出る</strong></td><td>角運動量、量子ホール、巻きつき数</td></tr>
<tr class="hi"><th>「この長さに、何個入るか」</th><td class="mid"><strong>出る</strong></td><td>バルマー、ブラッグ、ボーア</td></tr>
<tr class="hi"><th>「全部で何個あるか」</th><td class="mid"><strong>出る</strong></td><td>色の数、世代の数、倍数比例</td></tr>
<tr><th>「この量はいくつか」</th><td class="mid"><strong>出ない</strong></td><td>陽子質量、臨界指数、結合定数</td></tr>
</tbody>
</table>
</div>

<p>上の三つは<em>数え上げ</em>、いちばん下は<em>測定</em>です。<strong>数え上げには整数が返り、測定には実数が返ります。</strong></p>

<div class="aside">
<span class="tag">第 III 部とつながる</span>
<p>第9回のフィルタ（「答えが整数かゼロか」）と、この回の指針（「閉じた道があるか」）は、<strong>同じことを別の側から言っています</strong>。<br>閉じているから離散になり、離散だから整数で数えられ、整数だから厳密になる。<em>三つが一続きです。</em></p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>03節の「閉じている → 整数」は、<strong>離散スペクトルの十分条件であって必要条件ではありません</strong>。閉じていなくても束縛状態は離散になります（水素原子がそうです）。<br>ただし <em>その離散値が整数比になる</em> のは、可解なときだけです ── 水素が \(1/n^2\) というきれいな形になるのは、水素が厳密に解けるから。ヘリウムの基底状態エネルギーは、水素との比が生の実数になります。</p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>負けた歴史も見ます ── ケプラーの正多面体、ボーデの法則、エディントンの 137。そして<strong>いちばん使える発想</strong>が、負けた例の中から出てきます。プルーの仮説は 1815 年に破れて、<em>1913 年に復活しました</em>。</p>
</div>'''

build(out='../butsuri-kantan-12-integer-ratios.html', acc='#7a3a2a', ops='#3a5a7a',
      title='第12回：整数比の戦績 ── 全部「距離の比」だった ── 物理を簡単にする',
      ep='第 12 回 ／ 第 IV 部 整数比の探し方',
      eyebrow='勝った 10 例は、例外なく「閉じた道に何個入るか」',
      h1='整数比の戦績<br>── 全部「距離の比」だった',
      sub='整数が出るのは、閉じたものを数えているときだけ。<br><em>時計は数えられる。ロープは数えられない。</em>',
      byline_l='必要な予備知識：第9回（厳密値のフィルタ）',
      byline_r='検証：kensho/calc06.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第12回です。倍数比例の法則、バルマー系列、ブラッグ条件、角運動量・電荷の量子化、磁束量子、ジョセフソン効果、量子ホール効果はいずれも<strong>確立した標準的な内容</strong>です。<em>「勝った例は全部『閉じた道に何個入るか』である」という並べ方と、そこから作った指針は本シリーズの整理</em>で、教科書の主張ではありません（kensho/calc06.py）。<strong>「閉じている → 整数」は十分条件であって必要条件ではありません</strong>（水素原子は反例）── 04節の留保と合わせて読んでください。</p>')
