# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">ここまでずっと「1 % で合う」「15 % 以内」と書いてきました。<em>それは近似です。</em> では厳密とは何か ── 調べてみると、<strong>近似には三種類あって、そのうち一つは原理的に改良できません</strong>。そして第 II 部で作ったものが、まさにそれでした。</p>

<h2><span class="n">01</span>三種類ある</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>種類</th><th>中身</th><th>例</th><th>伸びしろ</th></tr></thead>
<tbody>
<tr class="hi"><th><strong>厳密</strong></th><td>誤差がゼロ。近似ではない</td><td>アノマリー相殺、指数定理</td><td><strong>改良の余地が無い</strong></td></tr>
<tr class="hi"><th><strong>制御された近似</strong></th><td>誤差の形が分かっていて、<strong>ゼロに持っていける</strong></td><td>格子 QCD、カイラル摂動論</td><td><strong>計算量を払えばいくらでも</strong></td></tr>
<tr><th>制御されていない近似</th><td>誤差がいくらか<strong>分からない</strong></td><td>構成子模型、バッグ模型</td><td><strong>改良できない</strong></td></tr>
</tbody>
</table>
</div>

<p>いちばん下と、上の二つとの差が決定的です。</p>

<div class="keybox">
<span class="lbl">第 II 部への判定</span>
<p><strong>第6回で作ったのは、いちばん下でした。</strong></p>
<p>「1 % で合う」が<em>なぜ 1 % なのか説明できない</em>のが、その証拠です。次に良くする方法もありません ── パラメータをもう一つ足す以外に。</p>
</div>

<p>だから「これだと単なる近似だ」という不満は、<strong>正しい</strong>のです。ただし「近似だから駄目」で切ると、真ん中の行まで捨ててしまいます。真ん中は<em>厳密値への収束列</em>であって、近似の対義語ではありません。</p>

<h2><span class="n">02</span>「厳密」と「閉じた形」は、別物</h2>

<p>ここが、この回のいちばん大事なところです。</p>

<p>\(\pi = 3.14159265358979\dots\) に、<strong>近似は一つも入っていません</strong>。無限に続きますが、それは厳密に定まった一つの実数です。</p>

<p>同じように、陽子質量とストリング張力の比 \(m_p/\sqrt{\sigma} = 2.13\dots\) も、<strong>QCD が厳密に定義している一つの実数</strong>です。違うのは、<em>短い式で書けるかどうか</em>だけ。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">厳密か</th><th class="mid">閉じた形</th><th>中身</th></tr></thead>
<tbody>
<tr><th>\(\pi\)</th><td class="mid">厳密</td><td class="mid">あり</td><td>円周率という定義がある</td></tr>
<tr class="hi"><th><strong>\(m_p/\sqrt{\sigma}\)</strong></th><td class="mid"><strong>厳密</strong></td><td class="mid"><strong>なし</strong></td><td><strong>QCD が定義している実数</strong></td></tr>
<tr><th>構成子模型の 1 %</th><td class="mid"><strong>近似</strong></td><td class="mid">─</td><td>そもそも別の量を計算している</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">願いが二つ混ざっている</span>
<p>「厳密に一致させたい」と書くと、<em>別の二つの願い</em>が混ざります。</p>
<p><strong>(i) 誤差ゼロで決まってほしい</strong> → 格子で原理的に達成できる<br>
<strong>(ii) 短い式で書けてほしい</strong> → 3 次元以上では前例が一つも無い</p>
</div>

<h2><span class="n">03</span>(i) はどこまで行けるか ── 値段を計算する</h2>

<p>格子計算の誤差は \(\varepsilon \propto a^2\)、コストは \(\propto a^{-6}\)。つまり <strong>コスト \(\propto \varepsilon^{-3}\)</strong>。</p>

<div class="calc">
<span class="tag">計算（kensho/calc04.py ⑥）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">目標精度</th><th class="mid">コスト [flops]</th><th>現実味</th></tr></thead>
<tbody>
<tr class="hi"><td class="mid">\(10^{-2}\)</td><td class="mid">\(10^{19}\)</td><td><strong>達成済み</strong></td></tr>
<tr><td class="mid">\(10^{-3}\)</td><td class="mid">\(10^{22}\)</td><td>現実的</td></tr>
<tr><td class="mid">\(10^{-4}\)</td><td class="mid">\(10^{25}\)</td><td>現実的</td></tr>
<tr><td class="mid">\(10^{-5}\)</td><td class="mid">\(10^{28}\)</td><td>世界中の計算機を数年</td></tr>
<tr><td class="mid">\(10^{-6}\)</td><td class="mid">\(10^{31}\)</td><td>世界の計算力 300 年ぶん</td></tr>
</tbody>
</table>
</div>

<p><strong>桁を 1 つ増やすたびに、計算は 1000 倍。</strong> 当面の壁は 4〜5 桁です。</p>

<p>ただしこれは「近似だから駄目」という話ではありません。<em>誤差が制御されている</em> ── どこまで行きたいかを言えば、いくら払えばよいかが計算できる。これが真ん中の行の意味です。</p>

<h2><span class="n">04</span>第 II 部の方法を、この目で仕分け直す</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>方法</th><th class="mid">種類</th><th>次に良くする方法</th></tr></thead>
<tbody>
<tr><th>アノマリー相殺、\(N_c=3\)</th><td class="mid"><strong>厳密</strong></td><td>不要（誤差ゼロ）</td></tr>
<tr><th>格子 QCD</th><td class="mid"><strong>制御された近似</strong></td><td>格子を細かくする（1000 倍で 1 桁）</td></tr>
<tr><th>カイラル摂動論</th><td class="mid"><strong>制御された近似</strong></td><td>次の次数まで計算する</td></tr>
<tr class="hi"><th><strong>構成子模型</strong></th><td class="mid"><strong>制御されていない</strong></td><td><strong>無い</strong></td></tr>
<tr class="hi"><th><strong>バッグ模型</strong></th><td class="mid"><strong>制御されていない</strong></td><td><strong>無い</strong></td></tr>
<tr><th>Gell-Mann–Okubo</th><td class="mid">制御されていない</td><td>SU(3) 破れの 2 次は書けるが、係数が新しいパラメータになる</td></tr>
</tbody>
</table>
</div>

<div class="aside">
<span class="tag">「次に良くする方法があるか」が判定基準</span>
<p>これが三分類の実務的な使い方です。<strong>手元の計算が「制御された」側か「制御されていない」側かは、次の一手を言えるかどうかで分かります。</strong></p>
<p>格子なら「格子間隔を半分にする」と言える。構成子模型では、言えることが「パラメータを増やす」しかない ── <em>そしてそれは第2回の帳簿で、いちばん高い買い物でした</em>。</p>
</div>

<h2><span class="n">05</span>だから、目標は言い直せる</h2>

<div class="keybox">
<span class="lbl">言い直し</span>
<p>× 「近似ではなく厳密に一致させたい」</p>
<p>○ <strong>(i) 制御されていない近似を、制御された近似に格上げする</strong><br>
○ <strong>(ii) そもそも厳密になりうる問いを、先に見分ける</strong></p>
</div>

<p>(i) の方は、やり方がはっきりしています ── 誤差の展開が書けるところまで戻る。</p>

<p>(ii) の方は、まだ何も分かっていません。<em>どんな問いなら厳密な答えが返ってくるのか</em>。次回はそれを、実際に厳密値を全部集めることで調べます。</p>

<div class="caveat">
<span class="tag">正直な線</span>
<p>03節のコスト外挿は \(a^{-6}\) という一つの仮定に依ります。<strong>アルゴリズムの改良（過去 30 年で \(10^{6}\) 倍あった）は勘定に入れていません</strong> ── 「壁」は動きうる、ということです。<br>04節の「制御されていない」という判定は、<em>その模型が役に立たないという意味ではありません</em>。構成子模型は暗算で 1 % に届きます。判定しているのは「次の一手があるか」だけです。</p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>物理で<strong>厳密に成り立っているものを、全部集めます</strong>。すると驚くほどきれいな結果が出ました ── <em>例外なく、整数・小さい有理数・\(\pi\) の有理数倍。生の実数の厳密値は、一件もありません。</em></p>
</div>'''

build(out='../butsuri-kantan-08-three-approximations.html', acc='#4a2f52', ops='#8a5a1a',
      title='第8回：近似には、三種類ある ── 物理を簡単にする',
      ep='第 8 回 ／ 第 III 部 厳密とは何か',
      eyebrow='厳密／制御された近似／制御されていない近似 ── 一つは改良できない',
      h1='近似には、<br>三種類ある',
      sub='「近似だから駄目」で切ると、<em>厳密値への収束列</em>まで捨ててしまいます。<br>そして「厳密」と「閉じた形」は別物でした。',
      byline_l='必要な予備知識：第 II 部（強い力の層）',
      byline_r='検証：kensho/calc04.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第8回です。格子 QCD のコストスケーリングとカイラル摂動論の系統的改良可能性は<strong>標準的な内容</strong>です。<em>「近似の三分類」と「次の一手があるかで判定する」という整理は本シリーズのもの</em>で、教科書の用語ではありません（「制御された近似」自体は分野で使われる言い方です）。数値は kensho/calc04.py で計算しました。<strong>03節の外挿はアルゴリズム改良を含んでいません</strong>。04節の判定は模型の有用性についてのものではありません。</p>')
