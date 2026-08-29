# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第 II 部の 10 本を、一枚に畳みます。重力・量子力学・原子・熱と情報・光・真空・流体・相転移・化学生物 ── <strong>どこに入れても、動いたのはいつも一つだけ</strong>でした。そして動かなかったものを全部並べると、それがそのまま<em>「物理とは何か」の一覧</em>になります。最後に、この記法が<strong>本当に役に立つ場所</strong>と<strong>まったく無力な場所</strong>を線引きして、第 II 部を閉じます。</p>

<h2><span class="n">01</span>10 本を、一行ずつ</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">回</th><th>入れた先</th><th>動いたもの</th><th>動かなかったもの</th></tr></thead>
<tbody>
<tr><th class="mid">7</th><td>重力</td><td>\(G\)（\(\div a^2\)）、\(g\)、\(r_s\)、\(T_H\)</td><td><strong>\(\alpha_G\)、ディラックの大数、BH エントロピー、重力波の \(h\)</strong></td></tr>
<tr><th class="mid">8</th><td>量子力学</td><td>ド・ブロイ波長、準位、コンプトン波長</td><td><strong>方程式の形、\(\Delta x\Delta p\)、\(S/\hbar\)、トンネル透過率</strong></td></tr>
<tr><th class="mid">9</th><td>原子</td><td>ボーア半径（\(7.2\times10^{-11}\)/年）</td><td><strong>スペクトル線、\(\alpha\)、\(\mu=m_p/m_e\)</strong></td></tr>
<tr><th class="mid">10</th><td>熱と情報</td><td>温度、ランダウアーのコスト</td><td><strong>エントロピー、ボルツマン因子、第二法則</strong></td></tr>
<tr><th class="mid">11</th><td>光</td><td>（何も動かない）</td><td><strong>\(n_\gamma\)、\(\rho_\gamma\)、\(T\)、\(\lambda\)、\(s/n\)、\(\eta_b\)</strong></td></tr>
<tr><th class="mid">12</th><td>真空</td><td>\(\rho_\Lambda\)（\(\propto t^4\)）、\(\rho_m\)、順位</td><td><strong>\(\rho_\Lambda/M_{\rm Pl}^4\)、\(w=-1\)、等密度点</strong></td></tr>
<tr><th class="mid">13</th><td>流体と乱流</td><td>\(\rho\)、\(\eta\)、\(L\)（バラバラに）</td><td><strong>Re・Ma・Pr・Fr・We・St、\(-5/3\) 則</strong></td></tr>
<tr><th class="mid">14</th><td>相転移</td><td>──</td><td><strong>臨界指数、\(\Delta\)</strong>（ただし<em>ウェイト表そのものに誤差棒</em>）</td></tr>
<tr><th class="mid">15</th><td>化学と生物</td><td>体重、体長、代謝率、寿命</td><td><strong>アレニウス因子、一生の心拍、遺伝情報</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0">左の列は<strong>全部が次元付き</strong>、右の列は<strong>全部が無次元</strong>。<br>
9 本の異なる分野で、例外は一つもありませんでした。</p>
</div>

<h2><span class="n">02</span>ウェイトの地図</h2>

<p>第 II 部で出てきた量を、ウェイトごとに並べ直します。これが完成版の表です。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">ウェイト</th><th class="mid">この絵で</th><th>そこに住む量</th></tr></thead>
<tbody>
<tr><th class="mid">\(+3\)</th><td class="mid">\(\times a^3\)</td><td>数密度</td></tr>
<tr><th class="mid">\(+2\)</th><td class="mid">\(\times a^2\)</td><td>面積、\(1/G\)</td></tr>
<tr><th class="mid">\(+1\)</th><td class="mid">\(\times a\)</td><td>長さ、時間、波長、ボーア半径、コンプトン波長、寿命、動粘性率、コルモゴロフ長</td></tr>
<tr class="hi"><th class="mid">\(0\)</th><td class="mid"><strong>不変</strong></td><td><strong>速度・\(c\)・\(\hbar\)・\(e\)・\(\alpha\)・\(\alpha_G\)・エントロピー・ビット・位相・すべての比・すべての指数</strong></td></tr>
<tr><th class="mid">\(-1\)</th><td class="mid">\(\div a\)</td><td>質量、エネルギー、温度、振動数、重力加速度、リアプノフ指数、散逸率</td></tr>
<tr><th class="mid">\(-2\)</th><td class="mid">\(\div a^2\)</td><td>曲率 \(R\)、代謝率、潮汐力</td></tr>
<tr><th class="mid">\(-3\)</th><td class="mid">\(\div a^3\)</td><td>粘性率、表面張力</td></tr>
<tr><th class="mid">\(-4\)</th><td class="mid">\(\div a^4\)</td><td>エネルギー密度、質量密度、圧力</td></tr>
</tbody>
</table>
</div>

<p>（表の「この絵で」は \(\tilde X=a^{-w}X\) の向きで書いています。ウェイト \(+1\) の長さは \(\div a\) で縮み、ウェイト \(-1\) の質量は \(\times a\) で育つ ── <em>符号と向きが逆なので、いつも混乱するところ</em>です。）</p>

<div class="fig">
<p class="cap">図：ウェイトの地図。ツマミで時代を遡ると、<strong>ウェイト 0 の列だけが動きません</strong>。他の列は \(a^{-w}\) で上下に散っていきます ── そして観測にかかるのは、動かない列だけ</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>いつの時代で見るか \(\log_{10}a\)（右端が今日）<input id="sa" type="range" min="-2000" max="0" value="-800" step="1"></label>
  <span class="val" id="va">a = 0.158</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1a3a3a"></i>次元付き（動く）</span>
  <span><i class="swatch" style="background:#9a5a2a"></i>ウェイト 0（動かない ＝ 物理）</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>役に立つ場所と、無力な場所</h2>

<p>第 II 部を通してはっきりしたのは、<strong>この記法にははっきりした適用範囲がある</strong>ということです。</p>

<div class="seven">
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>役に立つ：次元付きの量が主役の場所</strong><span>宇宙論と重力。膨張、曲率、\(G\)、質量スケール ── 記法を替えると<em>式が短くなり、見え方が変わる</em>（第4回：距離も年齢も閉じた式に）</span></div></div>
<div class="row"><div class="mk">△</div><div class="txt"><strong>中立：無次元と次元付きが混ざる場所</strong><span>量子力学、原子、熱。<em>不変なものと動くものを分ける訓練</em>にはなるが、新しい結論は出ない</span></div></div>
<div class="row"><div class="mk">✗</div><div class="txt"><strong>無力：最初から無次元で書かれている場所</strong><span>流体の相似則、臨界現象、情報理論、生物のスケーリング則。<em>この道具は何の情報も与えません</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>共形変換は、「大きさ」にしか触れない道具です。</strong><br>
だから大きさが主役の学問では強力で、かたちが主役の学問では無力。<br>
<em>そしてこの線引きは、道具の欠点ではなく、道具の定義そのものです。</em></p>
</div>

<h2><span class="n">04</span>ただし、ウェイト表自体に誤差棒が付く</h2>

<p>第14回で見つけた但し書きを、ここに置いておきます。02節の表は<strong>次元解析で作った古典近似</strong>です。場の理論では \(\Delta=\Delta_{\text{古典}}+\gamma\) で、\(\gamma\) は測定の対象でした ── 3 次元イジングで \(\gamma_\sigma=0.0181489(10)\)、7 桁。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>層</th><th>崩れるか</th><th class="mid">根拠</th></tr></thead>
<tbody>
<tr><th>測られる無次元量（比・指数・ビット）</th><td>崩れない</td><td class="mid">観測量だから</td></tr>
<tr class="hi"><th>ウェイトの値そのもの</th><td><strong>崩れる（量子補正）</strong></td><td class="mid">第14回、\(\gamma_\sigma\)</td></tr>
<tr><th>幾何のウェイト（長さ・時間）</th><td>崩れない</td><td class="mid">計量の定義だから</td></tr>
</tbody>
</table>
</div>

<p>だから正確には ── <em>「無次元だから安全」ではなく、「観測量だから安全」</em>。第 V 部では、この区別が効いてくる場所（アノマリー、ゴースト、回転する時空）を掘ります。</p>

<h2><span class="n">05</span>第 I 部と合わせて、ここまでの地図</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">部</th><th>やったこと</th><th class="mid">結論</th></tr></thead>
<tbody>
<tr><th class="mid">I</th><td>記法をつくる（第1〜6回）</td><td class="mid">\(c\cdot t=\)一定 は<strong>記法</strong>であって、モデルではない</td></tr>
<tr class="hi"><th class="mid">II</th><td>方程式に片っ端から入れる（第7〜16回）</td><td class="mid">どこでも<strong>動くのは一つだけ</strong>。触れるのは大きさだけ</td></tr>
<tr><th class="mid">III</th><td>情報として測る（第17〜26回）</td><td class="mid">これから</td></tr>
</tbody>
</table>
</div>

<div class="caveat">
<span class="tag">正直な線 ── 第 II 部全体について</span>
<p style="margin:0 0 10px"><strong>① 第 II 部で新しい物理は一つも出ていません。</strong> やったのは、既知の法則を別の記法で書き直し、何が動いて何が動かないかを数えることだけです。<em>それでも意味があると思うのは、「動かないもの＝物理」の一覧が、9 つの分野で例外なく成り立つのを確かめられたから</em>です。</p>
<p style="margin:0 0 10px"><strong>② 表の「動いた／動かなかった」は、宇宙全体をまとめて書き換える場合の話です。</strong> 実験室で固定された条件（決まった粘性率の液体、恒温槽、外部電場）を置くと、その量は勝手には変換されません。この注意は第8回①・第13回①・第15回③で繰り返した通りです。</p>
<p style="margin:0 0 10px"><strong>③ ウェイトの符号の向きは、規約です。</strong> 本稿は \(\tilde X=\Omega^{w}X\)（\(\Omega=1/a\)）と取り、長さを \(w=+1\)、質量を \(-1\) としています。文献によっては符号が逆だったり、\(\Delta=-w\) と書いたりします ── <em>比べるときは必ず規約を確認してください</em>。</p>
<p style="margin:0"><strong>④ 「役に立つ／無力」の線引きは、本シリーズの評価です。</strong> 共形場理論のように、無次元量が主役でありながら共形変換が決定的な役割を果たす分野もあります（前シリーズ番外編⑥）── そこでは<em>変換そのものではなく、変換に対する不変性（対称性）</em>が働いています。本稿が「無力」と言っているのは<strong>この記法（Weyl 変換で書き換える操作）</strong>についてです。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（第 II 部の総まとめ）</p>
<ol>
<li>第 II 部で「動いた」量に共通する性質は何か。
<details><summary>答えを見る</summary><div class="ans"><strong>全部が次元付き</strong>。\(G\)、ボーア半径、温度、\(\rho_\Lambda\)、粘性率、体重 ── 9 つの分野にまたがって、例外は一つもありませんでした。逆に「動かなかった」量は全部が無次元です。</div></details></li>

<li>ウェイト \(+1\) の量を三つ、\(-1\) の量を三つ挙げよ。
<details><summary>答えを見る</summary><div class="ans">\(+1\)（\(\div a\)）：長さ、時間、波長、ボーア半径、寿命、コルモゴロフ長。\(-1\)（\(\times a\)）：質量、エネルギー、温度、振動数、重力加速度、リアプノフ指数。<em>符号と向きが逆なので、混乱しやすいところです。</em></div></details></li>

<li>この記法が無力なのは、どういう学問か。理由も。
<details><summary>答えを見る</summary><div class="ans"><strong>最初から無次元で書かれている学問</strong> ── 流体の相似則、臨界現象、情報理論、生物のスケーリング則。この道具は「大きさ」にしか触れないので、無次元しか出てこない場所では何の情報も与えません（第13回）。<em>これは欠点ではなく、道具の定義そのもの</em>です。</div></details></li>

<li>「無次元だから安全」は、正確な言い方か。
<details><summary>答えを見る</summary><div class="ans">正確ではありません。第14回で見た通り、<strong>ウェイトの値そのものには量子補正（異常次元）が付き</strong>、3 次元イジングでは \(\gamma_\sigma=0.0181489\) と 7 桁で測られています。正確には <em>「観測量だから安全」</em> ── 測られる無次元量は動かないが、古典的に予想したウェイトは外れうる。</div></details></li>

<li>（やや難）第 II 部で新しい物理は出たか。では何のためにやったのか。
<details><summary>答えを見る</summary><div class="ans">新しい物理は<strong>一つも出ていません</strong>。やったのは既知の法則を別の記法で書き直し、何が動くかを数えることだけ。意味があるとすれば、<em>「動かないもの＝物理」という一覧が、重力から生物まで 9 つの分野で例外なく成り立つのを確かめられた</em>こと ── そして<strong>道具の適用範囲を正確に測れた</strong>ことです。前シリーズ最終回の判定手続きに、実際の使用実績が付いた形になります。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　動くのは、いつも一つだった</h2>
<p>第 II 部では、重力・量子力学・原子・熱と情報・光・真空・流体・相転移・化学生物の 9 分野に、同じ記法を入れました。結果はいつも同じ形でした ── <strong>動いたのは全部が次元付き、動かなかったのは全部が無次元</strong>。9 分野にまたがって、例外は一つもありません。</p>
<p>ウェイトの地図も完成しました。\(+3\) に数密度、\(+1\) に長さ・時間・寿命、\(0\) に速度と \(\hbar\) とエントロピーとすべての比、\(-1\) に質量・エネルギー・温度、\(-4\) にエネルギー密度。<strong>そして観測にかかるのは、\(0\) の列だけ</strong>です。</p>
<p>いちばんはっきりしたのは、<em>道具の適用範囲</em>でした。共形変換は「大きさ」にしか触れないので ── <strong>大きさが主役の学問（宇宙論・重力）では強力、かたちが主役の学問（流体・臨界現象・情報・生物）では完全に無力</strong>。これは欠点ではなく、道具の定義そのものです。第4回で宇宙論が「質量ひとつ」に潰れたのと同じ勢いで、第13回のナビエ＝ストークス方程式は一文字も潰れませんでした。</p>
<p>ただし但し書きが一つ ── 第14回で見つけたとおり、<strong>ウェイト表そのものは古典近似</strong>で、\(\gamma_\sigma=0.0181489(10)\) という誤差棒が付いています。だから正確には「無次元だから安全」ではなく <em>「観測量だから安全」</em>。この区別が効いてくる場所は、第 V 部でまとめて扱います。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第17回（第 III 部のはじまり）</span>
ここから第 III 部は、<strong>情報として測る</strong>部です。最初は通信 ── CMB は \(10^4\) 個の因果的に切れたパッチにまたがって \(\Delta T/T\sim10^{-5}\) で一様です。情報の言葉に直すと、<em>メッセージを一通も交換していない \(10^4\) 台のノードが、17 ビットぶん合意している</em>。分散システムなら不可能とされる状況です。\(c\cdot t=\text{一定}\) はノードが増えない唯一の膨張則なので、この問題を原理的に持ちません ── <strong>持たないはずでした。放射を入れるまでは。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sa=document.getElementById('sa'), va=document.getElementById('va'), ro=document.getElementById('ro');
  var X0=54, X1=700, YB=250;
  var COLS=[[3,'数密度'],[2,'面積'],[1,'長さ・時間'],[0,'比・指数・ビット'],[-1,'質量・温度'],[-2,'曲率'],[-3,'粘性率'],[-4,'密度・圧力']];

  function draw(){
    var la=parseInt(sa.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);

    var maxexp=4*Math.abs(la);
    var scale=Math.min(46, 150/Math.max(maxexp,1));

    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.textAlign='right';
    for(var e=-8;e<=8;e+=2){
      var y=YB-e*scale;
      if(y<24||y>YB+8) continue;
      g.strokeStyle=(e===0?'#c2d0d0':'#eef3f3'); g.lineWidth=(e===0?1.6:1);
      g.beginPath(); g.moveTo(X0-6,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#8fa3a3'; g.fillText(e===0?'×1':'10'+e, X0-10, y+4);
    }

    var n=COLS.length, w=62, gap=(X1-X0-n*w)/(n+1);
    for(var i=0;i<n;i++){
      var wt=COLS[i][0], ex=-wt*la;
      var x=X0+gap+(w+gap)*i, h=ex*scale;
      var zero=(wt===0);
      g.fillStyle=zero?'#9a5a2a':'#1a3a3a';
      g.globalAlpha=zero?0.95:0.8;
      if(zero) g.fillRect(x, YB-3, w, 6);
      else g.fillRect(x, h>=0? YB-h : YB, w, Math.abs(h));
      g.globalAlpha=1;
      g.fillStyle=zero?'#7a4418':'#12292a'; g.textAlign='center';
      g.font='bold 12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillText((wt>0?'+':'')+wt, x+w/2, YB+20);
      g.font='10px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillStyle=zero?'#9a6a3a':'#5a7070';
      var lab=COLS[i][1];
      if(lab.length>7){ g.fillText(lab.slice(0,7), x+w/2, YB+36); g.fillText(lab.slice(7), x+w/2, YB+48); }
      else g.fillText(lab, x+w/2, YB+36);
      g.font='10px sans-serif'; g.fillStyle=zero?'#7a4418':'#6a8080';
      g.fillText('×10'+(ex>=0?'+':'')+ex.toFixed(1), x+w/2, YB-Math.max(h,0)-8);
    }

    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillStyle='#5a7070'; g.textAlign='center';
    g.fillText('ウェイト w　── この絵での倍率は a^(−w)', (X0+X1)/2, YB+76);
    g.fillStyle='#9a5a2a'; g.font='bold 12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('観測にかかるのは、この列だけ', X0+gap+(w+gap)*3+w/2, YB+62);

    var a=Math.pow(10,la);
    va.textContent='a = '+(a<0.01? a.toExponential(2) : a.toFixed(3));
    ro.textContent='a = '+va.textContent+'（z = '+(1/a-1).toPrecision(3)+'）　'+
      '長さ ×10'+(-la).toFixed(1)+'　質量 ×10'+(la).toFixed(1)+'　密度 ×10'+(4*la).toFixed(1)+
      '　→　ウェイト 0 の列は ×1.000 のまま';
  }
  sa.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-16-partII.html', acc='#1a3a3a', ops='#9a5a2a',
      title='動くのは、いつも一つ ── わかる c·t=一定 第16回（第II部・総括）',
      ep='第 16 回 ／ 第 II 部・総括',
      eyebrow='9つの分野で、例外は一つもありませんでした',
      h1='動くのは、<br>いつも一つ',
      sub='重力から生物まで、同じ記法を入れて何が動くかを数えました。<br><em>動いたのは全部が次元付き、動かなかったのは全部が無次元。</em>',
      byline_l='必要な道具：これまでの 15 回',
      byline_r='触れるのは「大きさ」だけ',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第16回（第 II 部・総括）、物理好きの高校生・大学生向け読み物です。本回は第7〜15回の結果をまとめたもので、新しい計算は含みません ── 各回の数値と出典は、それぞれの回の巻末を参照してください。ウェイトの規約は \\(\\tilde X=\\Omega^{w}X\\)（\\(\\Omega=1/a\\)）で、長さ・時間が \\(w=+1\\)、質量・エネルギー・温度が \\(-1\\)、\\(c,\\hbar,e,\\alpha\\) および無次元量が \\(0\\) です ── <strong>文献によっては符号が逆であったり \\(\\Delta=-w\\) と書いたりするので、比較の際は規約の確認が必要です</strong>。「動いた／動かなかった」の分類は、宇宙全体をまとめて書き換える場合の話であり、実験室で固定された条件には適用されません。ウェイト表は次元解析による古典近似であり、場の理論では \\(\\Delta=\\Delta_{\\text{古典}}+\\gamma\\) と異常次元が加わります（第14回。3 次元イジングで \\(\\gamma_\\sigma=0.0181489(10)\\)）── したがって正確な言い方は「無次元だから安全」ではなく「観測量だから安全」です。「役に立つ／無力」の線引きは本シリーズの評価であり、共形場理論のように無次元量が主役でありながら共形<em>不変性</em>が決定的に働く分野もあります（前シリーズ番外編⑥）── 本稿が「無力」と言っているのは Weyl 変換で書き換えるという<strong>この記法の操作</strong>についてです。<strong>第 II 部を通じて、新しい物理は一つも導いていません。</strong> 線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルで、初期宇宙まで外挿した場合は元素合成と矛盾します（Lewis, Barnes &amp; Kaushik 2016）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで時代を変え、ウェイト 0 の列だけが動かない様子が見えます。「答えを見る」で解答が開きます。')
