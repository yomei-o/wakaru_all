# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Last time the breaking came from quantum theory being unable to stay at \(D=4\). This time, something <strong>worse</strong> — pull the conformal factor out of the Einstein action and <em>its kinetic term alone comes out with the wrong sign</em>. The energy has no lower bound and <strong>the Euclidean path integral diverges</strong>. This is the source of the ghost we met twice in Episode 34. And what it shows is this — <em>the ghost never disappears; it only moves.</em></p>

<h2><span class="n">01</span>Pull out the conformal factor and a kinetic term appears</h2>

<div class="calc">
<span class="tag">Write \(g=\Omega^2\hat g\) and rewrite the Einstein–Hilbert action</span>
$$\sqrt{g}\,R[g]=\sqrt{\hat g}\,\Omega^{D-2}\Big(\hat R-2(D-1)\hat\Box\ln\Omega-(D-1)(D-2)(\partial\ln\Omega)^2\Big)$$
<p class="lbl">after integrating by parts, the coefficient of \(\Omega\)'s kinetic term is \((D-1)(D-2)\) — with <strong>the sign opposite to an ordinary scalar field</strong></p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(D\)</th><th class="mid">\((D-1)(D-2)\)</th><th>meaning</th></tr></thead>
<tbody>
<tr><th class="mid">1</th><td class="mid">\(0\)</td><td>exactly zero</td></tr>
<tr><th class="mid">2</th><td class="mid">\(0\)</td><td>exactly zero — <em>in two dimensions the conformal factor has no kinetic term</em></td></tr>
<tr><th class="mid">3</th><td class="mid">\(2\)</td><td></td></tr>
<tr class="hi"><th class="mid">4</th><td class="mid"><strong>\(6\)</strong></td><td><strong>our dimension</strong></td></tr>
<tr><th class="mid">5</th><td class="mid">\(12\)</td><td></td></tr>
<tr><th class="mid">6</th><td class="mid">\(20\)</td><td></td></tr>
<tr><th class="mid">10</th><td class="mid">\(72\)</td><td></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>At \(D=4\) the coefficient is 6. Only \(D=1\) and \(D=2\) make it vanish.</strong><br>
── <em>In our dimension there is no way out.</em></p>
</div>

<h2><span class="n">02</span>The conformal factor is a conformally coupled scalar with the wrong sign</h2>

<div class="calc">
<span class="tag">The coupling of a conformally coupled scalar</span>
$$\xi=\frac{D-2}{4(D-1)}\qquad\xrightarrow{\ D=4\ }\qquad \xi=\frac16=0.1667$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(D\)</th><th class="mid">\(\xi\)</th><th></th></tr></thead>
<tbody>
<tr><th class="mid">3</th><td class="mid">\(0.1250\)</td><td></td></tr>
<tr class="hi"><th class="mid">4</th><td class="mid"><strong>\(0.1667\)</strong></td><td><strong>our dimension: \(1/6\)</strong></td></tr>
<tr><th class="mid">5</th><td class="mid">\(0.1875\)</td><td></td></tr>
<tr><th class="mid">6</th><td class="mid">\(0.2000\)</td><td></td></tr>
<tr><th class="mid">100</th><td class="mid">\(0.2475\)</td><td>approaches \(1/4\) as \(D\to\infty\)</td></tr>
</tbody>
</table>
</div>

<p>Regard \(\Omega\) as a field and <strong>the Einstein action is the action of a conformally coupled scalar multiplied by an overall minus sign</strong>. That is why the kinetic term has the wrong sign — this is the <strong>conformal factor problem</strong> (Gibbons–Hawking–Perry 1978).</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>The core — just make the wrinkles finer and it diverges</h2>

<div class="calc">
<span class="tag">Put a wrinkle on a flat four-torus of side \(L\) (Planck units)</span>
$$\Omega=a\sin\frac{2\pi n x}{L}\qquad\Rightarrow\qquad |S|=\frac{6}{16\pi}\,a^2\Big(\frac{2\pi n}{L}\Big)^2\frac{L^4}{2}=2.357\,a^2n^2L^2$$
<p class="lbl">the weight \(e^{-S}=e^{+|S|}\) measured in bits is \(|S|/\ln2\) (with \(L=10\,\ell_P\), \(a=0.1\))</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(n\) (number of wrinkles)</th><th class="mid">\(|S|\)</th><th class="mid">weight [bits]</th></tr></thead>
<tbody>
<tr><th class="mid">1</th><td class="mid">\(2.36\)</td><td class="mid">\(3.4\)</td></tr>
<tr><th class="mid">2</th><td class="mid">\(9.42\)</td><td class="mid">\(13.6\)</td></tr>
<tr><th class="mid">5</th><td class="mid">\(58.9\)</td><td class="mid">\(85.0\)</td></tr>
<tr><th class="mid">10</th><td class="mid">\(235.6\)</td><td class="mid">\(339.9\)</td></tr>
<tr><th class="mid">20</th><td class="mid">\(942.5\)</td><td class="mid">\(1359.7\)</td></tr>
<tr class="hi"><th class="mid">50</th><td class="mid">\(5890.5\)</td><td class="mid"><strong>\(8498.2\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>It grows as \(n^2\) and never stops.</strong><br>
Making the wrinkles finer makes the path-integral weight arbitrarily large — <em>\(e^{-S}\) diverges</em>.<br>
On Episode 19's scale, <strong>there are directions in which the "surprise" is infinite</strong>.</p>
</div>

<div class="fig">
<p class="cap">Figure: the Euclidean action, and the path-integral weight, when the conformal factor is wrinkled. <strong>An ordinary scalar field rises, so its weight shrinks</strong>; the conformal factor falls the other way and <em>its weight grows</em>. Move the slider — <strong>there is no bottom anywhere.</strong></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>number of wrinkles \(n\)<input id="sn" type="range" min="1" max="50" value="10" step="1"></label>
  <span class="val" id="vn">10</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#5a3a7a"></i>the conformal factor (wrong sign)</span>
  <span><i class="swatch" style="background:#8a9aa8"></i>an ordinary scalar field (right sign)</span>
</div>
</div>

<h2><span class="n">04</span>How many diverging directions are there?</h2>

<div class="calc">
<span class="tag">Planck volumes inside the Hubble radius</span>
$$\left(\frac{R_H}{\ell_P}\right)^3=(8.04\times10^{60})^3=5.2\times10^{182}$$
</div>

<p>The conformal factor carries <strong>one degree of freedom per point</strong>, so the action is unbounded below <em>in every one of those \(5.2\times10^{182}\) directions</em>. Logarithmically, that is 607 bits' worth of directions.</p>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0">It is <strong>the same currency</strong> as the \(3\times10^{122}\) bits of information Episode 24 counted the universe as having processed —<br>
except that this counts <em>not information, but broken directions</em>.</p>
</div>

<h2><span class="n">05</span>The fix — rotate the contour</h2>

<div class="seven">
<div class="row"><div class="mk">→</div><div class="txt"><strong>The Gibbons–Hawking–Perry prescription</strong><span>rotate the contour for the conformal factor alone, \(\Omega\to i\Omega\) — the sign returns and the Gaussian integral converges</span></div></div>
<div class="row"><div class="mk">pay</div><div class="txt"><strong>One rule added by hand: "treat the conformal factor separately"</strong><span>on Episode 5's balance, that is the cost</span></div></div>
<div class="row hi"><div class="mk">buy</div><div class="txt"><strong>The Euclidean path integral becomes definable</strong><span>it does work at one loop — <em>but there is no derivation from first principles</em></span></div></div>
</div>

<p>This is <strong>the same shape of ledger as Episode 32's cosmon or Episode 29's MOND</strong> — <em>a rule added by hand always carries a price.</em></p>

<h2><span class="n">06</span>Where the ghost sits — the trade with Episode 34</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Theory</th><th class="mid">Spin 2</th><th class="mid">Conformal factor</th><th class="mid">Prescription</th></tr></thead>
<tbody>
<tr class="hi"><th>Einstein gravity</th><td class="mid">healthy (right sign)</td><td class="mid"><strong>a ghost</strong></td><td class="mid">rotate the contour</td></tr>
<tr class="hi"><th>Conformal gravity (Ep. 34)</th><td class="mid"><strong>a ghost</strong> (fourth-order)</td><td class="mid">removed by gauge</td><td class="mid">unresolved</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0"><strong>It was a trade: put the ghost in the conformal factor, or put it in the spin 2.</strong><br>
<em>An option that puts it in neither has not been found.</em><br>
── This is Part V's thesis itself: <strong>the place where the tool breaks does not vanish; it moves.</strong></p>
</div>

<h2><span class="n">07</span>\(D=2\) is the exception — and it connects to Episode 37</h2>

<div class="seven">
<div class="row"><div class="mk">0</div><div class="txt"><strong>At \(D=2\), \((D-1)(D-2)=0\)</strong><span>the conformal factor has no kinetic term — as §01's table shows</span></div></div>
<div class="row"><div class="mk">?</div><div class="txt"><strong>Then why does two-dimensional gravity have a Liouville action?</strong><span>a kinetic term for the conformal factor is definitely there</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>It comes from the anomaly (Episode 37)</strong><span>zero classically, <em>grown by quantisation</em> — in two dimensions the kinetic term itself is of quantum origin</span></div></div>
</div>

<div class="aside">
<span class="tag">The same shape as last time</span>
Episode 37: quantum theory wrote a number into the "zero column" (\(\alpha\) acquired a \(\mu\)).<br>
Episode 38 §07: quantum theory wrote a kinetic term into the "zero coefficient" (Liouville in two dimensions).<br>
── <em>Something that vanished classically growing under quantisation is not a one-off coincidence.</em>
</div>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) §03's divergence is not a classical instability.</strong> In classical general relativity the conformal mode is <em>fixed by the Hamiltonian constraint and is not a propagating degree of freedom</em> (in four dimensions only the two spin-2 components propagate). <strong>What is broken is the definition of the Euclidean path integral, not the stability of stars or of spacetime.</strong></p>
<p style="margin:0 0 10px"><strong>(2) §03's numbers are a toy model: a single mode on a flat torus.</strong> The values \(L=10\,\ell_P\) and \(a=0.1\) carry no physical meaning — <em>they are an example chosen to display the behaviour "grows as \(n^2\), without bound"</em>. Do not take the absolute bit counts seriously.</p>
<p style="margin:0 0 10px"><strong>(3) §04's "\(5.2\times10^{182}\) directions" is a mode count with a Planck-length cutoff.</strong> It <em>depends entirely on how the cutoff is drawn</em>, and with the cutoff removed the number is infinite — <strong>it looks like a large finite number only because a cutoff was imposed, and it indicates scale, not the severity of the problem</strong>.</p>
<p style="margin:0 0 10px"><strong>(4) §01's sign depends on the metric signature convention and the overall sign of the action</strong>, and references write it as \(\pm6\) accordingly. <em>What is convention-independent is the relation "the conformal factor's kinetic term has the opposite sign to a matter scalar's" and the magnitude \((D-1)(D-2)\).</em></p>
<p style="margin:0 0 10px"><strong>(5) §05's contour rotation remains an active point of debate.</strong> Which contour to take in general is unsettled (prescriptions using Picard–Lefschetz theory have been discussed in recent years), and <em>this document claims nothing beyond "it works at one loop"</em>.</p>
<p style="margin:0"><strong>(6) §06's "trade" is this series' reading.</strong> It has not been proved that no theory can avoid a ghost in both places — <em>"none has been found within the known frameworks" is the accurate statement</em>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>What is the coefficient of the conformal factor's kinetic term in \(D\) dimensions, and where does it vanish?
<details><summary>Show the answer</summary><div class="ans">\((D-1)(D-2)\). It vanishes only at <strong>\(D=1\) and \(D=2\)</strong>, and at \(D=4\) it is <strong>6</strong> — <em>in our dimension there is no way out</em>.</div></details></li>

<li>What does "the conformal factor is a conformally coupled scalar with the wrong sign" mean?
<details><summary>Show the answer</summary><div class="ans">Regarded as a field, \(\Omega\) makes the Einstein action take the form of <strong>a conformally coupled scalar's action (\(\xi=(D-2)/4(D-1)\), which is \(1/6\) in four dimensions) multiplied by an overall minus</strong>. That flips the sign of the kinetic term, and <em>the energy loses its lower bound</em>.</div></details></li>

<li>Double the number of wrinkles \(n\). By what factor does the path-integral weight in bits grow?
<details><summary>Show the answer</summary><div class="ans">By <strong>four</strong> (it goes as \(n^2\)). As the table shows, \(n=10\) gives 339.9 bits and \(n=20\) gives 1359.7 — <em>with no upper bound</em>. But per caveat (2), these are toy-model numbers.</div></details></li>

<li>Does this divergence mean astronomical objects are unstable?
<details><summary>Show the answer</summary><div class="ans"><strong>No.</strong> In classical general relativity the conformal mode is <em>fixed by the Hamiltonian constraint and does not propagate</em>. What is broken is <strong>the definition of the Euclidean path integral</strong>, not the stability of spacetime.</div></details></li>

<li>(Harder) Putting Episode 34 and this episode together, what can be said about ghosts?
<details><summary>Show the answer</summary><div class="ans">That <strong>they move rather than disappear</strong>. Einstein gravity has a healthy spin 2 and a ghostly conformal factor; conformal gravity removes the conformal factor by gauge but pays with a spin-2 ghost. <em>An option that puts a ghost in neither has not been found within the known frameworks</em> (caveat 6).</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: the ghost does not vanish, it moves</h2>
<p>Write \(g=\Omega^2\hat g\), rewrite the Einstein action, and a kinetic term for the conformal factor \(\Omega\) appears. Its coefficient is <strong>\((D-1)(D-2)\)</strong>, with <em>the sign opposite to an ordinary scalar</em>. It vanishes only at \(D=1\) and \(D=2\); at <strong>\(D=4\) it is 6</strong> — our dimension has no way out. Regarded as a field, \(\Omega\) makes the Einstein action <strong>a conformally coupled scalar (\(\xi=1/6\)) with an overall minus</strong>.</p>
<p>How bad is it? Wrinkle a flat torus with \(\Omega=a\sin(2\pi nx/L)\) and the Euclidean action is \(|S|=2.357a^2n^2L^2\), so the weight \(e^{+|S|}\) <strong>grows as \(n^2\) forever</strong> — 340 bits at \(n=10\), 8498 bits at \(n=50\), <em>with no bound</em>. Making the wrinkles finer makes the path integral diverge. And there are \(5.2\times10^{182}\) Planck volumes inside the Hubble radius, so <strong>every one of them is an unbounded direction</strong>.</p>
<p>The fix is to rotate the contour for the conformal factor alone, \(\Omega\to i\Omega\) (Gibbons–Hawking–Perry). It does work at one loop, but <em>there is no derivation from first principles</em> — the same ledger as Episode 32's cosmon or Episode 29's MOND, where <strong>a rule added by hand always carries a price</strong>.</p>
<p>And the most important thing this time. <strong>It was a trade: put the ghost in the conformal factor, or put it in the spin 2.</strong> Einstein gravity has a healthy spin 2 and a ghostly conformal factor; conformal gravity (Episode 34) removes the conformal factor by gauge and pays with a spin-2 ghost. <em>An option putting it in neither has not been found</em> — which is Part V's thesis itself: <strong>the place where the tool breaks does not vanish; it moves.</strong></p>
<p>Finally, \(D=2\). The coefficient is zero, yet two-dimensional gravity does have a Liouville action — <strong>it grows out of the anomaly</strong> (Episode 37). Last time quantum theory wrote a number into the "zero column"; this time it writes a kinetic term into the "zero coefficient" — <em>something vanishing classically and growing under quantisation is not a one-off coincidence.</em></p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 39</span>
Episodes 37 and 38 looked at where conformal transformations <em>break</em> when applied to quantum theory and to gravity. Next time we change the view and look at <strong>rotating spacetime</strong> — the Kerr solution. A black hole's angular momentum is expressed by the <strong>dimensionless</strong> quantity \(a/M\), which sits in the <em>zero column</em> of Episode 16's weight table. What does Part II's conclusion, "a conformal transformation touches only size", mean for rotation? And the bound \(a/M\le1\) is <em>a constraint placed in the untouchable column — one that cannot be rewritten.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sn=document.getElementById('sn'), vn=document.getElementById('vn'), ro=document.getElementById('ro');
  var X0=88, X1=690, Y0=30, Y1=300;
  var L=10.0, A=0.1, K=6.0/(16*Math.PI)*A*A*(2*Math.PI/L)*(2*Math.PI/L)*L*L*L*L/2;
  var NMAX=50, SMAX=K*NMAX*NMAX;

  function px(n){ return X0+(n/NMAX)*(X1-X0); }
  function py(s){ return (Y0+Y1)/2 - s/SMAX*((Y1-Y0)/2); }

  function draw(){
    var n=parseInt(sn.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.strokeStyle='#cdc8d2'; g.lineWidth=1.4;
    g.beginPath(); g.moveTo(X0,py(0)); g.lineTo(X1,py(0)); g.stroke();
    g.fillStyle='#9c96a4'; g.textAlign='right';
    g.fillText('S = 0', X0-8, py(0)+4);

    g.strokeStyle='#8a9aa8'; g.lineWidth=2.2; g.setLineDash([5,4]); g.beginPath();
    for(var i=0;i<=NMAX;i++){ var s=K*i*i; var X=px(i), Y=py(s); if(i===0)g.moveTo(X,Y); else g.lineTo(X,Y); }
    g.stroke(); g.setLineDash([]);
    g.fillStyle='#7a8894'; g.textAlign='left';
    g.fillText('ordinary scalar: S > 0, so the weight e^(-S) shrinks', X0+10, py(SMAX*0.55));

    g.strokeStyle='#5a3a7a'; g.lineWidth=2.8; g.beginPath();
    for(var i2=0;i2<=NMAX;i2++){ var s2=-K*i2*i2; var X2=px(i2), Y2=py(s2); if(i2===0)g.moveTo(X2,Y2); else g.lineTo(X2,Y2); }
    g.stroke();
    g.fillStyle='#5a3a7a';
    g.fillText('conformal factor: S < 0, so the weight e^(+|S|) grows without bound', X0+10, py(-SMAX*0.62));

    var sv=-K*n*n;
    g.fillStyle='#5a3a7a';
    g.beginPath(); g.arc(px(n),py(sv),5,0,6.29); g.fill();
    g.strokeStyle='#5a3a7a'; g.lineWidth=1; g.setLineDash([3,3]);
    g.beginPath(); g.moveTo(px(n),py(0)); g.lineTo(px(n),py(sv)); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#9c96a4'; g.textAlign='center';
    for(var t=0;t<=NMAX;t+=10){ g.fillText(t.toFixed(0), px(t), Y1+22); }
    g.fillStyle='#7d7686';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('number of wrinkles  n  (fineness)', (X0+X1)/2, Y1+44);
    g.save(); g.translate(22,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('Euclidean action  S', 0,0); g.restore();

    vn.textContent=String(n);
    ro.textContent='n = '+n+'　→　S = -'+(K*n*n).toFixed(1)+
      '　/　path-integral weight = '+((K*n*n)/Math.LN2).toFixed(1)+' bits'+
      '　(double n and it quadruples: it goes as n squared)'+
      (n>=NMAX?'　★ the edge here is only the edge of the figure — in reality there is no bottom anywhere':'');
  }
  sn.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-38-conformal-factor.html', acc='#5a3a7a', ops='#8a9aa8',
      title='The conformal factor problem ── c·t = const, That Clicks, Episode 38 (Part V)',
      ep='EPISODE 38 ／ Part V — where the tool breaks',
      eyebrow='The ghost never disappears; it only moves',
      h1='A kinetic term<br>with the wrong sign',
      sub='Pull the conformal factor out of the Einstein action and its kinetic term alone flips sign.<br><em>The Euclidean path integral has no bottom.</em>',
      byline_l='What you need: Episode 5\'s balance, Episode 19\'s scale, Episode 24, Episode 34\'s ghost, Episode 37',
      byline_r='Coefficient \\((D-1)(D-2)\\) — which is 6 at \\(D=4\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 38 of "c·t = const, That Clicks" (the second of Part V), written for physics-minded high-school and university readers. The conformal factor problem has been a well-known standard issue since Gibbons, Hawking &amp; Perry (1978, Nucl. Phys. B138, 141) and nothing here is a new claim — the numbers are computed in kenshou/calc42.py. <strong>§03\'s divergence is not a classical instability</strong> — in classical general relativity the conformal mode is fixed by the Hamiltonian constraint and does not propagate (only the two spin-2 components do in four dimensions), so <em>what is broken is the definition of the Euclidean path integral, not the stability of spacetime</em>. <strong>§03\'s numbers are a toy model of a single mode on a flat torus, and \\(L=10\\,\\ell_P\\), \\(a=0.1\\) carry no physical meaning</strong> — they display the behaviour "grows as \\(n^2\\), without bound", so the absolute bit counts should not be taken seriously. §04\'s \\(5.2\\times10^{182}\\) is a mode count with a Planck-length cutoff and <strong>depends entirely on how the cutoff is drawn</strong>; with the cutoff removed the number is infinite — <em>it indicates scale only</em>. §01\'s sign depends on the metric signature and the overall sign of the action and is written as \\(\\pm6\\) in different references — <strong>what is convention-independent is the relation "opposite in sign to a matter scalar" and the magnitude \\((D-1)(D-2)\\)</strong>. §05\'s contour rotation remains an active point of debate; which contour to take in general is unsettled (prescriptions using Picard–Lefschetz theory have been discussed in recent years), and <em>nothing beyond "it works at one loop" is claimed here</em>. <strong>§06\'s "trade" is this series\' reading</strong> — it has not been proved that no theory can avoid a ghost in both places; <em>"none has been found within the known frameworks" is the accurate statement</em>. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the slider and watch the descending curve never find a bottom. "Show the answer" opens each solution.')
