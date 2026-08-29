# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第 III 部では八つの物差しで宇宙を測りました ── 分散合意、アドレス、驚き、光シート、時間の矢、命令セット、符号、帯域、そして記述長。<strong>並べてみると、同じ数が何度も出てきます。</strong> \(1.5\times10^{-18}\) が三度、\(140\) が四度、\(0.035\) が二度。<em>物差しが違うのに同じ数が出るとき、それは発見なのか、それとも最初から同じものを測っていたのか。</em> 第19回の手続きを、シリーズ自身に当てます。</p>

<h2><span class="n">01</span>\(1.5\times10^{-18}\) は三度出てきた</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>出どころ</th><th class="mid">式</th><th class="mid">値</th></tr></thead>
<tbody>
<tr><th>第6回・使用率</th><td class="mid">\((S/\ln2)/N\)</td><td class="mid">\(1.5132\times10^{-18}\)</td></tr>
<tr><th>第6回・占有率</th><td class="mid">\(\sum A_{BH}/A_H\)</td><td class="mid">\(1.5132\times10^{-18}\)</td></tr>
<tr><th>第21回・時間の矢</th><td class="mid">\(10^{-0.127\times140.24}\)</td><td class="mid">\(1.55\times10^{-18}\)</td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">正体 ── 一行で終わる</span>
<p class="lbl">ホログラフィーの定義そのものから</p>
$$N=\frac{A}{4\ell_P^2\ln2}\qquad\Longrightarrow\qquad \frac{S/\ln2}{N}=\frac{4\ell_P^2 S}{A}=\frac{\sum A_{BH}}{A_H}$$
<p class="lbl">比は 1.000000。ブラックホールが \(S\) を支配する限り、これは<strong>恒等式</strong></p>
</div>

<p>三つ目も独立ではありません ── 第21回の \(0.127\) decade/step は、そもそも \(1.5\times10^{-18}\) に合うように差を取って出した数でした。<strong>三度出てきた \(1.5\times10^{-18}\) は、一つの数です。</strong></p>

<h2><span class="n">02</span>\(140\) は四度出てきた</h2>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>第2回・時計 \(N_t\)</strong><span>\(\ln(t_0/t_P)=140.24\)</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>第20回・対数ステップ数</strong><span>同じ \(\ln(t_0/t_P)\)</span></div></div>
<div class="row"><div class="mk">③</div><div class="txt"><strong>第21回・「140 手のプログラム」</strong><span>同じ</span></div></div>
<div class="row"><div class="mk">④</div><div class="txt"><strong>第21回・\(0.127\) に掛けた 140.24</strong><span>同じ</span></div></div>
<div class="row hi"><div class="mk">◆</div><div class="txt"><strong>独立なのは温度のほうだけ</strong><span>\(N_T=\ln(T_P/T_0)=73.03\)。比 \(N_T/N_t=0.5207\approx1/2\) ── 輻射期 \(T\propto t^{-1/2}\) が対数レンジの大半を占めることの反映</span></div></div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>第 III 部の見出し数字を、全部並べる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">値</th><th class="mid">由来</th></tr></thead>
<tbody>
<tr><th>地平面の容量 \(N\)</th><td class="mid">\(2.956\times10^{122}\) bit</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr><th>容量が増える速さ \(dN/dt\)</th><td class="mid">\(1.358\times10^{105}\) bit/s</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr><th>1ビットあたり演算数 \(\Omega/N\)</th><td class="mid">0.0351</td><td class="mid">\(p\)</td></tr>
<tr><th>使用率</th><td class="mid">\(1.513\times10^{-18}\)</td><td class="mid">\(t_0,\ \ell_P,\ S\)</td></tr>
<tr class="hi"><th>占有率</th><td class="mid">\(1.513\times10^{-18}\)</td><td class="mid"><strong>＝使用率</strong></td></tr>
<tr class="hi"><th>時間の矢</th><td class="mid">\(1.55\times10^{-18}\)</td><td class="mid"><strong>＝使用率</strong></td></tr>
<tr class="hi"><th>冗長度 \(n/k\)</th><td class="mid">\(6.61\times10^{17}\)</td><td class="mid"><strong>＝1/使用率</strong></td></tr>
<tr><th>対数ステップ数</th><td class="mid">140.24</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr><th>温度ステップ数 \(N_T\)</th><td class="mid">73.03</td><td class="mid">\(T_0\)</td></tr>
<tr><th>通信路容量 \(C\)</th><td class="mid">\(6.789\times10^{104}\) bit/s</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr class="hi"><th>\(C\cdot t/N\)</th><td class="mid">1.000000</td><td class="mid"><strong>恒等式</strong></td></tr>
<tr class="hi"><th>\((dN/dt)/C\)</th><td class="mid">2.000000</td><td class="mid"><strong>恒等式</strong></td></tr>
<tr><th>パラメータ 1 個の値段</th><td class="mid">5.37 bit</td><td class="mid">\(N_{\rm data}\)</td></tr>
<tr><th>当てはまりの損</th><td class="mid">153.6 bit</td><td class="mid">\(\Delta\chi^2\)</td></tr>
<tr><th>CMB モード数</th><td class="mid">\(6.255\times10^{6}\)</td><td class="mid">\(l_{\max}\)</td></tr>
<tr><th>1 ビット ↔ 長さ</th><td class="mid">1.96 fm</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr><th>何もしない成分の取り分</th><td class="mid">95.0 %</td><td class="mid">\(\Omega_\Lambda,\ \Omega_{\rm dm}\)</td></tr>
<tr><th>地平線問題の情報量</th><td class="mid">20 KB</td><td class="mid">CMB パッチ数</td></tr>
<tr><th>20 KB の送信時間</th><td class="mid">\(8.55\times10^{-96}\) s</td><td class="mid">\(t_{\rm rec},\ \ell_P\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0">見出し数字 <strong>24 個</strong>。独立な入力 <strong>12 個</strong>（\(t_0,\ \ell_P,\ S,\ p,\ T_0,\ N_{\rm data},\ \Delta\chi^2,\ l_{\max},\ \Omega_\Lambda{+}\Omega_{\rm dm}\), CMB パッチ数, \(t_{\rm rec}\), ネット総量）。<br>
<strong>第 III 部自身の圧縮率は 2.0 倍</strong>。第25回の物差しを自分に当てると、<em>桁ではありませんでした</em>。</p>
</div>

<div class="fig">
<p class="cap">図：見出し数字と、その独立な入力。<strong>同じ色の点は、同じ入力から出た数</strong>です。ツマミで「恒等式で結ばれた数を畳む」と、24 個が何個まで縮むかが見えます</p>
<canvas id="cv" width="720" height="400"></canvas>
<div class="controls">
  <label>恒等式をどこまで畳むか<input id="sl" type="range" min="0" max="4" value="0" step="1"></label>
  <span class="val" id="vl">畳まない</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a4a5a"></i>\(t_0,\ell_P\) だけから出る数</span>
  <span><i class="swatch" style="background:#b0552a"></i>観測をもう一つ使う数</span>
  <span><i class="swatch" style="background:#8fa8b4"></i>畳まれて消えた数</span>
</div>
</div>

<h2><span class="n">04</span>第19回の手続きを、シリーズ自身に当てる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>一致</th><th class="mid">正体</th><th class="mid">驚き</th></tr></thead>
<tbody>
<tr><th>使用率 ＝ 占有率</th><td class="mid">恒等式（\(N=A/4\ell_P^2\ln2\) から）</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>\(C\cdot t=N\)</th><td class="mid">恒等式（\(E=c^4R/2G\) とホログラフィー）</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>\(dN/dt=2C\)</th><td class="mid">恒等式（\(N\propto t^2\)）</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>140 が四度</th><td class="mid">全て \(\ln(t_0/t_P)\)</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>\(\Omega/N=p\ln2/2\pi^2\)</th><td class="mid">状態方程式だけで決まる（導出）</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>\(N_T/N_t\approx1/2\)</th><td class="mid">輻射期が対数レンジを支配</td><td class="mid">1.0 bit</td></tr>
<tr class="hi"><th>1 ビット ↔ 1.96 fm</th><td class="mid">偶然（第18回で判定済み）</td><td class="mid"><strong>7.4 bit</strong></td></tr>
</tbody>
</table>
</div>

<p>合計 8.4 ビット ── そのうち 7.4 は第18回で「偶然」と判定済みの一件です。<strong>第 III 部で出てきた一致のほとんどは、驚き 0 ビット、つまり恒等式でした。</strong></p>

<h2><span class="n">05</span>種明かし ── では第 III 部は何をしたのか</h2>

<div class="keybox">
<p class="lbl">05節の結論</p>
<p style="margin:6px 0 0"><strong>発見したのではありません。同じ数を、八つの言語で言い直しました。</strong></p>
</div>

<p>これは自己批判ではなく、シリーズの主題そのものです。第25回の言葉で書き直すとこうなります ── <em>やっていたのは L(法則) を短くする作業であり、記述言語に依存するから判定には使えない</em>。ではなぜやるのか。</p>

<div class="seven">
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>言い直さないと、どの二つが恒等式で結ばれているか見えない</strong><span>「使用率」と「ブラックホールの占有率」が同じ数だと気づくには、二つの言葉で書いてみるしかありません</span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>恒等式が 5 本見つかった</strong><span>これは構造の地図であって、新しい物理ではない</span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>残った 1 本が本物の謎</strong><span>1.96 fm の 7.4 ビット。地図を描いたおかげで、<em>説明できていない場所が 1 か所だけ</em>だと分かった</span></div></div>
</div>

<p>地図を描く前は、24 個の数字が並んでいるように見えました。描いたあとは、<strong>12 個の入力と、1 個の説明できない一致</strong>です。<em>これが情報理論で物理を読むということの、正直な収穫です。</em></p>

<div class="aside">
<span class="tag">c·t=一定 の役割は、どこにあったか</span>
第 III 部で \(c\cdot t=\)一定 が効いたのは一箇所だけ ── \(\Omega/N=p\ln2/2\pi^2\) の \(p=1\)、つまり 0.0351 です。それ以外の 23 個は、<strong>膨張則を仮定しなくても同じ数が出ます</strong>（\(R_H=ct_0\) という規約は使いますが、これは第2回で決めた記法です）。<em>つまり第 III 部は、モデルの検証ではなく、記法の検証でした。</em> それでよいのです ── このシリーズの主題は判定ではなく圧縮だからです。判定は第3回で終わっています。
</div>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 「独立な入力 12 個」の数え方は一意ではありません。</strong> \(\ell_P\) を \(\hbar,G,c\) の三つと数えれば 14 個、\(N_{\rm data}\) と \(\Delta\chi^2\) を「Planck のデータ 1 個」とまとめれば 11 個になります。<em>圧縮率 2.0 倍という数字も、第25回で崩したのと同じ理由で数え方に依存します</em> ── だから桁の話としてだけ読んでください。</p>
<p style="margin:0 0 10px"><strong>② 「使用率＝占有率」が恒等式なのは、\(S\) をブラックホールが支配する限りです。</strong> 実際 CMB 光子の寄与は \(10^{-15}\) 倍以下ですが、これは観測に基づく事実であって恒等式ではありません。<em>恒等式なのは \((S/\ln2)/N=4\ell_P^2S/A\) の部分だけ</em>です。</p>
<p style="margin:0 0 10px"><strong>③ 第21回の \(0.127\) は逆算された数です。</strong> 本文でもそう書きましたが、あらためて ── あれは独立な確認ではなく、同じ \(1.5\times10^{-18}\) を対数ステップの言葉で書き直したものです。</p>
<p style="margin:0 0 10px"><strong>④ 「驚き 0.0 bit」は第19回の手続きによる分類で、主観的な事前範囲に依存します。</strong> 恒等式に 0 を割り当てるのは定義に近く、7.4 bit のほうは事前範囲の取り方次第で数ビット動きます。</p>
<p style="margin:0"><strong>⑤ 第3回の判定は動かしていません。</strong> 05節は「第 III 部は判定をしていない」と言っているのであって、判定を撤回しているのではありません。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>使用率と占有率が同じ数になることを示せ。
<details><summary>答えを見る</summary><div class="ans">\(N=A/(4\ell_P^2\ln2)\) を使うと \((S/\ln2)/N=(S/\ln2)\cdot4\ell_P^2\ln2/A=4\ell_P^2S/A\)。ブラックホールなら \(S=A_{BH}/(4\ell_P^2)\) なので、これは \(\sum A_{BH}/A_H\)。<strong>ホログラフィーの定義から一行</strong>です。</div></details></li>

<li>\(N_T/N_t=0.52\) が \(1/2\) に近い理由を述べよ。
<details><summary>答えを見る</summary><div class="ans">対数レンジの大半（プランク期から等密度期まで）が輻射優勢で、そこでは \(T\propto t^{-1/2}\)。つまり \(d\ln T/d\ln t=-1/2\) が 140 ステップのうち大部分を占めます。<strong>これは説明のある一致</strong>なので、驚きは 1 ビット程度です。</div></details></li>

<li>第 III 部の圧縮率を、\(\ell_P\) を \(\hbar,G,c\) の三つと数えて計算せよ。
<details><summary>答えを見る</summary><div class="ans">入力が 14 個になるので \(24/14=1.7\) 倍。<strong>数え方で変わる</strong>ことが分かります ── 第25回で L(法則) について見たのと同じ現象です。</div></details></li>

<li>第 III 部で \(c\cdot t=\)一定 が本当に効いた数はどれか。
<details><summary>答えを見る</summary><div class="ans">\(\Omega/N=p\ln2/2\pi^2\) の \(p=1\)、すなわち <strong>0.0351</strong> の一つだけ。残りは \(R_H=ct_0\) という記法だけを使っており、膨張則そのものには依存しません。</div></details></li>

<li>（やや難）「同じ数を八つの言語で言い直した」ことに価値はあるか。
<details><summary>答えを見る</summary><div class="ans">あります。言い直さなければ、<strong>どの二つが恒等式で結ばれているか</strong>が見えないからです。地図を描く前は 24 個の独立な発見に見えたものが、描いたあとは 12 個の入力と 1 個の説明できない一致になりました。<em>「説明できていない場所が 1 か所だけ」と分かることが収穫</em>です ── ただしこれは新しい物理ではなく、構造の地図です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　同じ数を、八つの言語で</h2>
<p>第 III 部で繰り返し出てきた数を追いかけました。\(1.5\times10^{-18}\) は三度出てきましたが、使用率と占有率は \(N=A/(4\ell_P^2\ln2)\) から一行で導ける<strong>恒等式</strong>で、第21回の時間の矢はその逆算でした ── <em>三度出てきた \(1.5\times10^{-18}\) は、一つの数です</em>。140 も四度出てきて、全て \(\ln(t_0/t_P)\) でした。独立なのは温度の \(N_T=73.03\) だけで、比 0.52 は輻射期が対数レンジを支配することの反映です。</p>
<p>見出し数字 24 個に対して独立な入力は 12 個。<strong>第 III 部自身の圧縮率は 2.0 倍</strong> ── 第25回の物差しを自分に当てると、桁ではありませんでした。第19回の手続きで一致を仕分けると、7 件のうち 5 件が驚き 0 ビット（恒等式）、1 件が 1 ビット（説明あり）、残る 1 件が 7.4 ビット ── 第18回の <strong>1.96 fm</strong> です。</p>
<p>だから第 III 部がしたのは発見ではなく、<em>同じ数を八つの言語で言い直すこと</em>でした。それでも価値はあります ── 言い直さなければ、どの二つが恒等式で結ばれているかは見えないからです。恒等式が 5 本見つかり、<strong>説明できていない場所が 1 か所だけ</strong>だと分かりました。地図を描く前は 24 個の独立な数字に見えたものが、描いたあとは 12 個の入力と 1 個の謎です。</p>
<p>そして \(c\cdot t=\)一定 が本当に効いた数は、24 個のうち <strong>1 個だけ</strong>（\(\Omega/N=0.0351\)）でした。第 III 部はモデルの検証ではなく、<em>記法の検証</em>だったということです ── このシリーズの主題は判定ではなく圧縮なので、それでよいのです。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第 IV 部・第27回</span>
第 III 部はここまで。第 IV 部では<strong>同じ手術を、他の理論に当てます</strong>。宇宙論を離れて、まず<em>熱力学</em>から ── カルノー効率、マクスウェルの悪魔、ランダウアー限界。<strong>\(c\cdot t=\)一定 の言葉で熱機関を書くと、効率の上限が「1 ビットあたりの演算数」と同じ形になります。</strong> 第1回の \(\Omega/N=p\ln2/2\pi^2\) が、まったく別の顔で出てきます。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sl=document.getElementById('sl'), vl=document.getElementById('vl'), ro=document.getElementById('ro');
  var items=[
    {n:'N',                g:0, f:-1},
    {n:'dN/dt',            g:0, f:-1},
    {n:'C',                g:0, f:2},
    {n:'C·t/N=1',          g:0, f:2},
    {n:'(dN/dt)/C=2',      g:0, f:2},
    {n:'140.24',           g:0, f:-1},
    {n:'1.96 fm',          g:0, f:-1},
    {n:'使用率',            g:1, f:-1},
    {n:'占有率',            g:1, f:1},
    {n:'時間の矢',          g:1, f:1},
    {n:'冗長度',            g:1, f:1},
    {n:'Ω/N=0.0351',       g:1, f:-1},
    {n:'N_T=73.03',        g:1, f:-1},
    {n:'N_T/N_t',          g:1, f:3},
    {n:'5.37 bit',         g:1, f:-1},
    {n:'153.6 bit',        g:1, f:-1},
    {n:'−148.3 bit',       g:1, f:4},
    {n:'6.26e6 モード',     g:1, f:-1},
    {n:'圧縮率 1.0e6',      g:1, f:4},
    {n:'95.0 %',           g:1, f:-1},
    {n:'20 KB',            g:1, f:-1},
    {n:'8.55e-96 s',       g:1, f:-1},
    {n:'1.91e-90',         g:1, f:-1},
    {n:'7.4 bit',          g:1, f:-1}
  ];
  var LAB=['畳まない','恒等式（使用率）を畳む','＋ C·t=N, dN/dt=2C','＋ 比の数','＋ 割り算の数'];
  var X0=48, Y0=52, CW=168, CH=30;
  function draw(){
    var lv=parseInt(sl.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    var alive=0;
    for(var i=0;i<items.length;i++){
      var it=items[i];
      var gone = it.f>=1 && it.f<=lv;
      if(!gone) alive++;
      var col = Math.floor(i/8), row = i%8;
      var x=X0+col*CW, y=Y0+row*(CH+8);
      g.fillStyle = gone ? '#eef2f4' : (it.g===0 ? '#2a4a5a' : '#b0552a');
      g.fillRect(x,y,150,CH);
      g.fillStyle = gone ? '#8fa8b4' : '#fff';
      g.textAlign='left';
      g.fillText(it.n, x+10, y+20);
      if(gone){
        g.strokeStyle='#8fa8b4'; g.lineWidth=1.4;
        g.beginPath(); g.moveTo(x+6,y+CH/2); g.lineTo(x+144,y+CH/2); g.stroke();
      }
    }
    g.fillStyle='#2a4a5a'; g.textAlign='left';
    g.font='bold 15px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('第III部の見出し数字 '+items.length+' 個  →  残り '+alive+' 個', X0, 30);
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillStyle='#6b8794';
    g.fillText('独立な入力は 12 個。ここまで畳んでも、まだ入力より多い ── 残りは別々の観測から来ている', X0, 386);
    vl.textContent=LAB[lv];
    ro.textContent=LAB[lv]+'　→　'+items.length+' 個 のうち '+alive+' 個が残る'+
      '（畳めた '+(items.length-alive)+' 個は全て驚き 0 ビットの恒等式）';
  }
  sl.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-26-partIII.html', acc='#2a4a5a', ops='#b0552a',
      title='第III部・総決算 ── わかる c·t=一定 第26回',
      ep='第 26 回 ／ 第 III 部・完',
      eyebrow='八つの物差しで測った数は、いくつあったのか',
      h1='同じ数を、<br>八つの言語で',
      sub='\\(1.5\\times10^{-18}\\) が三度、\\(140\\) が四度。<br><em>第19回の手続きを、シリーズ自身に当てます。</em>',
      byline_l='必要な道具：第 III 部の全回、引き算',
      byline_r='24 個 → 入力 12 個',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第26回（第 III 部・完）、物理好きの高校生・大学生向け読み物です。ホログラフィック境界 \\(N=A/(4\\ell_P^2\\ln2)\\)、ベケンシュタイン＝ホーキングのエントロピー \\(S_{BH}=A/(4\\ell_P^2)\\)、輻射優勢期の \\(T\\propto t^{-1/2}\\) はいずれも標準的です。<strong>本稿の主張（使用率＝占有率が恒等式であること、第 III 部の見出し数字 24 個が独立な入力 12 個に帰着すること、驚きの合計 8.4 ビット）は本稿での集計です</strong>（kenshou/calc30.py）。「独立な入力 12 個」の数え方は一意ではなく、\\(\\ell_P\\) を \\(\\hbar,G,c\\) の三つと数えれば 14 個、Planck のデータをまとめれば 11 個になります ── <em>圧縮率 2.0 倍という数字自体が、第25回で崩したのと同じ理由で数え方に依存します</em>。「使用率＝占有率」が恒等式なのは \\(S\\) をブラックホールが支配する限りで、その支配は観測に基づく事実であって恒等式ではありません。「驚き 0.0 bit」は第19回の手続きによる分類で、主観的な事前範囲に依存します。線形膨張（\\(c\\cdot t=\\)一定）は検証途上の少数派モデルで、その判定は第3回で扱いました ── 本稿は判定を撤回するものではなく、<em>第 III 部が判定ではなく記法を扱っていた</em>ことの確認です。\\(R_H=ct_0\\) はその記法上の規約です（\\(\\Lambda\\)CDM では \\(R_H=c/H_0\\) と粒子的地平線が異なります）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで恒等式を畳むと、24 個がどこまで縮むかが見えます。「答えを見る」で解答が開きます。')
