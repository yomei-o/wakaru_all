# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第17回は通信でした。今回は<strong>アドレッシング</strong>です。宇宙の空間セルは \((R_H/\ell_P)^3=5.27\times10^{182}\) 個あるのに、書けるビットは \(2.96\times10^{122}\)。<em>セル 1 個につき 1 ビットどころか、\(10^{-61}\) しかない。</em> ホログラフィーを「面積に書かれる」ではなく「<strong>番地が足りない</strong>」と読み替えると、途中で妙に具体的な長さが出てきます ── <em>1 ビットが担当する体積の一辺は、およそ陽子の大きさ</em>。</p>

<h2><span class="n">01</span>三つの数を、数える</h2>

<div class="calc">
<span class="tag">計算 ── 数えるだけ</span>
<p class="lbl">今日の宇宙をプランク長で測ると</p>
$$\frac{R_H}{\ell_P}=8.075\times10^{60}$$
<p class="lbl">空間セル（プランク体積の個数）</p>
$$\left(\frac{R_H}{\ell_P}\right)^3=5.27\times10^{182}$$
<p class="lbl">4 体積セル（プランク時空点の個数）</p>
$$\left(\frac{ct_0}{\ell_P}\right)^4=4.25\times10^{243}$$
<p class="lbl">書けるビット（第1回）</p>
$$N=\frac{\pi}{\ln2}\left(\frac{R_H}{\ell_P}\right)^2=2.96\times10^{122}$$
</div>

<p>並べると、指数が \(3\)、\(4\)、\(2\) です。<strong>ビットだけが 2 乗</strong> ── これがホログラフィーの全部です。</p>

<h2><span class="n">02</span>比は、きれいな恒等式になる</h2>

<div class="calc">
<span class="tag">割る</span>
$$\frac{N}{(R_H/\ell_P)^3}=\frac{\pi/\ln2}{R_H/\ell_P}=\frac{4.5324}{8.075\times10^{60}}=5.61\times10^{-61}$$
</div>

<div class="keybox">
<p class="lbl">02節の結論</p>
$$\boxed{\ \frac{\text{書けるビット}}{\text{空間セル}}=\frac{\pi/\ln2}{R_H/\ell_P}\ }$$
<p style="margin:10px 0 0"><strong>ホログラフィーとは「空間セルの \(10^{-61}\) にしか番地が振れない」ということ。</strong><br>
しかも比は \(1/R_H\) なので、<em>宇宙が大きくなるほど番地不足はひどくなります</em>。</p>
</div>

<p>逆に言えば ── 昔のほうがマシでした。\(N=(R_H/\ell_P)^3\) を解くと \(R_H/\ell_P=\pi/\ln2=4.53\)。<strong>アドレスが足りていたのは、宇宙がプランク長の 4.5 倍より小さかったときだけ</strong>です。</p>

<h2><span class="n">03</span>核心 ── 1 ビットが担当する体積</h2>

<p>比を逆にすると、もっと直観的な量になります ── <em>1 ビットあたり、どれだけの体積を面倒みているか</em>。</p>

<div class="calc">
<span class="tag">計算 ── 逆にするだけ</span>
$$\frac{(R_H/\ell_P)^3}{N}=\frac{\ln2}{\pi}\cdot\frac{R_H}{\ell_P}=1.78\times10^{60}\ \text{プランク体積}$$
<p class="lbl">体積に直すと</p>
$$7.52\times10^{-45}\ \mathrm{m^3}\qquad\Longrightarrow\qquad \text{一辺}\ \ell_{\rm bit}=1.96\times10^{-15}\ \mathrm{m}$$
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0">1 ビットが担当する体積は、<strong>一辺 1.96 フェムトメートル</strong>の立方体。<br>
── <em>陽子の大きさです</em>（電荷半径 0.84 fm、直径 1.68 fm）。</p>
</div>

<p>宇宙のホログラフィック・メモリを空間に割り当てると、<strong>ちょうど核子 1 個ぶんの体積に 1 ビット</strong>が対応します。もちろん「陽子 1 個が 1 ビット」という意味ではありません ── <em>数がたまたま合っているだけ</em>です。それでも、この一致は見た瞬間に足が止まります。</p>

<h2><span class="n">04</span>これは、どういうスケールなのか</h2>

<p>正体を確かめます。\(\ell_{\rm bit}^3\propto R_H\ell_P^2\) なので ──</p>

<div class="calc">
<span class="tag">中間スケール</span>
$$\ell_{\rm bit}=\left(\frac{\ln2}{\pi}\right)^{1/3}\left(R_H\,\ell_P^2\right)^{1/3}$$
<p class="lbl">係数を外した素の値</p>
$$\left(R_H\,\ell_P^2\right)^{1/3}=3.24\ \mathrm{fm}\qquad(\text{係数 }0.604\text{ を掛けて }1.96\ \mathrm{fm})$$
</div>

<p>つまり <strong>地平半径とプランク長の「3 分の 1 乗の中間スケール」</strong>です。宇宙でいちばん大きい長さと、いちばん小さい長さを、この重みで混ぜると核子の大きさが出る ── <em>説明のない数値的一致</em>で、前シリーズ番外編⑤の「\(\rho_\Lambda^{1/4}\) とニュートリノ質量が 22 倍しか違わない」と同じ種類のものです。</p>

<div class="aside">
<span class="tag">こういう一致の扱い方</span>
このシリーズは、数値的一致に対していつも同じ手続きを使ってきました ── <strong>恒等式か、偶然か、物理か</strong>。ディラックの大数（第7回）は<em>恒等式</em>でした。ランダウアー限界ぴったり（第10回）も<em>恒等式</em>。今回の 1.96 fm は恒等式ではありません（\(R_H\) と \(\ell_P\) を独立に与えれば任意の値になる）。かといって物理的な機構も知られていない。<strong>いまのところ「偶然」の欄に置くしかない</strong>数字です ── そう明記しておくのが、このシリーズの作法です。
</div>

<div class="fig">
<p class="cap">図：宇宙の大きさを変えると、三つの数がどう伸びるか。<strong>セルは傾き 3、4 体積は傾き 4、ビットは傾き 2</strong>。ビットだけが遅いので、大きくなるほど番地不足が開いていきます ── <em>足りていたのは、宇宙がプランク長の 4.5 倍以下だったときだけ</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>宇宙の大きさ \(\log_{10}(R_H/\ell_P)\)（右端が今日）<input id="sr" type="range" min="0" max="609" value="609" step="1"></label>
  <span class="val" id="vr">今日</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#4a3a1f"></i>空間セル（傾き 3）</span>
  <span><i class="swatch" style="background:#8a7a4a"></i>4 体積セル（傾き 4）</span>
  <span><i class="swatch" style="background:#2a6b5a"></i>書けるビット（傾き 2）</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">05</span>番地表そのものが、メモリに入らない</h2>

<p>「番地が足りない」をもう一段進めます。<strong>そもそも番地を書くのに何ビット要るか</strong>を数えてみましょう。</p>

<div class="calc">
<span class="tag">アドレス幅</span>
$$\log_2\left(5.27\times10^{182}\right)=607\ \text{ビット}$$
<p class="lbl">全セルに番地を振ると</p>
$$5.27\times10^{182}\times607=3.20\times10^{185}\ \text{ビット}$$
<p class="lbl">メモリと比べると</p>
$$\frac{3.20\times10^{185}}{2.96\times10^{122}}=1.1\times10^{63}\ \text{倍}$$
</div>

<div class="keybox">
<p class="lbl">05節の結論</p>
<p style="margin:6px 0 0"><strong>全セルに番地を振ること自体が、メモリの \(10^{63}\) 倍を要します。</strong><br>
── <em>番地表がメモリに入らない</em>。アドレス空間は、宇宙が扱える規模を超えています。</p>
</div>

<p>これは第6回の「使用率 \(10^{-18}\)」とは<strong>別の不足</strong>です。あちらは「容量はあるのに使っていない」という話でした。今回は「<em>そもそも番地が振れない</em>」── 使う以前の問題です。</p>

<h2><span class="n">06</span>時間方向は、さらに 61 桁足りない</h2>

<div class="calc">
<span class="tag">4 体積で数える</span>
$$\frac{N}{(ct_0/\ell_P)^4}=\frac{2.96\times10^{122}}{4.25\times10^{243}}=7.0\times10^{-122}$$
</div>

<p>空間だけなら \(10^{-61}\)、時間まで入れると \(10^{-122}\)。ちょうど 2 倍の桁数です（当然で、\(N\propto R^2\) に対し \(R^4\) だから）。意味するところは明確です ── <strong>「宇宙の全履歴を記録する」ことは、原理的に不可能</strong>。</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>いま起きていることを全部書く</strong><span>空間セルの \(10^{-61}\) しか番地がない → <em>不可能</em></span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>これまで起きたことを全部書く</strong><span>4 体積セルの \(10^{-122}\) → <em>さらに 61 桁不可能</em></span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>地平面に書ける量だけが上限</strong><span>そしてそれは \(R^2\) でしか増えない ── <em>これがホログラフィーの内容のすべて</em></span></div></div>
</div>

<h2><span class="n">07</span>種明かし ── これは圧縮ではない</h2>

<p>ホログラフィーを「体積の情報が面積に圧縮されている」と言うことがあります。<strong>アドレスの言葉で読むと、その言い方は誤解を招きます。</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th>圧縮なら</th><th class="mid">実際のホログラフィー</th></tr></thead>
<tbody>
<tr><th>元の情報</th><td>体積ぶんある</td><td class="mid"><strong>最初から面積ぶんしかない</strong></td></tr>
<tr><th>操作</th><td>冗長性を削って詰める</td><td class="mid">何も詰めていない</td></tr>
<tr><th>復元</th><td>元に戻せる</td><td class="mid">戻すべき「元」が存在しない</td></tr>
<tr class="hi"><th>正しい言い方</th><td>──</td><td class="mid"><strong>体積セルには、はじめから番地が振られていない</strong></td></tr>
</tbody>
</table>
</div>

<p>第13回で「共形変換は大きさにしか触れない」と線引きしました。今回はもっと基本的な線引きです ── <em>宇宙という記憶装置は、体積ではなく面積で番地が決まっている</em>。だから \(10^{182}\) 個のセルのうち \(10^{122}\) 個ぶんしか指定できず、その差は宇宙が大きくなるほど開いていきます。</p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 「空間セル」を \((R_H/\ell_P)^3\) 個と数えるのは、時空が離散格子であるという主張ではありません。</strong> プランク体積を単位に取った<em>目安の個数</em>で、前シリーズ番外編③の「セル／ティック」と同じ比喩の使い方です。</p>
<p style="margin:0 0 10px"><strong>② ホログラフィック限界は「これ以上は入らない」という不等式です。</strong> 「ここまで使える」という保証ではありません（第6回②と同じ注意）。したがって「番地が足りない」は<em>上限についての言明</em>であって、実際に何かを記録しようとして失敗した、という話ではありません。</p>
<p style="margin:0 0 10px"><strong>③ \(\ell_{\rm bit}=1.96\) fm という一致には、既知の説明がありません。</strong> 恒等式でもなく（\(R_H\) と \(\ell_P\) を独立に与えれば任意の値になります）、物理的な機構も知られていない。<em>「偶然」の欄に置くべき数字</em>です。なお \((R_H\ell_P^2)^{1/3}\) が核子スケールになるという指摘自体は文献にも見られる類のもので、本稿の発見ではありません。</p>
<p style="margin:0 0 10px"><strong>④ 05節のアドレス幅の議論は、素朴な符号化を仮定しています。</strong> 実際にはセルに個別の番地を振る必要はなく（座標そのものが番地になる）、「番地表を作る」という操作は物理的に要求されていません ── <em>アドレス空間の大きさを実感するための計算</em>として読んでください。</p>
<p style="margin:0"><strong>⑤ \(R_H=ct_0\) は \(c\cdot t=\text{一定}\) の規約です。</strong> \(\Lambda\)CDM では \(R_H=c/H_0\) と粒子的地平線が異なり、数値は数倍動きます ── 桁の議論として読んでください。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>書けるビットと空間セルの比を、\(R_H/\ell_P\) の式で表せ。
<details><summary>答えを見る</summary><div class="ans">\(N/(R_H/\ell_P)^3=[\pi(R_H/\ell_P)^2/\ln2]/(R_H/\ell_P)^3=(\pi/\ln2)/(R_H/\ell_P)\)。<strong>\(1/R_H\) に比例</strong>するので、宇宙が大きくなるほど番地不足はひどくなります。</div></details></li>

<li>アドレスが足りていたのはいつか。
<details><summary>答えを見る</summary><div class="ans">\(N=(R_H/\ell_P)^3\) を解いて \(R_H/\ell_P=\pi/\ln2=4.53\)。<strong>宇宙がプランク長の 4.5 倍より小さかったときだけ</strong>です。それ以降はずっと足りていません。</div></details></li>

<li>1 ビットが担当する体積の一辺を求めよ。
<details><summary>答えを見る</summary><div class="ans">\((R_H/\ell_P)^3/N=(\ln2/\pi)(R_H/\ell_P)=1.78\times10^{60}\) プランク体積 \(=7.52\times10^{-45}\ \mathrm{m^3}\)。立方根を取って <strong>1.96 fm</strong> ── <em>陽子の大きさ</em>です。</div></details></li>

<li>それはどんなスケールか。
<details><summary>答えを見る</summary><div class="ans">\(\ell_{\rm bit}\propto(R_H\ell_P^2)^{1/3}\)、つまり<strong>地平半径とプランク長の 3 分の 1 乗の中間スケール</strong>。素の値は 3.24 fm、係数 \((\ln2/\pi)^{1/3}=0.604\) を掛けて 1.96 fm。<em>説明のない数値的一致</em>で、恒等式でも物理でもありません。</div></details></li>

<li>（やや難）ホログラフィーを「圧縮」と呼ぶのは、なぜ誤解を招くか。
<details><summary>答えを見る</summary><div class="ans">圧縮なら「体積ぶんの情報を冗長性を削って詰める」ことになりますが、実際には<strong>最初から面積ぶんの情報しか存在しません</strong>。詰めてもいないし、戻すべき「元」もない。正しい言い方は <em>「体積セルには、はじめから番地が振られていない」</em> ── 情報の量ではなく、<strong>アドレス空間の構造</strong>の話です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　番地は、面積でしか増えない</h2>
<p>三つの数を数えました ── 空間セル \((R_H/\ell_P)^3=5.27\times10^{182}\)、4 体積セル \(4.25\times10^{243}\)、書けるビット \(2.96\times10^{122}\)。指数は \(3\)、\(4\)、\(2\) で、<strong>ビットだけが 2 乗</strong>。これがホログラフィーの内容のすべてです。</p>
<p>比はきれいな恒等式になりました ── \(N/(R_H/\ell_P)^3=(\pi/\ln2)/(R_H/\ell_P)=5.61\times10^{-61}\)。<strong>「空間セルの \(10^{-61}\) にしか番地が振れない」</strong>、しかも \(1/R_H\) に比例するので<em>宇宙が大きくなるほど不足は開きます</em>。足りていたのは、宇宙がプランク長の 4.5 倍より小さかったときだけ。</p>
<p>逆にすると、1 ビットが担当する体積が出ます ── \(1.78\times10^{60}\) プランク体積、一辺 <strong>1.96 フェムトメートル</strong>。<em>陽子の大きさ</em>です。正体は \((R_H\ell_P^2)^{1/3}\)、宇宙でいちばん大きい長さといちばん小さい長さの「3 分の 1 乗の中間スケール」── 恒等式でも物理でもなく、いまのところ<strong>偶然の欄に置くしかない一致</strong>です。</p>
<p>さらに、番地表そのものがメモリに入りません（全セルに番地を振ると \(10^{63}\) 倍）。時間方向まで数えると不足は \(10^{-122}\) に広がり、<strong>「宇宙の全履歴を記録する」ことは原理的に不可能</strong>。そして最後に言葉の整理 ── ホログラフィーは<em>圧縮ではありません</em>。詰めてもいないし戻すべき元もない。正しくは <strong>「体積セルには、はじめから番地が振られていない」</strong>。第6回の「使用率 \(10^{-18}\)」が「あるのに使っていない」話だったのに対し、今回は<em>使う以前の不足</em>でした。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第19回</span>
第10回で片付けきれなかった宿題に戻ります ── <strong>「宇宙はランダウアー限界ぴったりで走っている」</strong>。あの比 1.000000 は \(E=T_HS\) という恒等式でした。では<em>恒等式だと分かった数字には、まだ何か言うことが残っているのか</em>。第7回のディラックの大数、第14回の \(\alpha+2\beta+\gamma=2\)、そして今回の 1.96 fm ── このシリーズは恒等式と偶然と物理を何度も仕分けてきました。次回はその<strong>仕分けの手続きそのもの</strong>を、正面から作ります。<em>恒等式は本当に「物理ではない」のか。</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sr=document.getElementById('sr'), vr=document.getElementById('vr'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=316;
  var ln2=Math.log(2), PI=Math.PI;
  var xmin=0, xmax=62, ymin=0, ymax=250;
  var CROSS=Math.log(PI/ln2)/Math.LN10;   // ビット＝セル になる log10(R/l)

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function line(sl,off,col,w){
    g.strokeStyle=col; g.lineWidth=w; g.beginPath();
    var first=true;
    for(var i=0;i<=200;i++){
      var x=xmin+(xmax-xmin)*i/200, y=off+sl*x;
      if(y<ymin||y>ymax){ first=true; continue; }
      if(first){ g.moveTo(px(x),py(y)); first=false; } else g.lineTo(px(x),py(y));
    }
    g.stroke();
  }

  function draw(){
    var lr=parseInt(sr.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right';
    for(var e=0;e<=250;e+=50){
      var y=py(e);
      g.strokeStyle='#f2efe6'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a49a86'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=60;q+=10){
      var x=px(q);
      g.strokeStyle='#f8f6f1'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a49a86'; g.fillText('10'+q, x, Y1+16);
    }
    g.strokeStyle='#cdc6b5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    line(4,0,'#8a7a4a',2.6);                                  // 4体積セル
    line(3,0,'#4a3a1f',3.2);                                  // 空間セル
    line(2,Math.log(PI/ln2)/Math.LN10,'#2a6b5a',3.4);         // ビット

    // 交点（ビット＝セル）
    if(CROSS>xmin&&CROSS<xmax){
      var yc=3*CROSS;
      g.fillStyle='#2a6b5a';
      g.beginPath(); g.arc(px(CROSS),py(yc),5,0,6.2832); g.fill();
      g.fillStyle='#2a6b5a'; g.textAlign='left';
      g.fillText('ここまでは番地が足りていた（R/ℓ_P = 4.5）', px(CROSS)+10, py(yc)+18);
    }

    // カーソル
    g.strokeStyle='#7a6a48'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(lr),Y0); g.lineTo(px(lr),Y1); g.stroke();
    g.setLineDash([]);

    g.textAlign='left';
    g.fillStyle='#8a7a4a'; g.fillText('4体積セル（傾き 4）', px(38), py(4*38)-8);
    g.fillStyle='#4a3a1f'; g.fillText('空間セル（傾き 3）', px(50), py(3*50)-8);
    g.fillStyle='#2a6b5a'; g.fillText('書けるビット（傾き 2）', px(52), py(2*52)+18);

    g.fillStyle='#8a8272'; g.textAlign='center';
    g.fillText('宇宙の大きさ  R_H / ℓ_P', (X0+X1)/2, Y1+36);

    var R=Math.pow(10,lr);
    var cells=Math.pow(R,3), bits=(PI/ln2)*R*R, v4=Math.pow(R,4);
    vr.textContent = (lr>60.5?'今日':'10^'+lr.toFixed(1));
    ro.textContent='R_H/ℓ_P = '+R.toExponential(2)+
      '　セル '+cells.toExponential(2)+
      '　ビット '+bits.toExponential(2)+
      '　→　比 '+(bits/cells).toExponential(2)+
      '　／　1ビットあたり '+(cells/bits).toExponential(2)+' プランク体積'+
      (bits>cells?'　★ 番地が足りている':'');
  }
  sr.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-18-address.html', acc='#4a3a1f', ops='#2a6b5a',
      title='アドレス線が、足りない ── わかる c·t=一定 第18回',
      ep='第 18 回 ／ ホログラフィーを、アドレスの言葉で読む',
      eyebrow='1ビットが担当する体積の一辺は、およそ陽子の大きさでした',
      h1='アドレス線が、<br>足りない',
      sub='空間セルは \\(5.27\\times10^{182}\\) 個、書けるビットは \\(2.96\\times10^{122}\\)。<br><em>セルの \\(10^{-61}\\) にしか番地が振れない ── そして差は開き続けます。</em>',
      byline_l='必要な道具：割り算、立方根',
      byline_r='\\(\\ell_{\\rm bit}=1.96\\ \\mathrm{fm}\\)',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第18回、物理好きの高校生・大学生向け読み物です。地平面のホログラフィック上限 \\(N=A/(4\\ell_P^2\\ln2)\\) は標準的です。本稿の \\((R_H/\\ell_P)^3=5.27\\times10^{182}\\)、\\((ct_0/\\ell_P)^4=4.25\\times10^{243}\\)、\\(N/(R_H/\\ell_P)^3=(\\pi/\\ln2)/(R_H/\\ell_P)=5.61\\times10^{-61}\\)、1 ビットあたり \\(1.78\\times10^{60}\\) プランク体積（一辺 \\(1.96\\) fm）、アドレス幅 607 ビットと番地表が \\(10^{63}\\) 倍になること、\\(N/(ct_0/\\ell_P)^4=7.0\\times10^{-122}\\)、および「番地が足りていたのは \\(R_H/\\ell_P<\\pi/\\ln2=4.53\\) のときだけ」は、いずれも本稿での計算です（kenshou/calc22.py）。<strong>「空間セル」をプランク体積の個数で数えるのは目安であり、時空が離散格子であるという主張ではありません</strong>（前シリーズ番外編③の「セル／ティック」と同じ比喩の使い方）。ホログラフィック限界は「これ以上は入らない」という不等式であって貯蔵可能量の保証ではないため、「番地が足りない」は上限についての言明です。<strong>\\(\\ell_{\\rm bit}\\simeq1.96\\) fm が核子スケールになることには既知の説明がなく、恒等式でも物理的機構でもありません</strong> ── \\((R_H\\ell_P^2)^{1/3}\\) が核子スケールになるという指摘自体は文献に見られる類のもので、本稿の発見ではありません。05節のアドレス幅の議論は素朴な符号化を仮定したもので、実際には座標そのものが番地になるため「番地表を作る」操作は物理的に要求されていません。\\(R_H=ct_0\\) は \\(c\\cdot t=\\)一定 の規約で、\\(\\Lambda\\)CDM では \\(R_H=c/H_0\\) と粒子的地平線が異なり数値は数倍動きます。線形膨張は検証途上の少数派モデルで、初期宇宙まで外挿した場合は元素合成と矛盾します（Lewis, Barnes &amp; Kaushik 2016）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで宇宙の大きさを変え、ビットの線だけが遅れていく様子が見えます。「答えを見る」で解答が開きます。')
