# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第7回で重力に入れました。今回は量子力学です。結論から言うと、<strong>シュレディンガー方程式は一文字も書き換わりません</strong> ── ただし質量が \(m(t)=m_0\,t/t_0\) になる。そこから、ちょっと信じがたい帰結が出ます。<em>自由な波束が、時間に比例してではなく、対数でしか広がらない。</em> 積み上げると「物質は歩けなくなるが、光は歩き続ける」という一行になります。</p>

<h2><span class="n">01</span>まず、方程式が形を保つことを確かめる</h2>

<p>シュレディンガー方程式を書きます。</p>

<div class="calc">
<span class="tag">変換する相手</span>
$$i\hbar\frac{\partial\psi}{\partial t}=\left[-\frac{\hbar^2}{2m}\nabla^2+V\right]\psi$$
</div>

<p>\(\psi\) のウェイトは、規格化から決まります。\(\int|\psi|^2d^3x=1\) で \(d^3x\) がウェイト \(+3\) なので、\(|\psi|^2\) は \(-3\)、つまり \(\psi\) は \(-3/2\)。あとは各項を数えるだけです。</p>

<div class="calc">
<span class="tag">計算 ── 両辺のウェイトを数える</span>
<p class="lbl">左辺 \(i\hbar\,\partial\psi/\partial t\)</p>
$$\underbrace{0}_{\hbar}+\underbrace{(-3/2)}_{\psi}+\underbrace{(-1)}_{\partial/\partial t}=-\frac52$$
<p class="lbl">右辺 \(\hbar^2\nabla^2\psi/2m\)</p>
$$\underbrace{0}_{\hbar^2}-\underbrace{(-1)}_{1/m}+\underbrace{(-2)}_{\nabla^2}+\underbrace{(-3/2)}_{\psi}=+1-2-\frac32=-\frac52$$
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0">両辺とも \(-5/2\)。<strong>シュレディンガー方程式は、この絵でも一文字も変わりません。</strong><br>
変わるのは、そこに入っている質量だけ ── \(m(t)=m_0\,t/t_0\)。</p>
</div>

<p>これは第4回の「消せるものを全部消すと質量ひとつが残る」の、量子力学版です。<em>量子力学には、質量以外に共形変換にひっかかる相手がいない。</em></p>

<h2><span class="n">02</span>核心 ── 波束が、対数でしか広がらない</h2>

<p>自由粒子を考えます。力がないので運動量は保存し、速度は \(v=p/m\)。ところが \(m\) が \(t\) に比例して育つので ──</p>

<div class="calc">
<span class="tag">計算 ── 二行</span>
$$v(t)=\frac{p}{m_0\,t/t_0}=\frac{p\,t_0}{m_0\,t}\ \propto\ \frac{1}{t}$$
<p class="lbl">積分すると</p>
$$\Delta x(t)=\int v\,dt\ \propto\ \ln t$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th class="mid">標準の絵</th><th class="mid">この絵</th></tr></thead>
<tbody>
<tr><th>質量</th><td class="mid">一定</td><td class="mid">\(\propto t\)</td></tr>
<tr><th>自由粒子の速度</th><td class="mid">一定</td><td class="mid">\(\propto 1/t\)</td></tr>
<tr class="hi"><th>波束の広がり</th><td class="mid">\(\Delta x\propto t\)</td><td class="mid"><strong>\(\Delta x\propto\ln t\)</strong></td></tr>
</tbody>
</table>
</div>

<p>実験室では気づけません。\(\dot m/m=H_0\) は 138 億年で 1 なので、\(10^{-14}\) 秒で広がる電子の波束にとっては完全に無視できる。<strong>効いてくるのは、宇宙のスケールで積分したときだけ</strong>です。</p>

<h2><span class="n">03</span>積み上げる ── 物質の到達距離は、有限</h2>

<p>時刻 \(t_1\) に速度 \(v_1\) で走り出した粒子が、その後<em>永遠に</em>進み続けたとして、共動座標でどこまで行けるかを積分します。</p>

<div class="calc">
<span class="tag">計算 ── 物質と光を、並べて積分する</span>
<p class="lbl">質量を持つもの（速度が \(1/a\) で落ちる）</p>
$$\Delta\chi=\int_{t_1}^{\infty}\frac{v_1(t_1/t)}{t/t_1}\,dt=v_1t_1^2\int_{t_1}^{\infty}\frac{dt}{t^2}=\boxed{\,v_1t_1\,}$$
<p class="lbl">光</p>
$$\Delta\chi=\int_{t_1}^{\infty}\frac{c\,dt}{t/t_1}=c\,t_1\ln\frac{t}{t_1}\ \longrightarrow\ \infty$$
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>物質は歩けなくなる。光は歩き続ける。</strong><br>
質量を持つものの共動到達距離は \(v_1t_1\) で頭打ち ── <em>最初の 1 ハッブル時間で進む距離が、永遠ぶんの上限</em>です。</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>走り出すもの</th><th class="mid">初速</th><th class="mid">出発時刻</th><th class="mid">永遠ぶんの到達距離 \(v_1t_1\)</th></tr></thead>
<tbody>
<tr><th>再結合期の水素原子</th><td class="mid">5 km/s</td><td class="mid">38 万年</td><td class="mid"><strong>1.9 パーセク</strong></td></tr>
<tr><th>銀河（今日の固有速度）</th><td class="mid">600 km/s</td><td class="mid">今日</td><td class="mid">8.5 Mpc</td></tr>
<tr><th>熱い電子（今日）</th><td class="mid">1000 km/s</td><td class="mid">今日</td><td class="mid">14.1 Mpc</td></tr>
<tr class="hi"><th>光（今日）</th><td class="mid">\(c\)</td><td class="mid">今日</td><td class="mid"><strong>無限</strong>（\(4230\,\mathrm{Mpc}\times\ln(t/t_0)\)）</td></tr>
</tbody>
</table>
</div>

<p>一行目が効きます。<strong>再結合のときにいた水素原子は、宇宙の全歴史をかけても、共動で 2 パーセクしか動けません。</strong> CMB に焼き付いた模様が「その場に凍りついたまま」で、あとは重力で成長するしかないのは、この積分のせいです。</p>

<div class="aside">
<span class="tag">光速で走っても、追い抜かれる</span>
初速を \(c\) にしても到達距離は \(c\,t_1\) で頭打ちです（実際には質量があれば \(c\) には届きませんが、上限として）。一方その時刻に出発した光は \(c\,t_1\ln(t/t_1)\)。追い抜かれるのは \(\ln(t/t_1)=1\)、つまり <strong>宇宙が \(e=2.72\) 倍の年齢になったとき</strong>。<em>どんなに速く走り出しても、ひと桁も経たないうちに光に置いていかれる。</em>
</div>

<div class="fig">
<p class="cap">図：今日出発した粒子が、その後どこまで届くか（共動距離）。<strong>物質の線は必ず頭打ちになり、光の線は伸び続けます</strong>。ツマミで初速を変えると、頭打ちの高さだけが動きます</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>初速 \(v_1\)（対数、右端が光速）<input id="sv" type="range" min="0" max="1000" value="270" step="1"></label>
  <span class="val" id="vv">600 km/s</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1d3f56"></i>質量を持つもの（頭打ちになる）</span>
  <span><i class="swatch" style="background:#9a5a1e"></i>光（伸び続ける）</span>
  <span><i class="swatch" style="background:#94a3ac"></i>頭打ちの高さ \(v_1t_0\)</span>
</div>
</div>

<p>ツマミを右端（光速）まで振っても、青い線は必ず水平になります。<em>頭打ちになるかならないかは、速さの問題ではありません</em> ── 質量を持つかどうかの問題です。質量があれば速度が \(1/a\) で落ち、積分が収束する。質量がなければ落ちず、対数で発散する。</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>動くもの・動かないものを、一覧にする</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">ウェイト</th><th class="mid">この絵で</th></tr></thead>
<tbody>
<tr class="hi"><th>不確定性 \(\Delta x\Delta p\ge\hbar/2\)</th><td class="mid">\(0\)</td><td class="mid"><strong>不変</strong></td></tr>
<tr class="hi"><th>作用 \(S/\hbar\)</th><td class="mid">\(0\)</td><td class="mid"><strong>不変</strong></td></tr>
<tr class="hi"><th>トンネル透過率 \(e^{-2\int\kappa\,dx}\)</th><td class="mid">\(0\)</td><td class="mid"><strong>不変</strong></td></tr>
<tr><th>ド・ブロイ波長 \(h/p\)</th><td class="mid">\(+1\)</td><td class="mid">\(\div a\)</td></tr>
<tr><th>コンプトン波長 \(\hbar/mc\)</th><td class="mid">\(+1\)</td><td class="mid">\(\div a\)</td></tr>
<tr><th>熱ド・ブロイ波長 \(h/\sqrt{2\pi mk_BT}\)</th><td class="mid">\(+1\)</td><td class="mid">\(\div a\)</td></tr>
<tr><th>エネルギー準位</th><td class="mid">\(-1\)</td><td class="mid">\(\times a\)</td></tr>
</tbody>
</table>
</div>

<p>三行目を味わってください。<strong>トンネル効果の透過率は、完全に不変です。</strong> 指数の中身 \(\int\kappa\,dx\) は、\(\kappa=\sqrt{2m(V-E)}/\hbar\) がウェイト \(-1\)、\(dx\) が \(+1\) なので、掛けて \(0\)。だから ──</p>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0">太陽が燃える速さも、原子核の \(\alpha\) 崩壊の半減期も、走査トンネル顕微鏡の像も、<br>
この絵で<strong>一切変わりません</strong>。すべて無次元の指数だけで決まっているからです。</p>
</div>

<h2><span class="n">05</span>種明かし ── 世界は、時代とともに古典的になる</h2>

<p>不変なものが多いのに、一つだけ着実に動く無次元量があります。前シリーズ第6回で出てきた、あれです。</p>

<div class="calc">
<span class="tag">動く無次元量</span>
$$N=\frac{\text{見ている系の大きさ}}{\text{コンプトン波長}}=\frac{mc^2t}{\hbar}$$
<p class="lbl">今日の値</p>
$$N(\text{電子})=3.38\times10^{38},\qquad N(\text{水素原子})=6.21\times10^{41}$$
</div>

<p>標準の絵では「宇宙が大きくなるから \(N\) が増える」と読みます。この絵では<strong>宇宙は膨張していない</strong>ので、読み方が変わります ── <em>コンプトン波長のほうが縮んでいくから \(N\) が増える</em>。物差しが太り、量子的な粒度が細かくなっていく。</p>

<div class="keybox">
<p class="lbl">05節の結論</p>
<p style="margin:6px 0 0"><strong>宇宙は、時代とともに古典的になっていく。</strong><br>
\(N\propto t\) は「古典的な記述がどれだけ効くか」の目盛りで、これだけは共形変換で動かせません。<br>
── 前シリーズ第6回で「消えたのは幾何、残ったのは比」と言った、その比です。</p>
</div>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① シュレディンガー方程式は非相対論的な近似です。</strong> ウェイトの数え上げが両辺で一致するのは、\(V\) もエネルギー（ウェイト \(-1\)）として一緒に変換する場合です。外から固定されたポテンシャル（実験室の電極など）を置くと、その \(V\) は勝手には変換されないので、話が変わります ── 本稿が扱っているのは<em>宇宙全体を一緒に書き換える</em>操作です。</p>
<p style="margin:0 0 10px"><strong>② 「波束が \(\ln t\) でしか広がらない」は、宇宙論的な時間スケールでの話です。</strong> 実験室では \(\dot m/m=H_0\simeq10^{-18}\)/秒 なので、いかなる測定にもかかりません。また、これは<em>標準の絵で「固有速度が \(1/a\) で減衰する」と言っているのと同じ事実</em>であって、新しい物理ではありません。</p>
<p style="margin:0 0 10px"><strong>③ 到達距離 \(v_1t_1\) は、\(a\propto t\) を全時代に適用した場合の値です。</strong> 実際の宇宙（放射→物質→Λ）では積分が変わり、係数は動きます ── ただし「質量を持つものは収束、光は発散」という<em>定性的な結論は、減速膨張ならどれでも同じ</em>です。表の数値は桁の議論として読んでください。</p>
<p style="margin:0 0 10px"><strong>④ 再結合期の水素原子の速度 5 km/s は、\(T=3000\) K の熱速度の目安です。</strong> 実際のバリオンは音波に乗って集団運動しており、単独粒子の自由飛行として扱うのは粗い近似です。</p>
<p style="margin:0"><strong>⑤ トンネル透過率の不変性は、WKB 近似の指数部分についての話です。</strong> 前因子や共鳴条件まで含めた完全な不変性を主張するものではありません（ただしそれらも無次元比で書ける限り、同じ理由で不変です）。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>\(\psi\) のウェイトが \(-3/2\) なのはなぜか。
<details><summary>答えを見る</summary><div class="ans">規格化 \(\int|\psi|^2d^3x=1\) から。\(d^3x\) がウェイト \(+3\) なので \(|\psi|^2\) は \(-3\)、よって \(\psi\) は \(-3/2\)。<em>波動関数のウェイトは、選ぶものではなく規格化が決めます。</em></div></details></li>

<li>この絵で自由粒子の速度はどう変わるか。そこから波束の広がり方を出せ。
<details><summary>答えを見る</summary><div class="ans">力がないので運動量 \(p\) は保存、質量が \(\propto t\) なので \(v=p/m\propto1/t\)。積分すると \(\Delta x=\int v\,dt\propto\ln t\)。<strong>線形ではなく対数</strong>です。</div></details></li>

<li>時刻 \(t_1\) に速度 \(v_1\) で走り出した粒子の、永遠ぶんの共動到達距離を求めよ。
<details><summary>答えを見る</summary><div class="ans">\(\Delta\chi=\int_{t_1}^\infty v_1(t_1/t)/(t/t_1)\,dt=v_1t_1^2\int_{t_1}^\infty dt/t^2=v_1t_1\)。<strong>最初の 1 ハッブル時間で進む距離が、永遠ぶんの上限</strong>になります。光だけは \(\int c\,dt/a\propto\ln t\) で発散します。</div></details></li>

<li>なぜトンネル透過率は不変なのか。
<details><summary>答えを見る</summary><div class="ans">指数の中身 \(\int\kappa\,dx\) が無次元だから。\(\kappa=\sqrt{2m(V-E)}/\hbar\) はウェイト \(-1\)（長さの逆数）、\(dx\) は \(+1\) なので、積分すると \(0\)。<em>太陽が燃える速さも \(\alpha\) 崩壊の半減期も、この絵で一切変わりません。</em></div></details></li>

<li>（やや難）これだけ不変なものが多いのに、\(N=mc^2t/\hbar\) だけが動くのはなぜか。
<details><summary>答えを見る</summary><div class="ans">\(N\) は「系の大きさ ÷ コンプトン波長」で、<strong>分子と分母のウェイトが違う</strong>から（\(t\) は \(+1\)、\(\hbar/mc\) も \(+1\) ですが、\(t\) は宇宙が持ち込む長さで、\(\hbar/mc\) は粒子が持ち込む長さ）。正確には \(N=mc^2t/\hbar\) の \(m\)（\(-1\)）と \(t\)（\(+1\)）が打ち消して不変ですが、<em>その値が時間とともに増えていく</em>ことは、どのゲージで計算しても同じです ── 前シリーズ第6回で二つの絵から同じ式を出して確かめた通り。<strong>不変であることと、時間変化しないことは別</strong>です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　物質は歩けなくなり、光は歩き続ける</h2>
<p>シュレディンガー方程式に入れると、両辺のウェイトがどちらも \(-5/2\) で揃い、<strong>方程式は一文字も変わりません</strong>。変わるのは質量だけ ── \(m(t)=m_0t/t_0\)。第4回の「消せるものを全部消すと質量ひとつが残る」の、量子力学版です。</p>
<p>ところが、その一つが効きます。自由粒子は運動量を保存するので \(v=p/m\propto1/t\)。だから<strong>波束は \(\Delta x\propto t\) ではなく \(\Delta x\propto\ln t\) でしか広がらない</strong>。積み上げると、質量を持つものの共動到達距離は \(v_1t_1\) で<em>頭打ち</em>になります ── 最初の 1 ハッブル時間で進む距離が、永遠ぶんの上限。再結合期の水素原子なら <strong>1.9 パーセク</strong>。CMB の模様がその場に凍りついたままなのは、この積分のせいです。一方、光は \(c\,t_1\ln(t/t_1)\) で発散し続ける。<em>光速で走り出しても、宇宙が \(e=2.72\) 倍の年齢になれば光に追い抜かれます。</em></p>
<p>不変なものも数えました。不確定性、作用 \(S/\hbar\)、そして<strong>トンネル透過率</strong> ── 指数の中身 \(\int\kappa\,dx\) が無次元なので、太陽が燃える速さも \(\alpha\) 崩壊の半減期も一切変わりません。動くのはド・ブロイ波長・コンプトン波長・エネルギー準位で、どれも「長さか、エネルギーか」だけの違いです。</p>
<p>そして最後に一つだけ、着実に増える量が残ります ── \(N=mc^2t/\hbar\)（電子で \(3.4\times10^{38}\)）。標準の絵では「宇宙が大きくなるから増える」ですが、この絵では<strong>コンプトン波長が縮むから増える</strong>。<em>宇宙は膨張しているのではなく、量子的な粒度に対して相対的に粗くなっている</em> ── 世界は時代とともに古典的になっていきます。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第9回</span>
量子力学が通ったので、次は<strong>原子</strong>に入れます。この絵では原子が \(1/t\) で縮んでいくのに、スペクトル線はまったくぼやけません。なぜか ── <em>断熱パラメータ</em> を計算すると、水素で \(\hbar H/E_{\rm Ry}=1.1\times10^{-34}\)。桁違いにゆっくりなので、遷移が一つも誘起されないのです。これは 1918 年に<strong>アインシュタインがワイルの理論を殺した論法</strong>（第二時計効果でスペクトル線がぼける）の、ちょうど裏返し ── なぜ現代の共形変換は同じ刃で切られないのかが、一つの数字で言えます。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sv=document.getElementById('sv'), vv=document.getElementById('vv'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=318;
  var c=299792458.0, t0=4.3536e17, Mpc=3.0857e22;
  var xmin=0, xmax=6;            // log10(t/t0)
  var ymin=-2, ymax=5;           // log10(Δχ / Mpc)

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function lg(v){ return Math.log(v)/Math.LN10; }

  function draw(){
    // v: 1 km/s → c を対数で
    var f=parseInt(sv.value,10)/1000;
    var v=1e3*Math.pow(c/1e3, f);
    var sat=v*t0/Mpc;                       // 頭打ちの高さ [Mpc]
    var cl =c*t0/Mpc;                       // 光の係数 [Mpc]

    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right';
    for(var e=-2;e<=5;e++){
      var y=py(e);
      g.strokeStyle='#eef1f3'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#93a2ab';
      g.fillText((e<0?'10⁻'+Math.abs(e):(e===0?'1':'10'+e))+' Mpc', X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=6;q++){
      var x=px(q);
      g.strokeStyle='#f5f7f9'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#93a2ab'; g.fillText(q===0?'いま':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#c3ced5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // 頭打ちの高さ
    if(lg(sat)>ymin&&lg(sat)<ymax){
      g.strokeStyle='#94a3ac'; g.lineWidth=1.6; g.setLineDash([6,5]);
      g.beginPath(); g.moveTo(X0,py(lg(sat))); g.lineTo(X1,py(lg(sat))); g.stroke();
      g.setLineDash([]);
    }

    // 物質： Δχ = v t0 (1 - t0/t)
    g.strokeStyle='#1d3f56'; g.lineWidth=3.4; g.beginPath();
    var first=true;
    for(var i=0;i<=400;i++){
      var lx=xmin+(xmax-xmin)*i/400, T=Math.pow(10,lx);
      var d=sat*(1-1/T);
      if(d<=0){ first=true; continue; }
      var yy=lg(d);
      if(yy<ymin){ first=true; continue; }
      if(first){ g.moveTo(px(lx),py(Math.min(yy,ymax))); first=false; }
      else g.lineTo(px(lx),py(Math.min(yy,ymax)));
    }
    g.stroke();

    // 光： Δχ = c t0 ln(t/t0)
    g.strokeStyle='#9a5a1e'; g.lineWidth=3.4; g.beginPath();
    first=true;
    for(var i=0;i<=400;i++){
      var lx=xmin+(xmax-xmin)*i/400, T=Math.pow(10,lx);
      var d=cl*Math.log(T);
      if(d<=0){ first=true; continue; }
      var yy=lg(d);
      if(yy<ymin){ first=true; continue; }
      if(first){ g.moveTo(px(lx),py(Math.min(yy,ymax))); first=false; }
      else g.lineTo(px(lx),py(Math.min(yy,ymax)));
    }
    g.stroke();

    g.fillStyle='#1d3f56'; g.textAlign='right';
    if(lg(sat)>ymin+0.3&&lg(sat)<ymax-0.2)
      g.fillText('物質（頭打ち '+(sat<0.01?sat.toExponential(1):sat.toPrecision(3))+' Mpc）', X1-8, py(lg(sat))-9);
    g.fillStyle='#9a5a1e'; g.textAlign='left';
    g.fillText('光（伸び続ける）', px(4.1), py(lg(cl*Math.log(Math.pow(10,4.1))))-10);

    g.fillStyle='#6b7c86'; g.textAlign='center';
    g.fillText('経過した宇宙の年齢  t / t₀', (X0+X1)/2, Y1+36);

    // 読み出し
    var vk=v/1e3;
    vv.textContent = (v>0.5*c) ? (v/c).toFixed(3)+' c' : (vk>1e4? (vk/1e3).toPrecision(3)+' 千km/s' : vk.toPrecision(3)+' km/s');
    var overtake=Math.exp(v/c);           // ln(t/t0) = v/c で光が追い抜く
    ro.textContent='初速 '+vv.textContent+
      '　→　永遠ぶんの到達距離 v₁t₀ = '+(sat<0.01?sat.toExponential(2):sat.toPrecision(3))+' Mpc'+
      '　／　光がそこに届くのは t = '+overtake.toPrecision(3)+' t₀'+
      '　／　物質はそこで止まり、光は無限に伸びる';
  }
  sv.addEventListener('input',draw);
  draw();
})();
</script>'''

FOOT = ''

build(out='../wakaru-ct-08-quantum.html', acc='#1d3f56', ops='#9a5a1e',
      title='量子力学に入れてみる ── わかる c·t=一定 第8回',
      ep='第 8 回 ／ 方程式は一文字も変わらない。変わるのは質量だけ',
      eyebrow='物質は歩けなくなり、光は歩き続けます',
      h1='量子力学に、<br>入れてみる',
      sub='シュレディンガー方程式は形を保ちます ── ただし \\(m(t)=m_0\\,t/t_0\\)。<br>そこから、自由な波束が<em>対数でしか広がらない</em>という帰結が出ます。',
      byline_l='必要な道具：ウェイトの足し算、積分ひとつ',
      byline_r='\\(\\Delta\\chi=v_1t_1\\)（有限）　対　\\(c\\,t_1\\ln(t/t_1)\\)（無限）',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第8回、物理好きの高校生・大学生向け読み物です。共形変換のもとで長さ・時間がウェイト \\(+1\\)、質量・エネルギーが \\(-1\\)、\\(\\hbar,c\\) が \\(0\\)、規格化条件から波動関数が \\(-3/2\\) となることは標準的です。シュレディンガー方程式の両辺がともにウェイト \\(-5/2\\) となり形を保つこと、自由粒子の速度が \\(v\\propto1/a\\) で減衰すること（＝標準的な「固有速度の赤方偏移」）は、いずれも標準的な結果です。本稿の \\(\\Delta\\chi=v_1t_1\\)（\\(a\\propto t\\) のとき、質量を持つ粒子の共動到達距離が有限になること）、および光の \\(c\\,t_1\\ln(t/t_1)\\) が発散すること、光速で走り出しても \\(t=e\\,t_1\\) で光に追い抜かれることは本稿での計算です。表の数値（再結合期の水素原子 1.9 pc、銀河 8.5 Mpc、電子 14.1 Mpc、\\(c\\,t_0=4230\\) Mpc）も本稿での計算で、<strong>\\(a\\propto t\\) を全時代に適用した場合の値</strong>です ── 実際の宇宙では係数が変わりますが、「質量を持つものは収束、光は発散」という結論は減速膨張であれば共通です。再結合期の熱速度 5 km/s は \\(T=3000\\) K の目安で、実際のバリオンは音響振動に乗った集団運動をしています。トンネル透過率の不変性は WKB 近似の指数部分についての主張です。\\(N=mc^2t/\\hbar\\) が二つの絵で同一の式になることは前シリーズ第6回で示した通りです。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルで、初期宇宙まで外挿した場合は元素合成と矛盾します（Lewis, Barnes &amp; Kaushik 2016）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで初速を変え、物質の線が必ず頭打ちになる様子が見えます。「答えを見る」で解答が開きます。')
