# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第 II 部の最後の一本です。真空エネルギーに入れると、ちょっと愉快なことが起きます ── <strong>この絵では、宇宙定数がいちばん速く育ちます</strong>（\(\propto t^4\)）。そして本当に定数なのは、標準の絵でいちばん速く薄まっていた<em>放射</em>のほう。<strong>順序が完全に逆転する。</strong> つまり「宇宙定数」という名前そのものが、絵の取り方に依存していた ── ということです。</p>

<h2><span class="n">01</span>三成分を、まとめて変換する</h2>

<p>エネルギー密度はウェイト \(-4\) なので、この絵では \(\tilde\rho=a^4\rho\)。標準の絵での薄まり方と掛け合わせるだけです。</p>

<div class="calc">
<span class="tag">計算 ── 掛けるだけ</span>
$$\tilde\rho_r=a^4\cdot a^{-4}=\text{一定}$$
$$\tilde\rho_m=a^4\cdot a^{-3}=a\ \propto t$$
$$\tilde\rho_\Lambda=a^4\cdot 1=a^4\ \propto t^4$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>成分</th><th class="mid">標準の絵</th><th class="mid">この絵</th><th class="mid">順位</th></tr></thead>
<tbody>
<tr><th>放射</th><td class="mid">\(\propto a^{-4}\)（いちばん速く薄まる）</td><td class="mid"><strong>一定</strong></td><td class="mid">1位 ↔ 3位</td></tr>
<tr><th>物質</th><td class="mid">\(\propto a^{-3}\)</td><td class="mid">\(\propto t\)</td><td class="mid">2位 ↔ 2位</td></tr>
<tr class="hi"><th>宇宙定数 \(\Lambda\)</th><td class="mid">一定（だから「定数」）</td><td class="mid"><strong>\(\propto t^4\)</strong>（いちばん速く育つ）</td><td class="mid">3位 ↔ 1位</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>「宇宙定数」という名前は、絵の取り方に依存しています。</strong><br>
この絵で本当に一定なのは、標準の絵でいちばん速く薄まっていた<em>放射</em>のほう。<br>
── 第3回でシリーズの題名にやった手術が、こんなところにも当たります。</p>
</div>

<p>第11回で「光子ガスは完全に静止している」と数えました。今回の一行目は、その<em>エネルギー密度版</em>です。\(\rho_r=7.05\times10^{-14}\ \mathrm{J/m^3}\) が、宇宙の全歴史を通じて同じ値。</p>

<h2><span class="n">02</span>それでも、宇宙定数問題は一ミリも動かない</h2>

<p>宇宙定数問題は「素朴な場の理論の見積もりと、観測値が \(10^{120}\) 桁違う」という話でした。この絵で \(\rho_\Lambda\) が \(t^4\) で育つなら、問題も動くのでしょうか。</p>

<div class="calc">
<span class="tag">無次元にする</span>
$$\rho_\Lambda^{1/4}=2.240\ \mathrm{meV}\qquad\Longrightarrow\qquad \frac{\rho_\Lambda^{1/4}}{M_{\rm Pl}}=1.835\times10^{-31}$$
<p class="lbl">4 乗すると、あの数</p>
$$\frac{\rho_\Lambda}{M_{\rm Pl}^4}=1.13\times10^{-123}$$
</div>

<p>\(\rho_\Lambda\) は \(t^4\) で育ちますが、\(M_{\rm Pl}^4\) も同じ \(t^4\) で育ちます（\(M_{\rm Pl}\) は質量なのでウェイト \(-1\)）。<strong>割ると、完全に打ち消し合う。</strong></p>

<div class="keybox">
<p class="lbl">02節の結論</p>
<p style="margin:6px 0 0">宇宙定数問題（\(10^{-123}\)）は、<strong>絵を変えても一ミリも動きません</strong>。<br>
比は無次元 ── 第10回のランダウアーのコストと、まったく同じ構図です。</p>
</div>

<h2><span class="n">03</span>「なぜ今？」問題も、消えない</h2>

<p>もう一つの有名な謎 ── <em>なぜ物質と暗黒エネルギーの密度が、よりによって今ごろ同じくらいなのか</em>。この絵ではどう見えるでしょうか。</p>

<div class="calc">
<span class="tag">比の時間変化を、両方の絵で</span>
<p class="lbl">標準の絵</p>
$$\frac{\rho_\Lambda}{\rho_m}=\frac{1}{a^{-3}}\propto a^3$$
<p class="lbl">この絵</p>
$$\frac{\tilde\rho_\Lambda}{\tilde\rho_m}=\frac{a^4}{a}=a^3\qquad\text{── 同じ}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th class="mid">値</th><th class="mid">この絵で</th></tr></thead>
<tbody>
<tr><th>今日の \(\rho_\Lambda/\rho_m\)</th><td class="mid">2.175</td><td class="mid">不変</td></tr>
<tr class="hi"><th>\(\Lambda\) と物質が並ぶ時刻</th><td class="mid">\(a=0.772\)（\(z=0.30\)）</td><td class="mid"><strong>不変</strong></td></tr>
<tr><th>放射と物質が並ぶ時刻</th><td class="mid">\(a=2.9\times10^{-4}\)（\(z=3400\)）</td><td class="mid"><strong>不変</strong></td></tr>
</tbody>
</table>
</div>

<p>比だけでなく、<strong>比の時間変化まで同じ</strong>です。だから「よりによって今ごろ」という不思議さの度合いも、寸分変わらない。<em>絵を取り替えても、謎は謎のまま残ります。</em></p>

<div class="aside">
<span class="tag">消える謎と、消えない謎</span>
このシリーズで「絵を変えたら消えた」ものは、実は一つもありません ── 消えたように見えたのは幾何の特異点（前シリーズ第6回）だけで、無次元比を作ったらやはり残りました。今回もそうです。<strong>宇宙定数問題も「なぜ今」問題も、最初から無次元で書かれているので、書き換えの手が届かない。</strong> <em>良い謎は、無次元で書かれている。</em>
</div>

<div class="fig">
<p class="cap">図：三成分のエネルギー密度。ツマミで語り方を切り替えると、<strong>三本の傾きが順位ごと入れ替わります</strong>（右端では放射が水平、\(\Lambda\) が最も急）。それでも<em>二つの交点（等密度点）は、まったく動きません</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>語り方 \(s\)（左＝標準の絵／右＝質量が育つ絵）<input id="ss" type="range" min="0" max="1000" value="1000" step="1"></label>
  <span class="val" id="vs">s = 1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#9a3a5a"></i>放射</span>
  <span><i class="swatch" style="background:#1f4a2a"></i>物質</span>
  <span><i class="swatch" style="background:#4a7a3a"></i>宇宙定数 \(\Lambda\)</span>
  <span><i class="swatch" style="background:#9aa89a"></i>等密度点（動かない）</span>
</div>
</div>

<p>左端（標準の絵）では、赤が急降下し緑が水平 ── 教科書で見慣れた図です。ツマミを右へ動かすと三本が回転して、右端では<strong>赤が水平、濃緑が \(+1\)、明緑が \(+4\)</strong>。まるで別の宇宙のようですが、<em>交点は一つも動いていません</em>。</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>種明かし ── 「定数」は、比較相手を隠した言葉</h2>

<p>なぜこんな逆転が起きるのか。答えは第3回とまったく同じです ── <strong>「一定である」は、何と比べて一定なのかを言わないと意味を持たない</strong>から。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>\(\rho_\Lambda\) を何と比べるか</th><th class="mid">結果</th></tr></thead>
<tbody>
<tr><th>共動体積あたりのエネルギー（標準の絵）</th><td class="mid">一定 →「宇宙定数」</td></tr>
<tr><th>粒子の質量（この絵）</th><td class="mid">\(\propto t^4/t^4=\)一定</td></tr>
<tr><th>固定した物差しの体積（この絵）</th><td class="mid">\(\propto t^4\) → 定数ではない</td></tr>
<tr class="hi"><th>\(M_{\rm Pl}^4\)</th><td class="mid"><strong>\(1.13\times10^{-123}\)、不変</strong> ← これが物理</td></tr>
</tbody>
</table>
</div>

<p>本当に不変な言い方は最後の行だけです。そして\(\Lambda\) が \(w=-1\) という状態方程式を持つこと ── これも無次元なので、どの絵でも同じ。<strong>\(\Lambda\) について物理的に言えることは、この二つだけ</strong>でした。</p>

<h2><span class="n">05</span>おまけ ── 自然界でいちばん小さい二つの数</h2>

<div class="calc">
<span class="tag">並べてみる</span>
$$\frac{\rho_\Lambda^{1/4}}{M_{\rm Pl}}=1.83\times10^{-31},\qquad \frac{m_\nu}{M_{\rm Pl}}=4.10\times10^{-30}$$
<p class="lbl">比</p>
$$\frac{m_\nu}{\rho_\Lambda^{1/4}}=22.3$$
</div>

<p>自然界で知られている<em>いちばん小さい二つのスケール</em>が、たった 22 倍しか離れていません（他は \(10^{25}\) 単位で開いているのに）。前シリーズ番外編⑤で指摘したこの一致も、当然ながら無次元 ── <strong>絵を変えても動きません</strong>。説明する理論は、いまのところありません。</p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① \(\tilde\rho=a^4\rho\) は「エネルギー密度のウェイトが \(-4\)」から出しています。</strong> エネルギーが \(-1\)、体積が \(+3\) なので合わせて \(-4\)。標準的な数え方です。</p>
<p style="margin:0 0 10px"><strong>② 「宇宙定数問題は \(10^{120}\)」は、素朴なカットオフ計算（\(\rho_{\rm vac}\sim M_{\rm Pl}^4\)）と観測値の比です。</strong> この見積もり自体が正当かどうかは論争があり、超対称性や繰り込みの扱いで数字は大きく変わります。本稿が主張しているのは「<em>その比が何であれ、絵の取り替えでは動かない</em>」という点だけです。</p>
<p style="margin:0 0 10px"><strong>③ 「なぜ今」問題の定量化として \(\rho_\Lambda/\rho_m\) の時間変化を使いました。</strong> これは一つの定式化にすぎず、「coincidence problem がそもそも問題なのか」自体に議論があります（人間原理的な説明、動的な暗黒エネルギー、など）。</p>
<p style="margin:0 0 10px"><strong>④ \(\Lambda\) を \(w=-1\) の完全流体として扱っています。</strong> 動的な暗黒エネルギー（クインテッセンス等）では \(\rho_\Lambda\) が時間変化するので、01節の表の三行目が変わります ── ただし<em>絵の取り替えで動かない</em>という結論は同じです。</p>
<p style="margin:0"><strong>⑤ \(m_\nu=0.05\) eV は振動実験から得られる最も重いニュートリノの下限の目安です。</strong> \(\rho_\Lambda^{1/4}\) との 22 倍という近さは<strong>説明のない数値的一致</strong>であり、理論的な関係は知られていません（前シリーズ番外編⑤）。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>この絵で三成分のエネルギー密度はどう変わるか。順位はどうなるか。
<details><summary>答えを見る</summary><div class="ans">\(\tilde\rho=a^4\rho\) なので、放射 \(a^4a^{-4}=\)一定、物質 \(a^4a^{-3}=a\propto t\)、\(\Lambda\) は \(a^4\propto t^4\)。<strong>順位が完全に逆転</strong>し、「定数」だった \(\Lambda\) がいちばん速く育ち、いちばん速く薄まっていた放射が本当の定数になります。</div></details></li>

<li>\(\rho_\Lambda\) が \(t^4\) で育つのに、宇宙定数問題が動かないのはなぜか。
<details><summary>答えを見る</summary><div class="ans">比べる相手の \(M_{\rm Pl}^4\) も同じ \(t^4\) で育つから（\(M_{\rm Pl}\) は質量でウェイト \(-1\)）。割ると打ち消して \(\rho_\Lambda/M_{\rm Pl}^4=1.13\times10^{-123}\) は<strong>不変</strong>です。</div></details></li>

<li>「なぜ今」問題は、この絵で緩和されるか。
<details><summary>答えを見る</summary><div class="ans">されません。\(\rho_\Lambda/\rho_m\) は標準の絵で \(\propto a^3\)、この絵で \(a^4/a=a^3\) ── <strong>比の時間変化まで同じ</strong>。今日の値 2.175 も、等密度点 \(z=0.30\) も動きません。<em>良い謎は無次元で書かれているので、書き換えの手が届かない。</em></div></details></li>

<li>この絵で本当に「定数」なのは何か。
<details><summary>答えを見る</summary><div class="ans"><strong>放射のエネルギー密度</strong>（\(7.05\times10^{-14}\ \mathrm{J/m^3}\)）。第11回で「光子ガスは完全に静止している」と数えたことの、エネルギー密度版です。<em>「宇宙定数」という名前は、絵の取り方に依存していました。</em></div></details></li>

<li>（やや難）\(\Lambda\) について、絵に依らず言えることを全部挙げよ。
<details><summary>答えを見る</summary><div class="ans">二つだけです ── ①状態方程式 \(w=-1\)（無次元）、②\(\rho_\Lambda/M_{\rm Pl}^4=1.13\times10^{-123}\)（無次元）。そこから従う \(\rho_\Lambda/\rho_m\) の値と時間変化も不変です。<strong>「一定である」ことは、絵に依らずには言えません</strong> ── それが今回いちばん愉快なところです。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　「定数」という名前が、帳簿だった</h2>
<p>エネルギー密度はウェイト \(-4\) なので \(\tilde\rho=a^4\rho\)。三成分に当てると ── 放射は<strong>一定</strong>、物質は \(\propto t\)、宇宙定数は <strong>\(\propto t^4\)</strong>。<em>順位が完全に逆転します。</em> 標準の絵でいちばん速く薄まっていた放射が本当の定数になり、「定数」と呼ばれていた \(\Lambda\) がいちばん速く育つ。<strong>「宇宙定数」という名前そのものが、絵の取り方に依存していました。</strong></p>
<p>それでも謎は動きません。\(\rho_\Lambda\) が \(t^4\) で育っても \(M_{\rm Pl}^4\) が同じだけ育つので、<strong>\(\rho_\Lambda/M_{\rm Pl}^4=1.13\times10^{-123}\) は不変</strong>。宇宙定数問題は一ミリも動かない。「なぜ今」問題も同じで、\(\rho_\Lambda/\rho_m\) は両方の絵で \(\propto a^3\)、今日の値 2.175 も等密度点 \(z=0.30\) も動きません。<em>良い謎は最初から無次元で書かれているので、書き換えの手が届かない。</em></p>
<p>種明かしは第3回と同じでした ── <strong>「一定である」は、何と比べて一定かを言わないと意味を持たない</strong>。\(\Lambda\) について絵に依らず言えるのは、\(w=-1\) と \(\rho_\Lambda/M_{\rm Pl}^4\) の二つだけです。おまけに、自然界でいちばん小さい二つのスケール（\(\rho_\Lambda^{1/4}/M_{\rm Pl}=1.83\times10^{-31}\) と \(m_\nu/M_{\rm Pl}=4.10\times10^{-30}\)）が 22 倍しか離れていないという一致も、当然ながら不変のままです。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第13回</span>
第 II 部の残りは、宇宙論から完全に離れます。次は<strong>流体と乱流</strong>です ── レイノルズ数、マッハ数、プラントル数、ストローハル数。工学が使う無次元数は、<em>一つ残らず不変</em>です。だから相似則も、風洞実験も、乱流のコルモゴロフ則も、この絵で一文字も変わりません。では何が変わるのか ── <strong>粘性率と、レイノルズ数を作る三つの量が、それぞれ別のウェイトで動きます</strong>。動くものだけを見ると別世界なのに、組み合わせると必ず戻る。<em>「無次元だけが物理」が、宇宙論の外でどれだけ効くか</em>を確かめる回です。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=318;
  var xmin=-4.2, xmax=0.4;      // log10 a
  var ymin=-6, ymax=18;         // log10(ρ / ρ_Λ,today)
  var Om=0.315, OL=0.685, Or=9.2e-5;
  var A_EQ1=Math.log(Or/Om)/Math.LN10;          // 放射=物質
  var A_EQ2=Math.log(Math.pow(Om/OL,1/3))/Math.LN10; // 物質=Λ

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function lg(v){ return Math.log(v)/Math.LN10; }

  function seg(sl,off,col,w){
    g.strokeStyle=col; g.lineWidth=w; g.beginPath();
    var first=true;
    for(var i=0;i<=200;i++){
      var lx=xmin+(xmax-xmin)*i/200, y=off+sl*lx;
      if(y<ymin||y>ymax){ first=true; continue; }
      if(first){ g.moveTo(px(lx),py(y)); first=false; } else g.lineTo(px(lx),py(y));
    }
    g.stroke();
  }

  function draw(){
    var s=parseInt(ss.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.textAlign='right';
    for(var e=-6;e<=18;e+=4){
      var y=py(e);
      g.strokeStyle='#eef2ee'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#95a595'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-4;q<=0;q++){
      var x=px(q);
      g.strokeStyle='#f5f8f5'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#95a595'; g.fillText(q===0?'いま':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#c6d2c6'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // 等密度点（縦線）
    [[A_EQ1,'放射=物質'],[A_EQ2,'物質=Λ']].forEach(function(q){
      g.strokeStyle='#9aa89a'; g.lineWidth=1.5; g.setLineDash([5,4]);
      g.beginPath(); g.moveTo(px(q[0]),Y0); g.lineTo(px(q[0]),Y1); g.stroke();
      g.setLineDash([]);
      g.fillStyle='#7f8d7f'; g.textAlign='center';
      g.fillText(q[1], px(q[0]), Y0-8);
    });

    // 三成分（今日の値で規格化、Λ を 1 とする）
    seg(-4*(1-s), lg(Or/OL), '#9a3a5a', 3.2);   // 放射
    seg(-3*(1-s), lg(Om/OL), '#1f4a2a', 3.2);   // 物質
    seg( 0*(1-s)+4*s, 0,     '#4a7a3a', 3.2);   // Λ

    g.textAlign='left'; g.font='bold 12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillStyle='#9a3a5a'; g.fillText('放射', px(xmin)+8, py(Math.min(lg(Or/OL)-4*(1-s)*xmin,ymax))-6);
    g.fillStyle='#1f4a2a'; g.fillText('物質', px(xmin)+46, py(Math.min(lg(Om/OL)-3*(1-s)*xmin,ymax))+16);
    g.fillStyle='#4a7a3a'; g.fillText('Λ',    px(xmin)+8, py(Math.max(4*s*xmin,ymin))+16);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.fillStyle='#7a8a7a'; g.textAlign='center';
    g.fillText('スケール因子  a', (X0+X1)/2, Y1+36);

    vs.textContent='s = '+s.toFixed(2);
    var tag = s>0.995?'（質量が育つ絵）':(s<0.005?'（標準の絵）':'（途中の語り方）');
    ro.textContent='s = '+s.toFixed(2)+' '+tag+
      '　放射 ∝ a^'+(-4*(1-s)).toFixed(2)+
      '　物質 ∝ a^'+(-3*(1-s)).toFixed(2)+
      '　Λ ∝ a^'+(4*s).toFixed(2)+
      '　／　交点は z=3400 と z=0.30 に釘付け'+
      (s>0.995?'　★ 順位が完全に逆転した':'');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-12-vacuum.html', acc='#1f4a2a', ops='#9a3a5a',
      title='真空に入れてみる ── わかる c·t=一定 第12回',
      ep='第 12 回 ／ 第 II 部・宇宙論編のしめくくり',
      eyebrow='この絵では、宇宙定数がいちばん速く育ちます',
      h1='真空に、<br>入れてみる',
      sub='\\(\\tilde\\rho_\\Lambda\\propto t^4\\)、\\(\\tilde\\rho_m\\propto t\\)、\\(\\tilde\\rho_r=\\)一定。<br><em>順位が完全に逆転し、「定数」という名前が帳簿だったと分かります。</em>',
      byline_l='必要な道具：ウェイト \\(-4\\)、掛け算',
      byline_r='\\(\\rho_\\Lambda/M_{\\rm Pl}^4=1.13\\times10^{-123}\\) は不変',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第12回、物理好きの高校生・大学生向け読み物です。共形変換のもとでエネルギー密度がウェイト \\(-4\\)（エネルギー \\(-1\\)＋体積 \\(+3\\)）であること、標準宇宙論で \\(\\rho_r\\propto a^{-4}\\)、\\(\\rho_m\\propto a^{-3}\\)、\\(\\rho_\\Lambda=\\)一定 であることは、いずれも標準的です。本稿の \\(\\tilde\\rho_r=\\)一定、\\(\\tilde\\rho_m\\propto t\\)、\\(\\tilde\\rho_\\Lambda\\propto t^4\\)（順位の逆転）は、その二つを掛け合わせた本稿での計算です。\\(\\rho_\\Lambda^{1/4}=2.240\\) meV、\\(\\rho_\\Lambda^{1/4}/M_{\\rm Pl}=1.835\\times10^{-31}\\)、\\(\\rho_\\Lambda/M_{\\rm Pl}^4=1.13\\times10^{-123}\\) は \\(h=0.674\\)、\\(\\Omega_\\Lambda=0.685\\) からの本稿の計算です。<strong>「宇宙定数問題は \\(10^{120}\\)」という言い方は、素朴なカットオフ計算 \\(\\rho_{\\rm vac}\\sim M_{\\rm Pl}^4\\) と観測値の比であり、この見積もり自体の正当性には論争があります</strong> ── 本稿の主張は「その比が何であれ、絵の取り替えでは動かない」という点のみです。同様に coincidence problem（「なぜ今」問題）がそもそも問題なのかにも議論があります。\\(\\Lambda\\) は \\(w=-1\\) の完全流体として扱っており、動的な暗黒エネルギーでは 01節の表の三行目が変わります（ただし絵の取り替えで動かないという結論は同じです）。等密度点 \\(a=(\\Omega_m/\\Omega_\\Lambda)^{1/3}=0.772\\)（\\(z=0.30\\)）、\\(a=\\Omega_r/\\Omega_m=2.9\\times10^{-4}\\)（\\(z=3400\\)）も本稿の計算です。\\(m_\\nu=0.05\\) eV は振動実験からの最も重いニュートリノの下限の目安で、\\(\\rho_\\Lambda^{1/4}\\) との 22 倍という近さは説明のない数値的一致です（前シリーズ番外編⑤）。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルで、初期宇宙まで外挿した場合は元素合成と矛盾します（Lewis, Barnes &amp; Kaushik 2016）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで語り方を切り替え、三本の順位が逆転しても交点が動かない様子が見えます。「答えを見る」で解答が開きます。')
