# -*- coding: utf-8 -*-
from mkpage import build

BODY = r'''<p class="lead">第4回で「消せるものを全部消すと質量ひとつになる」と数えたとき、その絵の出典として名前だけ出しました ── <strong>ヴェッテリヒ</strong>、「膨張しない宇宙」を実際に場の理論として書いた人です。今回は中身に入ります。<em>第4回の絵が「記法」だったのに対し、コスモンは<strong>その記法を実装した動的な理論</strong>です</em> ── だから予言を持ちます。今回の問いは一つ：<strong>記法が理論になると、何が増えるのか。</strong></p>

<h2><span class="n">01</span>第4回の絵と、コスモンの違い</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">第4回の絵</th><th class="mid">コスモン</th></tr></thead>
<tbody>
<tr><th>動くもの</th><td class="mid">質量ひとつ \(\tilde m=a(t)m\)</td><td class="mid">質量ひとつ \(m\propto\chi\)</td></tr>
<tr class="hi"><th>\(a(t)\) や \(\chi(t)\) は</th><td class="mid"><strong>手で置いた関数</strong></td><td class="mid"><strong>場の方程式が決める</strong></td></tr>
<tr><th>パラメータ</th><td class="mid">0 個</td><td class="mid">ポテンシャル \(V(\chi)\) の 2 個</td></tr>
<tr><th>予言</th><td class="mid">0 個</td><td class="mid">\(w(z)\)、構造形成</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">01節の結論</p>
<p style="margin:6px 0 0">同じ絵でも、\(m(t)\) が <strong>「選ばれる」のか「決まる」のか</strong>で、まったく別物になります。<br>
── <em>第4回は記法、コスモンは理論。</em></p>
</div>

<p>ヴェッテリヒの模型では、スカラー場 \(\chi\)（コスモン）がすべての粒子質量を決めます ── \(m\propto\chi\)。そして<strong>同じ \(\chi\) が暗黒エネルギーの役もします</strong>。質量を育てる場と、宇宙を加速させる場が、同じ一つの場です。</p>

<h2><span class="n">02</span>払う ── パラメータの値段</h2>

<div class="calc">
<span class="tag">第5回の天秤</span>
<p class="lbl">指数型ポテンシャル \(V(\chi)=M^4e^{-\alpha\chi/M}\) は 2 個</p>
$$2\times\tfrac12\log_2(1701)=2\times5.37=10.7\ \text{ビット}$$
</div>

<p>第4回の絵は 0 個でしたから、<strong>10.7 ビット払った</strong>ことになります。では、何を買うのでしょうか。</p>

<h2><span class="n">03</span>買う ── 宇宙定数のチューニング</h2>

<div class="calc">
<span class="tag">第12回の数字を、ビットに直す</span>
$$\frac{\rho_\Lambda}{M_{\rm Pl}^4}=1.13\times10^{-123}\qquad\Longrightarrow\qquad -\log_2(1.13\times10^{-123})=408\ \text{ビット}$$
</div>

<div class="keybox">
<p class="lbl">今回いちばん言いたいこと</p>
<p style="margin:6px 0 0">この値を手で合わせるなら、<strong>408 ビットを設定する</strong>ことになります。<br>
クインテッセンスの主張は「それは<em>アトラクタ（引き込み解）</em>で自動的に出る」── <br>
<strong>払う 10.7 ビットで、最大 408 ビットを買い戻す勘定です。</strong></p>
</div>

<p>これが、パラメータを増やすのに動的な暗黒エネルギーが魅力的である理由です。第5回で「パラメータ 1 個の値段は 5.37 ビット」と数えました ── <em>408 ビットの説明が付くなら、2 個くらい安いものです</em>。（ただし全部は買い戻せません。⑦で正直に勘定します。）</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>なぜ第28回の VSL のように死なないのか</h2>

<p>ここが構造的にいちばん面白いところです。コスモンも「定数が変わる」型の理論なのに、第28回の VSL と運命が違います。</p>

<div class="calc">
<span class="tag">理由は一行</span>
<p class="lbl">コスモンは<strong>すべての質量を同じ \(\chi\) で決める</strong>ので</p>
$$\frac{m_p}{m_e},\quad \frac{m_n}{m_p},\quad \alpha\quad \text{はすべて厳密に不変}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>無次元比</th><th class="mid">観測上限</th><th class="mid">縛られたビット</th><th class="mid">コスモンの予言</th></tr></thead>
<tbody>
<tr><th>\(\alpha\)</th><td class="mid">\(1.4\times10^{-8}\)</td><td class="mid">26.1</td><td class="mid"><strong>厳密に 0</strong></td></tr>
<tr><th>\(m_p/m_e\)</th><td class="mid">\(1.4\times10^{-7}\)</td><td class="mid">22.8</td><td class="mid"><strong>厳密に 0</strong></td></tr>
<tr><th>\(m_n/m_p\)</th><td class="mid">\(1\times10^{-2}\)</td><td class="mid">6.6</td><td class="mid"><strong>厳密に 0</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">04節の結論</p>
<p style="margin:6px 0 0">同じ「定数が変わる」でも、<strong>比が守られるかどうかで生死が分かれます。</strong><br>
VSL は \(\alpha\) を動かして 26 ビットの制約に正面衝突しました（第28回）。<br>
コスモンは比を守るので、<em>定数の測定では一切ひっかかりません</em>。</p>
</div>

<p>これは偶然ではなく、<strong>設計原理</strong>です。第3回で「比較相手を言わなければ主張にならない」、第9回で「原子が縮んでも比べる相手が全部同じだけ縮む」と見ました。<em>コスモンは、その構造を理論の中に組み込んでいます</em> ── 一つの場がすべての質量を決めるので、比が動きようがない。</p>

<h2><span class="n">05</span>では、何で判定されるのか</h2>

<p>定数の測定で区別できないなら、判定は別のところへ移ります ── <strong>暗黒エネルギーの状態方程式</strong>です。</p>

<div class="calc">
<span class="tag">観測</span>
$$w=-1.03\pm0.03\qquad(\text{Planck} + \text{SNe} + \text{BAO})$$
<p class="lbl">事前範囲を \(w\in[-2,0]\) と取ると</p>
$$\text{縛られたビット}=-\log_2\frac{0.06}{2}=5.1\ \text{ビット}$$
</div>

<div class="fig">
<p class="cap">図：状態方程式 \(w\) の土俵。<strong>宇宙定数は \(w=-1\) の一点</strong>、クインテッセンスは幅を持ちます。ツマミでポテンシャルの傾き \(\alpha\) を変えると、\(w\) が動いて観測の帯を出入りします ── <em>これが「記法が理論になって手に入れた土俵」です</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>ポテンシャルの傾き \(\alpha\)（大きいほど \(w\) が \(-1\) から離れる）<input id="sa" type="range" min="0" max="200" value="40" step="1"></label>
  <span class="val" id="va">α = 0.40</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a4a2a"></i>コスモンの \(w(z)\)</span>
  <span><i class="swatch" style="background:#8a6a1a"></i>宇宙定数（\(w=-1\)）</span>
  <span><i class="swatch" style="background:#c8d2c8"></i>観測の許す帯（\(\pm0.03\)）</span>
</div>
</div>

<p>DESI（2024）は \(w\) が時間変化する模型を選好する兆候を報告しています ── <strong>現在進行形の話</strong>で、本稿は判定しません。<em>ただし「判定できる土俵に乗っている」こと自体が、第4回の絵との決定的な違い</em>です。</p>

<h2><span class="n">06</span>特異点は、消えるのか</h2>

<p>ヴェッテリヒの主張でいちばん派手なのは、<strong>「宇宙に始まりは無い」</strong>という部分です。第4回の表で \(\tilde R=0\)（曲率が消える）と数えたのと、同じ場所の話です。</p>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>曲率不変量は発散しない</strong><span>質量が育つ絵では、過去は \(\chi\to0\) の有限の側にある</span></div></div>
<div class="row"><div class="mk">△</div><div class="txt"><strong>光の測地線は延長できる</strong><span>ヌル測地線は共形変換で（再パラメータ化を除いて）保たれる ── 第11回の共形不変性</span></div></div>
<div class="row hi"><div class="mk">✗</div><div class="txt"><strong>質量を持つ粒子の世界線は保たれない</strong><span>特異点の本体は測地線の不完備性で、そこは共形不変ではない ── <em>ここが論争の的</em></span></div></div>
</div>

<p>第6回で「絵を変えたら消えた謎は一つもない ── 消えたように見えた幾何の特異点も、無次元比を作ったら戻ってきた」と書きました。<strong>ここでも同じ注意が要ります。</strong> ただしコスモンの絵では<em>過去で質量も 0 に近づく</em>ので、質量を持つ粒子も光に近づく ── <strong>「特異点が消えた」かどうかは、この極限をどう扱うかに依存します</strong>。論争中です。</p>

<h2><span class="n">07</span>正直な帳簿 ── 買い戻せない分</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">内容</th></tr></thead>
<tbody>
<tr class="hi"><th>買い戻せる</th><td class="mid">\(\rho_\Lambda\) の大きさ（アトラクタで説明できれば最大 <strong>408 ビット</strong>）</td></tr>
<tr><th>買い戻せない ①</th><td class="mid">ポテンシャルのスケール \(M\) は、依然として置く必要がある</td></tr>
<tr><th>買い戻せない ②</th><td class="mid"><strong>「なぜ今」問題（第12回）は残る</strong> ── アトラクタでも今日の一致は説明しない</td></tr>
<tr><th>買い戻せない ③</th><td class="mid">\(\chi\) と物質の結合の強さは、新しい自由度</td></tr>
</tbody>
</table>
</div>

<p>だから実際に買い戻せるのは 408 ビットのうち一部です ── <strong>桁は縮むが、ゼロにはなりません</strong>。第12回で「宇宙定数問題も『なぜ今』問題も、絵の取り替えでは動かない」と数えました。<em>コスモンは絵の取り替えではなく理論なので、前者には効きます。後者には効きません。</em></p>

<h2><span class="n">08</span>手術 ── 名前と中身</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>回</th><th>理論</th><th class="mid">名前が指しているもの</th><th class="mid">中身</th><th class="mid">手術は済んでいるか</th></tr></thead>
<tbody>
<tr><th>28</th><td>VSL</td><td class="mid">(A) 単位の取り替え</td><td class="mid">(B) \(\alpha\) が動く</td><td class="mid"><strong>済んでいない</strong></td></tr>
<tr><th>31</th><td>CCC</td><td class="mid">(A) と (B) の両方</td><td class="mid">(B) ホーキング点</td><td class="mid">済んでいる</td></tr>
<tr class="hi"><th>32</th><td><strong>コスモン</strong></td><td class="mid">(A) 「膨張しない宇宙」</td><td class="mid">(B) 動的なスカラー場</td><td class="mid"><strong>論文の中で済んでいる</strong></td></tr>
</tbody>
</table>
</div>

<p>論文の題「膨張しない宇宙」は (A) 側の言い方です。ところが<strong>ヴェッテリヒ自身が、二つの絵は Weyl 変換で等価だと明示しています</strong> ── だから第28回の VSL のような取り違えは起きません。<em>題は挑発的ですが、手術は論文の中で済んでいる</em>。第31回の CCC と同じ型です。</p>

<div class="aside">
<span class="tag">第 IV 部でわかってきたこと</span>
六つの理論を手術台に載せてきて、<strong>分かれ目がはっきりしてきました</strong> ── 名前が (A) を指しているかどうかではなく、<em>理論の側が (A) と (B) を区別できているかどうか</em>です。VSL だけが区別せず、\(\alpha\) の 26 ビットが見えなくなりました。インフレーション・MOND・CCC・コスモンは、どれも区別したうえで (B) に賭けています。<strong>第3回の手術は、良い理論なら最初から済ませてある</strong>ということでした。
</div>

<h2><span class="n">09</span>種明かし ── 記法が理論になると、何が増えるのか</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>増えるもの</th><th class="mid">変化</th><th class="mid">帳簿での意味</th></tr></thead>
<tbody>
<tr><th>パラメータ</th><td class="mid">0 個 → 2 個</td><td class="mid">10.7 ビット払う</td></tr>
<tr><th>予言</th><td class="mid">0 個 → \(w(z)\)</td><td class="mid">5.1 ビットの土俵に乗る</td></tr>
<tr class="hi"><th>説明</th><td class="mid">無し → \(\rho_\Lambda\) の大きさ</td><td class="mid"><strong>最大 408 ビット買い戻す</strong></td></tr>
<tr><th>反証可能性</th><td class="mid">無し → 有り</td><td class="mid">\(w=-1\) からのずれで判定できる</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">09節の結論</p>
<p style="margin:6px 0 0">第25回の言葉で言えば ──<br>
<strong>記法は \(L(\text{法則})\) を短くするだけ。理論は \(L(\text{パラメータ})\) を払って \(L(\text{残差})\) を減らしにいく。</strong><br>
<em>土俵が違います。</em> そして第25回で見たとおり、判定に使えるのは後者だけでした。</p>
</div>

<div class="caveat">
<span class="tag">正直な線 ── この回が置いている前提</span>
<p style="margin:0 0 10px"><strong>① コスモン模型は、ヴェッテリヒによる一連の仕事の要約です</strong>（Wetterich 1988 のクインテッセンス、2013 の「膨張しない宇宙」ほか）。<em>本稿は具体的な模型を一つに固定せず</em>、「すべての質量を一つのスカラー場が決める」という構造だけを扱っています ── 実際の模型には多くの変種があります。</p>
<p style="margin:0 0 10px"><strong>② 「パラメータ 2 個」は指数型ポテンシャルを仮定した見積もりです。</strong> 実際の模型はもっと複雑なポテンシャルや、\(\chi\) と暗黒物質の結合（成長するニュートリノ・クインテッセンスなど）を含み、パラメータは増えます ── <em>10.7 ビットは下限側の見積もり</em>です。</p>
<p style="margin:0 0 10px"><strong>③ 「408 ビット買い戻す」は最大値です。</strong> トラッカー型のクインテッセンスは \(\rho_\Lambda\) の<em>大きさ</em>の微調整を緩和しますが、⑦のとおりポテンシャルのスケールと「なぜ今」問題は残ります。<strong>桁は縮みますが、ゼロにはなりません。</strong> また 408 ビットは第30回の「縛ったビット数」と同じ \(-\log_2\) の読み方で、第5回の MDL の通貨とは<em>厳密には別の量</em>です（第30回④と同じ注意）── 並べたのは大きさの感覚をつかむためです。</p>
<p style="margin:0 0 10px"><strong>④ \(w=-1.03\pm0.03\) は代表的な組み合わせ（Planck + SNe + BAO）による値です。</strong> データセットと仮定する模型（定数 \(w\) か \(w_0w_a\) か）で数字は動きます。<strong>DESI (2024) が動的な暗黒エネルギーを選好する兆候を報告していますが、有意性の評価は現在進行形で、本稿は判定しません。</strong></p>
<p style="margin:0 0 10px"><strong>⑤ 「特異点が消える」かどうかは論争中です。</strong> 曲率不変量が有限に保てることと、測地線が完備であることは別の主張です ── 前者は示せますが、後者は質量を持つ粒子の扱いに依存します（第6回③と同じ注意）。</p>
<p style="margin:0"><strong>⑥ 本稿はコスモン模型を支持も否定もしません。</strong> やったのは、第4回の絵（記法）と比べて<em>何が増えたかを帳簿で数えた</em>ことだけです。</p>
</div>

<div class="prob">
<p class="lbl">練習問題（今回の式だけで解けます）</p>
<ol>
<li>第4回の絵とコスモンの、いちばん本質的な違いは何か。
<details><summary>答えを見る</summary><div class="ans">\(m(t)\) が<strong>「選ばれる」のか「決まる」のか</strong>。第4回は \(a(t)\) を手で置いたので予言ゼロ、コスモンは場の方程式が \(\chi(t)\) を決めるので予言を持ちます。<em>同じ絵でも、記法と理論では別物です。</em></div></details></li>

<li>コスモンが払うビット数と、買い戻せる最大ビット数を求めよ。
<details><summary>答えを見る</summary><div class="ans">払う：パラメータ 2 個 × \(\tfrac12\log_2(1701)=5.37\) ＝ <strong>10.7 ビット</strong>。買い戻す最大：\(-\log_2(1.13\times10^{-123})=\) <strong>408 ビット</strong>（\(\rho_\Lambda/M_{\rm Pl}^4\) の微調整）。<em>だから 2 個くらい安いものです。</em></div></details></li>

<li>コスモンが第28回の VSL のように死なないのはなぜか。
<details><summary>答えを見る</summary><div class="ans"><strong>すべての質量を同じ \(\chi\) が決めるので、質量比が固定される</strong>から。\(\alpha\)（26.1 ビット）、\(m_p/m_e\)（22.8 ビット）、\(m_n/m_p\)（6.6 ビット）の制約に一切ひっかかりません。VSL は \(\alpha\) を動かして正面衝突しました ── <em>比が守られるかどうかで生死が分かれます。</em></div></details></li>

<li>では、コスモンは何で判定されるのか。
<details><summary>答えを見る</summary><div class="ans"><strong>暗黒エネルギーの状態方程式 \(w\)</strong>。観測は \(w=-1.03\pm0.03\) で、事前範囲を \([-2,0]\) と取れば 5.1 ビット縛られています。宇宙定数（\(w=-1\) ちょうど）と動くクインテッセンスの差は、ここに出ます。</div></details></li>

<li>（やや難）記法が理論になると何が増えるか、第25回の言葉で述べよ。
<details><summary>答えを見る</summary><div class="ans"><strong>記法は \(L(\text{法則})\) を短くするだけで、理論は \(L(\text{パラメータ})\) を払って \(L(\text{残差})\) を減らしにいきます。</strong> 第25回で見たとおり、\(L(\text{法則})\) は記述言語に依存するので判定に使えず、使えるのは後ろの二つだけ ── <em>つまり記法は判定の土俵に乗っておらず、理論は乗っている</em>ということです。</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">まとめ　記法が理論になると、土俵に乗る</h2>
<p>第4回の絵とコスモンは、同じ「質量ひとつが動く」絵です。違いは一点 ── <strong>\(m(t)\) が手で置かれるのか、場の方程式で決まるのか</strong>。ヴェッテリヒの模型ではスカラー場 \(\chi\) がすべての粒子質量を決め、<em>同じ \(\chi\) が暗黒エネルギーの役もします</em>。</p>
<p>帳簿にすると、払うのはポテンシャルの <strong>2 パラメータ＝10.7 ビット</strong>。買うのは \(\rho_\Lambda/M_{\rm Pl}^4=1.13\times10^{-123}\) の微調整で、手で合わせるなら <strong>408 ビット</strong>を設定することになります ── <em>アトラクタで説明が付くなら、2 個くらい安いものです</em>。ただし全部は買い戻せません（ポテンシャルのスケール、「なぜ今」問題、結合の強さが残る）。</p>
<p>構造的にいちばん面白いのは、<strong>なぜ第28回の VSL のように死なないか</strong>でした。コスモンは<em>すべての質量を同じ \(\chi\) で決めるので、質量比が固定される</em> ── \(\alpha\)（26.1 ビット）も \(m_p/m_e\)（22.8 ビット）も厳密に不変で、定数の測定に一切ひっかかりません。VSL は \(\alpha\) を動かして正面衝突しました。<strong>同じ「定数が変わる」でも、比が守られるかどうかで生死が分かれます</strong> ── 第3回・第9回で見た構造が、理論の設計原理になっている。</p>
<p>だから判定は<strong>暗黒エネルギーの状態方程式</strong>へ移ります（\(w=-1.03\pm0.03\)、5.1 ビット）。そして種明かし ── 第25回の言葉で言えば、<em>記法は \(L(\text{法則})\) を短くするだけ、理論は \(L(\text{パラメータ})\) を払って \(L(\text{残差})\) を減らしにいく</em>。<strong>土俵が違います</strong>。そして判定に使えるのは、後者だけでした。</p>
</div>

<div class="next">
<span class="lbl">次回予告 ── 第33回</span>
次は<strong>ミルン宇宙と \(R_h=ct\)</strong>です。この二つはどちらも「\(a\propto t\)」に見えますが、<em>まったく別物</em>です ── <strong>ミルンは中身が空っぽの特殊相対論で、座標変換だけで平坦な時空に戻せます</strong>。\(R_h=ct\) は物質が入っていて、戻せません。第3回で「\(c\cdot t=\)一定 は座標変換ではなく共形変換」と書きましたが、今回はその区別を<em>いちばん紛らわしい相手</em>に対して当てます。<strong>座標変換で済むのか、共形変換が要るのか</strong> ── 見分ける手続きを作ります。
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sa=document.getElementById('sa'), va=document.getElementById('va'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=34, Y1=310;
  var xmin=0, xmax=2.0;          // z
  var ymin=-1.25, ymax=-0.55;    // w
  var W0=-1.03, WE=0.03;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  // 指数型ポテンシャルのトラッカー：w ≈ -1 + α²/3 を目安に、z とともに -1 へ近づく形
  function wOf(z,a){
    var dev=a*a/3.0;
    return -1.0 + dev*(1.0 - 0.35/(1.0+z));
  }

  function draw(){
    var a=parseInt(sa.value,10)/100;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px "Hiragino Kaku Gothic ProN","Yu Gothic",sans-serif';

    // 観測の帯
    g.fillStyle='#e6ece6';
    g.fillRect(X0, py(W0+WE), X1-X0, py(W0-WE)-py(W0+WE));
    g.fillStyle='#7d9080'; g.textAlign='left';
    g.fillText('観測の許す帯  w = −1.03 ± 0.03', X0+10, py(W0+WE)-7);

    g.textAlign='right';
    for(var e=-1.2;e<=-0.6;e+=0.1){
      var y=py(e);
      g.strokeStyle='#f1f4f1'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#95a595'; g.fillText(e.toFixed(1), X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=2;q+=0.5){
      var x=px(q);
      g.strokeStyle='#f7faf7'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#95a595'; g.fillText('z = '+q.toFixed(1), x, Y1+16);
    }
    g.strokeStyle='#c6d2c6'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    // 宇宙定数
    g.strokeStyle='#8a6a1a'; g.lineWidth=2.6; g.setLineDash([7,5]);
    g.beginPath(); g.moveTo(X0,py(-1)); g.lineTo(X1,py(-1)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#7a5c16'; g.textAlign='right';
    g.fillText('宇宙定数 w = −1', X1-8, py(-1)+16);

    // コスモン
    g.strokeStyle='#2a4a2a'; g.lineWidth=3.4;
    g.beginPath();
    for(var i=0;i<=200;i++){
      var z=xmin+(xmax-xmin)*i/200;
      var w=wOf(z,a);
      if(i===0) g.moveTo(px(z),py(Math.min(Math.max(w,ymin),ymax)));
      else g.lineTo(px(z),py(Math.min(Math.max(w,ymin),ymax)));
    }
    g.stroke();

    var w0=wOf(0,a);
    g.fillStyle='#2a4a2a';
    g.beginPath(); g.arc(px(0),py(Math.min(Math.max(w0,ymin),ymax)),5.5,0,6.2832); g.fill();
    g.strokeStyle='#fff'; g.lineWidth=1.8;
    g.beginPath(); g.arc(px(0),py(Math.min(Math.max(w0,ymin),ymax)),5.5,0,6.2832); g.stroke();

    g.fillStyle='#7d8d7d'; g.textAlign='center';
    g.fillText('赤方偏移  z', (X0+X1)/2, Y1+38);
    g.save(); g.translate(19,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('状態方程式  w', 0,0); g.restore();

    var inband = Math.abs(w0-W0)<=WE;
    va.textContent='α = '+a.toFixed(2);
    ro.textContent='α = '+a.toFixed(2)+'　→　今日の w = '+w0.toFixed(3)+
      '　'+(inband? '★ 観測の帯の中（区別できない）' : '観測の帯の外 ── この α は排除される')+
      '　／　α = 0 なら宇宙定数（w = −1）に一致';
  }
  sa.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-32-cosmon.html', acc='#2a4a2a', ops='#8a6a1a',
      title='ヴェッテリヒのコスモン ── わかる c·t=一定 第32回',
      ep='第 32 回 ／ 第 IV 部・記法が理論になると、何が増えるのか',
      eyebrow='第4回の絵を、場の理論として実装するとこうなります',
      h1='ヴェッテリヒの<br>コスモン',
      sub='質量を育てるスカラー場が、そのまま暗黒エネルギーの役をします。<br><em>払うのは 10.7 ビット、買い戻せるのは最大 408 ビット。</em>',
      byline_l='必要な道具：第5回の天秤、第12回の \\(\\rho_\\Lambda\\)、第30回の制約',
      byline_r='比が守られるから、\\(\\alpha\\) の 26 ビットに衝突しない',
      body=BODY + '\n\n<p class="foot">この文書は「わかる c·t=一定」シリーズ第32回、物理好きの高校生・大学生向け読み物です。コスモン／クインテッセンスは Wetterich (1988, Nucl. Phys. B302, 668)、質量が育つ描像での宇宙論は Wetterich (2013, Phys. Dark Univ. 2, 184「A Universe without expansion」) によります。<strong>本稿は具体的な模型を一つに固定せず、「すべての質量を一つのスカラー場が決める」という構造だけを扱っています</strong> ── 実際の模型には多くの変種があります。「パラメータ 2 個」は指数型ポテンシャル \\(V=M^4e^{-\\alpha\\chi/M}\\) を仮定した見積もりで、より複雑なポテンシャルや \\(\\chi\\) と暗黒物質の結合（成長するニュートリノ・クインテッセンス）を含む模型ではパラメータが増えます ── <em>10.7 ビットは下限側の見積もり</em>です。「408 ビット買い戻す」は最大値で、トラッカー型は \\(\\rho_\\Lambda\\) の大きさの微調整を緩和しますが、ポテンシャルのスケールと「なぜ今」問題は残ります ── <strong>桁は縮みますがゼロにはなりません</strong>。また 408 ビットは第30回の「縛ったビット数」と同じ \\(-\\log_2\\) の読み方で、第5回の MDL の通貨とは厳密には別の量です（第30回④と同じ注意）。\\(w=-1.03\\pm0.03\\) は Planck + SNe + BAO による代表的な値で、データセットと仮定する模型で数字は動きます ── <strong>DESI (2024) が動的な暗黒エネルギーを選好する兆候を報告していますが、有意性の評価は現在進行形であり本稿は判定しません</strong>。図の \\(w(z)\\) は指数型トラッカーの振る舞いを模した<em>模式</em>で、具体的な模型の数値解ではありません。原子時計・分子時計・元素合成による無次元比の制約は第30回のとおりです。「特異点が消える」かどうかは論争中で、曲率不変量が有限に保てることと測地線が完備であることは別の主張です（第6回③）。<strong>本稿はコスモン模型を支持も否定もせず</strong>、第4回の絵（記法）と比べて何が増えたかを帳簿で数えたものです。学術的な標準はインフレーションを含む \\(\\Lambda\\)CDM モデルです。 ── 印刷する場合はブラウザの「印刷」から「PDF に保存」を（印刷版ではスライダーと解答は静止・非表示になります）。</p>',
      script=SCRIPT,
      hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。画面ではスライダーでポテンシャルの傾きを変え、w が観測の帯を出入りする様子が見えます。「答えを見る」で解答が開きます。')
