# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第28回と第29回で「定数が変わる」型の理論を二つ扱いました。今回は<strong>実際に測っているほう</strong>を見ます ── 原子時計、オクロ天然原子炉、クエーサー吸収線。三つはまったく違う物理を使いますが、<em>骨格は同じ一行</em>でした。そして最後に一つの数が出ます ── <strong>私たちが \(\alpha\) を 26 ビットで知っているのは、宇宙の対数的な歴史の 0.1% だけ。</strong></p>

<h2><span class="n">01</span>三つの測り方</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>測り方</th><th class="mid">いつの \(\alpha\) か</th><th class="mid">\(|\Delta\alpha/\alpha|\) 上限</th><th class="mid">縛ったビット</th></tr></thead>
<tbody>
<tr class="hi"><th>原子時計（Yb⁺ E3 対 Sr）</th><td class="mid">今日（変化率）</td><td class="mid">\(1.4\times10^{-8}\)</td><td class="mid"><strong>26.1 bit</strong></td></tr>
<tr class="hi"><th>オクロ天然原子炉</th><td class="mid">18 億年前</td><td class="mid">\(1.1\times10^{-8}\)</td><td class="mid"><strong>26.4 bit</strong></td></tr>
<tr><th>クエーサー吸収線</th><td class="mid">\(z\sim2\)（105 億年前）</td><td class="mid">\(1.0\times10^{-5}\)</td><td class="mid">16.6 bit</td></tr>
<tr><th>CMB</th><td class="mid">\(z=1100\)</td><td class="mid">\(4.0\times10^{-3}\)</td><td class="mid">8.0 bit</td></tr>
<tr><th>元素合成</th><td class="mid">\(t=1\) 秒</td><td class="mid">\(1.0\times10^{-2}\)</td><td class="mid">6.6 bit</td></tr>
</tbody>
</table>
</div>

<p>実験室で測った \(\alpha\) 自体は、もっと精密です ── \(\alpha^{-1}=137.035999177(21)\)、相対精度 \(1.6\times10^{-10}\)、<strong>32.5 ビット</strong>。ただしそれは「今日の値」であって、「動いていないこと」の証拠ではありません。</p>

<h2><span class="n">02</span>核心 ── 三つとも、同じ一行でできている</h2>

<p>まったく違う物理に見えて、骨格は共通です。</p>

<div class="calc">
<span class="tag">すべての測定に共通する形</span>
$$(\text{観測量の変化})=K\times\frac{\Delta\alpha}{\alpha}\qquad\Longrightarrow\qquad \left|\frac{\Delta\alpha}{\alpha}\right|<\frac{\text{観測精度}}{K}$$
<p class="lbl">\(K\) は<strong>増幅率</strong> ── \(\alpha\) のわずかな変化を、観測量の大きな変化に翻訳する係数</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>測り方</th><th class="mid">増幅率 \(K\)</th><th class="mid">観測精度</th><th class="mid">何が増幅しているか</th></tr></thead>
<tbody>
<tr><th>原子時計</th><td class="mid">7</td><td class="mid">\(10^{-18}\)</td><td class="mid">二つの遷移の \(\alpha\) 感度の差</td></tr>
<tr class="hi"><th>オクロ</th><td class="mid"><strong>\(10^{7}\)</strong></td><td class="mid">\(2\times10^{-2}\)</td><td class="mid"><strong>MeV 級の量どうしの差が 97.3 meV</strong></td></tr>
<tr><th>クエーサー</th><td class="mid">0.3</td><td class="mid">\(3\times10^{-6}\)</td><td class="mid">多数の線を束ねた統計</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>オクロが強いのは、測定が精密だからではありません。</strong><br>
測定精度は 2%（原子時計の \(10^{16}\) 倍も粗い）── <em>それでも同じ上限が出るのは、増幅率が \(10^7\) あるから</em>。<br>
<strong>精度を上げるより、増幅する場所を見つけるほうが効く。</strong></p>
</div>

<h2><span class="n">03</span>オクロの増幅は、どこから来るのか</h2>

<p>18 億年前、ガボンのオクロで<em>天然のウラン鉱床が自発的に核分裂連鎖反応を起こしました</em>。その「灰」が残っています。鍵になるのは \(^{149}\mathrm{Sm}\) の中性子捕獲共鳴です。</p>

<div class="calc">
<span class="tag">なぜ \(10^7\) 倍になるのか</span>
<p class="lbl">共鳴エネルギー \(E_r=97.3\) meV は、<strong>MeV 級の量どうしの差</strong>として現れる</p>
$$E_r\ \sim\ (\text{核の結合エネルギー})-(\text{クーロンエネルギー})\ \sim\ 10^6\ \mathrm{eV}-10^6\ \mathrm{eV}$$
<p class="lbl">\(\alpha\) が動くとクーロン項だけがずれるので</p>
$$\frac{\Delta E_r}{E_r}\ \sim\ \frac{10^6\ \mathrm{eV}}{0.0973\ \mathrm{eV}}\times\frac{\Delta\alpha}{\alpha}\ \simeq\ 10^{7}\times\frac{\Delta\alpha}{\alpha}$$
</div>

<p>これは第19回で「一致」を測ったときと<em>ちょうど逆の構図</em>です。あちらでは「大きな数どうしの差が小さいこと」が驚きでした。ここでは<strong>その小ささが、測定装置の増幅器として使われています</strong>。<em>桁の消し合いは、謎にもなれば、道具にもなる。</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>対数ステップのどこに、データがあるか</h2>

<p>第2回で、宇宙の全歴史は <strong>140.24 対数ステップ</strong>だと数えました。この物差しの上に、五つの測定を置きます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>測り方</th><th class="mid">ステップ</th><th class="mid">縛ったビット</th></tr></thead>
<tbody>
<tr><th>元素合成</th><td class="mid">99.63</td><td class="mid">6.6</td></tr>
<tr><th>CMB</th><td class="mid">129.74</td><td class="mid">8.0</td></tr>
<tr><th>クエーサー吸収線</th><td class="mid">138.81</td><td class="mid">16.6</td></tr>
<tr class="hi"><th>オクロ</th><td class="mid">140.10</td><td class="mid"><strong>26.4</strong></td></tr>
<tr class="hi"><th>原子時計</th><td class="mid">140.24</td><td class="mid"><strong>26.1</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0">データが存在するのは ステップ 99.63 〜 140.24 ── <strong>全歴史の 29%</strong>。<br>
残る <strong>71% には \(\alpha\) のデータが一つも存在しません</strong>。<br>
そして 20 ビット以上の精度があるのは ステップ 140.10 〜 140.24 ── <em>全歴史の 0.1%</em>。</p>
</div>

<div class="fig">
<p class="cap">図：横軸は対数ステップ（宇宙の全歴史 140.24）、縦軸は \(\alpha\) について縛られたビット数。<strong>灰色はデータが存在しない領域</strong>。ツマミで時代を動かすと、その時代に何ビット知っているかが読めます ── <em>右端に全部が集まっています</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>いつの \(\alpha\) を知りたいか（対数ステップ）<input id="ss" type="range" min="0" max="1403" value="1403" step="1"></label>
  <span class="val" id="vs">140.3（今日）</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6a2a4a"></i>縛られたビット数</span>
  <span><i class="swatch" style="background:#3a6a2a"></i>測定</span>
  <span><i class="swatch" style="background:#cfc6cc"></i>データが存在しない</span>
</div>
</div>

<h2><span class="n">05</span>空白の期間</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>空白</th><th class="mid">ステップ</th><th class="mid">長さ</th><th class="mid">なぜ測れないか</th></tr></thead>
<tbody>
<tr class="hi"><th>元素合成 → CMB</th><td class="mid">99.6 → 129.7</td><td class="mid"><strong>30.1 ステップ</strong></td><td class="mid">プラズマで、光が届かない</td></tr>
<tr><th>CMB → クエーサー</th><td class="mid">129.7 → 138.8</td><td class="mid">9.1 ステップ</td><td class="mid">暗黒時代。光る天体がまだ無い</td></tr>
</tbody>
</table>
</div>

<p><strong>データは三つの島に分かれています</strong> ── 元素合成、CMB、そして \(z\lesssim4\) 以降。そのあいだは、理論による内挿でしかありません。第28回で「相転移型 VSL は元素合成より前に隠れれば排除されない」と書きましたが、<em>じつは元素合成と CMB のあいだにも 30 ステップの隠れ場所があります</em>。</p>

<h2><span class="n">06</span>種明かし ── 測定は、このシリーズの道具が触れられない場所にある</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">中身</th><th class="mid">ウェイト</th></tr></thead>
<tbody>
<tr><th>増幅率 \(K\)</th><td class="mid">比の比</td><td class="mid">\(0\)</td></tr>
<tr><th>\(\Delta\alpha/\alpha\)</th><td class="mid">無次元量の変化率</td><td class="mid">\(0\)</td></tr>
<tr class="hi"><th>縛ったビット数</th><td class="mid">対数を取った比</td><td class="mid"><strong>\(0\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">06節の結論</p>
<p style="margin:6px 0 0">定数の測定は、まるごと第16回のウェイトの地図の<strong>「ゼロの列」</strong>にあります。<br>
── <em>このシリーズの道具が一切触れられない場所。だからこそ、審判になれる。</em></p>
</div>

<p>第13回で「共形変換は大きさにしか触れない」と道具の限界を測りました。今回はその裏返しです ── <strong>審判の側は、まるごと道具の外にいます</strong>。だから第28回で VSL を、第29回で MOND を、そして第3回で c·t=一定 自身を判定できました。<em>判定できる理由は、判定する物差しが動かないからです。</em></p>

<h2><span class="n">07</span>おまけ ── 人間原理より、観測のほうが強い</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>もし \(\alpha\) が動いたら壊れるもの</th><th class="mid">必要な \(|\Delta\alpha/\alpha|\)</th></tr></thead>
<tbody>
<tr><th>炭素の 7.65 MeV 共鳴（三重α過程）が消える</th><td class="mid">\(4\times10^{-2}\)</td></tr>
<tr><th>\(^4\)He 収量が観測とずれる</th><td class="mid">\(1\times10^{-2}\)</td></tr>
<tr><th>再結合の時期がずれる</th><td class="mid">\(4\times10^{-3}\)</td></tr>
<tr class="hi"><th>実際の観測上限</th><td class="mid"><strong>\(1\times10^{-8}\)</strong></td></tr>
</tbody>
</table>
</div>

<p>「\(\alpha\) がこの値でなければ生命は存在できなかった」という論法（人間原理）が要求するのは、せいぜい <strong>4%</strong> の精度です。ところが実際の観測上限は \(10^{-8}\) ── <em>6 桁きつい</em>。<strong>\(\alpha\) が動いていないことは、人間原理が説明できる範囲をはるかに超えて確かめられています。</strong></p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 増幅率 \(K\) は桁の目安です。</strong> オクロの \(10^7\) は「共鳴エネルギーが MeV 級の量の差である」ことからの見積もりで、正確な値は核構造の計算に依存し、文献では \(10^7\)〜\(10^8\) の幅があります。原子時計の \(\Delta K\simeq7\) も遷移の組み合わせによります。</p>
<p style="margin:0 0 10px"><strong>② オクロの解析には核物理の仮定が入ります。</strong> 反応炉の温度、中性子スペクトル、\(\alpha\) 以外の定数（\(m_q/\Lambda_{\rm QCD}\) など）の同時変化の扱いで、上限は数倍動きます ── <em>\(10^{-8}\) は代表値です</em>。</p>
<p style="margin:0 0 10px"><strong>③ クエーサー吸収線は論争が続いています</strong>（第28回②と同じ注意）。Webb らは有意な変化を主張し、Keck と VLT で符号が食い違います。本稿の \(10^{-5}\) は保守的な上限で、単一の測定値ではありません。</p>
<p style="margin:0 0 10px"><strong>④ 「縛ったビット数」は \(-\log_2|\Delta\alpha/\alpha|\) と定義した本稿の量です。</strong> 「\(\alpha\) の二進表記が上位何桁まで動いていないか」という読み方で、第19回の驚きのビット数とは<em>別の量</em>です（あちらは事前範囲に対する比）。混同しないでください。</p>
<p style="margin:0 0 10px"><strong>⑤ 04節の「全歴史の 29%」は、対数ステップで測った割合です。</strong> 普通の時間で測れば、データがあるのは 99.99999...% になります ── <em>対数で測るからこそ「71% が空白」に見える</em>。どちらが正しいかではなく、<strong>何を等間隔と見なすかの選択</strong>です（第2回・第20回と同じ）。</p>
<p style="margin:0"><strong>⑥ 07節の \(4\times10^{-2}\) は、三重α過程の共鳴に関する代表的な見積もりです。</strong> 微調整の許容幅は計算方法に依存し、文献では 0.5%〜4% と幅があります。<em>結論（観測のほうが数桁きつい）は、この幅では変わりません。</em></p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>三つの測定に共通する形を書け。
<details><summary>答えを見る</summary><div class="ans">（観測量の変化）\(=K\times\Delta\alpha/\alpha\)、したがって \(|\Delta\alpha/\alpha|<\)（観測精度）\(/K\)。<strong>\(K\) は増幅率</strong>で、これが大きいほど同じ測定精度から強い上限が出ます。</div></details></li>

<li>オクロの増幅率が \(10^7\) になる理由を述べよ。
<details><summary>答えを見る</summary><div class="ans">\(^{149}\mathrm{Sm}\) の共鳴エネルギー 97.3 meV が、<strong>MeV 級の量どうしの差</strong>として現れるから。\(\alpha\) が動くとクーロン項だけがずれるので、\(\Delta E_r/E_r\sim(10^6\,\mathrm{eV}/0.0973\,\mathrm{eV})\times\Delta\alpha/\alpha\simeq10^7\times\Delta\alpha/\alpha\)。<em>桁の消し合いが、測定装置の増幅器になっています。</em></div></details></li>

<li>オクロの測定精度は 2% と粗い。それでも原子時計と同じ上限が出るのはなぜか。
<details><summary>答えを見る</summary><div class="ans">増幅率が \(10^7\) あるから。\(2\times10^{-2}/10^7=2\times10^{-9}\)。<strong>精度を上げるより、増幅する場所を見つけるほうが効く</strong>という例です。</div></details></li>

<li>\(\alpha\) のデータがあるのは、宇宙の対数的な歴史の何%か。
<details><summary>答えを見る</summary><div class="ans">元素合成（ステップ 99.63）から今日（140.24）までなので \((140.24-99.63)/140.24=\) <strong>29%</strong>。残る 71% にはデータが一つもありません。20 ビット以上の精度があるのは 0.1% だけです。</div></details></li>

<li>（やや難）定数の測定が、このシリーズの判定の審判になれるのはなぜか。
<details><summary>答えを見る</summary><div class="ans">増幅率も \(\Delta\alpha/\alpha\) も縛ったビット数も、<strong>すべて無次元＝ウェイト 0</strong> だから ── 第16回のウェイトの地図でいうゼロの列にあり、<em>このシリーズの道具（共形変換）が一切触れられません</em>。動かせない物差しだからこそ、VSL（第28回）も MOND（第29回）も c·t=一定 自身（第3回）も判定できます。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　増幅する場所を見つけた者が勝つ</h2>
<p>三つの測り方 ── 原子時計（今日、26.1 ビット）、オクロ天然原子炉（18 億年前、26.4 ビット）、クエーサー吸収線（105 億年前、16.6 ビット）。まったく違う物理に見えて、骨格は同じ一行でした ── <strong>（観測量の変化）\(=K\times\Delta\alpha/\alpha\)</strong>。</p>
<p>核心は増幅率 \(K\) です。<strong>オクロの測定精度は 2%、原子時計の \(10^{16}\) 倍も粗い</strong>のに同じ上限が出る ── <em>増幅率が \(10^7\) あるから</em>です。\(^{149}\mathrm{Sm}\) の 97.3 meV という共鳴が、MeV 級の量どうしの差として現れるので、\(\alpha\) のわずかな変化が桁で効く。<strong>桁の消し合いは、謎にもなれば、道具にもなる</strong> ── 第19回で「驚き」として測ったものが、ここでは増幅器でした。</p>
<p>対数ステップの上に置き直すと、風景が変わります。データが存在するのは全 140.24 ステップのうち <strong>29%</strong>、20 ビット以上の精度があるのは <strong>0.1%</strong>。しかも三つの島に分かれていて、元素合成と CMB のあいだには <strong>30 ステップの空白</strong>があります。<em>私たちは \(\alpha\) の不変性を、思っているより狭い窓でしか確かめていません。</em></p>
<p>そして種明かし ── 増幅率も \(\Delta\alpha/\alpha\) も縛ったビット数も、すべてウェイト 0。<strong>定数の測定は、まるごとこのシリーズの道具が触れられない場所にあります。</strong> 第13回で測った「共形変換は大きさにしか触れない」の、ちょうど裏返しです ── <em>審判が動かないからこそ、判定ができる</em>。おまけに、人間原理が要求する精度は 4% で、実際の観測上限はその <strong>6 桁きつい</strong> \(10^{-8}\) でした。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第31回</span>
第 IV 部の後半は、<strong>共形変換そのものを土台に据えた理論</strong>を扱います。最初はペンローズの<strong>共形サイクリック宇宙論（CCC）</strong>です。第6回で「ワイル曲率仮説 ── 宇宙は \(C=0\) で始まった」を使用率の言葉で書き直しました。CCC はその先へ行きます ── <em>宇宙の終わり（質量がすべて消えた遠い未来）と、次の宇宙の始まりを、共形変換で貼り合わせる</em>。このシリーズの道具が<strong>理論の中心に据えられたとき、何が起きるのか</strong>。そして貼り合わせに必要な条件を、第11回の「光は共形不変」と第6回の「使用率」で数えます。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=34, Y1=310;
  var NSTEP=140.24, SB=99.63;
  var P=[[99.63,6.6,'元素合成'],[129.74,8.0,'CMB'],[138.81,16.6,'クエーサー'],
         [140.10,26.4,'オクロ'],[140.24,26.1,'原子時計']];
  var xmin=0, xmax=145, ymin=0, ymax=34;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function bitsAt(s){
    if(s<SB) return 0;
    var b=0;
    for(var i=0;i<P.length;i++){ if(s>=P[i][0]) b=P[i][1]; }
    return b;
  }

  function draw(){
    var s=parseInt(ss.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    // データが存在しない領域
    g.fillStyle='#f2eef1';
    g.fillRect(X0, Y0, px(SB)-X0, Y1-Y0);
    g.fillStyle='#a89aa2'; g.textAlign='center';
    g.fillText('α のデータが一つも無い（全歴史の 71%）', (X0+px(SB))/2, Y0+18);

    g.textAlign='right';
    for(var e=0;e<=30;e+=10){
      var y=py(e);
      g.strokeStyle=(e===0?'#ddd2da':'#f5f0f4'); g.lineWidth=(e===0?1.5:1);
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a1959d'; g.fillText(e+' bit', X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=140;q+=20){
      var x=px(q);
      g.strokeStyle='#faf7f9'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a1959d'; g.fillText(String(q), x, Y1+16);
    }
    g.strokeStyle='#d6c8d2'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // 階段（塗り）
    g.fillStyle='rgba(106,42,74,0.16)';
    g.beginPath();
    g.moveTo(px(SB),py(0));
    for(var i=0;i<P.length;i++){
      g.lineTo(px(P[i][0]),py(i===0?0:P[i-1][1]));
      g.lineTo(px(P[i][0]),py(P[i][1]));
      var nx = (i+1<P.length)? P[i+1][0] : xmax;
      g.lineTo(px(nx),py(P[i][1]));
    }
    g.lineTo(px(xmax),py(0));
    g.closePath(); g.fill();

    // 階段（線）
    g.strokeStyle='#6a2a4a'; g.lineWidth=3;
    g.beginPath();
    g.moveTo(px(SB),py(0));
    for(var i=0;i<P.length;i++){
      g.lineTo(px(P[i][0]),py(i===0?0:P[i-1][1]));
      g.lineTo(px(P[i][0]),py(P[i][1]));
      var nx = (i+1<P.length)? P[i+1][0] : xmax;
      g.lineTo(px(nx),py(P[i][1]));
    }
    g.stroke();

    // 測定点
    for(var i=0;i<P.length;i++){
      g.fillStyle='#3a6a2a';
      g.beginPath(); g.arc(px(P[i][0]),py(P[i][1]),5,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=1.6;
      g.beginPath(); g.arc(px(P[i][0]),py(P[i][1]),5,0,6.2832); g.stroke();
      g.fillStyle='#2f5a22'; g.textAlign=(i>=3?'right':'left');
      g.fillText(P[i][2], px(P[i][0])+(i>=3?-10:10), py(P[i][1])-9-(i===4?14:0));
    }

    // カーソル
    g.strokeStyle='#8a6a7a'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(s),Y0); g.lineTo(px(s),Y1); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#8a7a84'; g.textAlign='center';
    g.fillText('対数ステップ  ln(t / t_P)　── 宇宙の全歴史は 140.24', (X0+X1)/2, Y1+36);

    var b=bitsAt(s);
    var t=Math.exp(s)*5.391247e-44;
    var tl = t<3.156e7 ? t.toExponential(2)+' 秒' : (t/3.156e16).toPrecision(3)+' Gyr';
    vs.textContent=s.toFixed(1)+(s>139.9?'（今日）':'');
    ro.textContent='ステップ '+s.toFixed(1)+'（宇宙年齢 '+tl+'）　→　'+
      (b>0 ? 'α について '+b.toFixed(1)+' ビット知っている（|Δα/α| < '+Math.pow(2,-b).toExponential(1)+'）'
           : '★ この時代の α について、私たちは 1 ビットも知らない');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-30-measure.html', acc='#6a2a4a', ops='#3a6a2a',
      title='変わる定数を、実際に測る ── わかる c·t=一定 第30回',
      ep='第 30 回 ／ 第 IV 部・測っているほうを見る',
      eyebrow='精度を上げるより、増幅する場所を見つけるほうが効きます',
      h1='変わる定数を、<br>実際に測る',
      sub='原子時計、オクロ天然原子炉、クエーサー吸収線 ── 三つの物理は違うのに、骨格は同じ一行でした。<br><em>そして \\(\\alpha\\) を 26 ビットで知っているのは、対数的な歴史の 0.1% だけ。</em>',
      byline_l='必要な道具：割り算、対数、増幅率という考え方',
      byline_r='\\(|\\Delta\\alpha/\\alpha|<\\)（精度）\\(/K\\)',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第30回、物理好きの高校生・大学生向け読み物です。原子時計による \\(|\\dot\\alpha/\\alpha|<1.0(1.1)\\times10^{-18}\\)/yr は Lange et al. (2021, PRL 126, 011102)、オクロ天然原子炉による制約は Shlyakhter (1976) 以来の一連の解析、クエーサー吸収線の多重項法は Webb, Murphy, Flambaum らによります。CODATA 2022 の \\(\\alpha^{-1}=137.035999177(21)\\) は標準値です。<strong>増幅率 \\(K\\) は桁の目安であり</strong>、オクロの \\(10^7\\) は「\\(^{149}\\mathrm{Sm}\\) の 97.3 meV 共鳴が MeV 級の量の差である」ことからの見積もりで、正確な値は核構造の計算に依存し文献では \\(10^7\\)〜\\(10^8\\) の幅があります。<strong>オクロの解析には反応炉温度・中性子スペクトル・\\(\\alpha\\) 以外の定数の同時変化などの仮定が入り、上限は数倍動きます</strong>。<strong>クエーサー吸収線については Webb らが有意な変化を主張した経緯があり、Keck と VLT で符号が食い違うなど論争が続いています</strong> ── 本稿の \\(10^{-5}\\) は保守的にまとめた上限で単一の測定値ではありません。「縛ったビット数」\\(-\\log_2|\\Delta\\alpha/\\alpha|\\) は本稿での定義で、第19回の「驚きのビット数」（事前範囲に対する比）とは<em>別の量</em>です。04節の「全歴史の 29%」は対数ステップで測った割合であり、普通の時間で測ればほぼ 100% になります ── <em>何を等間隔と見なすかの選択</em>です（第2回・第20回）。07節の三重α過程の許容幅 \\(4\\times10^{-2}\\) は代表的な見積もりで、計算方法により 0.5%〜4% の幅がありますが、結論（観測のほうが数桁きつい）は変わりません。対数ステップ 140.24 は \\(\\ln(t_0/t_P)\\) です（第2回）。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルです。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで時代を動かし、その時代に何ビット知っているかが読めます。「答えを見る」で解答が開きます。')
