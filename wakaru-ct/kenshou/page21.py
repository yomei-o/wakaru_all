# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">ここまでで、時間の向きを測る目盛りが<strong>四本</strong>そろいました ── 総エントロピー（第6回）、メモリ使用率（第6回）、ホログラフィック余裕（第20回）、そして自由度 \(a\)（第2回）。ところが妙なことに、<em>二本は増え、二本は減ります</em>。同じ時間の矢を測っているのに、向きが逆に見える。<strong>今回はその四本を突き合わせ、どこに時間の矢が入っているのかを特定します。</strong></p>

<h2><span class="n">01</span>四本の目盛り</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>目盛り</th><th class="mid">変化</th><th class="mid">桁数</th><th class="mid">向き</th><th class="mid">出どころ</th></tr></thead>
<tbody>
<tr><th>① 総エントロピー \(S/k_B\)</th><td class="mid">\(\sim1\to3.1\times10^{104}\)</td><td class="mid">\(+104\)</td><td class="mid"><strong>増える</strong></td><td class="mid">第6回</td></tr>
<tr><th>② メモリ使用率 \(S/S_{\max}\)</th><td class="mid">\(1\to1.5\times10^{-18}\)</td><td class="mid">\(-18\)</td><td class="mid"><strong>減る</strong></td><td class="mid">第6回</td></tr>
<tr><th>③ ホログラフィック余裕</th><td class="mid">0 桁 \(\to\) 33 桁</td><td class="mid">\(+33\)</td><td class="mid"><strong>増える</strong></td><td class="mid">第20回</td></tr>
<tr><th>④ 自由度 \(a\)（a定理）</th><td class="mid">\(995.5\to62.0\)</td><td class="mid">\(-1.2\)</td><td class="mid"><strong>減る</strong></td><td class="mid">第2回</td></tr>
</tbody>
</table>
</div>

<p>①と③が増え、②と④が減る。<strong>矛盾しているように見えます。</strong> ところが ──</p>

<h2><span class="n">02</span>四本とも、共形不変</h2>

<p>まず確認しておきます。この四本は、すべて無次元です。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>目盛り</th><th class="mid">中身</th><th class="mid">共形変換で</th></tr></thead>
<tbody>
<tr><th>総エントロピー</th><td class="mid">ビット数</td><td class="mid"><strong>不変</strong></td></tr>
<tr><th>メモリ使用率</th><td class="mid">ビット ÷ ビット</td><td class="mid"><strong>不変</strong></td></tr>
<tr><th>ホログラフィック余裕</th><td class="mid">比の対数</td><td class="mid"><strong>不変</strong></td></tr>
<tr><th>自由度 \(a\)</th><td class="mid">純粋な数</td><td class="mid"><strong>不変</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0"><strong>時間の矢は、まるごと「物理」の列にあります。</strong><br>
第16回のウェイトの地図でいえば、四本とも <em>ウェイト 0 の列</em>。<br>
── <strong>帳簿の書き換えでは、時間の向きに一切触れられない。</strong></p>
</div>

<p>これは前シリーズ番外編②の表（共形因子の側は時間の矢を持たない／ワイル側だけが持つ）を、四本の目盛りで裏づけたことになります。</p>

<h2><span class="n">03</span>核心 ── 分子と分母を、同じ速さで比べる</h2>

<p>向きが逆に見えるのは、<strong>比を取っているものと、取っていないものが混ざっている</strong>からです。分けて、同じ単位（1 対数ステップあたりの桁数）に揃えます。</p>

<div class="calc">
<span class="tag">計算 ── 140 ステップで割る</span>
<p class="lbl">分母（容量）：プランク期の \(\sim1\) から今日の \(2.05\times10^{122}\) へ</p>
$$\frac{122.31\ \text{桁}}{140.24\ \text{ステップ}}=0.872\ \text{桁/ステップ}$$
<p class="lbl">分子（実際のエントロピー）：\(\sim1\) から \(3.1\times10^{104}\) へ</p>
$$\frac{104.49\ \text{桁}}{140.24\ \text{ステップ}}=0.745\ \text{桁/ステップ}$$
<p class="lbl">差</p>
$$0.127\ \text{桁/ステップ}$$
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0">分子も分母も、猛烈な勢いで増えています。<strong>分母がわずかに（1 ステップあたり 0.13 桁）速いだけ。</strong><br>
その 0.13 桁の差が 140 ステップぶん積もって、<em>18 桁の空き</em>になりました。</p>
</div>

<div class="calc">
<span class="tag">検算</span>
$$0.127\times140.24=17.8\ \text{桁}\qquad\Longrightarrow\qquad \text{使用率}=1.5\times10^{-18}$$
<p class="lbl">第6回の実測値と一致</p>
</div>

<p>だから「二本は増えて二本は減る」は矛盾ではありません ── <strong>①（分子）は増え、②③（比）は分母の勝ち負けで決まっている</strong>だけです。分母は膨張が決めるので、<em>比の向きは膨張則しだい</em>。</p>

<div class="fig">
<p class="cap">図：分子（実際のエントロピー）と分母（ホログラフィック容量）が、対数ステップごとにどう伸びるか。<strong>どちらも猛烈に増えていて、傾きの差はわずか 0.13 桁/ステップ</strong>。塗った部分が「空き」で、140 ステップで 18 桁になります</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>いまどのステップを見るか（右端が今日）<input id="sn" type="range" min="0" max="1402" value="1402" step="1"></label>
  <span class="val" id="vn">140.2 ステップ</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1f5a6b"></i>分母：容量 \(S_{\max}\)（0.872 桁/ステップ）</span>
  <span><i class="swatch" style="background:#8a6a2a"></i>分子：エントロピー \(S_{\rm obs}\)（0.745 桁/ステップ）</span>
  <span><i class="swatch" style="background:#c8dde2"></i>空き</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>では、時間の矢はどこにあるのか</h2>

<div class="seven">
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>分子にある</strong><span>熱力学第二法則が縛るのは \(S_{\rm obs}\)。これは<em>絶対に減らない</em>。時間の矢の本体はここ</span></div></div>
<div class="row"><div class="mk">△</div><div class="txt"><strong>分母は舞台</strong><span>容量 \(S_{\max}\propto R_H^2\) は幾何が決める。膨張則が変われば向きも変わる（ド・ジッターなら一定になる）</span></div></div>
<div class="row"><div class="mk">△</div><div class="txt"><strong>比は、二つの競争の結果</strong><span>使用率も余裕も「分子 ÷ 分母」なので、<em>どちらが速いか</em>で向きが決まる ── 時間の矢そのものではない</span></div></div>
</div>

<p>第6回で「<em>道具が壊れていく度合いが、時間の矢</em>」と書きました。今回の言葉で言い直すと ── <strong>あれは比（②）で測った言い方</strong>です。正確には、道具が壊れるのは分子が増えるからで、それが薄まって見えるのは分母がもっと速いから。<em>二つを混ぜずに言えば、時間の矢は分子だけにあります。</em></p>

<h2><span class="n">05</span>a定理は、別の軸にいる</h2>

<p>四本目の \(a\) だけは、少し立ち位置が違います。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th class="mid">①②③</th><th class="mid">④ a定理</th></tr></thead>
<tbody>
<tr><th>何の向きか</th><td class="mid">宇宙時間</td><td class="mid"><strong>繰り込み群（エネルギー）</strong></td></tr>
<tr><th>軸</th><td class="mid">\(\ln t\)（140 ステップ）</td><td class="mid">\(\ln\mu\)（73 ステップ）</td></tr>
<tr><th>減る理由</th><td class="mid">膨張が容量を広げる</td><td class="mid">粗視化で情報を捨てる</td></tr>
<tr class="hi"><th>共通点</th><td class="mid" colspan="2"><strong>どちらも「忘却」── 戻れない向きがある</strong></td></tr>
</tbody>
</table>
</div>

<p>第2回で見た通り、この二つの軸は \(d\ln T/d\ln t=-p\) で結ばれています。<strong>宇宙時間の 1 ステップは、繰り込み群の \(p=0.513\) ステップ</strong>。だから \(a\) の減り方を宇宙時間に換算でき、実働区間（ステップ 74〜132）で <em>1 ステップあたり 4.8%</em> の忘却になります。</p>

<div class="aside">
<span class="tag">四本を一行にまとめると</span>
<strong>分子（エントロピー）が増え、分母（容量）はもっと速く増え、自由度は別の軸で減る。</strong><br>
三つとも「戻れない」向きを持ち、三つとも無次元で、三つとも共形変換で動かない ── <em>時間の矢は、このシリーズが「物理」と呼んできた列に、まるごと収まっています</em>。
</div>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 「プランク期の \(S_{\rm obs}\sim1\)」は目安です。</strong> 初期宇宙のエントロピーをどう数えるかは自明ではなく（地平面内の粒子数か、ホライズンエントロピーか）、桁の議論として読んでください。03節の 0.745 桁/ステップは、この目安に依存します。</p>
<p style="margin:0 0 10px"><strong>② \(S_{\rm obs}=3.1\times10^{104}k_B\) は Egan &amp; Lineweaver (2010) の集計値で、超巨大ブラックホールの質量関数に強く依存します</strong>（第6回①と同じ注意）。分子の伸びの大半はブラックホール形成なので、<em>その不確かさがそのまま 0.745 の不確かさになります</em>。</p>
<p style="margin:0 0 10px"><strong>③ 「分子は絶対に減らない」は、閉じた系についての熱力学第二法則です。</strong> 宇宙が閉じた系かどうか、地平面の内側を系とみなしてよいかは、それ自体が未解決の論点です ── 地平面を横切る流れがあるので、素朴な第二法則の適用には注意が要ります。</p>
<p style="margin:0 0 10px"><strong>④ \(a\) は共形固定点でのみ定義される量です</strong>（第2回・前シリーズ番外編⑦）。「\(a\) が 995.5 から 62 へ減る」は自由場勘定による模式図で、a定理の検証ではありません。「1 ステップあたり 4.8%」も同様です。</p>
<p style="margin:0"><strong>⑤ 「時間の矢は分子にある」は本シリーズの整理です。</strong> 時間の矢の起源をめぐる議論（過去仮説、ワイル曲率仮説、脱コヒーレンス、宇宙論的初期条件）はどれも決着しておらず、本稿はそのどれかを支持するものではありません ── <em>四本の目盛りが互いに矛盾しないことを確かめた</em>、というのが今回の範囲です。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>四本の目盛りのうち、増えるものと減るものを挙げよ。
<details><summary>答えを見る</summary><div class="ans">増える：総エントロピー（\(+104\) 桁）、ホログラフィック余裕（\(+33\) 桁）。減る：メモリ使用率（\(-18\) 桁）、自由度 \(a\)（\(-1.2\) 桁）。<em>矛盾ではありません</em> ── 比を取っているものと取っていないものが混ざっているだけです。</div></details></li>

<li>分子と分母の伸びを、1 ステップあたりの桁数で求めよ。
<details><summary>答えを見る</summary><div class="ans">分母 \(122.31/140.24=0.872\) 桁/ステップ、分子 \(104.49/140.24=0.745\) 桁/ステップ。<strong>差は 0.127</strong>。140 ステップで 17.8 桁になり、使用率 \(1.5\times10^{-18}\) と一致します。</div></details></li>

<li>四本とも共形変換で動かないのはなぜか。
<details><summary>答えを見る</summary><div class="ans">四本とも無次元（ビット数、比、比の対数、純粋な数）だから。第16回のウェイトの地図でいう<strong>ウェイト 0 の列</strong>にあります ── <em>帳簿の書き換えでは、時間の向きに一切触れられない</em>。</div></details></li>

<li>「道具が壊れていく度合いが時間の矢」（第6回）を、今回の言葉で言い直せ。
<details><summary>答えを見る</summary><div class="ans">あれは<strong>比（使用率）で測った言い方</strong>です。正確には、道具が壊れる（＝ワイル側が育つ）のは分子が増えるからで、それが薄まって見えるのは分母がもっと速いから。<em>二つを混ぜずに言えば、時間の矢は分子だけにあります。</em></div></details></li>

<li>（やや難）\(a\) 定理は、他の三本と同じ時間の矢か。
<details><summary>答えを見る</summary><div class="ans">向きは同じ（戻れない）ですが、<strong>軸が違います</strong> ── ①②③は宇宙時間 \(\ln t\)（140 ステップ）、\(a\) は繰り込み群のエネルギー軸 \(\ln\mu\)（73 ステップ）。第2回の \(d\ln T/d\ln t=-p\) で結ばれるので換算はでき、実働区間で 1 ステップあたり 4.8% の忘却になります。<em>どちらも「粗視化すると戻れない」という同じ形をしている</em>のが共通点です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　矢は分子にあり、分母は舞台だった</h2>
<p>時間の向きを測る目盛りが四本そろいました ── 総エントロピー（\(+104\) 桁）、メモリ使用率（\(-18\) 桁）、ホログラフィック余裕（\(+33\) 桁）、自由度 \(a\)（\(-1.2\) 桁）。二本が増え、二本が減る。<strong>まず確認したのは、四本とも無次元＝共形不変だ</strong>ということです ── <em>時間の矢は、まるごと「物理」の列にある</em>。帳簿の書き換えでは、向きに一切触れられません。</p>
<p>向きが逆に見えたのは、比を取っているものと取っていないものが混ざっていたからでした。同じ単位に揃えると ── <strong>分母（容量）は 0.872 桁/ステップ、分子（エントロピー）は 0.745 桁/ステップ</strong>。<em>どちらも猛烈に増えていて、差はわずか 0.127 桁/ステップ</em>。それが 140 ステップ積もって 17.8 桁になり、第6回の使用率 \(1.5\times10^{-18}\) にぴたりと一致します。</p>
<p>だから時間の矢の居場所がはっきりします ── <strong>矢は分子にある</strong>。熱力学第二法則が縛るのは \(S_{\rm obs}\) で、これは絶対に減らない。分母は幾何（膨張）が決める舞台で、比はその競争の結果にすぎません。第6回の「道具が壊れていく度合いが時間の矢」は、<em>比で測った言い方</em>だったことになります。</p>
<p>四本目の \(a\) だけは軸が違いました ── 宇宙時間ではなく<strong>繰り込み群のエネルギー軸</strong>。第2回の \(d\ln T/d\ln t=-p\) で換算でき、実働区間で 1 ステップあたり 4.8% の忘却。<em>軸は違っても、「粗視化すると戻れない」という形は同じ</em>です。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第22回</span>
第 III 部の後半は、計算機としての宇宙を<strong>もう一段具体的に</strong>書きます ── <em>命令セット</em>です。第1回でスペック（メモリ・クロック・演算）を取りましたが、「演算」の中身は空欄のままでした。マルゴラス＝レヴィティン限界が数えているのは<strong>直交状態への遷移</strong>だけで、何をしているかは問いません。では宇宙が実際にやっている操作は何か ── <em>粒子の伝播、相互作用、測定（脱コヒーレンス）</em>。それぞれのコストをビットで見積もり、\(10^{121}\) 回の内訳を作ります。<strong>ほとんどが「何もしない」に使われている</strong>はずです。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sn=document.getElementById('sn'), vn=document.getElementById('vn'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=316;
  var A=0.872, B=0.745, NMAX=140.24;
  var xmin=0, xmax=145, ymin=0, ymax=130;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function draw(){
    var n=parseInt(sn.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right';
    for(var e=0;e<=130;e+=20){
      var y=py(e);
      g.strokeStyle='#eef4f5'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#93a8ad'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=140;q+=20){
      var x=px(q);
      g.strokeStyle='#f5f9fa'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#93a8ad'; g.fillText(String(q), x, Y1+16);
    }
    g.strokeStyle='#c3d6da'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // 空き（塗り）
    g.fillStyle='#c8dde2'; g.globalAlpha=0.55;
    g.beginPath();
    g.moveTo(px(0),py(0));
    g.lineTo(px(n),py(A*n));
    g.lineTo(px(n),py(B*n));
    g.closePath(); g.fill();
    g.globalAlpha=1;

    // 二本
    g.strokeStyle='#1f5a6b'; g.lineWidth=3.2;
    g.beginPath(); g.moveTo(px(0),py(0)); g.lineTo(px(NMAX),py(A*NMAX)); g.stroke();
    g.strokeStyle='#8a6a2a'; g.lineWidth=3.2;
    g.beginPath(); g.moveTo(px(0),py(0)); g.lineTo(px(NMAX),py(B*NMAX)); g.stroke();

    g.textAlign='left';
    g.fillStyle='#1f5a6b'; g.fillText('容量 S_max（0.872 桁/ステップ）', px(92), py(A*92)-10);
    g.fillStyle='#8a6a2a'; g.fillText('エントロピー S_obs（0.745）', px(92), py(B*92)+18);

    // カーソル
    g.strokeStyle='#5a7a80'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(n),Y0); g.lineTo(px(n),Y1); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#1f5a6b';
    g.beginPath(); g.arc(px(n),py(A*n),4.5,0,6.2832); g.fill();
    g.fillStyle='#8a6a2a';
    g.beginPath(); g.arc(px(n),py(B*n),4.5,0,6.2832); g.fill();

    g.fillStyle='#6b858a'; g.textAlign='center';
    g.fillText('対数ステップ  ln(t / t_P)', (X0+X1)/2, Y1+36);

    var gap=(A-B)*n;
    vn.textContent=n.toFixed(1)+' ステップ';
    ro.textContent='ステップ '+n.toFixed(1)+
      '　容量 10^'+(A*n).toFixed(1)+
      '　エントロピー 10^'+(B*n).toFixed(1)+
      '　→　空き '+gap.toFixed(1)+' 桁　＝　使用率 '+Math.pow(10,-gap).toExponential(2)+
      (n>139?'　★ 今日の 1.5×10⁻¹⁸ と一致':'');
  }
  sn.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-21-arrows.html', acc='#1f5a6b', ops='#8a6a2a',
      title='時間の矢の目盛りは、四本ある ── わかる c·t=一定 第21回',
      ep='第 21 回 ／ 四本の目盛りを、突き合わせる',
      eyebrow='二本は増え、二本は減る ── 矛盾ではありませんでした',
      h1='時間の矢の目盛りは、<br>四本ある',
      sub='総エントロピー、メモリ使用率、ホログラフィック余裕、自由度 \\(a\\)。<br><em>同じ向きを指しているのか、突き合わせます。</em>',
      byline_l='必要な道具：桁数の引き算',
      byline_r='0.872 − 0.745 = 0.127 桁/ステップ',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第21回、物理好きの高校生・大学生向け読み物です。本回は第2回・第6回・第20回の結果を突き合わせたもので、新しい物理の主張はありません。分母 \\(S_{\\max}=2.05\\times10^{122}\\)（地平面のホログラフィック上限）、分子 \\(S_{\\rm obs}=3.1\\times10^{104}k_B\\)（Egan &amp; Lineweaver 2010, ApJ 710, 1825）、対数ステップ \\(\\ln(t_0/t_P)=140.24\\) から、0.872 桁/ステップと 0.745 桁/ステップ、差 0.127、140 ステップで 17.8 桁という計算は本稿でのものです（kenshou/calc25.py）。<strong>「プランク期の \\(S_{\\rm obs}\\sim1\\)」は目安であり、初期宇宙のエントロピーの数え方は自明ではありません</strong> ── 0.745 桁/ステップはこの目安に依存します。\\(S_{\\rm obs}\\) は超巨大ブラックホールの質量関数に強く依存し、その不確かさがそのまま分子の伸びの不確かさになります。「分子は絶対に減らない」は閉じた系についての熱力学第二法則で、<strong>地平面の内側を閉じた系とみなしてよいかは未解決の論点です</strong>（地平面を横切る流れがあります）。\\(a\\) は共形固定点でのみ定義される量であり、「995.5 → 62」は自由場勘定による模式図で a定理の検証ではありません（前シリーズ番外編⑦）。「1 ステップあたり 4.8%」も同様です。二つの軸を結ぶ \\(d\\ln T/d\\ln t=-p\\) は第2回で導いた関係です。<strong>「時間の矢は分子にある」は本シリーズの整理であり</strong>、時間の矢の起源をめぐる議論（過去仮説、Weyl 曲率仮説、脱コヒーレンス、宇宙論的初期条件）はいずれも決着しておらず、本稿はそのどれかを支持するものではありません ── 四本の目盛りが互いに矛盾しないことを確かめた、というのが本回の範囲です。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルです。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーでステップを動かし、二本の差（空き）が開いていく様子が見えます。「答えを見る」で解答が開きます。')
