# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">番外編④で、驚き・自然さ・数値の一致が<strong>「正準な測度はあるか」</strong>という一つの問いに潰れました。番外編③はそれに「コンパクトなら Haar、非コンパクトなら無い」と答えましたが ── <em>それは粗すぎました</em>。<strong>群の対称性以外にも、測度を配る仕組みがあります。</strong> そしてその先で、標準模型の三大微調整問題が<em>偽陽性ゼロで当たります</em>。</p>

<h2><span class="n">01</span>くりこみ群は、測度を配る</h2>

<div class="calc">
<span class="tag">1 次元の流れ \(dg/dt=\beta(g)\) で、流れに対して不変な測度</span>
$$\frac{d}{dt}\int\rho\,dg=0
\iff \frac{d(\rho\beta)}{dg}=0
\iff \rho\beta=\text{一定}
\iff \boxed{\rho\propto\frac1\beta}$$
<p class="lbl">規格化を除いて<strong>一意</strong>。そして \(\int dg/\beta\) は <strong>RG 時間</strong>そのもの</p>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0"><strong>「事前確率 ＝ その値の近くで理論が過ごす RG 時間」</strong>。<br>
── これは選択ではありません。<em>流れの不変測度は一意</em>だからです。</p>
</div>

<h2><span class="n">02</span>なぜ RG 不変でなければならないのか</h2>

<div class="seven">
<div class="row"><div class="mk">?</div><div class="txt"><strong>パラメータの値は、どのスケールで言うかで変わる</strong><span>第37回 ── \(\alpha\) は \(M_Z\) で 128、低エネルギーで 137</span></div></div>
<div class="row"><div class="mk">!</div><div class="txt"><strong>判定がスケールで変わるなら、判定は規約に依存している</strong><span>第3回：<em>規約で変わる答えは、答えではない</em></span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>だから事前分布は、RG 不変でなければならない</strong><span>そして 01節より、それは <em>一意に決まる</em></span></div></div>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>スケール</th><th class="mid">\(\alpha_s\)</th><th class="mid">一様な事前での「不自然さ」</th></tr></thead>
<tbody>
<tr><th>1 GeV あたり</th><td class="mid">\(0.500\)</td><td class="mid">\(1.00\) bit</td></tr>
<tr><th>\(m_b\) あたり</th><td class="mid">\(0.214\)</td><td class="mid">\(2.22\) bit</td></tr>
<tr><th>\(M_Z\)</th><td class="mid">\(0.118\)</td><td class="mid">\(3.08\) bit</td></tr>
<tr class="hi"><th>\(M_{\rm Planck}\)（1 ループ外挿）</th><td class="mid">\(0.0191\)</td><td class="mid"><strong>\(5.71\) bit</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>同じ理論の同じ結合が、スケールを変えるだけで 4.71 ビット動きます。</strong> <em>一様な事前は RG 不変ではない ── だから判定として使えません。</em></p>

<h2><span class="n">03</span>測度の形は、\(\beta\) の形だけで決まる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(\beta\) の形</th><th class="mid">\(dg/\beta\)</th><th class="mid">誘導される測度</th><th class="mid">値段</th></tr></thead>
<tbody>
<tr><th class="mid">\(\beta=0\)</th><td class="mid">縮退</td><td class="mid">群に戻る（Haar）</td><td class="mid">場合による</td></tr>
<tr class="hi"><th class="mid">\(\beta\propto g\)（乗法的）</th><td class="mid">\(dg/g\)</td><td class="mid"><strong>対数一様</strong></td><td class="mid"><strong>安い</strong></td></tr>
<tr><th class="mid">\(\beta\propto g^2\)</th><td class="mid">\(dg/g^2\)</td><td class="mid">\(1/g^2\) 重み</td><td class="mid">安い</td></tr>
<tr class="hi"><th class="mid">\(\beta=\)一定（加法的）</th><td class="mid">\(dg\)</td><td class="mid"><strong>線形</strong></td><td class="mid"><strong>高い</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">03節の結論</p>
<p style="margin:6px 0 0">そして <strong>\(\beta\propto g\) になるのは、\(g=0\) で対称性が増えるときだけ</strong>です ──<br>
\(g=0\) に対称性があれば \(g\) は自分に比例してしか生成されず、無ければ他の質量から加法的に生成される。<br>
── <em>これは 't Hooft の自然性の基準そのもの。</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>核心 ── 標準模型の全 20 パラメータを、\(\beta\) の形だけで採点する</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>パラメータ</th><th class="mid">個数</th><th class="mid">\(\beta\) の形</th><th class="mid">守る対称性</th><th class="mid">値段</th><th class="mid">実際の扱われ方</th></tr></thead>
<tbody>
<tr><th>ゲージ結合 \(g_1,g_2,g_3\)</th><td class="mid">3</td><td class="mid">\(\propto g^3\)（乗法的）</td><td class="mid">ゲージ対称性</td><td class="mid">安い</td><td class="mid">問題視されない</td></tr>
<tr><th>湯川結合</th><td class="mid">9</td><td class="mid">\(\propto y\)（乗法的）</td><td class="mid"><strong>カイラル対称性</strong></td><td class="mid">安い</td><td class="mid">'t Hooft の原例</td></tr>
<tr><th>CKM の 3 角 ＋ 1 位相</th><td class="mid">4</td><td class="mid">乗法的・コンパクト</td><td class="mid">コンパクト</td><td class="mid">安い</td><td class="mid">\(\theta_{13}\) だけ 8.8 bit</td></tr>
<tr><th>ヒッグス四点結合 \(\lambda\)</th><td class="mid">1</td><td class="mid">\(\supset-6y_t^4\)（<strong>加法的</strong>）</td><td class="mid">無し</td><td class="mid"><strong>要注意</strong></td><td class="mid">→ 真空の準安定性</td></tr>
<tr class="hi"><th>ヒッグス質量\(^2\) \(m^2\)</th><td class="mid">1</td><td class="mid">\(\supset M^2\)（新物理あれば）</td><td class="mid">無し</td><td class="mid"><strong>高い</strong></td><td class="mid"><strong>階層性問題</strong></td></tr>
<tr class="hi"><th>\(\theta_{\rm QCD}\)</th><td class="mid">1</td><td class="mid">\(\beta=0\)</td><td class="mid">コンパクトのみ</td><td class="mid"><strong>高い</strong></td><td class="mid"><strong>強い CP 問題</strong></td></tr>
<tr class="hi"><th>宇宙定数 \(\Lambda\)</th><td class="mid">1</td><td class="mid">\(\supset m^4\)（<strong>加法的</strong>）</td><td class="mid">無し</td><td class="mid"><strong>高い</strong></td><td class="mid"><strong>宇宙定数問題</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0"><strong>\(\beta\) の構造だけで採点して「高い」が出たのは 3 個。</strong><br>
それは<strong>階層性・強い CP・宇宙定数</strong> ── <em>既知の三大微調整問題そのもの</em>。<br>
── <strong>20 例で 3 つ当てて、偽陽性ゼロ、偽陰性ゼロ。</strong><br>
そして \(\lambda\) の「要注意」も外れではありません ── <em>真空の準安定性という別種の問題を、正しく引っかけています。</em></p>
</div>

<div class="fig">
<p class="cap">図：20 個のパラメータを、\(\beta\) の形で並べたもの。<strong>左が乗法的（対数測度・安い）、右が加法的またはゼロ（線形・Haar・高い）</strong>。ツマミで「新物理をどこに置くか」を動かしてください ── <em>ヒッグス質量だけが、置いた瞬間に左から右へ飛びます</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>新物理のスケール \(\log_{10}(M/\text{GeV})\)<input id="sn" type="range" min="3" max="19" value="19" step="1"></label>
  <span class="val" id="vn">19</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a4a"></i>乗法的（対数測度）── 安い</span>
  <span><i class="swatch" style="background:#8a3a3a"></i>加法的・\(\beta=0\) ── 高い</span>
</div>
</div>

<h2><span class="n">05</span>残った自由度は、物理の問いに化ける</h2>

<div class="seven">
<div class="row"><div class="mk">?</div><div class="txt"><strong>\(\int dg/\beta\) は固定点で発散する</strong><span>\(\beta\to0\) なので、範囲を切る必要が残る</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>ところがその切り口は恣意的ではない</strong><span><em>「理論がどこまで有効か」</em>── つまり新物理がどこに入るか</span></div></div>
<div class="row"><div class="mk">→</div><div class="txt"><strong>そしてそれこそが、階層性問題があるかどうかを決める当のもの</strong><span>04節の \(m^2\) の行 ── <em>事前分布に残った唯一の自由度が、物理の問いと一致した</em></span></div></div>
</div>

<h2><span class="n">06</span>七度目と八度目の圧縮</h2>

<div class="calc">
<span class="tag">七度目</span>
$$\underbrace{\text{第48回「事前に理由があるか」}}_{\text{基準}}
=\underbrace{\text{番外編③「コンパクトか」}}_{\text{定理}}
=\underbrace{\text{「}\beta\text{ が乗法的か」}=\text{「}g=0\text{ に対称性があるか」}}_{\textbf{機構}}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>\(\theta_{\rm QCD}\) の三つの顔</th><th class="mid">帰結</th></tr></thead>
<tbody>
<tr><th>\(\beta=0\) だから走らない</th><td class="mid">RG は測度を配れない</td></tr>
<tr><th>走らないから RG 不変</th><td class="mid">独立な入力で唯一の定数（番外編③）</td></tr>
<tr class="hi"><th>角度だからコンパクト</th><td class="mid">Haar 測度だけが使える</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">06節の結論 ── 八度目の圧縮</p>
<p style="margin:6px 0 0"><strong>三つは独立な事実ではなく、\(\beta=0\) という一つの事実の三つの顔でした。</strong><br>
── そして「唯一の争いなき微調整問題」であることも、同じ一つの理由から出ます。</p>
</div>

<h2><span class="n">07</span>自分の逃げ道を、二つ塞ぐ</h2>

<div class="seven">
<div class="row"><div class="mk">③</div><div class="txt"><strong>番外編③の訂正：非コンパクトでも RG が測度を配る</strong><span>測度が無いのは \(\beta=0\) かつ非コンパクトのときだけで、<em>標準模型にその例は無い</em> ── <strong>自然さは思ったより well-posed でした</strong></span></div></div>
<div class="row hi"><div class="mk">48</div><div class="txt"><strong>第48回の訂正：\(\rho_\Lambda\) の \(\beta\) は \(m^4\) が加法的</strong><span>だから<em>正準な測度は線形</em>であって対数一様ではない ── <strong>408 ビットが正しい答え。宇宙定数問題は逃げ場のない危機</strong></span></div></div>
<div class="row"><div class="mk">!</div><div class="txt"><strong>「事前次第で 400 ビット動く」は、正準な測度を知らなかったから出ていた</strong><span>── <em>自分の作った逃げ道を、自分で塞いだ</em></span></div></div>
</div>

<div class="aside">
<span class="tag">番外編②は無事か ── 頑健性の検査</span>
\(\log_2B\) の値：<strong>一様測度 8.67、RG 測度 8.66</strong> ── <em>0.01 ビットしか違いません</em>。<br>
（対数一様だけが 11.46 とずれますが、それも同じ桁。）<strong>圧縮則は測度の選び方に依存しませんでした。</strong>
</div>

<h2><span class="n">08</span>この見方で、新しく言えること</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>模型</th><th class="mid">見るべきもの</th><th class="mid">帰結</th></tr></thead>
<tbody>
<tr><th>新しいスカラーを足す</th><td class="mid">その質量の \(\beta\) に加法項が出るか</td><td class="mid">出れば新しい階層性問題を作る</td></tr>
<tr class="hi"><th>超対称性</th><td class="mid">ボーズ・フェルミの相殺で加法項が消える</td><td class="mid"><strong>だから階層性問題を解く</strong></td></tr>
<tr><th>アクシオン</th><td class="mid">\(\theta\) に \(\beta\) を与えて動かす</td><td class="mid">\(\beta=0\) の縮退を破って解く</td></tr>
<tr class="hi"><th>宇宙定数のあらゆる機構</th><td class="mid">\(m^4\) の加法項をどう消すか</td><td class="mid"><strong>まだ誰も消せていない</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">08節の結論</p>
<p style="margin:6px 0 0"><strong>超対称性が階層性問題を「解く」とは、\(\beta\) の加法項を消して、線形測度を対数測度に戻すことでした</strong>（408 → 約 7 ビット）。<br>
── <em>模型を見て \(\beta\) を書けば、微調整問題があるかどうかがその場で決まります。</em></p>
</div>

<div class="caveat">
<span class="tag">正直な線 ── そして、埋まっていない穴</span>
<p style="margin:0 0 10px"><strong>① 01節の一意性は、1 次元の流れについてのみです。</strong> 多次元では不変測度は一意ではありません（\(\nabla\!\cdot\!(\rho\beta)=0\) を満たす \(\rho\) は無数にある）── ゲージ結合は 1 ループで独立に走るので 1 次元が使えますが、<em>全パラメータには効きません</em>。ここは本稿のいちばん技術的な弱点です。</p>
<p style="margin:0 0 10px"><strong>② \(\beta\) はスキームに依存します</strong>（第35回で漸近安全性について書いたのと同じ弱点）。<em>乗法的か加法的かという構造はスキームに依りませんが、係数は依ります</em>。</p>
<p style="margin:0 0 10px"><strong>③ 07節の「\(\rho_\Lambda\) は線形が正準」は、物理として決着しているとは言いがたい主張です。</strong> 次元正則化では \(m^4\) 項の現れ方が違い、<em>繰り込み条件の取り方にも依ります</em> ── ここを疑う人は、第48回の「どちらとも言えない」に戻ることになります。</p>
<p style="margin:0 0 10px"><strong>④ 04節の採点表は、't Hooft の自然性を測度の言葉で言い直したものです。</strong> <em>物理は既知</em>で、新しいのは「事前分布の問題として閉じた」という読み方だけ ── そして 20 例という標本は小さく、「三大問題」という区分自体が文献の慣習です。</p>
<p style="margin:0"><strong>⑤ そして、いちばん大きな穴。</strong> 02節で「事前分布は RG 不変でなければならない」とは言えました。しかし ── <em><strong>測度があることと、それが確率であることは別</strong></em>です。「長く過ごす値はありそう」という読み替えは自然ですが、<strong>証明していません</strong>。ここは埋まっていません。同じ要求から統計学の Jeffreys 事前が導かれるので孤立した主張ではありませんが、<em>それも一つの立場</em>です。</p>
</div>

<div class="prob">
<p class="lbl">練習問題</p>
<ol>
<li>なぜ事前分布は RG 不変でなければならないのか。
<details><summary>答えを見る</summary><div class="ans"><strong>そうでないと、判定がスケールで変わるから</strong>です。一様な事前で \(\alpha_s\) を評価すると、1 GeV で 1.00 bit、\(M_{\rm P}\) で 5.71 bit ── <em>同じ結合が 4.71 ビット動きます</em>。第3回：<strong>規約で変わる答えは、答えではありません。</strong></div></details></li>

<li>RG 不変な測度はいくつあるか。
<details><summary>答えを見る</summary><div class="ans">1 次元の流れなら <strong>ただ一つ</strong>：\(\rho\beta=\)一定、つまり \(\rho\propto1/\beta\)。それは \(\int dg/\beta=\) <em>RG 時間</em>そのものです。── ただし①のとおり、<strong>多次元では一意ではありません</strong>。</div></details></li>

<li>\(\beta\) の形と値段の対応は。
<details><summary>答えを見る</summary><div class="ans"><strong>\(\beta\propto g\)（乗法的）→ 対数測度 → 安い。\(\beta=\)一定（加法的）→ 線形測度 → 高い。\(\beta=0\) → 群に戻る。</strong> そして \(\beta\propto g\) になるのは <em>\(g=0\) で対称性が増えるときだけ</em> ── <strong>'t Hooft の基準そのもの</strong>です。</div></details></li>

<li>20 個を採点すると、何個が「高い」に出るか。
<details><summary>答えを見る</summary><div class="ans"><strong>3 個</strong> ── \(m^2\)（新物理あり）、\(\theta_{\rm QCD}\)、\(\Lambda\)。それは<em>階層性・強い CP・宇宙定数</em>、既知の三大問題そのもので、<strong>偽陽性ゼロ、偽陰性ゼロ</strong>。\(\lambda\) の「要注意」も真空の準安定性を正しく引っかけています。</div></details></li>

<li>（やや難）本稿でいちばん埋まっていない穴は。
<details><summary>答えを見る</summary><div class="ans"><strong>測度があることと、それが確率であることは別だ、という点</strong>です。RG 不変性から測度が一意に決まることは示せましたが、<em>「長く過ごす値はありそう」と読み替えてよい理由は証明していません</em>。ここが崩れると 04節以降が全部崩れます。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　事前分布は、選ぶものではなかった</h2>
<p>1 次元の流れ \(dg/dt=\beta(g)\) で、流れに不変な測度は <strong>\(\rho\propto1/\beta\) のただ一つ</strong>。それは <strong>RG 時間</strong>そのものです。そして<em>なぜ RG 不変でなければならないか</em>も言えました ── <strong>判定がスケールで変わるなら、それは規約に依存していて、答えではないから</strong>（第3回）。実際、一様な事前だと \(\alpha_s\) の「不自然さ」は <strong>4.71 ビット</strong>も動きます。</p>
<p>測度の形は \(\beta\) の形だけで決まります ── <strong>乗法的なら対数測度で安く、加法的なら線形測度で高い</strong>。そして \(\beta\propto g\) になるのは \(g=0\) に対称性があるときだけ、つまり <em>'t Hooft の基準そのもの</em>でした。</p>
<p>そこで標準模型の <strong>全 20 パラメータを \(\beta\) の形だけで採点</strong>すると ── 「高い」が出たのは <strong>3 個だけ</strong>。<em>階層性・強い CP・宇宙定数</em>、既知の三大問題そのもので、<strong>偽陽性ゼロ、偽陰性ゼロ</strong>でした。\(\lambda\) の「要注意」も、真空の準安定性という別種の問題を正しく引っかけています。</p>
<p>残った自由度（積分範囲）も恣意的ではありませんでした ── それは<strong>「理論がどこまで有効か」</strong>、つまり新物理がどこに入るかで、<em>それこそが階層性問題の有無を決める当のもの</em>です。<strong>事前分布に残った唯一の自由度が、物理の問いと一致しました。</strong></p>
<p>そして自分の逃げ道を二つ塞ぎました。番外編③の「非コンパクトなら ill-posed」は粗すぎ ── <strong>自然さは思ったより well-posed</strong>でした。第48回の「事前次第で 400 ビット動く」も ── <strong>\(\rho_\Lambda\) の \(\beta\) は加法的なので正準な測度は線形、408 ビットが正しい答え。宇宙定数問題は逃げ場のない危機</strong>です。</p>
<p>ただし ── <em>測度があることと、それが確率であることは別</em>。そこは、まだ埋まっていません。</p>
</div>

<div class="next">
<span class="lbl">おわりに ── 五つの番外編で分かったこと</span>
①：<strong>質量の変化が普遍的かどうかなら測れる</strong>（\(\mu\)、23.3 ビット）＋ クォーク質量方向に 10.2 ビットの縮退。<br>
②：<strong>階層は自分の対数まで縮む</strong>（\(B\to\log_2B\)、頑健性は⑤で確認）。<br>
③：<strong>0 の列は一様ではなく、定数はほとんど残らない</strong>（残るのは \(\theta_{\rm QCD}\) ただ一つ）。<br>
④：<strong>4.1 ビットの予言が 15.7 ビットの発見に勝つ</strong> ── 「理論が先」とは測度を先に固定すること。<br>
⑤：<strong>その測度は、くりこみ群が配っていた</strong> ── \(\beta\) の形だけで三大問題が当たる。<br>
── 五つとも、本編第3回の一つの手続きの上に立っています。そして③⑤では、その手続きが<em>自分の作った基準を二つ削り、逃げ道を二つ塞ぎました</em>。<strong>道具は、まだ働いています。</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sn=document.getElementById('sn'), vn=document.getElementById('vn'), ro=document.getElementById('ro');
  var X0=60, X1=690, Y0=48, MID=375;

  // [ラベル, 個数, 常に安い?]
  var LEFT=[['ゲージ結合 g₁,g₂,g₃',3],['湯川結合 9 個',9],['CKM 3角+1位相',4]];
  var RIGHT=[['λ（要注意）',1],['θ_QCD',1],['宇宙定数 Λ',1]];

  function draw(){
    var M=parseInt(sn.value,10);
    var higgsRight = (M < 19);      // 新物理がプランク未満にあれば加法項が出る
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    g.strokeStyle='#cdc8d2'; g.lineWidth=1.6;
    g.beginPath(); g.moveTo(MID,Y0-20); g.lineTo(MID,300); g.stroke();
    g.textAlign='center';
    g.font='13px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillStyle='#2a5a4a'; g.fillText('乗法的 → 対数測度 → 安い', (X0+MID)/2, Y0-26);
    g.fillStyle='#8a3a3a'; g.fillText('加法的・β=0 → 高い', (MID+X1)/2, Y0-26);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    var y=Y0+6;
    for(var i=0;i<LEFT.length;i++){
      g.fillStyle='#2a5a4a'; g.globalAlpha=0.88;
      g.fillRect(X0+16, y, MID-X0-40, 30); g.globalAlpha=1;
      g.fillStyle='#fff'; g.textAlign='left';
      g.fillText(LEFT[i][0]+'（'+LEFT[i][1]+'）', X0+26, y+19);
      y+=38;
    }
    // ヒッグス質量²：位置が動く
    var hx = higgsRight ? MID+16 : X0+16;
    var hw = higgsRight ? (X1-MID-40) : (MID-X0-40);
    g.fillStyle = higgsRight ? '#8a3a3a' : '#2a5a4a';
    g.globalAlpha=0.95; g.fillRect(hx, y, hw, 30); g.globalAlpha=1;
    g.fillStyle='#fff'; g.textAlign='left';
    g.fillText('ヒッグス質量² m²（1）'+(higgsRight?'　← 新物理が加法項を作った':''), hx+10, y+19);
    g.strokeStyle='#5a5262'; g.lineWidth=1.4; g.setLineDash([3,3]);
    g.beginPath(); g.moveTo(X0+16, y+15); g.lineTo(X1-16, y+15); g.stroke(); g.setLineDash([]);

    var y2=Y0+6;
    for(var j=0;j<RIGHT.length;j++){
      g.fillStyle='#8a3a3a'; g.globalAlpha=0.88;
      g.fillRect(MID+16, y2, X1-MID-40, 30); g.globalAlpha=1;
      g.fillStyle='#fff'; g.textAlign='left';
      g.fillText(RIGHT[j][0], MID+26, y2+19);
      y2+=38;
    }

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';
    g.fillText('標準模型の 20 パラメータを、ベータ関数の形で分けたもの', (X0+X1)/2, 316);

    vn.textContent=String(M);
    var n_high = 2 + (higgsRight?1:0);
    ro.textContent='新物理を 10^'+M+' GeV に置く　→　「高い」パラメータは '+n_high+' 個'+
      (higgsRight
        ? '　★ 階層性・強い CP・宇宙定数 ── 既知の三大問題が揃った（偽陽性ゼロ）'
        : '　★ 新物理が無ければ、ヒッグス質量は左側 ── 純粋な標準模型に階層性問題は無い');
  }
  sn.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-b5-measure.html', acc='#2a5a4a', ops='#8a3a3a',
      title='番外編⑤：事前分布は、選ぶものではなかった ── わかる c·t=一定',
      ep='番外編 ⑤ ／ 本編完結後の深掘り',
      eyebrow='ベータ関数の形だけで、三大問題が偽陽性ゼロで当たる',
      h1='事前分布は、<br>選ぶものではなかった',
      sub='くりこみ群が測度を配ります ── 流れに不変な測度は、ただ一つ。<br><em>そして自分の作った逃げ道を、二つ塞ぐことになりました。</em>',
      byline_l='必要な道具：第3回の判定、第35回のスキーム依存、第37回の走り、第48回の事前分布、番外編②③④',
      byline_r='20 例で 3 つ ── 偽陽性ゼロ、偽陰性ゼロ',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズの番外編⑤（本編全50話の完結後に書いた深掘り）、物理好きの高校生・大学生向け読み物です。数値は kenshou/calc63.py と calc64.py で計算しています。くりこみ群、流れの不変測度、\'t Hooft の自然性、真空の準安定性はいずれも標準的な内容で、<strong>04節の採点表は \'t Hooft の自然性を測度の言葉で言い直したもの</strong> ── <em>物理は既知</em>で、新しいのは「事前分布の問題として閉じた」という読み方だけです。<strong>01節の一意性は 1 次元の流れについてのみ</strong>で、多次元では不変測度は一意ではありません（ゲージ結合は 1 ループで独立に走るので 1 次元が使えますが、全パラメータには効きません）── ここが本稿のいちばん技術的な弱点です。<strong>\\(\\beta\\) はスキームに依存し</strong>、乗法的か加法的かという構造は不変ですが係数は依ります。<strong>07節の「\\(\\rho_\\Lambda\\) は線形が正準」は物理として決着しているとは言いがたく</strong>、次元正則化では \\(m^4\\) 項の現れ方が違い繰り込み条件にも依ります ── ここを疑えば第48回の「どちらとも言えない」に戻ります。04節の 20 例という標本は小さく、「三大問題」という区分自体が文献の慣習です。<strong>そしていちばん大きな穴</strong>：測度が RG 不変性から一意に決まることは示せましたが、<em>測度があることとそれが確率であることは別</em>で、「長く過ごす値はありそう」という読み替えは<strong>証明していません</strong>（同じ要求から統計学の Jeffreys 事前が導かれるので孤立してはいませんが、それも一つの立場です）。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではツマミで新物理のスケールを動かすと、ヒッグス質量だけが左右を移ります。「答えを見る」で解答が開きます。')
