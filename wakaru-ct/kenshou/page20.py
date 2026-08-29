# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">前シリーズ番外編②は、こう結論して終わりました ── <em>「宇宙を有限リソースの計算機として書くなら、縛るべきは \(a(t)\) ではなく光シート上の情報量。その計算は、まだ誰もやっていない」</em>。番外編③はブソーの共変エントロピー境界を見かけの地平面に当てて \(s\le3H/4\ell_P^2\) を導き、<strong>恒等的に飽和させると \(a\propto t^{1/3}\) が出る</strong>ところまで進んで止まりました。今回はその先へ行きます ── <em>飽和ではなく、制約として課したまま、予言は出るのか。</em> 結論を先に言うと、<strong>出ません</strong>。そして<em>出ない理由</em>のほうが面白い。</p>

<h2><span class="n">01</span>境界を、時間で追う</h2>

<p>使うのは番外編③の不等式です。見かけの地平面から出る内向き・過去向きの光シートに、ブソーの境界を当てると ──</p>

<div class="calc">
<span class="tag">縛る相手</span>
$$s\ \le\ \frac{3H}{4\ell_P^2}\qquad\Longrightarrow\qquad f\equiv\frac{s}{3H/4\ell_P^2}\ \le\ 1$$
<p class="lbl">\(s\propto a^{-3}\)、\(H\propto1/t\) なので</p>
$$f\ \propto\ t^{\,1-3p}\qquad(a\propto t^p)$$
</div>

<p>標準の熱史（放射 \(p=1/2\) → 物質 \(p=2/3\)）で、プランク期に \(f\approx1\) として今日まで積みます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>時代</th><th class="mid">\(t\)</th><th class="mid">\(f\)</th><th class="mid">余裕</th></tr></thead>
<tbody>
<tr class="hi"><th>プランク期</th><td class="mid">\(5.4\times10^{-44}\) s</td><td class="mid"><strong>\(\approx1\)</strong></td><td class="mid"><strong>0 桁（飽和）</strong></td></tr>
<tr><th>電弱期</th><td class="mid">\(10^{-11}\) s</td><td class="mid">\(7.3\times10^{-17}\)</td><td class="mid">16 桁</td></tr>
<tr><th>元素合成</th><td class="mid">1 s</td><td class="mid">\(2.3\times10^{-22}\)</td><td class="mid">22 桁</td></tr>
<tr><th>再結合</th><td class="mid">38 万年</td><td class="mid">\(2.4\times10^{-29}\)</td><td class="mid">29 桁</td></tr>
<tr><th>今日</th><td class="mid">138 億年</td><td class="mid">\(6.7\times10^{-34}\)</td><td class="mid"><strong>33 桁</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>境界はプランク期にちょうど飽和し、そこからひたすら余裕が開いていきます。</strong><br>
今日の余裕は <em>33 桁</em>。── 縛られているのはプランク期だけです。</p>
</div>

<h2><span class="n">02</span>プランク期に飽和するのは、恒等式だった</h2>

<p>「境界がちょうどプランク期で飽和する」── これは意味ありげに見えます。第19回の道具で測ってみましょう。</p>

<div class="calc">
<span class="tag">次元だけで確かめる</span>
<p class="lbl">プランク期には \(T\sim M_{\rm Pl}\)、したがって</p>
$$s\sim T^3\sim\frac{1}{\ell_P^3},\qquad H\sim\frac{1}{t_P}\sim\frac{c}{\ell_P}$$
<p class="lbl">代入すると</p>
$$f=\frac{s}{3H/4\ell_P^2}\sim\frac{1/\ell_P^3}{(1/\ell_P)/\ell_P^2}=1$$
</div>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0">次元解析だけから \(O(1)\)。<strong>第19回の分類でいう【恒等式】── 驚きは 0 ビット</strong>です。<br>
<em>「境界がプランク期で飽和する」は、発見ではなく検算でした。</em></p>
</div>

<p>第7回のディラックの大数、第10回のランダウアー限界に続いて、<strong>三つ目の「意味ありげだが恒等式」</strong>です。前回作った手続きが、さっそく仕事をしました。</p>

<h2><span class="n">03</span>核心 ── 制約としては、弱すぎる</h2>

<p>では、この境界を<em>制約として課す</em>と、どんな宇宙が排除されるでしょうか。膨張則ごとに、遡って \(f=1\) になる時刻を求めます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(p\)</th><th>膨張則</th><th class="mid">\(f\) の指数 \(1-3p\)</th><th class="mid">\(f=1\) になる時刻</th><th class="mid">判定</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">1/3</th><td>stiff（\(w=1\)）</td><td class="mid">0</td><td class="mid">──（\(f\) が一定）</td><td class="mid"><strong>飽和させ続けられる唯一の膨張則</strong></td></tr>
<tr><th class="mid">1/2</th><td>放射</td><td class="mid">\(-0.5\)</td><td class="mid">\(2\times10^{-49}\) s</td><td class="mid">プランク時刻より前 ── 破らない</td></tr>
<tr><th class="mid">2/3</th><td>物質</td><td class="mid">\(-1\)</td><td class="mid">\(2.9\times10^{-16}\) s</td><td class="mid">形式的には破る（実際は放射期）</td></tr>
<tr><th class="mid">1</th><td>\(c\cdot t=\)一定</td><td class="mid">\(-2\)</td><td class="mid">\(11\) s</td><td class="mid">破る（番外編③の判決）</td></tr>
</tbody>
</table>
</div>

<p>ここが今回の核心です。<strong>境界が排除するのは「プランク期より前で \(f>1\) になる膨張則」だけ</strong>。実際の宇宙は放射が支配しているので、そこは無事に通ります。</p>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>光シート上の情報量を縛っても、予言は出ません。</strong><br>
今日の余裕が 33 桁もあるので、標準的な膨張則は<em>ほぼ全部が通ってしまう</em>。<br>
第19回の言葉で言えば ── <strong>この制約が持つ情報量は、ほぼゼロ</strong>です。</p>
</div>

<div class="fig">
<p class="cap">図：使用率 \(f=s/(3H/4\ell_P^2)\) の履歴。朱色の天井が \(f=1\)（境界）。<strong>標準の熱史はプランク期で天井に触れ、そこから 33 桁下りていきます</strong>。ツマミで膨張則を変えると傾きが変わり、\(p>1/2\) では遡ったときに天井を突き抜けます</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>膨張則の指数 \(p\)（全時代に適用した場合）<input id="sp" type="range" min="250" max="1200" value="500" step="1"></label>
  <span class="val" id="vp">p = 0.500</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6b2f5a"></i>指定した膨張則</span>
  <span><i class="swatch" style="background:#2a6b2a"></i>標準の熱史（放射→物質）</span>
  <span><i class="swatch" style="background:#a8452a"></i>境界 \(f=1\)</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>飽和させ続ける宇宙は、stiff だった</h2>

<p>番外編③の結果を、ここで確認しておきます。\(s=3H/4\ell_P^2\) を<em>恒等的に</em>課すとどうなるか。</p>

<div class="calc">
<span class="tag">計算 ── 二行</span>
$$\frac{\sigma}{a^3}=\frac{3\dot a}{4Ga}\quad(\sigma=\text{共動エントロピー密度、一定})$$
$$\Longrightarrow\quad a^2\dot a=\text{一定}\quad\Longrightarrow\quad \boxed{\ a\propto t^{1/3}\ }\quad(w=1)$$
</div>

<p>つまり<strong>「情報の詰め込み効率を常に最大にする宇宙」は stiff（キネーション）</strong>です。私たちの宇宙ではありません。前シリーズの資源の表を、もう一度並べておきます。</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>ビット数（地平面エントロピー）を一定に保つ</strong><span>\(a\propto e^{Ht}\) ── ド・ジッター</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>アドレス空間（共動ハッブル半径）を一定に保つ</strong><span>\(a\propto t\) ── \(c\cdot t=\)一定</span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>メモリ使用率を一定に保つ</strong><span>\(a\propto t^{1/3}\) ── stiff（今回の飽和条件）</span></div></div>
</div>

<p><strong>どの資源を固定するかで、答えが三つに割れる</strong>。そして観測される宇宙は、そのどれでもありません（放射→物質→\(\Lambda\) と乗り換えていく）。<em>「一つの資源を固定する」という発想そのものが、宇宙のかたちを決めるには足りない</em> ── これが番外編②の問いに対する、今回の答えです。</p>

<h2><span class="n">05</span>では、扉は閉まったのか</h2>

<p>正直に言えば、<strong>半分だけ閉まりました</strong>。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>番外編②の期待</th><th class="mid">今回の結果</th></tr></thead>
<tbody>
<tr><th>光シート上の情報量を縛れば予言が出る</th><td class="mid"><strong>出ない</strong>（余裕 33 桁、情報量ほぼゼロ）</td></tr>
<tr><th>それが \(a(t)\) を縛るより良い形だ</th><td class="mid">形としては正しい（共形不変で、ゲージに依らない）</td></tr>
<tr class="hi"><th>境界が意味を持つ場所</th><td class="mid"><strong>プランク期だけ</strong> ── しかもそこでの飽和は恒等式</td></tr>
</tbody>
</table>
</div>

<p>番外編②が「縛るべきは光シート上の情報量」と言ったのは、<em>形としては正しかった</em>のです ── ブソーの境界は共形不変で、ゲージに依らず、だから第3回の意味で「判定にかかる」形をしています。ところが実際に当ててみると、<strong>効く場所がプランク期しかない</strong>。</p>

<div class="aside">
<span class="tag">これは失敗ではなく、範囲の確定</span>
第16回で「共形変換は大きさにしか触れない」と道具の限界を測りました。今回はもう一つ、<strong>ホログラフィック境界の限界</strong>を測ったことになります ── <em>それは古典宇宙論に対しては、ほとんど何も言わない</em>。言うのは量子重力の領域だけ。<strong>「宇宙は有限リソースの計算機だ」という発想が意味を持つのは、プランクスケールにおいてだけ</strong>だ、という結論です。第 V 部で、まさにそこへ行きます。
</div>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① \(s\le3H/4\ell_P^2\) は、ブソーの共変エントロピー境界を見かけの地平面という特定の面に当てた結果です。</strong> ブソーの境界は任意の面について主張するので、他の面ではもっと強い条件になりえます ── 本稿が示したのは「少なくともこの面では制約が弱い」ことです（前シリーズ番外編③⑧節と同じ注意）。</p>
<p style="margin:0 0 10px"><strong>② エントロピーが共動的に保存されるという仮定に立っています。</strong> 再加熱などのエントロピー生成があると、遡ったときの \(s\) はもっと小さかった可能性があり、余裕はさらに広がります（＝結論は強まる向き）。</p>
<p style="margin:0 0 10px"><strong>③ 「プランク期に \(f\approx1\)」は 1 ループ的な見積もりです。</strong> \(g_*\) の取り方で係数が動きます（番外編③では標準宇宙論について \(T\le2.84M_{\rm Pl}/\sqrt{g_*}\) と評価しました）。<em>02節の主張は「次元解析だけで \(O(1)\) になる」ことであって、係数が厳密に 1 だということではありません。</em></p>
<p style="margin:0 0 10px"><strong>④ 03節の \(f=1\) 到達時刻は、その \(p\) を全時代に適用した場合の値です。</strong> \(c\cdot t=\)一定 の 11 秒は番外編③の 5 秒と同じ桁で、差は今日の \(f\) の値の取り方によります。実際の宇宙は膨張則を乗り換えるので、単一の \(p\) で遡るのは粗い近似です。</p>
<p style="margin:0"><strong>⑤ 「予言が出ない」は、この形の制約についての結論です。</strong> ホログラフィック原理そのものが無力だという意味ではありません ── AdS/CFT のように、ホログラフィーが強力な計算手段になる文脈は多数あります。ここで言っているのは <em>「宇宙論的な \(a(t)\) を決める制約としては弱い」</em> という一点です。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>\(f=s/(3H/4\ell_P^2)\) の時間依存を、\(a\propto t^p\) から求めよ。
<details><summary>答えを見る</summary><div class="ans">\(s\propto a^{-3}\propto t^{-3p}\)、\(H\propto1/t\) なので \(f\propto t^{-3p}/t^{-1}=t^{1-3p}\)。<strong>\(p=1/3\) のときだけ指数がゼロ</strong>になります。</div></details></li>

<li>プランク期に \(f\approx1\) になるのはなぜか。それは驚きか。
<details><summary>答えを見る</summary><div class="ans">\(T\sim M_{\rm Pl}\) なら \(s\sim1/\ell_P^3\)、\(H\sim c/\ell_P\) なので、代入すると \(f\sim1\)。<strong>次元解析だけから出る</strong>ので、第19回の分類では<em>恒等式＝驚き 0 ビット</em>。発見ではなく検算です。</div></details></li>

<li>境界を恒等的に飽和させる膨張則は何か。
<details><summary>答えを見る</summary><div class="ans">\(f\propto t^{1-3p}\) が一定になる \(p=1/3\)、すなわち <strong>\(a\propto t^{1/3}\)（\(w=1\)、stiff／キネーション）</strong>。「情報の詰め込み効率を常に最大にする宇宙」ですが、私たちの宇宙ではありません。</div></details></li>

<li>この境界を制約として課すと、何が排除されるか。
<details><summary>答えを見る</summary><div class="ans"><strong>プランク期より前で \(f>1\) になる膨張則だけ</strong>。今日の余裕が 33 桁もあるので、標準的なものはほぼ全部通ります ── <em>制約としての情報量はほぼゼロ</em>。ただし \(c\cdot t=\)一定 を全時代に適用したものは \(t\sim10\) 秒で破ります。</div></details></li>

<li>（やや難）番外編②の「縛るべきは光シート上の情報量」は、間違いだったのか。
<details><summary>答えを見る</summary><div class="ans"><strong>形としては正しく、効き目としては足りませんでした。</strong> ブソーの境界は共形不変でゲージに依らないので、第3回の意味で「判定にかかる」正しい形をしています。ところが実際に当てると、効く場所が<em>プランク期だけ</em>。しかもそこでの飽和は恒等式。<strong>「宇宙は有限リソースの計算機だ」という発想が意味を持つのは、量子重力の領域においてだけ</strong>だ、というのが今回の結論です ── これは失敗ではなく、<em>適用範囲の確定</em>です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　効く場所は、プランク期しかなかった</h2>
<p>前シリーズが開いたまま閉じた扉に入りました ── <em>光シート上の情報量を縛れば予言が出るか</em>。使ったのは番外編③の \(s\le3H/4\ell_P^2\) で、使用率 \(f\) の履歴を追うと、<strong>プランク期にちょうど飽和し、そこから 33 桁の余裕が開いていきます</strong>（電弱期で 16 桁、元素合成で 22 桁、今日で 33 桁）。</p>
<p>「ちょうどプランク期で飽和する」は意味ありげですが、第19回の道具で測ると <strong>恒等式でした</strong> ── \(T\sim M_{\rm Pl}\) なら \(s\sim1/\ell_P^3\)、\(H\sim c/\ell_P\) で、次元解析だけから \(f\sim1\)。驚きは 0 ビット。ディラックの大数（第7回）、ランダウアー限界（第10回）に続く三つ目です。</p>
<p>そして核心 ── <strong>制約としては弱すぎます</strong>。今日の余裕が 33 桁あるので、排除されるのは「プランク期より前で破る膨張則」だけで、標準的なものはほぼ全部通る。<em>光シート上の情報量を縛っても、予言は出ません。</em> 恒等的に飽和させれば \(a\propto t^{1/3}\)（stiff）が出ますが、それは私たちの宇宙ではない ── ビット数を固定すればド・ジッター、アドレス空間を固定すれば \(a\propto t\)、使用率を固定すれば \(a\propto t^{1/3}\)。<strong>どの資源を固定するかで答えが三つに割れ、観測される宇宙はそのどれでもありません。</strong></p>
<p>だから扉は半分だけ閉まりました。番外編②の「縛るべきは光シート上の情報量」は<em>形としては正しかった</em> ── ブソーの境界は共形不変で、ゲージに依らない。けれど<strong>効く場所がプランク期しかない</strong>。これは失敗ではなく<em>適用範囲の確定</em>です ── 第16回で共形変換の限界を測ったのと同じように、今回はホログラフィック境界の限界を測りました。<strong>「宇宙は有限リソースの計算機だ」が意味を持つのは、量子重力の領域だけ</strong>。第 V 部で、そこへ行きます。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第21回</span>
第 III 部の残りは、時間の向きです ── <strong>エントロピー生成と、時間の矢の目盛り</strong>。第6回で「使用率 \(1.5\times10^{-18}\) は、いま道具がどれだけ壊れているかの数字でもある」と書きました。今回はさらに、<em>ホログラフィック境界の余裕（33 桁）</em>という別の目盛りも手に入っています。<strong>時間の矢を測る目盛りは、いくつあるのか</strong> ── 熱のエントロピー、重力のエントロピー、ホログラフィック余裕、そして第2回の a定理。<em>四本の目盛りが、同じ向きを指しているかどうかを確かめます。</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sp=document.getElementById('sp'), vp=document.getElementById('vp'), ro=document.getElementById('ro');
  var X0=78, X1=700, Y0=30, Y1=314;
  var tP=5.391e-44, t_eq=1.6e12, t0=4.3536e17;
  var LP=Math.log(tP)/Math.LN10, LEQ=Math.log(t_eq)/Math.LN10, L0=Math.log(t0)/Math.LN10;
  var F0=6.746e-34;
  var xmin=-46, xmax=20, ymin=-40, ymax=6;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function draw(){
    var p=parseInt(sp.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    // 境界を超えた領域
    g.fillStyle='#f7ece9';
    g.fillRect(X0, Y0, X1-X0, py(0)-Y0);
    g.fillStyle='#c08878'; g.textAlign='left';
    g.fillText('この上は境界を破る領域', X0+10, Y0+16);

    g.textAlign='right';
    for(var e=-40;e<=0;e+=10){
      var y=py(e);
      g.strokeStyle=(e===0?'#e0c4bc':'#f5eef2'); g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a8909c'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-40;q<=20;q+=10){
      var x=px(q);
      g.strokeStyle='#faf5f8'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a8909c'; g.fillText('10'+q, x, Y1+16);
    }
    g.strokeStyle='#d8c2ce'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // 境界 f=1
    g.strokeStyle='#a8452a'; g.lineWidth=2.4; g.setLineDash([7,5]);
    g.beginPath(); g.moveTo(X0,py(0)); g.lineTo(X1,py(0)); g.stroke();
    g.setLineDash([]);

    // 標準の熱史（区分的）
    g.strokeStyle='#2a6b2a'; g.lineWidth=3;
    g.beginPath();
    g.moveTo(px(LP),py(0));
    g.lineTo(px(LEQ),py(-0.5*(LEQ-LP)));
    g.lineTo(px(L0),py(-0.5*(LEQ-LP)-1.0*(L0-LEQ)));
    g.stroke();
    g.fillStyle='#2a6b2a'; g.textAlign='left';
    g.fillText('標準の熱史', px(-20), py(-0.5*(-20-LP))-8);

    // 指定した p（今日の f を通り、傾き 1-3p）
    var sl=1-3*p;
    g.strokeStyle='#6b2f5a'; g.lineWidth=3;
    g.beginPath();
    var first=true;
    for(var i=0;i<=300;i++){
      var lx=xmin+(xmax-xmin)*i/300;
      var y=Math.log(F0)/Math.LN10 + sl*(lx-L0);
      if(y<ymin||y>ymax){ first=true; continue; }
      if(first){ g.moveTo(px(lx),py(y)); first=false; } else g.lineTo(px(lx),py(y));
    }
    g.stroke();

    // f=1 に達する時刻
    var lv = L0 + (0-Math.log(F0)/Math.LN10)/sl;
    if(sl<0 && lv>xmin && lv<xmax){
      g.fillStyle='#6b2f5a';
      g.beginPath(); g.arc(px(lv),py(0),5.5,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=1.8;
      g.beginPath(); g.arc(px(lv),py(0),5.5,0,6.2832); g.stroke();
    }

    // プランク時刻・今日
    [[LP,'プランク'],[L0,'いま']].forEach(function(q){
      g.strokeStyle='#cbb5c2'; g.lineWidth=1.3; g.setLineDash([4,4]);
      g.beginPath(); g.moveTo(px(q[0]),Y0); g.lineTo(px(q[0]),Y1); g.stroke();
      g.setLineDash([]);
      g.fillStyle='#9a8090'; g.textAlign='center';
      g.fillText(q[1], px(q[0]), Y1-8);
    });

    g.fillStyle='#8a7080'; g.textAlign='center';
    g.fillText('宇宙の年齢  t [秒]', (X0+X1)/2, Y1+36);
    g.save(); g.translate(20,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('使用率 f = s / (3H/4ℓ_P²)', 0,0); g.restore();

    vp.textContent='p = '+p.toFixed(3);
    var msg;
    if(Math.abs(sl)<1e-6) msg='指数 0 → f は一定。飽和させ続けられる唯一の膨張則（w=1, stiff）';
    else if(sl>0) msg='指数 '+sl.toFixed(2)+' → 遡るほど余裕が増える。境界は決して破らない';
    else {
      var tv=Math.pow(10,lv);
      msg='指数 '+sl.toFixed(2)+' → f=1 になるのは t = '+tv.toExponential(2)+' 秒'+
          (lv<LP?'（プランク時刻より前 ── 破らない）':'（破る）');
    }
    ro.textContent='p = '+p.toFixed(3)+'　'+msg+'　／　今日の余裕は 33 桁';
  }
  sp.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-20-lightsheet.html', acc='#6b2f5a', ops='#2a6b2a',
      title='光シートを、本当に縛ってみる ── わかる c·t=一定 第20回',
      ep='第 20 回 ／ 前シリーズが開いたまま閉じた扉',
      eyebrow='縛ってみた結果、予言は出ませんでした ── その理由が面白い',
      h1='光シートを、<br>本当に縛ってみる',
      sub='ブソーの境界を制約として課すと、何が排除されるのか。<br><em>今日の余裕は33桁。効く場所は、プランク期しかありませんでした。</em>',
      byline_l='必要な道具：指数の足し算、対数',
      byline_r='\\(f\\propto t^{1-3p}\\)、今日 \\(f=6.7\\times10^{-34}\\)',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第20回、物理好きの高校生・大学生向け読み物です。共変エントロピー境界は Bousso (1999) によります。見かけの地平面に当てて \\(s\\le3H/4\\ell_P^2\\) を得る手続き、および恒等的に飽和させると \\(a\\propto t^{1/3}\\)（\\(w=1\\)）が出ることは前シリーズ番外編③で示した通りです。本稿の使用率 \\(f\\) の履歴（プランク期 \\(\\approx1\\)、電弱期 \\(7.3\\times10^{-17}\\)、元素合成 \\(2.3\\times10^{-22}\\)、再結合 \\(2.4\\times10^{-29}\\)、今日 \\(6.7\\times10^{-34}\\)）、および膨張則ごとの \\(f=1\\) 到達時刻は本稿での計算です（kenshou/calc24.py）。<strong>\\(s\\le3H/4\\ell_P^2\\) は見かけの地平面という特定の面に当てた結果であり、他の面ではより強い条件になりえます</strong>（番外編③⑧節と同じ注意）。エントロピーが共動的に保存されるという仮定に立っており、再加熱等の生成があれば余裕はさらに広がります（結論は強まる向き）。「プランク期に \\(f\\approx1\\)」は 1 ループ的な見積もりで、\\(g_*\\) の取り方で係数が動きます ── 02節の主張は「次元解析だけで \\(O(1)\\) になる」ことであって係数が厳密に 1 だということではありません。03節の到達時刻は単一の \\(p\\) を全時代に適用した粗い近似で、\\(c\\cdot t=\\)一定 の 11 秒は番外編③の 5 秒と同じ桁です。<strong>「予言が出ない」はこの形の制約についての結論であり、ホログラフィー一般が無力だという意味ではありません</strong> ── AdS/CFT のようにホログラフィーが強力な計算手段となる文脈は多数あります。前シリーズ番外編②の「縛るべきは光シート上の情報量」という提案に対する本稿の評価（形としては正しく、効き目としては足りない）は本シリーズの読み方です。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルです。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで膨張則を変え、天井（境界）を破る時刻が動く様子が見えます。「答えを見る」で解答が開きます。')
