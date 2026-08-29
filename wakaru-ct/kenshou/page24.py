# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第17回で「合意に必要だった情報は 20 KB、問題はチャネルが無かったこと」と数えました。ではチャネルは、どれだけ<em>太い</em>のか。第1回で \(dN/dt=1.36\times10^{105}\) bit/s と数えましたが、あれは<strong>容量が増える速さ</strong>であって通信速度ではありません。今回は帯域そのものを求めます ── そして二つの数のあいだに、<em>きれいな恒等式</em>が出ます。</p>

<h2><span class="n">01</span>二つの「毎秒ビット」を、区別する</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">意味</th><th class="mid">値</th></tr></thead>
<tbody>
<tr><th>\(dN/dt\)</th><td class="mid">容量が増える速さ（第1回）</td><td class="mid">\(1.36\times10^{105}\) bit/s</td></tr>
<tr class="hi"><th>\(C\)</th><td class="mid"><strong>通信路容量</strong>（今回）</td><td class="mid"><strong>\(6.79\times10^{104}\) bit/s</strong></td></tr>
</tbody>
</table>
</div>

<p>帯域のほうは、ベケンシュタイン境界を「信号が横断する時間」で割って出します。半径 \(R\) の系に入る情報は \(S\le2\pi ER/\hbar c\)、横断時間は \(R/c\) なので ──</p>

<div class="calc">
<span class="tag">通信路容量</span>
$$C\ \le\ \frac{2\pi ER/\hbar c}{R/c}=\frac{2\pi E}{\hbar}\ [\text{nat/s}]\qquad\Longrightarrow\qquad C=\frac{2\pi E}{\hbar\ln2}\ [\text{bit/s}]$$
<p class="lbl">地平面内の全エネルギー \(E=7.90\times10^{69}\) J を入れて</p>
$$C=6.79\times10^{104}\ \mathrm{bit/s}$$
</div>

<h2><span class="n">02</span>核心 ── 帯域 × 年齢 ＝ メモリ</h2>

<p>二つの数の比を取ると、ちょうど 2.000000。偶然ではありません。</p>

<div class="calc">
<span class="tag">計算 ── 三行</span>
<p class="lbl">\(E=c^4R/2G\) と \(\ell_P^2=\hbar G/c^3\) を入れると</p>
$$C=\frac{2\pi}{\hbar\ln2}\cdot\frac{c^4R}{2G}=\frac{\pi cR}{\ell_P^2\ln2}$$
<p class="lbl">一方 \(N=\pi R^2/(\ell_P^2\ln2)\) で \(R=ct\) なので</p>
$$C\cdot t=\frac{\pi cR}{\ell_P^2\ln2}\cdot\frac{R}{c}=\frac{\pi R^2}{\ell_P^2\ln2}=N$$
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
$$\boxed{\ C\cdot t=N\ }$$
<p style="margin:10px 0 0"><strong>宇宙は、1 ハッブル時間で自分のメモリ全体をちょうど 1 回だけ動かせる帯域を持っています。</strong><br>
── 多くも少なくもなく、<em>ぴったり 1 回ぶん</em>。</p>
</div>

<p>そして \(N\propto t^2\) なので \(dN/dt=2N/t=2C\) ── 第1回の数と今回の数が 2 倍だったのは、<strong>同じ恒等式の裏表</strong>でした。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>言い方</th><th class="mid">式</th><th class="mid">意味</th></tr></thead>
<tbody>
<tr class="hi"><th>帯域で読む</th><td class="mid">\(C\cdot t=N\)</td><td class="mid">1 ハッブル時間で、メモリ全体を 1 回動かせる</td></tr>
<tr><th>増設で読む</th><td class="mid">\(dN/dt=2C\)</td><td class="mid">メモリは、動かせる速さの 2 倍で増える</td></tr>
</tbody>
</table>
</div>

<p>第19回の分類で言えば、これは<strong>恒等式 ── 驚き 0 ビット</strong>です。\(E=c^4R/2G\)（ディラックの大数）とホログラフィーから自動的に出ます。<em>それでも、宇宙という計算機の設計を読むには使えます。</em></p>

<h2><span class="n">03</span>第17回の 20 KB は、一瞬で送れた</h2>

<p>帯域が出たので、第17回の宿題を片付けます ── 地平線問題の「合意すべき 20 KB」は、送るのにどれだけかかったのでしょうか。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>時代</th><th class="mid">帯域 \(C\)</th><th class="mid">20 KB の送信時間</th></tr></thead>
<tbody>
<tr><th>元素合成（\(t=1\) s）</th><td class="mid">\(1.56\times10^{87}\) bit/s</td><td class="mid">\(1.0\times10^{-82}\) 秒</td></tr>
<tr class="hi"><th>再結合（38 万年）</th><td class="mid">\(1.87\times10^{100}\) bit/s</td><td class="mid"><strong>\(8.6\times10^{-96}\) 秒</strong></td></tr>
<tr><th>今日</th><td class="mid">\(6.79\times10^{104}\) bit/s</td><td class="mid">\(2.4\times10^{-100}\) 秒</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">03節の結論</p>
<p style="margin:6px 0 0">チャネルさえあれば、地平線問題の 20 KB は <strong>\(10^{-96}\) 秒</strong>で送れました。<br>
<em>問題は帯域ではなく、チャネルが存在しなかったこと</em> ── 第17回の結論が、数字で裏づきます。</p>
</div>

<div class="fig">
<p class="cap">図：時代ごとの帯域 \(C\)（傾き 1）と、そのときのメモリ \(N\)（傾き 2）。<strong>\(C\cdot t=N\) なので、二本は必ず \(t\) だけ離れます</strong>。ツマミで時代を動かすと、20 KB の送信時間が読み出せます</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>いつの時代で見るか \(\log_{10}(t/\mathrm{s})\)（右端が今日）<input id="st" type="range" min="-440" max="180" value="180" step="1"></label>
  <span class="val" id="vt">今日</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1a4a3a"></i>メモリ \(N\)（傾き 2）</span>
  <span><i class="swatch" style="background:#a04a2a"></i>帯域 \(C\)（傾き 1）</span>
  <span><i class="swatch" style="background:#9ab0a6"></i>第17回の 20 KB</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>1 粒子あたりの帯域</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>系</th><th class="mid">エネルギー</th><th class="mid">原理上の帯域</th></tr></thead>
<tbody>
<tr class="hi"><th>CMB 光子 1 個</th><td class="mid">\(2.35\times10^{-4}\) eV</td><td class="mid"><strong>\(3.2\times10^{12}\) bit/s</strong></td></tr>
<tr><th>陽子 1 個</th><td class="mid">938 MeV</td><td class="mid">\(1.3\times10^{25}\) bit/s</td></tr>
<tr><th>1 kg の物質</th><td class="mid">\(9.0\times10^{16}\) J</td><td class="mid">\(7.7\times10^{51}\) bit/s</td></tr>
</tbody>
</table>
</div>

<p><strong>CMB 光子 1 個は、原理上は毎秒 3 兆ビットを運べます。</strong> 実際に運んでいるのは数ビット（温度と偏光）── ここでも「能力に対して、まったく使っていない」という同じ絵になります。</p>

<div class="calc">
<span class="tag">人間の作ったものと比べる</span>
<p class="lbl">世界のインターネット総トラフィック（おおよそ）</p>
$$1.3\times10^{15}\ \mathrm{bit/s}$$
<p class="lbl">1 kg の物質の原理上の帯域に対して</p>
$$1.7\times10^{-37}\qquad(\text{地平面に対しては }1.9\times10^{-90})$$
</div>

<h2><span class="n">05</span>種明かし ── 使っていないのは、能力不足ではない</h2>

<p>ここまでの三つを並べます。</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>帯域は、メモリ 1 回ぶん／ハッブル時間ある</strong><span>\(C\cdot t=N\)。動かす力は、必要十分に用意されている</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>ところが演算は 1 ビットあたり 0.035 回</strong><span>第1回。しかもその 95% は何も起きない成分の取り分（第22回）</span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>だから「使っていない」のは能力不足ではない</strong><span>帯域も容量も足りている。使われていないだけ ── <em>宇宙は、性能を持て余している</em></span></div></div>
</div>

<p>第6回で「メモリの \(10^{-18}\) しか使っていない」、第22回で「演算資源の 95% は何も起きない成分」、今回で「帯域はメモリ 1 回ぶんある」。<strong>三方向から同じ結論に着きました</strong> ── 宇宙という計算機は、<em>スペックに対して圧倒的に働いていない</em>。</p>

<div class="aside">
<span class="tag">では、何がボトルネックなのか</span>
性能ではないとすれば、何が制限しているのか。第17回の答えがそれでした ── <strong>チャネルの「太さ」ではなく「有無」</strong>。因果的に切れていれば、帯域が \(10^{100}\) bit/s あっても 1 ビットも渡りません。<em>宇宙という計算機のボトルネックは、帯域でも容量でもなく、配線（因果構造）です。</em> そして配線を決めるのは膨張則 ── 第17回で見た通り、\(a\propto t\) だけがノードを増やしません。
</div>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① \(C=2\pi E/(\hbar\ln2)\) は、ベケンシュタイン境界を横断時間で割った見積もりです。</strong> ブレーメルマン限界と同型の量ですが、係数は導出の仕方（境界の形、\(R\) の取り方）に依存します ── \(\pi\) 程度の因子は動きます。第1回のマルゴラス＝レヴィティン限界（\(2E/\pi\hbar\)）とは \(\pi^2\) 違いますが、これも規約の違いです。</p>
<p style="margin:0 0 10px"><strong>② \(C\cdot t=N\) は恒等式です</strong>（第19回の分類で驚き 0 ビット）。\(E=c^4R/2G\) というディラックの大数の恒等式と、ホログラフィー \(N\propto R^2\) から自動的に出ます。<em>「宇宙が帯域をぴったり用意している」という物理的な主張ではありません。</em></p>
<p style="margin:0 0 10px"><strong>③ 03節の送信時間は、帯域だけで割った値です。</strong> 実際には信号が距離を渡る時間（\(R/c\)、再結合なら 38 万年）がかかります ── <em>「帯域はボトルネックにならない」ことを示すための計算</em>であって、20 KB が \(10^{-96}\) 秒で相手に届くという意味ではありません。</p>
<p style="margin:0 0 10px"><strong>④ 「CMB 光子 1 個が毎秒 3 兆ビット」も原理上の上限です。</strong> 実際の光子が運ぶのは、その振動数・偏光・到来方向という数ビットです。</p>
<p style="margin:0"><strong>⑤ インターネットの \(1.3\times10^{15}\) bit/s は桁の目安です。</strong> 何を「トラフィック」に数えるかで数倍動きます。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>\(dN/dt\) と \(C\) の違いを述べよ。
<details><summary>答えを見る</summary><div class="ans">\(dN/dt\) は<strong>容量が増える速さ</strong>（新しく書ける場所がどれだけ増えるか）、\(C\) は<strong>通信路容量</strong>（既にある情報をどれだけ動かせるか）。まったく別の量ですが、\(dN/dt=2C\) という恒等式で結ばれています。</div></details></li>

<li>\(C\cdot t=N\) を示せ。
<details><summary>答えを見る</summary><div class="ans">\(C=2\pi E/(\hbar\ln2)\) に \(E=c^4R/2G\) と \(\ell_P^2=\hbar G/c^3\) を入れると \(C=\pi cR/(\ell_P^2\ln2)\)。これに \(t=R/c\) を掛けると \(\pi R^2/(\ell_P^2\ln2)=N\)。<strong>1 ハッブル時間で、メモリ全体をちょうど 1 回動かせる</strong>。</div></details></li>

<li>再結合のとき、20 KB を送るのにどれだけかかるか。
<details><summary>答えを見る</summary><div class="ans">\(C=1.87\times10^{100}\) bit/s なので \(1.6\times10^5/1.87\times10^{100}=8.6\times10^{-96}\) 秒。<strong>帯域はまったくボトルネックではありません</strong> ── 第17回の「問題はチャネルの有無」が裏づきます。</div></details></li>

<li>CMB 光子 1 個の原理上の帯域は。
<details><summary>答えを見る</summary><div class="ans">\(C=2\pi E/(\hbar\ln2)\) に \(E=2.35\times10^{-4}\) eV \(=3.76\times10^{-23}\) J を入れて <strong>\(3.2\times10^{12}\) bit/s</strong>。実際に運んでいるのは数ビットです。</div></details></li>

<li>（やや難）宇宙という計算機のボトルネックは何か。
<details><summary>答えを見る</summary><div class="ans"><strong>配線（因果構造）</strong>です。容量は \(10^{-18}\) しか使われておらず（第6回）、演算資源の 95% は何も起きない成分の取り分で（第22回）、帯域はメモリ 1 回ぶん用意されている（今回）── <em>性能はどれも余っています</em>。制限しているのは、因果的に切れていると帯域がいくらあっても 1 ビットも渡らないこと（第17回）。そして配線を決めるのは膨張則です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　帯域 × 年齢 ＝ メモリ</h2>
<p>二つの「毎秒ビット」を区別しました ── \(dN/dt=1.36\times10^{105}\) bit/s は<em>容量が増える速さ</em>、\(C=2\pi E/(\hbar\ln2)=6.79\times10^{104}\) bit/s が<em>通信路容量</em>です。後者はベケンシュタイン境界を横断時間で割って出しました。</p>
<p>比はちょうど 2.000000 で、これは恒等式でした ── \(E=c^4R/2G\) とホログラフィーから \(C=\pi cR/(\ell_P^2\ln2)\)、したがって <strong>\(C\cdot t=N\)</strong>。<em>宇宙は、1 ハッブル時間で自分のメモリ全体をちょうど 1 回だけ動かせる帯域を持っています</em> ── 多くも少なくもなく、ぴったり 1 回ぶん。第1回の数と 2 倍だったのは、\(N\propto t^2\) の裏返しにすぎません。</p>
<p>おかげで第17回の宿題が片付きました。地平線問題の 20 KB は、再結合のときの帯域なら <strong>\(10^{-96}\) 秒</strong>で送れます。<em>帯域はまったくボトルネックではない</em> ── 問題はチャネルの太さではなく、その<strong>有無</strong>でした。</p>
<p>そして三方向から同じ結論に着きました ── 容量は \(10^{-18}\) しか使われず（第6回）、演算資源の 95% は何も起きない成分の取り分で（第22回）、帯域はメモリ 1 回ぶん余っている（今回）。<strong>「使っていない」のは能力不足ではありません。</strong> 宇宙という計算機のボトルネックは、帯域でも容量でもなく<em>配線（因果構造）</em>であり、それを決めるのは膨張則です。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第25回</span>
第 III 部もあと二回。次は<strong>物理法則は圧縮アルゴリズムか</strong>という問いを、まじめに数えます。第5回で「\(\Lambda\)CDM は 6 個のパラメータで \(6.3\times10^6\) 個の多重極を説明する」と書きました ── <em>圧縮率 \(10^6\) 倍</em>。では標準模型は？ 19 個のパラメータで、これまでに測られた全ての散乱断面積を。そして一般相対論は？ <strong>パラメータ 0 個</strong>。<em>物理法則を圧縮率で並べると、どれがいちばん「良い」のか</em> ── そして<strong>圧縮率が高すぎる理論には、共通の弱点があります</strong>。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var st=document.getElementById('st'), vt=document.getElementById('vt'), ro=document.getElementById('ro');
  var X0=78, X1=700, Y0=30, Y1=314;
  var c=299792458.0, lP=1.616255e-35, ln2=Math.log(2), PI=Math.PI;
  var xmin=-45, xmax=19, ymin=-5, ymax=130;
  var BITS=1.6e5;
  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function lg(v){ return Math.log(v)/Math.LN10; }
  function Nof(t){ var R=c*t; return PI*R*R/(lP*lP*ln2); }
  function Cof(t){ var R=c*t; return PI*c*R/(lP*lP*ln2); }
  function draw(){
    var lt=parseInt(st.value,10)/10;
    var t=Math.pow(10,lt);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.textAlign='right';
    for(var e=0;e<=130;e+=20){
      var y=py(e);
      g.strokeStyle='#eef3f0'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#93a89c'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-40;q<=10;q+=10){
      var x=px(q);
      g.strokeStyle='#f5f9f6'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#93a89c'; g.fillText('10'+q, x, Y1+16);
    }
    g.strokeStyle='#c3d6c9'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();
    // 20KB の線
    g.strokeStyle='#9ab0a6'; g.lineWidth=1.8; g.setLineDash([6,5]);
    g.beginPath(); g.moveTo(X0,py(lg(BITS))); g.lineTo(X1,py(lg(BITS))); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#7d938a'; g.textAlign='left';
    g.fillText('第17回の 20 KB（1.6×10⁵ bit）', X0+10, py(lg(BITS))-7);
    function curve(fn,col,w){
      g.strokeStyle=col; g.lineWidth=w; g.beginPath();
      var first=true;
      for(var i=0;i<=300;i++){
        var lx=xmin+(xmax-xmin)*i/300;
        var y=lg(fn(Math.pow(10,lx)));
        if(y<ymin||y>ymax){ first=true; continue; }
        if(first){ g.moveTo(px(lx),py(y)); first=false; } else g.lineTo(px(lx),py(y));
      }
      g.stroke();
    }
    curve(Nof,'#1a4a3a',3.2);
    curve(Cof,'#a04a2a',3.2);
    g.textAlign='left';
    g.fillStyle='#1a4a3a'; g.fillText('メモリ N（傾き 2）', px(-8), py(lg(Nof(1e-8)))-10);
    g.fillStyle='#a04a2a'; g.fillText('帯域 C（傾き 1）', px(-8), py(lg(Cof(1e-8)))+18);
    g.strokeStyle='#5a7a68'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(lt),Y0); g.lineTo(px(lt),Y1); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#7d938a'; g.textAlign='center';
    g.fillText('宇宙の年齢  t [秒]', (X0+X1)/2, Y1+36);
    var C=Cof(t), N=Nof(t);
    vt.textContent = (lt>17.5?'今日':'10^'+lt.toFixed(1)+' 秒');
    ro.textContent='t = '+t.toExponential(2)+' 秒　'+
      'メモリ '+N.toExponential(2)+' bit　帯域 '+C.toExponential(2)+' bit/s'+
      '　→　C×t = '+(C*t).toExponential(2)+'（＝N）'+
      '　／　20KB の送信に '+(BITS/C).toExponential(2)+' 秒';
  }
  st.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-24-channel.html', acc='#1a4a3a', ops='#a04a2a',
      title='地平面を、毎秒何ビットが渡れるか ── わかる c·t=一定 第24回',
      ep='第 24 回 ／ 容量が増える速さと、通信速度は別物',
      eyebrow='帯域 × 年齢 ＝ メモリ ── ぴったり 1 回ぶんでした',
      h1='地平面を、毎秒<br>何ビットが渡れるか',
      sub='第17回の「20 KB を送る手段が無かった」に、帯域という数字を入れます。<br><em>そして帯域はまったくボトルネックではありませんでした。</em>',
      byline_l='必要な道具：ベケンシュタイン境界、割り算',
      byline_r='\\(C\\cdot t=N\\)',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第24回、物理好きの高校生・大学生向け読み物です。ベケンシュタイン境界 \\(S\\le2\\pi ER/\\hbar c\\) は標準的で、それを横断時間 \\(R/c\\) で割って通信路容量 \\(C=2\\pi E/(\\hbar\\ln2)\\) を得る手続きはブレーメルマン限界と同型ですが、<strong>係数は導出の仕方（境界の形、\\(R\\) の取り方）に依存します</strong> ── 第1回のマルゴラス＝レヴィティン限界（\\(2E/\\pi\\hbar\\)）との \\(\\pi^2\\) の違いも規約によるものです。本稿の \\(C=6.79\\times10^{104}\\) bit/s、\\(C=\\pi cR/(\\ell_P^2\\ln2)\\)、および恒等式 \\(C\\cdot t=N\\)、\\(dN/dt=2C\\) は本稿での導出です（kenshou/calc28.py）。<strong>これは恒等式であり</strong>（\\(E=c^4R/2G\\) というディラックの大数の恒等式とホログラフィー \\(N\\propto R^2\\) から自動的に従う）、「宇宙が帯域をぴったり用意している」という物理的主張ではありません（第19回の分類で驚き 0 ビット）。03節の送信時間は帯域だけで割った値であり、<em>信号が距離を渡る時間（再結合なら 38 万年）は別途かかります</em> ── 「帯域はボトルネックにならない」ことを示すための計算です。1 粒子あたりの帯域も原理上の上限で、実際の CMB 光子が運ぶのは振動数・偏光・到来方向という数ビットです。インターネットの \\(1.3\\times10^{15}\\) bit/s は桁の目安で、何をトラフィックに数えるかで数倍動きます。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルで、\\(R_H=ct\\) はその規約です（\\(\\Lambda\\)CDM では \\(R_H=c/H_0\\) と粒子的地平線が異なります）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで時代を動かし、C×t=N が保たれる様子が見えます。「答えを見る」で解答が開きます。')
