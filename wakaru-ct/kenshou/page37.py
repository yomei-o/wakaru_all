# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第11回で「光には何も起きていない」と数えました。<strong>あれは古典の範囲の話でした。</strong> 量子にすると、細かさの基準 \(\mu\) が持ち込まれ、共形対称性が破れます ── しかもその破れは、<em>第34回で見た \(\Omega^{D-4}\) という指数そのもの</em>です。今回はその破れを、<strong>ビットで測ります</strong>。そして破れの大きさが<em>自由度の個数を数えているだけ</em>だと分かります。</p>

<h2><span class="n">01</span>量子は、\(D=4\) に留まれない</h2>

<div class="calc">
<span class="tag">第34回で数えた指数を、もう一度</span>
$$S_{\text{Maxwell}}\;\to\;\Omega^{\,D-4}\,S_{\text{Maxwell}}$$
<p class="lbl">指数がちょうどゼロになるのは \(D=4\) だけ ── 第11回の「何も起きていない」はこれです</p>
</div>

<p>ところが、<strong>量子にすると \(D=4\) に留まれません</strong>。</p>

<div class="seven">
<div class="row"><div class="mk">A</div><div class="txt"><strong>次元正則化</strong><span>\(D=4-\varepsilon\) で計算し、\(\varepsilon\to0\) は最後に取る ── <em>計算のあいだ、次元は 4 ではない</em></span></div></div>
<div class="row"><div class="mk">B</div><div class="txt"><strong>格子・切断</strong><span>細かさの基準 \(\mu\) を持ち込む ── <em>「どこまで細かく見るか」を決めないと積分が定義できない</em></span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>どちらでも \(\Omega^{D-4}=\Omega^{-\varepsilon}\ne1\)</strong><span>第34回で見た指数が、<em>そのまま破れになる</em></span></div></div>
</div>

<div class="calc">
<span class="tag">次元を数える</span>
$$[\,e^2\,]=\text{質量}^{\,4-D}=\text{質量}^{\,\varepsilon}$$
<p class="lbl">\(\alpha\) が無次元なのは \(D=4\) でだけ。\(\varepsilon\ne0\) では次元を持ってしまう</p>
</div>

<p>次元を持ってしまったら、<strong>第35回とまったく同じ手当て</strong>が要ります ── <em>スケールと組ませて無次元にする</em>。漸近安全性が \(g=Gk^2\) を作ったのと同じことを、QED は \(\alpha(\mu)\) でやっています。</p>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>第16回のウェイトの地図で「0 の列」にいた \(\alpha\) が、量子にすると \(\mu\) を持ちます。</strong><br>
── <em>このシリーズが「触れられない場所」と呼んできた列に、量子が数字を書き込んだ。</em></p>
</div>

<h2><span class="n">02</span>どれくらい動くのか</h2>

<div class="calc">
<span class="tag">1 ループの QED</span>
$$\frac{1}{\alpha(\mu)}=\frac{1}{\alpha(0)}-\frac{2}{3\pi}\sum_f N_c Q_f^2\,\ln\frac{\mu}{m_f}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">\(1/\alpha\)</th><th class="mid">中身</th></tr></thead>
<tbody>
<tr><th>低エネルギー（\(q\to0\)）</th><td class="mid">\(137.036\)</td><td class="mid">CODATA 2022</td></tr>
<tr><th>電子ループだけで \(M_Z\) まで</th><td class="mid">\(134.47\)</td><td class="mid">\(\ln(M_Z/m_e)=12.09\)、\(\Delta=2.566\)</td></tr>
<tr class="hi"><th>実測 \(1/\alpha(M_Z)\)</th><td class="mid"><strong>\(127.951\)</strong></td><td class="mid">PDG（\(\overline{\text{MS}}\)）</td></tr>
</tbody>
</table>
</div>

<p>電子ループだけで全体のずれの <strong>28 パーセント</strong>。残りはミューオン、タウ、クォークが埋めます ── <em>ただし、そのうちハドロンの寄与は摂動では計算できず、\(e^+e^-\to\)ハドロンの実測データから入れます</em>。<strong>ここは理論ではなく測定値です。</strong></p>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0">$$\frac{\alpha(M_Z)}{\alpha(0)}=1.0710\qquad\text{── }\textbf{7.1 パーセント大きい}$$</p>
</div>

<h2><span class="n">03</span>「実効ウェイト」を測る</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>入っている荷電フェルミオン</th><th class="mid">\(d\ln\alpha/d\ln\mu\)</th></tr></thead>
<tbody>
<tr><th>電子 1 種のみ</th><td class="mid">\(1.55\times10^{-3}\)</td></tr>
<tr><th>荷電レプトン 3 種</th><td class="mid">\(4.65\times10^{-3}\)</td></tr>
<tr class="hi"><th>標準模型の全荷電フェルミオン</th><td class="mid"><strong>\(1.03\times10^{-2}\)</strong></td></tr>
</tbody>
</table>
</div>

<p>古典のウェイトは <strong>0</strong>。量子では \(10^{-3}\) 台の「実効ウェイト」が付きます。1 e-fold あたりは小さいのですが、<em>12.1 e-fold ぶん積むと 7.1 パーセント</em>になります。</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>核心 ── 破れを、ビットで測る</h2>

<div class="calc">
<span class="tag">第19回の作法で</span>
<p class="lbl">実験室での \(\alpha\) の精度（CODATA 2022）＝ 雑音の床</p>
$$1.6\times10^{-10}\;\to\;32.5\ \text{ビット}$$
<p class="lbl">\(m_e\to M_Z\) の走りを、その床を単位に測る</p>
$$\frac{7.10\times10^{-2}}{1.6\times10^{-10}}=4.44\times10^{8}\;\to\;\mathbf{28.7\ ビット}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>第19回の目盛りの上で</th><th class="mid">驚き</th></tr></thead>
<tbody>
<tr><th>恒等式（第24回の \(C\cdot t=N\)）</th><td class="mid">\(0\) bit</td></tr>
<tr><th>偶然の帯（第36回）</th><td class="mid">\(5.6\) bit</td></tr>
<tr><th>小出の関係式</th><td class="mid">\(15.7\) bit</td></tr>
<tr class="hi"><th><strong>QED の共形対称性の破れ</strong></th><td class="mid"><strong>\(28.7\) bit</strong></td></tr>
<tr><th>CMB の一様性（第17回）</th><td class="mid">\(1.6\times10^5\) bit</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>破れは、雑音の上 29 ビットあります。</strong><br>
── 偶然の帯（4〜7）のはるか上、<em>偶然ではありえない、測定された効果</em>です。<br>
<strong>第11回の「何も起きていない」は、量子では成り立ちません。</strong></p>
</div>

<div class="fig">
<p class="cap">図：\(1/\alpha\) の走り。<strong>古典なら水平線</strong>（ウェイト 0）ですが、量子では傾きが付きます。ツマミで「勘定に入れる荷電フェルミオンの数」を動かすと、傾きが変わります ── <em>傾きは、場の個数を数えているだけです</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>勘定に入れる \(\sum N_cQ^2\)<input id="sf" type="range" min="0" max="80" value="10" step="1"></label>
  <span class="val" id="vf">1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a4a7a"></i>1 ループの走り</span>
  <span><i class="swatch" style="background:#b8b2c0"></i>古典（ウェイト 0 なら水平）</span>
  <span><i class="swatch" style="background:#a03a3a"></i>実測 1/α(M_Z) = 127.95</span>
</div>
</div>

<h2><span class="n">05</span>第30回と矛盾しないのか</h2>

<div class="seven">
<div class="row"><div class="mk">30</div><div class="txt"><strong>\(\alpha\) は宇宙時間について 26 ビットで一定</strong><span>オクロ・原子時計 ── <em>同じ \(\mu\) で、時代を変える</em>：\(\partial\alpha/\partial t=0\)</span></div></div>
<div class="row"><div class="mk">37</div><div class="txt"><strong>\(\alpha\) はエネルギースケールについて 28.7 ビットぶん動く</strong><span><em>同じ時代で、\(\mu\) を変える</em>：\(\partial\alpha/\partial\mu\ne0\)</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>矛盾しない ── 別の問いだから</strong><span>「\(\alpha\) は一定」は、<em>何について一定かを言わないと、まだ文になっていない</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">05節の結論</p>
<p style="margin:6px 0 0"><strong>第3回の判定手続きが、そのまま効いています。</strong><br>
── <em>「比較相手を言わなければ、まだ文になっていない」</em>。ここでは比較相手が「時代」なのか「スケール」なのかで、答えが正反対になります。</p>
</div>

<h2><span class="n">06</span>破れの大きさは、自由度の個数を数えている</h2>

<div class="calc">
<span class="tag">曲がった時空でのトレースアノマリー</span>
$$\langle T^\mu{}_\mu\rangle=\frac{1}{16\pi^2}\left(c\,C^2-a\,E_4\right)$$
<p class="lbl">\(C^2\)＝ワイル曲率の二乗、\(E_4\)＝ガウス・ボネ項</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>場の中身</th><th class="mid">\(a\)</th><th class="mid">\(c\)</th><th class="mid">\(c/a\)</th></tr></thead>
<tbody>
<tr><th>実スカラー 1 個</th><td class="mid">\(0.0028\)</td><td class="mid">\(0.0083\)</td><td class="mid">\(3.000\)</td></tr>
<tr><th>ワイル フェルミオン 1 個</th><td class="mid">\(0.0306\)</td><td class="mid">\(0.0500\)</td><td class="mid">\(1.636\)</td></tr>
<tr><th>ベクトル場 1 個（光子）</th><td class="mid">\(0.1722\)</td><td class="mid">\(0.1000\)</td><td class="mid">\(0.581\)</td></tr>
<tr class="hi"><th>標準模型（\(N_0=4,\ N_{1/2}=45,\ N_1=12\)）</th><td class="mid"><strong>\(3.4528\)</strong></td><td class="mid">\(3.4833\)</td><td class="mid">\(1.009\)</td></tr>
</tbody>
</table>
</div>

<p>係数は場の中身だけで決まります ── \(a=(N_0+11N_{1/2}+62N_1)/360\)、\(c=(N_0+6N_{1/2}+12N_1)/120\)。<strong>アノマリーの係数は、場を数えているだけ</strong>です。</p>

<div class="keybox">
<p class="lbl">06節の結論</p>
<p style="margin:6px 0 0"><strong>破れの大きさ ＝ 自由度の個数。</strong> 第24回で情報を数えたのと同じ通貨です。<br>
そして <strong>\(a\) 定理</strong>（Komargodski–Schwimmer 2011）── <em>RG の流れに沿って \(a\) は減る一方</em>（\(a_{\rm UV}>a_{\rm IR}\)）。<br>
── 第4回で「粗視化は不可逆」と書いたことの、<strong>場の理論での対応物が定理になっています。</strong></p>
</div>

<h2><span class="n">07</span>第11回は、間違っていたか</h2>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>間違っていない ── 古典の範囲では厳密に正しい</strong><span>マクスウェル作用は \(D=4\) でちょうど共形不変</span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>光子そのもののウェイトは、量子でも変わらない</strong><span>第16回の表は生きている</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>破れたのは場ではなく、結合定数だった</strong><span>\(\alpha\) が \(\mu\) を持った ── <em>付ける但し書きは一行</em>：「ただし古典の話」</span></div></div>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p style="margin:0 0 10px"><strong>① 02節の \(1/\alpha(M_Z)=127.951\) は測定値であって、この記事の計算結果ではありません。</strong> 電子ループの \(134.47\) だけが 1 ループ公式から出た数で、<em>残りの寄与のうちハドロン部分は摂動では計算できず</em>、\(e^+e^-\to\)ハドロンの断面積データから入れます。ここは理論の予言ではなく、実験の入力です。</p>
<p style="margin:0 0 10px"><strong>② \(\alpha(\mu)\) の値はスキームに依存します。</strong> \(127.951\) は \(\overline{\text{MS}}\) スキームの値で、他のスキームでは数字が変わります ── <em>「\(\alpha\) が 7.1 パーセント動く」という言い方も、スキームを言わなければ厳密には文になっていません</em>（05節と同じ構造です）。ただし物理的な散乱振幅そのものはスキームに依らず、走りが実験にかかること自体は確立しています。</p>
<p style="margin:0 0 10px"><strong>③ 04節の 28.7 ビットは「実験室での \(\alpha\) の精度を雑音の床に取る」という選び方に依存します。</strong> 床を \(\alpha(M_Z)\) の精度（およそ \(10^{-4}\)）に取れば 9.5 ビット程度になります ── <em>数字そのものより、「偶然の帯のはるか上」という位置づけが要点</em>です。</p>
<p style="margin:0 0 10px"><strong>④ 06節の \(a,c\) の規格化は文献によって異なります。</strong> ここでは \(a=(N_0+11N_{1/2}+62N_1)/360\)、\(c=(N_0+6N_{1/2}+12N_1)/120\) を採りました。<em>比 \(c/a\) と「場を数えている」という構造は規格化に依りませんが、絶対値は採った規格化のもの</em>です。標準模型の \(N_{1/2}=45\) は右巻きニュートリノを含めない数え方です。また、この形の \(a,c\) は<strong>共形不変な場の理論についてのもの</strong>で、質量を持つ標準模型にそのまま当てはめた 3.45 という数字は<em>目安</em>と読んでください。</p>
<p style="margin:0"><strong>⑤ \(a\) 定理は 4 次元では証明されていますが、\(c\) については対応する定理がありません</strong>（2 次元の \(c\) 定理とは別物です）。06節の「粗視化は不可逆」との対応は、<em>本シリーズの読み方</em>であって、Komargodski–Schwimmer の主張そのものではありません。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>量子にすると共形対称性が破れるのは、なぜか。第34回の言葉で言うと。
<details><summary>答えを見る</summary><div class="ans">第34回で見たとおりマクスウェル作用は \(S\to\Omega^{D-4}S\) で、<strong>指数がゼロになるのは \(D=4\) だけ</strong>。ところが量子計算は次元正則化なら \(D=4-\varepsilon\)、切断なら \(\mu\) を持ち込むので、<em>\(D=4\) に留まれません</em>。破れは \(\Omega^{-\varepsilon}\ne1\) そのものです。</div></details></li>

<li>電子ループだけで \(1/\alpha(M_Z)\) を計算するといくつになるか。実測との差はどこから来るか。
<details><summary>答えを見る</summary><div class="ans">\(137.036-\frac{2}{3\pi}\ln(M_Z/m_e)=137.036-2.566=\mathbf{134.47}\)。実測は \(127.951\) なので、電子は全体のずれの <strong>28 パーセント</strong>だけ。残りはミューオン・タウ・クォークですが、<em>ハドロンの寄与は摂動では計算できず、\(e^+e^-\to\)ハドロンの実測データから入れます</em>。</div></details></li>

<li>「\(\alpha\) は一定」（第30回）と「\(\alpha\) は動く」（今回）は矛盾するか。
<details><summary>答えを見る</summary><div class="ans">矛盾しません。<strong>別の問いだから</strong>です ── 第30回は \(\partial\alpha/\partial t=0\)（同じ \(\mu\) で時代を変える）、今回は \(\partial\alpha/\partial\mu\ne0\)（同じ時代で \(\mu\) を変える）。<em>「一定」は、何について一定かを言わないと、まだ文になっていません</em>（第3回）。</div></details></li>

<li>トレースアノマリーの係数 \(a\) は何を数えているか。
<details><summary>答えを見る</summary><div class="ans"><strong>場の個数</strong>です ── \(a=(N_0+11N_{1/2}+62N_1)/360\)。破れの大きさが自由度の個数そのもので、<em>第24回で情報を数えたのと同じ通貨</em>。さらに \(a\) 定理により <strong>RG の流れに沿って \(a\) は減る一方</strong>で、第4回の「粗視化は不可逆」に対応します。</div></details></li>

<li>（やや難）第11回の「光には何も起きていない」に付ける但し書きは何行か。
<details><summary>答えを見る</summary><div class="ans"><strong>一行です</strong> ──「ただし古典の話」。<em>光子そのもののウェイトは量子でも変わらず、第16回の表は生きています</em>。破れたのは場ではなく<strong>結合定数</strong>で、\(\alpha\) が \(\mu\) を持ったことが破れの中身です。第11回の主張を取り下げる必要はありません。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　0 の列に、量子が数字を書き込んだ</h2>
<p>第34回で数えた \(S\to\Omega^{D-4}S\) の指数は、<strong>\(D=4\) でだけゼロ</strong>でした。そして<strong>量子は \(D=4\) に留まれません</strong> ── 次元正則化なら \(D=4-\varepsilon\)、切断なら \(\mu\)。どちらでも \(\Omega^{-\varepsilon}\ne1\) で、<em>第34回で見た指数がそのまま破れになります</em>。次元を数えると \([e^2]=\)質量\(^{\,\varepsilon}\)、つまり <strong>\(\alpha\) が無次元なのは \(D=4\) でだけ</strong>。だから第35回とまったく同じ手当てが要ります ── スケールと組ませて \(\alpha(\mu)\) にする。</p>
<p>どれくらい動くか。電子ループだけで \(1/\alpha\) は \(137.04\to134.47\)、実測の \(M_Z\) では \(127.951\)。<strong>\(\alpha(M_Z)/\alpha(0)=1.0710\)</strong>、7.1 パーセント大きい。1 e-fold あたりの「実効ウェイト」は \(10^{-3}\) 台ですが、12.1 e-fold ぶん積むとそうなります ── <em>第16回の地図で「0 の列」にいた \(\alpha\) に、量子が小さな数字を書き込んだ</em>のです。</p>
<p>破れをビットで測ります。実験室の精度 \(1.6\times10^{-10}\)（32.5 ビット）を雑音の床に取ると、7.1 パーセントの走りは <strong>雑音の上 28.7 ビット</strong>。第36回で見た偶然の帯（4〜7 ビット）のはるか上で、<em>偶然ではありえない、測定された効果</em>です。</p>
<p>第30回の「\(\alpha\) は 26 ビットで一定」と矛盾しないのか ── しません。<strong>別の問いだから</strong>です。第30回は同じ \(\mu\) で時代を変え、今回は同じ時代で \(\mu\) を変える。<em>「一定」は、何について一定かを言わないと、まだ文になっていない</em> ── 第3回の判定手続きがそのまま効いています。</p>
<p>そして破れの大きさは何を測っているのか。トレースアノマリーの係数 \(a,c\) は<strong>場の個数を数えているだけ</strong>でした（標準模型で \(a=3.45\)）。破れの大きさ ＝ 自由度の個数 ── 第24回で情報を数えたのと同じ通貨です。さらに <strong>\(a\) 定理</strong>により、RG の流れに沿って \(a\) は減る一方。<em>第4回で「粗視化は不可逆」と書いたことの、場の理論での対応物が定理になっています。</em></p>
<p>第11回は間違っていたか。<strong>間違っていません</strong> ── 付ける但し書きは一行、「ただし古典の話」。破れたのは場ではなく、結合定数でした。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第38回</span>
今回は、量子が \(D=4\) から出ざるを得ないせいで破れが出ました。次回は、それでも共形変換を<strong>重力に</strong>当てようとしたときに起きる、<em>もっと悪いこと</em>を見ます ── <strong>共形因子問題</strong>。アインシュタイン作用を共形因子で分解すると、その運動項だけ<strong>符号が逆</strong>になります。エネルギーに下限が無く、経路積分が発散する。第34回で二度出会ったゴーストの、<em>源</em>へ行きます。そして<strong>その発散を、やはりビットで測ります。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sf=document.getElementById('sf'), vf=document.getElementById('vf'), ro=document.getElementById('ro');
  var X0=86, X1=690, Y0=34, Y1=306;
  var A0=137.035999, ME=0.51099895e-3, MZ=91.1876;
  var L0=Math.log(ME), L1=Math.log(500.0);
  var YT=138.5, YB=124.0;

  function px(l){ return X0+(l-L0)/(L1-L0)*(X1-X0); }
  function py(v){ return Y1-(v-YB)/(YT-YB)*(Y1-Y0); }

  function draw(){
    var S=parseInt(sf.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var v=126;v<=138;v+=2){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(v)); g.lineTo(X1,py(v)); g.stroke();
      g.fillText(v.toFixed(0), X0-8, py(v)+4);
    }
    g.textAlign='center';
    var marks=[[ME,'m_e'],[0.10566,'m_μ'],[1.77686,'m_τ'],[MZ,'M_Z']];
    for(var i=0;i<marks.length;i++){
      var x=px(Math.log(marks[i][0]));
      g.strokeStyle='#eceaf0'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#9c96a4'; g.fillText(marks[i][1], x, Y1+18);
    }

    // 古典（水平線）
    g.strokeStyle='#b8b2c0'; g.lineWidth=2; g.setLineDash([5,4]);
    g.beginPath(); g.moveTo(X0,py(A0)); g.lineTo(X1,py(A0)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#a09aa8'; g.textAlign='left';
    g.fillText('古典：ウェイト 0 → 動かない', X0+8, py(A0)-8);

    // 実測 1/α(M_Z)
    g.strokeStyle='#a03a3a'; g.lineWidth=1.4; g.setLineDash([3,3]);
    g.beginPath(); g.moveTo(X0,py(127.951)); g.lineTo(X1,py(127.951)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#a03a3a'; g.textAlign='left';
    g.fillText('実測 1/α(M_Z) = 127.95', X0+8, py(127.951)-7);

    // 走り
    g.strokeStyle='#2a4a7a'; g.lineWidth=2.6; g.beginPath();
    for(var k=0;k<=260;k++){
      var l=L0+(L1-L0)*k/260;
      var v=A0-(2/(3*Math.PI))*S*(l-L0);
      var X=px(l), Y=py(v);
      if(k===0) g.moveTo(X,Y); else g.lineTo(X,Y);
    }
    g.stroke();

    var vz=A0-(2/(3*Math.PI))*S*(Math.log(MZ)-L0);
    g.fillStyle='#2a4a7a';
    g.beginPath(); g.arc(px(Math.log(MZ)),py(vz),4.5,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('エネルギースケール μ（対数）', (X0+X1)/2, Y1+40);
    g.save(); g.translate(22,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('1 / α(μ)', 0,0); g.restore();

    vf.textContent=S.toFixed(2);
    var pct=100*(A0/vz-1);
    ro.textContent='ΣN_cQ² = '+S.toFixed(2)+
      '　→　M_Z で 1/α = '+vz.toFixed(2)+
      '　（α は '+pct.toFixed(1)+' パーセント大きい）'+
      (S===0?'　★ 0 にすると水平 ── これが古典の「何も起きていない」':'')+
      (Math.abs(S-1)<0.06?'　← 電子 1 種だけ':'')+
      (Math.abs(S-6.67)<0.06?'　← 標準模型の全荷電フェルミオン':'')+
      (S>3.2?'　※ 全部を m_e から走らせるのは粗い近似 ── 実際は各粒子が自分の質量から走り始める':'');
  }
  sf.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-37-anomaly.html', acc='#2a4a7a', ops='#a03a3a',
      title='量子アノマリー ── わかる c·t=一定 第37回（第V部）',
      ep='第 37 回 ／ 第 V 部・道具が壊れる場所',
      eyebrow='「光には何も起きていない」は、古典の話でした',
      h1='0 の列に、<br>量子が数字を書き込む',
      sub='量子は \\(D=4\\) に留まれない ── 第34回で見た \\(\\Omega^{D-4}\\) が、そのまま破れになります。<br><em>その破れを、ビットで測ります。</em>',
      byline_l='必要な道具：第11回、第16回のウェイト表、第19回の目盛り、第34・35回',
      byline_r='雑音の上 28.7 ビット ── 偶然ではありえない',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第37回（第 V 部の 1 回目）、物理好きの高校生・大学生向け読み物です。トレースアノマリー（共形アノマリー）、QED の走る結合定数、\\(a\\) 定理はいずれも確立した標準的な内容で、本稿に新しい主張はありません ── 数値は kenshou/calc41.py で計算しています。<strong>\\(1/\\alpha(M_Z)=127.951\\) は測定値であって本稿の計算結果ではありません</strong>（PDG、\\(\\overline{\\text{MS}}\\)）── 電子ループの 134.47 だけが 1 ループ公式から出た数で、<em>残りのうちハドロンの寄与は摂動では計算できず \\(e^+e^-\\to\\)ハドロンの断面積データから入れます</em>。\\(\\alpha(\\mu)\\) の値はスキームに依存し、「7.1 パーセント動く」という言い方もスキームを言わなければ厳密には文になっていません（ただし散乱振幅自体はスキームに依らず、走りが実験にかかることは確立しています）。<strong>28.7 ビットという値は「実験室での \\(\\alpha\\) の精度を雑音の床に取る」という選び方に依存し</strong>、床を \\(\\alpha(M_Z)\\) の精度（\\(\\sim10^{-4}\\)）に取れば 9.5 ビット程度になります ── <em>数字より「偶然の帯のはるか上」という位置づけが要点</em>です。\\(a,c\\) の規格化は文献で異なり、ここでは \\(a=(N_0+11N_{1/2}+62N_1)/360\\)、\\(c=(N_0+6N_{1/2}+12N_1)/120\\) を採りました ── <strong>この形は共形不変な場の理論についてのもので、質量を持つ標準模型に当てはめた 3.45 は目安</strong>です（\\(N_{1/2}=45\\) は右巻きニュートリノを含めない数え方）。\\(a\\) 定理（Komargodski &amp; Schwimmer 2011）は 4 次元で証明されていますが \\(c\\) には対応する定理がなく、<strong>第4回の「粗視化は不可逆」との対応づけは本シリーズの読み方</strong>であって原論文の主張ではありません。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミを 0 にすると水平線 ── 古典の「何も起きていない」が見えます。「答えを見る」で解答が開きます。')
