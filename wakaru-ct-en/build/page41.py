# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Last time we found that the early universe's gravitational entropy is <strong>exactly zero</strong> (FLRW has Weyl \(=0\)). This time we look at a proposal that <em>turns that into a law</em> — the <strong>Weyl curvature hypothesis</strong>. We count out what the famous number \(10^{10^{123}}\) actually is, and restate <em>which way the arrow of time points</em> in this series' own language.</p>

<h2><span class="n">01</span>What the Weyl curvature hypothesis says</h2>

<div class="seven">
<div class="row"><div class="mk">in</div><div class="txt"><strong>At initial singularities, the Weyl curvature \(C=0\)</strong><span>Penrose's (1979) demand</span></div></div>
<div class="row"><div class="mk">out</div><div class="txt"><strong>At final singularities (black holes), no restriction</strong><span>Weyl may be as large as it likes</span></div></div>
<div class="row hi"><div class="mk">→</div><div class="txt"><strong>A law that makes beginning and end asymmetric</strong><span>and that asymmetry, the claim goes, <em>is the origin of the arrow of time</em></span></div></div>
</div>

<div class="calc">
<span class="tag">In four dimensions the Riemann curvature has 20 independent components</span>
$$\underbrace{10}_{\text{Ricci: fixed by matter}}\;+\;\underbrace{10}_{\text{Weyl: free. Gravitational waves, tides}}$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>The hypothesis switches off <em>exactly half</em> the curvature's degrees of freedom on the initial surface.</strong></p>
</div>

<h2><span class="n">02</span>Why the demand is needed — turning the headroom into a probability</h2>

<div class="calc">
<span class="tag">Statistical mechanics: the phase-space volume ratio is \(e^{\Delta S/k_B}\)</span>
$$\exp\!\left(2.265\times10^{122}\right)=10^{\,9.84\times10^{121}}$$
<p class="lbl">so the initial state was <strong>a one-in-\(10^{10^{122}}\) draw</strong></p>
</div>

<p>Penrose writes \(10^{10^{123}}\) — <em>his estimate of \(S_{\max}\) is slightly larger; it is the same number and the same argument.</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>The core — measuring that monstrous number in bits</h2>

<div class="calc">
<span class="tag">By Episode 19's practice</span>
$$\text{surprise}=\frac{S_{\max}}{\ln 2}=\mathbf{3.27\times10^{122}\ \text{bits}}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>The \(10^{122}\)s so far</th><th class="mid">bits</th></tr></thead>
<tbody>
<tr><th>Ep. 24: information the universe has processed, \(N=C\cdot t_0\)</th><td class="mid">\(3.11\times10^{122}\)</td></tr>
<tr><th>Ep. 40: the holographic bound</th><td class="mid">\(3.27\times10^{122}\)</td></tr>
<tr><th>Ep. 40: \(S\) with all the mass as one black hole</th><td class="mid">\(3.27\times10^{122}\)</td></tr>
<tr class="hi"><th><strong>Ep. 41: how special the initial state was</strong></th><td class="mid"><strong>\(3.27\times10^{122}\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>All four are the same number.</strong><br>
Penrose's \(10^{10^{123}}\) is, in this series' currency, <strong>\(3.3\times10^{122}\) bits</strong> — <em>a familiar number.</em><br>
── After Episodes 26 and 40, <strong>the compression works a third time.</strong></p>
</div>

<h2><span class="n">04</span>The ledger — is this the series' best deal?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Theory</th><th class="mid">Pays [bits]</th><th class="mid">Buys</th><th class="mid">Amount bought</th></tr></thead>
<tbody>
<tr><th>Inflation (Ep. 27)</th><td class="mid">\(10.73\)</td><td class="mid">horizon, flatness, \(n_s\)</td><td class="mid">assessed at \(-6.5\)</td></tr>
<tr><th>Cosmon (Ep. 32)</th><td class="mid">\(10.73\)</td><td class="mid">the size of \(\rho_\Lambda\)</td><td class="mid">up to \(408\)</td></tr>
<tr><th>MOND (Ep. 29)</th><td class="mid">\(21.46\)</td><td class="mid">rotation curves</td><td class="mid">\(+1971\) (a loss)</td></tr>
<tr class="hi"><th><strong>Weyl curvature hypothesis</strong></th><td class="mid"><strong>\(5.37\)</strong></td><td class="mid">how special the initial state was</td><td class="mid"><strong>\(3.27\times10^{122}\)</strong></td></tr>
</tbody>
</table>
</div>

<p>On the ledger it is <strong>better by many orders of magnitude than anything else in this series</strong> (a ratio of \(6\times10^{121}\)). But — <em>the price "one law = one parameter = 5.37 bits" is a convenience from Episode 5</em>, and <strong>there is no guarantee that a boundary condition can be bought at a parameter's price</strong>. That is this episode's weakest point (honest line 2).</p>

<h2><span class="n">05</span>The arrow of time runs from where the tool reaches to where it does not</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Epoch</th><th class="mid">Weyl</th><th class="mid">Step (Ep. 33)</th><th class="mid">Conformal transformation</th></tr></thead>
<tbody>
<tr class="hi"><th>Initial singularity (the hypothesis)</th><td class="mid">\(C=0\)</td><td class="mid"><strong>Step 2: conformally flat</strong></td><td class="mid"><strong>reaches</strong></td></tr>
<tr><th>The universe now (globally FLRW)</th><td class="mid">\(C\approx0\)</td><td class="mid">Step 2</td><td class="mid">nearly reaches</td></tr>
<tr class="hi"><th>The end state (black holes, Ep. 39)</th><td class="mid">\(C\ne0\)</td><td class="mid"><strong>Step 3</strong></td><td class="mid"><strong>does not reach</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>The arrow of time runs from where conformal transformations reach to where they do not.</strong><br>
── The "the tool breaks / the tool cannot reach" of Part V turns out to be <em>the direction of time itself.</em></p>
</div>

<div class="fig">
<p class="cap">Figure: the life of the universe seen through Weyl curvature. <strong>At the left (the beginning) Weyl is 0 and we are in Step 2; further right Weyl grows and we cross into Step 3.</strong> Move the slider to see where the tool stops reaching — <em>that boundary is the arrow of time.</em></p>
<canvas id="cv" width="720" height="350"></canvas>
<div class="controls">
  <label>epoch (log steps, Episode 2)<input id="st" type="range" min="0" max="1000" value="600" step="1"></label>
  <span class="val" id="vt">84.1</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3a5a3a"></i>Step 2 (conformally flat, the tool reaches)</span>
  <span><i class="swatch" style="background:#8a4a2a"></i>Step 3 (Weyl not 0, it does not)</span>
</div>
</div>

<h2><span class="n">06</span>The link to Episode 31 — the same demand, seen twice</h2>

<div class="seven">
<div class="row"><div class="mk">31</div><div class="txt"><strong>CCC: to glue aeons there must be no ruler at the boundary</strong><span>= only the conformal structure survives there = <em>the demand that Weyl \(=0\)</em></span></div></div>
<div class="row"><div class="mk">41</div><div class="txt"><strong>The hypothesis: Weyl \(=0\) at the initial singularity</strong><span>= the explanation of why the beginning was special</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>The same demand put to two different uses</strong><span>CCC for "there is a continuation", the hypothesis for "the beginning was special" — <em>Penrose's two proposals share one root</em></span></div></div>
</div>

<h2><span class="n">07</span>Can it be observed?</h2>

<div class="calc">
<span class="tag">Weyl curvature is the gravitational-wave degree of freedom</span>
$$\text{Weyl}=0\ \text{initially}\ \Longrightarrow\ \text{no primordial gravitational waves}$$
<p class="lbl">the current bound is \(r<0.036\) (BICEP/Keck 2021, 95% CL) → <strong>4.8 bits</strong> by Episode 19's practice</p>
</div>

<p>So far <strong>no primordial gravitational waves have been found</strong> — a tailwind for the hypothesis. <em>But the logic is not airtight</em>: the hypothesis is a demand on <strong>the singularity itself</strong>, while inflation concerns the stage after it. <em>A non-zero \(r\) would not immediately refute the hypothesis.</em></p>

<h2><span class="n">08</span>The objection — inflation is not a substitute</h2>

<div class="aside">
<span class="tag">The debate</span>
<strong>Objection:</strong> "Is the special beginning not already explained by inflation?"<br>
<strong>Penrose's reply:</strong> starting inflation <em>itself requires a low-entropy initial state</em>. It presupposes the very thing to be explained.<br>
── <em>The two are not substitutes, on Penrose's view. This debate is unsettled, and this document endorses neither side.</em>
</div>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) The numbers in §02 and §03 inherit Episode 40's estimates directly.</strong> \(S_{\max}\) is the holographic bound counted on the Hubble sphere, and <em>it moves by an order of magnitude depending on which horizon is used</em> (Episode 40, caveat 2). The difference between \(10^{10^{122}}\) and \(10^{10^{123}}\) is of that size.</p>
<p style="margin:0 0 10px"><strong>(2) §04's ledger is this episode's weakest point.</strong> "One law = 5.37 bits" was built in Episode 5 as <em>the price of a parameter</em>, and <strong>there is no guarantee that a boundary condition can be bought at that price</strong>. Strictly, specifying an initial condition should be paid for by <em>the description length needed to write that condition down</em>, which could be far larger than 5.37 bits — §04 is <strong>an observation that it looks like a good deal, not a proof</strong>.</p>
<p style="margin:0 0 10px"><strong>(3) "Phase-space volume ratio \(=e^{\Delta S}\)" may be too naive once gravity is involved.</strong> Whether black-hole entropy really is the logarithm of a phase-space volume is <em>an open question in quantum gravity</em>, and §02's probability reading rests on that assumption.</p>
<p style="margin:0 0 10px"><strong>(4) §07's observational link is not airtight.</strong> The hypothesis is a demand at the singularity and <em>does not directly say that no primordial gravitational waves are generated during the evolution afterwards</em> — read "the bound on \(r\) is a tailwind" as <strong>circumstantial</strong>. The 4.8 bits also assumes a uniform prior over \(r\in[0,1]\).</p>
<p style="margin:0"><strong>(5) The Weyl curvature hypothesis is a hypothesis, not an established law.</strong> Even its formulation is debated (how to state "Weyl \(=0\)" rigorously at a singularity is not obvious), and <em>this document endorses neither it nor inflation</em>. The academic standard remains the \(\Lambda\)CDM model including inflation.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>What does the hypothesis switch off on the initial surface? Put it in numbers.
<details><summary>Show the answer</summary><div class="ans">Of the 20 independent components of the Riemann curvature in four dimensions, <strong>the 10 Weyl components</strong> — <em>exactly half the curvature's degrees of freedom</em>. The other 10 are Ricci, fixed by matter through the Einstein equations.</div></details></li>

<li>How many bits is Penrose's \(10^{10^{123}}\)?
<details><summary>Show the answer</summary><div class="ans"><strong>\(3.3\times10^{122}\) bits</strong> (\(S_{\max}/\ln2\)) — <em>the same number as Episode 24's \(N=C\cdot t_0\) and Episode 40's holographic bound</em>. <strong>Four headline numbers turned out to be one.</strong></div></details></li>

<li>Where is §04's ledger weak?
<details><summary>Show the answer</summary><div class="ans">In assuming a boundary condition can be bought at "one law = 5.37 bits". Episode 5's 5.37 bits is <em>the price of a parameter</em>, and there is no guarantee it applies to specifying an initial condition — strictly one should pay the description length of writing that condition down, which may be far larger.</div></details></li>

<li>State the arrow of time in terms of Episode 33's three-step test.
<details><summary>Show the answer</summary><div class="ans"><strong>It runs from Step 2 (conformally flat, the tool reaches) to Step 3 (Weyl \(\ne0\), it does not).</strong> The initial singularity has Weyl \(=0\); the final black holes have Weyl \(\ne0\) — <em>Part V's "the tool breaks / cannot reach" turns out to be the direction of time itself.</em></div></details></li>

<li>(Harder) How is Episode 31's CCC related to this hypothesis?
<details><summary>Show the answer</summary><div class="ans"><strong>They are the same demand put to different uses.</strong> CCC requires that there be no ruler at the gluing boundary (= only the conformal structure survives = Weyl \(=0\)); the hypothesis places the same condition to explain why the beginning was special — <em>Penrose's two proposals share one root</em>.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: the monstrous number was a familiar one</h2>
<p>The Weyl curvature hypothesis demands <strong>Weyl \(=0\) at initial singularities and nothing at final ones</strong>. Of the 20 Riemann components in four dimensions it switches off <em>the 10 Weyl components — exactly half</em> — on the initial surface.</p>
<p>Why is it needed? Turning Episode 40's headroom into a probability, the initial state was <strong>a one-in-\(10^{10^{122}}\) draw</strong> (Penrose writes \(10^{10^{123}}\)). But measured in bits that is <strong>\(3.27\times10^{122}\) bits</strong> — <em>exactly the same number as Episode 24's \(N=C\cdot t_0\) and Episode 40's holographic bound</em>. <strong>Four headline numbers were one.</strong> After Episodes 26 and 40, that is the third compression.</p>
<p>On the ledger: pay 5.37 bits, buy \(3.27\times10^{122}\) — <em>it looks like a spectacular deal</em>. But <strong>there is no guarantee that a boundary condition can be bought at a parameter's price</strong>, and that is this episode's weakest point.</p>
<p>And the most important thing this time. Lining up beginning and end on Episode 33's three-step test: <strong>the beginning has Weyl \(=0\) and is Step 2 (conformally flat, the tool reaches); the final black holes have Weyl \(\ne0\) and are Step 3 (it does not)</strong>. In other words — <em>the arrow of time runs from where conformal transformations reach to where they do not.</em> Part V's "the tool breaks / cannot reach" turns out to be <strong>the direction of time itself.</strong></p>
<p>Finally, it is the same demand as Episode 31's CCC — no ruler at the boundary, which is Weyl \(=0\). <em>Penrose's two proposals share one root.</em></p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 42</span>
This time the end state turned out to be <strong>Step 3</strong>, where the tool does not reach. Next time we go inside it — <strong>the interior of a black hole</strong>. What does a conformal transformation do inside the horizon, and what does "<em>is information lost?</em>" look like in this series' currency? <strong>Where do the \(1.5\times10^{77}\) bits counted in Episode 40 actually go?</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var st=document.getElementById('st'), vt=document.getElementById('vt'), ro=document.getElementById('ro');
  var X0=76, X1=690, Y0=40, Y1=250;
  var S0=0, S1=140.24;

  function px(s){ return X0+(s-S0)/(S1-S0)*(X1-X0); }
  function weyl(s){ var x=(s-95)/45; return 1/(1+Math.exp(-6*(x-0.55))); }
  function py(w){ return Y1-w*(Y1-Y0); }

  function draw(){
    var s=parseInt(st.value,10)/1000*S1;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    var sc=0; for(var i=0;i<=600;i++){ var v=S0+(S1-S0)*i/600; if(weyl(v)>0.5){ sc=v; break; } }
    g.fillStyle='#eef2ee'; g.fillRect(X0,Y0,px(sc)-X0,Y1-Y0);
    g.fillStyle='#f6efe9'; g.fillRect(px(sc),Y0,X1-px(sc),Y1-Y0);
    g.fillStyle='#5a7a5a'; g.textAlign='center';
    g.fillText('Step 2: conformally flat — the tool reaches', (X0+px(sc))/2, Y0+18);
    g.fillStyle='#a06a4a';
    g.fillText('Step 3: Weyl not 0 — it does not', (px(sc)+X1)/2, Y0+18);

    g.strokeStyle='#3a5a3a'; g.lineWidth=2.8; g.beginPath();
    for(var k=0;k<=400;k++){
      var v2=S0+(S1-S0)*k/400, X=px(v2), Y=py(weyl(v2));
      if(v2>sc){ g.stroke(); g.strokeStyle='#8a4a2a'; g.lineWidth=2.8; g.beginPath(); g.moveTo(X,Y); }
      else if(k===0) g.moveTo(X,Y); else g.lineTo(X,Y);
    }
    g.stroke();

    g.textAlign='center'; g.fillStyle='#9c96a4';
    var marks=[[0,'initial singularity'],[99.6,'nucleosynthesis'],[129.7,'CMB'],[140.2,'now']];
    for(var m=0;m<marks.length;m++){
      var X3=px(marks[m][0]);
      g.strokeStyle='#e6e2ea'; g.lineWidth=1; g.setLineDash([2,3]);
      g.beginPath(); g.moveTo(X3,Y0); g.lineTo(X3,Y1); g.stroke(); g.setLineDash([]);
      g.fillText(marks[m][1], X3, Y1+18);
    }

    var X4=px(s), W=weyl(s);
    g.strokeStyle='#5a5262'; g.lineWidth=1.8; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(X4,Y0); g.lineTo(X4,Y1); g.stroke(); g.setLineDash([]);
    g.fillStyle= W>0.5 ? '#8a4a2a' : '#3a5a3a';
    g.beginPath(); g.arc(X4,py(W),5,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('log steps (Episode 2) — the arrow of time runs left to right', (X0+X1)/2, Y1+42);
    g.save(); g.translate(24,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('growth of Weyl curvature (schematic)', 0,0); g.restore();

    vt.textContent=s.toFixed(1);
    ro.textContent='log step '+s.toFixed(1)+
      '　→　Weyl grown to '+(100*W).toFixed(1)+' per cent　/　'+
      (W>0.5?'Step 3: conformal transformations do not reach':'Step 2: conformal transformations reach')+
      (s<1?'　★ the hypothesis demands exactly 0 right here':'')+
      '　※ the curve is schematic, not a numerical prediction';
  }
  st.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-41-weyl-hypothesis.html', acc='#3a5a3a', ops='#8a4a2a',
      title='The Weyl curvature hypothesis ── c·t = const, That Clicks, Episode 41 (Part V)',
      ep='EPISODE 41 ／ Part V — where the tool breaks',
      eyebrow='The monstrous number was a familiar one',
      h1='Time runs from where<br>the tool reaches',
      sub='Measured in bits, Penrose\'s \\(10^{10^{123}}\\) is the same number that has appeared three times already.<br><em>And the direction of time can be restated as the reach of a conformal transformation.</em>',
      byline_l='What you need: Episode 19\'s scale, Episode 24, Episode 31\'s CCC, Episode 33\'s three-step test, Episode 40',
      byline_r='\\(3.27\\times10^{122}\\) bits — the same number, a fourth time',
      body=BODY + '\n\n<p class="foot">This document is Episode 41 of "c·t = const, That Clicks" (the fifth of Part V), written for physics-minded high-school and university readers. The Weyl curvature hypothesis is Penrose\'s (1979) proposal, and the \\(10^{10^{123}}\\) estimate is his — the numbers are computed in kenshou/calc45.py. <strong>§02 and §03 inherit Episode 40\'s estimates directly</strong>: \\(S_{\\max}\\) is the holographic bound counted on the Hubble sphere and moves by an order of magnitude depending on which horizon is used — the difference between \\(10^{10^{122}}\\) and \\(10^{10^{123}}\\) is of that size. <strong>§04\'s ledger is this episode\'s weakest point</strong>: "one law = 5.37 bits" was built in Episode 5 as <em>the price of a parameter</em>, and <strong>there is no guarantee a boundary condition can be bought at that price</strong> — strictly one should pay the description length of the condition, possibly far larger, so §04 is an observation that it looks like a good deal, not a proof. <strong>"Phase-space volume ratio = \\(e^{\\Delta S}\\)" may be too naive once gravity is involved</strong>; whether black-hole entropy really is the logarithm of a phase-space volume is an open question in quantum gravity. <strong>§07\'s observational link is not airtight</strong> — the hypothesis is a demand at the singularity and does not directly forbid primordial gravitational waves generated afterwards, so the bound on \\(r\\) is circumstantial (and the 4.8 bits assumes a uniform prior). <strong>The hypothesis is a hypothesis, not an established law</strong>, and even its formulation is debated — <em>this document endorses neither it nor inflation</em>; the academic standard remains the \\(\\Lambda\\)CDM model including inflation. The curve in the figure is schematic, not a numerical prediction. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the slider to see where the tool stops reaching. "Show the answer" opens each solution.')
