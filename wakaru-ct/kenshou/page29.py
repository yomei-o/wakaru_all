# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第 IV 部の三人目は <strong>MOND</strong> です。「加速度が \(a_0=1.2\times10^{-10}\ \mathrm{m/s^2}\) より小さいところでニュートン則が変わる」── この \(a_0\) は<em>次元付き</em>なので、第3回の手術がそのまま当たります。<strong>小さいって、何と比べて？</strong> 探すと、すぐ隣に \(cH_0\) がいました。そして手術のあとに残った主張を第5回の天秤にかけると、<em>「暗黒物質か MOND か」がそもそも一つの問いではない</em>ことが見えます。</p>

<h2><span class="n">01</span>\(a_0\) は次元付き ── だから比較相手が要る</h2>

<div class="calc">
<span class="tag">ウェイトを数える</span>
<p class="lbl">加速度の次元は \(L/T^2\)、長さも時間もウェイト \(+1\) なので</p>
$$w(a)=(+1)-2(+1)=-1\qquad(\text{次元付き＝帳簿})$$
</div>

<p>第13回でやった機械的な数え上げです。<strong>\(a_0\) は帳簿の側にいる</strong>ので、「加速度が \(a_0\) より小さい」は ── <em>比較相手を言うまで文になっていません</em>。もちろん MOND は比較相手を用意しています（\(a_0\) そのもの）。問題は、<strong>その \(a_0\) がどこから来たのか</strong>です。</p>

<h2><span class="n">02</span>比較相手を探すと、すぐ隣に \(cH_0\) がいる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>候補</th><th class="mid">値 [m/s²]</th><th class="mid">\(a_0\) との比</th></tr></thead>
<tbody>
<tr><th>\(cH_0\)</th><td class="mid">\(6.548\times10^{-10}\)</td><td class="mid">0.183</td></tr>
<tr class="hi"><th>\(cH_0/2\pi\)</th><td class="mid">\(1.042\times10^{-10}\)</td><td class="mid"><strong>1.15</strong></td></tr>
<tr><th>\(c^2\sqrt{\Lambda/3}=cH_0\sqrt{\Omega_\Lambda}\)</th><td class="mid">\(5.420\times10^{-10}\)</td><td class="mid">0.221</td></tr>
<tr><th>\(cH_0/6\)</th><td class="mid">\(1.091\times10^{-10}\)</td><td class="mid">1.10</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0">どれも \(O(1)\) ── <strong>\(a_0\) は「宇宙の地平面スケールの加速度」と同じ桁にいます。</strong><br>
ミルグロム自身が 1983 年の最初から指摘している一致です。</p>
</div>

<p>これは気味が悪いほど示唆的です。<em>銀河の回転曲線を合わせるために導入した定数が、宇宙の年齢から作った加速度と一致する</em> ── 天文学のいちばん小さいスケールと、宇宙論のいちばん大きいスケールが、ここで触れています。</p>

<h2><span class="n">03</span>この一致は、絵を取り替えても動かない</h2>

<div class="calc">
<span class="tag">ウェイトを突き合わせる</span>
$$w(a_0)=-1,\qquad w(cH_0)=w(c/t)=0-(+1)=-1$$
<p class="lbl">同じウェイトなので、比は</p>
$$\frac{a_0}{cH_0}\ \text{はウェイト }0\ \text{── 共形不変}$$
</div>

<p>第16回のウェイトの地図でいう<strong>ゼロの列</strong>です。<em>この一致は、このシリーズの道具では一ミリも動かせません</em> ── だからこそ、まじめに仕分ける価値があります。</p>

<h2><span class="n">04</span>驚きをビットで測る</h2>

<div class="calc">
<span class="tag">第19回の手続き</span>
<p class="lbl">自然界の加速度スケールの幅</p>
$$\text{プランク加速度}\ \frac{c}{t_P}=5.56\times10^{51}\ \mathrm{m/s^2}\ \longrightarrow\ cH_0=6.55\times10^{-10}\ \mathrm{m/s^2}$$
$$\text{幅}=60.9\ \text{桁}$$
<p class="lbl">「係数 10 以内で一致」の驚き</p>
$$-\log_2\frac{1.0}{60.9}=5.9\ \text{ビット}\qquad(\text{係数 3 以内なら }6.9\ \text{ビット})$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>一致</th><th class="mid">驚き</th><th class="mid">分類（第19回）</th></tr></thead>
<tbody>
<tr><th>\(\rho_\Lambda^{1/4}\) と \(m_\nu\)</th><td class="mid">4.7 bit</td><td class="mid">偶然</td></tr>
<tr class="hi"><th>\(a_0\simeq cH_0/2\pi\)</th><td class="mid"><strong>5.9 bit</strong></td><td class="mid"><strong>偶然の帯</strong></td></tr>
<tr><th>1 ビット ↔ 1.96 fm</th><td class="mid">7.4 bit</td><td class="mid">偶然</td></tr>
<tr><th>小出の関係式</th><td class="mid">15.7 bit</td><td class="mid">経験式</td></tr>
</tbody>
</table>
</div>

<p><strong>コイン 6 回ぶん</strong>です ── 前シリーズ番外編⑤の \(\rho_\Lambda^{1/4}\) と \(m_\nu\)（4.7 ビット）と、ほぼ同じ層にいます。<em>「気味が悪いほど示唆的」という印象と、実際の驚きの大きさは、こんなに違う。</em> ただし ── <strong>説明を与える理論があれば、分類は「物理」へ移ります</strong>（第27回でインフレーションの \(N\) の一致がそうなったように）。地平面が力学の境界条件を与える型の説明は実際に提案されており、そちらが正しければこの 5.9 ビットは物理です。</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">05</span>手術 ── MOND が実際に主張していること</h2>

<div class="seven">
<div class="row"><div class="mk">A</div><div class="txt"><strong>「加速度が小さい」</strong><span>\(a_0\) を天下りで置くだけなら、<em>比較相手を持ち込んだ</em>にすぎません</span></div></div>
<div class="row hi"><div class="mk">B</div><div class="txt"><strong>「力学が無次元比 \(g/a_0\) だけで決まる」</strong><span>これは観測にかかる主張 ── そして<em>強い予言を持ちます</em>：バリオンの分布だけから回転曲線が決まる（動径加速度関係）</span></div></div>
</div>

<p>第27回・第28回とまったく同じ形です。<strong>(B) が本体</strong>で、しかも MOND の (B) は非常に強い ── <em>暗黒物質を仮定する模型では、バリオンとハローの量が独立なので、こんな予言はできません</em>。</p>

<h2><span class="n">06</span>核心 ── 第5回の天秤にかける</h2>

<p>では (B) を、記述長で測ります。銀河の回転曲線のデータセット（SPARC：175 銀河、2693 点）で勘定します。</p>

<div class="calc">
<span class="tag">パラメータの値段</span>
$$\tfrac12\log_2(2693)=5.70\ \text{ビット／個}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>模型</th><th class="mid">パラメータ数</th><th class="mid">記述長</th><th class="mid">内訳</th></tr></thead>
<tbody>
<tr class="hi"><th>MOND</th><td class="mid"><strong>4</strong></td><td class="mid"><strong>22.8 bit</strong></td><td class="mid">\(a_0\)（全銀河共通）＋ 内挿関数の形</td></tr>
<tr><th>ハロー模型</th><td class="mid">350</td><td class="mid">1994 bit</td><td class="mid">銀河ごとに 2 個（例：NFW の \(M_{200}\) と集中度）</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0">銀河の回転曲線というデータセットに限れば、<strong>MOND が 1971 ビット勝ちます。</strong><br>
── 第5回で \(c\cdot t=\)一定 が 148 ビット負けたのと、同じ天秤・同じ単位です。</p>
</div>

<p>（質量光度比 \(M/L\) は両方の模型が銀河ごとに持つので、相殺して勘定に入りません。）</p>

<h2><span class="n">07</span>ところが、データセットを変えると逆転する</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>データセット</th><th class="mid">勝つのは</th><th class="mid">理由</th></tr></thead>
<tbody>
<tr class="hi"><th>銀河の回転曲線</th><td class="mid"><strong>MOND</strong></td><td class="mid">パラメータ 4 対 350 ── 1971 ビット</td></tr>
<tr><th>銀河団</th><td class="mid">\(\Lambda\)CDM</td><td class="mid">MOND でも 2 倍程度の未検出質量が残る</td></tr>
<tr><th>弾丸銀河団</th><td class="mid">\(\Lambda\)CDM</td><td class="mid">質量分布とガスが空間的に分離している</td></tr>
<tr><th>CMB の音響ピーク</th><td class="mid">\(\Lambda\)CDM</td><td class="mid">6 パラメータで 1701 点、\(\chi^2/\mathrm{dof}\approx1\)</td></tr>
<tr><th>大規模構造の成長</th><td class="mid">\(\Lambda\)CDM</td><td class="mid">相対論的完成形ごとに結果が違う</td></tr>
</tbody>
</table>
</div>

<div class="fig">
<p class="cap">図：データセットごとの記述長の差。<strong>右へ行くほど \(\Lambda\)CDM 有利、左へ行くほど MOND 有利</strong>。ツマミで「どのデータセットを重く見るか」を変えると、総合の勝敗が動きます ── <em>これが「一つの問いではない」ということです</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>銀河の回転曲線をどれだけ重く見るか<input id="sw" type="range" min="0" max="100" value="50" step="1"></label>
  <span class="val" id="vw">50%</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2f5a3a"></i>MOND 有利</span>
  <span><i class="swatch" style="background:#8a4a6a"></i>\(\Lambda\)CDM 有利</span>
</div>
</div>

<div class="keybox">
<p class="lbl">07節の結論</p>
<p style="margin:6px 0 0"><strong>「暗黒物質か MOND か」は、一つの問いではありません。</strong><br>
第5回の天秤で測ると、<em>答えがデータセットごとに違う</em>ことが露わになります。<br>
── そして<strong>どちらの側も、相手が勝っているデータセットを説明できていない</strong>。</p>
</div>

<h2><span class="n">08</span>検証可能な方向 ── \(a_0\) は時間変化するか</h2>

<p>02節の一致には、実は<strong>検証可能な分岐</strong>が隠れています。\(a_0=cH/2\pi\) が<em>動的な関係</em>なら、\(a_0\) は \(H\) とともに減ってきたはずです。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(z\)</th><th class="mid">0</th><th class="mid">0.5</th><th class="mid">1.0</th><th class="mid">2.0</th></tr></thead>
<tbody>
<tr><th>\(H(z)/H_0\)</th><td class="mid">1.00</td><td class="mid">1.32</td><td class="mid">1.79</td><td class="mid">3.03</td></tr>
<tr class="hi"><th>\(a_0(z)/a_0\)（動的なら）</th><td class="mid">1.00</td><td class="mid">1.32</td><td class="mid">1.79</td><td class="mid"><strong>3.03</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>\(z=2\) で 3 倍</strong>です。高赤方偏移の回転曲線で、原理的には判定できます。逆に \(a_0\) が<em>ただの定数</em>なら、この予言はありません ── <strong>同じ「一致」でも、中身が別のものだった</strong>ということです。観測は現在進行形で、本稿は判定しません。</p>

<div class="aside">
<span class="tag">第19回の分類が、そのまま実験計画になる</span>
第19回で「恒等式・偶然・物理」の仕分け手続きを作りました。今回はそれが<em>次に何を測ればよいか</em>を教えてくれます ── <strong>偶然なら \(a_0\) は定数、物理なら \(a_0\propto H\)</strong>。5.9 ビットの一致がどちらなのかは、\(z\sim2\) の回転曲線が 3 倍の差として見せてくれる。<em>「驚きをビットで測る」は、鑑賞ではなく設計の道具でした。</em>
</div>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① MOND の「パラメータ 4 個」は、内挿関数 \(\mu(x)\) の自由度を 3 個ぶんと数えた本稿の見積もりです。</strong> \(\mu(x)\) は<em>関数</em>なので、厳密にはパラメータ 1 個ではありません ── 実務では「simple」「standard」「RAR」など数種類の形が使われ、どれを選ぶかも自由度です。3 個は甘めの数え方で、<em>これを 10 個と数えても 06節の結論（1900 ビット以上の差）は変わりません</em>。</p>
<p style="margin:0 0 10px"><strong>② ハロー模型の「銀河ごとに 2 個」も見積もりです。</strong> 実際には \(\Lambda\)CDM 側にも質量–集中度関係などの<em>事前分布</em>があり、それが実効的なパラメータ数を減らします。厳密な比較にはベイズ証拠の計算が要ります ── <strong>本稿の 1971 ビットは上限側の見積もり</strong>と読んでください。それでも桁は変わりません。</p>
<p style="margin:0 0 10px"><strong>③ 07節の表は、各分野の到達点を要約したものです。</strong> 相対論的 MOND（TeVeS、および Skordis &amp; Złośnik 2021 のような近年の定式化）は CMB を再現できる場合もありますが、そのぶん場とパラメータが増えます ── <em>「CMB で \(\Lambda\)CDM が勝つ」は定式化に依存します</em>。銀河団の残存質量問題は、MOND 側でも広く認められています。</p>
<p style="margin:0 0 10px"><strong>④ 04節の驚きは事前範囲の取り方に依存します</strong>（第19回①と同じ注意）。プランク加速度から \(cH_0\) までの 60.9 桁を事前範囲としましたが、「銀河で意味を持つ加速度」に限れば範囲は狭くなり、驚きは小さくなります。<em>順序をつけるには使えますが、絶対的な数値ではありません。</em></p>
<p style="margin:0"><strong>⑤ 本稿は MOND を支持も否定もしません。</strong> やったのは、\(a_0\) の中に隠れた比較相手を名指しし、一致の驚きを測り、記述長の勘定をデータセットごとに分けたことだけです。<em>この記法（\(c\cdot t=\)一定）は MOND について何も言いません</em> ── 03節のとおり、関係する量がすべて共形不変だからです（第13回・第16回の結論のとおり）。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>\(a_0\) のウェイトを求め、第3回の手術がなぜ当たるか説明せよ。
<details><summary>答えを見る</summary><div class="ans">加速度の次元は \(L/T^2\)、長さも時間もウェイト \(+1\) なので \(w=(+1)-2(+1)=-1\)。<strong>次元付き＝帳簿</strong>なので、「加速度が小さい」は比較相手を言うまで文になりません。</div></details></li>

<li>\(a_0\) と \(cH_0\) の比を求めよ。
<details><summary>答えを見る</summary><div class="ans">\(cH_0=2.998\times10^8\times2.184\times10^{-18}=6.548\times10^{-10}\ \mathrm{m/s^2}\)。\(a_0/cH_0=0.183\)、すなわち <strong>\(a_0\simeq cH_0/5.5\simeq cH_0/2\pi\)</strong>。</div></details></li>

<li>この一致が共形変換で動かないことを示せ。
<details><summary>答えを見る</summary><div class="ans">\(w(a_0)=-1\)、\(w(cH_0)=w(c/t)=0-(+1)=-1\)。<strong>同じウェイトなので比はウェイト 0 ＝ 共形不変</strong>。第16回のウェイトの地図のゼロの列にいます。</div></details></li>

<li>回転曲線のデータセットで、記述長の差を求めよ。
<details><summary>答えを見る</summary><div class="ans">パラメータ 1 個の値段は \(\tfrac12\log_2(2693)=5.70\) ビット。MOND は 4 個で 22.8 ビット、ハロー模型は \(2\times175=350\) 個で 1994 ビット。差は <strong>1971 ビット、MOND の勝ち</strong>（このデータセットに限れば）。</div></details></li>

<li>（やや難）「暗黒物質か MOND か」に一つの答えがあるか。
<details><summary>答えを見る</summary><div class="ans">ありません。<strong>第5回の天秤で測ると、答えがデータセットごとに違います</strong> ── 銀河の回転曲線では MOND が 1971 ビット勝ち、銀河団・弾丸銀河団・CMB・構造成長では \(\Lambda\)CDM が勝つ。<em>そしてどちらの側も、相手が勝っているデータセットを説明できていません。</em> 記述長で測ることの効用は、勝敗を決めることではなく、<strong>問いが一つではないことを可視化する</strong>ところにあります。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　問いが一つではなかった</h2>
<p>\(a_0\) は次元付き（ウェイト \(-1\)）なので、「加速度が小さい」は比較相手を言うまで文になりません。探すと、すぐ隣に \(cH_0\) がいました ── <strong>\(a_0/cH_0=0.18\)、\(a_0\simeq cH_0/2\pi\) なら比 1.15</strong>。銀河の回転曲線を合わせるために導入した定数が、宇宙の年齢から作った加速度と同じ桁にいる。しかも \(a_0\) と \(cH_0\) はウェイトが同じなので、<em>この一致は共形変換で一ミリも動きません</em>。</p>
<p>第19回の手続きで驚きを測ると <strong>5.9 ビット</strong> ── コイン 6 回ぶんで、\(\rho_\Lambda^{1/4}\) と \(m_\nu\)（4.7 ビット）とほぼ同じ層です。<em>「気味が悪いほど示唆的」という印象と、実際の驚きの大きさは、ずいぶん違いました。</em></p>
<p>手術の結果、MOND の本体は (B)「力学が無次元比 \(g/a_0\) だけで決まる」でした。これは強い予言を持ちます ── バリオンの分布だけから回転曲線が決まる。第5回の天秤にかけると、SPARC（175 銀河、2693 点）で <strong>MOND がパラメータ 4 個、ハロー模型が 350 個 ── 差 1971 ビット</strong>。</p>
<p>ところがデータセットを変えると逆転します ── 銀河団、弾丸銀河団、CMB の音響ピーク、構造成長では \(\Lambda\)CDM。<strong>「暗黒物質か MOND か」は一つの問いではありませんでした。</strong> そして最後に、02節の一致には検証可能な分岐が隠れています ── <em>偶然なら \(a_0\) は定数、物理なら \(a_0\propto H\) で \(z=2\) に 3 倍の差</em>。第19回の仕分け手続きが、そのまま実験計画になりました。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第30回</span>
第28回と第29回で「定数が変わる」型の理論を二つ扱いました。次は<strong>実際に測っているほうを見ます</strong> ── 原子時計、オクロ天然原子炉、クエーサー吸収線。<em>人類は無次元定数の不変性を、どれだけの精度で、どれだけの時間にわたって確かめたのか</em>。第28回で表にした上限を、今度は<strong>測定の側から</strong>読み直します。そして一つの数を出します ── <em>宇宙の全歴史にわたって、\(\alpha\) について私たちが知っているのは何ビットか。</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sw=document.getElementById('sw'), vw=document.getElementById('vw'), ro=document.getElementById('ro');
  var X0=210, X1=690, Y0=44;
  // [名前, MOND 側の記述長優位(bit), ΛCDM 側の優位(bit)]  ── 正なら MOND 有利
  var SETS=[
    ['銀河の回転曲線', +1971],
    ['銀河団', -300],
    ['弾丸銀河団', -200],
    ['CMB の音響ピーク', -800],
    ['大規模構造の成長', -250]
  ];
  var SCALE=2100;

  function draw(){
    var w=parseInt(sw.value,10)/100;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    var XM=(X0+X1)/2;
    // 中央線
    g.strokeStyle='#c8ccd2'; g.lineWidth=1.6;
    g.beginPath(); g.moveTo(XM,Y0-16); g.lineTo(XM,Y0+5*44+14); g.stroke();
    g.fillStyle='#2f5a3a'; g.textAlign='center';
    g.fillText('← MOND 有利', XM-110, Y0-24);
    g.fillStyle='#8a4a6a';
    g.fillText('ΛCDM 有利 →', XM+110, Y0-24);

    var total=0;
    for(var i=0;i<SETS.length;i++){
      var v=SETS[i][1];
      var ww = (i===0? w*2 : (2-2*w)/4);      // 重み：回転曲線 vs その他
      var vv=v*ww;
      total+=vv;
      var y=Y0+i*44+8;
      var half=(X1-X0)/2;
      var len=Math.max(Math.min(Math.abs(vv)/SCALE,1)*half,2);
      g.fillStyle = v>0 ? '#2f5a3a' : '#8a4a6a';
      g.globalAlpha=0.85;
      if(v>0) g.fillRect(XM-len, y, len, 24); else g.fillRect(XM, y, len, 24);
      g.globalAlpha=1;
      g.fillStyle='#3a4048'; g.textAlign='right';
      g.fillText(SETS[i][0], X0-14, y+17);
      g.fillStyle = v>0 ? '#24462d' : '#6d3a54';
      g.textAlign = v>0 ? 'right' : 'left';
      g.font='11px sans-serif';
      g.fillText((v>0?'':'−')+Math.abs(vv).toFixed(0)+' bit', v>0? XM-len-8 : XM+len+8, y+17);
      g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    }

    // 総合
    var y2=Y0+5*44+26;
    g.strokeStyle='#e0e3e8'; g.lineWidth=1;
    g.beginPath(); g.moveTo(X0-30,y2-8); g.lineTo(X1,y2-8); g.stroke();
    var half=(X1-X0)/2;
    var len=Math.max(Math.min(Math.abs(total)/SCALE,1)*half,2);
    g.fillStyle = total>0 ? '#2f5a3a' : '#8a4a6a';
    if(total>0) g.fillRect(XM-len, y2+4, len, 28); else g.fillRect(XM, y2+4, len, 28);
    g.fillStyle='#3a4048'; g.textAlign='right';
    g.font='bold 13px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('総合', X0-14, y2+24);
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    vw.textContent=Math.round(w*100)+'%';
    ro.textContent='回転曲線の重み '+Math.round(w*100)+'%　→　総合 '+
      (total>0? 'MOND が '+total.toFixed(0)+' ビット勝ち' : 'ΛCDM が '+(-total).toFixed(0)+' ビット勝ち')+
      '　／　重みを変えるだけで勝敗が入れ替わる ── 問いが一つではない';
  }
  sw.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-29-mond.html', acc='#2f5a3a', ops='#8a4a6a',
      title='MOND ── 加速度に隠れた比較相手 ── わかる c·t=一定 第29回',
      ep='第 29 回 ／ 第 IV 部・三人目の患者',
      eyebrow='「暗黒物質か MOND か」は、そもそも一つの問いではありませんでした',
      h1='MOND ── 加速度に<br>隠れた比較相手',
      sub='\\(a_0=1.2\\times10^{-10}\\ \\mathrm{m/s^2}\\) は次元付きです ── 小さいって、何と比べて？<br><em>探すと、すぐ隣に \\(cH_0\\) がいました。</em>',
      byline_l='必要な道具：ウェイトの足し算、第19回の作法、第5回の天秤',
      byline_r='\\(a_0/cH_0=0.18\\)　／　驚き 5.9 bit',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第29回、物理好きの高校生・大学生向け読み物です。MOND は Milgrom (1983, ApJ 270, 365) によります。加速度スケール \\(a_0\\simeq1.2\\times10^{-10}\\ \\mathrm{m/s^2}\\) が \\(cH_0\\) と同じ桁にあることはミルグロム自身が当初から指摘しており、動径加速度関係（RAR）は McGaugh, Lelli &amp; Schombert (2016, PRL 117, 201101)、SPARC のサンプル（175 銀河・2693 点）は Lelli, McGaugh &amp; Schombert (2016, AJ 152, 157) によります。本稿の \\(a_0/cH_0=0.183\\)、\\(a_0/(cH_0/2\\pi)=1.15\\)、驚き 5.9 ビット、記述長の差 1971 ビット、および \\(a_0\\propto H\\) とした場合の \\(z=2\\) での 3.0 倍は本稿での計算です（kenshou/calc33.py）。<strong>MOND の「パラメータ 4 個」は内挿関数 \\(\\mu(x)\\) の自由度を 3 個ぶんと数えた本稿の見積もりで、\\(\\mu(x)\\) は本来<em>関数</em>であってパラメータ 1 個ではありません</strong> ── 10 個と数えても 06節の結論（1900 ビット以上の差）は変わりません。ハロー模型の「銀河ごとに 2 個」も見積もりで、実際には質量–集中度関係などの事前分布が実効的なパラメータ数を減らすため、<em>1971 ビットは上限側の見積もり</em>です（厳密な比較にはベイズ証拠の計算が要ります）。07節の表は各分野の到達点の要約で、相対論的 MOND（TeVeS、Skordis &amp; Złośnik 2021 ほか）には CMB を再現する定式化もあり、そのぶん場とパラメータが増えます ── <em>「CMB で \\(\\Lambda\\)CDM が勝つ」は定式化に依存します</em>。銀河団に残る未検出質量の問題は MOND 側でも広く認められています。04節の驚きは事前範囲の取り方に依存します（第19回①）。<strong>本稿は MOND を支持も否定もせず</strong>、\\(a_0\\) に隠れた比較相手を名指しし、一致の驚きを測り、記述長の勘定をデータセットごとに分けたものです。なおこの記法（\\(c\\cdot t=\\)一定）は MOND について何も言いません ── 関係する量がすべて共形不変だからです（第13回・第16回）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーでデータセットの重みを変え、総合の勝敗が入れ替わる様子が見えます。「答えを見る」で解答が開きます。')
