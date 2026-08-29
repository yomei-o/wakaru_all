# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">残り二回です。今回は<strong>開いたままの扉</strong> ── 48 回で開けて、<em>閉じなかった問い</em>を全部並べます。そして並べると分かるのは ── <strong>扉には四種類しかなく、そのうち 4 割近くはデータでは閉じない</strong>ということです。<em>どの種類の扉かを見分けること</em>が、このシリーズがやってきたことでした。</p>

<h2><span class="n">01</span>開けて、閉じなかった扉</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">回</th><th>問い</th><th class="mid">何が閉じるか</th><th class="mid">種類</th></tr></thead>
<tbody>
<tr><th class="mid">18</th><td>1 ビット \(\leftrightarrow\) 1.96 fm は意味があるのか</td><td class="mid">──</td><td class="mid">偶然</td></tr>
<tr><th class="mid">29</th><td>MOND は他のデータセットでも生き残るか</td><td class="mid">銀河団・CMB の解析</td><td class="mid">観測</td></tr>
<tr><th class="mid">34</th><td>共形重力の CMB 予言は立つのか</td><td class="mid">計算が未確立</td><td class="mid">計算</td></tr>
<tr><th class="mid">36</th><td>「偶然の帯」は本物か</td><td class="mid">標本を増やす</td><td class="mid">観測</td></tr>
<tr><th class="mid">38</th><td>共形因子の積分路はどれが正しいか</td><td class="mid">第一原理からの導出</td><td class="mid">計算</td></tr>
<tr class="hi"><th class="mid">38</th><td>ゴーストを両方に置かない理論はあるか</td><td class="mid">存在証明か不可能性証明</td><td class="mid">計算</td></tr>
<tr><th class="mid">40</th><td>地平面の無い重力場のエントロピーとは何か</td><td class="mid">合意された定義</td><td class="mid">定義</td></tr>
<tr class="hi"><th class="mid">41</th><td>初期の低エントロピーは何が説明するか</td><td class="mid">原始重力波 \(r\) の測定</td><td class="mid">観測</td></tr>
<tr><th class="mid">42</th><td>情報はブラックホールから出てくるか</td><td class="mid">機構の解明</td><td class="mid">計算</td></tr>
<tr><th class="mid">43</th><td>時空は離散か</td><td class="mid">ローレンツ不変性の 2 次の効果</td><td class="mid">観測</td></tr>
<tr class="hi"><th class="mid">43</th><td>\(G\) は共形変換で動くのか</td><td class="mid">──（規約の選択）</td><td class="mid">定義</td></tr>
<tr><th class="mid">44</th><td>\(^4\)He の \(\lambda\) 転移の \(6\sigma\) は何か</td><td class="mid">実験の再現と系統誤差</td><td class="mid">観測</td></tr>
<tr class="hi"><th class="mid">46</th><td>ハッブル定数の食い違いはどちらに落ちるか</td><td class="mid">距離はしごと CMB の再検討</td><td class="mid">観測</td></tr>
<tr><th class="mid">47</th><td>基本定数はいくつあるか</td><td class="mid">──（規約の選択）</td><td class="mid">定義</td></tr>
<tr class="hi"><th class="mid">48</th><td>感覚的な美しさは測れるか</td><td class="mid">──（この道具の外）</td><td class="mid">測れない</td></tr>
<tr><th class="mid">48</th><td>自然さの事前分布は何が決めるか</td><td class="mid">──（事前の選択）</td><td class="mid">定義</td></tr>
</tbody>
</table>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">02</span>核心 ── 扉は、四種類しかなかった</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">種類</th><th class="mid">個数</th><th>性質</th></tr></thead>
<tbody>
<tr><th class="mid">観測</th><td class="mid">\(6\)</td><td>データが決める。<strong>いつか閉じる</strong></td></tr>
<tr><th class="mid">計算</th><td class="mid">\(4\)</td><td>証明か導出が決める。<strong>原理的には閉じる</strong></td></tr>
<tr class="hi"><th class="mid">定義</th><td class="mid">\(4\)</td><td>規約の選択。<strong>データでは閉じない</strong></td></tr>
<tr class="hi"><th class="mid">偶然／測れない</th><td class="mid">\(2\)</td><td>追う価値が無い／この道具の外。<strong>閉じられない</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>16 個のうち 6 個（4 割近く）は、データでは閉じません。</strong><br>
「物理の未解決問題」と聞いて思い浮かぶのは観測待ちのものですが、<br>
実際には<em>規約と、道具の外にあるものが同じくらいの数あります</em>。<br>
── <strong>「どの種類の扉か」を見分けることが、すでに一つの結果です。</strong></p>
</div>

<div class="fig">
<p class="cap">図：16 個の扉を種類別に並べたもの。<strong>観測で閉じるもの（左）は時期の見込みがあり、定義で決まるもの（右）は待っても閉じません</strong>。ツマミで「待つ年数」を動かすと、<em>どれだけ待っても右側が残る</em>ことが見えます</p>
<canvas id="cv" width="720" height="340"></canvas>
<div class="controls">
  <label>いまから待つ年数<input id="sy" type="range" min="0" max="30" value="0" step="1"></label>
  <span class="val" id="vy">0 年</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a3a"></i>観測で閉じる</span>
  <span><i class="swatch" style="background:#4a4a7a"></i>計算で閉じる</span>
  <span><i class="swatch" style="background:#8a5a2a"></i>定義で決まる（閉じない）</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>閉じたもの</span>
</div>
</div>

<h2><span class="n">03</span>観測で閉じる扉は、いつ閉じるか</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>測るもの</th><th class="mid">いまの値</th><th class="mid">装置</th><th class="mid">時期</th></tr></thead>
<tbody>
<tr class="hi"><th>原始重力波 \(r\)</th><td class="mid">\(<0.036\)</td><td class="mid">LiteBIRD / CMB-S4</td><td class="mid">2030 年代</td></tr>
<tr><th>暗黒エネルギー \(w(z)\)</th><td class="mid">\(-1.03\pm0.03\)</td><td class="mid">Euclid / DESI / Rubin</td><td class="mid">2020 年代後半</td></tr>
<tr><th>\(\alpha\) の時間変化</th><td class="mid">\(|\Delta\alpha/\alpha|<1.4\times10^{-8}\)</td><td class="mid">光格子時計・核時計</td><td class="mid">2020 年代</td></tr>
<tr class="hi"><th>ハッブル定数</th><td class="mid">\(67.4\) 対 \(73.0\)</td><td class="mid">JWST / 標準サイレン</td><td class="mid">2020 年代後半</td></tr>
<tr><th>BH のスピンと合体</th><td class="mid">モデル依存</td><td class="mid">LISA / Einstein Telescope</td><td class="mid">2030 年代</td></tr>
<tr><th>時空の離散性（2 次）</th><td class="mid">\(E_{\rm QG,2}>10^{11}\) GeV</td><td class="mid">CTA など</td><td class="mid">2020 年代後半</td></tr>
</tbody>
</table>
</div>

<p><strong>観測で閉じる 6 つのうち、ほとんどが 2020〜2030 年代に決着する見込み</strong>です ── <em>このシリーズの読者が、生きているうちに答えを見ます。</em></p>

<h2><span class="n">04</span>定義で決まる扉は、閉じない</h2>

<div class="seven">
<div class="row"><div class="mk">43</div><div class="txt"><strong>\(G\) は共形変換で動くのか</strong><span>規約の選択 ── 観測では決まらない</span></div></div>
<div class="row"><div class="mk">47</div><div class="txt"><strong>基本定数はいくつあるか</strong><span>同上</span></div></div>
<div class="row hi"><div class="mk">48</div><div class="txt"><strong>自然さの事前分布は何が決めるか</strong><span>同上 ── <em>ただしこれは「どうでもよい」という意味ではない</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0"><strong>規約を選ばないと、文が完成しません</strong>（第3回）。<br>
── <em>選んでから測る。順序が逆になると、答えが規約に依存していることに気づけません。</em><br>
第37回⑤（\(\alpha\) は一定か）、第43回②（最小長）は、<strong>まさにその実例</strong>でした。</p>
</div>

<h2><span class="n">05</span>判定が変わらなかったもの</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>言明</th><th class="mid">初出</th><th class="mid">その後</th></tr></thead>
<tbody>
<tr class="hi"><th>\(c\cdot t=\)一定 は記法であって、新しい物理ではない</th><td class="mid">第3回</td><td class="mid">第46回で再確認</td></tr>
<tr><th>初期宇宙まで額面で外挿すると元素合成と矛盾する</th><td class="mid">前シリーズ</td><td class="mid">動かない</td></tr>
<tr class="hi"><th>次元付きは帳簿、無次元が物理</th><td class="mid">第3回</td><td class="mid">第47回で SI が同じ線を引いていた</td></tr>
<tr><th>比較相手を言わなければ、まだ文になっていない</th><td class="mid">第3回</td><td class="mid">第37・43回で二度効いた</td></tr>
</tbody>
</table>
</div>

<p><strong>開いた扉の数だけ、閉じたままの扉もあります。</strong></p>

<div class="caveat">
<span class="tag">正直な線</span>
<p style="margin:0 0 10px"><strong>① 01節の 16 個という数は、本シリーズが数えた結果です。</strong> <em>何を「一つの扉」と数えるかは恣意的</em>で、細かく分ければもっと増え、まとめればもっと減ります ── 02節の割合（38 パーセント）も同じだけ動きます。<strong>要点は「四種類ある」という構造のほうで、個数ではありません</strong>（第46回③と同じ注意）。</p>
<p style="margin:0 0 10px"><strong>② 03節の「時期」は、各計画が公表している目標に基づく見込みです。</strong> <em>計画は遅れることがあり、目標精度に届かないこともあります</em> ── 装置名と時期は<strong>本稿執筆時点（2026 年）の見通し</strong>であって、約束ではありません。また「決着する」と書いた項目でも、結果が中間的で決着しない可能性は常にあります。</p>
<p style="margin:0 0 10px"><strong>③ 「計算で閉じる」に入れた 4 個は、楽観的な分類かもしれません。</strong> ブラックホールの情報問題（第42回）は<em>半世紀にわたって「もうすぐ解ける」と言われ続けてきた</em>問題で、「原理的には閉じる」という言い方が正しいかどうか自体、確かではありません。</p>
<p style="margin:0 0 10px"><strong>④ 「定義で決まる」ものを軽く扱ってはいけません。</strong> 規約の選択は<em>データでは決まりませんが、選び方によって何が測れるかが変わります</em> ── たとえば \(G\) を動かすかどうかで、最小長についての言明の意味がまるごと変わりました（第43回）。<strong>「観測で決まらない」は「重要でない」ではありません。</strong></p>
<p style="margin:0"><strong>⑤ この一覧は、本シリーズが扱った範囲の扉だけです。</strong> 物理学の未解決問題はこれよりはるかに多く（量子重力、暗黒物質の正体、バリオン非対称性、測定問題……）、<em>本稿はそれらを網羅していません</em> ── 「48 回で開けて閉じなかったもの」という限定つきの一覧です。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>開いたままの扉は、何種類に分かれたか。
<details><summary>答えを見る</summary><div class="ans"><strong>四種類</strong> ── ①観測で閉じる（6 個）、②計算で閉じる（4 個）、③定義で決まる（4 個）、④偶然／測れない（2 個）。<em>「どの種類の扉か」を見分けることが、すでに一つの結果</em>です。</div></details></li>

<li>データでは閉じない扉は、何割か。
<details><summary>答えを見る</summary><div class="ans"><strong>4 割近く（6 個、38 パーセント）</strong>です ── 定義で決まるもの 4 個と、偶然／測れないもの 2 個。<em>「物理の未解決問題」と聞いて思い浮かぶのは観測待ちのものですが、規約と道具の外にあるものが同じくらいあります</em>。ただし①のとおり、数え方に依存します。</div></details></li>

<li>観測で閉じる扉のうち、いちばん早く閉じそうなのは。
<details><summary>答えを見る</summary><div class="ans"><strong>\(\alpha\) の時間変化</strong>（光格子時計・核時計、2020 年代）と <strong>暗黒エネルギー \(w(z)\)</strong>、<strong>ハッブル定数</strong>（いずれも 2020 年代後半）です ── <em>このシリーズの読者が、生きているうちに答えを見ます</em>。ただし②のとおり、これは見通しであって約束ではありません。</div></details></li>

<li>「定義で決まる」扉は、どうでもよいのか。
<details><summary>答えを見る</summary><div class="ans"><strong>違います。</strong> 規約を選ばないと<em>文が完成しません</em>（第3回）── 選んでから測る、という順序が要ります。逆にすると、答えが規約に依存していることに気づけません。<strong>「観測で決まらない」は「重要でない」ではありません</strong>（正直な線④）。</div></details></li>

<li>（やや難）48 回で一度も動かなかった判定は何か。
<details><summary>答えを見る</summary><div class="ans">四つ ── ①\(c\cdot t=\)一定 は記法であって新しい物理ではない（第3回、第46回で再確認）、②初期宇宙まで額面で外挿すると元素合成と矛盾する（前シリーズ）、③次元付きは帳簿・無次元が物理（第47回で SI が同じ線を引いていた）、④比較相手を言わなければまだ文になっていない（第37・43回で二度効いた）。<em>開いた扉の数だけ、閉じたままの扉もあります。</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　扉には、四種類しかなかった</h2>
<p>48 回で開けて閉じなかった問いを並べると <strong>16 個</strong>あり、それは<strong>四種類</strong>に分かれました ── <em>観測で閉じる</em>もの 6 個、<em>計算で閉じる</em>もの 4 個、<em>定義で決まる</em>もの 4 個、<em>偶然／測れない</em>もの 2 個。</p>
<p>観測で閉じる 6 つは、ほとんどが <strong>2020〜2030 年代に決着する見込み</strong>です ── 原始重力波 \(r\)（LiteBIRD / CMB-S4）、暗黒エネルギー \(w(z)\)（Euclid / DESI / Rubin）、\(\alpha\) の時間変化（光格子時計）、ハッブル定数（JWST / 標準サイレン）、BH のリングダウン（LISA / Einstein Telescope）、時空の離散性（CTA）。<em>このシリーズの読者が、生きているうちに答えを見ます。</em></p>
<p>ところが <strong>16 個のうち 6 個（4 割近く）は、データでは閉じません</strong>。「物理の未解決問題」と聞いて思い浮かぶのは観測待ちのものですが、実際には<em>規約と、道具の外にあるものが同じくらいの数あります</em> ── <strong>「どの種類の扉か」を見分けることが、すでに一つの結果でした。</strong></p>
<p>そして定義で決まる扉を、軽く扱ってはいけません。<strong>規約を選ばないと、文が完成しない</strong>（第3回）── 選んでから測る。順序が逆になると、答えが規約に依存していることに気づけません。第37回の「\(\alpha\) は一定か」も、第43回の「最小長」も、<em>まさにその実例</em>でした。</p>
<p>最後に、<strong>48 回で一度も動かなかったもの</strong>も書いておきます ── \(c\cdot t=\)一定 は記法であって新しい物理ではないこと、初期宇宙まで外挿すれば元素合成と矛盾すること、次元付きは帳簿で無次元が物理であること、比較相手を言わなければまだ文になっていないこと。<em>開いた扉の数だけ、閉じたままの扉もあります。</em></p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第50回（最終回）</span>
次回で終わりです。題は<strong>「動くのは、一つだけだった」</strong> ── 50 回でやってきたことを、<em>一つの文</em>にまとめます。第 I 部から第 VI 部まで、九つの理論、八つの壊れる場所、16 の開いた扉、そして四度の圧縮 ── <strong>それらが全部、第3回で作った一つの手続きの帰結だったこと</strong>を、最後にもう一度だけ確かめます。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sy=document.getElementById('sy'), vy=document.getElementById('vy'), ro=document.getElementById('ro');
  var X0=54, X1=690, Y0=44;

  // [label, kind, yearsToClose]  kind: 0=観測 1=計算 2=定義/閉じない
  var D=[
    ['α の時間変化', 0, 3],
    ['w(z)', 0, 4],
    ['ハッブル定数', 0, 5],
    ['時空の離散性', 0, 6],
    ['原始重力波 r', 0, 11],
    ['BH リングダウン', 0, 12],
    ['MOND の他データ', 0, 8],
    ['共形重力の CMB', 1, 15],
    ['積分路の導出', 1, 99],
    ['ゴーストの可否', 1, 99],
    ['BH 情報問題', 1, 99],
    ['重力エントロピーの定義', 2, 99],
    ['G は動くか', 2, 99],
    ['基本定数の個数', 2, 99],
    ['自然さの事前', 2, 99],
    ['感覚的な美しさ', 2, 99]
  ];
  var COL=['#2a5a3a','#4a4a7a','#8a5a2a'];

  function draw(){
    var yr=parseInt(sy.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    var cols=4, rows=4, cw=(X1-X0)/cols, ch=58, open=0;
    for(var i=0;i<D.length;i++){
      var r=Math.floor(i/cols), c=i%cols;
      var x=X0+c*cw, y=Y0+r*ch;
      var closed=(D[i][2]<=yr);
      if(!closed) open++;
      g.fillStyle = closed ? '#f0eef3' : COL[D[i][1]];
      g.globalAlpha = closed ? 1 : 0.9;
      g.fillRect(x+4, y, cw-10, ch-14);
      g.globalAlpha=1;
      g.fillStyle = closed ? '#b8b2c0' : '#fff';
      g.textAlign='center';
      g.fillText(D[i][0], x+cw/2-1, y+ch/2-6);
      if(closed) g.fillText('（閉じた）', x+cw/2-1, y+ch/2+10);
    }

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('16 個の扉 ── 待っても閉じないものが残る', (X0+X1)/2, Y0+rows*ch+16);

    vy.textContent=yr+' 年';
    var perm=6;
    ro.textContent=yr+' 年待つと　→　開いたままの扉は '+open+' 個／16 個'+
      (yr>=15?'　★ これ以上待っても '+perm+' 個は閉じない ── 規約と、道具の外にあるもの':'')+
      (yr===0?'　（いまの状態）':'');
  }
  sy.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-49-open-doors.html', acc='#2a5a3a', ops='#8a5a2a',
      title='開いたままの扉 ── わかる c·t=一定 第49回（第VI部）',
      ep='第 49 回 ／ 第 VI 部・手続きを検査する',
      eyebrow='4 割近くは、データでは閉じません',
      h1='扉には、<br>四種類しかなかった',
      sub='48 回で開けて閉じなかった問いを、全部並べます。<br><em>そして「どの種類の扉か」を見分けることが、すでに一つの結果でした。</em>',
      byline_l='必要な道具：第3回の判定、第19回の目盛り、第 IV・V 部の未解決、第48回',
      byline_r='16 個の扉、6 個は待っても閉じない',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第49回（第 VI 部の 4 回目）、物理好きの高校生・大学生向け読み物です。本回は第1〜48回で「未解決」「未決着」「測れない」と書いた箇所を集めたもので、新しい計算はありません（集計は kenshou/calc53.py）── 各項目の詳細はそれぞれの回の巻末を参照してください。<strong>01節の 16 個という数は本シリーズが数えた結果で、何を「一つの扉」と数えるかは恣意的です</strong> ── 細かく分ければ増え、まとめれば減り、02節の割合も同じだけ動きます。<em>要点は「四種類ある」という構造で、個数ではありません</em>。<strong>03節の「時期」は各計画が公表している目標に基づく見込みで</strong>、計画は遅れることがあり目標精度に届かないこともあります ── 装置名と時期は<em>本稿執筆時点（2026 年）の見通し</em>であって約束ではなく、「決着する」と書いた項目でも結果が中間的で決着しない可能性は常にあります。<strong>「計算で閉じる」に入れた 4 個は楽観的な分類かもしれません</strong> ── ブラックホールの情報問題は半世紀にわたって「もうすぐ解ける」と言われ続けてきた問題です。<strong>「定義で決まる」ものを軽く扱ってはいけません</strong>：規約の選択はデータでは決まりませんが、選び方によって何が測れるかが変わります（第43回で \\(G\\) を動かすかどうかが最小長の言明の意味を変えました）── <em>「観測で決まらない」は「重要でない」ではありません</em>。<strong>この一覧は本シリーズが扱った範囲の扉だけで</strong>、物理学の未解決問題はこれよりはるかに多く（量子重力、暗黒物質の正体、バリオン非対称性、測定問題……）、本稿はそれらを網羅していません。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで年数を進めると、閉じない扉が残ることが見えます。「答えを見る」で解答が開きます。')
