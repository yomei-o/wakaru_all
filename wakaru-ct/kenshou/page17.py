# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">ここから第 III 部は、宇宙を<strong>情報として測る</strong>部です。最初は通信 ── そして最初から、いちばん有名な難問にぶつかります。<em>宇宙マイクロ波背景放射は、因果的に切れた \(10^4\) 個の領域にまたがって、\(10^{-5}\) の精度で一様</em>。これを情報の言葉に直すと、こうなります ── <strong>メッセージを一通も交換していない 9600 台のノードが、17 ビットぶん合意している。</strong> 分散システムなら、起こりえない状況です。</p>

<h2><span class="n">01</span>一様性を、ビットで測る</h2>

<p>「\(\Delta T/T\sim10^{-5}\) で一様」を、情報の言葉に翻訳します。二つの温度が \(10^{-5}\) の精度で一致しているとは、<em>上位何桁が揃っているか</em>ということです。</p>

<div class="calc">
<span class="tag">計算 ── 対数を取るだけ</span>
$$\log_2\frac{1}{10^{-5}}=16.61\ \text{ビット}$$
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0">天球上の任意の二点が、温度について <strong>17 ビットぶん一致している</strong>。<br>
── これは「揃っている」という定性的な話ではなく、<em>数えられる量</em>です。</p>
</div>

<h2><span class="n">02</span>ノードは、何台あるか</h2>

<p>次に「因果的に切れた領域」を数えます。再結合の時点で、光が届いていた範囲（共動の粒子的地平線）は 288 Mpc。私たちから最終散乱面までの共動距離は 14100 Mpc。だから ──</p>

<div class="calc">
<span class="tag">計算 ── 立体角で割る</span>
<p class="lbl">地平線が張る角度</p>
$$\theta=\frac{288}{14100}=0.0204\ \mathrm{rad}=1.17^\circ$$
<p class="lbl">全天をその立体角で割る</p>
$$N=\frac{4\pi}{2\pi(1-\cos\theta)}=9.6\times10^{3}$$
</div>

<p>およそ <strong>9600 台</strong>。よく引かれる「\(10^4\) 個の因果的パッチ」と同じ桁です。<em>この 9600 台は、CMB が放たれるまで一度も互いに信号を交換していません</em> ── 光速で届く範囲の外にいたからです。</p>

<h2><span class="n">03</span>合意している情報の総量は、20 キロバイト</h2>

<div class="calc">
<span class="tag">掛けるだけ</span>
$$9.6\times10^{3}\ \text{台}\ \times\ 16.6\ \text{ビット}=1.59\times10^{5}\ \text{ビット}\simeq20\ \mathrm{KB}$$
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0">合意に必要だった情報は、たった <strong>20 キロバイト</strong>。<br>
スマホなら一瞬で送れる量です。<em>問題は情報の量ではなく、送る手段が無かったこと</em> ── <strong>チャネルの不在</strong>です。</p>
</div>

<p>地平線問題を「なぜこんなに揃っているのか」と言うと不思議に聞こえますが、情報の言葉にすると問題の形が変わります ── <em>揃っていること自体は大した量ではない。あり得ないのは、通信路がゼロなのに揃っていること。</em></p>

<h2><span class="n">04</span>偶然では、絶対に説明できない</h2>

<p>「たまたま揃った」で済むでしょうか。各パッチの温度が独立にばらつくとすると、一台が \(10^{-5}\) の精度で一致する確率は \(10^{-5}\)。全部そろう確率は ──</p>

<div class="calc">
<span class="tag">掛け算</span>
$$\left(10^{-5}\right)^{9600}=10^{-48000}$$
</div>

<p>宇宙の全ビット数が \(10^{122}\) であることを思い出すと、これは<strong>「宇宙が扱える確率の範囲を、桁数の桁で超えている」</strong>数です。<em>偶然という選択肢は、完全に消えます。</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">05</span>\(c\cdot t=\text{一定}\) は、この問題を持たない</h2>

<p>ではパッチ数は、膨張則をどう変えると減るのでしょうか。共動の粒子的地平線は \(\chi=\int c\,dt/a\) なので、\(a\propto t^p\) なら \(\chi\propto t^{1-p}\)。パッチ数はその比の 2 乗です。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">膨張則 \(p\)</th><th class="mid">共動地平線の比</th><th class="mid">パッチ数</th><th class="mid">合意すべきビット</th></tr></thead>
<tbody>
<tr><th class="mid">0.500（放射）</th><td class="mid">190</td><td class="mid">\(3.6\times10^{4}\)</td><td class="mid">75 KB</td></tr>
<tr><th class="mid">0.513（観測の対数平均）</th><td class="mid">166</td><td class="mid">\(2.8\times10^{4}\)</td><td class="mid">57 KB</td></tr>
<tr><th class="mid">0.667（物質）</th><td class="mid">33</td><td class="mid">\(1.1\times10^{3}\)</td><td class="mid">2.3 KB</td></tr>
<tr><th class="mid">0.900</th><td class="mid">2.9</td><td class="mid">8.2</td><td class="mid">17 バイト</td></tr>
<tr class="hi"><th class="mid">1.000（\(c\cdot t=\)一定）</th><td class="mid">発散（∞）</td><td class="mid"><strong>1</strong></td><td class="mid"><strong>0</strong></td></tr>
</tbody>
</table>
</div>

<p>\(a\propto t\) では粒子的地平線が発散します（前シリーズ番外編③の特徴づけ⑤）。つまり<strong>宇宙のどの二点も、必ずどこかの時点で通信できていた</strong> ── パッチは 1 個、合意すべきビットはゼロ。<em>地平線問題が、原理的に発生しません。</em></p>

<div class="fig">
<p class="cap">図：膨張則を変えると、因果的に切れたノードの数がどう変わるか。<strong>\(p\to1\) でパッチ数が 1 に落ち、合意すべきビットがゼロになります</strong>。灰色の帯が、観測が示す膨張則（対数平均 \(p=0.513\)）の位置</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>膨張則の指数 \(p\)<input id="sp" type="range" min="300" max="999" value="513" step="1"></label>
  <span class="val" id="vp">p = 0.513</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#7a4a2a"></i>因果的に切れたノードの数</span>
  <span><i class="swatch" style="background:#2a5a7a"></i>合意すべきビット数</span>
  <span><i class="swatch" style="background:#a8968a"></i>観測の対数平均（\(p=0.513\)）</span>
</div>
</div>

<h2><span class="n">06</span>ただし、放射を入れると壊れる</h2>

<p>前シリーズ番外編②で、この売りは一度潰れています。おさらいします ── <strong>放射は共形不変なのでディラトンと結合できず、\(\rho_r\propto a^{-4}\) のまま</strong>。すると総和を乗っ取る時期が来ます。</p>

<div class="calc">
<span class="tag">いつ乗っ取られるか</span>
$$\sqrt{\Omega_r}=9.6\times10^{-3}\qquad\Longrightarrow\qquad z>103\ \text{で放射が支配}$$
</div>

<p>再結合（\(z=1100\)）は完全にこの内側です。だから<strong>\(a\propto t\) は再結合より前には成立できず、パッチ数は \(1.2\times10^4\) に戻ります</strong> ── \(\Lambda\)CDM とほぼ同じ深刻さで、地平線問題が復活する。<em>唯一の売りが、いちばん必要な時期に効かない。</em></p>

<div class="aside">
<span class="tag">これが番外編②の「縛る相手を間違えていた」の中身</span>
\(c\cdot t=\text{一定}\) は共動ハッブル半径（＝アドレス空間）を固定する唯一の膨張則でした。ところがそれは<strong>共形因子への条件</strong>＝帳簿への条件です。放射は共形不変なので、帳簿をいくら縛っても放射には触れられない ── <em>そして初期宇宙を支配するのは、まさにその放射</em>。前シリーズの結論「縛るべきだったのは光シート上の情報量」は、第20回で正面から扱います。
</div>

<h2><span class="n">07</span>インフレーションは、合意ではなく複製で解いている</h2>

<p>標準的な解も、情報の言葉に直しておきます。インフレーションは約 60 e-fold の指数膨張で、これを分散システムの用語にすると ──</p>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>合意（consensus）ではない</strong><span>ノード同士が通信して値を揃えるのではない</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>ブロードキャスト＋分割（複製）</strong><span>1 台のノードの状態を \(e^{60}=10^{26}\) 倍の体積にコピーしてから、切り離す。<em>揃っているのは、もともと同じものだったから</em></span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>\(c\cdot t=\)一定 は通信で解く</strong><span>粒子的地平線が無限なので、どの二点も過去のどこかで通信できていた ── ただし 06節のとおり、放射があると成立しない</span></div></div>
</div>

<p><strong>二つの解法は、分散システムでは完全に別のもの</strong>です。一方は「同じ初期状態をコピーする」、もう一方は「通信して合わせる」。<em>そして観測は、どちらが起きたかを直接には区別しません</em> ── 区別できるのは、揺らぎのスペクトル（\(n_s\)）のような二次的な予言だけです。</p>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① パッチ数 9600 は、共動地平線 288 Mpc と最終散乱面まで 14100 Mpc から出した見積もりです。</strong> どちらも \(\Lambda\)CDM の標準値で、「因果的パッチ」の定義（粒子的地平線か音響地平線か、円板か球冠か）によって数字は数倍動きます ── よく引かれる「\(10^4\)〜\(10^5\) 個」の幅は、この定義の違いによるものです。</p>
<p style="margin:0 0 10px"><strong>② 「17 ビットの合意」は、\(\Delta T/T\sim10^{-5}\) を素朴に対数へ直したものです。</strong> 実際の CMB のゆらぎは<em>ランダムではなく構造を持って</em>いて（音響振動）、\(10^{-5}\) は双極子を除いた rms です。「独立な 17 ビットが揃っている」という言い方は<strong>比喩の域を出ません</strong> ── 情報量として正確に数えるには、多重極ごとの相関を扱う必要があります。</p>
<p style="margin:0 0 10px"><strong>③ 04節の「偶然の確率 \(10^{-48000}\)」は、各パッチが独立ランダムだと仮定した場合の値です。</strong> これは<em>帰無仮説がどれだけ馬鹿げているかを示すための計算</em>であって、そんな仮説を誰も立てていません。桁を実感するためのものと読んでください。</p>
<p style="margin:0 0 10px"><strong>④ 05節の表は \(a\propto t^p\) を全時代に適用した粗い見積もりです。</strong> \(\chi\propto t^{1-p}\) の係数や、再結合の時刻が \(p\) に依存して動くことは無視しています。桁の議論です。</p>
<p style="margin:0"><strong>⑤ インフレーションを「複製」と呼ぶのは本稿の言い方です。</strong> 標準的には「因果的接触にあった小領域が指数的に引き伸ばされた」と表現されます ── 中身は同じですが、<em>分散システムの用語に翻訳したのは本稿の整理</em>であり、標準的な定式化ではありません。またインフレーションには地平線問題の解決以外に、平坦性・単極子・ゆらぎのスペクトルという独立した動機と予言があります。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>\(\Delta T/T\sim10^{-5}\) は何ビットの一致か。
<details><summary>答えを見る</summary><div class="ans">\(\log_2(10^5)=16.6\) ビット。<em>「揃っている」を数えられる量に翻訳する</em>と、こうなります。</div></details></li>

<li>因果的パッチの数を、地平線角から求めよ。
<details><summary>答えを見る</summary><div class="ans">\(\theta=288/14100=0.0204\) rad。立体角 \(2\pi(1-\cos\theta)=1.31\times10^{-3}\) sr。全天 \(4\pi\) を割って <strong>\(9.6\times10^3\)</strong> 個。</div></details></li>

<li>合意している情報の総量は。それは多いか。
<details><summary>答えを見る</summary><div class="ans">\(9.6\times10^3\times16.6=1.6\times10^5\) ビット ＝ 約 <strong>20 KB</strong>。まったく多くありません ── <em>問題は量ではなく、送る手段（チャネル）がゼロだったこと</em>です。</div></details></li>

<li>\(a\propto t\) でパッチ数が 1 になるのはなぜか。
<details><summary>答えを見る</summary><div class="ans">共動の粒子的地平線 \(\chi=\int c\,dt/a\propto\int dt/t=\ln t\) が、\(t\to0\) で<strong>発散する</strong>から（前シリーズ番外編③の特徴づけ⑤）。どの二点も過去のどこかで通信できていたので、合意すべきビットはゼロです。</div></details></li>

<li>（やや難）インフレーションと \(c\cdot t=\text{一定}\) は、分散システムとしてどう違うか。
<details><summary>答えを見る</summary><div class="ans">インフレーションは<strong>ブロードキャスト＋分割（複製）</strong> ── 1 台の状態を \(e^{60}\) 倍の体積にコピーしてから切り離す。揃っているのは「もともと同じもの」だから。\(c\cdot t=\text{一定}\) は<strong>通信</strong> ── 粒子的地平線が無限なので、どの二点も過去に信号を交換できた。<em>分散システムでは完全に別の解法</em>ですが、CMB の一様性だけでは区別できません（区別は \(n_s\) などの二次的な予言で）。なお \(c\cdot t=\text{一定}\) 側は、放射を入れると 06節のとおり成立しません。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　問題は量ではなく、チャネルの不在だった</h2>
<p>地平線問題を情報の言葉に直しました。\(\Delta T/T\sim10^{-5}\) は <strong>16.6 ビットの一致</strong>、因果的に切れた領域は <strong>9600 台</strong>（共動地平線 288 Mpc ÷ 最終散乱面まで 14100 Mpc）。掛けると <strong>約 20 キロバイト</strong> ── <em>スマホなら一瞬で送れる量です</em>。</p>
<p>だから問題の形が変わります。<strong>揃っていること自体は大した情報量ではない。あり得ないのは、通信路がゼロなのに揃っていること</strong> ── チャネルの不在です。偶然という選択肢は \(10^{-48000}\) で完全に消えます。</p>
<p>そして \(c\cdot t=\text{一定}\) は、この問題を原理的に持ちません。粒子的地平線が \(\ln t\) で発散するので、<strong>パッチは 1 個、合意すべきビットはゼロ</strong>。膨張則を \(p=0.5\) から \(1\) へ動かすと、パッチ数は \(3.6\times10^4\) から 1 へ落ちます。── <em>ただし放射を入れると壊れます</em>。放射は共形不変でディラトンと結合できず、\(z>103\) で総和を乗っ取る。再結合はその内側なので、\(a\propto t\) は成立できず、パッチ数は \(1.2\times10^4\) に戻る。<strong>唯一の売りが、いちばん必要な時期に効かない</strong>（番外編②）。</p>
<p>標準的な解も翻訳しておきました。インフレーションは<strong>合意ではなく複製</strong>です ── 1 台のノードの状態を \(e^{60}=10^{26}\) 倍の体積にコピーしてから切り離す。揃っているのは、もともと同じものだったから。<em>分散システムでは「通信して合わせる」と「同じものをコピーする」は完全に別の解法</em>ですが、CMB の一様性だけでは区別できません。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第18回</span>
通信の次は<strong>アドレッシング</strong>です。宇宙の空間セルは \((R_H/\ell_P)^3=5.3\times10^{182}\) 個あるのに、書けるビットは \(3\times10^{122}\)。比はちょうど \(1/(R_H/\ell_P)\) ── つまり<strong>ホログラフィーとは「セルの \(10^{-61}\) にしか番地が振れない」ということ</strong>だ、という読み方をします。第6回で「使用率 \(10^{-18}\)」を数えましたが、今回はもっと根本的な不足です ── <em>使っていないのではなく、そもそも番地が足りない。</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sp=document.getElementById('sp'), vp=document.getElementById('vp'), ro=document.getElementById('ro');
  var X0=78, X1=690, Y0=32, Y1=310;
  var R=3.628e4;                        // t0/t_rec
  var BITS=16.61;
  var xmin=0.30, xmax=1.0;
  var ymin=0, ymax=5.2;                 // log10(パッチ数)

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function patches(p){ return (p>=0.999)?1:Math.pow(R,2*(1-p)); }

  function draw(){
    var p=parseInt(sp.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    // 観測の帯
    g.fillStyle='#f3ede8';
    g.fillRect(px(0.50), Y0, px(0.53)-px(0.50), Y1-Y0);
    g.fillStyle='#a8968a'; g.textAlign='center';
    g.fillText('観測（対数平均）', px(0.515), Y0-8);

    g.textAlign='right';
    for(var e=0;e<=5;e++){
      var y=py(e);
      g.strokeStyle=(e===0?'#d8c8bc':'#f6f0eb'); g.lineWidth=(e===0?1.6:1);
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a89286'; g.fillText(e===0?'1 台':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    [0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0].forEach(function(v){
      var x=px(v);
      g.strokeStyle='#faf6f3'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a89286'; g.fillText(v.toFixed(1), x, Y1+16);
    });
    g.strokeStyle='#d4c2b4'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // パッチ数
    g.strokeStyle='#7a4a2a'; g.lineWidth=3.4; g.beginPath();
    for(var i=0;i<=300;i++){
      var q=xmin+(xmax-xmin)*i/300;
      var y=Math.log(patches(q))/Math.LN10;
      if(i===0) g.moveTo(px(q),py(Math.min(y,ymax))); else g.lineTo(px(q),py(Math.min(y,ymax)));
    }
    g.stroke();

    // 合意すべきビット（同じ形、係数だけ違うので破線で）
    g.strokeStyle='#2a5a7a'; g.lineWidth=2.2; g.setLineDash([6,4]); g.beginPath();
    for(var i=0;i<=300;i++){
      var q=xmin+(xmax-xmin)*i/300;
      var v=patches(q)*BITS;
      var y=Math.log(v)/Math.LN10;
      if(i===0) g.moveTo(px(q),py(Math.min(y,ymax))); else g.lineTo(px(q),py(Math.min(y,ymax)));
    }
    g.stroke(); g.setLineDash([]);

    // p=1 の点
    g.fillStyle='#7a4a2a';
    g.beginPath(); g.arc(px(1.0),py(0),6,0,6.2832); g.fill();
    g.strokeStyle='#fff'; g.lineWidth=2;
    g.beginPath(); g.arc(px(1.0),py(0),6,0,6.2832); g.stroke();
    g.fillStyle='#7a4a2a'; g.textAlign='right';
    g.fillText('a ∝ t：1 台・0 ビット', px(1.0)-12, py(0)-10);

    // カーソル
    g.strokeStyle='#8a6a52'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(p),Y0); g.lineTo(px(p),Y1); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#8a7565'; g.textAlign='center';
    g.fillText('膨張則の指数  p　（a ∝ t^p）', (X0+X1)/2, Y1+38);

    var N=patches(p), B=N*BITS;
    vp.textContent='p = '+p.toFixed(3);
    ro.textContent='p = '+p.toFixed(3)+
      '　→　因果的に切れたノード '+(N<10?N.toFixed(1):N.toExponential(2))+' 台'+
      '　／　合意すべき情報 '+(B<8?B.toFixed(1)+' ビット':(B/8<1024? (B/8).toPrecision(3)+' バイト' : (B/8/1024).toPrecision(3)+' KB'))+
      (p>0.999?'　★ 地平線問題が原理的に発生しない':'');
  }
  sp.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-17-consensus.html', acc='#7a4a2a', ops='#2a5a7a',
      title='一度も通信していない 9600 台が、17ビット合意している ── わかる c·t=一定 第17回',
      ep='第 17 回 ／ 第 III 部のはじまり ── 情報として測る',
      eyebrow='地平線問題を、分散システムの言葉で書き直します',
      h1='一度も通信していない<br>9600 台が、17ビット合意している',
      sub='合意に必要だった情報は、たった 20 キロバイト。<br><em>問題は量ではなく、送る手段が無かったこと ── チャネルの不在です。</em>',
      byline_l='必要な道具：対数、立体角、割り算',
      byline_r='\\(9.6\\times10^3\\ \\text{台}\\times16.6\\ \\text{ビット}=20\\ \\mathrm{KB}\\)',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第17回、物理好きの高校生・大学生向け読み物です。CMB の温度ゆらぎが \\(\\Delta T/T\\sim10^{-5}\\)（双極子を除いた rms）であること、再結合時の共動粒子的地平線が約 288 Mpc、最終散乱面までの共動距離が約 14100 Mpc であることは \\(\\Lambda\\)CDM の標準値です。本稿のパッチ数 \\(9.6\\times10^3\\)、合意ビット \\(1.6\\times10^5\\)（約 20 KB）、および膨張則ごとのパッチ数の表は本稿での計算です（kenshou/calc21.py）。<strong>「因果的パッチ」の定義（粒子的地平線か音響地平線か、円板か球冠か）によって数字は数倍動き</strong>、文献でよく引かれる「\\(10^4\\)〜\\(10^5\\) 個」の幅はこの違いによります。<strong>「17 ビットの合意」は \\(10^{-5}\\) を素朴に対数へ直した比喩であり</strong>、実際の CMB のゆらぎは音響振動という構造を持つため、情報量として正確に数えるには多重極ごとの相関を扱う必要があります。04節の \\(10^{-48000}\\) は各パッチが独立ランダムという（誰も立てていない）帰無仮説のもとでの値で、桁を実感するための計算です。05節の表は \\(a\\propto t^p\\) を全時代に適用した粗い見積もりで、係数や再結合時刻の \\(p\\) 依存性は無視しています。\\(a\\propto t\\) で粒子的地平線が発散することは前シリーズ番外編③の特徴づけ⑤、放射が共形不変ゆえディラトンと結合できず \\(z>103\\) で支配的になることは同番外編②によります。インフレーションを「ブロードキャスト＋分割（複製）」と呼ぶのは本稿の翻訳で、標準的な定式化ではありません ── またインフレーションには平坦性・単極子・ゆらぎのスペクトルという独立した動機と予言があります。線形膨張（\\(c\\cdot t=\\)一定、\\(R_h=ct\\)）は検証途上の少数派モデルで、初期宇宙まで外挿した場合は元素合成と矛盾します（Lewis, Barnes &amp; Kaushik 2016）。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーで膨張則を変え、p→1 でノードが 1 台に落ちる様子が見えます。「答えを見る」で解答が開きます。')
