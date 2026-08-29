# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episodes 37 and 38 looked at where conformal transformations <em>break</em> when applied to quantum theory and to gravity. This time we change the view and look at <strong>rotating spacetime</strong> — the Kerr solution. A black hole carries two labels, \(M\) and \(\chi=a/(GM/c^2)\), and <em>only one of them is bookkeeping</em>. It is the <strong>cleanest example</strong> of Part II's conclusion, "a conformal transformation touches only size". And the bound \(\chi\le1\) is <em>a line placed in the untouchable column — one that cannot be rewritten.</em></p>

<h2><span class="n">01</span>Putting Kerr's two labels on the weight table</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Weight</th><th class="mid">Class</th><th class="mid">Conformal transformation</th></tr></thead>
<tbody>
<tr><th>Mass \(M\)</th><td class="mid">\(-1\)</td><td class="mid">dimensionful = bookkeeping</td><td class="mid">moves</td></tr>
<tr class="hi"><th>Angular momentum \(J\sim ML^2/T\)</th><td class="mid">\(-1+2-1=\mathbf{0}\)</td><td class="mid"><strong>dimensionless = physics</strong></td><td class="mid"><strong>does not move</strong></td></tr>
<tr><th>Spin length \(a=J/(Mc)\)</th><td class="mid">\(0-(-1)-0=+1\)</td><td class="mid">a length = bookkeeping</td><td class="mid">moves</td></tr>
<tr><th>Gravitational radius \(GM/c^2\) (\(G\) is \(+2\))</th><td class="mid">\(+2-1=+1\)</td><td class="mid">a length = bookkeeping</td><td class="mid">moves</td></tr>
<tr class="hi"><th>Spin \(\chi=a/(GM/c^2)\)</th><td class="mid">\(+1-1=\mathbf{0}\)</td><td class="mid"><strong>dimensionless = physics</strong></td><td class="mid"><strong>does not move</strong></td></tr>
</tbody>
</table>
</div>

<div class="aside">
<span class="tag">A check</span>
Angular momentum is measured in units of \(\hbar\), and \(\hbar\) has weight 0 (Episode 16).<br>
That agrees with the independent count \(-1+2-1=0\) — <em>the table is not inconsistent.</em>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>Kerr carries two labels, \((M,\chi)\). Only one is bookkeeping; the other is physics.</strong><br>
── <em>The cleanest example of Part II's "a conformal transformation touches only size".</em></p>
</div>

<h2><span class="n">02</span>How much of that is notation?</h2>

<div class="calc">
<span class="tag">Counted with Episode 5's price</span>
$$2\times5.37=10.7\ \text{bits}\qquad\text{of which }M\text{'s }5.37\ \text{bits are }\textbf{entirely notation}$$
</div>

<p><strong>Half of the information in the Kerr solution was information about how it is written.</strong> Change the units and \(M\)'s number changes, but \(\chi\) does not — <em>the physics lives in the other 5.37 bits alone.</em></p>

<h2><span class="n">03</span>\(\chi\le1\) — a bound placed in the untouchable column</h2>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>Kerr has a horizon only when \(\chi\le1\)</strong><span>above that the horizon disappears and a naked singularity remains (cosmic censorship)</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>The bound sits in a dimensionless quantity</strong><span>the weight-0 column — <em>no conformal transformation can carry a black hole across that line</em></span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>Put in Episode 3's language</strong><span>the claim sits in a dimensionless quantity, so <em>it reaches the arena where it can be judged</em></span></div></div>
</div>

<h2><span class="n">04</span>Horizon area and entropy</h2>

<div class="calc">
<span class="tag">Area ratio at fixed \(M\)</span>
$$\frac{A(\chi)}{A(0)}=\frac{1+\sqrt{1-\chi^2}}{2}$$
<p class="lbl">for a solar-mass Schwarzschild hole, \(S/k_B=4\pi GM^2/\hbar c=1.05\times10^{77}\) → \(\mathbf{1.51\times10^{77}}\) bits</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(\chi\)</th><th class="mid">\(A/A(0)\)</th><th class="mid">Entropy [bits]</th><th class="mid">Extractable mass fraction</th></tr></thead>
<tbody>
<tr><th class="mid">\(0\)</th><td class="mid">\(1.0000\)</td><td class="mid">\(1.51\times10^{77}\)</td><td class="mid">\(0\)</td></tr>
<tr><th class="mid">\(0.5\)</th><td class="mid">\(0.9330\)</td><td class="mid">\(1.41\times10^{77}\)</td><td class="mid">\(0.0341\)</td></tr>
<tr><th class="mid">\(0.686\)</th><td class="mid">\(0.8638\)</td><td class="mid">\(1.31\times10^{77}\)</td><td class="mid">\(0.0706\)</td></tr>
<tr><th class="mid">\(0.9\)</th><td class="mid">\(0.7179\)</td><td class="mid">\(1.09\times10^{77}\)</td><td class="mid">\(0.1527\)</td></tr>
<tr><th class="mid">\(0.998\)</th><td class="mid">\(0.5316\)</td><td class="mid">\(8.05\times10^{76}\)</td><td class="mid">\(0.2709\)</td></tr>
<tr class="hi"><th class="mid">\(1\)</th><td class="mid"><strong>\(0.5000\)</strong></td><td class="mid"><strong>\(7.57\times10^{76}\)</strong></td><td class="mid"><strong>\(0.29289\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0"><strong>A \(\chi=1\) Kerr hole has <em>exactly half</em> the entropy of a Schwarzschild hole of the same mass.</strong><br>
And the maximum extractable mass fraction is \(1-1/\sqrt2=\mathbf{0.29289}\) — <em>dimensionless too, untouchable too.</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">05</span>The core — measured spins line up just below the bound</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Object or value</th><th class="mid">\(\chi\)</th><th>note</th></tr></thead>
<tbody>
<tr><th>GRS 1915+105 (continuum fitting)</th><td class="mid">\(0.98\)</td><td>other analyses report around 0.7</td></tr>
<tr><th>Cyg X-1 (continuum fitting)</th><td class="mid">\(0.95\)</td><td>same caveat; <em>strongly model-dependent</em></td></tr>
<tr><th>GW150914 remnant</th><td class="mid">\(0.67\)</td><td>from the waveform</td></tr>
<tr><th>Equal-mass, non-spinning merger (theory)</th><td class="mid">\(0.686\)</td><td>numerical relativity</td></tr>
<tr class="hi"><th>Thorne limit (reachable by accretion)</th><td class="mid"><strong>\(0.998\)</strong></td><td><strong>photon capture keeps it below 1</strong></td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">Surprise, by Episode 19's practice (prior range \(\chi\in[0,1]\))</span>
$$\text{high-spin sources within }0.05\text{ of the bound}\;\to\;4.3\ \text{bits}\qquad
\text{Thorne limit within }0.002\;\to\;9.0\ \text{bits}$$
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>High-spin sources give 4.3 bits — back inside Episode 36's "band of coincidences" (4 to 7).</strong><br>
But <em>there is an explanation</em> (accretion delivers angular momentum; photon capture keeps it under 1).<br>
── So Episode 19 classifies it not as coincidence but as <strong>physics</strong>: another member of the "explained, 4 to 7 bits" family from Episode 36.</p>
</div>

<div class="fig">
<p class="cap">Figure: horizon area, entropy and extractable mass as the spin \(\chi\) varies. <strong>All of these are dimensionless relations and a conformal transformation moves none of them.</strong> The vertical lines mark measured spins and the Thorne limit — <em>they sit just below the bound.</em></p>
<canvas id="cv" width="720" height="390"></canvas>
<div class="controls">
  <label>spin \(\chi\)<input id="sc" type="range" min="0" max="1000" value="686" step="1"></label>
  <span class="val" id="vc">0.686</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#7a5a2a"></i>horizon area A/A(0)</span>
  <span><i class="swatch" style="background:#2a6a5a"></i>extractable mass fraction</span>
  <span><i class="swatch" style="background:#a03a3a"></i>Hawking temperature T/T(0)</span>
</div>
</div>

<h2><span class="n">06</span>The trouble with extremal Kerr</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(\chi\)</th><th class="mid">\(T/T(0)\)</th></tr></thead>
<tbody>
<tr><th class="mid">\(0\)</th><td class="mid">\(1.00000\)</td></tr>
<tr><th class="mid">\(0.5\)</th><td class="mid">\(0.92820\)</td></tr>
<tr><th class="mid">\(0.9\)</th><td class="mid">\(0.60714\)</td></tr>
<tr><th class="mid">\(0.99\)</th><td class="mid">\(0.24726\)</td></tr>
<tr><th class="mid">\(0.999\)</th><td class="mid">\(0.08559\)</td></tr>
<tr class="hi"><th class="mid">\(1\)</th><td class="mid"><strong>\(0\)</strong></td></tr>
</tbody>
</table>
</div>

<p>As \(\chi\to1\) the <strong>temperature goes to zero while the entropy stays finite at half</strong>. An entropy of \(7.6\times10^{76}\) bits surviving at zero temperature <em>collides with the naive form of the third law of thermodynamics</em>. The escape is that \(\chi=1\) cannot be reached in a finite number of operations (Israel 1986). <strong>Like Episode 4's "coarse-graining is irreversible", it is a line you can approach but not reach.</strong></p>

<h2><span class="n">07</span>Kerr is a spacetime the conformal tool cannot reach</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Step</th><th class="mid">Example</th><th class="mid">Meaning</th></tr></thead>
<tbody>
<tr><th>Riemann \(=0\)</th><td class="mid">Minkowski</td><td class="mid">flat by a coordinate change alone</td></tr>
<tr><th>Weyl \(=0\) (conformally flat)</th><td class="mid"><strong>every FLRW</strong></td><td class="mid">flat by a conformal transformation</td></tr>
<tr class="hi"><th>Weyl \(\ne0\)</th><td class="mid"><strong>Schwarzschild, Kerr</strong></td><td class="mid"><strong>flat by neither</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §07</p>
<p style="margin:6px 0 0">Every spacetime this series has handled <strong>on the cosmological side</strong> was <strong>Step 2</strong> (Episode 33).<br>
Kerr is <strong>Step 3</strong> — <em>the case where the conformal tool stops reaching, outside cosmology.</em><br>
It is Petrov type D, and its Weyl curvature cannot be made to vanish.</p>
</div>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) Every spin measurement in §05 is strongly model-dependent.</strong> Continuum fitting and iron-line (reflection) methods disagree for some objects — <em>GRS 1915+105 is reported both as 0.98 and as around 0.7</em>. The statement "high-spin sources line up just below the bound" <strong>lists only the measurements that reported high spin</strong>; low-spin reports exist, so the selection is biased (the same structure as Episode 36, caveat 2).</p>
<p style="margin:0 0 10px"><strong>(2) §05's 4.3 bits assumes a uniform prior over \(\chi\in[0,1]\).</strong> Put accretion theory into the prior and the distribution is no longer uniform, so the surprise shrinks — <em>in Episode 19's framework, "there is an explanation" and "the surprise is small" are two ways of saying the same thing.</em></p>
<p style="margin:0 0 10px"><strong>(3) §04's table compares holes of the same \(M\).</strong> It is not a <em>process</em> in which "spinning it up lowers the entropy" — spinning it up injects energy along with angular momentum, so \(M\) changes, and by the area theorem the area does not decrease in an actual process.</p>
<p style="margin:0 0 10px"><strong>(4) Cosmic censorship is a hypothesis, not a theorem.</strong> There is no proof in the general case, and candidate counterexamples (instabilities in higher dimensions, among others) are discussed in numerical relativity — <em>§03's "cannot carry across" means that within the Kerr family \(\chi\le1\) is the condition for a horizon to exist.</em></p>
<p style="margin:0"><strong>(5) §02's "half the information is notation" uses Episode 5's price</strong> (one parameter = 5.37 bits), a number that came from a particular dataset size \(N=1701\) — <em>the structure "one of the two labels is notation" is the substance</em>; the bit count is an incidental conversion.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>What is the conformal weight of angular momentum \(J\)? Check it two ways.
<details><summary>Show the answer</summary><div class="ans"><strong>0</strong>. (i) From dimensions: \(J\sim ML^2/T\) gives \(-1+2(+1)-(+1)=0\). (ii) \(J\) is measured in units of \(\hbar\), and \(\hbar\) has weight 0 (Episode 16). <em>The two agreeing is the check.</em></div></details></li>

<li>Of Kerr's two labels, which one does a conformal transformation move?
<details><summary>Show the answer</summary><div class="ans">Only \(M\) (weight \(-1\)). \(\chi=a/(GM/c^2)\) has weight 0 and <strong>does not move</strong> — <em>the cleanest example of Part II's "a conformal transformation touches only size"</em>.</div></details></li>

<li>How does a \(\chi=1\) Kerr hole's entropy compare with a Schwarzschild hole of the same mass?
<details><summary>Show the answer</summary><div class="ans"><strong>Exactly half</strong>, because \(A(\chi)/A(0)=(1+\sqrt{1-\chi^2})/2\) equals \(1/2\) at \(\chi=1\). For a solar mass, \(1.51\times10^{77}\) bits becomes \(7.57\times10^{76}\). But per caveat (3), this is <em>a comparison at fixed \(M\), not a process</em>.</div></details></li>

<li>How many bits of surprise is it that high-spin sources sit just below the bound? Is that a coincidence?
<details><summary>Show the answer</summary><div class="ans">With a uniform prior over \(\chi\in[0,1]\), <strong>4.3 bits</strong> — inside Episode 36's band of coincidences (4 to 7). But <em>accretion delivering angular momentum explains it, and photon capture explains the Thorne limit of 0.998</em> — so Episode 19 classifies it as <strong>physics</strong>. See also caveats (1) and (2).</div></details></li>

<li>(Harder) Why is Kerr special for this series?
<details><summary>Show the answer</summary><div class="ans">Because on Episode 33's three-step test it is <strong>Step 3 (Weyl \(\ne0\))</strong>. Every FLRW spacetime the series handled in cosmology was <em>Step 2 (conformally flat)</em> and could be flattened by a conformal transformation. <strong>Kerr is where the conformal tool stops reaching</strong> — Petrov type D, with a Weyl curvature that cannot be made to vanish.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: two labels, and only one of them moves</h2>
<p>The Kerr solution carries two labels, \(M\) and \(\chi=a/(GM/c^2)\). On the weight table \(M\) is \(-1\) and \(\chi\) is \(0\) — <strong>one is bookkeeping, the other is physics</strong>. Angular momentum itself has weight 0, and counting it as "measured in units of \(\hbar\)" gives the same answer (the check). It is <em>the cleanest example of Part II's "a conformal transformation touches only size"</em>. In Episode 5's currency, of Kerr's 10.7 bits, <strong>5.37 are entirely notation</strong>.</p>
<p>And the bound \(\chi\le1\) <strong>sits in a dimensionless quantity</strong> — the weight-0 column, meaning <em>no conformal transformation can carry a black hole across that line</em>. The maximum extractable mass fraction \(1-1/\sqrt2=0.29289\), and the fact that entropy at \(\chi=1\) is <strong>exactly half</strong>, live in the same column.</p>
<p>Measured spins line up just below that bound — 0.98 for GRS 1915+105, 0.95 for Cyg X-1, and the accretion-reachable Thorne limit at 0.998. By Episode 19's practice that is <strong>4.3 bits for the high-spin sources and 9.0 for the Thorne limit</strong>, <em>back inside Episode 36's "band of coincidences" (4 to 7)</em>. But explanations exist, so the classification is not coincidence but <strong>physics</strong> — another member of the "explained, 4 to 7 bits" family.</p>
<p>As \(\chi\to1\) the temperature goes to zero while the entropy stays finite at \(7.6\times10^{76}\) bits — <em>colliding with the naive third law</em>, and escaped by the fact that it cannot be reached in finitely many operations. <strong>Like Episode 4's "coarse-graining is irreversible", a line you approach but never reach.</strong></p>
<p>And the most important point. On Episode 33's three-step test, <strong>Kerr is Step 3 (Weyl \(\ne0\))</strong>. Every FLRW spacetime handled in cosmology was Step 2 and could be flattened conformally — <em>Kerr is the first case this tool cannot reach head-on.</em></p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 40</span>
This time a spacetime appeared whose <strong>Weyl curvature cannot be removed</strong> (Kerr, Schwarzschild). Next time: <strong>gravitational entropy</strong> — <em>what information exactly are the \(1.5\times10^{77}\) bits counted in §04?</em> And the leading candidate for measuring "the entropy of the gravitational field itself" turns out to be <strong>the Weyl curvature</strong>. It is the doorway to Episode 41's <em>Weyl curvature hypothesis</em>.
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sc=document.getElementById('sc'), vc=document.getElementById('vc'), ro=document.getElementById('ro');
  var X0=76, X1=690, Y0=34, Y1=300;

  function px(x){ return X0+x*(X1-X0); }
  function py(y){ return Y1-y*(Y1-Y0); }
  function area(x){ return (1+Math.sqrt(Math.max(0,1-x*x)))/2; }
  function extr(x){ return 1-Math.sqrt(area(x)); }
  function temp(x){ var r=Math.sqrt(Math.max(0,1-x*x)); return (r/(1+r))/0.5; }

  function curve(f,col,w){
    g.strokeStyle=col; g.lineWidth=w; g.beginPath();
    for(var i=0;i<=300;i++){ var x=i/300, X=px(x), Y=py(f(x)); if(i===0)g.moveTo(X,Y); else g.lineTo(X,Y); }
    g.stroke();
  }

  function draw(){
    var chi=parseInt(sc.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var v=0;v<=1.0001;v+=0.25){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(v)); g.lineTo(X1,py(v)); g.stroke();
      g.fillText(v.toFixed(2), X0-8, py(v)+4);
    }
    g.textAlign='center';
    for(var t=0;t<=1.0001;t+=0.2){
      g.fillStyle='#9c96a4'; g.fillText(t.toFixed(1), px(t), Y1+20);
    }

    var obs=[[0.686,'remnant 0.686'],[0.95,'Cyg X-1'],[0.998,'Thorne limit']];
    for(var i=0;i<obs.length;i++){
      var X=px(obs[i][0]);
      g.strokeStyle='#e2dce6'; g.lineWidth=1; g.setLineDash([2,3]);
      g.beginPath(); g.moveTo(X,Y0); g.lineTo(X,Y1); g.stroke(); g.setLineDash([]);
      g.save(); g.translate(X-4,Y0+70); g.rotate(-Math.PI/2);
      g.fillStyle='#a89fae'; g.textAlign='left'; g.fillText(obs[i][1],0,0); g.restore();
    }

    curve(area,'#7a5a2a',2.6);
    curve(extr,'#2a6a5a',2.4);
    curve(temp,'#a03a3a',2.0);

    g.textAlign='left';
    g.fillStyle='#7a5a2a'; g.fillText('horizon area A/A(0)', X0+10, py(area(0.12))-8);
    g.fillStyle='#a03a3a'; g.fillText('Hawking temperature T/T(0)', px(0.28), py(temp(0.28))+16);
    g.fillStyle='#2a6a5a'; g.fillText('extractable mass fraction', px(0.52), py(extr(0.52))-10);

    for(var j=0;j<3;j++){
      var f=[area,extr,temp][j], col=['#7a5a2a','#2a6a5a','#a03a3a'][j];
      g.fillStyle=col; g.beginPath(); g.arc(px(chi),py(f(chi)),4.2,0,6.29); g.fill();
    }
    g.strokeStyle='#5a5262'; g.lineWidth=1.6; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(chi),Y0); g.lineTo(px(chi),Y1); g.stroke(); g.setLineDash([]);

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('spin  chi = a / (GM/c^2)  — dimensionless, unmoved by conformal transformations', (X0+X1)/2, Y1+42);

    vc.textContent=chi.toFixed(3);
    ro.textContent='chi = '+chi.toFixed(3)+
      '　→　area '+area(chi).toFixed(4)+
      '　/　entropy '+(1.514e77*area(chi)).toExponential(2)+' bits (solar mass)'+
      '　/　extractable mass '+(100*extr(chi)).toFixed(2)+' per cent'+
      '　/　temperature '+temp(chi).toFixed(4)+
      (chi>0.995?'　★ temperature heads to zero, entropy stays finite at half':'');
  }
  sc.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-39-kerr.html', acc='#7a5a2a', ops='#2a6a5a',
      title='Rotating spacetime ── c·t = const, That Clicks, Episode 39 (Part V)',
      ep='EPISODE 39 ／ Part V — where the tool breaks',
      eyebrow='Two labels, and only one of them moves',
      h1='A bound placed in<br>the untouchable column',
      sub='Kerr carries the labels \\(M\\) and \\(\\chi\\); only one is bookkeeping.<br><em>And \\(\\chi\\le1\\) cannot be crossed by any conformal transformation.</em>',
      byline_l='What you need: Episode 16\'s weight table, Episode 19\'s scale, Episode 33\'s three-step test, Episode 36\'s band',
      byline_r='\\(1-1/\\sqrt2=0.29289\\) — the extractable-mass ceiling',
      body=BODY + '\n\n<p class="foot">This document is Episode 39 of "c·t = const, That Clicks" (the third of Part V), written for physics-minded high-school and university readers. The Kerr solution, the area and entropy expressions, the irreducible mass, the Thorne limit (Thorne 1974) and Israel\'s form of the third law are all standard and nothing here is a new claim — the numbers are computed in kenshou/calc43.py. <strong>Every spin measurement in §05 is strongly model-dependent</strong>, with continuum fitting and iron-line (reflection) methods disagreeing for some objects (GRS 1915+105 is reported both as 0.98 and as around 0.7) — <em>"high-spin sources line up just below the bound" lists only the measurements that reported high spin, so the selection is biased</em>. §05\'s 4.3 bits assumes a uniform prior over \\(\\chi\\in[0,1]\\); putting accretion theory into the prior shrinks the surprise. <strong>§04\'s table compares holes of the same \\(M\\) and is not a process in which "spinning it up lowers the entropy"</strong> — spinning it up injects energy too, so \\(M\\) changes, and by the area theorem the area does not decrease in an actual process. <strong>Cosmic censorship is a hypothesis, not a theorem</strong>, with no proof in the general case — §03\'s "cannot carry across" means that within the Kerr family \\(\\chi\\le1\\) is the condition for a horizon to exist. §02\'s "half the information is notation" uses Episode 5\'s price (5.37 bits, from a dataset of \\(N=1701\\)) — <em>the structure "one of the two labels is notation" is the substance</em>. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the spin and three dimensionless quantities move together. "Show the answer" opens each solution.')
