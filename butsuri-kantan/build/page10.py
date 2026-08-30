# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">前回のフィルタには反例があります。<strong>4 次元の相互作用する理論で、厳密に解けたものが六つ。</strong> ところが並べてみると、全部が<em>一つの定理の裏返し</em>でした。そして分かったのは ── <strong>QCD が厳密に解けないのは、誰も賢くないからではありません。定理の帰結です。</strong></p>

<h2><span class="n">01</span>反例を探す</h2>

<p>前回「相互作用する 3 次元以上で厳密解は前例ゼロ」と書きました。これは言い過ぎです。</p>

<div class="calc">
<span class="tag">計算（kensho/calc05.py ①）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>いつ・誰</th><th>何を</th><th>どこまで</th><th class="mid">何に頼ったか</th></tr></thead>
<tbody>
<tr><th>Seiberg–Witten (1994)</th><td>\(N{=}2\) 超対称ヤン・ミルズ</td><td>低エネルギー有効作用が厳密</td><td class="mid"><strong>超対称</strong></td></tr>
<tr><th>局所化 (2007〜)</th><td>球面上の超対称理論</td><td>分配関数が厳密</td><td class="mid"><strong>超対称</strong></td></tr>
<tr><th>\(N{=}4\) の可積分性</th><td>平面極限の異常次元</td><td>スペクトルが厳密</td><td class="mid"><strong>超対称＋平面＋共形</strong></td></tr>
<tr><th>BES 方程式</th><td>カスプ異常次元 \(\Gamma(g)\)</td><td>全結合で厳密</td><td class="mid">同上</td></tr>
<tr><th>大 \(N\) の \(O(N)\) 模型</th><td>3 次元の臨界指数</td><td>\(1/N\) の各次で厳密</td><td class="mid"><strong>大 \(N\)</strong></td></tr>
<tr class="hi"><th>'t Hooft 模型 (1974)</th><td><strong>2 次元の平面 QCD</strong></td><td>中間子スペクトルが厳密</td><td class="mid"><strong>2 次元＋平面</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">反例はあった。ただし</span>
<p><strong>例外なく、超対称か・大 \(N\) か・平面極限か・2 次元。</strong></p>
<p>そして <em>QCD はそのどれでもありません。</em></p>
</div>

<h2><span class="n">02</span>QCD に足りないものは何か ── 保存量を数える</h2>

<p>「厳密に解ける」を、もう少し正確に言うと <strong>可積分</strong> ということです。可積分とは、<em>方程式の数が未知数と同じだけある</em> ── つまり保存量が十分にある、という意味。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>理論</th><th>保存量</th><th class="mid">個数</th><th class="mid">結果</th></tr></thead>
<tbody>
<tr class="hi"><th>QCD（現実）</th><td>ポアンカレ 10 ＋ フレーバー 8 ＋ バリオン数 1</td><td class="mid"><strong>19 個（有限）</strong></td><td class="mid">解けない</td></tr>
<tr><th>2 次元可積分系</th><td>高スピンの保存流が<strong>無限個</strong></td><td class="mid">\(\infty\)</td><td class="mid"><strong>解ける</strong></td></tr>
<tr><th>\(N{=}4\) 平面極限</th><td>同上（可積分スピン鎖）</td><td class="mid">\(\infty\)</td><td class="mid"><strong>解ける</strong></td></tr>
<tr><th>自由場</th><td>各モードごとに保存量</td><td class="mid">\(\infty\)</td><td class="mid"><strong>解ける</strong></td></tr>
</tbody>
</table>
</div>

<p>分かれ目は、<strong>保存量が無限個あるかどうか</strong>です。ではなぜ QCD に高スピンの保存流を足せないのか。</p>

<h2><span class="n">03</span>足せない ── 定理で禁じられている</h2>

<div class="keybox">
<span class="lbl">コールマン–マンデュラの定理（1967）</span>
<p><strong>仮定</strong>：(1) 4 次元である　(2) \(S\) 行列が自明でない（相互作用する）　(3) 質量ギャップがある（離散的な粒子）　(4) ある質量以下の粒子種が有限個</p>
<p><strong>結論</strong>：対称性は「ポアンカレ × 内部対称性」に限られる。<br>→ <em>高スピンの保存量は存在できない。</em></p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>仮定</th><th class="mid">QCD は</th></tr></thead>
<tbody>
<tr><th>4 次元である</th><td class="mid"><strong>満たす</strong></td></tr>
<tr><th>\(S\) 行列が自明でない</th><td class="mid"><strong>満たす</strong></td></tr>
<tr><th>質量ギャップがある</th><td class="mid"><strong>満たす</strong></td></tr>
<tr><th>粒子種が有限個</th><td class="mid"><strong>満たす</strong></td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>この回の中心</h2>
<p><strong>QCD は四つの仮定を全部満たします。だから可積分になりえません。</strong></p>
<p>「QCD が厳密に解けない」のは、誰も賢くないからではなく、<em>仮定から出る帰結</em>です。</p>
</div>

<h2><span class="n">04</span>反例は、どうやって逃げているのか</h2>

<p>ここで①の六つに戻ります。全部、定理の仮定のどれかを外していました。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>逃げ道</th><th>どうやって</th><th class="mid">破る仮定</th></tr></thead>
<tbody>
<tr class="hi"><th>\(N{=}4\) 超対称</th><td><strong>共形不変 → 質量ギャップが無い</strong></td><td class="mid"><strong>仮定 3</strong></td></tr>
<tr><th>\(N{=}2\) Seiberg–Witten</th><td>超対称電荷はスピン \(1/2\)（ボゾンでない）</td><td class="mid">定理の対象外</td></tr>
<tr><th>大 \(N\)</th><td>\(N=\infty\) で \(S\) 行列が自明になる</td><td class="mid">仮定 2</td></tr>
<tr class="hi"><th><strong>2 次元</strong></th><td><strong>そもそも定理が 4 次元のもの</strong></td><td class="mid"><strong>仮定 1</strong></td></tr>
<tr><th>自由場</th><td>\(S\) 行列が 1</td><td class="mid">仮定 2</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">前回のフィルタの、本当の中身</span>
<p>ばらばらに見えた六つの厳密解が、<strong>一つの定理の裏返し</strong>でした。</p>
<p>第9回のフィルタは、言い換えると <em>「コールマン–マンデュラの仮定を外せるか」</em> です。</p>
</div>

<h2><span class="n">05</span>2 次元 QCD は、本当に解けている</h2>

<p>いちばん近い例を見ておきます。't Hooft 模型 ── 2 次元、\(N_c\to\infty\) の QCD では、中間子スペクトルが厳密に決まります。</p>

<div class="calc">
<span class="tag">2 次元の平面 QCD（'t Hooft, 1974）</span>
<p>大きい \(n\) で　\(M_n^2 \approx \pi^2 g^2 n\)　── <strong>レッジェ軌道が厳密に直線</strong></p>
</div>

<p>4 次元で「実験的に直線に見える」ものが、2 次元では<em>厳密に直線</em>になります。</p>

<p>そして <strong>4 次元の平面 QCD（\(N_c=\infty\)）は、いまだ未解決</strong>です。次元を 2 から 4 に上げるだけで、解ける／解けないが変わる。</p>

<div class="aside">
<span class="tag">そこだけは開いている</span>
<p>\(N_c=\infty\) は仮定 2（\(S\) 行列が自明でない）を破るので、<strong>4 次元の平面 QCD が解けてもコールマン–マンデュラとは矛盾しません</strong>。つまり ── <em>そこだけは、まだ開いた扉です</em>。</p>
</div>

<h2><span class="n">06</span>「解けない」の意味が変わる</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>読み</th><th class="mid">正しいか</th></tr></thead>
<tbody>
<tr><th>「まだ誰も解けていない」（未解決問題）</th><td class="mid"><strong>×</strong></td></tr>
<tr class="hi"><th><strong>「可積分にする道具が存在できない」（既解決問題）</strong></th><td class="mid"><strong>○</strong></td></tr>
</tbody>
</table>
</div>

<p>答えは「無い」であって、「まだ見つかっていない」ではありません。<em>これは悪い知らせではなく、探索範囲が狭まったという意味では良い知らせです。</em></p>

<div class="caveat">
<span class="tag">正直な線</span>
<p>コールマン–マンデュラは <strong>\(S\) 行列の対称性についての定理</strong>で、「厳密解が無い」を厳密に導くわけではありません ── <em>可積分性を封じる</em>だけです。可積分でなくても厳密に解ける道が、原理的に否定されたわけではありません。<br>04節の「\(N{=}2\) は定理の対象外」は正しいですが、<strong>Seiberg–Witten が厳密なのは低エネルギー有効作用まで</strong>で、完全なスペクトルは厳密には解けていません。<br>02節の「保存量 19 個」は数え方の一例です（フレーバー対称性は近似的なものを含みます）。</p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>では QCD に厳密なものは整数だけなのか。<strong>いいえ ── 「関係」があります。</strong> どれも値については何も言わず、量と量の間だけを言う。そして<em>関係だけで数値が 7 桁決まる</em>例が、実際にあります。</p>
</div>'''

build(out='../butsuri-kantan-10-coleman-mandula.html', acc='#4a2f52', ops='#8a5a1a',
      title='第10回：なぜ解けないのか ── 定理だった ── 物理を簡単にする',
      ep='第 10 回 ／ 第 III 部 厳密とは何か',
      eyebrow='コールマン–マンデュラの定理 ── QCD は四つの仮定を全部満たす',
      h1='なぜ解けないのか<br>── 定理だった',
      sub='4 次元の厳密解は六つある。ただし全部、超対称か大 \\(N\\) か平面極限か 2 次元。<br><em>並べると、一つの定理の裏返しでした。</em>',
      byline_l='必要な予備知識：第9回（厳密値のフィルタ）',
      byline_r='検証：kensho/calc05.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第10回です。コールマン–マンデュラの定理、Seiberg–Witten 解、\\(N{=}4\\) 平面極限の可積分性、\'t Hooft 模型はいずれも<strong>確立した標準的な内容</strong>です。<em>「六つの厳密解が一つの定理の裏返しである」という並べ方は本シリーズの整理</em>で、教科書がこの形で書いているわけではありません（kensho/calc05.py）。<strong>コールマン–マンデュラは可積分性を封じる定理であって、「厳密解が存在しない」ことの証明ではありません</strong> ── 06節の言い方はこの留保つきで読んでください。02節の保存量の数え方は一例です。</p>')
