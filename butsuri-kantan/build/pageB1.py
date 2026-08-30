# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第16回で「生き残るのは小出の関係だけ」と書きました。ただしその採点には、<strong>筆者が推測で決めた数が二つ</strong>入っています ── 探索空間 \(M\) と、事前分布の形。<em>推測を全部、計算に置き換えます。</em> そして途中で、こちらの書き方の誤りが一つ見つかりました。</p>

<h2><span class="n">01</span>値そのもの</h2>

<div class="keybox">
<span class="lbl">小出の関係（1981）</span>
<p>$$K = \frac{m_e+m_\mu+m_\tau}{\left(\sqrt{m_e}+\sqrt{m_\mu}+\sqrt{m_\tau}\right)^2} = \frac{2}{3}\;?$$</p>
</div>

<div class="calc">
<span class="tag">計算（kensho/calc08.py ①）</span>
<p>\(K = \mathbf{0.6666605115}\)<br>
\(2/3 = 0.6666666667\)<br>
ずれ（相対）\(= \mathbf{9.23\times10^{-6}}\)</p>
</div>

<h2><span class="n">02</span>まず、こちらの誤り ── 「5〜6 桁」は言い過ぎだった</h2>

<p>\(m_e\) と \(m_\mu\) は極めて精密に測られていますが、\(m_\tau = 1776.86 \pm 0.12\) MeV には<strong>相対 \(6.8\times10^{-5}\) の誤差</strong>があります。これを振ってみます。</p>

<div class="calc">
<span class="tag">計算（kensho/calc08.py ②）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">\(K\)</th><th class="mid">2/3 からの相対</th></tr></thead>
<tbody>
<tr><th>\(m_\tau - \sigma\)</th><td class="mid">0.6666537364</td><td class="mid">\(1.94\times10^{-5}\)</td></tr>
<tr class="hi"><th>\(m_\tau\)（中心値）</th><td class="mid"><strong>0.6666605115</strong></td><td class="mid"><strong>\(9.23\times10^{-6}\)</strong></td></tr>
<tr><th>\(m_\tau + \sigma\)</th><td class="mid">0.6666672861</td><td class="mid">\(9.29\times10^{-7}\)</td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>訂正</h2>
<p>\(K\) の \(1\sigma\) 幅は <strong>\(1.02\times10^{-5}\)</strong>。実際のずれ \(9.23\times10^{-6}\) は、<em>それより小さい</em>。</p>
<p>つまりずれは <strong>0.91 \(\sigma\)</strong> ── <strong>「5〜6 桁合っている」とは言えません。</strong></p>
<p>言えるのは <em>「\(\tau\) 質量の誤差の範囲内で \(2/3\) と無矛盾」</em> まで。</p>
</div>

<p>第16回の「5〜6 桁合っていて」という書き方は、<strong>誤差を無視していました</strong>。訂正します。買いのビット数も、ずれではなく<em>誤差</em>で頭打ちになります ── \(16.7\) ではなく <strong>\(16.6\)</strong>（この差は小さいですが、意味が違います）。</p>

<div class="aside">
<span class="tag">これは良い知らせでもある</span>
<p><strong>\(\tau\) 質量が 10 倍精密になれば、この判定は作り直せます。</strong> いまは「無矛盾」としか言えませんが、精度が上がれば <em>本当に \(2/3\) なのか、たまたま近いだけなのか</em> が決まる。<br>第9回の言葉でいえば ── <em>これは「制御された」判定です</em>。次の一手がある。</p>
</div>

<h2><span class="n">03</span>事前分布を、推測ではなく作る</h2>

<p>採点の「買い」は、<em>\(K\) がたまたま \(2/3\) に近づく確率</em>で決まります。第16回では「\(K\) は \([1/3, 1]\) に一様」と仮定しました。コーシー・シュワルツから値域はその通りですが、<strong>一様かどうかは確かめていませんでした</strong>。</p>

<p>そこで、質量三つ組をランダムに引いて \(K\) の分布を実際に作ります（対数一様、各 40 万回）。</p>

<div class="calc">
<span class="tag">計算（kensho/calc08.py ④）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">比の振れ幅</th><th class="mid">2/3 近傍の密度</th><th class="mid">一様（1.500）との比</th></tr></thead>
<tbody>
<tr><td class="mid">\(\pm 0.0\) 桁</td><td class="mid">1.362</td><td class="mid">0.91 倍</td></tr>
<tr><td class="mid">\(\pm 0.5\) 桁</td><td class="mid">1.344</td><td class="mid">0.90 倍</td></tr>
<tr class="hi"><td class="mid">\(\pm 1.0\) 桁</td><td class="mid"><strong>1.401</strong></td><td class="mid"><strong>0.93 倍</strong></td></tr>
</tbody>
</table>
</div>

<p>分位点は 5 % で 0.494、中央値 <strong>0.757</strong>、95 % で 0.953。<em>分布は高い側（\(K\to 1\)）に寄っています。</em></p>

<div class="keybox">
<span class="lbl">予想と逆だった</span>
<p>「階層があると \(K\) は自然に \(2/3\) 付近に来るのでは」と疑いましたが、<strong>逆でした</strong> ── \(2/3\) 近傍の密度は一様より <strong>0.93 倍</strong>、つまり<em>むしろ出にくい</em>。</p>
<p>→ 一様を仮定した買いは、<strong>0.10 ビットだけ控えめ</strong>だった。過大評価ではありませんでした。</p>
</div>

<h2><span class="n">04</span>他の三つ組では、\(2/3\) にならない</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>三つ組</th><th class="mid">\(K\)</th><th class="mid">2/3 からのずれ</th></tr></thead>
<tbody>
<tr class="hi"><th>荷電レプトン</th><td class="mid"><strong>0.666661</strong></td><td class="mid"><strong>0.0 %</strong></td></tr>
<tr><th>アップ型クォーク</th><td class="mid">0.849006</td><td class="mid">27.4 %</td></tr>
<tr><th>ダウン型クォーク</th><td class="mid">0.731428</td><td class="mid">9.7 %</td></tr>
</tbody>
</table>
</div>

<p>クォークは 10〜30 % ずれます。<strong>\(K\) が自動的に \(2/3\) になるわけではありません</strong> ── 03節で見た「集まりやすさ」は 10 % 程度の話で、\(10^{-5}\) を説明するものではない。</p>

<h2><span class="n">05</span>探索空間を、推測ではなく列挙する</h2>

<p>ここが本題です。第16回では \(M = 1000\)（\(\log_2 M = 10.0\)）と<em>推測</em>しました。実際に列挙します。</p>

<p>小出の式は \((\sum m^p)/(\sum m^q)^{p/q}\) の \(p=1, q=1/2\) の場合です。同じ形で \(p, q\) を小さい有理数の格子に振り、<strong>単純な有理数に当たるものを全部数えます</strong>。</p>

<div class="calc">
<span class="tag">計算（kensho/calc08.py ⑥）</span>
<p>試した \((p,q)\)：<strong>57 通り</strong> → 族の値段 \(\log_2 57 = \mathbf{5.83}\) ビット<br>
分母 12 以下の有理数に \(10^{-4}\) 以内で当たったもの：<strong>10 個</strong></p>
</div>

<p><strong>10 個も当たります。</strong> つまり「単純な有理数に当たった」だけでは、まったく驚けない。ここで、第16回では入れていなかった値段を入れます。</p>

<div class="keybox">
<span class="lbl">狙う有理数にも、値段がある</span>
<p>\(2/3\) を当てるのと \(513/8\) を当てるのは、<em>同じではありません</em>。<br>
有理数 \(a/b\) を指定する値段 \(\approx \log_2(a\cdot b)\) ビット。</p>
<p>\(2/3\) なら \(\log_2 6 = \mathbf{2.58}\)、\(513/8\) なら \(\log_2 4104 = \mathbf{12.0}\) ── <strong>桁違い</strong>。</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\((p, q)\)</th><th class="mid">\(\approx\)</th><th class="mid">ずれ</th><th class="mid">有理数の値段</th><th class="mid">族を引いた後</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">\(p=1,\ q=1/2\)</th><td class="mid"><strong>2/3</strong></td><td class="mid">\(9.2\times10^{-6}\)</td><td class="mid"><strong>2.6</strong></td><td class="mid"><strong>\(+8.3\)</strong></td></tr>
<tr><th class="mid">\(p=-1/2,\ q=2\)</th><td class="mid">513/8</td><td class="mid">\(7.0\times10^{-6}\)</td><td class="mid">12.0</td><td class="mid">\(-0.7\)</td></tr>
<tr><th class="mid">\(p=-1/2,\ q=1/3\)</th><td class="mid">563/5</td><td class="mid">\(1.0\times10^{-5}\)</td><td class="mid">11.5</td><td class="mid">\(-0.7\)</td></tr>
<tr><th class="mid">\(p=-1/2,\ q=1/2\)</th><td class="mid">727/9</td><td class="mid">\(1.1\times10^{-5}\)</td><td class="mid">12.7</td><td class="mid">\(-2.1\)</td></tr>
<tr><th class="mid">\(p=1/3,\ q=-1\)</th><td class="mid">221/10</td><td class="mid">\(3.8\times10^{-5}\)</td><td class="mid">11.1</td><td class="mid">\(-2.3\)</td></tr>
<tr><th class="mid">（ほか 5 個）</th><td class="mid">…</td><td class="mid">…</td><td class="mid">12〜15</td><td class="mid">\(-3.0\) 〜 \(-5.3\)</td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>ここが今回いちばん面白いところ</h2>
<p><strong>\(513/8\) は、精度では小出より良い</strong>（\(7.0\times10^{-6}\) 対 \(9.2\times10^{-6}\)、0.4 ビット分）。</p>
<p>それでも負けます ── <em>有理数として 9.4 ビット高いから</em>。</p>
<p><strong>族の値段 5.83 を引くと、10 個のうち黒字は 1 個だけ。\(2/3\) です。</strong></p>
</div>

<p>これが、第16回で「探索空間を引いても黒字」と書いたことの<em>実際の中身</em>でした。しかも <strong>\(M\) の推測（\(\log_2 M = 10.0\)）は、実際の族（5.83）より大きすぎた</strong> ── 筆者は自分に厳しく見積もりすぎていたことになります。</p>

<h2><span class="n">06</span>採点を組み直す</h2>

<div class="calc">
<span class="tag">計算（kensho/calc08.py ⑦）</span>
<p>買い（誤差で頭打ち）　　　　　　： \(\mathbf{+16.6}\) ビット<br>
引き算① 狙う有理数 \(2/3\) の値段　： \(\mathbf{-2.58}\) ビット<br>
引き算② 式の族 57 通り　　　　　： \(\mathbf{-5.83}\) ビット<br>
補正③ 帰無分布が一様でない　　　： \(\mathbf{-0.10}\) ビット<br>
────────────────<br>
差引 <strong>\(+8.1\) ビット</strong></p>
</div>

<div class="keybox">
<span class="lbl">結論</span>
<p><strong>第16回の \(+6.8\) に対して、\(+8.1\)。結論は変わりません。</strong></p>
<p>ただし<em>内訳が入れ替わりました</em> ── 買いは下がり（誤差で頭打ち）、払いも下がった（族が推測より小さかった）。<br>そして新しく <strong>「狙う有理数の値段」という項目</strong>が入りました。</p>
</div>

<h2><span class="n">07</span>持ち帰るもの</h2>

<p>この番外編で出てきた道具は、小出の関係に限らず使えます。</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>道具</th><th>中身</th><th>効いた場面</th></tr></thead>
<tbody>
<tr class="hi"><th><strong>誤差で頭打ちにする</strong></th><td>「何桁合った」は<em>実験誤差より細かくは主張できない</em></td><td>「5〜6 桁」→「0.91 \(\sigma\)」</td></tr>
<tr class="hi"><th><strong>帰無分布を作る</strong></th><td>事前分布を仮定せず、<em>乱数で分布を作る</em></td><td>一様仮定は 0.10 ビット控えめだった</td></tr>
<tr class="hi"><th><strong>族を列挙する</strong></th><td>\(M\) を推測せず、<em>数える</em></td><td>推測 10.0 → 実際 5.83</td></tr>
<tr class="hi"><th><strong>狙う値の単純さも払う</strong></th><td>\(2/3\) と \(513/8\) は同じではない</td><td><em>9.4 ビットの差で順位が逆転</em></td></tr>
</tbody>
</table>
</div>

<p>とくに最後の一つは、第13回の \(6\pi^5\) にもそのまま効きます ── <strong>「それっぽい式」を採点するときは、当てた値そのものの単純さも勘定に入れること。</strong></p>

<div class="caveat">
<span class="tag">正直な線</span>
<p>05節の族は \(9\times 8\) の格子で、<strong>「同じくらい自然な式」の定義は筆者のもの</strong>です。族を広げれば払いが増え、黒字は縮みます。<em>この一点は依然として解決していません。</em><br>ただし ── <strong>有理数の単純さの値段は族に依りません</strong>。族をいくら広げても、\(513/8\) 型の競合が \(2/3\) を追い抜くことはない。<br>「有理数の値段 \(\log_2(a\cdot b)\)」は一つの選び方です（Stern–Brocot 木の深さでも近い値になります）。\(2/3\) と \(513/8\) の差が 9 ビットあることは、定義を変えても動きません。<br>03節の帰無分布は「対数一様」という一つの引き方で、別の引き方で \(\pm 0.5\) ビット動きます。<br>04節のクォークは PDG の \(\overline{\rm MS}\) 値です ── <strong>本来は極質量で揃えるべき</strong>で、揃えると値は動きます（ただし \(2/3\) に寄る向きではありません）。<br>そして最大の留保 ── <strong>\(+8.1\) ビットは「関係が在る」の証明ではありません</strong>。機構の説明は依然としてゼロで、なぜ \(2/3\) なのかを言える人はいません。</p>
</div>

<div class="next">
<span class="lbl">この先</span>
<p><strong>\(\tau\) 質量の精度が、この問いの首を握っています。</strong> いまの \(\pm 0.12\) MeV が \(\pm 0.012\) MeV になれば、\(K\) の \(1\sigma\) 幅は \(10^{-6}\) になり ── <em>小出の関係は、本当に \(2/3\) なのかどうかが決まります</em>。<br>第9回の分類でいえば、これは<strong>制御された問い</strong>です。次の一手があり、その一手は実験で打てます。</p>
</div>'''

build(out='../butsuri-kantan-b1-koide.html', acc='#5a3a6a', ops='#8a5a1a',
      title='番外編：小出の関係を、推測なしで採点する ── 物理を簡単にする',
      ep='番外編 ① ／ 第16回の訂正と、採点のやり直し',
      eyebrow='推測で決めていた二つの数を、計算に置き換える',
      h1='小出の関係を、<br>推測なしで採点する',
      sub='「5〜6 桁合っている」は<em>言い過ぎ</em>でした ── \\(\\tau\\) 質量の誤差を入れると 0.91 \\(\\sigma\\)。<br>そして探索空間は、推測より<em>小さかった</em>。',
      byline_l='必要な予備知識：第13回（探索の値段）、第16回（候補の採点）',
      byline_r='検証：kensho/calc08.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ番外編①です。<strong>本編第16回の記述（「5〜6 桁合っている」）の訂正を含みます</strong>。小出の関係（1981）と \\(K\\in[1/3,1]\\) は<strong>よく知られた事実</strong>で、\\(\\tau\\) 質量とその誤差は PDG の値です。<em>帰無分布のシミュレーション、式の族の列挙、「狙う有理数の単純さ」を値段に入れる採点は、本シリーズの計算と整理</em>です（kensho/calc08.py）。<strong>05節の族の定義は筆者のもので、族を広げれば黒字は縮みます</strong> ── この一点は未解決です。<strong>\\(+8.1\\) ビットは「関係が実在する」ことの証明ではありません</strong>。機構の説明は依然としてゼロで、なぜ \\(2/3\\) なのかを説明できる理論はありません。</p>')
