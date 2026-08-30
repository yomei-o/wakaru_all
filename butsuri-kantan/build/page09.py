# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">前回、「そもそも厳密になりうる問いを先に見分けたい」と書きました。見分けるには、<em>実例を全部集めるのが早い</em>。物理で厳密に成り立っているものを並べてみたら ── <strong>例外なく、整数・小さい有理数・\(\pi\) の有理数倍でした。生の実数の厳密値は、一件もありません。</strong></p>

<h2><span class="n">01</span>強い力で、厳密に成り立つもの</h2>

<div class="calc">
<span class="tag">計算（kensho/calc04.py ②）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>結果</th><th>値</th><th>起源</th><th class="mid">値の型</th></tr></thead>
<tbody>
<tr class="hi"><th>アノマリー相殺</th><td>\(N_c/3 - 1 = \mathbf{0}\)</td><td>無矛盾性</td><td class="mid"><strong>整数</strong></td></tr>
<tr class="hi"><th>色の数</th><td>\(N_c = \mathbf{3}\)</td><td>同上</td><td class="mid"><strong>整数</strong></td></tr>
<tr><th>電荷の量子化</th><td>すべて \(e/3\) の<strong>整数倍</strong></td><td>同上</td><td class="mid">整数</td></tr>
<tr><th>指数定理</th><td>\(n_+ - n_- = \) 位相電荷 \(Q\)</td><td>位相幾何</td><td class="mid">整数</td></tr>
<tr><th>バリオン数の保存</th><td>整数</td><td>位相</td><td class="mid">整数</td></tr>
<tr><th>アドラー和則</th><td>\(\int(F_2^{\nu n}-F_2^{\nu p})\,dx/x = \mathbf{2}\)</td><td>カレント代数</td><td class="mid">整数</td></tr>
<tr><th>ゴールドストンの定理</th><td>\(m_q=0\) なら \(m_\pi = \mathbf{0}\)</td><td>対称性</td><td class="mid"><strong>ゼロ</strong></td></tr>
<tr><th>Adler–Bardeen 定理</th><td>アノマリーは 1 ループで完全</td><td>位相</td><td class="mid">有理数</td></tr>
</tbody>
</table>
</div>

<p><strong>全部、値が整数かゼロです。</strong> 一つも「生の実数」がありません。</p>

<h2><span class="n">02</span>物理全体でも、同じか</h2>

<p>強い力に限らず、思いつく限りの厳密値を集めました。</p>

<div class="calc">
<span class="tag">計算（kensho/calc04.py ③）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th>式</th><th class="mid">厳密値</th><th>起源</th></tr></thead>
<tbody>
<tr><th>電子 \(g-2\) の 1 ループ</th><td>\(\alpha/2\pi\)</td><td class="mid">係数 \(\mathbf{1/2}\)</td><td>自由場＋1 ループ</td></tr>
<tr><th>ベッケンシュタイン–ホーキング</th><td>\(S = A/4\)</td><td class="mid">\(\mathbf{1/4}\)</td><td>自由場</td></tr>
<tr><th>ホーキング温度</th><td>\(T = 1/(8\pi M)\)</td><td class="mid">\(\mathbf{1/8\pi}\)</td><td>自由場</td></tr>
<tr><th>ウンルー温度</th><td>\(T = a/2\pi\)</td><td class="mid">\(\mathbf{1/2\pi}\)</td><td>自由場</td></tr>
<tr><th>カシミール（1 次元）</th><td>\(E = -\pi/24L\)</td><td class="mid">\(\mathbf{-\pi/24}\)</td><td>自由場の零点</td></tr>
<tr class="hi"><th>リュッシャー項</th><td>\(V \supset -\pi/12r\)</td><td class="mid">\(\mathbf{-\pi/12}\)</td><td>弦の零点振動</td></tr>
<tr><th>シュテファン–ボルツマン</th><td>\(\propto \pi^2/60\)</td><td class="mid">\(\mathbf{\pi^2/60}\)</td><td>自由場の積分</td></tr>
<tr><th>2 次元イジング \(\nu\)</th><td></td><td class="mid">\(\mathbf{1}\)</td><td>可解模型</td></tr>
<tr><th>2 次元イジング \(\beta\)</th><td></td><td class="mid">\(\mathbf{1/8}\)</td><td>可解模型</td></tr>
<tr><th>2 次元イジング \(\eta\)</th><td></td><td class="mid">\(\mathbf{1/4}\)</td><td>可解模型</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">集めた結果</span>
<p><strong>例外なく、整数・小さい有理数・\(\pi\) の有理数倍。</strong></p>
<p><em>「生の実数」の厳密値は、一件もありませんでした。</em></p>
</div>

<div class="caveat">
<span class="tag">番外編で訂正しました</span>
<p>この言い方には<strong>反例がありました</strong> ―― 黒体輻射の光子数密度には \(\zeta(3)\)、2 次元イジングの臨界自由エネルギーには<strong>カタラン定数</strong>が出ます。どちらも厳密値で、しかも \(\pi\) の有理数倍ではありません。正しい言い方は <strong>「厳密値は必ず閉じた形を持つ」</strong> でした ―― <strong><a href="butsuri-kantan-b2-zeta.html">番外編②：厳密値に、\(\pi\) 以外の定数が出る</a></strong>。<em>ただし境目（相互作用を実際に解いたかどうか）は動いていません。</em></p>
</div>

<h2><span class="n">03</span>逆側 ── 閉じた形が無いことが分かっている量</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">値</th><th>閉じた形</th><th>なぜ</th></tr></thead>
<tbody>
<tr><th>3 次元イジング \(\nu\)</th><td class="mid">0.6299709</td><td>知られていない</td><td>相互作用する 3 次元</td></tr>
<tr><th>3 次元イジング \(\eta\)</th><td class="mid">0.0362978</td><td>同上</td><td>同上</td></tr>
<tr class="hi"><th>\(m_p/\sqrt{\sigma}\)</th><td class="mid"><strong>2.13…</strong></td><td>同上</td><td><strong>相互作用する 4 次元</strong></td></tr>
<tr><th>グルーボール \(0^{++}/\sqrt{\sigma}\)</th><td class="mid">3.405…</td><td>同上</td><td>同上</td></tr>
<tr><th>\(m_p/m_\rho\)</th><td class="mid">1.211…</td><td>同上</td><td>同上</td></tr>
</tbody>
</table>
</div>

<p>境目がはっきりしています。<strong>相互作用する 3 次元以上の理論を実際に解いた答えは、一つも閉じた形を持っていません。</strong>（この「一つも」には例外があります ── 次回で扱います。）</p>

<h2><span class="n">04</span>フィルタが作れる</h2>

<p>①〜③を並べると、<em>計算を始める前にかけられるふるい</em>ができます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>問いの型</th><th>理由</th><th class="mid">見込み</th><th>例</th></tr></thead>
<tbody>
<tr class="hi"><th>答えが<strong>整数</strong>か</th><td>数え上げ／位相</td><td class="mid"><strong>厳密が取れる</strong></td><td>\(N_c=3\)、指数定理、和則</td></tr>
<tr class="hi"><th>答えが<strong>ゼロ</strong>か</th><td>対称性が禁じている</td><td class="mid"><strong>厳密が取れる</strong></td><td>アノマリー相殺、\(m_\pi\)</td></tr>
<tr><th><strong>自由場の積分</strong>か</th><td>ガウス積分は解ける</td><td class="mid"><strong>厳密が取れる</strong></td><td>\(\pi/12\)、\(A/4\)、\(\pi^2/60\)</td></tr>
<tr><th><strong>2 次元</strong>か</th><td>可解模型がある</td><td class="mid"><strong>厳密が取れる</strong></td><td>イジング \(\nu=1\)</td></tr>
<tr><th>上のどれでもない</th><td>相互作用を実際に解く</td><td class="mid"><strong>前例ゼロ</strong></td><td>\(m_p/\sqrt{\sigma}\)、3D \(\nu\)</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">05</span>そのフィルタを、第6回の 5 本にかける</h2>

<p>第6回で「パラメータ不要の関係が 5 本」と喜びました。厳密でしょうか。</p>

<div class="calc">
<span class="tag">計算（kensho/calc04.py ⑧）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>関係</th><th class="mid">ずれ</th><th>なぜ厳密でないか</th></tr></thead>
<tbody>
<tr><th>Gell-Mann–Okubo</th><td class="mid">0.57 %</td><td>SU(3) 破れの<strong>1 次まで</strong></td></tr>
<tr><th>Coleman–Glashow</th><td class="mid">0.78 %</td><td>電磁破れの<strong>1 次まで</strong></td></tr>
<tr><th>\(\mu_n/\mu_p = -2/3\)</th><td class="mid">2.75 %</td><td>SU(6)、破れが大きい</td></tr>
<tr><th>\((\Sigma^*-\Sigma)/(\Delta-N)\)</th><td class="mid">3.56 %</td><td>模型の中の関係</td></tr>
<tr><th>十重項の等間隔</th><td class="mid">9.19 %</td><td><strong>1 次まで</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">判定</span>
<p><strong>5 本とも、厳密ではありませんでした。</strong> どれも「対称性の破れの 1 次」で止まっています。</p>
<p>一方、同じ話の中で<em>厳密だったもの</em> ── \(N_c=3\)、アノマリー相殺、電荷の量子化、指数定理、アドラー和則。</p>
<p><strong>違いは一つ。厳密な方は、答えが整数かゼロです。</strong></p>
</div>

<p>0.57 % ずれる関係は、<em>もともと厳密になりようがなかった</em>。\(1128.61\) と \(1135.05\) という二つの生の実数を比べているのだから、ぴたりと合う理由が最初から無い。</p>

<h2><span class="n">06</span>だから、目標はこう書き換わる</h2>

<div class="keybox">
<span class="lbl">書き換え</span>
<p>× 「物理を厳密に一致する単純な法則にする」</p>
<p>○ <strong>「答えが整数かゼロになる形に、問いを書き換える」</strong></p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>問い</th><th>答え</th><th class="mid">厳密性</th></tr></thead>
<tbody>
<tr><th>「陽子の質量は？」</th><td>生の実数。閉じた形なし</td><td class="mid">厳密は無理</td></tr>
<tr class="hi"><th><strong>「色は何色か？」</strong></th><td><strong>3</strong></td><td class="mid"><strong>厳密</strong></td></tr>
<tr><th>「\(\Lambda\) の値は？」</th><td>次元を持つ ＝ 単位</td><td class="mid">問いが無意味</td></tr>
<tr class="hi"><th><strong>「1 世代の電荷の和は？」</strong></th><td><strong>0</strong></td><td class="mid"><strong>厳密</strong></td></tr>
<tr><th>「\(\nu\) は？」</th><td>0.6299709…</td><td class="mid">厳密は無理</td></tr>
<tr class="hi"><th><strong>「2 次元の \(\nu\) は？」</strong></th><td><strong>1</strong></td><td class="mid"><strong>厳密</strong></td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>この回の結論</h2>
<p><strong>同じ物理でも、問いの立て方で厳密性が変わります。</strong></p>
<p>「量はいくつか」は近似にしかなりません。<br><em>「いくつあるか」「ゼロか」「何倍か」は、厳密になりうる。</em></p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>02〜03節の分類は<strong>現時点で知られている限り</strong>の話です。3 次元イジングの \(\nu\) に閉じた形が無いことは<em>証明されていません</em> ── ブートストラップが将来、閉じた形を出す可能性は残っています。<br>04節のフィルタは経験則であって定理ではありません。<strong>そして次回、このフィルタには反例があることを示します。</strong><br>05節で「厳密でない」と判定した 5 本は、<em>役に立たないという意味ではありません</em>。0.57 % で合うことは、それ自体が測定であり、検定に使えます。</p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>04節のフィルタには、実は<strong>反例</strong>があります ── 4 次元の相互作用する理論で、厳密に解けたものが六つ。ところがそれを並べると、全部が<em>一つの定理の裏返し</em>でした。そして <strong>QCD が厳密に解けないのは、能力不足ではなく定理の帰結</strong>だと分かります。</p>
</div>'''

build(out='../butsuri-kantan-09-exact-values.html', acc='#4a2f52', ops='#8a5a1a',
      title='第9回：厳密値を全部集めたら、整数と π しかなかった ── 物理を簡単にする',
      ep='第 9 回 ／ 第 III 部 厳密とは何か',
      eyebrow='生の実数の厳密値は、一件もない',
      h1='厳密値を全部集めたら、<br>整数と \\(\\pi\\) しかなかった',
      sub='そして第6回で喜んだ「パラメータ不要の関係 5 本」は、<br><em>5 本とも厳密ではありませんでした。</em>',
      byline_l='必要な予備知識：第8回（近似の三分類）',
      byline_r='検証：kensho/calc04.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第9回です。表に挙げた厳密値（アノマリー相殺、指数定理、アドラー和則、\\(A/4\\)、\\(\\pi/12\\)、2 次元イジングの臨界指数など）はいずれも<strong>確立した標準的な内容</strong>です。<em>それらを「値の型」で分類し、フィルタとして使えると整理したのが本シリーズの部分</em>です（kensho/calc04.py）。<strong>「生の実数の厳密値は一件もない」は網羅的な調査の結果ではなく、集めた範囲での観察</strong>です。<strong>3 次元イジングの \\(\\nu\\) に閉じた形が無いことは証明されていません</strong>。04節のフィルタには反例があり、次回で扱います。</p>')
