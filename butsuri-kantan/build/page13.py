# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">前回は勝った歴史でした。この回は<strong>負けた歴史</strong>です ── ケプラーの正多面体、ボーデの法則、エディントンの 137。同じくらい大事なのは、負け方に型があることです。そして<em>いちばん使える発想</em>が、負けた例の中から出てきます ── <strong>プルーの仮説は 1815 年に破れて、1913 年に復活しました。</strong></p>

<h2><span class="n">01</span>負けた歴史</h2>

<div class="calc">
<span class="tag">計算（kensho/calc06.py ④）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>いつ・誰</th><th>主張</th><th class="mid">結果</th><th>中身</th></tr></thead>
<tbody>
<tr><th>ケプラーの正多面体 (1596)</th><td>惑星軌道の比 ＝ 正多面体</td><td class="mid"><strong>外れ</strong></td><td>軌道の数が合わない</td></tr>
<tr><th>ボーデの法則 (1772)</th><td>\(a = 0.4 + 0.3\cdot 2^n\)</td><td class="mid">天王星まで当たり</td><td><strong>海王星で破綻</strong></td></tr>
<tr class="hi"><th>プルーの仮説 (1815)</th><td>原子量は水素の整数倍</td><td class="mid"><strong>一度外れ</strong></td><td><strong>→ 04節で復活する</strong></td></tr>
<tr><th>エディントン (1929)</th><td>\(1/\alpha = 136 \to 137\)</td><td class="mid"><strong>外れ</strong></td><td>実測 137.035999</td></tr>
<tr><th>\(6\pi^5 = 1836.12\)</th><td>\(m_p/m_e = 1836.15\)</td><td class="mid"><strong>微妙</strong></td><td>→ 03節で採点</td></tr>
</tbody>
</table>
</div>

<p>ボーデの法則が示唆的です。<strong>天王星まで当たっていました。</strong> 当たっているうちは、誰も疑いません。そして海王星で外れた。</p>

<p>エディントンは、最初 \(1/\alpha = 136\) と主張し、測定が改善すると <strong>137 に変更しました</strong>。この「一度調整した」という事実が、あとで効いてきます。</p>

<h2><span class="n">02</span>負ける理由は、いつも同じ</h2>

<p>整数式は、<em>いくらでも作れます</em>。だから「当たった」だけでは何も言えません。<strong>いくつ試したかを数えないと、驚けない。</strong></p>

<div class="keybox">
<span class="lbl">探索の値段</span>
<p>候補が \(M\) 通りあるとき、そのうち一つが当たっても、驚きから <strong>\(\log_2 M\) ビット</strong>を引かなければなりません。</p>
<p>誕生日で言えば ── 23 人の部屋で「誕生日が同じ二人がいた」は驚けません（組が 253 通りあるから）。<em>「先に一人を指名して、その人と一致した」なら驚けます。</em></p>
</div>

<h2><span class="n">03</span>\(6\pi^5\) を、実際に採点する</h2>

<p>陽子と電子の質量比 \(m_p/m_e = 1836.15267\) は、\(6\pi^5 = 1836.11811\) に非常に近い。有名な「近さ」です。採点します。</p>

<div class="calc">
<span class="tag">計算（kensho/calc06.py ⑤）</span>
<p>\(6\pi^5 = 1836.11811\)、実測 \(1836.15267\)、ずれ \(\mathbf{1.9\times10^{-5}}\)<br>
→ 買い \(-\log_2(1.9\times10^{-5}) = \mathbf{15.7}\) ビット</p>
<p class="lbl">払い（探索空間 \(M\) の見積もり）</p>
<p>\(a\pi^b/c\)（\(a,c\le10\)、\(b\le6\)）だけ数えて \(M=700\)　→ 払い 9.5　→ <strong>差引 \(+6.2\) ビット</strong><br>
指数・平方根・他の定数も入れると \(M=10^4\)　→ 払い 13.3　→ <strong>差引 \(+2.4\) ビット</strong></p>
</div>

<div class="keybox">
<span class="lbl">判定</span>
<p><strong>探索空間の見積もり次第で、生き残ったり消えたりします。</strong></p>
<p>しかも<em>機構の説明がゼロ</em> ── なぜ \(\pi^5\) なのかを言える人がいません。</p>
</div>

<p>これが「それっぽい整数式」の扱い方です。<strong>必ず \(\log_2 M\) を引いてから判断する。</strong> 引かずに喜ぶと、エディントンと同じ道を行きます。</p>

<h2><span class="n">04</span>プルーの復活 ── いちばん使える発想</h2>

<p>ここからがこの回の本題です。</p>

<p>1815 年、プルーは「すべての原子量は水素の整数倍だ」と主張しました。水素 1、炭素 12、酸素 16 ── みごとに当たっています。</p>

<p>ところが<strong>塩素が 35.45</strong> でした。整数ではありません。半端でもない、35 でも 36 でもない中途半端な数。仮説は破れました。</p>

<p>そして 1913 年、同位体が発見されます。</p>

<div class="calc">
<span class="tag">計算（kensho/calc06.py ⑥）</span>
<p>\(0.7576 \times 34.96885 \;+\; 0.2424 \times 36.96590 = \mathbf{35.453}\)</p>
<p>実測 35.45 に対して、ずれ \(8.3\times10^{-5}\)</p>
</div>

<div class="record">
<h2>プルーの教訓</h2>
<p><strong>一つ一つは整数でした。意味不明だったのは「混ぜた平均」の方です。</strong></p>
<p>塩素 35.45 は、\(^{35}\)Cl が 75.8 %、\(^{37}\)Cl が 24.2 % の混合でした。</p>
</div>

<h2><span class="n">05</span>この発想は、いまでも使える</h2>

<div class="keybox">
<span class="lbl">手順</span>
<p><strong>意味不明な比を見たら、まず「混合ではないか」を疑う。</strong></p>
</div>

<p>実例があります。\(m_p/m_e = 1836.15\) が汚いのは、<em>陽子が混合だから</em>です。</p>

<div class="calc">
<span class="tag">計算（kensho/calc06.py ⑥）</span>
<p>クォーク質量 \(9.0\) MeV（<strong>1.0 %</strong>、ヒッグス起源）<br>
＋ グルーオン場 \(929.3\) MeV（<strong>99.0 %</strong>、\(\Lambda\) 起源）<br>
＝ 陽子 938.3 MeV</p>
</div>

<p>電子は 100 % がヒッグス起源です。陽子は 99 % が閉じ込めのエネルギー。<strong>起源の違う二つを足した数と、単一起源の数の比</strong>に、きれいな整数比を期待する理由がありません。</p>

<div class="aside">
<span class="tag">なぜこれが使えるのか</span>
<p>混合を疑うと、<em>次の一手が具体的になります</em>。「では何と何の混合か」「比率はいくつか」「片方だけを取り出せないか」── どれも実験や計算で答えが出る問いです。<br>一方「\(6\pi^5\) ではないか」には次の一手がありません。<strong>合っているか外れているかしか言えない。</strong></p>
</div>

<h2><span class="n">06</span>負けた歴史から取り出せる三つ</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>教訓</th><th>出どころ</th><th>使い方</th></tr></thead>
<tbody>
<tr><th><strong>当たっているうちは疑えない</strong></th><td>ボーデの法則</td><td>次の一点を予言させる</td></tr>
<tr><th><strong>調整したら、その分を引く</strong></th><td>エディントン \(136\to137\)</td><td>\(\log_2 M\) を数える</td></tr>
<tr class="hi"><th><strong>汚い数は、混合かもしれない</strong></th><td>プルー → 同位体</td><td><strong>分解を試す</strong></td></tr>
</tbody>
</table>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>03節の探索空間 \(M\) は<strong>筆者の見積もり</strong>です。この一点で結論が変わります ── \(M=700\) なら \(6\pi^5\) は生き残り、\(M=10^4\) ならほぼ消える。<em>「正しい \(M\)」を決める客観的な方法を、本シリーズは持っていません。</em><br>05節の「陽子は混合だから汚い」は<strong>説明であって証明ではありません</strong>。混合だから汚い、という因果を示したわけではなく、汚さと混合が同時に成り立っているだけです。</p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>では実際に検定します。<strong>13 個のハドロンの質量比は、単純な有理数に寄っているのか。</strong> 同じ範囲から引いた「偽ハドロン」4000 組と比べて、統計的に判定します。</p>
</div>'''

build(out='../butsuri-kantan-13-prout.html', acc='#7a3a2a', ops='#3a5a7a',
      title='第13回：負けた整数比と、プルーの復活 ── 物理を簡単にする',
      ep='第 13 回 ／ 第 IV 部 整数比の探し方',
      eyebrow='塩素 35.45 は、35 と 37 の混合だった',
      h1='負けた整数比と、<br>プルーの復活',
      sub='一つ一つは整数でした。意味不明だったのは<em>混ぜた平均</em>の方。<br>汚い比を見たら、まず混合を疑う。',
      byline_l='必要な予備知識：第12回（整数比の戦績）',
      byline_r='検証：kensho/calc06.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第13回です。ケプラーの正多面体、ボーデの法則、プルーの仮説と同位体、エディントンの \\(1/\\alpha\\)、\\(6\\pi^5\\) の近さは<strong>いずれも歴史的事実</strong>です。陽子質量のクォーク質量寄与が約 1 % であることも<strong>標準的な内容</strong>です。<em>「探索空間 \\(\\log_2 M\\) を引いてから判断する」という採点法と、「汚い比は混合を疑う」という手順は本シリーズの整理</em>です（kensho/calc06.py）。<strong>03節の \\(M\\) は筆者の見積もりで、この一点で結論が変わります</strong>。05節は説明であって因果の証明ではありません。</p>')
