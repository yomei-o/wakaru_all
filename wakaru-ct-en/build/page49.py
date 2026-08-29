# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Two episodes remain. This time: <strong>the doors left open</strong> — every question opened in 48 episodes and <em>not closed</em>. Laid out together, what emerges is that <strong>there are only four kinds of door, and nearly four in ten of them cannot be closed by data.</strong> <em>Telling which kind a door is</em> has been what this series was doing all along.</p>

<h2><span class="n">01</span>Doors opened and not closed</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Ep.</th><th>Question</th><th class="mid">What would close it</th><th class="mid">Kind</th></tr></thead>
<tbody>
<tr><th class="mid">18</th><td>Does one bit \(\leftrightarrow\) 1.96 fm mean anything?</td><td class="mid">──</td><td class="mid">coincidence</td></tr>
<tr><th class="mid">29</th><td>Does MOND survive on other datasets?</td><td class="mid">clusters and the CMB</td><td class="mid">observation</td></tr>
<tr><th class="mid">34</th><td>Does conformal gravity have a CMB prediction?</td><td class="mid">the calculation is unestablished</td><td class="mid">calculation</td></tr>
<tr><th class="mid">36</th><td>Is the "band of coincidences" real?</td><td class="mid">a larger sample</td><td class="mid">observation</td></tr>
<tr><th class="mid">38</th><td>Which contour for the conformal factor is right?</td><td class="mid">a first-principles derivation</td><td class="mid">calculation</td></tr>
<tr class="hi"><th class="mid">38</th><td>Is there a theory with a ghost in neither place?</td><td class="mid">an existence or impossibility proof</td><td class="mid">calculation</td></tr>
<tr><th class="mid">40</th><td>What is the entropy of a gravitational field without a horizon?</td><td class="mid">an agreed definition</td><td class="mid">definition</td></tr>
<tr class="hi"><th class="mid">41</th><td>What explains the low initial entropy?</td><td class="mid">measuring \(r\)</td><td class="mid">observation</td></tr>
<tr><th class="mid">42</th><td>Does information come out of black holes?</td><td class="mid">a mechanism</td><td class="mid">calculation</td></tr>
<tr><th class="mid">43</th><td>Is spacetime discrete?</td><td class="mid">quadratic Lorentz violation</td><td class="mid">observation</td></tr>
<tr class="hi"><th class="mid">43</th><td>Does \(G\) transform under a conformal transformation?</td><td class="mid">── (a choice of convention)</td><td class="mid">definition</td></tr>
<tr><th class="mid">44</th><td>What is the \(6\sigma\) in \(^4\)He's \(\lambda\) transition?</td><td class="mid">replication and systematics</td><td class="mid">observation</td></tr>
<tr class="hi"><th class="mid">46</th><td>Which way does the Hubble tension fall?</td><td class="mid">the distance ladder and the CMB</td><td class="mid">observation</td></tr>
<tr><th class="mid">47</th><td>How many fundamental constants are there?</td><td class="mid">── (a choice of convention)</td><td class="mid">definition</td></tr>
<tr class="hi"><th class="mid">48</th><td>Can sensory beauty be measured?</td><td class="mid">── (outside this tool)</td><td class="mid">not measurable</td></tr>
<tr><th class="mid">48</th><td>What fixes the prior in naturalness?</td><td class="mid">── (a choice of prior)</td><td class="mid">definition</td></tr>
</tbody>
</table>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">02</span>The core — there are only four kinds of door</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Kind</th><th class="mid">Count</th><th>Character</th></tr></thead>
<tbody>
<tr><th class="mid">observation</th><td class="mid">\(6\)</td><td>data decides. <strong>It will close one day</strong></td></tr>
<tr><th class="mid">calculation</th><td class="mid">\(4\)</td><td>a proof or derivation decides. <strong>In principle it closes</strong></td></tr>
<tr class="hi"><th class="mid">definition</th><td class="mid">\(4\)</td><td>a choice of convention. <strong>Data will not close it</strong></td></tr>
<tr class="hi"><th class="mid">coincidence / not measurable</th><td class="mid">\(2\)</td><td>not worth pursuing / outside the tool. <strong>Cannot be closed</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>Six of the sixteen — nearly four in ten — cannot be closed by data.</strong><br>
"Open problems in physics" brings to mind the ones waiting on measurements,<br>
but <em>conventions and things outside the tool are about as numerous</em>.<br>
── <strong>Telling which kind of door it is, is already a result.</strong></p>
</div>

<div class="fig">
<p class="cap">Figure: the sixteen doors sorted by kind. <strong>The observational ones have expected dates; the definitional ones do not close however long you wait.</strong> Move the slider forward in years — <em>however far you go, some remain.</em></p>
<canvas id="cv" width="720" height="340"></canvas>
<div class="controls">
  <label>years from now<input id="sy" type="range" min="0" max="30" value="0" step="1"></label>
  <span class="val" id="vy">0 yr</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a3a"></i>closed by observation</span>
  <span><i class="swatch" style="background:#4a4a7a"></i>closed by calculation</span>
  <span><i class="swatch" style="background:#8a5a2a"></i>fixed by definition (never closes)</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>closed</span>
</div>
</div>

<h2><span class="n">03</span>When will the observational doors close?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>What is measured</th><th class="mid">Current value</th><th class="mid">Instrument</th><th class="mid">Timescale</th></tr></thead>
<tbody>
<tr class="hi"><th>Primordial gravitational waves \(r\)</th><td class="mid">\(<0.036\)</td><td class="mid">LiteBIRD / CMB-S4</td><td class="mid">2030s</td></tr>
<tr><th>Dark energy \(w(z)\)</th><td class="mid">\(-1.03\pm0.03\)</td><td class="mid">Euclid / DESI / Rubin</td><td class="mid">late 2020s</td></tr>
<tr><th>Variation of \(\alpha\)</th><td class="mid">\(|\Delta\alpha/\alpha|<1.4\times10^{-8}\)</td><td class="mid">optical and nuclear clocks</td><td class="mid">2020s</td></tr>
<tr class="hi"><th>The Hubble constant</th><td class="mid">\(67.4\) versus \(73.0\)</td><td class="mid">JWST / standard sirens</td><td class="mid">late 2020s</td></tr>
<tr><th>Black hole spins and mergers</th><td class="mid">model-dependent</td><td class="mid">LISA / Einstein Telescope</td><td class="mid">2030s</td></tr>
<tr><th>Discreteness of spacetime (quadratic)</th><td class="mid">\(E_{\rm QG,2}>10^{11}\) GeV</td><td class="mid">CTA and others</td><td class="mid">late 2020s</td></tr>
</tbody>
</table>
</div>

<p><strong>Most of the six observational doors are expected to settle in the 2020s and 2030s</strong> — <em>readers of this series will see the answers within their lifetimes.</em></p>

<h2><span class="n">04</span>The definitional doors do not close</h2>

<div class="seven">
<div class="row"><div class="mk">43</div><div class="txt"><strong>Does \(G\) transform?</strong><span>a choice of convention — no observation settles it</span></div></div>
<div class="row"><div class="mk">47</div><div class="txt"><strong>How many fundamental constants are there?</strong><span>likewise</span></div></div>
<div class="row hi"><div class="mk">48</div><div class="txt"><strong>What fixes the prior in naturalness?</strong><span>likewise — <em>but this does not mean it does not matter</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0"><strong>Without choosing the convention, the sentence is not finished</strong> (Episode 3).<br>
── <em>Choose, then measure. Reverse the order and you cannot see that the answer depends on the convention.</em><br>
Episode 37 §05 (is \(\alpha\) constant?) and Episode 43 §02 (a smallest length) were <strong>exactly that</strong>.</p>
</div>

<h2><span class="n">05</span>What did not change</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Statement</th><th class="mid">First stated</th><th class="mid">Since</th></tr></thead>
<tbody>
<tr class="hi"><th>\(c\cdot t=\)const is a notation, not new physics</th><td class="mid">Episode 3</td><td class="mid">reconfirmed in Episode 46</td></tr>
<tr><th>Extrapolated at face value it contradicts nucleosynthesis</th><td class="mid">previous series</td><td class="mid">unmoved</td></tr>
<tr class="hi"><th>Dimensionful is bookkeeping, dimensionless is physics</th><td class="mid">Episode 3</td><td class="mid">the SI drew the same line (Ep. 47)</td></tr>
<tr><th>Name what you compare to, or it is not yet a sentence</th><td class="mid">Episode 3</td><td class="mid">it bit twice, in Eps. 37 and 43</td></tr>
</tbody>
</table>
</div>

<p><strong>For every door that opened, one stayed shut.</strong></p>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) The count of sixteen is this series' own.</strong> <em>What counts as "one door" is arbitrary</em> — split them finely and there are more, merge them and fewer, and §02's percentage moves with it. <strong>The substance is the structure "there are four kinds", not the count</strong> (the same caution as Episode 46 §03).</p>
<p style="margin:0 0 10px"><strong>(2) §03's timescales are expectations based on published programme goals.</strong> <em>Programmes slip, and target sensitivities are not always reached</em> — the instruments and dates are <strong>the outlook as of writing (2026)</strong>, not promises, and even an item marked "settles" may return an intermediate result that settles nothing.</p>
<p style="margin:0 0 10px"><strong>(3) The four placed under "closed by calculation" may be an optimistic sorting.</strong> The black hole information problem (Episode 42) has been <em>"about to be solved" for half a century</em>, and whether "in principle it closes" is even the right description is itself uncertain.</p>
<p style="margin:0 0 10px"><strong>(4) The definitional doors should not be dismissed.</strong> A choice of convention <em>is not settled by data, but it changes what can be measured</em> — whether \(G\) transforms changed the entire meaning of the statement about a smallest length (Episode 43). <strong>"Not settled by observation" is not "unimportant".</strong></p>
<p style="margin:0"><strong>(5) This list covers only the doors this series opened.</strong> Physics has far more open problems (quantum gravity, the identity of dark matter, the baryon asymmetry, the measurement problem…) and <em>this document does not survey them</em> — it is the restricted list of "opened in 48 episodes and not closed".</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>Into how many kinds do the open doors fall?
<details><summary>Show the answer</summary><div class="ans"><strong>Four</strong> — closed by observation (6), closed by calculation (4), fixed by definition (4), coincidence or not measurable (2). <em>Telling which kind a door is, is already a result.</em></div></details></li>

<li>What fraction cannot be closed by data?
<details><summary>Show the answer</summary><div class="ans"><strong>Nearly four in ten (6 of 16, 38 per cent)</strong> — the four definitional ones plus the two that are coincidence or unmeasurable. <em>"Open problems in physics" brings to mind the observational ones, but conventions and things outside the tool are about as numerous.</em> Per caveat (1), this depends on how one counts.</div></details></li>

<li>Which observational door is likely to close first?
<details><summary>Show the answer</summary><div class="ans"><strong>The variation of \(\alpha\)</strong> (optical and nuclear clocks, 2020s), along with <strong>dark energy \(w(z)\)</strong> and <strong>the Hubble constant</strong> (both late 2020s) — <em>readers of this series will see the answers within their lifetimes</em>. Per caveat (2), these are outlooks, not promises.</div></details></li>

<li>Do the definitional doors not matter?
<details><summary>Show the answer</summary><div class="ans"><strong>They do.</strong> Without choosing the convention <em>the sentence is not finished</em> (Episode 3) — choose, then measure. Reverse the order and you cannot see that the answer depends on the convention. <strong>"Not settled by observation" is not "unimportant"</strong> (caveat 4).</div></details></li>

<li>(Harder) What never changed across 48 episodes?
<details><summary>Show the answer</summary><div class="ans">Four things — (i) \(c\cdot t=\)const is a notation, not new physics (Episode 3, reconfirmed in 46); (ii) extrapolated at face value it contradicts nucleosynthesis (previous series); (iii) dimensionful is bookkeeping and dimensionless is physics (the SI drew the same line in Episode 47); (iv) name what you compare to or it is not yet a sentence (it bit twice, in Episodes 37 and 43). <em>For every door that opened, one stayed shut.</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: there were only four kinds of door</h2>
<p>The questions opened in 48 episodes and left unclosed come to <strong>sixteen</strong>, and they fall into <strong>four kinds</strong> — <em>closed by observation</em> (6), <em>closed by calculation</em> (4), <em>fixed by definition</em> (4), <em>coincidence or not measurable</em> (2).</p>
<p>Most of the six observational ones are expected to settle in the <strong>2020s and 2030s</strong> — primordial gravitational waves (LiteBIRD / CMB-S4), dark energy \(w(z)\) (Euclid / DESI / Rubin), the variation of \(\alpha\) (optical clocks), the Hubble constant (JWST / standard sirens), black hole ringdowns (LISA / Einstein Telescope), the discreteness of spacetime (CTA). <em>Readers of this series will see the answers within their lifetimes.</em></p>
<p>But <strong>six of the sixteen — nearly four in ten — cannot be closed by data</strong>. "Open problems in physics" brings to mind the ones waiting on measurements, yet <em>conventions and things outside the tool are about as numerous</em> — and <strong>telling which kind of door it is, is already a result.</strong></p>
<p>The definitional doors must not be dismissed. <strong>Without choosing the convention, the sentence is not finished</strong> (Episode 3) — choose, then measure; reverse the order and you cannot see that the answer depends on the convention. Episode 37's "is \(\alpha\) constant?" and Episode 43's "a smallest length" were <em>exactly that</em>.</p>
<p>Finally, what <strong>never moved across 48 episodes</strong>: that \(c\cdot t=\)const is a notation and not new physics; that extrapolated at face value it contradicts nucleosynthesis; that dimensionful is bookkeeping and dimensionless is physics; and that naming what you compare to is what makes a sentence. <em>For every door that opened, one stayed shut.</em></p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 50 (the finale)</span>
The last one. Its title: <strong>"Only one thing moves"</strong> — everything done across 50 episodes, reduced to <em>a single sentence</em>. Parts I through VI, nine theories, eight places where the tool broke, sixteen open doors and four compressions — <strong>we confirm one final time that all of it followed from the one procedure built in Episode 3.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sy=document.getElementById('sy'), vy=document.getElementById('vy'), ro=document.getElementById('ro');
  var X0=54, X1=690, Y0=44;

  var D=[
    ['alpha variation', 0, 3],
    ['w(z)', 0, 4],
    ['Hubble constant', 0, 5],
    ['discreteness', 0, 6],
    ['primordial GW r', 0, 11],
    ['BH ringdown', 0, 12],
    ['MOND, other data', 0, 8],
    ['conformal gravity CMB', 1, 15],
    ['the contour', 1, 99],
    ['ghost in neither', 1, 99],
    ['BH information', 1, 99],
    ['grav. entropy definition', 2, 99],
    ['does G transform', 2, 99],
    ['how many constants', 2, 99],
    ['the naturalness prior', 2, 99],
    ['sensory beauty', 2, 99]
  ];
  var COL=['#2a5a3a','#4a4a7a','#8a5a2a'];

  function draw(){
    var yr=parseInt(sy.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    var cols=4, rows=4, cw=(X1-X0)/cols, ch=58, open=0;
    for(var i=0;i<D.length;i++){
      var r=Math.floor(i/cols), c=i%cols;
      var x=X0+c*cw, y=Y0+r*ch;
      var closed=(D[i][2]<=yr);
      if(!closed) open++;
      g.fillStyle = closed ? '#f0eef3' : COL[D[i][1]];
      g.globalAlpha = closed ? 1 : 0.9;
      g.fillRect(x+4, y, cw-10, ch-14);
      g.globalAlpha=1;
      g.fillStyle = closed ? '#b8b2c0' : '#fff';
      g.textAlign='center';
      g.fillText(D[i][0], x+cw/2-1, y+ch/2-6);
      if(closed) g.fillText('(closed)', x+cw/2-1, y+ch/2+10);
    }

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('sixteen doors — some do not close however long you wait', (X0+X1)/2, Y0+rows*ch+16);

    vy.textContent=yr+' yr';
    ro.textContent='waiting '+yr+' years　→　'+open+' of 16 doors still open'+
      (yr>=15?'　★ waiting longer will not close these 6 — conventions, and what lies outside the tool':'')+
      (yr===0?'　(the present state)':'');
  }
  sy.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-49-open-doors.html', acc='#2a5a3a', ops='#8a5a2a',
      title='The doors left open ── c·t = const, That Clicks, Episode 49 (Part VI)',
      ep='EPISODE 49 ／ Part VI — examining the procedure',
      eyebrow='Nearly four in ten cannot be closed by data',
      h1='There were only<br>four kinds of door',
      sub='Every question opened in 48 episodes and not closed, laid out.<br><em>And telling which kind a door is turned out to be a result in itself.</em>',
      byline_l='What you need: Episode 3\'s procedure, Episode 19\'s scale, the unresolved items of Parts IV and V, Episode 48',
      byline_r='Sixteen doors; six stay open however long you wait',
      body=BODY + '\n\n<p class="foot">This document is Episode 49 of "c·t = const, That Clicks" (the fourth of Part VI), written for physics-minded high-school and university readers. It collects the places in Episodes 1 to 48 marked "unresolved", "unsettled" or "not measurable"; there are no new computations (the tally is in kenshou/calc53.py) — for details see the endnotes of each episode. <strong>The count of sixteen is this series\' own, and what counts as "one door" is arbitrary</strong> — split them finely and there are more, merge them and fewer, and §02\'s percentage moves with it; <em>the substance is the structure, not the count</em>. <strong>§03\'s timescales are expectations based on published programme goals</strong>; programmes slip and target sensitivities are not always reached — the instruments and dates are <em>the outlook as of writing (2026)</em>, not promises, and an item marked "settles" may still return an intermediate result. <strong>The four placed under "closed by calculation" may be an optimistic sorting</strong> — the black hole information problem has been "about to be solved" for half a century. <strong>The definitional doors should not be dismissed</strong>: a choice of convention is not settled by data but changes what can be measured (whether \\(G\\) transforms changed the meaning of the smallest-length statement entirely) — <em>"not settled by observation" is not "unimportant"</em>. <strong>This list covers only the doors this series opened</strong>; physics has far more open problems (quantum gravity, dark matter, the baryon asymmetry, the measurement problem…) which this document does not survey. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the years forward and watch which doors never close. "Show the answer" opens each solution.')
