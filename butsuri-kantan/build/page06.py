# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">残った 12 倍の幅を潰します。使う法則は<em>一本だけ</em>で、必要な計算は<strong>足し算と割り算</strong>です。それで 8 個のバリオンが全部 1 % 以内に入りました。しかも ── <strong>パラメータを一つも足さない関係が、5 本も残ります。</strong></p>

<h2><span class="n">01</span>法則は、これだけ</h2>

<div class="keybox">
<span class="lbl">構成子＋超微細</span>
<p>$$M = \sum_i m_i \;+\; A\sum_{i&lt;j}\frac{\langle \mathbf{S}_i\cdot\mathbf{S}_j\rangle}{m_i m_j}$$</p>
<p>第一項は「中の粒の重さを足す」。第二項は「スピンの向きが合っているかどうか」。</p>
</div>

<p>そして \(\langle \mathbf{S}_i\cdot\mathbf{S}_j\rangle\) は、<strong>スピンの足し算だけ</strong>で出ます。動力学は一切要りません。</p>

<div class="calc">
<span class="tag">スピンの合成（暗算でできる）</span>
<p>二つのスピン \(1/2\) なら \(\langle \mathbf{S}_1\cdot\mathbf{S}_2\rangle = \tfrac12\!\left[S(S+1)-\tfrac32\right]\)</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>状態</th><th class="mid">\(\sum\langle \mathbf{S}_i\cdot\mathbf{S}_j\rangle\)</th></tr></thead>
<tbody>
<tr><th>中間子 \(S=0\)（\(\pi, K\)）</th><td class="mid">\(-3/4\)</td></tr>
<tr><th>中間子 \(S=1\)（\(\rho, K^*, \phi\)）</th><td class="mid">\(+1/4\)</td></tr>
<tr><th>バリオン \(J=1/2\)（同種 3 個、\(N\)）</th><td class="mid">\(-3/4\)</td></tr>
<tr><th>バリオン \(J=3/2\)（\(\Delta, \Omega\)）</th><td class="mid">\(+3/4\)</td></tr>
<tr><th>\(\Lambda\)（\(ud\) が \(S=0\)）</th><td class="mid">\(ud\): \(-3/4\)、\(s\) とは \(0\)</td></tr>
<tr><th>\(\Sigma\)（\(ud\) が \(S=1\)）</th><td class="mid">\(ud\): \(+1/4\)、\(s\) とは \(-1\)</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">02</span>当てはめる</h2>

<p>パラメータは 3 個（\(m_u\)、\(m_s\)、\(A\)）。データは 8 個のバリオン。</p>

<div class="calc">
<span class="tag">計算（kensho/calc02.py ④）</span>
<p>フィット結果： \(m_u = 364\) MeV、\(m_s = 537\) MeV</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">実測 [MeV]</th><th class="mid">模型 [MeV]</th><th class="mid">ずれ</th></tr></thead>
<tbody>
<tr><th>\(N\)</th><td class="mid">938.9</td><td class="mid">942.7</td><td class="mid">+0.4 %</td></tr>
<tr><th>\(\Delta\)</th><td class="mid">1232.0</td><td class="mid">1238.9</td><td class="mid">+0.6 %</td></tr>
<tr><th>\(\Lambda\)</th><td class="mid">1115.7</td><td class="mid">1115.9</td><td class="mid">+0.0 %</td></tr>
<tr><th>\(\Sigma\)</th><td class="mid">1193.2</td><td class="mid">1179.6</td><td class="mid">−1.1 %</td></tr>
<tr><th>\(\Sigma^*\)</th><td class="mid">1384.6</td><td class="mid">1380.2</td><td class="mid">−0.3 %</td></tr>
<tr><th>\(\Xi\)</th><td class="mid">1318.3</td><td class="mid">1326.1</td><td class="mid">+0.6 %</td></tr>
<tr><th>\(\Xi^*\)</th><td class="mid">1533.4</td><td class="mid">1526.7</td><td class="mid">−0.4 %</td></tr>
<tr class="hi"><th>\(\Omega\)</th><td class="mid">1672.5</td><td class="mid">1678.3</td><td class="mid"><strong>+0.3 %</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<span class="lbl">結果</span>
<p><strong>RMS 7.1 MeV。8 個のバリオンが、3 パラメータで全部 1 % 以内。</strong></p>
<p>ばらつきは \(403 \to 17\) MeV。ハドロン 1 個あたり <strong>4.5 ビット</strong>、13 個で <strong>59 ビット</strong>買って、払いは \(6\times5.37 = 32.2\) ビット ── <strong>差し引き \(+27\) ビット</strong>。</p>
</div>

<p>中間子の方は RMS 26.7 MeV で、\(\pi\) が \(+5.6\) % ずれます。これは既知の欠陥で、\(\pi\) は南部・ゴールドストン粒子だからこの模型の枠外です。</p>

<h2><span class="n">03</span>そして、タダの関係が 5 本残る</h2>

<p>ここからが面白いところです。<strong>パラメータを一つも足さずに成り立つ関係</strong>が、同じ枠組みから出てきます。</p>

<div class="calc">
<span class="tag">計算（kensho/calc02.py ⑥）</span>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>関係</th><th>中身</th><th class="mid">ずれ</th><th class="mid">ビット</th></tr></thead>
<tbody>
<tr class="hi"><th>Gell-Mann–Okubo</th><td>\((m_N+m_\Xi)/2 = (3m_\Lambda+m_\Sigma)/4\)</td><td class="mid"><strong>0.57 %</strong></td><td class="mid"><strong>7.5</strong></td></tr>
<tr class="hi"><th>Coleman–Glashow</th><td>\((p-n)+(\Xi^0-\Xi^-) = \Sigma^+-\Sigma^-\)</td><td class="mid"><strong>0.78 %</strong></td><td class="mid"><strong>7.0</strong></td></tr>
<tr><th>磁気能率の比</th><td>\(\mu_n/\mu_p = -2/3\)</td><td class="mid">2.75 %</td><td class="mid">5.2</td></tr>
<tr><th>超微細のスケーリング</th><td>\((\Sigma^*-\Sigma)/(\Delta-N) = m_u/m_s\)</td><td class="mid">3.56 %</td><td class="mid">4.8</td></tr>
<tr><th>十重項の等間隔</th><td>\(\Delta\to\Sigma^*\to\Xi^*\to\Omega\) の間隔が等しい</td><td class="mid">9.19 %</td><td class="mid">3.4</td></tr>
<tr><th><strong>合計</strong></th><td></td><td class="mid"></td><td class="mid"><strong>27.9</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>全部、紙と鉛筆。パラメータの追加はゼロ。合計 28 ビット。</strong></p>

<p>とくに Coleman–Glashow は、電磁相互作用による質量差だけを 6 個並べて足し引きする関係で、<em>動力学を一切使っていません</em>。使ったのは SU(3) の足し算とスピンの足し算だけです。</p>

<h2><span class="n">04</span>質量以外も、同じ層で行ける</h2>

<p>「大きさ」と「エネルギー」も、同じくらい単純に出ます。MIT バッグ模型は、<strong>不確定性原理と真空の一定圧力</strong>、それだけです。</p>

<div class="keybox">
<span class="lbl">バッグ模型</span>
<p>$$E(R) = \frac{3\times 2.04 - 1.84}{R} + \frac{4}{3}\pi R^3 B$$</p>
<p>第一項は「狭い所に閉じ込めるとエネルギーが上がる」（不確定性）。<br>第二項は「真空を押しのけた体積ぶんの代金」（一定圧力）。</p>
</div>

<div class="calc">
<span class="tag">計算（kensho/calc02.py ⑦）</span>
<p>\(B^{1/4} = 145\) MeV とすると<br>
\(dE/dR = 0\) → \(R = \mathbf{1.04}\) fm、\(E = \tfrac43 K/R = \mathbf{1083}\) MeV<br>
実測の核子質量 938.9 MeV に対して <strong>\(+15\) %</strong></p>
</div>

<p><strong>微分 1 回で、陽子の質量が 15 % 以内。</strong> 閉じ込めを「一定の圧力」に置き換えるだけで、この精度です。</p>

<h2><span class="n">05</span>第 II 部の途中結果</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>何が</th><th>何で</th><th class="mid">どれだけ</th><th class="mid">重さ</th></tr></thead>
<tbody>
<tr><th>なぜ 1 GeV か</th><td>指数関数 1 個</td><td class="mid">65 ビットを 6.0 で</td><td class="mid">1 行</td></tr>
<tr><th>どれも \(\Lambda\) の \(O(1)\) 倍</th><td>次元解析</td><td class="mid">桁は全部当たる</td><td class="mid">暗算</td></tr>
<tr><th>質量のパターン</th><td>構成子＋スピンの足し算</td><td class="mid">\(+27\) ビット</td><td class="mid">四則演算</td></tr>
<tr class="hi"><th><strong>パラメータ不要の関係 5 本</strong></th><td><strong>SU(3) とスピン</strong></td><td class="mid"><strong>28 ビット／0 個</strong></td><td class="mid"><strong>紙と鉛筆</strong></td></tr>
<tr><th>大きさとエネルギー</th><td>不確定性＋一定圧力</td><td class="mid">15 % 以内</td><td class="mid">微分 1 回</td></tr>
<tr><th>残り（数 % 以下）</th><td>格子 QCD</td><td class="mid">─</td><td class="mid">\(10^{19}\) flops</td></tr>
</tbody>
</table>
</div>

<div class="record">
<h2>ここまでの結論</h2>
<p><strong>数 % までは、全部が単純な計算で届きます。</strong> 格子 QCD が要るのは<em>最後の数 % だけ</em>でした。</p>
<p>そして層の切れ目が明確です ── <strong>スケール（指数関数）／桁（次元解析）／パターン（足し算）／残り（数値計算）</strong>。</p>
</div>

<div class="caveat">
<span class="tag">正直な線</span>
<p>構成子質量（\(m_u = 364\) MeV）は<strong>この模型の中でだけ意味のある数</strong>です。カレント質量（\(u \approx 2\) MeV）とは別物で、<em>閉じ込めの効果を質量に繰り込んだ記法</em>にすぎません。<br>03節の 5 本のうち、Gell-Mann–Okubo と十重項等間隔は<strong>同じ SU(3) 破れの 1 次から出る</strong>ので完全には独立でなく、合計 28 ビットは上振れしています。<br>そして最大の留保 ── <em>ここで持ち込んだ定数を、まだ数えていません</em>。それが次回です。</p>
</div>

<div class="next">
<span class="lbl">次回</span>
<p>「単純にした」と言いながら、この二回で<strong>12 個の定数</strong>を持ち込みました。構成子質量、超微細係数、バッグ定数 ── どれも出どころが説明されていない。<em>それを一つずつ潰せるか</em>を、次回やります。答えは <strong>12 個 → 0 個</strong>でした。</p>
</div>'''

build(out='../butsuri-kantan-06-arithmetic.html', acc='#2a4d3a', ops='#8a5a1a',
      title='第6回：足し算だけで、1 % に届く ── 物理を簡単にする',
      ep='第 6 回 ／ 第 II 部 強い力で実演する',
      eyebrow='構成子＋スピンの合成 ── 8 個のバリオンが 3 パラメータで 1 % 以内',
      h1='足し算だけで、<br>1 % に届く',
      sub='動力学は一切使いません。スピンの足し算と、割り算だけ。<br><em>おまけにパラメータ不要の関係が 5 本残りました。</em>',
      byline_l='必要な予備知識：第5回（層の切り方）',
      byline_r='検証：kensho/calc02.py',
      body=BODY + '\n\n<p class="foot">この文書は「物理を簡単にする」シリーズ第6回です。構成子クォーク模型、超微細相互作用、Gell-Mann–Okubo、Coleman–Glashow、MIT バッグ模型はいずれも<strong>確立した標準的な内容</strong>です。02節のフィットと05節のビット勘定は本シリーズの計算です（kensho/calc02.py）。<strong>構成子質量はこの模型の中でだけ意味を持つ量</strong>で、カレントクォーク質量とは別物です。<strong>\\(\\pi\\) 中間子はこの模型の枠外</strong>（南部・ゴールドストン粒子）で、フィットが悪いのは既知の欠陥です。03節の 5 本は完全に独立ではなく、合計ビットは上振れしています。</p>')
