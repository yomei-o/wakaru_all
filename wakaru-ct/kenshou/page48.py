# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第5回の天秤は、<strong>短さ</strong>（パラメータの値段）と<strong>当てはまり</strong>（\(\Delta\chi^2\)）の二つを測りました。ところが物理学者はしばしば三つ目のことを言います ── 「<em>美しい</em>」。今回はそれを正面から扱います：<strong>美しさは三つ目の通貨なのか、それとも前の二つの言い換えなのか。</strong> そして<em>測れなかったものが何かも、正直に書きます</em>。</p>

<h2><span class="n">01</span>「美しさ」を、部品に分解する</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>部品</th><th class="mid">中身</th><th class="mid">どの通貨か</th></tr></thead>
<tbody>
<tr><th>対称性</th><td class="mid">独立なパラメータを減らす</td><td class="mid"><strong>短さ</strong>に還元できる</td></tr>
<tr><th>統一</th><td class="mid">入力の個数を減らす</td><td class="mid"><strong>短さ</strong>に還元できる</td></tr>
<tr><th>剛性（他に選びようがない）</th><td class="mid">自由な選択を減らす</td><td class="mid"><strong>短さ</strong>に還元できる</td></tr>
<tr><th>深さ（目的外まで当たる）</th><td class="mid">合わせていないデータに当たる</td><td class="mid"><strong>当てはまり</strong>に還元できる</td></tr>
<tr class="hi"><th>自然さ</th><td class="mid"><strong>事前分布についての主張</strong></td><td class="mid"><strong>還元できない</strong></td></tr>
<tr class="hi"><th>感覚的な快</th><td class="mid">式を見たときの手応え</td><td class="mid"><strong>測れない</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0">六つのうち<strong>四つは既存の二通貨に還元できます</strong>。<br>
残るのは <em>自然さ</em>（03節で測ります）と <em>感覚的な快</em>（06節で扱います）。</p>
</div>

<h2><span class="n">02</span>対称性は、いくら買うのか ── CKM 行列で数える</h2>

<div class="calc">
<span class="tag">3×3 のユニタリ行列</span>
$$\underbrace{9}_{\text{独立なパラメータ}}\;-\;\underbrace{5}_{\text{位相の付け替えで落ちる}}\;=\;\underbrace{4}_{\text{3 つの角 ＋ 1 つの位相}}$$
<p class="lbl">圧縮 2.25 倍、第5回の値段では <strong>26.8 ビットの節約</strong></p>
</div>

<p><strong>対称性は、短さで測れます。</strong> <em>ここに謎はありません。</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>核心 ── 「自然さ」は、事前分布についての主張だった</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">線形な事前なら</th><th class="mid">対数一様な事前なら</th><th class="mid">差</th></tr></thead>
<tbody>
<tr><th>\(v/M_{\rm Planck}\)（階層性問題）</th><td class="mid">\(55.5\) bit</td><td class="mid">\(6.3\) bit</td><td class="mid">\(49.1\)</td></tr>
<tr><th>\((v/M_{\rm Planck})^2\)（ヒッグスの微調整）</th><td class="mid">\(110.9\) bit</td><td class="mid">\(6.3\) bit</td><td class="mid">\(104.6\)</td></tr>
<tr class="hi"><th>\(\rho_\Lambda/\rho_{\rm Planck}\)（第32回）</th><td class="mid"><strong>\(408.4\) bit</strong></td><td class="mid"><strong>\(8.2\) bit</strong></td><td class="mid">\(400.2\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>同じ数が、55 ビット驚きにも 6 ビット驚きにもなります。</strong><br>
「不自然だ」という言明は、<em>事前分布を線形に取ると宣言している</em>のと同じです ──<br>
第19回①で「事前範囲の取り方に依存する」と書いた、<strong>その場所そのもの</strong>。<br>
── したがって：<strong>自然さは第三の通貨ではなく、事前分布の選択です。</strong></p>
</div>

<div class="fig">
<p class="cap">図：同じ小さな数を、二つの事前分布で測ったときの驚き。<strong>線形な事前では桁がそのままビットになり、対数一様な事前では桁数の対数にしかなりません</strong>。ツマミで数の小ささを動かしてください ── <em>「不自然さ」は、どちらの物差しを当てるかで決まります</em></p>
<canvas id="cv" width="720" height="360"></canvas>
<div class="controls">
  <label>量の小ささ \(\log_{10}\)<input id="sx" type="range" min="-300" max="-1" value="-17" step="1"></label>
  <span class="val" id="vx">-17</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#7a3a4a"></i>線形な事前（「不自然だ」）</span>
  <span><i class="swatch" style="background:#2a5a6a"></i>対数一様な事前（「普通だ」）</span>
</div>
</div>

<h2><span class="n">04</span>ただし、線形な事前が正当な場合もある</h2>

<div class="calc">
<span class="tag">強い CP 問題</span>
$$\theta_{\rm QCD}<10^{-10}\qquad\text{（中性子の電気双極子モーメントから）}$$
<p class="lbl">\(\theta\) は<strong>角度</strong>なので、事前分布が \([0,2\pi)\) の一様分布であることに理由がある</p>
$$-\log_2\frac{10^{-10}}{2\pi}=\mathbf{35.9\ \text{ビット}}$$
</div>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0"><strong>これは本物の微調整です</strong> ── 対数一様に逃げられません。<br>
── 「自然さ」を言うときは、<em>事前分布に理由があるかどうか</em>を見ればよい。<br>
<strong>角度には理由がある。質量の比には、いまのところ無い。</strong></p>
</div>

<h2><span class="n">05</span>有名な「美しい理論」を、分解してみる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>理論</th><th class="mid">美しさの中身</th><th class="mid">通貨</th><th class="mid">測れるか</th></tr></thead>
<tbody>
<tr class="hi"><th>一般相対論</th><td class="mid">剛性（仮定を置くとほぼ一意）</td><td class="mid">短さ</td><td class="mid"><strong>測れる</strong></td></tr>
<tr class="hi"><th>ディラック方程式</th><td class="mid">陽電子を予言した（目的外）</td><td class="mid">当てはまり</td><td class="mid"><strong>測れる</strong></td></tr>
<tr><th>標準模型</th><td class="mid">32 個のパラメータ</td><td class="mid">短くない</td><td class="mid">美しいとは呼ばれない</td></tr>
<tr><th>超対称性</th><td class="mid">階層性問題を解く（自然さ）</td><td class="mid">事前分布</td><td class="mid">事前次第</td></tr>
<tr><th>弦理論</th><td class="mid">一意性の主張 → ランドスケープ</td><td class="mid">短さの主張が崩れた</td><td class="mid">未決着</td></tr>
</tbody>
</table>
</div>

<p><strong>「美しい」と呼ばれる理由は、たいてい短さか当てはまりに分解できます。</strong> <em>分解できないときは、事前分布を疑うとよい。</em></p>

<h2><span class="n">06</span>測れなかったもの</h2>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>記述長では測れない</strong><span>短い式が美しいとは限らない</span></div></div>
<div class="row"><div class="mk">✗</div><div class="txt"><strong>当てはまりでは測れない</strong><span>当たる式が美しいとは限らない</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>事前分布でも測れない</strong><span>それは自然さの話 ── <em>感覚的な快は、本シリーズの道具の外にある</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">06節の結論</p>
<p style="margin:6px 0 0"><strong>正直に書いておきます：ここは測れません。</strong><br>
── <em>測れないことは、無いことではありません</em>。ただ、本シリーズの通貨では扱えない。<br>
そして<strong>「測れないものを判定に使わない」のが、第3回以来の作法でした。</strong></p>
</div>

<h2><span class="n">07</span>このシリーズ自身を、この物差しに当てる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">通貨</th><th>\(c\cdot t=\)一定 では</th><th class="mid">判定</th></tr></thead>
<tbody>
<tr><th class="mid">短さ</th><td>パラメータが 1 個減る（第25回）</td><td class="mid"><strong>買っている</strong></td></tr>
<tr class="hi"><th class="mid">当てはまり</th><td>\(q\)、\(w\) が桁で外れる（第46回）</td><td class="mid"><strong>大きく払っている</strong></td></tr>
<tr><th class="mid">自然さ</th><td>不自然な数を含まない</td><td class="mid">事前分布の話 ── 効かない</td></tr>
<tr class="hi"><th class="mid">感覚的な快</th><td>「一定」という形の心地よさ</td><td class="mid"><strong>測れない</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>短さで買い、当てはまりで大きく払っている</strong> ── 判定は変わりません。そして<em>「形が心地よい」ことは、判定に入れません</em> ── <strong>それが手続きでした。</strong></p>

<div class="caveat">
<span class="tag">正直な線</span>
<p style="margin:0 0 10px"><strong>① 01節の「六つの部品」は、本シリーズの分解です。</strong> 美学の議論には長い歴史があり（Dirac、Weinberg、最近では Hossenfelder の批判的な整理まで）、<em>「美しさ」の分け方に定説はありません</em> ── 本稿の六分割は<strong>この道具で扱えるかどうかを基準にした、便宜的な分け方</strong>です。</p>
<p style="margin:0 0 10px"><strong>② 03節の「対数一様なら 6.3 ビット」の 80 桁という幅は、恣意的です。</strong> どこからどこまでを事前範囲に取るかで値が動きます ── <em>要点は「線形か対数一様かで 50 ビット動く」という構造</em>であって、6.3 という数字ではありません（第19回①と同じ注意）。</p>
<p style="margin:0 0 10px"><strong>③ 04節の「角度だから線形な事前が正当」も、絶対ではありません。</strong> 高エネルギーの理論が \(\theta\) をどう生成するかによっては、<em>一様でない事前がありうる</em>という議論もあります（アクシオン模型では \(\theta\) は動的に緩和します）── <strong>「線形な事前に理由があると言いやすい」程度に読んでください</strong>。</p>
<p style="margin:0 0 10px"><strong>④ 05節の理論の評価は、要約です。</strong> 「一般相対論はほぼ一意」はロブロックの定理などの意味での言い方で、仮定の置き方に依存します。「弦理論の一意性の主張が崩れた」も<em>ランドスケープをどう評価するかで見方が分かれる</em>論点です ── 本稿はどの理論も支持・否定しません。</p>
<p style="margin:0"><strong>⑤ 06節の「測れない」は、本シリーズの道具についての言明です。</strong> <em>他の枠組みで美的判断が扱えないという主張ではありません</em> ── 認知科学や科学哲学には別の扱い方があります。ここで言えるのは<strong>「記述長・当てはまり・事前分布のどれでもない」</strong>ということだけです。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>「美しさ」の六つの部品のうち、既存の二通貨に還元できるのはいくつか。
<details><summary>答えを見る</summary><div class="ans"><strong>四つ</strong> ── 対称性・統一・剛性は<em>短さ</em>に、深さ（目的外まで当たる）は<em>当てはまり</em>に還元できます。残るのは<strong>自然さ</strong>（事前分布の話）と<strong>感覚的な快</strong>（測れない）です。</div></details></li>

<li>CKM 行列で、対称性はいくら買っているか。
<details><summary>答えを見る</summary><div class="ans">3×3 ユニタリ行列の 9 個から、位相の付け替えで 5 個が落ちて <strong>4 個</strong>（3 角 ＋ 1 位相）。第5回の値段では <strong>26.8 ビットの節約</strong>です ── <em>対称性は短さで測れ、ここに謎はありません</em>。</div></details></li>

<li>\(\rho_\Lambda/\rho_{\rm Planck}=1.13\times10^{-123}\) の驚きは何ビットか。
<details><summary>答えを見る</summary><div class="ans"><strong>事前分布によります</strong> ── 線形なら <strong>408.4 ビット</strong>（第32回の数）、対数一様（300 桁）なら <strong>8.2 ビット</strong>。差は 400 ビット。<em>「不自然だ」は、線形な事前を宣言しているのと同じ</em>です。</div></details></li>

<li>強い CP 問題が④の二つと違うのはなぜか。
<details><summary>答えを見る</summary><div class="ans">\(\theta\) が<strong>角度</strong>だからです ── 事前分布が \([0,2\pi)\) の一様分布であることに理由があり、<em>対数一様に逃げられません</em>。だから <strong>35.9 ビット</strong>は本物の微調整です。<em>「自然さ」を言うときは、事前分布に理由があるかを見ればよい。</em></div></details></li>

<li>（やや難）このシリーズの道具で測れなかったものは何か。
<details><summary>答えを見る</summary><div class="ans"><strong>感覚的な快</strong>です ── 記述長でも当てはまりでも事前分布でも測れません。<em>測れないことは無いことではありません</em>が、本シリーズの通貨では扱えません ── そして<strong>「測れないものを判定に使わない」のが第3回以来の作法</strong>でした。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　美しさは、三つ目の通貨ではなかった</h2>
<p>「美しさ」を六つの部品に分けると、<strong>四つは既存の二通貨に還元できました</strong> ── 対称性・統一・剛性は<em>短さ</em>へ、深さは<em>当てはまり</em>へ。対称性がいくら買うかは実際に数えられます：CKM 行列の 9 個は位相の付け替えで 4 個になり、<strong>26.8 ビットの節約</strong>です。</p>
<p>残るのが<strong>自然さ</strong>でした。そしてこれは第三の通貨ではなく、<em>事前分布の選択</em>だと分かりました ── \(v/M_P=2\times10^{-17}\) は線形な事前なら 55.5 ビット驚きですが、対数一様なら 6.3 ビット。\(\rho_\Lambda/\rho_{\rm Planck}\) にいたっては <strong>408.4 ビットと 8.2 ビット</strong>、差は 400 ビットです。<strong>「不自然だ」という言明は、事前分布を線形に取ると宣言しているのと同じ</strong> ── 第19回①で「事前範囲の取り方に依存する」と書いた、まさにその場所でした。</p>
<p>ただし<em>線形な事前が正当な場合もあります</em> ── 強い CP 問題の \(\theta_{\rm QCD}<10^{-10}\) は、\(\theta\) が<strong>角度</strong>なので \([0,2\pi)\) の一様分布に理由があり、対数一様に逃げられません。<strong>35.9 ビット、本物の微調整</strong>です。<em>「自然さ」を言うときは、事前分布に理由があるかどうかを見ればよい</em> ── 角度には理由があり、質量の比にはいまのところありません。</p>
<p>そして<strong>測れなかったもの</strong>があります ── <em>感覚的な快</em>。記述長でも当てはまりでも事前分布でも測れません。<strong>正直に書いておきます：ここは測れません。</strong> 測れないことは無いことではありませんが、本シリーズの通貨では扱えない ── そして<em>「測れないものを判定に使わない」のが、第3回以来の作法でした。</em></p>
<p>最後に自分に当てました。\(c\cdot t=\)一定 は<strong>短さで買い、当てはまりで大きく払っている</strong> ── 判定は変わりません。「一定」という形の心地よさは、<em>判定に入れません</em>。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第49回</span>
残り二回です。次回は<strong>開いたままの扉</strong> ── 48 回で開けて、<em>閉じなかった問い</em>を全部並べます。第 II 部で保留したもの、第 IV 部で「未解決」と書いたもの、第 V 部で「決着していない」と書いたもの、そして今回「測れない」と書いたもの。<strong>答えを出せなかったものを、答えを出せなかったものとして書きます。</strong> ── <em>それが、このシリーズが最後にできる、いちばん誠実なことだからです。</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sx=document.getElementById('sx'), vx=document.getElementById('vx'), ro=document.getElementById('ro');
  var X0=76, X1=690, Y0=34, Y1=272;
  var A0=-300, A1=0, B0=0, B1=1000;

  function px(v){ return X0+(v-A0)/(A1-A0)*(X1-X0); }
  function py(b){ return Y1-b/B1*(Y1-Y0); }
  function lin(v){ return -v*Math.LN10/Math.LN2; }
  function logu(v){ return Math.log(Math.abs(v)+20)/Math.LN2; }

  function draw(){
    var v=parseInt(sx.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var b=0;b<=B1;b+=200){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(b)); g.lineTo(X1,py(b)); g.stroke();
      g.fillText(b+' bit', X0-8, py(b)+4);
    }
    g.textAlign='center';
    for(var t=A0;t<=A1;t+=50){ g.fillStyle='#9c96a4'; g.fillText('10^'+t, px(t), Y1+20); }

    g.strokeStyle='#7a3a4a'; g.lineWidth=2.8; g.beginPath();
    for(var i=0;i<=200;i++){ var x=A0+(A1-A0)*i/200; if(i===0)g.moveTo(px(x),py(lin(x))); else g.lineTo(px(x),py(lin(x))); }
    g.stroke();
    g.strokeStyle='#2a5a6a'; g.lineWidth=2.8; g.beginPath();
    for(var j=0;j<=200;j++){ var x2=A0+(A1-A0)*j/200; if(j===0)g.moveTo(px(x2),py(logu(x2))); else g.lineTo(px(x2),py(logu(x2))); }
    g.stroke();

    g.textAlign='left';
    g.fillStyle='#7a3a4a'; g.fillText('線形な事前：桁がそのままビットになる', px(-230), py(lin(-230))-12);
    g.fillStyle='#2a5a6a'; g.fillText('対数一様な事前：桁数の対数にしかならない', px(-230), py(logu(-230))-12);

    var Xc=px(v);
    g.strokeStyle='#5a5262'; g.lineWidth=1.6; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(Xc,Y0); g.lineTo(Xc,Y1); g.stroke(); g.setLineDash([]);
    g.fillStyle='#7a3a4a'; g.beginPath(); g.arc(Xc,py(Math.min(lin(v),B1)),4.8,0,6.29); g.fill();
    g.fillStyle='#2a5a6a'; g.beginPath(); g.arc(Xc,py(logu(v)),4.8,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('量の小ささ（10 の何乗か）', (X0+X1)/2, Y1+44);

    vx.textContent=String(v);
    var tag='';
    if(v===-17) tag='　★ v/M_Planck（階層性問題）';
    if(v===-123) tag='　★ ρ_Λ/ρ_Planck（宇宙定数問題）';
    ro.textContent='10^'+v+'　→　線形な事前なら '+lin(v).toFixed(1)+' ビット　／　対数一様なら '+
      logu(v).toFixed(1)+' ビット　／　差 '+(lin(v)-logu(v)).toFixed(1)+' ビット'+tag;
  }
  sx.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-48-beauty.html', acc='#7a3a4a', ops='#2a5a6a',
      title='短さ・当てはまり・美しさ ── わかる c·t=一定 第48回（第VI部）',
      ep='第 48 回 ／ 第 VI 部・手続きを検査する',
      eyebrow='「不自然だ」は、事前分布の宣言でした',
      h1='美しさは、<br>三つ目の通貨ではなかった',
      sub='六つの部品に分けると、四つは短さと当てはまりに還元できます。<br><em>残ったのは事前分布の選択と、測れないもの。</em>',
      byline_l='必要な道具：第5回の天秤、第19回の目盛り、第32回、第47回の地図',
      byline_r='同じ数が 408 ビットにも 8 ビットにもなる',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第48回（第 VI 部の 3 回目）、物理好きの高校生・大学生向け読み物です。MDL、自然さと事前分布の関係、強い CP 問題はいずれも標準的な内容で、本稿に新しい主張はありません ── 数値は kenshou/calc52.py で計算しています。<strong>01節の「六つの部品」は本シリーズの分解</strong>で、美学の議論には長い歴史があり（Dirac、Weinberg、最近では Hossenfelder の批判的な整理まで）<em>「美しさ」の分け方に定説はありません</em> ── 本稿の六分割は<strong>この道具で扱えるかどうかを基準にした便宜的な分け方</strong>です。<strong>03節の「対数一様なら 6.3 ビット」の 80 桁という幅は恣意的で</strong>、事前範囲の取り方で値が動きます ── <em>要点は「線形か対数一様かで 50 ビット動く」という構造</em>であって数字ではありません。<strong>04節の「角度だから線形な事前が正当」も絶対ではなく</strong>、高エネルギーの理論が \\(\\theta\\) をどう生成するかによっては一様でない事前もありえます（アクシオン模型では \\(\\theta\\) は動的に緩和します）── 「線形な事前に理由があると言いやすい」程度に読んでください。<strong>05節の理論の評価は要約</strong>で、「一般相対論はほぼ一意」はロブロックの定理などの意味での言い方、「弦理論の一意性の主張が崩れた」もランドスケープの評価で見方が分かれる論点です ── 本稿はどの理論も支持・否定しません。<strong>06節の「測れない」は本シリーズの道具についての言明</strong>で、<em>他の枠組みで美的判断が扱えないという主張ではありません</em>。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで数の小ささを動かすと、二つの物差しが離れていくのが見えます。「答えを見る」で解答が開きます。')
