# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第1回で宇宙のスペックを取ったとき、演算数だけは中身が空欄のままでした ── マルゴラス＝レヴィティン限界が数えているのは<em>直交状態への遷移</em>だけで、何をしているかは問わないからです。今回その空欄を埋めます。<strong>ML のレートはエネルギーに比例するので、演算はそのままエネルギーの割り当てで決まります。</strong> 数えてみると、かなり呆れた結果が出ます ── <em>演算資源の 95% が、何も起きない成分に割り当てられている。</em></p>

<h2><span class="n">01</span>演算は、エネルギーの割り当てで決まる</h2>

<div class="calc">
<span class="tag">レートの分配</span>
$$\frac{d\Omega}{dt}=\frac{2E}{\pi\hbar}\qquad\Longrightarrow\qquad \frac{d\Omega_i}{dt}=\frac{2E_i}{\pi\hbar}=\Omega_i\text{（エネルギー割合）}\times\frac{2E}{\pi\hbar}$$
</div>

<p>レートが \(E\) に比例するので、<strong>演算資源の配分は、そのまま宇宙のエネルギー収支表</strong>になります。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>成分</th><th class="mid">エネルギー割合</th><th class="mid">今日の演算レート</th></tr></thead>
<tbody>
<tr class="hi"><th>暗黒エネルギー</th><td class="mid"><strong>68.5%</strong></td><td class="mid">\(3.27\times10^{103}\) /s</td></tr>
<tr><th>暗黒物質</th><td class="mid">26.5%</td><td class="mid">\(1.26\times10^{103}\) /s</td></tr>
<tr><th>バリオン</th><td class="mid">4.9%</td><td class="mid">\(2.34\times10^{102}\) /s</td></tr>
<tr><th>光子</th><td class="mid">0.0054%</td><td class="mid">\(2.58\times10^{99}\) /s</td></tr>
<tr><th>ニュートリノ</th><td class="mid">0.0038%</td><td class="mid">\(1.81\times10^{99}\) /s</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">02</span>真空は、遷移する先を持たない</h2>

<p>ここで一言が効きます。マルゴラス＝レヴィティン限界の \(E\) は、<strong>基底状態から測ったエネルギー</strong>です。ところが真空エネルギーは、その基底そのもの。</p>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0"><strong>真空は、遷移する先を持ちません。</strong><br>
だから演算に数えるべきではない ── <em>この一言で、演算資源の 68.5% が最初から消えます。</em></p>
</div>

<p>残るのは 31.5%。そしてそのうち <strong>84.1% が暗黒物質</strong>です。暗黒物質は、私たちが知る限り<em>重力以外に相互作用しません</em> ── つまり、状態を変える相手がいない。</p>

<div class="calc">
<span class="tag">何かしているのは、どれだけか</span>
$$\text{バリオン}+\text{放射}=4.909\%\qquad(\text{真空を除いた中でも }15.6\%)$$
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>宇宙は、演算資源の 95.0% を「何も起きない」成分に割り当てています。</strong><br>
真空（68.5%）＋暗黒物質（26.5%）── <em>どちらも状態が変わらない。</em></p>
</div>

<div class="fig">
<p class="cap">図：宇宙のエネルギー＝演算資源の割り当て。ツマミで<strong>「何を演算と数えるか」の厳しさ</strong>を上げていくと、残る資源が段階的に崩れていきます ── 全部数える \(10^{121}\) 回から、星の光だけを数える \(10^{115}\) 回まで</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>何を「演算」と数えるか（右へ行くほど厳しい）<input id="ss" type="range" min="0" max="3" value="1" step="1"></label>
  <span class="val" id="vs">真空を除く</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#0f4a5a"></i>数える成分</span>
  <span><i class="swatch" style="background:#c3cfd4"></i>数えない成分</span>
  <span><i class="swatch" style="background:#a8622a"></i>残った演算数</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>では、バリオンは何をしているのか</h2>

<p>残った 4.9% の中身を見ます。バリオンがやっていることのうち、いちばん派手なのは<strong>恒星の核融合</strong>です。宇宙が誕生以来、星として輝いたエネルギーの総量を見積もります。</p>

<div class="calc">
<span class="tag">計算 ── 光度密度から</span>
<p class="lbl">ハッブル体積 × 宇宙の光度密度</p>
$$3.17\times10^{11}\ \mathrm{Mpc^3}\times2\times10^{8}\ L_\odot/\mathrm{Mpc^3}=2.43\times10^{46}\ \mathrm{W}$$
<p class="lbl">宇宙年齢ぶん積算して、全エネルギーと比べる</p>
$$\frac{1.06\times10^{64}\ \mathrm{J}}{7.90\times10^{69}\ \mathrm{J}}=1.3\times10^{-6}$$
</div>

<p><strong>宇宙が誕生以来「星として輝いた」エネルギーは、全体の 100 万分の 1</strong>です。核融合という、宇宙でいちばん目立つ活動が、この規模。</p>

<h2><span class="n">04</span>命令セットの一覧</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>成分</th><th class="mid">割合</th><th>実際にやっていること</th><th class="mid">演算か</th></tr></thead>
<tbody>
<tr><th>真空</th><td class="mid">68.5%</td><td>基底状態にいる。遷移先がない</td><td class="mid"><strong>×</strong></td></tr>
<tr><th>暗黒物質</th><td class="mid">26.5%</td><td>重力で集まるだけ。相互作用しない</td><td class="mid"><strong>×</strong></td></tr>
<tr class="hi"><th>バリオン</th><td class="mid">4.9%</td><td>化学結合・核融合・生命</td><td class="mid"><strong>○</strong></td></tr>
<tr><th>放射</th><td class="mid">0.009%</td><td>自由伝播（第11回：完全に静止）</td><td class="mid">△</td></tr>
</tbody>
</table>
</div>

<p>第11回で「この絵では光子ガスは完全に静止している」と数えました。今回の四行目が、その言い換えです ── <em>放射は伝播するだけで、状態を変えない</em>。だから ML の意味で「演算」と呼ぶには微妙です。</p>

<div class="aside">
<span class="tag">第1回の 0.035 とつながる</span>
第1回で「宇宙は 1 ビットあたり 0.035 回しか演算していない」と数えました。今回わかったのは、<strong>その 0.035 回のうち 95% が、何も起きない成分の取り分だ</strong>ということです。<em>実質は 1 ビットあたり \(0.035\times0.049=1.7\times10^{-3}\) 回</em> ── <strong>580 ビットに 1 回</strong>。宇宙という計算機は、思っていたよりさらに働いていませんでした。
</div>

<h2><span class="n">05</span>種明かし ── ML 限界は「上限」しか数えない</h2>

<p>今回の結果は、じつは<strong>マルゴラス＝レヴィティン限界の性質</strong>そのものです。</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>ML はエネルギーしか見ない</strong><span>「そのエネルギーで、原理的に何回まで状態を変えられるか」の上限。<em>実際に変えたかどうかは問わない</em></span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>だから真空も暗黒物質も、上限には寄与する</strong><span>エネルギーを持っているから。でも実際には遷移していない</span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>上限と実績のあいだに、95% の隙間がある</strong><span>第1回の \(10^{121}\) は<em>スペック表であってベンチマークではない</em>と書いた、その隙間の中身</span></div></div>
</div>

<p>第1回の「正直な線」で <em>「これはスペック表であって、ベンチマークではない」</em> と書きました。今回はその隙間を、実際に測ったことになります ── <strong>スペックの 95% は、使われる見込みのない成分に割り当てられている。</strong></p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① 「真空は遷移先を持たないので演算に数えない」は、本稿の判断です。</strong> マルゴラス＝レヴィティン限界の \(E\) を「基底状態からのエネルギー」と読む標準的な解釈に従っていますが、宇宙論的な真空エネルギーをその意味の基底状態とみなしてよいかは自明ではありません ── ド・ジッター空間には地平面温度があり、揺らぎもあります。<em>02節は「素朴に全エネルギーを入れるのはおかしい」という指摘までが確かな部分</em>です。</p>
<p style="margin:0 0 10px"><strong>② 「暗黒物質は何もしていない」は、現在の知識に基づく言い方です。</strong> 重力以外の相互作用が見つかれば変わります。また重力による構造形成は立派な「状態の変化」なので、<em>「何もしていない」は ML の意味に限った話</em>です。</p>
<p style="margin:0 0 10px"><strong>③ 光度密度 \(2\times10^8\,L_\odot/\mathrm{Mpc^3}\) は目安です。</strong> 波長域と赤方偏移依存性で数倍動きます。また過去の星形成率は今より高かったので、単純に \(t_0\) を掛けるのは粗い ── <em>\(10^{-6}\) という桁の主張</em>として読んでください。</p>
<p style="margin:0 0 10px"><strong>④ エネルギー割合は今日の値です。</strong> 演算数 \(\Omega=\int(2E/\pi\hbar)dt\) は過去も積むので、正確な内訳は各成分の \(\int\rho_i V\,dt\) を要します（放射優勢期には放射の取り分がずっと大きい）。04節の表は<em>今日のスナップショット</em>です。</p>
<p style="margin:0"><strong>⑤ 「演算」は依然としてエネルギーが許す遷移回数の上限で、意味のある計算ではありません</strong>（第1回①と同じ注意）。本稿がやったのは、その上限を成分ごとに分解しただけです。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>演算資源が「エネルギー収支表そのもの」になるのはなぜか。
<details><summary>答えを見る</summary><div class="ans">マルゴラス＝レヴィティン限界のレートが \(2E/\pi\hbar\) で <strong>\(E\) に比例する</strong>から。だから成分ごとの演算レートは、そのままエネルギー割合になります。</div></details></li>

<li>真空を演算に数えるべきでないのはなぜか。それで何%が消えるか。
<details><summary>答えを見る</summary><div class="ans">ML の \(E\) は<strong>基底状態から測ったエネルギー</strong>で、真空エネルギーはその基底そのものだから ── 遷移する先がありません。これで <strong>68.5%</strong> が消え、残りは 31.5%。</div></details></li>

<li>「何かしている」成分は全体の何%か。
<details><summary>答えを見る</summary><div class="ans">バリオン 4.9% ＋ 放射 0.009% ＝ <strong>4.91%</strong>（真空を除いた中でも 15.6%）。つまり<em>演算資源の 95.0% が、何も起きない成分（真空＋暗黒物質）に割り当てられている</em>。</div></details></li>

<li>星として輝いたエネルギーは、全体のどれだけか。
<details><summary>答えを見る</summary><div class="ans">ハッブル体積 \(3.17\times10^{11}\) Mpc³ × 光度密度 \(2\times10^8L_\odot/\mathrm{Mpc^3}\) ＝ \(2.4\times10^{46}\) W。宇宙年齢ぶんで \(1.1\times10^{64}\) J、全体の <strong>\(1.3\times10^{-6}\)</strong>。<em>核融合という宇宙でいちばん目立つ活動が、100 万分の 1。</em></div></details></li>

<li>（やや難）第1回の「1 ビットあたり 0.035 回」は、今回どう修正されるか。
<details><summary>答えを見る</summary><div class="ans">その 0.035 回のうち 95% が「何も起きない」成分の取り分なので、実質は \(0.035\times0.049=1.7\times10^{-3}\) 回 ── <strong>580 ビットに 1 回</strong>。第1回で「スペック表であってベンチマークではない」と書いた、その隙間の中身が今回わかったことになります。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　95% は、何も起きない成分の取り分だった</h2>
<p>第1回で空欄のままだった「演算の中身」を埋めました。マルゴラス＝レヴィティン限界のレートは \(2E/\pi\hbar\) で <strong>エネルギーに比例する</strong>ので、演算資源の配分はそのまま宇宙のエネルギー収支表になります ── 暗黒エネルギー 68.5%、暗黒物質 26.5%、バリオン 4.9%、放射 0.009%。</p>
<p>ここで一言が効きました。<strong>ML の \(E\) は基底状態から測ったエネルギーで、真空エネルギーはその基底そのもの</strong> ── 遷移する先がありません。これで 68.5% が消え、残る 31.5% のうち 84.1% は暗黒物質（重力以外に相互作用しない）。<em>「何かしている」と言えるのは 4.91% だけ</em>です。</p>
<div class="keybox" style="margin:18px 0 0">
<p style="margin:0;text-align:center;font-size:19px">宇宙は、演算資源の <strong>95.0%</strong> を<br>「何も起きない」成分に割り当てている</p>
</div>
<p style="margin-top:22px">残る 4.9% の中身も見ました ── 宇宙が誕生以来「星として輝いた」エネルギーは、全体の <strong>\(1.3\times10^{-6}\)</strong>。核融合という宇宙でいちばん目立つ活動が、100 万分の 1 です。そして第1回の「1 ビットあたり 0.035 回」は、実質 <strong>580 ビットに 1 回</strong>まで下がります。</p>
<p>種明かしは ML 限界の性質そのものでした ── <em>ML はエネルギーしか見ず、実際に遷移したかは問わない</em>。だから真空も暗黒物質も上限には寄与する。第1回で「これはスペック表であってベンチマークではない」と書いた、その隙間を今回測ったことになります。<strong>スペックの 95% は、使われる見込みのない成分に割り当てられていました。</strong></p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第23回</span>
次は<strong>誤り訂正</strong>です。第18回で「体積セルには、はじめから番地が振られていない」と数えました。では地平面に書かれた \(10^{122}\) ビットは、<em>どうやって守られているのか</em>。ホログラフィック符号（AdS/CFT の量子誤り訂正としての読み方）は、境界の情報からバルクを再構成する仕組みを、<strong>誤り訂正符号そのもの</strong>として定式化します。この絵に持ち込むと ── <em>「バルクの一点が壊れても、境界の情報からは復元できる」</em>。第6回の「使われているメモリに道具は届かない」と、正面からぶつかります。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=60, X1=690;
  var COMP=[['真空',0.685,'#0f4a5a'],['暗黒物質',0.265,'#1f6a7a'],
            ['バリオン',0.049,'#3f8a9a'],['放射',0.000092,'#7fb4be']];
  var STAGE=['全部数える','真空を除く','暗黒物質も除く','星の光だけ'];
  var KEEP=[4,3,2,1];   // 何成分まで数えるか（放射側から）
  var TOT=1.04e121;

  function draw(){
    var s=parseInt(ss.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);

    // 帯グラフ
    var Y=90, H=64, x=X0;
    var frac=0;
    for(var i=0;i<COMP.length;i++){
      var w=(X1-X0)*COMP[i][1];
      var counted = (i>= (4-KEEP[s]));
      if(s===3) counted=false;                    // 星の光だけ：帯では別扱い
      g.fillStyle = counted ? COMP[i][2] : '#c3cfd4';
      g.fillRect(x, Y, Math.max(w,2), H);
      if(counted) frac+=COMP[i][1];
      if(COMP[i][1]>0.03){
        g.fillStyle='#fff'; g.textAlign='center';
        g.font='bold 13px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
        g.fillText(COMP[i][0], x+w/2, Y+H/2+5);
        g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
        g.fillText((COMP[i][1]*100).toFixed(1)+'%', x+w/2, Y+H/2+22);
      }
      x+=w;
    }
    if(s===3) frac=1.338e-6;
    g.strokeStyle='#93a8ae'; g.lineWidth=1.2;
    g.strokeRect(X0,Y,X1-X0,H);

    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillStyle='#5a7a84'; g.textAlign='left';
    g.fillText('宇宙のエネルギー ＝ 演算資源の割り当て', X0, Y-16);

    // 残った演算数（対数の棒）
    var Y2=210, H2=40;
    var lg=Math.log10(TOT*frac), lg0=Math.log10(TOT);
    var w2=(X1-X0)*(lg/lg0);
    g.fillStyle='#e6dcd0';
    g.fillRect(X0,Y2,X1-X0,H2);
    g.fillStyle='#a8622a';
    g.fillRect(X0,Y2,Math.max(w2,2),H2);
    g.strokeStyle='#c9b6a2'; g.lineWidth=1.2;
    g.strokeRect(X0,Y2,X1-X0,H2);
    g.fillStyle='#7a4418'; g.textAlign='left';
    g.fillText('残った演算数', X0, Y2-12);
    g.fillStyle='#fff'; g.textAlign='right';
    g.font='bold 14px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText((TOT*frac).toExponential(2)+' 回', X0+Math.max(w2,120)-12, Y2+26);
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillStyle='#9a8674'; g.textAlign='right';
    g.fillText('全部数えると 1.04×10¹²¹ 回', X1, Y2+H2+20);

    // 段階の表示
    g.textAlign='center'; g.fillStyle='#5a7a84';
    for(var i=0;i<4;i++){
      var xx=X0+(X1-X0)*(i+0.5)/4;
      g.fillStyle = (i===s)?'#0f4a5a':'#a8bcc2';
      g.font=(i===s?'bold ':'')+'12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillText(STAGE[i], xx, 320);
    }

    vs.textContent=STAGE[s];
    var pct=frac*100;
    ro.textContent=STAGE[s]+'　→　残る割合 '+(pct<0.01?pct.toExponential(2):pct.toFixed(3))+'%'+
      '　演算数 '+(TOT*frac).toExponential(2)+' 回'+
      '　／　1ビットあたり '+(0.0351*frac).toExponential(2)+' 回'+
      (s===1?'　★ 真空は基底状態なので遷移先がない':'')+
      (s===2?'　★ 暗黒物質は重力以外に相互作用しない':'')+
      (s===3?'　★ 星として輝いたのは全体の 100万分の1':'');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-22-instruction.html', acc='#0f4a5a', ops='#a8622a',
      title='宇宙という計算機の、命令セット ── わかる c·t=一定 第22回',
      ep='第 22 回 ／ 第1回で空欄だった「演算の中身」を埋める',
      eyebrow='演算資源の95%は、何も起きない成分の取り分でした',
      h1='宇宙という計算機の、<br>命令セット',
      sub='ML 限界のレートはエネルギーに比例する ── だから演算の配分は、<br>そのまま宇宙のエネルギー収支表になります。<em>数えると、呆れた結果が出ます。</em>',
      byline_l='必要な道具：割合の掛け算',
      byline_r='真空 68.5% ＋ 暗黒物質 26.5% ＝ 95.0%',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第22回、物理好きの高校生・大学生向け読み物です。マルゴラス＝レヴィティン限界（レート \\(2E/\\pi\\hbar\\)）とそれが基底状態からのエネルギーで測られることは標準的です。エネルギー割合 \\(\\Omega_\\Lambda=0.685\\)、\\(\\Omega_c=0.265\\)、\\(\\Omega_b=0.049\\)、\\(\\Omega_\\gamma=5.4\\times10^{-5}\\)、\\(\\Omega_\\nu=3.8\\times10^{-5}\\) は Planck 系の標準値です。本稿の成分別演算レート、「真空を除くと 31.5%、そのうち暗黒物質が 84.1%」「何かしているのは 4.91%」「演算資源の 95.0% が何も起きない成分」、および星として輝いたエネルギーが全体の \\(1.3\\times10^{-6}\\) であることは本稿での計算です（kenshou/calc26.py）。<strong>「真空は遷移先を持たないので演算に数えない」は本稿の判断です</strong> ── ML の \\(E\\) を基底状態からのエネルギーと読む標準的な解釈に従っていますが、宇宙論的な真空エネルギーをその意味の基底とみなしてよいかは自明ではありません（ド・ジッター空間には地平面温度と揺らぎがあります）。02節で確かなのは「素朴に全エネルギーを入れるのはおかしい」という指摘までです。<strong>「暗黒物質は何もしていない」は現在の知識に基づく言い方で、ML の意味に限った話です</strong> ── 重力による構造形成は立派な状態変化です。光度密度 \\(2\\times10^8\\,L_\\odot/\\mathrm{Mpc^3}\\) は目安で、波長域・赤方偏移依存性で数倍動き、過去の星形成率が高かったことも考慮していません（\\(10^{-6}\\) という桁の主張です）。エネルギー割合は今日の値であり、\\(\\Omega=\\int(2E/\\pi\\hbar)dt\\) の正確な内訳には各成分の \\(\\int\\rho_iV\\,dt\\) が必要です（放射優勢期には放射の取り分がずっと大きくなります）。「演算」は依然としてエネルギーが許す遷移回数の上限であり、意味のある計算ではありません。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルです。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで「何を演算と数えるか」を変え、残る資源が崩れていく様子が見えます。「答えを見る」で解答が開きます。')
