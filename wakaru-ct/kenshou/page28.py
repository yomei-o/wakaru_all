# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第 IV 部の二人目は <strong>VSL（光速可変理論）</strong>です。このシリーズといちばん近い場所にいる理論で、<em>だからこそ手術がよく効きます</em>。「光速が昔は速かった」の中にも、やはり二つの別物が入っています ── <strong>単位の取り替え</strong>と、<strong>無次元量が動くという主張</strong>。切り分けると、VSL がどこで<em>手術に失敗したのか</em>がはっきりします。答えを先に言うと ── <strong>失敗は「c を動かしたこと」ではなく、「c と呼び続けたこと」でした。</strong></p>

<h2><span class="n">01</span>そもそも \(c\) は、四つある</h2>

<p>手術の前に、切る対象を確認します。「光速」と呼ばれている \(c\) は、じつは<strong>別々の場所に別々の役割で四回出てきます</strong>。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>どこの \(c\) か</th><th class="mid">何をしている</th></tr></thead>
<tbody>
<tr><th>マクスウェル方程式の \(c\)</th><td class="mid">電磁波の伝播速度</td></tr>
<tr><th>ローレンツ変換の \(c\)</th><td class="mid">因果構造 ── 光円錐の傾き</td></tr>
<tr><th>\(E=mc^2\) の \(c\)</th><td class="mid">質量とエネルギーの換算係数</td></tr>
<tr><th>アインシュタイン方程式の \(c\)</th><td class="mid">曲率と物質の結合 \(8\pi G/c^4\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0">この四つは、原理的には<strong>別々に動かせる量</strong>です。<br>
だから「\(c\) が変わる」は、<em>どれが変わるのかを言っていません</em> ── エリス＝ユザン（2005）の指摘。<br>
<strong>手術の対象は、二つではなく四つ以上ありました。</strong></p>
</div>

<h2><span class="n">02</span>VSL が実際に主張しているのは、\(\alpha\) の変化</h2>

<p>VSL（アルブレヒト＝マゲイジョ 1999 ほか）は、この選択をはっきり行います ── <strong>\(e\) と \(\hbar\) を固定して、\(c\) を動かす</strong>。すると微細構造定数がついてきます。</p>

<div class="calc">
<span class="tag">連動する無次元量</span>
$$\alpha=\frac{e^2}{4\pi\varepsilon_0\hbar c}\qquad\Longrightarrow\qquad \frac{\Delta\alpha}{\alpha}=-\frac{\Delta c}{c}$$
</div>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0"><strong>「光速が変わる」の、観測にかかる中身はまるごと「\(\alpha\) が変わる」です。</strong><br>
── 前シリーズ番外編③で「VSL は原子時計に衝突する」と書いたのは、この一行のことでした。</p>
</div>

<h2><span class="n">03</span>\(\alpha\) は、どれだけ縛られているか</h2>

<p>第19回の作法で、ビットに直して並べます ── <em>上限が \(10^{-n}\) なら、\(\log_2(10^n)\) ビットぶん押さえられている</em>。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>測定</th><th class="mid">時代</th><th class="mid">\(|\Delta\alpha/\alpha|\) 上限</th><th class="mid">縛られたビット</th></tr></thead>
<tbody>
<tr class="hi"><th>実験室（CODATA 2022）</th><td class="mid">今日</td><td class="mid">\(1.6\times10^{-10}\)</td><td class="mid"><strong>32.5 bit</strong></td></tr>
<tr><th>原子時計（13.8 Gyr 外挿）</th><td class="mid">\(z\simeq0\)</td><td class="mid">\(1.4\times10^{-8}\)</td><td class="mid">26.1 bit</td></tr>
<tr class="hi"><th>オクロ天然原子炉</th><td class="mid">18 億年前</td><td class="mid">\(1.1\times10^{-8}\)</td><td class="mid"><strong>26.4 bit</strong></td></tr>
<tr><th>クエーサー吸収線</th><td class="mid">\(z\sim2\)</td><td class="mid">\(1.0\times10^{-5}\)</td><td class="mid">16.6 bit</td></tr>
<tr><th>CMB</th><td class="mid">\(z=1100\)</td><td class="mid">\(4.0\times10^{-3}\)</td><td class="mid">8.0 bit</td></tr>
<tr><th>元素合成</th><td class="mid">\(z=4\times10^{8}\)</td><td class="mid">\(1.0\times10^{-2}\)</td><td class="mid">6.6 bit</td></tr>
</tbody>
</table>
</div>

<p>直近の宇宙では <strong>26 ビット</strong>、元素合成の時代でも <strong>6.6 ビット</strong>が押さえられています。第19回の目盛りで言えば、<em>小出の関係式（15.7 ビット）を超える精度で「動いていない」ことが分かっている</em>量です。</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>核心 ── 地平線問題を解くには、\(c\) がどれだけ変わればよいか</h2>

<p>VSL の売りは、インフレーションなしで地平線問題を解くことです。ではどれだけの変化が要るのか。第27回で使った粒子的地平線を、\(c\) が変わる場合に書き直します。</p>

<div class="calc">
<span class="tag">計算 ── 二行</span>
<p class="lbl">\(c=c_0(a/a_0)^n\) として、輻射期（\(a\propto t^{1/2}\)、\(dt\propto a\,da\)）で積むと</p>
$$\chi=\int\frac{c\,dt}{a}\ \propto\ \int a^{n}\,da=\frac{a^{n+1}}{n+1}$$
<p class="lbl">\(a\to0\) で発散する条件は</p>
$$\boxed{\ n<-1\ }\qquad(\text{標準の }n=0\text{ では }\chi\propto a\text{ で発散しない})$$
</div>

<p>つまり VSL は、<strong>過去にさかのぼると \(c\) が少なくとも \(1/a\) の速さで増える</strong>ことを要求します。すると \(\alpha\propto1/c\propto a^{-n}\) なので ──</p>

<div class="calc">
<span class="tag">要求される \(\alpha\) の変化</span>
$$\frac{\alpha(z)}{\alpha_0}\ \ge\ 1+z$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>時代</th><th class="mid">\(1+z\)</th><th class="mid">要求される \(\Delta\alpha/\alpha\)</th><th class="mid">観測上限の何倍か</th></tr></thead>
<tbody>
<tr><th>オクロ（18 億年前）</th><td class="mid">1.14</td><td class="mid">0.14</td><td class="mid">\(1.3\times10^{7}\) 倍</td></tr>
<tr><th>クエーサー（\(z\sim2\)）</th><td class="mid">3.0</td><td class="mid">2.0</td><td class="mid">\(2.0\times10^{5}\) 倍</td></tr>
<tr><th>CMB（\(z=1100\)）</th><td class="mid">1101</td><td class="mid">1100</td><td class="mid">\(2.8\times10^{5}\) 倍</td></tr>
<tr class="hi"><th>元素合成（\(z=4\times10^8\)）</th><td class="mid">\(4\times10^{8}\)</td><td class="mid">\(4\times10^{8}\)</td><td class="mid"><strong>\(4\times10^{10}\) 倍</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>滑らかな冪の VSL で地平線問題を解くことは、観測が排除します。</strong><br>
元素合成のところで、要求 \(4\times10^8\) に対して上限 \(10^{-2}\) ── <em>10 桁の超過</em>。<br>
しかも 18 億年前のオクロですら、すでに 7 桁足りません。</p>
</div>

<h2><span class="n">05</span>生き残る VSL ── そして、生き残り方の代償</h2>

<p>ところが VSL は死んでいません。アルブレヒト＝マゲイジョの提案は<em>冪ではなく相転移</em>だからです ── <strong>ある時刻に \(c\) が一気に落ち、以後は一定</strong>。</p>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>相転移を元素合成より前に置けば、03節の上限には一切かからない</strong><span>\(z>4\times10^8\) には \(\alpha\) のデータが無いから</span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>地平線問題は解ける</strong><span>相転移より前で \(c\) が十分大きければよい（プランク期に置くなら \(10^{32}\) 倍）</span></div></div>
<div class="row hi"><div class="mk">✗</div><div class="txt"><strong>代償：観測できる時代に、予言がゼロになる</strong><span>元素合成以降は \(\alpha\) が完全に一定 ── <em>標準宇宙論と区別がつかない</em></span></div></div>
</div>

<div class="fig">
<p class="cap">図：横軸は赤方偏移、縦軸は \(|\Delta\alpha/\alpha|\)。<strong>灰色の点が観測上限で、その上は排除された領域</strong>。ツマミで相転移の時刻を動かすと、<em>データを逃れた瞬間に、観測できる時代の予言もゼロになります</em></p>
<canvas id="cv" width="720" height="390"></canvas>
<div class="controls">
  <label>相転移をいつに置くか \(\log_{10}(1+z_t)\)<input id="sz" type="range" min="0" max="320" value="30" step="1"></label>
  <span class="val" id="vz">1+z = 1000</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3f2a4a"></i>相転移型 VSL の \(\Delta\alpha/\alpha\)</span>
  <span><i class="swatch" style="background:#7a8a2a"></i>冪型 VSL（\(n=-1\)）</span>
  <span><i class="swatch" style="background:#9a9098"></i>観測上限（この上は排除）</span>
</div>
</div>

<p>ツマミを右へ動かして相転移を早めていくと、紫の線が灰色の点をくぐり抜けます。ところが<strong>くぐり抜けた瞬間、観測できる全時代で線が床（\(\Delta\alpha/\alpha=0\)）に貼りつきます</strong>。<em>排除を逃れることと、予言を失うことが、同じ操作でした。</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">06</span>種明かし ── 三つの運命</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">\(\alpha\) は動くか</th><th class="mid">観測との衝突</th><th class="mid">予言</th></tr></thead>
<tbody>
<tr><th>冪型 VSL</th><td class="mid">動く（\(O(1)\)）</td><td class="mid">元素合成で 10 桁超過</td><td class="mid"><strong>反証済み</strong></td></tr>
<tr><th>相転移型 VSL</th><td class="mid">元素合成より前だけ</td><td class="mid">なし</td><td class="mid">観測可能な時代にゼロ</td></tr>
<tr class="hi"><th>c·t=一定（共形変換）</th><td class="mid"><strong>厳密に不変</strong></td><td class="mid">なし</td><td class="mid">記法。それ自体はゼロ</td></tr>
</tbody>
</table>
</div>

<p>同じ「光速が変わる」という言葉が、<strong>何を固定するかで三つに割れます</strong>。第9回の練習問題5で「VSL は原子時計に殺されて、この絵は殺されない」と書いたのは、この表の一行目と三行目のことでした。今回は真ん中の行が加わっています。</p>

<div class="keybox">
<p class="lbl">06節の結論 ── 手術の結果</p>
<p style="margin:6px 0 0">「光速が変わる」の中身は、第3回とまったく同じ二つでした ──<br>
<strong>(A) 単位の取り替え</strong>（何も言わない）と <strong>(B) 無次元量が動くという主張</strong>（観測にかかる）。<br>
VSL は (B) を選んだのに、<em>名前は (A) のまま残しました</em>。<br>
── <strong>正しい名前は「\(\alpha\) 可変理論」です。</strong></p>
</div>

<div class="aside">
<span class="tag">どこで手術に失敗したのか</span>
VSL は<strong>手術を半分だけやりました</strong>。「\(c\) だけでは足りない」ことは正しく認識して \(e\) と \(\hbar\) を固定した ── そこまでは第3回と同じです。ところが<em>名前を変えなかった</em>。その結果、「光速が変わる」という言い方が中身（\(\alpha\) が変わる）を隠し、\(\alpha\) の測定という<strong>26 ビットの制約</strong>が正面から見えなくなりました。<em>手術の失敗は「\(c\) を動かしたこと」ではなく、「\(c\) と呼び続けたこと」です。</em>
</div>

<h2><span class="n">07</span>混同しないこと ── \(\alpha\) の「走り」</h2>

<div class="calc">
<span class="tag">これは時間変化ではない</span>
$$\alpha^{-1}(0)=137.036\ \longrightarrow\ \alpha^{-1}(M_Z)=127.951\qquad(6.6\%\ \text{の差})$$
</div>

<p>第11回・第14回で見た繰り込み群による走りです。これは<strong>エネルギースケール依存</strong>であって、<em>時間変化ではありません</em>。03節の上限はすべて「同じエネルギースケールで測った \(\alpha\) が、時代とともに動いていないか」を見ています ── <strong>軸が違う</strong>ので、混同すると 6.6% と \(10^{-8}\) を比べることになります。第21回で a定理を「別の軸」に置いたのと、同じ整理です。</p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 「\(c\) が四つある」はエリス＝ユザン（2005）の整理です。</strong> どの \(c\) を動かすかによって理論の中身は変わり、本稿はそのうち「\(\alpha\) が動く選択」だけを追っています。ローレンツ変換の \(c\) を動かす（＝因果構造そのものを変える）タイプの VSL は、また別の議論が要ります。</p>
<p style="margin:0 0 10px"><strong>② 03節の上限は、代表的な値をまとめたものです。</strong> クエーサー吸収線については Webb らが \(\Delta\alpha/\alpha\simeq-0.6\times10^{-5}\) の<em>有意な変化</em>を主張した経緯があり、Keck と VLT で符号が食い違うなど<strong>論争が続いています</strong>。本稿の \(10^{-5}\) は保守的にまとめた上限で、単一の測定値ではありません。CMB と元素合成の上限も、他のパラメータとの縮退の扱いで数倍動きます。</p>
<p style="margin:0 0 10px"><strong>③ 04節の \(n<-1\) は、輻射優勢で \(c\) が \(a\) の冪に従う場合の条件です。</strong> \(c\) が変わると \(H\) の式も変わるので、正確には修正フリードマン方程式を解く必要があります ── 本稿は<em>桁の議論</em>として、地平線が発散するかどうかだけを見ています。</p>
<p style="margin:0 0 10px"><strong>④ 「相転移型は観測可能な時代に予言がゼロ」は、\(\alpha\) についての話です。</strong> VSL には他の予言（ゆらぎのスペクトル、平坦性問題の解き方など）を持たせる定式化もあり、それらは別に検証されます ── <em>本稿が言っているのは「\(\alpha\) の測定では区別できない」という一点</em>です。</p>
<p style="margin:0"><strong>⑤ この回は VSL を否定していません。</strong> 冪型が排除されることと、相転移型が \(\alpha\) の測定にかからないことを数えただけです。<em>手術の目的は、名前の中に隠れた比較相手を名指しすること</em>でした。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>「光速が変わる」が、それだけでは主張になっていないのはなぜか。
<details><summary>答えを見る</summary><div class="ans">\(c\) は次元付き＝帳簿だから ── <strong>何を固定するかを言わないと意味が出ません</strong>。しかも \(c\) は四か所（マクスウェル、ローレンツ変換、\(E=mc^2\)、アインシュタイン方程式）に別々に出てくるので、<em>どの \(c\) かも言う必要があります</em>。</div></details></li>

<li>VSL が実際に主張しているのは何か。
<details><summary>答えを見る</summary><div class="ans">\(e\) と \(\hbar\) を固定して \(c\) を動かすので、\(\alpha=e^2/4\pi\varepsilon_0\hbar c\) が \(\Delta\alpha/\alpha=-\Delta c/c\) で動きます。<strong>観測にかかる中身はまるごと「\(\alpha\) が変わる」</strong>。正しい名前は「\(\alpha\) 可変理論」です。</div></details></li>

<li>地平線問題を解くために必要な \(c\) の変化を求めよ。
<details><summary>答えを見る</summary><div class="ans">\(c=c_0(a/a_0)^n\) として \(\chi=\int c\,dt/a\propto\int a^n da=a^{n+1}/(n+1)\)。\(a\to0\) で発散する条件は <strong>\(n<-1\)</strong>。したがって \(\alpha\propto a^{-n}\) より \(\alpha(z)/\alpha_0\ge1+z\)。</div></details></li>

<li>元素合成の時代で、要求と観測上限を比べよ。
<details><summary>答えを見る</summary><div class="ans">\(z=4\times10^8\) なので要求は \(\Delta\alpha/\alpha\ge4\times10^8\)、観測上限は \(10^{-2}\)。比は <strong>\(4\times10^{10}\) 倍</strong> ── 10 桁の超過で、<em>滑らかな冪の VSL は排除されます</em>。オクロ（18 億年前）ですら 7 桁足りません。</div></details></li>

<li>（やや難）相転移型 VSL は、なぜ排除されないのか。その代償は。
<details><summary>答えを見る</summary><div class="ans">\(c\) の変化を元素合成より前（\(z>4\times10^8\)）に閉じ込めれば、<strong>\(\alpha\) のデータが存在しない領域</strong>なので上限にかかりません。代償は<em>観測できる時代に \(\alpha\) の予言がゼロになる</em>こと ── 標準宇宙論と区別がつきません。<strong>排除を逃れることと予言を失うことが、同じ操作</strong>です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　失敗は、\(c\) を動かしたことではなかった</h2>
<p>まず切る対象を確認しました ── 「光速」と呼ばれる \(c\) は、マクスウェル方程式・ローレンツ変換・\(E=mc^2\)・アインシュタイン方程式に<strong>別々の役割で四回</strong>出てきます。だから「\(c\) が変わる」は、どれが変わるかを言っていない（エリス＝ユザン 2005）。</p>
<p>VSL はこの選択をはっきり行います ── \(e\) と \(\hbar\) を固定して \(c\) を動かす。すると \(\Delta\alpha/\alpha=-\Delta c/c\) で、<strong>観測にかかる中身はまるごと「\(\alpha\) が変わる」</strong>になります。そして \(\alpha\) は、実験室で 32.5 ビット、18 億年前のオクロで 26.4 ビット、元素合成でも 6.6 ビット押さえられている ── <em>第19回の目盛りでいえば、小出の関係式より高い精度で「動いていない」と分かっている量</em>です。</p>
<p>核心は 04節でした。地平線問題を解くには、粒子的地平線 \(\chi\propto a^{n+1}/(n+1)\) が発散する必要があり、条件は \(n<-1\)。すると \(\alpha(z)/\alpha_0\ge1+z\) が要求されます。元素合成のところで<strong>要求 \(4\times10^8\)、上限 \(10^{-2}\) ── 10 桁の超過</strong>。<em>滑らかな冪の VSL で地平線問題を解くことは、観測が排除します。</em></p>
<p>ただし VSL は死んでいません。相転移型なら \(c\) の変化を元素合成より前に閉じ込められるからです ── <strong>ところが、排除を逃れることと予言を失うことが同じ操作でした</strong>。観測できる時代には \(\alpha\) が完全に一定で、標準宇宙論と区別がつかない。</p>
<p>そして手術の結果。「光速が変わる」の中身は第3回とまったく同じ二つ ── <strong>(A) 単位の取り替え</strong>（何も言わない）と <strong>(B) 無次元量が動くという主張</strong>（観測にかかる）。<em>VSL は (B) を選んだのに、名前は (A) のまま残しました。</em> 正しい名前は「\(\alpha\) 可変理論」です。<strong>手術の失敗は「\(c\) を動かしたこと」ではなく、「\(c\) と呼び続けたこと」でした。</strong></p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第29回</span>
次の患者は <strong>MOND</strong> です。「加速度が \(a_0=1.2\times10^{-10}\ \mathrm{m/s^2}\) より小さいところでニュートン則が変わる」── この \(a_0\) は<em>次元付き</em>です。だから第3回の手術がそのまま当たります ── <strong>何と比べて小さいのか</strong>。ところが面白いことに、\(a_0\) を無次元にする相手を探すと、<em>\(cH_0\) がすぐ隣にいます</em>（\(a_0/cH_0=0.18\)）。これは恒等式か、偶然か、物理か ── 第19回の手続きで仕分けます。<strong>そして「暗黒物質か MOND か」という問いが、じつは「どちらが記述長を減らすか」という第5回の天秤で測れることを見ます。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sz=document.getElementById('sz'), vz=document.getElementById('vz'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=34, Y1=316;
  var xmin=0, xmax=33;        // log10(1+z)
  var ymin=-12, ymax=34;      // log10|Δα/α|
  // 観測上限（log10(1+z), log10 bound）
  var BND=[[Math.log(1.14)/Math.LN10,-7.96,'オクロ'],
           [Math.log(3.0)/Math.LN10,-5.0,'クエーサー'],
           [Math.log(1101)/Math.LN10,-2.40,'CMB'],
           [Math.log(4.0e8)/Math.LN10,-2.0,'元素合成']];
  var LBBN=Math.log(4.0e8)/Math.LN10;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function draw(){
    var lzt=parseInt(sz.value,10)/10;      // log10(1+z_t)
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    // データが存在しない領域
    g.fillStyle='#f6f4f7';
    g.fillRect(px(LBBN), Y0, X1-px(LBBN), Y1-Y0);
    g.fillStyle='#a49aa8'; g.textAlign='center';
    g.fillText('α のデータが存在しない', (px(LBBN)+X1)/2, Y0+16);

    g.textAlign='right';
    for(var e=-10;e<=30;e+=10){
      var y=py(e);
      g.strokeStyle=(e===0?'#ddd2e0':'#f4f0f6'); g.lineWidth=(e===0?1.5:1);
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a1959f'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=30;q+=5){
      var x=px(q);
      g.strokeStyle='#faf7fb'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a1959f'; g.fillText(q===0?'いま':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#d6c8dc'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // 排除領域（観測上限の上）
    g.fillStyle='rgba(154,144,152,0.16)';
    g.beginPath();
    g.moveTo(px(BND[0][0]),py(BND[0][1]));
    for(var i=1;i<BND.length;i++) g.lineTo(px(BND[i][0]),py(BND[i][1]));
    g.lineTo(px(LBBN),Y0); g.lineTo(px(BND[0][0]),Y0);
    g.closePath(); g.fill();

    // 上限の点と折れ線
    g.strokeStyle='#9a9098'; g.lineWidth=2; g.setLineDash([5,4]);
    g.beginPath();
    for(var i=0;i<BND.length;i++){
      if(i===0) g.moveTo(px(BND[i][0]),py(BND[i][1])); else g.lineTo(px(BND[i][0]),py(BND[i][1]));
    }
    g.stroke(); g.setLineDash([]);
    for(var i=0;i<BND.length;i++){
      g.fillStyle='#6f6670';
      g.beginPath(); g.arc(px(BND[i][0]),py(BND[i][1]),4.5,0,6.2832); g.fill();
      g.fillStyle='#7d7480'; g.textAlign='left';
      g.fillText(BND[i][2], px(BND[i][0])+8, py(BND[i][1])-8);
    }

    // 冪型 VSL（n=-1）: Δα/α = z ≈ 10^x
    g.strokeStyle='#7a8a2a'; g.lineWidth=2.6; g.setLineDash([7,4]);
    g.beginPath();
    g.moveTo(px(0.02),py(-1.7));
    g.lineTo(px(xmax),py(xmax));
    g.stroke(); g.setLineDash([]);
    g.fillStyle='#5f6b1e'; g.textAlign='right';
    g.fillText('冪型 VSL（n=−1）', px(28), py(28)+16);

    // 相転移型
    g.strokeStyle='#3f2a4a'; g.lineWidth=3.4;
    g.beginPath();
    g.moveTo(px(0), py(ymin+0.6));
    g.lineTo(px(lzt), py(ymin+0.6));
    g.lineTo(px(lzt), py(Math.max(lzt,0)));
    g.lineTo(px(xmax), py(xmax));
    g.stroke();
    g.fillStyle='#3f2a4a';
    g.beginPath(); g.arc(px(lzt),py(Math.max(lzt,0)),5.5,0,6.2832); g.fill();
    g.strokeStyle='#fff'; g.lineWidth=1.8;
    g.beginPath(); g.arc(px(lzt),py(Math.max(lzt,0)),5.5,0,6.2832); g.stroke();

    g.fillStyle='#8a7f90'; g.textAlign='center';
    g.fillText('赤方偏移  1 + z', (X0+X1)/2, Y1+36);
    g.save(); g.translate(19,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('|Δα/α|', 0,0); g.restore();

    // 判定：相転移が BBN より後なら、そこでの上限と比べる
    var zt=Math.pow(10,lzt)-1;
    var viol=false, worst=0, name='';
    for(var i=0;i<BND.length;i++){
      if(lzt<=BND[i][0]){                       // その測定より前に相転移 → その時代に変化あり
        var req=Math.pow(10,BND[i][0])-1;
        var lim=Math.pow(10,BND[i][1]);
        if(req/lim>worst){ worst=req/lim; name=BND[i][2]; }
        viol=true;
      }
    }
    vz.textContent='1+z = '+(Math.pow(10,lzt)<1e4?Math.pow(10,lzt).toPrecision(3):Math.pow(10,lzt).toExponential(1));
    ro.textContent='相転移を 1+z = '+vz.textContent+' に置く　→　'+
      (viol
        ? '★ '+name+' の時代に Δα/α が上限を '+worst.toExponential(1)+' 倍 超える ── 排除'
        : '排除されない（α のデータが存在しない領域に隠れた）'+
          '　／　同時に、観測できる全時代で Δα/α = 0 ── 予言もゼロ');
  }
  sz.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-28-vsl.html', acc='#3f2a4a', ops='#7a8a2a',
      title='VSL ── どこで手術に失敗したのか ── わかる c·t=一定 第28回',
      ep='第 28 回 ／ 第 IV 部・いちばん近い場所にいる理論',
      eyebrow='失敗は「c を動かしたこと」ではなく、「c と呼び続けたこと」でした',
      h1='VSL ── どこで<br>手術に失敗したのか',
      sub='「光速が昔は速かった」の中にも、二つの別物が入っています。<br><em>切り分けると、観測にかかる中身はまるごと「\\(\\alpha\\) が変わる」でした。</em>',
      byline_l='必要な道具：粒子的地平線、対数、第19回の作法',
      byline_r='\\(\\Delta\\alpha/\\alpha=-\\Delta c/c\\)',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第28回、物理好きの高校生・大学生向け読み物です。\\(c\\) が理論の複数の場所に別々の役割で現れ「どの \\(c\\) が変わるのか」を指定しないと VSL が定義されないことは Ellis &amp; Uzan (2005, Am. J. Phys. 73, 240) の指摘です。VSL は Albrecht &amp; Magueijo (1999, PRD 59, 043516)、Barrow (1999) ほかによります。\\(\\alpha=e^2/4\\pi\\varepsilon_0\\hbar c\\) および \\(e,\\hbar\\) 固定のもとでの \\(\\Delta\\alpha/\\alpha=-\\Delta c/c\\) は定義から従います。03節の上限は代表的な値をまとめたもので、CODATA 2022 の \\(\\alpha^{-1}=137.035999177(21)\\)、原子時計は Lange et al. (2021, PRL 126, 011102) の \\(|\\dot\\alpha/\\alpha|<1.0(1.1)\\times10^{-18}\\)/yr、オクロ天然原子炉、クエーサー吸収線、CMB、元素合成による制約に基づきます ── <strong>クエーサー吸収線については Webb らが有意な変化を主張した経緯があり、Keck と VLT で結果が食い違うなど論争が続いています</strong>。本稿の \\(10^{-5}\\) は保守的にまとめた上限で単一の測定値ではなく、CMB と元素合成の上限も他パラメータとの縮退の扱いで数倍動きます。04節の \\(\\chi\\propto a^{n+1}/(n+1)\\) と条件 \\(n<-1\\)、および \\(\\alpha(z)/\\alpha_0\\ge1+z\\)、各時代での超過倍率（元素合成で \\(4\\times10^{10}\\) 倍）は本稿での計算です（kenshou/calc32.py）── <em>\\(c\\) が変わると \\(H\\) の式も変わるため、正確には修正フリードマン方程式を解く必要があり、本稿は地平線が発散するかどうかだけを見た桁の議論です</em>。「相転移型は観測可能な時代に予言がゼロ」は \\(\\alpha\\) についての言明で、VSL には他の予言を持たせる定式化もあります。\\(\\alpha^{-1}\\) が 137.036 から \\(M_Z\\) で 127.951 へ走ることはエネルギースケール依存であって時間変化ではありません（第11回・第14回）。<strong>本稿は VSL を否定するものではなく</strong>、冪型が排除されることと相転移型が \\(\\alpha\\) の測定にかからないことを数え、名前の中に隠れた比較相手を名指ししたものです。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルです。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで相転移の時刻を動かし、排除を逃れる瞬間に予言も消える様子が見えます。「答えを見る」で解答が開きます。')
