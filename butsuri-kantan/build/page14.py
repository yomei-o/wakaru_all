# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">ここまで方針の話でした。この回は<strong>検定</strong>です ── ハドロンの質量比は、単純な有理数に寄っているのか。ちゃんと対照群を作って調べます。答えは<em>寄っていない</em>。ところが<strong>同じハドロンの中に、完全な整数がちゃんとある場所</strong>がありました。</p>

<h2><span class="n">01</span>検定の設計</h2>

<p>「分母 10 以下の有理数に近いか」を測ります。ただしこの手の検定は、<em>対照群の作り方で結論が変わります</em>。</p>

<div class="aside">
<span class="tag">最初にやった間違い</span>
<p>最初、対照を「同じ範囲の一様乱数」から作りました。<strong>これは駄目です。</strong> ハドロンの比は 1〜2 付近に集中していて、一様乱数は大きい値に偏る。<em>分布が揃っていないものを比べても意味がありません。</em></p>
<p>正しい対照は ── <strong>同じ個数・同じ質量範囲から引いた「偽ハドロン」</strong>で、同じ手順で全ペアの比を作ったもの。</p>
</div>

<div class="keybox">
<span class="lbl">検定の手順</span>
<p>① 13 個のハドロン（\(\pi\) から \(\Omega\) まで）の全ペア 78 通りの比を作る<br>
② それぞれについて、分母 10 以下でいちばん近い有理数までの距離を測る<br>
③ <strong>対照</strong>：同じ質量範囲から対数一様に 13 個引いて、同じ手順を <strong>4000 回</strong><br>
④ 実際のハドロンが、対照の分布のどこにいるかを見る</p>
</div>

<h2><span class="n">02</span>結果</h2>

<div class="calc">
<span class="tag">計算（kensho/calc06.py ⑦）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">平均ずれ</th><th class="mid">0.2 % 以内の数</th></tr></thead>
<tbody>
<tr class="hi"><th><strong>実際のハドロン</strong></th><td class="mid"><strong>0.00713</strong></td><td class="mid"><strong>23 / 78</strong></td></tr>
<tr><th>偽ハドロン（対照 4000 回）</th><td class="mid">0.00601</td><td class="mid">25.8 ± 4.9</td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">判定</span>
<p>ずれの \(z\) 値 \(= \mathbf{+1.23\,\sigma}\)、当たり数の \(z\) 値 \(= \mathbf{-0.57\,\sigma}\)</p>
</div>

<div class="record">
<h2>検定の結論</h2>
<p><strong>偽ハドロンと区別がつきません（2 \(\sigma\) 以内）。</strong></p>
<p>ハドロンの質量比に、単純な整数比に寄っている証拠はありません。</p>
</div>

<p>「分母 10 以下ならだいたい当たるじゃないか」と思うかもしれません。実際、78 組のうち 23 組は 0.2 % 以内で有理数に当たっています。<strong>しかしそれは、有理数が稠密だからです</strong> ── 偽ハドロンでも 25.8 組当たる。<em>当たった数ではなく、対照との差を見なければなりません。</em></p>

<h2><span class="n">03</span>ところが、整数がちゃんと出る場所がある</h2>

<p>同じハドロンで、別の量を見ます。<strong>レッジェ軌道</strong> ── スピン \(J\) と質量の 2 乗の関係です。</p>

<div class="calc">
<span class="tag">計算（kensho/calc06.py ⑧）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>粒子</th><th class="mid">\(m^2\) [GeV\(^2\)]</th><th class="mid">\(J\)</th><th class="mid">\(\Delta m^2\)</th></tr></thead>
<tbody>
<tr><th>\(\rho\)</th><td class="mid">0.6011</td><td class="mid"><strong>1</strong></td><td class="mid">─</td></tr>
<tr><th>\(a_2\)</th><td class="mid">1.7377</td><td class="mid"><strong>2</strong></td><td class="mid">1.137</td></tr>
<tr><th>\(\rho_3\)</th><td class="mid">2.8520</td><td class="mid"><strong>3</strong></td><td class="mid">1.114</td></tr>
<tr><th>\(a_4\)</th><td class="mid">3.9840</td><td class="mid"><strong>4</strong></td><td class="mid">1.132</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">同じ粒子の中で、二つに割れる</span>
<p>\(J\) は <strong>1, 2, 3, 4 ── 完全な整数</strong>。誤差ゼロ。<br>（回転が「一周して戻る」ものだから ── 第12回の指針そのままです。）</p>
<p>一方 \(\Delta m^2\) は 1.137, 1.114, 1.132 ── <strong>ばらつき 2 %</strong>。<br><em>傾き（生の実数）は整数比になりません。</em></p>
</div>

<p>これが決定的です。<strong>同じ粒子の同じ表の中で、整数の側と実数の側がきれいに分かれています。</strong> 「ハドロンには整数が無い」のではなく、<em>整数がある場所と無い場所が決まっている</em>。</p>

<h2><span class="n">04</span>02 と 03 を、並べて読む</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">整数か</th><th>何を数えているか</th></tr></thead>
<tbody>
<tr class="hi"><th>\(J\)（スピン）</th><td class="mid"><strong>完全な整数</strong></td><td><strong>一周したときの位相の回転数</strong></td></tr>
<tr><th>\(m^2\) の間隔</th><td class="mid">2 % ばらつく</td><td>数えていない（測っている）</td></tr>
<tr><th>質量比</th><td class="mid"><strong>整数比なし</strong></td><td>数えていない（測っている）</td></tr>
</tbody>
</table>
</div>

<p>第12回の指針が、そのまま働いています ── <strong>閉じた道を数えているところにだけ、整数がある。</strong></p>

<h2><span class="n">05</span>だから、探す場所が決まる</h2>

<div class="keybox">
<span class="lbl">検定から出た指針</span>
<p><strong>「陽子と \(\rho\) の質量比は簡単な分数か」を探すのは、時間の無駄です。</strong></p>
<p>対照群と区別がつかないところに、いくら分母を大きくして探しても、出てくるのは<em>探索空間の値段</em>だけです（第13回）。</p>
<p>探すべきは ── <strong>スピン、電荷、色、世代、巻きつき数</strong>。<em>数えているものの側。</em></p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>02節の検定は「分母 10 以下」という<strong>一つの選び方</strong>です。分母を大きくすれば当然よく当たりますが、それは第13回の \(\log_2 M\) を払うだけで、<em>情報は増えません</em>。<br>13 個・78 組という<strong>標本の小ささ</strong>も留保です。もっと多くのハドロンで、もっと精密にやれば違う結果が出る可能性は残ります。<br>対照を「対数一様」に取ったのも一つの選び方で、別の分布を取れば \(z\) 値は動きます。<em>ただし「2 \(\sigma\) 以内」という結論は、この程度の選択では覆りません。</em></p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>「整数がある場所と無い場所」の境目を、QCD の中で全部並べます。すると <strong>境目は一本しかありませんでした</strong>。そして驚くべきことに ── <em>結合定数の走り方は、単純な整数で決まっています</em>。</p>
</div>'''

build(out='../butsuri-kantan-14-test.html', acc='#7a3a2a', ops='#3a5a7a',
      title='第14回：検定 ── ハドロンの質量比は整数比か ── 物理を簡単にする',
      ep='第 14 回 ／ 第 IV 部 整数比の探し方',
      eyebrow='偽ハドロン 4000 組と比べる ── 差は 1.23 σ',
      h1='検定 ── ハドロンの<br>質量比は整数比か',
      sub='答えは「寄っていない」。<br><em>ところが同じ表の中に、完全な整数がありました。</em>',
      byline_l='必要な予備知識：第12〜13回',
      byline_r='検証：kensho/calc06.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第14回です。ハドロン質量とレッジェ軌道は<strong>実測値</strong>で、02節の検定と対照群のシミュレーションは本シリーズの計算です（kensho/calc06.py）。<strong>対照群を「同じ範囲・同じ個数から対数一様に引いた偽ハドロン」に揃えた</strong>のは、最初に一様乱数で比べて分布が揃わない誤りを出したための修正です ── 01節に経緯を書きました。<strong>標本は 13 個・78 組と小さく</strong>、分母の上限や対照の分布の取り方は一つの選択です。「2 \\(\\sigma\\) 以内」という結論はこの範囲での話です。</p>')
