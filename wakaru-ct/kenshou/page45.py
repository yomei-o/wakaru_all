# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第 V 部の八回を、一枚に並べます ── 量子アノマリー、共形因子問題、回転する時空、重力エントロピー、ワイル曲率仮説、ブラックホール内部、プランクスケール、離散化。並べると分かるのは、<em>「壊れた」と呼んできたものが、じつは一度も故障ではなかった</em>ということです。そして ── <strong>道具が触れるのは、世界のちょうど半分。残りの半分に、時間の矢があります。</strong></p>

<h2><span class="n">01</span>八回を、一枚の表に</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">回</th><th>題</th><th class="mid">何が起きたか</th><th class="mid">分類</th><th class="mid">得たもの</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">37</th><td>量子アノマリー</td><td class="mid">\(\mu\) が持ち込まれる</td><td class="mid"><strong>スケールが入った</strong></td><td class="mid">破れを 28.7 bit で測れた</td></tr>
<tr><th class="mid">38</th><td>共形因子問題</td><td class="mid">\(\Omega\) が場になる</td><td class="mid">道具は正しく働いた</td><td class="mid">壊れていたのは理論の側</td></tr>
<tr class="hi"><th class="mid">39</th><td>回転する時空</td><td class="mid">ワイル \(\ne0\)</td><td class="mid"><strong>触れられない構造</strong></td><td class="mid">第 3 段 ── 平坦にできない</td></tr>
<tr><th class="mid">40</th><td>重力エントロピー</td><td class="mid">全部が無次元</td><td class="mid">道具の内側</td><td class="mid">三つの \(10^{122}\) が一つに</td></tr>
<tr class="hi"><th class="mid">41</th><td>ワイル曲率仮説</td><td class="mid">初期でワイル \(=0\)</td><td class="mid"><strong>触れない側の要請</strong></td><td class="mid">時間の矢の向き</td></tr>
<tr><th class="mid">42</th><td>BH の内部</td><td class="mid">事象 vs 見かけ</td><td class="mid">片方だけ触れる</td><td class="mid">因果は 0、\(\theta=0\) は違う</td></tr>
<tr class="hi"><th class="mid">43</th><td>プランクスケール</td><td class="mid">\(\ell_P\) はウェイト \(+1\)</td><td class="mid"><strong>スケールが入った</strong></td><td class="mid">仮定からして排除</td></tr>
<tr><th class="mid">44</th><td>離散化</td><td class="mid">\(a\) は irrelevant</td><td class="mid">スケールが残らない</td><td class="mid">それなら戻ってくる</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">02</span>失敗は、二種類しかなかった</h2>

<div class="seven">
<div class="row"><div class="mk">A</div><div class="txt"><strong>スケールが持ち込まれた</strong><span>第37回（\(\mu\)）、第43回（\(\ell_P\)）、第44回（\(a\)）── 道具は<em>正しく報告している</em>。生き残るかは irrelevant かどうか</span></div></div>
<div class="row"><div class="mk">B</div><div class="txt"><strong>共形類に入らない構造</strong><span>第39回（ワイル）、第42回（見かけの地平面）── 道具に<em>言うことが無い</em>。触れないのが正常</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>どちらも道具の故障ではない</strong><span>A は「スケールが入った」の報告、B は「それは私の担当ではない」の報告</span></div></div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>核心 ── 道具が触れるのは、曲率のちょうど半分</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>成分</th><th class="mid">共形変換のもとで</th><th class="mid">道具</th><th class="mid">中身</th></tr></thead>
<tbody>
<tr><th>リッチ 10 個</th><td class="mid">\(g\to\Omega^2g\) で<strong>変わる</strong></td><td class="mid">触れる</td><td class="mid">物質が決める側</td></tr>
<tr class="hi"><th>ワイル 10 個</th><td class="mid">\(C^a{}_{bcd}\) は<strong>共形不変</strong></td><td class="mid"><strong>触れない</strong></td><td class="mid">重力波・潮汐力の側</td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">4 次元でのリーマン曲率の独立成分は 20 個</span>
$$\underbrace{10}_{\text{触れる}}\;:\;\underbrace{10}_{\text{触れない}}\;=\;\textbf{ちょうど半分}$$
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0">「カーに届かない」のは、道具が弱いからではありません ──<br>
<strong>ワイル曲率とは、共形変換が保つ部分そのもの</strong>だからです。<br>
── <em>道具は失敗していません。自分の担当範囲を、正確に区切っているのです。</em></p>
</div>

<div class="fig">
<p class="cap">図：曲率の 20 成分を、道具が触れる側と触れない側に分けたもの。<strong>ちょうど半分ずつ</strong>です。ツマミで「共形因子 \(\Omega\)」を動かすと、<em>左半分だけが動き、右半分はまったく動きません</em> ── そして<strong>時間の矢は、動かない右半分に書かれています</strong></p>
<canvas id="cv" width="720" height="340"></canvas>
<div class="controls">
  <label>共形因子 \(\Omega\)<input id="so" type="range" min="30" max="300" value="100" step="1"></label>
  <span class="val" id="vo">1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#5a4a2a"></i>リッチ 10 個（触れる ＝ 帳簿）</span>
  <span><i class="swatch" style="background:#2a5a5a"></i>ワイル 10 個（触れない ＝ 物理）</span>
</div>
</div>

<h2><span class="n">04</span>すると、第41回が違って見える</h2>

<div class="seven">
<div class="row"><div class="mk">41</div><div class="txt"><strong>ワイル曲率仮説は「初期特異点でワイル \(=0\)」を要請する</strong><span>そして 03節より、ワイルは<em>共形変換が触れない側</em></span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>時間の矢は、道具が触れない半分だけで書かれている</strong><span>第41回では「届く場所から届かない場所へ」と書いたが、正確には <em>矢そのものが、触れない側の量で定義されている</em></span></div></div>
<div class="row"><div class="mk">→</div><div class="txt"><strong>だから矢は動かせない</strong><span>道具で動かせない量に矢が書いてあるから</span></div></div>
</div>

<h2><span class="n">05</span>第 V 部で測ったビットを並べる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>量</th><th class="mid">ビット</th><th class="mid">備考</th></tr></thead>
<tbody>
<tr><th>第37回：QED の共形対称性の破れ</th><td class="mid">\(28.7\)</td><td class="mid">雑音の床に対して</td></tr>
<tr><th>第38回：皺 \(n=50\) の経路積分の重み</th><td class="mid">\(8498\)</td><td class="mid">玩具模型、上限なし</td></tr>
<tr><th>第39回：高スピン源が上限のすぐ下</th><td class="mid">\(4.3\)</td><td class="mid">偶然の帯（説明あり）</td></tr>
<tr><th>第40回：使っていない容量</th><td class="mid">\(59.3\)</td><td class="mid">倍化の回数</td></tr>
<tr class="hi"><th>第41回：初期状態の特別さ</th><td class="mid"><strong>\(3.27\times10^{122}\)</strong></td><td class="mid">＝ 第24回・第40回と同じ数</td></tr>
<tr><th>第42回：M87\(^*\) の中で読めない量</th><td class="mid">\(126.5\)</td><td class="mid">上限の上限でも足りない</td></tr>
<tr><th>第43回：LHC からプランク長まで</th><td class="mid">\(49.7\)</td><td class="mid">倍化の回数</td></tr>
<tr><th>第44回：格子を 2 倍細かくして買える量</th><td class="mid">\(0.83\)</td><td class="mid">1 回あたり</td></tr>
</tbody>
</table>
</div>

<p><strong>これらは同じ単位で書いてありますが、同じものではありません</strong> ── 驚き、余白、隔たり、獲得。第26回・第36回と同じ注意です。<em>それでも一つ言えます</em>：<strong>全部が無次元の列にあります。</strong> 第 V 部で 0 の列に入らなかったのは、見かけの地平面と \(\ell_P\) だけでした（第43回⑦）。</p>

<h2><span class="n">06</span>第 IV 部の総括と、つなぐ</h2>

<div class="seven">
<div class="row"><div class="mk">36</div><div class="txt"><strong>第 IV 部：良い理論は、第3回の手術を最初から済ませてある</strong><span>── <em>理論についての</em>結論</span></div></div>
<div class="row"><div class="mk">45</div><div class="txt"><strong>第 V 部：道具が触れるのは、次元を持つ側のちょうど半分</strong><span>── <em>世界についての</em>結論</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>二つは同じ形をしている</strong><span>理論の側では「(A) 記法と (B) 主張を分けること」、世界の側では「触れる半分と触れない半分が決まっていること」── <em>どちらも第3回の一つの手続きの言い直し</em></span></div></div>
</div>

<div class="aside">
<span class="tag">第 I〜V 部を、一行ずつ</span>
<strong>第 I 部</strong>：\(c\cdot t=\)一定 は記法であって、モデルではない。<br>
<strong>第 II 部</strong>：どこに入れても、動くのは一つだけ。触れるのは大きさだけ。<br>
<strong>第 III 部</strong>：情報として測ると、同じ数を八つの言語で言い直していた。<br>
<strong>第 IV 部</strong>：同じ手術を他の理論に当てると、良い理論は最初から済ませてあった。<br>
<strong>第 V 部</strong>：<em>道具が触れるのは、世界のちょうど半分。残りの半分に、時間の矢がある。</em>
</div>

<div class="caveat">
<span class="tag">正直な線 ── 第 V 部全体について</span>
<p style="margin:0 0 10px"><strong>① 03節の「ちょうど半分」は、4 次元での成分の数え上げです。</strong> リーマン 20 ＝ リッチ 10 ＋ ワイル 10 は正しく、\(C^a{}_{bcd}\) が共形不変であることも標準的な結果ですが、<em>「触れる／触れない」を成分の個数で言うのは本シリーズの言い方</em>です。\(D\) 次元では比が変わります（\(D=3\) ではワイルは恒等的にゼロ、\(D=5\) では \(10:35\)）── <strong>「ちょうど半分」は \(D=4\) だけの性質</strong>で、そこが面白いところでもあります。</p>
<p style="margin:0 0 10px"><strong>② 02節の「失敗は二種類」という分類は、本シリーズの整理です。</strong> 第38回（共形因子問題）を「道具は正しく働いた」に入れたのは<em>読み方の選択</em>で、「道具が病理を露わにした」と読むか「道具の適用限界」と読むかは、立場によります。</p>
<p style="margin:0 0 10px"><strong>③ 05節の表は、単位が同じでも中身が違うものを並べています。</strong> 驚き（第37・39回）、余白（第40回）、隔たり（第42・43回）、1 手あたりの獲得（第44回）── <em>足したり比べたりできる量ではありません</em>。ビットという単位が「同じ通貨で書ける」ことを示すだけで、順位表ではありません（第36回⑤と同じ注意）。</p>
<p style="margin:0 0 10px"><strong>④ 04節の「時間の矢は触れない側で書かれている」は、ワイル曲率仮説を採ったときの言い方です。</strong> <em>ワイル曲率仮説自体が確立した法則ではありません</em>（第41回⑤）── 時間の矢の起源については他の立場もあり、本稿はワイル仮説を支持していません。</p>
<p style="margin:0"><strong>⑤ 第 V 部は、確立した内容の紹介と、本シリーズの読み方の両方を含んでいます。</strong> 量子アノマリー、共形因子問題、カー解、ブラックホール熱力学、くりこみ群と普遍性は<em>いずれも標準的な物理</em>です。一方、「壊れる場所は移動する」（第38回）、「時間の矢は届く範囲で言い直せる」（第41回）、「触れるのはちょうど半分」（今回）は<strong>本シリーズが並べて見つけた読み方</strong>であって、教科書に書いてある主張ではありません。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（第 V 部の総まとめ）</p>
<ol>
<li>第 V 部で起きた「失敗」は何種類か。
<details><summary>答えを見る</summary><div class="ans"><strong>二種類</strong>です。A：スケールが持ち込まれた（第37・43・44回）── <em>道具は正しく報告している</em>。B：共形類に入らない構造（第39・42回）── <em>道具に言うことが無い</em>。<strong>どちらも故障ではありません。</strong></div></details></li>

<li>共形変換が触れるのは、曲率の何割か。
<details><summary>答えを見る</summary><div class="ans"><strong>ちょうど半分</strong>。4 次元のリーマン 20 成分は リッチ 10（\(\Omega^2\) で変わる）＋ ワイル 10（\(C^a{}_{bcd}\) は共形不変）。<em>ただし①のとおり、これは \(D=4\) だけの性質</em>です。</div></details></li>

<li>「カーに届かない」のはなぜか。道具の弱さか。
<details><summary>答えを見る</summary><div class="ans"><strong>弱さではありません。</strong> ワイル曲率とは<em>共形変換が保つ部分そのもの</em>だからです ── 道具は失敗しておらず、<strong>自分の担当範囲を正確に区切っています</strong>。</div></details></li>

<li>時間の矢は、どちら側の量で書かれているか。
<details><summary>答えを見る</summary><div class="ans"><strong>道具が触れない側</strong>（ワイル）です。ワイル曲率仮説は初期特異点でワイル \(=0\) を要請しますが、ワイルは共形不変 ── <em>道具で動かせない量に矢が書いてあるからこそ、矢は動かせません</em>。ただし④のとおり、これはワイル仮説を採ったときの言い方です。</div></details></li>

<li>（やや難）第36回と第45回の結論は、どうつながるか。
<details><summary>答えを見る</summary><div class="ans"><strong>同じ形をしています。</strong> 第36回は<em>理論</em>について「(A) 記法と (B) 主張を分けてあるか」、第45回は<em>世界</em>について「触れる半分と触れない半分が決まっている」── <strong>どちらも第3回の一つの手続きの言い直し</strong>です。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　道具は一度も故障していなかった</h2>
<p>第 V 部の八回を並べると、「壊れた」と呼んできたものは<strong>二種類しかありませんでした</strong>。<em>A：スケールが持ち込まれた</em>（第37回の \(\mu\)、第43回の \(\ell_P\)、第44回の \(a\)）── これは道具が<strong>正しく報告している</strong>ので、生き残るかどうかは irrelevant かどうかで決まります（第44回）。<em>B：共形類に入らない構造</em>（第39回のワイル、第42回の見かけの地平面）── これは道具に<strong>言うことが無い</strong>だけで、触れないのが正常です。</p>
<p>そして今回いちばん大事なこと。4 次元のリーマン曲率 20 成分は、<strong>リッチ 10（\(g\to\Omega^2g\) で変わる）とワイル 10（\(C^a{}_{bcd}\) は共形不変）── ちょうど半分ずつ</strong>です。つまり「カーに届かない」のは道具が弱いからではなく、<em>ワイル曲率とは共形変換が保つ部分そのものだから</em>。<strong>道具は失敗しておらず、自分の担当範囲を正確に区切っています。</strong></p>
<p>すると第41回が違って見えてきます。ワイル曲率仮説は初期特異点でワイル \(=0\) を要請しますが、ワイルは<em>触れない側</em>。つまり ── <strong>時間の矢は、道具が触れない半分だけで書かれています。</strong> 道具で動かせない量に矢が書いてあるからこそ、矢は動かせないのです。</p>
<p>第 V 部で測ったビットも並べました ── 28.7、8498、4.3、59.3、\(3.27\times10^{122}\)、126.5、49.7、0.83。<em>単位は同じでも中身は違います</em>が、<strong>全部が無次元の列にあります</strong>。0 の列に入らなかったのは、見かけの地平面と \(\ell_P\) だけでした。</p>
<p>最後に第 IV 部とつなぎます。第36回は<strong>理論について</strong>「良い理論は第3回の手術を済ませてある」、第45回は<strong>世界について</strong>「道具が触れるのは次元を持つ側のちょうど半分」── <em>二つは同じ形をしており、どちらも第3回の一つの手続きの言い直し</em>でした。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第46回（第 VI 部のはじまり、最終部）</span>
第 VI 部は、<strong>手続きそのものを検査する部</strong>です。最初は <strong>\(a\propto t\) の特徴づけ、全部</strong> ── このシリーズが 45 回かけて扱ってきた \(a\propto t\) には、<em>いったい何通りの言い方があるのか</em>。\(w=-1/3\)、\(q=0\)、地平線がちょうど \(ct\)、第33回の \(R=6(1+k)/t^2\) がゼロ、共形時間が \(\ln t\) ── <strong>全部集めて、いくつあるかを数え、そのうち独立なのはいくつかを数えます。</strong> 第26回・第40回・第41回で三度効いた圧縮を、<em>今度はシリーズ自身の主題に当てます。</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var so=document.getElementById('so'), vo=document.getElementById('vo'), ro=document.getElementById('ro');
  var X0=60, X1=690, Y0=40, Y1=250, MID=(X0+X1)/2;

  function draw(){
    var om=parseInt(so.value,10)/100;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.strokeStyle='#cdc8d2'; g.lineWidth=1.6;
    g.beginPath(); g.moveTo(MID,Y0-14); g.lineTo(MID,Y1+22); g.stroke();

    g.textAlign='center';
    g.fillStyle='#5a4a2a'; g.font='13px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('リッチ 10 個 ── 触れる', (X0+MID)/2, Y0-22);
    g.fillStyle='#2a5a5a';
    g.fillText('ワイル 10 個 ── 触れない', (MID+X1)/2, Y0-22);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    // 左：Ω² で伸び縮みする棒
    var bw=(MID-X0-40)/10;
    for(var i=0;i<10;i++){
      var h=40*om*om;
      if(h>150) h=150;
      var x=X0+16+i*bw;
      g.fillStyle='#5a4a2a'; g.globalAlpha=0.85;
      g.fillRect(x, (Y0+Y1)/2-h/2, bw-6, h);
      g.globalAlpha=1;
    }
    // 右：まったく動かない棒
    for(var j=0;j<10;j++){
      var x2=MID+16+j*bw;
      g.fillStyle='#2a5a5a'; g.globalAlpha=0.85;
      g.fillRect(x2, (Y0+Y1)/2-20, bw-6, 40);
      g.globalAlpha=1;
    }

    g.fillStyle='#8a7a5a'; g.textAlign='center';
    g.fillText('Ω² = '+(om*om).toFixed(2)+' 倍に伸び縮みする', (X0+MID)/2, Y1+16);
    g.fillStyle='#3a6a6a';
    g.fillText('Ω をどう動かしても、まったく変わらない', (MID+X1)/2, Y1+16);

    g.fillStyle='#7d7686';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('4 次元のリーマン曲率 20 成分 ── ちょうど半分ずつ', MID, Y1+48);
    g.fillStyle='#2a5a5a';
    g.fillText('★ 時間の矢は、この右半分に書かれている', (MID+X1)/2, Y1+72);

    vo.textContent=om.toFixed(2);
    ro.textContent='Ω = '+om.toFixed(2)+
      '　→　リッチ側は '+(om*om).toFixed(2)+' 倍　／　ワイル側は 1.00 倍（不変）'+
      (om<0.5?'　★ どれだけ縮めても、右半分は動かない':'')+
      (om>2.5?'　★ どれだけ伸ばしても、右半分は動かない':'');
  }
  so.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-45-partV.html', acc='#2a5a5a', ops='#5a4a2a',
      title='道具が触れるのは、ちょうど半分 ── わかる c·t=一定 第45回（第V部・総括）',
      ep='第 45 回 ／ 第 V 部・総括',
      eyebrow='道具は一度も故障していませんでした',
      h1='触れるのは、<br>ちょうど半分',
      sub='第 V 部の「壊れた」は、二種類しかありませんでした ── どちらも故障ではありません。<br><em>そして残りの半分に、時間の矢があります。</em>',
      byline_l='必要な道具：第 V 部の八回、第3回の判定、第33回の三段判定、第36回の総括',
      byline_r='リッチ 10 ： ワイル 10 ── \\(D=4\\) だけの性質',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第45回（第 V 部・総括）、物理好きの高校生・大学生向け読み物です。本回は第37〜44回の結果をまとめたもので、新しい計算は 03節の成分の数え上げと 05節の集計のみです（kenshou/calc49.py）── 各回の数値と出典はそれぞれの回の巻末を参照してください。<strong>03節の「ちょうど半分」は 4 次元での成分の数え上げです</strong>：リーマン 20 ＝ リッチ 10 ＋ ワイル 10 は正しく \\(C^a{}_{bcd}\\) が共形不変であることも標準的な結果ですが、<em>「触れる／触れない」を成分の個数で言うのは本シリーズの言い方</em>で、\\(D\\) 次元では比が変わります（\\(D=3\\) ではワイルは恒等的にゼロ、\\(D=5\\) では 10:35）── <strong>「ちょうど半分」は \\(D=4\\) だけの性質</strong>です。<strong>02節の「失敗は二種類」という分類は本シリーズの整理</strong>で、第38回を「道具は正しく働いた」に入れたのは読み方の選択です。05節の表は<em>単位が同じでも中身が違うもの</em>（驚き・余白・隔たり・獲得）を並べており、足したり比べたりできる量ではありません。<strong>04節の「時間の矢は触れない側で書かれている」はワイル曲率仮説を採ったときの言い方で</strong>、ワイル曲率仮説自体が確立した法則ではありません ── 時間の矢の起源については他の立場もあり、本稿はワイル仮説を支持していません。<strong>第 V 部は確立した内容の紹介と本シリーズの読み方の両方を含みます</strong>：量子アノマリー、共形因子問題、カー解、ブラックホール熱力学、くりこみ群と普遍性はいずれも標準的な物理ですが、<em>「壊れる場所は移動する」「時間の矢は届く範囲で言い直せる」「触れるのはちょうど半分」は本シリーズが並べて見つけた読み方</em>であって、教科書に書いてある主張ではありません。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで Ω を動かすと、左半分だけが動きます。「答えを見る」で解答が開きます。')
