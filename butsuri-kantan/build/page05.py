# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">物差しができたので、いちばん手強い相手に当てます ── <strong>強い力</strong>です。一気に解こうとするから \(10^{19}\) flops になる。<em>層に切って、下から順に</em>やってみます。この回は下の二層 ── <strong>指数関数 1 個で 65 ビットが決まり、割り算だけで全部が桁の中に収まりました。</strong></p>

<h2><span class="n">01</span>切り方</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">層</th><th>何を決めるか</th><th>使う道具</th><th class="mid">計算の重さ</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">第 0 層</th><td>なぜ 1 GeV なのか（スケールそのもの）</td><td><strong>次元転移</strong></td><td class="mid"><strong>1 行</strong></td></tr>
<tr class="hi"><th class="mid">第 2 層</th><td>全部の質量が \(\Lambda\) の \(O(1)\) 倍</td><td><strong>次元解析</strong></td><td class="mid"><strong>暗算</strong></td></tr>
<tr><th class="mid">第 3 層</th><td>その \(O(1)\) の中身のパターン</td><td>構成子＋スピンの足し算</td><td class="mid">四則演算</td></tr>
<tr><th class="mid">第 4 層</th><td>残り</td><td>格子 QCD</td><td class="mid">\(10^{19}\) flops</td></tr>
</tbody>
</table>
</div>

<p>この回は上の二つ。第 3 層は次回、第 4 層は第 III 部で扱います。</p>

<h2><span class="n">02</span>第 0 層 ── 指数関数 1 個で、スケールが決まる</h2>

<p>強い力の結合定数はエネルギーとともに走ります。それを逆に解くと、<em>結合が強くなる場所</em>がひとつ決まる。それが \(\Lambda\) です。</p>

<div class="keybox">
<span class="lbl">次元転移</span>
<p>\[\Lambda = \mu\,\exp\!\left(-\frac{2\pi}{b_0\,\alpha_s(\mu)}\right),\qquad b_0 = 11 - \frac{2n_f}{3}\]</p>
</div>

<div class="calc">
<span class="tag">計算（kensho/calc02.py ②）</span>
<p>\(n_f=5\) → \(b_0 = 7.667\)、\(\alpha_s(M_Z) = 0.1180\)<br>
→ \(\Lambda \approx \mathbf{88}\) MeV（1 ループなので粗い。2 ループなら 210 MeV）</p>
</div>

<p>ここで大事なのは値そのものではなく、<strong>この式が何を成し遂げているか</strong>です。</p>

<div class="calc">
<span class="tag">計算（kensho/calc02.py ②）</span>
<p>プランク質量 \(1.22\times10^{22}\) MeV から \(\Lambda \approx 300\) MeV まで <strong>19.6 桁</strong><br>
= <strong>65 ビットの階層</strong>。これを買う値段は \(\log_2 65 = \mathbf{6.0}\) ビット</p>
</div>

<div class="keybox">
<span class="lbl">第 0 層の成果</span>
<p><strong>65 ビットを 6.0 ビットで買っている（圧縮 11 倍）。</strong></p>
<p>指数関数が 1 個あるだけで、原子核のスケールが全部決まります。</p>
</div>

<p>なぜこんなに安いのか。指数関数の中身を 1 桁決めれば、外側は何十桁でも決まるからです。<em>複利と同じ</em> ── 利率を小数第一位まで決めれば、100 年後の残高は何十桁でも定まる。</p>

<h2><span class="n">03</span>第 2 層 ── 割り算だけで、どこまで行くか</h2>

<p>スケールが一つ決まったので、あとは全部それで割ってみます。\(\Lambda_{\overline{\rm MS}}(n_f=3) \approx 332\) MeV を使います。</p>

<div class="calc">
<span class="tag">計算（kensho/calc02.py ③）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>ハドロン</th><th class="mid">質量 [MeV]</th><th class="mid">\(\Lambda\) の何倍</th></tr></thead>
<tbody>
<tr><th>\(\pi\)</th><td class="mid">138.0</td><td class="mid">0.42</td></tr>
<tr><th>\(K\)</th><td class="mid">495.6</td><td class="mid">1.49</td></tr>
<tr><th>\(\rho\)</th><td class="mid">775.3</td><td class="mid">2.34</td></tr>
<tr><th>\(K^*\)</th><td class="mid">893.6</td><td class="mid">2.69</td></tr>
<tr class="hi"><th>核子</th><td class="mid">938.9</td><td class="mid"><strong>2.83</strong></td></tr>
<tr><th>\(\phi\)</th><td class="mid">1019.5</td><td class="mid">3.07</td></tr>
<tr><th>\(\Lambda\)</th><td class="mid">1115.7</td><td class="mid">3.36</td></tr>
<tr><th>\(\Sigma\)</th><td class="mid">1193.2</td><td class="mid">3.59</td></tr>
<tr><th>\(\Delta\)</th><td class="mid">1232.0</td><td class="mid">3.71</td></tr>
<tr><th>\(\Xi\)</th><td class="mid">1318.3</td><td class="mid">3.97</td></tr>
<tr><th>\(\Sigma^*\)</th><td class="mid">1384.6</td><td class="mid">4.17</td></tr>
<tr><th>\(\Xi^*\)</th><td class="mid">1533.4</td><td class="mid">4.62</td></tr>
<tr class="hi"><th>\(\Omega\)</th><td class="mid">1672.5</td><td class="mid"><strong>5.04</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>全部 0.42〜5.04 倍。</strong> 桁で外れているものは一つもありません。</p>

<div class="calc">
<span class="tag">計算（kensho/calc02.py ⑤）</span>
<p>事前に「\(\Lambda\) の \(10^{-2}\)〜\(10^{2}\) 倍」と置くと <strong>13.3 ビット</strong>の不定性<br>
実際に収まった幅は <strong>3.6 ビット</strong><br>
→ <strong>買い 9.7 ビット、追加パラメータ 0</strong></p>
</div>

<p>これが「強い力の量は \(\Lambda\) の \(O(1)\) 倍」という言い方の中身です。<em>暗算で 10 ビット</em>。</p>

<h2><span class="n">04</span>ただし、まだ 12 倍の開きがある</h2>

<p>0.42（\(\pi\)）と 5.04（\(\Omega\)）では 12 倍違います。この幅を潰すのが次の層です。</p>

<div class="aside">
<span class="tag">下の二層で分かったこと</span>
<p><strong>「なぜ 1 GeV なのか」は 1 行で片づく</strong> ── しかも \(10^{19}\) 桁ぶんの決定を 6 ビットで買っている。<br><strong>「どれも同じくらいの重さか」も暗算で片づく</strong> ── 桁は全部当たる。<br>残ったのは <em>同じ桁の中でのパターン</em> だけです。</p>
</div>

<h2><span class="n">05</span>なぜ層に切ると得なのか</h2>

<p>第 I 部の言葉で言うと、こうです。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">層</th><th class="mid">買い</th><th class="mid">払い</th><th class="mid">計算量</th></tr></thead>
<tbody>
<tr><th class="mid">第 0 層</th><td class="mid"><strong>65 ビット</strong></td><td class="mid">6.0 ビット</td><td class="mid">1 行</td></tr>
<tr><th class="mid">第 2 層</th><td class="mid">9.7 ビット</td><td class="mid"><strong>0</strong></td><td class="mid">暗算</td></tr>
</tbody>
</table>
</div>

<p>いちばん大きな買い物が、いちばん安い計算で済んでいます。<strong>一気に解くと、この構造が見えません</strong> ── 格子 QCD に全部投げると、65 ビットも 9.7 ビットも残りの数 % も、区別なく \(10^{19}\) flops の中に入ってしまう。</p>

<div class="caveat">
<span class="tag">正直な線</span>
<p>02節の \(\Lambda \approx 88\) MeV は<strong>1 ループの粗い値</strong>で、2 ループなら 210 MeV です。桁の話としてだけ読んでください。03節で使った \(332\) MeV は \(n_f=3\) の標準値で、<em>スキームの取り方に依存します</em>。<br>「19.6 桁 ＝ 65 ビット」の階層は、プランク質量を上端に取ったときの話です。上端の取り方で数値は動きますが、<strong>「指数関数 1 個が桁を稼ぐ」という構造は動きません</strong>。</p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>残った 12 倍の幅を潰します。使うのは <strong>足し算だけ</strong> ── 構成子質量とスピンの合成。それで 8 個のバリオンが <em>全部 1 % 以内</em>に入ります。おまけに、パラメータを一つも足さない関係が <strong>5 本</strong>残りました。</p>
</div>'''

build(out='../butsuri-kantan-05-layers.html', acc='#2a4d3a', ops='#8a5a1a',
      title='第5回：強い力を、四つの層に切る ── 物理を簡単にする',
      ep='第 5 回 ／ 第 II 部 強い力で実演する',
      eyebrow='指数関数 1 個で 65 ビット、割り算だけで 9.7 ビット',
      h1='強い力を、<br>四つの層に切る',
      sub='一気に解くから \\(10^{19}\\) flops になる。<br><em>下から順にやると、いちばん大きな買い物がいちばん安く済みました。</em>',
      byline_l='必要な予備知識：第 I 部（三つの通貨）',
      byline_r='検証：kensho/calc02.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第5回です。次元転移、\\(\\Lambda_{\\rm QCD}\\)、\\(\\beta\\) 関数の 1 ループ係数はいずれも<strong>確立した標準的な内容</strong>です。新しいのは<em>それらを「層に切って、各層が何ビット説明したか」を数えたこと</em>で、この数え方は本シリーズの独自のものです。数値は kensho/calc02.py で計算しました。<strong>\\(\\Lambda\\) の値はスキームと \\(n_f\\) の取り方に依存し</strong>、02節の 88 MeV は 1 ループの粗い値です。「65 ビットの階層」はプランク質量を上端に取った場合の値です。</p>')
