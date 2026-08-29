# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第37回と第38回は、共形変換を量子と重力に当てたときに<em>壊れる場所</em>を見ました。今回は視点を変えて、<strong>回転する時空</strong>を見ます ── カー解。ブラックホールのラベルは \(M\) と \(\chi=a/(GM/c^2)\) の二つで、<em>片方だけが帳簿、片方は物理</em>です。第 II 部の結論「共形変換が触れるのは大きさだけ」の、<strong>いちばん綺麗な例</strong>。そして \(\chi\le1\) という上限は ── <em>触れられない列に置かれた、書き換えのきかない線</em>です。</p>

<h2><span class="n">01</span>カー解の二つのラベルを、ウェイト表に置く</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">ウェイト</th><th class="mid">分類</th><th class="mid">共形変換</th></tr></thead>
<tbody>
<tr><th>質量 \(M\)</th><td class="mid">\(-1\)</td><td class="mid">次元付き ＝ 帳簿</td><td class="mid">動く</td></tr>
<tr class="hi"><th>角運動量 \(J\sim ML^2/T\)</th><td class="mid">\(-1+2-1=\mathbf{0}\)</td><td class="mid"><strong>次元なし ＝ 物理</strong></td><td class="mid"><strong>動かない</strong></td></tr>
<tr><th>回転の長さ \(a=J/(Mc)\)</th><td class="mid">\(0-(-1)-0=+1\)</td><td class="mid">長さ ＝ 帳簿</td><td class="mid">動く</td></tr>
<tr><th>重力半径 \(GM/c^2\)（\(G\) は \(+2\)）</th><td class="mid">\(+2-1=+1\)</td><td class="mid">長さ ＝ 帳簿</td><td class="mid">動く</td></tr>
<tr class="hi"><th>スピン \(\chi=a/(GM/c^2)\)</th><td class="mid">\(+1-1=\mathbf{0}\)</td><td class="mid"><strong>次元なし ＝ 物理</strong></td><td class="mid"><strong>動かない</strong></td></tr>
</tbody>
</table>
</div>

<div class="aside">
<span class="tag">検算</span>
角運動量は \(\hbar\) を単位に測る量で、\(\hbar\) はウェイト 0（第16回）。<br>
独立に数えた \(-1+2-1=0\) と一致します ── <em>表は矛盾していません。</em>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>カー解のラベルは \((M,\chi)\) の二つ。片方だけが帳簿、片方は物理です。</strong><br>
── <em>第 II 部の結論「共形変換が触れるのは大きさだけ」の、いちばん綺麗な例。</em></p>
</div>

<h2><span class="n">02</span>そのうち、いくらぶんが記法か</h2>

<div class="calc">
<span class="tag">第5回の値段で数える</span>
$$2\times5.37=10.7\ \text{ビット}\qquad\text{そのうち }M\text{ の }5.37\ \text{ビットは}\textbf{まるごと記法}$$
</div>

<p><strong>カー解の情報の半分は、書き方の情報でした。</strong> 単位を変えれば \(M\) の数値は変わりますが、\(\chi\) は動きません ── <em>物理はもう一方の 5.37 ビットだけに入っています</em>。</p>

<h2><span class="n">03</span>\(\chi\le1\) ── 触れられない列に置かれた上限</h2>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>カー解に地平面があるのは \(\chi\le1\) のときだけ</strong><span>\(\chi>1\) なら地平面が消え、裸の特異点になる（宇宙検閲仮説）</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>この上限は無次元量に置かれている</strong><span>ウェイト 0 の列 ── <em>どんな共形変換も、ブラックホールをこの線の向こう側へ運べない</em></span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>第3回の言い方をすると</strong><span>予言が無次元量に置かれているから、<em>判定の土俵に乗る</em></span></div></div>
</div>

<h2><span class="n">04</span>地平面の面積とエントロピー</h2>

<div class="calc">
<span class="tag">同じ \(M\) で比べたときの面積比</span>
$$\frac{A(\chi)}{A(0)}=\frac{1+\sqrt{1-\chi^2}}{2}$$
<p class="lbl">太陽質量のシュヴァルツシルト BH： \(S/k_B=4\pi GM^2/\hbar c=1.05\times10^{77}\) → \(\mathbf{1.51\times10^{77}}\) ビット</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(\chi\)</th><th class="mid">\(A/A(0)\)</th><th class="mid">エントロピー [bit]</th><th class="mid">取り出せる質量の割合</th></tr></thead>
<tbody>
<tr><th class="mid">\(0\)</th><td class="mid">\(1.0000\)</td><td class="mid">\(1.51\times10^{77}\)</td><td class="mid">\(0\)</td></tr>
<tr><th class="mid">\(0.5\)</th><td class="mid">\(0.9330\)</td><td class="mid">\(1.41\times10^{77}\)</td><td class="mid">\(0.0341\)</td></tr>
<tr><th class="mid">\(0.686\)</th><td class="mid">\(0.8638\)</td><td class="mid">\(1.31\times10^{77}\)</td><td class="mid">\(0.0706\)</td></tr>
<tr><th class="mid">\(0.9\)</th><td class="mid">\(0.7179\)</td><td class="mid">\(1.09\times10^{77}\)</td><td class="mid">\(0.1527\)</td></tr>
<tr><th class="mid">\(0.998\)</th><td class="mid">\(0.5316\)</td><td class="mid">\(8.05\times10^{76}\)</td><td class="mid">\(0.2709\)</td></tr>
<tr class="hi"><th class="mid">\(1\)</th><td class="mid"><strong>\(0.5000\)</strong></td><td class="mid"><strong>\(7.57\times10^{76}\)</strong></td><td class="mid"><strong>\(0.29289\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0"><strong>\(\chi=1\) のカー BH は、同じ質量のシュヴァルツシルト BH の<em>ちょうど半分</em>のエントロピーしか持ちません。</strong><br>
そして取り出せる質量の上限は \(1-1/\sqrt2=\mathbf{0.29289}\) ── <em>これも無次元、これも触れられません。</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">05</span>核心 ── 実測されたスピンは、上限のすぐ下に並ぶ</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>天体・値</th><th class="mid">\(\chi\)</th><th>備考</th></tr></thead>
<tbody>
<tr><th>GRS 1915+105（連続スペクトル法）</th><td class="mid">\(0.98\)</td><td>解析法により 0.7 前後という結果もある</td></tr>
<tr><th>Cyg X-1（連続スペクトル法）</th><td class="mid">\(0.95\)</td><td>同上、<em>モデル依存が大きい</em></td></tr>
<tr><th>GW150914 の合体後</th><td class="mid">\(0.67\)</td><td>波形から</td></tr>
<tr><th>等質量・無スピン合体の理論値</th><td class="mid">\(0.686\)</td><td>数値相対論</td></tr>
<tr class="hi"><th>ソーン限界（降着で到達できる上限）</th><td class="mid"><strong>\(0.998\)</strong></td><td><strong>光子捕獲のため 1 には届かない</strong></td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">第19回の作法で驚きを測る（事前範囲は \(\chi\in[0,1]\)）</span>
$$\text{高スピン源が上限の }0.05\text{ 以内}\;\to\;4.3\ \text{ビット}\qquad
\text{ソーン限界が上限の }0.002\text{ 以内}\;\to\;9.0\ \text{ビット}$$
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>高スピン源は 4.3 ビット ── 第36回の「偶然の帯」（4〜7）に戻ってきます。</strong><br>
ただし<em>説明があります</em>（降着で角運動量を貰う、光子捕獲で 1 には届かない）。<br>
── だから第19回の分類では【偶然】ではなく<strong>【物理】</strong>。第36回で見た「説明ありの 4〜7 ビット」の仲間です。</p>
</div>

<div class="fig">
<p class="cap">図：スピン \(\chi\) を動かしたときの、地平面の面積・エントロピー・取り出せる質量。<strong>すべて無次元の関係で、共形変換ではまったく動きません</strong>。縦の線は実測されたスピンとソーン限界 ── <em>上限のすぐ下に並んでいます</em></p>
<canvas id="cv" width="720" height="390"></canvas>
<div class="controls">
  <label>スピン \(\chi\)<input id="sc" type="range" min="0" max="1000" value="686" step="1"></label>
  <span class="val" id="vc">0.686</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#7a5a2a"></i>地平面の面積 A/A(0)</span>
  <span><i class="swatch" style="background:#2a6a5a"></i>取り出せる質量の割合</span>
  <span><i class="swatch" style="background:#a03a3a"></i>ホーキング温度 T/T(0)</span>
</div>
</div>

<h2><span class="n">06</span>極限カーの困りごと</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(\chi\)</th><th class="mid">\(T/T(0)\)</th></tr></thead>
<tbody>
<tr><th class="mid">\(0\)</th><td class="mid">\(1.00000\)</td></tr>
<tr><th class="mid">\(0.5\)</th><td class="mid">\(0.92820\)</td></tr>
<tr><th class="mid">\(0.9\)</th><td class="mid">\(0.60714\)</td></tr>
<tr><th class="mid">\(0.99\)</th><td class="mid">\(0.24726\)</td></tr>
<tr><th class="mid">\(0.999\)</th><td class="mid">\(0.08559\)</td></tr>
<tr class="hi"><th class="mid">\(1\)</th><td class="mid"><strong>\(0\)</strong></td></tr>
</tbody>
</table>
</div>

<p>\(\chi\to1\) で<strong>温度はゼロ、エントロピーは半分のまま有限</strong>です。温度ゼロでエントロピーが \(7.6\times10^{76}\) ビット残る ── <em>熱力学第三法則の素朴な形と衝突します</em>。回避されるのは「有限回の操作では \(\chi=1\) に到達できない」という形で（Israel 1986）。<strong>第4回の「粗視化は不可逆」と同じく、近づけるが届かない線です。</strong></p>

<h2><span class="n">07</span>カーは、共形変換が届かない時空</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>段</th><th class="mid">例</th><th class="mid">意味</th></tr></thead>
<tbody>
<tr><th>リーマン \(=0\)</th><td class="mid">ミンコフスキー</td><td class="mid">座標変換だけで平坦にできる</td></tr>
<tr><th>ワイル \(=0\)（共形平坦）</th><td class="mid"><strong>すべての FLRW</strong></td><td class="mid">共形変換で平坦にできる</td></tr>
<tr class="hi"><th>ワイル \(\ne0\)</th><td class="mid"><strong>シュヴァルツシルト、カー</strong></td><td class="mid"><strong>どちらでも平坦にできない</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">07節の結論</p>
<p style="margin:6px 0 0">このシリーズが<strong>宇宙論の側で</strong>扱ってきた時空は、全部<strong>第 2 段</strong>でした（第33回）。<br>
カーは<strong>第 3 段</strong> ── <em>共形変換という道具が、宇宙論の外で正面から届かなくなる相手</em>です。<br>
ペトロフ型 D で、ワイル曲率が本質的にゼロにできません。</p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p style="margin:0 0 10px"><strong>① 05節のスピン測定値は、いずれもモデル依存が大きい量です。</strong> 連続スペクトル法と鉄輝線（反射）法で結果が食い違う天体があり、<em>GRS 1915+105 は 0.98 とも 0.7 前後とも報告されています</em>。「高スピン源が上限のすぐ下に並ぶ」という 05節の言い方は、<strong>高スピンを報告した測定だけを並べたものです</strong> ── 低スピンの報告もあり、選び方にバイアスがあります（第36回②と同じ構造）。</p>
<p style="margin:0 0 10px"><strong>② 05節の 4.3 ビットは、事前範囲を \(\chi\in[0,1]\) と一様に取ったときの値です。</strong> 降着の理論を事前に入れれば分布は一様でなくなり、驚きは小さくなります ── <em>「説明がある」ことと「驚きが小さい」ことは、第19回では同じことの言い換えです</em>。</p>
<p style="margin:0 0 10px"><strong>③ 04節の表は、同じ \(M\) どうしの比較です。</strong> 「回すとエントロピーが減る」という<em>過程</em>ではありません ── 回すには角運動量とともにエネルギーも入るので \(M\) が変わり、面積定理により実際の過程では面積は減りません。</p>
<p style="margin:0 0 10px"><strong>④ 宇宙検閲仮説は仮説であって、定理ではありません。</strong> 一般の場合の証明はなく、数値相対論では反例候補（高次元での不安定性など）も議論されています ── <em>03節の「運べない」は、カー解の族の内部で \(\chi\le1\) が地平面の存在条件だという意味</em>です。</p>
<p style="margin:0"><strong>⑤ 02節の「情報の半分が記法」は、第5回の値段（パラメータ 1 個 = 5.37 ビット）を使った言い方です。</strong> あの値は \(N=1701\) という特定のデータ点数から出た数で、<em>「2 個のうち 1 個が記法」という構造のほうが本質</em>です ── ビット数そのものは付随的な換算にすぎません。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>角運動量 \(J\) の共形ウェイトはいくつか。二通りで確かめよ。
<details><summary>答えを見る</summary><div class="ans"><strong>0</strong>。①次元から：\(J\sim ML^2/T\) なので \(-1+2\times(+1)-(+1)=0\)。②\(J\) は \(\hbar\) を単位に測る量で、\(\hbar\) はウェイト 0（第16回）。<em>二通りが一致するのが検算になります</em>。</div></details></li>

<li>カー解のラベル 2 個のうち、共形変換で動くのはどちらか。
<details><summary>答えを見る</summary><div class="ans">\(M\) だけ（ウェイト \(-1\)）。\(\chi=a/(GM/c^2)\) はウェイト 0 で<strong>動きません</strong> ── <em>第 II 部の「共形変換が触れるのは大きさだけ」の、いちばん綺麗な例</em>です。</div></details></li>

<li>\(\chi=1\) のカー BH のエントロピーは、同じ質量のシュヴァルツシルト BH の何倍か。
<details><summary>答えを見る</summary><div class="ans"><strong>ちょうど半分</strong>。\(A(\chi)/A(0)=(1+\sqrt{1-\chi^2})/2\) が \(\chi=1\) で \(1/2\) になるからです。太陽質量なら \(1.51\times10^{77}\) ビットが \(7.57\times10^{76}\) ビットに。ただし③のとおり、これは<em>同じ \(M\) どうしの比較であって過程ではありません</em>。</div></details></li>

<li>高スピン源が上限のすぐ下に並ぶことの驚きは何ビットか。それは【偶然】か。
<details><summary>答えを見る</summary><div class="ans">事前範囲を \(\chi\in[0,1]\) と取れば <strong>4.3 ビット</strong>で、第36回の偶然の帯（4〜7）に入ります。しかし<em>降着で角運動量を貰うという説明があり、ソーン限界 0.998 は光子捕獲で説明されます</em> ── だから第19回の分類では<strong>【物理】</strong>。①②の但し書きも参照してください。</div></details></li>

<li>（やや難）カーがこのシリーズにとって特別なのはなぜか。
<details><summary>答えを見る</summary><div class="ans">第33回の三段判定で<strong>第 3 段（ワイル \(\ne0\)）</strong>だからです。宇宙論で扱ってきた FLRW は全部<em>第 2 段（共形平坦）</em>で、共形変換で平坦にできました。<strong>カーは共形変換という道具が正面から届かない相手</strong>です ── ペトロフ型 D で、ワイル曲率が本質的にゼロにできません。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　二つのラベルのうち、動くのは一つ</h2>
<p>カー解のラベルは \(M\) と \(\chi=a/(GM/c^2)\) の二つ。ウェイト表に置くと \(M\) は \(-1\)、\(\chi\) は \(0\) ── <strong>片方だけが帳簿、片方は物理</strong>です。角運動量そのものもウェイト 0 で、これは \(J\) を \(\hbar\) を単位に測る量として数えても同じ結果になります（検算）。<em>第 II 部の結論「共形変換が触れるのは大きさだけ」の、いちばん綺麗な例</em>でした。第5回の値段で言えば、カー解の 10.7 ビットのうち <strong>5.37 ビットはまるごと記法</strong>です。</p>
<p>そして \(\chi\le1\) という上限 ── これは<strong>無次元量に置かれています</strong>。ウェイト 0 の列、つまり<em>どんな共形変換も、ブラックホールをこの線の向こう側へ運べません</em>。取り出せる質量の上限 \(1-1/\sqrt2=0.29289\) も、\(\chi=1\) のエントロピーが<strong>ちょうど半分</strong>になることも、同じ列にあります。</p>
<p>実測されたスピンは、その上限のすぐ下に並びます ── GRS 1915+105 で 0.98、Cyg X-1 で 0.95、そして降着で到達できるソーン限界が 0.998。第19回の作法で測ると <strong>高スピン源は 4.3 ビット、ソーン限界は 9.0 ビット</strong>で、<em>第36回の「偶然の帯」（4〜7）に戻ってきます</em>。ただし説明があるので、分類は【偶然】ではなく<strong>【物理】</strong> ── 第36回で見た「説明ありの 4〜7 ビット」の仲間です。</p>
<p>\(\chi\to1\) では温度がゼロになり、エントロピーは半分のまま \(7.6\times10^{76}\) ビット残ります ── <em>熱力学第三法則の素朴な形と衝突し</em>、「有限回の操作では届かない」という形で回避されます。<strong>第4回の「粗視化は不可逆」と同じ、近づけるが届かない線</strong>です。</p>
<p>最後にいちばん大事なこと。第33回の三段判定で、<strong>カーは第 3 段（ワイル \(\ne0\)）</strong>でした。宇宙論で扱ってきた FLRW は全部第 2 段で、共形変換で平坦にできた ── <em>カーは、この道具が正面から届かなくなる最初の相手</em>です。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第40回</span>
今回、<strong>ワイル曲率が消せない時空</strong>が出てきました（カー、シュヴァルツシルト）。次回は<strong>重力エントロピー</strong> ── 04節で数えた \(1.5\times10^{77}\) ビットは、<em>いったい何の情報なのか</em>。そして「重力場そのもののエントロピー」を測る候補が、<strong>まさにワイル曲率だ</strong>という話へ進みます。第41回の<em>ワイル曲率仮説</em>への入口です。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sc=document.getElementById('sc'), vc=document.getElementById('vc'), ro=document.getElementById('ro');
  var X0=76, X1=690, Y0=34, Y1=300;

  function px(x){ return X0+x*(X1-X0); }
  function py(y){ return Y1-y*(Y1-Y0); }
  function area(x){ return (1+Math.sqrt(Math.max(0,1-x*x)))/2; }
  function extr(x){ return 1-Math.sqrt(area(x)); }
  function temp(x){ var r=Math.sqrt(Math.max(0,1-x*x)); return (r/(1+r))/0.5; }

  function curve(f,col,w){
    g.strokeStyle=col; g.lineWidth=w; g.beginPath();
    for(var i=0;i<=300;i++){ var x=i/300, X=px(x), Y=py(f(x)); if(i===0)g.moveTo(X,Y); else g.lineTo(X,Y); }
    g.stroke();
  }

  function draw(){
    var chi=parseInt(sc.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var v=0;v<=1.0001;v+=0.25){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(v)); g.lineTo(X1,py(v)); g.stroke();
      g.fillText(v.toFixed(2), X0-8, py(v)+4);
    }
    g.textAlign='center';
    for(var t=0;t<=1.0001;t+=0.2){
      g.fillStyle='#9c96a4'; g.fillText(t.toFixed(1), px(t), Y1+20);
    }

    // 実測の縦線
    var obs=[[0.686,'合体後 0.686'],[0.95,'Cyg X-1'],[0.998,'ソーン限界']];
    for(var i=0;i<obs.length;i++){
      var X=px(obs[i][0]);
      g.strokeStyle='#e2dce6'; g.lineWidth=1; g.setLineDash([2,3]);
      g.beginPath(); g.moveTo(X,Y0); g.lineTo(X,Y1); g.stroke(); g.setLineDash([]);
      g.save(); g.translate(X-4,Y0+56); g.rotate(-Math.PI/2);
      g.fillStyle='#a89fae'; g.textAlign='left'; g.fillText(obs[i][1],0,0); g.restore();
    }

    curve(area,'#7a5a2a',2.6);
    curve(extr,'#2a6a5a',2.4);
    curve(temp,'#a03a3a',2.0);

    g.textAlign='left';
    g.fillStyle='#7a5a2a'; g.fillText('地平面の面積 A/A(0)', X0+10, py(area(0.12))-8);
    g.fillStyle='#a03a3a'; g.fillText('ホーキング温度 T/T(0)', px(0.30), py(temp(0.30))+16);
    g.fillStyle='#2a6a5a'; g.fillText('取り出せる質量の割合', px(0.55), py(extr(0.55))-10);

    for(var j=0;j<3;j++){
      var f=[area,extr,temp][j], col=['#7a5a2a','#2a6a5a','#a03a3a'][j];
      g.fillStyle=col; g.beginPath(); g.arc(px(chi),py(f(chi)),4.2,0,6.29); g.fill();
    }
    g.strokeStyle='#5a5262'; g.lineWidth=1.6; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(chi),Y0); g.lineTo(px(chi),Y1); g.stroke(); g.setLineDash([]);

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('スピン χ = a / (GM/c²)　── 無次元、共形変換で動かない', (X0+X1)/2, Y1+42);

    vc.textContent=chi.toFixed(3);
    ro.textContent='χ = '+chi.toFixed(3)+
      '　→　面積 '+area(chi).toFixed(4)+
      '　／　エントロピー '+(1.514e77*area(chi)).toExponential(2)+' bit（太陽質量）'+
      '　／　取り出せる質量 '+(100*extr(chi)).toFixed(2)+' パーセント'+
      '　／　温度 '+temp(chi).toFixed(4)+
      (chi>0.995?'　★ 温度はゼロへ、エントロピーは半分のまま有限':'');
  }
  sc.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-39-kerr.html', acc='#7a5a2a', ops='#2a6a5a',
      title='回転する時空 ── わかる c·t=一定 第39回（第V部）',
      ep='第 39 回 ／ 第 V 部・道具が壊れる場所',
      eyebrow='二つのラベルのうち、動くのは一つだけ',
      h1='触れられない列に、<br>置かれた上限',
      sub='カー解のラベルは \\(M\\) と \\(\\chi\\)。片方だけが帳簿、片方は物理です。<br><em>そして \\(\\chi\\le1\\) は、共形変換では越えられません。</em>',
      byline_l='必要な道具：第16回のウェイト表、第19回の目盛り、第33回の三段判定、第36回の帯',
      byline_r='\\(1-1/\\sqrt2=0.29289\\) ── 取り出せる質量の上限',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第39回（第 V 部の 3 回目）、物理好きの高校生・大学生向け読み物です。カー解、面積・エントロピーの表式、既約質量、ソーン限界（Thorne 1974）、Israel の第三法則はいずれも標準的な内容で、本稿に新しい主張はありません ── 数値は kenshou/calc43.py で計算しています。<strong>05節のスピン測定値はいずれもモデル依存が大きく</strong>、連続スペクトル法と鉄輝線（反射）法で結果が食い違う天体があります（GRS 1915+105 は 0.98 とも 0.7 前後とも報告されています）── <em>「高スピン源が上限のすぐ下に並ぶ」という言い方は高スピンを報告した測定だけを並べたもので、選び方にバイアスがあります</em>。05節の 4.3 ビットは事前範囲を \\(\\chi\\in[0,1]\\) と一様に取ったときの値で、降着の理論を事前に入れれば驚きは小さくなります。<strong>04節の表は同じ \\(M\\) どうしの比較であって「回すとエントロピーが減る」過程ではありません</strong> ── 回すにはエネルギーも入るので \\(M\\) が変わり、面積定理により実際の過程で面積は減りません。<strong>宇宙検閲仮説は仮説であって定理ではなく</strong>、一般の場合の証明はありません ── 03節の「運べない」はカー解の族の内部で \\(\\chi\\le1\\) が地平面の存在条件だという意味です。02節の「情報の半分が記法」は第5回の値段（\\(N=1701\\) から出た 5.37 ビット）を使った言い方で、<em>「2 個のうち 1 個が記法」という構造のほうが本質</em>です。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミでスピンを動かすと、三つの無次元量が同時に動きます。「答えを見る」で解答が開きます。')
