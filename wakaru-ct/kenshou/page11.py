# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">ここまで「光は共形変換を素通りする」と何度も書いてきましたが、正面から扱ったことはありませんでした。今回やります。この絵で光子ガスを見ると ── <strong>数密度も、エネルギー密度も、温度も、波長も、全部が一定</strong>。<em>完全に静止しています。</em> 宇宙の歴史を通じて、光には何も起きていない。育っているのは物質のほうだけ。前シリーズ第7回の「4 次元のマクスウェル作用だけがぴったり共形不変」が、いちばん露骨な形で見えます。</p>

<h2><span class="n">01</span>光子ガスを、片っ端から変換する</h2>

<p>ウェイト表に従って、CMB の量を順に変換します。標準の絵での時間変化と、掛け合わせるだけです。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">ウェイト</th><th class="mid">標準の絵</th><th class="mid">この絵</th></tr></thead>
<tbody>
<tr class="hi"><th>光子数密度 \(n_\gamma\)</th><td class="mid">\(+3\)</td><td class="mid">\(\propto a^{-3}\)</td><td class="mid"><strong>一定</strong></td></tr>
<tr class="hi"><th>エネルギー密度 \(\rho_\gamma\)</th><td class="mid">\(-4\)</td><td class="mid">\(\propto a^{-4}\)</td><td class="mid"><strong>一定</strong></td></tr>
<tr class="hi"><th>温度 \(T\)</th><td class="mid">\(-1\)</td><td class="mid">\(\propto a^{-1}\)</td><td class="mid"><strong>一定</strong></td></tr>
<tr class="hi"><th>光子 1 個のエネルギー \(\hbar\omega\)</th><td class="mid">\(-1\)</td><td class="mid">\(\propto a^{-1}\)</td><td class="mid"><strong>一定</strong></td></tr>
<tr class="hi"><th>波長 \(\lambda\)</th><td class="mid">\(+1\)</td><td class="mid">\(\propto a\)</td><td class="mid"><strong>一定</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>光について、動くものが一つもありません。</strong><br>
今日の光子数密度 \(4.11\times10^{8}\ \mathrm{m^{-3}}\) が、宇宙の全歴史を通じて同じ値。<br>
<em>この絵の光子ガスは、完全に静止しています。</em></p>
</div>

<p>偶然ではありません。標準の絵で光子の量が \(a\) の何乗で変わるかと、その量のウェイトが、<strong>ぴったり同じ数</strong>だからです。だから掛けると必ず消える。<em>光は、共形変換に対して過不足なくできている。</em></p>

<h2><span class="n">02</span>それでも、観測は一つも変わらない</h2>

<p>「光の量が全部一定」と聞くと、何かが壊れそうに思えます。壊れません ── <strong>CMB を決めている無次元数は、二つしかない</strong>からです。</p>

<div class="calc">
<span class="tag">CMB を決める二つの数</span>
<p class="lbl">① 光子 1 個あたりのエントロピー</p>
$$\frac{s_\gamma}{n_\gamma}=\frac{1.478\times10^{9}}{4.111\times10^{8}}=3.60\ k_B\qquad(\text{黒体の理論値 }3.602)$$
<p class="lbl">② バリオン光子比</p>
$$\eta=\frac{n_b}{n_\gamma}=6.1\times10^{-10}$$
</div>

<p>どちらも無次元なので、この絵でも標準の絵でもまったく同じ値です。そして黒体スペクトルの形も、\(\hbar\omega/k_BT\) という無次元の組み合わせだけで決まるので、<strong>不変</strong>。<em>プランク分布の形は一文字も変わりません。</em></p>

<div class="aside">
<span class="tag">元素合成が \(\eta\) だけで決まる、の意味</span>
ビッグバン元素合成の予言は、突き詰めると \(\eta\) ただ一つの関数です。\(\eta\) は無次元なので、この絵でも動きません ── だから<strong>ヘリウム量の予言も、絵の取り替えでは 1 ミリも動かない</strong>。前シリーズ番外編①が「三つの絵のどれで弁護しても判決は同じ」と書いたのは、突き詰めればこの一行でした。<em>絵が変わっても \(\eta\) は変わらないので、判決も変わらない。</em>
</div>

<h2><span class="n">03</span>赤方偏移が、まるごと裏返る</h2>

<p>光が何も変わらないなら、赤方偏移はどこから来るのか。<strong>受け取る側です。</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th>標準の絵</th><th>この絵</th></tr></thead>
<tbody>
<tr><th>飛んでいる光</th><td>空間が伸びるので、波長も伸びる</td><td><strong>何も起きない</strong></td></tr>
<tr><th>実験室の水素原子</th><td>ずっと同じ</td><td><strong>重くなっていく</strong>（\(\tilde m=am\)）</td></tr>
<tr><th>基準のライマン α</th><td>ずっと同じ波長</td><td>時代とともに短くなる</td></tr>
<tr class="hi"><th>分光器の読み \(1+z\)</th><td class="mid">\(\lambda_{\rm obs}/\lambda_{\rm lab}\)</td><td class="mid">同じ値</td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">同じ数字を、二通りに読む</span>
<p class="lbl">\(z=7\) の銀河のライマン α</p>
$$\text{標準：}\ \text{波長が }8\ \text{倍に伸びた}\qquad\text{この絵：}\ \text{実験室の基準が }8\ \text{倍細かくなった}$$
<p class="lbl">\(z=1100\) の CMB</p>
$$1101\ \text{倍}\qquad\text{どちらの読み方でも、分光器の目盛りは同じ}$$
</div>

<p><em>「光が伸びた」のではなく「物差しが育った」</em> ── 前シリーズ第2回・第3回で言葉として出したことが、今回の 01節の表で完全に裏づけられました。<strong>光の側には、伸びる余地がそもそも無い。</strong></p>

<div class="fig">
<p class="cap">図：ツマミで語り方を切り替えます。左端（標準の絵）では光子の量が全部あちこちへ動き、右端（この絵）では<strong>四本とも完全に水平になります</strong>。無次元の比（\(s/n\) と \(\eta\)）は、どこでも動きません</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>語り方 \(s\)（左＝標準の絵／右＝質量が育つ絵）<input id="ss" type="range" min="0" max="1000" value="1000" step="1"></label>
  <span class="val" id="vs">s = 1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6b2f2f"></i>光子数密度 \(n_\gamma\)</span>
  <span><i class="swatch" style="background:#a85a3a"></i>エネルギー密度 \(\rho_\gamma\)</span>
  <span><i class="swatch" style="background:#8a6a6a"></i>温度 \(T\)</span>
  <span><i class="swatch" style="background:#b09090"></i>波長 \(\lambda\)</span>
  <span><i class="swatch" style="background:#1f5f5a"></i>無次元比（\(s/n\)、\(\eta\)）</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>種明かし ── 4 次元でだけ、ぴったり釣り合う</h2>

<p>なぜ光だけがこうなるのか。前シリーズ第7回の二行の計算を、もう一度。</p>

<div class="calc">
<span class="tag">マクスウェル作用の、数え上げ</span>
$$S_{\rm EM}=-\frac{1}{4\mu_0}\int\!\sqrt{-g}\;F_{\mu\nu}F_{\alpha\beta}\,g^{\mu\alpha}g^{\nu\beta}\;d^Dx$$
<p class="lbl">体積の測り方が \(\Omega\) を \(D\) 個産み、逆計量が二つで 4 個食う</p>
$$S_{\rm EM}\ \longrightarrow\ \Omega^{\,D-4}\,S_{\rm EM}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">次元 \(D\)</th><th class="mid">2</th><th class="mid">3</th><th class="mid">4</th><th class="mid">5</th><th class="mid">6</th></tr></thead>
<tbody>
<tr><th>残る因子</th><td class="mid">\(\Omega^{-2}\)</td><td class="mid">\(\Omega^{-1}\)</td><td class="mid"><strong>\(\Omega^{0}=1\)</strong></td><td class="mid">\(\Omega^{+1}\)</td><td class="mid">\(\Omega^{+2}\)</td></tr>
</tbody>
</table>
</div>

<p>産んだ数と食った数が釣り合うのは \(D=4\) だけ。<strong>私たちが 4 次元に住んでいることが、光子ガスが静止して見える理由です。</strong> もし 5 次元なら、この絵でも光の量が動いてしまい、「膨張は全部質量に押し込める」という話が成り立ちません。</p>

<h2><span class="n">05</span>もっと素朴な言い方 ── 光には、比べる相手がない</h2>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>物差しを持たない</strong><span>コンプトン波長 \(\hbar/mc\) は \(m\to0\) で無限大 ── どんな長さも指定しない</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>時計も持たない</strong><span>光の世界線に沿った固有時間はゼロ ── どんな時間も指定しない</span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>だから、気づけない</strong><span>物差しを取り替えられても、比べる相手がいないので変化を検出できない</span></div></div>
</div>

<p>第3回で「\(c\cdot t\) を一定と言うには比較相手が要る」、第9回で「原子が縮んでいると言うには比較相手が要る」と書きました。<em>光は、そもそも比較相手を一つも持っていません</em> ── だから共形変換に対して、言うことが何もない。<strong>これが「共形不変」の日常語訳です。</strong></p>

<h2><span class="n">06</span>ただし、量子では壊れる</h2>

<p>ここまでは古典の話です。量子にすると、質量ゼロの理論でも共形対称性は破れます ── 場の理論を定義するのに「細かさの基準 \(\mu\)」が要るからです（前シリーズ第8回）。</p>

<div class="calc">
<span class="tag">破れの大きさ</span>
$$T^\mu{}_\mu=\frac{\beta(g)}{2g}F_{\mu\nu}F^{\mu\nu}$$
<p class="lbl">実験で測れている</p>
$$\frac{1}{\alpha}:\ 137.036\ \longrightarrow\ 127.95\quad(\text{電子質量から }M_Z\text{ まで})$$
</div>

<p>つまり<strong>「光には何も起きていない」は、古典の範囲での話</strong>。量子論は、光にも無理やり物差しを持たせてしまう。この破れは第 V 部（第37回）で正面から扱います ── <em>シリーズの道具が壊れる場所の一つ目</em>です。</p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 「光子ガスが静止している」は、共形変換したあとの座標での話です。</strong> 局所的に測る光速はどの絵でも \(c_0\)、CMB の温度計はどの絵でも 2.7255 K を示します。<em>絵の取り替えで観測が変わることは、一つもありません。</em></p>
<p style="margin:0 0 10px"><strong>② \(n_\gamma\propto a^{-3}\)、\(T\propto a^{-1}\) は断熱膨張の結果です。</strong> 粒子の対消滅でエントロピーが放出される時期には \(g_{*s}\) の変化ぶんの補正が入ります（第2回で 1.10 nat と計算しました）。表は「補正を除いた素直な依存性」を示しています。</p>
<p style="margin:0 0 10px"><strong>③ 「元素合成は \(\eta\) だけの関数」は簡略化です。</strong> 正確には有効相対論的自由度 \(g_*\)、中性子寿命、膨張率も効きます ── そして<em>膨張率こそが前シリーズ番外編①で \(a\propto t\) を落とした当のもの</em>でした。ここで言っているのは「絵を取り替えても \(\eta\) は動かないので、絵のせいで判決は変わらない」ということだけです。</p>
<p style="margin:0 0 10px"><strong>④ \(s_\gamma/n_\gamma=3.60\) は本稿で数値から出した値で、</strong> 黒体の厳密値は \(4\pi^4/(45\zeta(3))=3.6017\)。使った \(n_\gamma=4.11\times10^8\ \mathrm{m^{-3}}\)、\(s_\gamma=1.478\times10^9\ k_B\,\mathrm{m^{-3}}\) は \(T_0=2.7255\) K での標準値です。</p>
<p style="margin:0"><strong>⑤ マクスウェル作用の \(\Omega^{D-4}\) は、\(A_\mu\)（添字が下）のウェイトが 0 であることを使っています。</strong> これは標準的な取り方ですが、\(A^\mu\) で書けば当然ウェイトが変わります ── <em>作用が不変かどうかは書き方に依りません</em>が、途中の数え上げは規約に依ります。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>この絵で光子数密度が一定になる理由を、ウェイトで説明せよ。
<details><summary>答えを見る</summary><div class="ans">\(n_\gamma\) はウェイト \(+3\)（体積の逆数）なので \(\tilde n=a^3n\)。標準の絵では \(n\propto a^{-3}\)。掛けると \(a^3\cdot a^{-3}=1\) で、<strong>完全に相殺</strong>します。エネルギー密度（\(-4\) と \(a^{-4}\)）、温度（\(-1\) と \(a^{-1}\)）、波長（\(+1\) と \(a\)）も同じ構造です。</div></details></li>

<li>CMB を決める無次元数を二つ挙げ、この絵でどうなるか答えよ。
<details><summary>答えを見る</summary><div class="ans">光子 1 個あたりのエントロピー \(s/n=3.60\,k_B\) と、バリオン光子比 \(\eta=6.1\times10^{-10}\)。どちらも無次元なので<strong>まったく動きません</strong>。黒体スペクトルの形も \(\hbar\omega/k_BT\) だけで決まるので不変です。</div></details></li>

<li>マクスウェル作用が共形不変になる次元は。理由も。
<details><summary>答えを見る</summary><div class="ans">\(D=4\) のみ。\(\sqrt{-g}\) が \(\Omega\) を \(D\) 個産み、逆計量二つが 4 個食うので \(\Omega^{D-4}\) が残ります。<em>私たちが 4 次元にいることが、この絵で光子ガスが静止して見える理由</em>です。</div></details></li>

<li>\(z=7\) の銀河のライマン α を、二つの絵で説明せよ。
<details><summary>答えを見る</summary><div class="ans">標準：空間が 8 倍に伸びたので、飛んでいる光の波長も 8 倍になった。この絵：<strong>光は何も変わらず届き</strong>、実験室の水素が重くなって基準のライマン α が 8 倍細かくなった。分光器の読み \(\lambda_{\rm obs}/\lambda_{\rm lab}=8\) は、どちらでも同じ。</div></details></li>

<li>（やや難）「光には何も起きていない」は、どこまで正しいか。
<details><summary>答えを見る</summary><div class="ans"><strong>古典の範囲まで</strong>。量子化には細かさの基準 \(\mu\) が要るので、質量ゼロの理論でも共形対称性は破れます（トレースアノマリー \(T^\mu{}_\mu=(\beta/2g)F^2\)）。その破れは実験で測れていて、\(1/\alpha\) が 137.036 から 127.95 へ走ることがそれです。<em>量子論は、光にも無理やり物差しを持たせてしまう。</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　光には、伸びる余地がなかった</h2>
<p>ウェイト表に従って CMB の量を変換すると、<strong>数密度も、エネルギー密度も、温度も、光子 1 個のエネルギーも、波長も、全部が一定</strong>になります。標準の絵での \(a\) の指数と、その量のウェイトが、ぴったり同じ数だからです。<em>この絵の光子ガスは、完全に静止している</em> ── 今日の \(4.11\times10^8\ \mathrm{m^{-3}}\) が、宇宙の全歴史を通じて同じ値。</p>
<p>それでも観測は一つも変わりません。CMB を決めている無次元数は二つだけ ── 光子 1 個あたりのエントロピー \(3.60\,k_B\) と、バリオン光子比 \(\eta=6.1\times10^{-10}\)。どちらも動かず、黒体スペクトルの形も \(\hbar\omega/k_BT\) で決まるので不変。<strong>元素合成の予言が \(\eta\) の関数である以上、絵を取り替えても判決は動きません</strong> ── 前シリーズ番外編①の「三つの絵のどれで弁護しても同じ」は、突き詰めればこの一行でした。</p>
<p>そして赤方偏移が、まるごと裏返ります。光の側に伸びる余地がないので、<em>変わったのは受け取る側</em>。\(z=7\) なら「波長が 8 倍に伸びた」ではなく「実験室の基準が 8 倍細かくなった」。分光器の読みは同じ 8 です。</p>
<p>種明かしは次元でした ── マクスウェル作用は \(\Omega^{D-4}\) 倍になるので、<strong>ぴったり共形不変なのは \(D=4\) だけ</strong>。私たちが 4 次元に住んでいることが、この絵が成立する理由です。もっと素朴に言えば、光は<em>物差しも時計も持たない</em>（コンプトン波長は無限大、固有時間はゼロ）── だから物差しを取り替えられても、比べる相手がいないので気づけない。ただしこれは古典の話で、量子にすると細かさの基準 \(\mu\) が持ち込まれ、\(1/137\to1/128\) という形で破れが実験にかかります。<strong>道具が壊れる場所の一つ目</strong>です。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第12回</span>
第 II 部もあと数回。次は<strong>真空</strong>です。エネルギー密度はウェイト \(-4\) なので、この絵で真空エネルギーは \(\tilde\rho_\Lambda=a^4\rho_\Lambda\propto t^4\) ── <em>宇宙定数だけが \(t^4\) で育ちます</em>。物質は \(\propto t\)、放射は一定。<strong>三者三様で、しかも \(\Lambda\) がいちばん速い。</strong> ところが無次元にすると \(\rho_\Lambda^{1/4}/M_{\rm Pl}=1.84\times10^{-31}\) で不変。宇宙定数問題（\(10^{120}\) のずれ）が、この絵でどう見えるか ── そして<em>「なぜ今?」問題だけは、絵を変えても消えない</em>ことを確かめます。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=318;
  var xmin=-3, xmax=0.3;      // log10 a
  var ymin=-4, ymax=13;       // log10(値／今日)

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function line(sl,col,w,dash){
    g.strokeStyle=col; g.lineWidth=w; if(dash) g.setLineDash(dash);
    g.beginPath();
    var y0=sl*xmin, y1=sl*xmax;
    g.moveTo(px(xmin),py(Math.max(Math.min(y0,ymax),ymin)));
    g.lineTo(px(xmax),py(Math.max(Math.min(y1,ymax),ymin)));
    g.stroke(); g.setLineDash([]);
  }

  function draw(){
    var s=parseInt(ss.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right';
    for(var e=-4;e<=12;e+=2){
      var y=py(e);
      g.strokeStyle=(e===0?'#e0d2d2':'#f6efef'); g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a89494'; g.fillText(e===0?'1':(e<0?'10⁻'+Math.abs(e):'10'+e), X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-3;q<=0;q++){
      var x=px(q);
      g.strokeStyle='#faf5f5'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a89494'; g.fillText(q===0?'いま':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#d2c0c0'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // 標準の絵での指数 × (1-s)
    line(-3*(1-s), '#6b2f2f', 3.2);          // n ∝ a^-3
    line(-4*(1-s), '#a85a3a', 2.8);          // ρ ∝ a^-4
    line(-1*(1-s), '#8a6a6a', 2.4);          // T ∝ a^-1
    line(+1*(1-s), '#b09090', 2.4);          // λ ∝ a
    line(0,        '#1f5f5a', 3.6);          // 無次元比

    g.textAlign='left';
    if(s<0.9){
      g.fillStyle='#6b2f2f'; g.fillText('n', px(xmin)+6, py(Math.min(-3*(1-s)*xmin,ymax))-6);
      g.fillStyle='#a85a3a'; g.fillText('ρ', px(xmin)+22, py(Math.min(-4*(1-s)*xmin,ymax))+14);
      g.fillStyle='#8a6a6a'; g.fillText('T', px(xmin)+6, py(-1*(1-s)*xmin)-6);
      g.fillStyle='#b09090'; g.fillText('λ', px(xmin)+6, py(1*(1-s)*xmin)+14);
    }
    g.fillStyle='#1f5f5a';
    g.fillText('無次元比 s/n・η（どこでも水平）', px(-1.5), py(0)-10);
    if(s>0.985){
      g.fillStyle='#6b2f2f'; g.textAlign='right';
      g.fillText('n・ρ・T・λ が全部ここに重なる', X1-8, py(0)+18);
    }

    g.fillStyle='#8a7070'; g.textAlign='center';
    g.fillText('スケール因子  a', (X0+X1)/2, Y1+36);

    vs.textContent='s = '+s.toFixed(2);
    var tag = s>0.995?'（質量が育つ絵）':(s<0.005?'（標準の絵）':'（途中の語り方）');
    ro.textContent='s = '+s.toFixed(2)+' '+tag+
      '　n ∝ a^'+(-3*(1-s)).toFixed(2)+
      '　ρ ∝ a^'+(-4*(1-s)).toFixed(2)+
      '　T ∝ a^'+(-1*(1-s)).toFixed(2)+
      '　λ ∝ a^'+(1*(1-s)).toFixed(2)+
      (s>0.995 ? '　★ 四本とも指数ゼロ ── 光子ガスは完全に静止' : '');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-11-light.html', acc='#6b2f2f', ops='#1f5f5a',
      title='光に入れてみる ── わかる c·t=一定 第11回',
      ep='第 11 回 ／ 光子ガスは、完全に静止している',
      eyebrow='光には、伸びる余地がそもそもありませんでした',
      h1='光に、<br>入れてみる',
      sub='数密度も、エネルギー密度も、温度も、波長も、全部が一定。<br><em>宇宙の歴史を通じて、光には何も起きていない。</em>',
      byline_l='必要な道具：ウェイトの足し算、指数の突き合わせ',
      byline_r='\\(\\Omega^{D-4}\\) ── 4次元でだけ、ぴったり',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第11回、物理好きの高校生・大学生向け読み物です。断熱膨張のもとで \\(n_\\gamma\\propto a^{-3}\\)、\\(\\rho_\\gamma\\propto a^{-4}\\)、\\(T\\propto a^{-1}\\)、\\(\\lambda\\propto a\\) となること、共形変換のもとでそれぞれのウェイトが \\(+3,-4,-1,+1\\) であること、およびマクスウェル作用が \\(\\Omega^{D-4}\\) 倍になり \\(D=4\\) でのみ共形不変となることは、いずれも標準的な結果です（前シリーズ第7回）。今日の CMB の値 \\(T_0=2.7255\\) K、\\(n_\\gamma=4.11\\times10^8\\ \\mathrm{m^{-3}}\\)、\\(s_\\gamma=1.478\\times10^9\\,k_B\\,\\mathrm{m^{-3}}\\)、\\(\\eta=6.1\\times10^{-10}\\) は標準値で、\\(s_\\gamma/n_\\gamma=3.60\\,k_B\\)（黒体の厳密値 \\(4\\pi^4/45\\zeta(3)=3.6017\\)）は本稿での計算です。粒子の対消滅によるエントロピー放出期には \\(g_{*s}\\) の変化ぶんの補正が入ります（第2回で 1.10 nat と計算）。「元素合成は \\(\\eta\\) だけの関数」は簡略化で、正確には \\(g_*\\)・中性子寿命・膨張率も効きます ── <strong>そして膨張率こそが前シリーズ番外編①で \\(a\\propto t\\) を棄却した当のものです</strong>。本稿が主張しているのは「絵を取り替えても \\(\\eta\\) は動かないので、絵のせいで判決は変わらない」という点のみです。\\(A_\\mu\\)（添字が下）のウェイトを 0 と取るのは標準的な規約で、途中の数え上げは規約に依存しますが作用の不変性そのものは依りません。量子化により共形対称性が破れること（トレースアノマリー \\(T^\\mu{}_\\mu=(\\beta/2g)F_{\\mu\\nu}F^{\\mu\\nu}\\)）、\\(\\alpha^{-1}\\) が 137.036 から \\(M_Z\\) で 127.95 へ走ることも標準的です（前シリーズ第8回）。局所的に測る光速および CMB 温度計の読みは、どの絵でも同じです。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルで、初期宇宙まで外挿した場合は元素合成と矛盾します（Lewis, Barnes &amp; Kaushik 2016）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで語り方を切り替え、右端で光子の四本が全部水平になる様子が見えます。「答えを見る」で解答が開きます。')
