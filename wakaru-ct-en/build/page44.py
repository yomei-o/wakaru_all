# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Last time we found that <strong>a theory with a smallest length cannot be conformally invariant</strong>. And yet, as a matter of fact — <em>conformal field theories are computed on lattices every day</em>, and a lattice spacing is a smallest length. This time we count out <strong>why there is no contradiction</strong>. And there, at last, is the reason the tool that has been breaking all through Part V <em>survives anyway</em>.</p>

<h2><span class="n">01</span>The apparent contradiction</h2>

<div class="seven">
<div class="row"><div class="mk">43</div><div class="txt"><strong>A theory with a smallest length cannot be conformally invariant</strong><span>conformal invariance demands the absence of a scale, and a smallest length is a scale</span></div></div>
<div class="row"><div class="mk">fact</div><div class="txt"><strong>Yet conformal field theories are computed on lattices</strong><span>the 3D Ising critical exponents are known to five or six digits from lattice Monte Carlo</span></div></div>
<div class="row hi"><div class="mk">?</div><div class="txt"><strong>The lattice spacing \(a\) is a smallest length. Why is there no contradiction?</strong><span>that is this episode's question</span></div></div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">02</span>The core — the scale need not be absent, only irrelevant</h2>

<div class="calc">
<span class="tag">A lattice theory has two lengths</span>
$$a\ (\text{the lattice spacing})\qquad \xi\ (\text{the correlation length})$$
<p class="lbl">observables can depend only on the dimensionless ratio \(\xi/a\) (Episode 3) — and at criticality \(\xi/a\to\infty\)</p>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>Conformal invariance is not a property of the lattice but of the <em>fixed point</em> the lattice theory flows to.</strong><br>
The scale is not <em>absent</em>; it becomes <strong>irrelevant</strong>.<br>
── This is Episode 3's procedure exactly: <em>the physics is in the ratio, and when the ratio diverges the answer stops depending on \(a\).</em></p>
</div>

<h2><span class="n">03</span>How well do they agree? — the 3D Ising model</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Exponent</th><th class="mid">Conformal bootstrap (continuum)</th><th class="mid">Lattice Monte Carlo</th><th class="mid">Relative difference</th><th class="mid">\(\sigma\)</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">\(\nu\)</th><td class="mid">\(0.6299709(4)\)</td><td class="mid">\(0.63002(10)\)</td><td class="mid">\(7.8\times10^{-5}\)</td><td class="mid"><strong>\(0.5\)</strong></td></tr>
<tr><th class="mid">\(\eta\)</th><td class="mid">\(0.0362978(20)\)</td><td class="mid">\(0.03627(10)\)</td><td class="mid">\(7.7\times10^{-4}\)</td><td class="mid">\(0.3\)</td></tr>
</tbody>
</table>
</div>

<p>Kos et al. (2016) for the bootstrap, Hasenbusch (2010) for the lattice. <strong>The lattice answer and the continuum answer agree to four digits in \(\nu\) and three in \(\eta\)</strong> (both within \(1\sigma\)) — <em>the "smallest length" of the lattice spacing is nowhere in the answer.</em></p>

<h2><span class="n">04</span>Universality — different insides, the same numbers</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>The 3D Ising model (lattice spins)</strong><span>\(\nu=0.6300\)</span></div></div>
<div class="row"><div class="mk">2</div><div class="txt"><strong>The liquid–gas critical point (water, CO\(_2\))</strong><span>the same</span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>The mixing critical point of a binary fluid</strong><span>the same</span></div></div>
<div class="row hi"><div class="mk">4</div><div class="txt"><strong>Uniaxial ferromagnets</strong><span>the same — <em>completely different microscopic contents, identical exponents</em></span></div></div>
</div>

<p><strong>The details of the lattice and the details of the molecules have both vanished from the answer</strong> — that is what "becoming irrelevant" means <em>experimentally</em>.</p>

<h2><span class="n">05</span>How fast does it vanish? — the correction exponent \(\omega\)</h2>

<div class="calc">
<span class="tag">Lattice traces die as \((a/\xi)^\omega\), with \(\omega=0.8303\) for the 3D Ising model</span>
$$\text{every halving of the lattice spacing buys }\mathbf{0.83\ \text{bits}}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(\xi/a\)</th><th class="mid">residual error \((a/\xi)^\omega\)</th><th class="mid">bits</th></tr></thead>
<tbody>
<tr><th class="mid">\(10\)</th><td class="mid">\(1.5\times10^{-1}\)</td><td class="mid">\(2.8\)</td></tr>
<tr><th class="mid">\(10^2\)</th><td class="mid">\(2.2\times10^{-2}\)</td><td class="mid">\(5.5\)</td></tr>
<tr><th class="mid">\(10^3\)</th><td class="mid">\(3.2\times10^{-3}\)</td><td class="mid">\(8.3\)</td></tr>
<tr><th class="mid">\(10^4\)</th><td class="mid">\(4.8\times10^{-4}\)</td><td class="mid">\(11.0\)</td></tr>
<tr class="hi"><th class="mid">\(10^6\)</th><td class="mid">\(1.0\times10^{-5}\)</td><td class="mid">\(16.5\)</td></tr>
</tbody>
</table>
</div>

<p>Reaching six digits (\(10^{-6}\)) would need \(\xi/a>1.7\times10^7\) — <strong>no lattice that large fits</strong>. In practice one uses <em>improved actions</em> (which cancel the leading correction) and extrapolation. <strong>The agreement in §03 is not the achievement of a naive lattice computation; it is the achievement of the work done to cancel the corrections.</strong></p>

<div class="fig">
<p class="cap">Figure: how fast the lattice's traces vanish. <strong>Refining the lattice reduces the error as \((a/\xi)^{0.83}\)</strong>, but <em>six digits would need \(\xi/a>10^7\)</em>, so improved actions cancel the leading correction instead. Move the slider.</p>
<canvas id="cv" width="720" height="360"></canvas>
<div class="controls">
  <label>lattice fineness \(\log_{10}(\xi/a)\)<input id="sx" type="range" min="5" max="80" value="30" step="1"></label>
  <span class="val" id="vx">3.0</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3a4a7a"></i>naive lattice (\(\omega=0.83\))</span>
  <span><i class="swatch" style="background:#7a3a4a"></i>improved action (leading term cancelled)</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>beyond what a lattice can hold</span>
</div>
</div>

<h2><span class="n">06</span>The link to Episode 14</h2>

<div class="seven">
<div class="row"><div class="mk">14</div><div class="txt"><strong>The anomalous dimension \(\eta=0.036\) was "a 3.6 per cent error in the weight table"</strong><span>the quantity measured in Episode 14</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>And the lattice spacing \(a\) does not enter \(\eta\) at all</strong><span>the weight table's numbers are <em>properties of the fixed point</em>, not of the lattice</span></div></div>
<div class="row"><div class="mk">→</div><div class="txt"><strong>This is why Episode 16's weight table survives quantisation</strong><span>the number quantum theory wrote into the zero column in Episode 37 is also a fixed-point quantity</span></div></div>
</div>

<h2><span class="n">07</span>Where it did not work — the \(\lambda\) transition of helium</h2>

<div class="calc">
<span class="tag">The heat-capacity exponent of the 3D XY class (superfluid \(^4\)He), \(\alpha=2-3\nu\)</span>
$$\text{theory}\ \alpha=-0.01525\pm0.00030\qquad
\text{experiment}\ \alpha=-0.0127\pm0.0003$$
<p class="lbl">difference \(0.00255\), combined error \(0.00042\) → <strong>\(6.0\sigma\)</strong>, i.e. <strong>29.0 bits</strong> on Episode 19's scale</p>
</div>

<p>The measurement was made aboard the Space Shuttle (Lipa et al. 2003), to avoid gravitational pressure gradients. <strong>This discrepancy is unresolved.</strong> Whether universality fails, or a systematic error lies on the experimental or the theoretical side, is not settled — <em>universality works very well, but it is not universal magic.</em></p>

<h2><span class="n">08</span>In the end this too was (A)/(B)</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Reading</th><th class="mid">The limit</th><th class="mid">Conformal invariance</th><th class="mid">Consequence</th></tr></thead>
<tbody>
<tr><th>(A) \(a\) is a regulator to be removed</th><td class="mid">take the continuum limit</td><td class="mid"><strong>exact</strong> at the fixed point</td><td class="mid">the lattice is a tool</td></tr>
<tr class="hi"><th>(B) \(a\) is physical (spacetime really is discrete)</th><td class="mid">do not remove it</td><td class="mid"><strong>approximate</strong></td><td class="mid">violations could be observed</td></tr>
</tbody>
</table>
</div>

<p>Episode 36's (A)/(B) applies to the lattice spacing as well. And <strong>the GRB constraints of Episode 43 §05 were a measurement testing (B)</strong>.</p>

<div class="keybox">
<p class="lbl">Part V's answer</p>
<p style="margin:6px 0 0">Episode 43: a smallest length is incompatible with conformal invariance (excluded by hypothesis).<br>
Episode 44: <strong>and the tool survives anyway</strong> — provided the scale becomes <em>irrelevant</em>.<br>
── <strong>What the tool demanded was never "no scale", but "no scale left in the answer".</strong><br>
If it is irrelevant in the renormalisation-group sense, conformal invariance returns at long distances to any accuracy you like.</p>
</div>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) §03's agreement is a consequence of the lattice side having taken the continuum limit.</strong> These are not raw numbers from a finite lattice but values <em>extrapolated from several lattice sizes with improved actions cancelling the leading correction</em> — per §05, a naive computation on a \(10^3\) lattice still carries a 0.3 per cent error. <strong>"The lattice gives the same answer" properly means "carefully taking the continuum limit gives the same answer".</strong></p>
<p style="margin:0 0 10px"><strong>(2) §02's "irrelevant" is renormalisation-group jargon.</strong> It does not mean "beside the point" but <em>an operator whose coefficient shrinks under the RG transformation</em> — and <strong>which operators are irrelevant differs from theory to theory and is not obvious</strong>. For gravity, that is exactly the open question of Episode 35's asymptotic safety.</p>
<p style="margin:0 0 10px"><strong>(3) §07's helium discrepancy is still under discussion.</strong> Systematic errors on the experimental side (finite-size effects, temperature control) and the theoretical error budget have both been suggested — <em>this document claims nothing beyond "it is unresolved"</em>. The \(6.0\sigma\) simply combines the quoted errors and <strong>would move substantially with a different systematic estimate</strong>.</p>
<p style="margin:0 0 10px"><strong>(4) §04's universality examples are a textbook summary.</strong> In real experiments <em>the number of reliable digits depends on how the critical point is approached and how corrections are handled</em> — not all of these are confirmed to the same precision, and the liquid–gas exponents are not known as precisely as the magnetic ones.</p>
<p style="margin:0"><strong>(5) §08's (B) is not a claim that spacetime is discrete.</strong> It is <em>a statement that the reading is logically available</em>; current observations only exclude the linear effect (Episode 43 §05) — <strong>whether spacetime is discrete is unresolved</strong>, and this document endorses neither answer.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>The lattice has a smallest length, so why can conformal field theories be computed on it?
<details><summary>Show the answer</summary><div class="ans">Because conformal invariance is <strong>a property of the fixed point the lattice theory flows to, not of the lattice</strong>. Observables can depend only on \(\xi/a\), which diverges at criticality, so <em>\(a\) drops out of the answer</em> — the scale is not <strong>absent</strong> but <strong>irrelevant</strong>.</div></details></li>

<li>How many bits does halving the lattice spacing buy?
<details><summary>Show the answer</summary><div class="ans"><strong>0.83 bits</strong> (the 3D Ising correction exponent \(\omega=0.8303\)). Even at \(\xi/a=10^3\) a 0.3 per cent error remains (8.3 bits), and <em>six digits would need \(\xi/a>1.7\times10^7\)</em>, beyond any lattice — hence improved actions and extrapolation.</div></details></li>

<li>What is the experimental meaning of universality?
<details><summary>Show the answer</summary><div class="ans"><strong>That completely different microscopic contents give identical exponents</strong> — lattice spins, the liquid–gas critical point of water, binary fluids and uniaxial ferromagnets all give \(\nu=0.6300\). <em>The details of the lattice and of the molecules have vanished from the answer</em>: that is what "irrelevant" looks like in the laboratory.</div></details></li>

<li>Is there a case where universality is in question?
<details><summary>Show the answer</summary><div class="ans"><strong>The \(\lambda\) transition of \(^4\)He.</strong> The 3D XY class gives \(\alpha=2-3\nu=-0.01525(30)\), while the Space Shuttle experiment gives \(-0.0127(3)\) — a <strong>\(6.0\sigma\), 29-bit</strong> discrepancy. It is <em>unresolved</em>; whether universality fails or a systematic error is responsible is not settled.</div></details></li>

<li>(Harder) Taking Episodes 43 and 44 together, what does the tool actually demand?
<details><summary>Show the answer</summary><div class="ans"><strong>Not "no scale" but "no scale left in the answer".</strong> As Episode 43 showed, a smallest length excludes exact conformal invariance; but <em>if that scale is irrelevant in the RG sense, conformal invariance returns at long distances to any accuracy you like</em> — that is Part V's answer.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: what the tool demanded was never absence</h2>
<p>Episode 43 showed that a theory with a smallest length cannot be conformally invariant. Yet <strong>conformal field theories are computed on lattices</strong>. The reason there is no contradiction: <em>conformal invariance is a property of the fixed point the lattice theory flows to, not of the lattice</em>. Observables can depend only on \(\xi/a\), which diverges at criticality, so <strong>\(a\) drops out of the answer</strong>. The scale is not <em>absent</em>; it becomes <strong>irrelevant</strong>.</p>
<p>In practice, the 3D Ising exponents from the continuum bootstrap and from lattice Monte Carlo <strong>agree to four digits in \(\nu\)</strong> (\(0.5\sigma\)). And there is <strong>universality</strong> — lattice spins, the liquid–gas critical point of water, binary fluids, uniaxial ferromagnets, all with the same \(\nu=0.6300\). <em>The details of the lattice and of the molecules have vanished from the answer.</em></p>
<p>But the vanishing has a speed. Lattice traces die as \((a/\xi)^{0.83}\) — <strong>0.83 bits per halving of the spacing</strong>. Six digits would need \(\xi/a>1.7\times10^7\), which no lattice can hold. <em>The agreement in §03 is not the achievement of a naive computation but of improved actions and extrapolation — the work of cancelling the corrections.</em></p>
<p>And there is a case where it did not work — <strong>the \(\lambda\) transition of \(^4\)He</strong>. Against the 3D XY prediction \(\alpha=-0.01525(30)\), the Space Shuttle experiment gives \(-0.0127(3)\): a <strong>\(6.0\sigma\), 29-bit</strong> discrepancy, still unresolved. <em>Universality works very well, but it is not universal magic.</em></p>
<p>In the end this too was (A)/(B) — is \(a\) a regulator to be removed, or a physical discreteness? Episode 43's GRB constraints were a measurement of (B). <strong>Part V's answer: what the tool demanded was never "no scale", but "no scale left in the answer".</strong></p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 45 (Part V wrap-up)</span>
Part V's episodes go onto one page — <strong>quantum anomalies, the conformal factor problem, rotating spacetime, gravitational entropy, the Weyl curvature hypothesis, the black hole interior, the Planck scale, discretisation</strong>. We sort them into <em>where the tool broke, where it could not reach, and where it was excluded</em>, and draw <strong>a map of where the tool works</strong>. Then we write how Part IV's wrap-up ("good theories have already had the surgery") and this part's answer ("the scale only has to not remain") <em>connect.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sx=document.getElementById('sx'), vx=document.getElementById('vx'), ro=document.getElementById('ro');
  var X0=80, X1=690, Y0=34, Y1=272;
  var OM=0.8303, OM2=1.66, A0=0.5, A1=8, B0=0, B1=24;

  function px(v){ return X0+(v-A0)/(A1-A0)*(X1-X0); }
  function py(b){ return Y1-(b-B0)/(B1-B0)*(Y1-Y0); }
  function bits(v,om){ return om*v*Math.LN10/Math.LN2; }

  function draw(){
    var lx=parseInt(sx.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.fillStyle='#f4f2f6'; g.fillRect(px(3),Y0,X1-px(3),Y1-Y0);
    g.fillStyle='#a89fae'; g.textAlign='left';
    g.fillText('beyond here, no naive lattice fits', px(3)+8, Y0+16);

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var b=0;b<=B1;b+=4){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(b)); g.lineTo(X1,py(b)); g.stroke();
      g.fillText(b+' bit', X0-8, py(b)+4);
    }
    g.textAlign='center';
    for(var t=1;t<=8;t+=1){ g.fillStyle='#9c96a4'; g.fillText('10^'+t, px(t), Y1+20); }

    g.strokeStyle='#3a4a7a'; g.lineWidth=2.8; g.beginPath();
    for(var i=0;i<=200;i++){ var v=A0+(A1-A0)*i/200; if(i===0)g.moveTo(px(v),py(bits(v,OM))); else g.lineTo(px(v),py(bits(v,OM))); }
    g.stroke();
    g.strokeStyle='#7a3a4a'; g.lineWidth=2.4; g.setLineDash([6,4]); g.beginPath();
    for(var j=0;j<=200;j++){ var v2=A0+(A1-A0)*j/200; if(j===0)g.moveTo(px(v2),py(bits(v2,OM2))); else g.lineTo(px(v2),py(bits(v2,OM2))); }
    g.stroke(); g.setLineDash([]);

    g.textAlign='left';
    g.fillStyle='#3a4a7a'; g.fillText('naive lattice: 0.83 bit per halving', px(4.2), py(bits(4.2,OM))+18);
    g.fillStyle='#7a3a4a'; g.fillText('improved action: about twice as fast', px(1.4), py(bits(1.4,OM2))-10);

    var Xc=px(lx);
    g.strokeStyle='#5a5262'; g.lineWidth=1.6; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(Xc,Y0); g.lineTo(Xc,Y1); g.stroke(); g.setLineDash([]);
    g.fillStyle='#3a4a7a'; g.beginPath(); g.arc(Xc,py(bits(lx,OM)),4.6,0,6.29); g.fill();
    g.fillStyle='#7a3a4a'; g.beginPath(); g.arc(Xc,py(bits(lx,OM2)),4.6,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('lattice fineness  xi / a', (X0+X1)/2, Y1+44);

    vx.textContent=lx.toFixed(1);
    var e1=Math.pow(10,-OM*lx), e2=Math.pow(10,-OM2*lx);
    ro.textContent='xi/a = 10^'+lx.toFixed(1)+
      '　→　naive residual error '+e1.toExponential(2)+' ('+bits(lx,OM).toFixed(1)+' bits)'+
      '　/　improved '+e2.toExponential(2)+' ('+bits(lx,OM2).toFixed(1)+' bits)'+
      (lx>3?'　★ no real lattice reaches here — extrapolation does':'');
  }
  sx.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-44-lattice.html', acc='#3a4a7a', ops='#7a3a4a',
      title='Discretisation ── c·t = const, That Clicks, Episode 44 (Part V)',
      ep='EPISODE 44 ／ Part V — where the tool breaks',
      eyebrow='What was demanded was never absence',
      h1='The scale only has<br>to become irrelevant',
      sub='A lattice spacing is a smallest length, yet conformal field theories are computed on lattices.<br><em>Because conformal invariance belongs to the fixed point, not to the lattice.</em>',
      byline_l='What you need: Episode 3\'s procedure, Episode 14\'s anomalous dimensions, Episode 19\'s scale, Episode 36\'s (A)/(B), Episode 43',
      byline_r='0.83 bits per halving of the lattice spacing',
      body=BODY + '\n\n<p class="foot">This document is Episode 44 of "c·t = const, That Clicks" (the eighth of Part V), written for physics-minded high-school and university readers. The renormalisation group, universality, the continuum limit of lattice theories and the conformal bootstrap are all established standard material and nothing here is a new claim — the numbers are computed in kenshou/calc48.py. The values quoted are the 3D Ising bootstrap of Kos, Poland, Simmons-Duffin &amp; Vichi (2016) and the lattice Monte Carlo of Hasenbusch (2010), the 3D XY bootstrap of Chester et al. (2019), and the \\(^4\\)He experiment of Lipa et al. (2003). <strong>§03\'s agreement follows from the lattice side having taken the continuum limit</strong> — these are not raw finite-lattice numbers but values extrapolated from several sizes with improved actions cancelling the leading correction, and <em>a naive computation on a \\(10^3\\) lattice still carries a 0.3 per cent error</em>. <strong>§02\'s "irrelevant" is renormalisation-group jargon</strong>, and which operators are irrelevant differs between theories and is not obvious — for gravity that is exactly the open question of Episode 35. <strong>§07\'s helium discrepancy is still under discussion</strong>, with systematic errors suggested on both the experimental and the theoretical side; <em>this document claims nothing beyond "it is unresolved"</em>, and the \\(6.0\\sigma\\) simply combines the quoted errors. §04\'s universality examples are a textbook summary and <em>not all are confirmed to the same precision</em>. <strong>§08\'s (B) is not a claim that spacetime is discrete</strong> but a statement that the reading is logically available — whether spacetime is discrete is unresolved, and this document endorses neither answer. The "improved action" curve in the figure is schematic and does not represent the performance of any particular method. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the lattice fineness to see how many bits it buys. "Show the answer" opens each solution.')
