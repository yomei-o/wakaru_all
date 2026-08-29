# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">前回、試せたのは<strong>無次元量に置かれた特徴づけだけ</strong>でした。今回はその地図を描きます ── 物理に出てくる無次元量を並べ、<em>何が物理で、何が帳簿か</em>の境界線を一枚に。そして分かるのは ── <strong>2019 年に、国際単位系がその線を同じ場所に引いていた</strong>ことです。</p>

<h2><span class="n">01</span>2019 年、国際単位系が線を引き直した</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">定数</th><th class="mid">固定された値（厳密）</th><th class="mid">定義される単位</th></tr></thead>
<tbody>
<tr><th class="mid">\(\Delta\nu_{\rm Cs}\)</th><td class="mid">9 192 631 770 Hz</td><td class="mid">秒</td></tr>
<tr><th class="mid">\(c\)</th><td class="mid">299 792 458 m/s</td><td class="mid">メートル</td></tr>
<tr class="hi"><th class="mid">\(h\)</th><td class="mid">\(6.62607015\times10^{-34}\) J·s</td><td class="mid"><strong>キログラム</strong></td></tr>
<tr><th class="mid">\(e\)</th><td class="mid">\(1.602176634\times10^{-19}\) C</td><td class="mid">アンペア</td></tr>
<tr><th class="mid">\(k_B\)</th><td class="mid">\(1.380649\times10^{-23}\) J/K</td><td class="mid">ケルビン</td></tr>
<tr><th class="mid">\(N_A\)</th><td class="mid">\(6.02214076\times10^{23}\) /mol</td><td class="mid">モル</td></tr>
<tr><th class="mid">\(K_{\rm cd}\)</th><td class="mid">683 lm/W</td><td class="mid">カンデラ</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>キログラム原器は廃止されました。</strong> 質量は \(h\) から作られます。<br>
── これは、<em>次元付きの量が帳簿であることの、国際的な公式宣言</em>です。<br>
<strong>第3回でこのシリーズが手で引いた線を、世界の度量衡が同じ場所に引いていました。</strong></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">02</span>核心 ── ところが \(\alpha\) は固定できなかった</h2>

<div class="calc">
<span class="tag">\(e\)、\(\hbar\)、\(c\) はいま厳密に固定されている。では \(\alpha\) も決まるのか？</span>
$$\alpha=\frac{e^2}{4\pi\varepsilon_0\hbar c}\qquad\Longrightarrow\qquad \textbf{決まらない}$$
<p class="lbl">\(\varepsilon_0\) が測定量になったから ── \(1/\alpha=137.035999177(21)\)、いまも<strong>測る</strong>しかない</p>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>無次元だから、法令では決められないのです。</strong><br>
── \(c\) は決められて \(\alpha\) は決められない。<br>
<em>これが第3回の線の、いちばん鮮明な形です。</em></p>
</div>

<h2><span class="n">03</span>単位を決めるのに、いくつ要るか</h2>

<div class="seven">
<div class="row"><div class="mk">3</div><div class="txt"><strong>力学の世界には次元が三つ</strong><span>長さ・時間・質量</span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>\(c\)、\(\hbar\)、\(G\) の三つで、ちょうど使い切れる</strong><span>プランク単位系 ── <em>そこで書けば、すべての量は無次元になる</em></span></div></div>
<div class="row hi"><div class="mk">?</div><div class="txt"><strong>「基本定数はいくつあるか」は決着していない</strong><span>3 個／2 個／1 個／0 個 と立場が分かれる（Duff–Okun–Veneziano 2002 の三者鼎談）── <em>ただしどの立場でも一致していることがある</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">03節の結論</p>
<p style="margin:6px 0 0"><strong>どの立場でも一致していること ── 物理の中身は、無次元量の側にある。</strong></p>
</div>

<h2><span class="n">04</span>無次元量の地図</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">値</th><th class="mid">説明はあるか</th></tr></thead>
<tbody>
<tr class="hi"><th>宇宙が処理した情報 \(N\)（第24回）</th><td class="mid">\(3.1\times10^{122}\)</td><td class="mid">第40・41回と同じ数</td></tr>
<tr><th>陽子と電子の質量比 \(m_p/m_e\)</th><td class="mid">\(1836.15\)</td><td class="mid">説明されていない</td></tr>
<tr><th>\(1/\alpha\)</th><td class="mid">\(137.036\)</td><td class="mid">説明されていない</td></tr>
<tr><th>スペクトル指数 \(n_s\)</th><td class="mid">\(0.9649\)</td><td class="mid">インフレーションが説明を主張</td></tr>
<tr><th>\(\Omega_\Lambda\)</th><td class="mid">\(0.685\)</td><td class="mid">説明されていない</td></tr>
<tr><th>\(v/M_P\)</th><td class="mid">\(2.0\times10^{-17}\)</td><td class="mid"><strong>階層性問題</strong></td></tr>
<tr><th>\(\alpha_G=Gm_p^2/\hbar c\)</th><td class="mid">\(5.9\times10^{-39}\)</td><td class="mid">説明されていない</td></tr>
<tr class="hi"><th>\(\rho_\Lambda/\rho_{\rm Planck}\)（第32回）</th><td class="mid">\(1.13\times10^{-123}\)</td><td class="mid"><strong>宇宙定数問題</strong></td></tr>
</tbody>
</table>
</div>

<p>いちばん大きい \(3.1\times10^{122}\) から いちばん小さい \(1.13\times10^{-123}\) まで ── <strong>815 ビットの幅</strong>があります。<em>そしてすべてが同じ列（ウェイト 0）にあり、共形変換はどれ一つ動かせません。</em></p>

<div class="fig">
<p class="cap">図：物理に出てくる無次元量を、対数の一本の軸に並べたもの。<strong>815 ビットの幅</strong>があります。ツマミで「窓」を動かすと、そこにいくつ入るかが読めます ── <em>大きい側にも小さい側にも、説明されていない数が並んでいます</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>窓の中心（\(\log_{10}\)）<input id="sw" type="range" min="-130" max="130" value="0" step="1"></label>
  <span class="val" id="vw">0</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3a5a4a"></i>説明されていない</span>
  <span><i class="swatch" style="background:#8a6a2a"></i>説明の候補がある</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>窓（幅 40 桁）</span>
</div>
</div>

<h2><span class="n">05</span>いくつあって、いくつ説明されているか</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>枠組み</th><th class="mid">個数</th><th class="mid">内訳</th></tr></thead>
<tbody>
<tr class="hi"><th>標準模型（ニュートリノ質量を除く）</th><td class="mid">\(19\)</td><td class="mid">次元を持つのは \(\mu^2\)（＝ヒッグスの \(v\)）<strong>1 個だけ</strong></td></tr>
<tr><th>ニュートリノの質量と混合</th><td class="mid">\(7\)</td><td class="mid">3 質量 ＋ 3 角 ＋ 1 位相</td></tr>
<tr class="hi"><th>\(\Lambda\)CDM の基本パラメータ</th><td class="mid">\(6\)</td><td class="mid"><strong>6 個すべてが無次元</strong></td></tr>
<tr><th>合計</th><td class="mid"><strong>\(32\)</strong></td><td class="mid">\(\times5.37=\mathbf{171.7}\) ビット</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">05節の結論</p>
<p style="margin:6px 0 0"><strong>標準模型のラグランジアンで次元を持つ定数は \(\mu^2\) ただ一つ</strong>です。残りは全部が無次元 ── そして \(\Lambda\)CDM の 6 個も全部が無次元。<br>
── <em>現代物理はすでに、パラメータを物理の列に書いています。</em><br>
そして第一原理から導かれているものは<strong>ほぼゼロ</strong> ── <strong>171.7 ビットが説明されていません。</strong></p>
</div>

<h2><span class="n">06</span>手続きを、自分に当てる</h2>

<p>ここで一つ、<em>やってみたくなること</em>があります。いま出した <strong>171.7 ビット</strong>と、第2回の「宇宙の全歴史 \(=140.24\) 対数ステップ」── なんとなく似た桁に見えます。何か意味があるのでしょうか。</p>

<div class="calc">
<span class="tag">第19回の手続きに掛ける</span>
$$|171.7-140.24|=31.5\qquad\text{相対差 }\mathbf{22\ \text{パーセント}}$$
<p class="lbl">「一致した」と言うには ±5 パーセント以内が要る → <strong>命中していない。驚きは 0 ビット</strong></p>
</div>

<p>しかも<em>仮に近かったとしても</em>、驚きは小さいものでした ── パラメータの個数は 15〜30 個、1 個の値段は 5〜6 ビットがもっともらしいので、積の事前範囲は 75〜180（幅 105）。±5 パーセント（幅 14）に落ちる驚きは <strong>2.9 ビット</strong>、<em>偶然の帯の下端</em>です。</p>

<div class="keybox">
<p class="lbl">06節の結論</p>
<p style="margin:6px 0 0"><strong>これが、手続きを持っていることの値打ちです。</strong><br>
「似ている」という印象を、<em>その場で数字にして棄却できる</em>。<br>
── 第36回で「偶然の帯は選択効果」と書きましたが、<strong>選択の網に掛からないものは、こうやって落ちていきます。</strong></p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p style="margin:0 0 10px"><strong>① 05節のパラメータの数え方には、複数の流儀があります。</strong> 標準模型の 19 個は<em>ニュートリノ質量を含めない標準的な数え方</em>で、含めれば 26〜28 個（マヨラナ位相を数えるかで変わります）。\(\theta_{\rm QCD}\) を数えるかどうかでも変わります ── <strong>「32」は一つの数え方の結果</strong>で、20 台後半から 30 台前半で動きます。</p>
<p style="margin:0 0 10px"><strong>② 「171.7 ビットが説明されていない」の 5.37 ビットは、第5回の値段です。</strong> あれは \(N=1701\) という特定のデータ点数から出た数で、<em>パラメータ 1 個の「値段」に普遍的な値があるわけではありません</em> ── 本質は「32 個がほぼ全部未説明」という構造のほうで、<strong>171.7 という数字の有効数字に意味はありません</strong>（第39回⑤と同じ注意）。</p>
<p style="margin:0 0 10px"><strong>③ 02節の「\(\alpha\) は固定できない」は、SI の設計についての言い方です。</strong> \(e\)、\(\hbar\)、\(c\) を固定すると \(\varepsilon_0\)（および \(\mu_0\)）が測定量になり、その不確かさは \(\alpha\) の不確かさで決まります ── <em>「無次元量は法令で決められない」という言い方は本シリーズの表現</em>で、より正確には<strong>「単位の定義は無次元量を決めない」</strong>です。</p>
<p style="margin:0 0 10px"><strong>④ 03節の「基本定数はいくつか」は、いまも意見が分かれる問いです。</strong> Duff、Okun、Veneziano がそれぞれ 0 個、3 個、2 個を主張した 2002 年の鼎談が有名で、<em>決着はしていません</em> ── 本稿が採ったのは「どの立場でも物理は無次元側にある」という、争点にならない部分だけです。</p>
<p style="margin:0"><strong>⑤ 04節の「説明されていない」は、第一原理からの導出が無いという意味です。</strong> 多くの量には<em>部分的な理解や、模型の中での関係</em>があります（たとえば \(m_p/m_e\) は QCD と電弱理論から原理的には計算できるはずの量です）── <strong>「まったく何も分かっていない」という意味ではありません</strong>。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>2019 年の SI は、何を固定して単位を定義したか。
<details><summary>答えを見る</summary><div class="ans"><strong>七つの定数の値を厳密に固定しました</strong> ── \(\Delta\nu_{\rm Cs}\)、\(c\)、\(h\)、\(e\)、\(k_B\)、\(N_A\)、\(K_{\rm cd}\)。<em>キログラム原器は廃止され、質量は \(h\) から作られます</em> ── <strong>次元付きの量が帳簿であることの、国際的な公式宣言</strong>です。</div></details></li>

<li>\(e\)、\(\hbar\)、\(c\) が固定されたのに、なぜ \(\alpha\) は決まらないのか。
<details><summary>答えを見る</summary><div class="ans">\(\varepsilon_0\) が<strong>測定量になった</strong>からです。\(\alpha=e^2/4\pi\varepsilon_0\hbar c\) の不確かさは、そのまま \(\varepsilon_0\) の不確かさになります ── <em>単位の定義は、無次元量を決めません</em>。\(c\) は決められて \(\alpha\) は決められない、<strong>これが第3回の線のいちばん鮮明な形</strong>です。</div></details></li>

<li>標準模型のラグランジアンで、次元を持つ定数はいくつか。
<details><summary>答えを見る</summary><div class="ans"><strong>\(\mu^2\) ただ一つ</strong>（ヒッグスの質量項、\(v\) を決めるもの）です。残りの結合定数と湯川結合はすべて無次元 ── <em>現代物理はすでに、パラメータを物理の列に書いています</em>。\(\Lambda\)CDM の基本 6 個も全部が無次元です。</div></details></li>

<li>171.7 ビットと 140.24 対数ステップは一致しているか。
<details><summary>答えを見る</summary><div class="ans"><strong>していません</strong> ── 相対差 22 パーセント。「一致」と言うには ±5 パーセント以内が要るので、<em>命中しておらず驚きは 0 ビット</em>です。仮に近くても驚きは 2.9 ビットで、偶然の帯の下端でした ── <strong>手続きがあると、印象をその場で棄却できます。</strong></div></details></li>

<li>（やや難）無次元量の地図の幅は何ビットか。
<details><summary>答えを見る</summary><div class="ans">\(3.1\times10^{122}\) から \(1.13\times10^{-123}\) まで、<strong>815 ビット</strong>です。<em>そしてそのすべてが同じ列（ウェイト 0）にあり、共形変換はどれ一つ動かせません</em> ── だからこそ、この列が判定の土俵になります。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　世界の度量衡が、同じ場所に線を引いていた</h2>
<p>2019 年 5 月 20 日から、SI は<strong>七つの定数の値を厳密に固定して</strong>単位を定義しています ── \(\Delta\nu_{\rm Cs}\)、\(c\)、\(h\)、\(e\)、\(k_B\)、\(N_A\)、\(K_{\rm cd}\)。<em>キログラム原器は廃止され、質量は \(h\) から作られます</em>。これは<strong>次元付きの量が帳簿であることの、国際的な公式宣言</strong>でした ── 第3回でこのシリーズが手で引いた線を、世界の度量衡が同じ場所に引いていたのです。</p>
<p>ところが <strong>\(\alpha\) は固定できませんでした</strong>。\(e\)、\(\hbar\)、\(c\) を固定すると \(\varepsilon_0\) が測定量になり、\(1/\alpha=137.035999177(21)\) はいまも測るしかありません ── <em>無次元だから、法令では決められない</em>。<strong>\(c\) は決められて \(\alpha\) は決められない ── これが第3回の線の、いちばん鮮明な形です。</strong></p>
<p>無次元量の地図を描くと、\(3.1\times10^{122}\)（第24回の \(N\)）から \(1.13\times10^{-123}\)（宇宙定数）まで <strong>815 ビットの幅</strong>があり、そのすべてが同じ列にあります。数えると、標準模型 19 ＋ ニュートリノ 7 ＋ \(\Lambda\)CDM 6 で <strong>32 個</strong>。うち<strong>次元を持つのは \(\mu^2\) ただ一つ</strong>で、第一原理から導かれているものは<em>ほぼゼロ</em> ── <strong>171.7 ビットが説明されていません</strong>。</p>
<p>最後に、手続きを自分に当てました。171.7 ビットと第2回の 140.24 対数ステップが似た桁に見えますが、<strong>相対差は 22 パーセント。命中しておらず、驚きは 0 ビット</strong>です。仮に近くても 2.9 ビット、偶然の帯の下端でした ── <em>「似ている」という印象を、その場で数字にして棄却できる</em>。<strong>これが手続きを持っていることの値打ちです。</strong></p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第48回</span>
第5回の天秤は、<strong>短さ</strong>（パラメータの値段）と<strong>当てはまり</strong>（\(\Delta\chi^2\)）の二つを測りました。ところが物理学者はしばしば三つ目のことを言います ── 「<em>美しい</em>」。次回はそれを正面から扱います：<strong>美しさは三つ目の通貨なのか、それとも前の二つの言い換えなのか。</strong> このシリーズが 47 回で使ってきた道具で、<em>美しさそのものを測ろう</em>とします ── そして<strong>測れなかったものが何かも、正直に書きます。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sw=document.getElementById('sw'), vw=document.getElementById('vw'), ro=document.getElementById('ro');
  var X0=60, X1=690, YB=190;
  var L0=-130, L1=130, W=20;   // 窓は片側 20 桁

  var D=[
    ['ρ_Λ/ρ_P', -123, 0],
    ['α_G', -38.2, 0],
    ['v/M_P', -16.7, 0],
    ['α', -2.14, 0],
    ['Ω_Λ', -0.16, 0],
    ['n_s', -0.016, 1],
    ['m_p/m_e', 3.26, 0],
    ['N（第24回）', 122.5, 1]
  ];

  function px(l){ return X0+(l-L0)/(L1-L0)*(X1-X0); }

  function draw(){
    var wc=parseInt(sw.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.fillStyle='#f0eef3';
    g.fillRect(px(wc-W), YB-92, px(wc+W)-px(wc-W), 184);

    g.strokeStyle='#cdc8d2'; g.lineWidth=1.6;
    g.beginPath(); g.moveTo(X0,YB); g.lineTo(X1,YB); g.stroke();

    g.textAlign='center'; g.fillStyle='#9c96a4';
    for(var t=L0;t<=L1;t+=40){
      var x=px(t);
      g.strokeStyle='#e6e2ea'; g.lineWidth=1;
      g.beginPath(); g.moveTo(x,YB-6); g.lineTo(x,YB+6); g.stroke();
      g.fillText('10^'+t, x, YB+24);
    }

    var cnt=0;
    for(var i=0;i<D.length;i++){
      var l=D[i][1], kind=D[i][2], x2=px(l);
      var inw = (l>=wc-W && l<=wc+W);
      if(inw) cnt++;
      var up = (i%2===0);
      var y = up ? YB-30-(i%4)*17 : YB+38+(i%4)*17;
      g.strokeStyle = inw ? (kind===1?'#8a6a2a':'#3a5a4a') : '#ddd8e2';
      g.lineWidth=1.4;
      g.beginPath(); g.moveTo(x2,YB); g.lineTo(x2,y+(up?6:-6)); g.stroke();
      g.fillStyle = inw ? (kind===1?'#8a6a2a':'#3a5a4a') : '#c4bece';
      g.beginPath(); g.arc(x2,YB,4.2,0,6.29); g.fill();
      g.textAlign='center';
      g.fillText(D[i][0], x2, y);
    }

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('無次元量（対数目盛り）── 全体で 815 ビットの幅', (X0+X1)/2, YB+120);

    vw.textContent=String(wc);
    ro.textContent='窓の中心 10^'+wc+'（幅 ±20 桁）　→　この窓に入るのは '+cnt+' 個／8 個'+
      (cnt===0?'　★ ここには何も無い ── 地図はすかすかである':'')+
      (Math.abs(wc)<5?'　★ 1 のまわり ── α、Ω_Λ、n_s が集まる':'');
  }
  sw.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-47-map.html', acc='#3a5a4a', ops='#8a6a2a',
      title='無次元量の地図 ── わかる c·t=一定 第47回（第VI部）',
      ep='第 47 回 ／ 第 VI 部・手続きを検査する',
      eyebrow='\\(c\\) は決められて、\\(\\alpha\\) は決められない',
      h1='世界の度量衡が、<br>同じ場所に線を引いていた',
      sub='2019 年、SI は七つの定数を固定して単位を定義し直しました ── キログラム原器は廃止。<br><em>次元付きが帳簿であることの、国際的な公式宣言です。</em>',
      byline_l='必要な道具：第3回の判定、第5回の天秤、第16回のウェイト表、第19回の目盛り',
      byline_r='32 個のパラメータ、171.7 ビットが未説明',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第47回（第 VI 部の 2 回目）、物理好きの高校生・大学生向け読み物です。2019 年の SI 改定、標準模型と \\(\\Lambda\\)CDM のパラメータの数え方、無次元量の一覧はいずれも標準的な内容で、本稿に新しい主張はありません ── 数値は kenshou/calc51.py で計算しています。<strong>05節のパラメータの数え方には複数の流儀があります</strong> ── 標準模型の 19 個はニュートリノ質量を含めない数え方で、含めれば 26〜28 個（マヨラナ位相を数えるかで変わります）、\\(\\theta_{\\rm QCD}\\) を数えるかでも変わります ── <em>「32」は一つの数え方の結果</em>です。<strong>「171.7 ビット」の 5.37 ビットは第5回の値段（\\(N=1701\\) から出た数）で、パラメータ 1 個の値段に普遍的な値があるわけではありません</strong> ── 本質は「32 個がほぼ全部未説明」という構造で、有効数字に意味はありません。<strong>02節の「\\(\\alpha\\) は固定できない」は SI の設計についての言い方</strong>で、より正確には「単位の定義は無次元量を決めない」です（\\(e,\\hbar,c\\) の固定により \\(\\varepsilon_0\\) が測定量になり、その不確かさが \\(\\alpha\\) の不確かさで決まります）。<strong>03節の「基本定数はいくつか」はいまも意見が分かれる問い</strong>で（Duff・Okun・Veneziano が 0 個・3 個・2 個を主張した 2002 年の鼎談が有名）、本稿は争点にならない部分だけを採りました。<strong>04節の「説明されていない」は第一原理からの導出が無いという意味</strong>で、多くの量には部分的な理解や模型内での関係があります ── <em>「まったく何も分かっていない」という意味ではありません</em>。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで窓を動かすと、地図がすかすかであることが見えます。「答えを見る」で解答が開きます。')
