# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Part V's eight episodes go onto one page — quantum anomalies, the conformal factor problem, rotating spacetime, gravitational entropy, the Weyl curvature hypothesis, the black hole interior, the Planck scale, discretisation. Laid out together, what becomes clear is that <em>what we kept calling "breaking" was never once a malfunction</em>. And — <strong>the tool touches exactly half the world. The arrow of time is written in the other half.</strong></p>

<h2><span class="n">01</span>Eight episodes on one table</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Ep.</th><th>Title</th><th class="mid">What happened</th><th class="mid">Class</th><th class="mid">What we got</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">37</th><td>Quantum anomalies</td><td class="mid">a \(\mu\) is brought in</td><td class="mid"><strong>a scale entered</strong></td><td class="mid">the breaking measured at 28.7 bits</td></tr>
<tr><th class="mid">38</th><td>The conformal factor problem</td><td class="mid">\(\Omega\) becomes a field</td><td class="mid">the tool worked correctly</td><td class="mid">what was broken was the theory</td></tr>
<tr class="hi"><th class="mid">39</th><td>Rotating spacetime</td><td class="mid">Weyl \(\ne0\)</td><td class="mid"><strong>an untouchable structure</strong></td><td class="mid">Step 3 — cannot be flattened</td></tr>
<tr><th class="mid">40</th><td>Gravitational entropy</td><td class="mid">everything dimensionless</td><td class="mid">inside the tool's reach</td><td class="mid">three \(10^{122}\)s became one</td></tr>
<tr class="hi"><th class="mid">41</th><td>The Weyl curvature hypothesis</td><td class="mid">Weyl \(=0\) at the start</td><td class="mid"><strong>a demand on the untouchable side</strong></td><td class="mid">the direction of time</td></tr>
<tr><th class="mid">42</th><td>Inside a black hole</td><td class="mid">event vs apparent</td><td class="mid">only one is touched</td><td class="mid">causal is 0, \(\theta=0\) is not</td></tr>
<tr class="hi"><th class="mid">43</th><td>The Planck scale</td><td class="mid">\(\ell_P\) has weight \(+1\)</td><td class="mid"><strong>a scale entered</strong></td><td class="mid">excluded by hypothesis</td></tr>
<tr><th class="mid">44</th><td>Discretisation</td><td class="mid">\(a\) is irrelevant</td><td class="mid">no scale left in the answer</td><td class="mid">then it comes back</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">02</span>There were only two kinds of failure</h2>

<div class="seven">
<div class="row"><div class="mk">A</div><div class="txt"><strong>A scale was brought in</strong><span>Episode 37 (\(\mu\)), 43 (\(\ell_P\)), 44 (\(a\)) — the tool is <em>reporting correctly</em>; whether it survives depends on relevance</span></div></div>
<div class="row"><div class="mk">B</div><div class="txt"><strong>A structure outside the conformal class</strong><span>Episode 39 (Weyl), 42 (the apparent horizon) — the tool <em>has nothing to say</em>, and not touching it is correct</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>Neither is a malfunction</strong><span>A is the report "a scale entered"; B is the report "that is not mine to handle"</span></div></div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>The core — the tool touches exactly half the curvature</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Components</th><th class="mid">Under \(g\to\Omega^2g\)</th><th class="mid">The tool</th><th class="mid">What they are</th></tr></thead>
<tbody>
<tr><th>Ricci, 10</th><td class="mid"><strong>change</strong></td><td class="mid">touches them</td><td class="mid">the side matter fixes</td></tr>
<tr class="hi"><th>Weyl, 10</th><td class="mid">\(C^a{}_{bcd}\) is <strong>conformally invariant</strong></td><td class="mid"><strong>does not touch</strong></td><td class="mid">gravitational waves and tides</td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">The Riemann curvature has 20 independent components in four dimensions</span>
$$\underbrace{10}_{\text{touched}}\;:\;\underbrace{10}_{\text{untouched}}\;=\;\textbf{exactly half}$$
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0">"The tool cannot reach Kerr" is not a weakness of the tool —<br>
<strong>the Weyl curvature <em>is</em> the part a conformal transformation preserves.</strong><br>
── <em>The tool has not failed. It is drawing the boundary of its own jurisdiction, precisely.</em></p>
</div>

<div class="fig">
<p class="cap">Figure: the 20 curvature components split into the half the tool touches and the half it does not — <strong>exactly ten each</strong>. Move the conformal factor \(\Omega\) and <em>only the left half moves; the right half does not budge</em> — and <strong>the arrow of time is written in that unmoving right half.</strong></p>
<canvas id="cv" width="720" height="340"></canvas>
<div class="controls">
  <label>conformal factor \(\Omega\)<input id="so" type="range" min="30" max="300" value="100" step="1"></label>
  <span class="val" id="vo">1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#5a4a2a"></i>Ricci, 10 (touched = bookkeeping)</span>
  <span><i class="swatch" style="background:#2a5a5a"></i>Weyl, 10 (untouched = physics)</span>
</div>
</div>

<h2><span class="n">04</span>Which makes Episode 41 look different</h2>

<div class="seven">
<div class="row"><div class="mk">41</div><div class="txt"><strong>The Weyl curvature hypothesis demands Weyl \(=0\) at the initial singularity</strong><span>and by §03, Weyl is the side <em>a conformal transformation does not touch</em></span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>The arrow of time is written entirely in the half the tool cannot touch</strong><span>Episode 41 said "from where it reaches to where it does not"; more precisely, <em>the arrow itself is defined by untouchable quantities</em></span></div></div>
<div class="row"><div class="mk">→</div><div class="txt"><strong>Which is why the arrow cannot be moved</strong><span>it is written in a quantity the tool cannot move</span></div></div>
</div>

<h2><span class="n">05</span>The bits measured in Part V</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">bits</th><th class="mid">note</th></tr></thead>
<tbody>
<tr><th>Ep. 37: the breaking of conformal symmetry in QED</th><td class="mid">\(28.7\)</td><td class="mid">against the noise floor</td></tr>
<tr><th>Ep. 38: the path-integral weight at \(n=50\)</th><td class="mid">\(8498\)</td><td class="mid">toy model, unbounded</td></tr>
<tr><th>Ep. 39: high spins just below the bound</th><td class="mid">\(4.3\)</td><td class="mid">the band (explained)</td></tr>
<tr><th>Ep. 40: unused capacity</th><td class="mid">\(59.3\)</td><td class="mid">doublings</td></tr>
<tr class="hi"><th>Ep. 41: how special the initial state was</th><td class="mid"><strong>\(3.27\times10^{122}\)</strong></td><td class="mid">= the same number as Eps. 24 and 40</td></tr>
<tr><th>Ep. 42: unreadable inside M87\(^*\)</th><td class="mid">\(126.5\)</td><td class="mid">short even on the loosest bound</td></tr>
<tr><th>Ep. 43: from the LHC to the Planck length</th><td class="mid">\(49.7\)</td><td class="mid">doublings</td></tr>
<tr><th>Ep. 44: bought by halving the lattice spacing</th><td class="mid">\(0.83\)</td><td class="mid">per halving</td></tr>
</tbody>
</table>
</div>

<p><strong>These are written in the same unit but are not the same thing</strong> — surprise, headroom, shortfall, gain. The same caution as Episodes 26 and 36. <em>Still, one thing can be said</em>: <strong>all of them sit in the dimensionless column.</strong> Only the apparent horizon and \(\ell_P\) failed to (Episode 43 §07).</p>

<h2><span class="n">06</span>Connecting to Part IV's wrap-up</h2>

<div class="seven">
<div class="row"><div class="mk">36</div><div class="txt"><strong>Part IV: good theories have already performed Episode 3's surgery</strong><span>── a conclusion about <em>theories</em></span></div></div>
<div class="row"><div class="mk">45</div><div class="txt"><strong>Part V: the tool touches exactly half — the dimensionful side</strong><span>── a conclusion about <em>the world</em></span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>The two have the same shape</strong><span>on the theory side, "separate (A) notation from (B) claim"; on the world side, "which half is touched is already fixed" — <em>both restate the one procedure from Episode 3</em></span></div></div>
</div>

<div class="aside">
<span class="tag">Parts I to V, one line each</span>
<strong>Part I</strong>: \(c\cdot t=\)const is a notation, not a model.<br>
<strong>Part II</strong>: wherever you put it, only one thing moves, and only its size is touched.<br>
<strong>Part III</strong>: measured as information, it was one number restated in eight languages.<br>
<strong>Part IV</strong>: applied to other theories, the good ones had already done the surgery.<br>
<strong>Part V</strong>: <em>the tool touches exactly half the world. The arrow of time is in the other half.</em>
</div>

<div class="caveat">
<span class="tag">The honest line — for Part V as a whole</span>
<p style="margin:0 0 10px"><strong>(1) §03's "exactly half" is a component count in four dimensions.</strong> Riemann 20 = Ricci 10 + Weyl 10 is correct, and the conformal invariance of \(C^a{}_{bcd}\) is standard, but <em>phrasing "touched / untouched" as a count of components is this series' way of putting it</em>. In \(D\) dimensions the ratio changes (Weyl vanishes identically at \(D=3\); at \(D=5\) it is 10:35) — <strong>"exactly half" is a property of \(D=4\) alone</strong>, which is part of what makes it interesting.</p>
<p style="margin:0 0 10px"><strong>(2) §02's "only two kinds of failure" is this series' sorting.</strong> Placing Episode 38 under "the tool worked correctly" is <em>a choice of reading</em>; whether to call it "the tool exposed a pathology" or "a limit of applicability" depends on one's stance.</p>
<p style="margin:0 0 10px"><strong>(3) §05's table lines up things that share a unit but not a meaning.</strong> Surprise (Eps. 37, 39), headroom (Ep. 40), shortfall (Eps. 42, 43), gain per step (Ep. 44) — <em>they cannot be added or compared</em>. The bit shows only that all of it can be written in one currency; it is not a league table (the same caution as Episode 36 §05).</p>
<p style="margin:0 0 10px"><strong>(4) §04's "the arrow is written on the untouchable side" holds if one adopts the Weyl curvature hypothesis.</strong> <em>That hypothesis is not an established law</em> (Episode 41, caveat 5) — other positions on the origin of the arrow of time exist, and this document does not endorse the hypothesis.</p>
<p style="margin:0"><strong>(5) Part V mixes established material with this series' readings.</strong> Quantum anomalies, the conformal factor problem, the Kerr solution, black hole thermodynamics, the renormalisation group and universality are <em>all standard physics</em>. But "the place where the tool breaks moves" (Ep. 38), "the arrow of time can be restated as the tool's reach" (Ep. 41) and "it touches exactly half" (this one) are <strong>readings this series found by laying things side by side</strong>, not claims found in textbooks.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (Part V wrap-up)</p>
<ol>
<li>How many kinds of "failure" occurred in Part V?
<details><summary>Show the answer</summary><div class="ans"><strong>Two.</strong> A: a scale was brought in (Eps. 37, 43, 44) — <em>the tool is reporting correctly</em>. B: a structure outside the conformal class (Eps. 39, 42) — <em>the tool has nothing to say</em>. <strong>Neither is a malfunction.</strong></div></details></li>

<li>What fraction of the curvature does a conformal transformation touch?
<details><summary>Show the answer</summary><div class="ans"><strong>Exactly half.</strong> The 20 Riemann components in four dimensions are Ricci 10 (which change) plus Weyl 10 (\(C^a{}_{bcd}\) is conformally invariant). <em>Per caveat (1), this is a property of \(D=4\) alone.</em></div></details></li>

<li>Why can the tool not reach Kerr? Is it weakness?
<details><summary>Show the answer</summary><div class="ans"><strong>Not weakness.</strong> The Weyl curvature <em>is the part a conformal transformation preserves</em> — the tool has not failed; it is <strong>drawing the boundary of its own jurisdiction, precisely.</strong></div></details></li>

<li>On which side is the arrow of time written?
<details><summary>Show the answer</summary><div class="ans"><strong>The side the tool does not touch</strong> (Weyl). The hypothesis demands Weyl \(=0\) at the initial singularity, and Weyl is conformally invariant — <em>the arrow cannot be moved precisely because it is written in a quantity the tool cannot move</em>. Per caveat (4), this holds if one adopts the hypothesis.</div></details></li>

<li>(Harder) How do Episode 36's and Episode 45's conclusions connect?
<details><summary>Show the answer</summary><div class="ans"><strong>They have the same shape.</strong> Episode 36 is about <em>theories</em> ("has (A) notation been separated from (B) claim?"); Episode 45 is about <em>the world</em> ("which half is touched is already fixed") — <strong>both restate the one procedure from Episode 3.</strong></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: the tool never once malfunctioned</h2>
<p>Laid side by side, Part V's eight episodes show that what we called "breaking" came in <strong>only two kinds</strong>. <em>A: a scale was brought in</em> (Episode 37's \(\mu\), 43's \(\ell_P\), 44's \(a\)) — here the tool is <strong>reporting correctly</strong>, and survival depends on whether the scale is irrelevant (Episode 44). <em>B: a structure outside the conformal class</em> (Episode 39's Weyl, 42's apparent horizon) — here the tool simply <strong>has nothing to say</strong>, and not touching it is correct.</p>
<p>And the most important thing this time. The 20 Riemann components in four dimensions split into <strong>Ricci 10 (which change under \(g\to\Omega^2g\)) and Weyl 10 (\(C^a{}_{bcd}\) is conformally invariant) — exactly half each</strong>. So "the tool cannot reach Kerr" is not weakness: <em>the Weyl curvature is the part a conformal transformation preserves.</em> <strong>The tool has not failed; it is drawing the boundary of its own jurisdiction, precisely.</strong></p>
<p>Which makes Episode 41 look different. The Weyl curvature hypothesis demands Weyl \(=0\) at the initial singularity, and Weyl is <em>the untouchable side</em>. In other words — <strong>the arrow of time is written entirely in the half the tool cannot touch.</strong> It cannot be moved precisely because it is written in a quantity the tool cannot move.</p>
<p>We also lined up Part V's bits — 28.7, 8498, 4.3, 59.3, \(3.27\times10^{122}\), 126.5, 49.7, 0.83. <em>Same unit, different meanings</em>, but <strong>all of them in the dimensionless column</strong>. Only the apparent horizon and \(\ell_P\) were not.</p>
<p>Finally, the connection to Part IV. Episode 36 was about <strong>theories</strong> ("good ones have already had Episode 3's surgery"); Episode 45 is about <strong>the world</strong> ("the tool touches exactly half — the dimensionful side") — <em>the two have the same shape, and both restate the one procedure from Episode 3.</em></p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 46 (Part VI begins, the final part)</span>
Part VI <strong>puts the procedure itself under examination</strong>. First: <strong>every characterisation of \(a\propto t\)</strong> — after 45 episodes on this one condition, <em>how many different ways are there to say it?</em> \(w=-1/3\), \(q=0\), the horizon being exactly \(ct\), Episode 33's \(R=6(1+k)/t^2\) vanishing, conformal time going as \(\ln t\) — <strong>we collect them all, count how many there are, and count how many are independent.</strong> The compression that worked three times in Episodes 26, 40 and 41 <em>now gets applied to the series' own subject.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var so=document.getElementById('so'), vo=document.getElementById('vo'), ro=document.getElementById('ro');
  var X0=60, X1=690, Y0=40, Y1=250, MID=(X0+X1)/2;

  function draw(){
    var om=parseInt(so.value,10)/100;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.strokeStyle='#cdc8d2'; g.lineWidth=1.6;
    g.beginPath(); g.moveTo(MID,Y0-14); g.lineTo(MID,Y1+22); g.stroke();

    g.textAlign='center';
    g.font='13px ui-sans-serif,system-ui,sans-serif';
    g.fillStyle='#5a4a2a'; g.fillText('Ricci, 10 — touched', (X0+MID)/2, Y0-22);
    g.fillStyle='#2a5a5a'; g.fillText('Weyl, 10 — untouched', (MID+X1)/2, Y0-22);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    var bw=(MID-X0-40)/10;
    for(var i=0;i<10;i++){
      var h=40*om*om; if(h>150) h=150;
      var x=X0+16+i*bw;
      g.fillStyle='#5a4a2a'; g.globalAlpha=0.85;
      g.fillRect(x, (Y0+Y1)/2-h/2, bw-6, h);
      g.globalAlpha=1;
    }
    for(var j=0;j<10;j++){
      var x2=MID+16+j*bw;
      g.fillStyle='#2a5a5a'; g.globalAlpha=0.85;
      g.fillRect(x2, (Y0+Y1)/2-20, bw-6, 40);
      g.globalAlpha=1;
    }

    g.fillStyle='#8a7a5a'; g.textAlign='center';
    g.fillText('stretched by a factor of '+(om*om).toFixed(2), (X0+MID)/2, Y1+16);
    g.fillStyle='#3a6a6a';
    g.fillText('unchanged, however you move Omega', (MID+X1)/2, Y1+16);

    g.fillStyle='#7d7686';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('the 20 Riemann components in four dimensions — exactly half each', MID, Y1+48);
    g.fillStyle='#2a5a5a';
    g.fillText('★ the arrow of time is written in this right half', (MID+X1)/2, Y1+72);

    vo.textContent=om.toFixed(2);
    ro.textContent='Omega = '+om.toFixed(2)+
      '　→　Ricci side scales by '+(om*om).toFixed(2)+'　/　Weyl side scales by 1.00 (invariant)'+
      (om<0.5?'　★ however far you shrink it, the right half does not move':'')+
      (om>2.5?'　★ however far you stretch it, the right half does not move':'');
  }
  so.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-45-partV.html', acc='#2a5a5a', ops='#5a4a2a',
      title='The tool touches exactly half ── c·t = const, That Clicks, Episode 45 (Part V wrap-up)',
      ep='EPISODE 45 ／ Part V — wrap-up',
      eyebrow='The tool never once malfunctioned',
      h1='It touches<br>exactly half',
      sub='Part V\'s "breaking" came in only two kinds — and neither was a malfunction.<br><em>And the arrow of time is in the other half.</em>',
      byline_l='What you need: Part V\'s eight episodes, Episode 3\'s procedure, Episode 33\'s three-step test, Episode 36\'s wrap-up',
      byline_r='Ricci 10 : Weyl 10 — a property of \\(D=4\\) alone',
      body=BODY + '\n\n<p class="foot">This document is Episode 45 of "c·t = const, That Clicks" (the Part V wrap-up), written for physics-minded high-school and university readers. It collects results from Episodes 37 to 44; the only new computations are §03\'s component count and §05\'s tally (kenshou/calc49.py) — for the numbers and sources of each result see the endnotes of the episode concerned. <strong>§03\'s "exactly half" is a component count in four dimensions</strong>: Riemann 20 = Ricci 10 + Weyl 10 is correct and the conformal invariance of \\(C^a{}_{bcd}\\) is standard, but <em>phrasing "touched / untouched" as a count of components is this series\' way of putting it</em>, and in \\(D\\) dimensions the ratio changes (Weyl vanishes identically at \\(D=3\\); at \\(D=5\\) it is 10:35) — <strong>"exactly half" is a property of \\(D=4\\) alone</strong>. <strong>§02\'s "only two kinds of failure" is this series\' sorting</strong>, and placing Episode 38 under "the tool worked correctly" is a choice of reading. §05\'s table lines up things that share a unit but not a meaning (surprise, headroom, shortfall, gain) and they cannot be added or compared. <strong>§04\'s "the arrow is on the untouchable side" holds if one adopts the Weyl curvature hypothesis</strong>, which is not an established law — other positions on the arrow of time exist and this document does not endorse it. <strong>Part V mixes established material with this series\' readings</strong>: quantum anomalies, the conformal factor problem, the Kerr solution, black hole thermodynamics, the renormalisation group and universality are all standard physics, while <em>"the place where the tool breaks moves", "the arrow of time can be restated as the tool\'s reach" and "it touches exactly half" are readings this series found by laying things side by side</em>, not textbook claims. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move Omega and watch only the left half respond. "Show the answer" opens each solution.')
