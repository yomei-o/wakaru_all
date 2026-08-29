# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">50 回のあいだ、「無次元は物理、次元付きは帳簿」を背骨にしてきました。<strong>では、無次元量とはいったい何なのか。</strong> そして<strong>それらは本当に定数なのか。</strong> 二つの問いを詰めたら ── <em>「0 の列」は一様ではなく、対数は発見ではなく、そして定数はほとんど一つも残りませんでした。</em></p>

<h2><span class="n">01</span>無次元量とは、電波で送れるもの</h2>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>「1 メートル」は送れない</strong><span>受け取る側に物差しが要る ── 物を運ばないと伝わらない</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>「\(\alpha=1/137.036\)」は送れる</strong><span>受け取った側が<em>自分の実験で確かめられる</em></span></div></div>
<div class="row"><div class="mk">47</div><div class="txt"><strong>SI が \(c\) を法令で決めて \(\alpha\) を決められなかったのも、これと同じこと</strong><span>第47回 ── 単位の定義は、送れる量には触れない</span></div></div>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>無次元量とは、物を運ばずに伝えられる量です。</strong><br>
── それが「物理」の中身でした。</p>
</div>

<h2><span class="n">02</span>ところが「0 の列」は、一様ではなかった</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>型</th><th class="mid">例</th><th class="mid">群</th><th class="mid">自然な測度（Haar）</th><th class="mid">全測度</th></tr></thead>
<tbody>
<tr class="hi"><th>比（スケール的）</th><td class="mid">\(\alpha\)、\(m_p/m_e\)、\(\rho_\Lambda/\rho_P\)</td><td class="mid">乗法群 \(\mathbb{R}_+\)</td><td class="mid">\(d(\ln x)\)＝対数一様</td><td class="mid"><strong>発散する</strong></td></tr>
<tr class="hi"><th>角度・位相</th><td class="mid">\(\theta_{\rm QCD}\)、CKM/PMNS</td><td class="mid">コンパクト群 \(U(1)\) など</td><td class="mid">\(d\theta\)＝一様</td><td class="mid"><strong>有限</strong></td></tr>
<tr><th>個数</th><td class="mid">世代 3、色 3、次元 4</td><td class="mid">離散</td><td class="mid">数える</td><td class="mid">有限</td></tr>
<tr><th>指数（対数微分）</th><td class="mid">\(n_s\)、\(\nu\)、\(\eta\)、\(\omega\)</td><td class="mid">接空間</td><td class="mid">定めにくい</td><td class="mid">──</td></tr>
</tbody>
</table>
</div>

<p><strong>50 回のあいだ、これをひとつの列に入れて扱ってきました。</strong> <em>中身は少なくとも四種類あり、群が違います。</em></p>

<h2><span class="n">03</span>「本当に対数なのか」── 対数は発見ではなく、同型</h2>

<div class="calc">
<span class="tag">比は掛け算で合成する ── 乗法群</span>
$$\log:\ \mathbb{R}_+\ \xrightarrow{\ \cong\ }\ \mathbb{R}
\qquad\text{Haar 測度}\ \frac{dx}{x}=d(\ln x)$$
<p class="lbl">対数一様が「自然」なのは、それが乗法群の Haar 測度だから ── <strong>発見ではなく、群の同型</strong></p>
</div>

<div class="calc">
<span class="tag">角度は足し算で合成し、\(2\pi\) で戻る ── コンパクト群</span>
$$\text{Haar 測度}\ d\theta\ \text{（一様）}\qquad\Longrightarrow\qquad \textbf{角度の }\log\textbf{ には意味が無い}$$
</div>

<div class="keybox">
<p class="lbl">03節の結論</p>
<p style="margin:6px 0 0"><strong>ビットは、量そのものの対数ではありません。確率の対数です。</strong><br>
\(-\log_2(\text{確率})\) を測るには測度が要り、<em>測度は群が決めます</em>。<br>
── 本シリーズが 50 回ぶんやってきたのは、ずっとこれでした。</p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>核心 ── これで第48回の基準が「定理」になる</h2>

<div class="seven">
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>コンパクト群 → Haar 測度が有限 → 正規化できる</strong><span>事前分布が<em>一意に決まる</em> → 微調整の議論は <strong>well-posed</strong></span></div></div>
<div class="row"><div class="mk">✗</div><div class="txt"><strong>非コンパクト（\(\mathbb{R}_+\)）→ Haar 測度が無限 → 正規化できない</strong><span>事前分布は<em>決まらない</em>（切断を入れるのは選択）→ 微調整の議論は <strong>ill-posed</strong></span></div></div>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと（その一）</p>
<p style="margin:6px 0 0">第48回の「<em>角度には理由がある、質量比には無い</em>」は ──<br>
<strong>コンパクトか否かの言い換えでした。</strong><br>
── <em>基準ではなく、定理です。</em></p>
</div>

<h2><span class="n">05</span>検証 ── コンパクト類のなかで、ビットは深刻さを予測するか</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>角度</th><th class="mid">値 [度]</th><th class="mid">驚き [bit]</th><th class="mid">実際の扱われ方</th></tr></thead>
<tbody>
<tr><th>PMNS \(\theta_{23}\)</th><td class="mid">\(49.0\)</td><td class="mid">\(0.88\)</td><td class="mid">最大混合に近い（「小さい」とは別種）</td></tr>
<tr><th>PMNS \(\theta_{12}\)</th><td class="mid">\(33.4\)</td><td class="mid">\(1.43\)</td><td class="mid">とくに問題視されない</td></tr>
<tr><th>CKM \(\theta_{12}\)（カビボ角）</th><td class="mid">\(13.04\)</td><td class="mid">\(2.79\)</td><td class="mid">とくに問題視されない</td></tr>
<tr><th>PMNS \(\theta_{13}\)</th><td class="mid">\(8.57\)</td><td class="mid">\(3.39\)</td><td class="mid">小さめ、議論はある</td></tr>
<tr><th>CKM \(\theta_{23}\)</th><td class="mid">\(2.38\)</td><td class="mid">\(5.24\)</td><td class="mid">フレーバー階層の一部</td></tr>
<tr class="hi"><th>CKM \(\theta_{13}\)</th><td class="mid">\(0.201\)</td><td class="mid">\(8.81\)</td><td class="mid"><strong>フレーバー puzzle の中心</strong></td></tr>
<tr class="hi"><th>\(\theta_{\rm QCD}\)</th><td class="mid">\(<10^{-10}\)</td><td class="mid"><strong>\(35.87\)</strong></td><td class="mid"><strong>唯一の「危機」</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">05節の結論</p>
<p style="margin:6px 0 0"><strong>コンパクト類の中では、ビット数と深刻さがきれいに単調です</strong> ── 0〜3 ＝ 話題にならない／5〜9 ＝ フレーバー puzzle／36 ＝ 危機。<br>
そして<strong>争いのない微調整問題は、唯一の角度（\(\theta_{\rm QCD}\)）だけ</strong>。<br>
── 論争中のもの（\(v/M_P\)、\(\rho_\Lambda\)）はすべて非コンパクト類です。<br>
<em>論争しているのではありません。問いが well-posed でないから決まらないのです。</em></p>
</div>

<div class="fig">
<p class="cap">図：無次元量を二つの類に分けて並べたもの。<strong>左（コンパクト）ではビットが定義でき、深刻さと単調に対応します。右（非コンパクト）ではビット自体が事前分布次第で動きます</strong>。ツマミで事前範囲を動かしてください ── <em>左は動かず、右だけが動きます</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>非コンパクト側の事前範囲（桁）<input id="sd" type="range" min="10" max="300" value="123" step="1"></label>
  <span class="val" id="vd">123 桁</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a5a"></i>コンパクト類（角度）── 動かない</span>
  <span><i class="swatch" style="background:#8a4a2a"></i>非コンパクト類（比）── 事前次第で動く</span>
</div>
</div>

<h2><span class="n">06</span>次の問い ── では、それらは「定数」なのか</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>種別</th><th class="mid">個数</th><th class="mid">何について定数か</th><th class="mid">判定</th></tr></thead>
<tbody>
<tr class="hi"><th>走る結合定数（ゲージ 3、湯川 9、\(\lambda\)、混合角も弱く走る）</th><td class="mid">\(\approx24\)</td><td class="mid"><strong>スケールで変わる</strong></td><td class="mid">定数ではない</td></tr>
<tr class="hi"><th>\(\Lambda\)CDM の基本 6</th><td class="mid">\(6\)</td><td class="mid">この宇宙の<strong>状態</strong>の記述</td><td class="mid">法則の定数ではない</td></tr>
<tr><th>\(\theta_{\rm QCD}\)</th><td class="mid">\(1\)</td><td class="mid"><strong>RG 不変な角度</strong></td><td class="mid"><strong>定数と呼べる</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>「定数」と呼んできたものの大半は、走る関数でした。</strong> 第37回で見たとおり \(\alpha\) は \(0\) から \(M_Z\) で 7 パーセント動きます ── 私たちが「\(\alpha=1/137\)」と言うとき、それは<em>\(M_Z\) を選んだという規約込みの数</em>です。そして \(\Lambda\)CDM の 6 個はさらに違う ── <em>あれは法則ではなく、この宇宙の初期条件</em>。地球の公転半径を「自然定数」と呼ばないのと同じ理由で、定数ではありません。</p>

<h2><span class="n">07</span>では、本当に不変なのは何か</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">何に依らないか</th></tr></thead>
<tbody>
<tr><th>臨界指数 \(\nu=0.6300\)</th><td class="mid">スケール・スキーム・微視的な中身（第44回）</td></tr>
<tr><th>異常次元 \(\eta=0.0363\)</th><td class="mid">同上（第14回）</td></tr>
<tr><th>補正の指数 \(\omega=0.8303\)</th><td class="mid">同上</td></tr>
<tr><th>アノマリー係数 \(a\)、\(c\)</th><td class="mid">場の中身だけで決まる（第37回）</td></tr>
<tr class="hi"><th>\((D-1)(D-2)=6\)</th><td class="mid">次元だけで決まる（第38回）</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">07節の結論</p>
<p style="margin:6px 0 0">ところが ── <strong>これらは「自然定数」ではなく、定理です。</strong><br>
\(\nu=0.6300\) は 3 次元イジング固定点についての<em>数学的事実</em>であって、測って決めた入力ではありません。<br>
── <strong>本当に不変なものは、定数ではなく定理でした。</strong></p>
</div>

<h2><span class="n">08</span>残るのは \(\theta_{\rm QCD}\) ただ一つ。そして</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>独立な入力のうち、定数と呼べるのは \(\theta_{\rm QCD}\) だけ</strong><span>走る結合は関数、\(\Lambda\)CDM は状態、臨界指数は定理</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>ところが、その \(\theta_{\rm QCD}\) こそ、アクシオンが「場にして動かそう」としている当のもの</strong><span>ペッチェイ–クイン機構が正しければ、\(\theta\) は動的に \(0\) へ緩和する</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>もし PQ が正しければ、定数は一つも残らない</strong><span>走る結合／この宇宙の状態／数学の定理／緩和する場 ── それだけになる</span></div></div>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと（その二）</p>
<p style="margin:6px 0 0"><strong>「定数がいくつもあるのはおかしい、一つも無いのではないか」── かなりの精度で当たっています。</strong><br>
ただし正確には ── <em>独立な入力のうち、スケールに依らないものはほぼ無い。定数に見えるものは、出力（定理）か、この宇宙の状態か、走る関数の値である。</em></p>
</div>

<h2><span class="n">09</span>ついでに、番外編②を訂正しておく</h2>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>旧：「指数写像そのものが 47 倍の圧縮を生む」</strong><span>これは甘かった ── 写像が全単射で誘導事前を使うなら、<em>圧縮は厳密にゼロ</em></span></div></div>
<div class="row hi"><div class="mk">○</div><div class="txt"><strong>新：圧縮の実体は「\(\alpha\) の事前範囲が \(O(1)\) に縛られている」こと</strong><span>結合定数が \(O(1)\) なのには理由がある（摂動性、無次元性）── <em>スケールの比には無い</em></span></div></div>
<div class="row"><div class="mk">→</div><div class="txt"><strong>つまり第二の基準は、第一の基準に潰れる</strong><span>指数写像は「事前に理由がある量へ問いを運ぶ」道具にすぎなかった ── <em>五度目の圧縮</em></span></div></div>
</div>

<p><strong>数字（\(408\to8.67\) ビット）は動きません。動くのは言明の主語です。</strong> ── 第3回の作法そのもの：<em>比較相手（ここでは事前分布）を言わなければ、まだ文になっていない。</em> 番外編②はそこが甘かったので、消さずに印をつけて残します。</p>

<div class="caveat">
<span class="tag">正直な線 ── いちばん効く反論から</span>
<p style="margin:0 0 10px"><strong>① 物理的な質量比は、本当に RG 不変です。</strong> \(m_p/m_e\) は極質量の比なので走りません ── <em>これは正真正銘の無次元定数</em>です。だから「定数はゼロ」は言い過ぎで、08節のように「<strong>独立な入力のうち</strong>」と限定しなければなりません。\(m_p/m_e\) は<em>入力ではなく出力</em>（ラグランジアンから原理的には計算できる予言）だ、というのがこちらの応答ですが、<strong>これは弱い応答です</strong> ── 実際には計算できていないので、当面は入力と同じ扱いをせざるをえません。</p>
<p style="margin:0 0 10px"><strong>② 「走る」ということ自体、半分は規約です。</strong> \(\mu\) を選ぶのは人間で、RG 不変な組み合わせを取れば定数は作れます ── ただしそれは \(\Lambda_{\rm QCD}\) のように<em>次元付き</em>になりがちで、次元付きは帳簿（第3回）。この往復自体が、このシリーズの主題そのものです。</p>
<p style="margin:0 0 10px"><strong>③ \(\Lambda\)CDM の 6 個を「状態」と切るのは、強すぎるかもしれません。</strong> \(n_s\) は初期条件ですが、インフレーション模型の<em>予言</em>でもあります ── 「法則か状態か」の境界は分野の慣習に依り、鋭くは引けません。</p>
<p style="margin:0 0 10px"><strong>④ 05節の「単調」は 7 例の観察です。</strong> 「実際の扱われ方」は文献の空気の要約で、<em>私の偏りが入っています</em>（第36回②と同じ但し書き）。PMNS \(\theta_{23}\) は「小さい」のではなく「最大混合に近い」ことが問題視されており、<strong>同じ物差しで測れていません</strong>。</p>
<p style="margin:0"><strong>⑤ 04節の Haar 測度の議論は、標準的な数学です。</strong> ただし「だから微調整の議論が well-posed／ill-posed だ」という<em>読み方は本シリーズのもの</em>で、統計学や科学哲学ではもっと精緻な議論があります（不変事前分布、Jeffreys 事前など）── ここで言えるのは<strong>「コンパクトなら正規化できる、非コンパクトならできない」</strong>という一点だけです。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>無次元量とは何か、作業的に言うと。
<details><summary>答えを見る</summary><div class="ans"><strong>電波で送れる量</strong> ── 物を運ばずに伝えられるもの。「1 メートル」は送れませんが「\(\alpha=1/137.036\)」は送れます。<em>第47回で SI が \(c\) を法令で決めて \(\alpha\) を決められなかったのも、同じこと</em>です。</div></details></li>

<li>なぜ比には対数が自然で、角度には自然でないのか。
<details><summary>答えを見る</summary><div class="ans">比は<strong>乗法群 \(\mathbb{R}_+\)</strong> で、その Haar 測度が \(d(\ln x)\) だから ── <em>対数は発見ではなく、乗法群から加法群への同型</em>です。角度は<strong>コンパクト群</strong>で Haar 測度は \(d\theta\)（一様）── <em>log を取る意味がありません</em>。</div></details></li>

<li>第48回の「事前分布に理由があるか」は、何の言い換えだったか。
<details><summary>答えを見る</summary><div class="ans"><strong>コンパクトか否か</strong>です。コンパクト → Haar 測度が有限 → 正規化できる → 事前分布が一意に決まる → 微調整の議論が <strong>well-posed</strong>。非コンパクト → 正規化できない → <strong>ill-posed</strong>。<em>基準ではなく定理でした。</em></div></details></li>

<li>争いのない微調整問題が \(\theta_{\rm QCD}\) だけなのはなぜか。
<details><summary>答えを見る</summary><div class="ans"><strong>それが唯一のコンパクト類の問題だから</strong>です。\(v/M_P\) や \(\rho_\Lambda\) は非コンパクト類なので、ビット数そのものが事前分布次第で動きます ── <em>論争しているのではなく、問いが well-posed でないから決まらない</em>のです。</div></details></li>

<li>（やや難）「定数は一つも無いのでは」という見立ては、どこまで正しいか。
<details><summary>答えを見る</summary><div class="ans"><strong>かなりの精度で正しい</strong>です。32 個のうち約 24 は走る関数、6 個はこの宇宙の状態、本当に不変なもの（\(\nu\)、\(\eta\)、\(\omega\)）は<em>定数ではなく定理</em>。残る \(\theta_{\rm QCD}\) は、まさにアクシオンが動的にしようとしている当のもの ── <strong>PQ が正しければ一つも残りません</strong>。ただし正直な線①のとおり、\(m_p/m_e\) は本当に RG 不変なので「ゼロ」は言い過ぎで、<em>「独立な入力のうち」</em>と限定が要ります。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　0 の列は一様ではなく、定数はほとんど残らなかった</h2>
<p><strong>無次元量とは、電波で送れる量</strong>でした ── 物を運ばずに伝えられるもの。それが「物理」の中身です。</p>
<p>ところが「0 の列」は一様ではありませんでした。<strong>比／角度／個数／指数</strong>の四型があり、<em>群が違います</em>。比は乗法群 \(\mathbb{R}_+\)、角度はコンパクト群。そして <strong>対数は発見ではなく、乗法群から加法群への同型</strong> ── \(\mathbb{R}_+\) の Haar 測度が \(d(\ln x)\) だから対数一様が自然になるのであって、角度には log を取る意味がありません。<em>ビットは量の対数ではなく、確率の対数だったのです。</em></p>
<p>すると第48回の基準が<strong>定理</strong>になります ── コンパクトなら Haar 測度が有限で正規化でき、<em>事前分布が一意に決まる</em>（well-posed）。非コンパクトなら正規化できず、<em>決まらない</em>（ill-posed）。検証すると、コンパクト類の中では<strong>ビット数と深刻さが単調</strong>（PMNS \(\theta_{23}\) 0.88 → CKM \(\theta_{13}\) 8.81 → \(\theta_{\rm QCD}\) 35.87）で、<strong>争いのない微調整問題は唯一の角度である \(\theta_{\rm QCD}\) だけ</strong>。論争中のものはすべて非コンパクト類でした ── <em>論争しているのではなく、問いが well-posed でないのです。</em></p>
<p>そして「定数なのか」。32 個を分け直すと、約 24 は<strong>走る関数</strong>、6 個は<strong>この宇宙の状態</strong>、残るのは <strong>\(\theta_{\rm QCD}\) ただ一つ</strong>。本当に不変なもの（\(\nu\)、\(\eta\)、\(\omega\)、\(a\)、\(c\)）は <em>定数ではなく定理</em> ── \(\pi\) が円についての定理であるのと同じです。</p>
<p>そして最後に ── <strong>その \(\theta_{\rm QCD}\) こそ、アクシオンが場にして動かそうとしている当のもの。もしペッチェイ–クインが正しければ、定数は一つも残りません。</strong> <em>「定数がいくつもあるのはおかしい」という見立ては、かなりの精度で当たっていました。</em></p>
</div>

<div class="next">
<span class="lbl">おわりに ── 三つの番外編で分かったこと</span>
番外編①：<strong>質量の変化が普遍的かどうかなら測れる</strong>（\(\mu\)、23.3 ビット）。そしてクォーク質量方向に 10.2 ビットの縮退。<br>
番外編②：<strong>階層は自分の対数まで縮む</strong>（算術は正しい。ただし解釈は番外編③で訂正）。<br>
番外編③：<strong>0 の列は一様ではなく、第48回の基準は定理だった。そして定数はほとんど残らない。</strong><br>
── 三つとも、本編第3回の一つの手続きの上に立っています。そして三つめでその手続き自身が、<em>自分の作った基準を一つ削りました</em>。<strong>道具は、まだ働いています。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sd=document.getElementById('sd'), vd=document.getElementById('vd'), ro=document.getElementById('ro');
  var X0=64, X1=690, Y0=40, Y1=280, MID=372;

  // コンパクト側（角度）：事前は一意。ビットは固定。
  var COMP=[
    ['PMNS θ23',0.88],['PMNS θ12',1.43],['CKM θ12',2.79],
    ['PMNS θ13',3.39],['CKM θ23',5.24],['CKM θ13',8.81],['θ_QCD',35.87]
  ];
  // 非コンパクト側（比）：ビットは事前範囲に依存
  var NON=[['v/M_P',16.7],['ρ_Λ/ρ_P',123.0]];   // 桁数（log10 の小ささ）

  function py(b){ return Y1-Math.min(b,40)/40*(Y1-Y0); }

  function draw(){
    var dec=parseInt(sd.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.strokeStyle='#cdc8d2'; g.lineWidth=1.4;
    g.beginPath(); g.moveTo(MID,Y0-16); g.lineTo(MID,Y1+30); g.stroke();

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var b=0;b<=40;b+=10){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(b)); g.lineTo(X1,py(b)); g.stroke();
      g.fillText(b+' bit', X0-6, py(b)+4);
    }

    g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillStyle='#2a5a5a'; g.fillText('コンパクト類（角度）── 事前が一意に決まる', (X0+MID)/2, Y0-22);
    g.fillStyle='#8a4a2a'; g.fillText('非コンパクト類（比）── 事前が決まらない', (MID+X1)/2, Y0-22);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    var bw=(MID-X0-24)/COMP.length;
    for(var i=0;i<COMP.length;i++){
      var x=X0+12+i*bw, b2=COMP[i][1];
      g.fillStyle='#2a5a5a'; g.globalAlpha=0.9;
      g.fillRect(x, py(b2), bw-8, Y1-py(b2));
      g.globalAlpha=1;
      g.save(); g.translate(x+(bw-8)/2, Y1+8); g.rotate(Math.PI/2.6);
      g.fillStyle='#5a7a7a'; g.textAlign='left'; g.fillText(COMP[i][0],0,0); g.restore();
      if(b2>30){ g.fillStyle='#2a5a5a'; g.textAlign='center'; g.fillText(b2.toFixed(1), x+(bw-8)/2, py(b2)-8); }
    }

    // 非コンパクト：事前範囲 dec 桁のとき、対数一様なら -log2(1/dec)
    var bw2=(X1-MID-24)/NON.length;
    for(var j=0;j<NON.length;j++){
      var x2=MID+12+j*bw2;
      var bits=Math.log(dec)/Math.LN2;          // 対数一様の読み
      var bitsLin=NON[j][1]*Math.LN10/Math.LN2; // 線形の読み
      g.fillStyle='#8a4a2a'; g.globalAlpha=0.9;
      g.fillRect(x2, py(bits), bw2-8, Y1-py(bits));
      g.globalAlpha=1;
      g.strokeStyle='#8a4a2a'; g.lineWidth=1.6; g.setLineDash([4,3]);
      g.beginPath(); g.moveTo(x2, py(bitsLin)); g.lineTo(x2+bw2-8, py(bitsLin)); g.stroke();
      g.setLineDash([]);
      g.save(); g.translate(x2+(bw2-8)/2, Y1+8); g.rotate(Math.PI/2.6);
      g.fillStyle='#8a6a4a'; g.textAlign='left'; g.fillText(NON[j][0],0,0); g.restore();
      g.fillStyle='#8a4a2a'; g.textAlign='center';
      g.fillText(bits.toFixed(1), x2+(bw2-8)/2, py(bits)-8);
    }
    g.fillStyle='#a08a6a'; g.textAlign='left';
    g.fillText('破線＝線形な事前で読んだ場合（枠外）', MID+14, Y0+10);

    vd.textContent=dec+' 桁';
    ro.textContent='非コンパクト側の事前範囲 '+dec+' 桁　→　対数一様なら '+
      (Math.log(dec)/Math.LN2).toFixed(2)+' ビット、線形なら 55〜408 ビット'+
      '　★ 左（角度）はツマミを動かしても 1 ビットも動かない ── そこだけが well-posed';
  }
  sd.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-b3-dimensionless.html', acc='#2a5a5a', ops='#8a4a2a',
      title='番外編③：無次元量とは何か、そして定数はあるのか ── わかる c·t=一定',
      ep='番外編 ③ ／ 本編完結後の深掘り',
      eyebrow='0 の列は一様ではなく、定数はほとんど残らなかった',
      h1='定数は、<br>一つも無いのかもしれない',
      sub='無次元量とは電波で送れる量でした。ただしその中身は四種類あり、群が違います。<br><em>そして「定数」と呼んできたものの大半は、走る関数でした。</em>',
      byline_l='必要な道具：第3回の判定、第14・44回の臨界指数、第37回の走り、第47回の地図、第48回の事前分布',
      byline_r='残るのは \\(\\theta_{\\rm QCD}\\) ただ一つ ── そしてアクシオンがそれを消す',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズの番外編③（本編全50話の完結後に書いた深掘り）、物理好きの高校生・大学生向け読み物です。数値は kenshou/calc58.py と calc59.py で計算しています。Haar 測度、くりこみ群による結合定数の走り、臨界指数の普遍性、ペッチェイ–クイン機構はいずれも標準的な内容です。<strong>いちばん効く反論は正直な線①</strong>：\\(m_p/m_e\\) は極質量の比なので本当に RG 不変で、<em>正真正銘の無次元定数</em>です ── だから「定数はゼロ」は言い過ぎで、「<strong>独立な入力のうち</strong>」という限定が要ります（「出力だから」という応答は、実際には計算できていない以上、弱い応答です）。<strong>「走る」ということ自体、半分は規約</strong>で、RG 不変な組み合わせを取れば定数は作れますが、それは \\(\\Lambda_{\\rm QCD}\\) のように次元付きになりがちです。<strong>\\(\\Lambda\\)CDM の 6 個を「状態」と切るのは強すぎるかもしれません</strong> ── \\(n_s\\) は初期条件であると同時にインフレーション模型の予言でもあり、境界は鋭く引けません。<strong>05節の「単調」は 7 例の観察</strong>で、「実際の扱われ方」は文献の空気の要約であり私の偏りが入っています（PMNS \\(\\theta_{23}\\) は「小さい」のではなく「最大混合に近い」ことが問題視されており、同じ物差しでは測れていません）。<strong>04節の Haar 測度の議論は標準的な数学ですが、「だから微調整が well-posed／ill-posed だ」という読み方は本シリーズのもの</strong>で、統計学には不変事前分布や Jeffreys 事前など、より精緻な議論があります。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで事前範囲を動かすと、左（角度）だけが動かないことが見えます。「答えを見る」で解答が開きます。')
