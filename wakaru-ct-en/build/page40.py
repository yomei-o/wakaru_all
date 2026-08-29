# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 39 counted a solar-mass black hole as holding \(1.5\times10^{77}\) bits of entropy. <strong>Information about what, exactly?</strong> This time we count again for the whole universe — and find that <em>three separate "\(10^{122}\)" headline numbers are in fact one and the same</em>. The compression of Episode 26 works again.</p>

<h2><span class="n">01</span>Gravitational entropy sits entirely in the weight-0 column</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Weight</th><th class="mid">What it is</th></tr></thead>
<tbody>
<tr class="hi"><th>\(S/k_B=A/4\ell_P^2\)</th><td class="mid">\(+2-(+2)=\mathbf{0}\)</td><td class="mid">an area divided by an area</td></tr>
<tr><th>Bekenstein bound \(2\pi ER/\hbar c\)</th><td class="mid">\(-1+1-0=\mathbf{0}\)</td><td class="mid">energy × length</td></tr>
<tr><th>Weyl\(^2\)/Ricci\(^2\) (Penrose)</th><td class="mid">\(-4-(-4)=\mathbf{0}\)</td><td class="mid">curvature\(^2\) divided by curvature\(^2\)</td></tr>
<tr><th>\(K\cdot r_s^4\) (Kretschmann × radius\(^4\))</th><td class="mid">\(-4+4=\mathbf{0}\)</td><td class="mid">used in §07</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>The whole subject of gravitational entropy lives in the dimensionless column.</strong><br>
── <em>As §03 of Episode 36 found: it reaches the arena where it can be judged.</em></p>
</div>

<h2><span class="n">02</span>The Hubble sphere sits exactly at its own Schwarzschild radius</h2>

<div class="calc">
<span class="tag">Count it (with \(H_0=67.4\))</span>
$$R_H=\frac{c}{H_0}=1.3725\times10^{26}\ \text{m}\qquad
M=\rho_cV=9.241\times10^{52}\ \text{kg}\qquad
r_s=\frac{2GM}{c^2}=1.3725\times10^{26}\ \text{m}$$
<p class="lbl">\(r_s/R_H=1.000000\)</p>
</div>

<div class="calc">
<span class="tag">Why it is exactly 1</span>
$$r_s=\frac{2G}{c^2}\cdot\frac{4}{3}\pi R^3\cdot\frac{3H^2}{8\pi G}=\frac{R^3H^2}{c^2}=R\qquad(\text{because }R=c/H)$$
</div>

<p><strong>Not a coincidence but an identity.</strong> On Episode 19's scale, <strong>0 bits</strong> — <em>nothing to be surprised by.</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>The core — three "\(10^{122}\)" numbers are one number</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Value</th></tr></thead>
<tbody>
<tr><th>Holographic bound \(A/4\ell_P^2\)</th><td class="mid">\(2.265\times10^{122}\) nat \(=3.268\times10^{122}\) bit</td></tr>
<tr><th>\(S/k_B\) if all the mass were one black hole</th><td class="mid">\(2.265\times10^{122}\) nat</td></tr>
<tr class="hi"><th>Episode 24's \(N=C\cdot t_0\)</th><td class="mid"><strong>\(3.107\times10^{122}\) bit</strong></td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">Take the ratios</span>
$$\frac{S_{\rm BH}}{S_{\rm holo}}=1.000000\quad(\text{an identity, by }\S02)\qquad
\frac{N}{S_{\rm holo}/\ln2}=0.9505$$
<p class="lbl">and the gap is exactly \(t_0/(R_H/c)=0.9505\) — <strong>the difference between the age of the universe and the Hubble time</strong></p>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>The three headline numbers were one.</strong><br>
"How much information the universe has processed" (Episode 24) and "how much information the universe can hold" (the holographic bound) are the <em>same number</em>,<br>
and the 5 per cent gap is <strong>the ratio of the age to the Hubble time</strong>, nothing else.<br>
── On Episode 19's scale, <strong>0 bits</strong>. <em>Episode 26's compression worked again.</em></p>
</div>

<h2><span class="n">04</span>So what is the actual entropy?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Component</th><th class="mid">\(S/k_B\)</th><th class="mid">Fraction</th></tr></thead>
<tbody>
<tr class="hi"><th>Supermassive black holes</th><td class="mid"><strong>\(3.10\times10^{104}\)</strong></td><td class="mid"><strong>\(1.00\)</strong></td></tr>
<tr><th>Stellar-mass black holes</th><td class="mid">\(2.20\times10^{96}\)</td><td class="mid">\(7.1\times10^{-9}\)</td></tr>
<tr><th>CMB photons</th><td class="mid">\(2.03\times10^{89}\)</td><td class="mid">\(6.6\times10^{-16}\)</td></tr>
<tr><th>Relic neutrinos</th><td class="mid">\(1.93\times10^{89}\)</td><td class="mid">\(6.2\times10^{-16}\)</td></tr>
<tr><th>Relic gravitational waves</th><td class="mid">\(2.3\times10^{87}\)</td><td class="mid">\(7.4\times10^{-18}\)</td></tr>
<tr><th>Stars, interstellar medium etc.</th><td class="mid">\(2.6\times10^{81}\)</td><td class="mid">\(8.4\times10^{-24}\)</td></tr>
</tbody>
</table>
</div>

<p>These are Egan &amp; Lineweaver's (2010) estimates. <strong>99.999… per cent of it is already gravitational entropy — horizon entropy.</strong> Everything that is not a black hole sums to \(3.8\times10^{89}\), which is <em>49.5 bits (15 orders of magnitude) below the black holes.</em></p>

<h2><span class="n">05</span>How much of the capacity is in use?</h2>

<div class="calc">
<span class="tag">Actual versus bound</span>
$$\frac{3.10\times10^{104}}{2.27\times10^{122}}=1.4\times10^{-18}
\qquad\Longrightarrow\qquad \textbf{59.3 bits of headroom}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>The ladder of doublings</th><th class="mid">\(S/k_B\)</th><th class="mid">\(\log_2 S\)</th></tr></thead>
<tbody>
<tr><th>Around recombination (CMB + neutrinos)</th><td class="mid">\(3.96\times10^{89}\)</td><td class="mid">\(297.6\)</td></tr>
<tr><th>Today (total)</th><td class="mid">\(3.10\times10^{104}\)</td><td class="mid">\(347.1\)</td></tr>
<tr class="hi"><th>The bound (holographic)</th><td class="mid">\(2.27\times10^{122}\)</td><td class="mid"><strong>\(406.5\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>49.5 doublings</strong> from the beginning until now; <strong>59.3 doublings</strong> from now to the bound.<br>
── <em>The universe is not even halfway along.</em></p>
</div>

<div class="fig">
<p class="cap">Figure: the ladder of entropy doublings. <strong>The horizontal axis is \(\log_2 S\) — how many times the entropy has doubled.</strong> Move the slider to see where today's universe sits — <em>the headroom is longer than the road already travelled.</em></p>
<canvas id="cv" width="720" height="330"></canvas>
<div class="controls">
  <label>position in doublings (\(\log_2 S\))<input id="sl" type="range" min="290" max="410" value="347" step="1"></label>
  <span class="val" id="vl">347</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a6a"></i>road travelled (49.5 doublings)</span>
  <span><i class="swatch" style="background:#d8d2dc"></i>headroom (59.3 doublings)</span>
  <span><i class="swatch" style="background:#a05a2a"></i>current position</span>
</div>
</div>

<h2><span class="n">06</span>What the headroom is — gravity's degrees of freedom are not thermalised</h2>

<div class="seven">
<div class="row"><div class="mk">?</div><div class="txt"><strong>Why is the headroom not used?</strong><span>the capacity is there, yet only one part in \(10^{18}\) is taken up</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>Because gravity only attracts</strong><span>a uniform gas is at <em>maximum</em> entropy; <strong>a uniform gravitational field is at minimum entropy</strong> — the sign is reversed</span></div></div>
<div class="row"><div class="mk">→</div><div class="txt"><strong>So "the entropy of the gravitational field itself" needs its own measure</strong><span>and the candidate is the <em>Weyl curvature</em> from Episode 39</span></div></div>
</div>

<h2><span class="n">07</span>Penrose's candidate, and its weakness</h2>

<div class="calc">
<span class="tag">The proposal: gravitational entropy is gauged by</span>
$$\frac{C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}}{R_{\mu\nu}R^{\mu\nu}}\qquad\text{(dimensionless, weight 0)}$$
</div>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>FLRW: Weyl is exactly 0, so the ratio is 0</strong><span>the early universe has zero gravitational entropy — <em>exactly the property wanted</em></span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>A lumpy universe: Weyl grows, so the ratio rises</strong><span>structure formation by gravity is itself the increase in entropy</span></div></div>
<div class="row hi"><div class="mk">✗</div><div class="txt"><strong>But in vacuum Ricci \(=0\), so the ratio diverges</strong><span>Schwarzschild and Kerr are vacuum — <em>it breaks on exactly the cases whose gravitational entropy should be highest</em></span></div></div>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Black hole</th><th class="mid">\(r_s\) [m]</th><th class="mid">\(K\) [m\(^{-4}\)]</th><th class="mid">\(K\cdot r_s^4\)</th></tr></thead>
<tbody>
<tr><th>Solar mass</th><td class="mid">\(2.954\times10^{3}\)</td><td class="mid">\(1.576\times10^{-13}\)</td><td class="mid"><strong>\(12.0\)</strong></td></tr>
<tr class="hi"><th>M87\(^*\) (\(6.5\times10^9\,M_\odot\))</th><td class="mid">\(1.920\times10^{13}\)</td><td class="mid">\(8.828\times10^{-53}\)</td><td class="mid"><strong>\(12.0\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §07</p>
<p style="margin:6px 0 0"><strong>The Weyl side is finite and dimensionless</strong> — at the horizon \(K\cdot r_s^4=12\), <em>the same 12 whatever the mass</em>.<br>
What breaks is the dividing by Ricci.<br>
── The ratio form works in cosmology but <strong>not in vacuum</strong>. Alternative definitions have been proposed (Clifton–Ellis–Tavakol 2013 among them).</p>
</div>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) §04's figures are order-of-magnitude estimates.</strong> Egan &amp; Lineweaver themselves assign a large uncertainty to the supermassive black hole entropy (it depends on extrapolating the mass function) — <em>\(3.1\times10^{104}\) is a central value that can move by an order of magnitude either way</em>, and §05's "59.3 doublings" moves with it.</p>
<p style="margin:0 0 10px"><strong>(2) §03's "the same number" refers to counting on the Hubble sphere.</strong> Count on the particle horizon (about \(4.4\times10^{26}\) m) and the value is roughly ten times larger; the event horizon gives another answer — <em>"which horizon?" has to be named or the number is not yet a sentence</em> (the same structure as Episode 3 and Episode 37 §05). The identity \(r_s=R_H\) in §02 holds <strong>only for the Hubble sphere at critical density</strong>.</p>
<p style="margin:0 0 10px"><strong>(3) §05's "bound" is the holographic bound</strong>, but which surface it should be applied to in an expanding universe is not obvious (Bousso's covariant entropy bound is one formulation) — <em>"the universe uses \(10^{-18}\) of its capacity" is the statement for the naive form of the bound.</em></p>
<p style="margin:0 0 10px"><strong>(4) §07's \(C^2/R^2\) is the most naive way of writing Penrose's idea.</strong> Penrose did not propose this ratio as a final definition; it is <em>the widely quoted gauge for the idea that Weyl curvature measures gravitational entropy</em>. Its divergence in vacuum is a weakness of the naive form, and later proposals try to repair exactly that.</p>
<p style="margin:0"><strong>(5) There is still no agreed definition of "the entropy of the gravitational field".</strong> The black-hole entropy \(A/4\ell_P^2\) is established, but <em>the general case without a horizon is unresolved</em> — §06 states the problem, not an answer.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>What is the ratio of the Hubble radius to the Schwarzschild radius of the mass it contains?
<details><summary>Show the answer</summary><div class="ans"><strong>Exactly 1.</strong> At critical density, \(r_s=\frac{2G}{c^2}\cdot\frac43\pi R^3\cdot\frac{3H^2}{8\pi G}=\frac{R^3H^2}{c^2}=R\). <em>Not a coincidence but an identity</em>, so <strong>0 bits</strong> on Episode 19's scale — though per caveat (2) it holds only for the Hubble sphere at critical density.</div></details></li>

<li>Episode 24's \(N=C\cdot t_0\) is 0.95 of the holographic bound. What is the 5 per cent?
<details><summary>Show the answer</summary><div class="ans"><strong>The ratio of the age of the universe to the Hubble time</strong>, \(t_0/(R_H/c)=0.9505\), exactly. So the two are <em>the same number</em>, and even the gap is accounted for — <strong>Episode 26's compression working again</strong>.</div></details></li>

<li>What fraction of the universe's entropy is in black holes?
<details><summary>Show the answer</summary><div class="ans"><strong>99.999… per cent.</strong> Everything else sums to \(3.8\times10^{89}\), which is <em>49.5 bits (15 orders) below</em> the total \(3.1\times10^{104}\). <strong>The entropy of the universe is already almost entirely gravitational.</strong></div></details></li>

<li>Why is only \(10^{-18}\) of the capacity used?
<details><summary>Show the answer</summary><div class="ans"><strong>Because gravity only attracts.</strong> A uniform gas is at <em>maximum</em> entropy, but <strong>a uniform gravitational field is at minimum entropy</strong> — the sign is reversed. So gravity's degrees of freedom cannot sit at thermal equilibrium, and headroom remains.</div></details></li>

<li>(Harder) What is the weakness of \(C^2/R^2\)? Put it in numbers.
<details><summary>Show the answer</summary><div class="ans"><strong>It diverges in vacuum.</strong> Schwarzschild and Kerr have Ricci \(=0\), so the denominator vanishes. <em>The Weyl side is healthy</em>: at the horizon \(K\cdot r_s^4\) is <strong>12.0</strong> for both a solar-mass hole and M87\(^*\) — finite and dimensionless. Only the dividing by Ricci is broken.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: the three headline numbers were one</h2>
<p>The subject of gravitational entropy sits <strong>entirely in the weight-0 column</strong> — \(A/4\ell_P^2\), the Bekenstein bound, \(C^2/R^2\), \(K\,r_s^4\), all dimensionless.</p>
<p>Counting it out, <strong>the Hubble sphere sits exactly at its own Schwarzschild radius</strong> (\(r_s/R_H=1.000000\)) — an identity at critical density, worth 0 bits on Episode 19's scale. Because of it, <strong>three \(10^{122}\) numbers coincide</strong>: the holographic bound, the entropy of the total mass as one black hole, and Episode 24's \(N=C\cdot t_0\). <em>"How much the universe has processed" and "how much the universe can hold" are the same number, and the 5 per cent gap is exactly the ratio of the age to the Hubble time.</em> <strong>Episode 26's compression worked again.</strong></p>
<p>And the actual entropy? \(3.1\times10^{104}\), of which <strong>99.999… per cent is supermassive black holes</strong> — the entropy of the universe is already almost entirely gravitational. Against the bound that is \(1.4\times10^{-18}\), i.e. <strong>59.3 doublings of headroom</strong>. Since the road from the beginning to now was 49.5 doublings, <em>the universe is not even halfway along.</em></p>
<p>The headroom survives because <strong>gravity only attracts</strong> — a uniform gas is at maximum entropy, <em>a uniform gravitational field at minimum</em>. So "the entropy of the gravitational field itself" needs its own measure, and the candidate is the <strong>Weyl curvature</strong>. Penrose's naive form \(C^2/R^2\) has the property one wants — exactly zero for FLRW — but <strong>diverges in vacuum, where the denominator goes to zero</strong>. The Weyl side is healthy: at the horizon \(K\,r_s^4\) is <strong>12.0</strong> regardless of mass. Only the dividing by Ricci is broken.</p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 41</span>
This time we found that the early universe's gravitational entropy is <strong>exactly zero</strong> (FLRW has Weyl \(=0\)). Next time we look at a proposal that <em>turns that into a requirement</em> — the <strong>Weyl curvature hypothesis</strong>. Penrose demanded, as a law, that Weyl \(=0\) at initial singularities. <em>Why is it needed, and how special a demand is it?</em> As always, we <strong>measure it in bits</strong> — and count out what the famous number \(10^{10^{123}}\) actually is.
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sl=document.getElementById('sl'), vl=document.getElementById('vl'), ro=document.getElementById('ro');
  var X0=70, X1=690, YB=178;
  var L0=290, L1=410, INIT=297.6, NOW=347.1, MAX=406.5;

  function px(v){ return X0+(v-L0)/(L1-L0)*(X1-X0); }

  function draw(){
    var p=parseInt(sl.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.fillStyle='#d8d2dc';
    g.fillRect(px(NOW), YB-24, px(MAX)-px(NOW), 48);
    g.fillStyle='#2a5a6a';
    g.fillRect(px(INIT), YB-24, px(NOW)-px(INIT), 48);

    g.textAlign='center';
    var marks=[[INIT,'recombination','3.96e89'],[NOW,'today','3.10e104'],[MAX,'the bound','2.27e122']];
    for(var i=0;i<marks.length;i++){
      var X=px(marks[i][0]);
      g.strokeStyle='#8a8494'; g.lineWidth=1.4;
      g.beginPath(); g.moveTo(X,YB-40); g.lineTo(X,YB+40); g.stroke();
      g.fillStyle='#3a3640'; g.fillText(marks[i][1], X, YB-50);
      g.fillStyle='#9c96a4'; g.fillText(marks[i][2], X, YB+58);
      g.fillText('log2 S = '+marks[i][0].toFixed(1), X, YB+74);
    }

    g.fillStyle='#fff'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('49.5 doublings', (px(INIT)+px(NOW))/2, YB+5);
    g.fillStyle='#6a6274';
    g.fillText('59.3 doublings of headroom', (px(NOW)+px(MAX))/2, YB+5);

    var X=px(p);
    g.strokeStyle='#a05a2a'; g.lineWidth=2.4;
    g.beginPath(); g.moveTo(X,YB-46); g.lineTo(X,YB+46); g.stroke();
    g.fillStyle='#a05a2a';
    g.beginPath(); g.arc(X,YB,5.5,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('number of entropy doublings  (log2 S)', (X0+X1)/2, YB+110);

    vl.textContent=String(p);
    var S=Math.pow(2,p);
    var pos = p<INIT ? 'before recombination' : (p<NOW ? 'along the road travelled' : (p<MAX ? 'inside the headroom' : 'past the bound (unreachable)'));
    ro.textContent='log2 S = '+p+'　→　S = '+S.toExponential(2)+' k_B　/　'+pos+
      '　/　'+(p-INIT).toFixed(1)+' doublings so far, '+(MAX-p).toFixed(1)+' left to the bound'+
      (Math.abs(p-NOW)<1?'　★ this is where the universe is now':'');
  }
  sl.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-40-gravity-entropy.html', acc='#2a5a6a', ops='#a05a2a',
      title='Gravitational entropy ── c·t = const, That Clicks, Episode 40 (Part V)',
      ep='EPISODE 40 ／ Part V — where the tool breaks',
      eyebrow='Three "10^122" numbers turned out to be one',
      h1='Not even<br>halfway along',
      sub='What the universe has processed and what the universe can hold are the same number.<br><em>And what it actually uses is \\(10^{-18}\\) of that.</em>',
      byline_l='What you need: Episode 19\'s scale, Episode 24\'s channel capacity, Episode 26\'s compression, Episode 39\'s Weyl',
      byline_r='59.3 doublings of headroom — 49.5 travelled',
      body=BODY + '\n\n<p class="foot">This document is Episode 40 of "c·t = const, That Clicks" (the fourth of Part V), written for physics-minded high-school and university readers. Bekenstein–Hawking entropy, the holographic bound, and Penrose\'s idea of gauging gravitational entropy by Weyl curvature are all standard, and nothing here is a new claim — the numbers are computed in kenshou/calc44.py. <strong>§04\'s figures are from Egan &amp; Lineweaver (2010, ApJ 710, 1825) and carry a large uncertainty on the supermassive black hole entropy</strong> (it depends on extrapolating the mass function); \\(3.1\\times10^{104}\\) is a central value that can move an order of magnitude either way, and §05\'s "59.3 doublings" moves with it. <strong>§03\'s "the same number" refers to counting on the Hubble sphere</strong>; the particle horizon (about \\(4.4\\times10^{26}\\) m) gives roughly ten times more — <em>"which horizon?" must be named or the number is not yet a sentence</em>. The identity \\(r_s=R_H\\) in §02 holds only for the Hubble sphere at critical density. §05\'s bound is the holographic one, but <strong>which surface it applies to in an expanding universe is not obvious</strong> (Bousso\'s covariant entropy bound is one formulation), so this is the statement for the naive form. <strong>§07\'s \\(C^2/R^2\\) is the most naive way of writing Penrose\'s idea</strong> and not a final definition he proposed — the vacuum divergence is a weakness of that naive form, which later proposals (Clifton–Ellis–Tavakol 2013 among them) try to repair. <strong>There is still no agreed definition of "the entropy of the gravitational field"</strong> away from horizons — §06 states the problem, not an answer. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the slider and see that the headroom is longer than the road travelled. "Show the answer" opens each solution.')
