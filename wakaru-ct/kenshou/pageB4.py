# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">「\(1/\alpha\) がちょうど 137 だったら何がずれるのか」── そして「こっちの無次元量を変えるのは、あっちを変えるのと同じ、ということはないか」。この二つは<strong>同じ一つの問い</strong>でした ── <em>定数のあいだに、隠れた構造はあるか。</em> 掘ったら、<strong>4.1 ビットの予言が 15.7 ビットの発見に勝つ</strong>ところまで行きました。</p>

<h2><span class="n">01</span>まず 137 ── 排除は巨大、物理的な差はほぼゼロ</h2>

<div class="calc">
<span class="tag">CODATA 2022</span>
$$\frac1\alpha=137.035999177(21)\qquad\Longrightarrow\qquad
\frac{0.035999}{2.1\times10^{-8}}=\mathbf{1.7\times10^{6}\,\sigma}$$
<p class="lbl">ところが \(\alpha\) としては <strong>0.026 パーセント</strong>しか違わない</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>何が</th><th class="mid">ずれ</th><th class="mid">何 \(\sigma\)</th></tr></thead>
<tbody>
<tr><th>電子の g−2</th><td class="mid">\(3.05\times10^{-7}\)</td><td class="mid">\(2.3\times10^{6}\)</td></tr>
<tr><th>水素 1S-2S</th><td class="mid">1.3 THz</td><td class="mid">\(1.3\times10^{11}\)</td></tr>
<tr class="hi"><th>中性子寿命</th><td class="mid"><strong>\(+1.53\) s</strong></td><td class="mid"><strong>\(3.1\)</strong></td></tr>
<tr><th>元素合成の \(Y_p\)</th><td class="mid">\(7.4\times10^{-5}\)</td><td class="mid">\(0.025\)（見えない）</td></tr>
<tr><th>ホイル状態</th><td class="mid">──</td><td class="mid">破綻には 4 パーセント要る（1/152）</td></tr>
</tbody>
</table>
</div>

<p><strong>世界の側で効くのは中性子寿命だけ</strong>（陽子・中性子質量差の電磁寄与 \(-1.04\) MeV が \(0.27\) keV 動き、\(\tau\propto Q^{-5}\) で 1.5 秒）。それも 3\(\sigma\)。<em>排除が巨大なのは測定が精密だからであって、物理が微妙に釣り合っているからではありません。</em></p>

<h2><span class="n">02</span>では、なぜ 137 が気になるのか ── 整数だから</h2>

<div class="seven">
<div class="row"><div class="mk">?</div><div class="txt"><strong>整数なら \(\alpha\) は「比」ではなく「個数」かもしれない</strong><span>番外編③の四型でいえば <em>型 R ではなく型 N</em></span></div></div>
<div class="row"><div class="mk">1929</div><div class="txt"><strong>エディントンが賭けたのは、まさにそれ</strong><span>最初は 136、のち 137</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>第19回で測ると 3.8 ビット</strong><span>\([136.5,137.5]\) に一様なら整数から \(\pm0.036\) 以内に入る確率は 0.072 ── <em>偶然の帯の、下のほう</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">01–02節の結論</p>
<p style="margin:6px 0 0"><strong>エディントンの誤りは、3.8 ビットの偶然を 0 ビットの恒等式として扱ったことでした。</strong><br>
そしてもっと効く反論があります ── <em>\(\alpha\) は走る</em>（第37回、\(M_Z\) で 128）。<br>
<strong>どのスケールで整数なのかを言わないと、その主張は文になっていません。</strong><br>
── エディントンの時代には走りが知られていなかったので、<em>当時は文になっていて、いまは文になっていない。</em></p>
</div>

<h2><span class="n">03</span>もう一つの問い ── 縮退は三種類ある</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">型</th><th>中身</th><th class="mid">正体</th><th class="mid">見つけたら何が分かるか</th></tr></thead>
<tbody>
<tr><th class="mid">A</th><td>原理的に区別できない</td><td class="mid">記法の冗長性</td><td class="mid"><strong>記法についての発見</strong></td></tr>
<tr><th class="mid">B</th><td>いまの装置では分けられない</td><td class="mid">道具の限界</td><td class="mid"><strong>道具についての発見</strong></td></tr>
<tr class="hi"><th class="mid">C</th><td>独立だと思っていたら関係があった</td><td class="mid">自然の構造</td><td class="mid"><strong>物理の発見</strong></td></tr>
</tbody>
</table>
</div>

<h2><span class="n">04</span>型 A ── 質問そのものが、実在する</h2>

<div class="calc">
<span class="tag">いちばん綺麗な例</span>
$$\text{物理に効くのは}\quad \bar\theta=\theta+\arg\det M_q\quad\text{という組み合わせだけ}$$
<p class="lbl">\(\theta\) を動かして、同時にクォーク場の位相を回せば ── <strong>何も起きない</strong></p>
</div>

<p>CKM も同じです。3×3 ユニタリ行列の 9 個のうち位相の付け替えで <strong>5 方向が消える</strong> ── その 5 方向は<em>原理的に観測にかかりません</em>（\(26.8\) ビットぶんが記法でした）。</p>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0">ただし第47回の 19 個は、<strong>これらを消したあとの数</strong>です。<br>
「完全な縮退はもう残っていない」が答えで、<em>それは構成上そうしただけ</em>。<br>
── <strong>型 A を見つけることは、自然についてではなく、自分の記法について知ることでした。</strong></p>
</div>

<div class="aside">
<span class="tag">ついでに出てきた、いちばん妙なこと</span>
\(\bar\theta\) が物理的でいられるのは、<strong>クォーク質量がどれもゼロでないから</strong>。もし \(m_u=0\) なら \(\bar\theta\) はまるごと回して消せて、強い CP 問題が消滅します（実測 \(m_u=2.16\pm0.11\) MeV で \(19.6\sigma\) 除外）。<br>
── <strong>19 個は完全に独立ではありません。湯川がひとつ消えれば、\(\bar\theta\) も一緒に消える。「定数の個数」そのものが、定数の値に依存しています。</strong>
</div>

<h2><span class="n">05</span>型 B ── そして、幻だったもの</h2>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>本物：分光での \(m_q\) 方向</strong><span>番外編① ── 条件数 1196 倍、いまも残っている</span></div></div>
<div class="row hi"><div class="mk">✗</div><div class="txt"><strong>幻：原子物理での \(\alpha\) と \(m_e\)</strong><span>総体 \(\propto\alpha^2m_e\)、微細構造 \(\propto\alpha^4m_e\) で絡んで見えるが、<em>比を取れば \(m_e\) は落ちる</em></span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>そもそも \(m_e\) は無次元の観測量に現れない</strong><span>同じ原子の二つの遷移の比を取れば必ず消える ── <em>次元付きで書いたせいで生まれた幻</em>（第3回）</span></div></div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">06</span>核心 ── 型 C を「探す」ことには、値段がつく</h2>

<p>型 C（隠れた関係）が見つかれば物理の発見です。では<strong>総当たりで探してもいい</strong>のか。直感的には「それは数秘術だ」と言いたくなりますが ── <em>では、どこが違うのか。</em></p>

<div class="calc">
<span class="tag">look-elsewhere</span>
$$M\ \text{個の候補式を試したなら、意味を持つ閾値は}\ \log_2 M\ \text{ビット}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>読み方</th><th class="mid">探索空間 \(M\)</th><th class="mid">閾値</th><th class="mid">小出（15.7 ビット）は</th></tr></thead>
<tbody>
<tr><th>狭い（小出の形だけ）</th><td class="mid">\(126\)</td><td class="mid">\(7.0\) bit</td><td class="mid">通る</td></tr>
<tr class="hi"><th>広い（12 質量の部分集合など）</th><td class="mid">\(1.4\times10^{8}\)</td><td class="mid">\(27.1\) bit</td><td class="mid"><strong>11.4 ビット足りない</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>b–τ 統一は SU(5) が先に予言したので、候補は 1 個 ── 閾値はゼロビット。</strong><br>
素の驚きでは小出（15.7）が b–τ（4.1）より 11.6 ビット上なのに、<br>
<strong>探索の値段を引くと逆転します。</strong><br>
── <em>「理論が先か、数字が先か」の差が、ちょうど \(\log_2M\) ビットとして出る。</em><br>
これは社会的な慣習ではなく、<strong>引き算の結果</strong>でした。</p>
</div>

<div class="fig">
<p class="cap">図：素の驚きから探索の値段を引くと、順位が入れ替わります。<strong>ツマミで「どれだけ広く探したか」を動かしてください</strong> ── \(M\) を上げると小出だけが沈み、<em>先に予言された b–τ は動きません</em></p>
<canvas id="cv" width="720" height="360"></canvas>
<div class="controls">
  <label>探した空間の広さ \(\log_2 M\)<input id="sm" type="range" min="0" max="40" value="7" step="1"></label>
  <span class="val" id="vm">7</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6a3a5a"></i>小出の関係式（探して見つけた）</span>
  <span><i class="swatch" style="background:#2a5a4a"></i>b–τ 統一（先に予言された）</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>意味を持つ線（0 ビット）</span>
</div>
</div>

<h2><span class="n">07</span>そして、これは自然さと同じ病気だった</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>場面</th><th class="mid">必要な「空間」</th><th class="mid">その後</th></tr></thead>
<tbody>
<tr><th>第19回：驚き</th><td class="mid">量の<strong>事前範囲</strong></td><td class="mid">第19回①で依存性を明記</td></tr>
<tr><th>第48回：自然さ</th><td class="mid">パラメータの<strong>事前分布</strong></td><td class="mid">番外編③で定理になった</td></tr>
<tr class="hi"><th>今回：数値の一致</th><td class="mid"><strong>探索空間</strong></td><td class="mid">申告しだいで判定が反転</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">07節の結論 ── 六度目の圧縮</p>
<p style="margin:6px 0 0"><strong>三つとも同じ問いでした：「正準な測度はあるか」。</strong><br>
確率を計算するには測度が要り、測度が無ければ確率は決まりません。<br>
── 探索空間は<em>上限を宣言すれば有限</em>。<strong>先に宣言することが、well-posed にする唯一の方法。</strong><br>
<em>「理論が先」とは、社会的な作法ではなく、測度を先に固定することでした。</em></p>
</div>

<h2><span class="n">08</span>おまけ ── 第36回の「偶然の帯」に、閾値がついた</h2>

<p>第36回は「帯（4〜7.5 ビット）は選択効果」と<strong>観察</strong>しました。いま<strong>閾値が計算できます</strong>（7〜27 ビット）── <em>帯は閾値のはるか下、だから一つも意味を持たない</em>。小出だけが帯を抜けましたが、広い読みには 11.4 ビット足りません。</p>

<div class="keybox">
<p class="lbl">08節の結論</p>
<p style="margin:6px 0 0"><strong>観察が、引き算になりました。</strong></p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p style="margin:0 0 10px"><strong>① いちばん弱いのは 06節の探索空間の見積もりです。</strong> 狭い読みと広い読みで <em>20 ビット違い</em>、どちらが正しいかを決める方法はありません ── <strong>それ自体が 07節の主張そのもの</strong>です。</p>
<p style="margin:0 0 10px"><strong>② 小出の 15.7 ビットは第19回・第36回から引き継いだ値</strong>で、事前範囲の取り方に依存します。b–τ の 4.1 ビットも同じです。</p>
<p style="margin:0 0 10px"><strong>③ b–τ の「探索空間ゼロ」は理想化です。</strong> SU(5) 以外にも大統一の候補はあり、<em>どの模型を試したかを数えれば、こちらにも数ビットは付きます</em> ── ゼロではなく「小さい」が正しい。</p>
<p style="margin:0 0 10px"><strong>④ 01節の中性子寿命の見積もりは粗いものです。</strong> \(n\)–\(p\) 質量差への電磁的寄与（\(\approx-1.04\) MeV）は格子計算で幅があり、\(\tau\propto Q^{-5}\) も位相空間の近似です ── <em>「3\(\sigma\) 級」以上の精度で読まないでください</em>。</p>
<p style="margin:0"><strong>⑤ 07節の統一は本シリーズの読み方</strong>であって、統計学の標準的な定式化ではありません ── 多重比較補正、ベイズ因子など、既存のより精緻な枠組みがあります。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>\(1/\alpha=137\) ちょうどなら、世界で何がずれるか。
<details><summary>答えを見る</summary><div class="ans"><strong>中性子寿命だけ</strong>（\(+1.53\) s、3.1\(\sigma\)）。実験室では g−2 が \(2.3\times10^6\sigma\)、1S-2S が \(1.3\times10^{11}\sigma\) で見えますが、<em>元素合成は 0.025\(\sigma\) で見えず、ホイル状態には 1/152 で届きません</em>。<strong>排除が巨大なのは測定が精密だから</strong>です。</div></details></li>

<li>エディントンの誤りは何だったか。
<details><summary>答えを見る</summary><div class="ans"><strong>3.8 ビットの偶然を、0 ビットの恒等式として扱ったこと</strong>です。さらにいまは <em>\(\alpha\) が走る</em>ので（\(M_Z\) で 128）、<strong>どのスケールで整数かを言わないと文になっていません</strong> ── 当時は文になっていて、いまはなっていない。</div></details></li>

<li>縮退の三つの型と、それぞれ何が分かるか。
<details><summary>答えを見る</summary><div class="ans"><strong>A</strong>（完全）＝記法についての発見、<strong>B</strong>（観測上）＝道具についての発見、<strong>C</strong>（隠れた関係）＝<em>物理の発見</em>。見分け方は<strong>「観測で破れうるか」</strong> ── A は破れず、C は破れます（b–τ が外れれば SU(5) が死ぬ）。</div></details></li>

<li>なぜ 4.1 ビットの予言が 15.7 ビットの発見に勝つのか。
<details><summary>答えを見る</summary><div class="ans"><strong>探索の値段 \(\log_2M\) を引くから</strong>です。b–τ は先に予言されたので候補 1 個＝閾値ゼロ。小出は探して見つけたので閾値 7〜27 ビット ── <em>広い読みでは 11.4 ビット足りません</em>。<strong>「理論が先」の差が、ちょうど \(\log_2M\) ビットとして出ます。</strong></div></details></li>

<li>（やや難）驚き・自然さ・数値の一致に共通するものは。
<details><summary>答えを見る</summary><div class="ans"><strong>どれも「空間」を必要とすること</strong> ── 事前範囲／事前分布／探索空間。<em>三つとも「正準な測度はあるか」という一つの問い</em>でした（六度目の圧縮）。そして<strong>「理論が先」とは、測度を先に固定すること</strong>です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　理論が先とは、測度を先に固定することだった</h2>
<p>\(1/\alpha=137\) ちょうどは <strong>\(1.7\times10^6\sigma\)</strong> で排除されますが、物理的な差は <strong>0.026 パーセント</strong>しかありません ── 世界の側で効くのは<em>中性子寿命の 3\(\sigma\) だけ</em>。気になる理由は整数だからで、その「近さ」の驚きは <strong>3.8 ビット</strong>、偶然の帯の下端でした。<em>エディントンの誤りは、3.8 ビットの偶然を 0 ビットの恒等式として扱ったこと</em>。しかも \(\alpha\) は走るので、いまではその主張は<strong>文にすらなっていません</strong>。</p>
<p>「こっちを変えるのはあっちを変えるのと同じ」は<strong>三種類</strong>ありました。<strong>型 A</strong>（完全な縮退）は実在します ── \(\bar\theta=\theta+\arg\det M_q\)、CKM の 5 方向。ただし 19 個はそれらを消したあとの数なので、<em>型 A を見つけることは自分の記法について知ること</em>でした。<strong>型 B</strong>（観測上）は番外編①の \(m_q\) 方向として残っていますが、原子物理の \(\alpha\)–\(m_e\) は<em>次元付きで書いたせいの幻</em>でした。</p>
<p>そして<strong>型 C を探すことには値段がつきます</strong>。\(M\) 個の候補を試せば閾値は \(\log_2M\) ── 小出の 15.7 ビットは狭い読み（7.0）なら通り、広い読み（27.1）なら 11.4 ビット足りない。一方 b–τ 統一は<em>先に予言された</em>ので候補 1 個、閾値ゼロ。<strong>4.1 ビットの予言が、15.7 ビットの発見に勝ちます。</strong></p>
<p>最後に ── 驚き（事前範囲）、自然さ（事前分布）、数値の一致（探索空間）は、<strong>三つとも「正準な測度はあるか」という一つの問い</strong>でした（六度目の圧縮）。<em>「理論が先」とは、社会的な作法ではなく、測度を先に固定することだった</em>のです。そして第36回の「偶然の帯」にも閾値がつきました ── <strong>観察が、引き算になりました。</strong></p>
</div>

<div class="next">
<span class="lbl">番外編⑤へ</span>
07節で「正準な測度はあるか」に全部が潰れました。<strong>では、あるのか。</strong> 番外編③は「コンパクトなら Haar、非コンパクトなら無い」と答えましたが ── <em>それは粗すぎました</em>。次回は<strong>くりこみ群が測度を配る</strong>という筋を辿ります。そして<strong>標準模型の全 20 パラメータをベータ関数の形だけで採点して、三大微調整問題を偽陽性ゼロで当てます。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sm=document.getElementById('sm'), vm=document.getElementById('vm'), ro=document.getElementById('ro');
  var X0=90, X1=690, Y0=40, Y1=280;
  var KO=15.7, BT=4.1;

  function py(v){ return Y1-(v+20)/40*(Y1-Y0); }   // -20 .. +20 bit

  function draw(){
    var M=parseInt(sm.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var v=-20;v<=20;v+=10){
      g.strokeStyle=(v===0?'#cdc8d2':'#f2f0f4'); g.lineWidth=(v===0?1.8:1);
      g.beginPath(); g.moveTo(X0,py(v)); g.lineTo(X1,py(v)); g.stroke();
      g.fillText((v>0?'+':'')+v+' bit', X0-8, py(v)+4);
    }
    g.fillStyle='#a89fae'; g.textAlign='left';
    g.fillText('この線より上でないと、意味を持たない', X0+10, py(0)-8);

    var bw=(X1-X0)/2;
    var items=[['小出（探して見つけた）', KO-M, '#6a3a5a'],
               ['b–τ（先に予言された）', BT, '#2a5a4a']];
    for(var i=0;i<2;i++){
      var x=X0+i*bw+50, val=items[i][1];
      g.fillStyle=items[i][2]; g.globalAlpha=0.9;
      var y0=py(0), y1=py(val);
      g.fillRect(x, Math.min(y0,y1), bw-100, Math.abs(y1-y0));
      g.globalAlpha=1;
      g.fillStyle='#3a3640'; g.textAlign='center';
      g.fillText(items[i][0], x+(bw-100)/2, Y1+20);
      g.fillStyle=items[i][2];
      g.font='13px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
      g.fillText((val>0?'+':'')+val.toFixed(1), x+(bw-100)/2, y1+(val>0?-8:16));
      g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    }

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('素の驚き − 探索の値段（log₂M）', (X0+X1)/2, Y1+46);

    vm.textContent=String(M);
    var ko=KO-M;
    var msg;
    if(ko>BT) msg='　小出がまだ上 ── 狭く探したという申告が要る';
    else if(ko>0) msg='　★ 逆転した ── 予言が発見に勝っている';
    else msg='　★ 小出は線の下 ── 意味を失った';
    ro.textContent='log₂M = '+M+'（探した候補 '+Math.round(Math.pow(2,M)).toLocaleString('en-US')+' 通り）'+
      '　→　小出 '+ko.toFixed(1)+' bit ／ b–τ '+BT.toFixed(1)+' bit'+msg;
  }
  sm.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-b4-relations.html', acc='#6a3a5a', ops='#2a5a4a',
      title='番外編④：定数のあいだに、隠れた関係はあるか ── わかる c·t=一定',
      ep='番外編 ④ ／ 本編完結後の深掘り',
      eyebrow='4.1 ビットの予言が、15.7 ビットの発見に勝つ',
      h1='理論が先とは、<br>測度を先に固定すること',
      sub='137 に近いこと、定数どうしの縮退、そして「関係を探す」ことの値段。<br><em>三つとも、同じ一つの問いに潰れました。</em>',
      byline_l='必要な道具：第19回の目盛り、第36回の帯、第37回の走り、第47回の地図、番外編③の型',
      byline_r='六度目の圧縮 ── 三つの問い → 一つ',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズの番外編④（本編全50話の完結後に書いた深掘り）、物理好きの高校生・大学生向け読み物です。数値は kenshou/calc60.py、calc61.py、calc62.py で計算しています。エディントンの数秘術、CKM の位相の付け替え、\\(\\bar\\theta\\) の組み合わせ、b–τ 統一、look-elsewhere 効果はいずれも標準的な内容です。<strong>いちばん弱いのは 06節の探索空間の見積もり</strong> ── 狭い読みと広い読みで 20 ビット違い、どちらが正しいかを決める方法はありません（<em>それ自体が 07節の主張そのもの</em>）。<strong>小出の 15.7 ビットと b–τ の 4.1 ビットは事前範囲の取り方に依存し</strong>、b–τ の「探索空間ゼロ」も理想化です（SU(5) 以外の大統一候補を数えれば数ビット付きます）。<strong>01節の中性子寿命の見積もりは粗く</strong>、\\(n\\)–\\(p\\) 質量差への電磁的寄与は格子計算で幅があり \\(\\tau\\propto Q^{-5}\\) も位相空間の近似です ── 「3\\(\\sigma\\) 級」以上の精度で読まないでください。<strong>07節の統一は本シリーズの読み方</strong>であって統計学の標準的な定式化ではなく、多重比較補正やベイズ因子など既存のより精緻な枠組みがあります。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで探索空間を広げると、順位が入れ替わります。「答えを見る」で解答が開きます。')
