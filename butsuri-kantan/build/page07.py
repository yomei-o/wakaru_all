# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">前の二回は「単純にした」と言いながら、<strong>12 個の定数を持ち込んでいました</strong>。構成子質量、超微細係数、バッグ定数 ── どれも出どころが説明されていません。この回では、それを一つずつ潰します。三つのふるいにかけると、<em>全部落ちました</em>。強い力の本物の入力は <strong>0 個</strong>です。</p>

<h2><span class="n">01</span>まず、持ち込んだものを全部並べる</h2>

<div class="calc">
<span class="tag">計算（kensho/calc03.py ①）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>定数</th><th class="mid">値</th><th>出どころ</th></tr></thead>
<tbody>
<tr><th>\(m_u\)（中間子）</th><td class="mid">291 MeV</td><td>フィット</td></tr>
<tr><th>\(m_s\)（中間子）</th><td class="mid">484 MeV</td><td>フィット</td></tr>
<tr><th>\(A_M^{1/3}\)</th><td class="mid">367 MeV</td><td>フィット</td></tr>
<tr><th>\(m_u\)（バリオン）</th><td class="mid">364 MeV</td><td>フィット</td></tr>
<tr><th>\(m_s\)（バリオン）</th><td class="mid">537 MeV</td><td>フィット</td></tr>
<tr><th>\(A_B^{1/3}\)</th><td class="mid">297 MeV</td><td>フィット</td></tr>
<tr><th>\(B^{1/4}\)（バッグ）</th><td class="mid">145 MeV</td><td>フィット</td></tr>
<tr><th>\(\Lambda_{\overline{\rm MS}}\)</th><td class="mid">332 MeV</td><td>入力</td></tr>
<tr><th>\(x = 2.04\)、\(Z_0 = 1.84\)</th><td class="mid">─</td><td>？</td></tr>
<tr><th>\(\langle \mathbf{S}_i\cdot\mathbf{S}_j\rangle\)、色因子</th><td class="mid">─</td><td>？</td></tr>
</tbody>
</table>
</div>

<p>合計 12 個。<strong>これを数えずに「単純にした」と言うのは、帳簿をごまかしています。</strong></p>

<h2><span class="n">02</span>ふるい① ── それは、計算できる純粋な数か</h2>

<p>下の四つは、値を決める自由が<em>そもそもありません</em>。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>定数</th><th>中身</th><th>出どころ</th></tr></thead>
<tbody>
<tr><th>\(\langle \mathbf{S}_i\cdot\mathbf{S}_j\rangle\)</th><td>\(-3/4, +1/4, \pm 1, \dots\)</td><td><strong>スピンの足し算</strong></td></tr>
<tr><th>色因子 \(-16/3, -8/3\)</th><td>中間子と 3 体の違い</td><td><strong>SU(3) の 2 次カシミール</strong></td></tr>
<tr><th>\(x = 2.0428\)</th><td>球の中の質量ゼロのディラック粒子の最低モード</td><td><strong>\(j_0(x)=j_1(x)\) の最初の解</strong></td></tr>
</tbody>
</table>
</div>

<p>\(x = 2.0428\) は<strong>ベッセル関数の零点</strong>です。円周率が 3.14159… であるのと同じ種類の数で、決める自由度はゼロ。</p>

<div class="keybox">
<span class="lbl">ふるい① の結果</span>
<p><strong>これらは「意味不明な定数」ではなく、計算をサボった記号でした。</strong><br>消せる ── というより、<em>最初から入力ではなかった</em>。</p>
</div>

<h2><span class="n">03</span>ふるい② ── それは、唯一のスケールの \(O(1)\) 倍か</h2>

<p>残った次元を持つ定数を、全部 \(\Lambda = 332\) MeV で割ってみます。</p>

<div class="calc">
<span class="tag">計算（kensho/calc03.py ③）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>定数</th><th class="mid">値 [MeV]</th><th class="mid">\(\Lambda\) の何倍</th></tr></thead>
<tbody>
<tr><th>\(B^{1/4}\)（バッグ）</th><td class="mid">145</td><td class="mid">0.44</td></tr>
<tr><th>\(m_u\)（中間子）</th><td class="mid">291</td><td class="mid">0.88</td></tr>
<tr><th>\(A_B^{1/3}\)</th><td class="mid">297</td><td class="mid">0.89</td></tr>
<tr><th>\(m_u\)（バリオン）</th><td class="mid">364</td><td class="mid">1.10</td></tr>
<tr><th>\(A_M^{1/3}\)</th><td class="mid">367</td><td class="mid">1.10</td></tr>
<tr><th>\(m_s\)（中間子）</th><td class="mid">484</td><td class="mid">1.46</td></tr>
<tr class="hi"><th>\(m_s\)（バリオン）</th><td class="mid">537</td><td class="mid"><strong>1.62</strong></td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">計算（kensho/calc03.py ③）</span>
<p>全部 <strong>0.44〜1.62 倍</strong>、開きは <strong>3.7 倍</strong>しかない。</p>
<p>完全に自由なら \(8\times5.37 = \mathbf{43}\) ビット払う。<br>
実際は \(\Lambda\) の 3.7 倍の窓に収まるので、<strong>15 ビット</strong>しか新しくない。<br>
→ <strong>65 % は \(\Lambda\) 一つで決まっていた。</strong></p>
</div>

<p><em>「定数が増えた」のは見かけだけ</em>でした。8 個あるように見えて、実質は 3 個分の情報しかない。</p>

<h2><span class="n">04</span>ふるい③ ── その \(\Lambda\) は、そもそも定数か</h2>

<p>ここで一段深くなります。\(\Lambda\) は質量の次元を持ちます。<strong>次元を持つ量は、単位の取り方で数値が変わります。</strong> だから \(\Lambda\) は「世界についての数」ではなく、<em>単位を決めているだけ</em>です。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">次元</th><th>身分</th></tr></thead>
<tbody>
<tr><th>\(\Lambda_{\rm QCD}\)</th><td class="mid">質量</td><td>定数ではなく<strong>単位</strong></td></tr>
<tr><th>\(m_q\)（クォーク質量）</th><td class="mid">質量</td><td>同上</td></tr>
<tr class="hi"><th><strong>\(m_q/\Lambda\)</strong></th><td class="mid"><strong>無次元</strong></td><td><strong>これが本当の入力</strong></td></tr>
<tr><th>\(m_p/\Lambda\)</th><td class="mid">無次元</td><td><strong>計算で出る（入力ではない）</strong></td></tr>
</tbody>
</table>
</div>

<h2><span class="n">05</span>そして、残りも実際に消されている</h2>

<p>これは机上の整理ではありません。<strong>格子 QCD は、①の 12 個を一つも使いません。</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>方法</th><th>余分な入力</th><th class="mid">個数</th><th class="mid">計算量</th></tr></thead>
<tbody>
<tr><th>構成子模型</th><td>\(m_u, m_s, A\)（中間子・バリオン別）＋ \(B, Z_0\)</td><td class="mid">8</td><td class="mid">四則演算</td></tr>
<tr class="hi"><th><strong>格子 QCD</strong></th><td><strong>ゲージ結合 1 個 ＋ クォーク質量</strong></td><td class="mid"><strong>0</strong></td><td class="mid"><strong>\(10^{19}\) flops</strong></td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">計算（kensho/calc03.py ④）</span>
<p>消したパラメータ： 8 個 \(= \mathbf{43}\) ビット<br>
払った計算量　　： \(63 - 7 = \mathbf{56}\) ビット</p>
<p>→ <strong>パラメータ 1 ビットを消すのに、計算 1.3 ビット。</strong></p>
</div>

<div class="keybox">
<span class="lbl">この回の要点</span>
<p><strong>「意味不明な定数が増える」は、計算を避けた代金です。</strong></p>
<p>第 I 部で測った三つの通貨の、そのままの実演でした。</p>
</div>

<h2><span class="n">06</span>極端に行くと、入力がゼロになる</h2>

<p>クォーク質量を全部ゼロにした純粋な QCD（純ヤン・ミルズ）は、<strong>無次元パラメータをただの一つも持ちません</strong>。すべての比が、計算で決まる純粋な数になります。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">\(\sqrt{\sigma}\) の何倍</th><th class="mid">誤差</th></tr></thead>
<tbody>
<tr><th>グルーボール \(0^{++}\)</th><td class="mid">3.405</td><td class="mid">±0.021</td></tr>
<tr><th>グルーボール \(2^{++}\)</th><td class="mid">4.850</td><td class="mid">±0.040</td></tr>
<tr><th>グルーボール \(0^{-+}\)</th><td class="mid">5.800</td><td class="mid">±0.100</td></tr>
<tr><th>グルーボール \(1^{+-}\)</th><td class="mid">6.270</td><td class="mid">±0.090</td></tr>
</tbody>
</table>
</div>

<p>これらは <strong>\(\pi\) や \(e\) と同じ種類の数</strong>です。測って決めるものではなく、<em>理論が持っている数</em>。</p>

<h2><span class="n">07</span>棚卸しの結果</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>種類</th><th class="mid">個数</th><th>理由</th></tr></thead>
<tbody>
<tr><th>スピン係数、色因子、ベッセル零点</th><td class="mid">0</td><td>計算できる純粋な数</td></tr>
<tr><th>構成子質量、\(A\)、\(B\)</th><td class="mid">0</td><td>\(\Lambda\) の \(O(1)\) 倍。格子は使わない</td></tr>
<tr><th>\(\Lambda_{\rm QCD}\)</th><td class="mid">0</td><td>次元を持つ → 単位</td></tr>
<tr class="hi"><th><strong>クォーク質量の比 6 個</strong></th><td class="mid"><strong>6</strong></td><td><strong>無次元。計算で出せない</strong></td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>第 II 部の結論</h2>
<p><strong>12 個 → 0 個。</strong> 強い力の本物の入力は、クォーク質量の比 6 個だけでした。</p>
<p>しかもその 6 個は QCD の話ではなく、<em>ヒッグスの話</em>です。</p>
<p>→ <strong>強い力そのものは、パラメータをほぼ持っていません。</strong></p>
</div>

<h2><span class="n">08</span>持ち帰る三つのふるい</h2>

<div class="keybox">
<span class="lbl">「意味不明な定数が増えた」と感じたら</span>
<p>① <strong>純粋な数か</strong> ── 群論・特殊関数から出るなら、それは記号であって定数ではない<br>
② <strong>唯一のスケールの \(O(1)\) 倍か</strong> ── そうなら、増えているのは見かけだけ<br>
③ <strong>無次元か</strong> ── 次元を持つなら単位であって、世界についての数ではない</p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>03節の「\(\Lambda\) の 3.7 倍以内」は、\(\Lambda\) の定義（スキーム、\(n_f\)）に依ります。\(\Lambda\) を 2 倍違う値に取れば倍率は全部ずれますが、<strong>開きの幅は変わりません</strong>。<br>05節の「\(10^{19}\) flops \(=63\) ビット」は桁の見積もりで、交換レート 1.3 は 2 倍の幅を持ちます。<br>06節のグルーボール質量は<strong>まだ実験で確認されていません</strong>（格子の計算値どうしは一致していますが、対応する粒子の同定が未確定）。<br>そして最大の留保 ── <em>「消せる」と「消した方がよい」は別</em>です。構成子模型は 8 個払って暗算で 1 % に届き、格子は 0 個で \(10^{19}\) flops。目標が「わかりやすく」なら、<strong>前者の方が正しい選択でありうる</strong>。</p>
</div>

<div class="next">
<span class="lbl">次回から第 III 部</span>
<p>ここまでずっと「1 % で合う」「15 % 以内」と書いてきました。<em>それは近似です</em>。では<strong>厳密</strong>とは何なのか。近似には三種類あって、そのうち一つは<strong>改良できません</strong> ── そしてこの二回で作ったものが、まさにそれでした。</p>
</div>'''

build(out='../butsuri-kantan-07-inventory.html', acc='#2a4d3a', ops='#8a5a1a',
      title='第7回：持ち込んだ定数を、棚卸しする ── 物理を簡単にする',
      ep='第 7 回 ／ 第 II 部 強い力で実演する（部の終わり）',
      eyebrow='12 個 → 0 個。本物の入力はクォーク質量比 6 個だけ',
      h1='持ち込んだ定数を、<br>棚卸しする',
      sub='「単純にした」と言いながら、12 個の定数を持ち込んでいました。<br><em>三つのふるいにかけたら、全部落ちました。</em>',
      byline_l='必要な予備知識：第5〜6回（層と構成子模型）',
      byline_r='検証：kensho/calc03.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第7回（第 II 部の終わり）です。色因子、ベッセル零点、格子 QCD の入力、グルーボール質量比はいずれも<strong>確立した標準的な内容</strong>です。新しいのは<em>「三つのふるい」という整理と、パラメータと計算量の交換レートを数えたこと</em>で、これは本シリーズの枠組みです（kensho/calc03.py）。<strong>\\(\\Lambda\\) の値はスキーム依存</strong>で、03節の倍率はその取り方で動きます。<strong>グルーボールは実験的に未確認</strong>です。「消せる」と「消した方がよい」は別だという留保を、07節の結論と同じ重みで読んでください。</p>')
