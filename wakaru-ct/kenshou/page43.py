# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第18回で「1 ビット \(\leftrightarrow\) 1.96 fm」を出しました。では<strong>プランク長そのもの</strong>は、ウェイト表のどこにいるのでしょうか。答えは意外です ── <em>\(\ell_P\) はウェイト \(+1\)、ただの長さ、帳簿の列</em>。そして「長さに最小単位がある」という主張は、<strong>共形不変性とそもそも両立しません</strong>。第 V 部でいちばんはっきりした、<em>道具の効く範囲の端</em>です。</p>

<h2><span class="n">01</span>プランク長は、ウェイト表のどこにいるか</h2>

<div class="calc">
<span class="tag">\(\hbar\) と \(c\) はウェイト 0、\(G\) はウェイト \(+2\)（第35回①）</span>
$$\ell_P=\sqrt{\frac{\hbar G}{c^3}}\qquad\Longrightarrow\qquad \text{ウェイト}=\frac{+2}{2}=\mathbf{+1}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">ウェイト</th><th class="mid">分類</th></tr></thead>
<tbody>
<tr><th>\(\ell_P=1.616\times10^{-35}\) m</th><td class="mid">\(+1\)</td><td class="mid">長さ ＝ 帳簿</td></tr>
<tr><th>\(t_P=5.391\times10^{-44}\) s</th><td class="mid">\(+1\)</td><td class="mid">時間 ＝ 帳簿</td></tr>
<tr><th>\(m_P=2.176\times10^{-8}\) kg</th><td class="mid">\(-1\)</td><td class="mid">質量 ＝ 帳簿</td></tr>
<tr><th>\(E_P=1.221\times10^{19}\) GeV</th><td class="mid">\(-1\)</td><td class="mid">エネルギー ＝ 帳簿</td></tr>
<tr class="hi"><th>\(L/\ell_P\)（長さの比）</th><td class="mid"><strong>\(0\)</strong></td><td class="mid"><strong>無次元 ＝ 物理</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>プランク量はどれも帳簿の列にいます。</strong> 物理の列にいるのは<em>比だけ</em>。<br>
── 「最小の長さは \(\ell_P\)」は、そのままでは第3回の意味で<strong>まだ文になっていません</strong>。<br>
文にするなら <strong>\(L/\ell_P\ge1\)</strong>。</p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">02</span>核心 ── ここで、道具が本当に壊れる</h2>

<p>問題は「<strong>\(G\) は共形変換で動くのか</strong>」です ── 第36回の (A)/(B) が、そのまま \(G\) に当たります。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>読み方</th><th class="mid">\(\ell_P\)</th><th class="mid">\(L/\ell_P\)</th><th class="mid">帰結</th></tr></thead>
<tbody>
<tr><th>(A) \(G\) も動く（\(G\to\Omega^2G\)）</th><td class="mid">一緒に動く</td><td class="mid">ウェイト \(0\)</td><td class="mid">最小長は保たれる → <strong>記法</strong></td></tr>
<tr class="hi"><th>(B) \(G\) は固定</th><td class="mid">動かない</td><td class="mid">ウェイト \(+1\)</td><td class="mid"><strong>最小長を割り込ませられる</strong> → 主張</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>「最小の長さがある」理論は、そもそも共形不変ではありえません。</strong><br>
共形不変性は<em>スケールが無いこと</em>を要求し、最小長は<em>スケールそのもの</em>だからです。<br>
── 第 V 部でここまで「壊れる／届かない」を見てきましたが、ここは違います。<br>
<strong>仮定からして排除されている</strong> ── 道具の効く範囲の、はっきりした端です。</p>
</div>

<h2><span class="n">03</span>では、プランクスケールとは結局何か</h2>

<div class="calc">
<span class="tag">指させる長さではなく、指させる二つの長さの比が 1 になる場所</span>
$$\lambda_C=\frac{\hbar}{mc}\quad(\text{量子の広がり})\qquad
r_s=\frac{2Gm}{c^2}\quad(\text{重力の広がり})$$
$$\lambda_C=r_s\ \Longleftrightarrow\ m=\sqrt{\frac{\hbar c}{2G}}=1.539\times10^{-8}\ \text{kg}=\frac{m_P}{\sqrt2}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">質量 [kg]</th><th class="mid">\(\lambda_C\) [m]</th><th class="mid">\(r_s\) [m]</th><th class="mid">\(\lambda_C/r_s\)</th></tr></thead>
<tbody>
<tr><th class="mid">電子 \(9.11\times10^{-31}\)</th><td class="mid">\(3.86\times10^{-13}\)</td><td class="mid">\(1.35\times10^{-57}\)</td><td class="mid">\(2.9\times10^{44}\)</td></tr>
<tr><th class="mid">陽子 \(1.67\times10^{-27}\)</th><td class="mid">\(2.10\times10^{-16}\)</td><td class="mid">\(2.49\times10^{-54}\)</td><td class="mid">\(8.5\times10^{37}\)</td></tr>
<tr class="hi"><th class="mid">\(m_P/\sqrt2=1.54\times10^{-8}\)</th><td class="mid">\(2.286\times10^{-35}\)</td><td class="mid">\(2.286\times10^{-35}\)</td><td class="mid"><strong>\(1.000\)</strong></td></tr>
<tr><th class="mid">1 g</th><td class="mid">\(3.52\times10^{-40}\)</td><td class="mid">\(1.49\times10^{-30}\)</td><td class="mid">\(2.4\times10^{-10}\)</td></tr>
<tr><th class="mid">1 kg</th><td class="mid">\(3.52\times10^{-43}\)</td><td class="mid">\(1.49\times10^{-27}\)</td><td class="mid">\(2.4\times10^{-16}\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">03節の結論</p>
<p style="margin:6px 0 0"><strong>交点は無次元の言明です。</strong> だからプランクスケールという概念は生き残ります ──<br>
<em>「長さ」としてではなく、「二つの効果が並ぶ場所」として。</em></p>
</div>

<div class="fig">
<p class="cap">図：質量を動かしたときの<strong>コンプトン波長</strong>と<strong>シュヴァルツシルト半径</strong>。片方は \(1/m\)、もう片方は \(m\) に比例するので、<em>必ずどこかで交わります</em>。その交点がプランクスケール ── <strong>指させる長さではなく、比が 1 になる場所</strong>です</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>質量 \(\log_{10}(m/\text{kg})\)<input id="sm" type="range" min="-320" max="30" value="-80" step="1"></label>
  <span class="val" id="vm">-8.0</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a4a6a"></i>コンプトン波長 λ_C = ħ/mc</span>
  <span><i class="swatch" style="background:#8a5a2a"></i>シュヴァルツシルト半径 r_s = 2Gm/c²</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>プランク長 ℓ_P</span>
</div>
</div>

<h2><span class="n">04</span>私たちは、そこからどれだけ遠いか</h2>

<div class="calc">
<span class="tag">LHC の重心系 13.6 TeV で見えている長さ</span>
$$\frac{\hbar c}{E}=1.45\times10^{-20}\ \text{m}\qquad
\frac{1.45\times10^{-20}}{\ell_P}=9.0\times10^{14}=2^{\,49.7}$$
</div>

<p><strong>50 回の倍化ぶん遠い</strong> ── 加速器のエネルギーを 2 倍にするたびに 1 歩です。</p>

<div class="aside">
<span class="tag">第2回の目盛りとの一致</span>
\(\ln(R_H/\ell_P)=140.29\)、\(\ln(t_0/t_P)=140.24\) ── <strong>第2回の「140.24 対数ステップ」は、空間で数えても同じ</strong>でした。<br>
1 次元の位置をプランク精度で指定するには \(\log_2(R_H/\ell_P)=202.4\) ビット、3 次元なら <strong>607 ビット</strong>（第38回④と同じ数）。
</div>

<h2><span class="n">05</span>観測は何か言っているか</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>測定</th><th class="mid">\(E_{\rm QG}/E_P\)</th><th class="mid">意味</th></tr></thead>
<tbody>
<tr class="hi"><th>Fermi GRB 090510（1 次の効果）</th><td class="mid"><strong>\(>7.6\)</strong></td><td class="mid"><strong>プランクエネルギーを超えて排除</strong></td></tr>
<tr><th>同（2 次の効果）</th><td class="mid">\(>1.3\times10^{-8}\)</td><td class="mid">\(E_P\) の \(10^{-8}\) 倍までしか縛れない</td></tr>
</tbody>
</table>
</div>

<p>最小長があると、光の速さがエネルギーにわずかに依存しうる（分散）── ガンマ線バーストの到着時間差で縛れます。<strong>1 次の効果は排除されました</strong>。<em>ローレンツ不変性を素朴に破る形の最小長は苦しい</em>。一方 2 次の効果は 8 桁ぶん手つかずで、ここはまだ空白です。<em>ただし、最小長のあるすべての理論がローレンツ不変性を破るわけではありません</em>（破らない定式化もあります）── この制限が効くのは破る形のものだけです。</p>

<h2><span class="n">06</span>第18回の 1.96 fm との関係</h2>

<div class="calc">
<span class="tag">第18回：1 ビットに対応する長さ</span>
$$\left(\frac{\ln2}{\pi}R_H\,\ell_P^2\right)^{1/3}=1.96\ \text{fm}\qquad\text{ウェイト}=\frac{(+1)+(+2)}{3}=\mathbf{+1}$$
</div>

<p>これも帳簿の列でした。<strong>物理は \(\ell_P\) との比のほうにあります</strong> ── \(1.96\ \text{fm}/\ell_P=1.21\times10^{20}=2^{66.7}\)。つまり「1 ビットの長さ」は、<em>プランク長から 67 倍化ぶん上</em>にあります。</p>

<h2><span class="n">07</span>ウェイト表の総点検 ── 第 V 部を並べる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">ウェイト</th><th class="mid">理由</th></tr></thead>
<tbody>
<tr><th>\(\alpha\) の走り（第37回）</th><td class="mid">\(0\)</td><td class="mid">無次元</td></tr>
<tr><th>\((D-1)(D-2)\)（第38回）</th><td class="mid">\(0\)</td><td class="mid">ただの数</td></tr>
<tr><th>カーのスピン \(\chi\)（第39回）</th><td class="mid">\(0\)</td><td class="mid">無次元</td></tr>
<tr><th>ホログラフィック限界（第40回）</th><td class="mid">\(0\)</td><td class="mid">面積 ÷ 面積</td></tr>
<tr><th>初期状態の特別さ（第41回）</th><td class="mid">\(0\)</td><td class="mid">ビット数</td></tr>
<tr><th>事象の地平面（第42回）</th><td class="mid">\(0\)</td><td class="mid">因果構造</td></tr>
<tr class="hi"><th><strong>見かけの地平面（第42回）</strong></th><td class="mid"><strong>\(\ne0\)</strong></td><td class="mid">局所量</td></tr>
<tr class="hi"><th><strong>プランク長（第43回）</strong></th><td class="mid"><strong>\(+1\)</strong></td><td class="mid">ただの長さ</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">07節の結論</p>
<p style="margin:6px 0 0">第 V 部で 0 の列に入らなかったのは<strong>二つだけ</strong> ── 見かけの地平面とプランク長。<br>
── <em>どちらも「局所的な尺度を持ち込む」量でした。</em></p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p style="margin:0 0 10px"><strong>① 02節の (A)/(B) は、規約の選択の問題です。</strong> 「\(G\) を動かすかどうか」は<em>物理が決めることではなく、どういう変換を考えるかの定義</em>です ── (A) を採れば共形変換は単位の取り替えになり、(B) を採れば物理的な主張になります。<strong>本稿の主張は「どちらかが正しい」ではなく、「どちらかを言わないと文にならない」</strong>という第3回の繰り返しです。</p>
<p style="margin:0 0 10px"><strong>② 「最小長は共形不変性と両立しない」は、大域的な共形不変性についての言い方です。</strong> 局所的な Weyl 変換をゲージ対称性として持つ理論（第34回の共形重力など）では、<em>スケールを固定するゲージ選択があってよい</em> ので、話はもう少し込み入ります ── 02節は<strong>「スケールを持つ理論はスケール不変ではない」という、ほとんど同語反復に近い言明</strong>で、それゆえ強いのです。</p>
<p style="margin:0 0 10px"><strong>③ 「プランク長が最小長である」こと自体、確立した事実ではありません。</strong> プランク長は<em>三つの定数から次元だけで作れる長さ</em>であって、そこで何かが起きるという証拠はまだありません ── 03節の交点は「量子と重力が同じ大きさになる」という<strong>目安</strong>であって、そこに最小単位があるという主張ではありません。</p>
<p style="margin:0 0 10px"><strong>④ 05節の \(E_{\rm QG}\) の制限は、特定の分散関係の形を仮定したものです。</strong> Fermi の値は GRB 090510 の解析によるもので、<em>光子の放出時刻に関する仮定に依存します</em>。また注記のとおり、<strong>最小長を持つ理論がすべてローレンツ不変性を破るわけではありません</strong>（ループ量子重力や非可換幾何にも破らない定式化があります）。</p>
<p style="margin:0"><strong>⑤ 06節の 1.96 fm は第18回の値をそのまま使っており</strong>、\(R_H=1.3\times10^{26}\) m を採ったときの数字です（\(1.3725\times10^{26}\) なら 1.99 fm）── <em>倍化の回数 66.7 はその程度の精度</em>です。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>プランク長の共形ウェイトはいくつか。
<details><summary>答えを見る</summary><div class="ans"><strong>\(+1\)</strong>。\(\ell_P=\sqrt{\hbar G/c^3}\) で \(\hbar,c\) はウェイト 0、\(G\) は \(+2\) なので \((+2)/2=+1\) ── <em>ただの長さ、帳簿の列</em>です。物理の列にいるのは \(L/\ell_P\) のほうだけ。</div></details></li>

<li>「最小の長さは \(\ell_P\)」は、第3回の意味で文になっているか。
<details><summary>答えを見る</summary><div class="ans"><strong>なっていません</strong> ── 次元付きの量に主張を置いているからです。文にするなら <strong>\(L/\ell_P\ge1\)</strong>。<em>「比較相手を言わなければ、まだ文になっていない」</em>がここでも効きます。</div></details></li>

<li>最小長のある理論は共形不変でありうるか。
<details><summary>答えを見る</summary><div class="ans"><strong>ありえません</strong>。共形不変性は<em>スケールが無いこと</em>を要求し、最小長は<em>スケールそのもの</em>だからです ── 第 V 部でここまでの「壊れる／届かない」と違って、ここは<strong>仮定からして排除されています</strong>（ただし②の但し書き）。</div></details></li>

<li>プランクスケールを、無次元の言明として述べよ。
<details><summary>答えを見る</summary><div class="ans"><strong>コンプトン波長とシュヴァルツシルト半径の比が 1 になる場所</strong>です ── \(\lambda_C/r_s=1\) は \(m=\sqrt{\hbar c/2G}=m_P/\sqrt2\)。<em>「長さ」としてではなく「二つの効果が並ぶ場所」として</em>、概念は生き残ります。</div></details></li>

<li>（やや難）LHC からプランク長まで、倍化で何回か。
<details><summary>答えを見る</summary><div class="ans"><strong>約 50 回</strong>（\(9.0\times10^{14}=2^{49.7}\)）。13.6 TeV で見えている長さは \(1.45\times10^{-20}\) m です ── <em>加速器のエネルギーを 2 倍にするたびに 1 歩</em>。ちなみに第2回の「140.24 対数ステップ」は空間で数えても同じ値でした（\(\ln(R_H/\ell_P)=140.29\)）。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　道具の効く範囲の、はっきりした端</h2>
<p>プランク長は \(\sqrt{\hbar G/c^3}\)、\(G\) がウェイト \(+2\) なので <strong>\(\ell_P\) はウェイト \(+1\) ── ただの長さ、帳簿の列</strong>です。\(t_P\)、\(m_P\)、\(E_P\) も同じ。<em>物理の列にいるのは \(L/\ell_P\) のような比だけ</em>で、だから「最小の長さは \(\ell_P\)」は、そのままでは第3回の意味で<strong>まだ文になっていません</strong>。</p>
<p>そしてここで道具が本当に壊れます。<strong>「最小の長さがある」理論は、そもそも共形不変ではありえない</strong> ── 共形不変性はスケールが無いことを要求し、最小長はスケールそのものだからです。第 V 部でここまで見てきた「壊れる／届かない」と違って、<em>ここは仮定からして排除されています</em>。</p>
<p>ではプランクスケールという概念は無意味なのか。そうではありません ── <strong>コンプトン波長 \(\hbar/mc\) とシュヴァルツシルト半径 \(2Gm/c^2\) の比が 1 になる場所</strong>として述べれば、それは無次元の言明です（\(m=m_P/\sqrt2=1.54\times10^{-8}\) kg）。<em>「長さ」としてではなく「二つの効果が並ぶ場所」として、概念は生き残ります。</em></p>
<p>私たちはそこから <strong>約 50 回の倍化ぶん</strong>離れています（LHC の \(1.45\times10^{-20}\) m から \(\ell_P\) まで \(2^{49.7}\)）。観測では、ローレンツ不変性を素朴に破る形の 1 次の効果は<strong>プランクエネルギーを超えて排除</strong>されましたが、2 次の効果は 8 桁ぶん手つかずです。</p>
<p>第 V 部を並べ直すと、<strong>ウェイト 0 の列に入らなかったのは二つだけ</strong> ── 見かけの地平面（第42回）とプランク長（今回）。<em>どちらも「局所的な尺度を持ち込む」量でした。</em></p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第44回</span>
今回、<strong>最小長は共形不変性と両立しない</strong>と分かりました。ところが ── <em>共形場理論は、実際に格子の上で計算されています</em>。格子は最小長そのものなのに。次回は<strong>離散化</strong>を見ます。<em>なぜ矛盾しないのか</em>を、第14回の異常次元まで戻って確かめます ── そこには、<strong>このシリーズの道具が壊れずに生き延びる理由</strong>があります。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sm=document.getElementById('sm'), vm=document.getElementById('vm'), ro=document.getElementById('ro');
  var X0=82, X1=690, Y0=34, Y1=286;
  var G=6.6743e-11, c=2.99792458e8, hbar=1.054571817e-34, lP=1.616255e-35;
  var M0=-32, M1=3;          // log10 m
  var L0=-60, L1=0;          // log10 length

  function px(lm){ return X0+(lm-M0)/(M1-M0)*(X1-X0); }
  function py(ll){ return Y1-(ll-L0)/(L1-L0)*(Y1-Y0); }
  function lC(lm){ return Math.log(hbar/(Math.pow(10,lm)*c))/Math.LN10; }
  function lS(lm){ return Math.log(2*G*Math.pow(10,lm)/(c*c))/Math.LN10; }

  function draw(){
    var lm=parseInt(sm.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var v=L0;v<=L1;v+=10){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(v)); g.lineTo(X1,py(v)); g.stroke();
      g.fillText('10^'+v, X0-8, py(v)+4);
    }
    g.textAlign='center';
    for(var t=M0;t<=M1;t+=5){
      g.fillStyle='#9c96a4'; g.fillText('10^'+t, px(t), Y1+20);
    }

    var lpl=Math.log(lP)/Math.LN10;
    g.strokeStyle='#c8c2d0'; g.lineWidth=1.6; g.setLineDash([5,4]);
    g.beginPath(); g.moveTo(X0,py(lpl)); g.lineTo(X1,py(lpl)); g.stroke(); g.setLineDash([]);
    g.fillStyle='#a89fae'; g.textAlign='left';
    g.fillText('プランク長 ℓ_P', X0+8, py(lpl)-7);

    g.strokeStyle='#2a4a6a'; g.lineWidth=2.8; g.beginPath();
    for(var i=0;i<=300;i++){ var v2=M0+(M1-M0)*i/300; if(i===0)g.moveTo(px(v2),py(lC(v2))); else g.lineTo(px(v2),py(lC(v2))); }
    g.stroke();
    g.strokeStyle='#8a5a2a'; g.lineWidth=2.8; g.beginPath();
    for(var j=0;j<=300;j++){ var v3=M0+(M1-M0)*j/300; if(j===0)g.moveTo(px(v3),py(lS(v3))); else g.lineTo(px(v3),py(lS(v3))); }
    g.stroke();

    var lmx=Math.log(Math.sqrt(hbar*c/(2*G)))/Math.LN10;
    g.fillStyle='#7a3a5a';
    g.beginPath(); g.arc(px(lmx),py(lC(lmx)),5.5,0,6.29); g.fill();
    g.textAlign='center'; g.fillText('交点 = プランクスケール', px(lmx), py(lC(lmx))-14);

    g.textAlign='left';
    g.fillStyle='#2a4a6a'; g.fillText('λ_C = ħ/mc', px(M0+2), py(lC(M0+2))-10);
    g.fillStyle='#8a5a2a'; g.fillText('r_s = 2Gm/c²', px(M1-6), py(lS(M1-6))-10);

    var Xc=px(lm);
    g.strokeStyle='#5a5262'; g.lineWidth=1.6; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(Xc,Y0); g.lineTo(Xc,Y1); g.stroke(); g.setLineDash([]);
    g.fillStyle='#2a4a6a'; g.beginPath(); g.arc(Xc,py(lC(lm)),4.2,0,6.29); g.fill();
    g.fillStyle='#8a5a2a'; g.beginPath(); g.arc(Xc,py(lS(lm)),4.2,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('質量 m [kg]', (X0+X1)/2, Y1+44);

    vm.textContent=lm.toFixed(1);
    var r=Math.pow(10,lC(lm)-lS(lm));
    ro.textContent='m = 10^'+lm.toFixed(1)+' kg　→　λ_C = 10^'+lC(lm).toFixed(1)+
      ' m　／　r_s = 10^'+lS(lm).toFixed(1)+' m　／　λ_C/r_s = '+r.toExponential(2)+
      (r>1?'　（量子のほうが大きい）':'　（重力のほうが大きい）')+
      (Math.abs(lm-lmx)<0.2?'　★ ここが交点 ── 比が 1、無次元の言明':'');
  }
  sm.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-43-planck.html', acc='#2a4a6a', ops='#8a5a2a',
      title='プランクスケール ── わかる c·t=一定 第43回（第V部）',
      ep='第 43 回 ／ 第 V 部・道具が壊れる場所',
      eyebrow='最小長は、共形不変性とそもそも両立しません',
      h1='プランク長は、<br>帳簿の列にいた',
      sub='\\(\\ell_P\\) はウェイト \\(+1\\) ── ただの長さです。<br><em>そして「最小の長さがある」理論は、仮定からして共形不変ではありえません。</em>',
      byline_l='必要な道具：第2回の対数ステップ、第3回の判定、第16回のウェイト表、第18回、第35回',
      byline_r='LHC からプランク長まで、50 倍化',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第43回（第 V 部の 7 回目）、物理好きの高校生・大学生向け読み物です。プランク単位、コンプトン波長とシュヴァルツシルト半径の交点、量子重力現象論のローレンツ不変性検証はいずれも標準的な内容で、本稿に新しい主張はありません ── 数値は kenshou/calc47.py で計算しています。<strong>02節の (A)/(B) は規約の選択の問題で</strong>、「\\(G\\) を動かすかどうか」は物理が決めることではなく変換の定義です ── <em>本稿の主張は「どちらかが正しい」ではなく「どちらかを言わないと文にならない」</em>という第3回の繰り返しです。<strong>「最小長は共形不変性と両立しない」は大域的な共形不変性についての言い方で</strong>、局所的な Weyl 変換をゲージ対称性として持つ理論（第34回の共形重力など）では話はもう少し込み入ります ── 02節は<em>「スケールを持つ理論はスケール不変ではない」というほとんど同語反復に近い言明</em>で、それゆえ強いのです。<strong>「プランク長が最小長である」こと自体、確立した事実ではありません</strong> ── プランク長は三つの定数から次元だけで作れる長さであって、そこで何かが起きるという証拠はまだなく、03節の交点は「量子と重力が同じ大きさになる」という目安です。<strong>05節の \\(E_{\\rm QG}\\) の制限は特定の分散関係の形を仮定したもの</strong>で、Fermi の値は GRB 090510 の解析により光子の放出時刻に関する仮定に依存します ── また<em>最小長を持つ理論がすべてローレンツ不変性を破るわけではありません</em>。06節の 1.96 fm は第18回の値（\\(R_H=1.3\\times10^{26}\\) m）をそのまま使っており、\\(1.3725\\times10^{26}\\) なら 1.99 fm です。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで質量を動かすと、二つの長さが必ず交わることが見えます。「答えを見る」で解答が開きます。')
