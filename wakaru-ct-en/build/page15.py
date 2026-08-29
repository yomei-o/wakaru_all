# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Part II closes at the farthest remove — <strong>chemistry and biology</strong>. Bond energy ÷ \(k_BT\), the Arrhenius factor, pH, Kleiber's exponent, heartbeats per lifetime, the information content of DNA. <em>All dimensionless without exception</em>, so nothing changes by a character in this picture. And the conclusion that follows is a strong one: <strong>life cannot, in principle, know whether the universe is "expanding" or "growing in mass".</strong></p>

<h2><span class="n">01</span>Chemistry comes through entirely intact</h2>

<div class="calc">
<span class="tag">The exponent is dimensionless</span>
$$k\ \propto\ \exp\!\left(-\frac{E_a}{k_BT}\right)$$
<p class="lbl">\(E_a\) and \(k_BT\) both have weight \(-1\), so the ratio is invariant</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Chemical quantity</th><th class="mid">Content</th><th class="mid">In this picture</th></tr></thead>
<tbody>
<tr class="hi"><th>Arrhenius factor</th><td class="mid">\(e^{-E_a/k_BT}\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Equilibrium constant</th><td class="mid">\(e^{-\Delta G/RT}\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>pH</th><td class="mid">log of a concentration ratio</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Bond energy ÷ thermal energy</th><td class="mid">\(E_b/k_BT\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Ratios of reaction rates</th><td class="mid">──</td><td class="mid"><strong>invariant</strong></td></tr>
</tbody>
</table>
</div>

<p>Exactly the reason tunnelling was invariant in Episode 8 — <em>the exponent is dimensionless</em>. So the Sun's burning rate and enzyme kinetics are both untouched here.</p>

<h2><span class="n">02</span>Taking Kleiber's law apart</h2>

<p>The most famous scaling law in biology — <strong>metabolic rate goes as body mass to the 3/4</strong>, holding over six orders of magnitude from mouse to elephant.</p>

<div class="calc">
<span class="tag">Weight of each part</span>
<p class="lbl">Metabolic rate \(B\) (energy per time = \(ML^2/T^3\))</p>
$$w(B)=-1+2\cdot1-3\cdot1\cdot(-1)\ \Longrightarrow\ w=-2\qquad(\times a^2)$$
<p class="lbl">Body mass \(M\)</p>
$$w(M)=-1\qquad(\times a)$$
<p class="lbl">For \(B=CM^{3/4}\) to keep its form</p>
$$w(C)=-2-\tfrac34(-1)=-\tfrac54\qquad(\times a^{5/4})$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0"><strong>The exponent 3/4 is invariant. The coefficient \(C\) moves as \(\times a^{5/4}\).</strong><br>
The coefficient is dimensionful — bookkeeping. <em>The gauge-invariant statement is "the ratio of two animals' metabolic rates = (mass ratio)\(^{3/4}\)"</em>, a ratio of ratios, which does not move.</p>
</div>

<p>The surgery of Episode 3 (on the series title), Episode 9 (on the atom) and Episode 12 (on the cosmological constant) applies here in the same shape — <strong>the 3/4 in "metabolic rate goes as mass to the 3/4" is physics; the coefficient is bookkeeping.</strong></p>

<h2><span class="n">03</span>Heartbeats per lifetime were dimensionless</h2>

<div class="calc">
<span class="tag">Multiply and the mass cancels</span>
$$\text{heart rate}\ \propto M^{-1/4},\qquad \text{lifespan}\ \propto M^{+1/4}$$
<p class="lbl">so the product is</p>
$$\text{heartbeats per lifetime}\ \propto M^{0}\ \simeq\ 1.5\times10^{9}$$
</div>

<p>Mouse and elephant alike, roughly 1.5 billion beats in a lifetime. <strong>Independent of mass — that is, dimensionless.</strong> So the same 1.5 billion here.</p>

<div class="aside">
<span class="tag">What do you measure a life in?</span>
Lifespan is a time, weight \(+1\), so it shrinks as \(\div a\) here. Mice and elephants alike become <em>shorter-lived with time</em>. But the heart rate speeds up by the same factor, so <strong>the number of beats is unchanged</strong>. <em>Measure a life in seconds and it shrinks; measure it in heartbeats and it does not</em> — the same structure as Episode 9's "the Bohr radius shrinks but has nothing to compare against".
</div>

<h2><span class="n">04</span>Listing everything life can measure</h2>

<div class="fig">
<p class="cap">Figure: the top row is <strong>dimensionful quantities</strong> (mass, length, metabolic rate, lifespan) — drag back in time and they thrash. The bottom row is <strong>what life actually measures</strong> — <em>every one pinned to 1</em>.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Which epoch, \(\log_{10}a\) (right edge = today)<input id="sa" type="range" min="-2000" max="0" value="-700" step="1"></label>
  <span class="val" id="va">a = 0.200</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6b4a7a"></i>dimensionful quantities (move)</span>
  <span><i class="swatch" style="background:#a06020"></i>what life measures (do not move)</span>
</div>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>What life can measure</th><th class="mid">Content</th><th class="mid">In this picture</th></tr></thead>
<tbody>
<tr><th>Concentration ratios</th><td class="mid">count ÷ count</td><td class="mid">invariant</td></tr>
<tr><th>Ratios of reaction rates</th><td class="mid">time ÷ time</td><td class="mid">invariant</td></tr>
<tr class="hi"><th>Heartbeats per lifetime</th><td class="mid">a count</td><td class="mid"><strong>invariant (\(1.5\times10^9\))</strong></td></tr>
<tr><th>Number of generations</th><td class="mid">a count</td><td class="mid">invariant</td></tr>
<tr class="hi"><th>Genetic information</th><td class="mid">bits</td><td class="mid"><strong>invariant (\(6.2\times10^9\) bit = 775 MB)</strong></td></tr>
<tr><th>Body length ÷ cell size</th><td class="mid">length ÷ length</td><td class="mid">invariant</td></tr>
<tr><th>Ratios of metabolic rates</th><td class="mid">──</td><td class="mid">invariant</td></tr>
<tr><th>Temperature difference ÷ temperature</th><td class="mid">──</td><td class="mid">invariant</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>Everything life can measure is dimensionless, without exception.</strong><br>
So life cannot, <em>in principle</em>, know whether the universe is "expanding" or "growing in mass".</p>
</div>

<p>Episode 9 said "an atom has no comparison partner". This <strong>pushes that up to the scale of biology</strong>. Cells, hearts and genes cannot notice the difference between the pictures, so long as their comparisons bottom out in atoms.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">05</span>An aside — two kinds of "step count"</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Steps of what</th><th class="mid">Count</th><th class="mid">From</th></tr></thead>
<tbody>
<tr><th>The universe's logarithmic clock</th><td class="mid">140.2</td><td class="mid">Episode 2</td></tr>
<tr><th>The universe's Planck ticks</th><td class="mid">\(8.08\times10^{60}\)</td><td class="mid">Episode 1</td></tr>
<tr class="hi"><th>A human's lifetime heartbeats</th><td class="mid">\(1.5\times10^{9}\)</td><td class="mid">today</td></tr>
<tr><th>Information in the human genome</th><td class="mid">\(6.2\times10^{9}\) bit</td><td class="mid">today</td></tr>
<tr><th>The universe's memory</th><td class="mid">\(2.96\times10^{122}\) bit</td><td class="mid">Episode 1</td></tr>
</tbody>
</table>
</div>

<p>The third row is the fun one — <strong>the universe has made only 140 moves, while a human heart beats 1.5 billion times in a lifetime</strong>. The units of counting differ, of course (doublings versus beats). Still, <em>both are dimensionless and neither moves when the picture is swapped</em>.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① Kleiber's exponent 3/4 is disputed.</strong> Some analyses support 2/3 (a surface-area law), and the effective exponent varies with taxon and mass range. What is used here is only that <em>whatever the exponent is, it is dimensionless and therefore invariant</em>; the value 3/4 itself is not being asserted.</p>
<p style="margin:0 0 10px"><strong>② "\(1.5\times10^9\) heartbeats per lifetime" is a rough mammalian marker.</strong> Species vary by factors of a few, and humans (partly thanks to medicine) sit above it. What matters here is <em>the structure of being mass-independent, hence dimensionless</em>, not the precision of the number.</p>
<p style="margin:0 0 10px"><strong>③ It is assumed that chemical and biological quantities transform along with everything else.</strong> Same caveat as Episode 8 ① and Episode 13 ①: fixed laboratory conditions (a thermostat at a set temperature) change the story — what is treated here is <em>rewriting the whole universe at once</em>.</p>
<p style="margin:0 0 10px"><strong>④ "Life cannot know in principle" is a consequence of this series' decision procedure.</strong> More precisely: <em>so long as only dimensionless quantities are measured, the two cannot be distinguished</em> — a limitation not peculiar to life but bearing equally on every observer (final episode of the previous series).</p>
<p style="margin:0"><strong>⑤ The human genome's \(3.1\times10^9\) base pairs × 2 bit is an upper bound for a naive encoding.</strong> The actual information content (compressed, or functionally meaningful) is smaller, and estimating it is contested.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Why is the Arrhenius factor invariant here?
<details><summary>Show the answer</summary><div class="ans">Because the exponent \(E_a/k_BT\) is energy ÷ energy = dimensionless. <em>Exactly the reason tunnelling was invariant in Episode 8</em>, and reaction rates are untouched.</div></details></li>

<li>Find the weight of metabolic rate \(B\) (dimensions \(ML^2/T^3\)).
<details><summary>Show the answer</summary><div class="ans">\(M\) is \(-1\), \(L^2\) is \(+2\), \(T^{-3}\) is \(-3\), giving \(-1+2-3=-2\), so \(\tilde B=a^2B\). <em>Older creatures have slower metabolism in this picture</em> — but so does everything they are compared with.</div></details></li>

<li>How does the coefficient \(C\) move in Kleiber's law \(B=CM^{3/4}\)?
<details><summary>Show the answer</summary><div class="ans">\(w(C)=w(B)-\tfrac34w(M)=-2-\tfrac34(-1)=-\tfrac54\), i.e. \(\times a^{5/4}\). <strong>The exponent 3/4 is invariant; the coefficient moves</strong> — being dimensionful, it is bookkeeping. The gauge-invariant statement is "the ratio of two animals' metabolic rates = (mass ratio)\(^{3/4}\)".</div></details></li>

<li>Show that heartbeats per lifetime are mass-independent, and say what happens here.
<details><summary>Show the answer</summary><div class="ans">Heart rate \(\propto M^{-1/4}\) and lifespan \(\propto M^{+1/4}\), so the product is \(M^0\). <strong>Mass-independent, hence dimensionless</strong>, so the same \(1.5\times10^9\) in this picture. <em>Lifespan shrinks as \(\div a\) and the heart speeds up by the same factor, leaving the count unchanged.</em></div></details></li>

<li>(Harder) Is "life cannot know which picture it is in" a limitation peculiar to life?
<details><summary>Show the answer</summary><div class="ans">No — <strong>it bears equally on every observer</strong>. "Only dimensionless quantities are measurable" is the decision procedure of the previous series' final episode. Biology was brought in to see that <em>even the things furthest from cosmology — cells, hearts, genes — give the same conclusion</em>. It is Episode 9 (the atom) pushed up to biological scale.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — life has no way of knowing which picture it is in</h2>
<p>Chemistry came through entirely intact — Arrhenius factor, equilibrium constant, pH, bond energy ÷ \(k_BT\). <em>The exponents are dimensionless</em>, so reaction rates do not change at all (the same reason as tunnelling in Episode 8).</p>
<p>In biology we took Kleiber's law apart. Metabolic rate has weight \(-2\) (\(\times a^2\)) and body mass \(-1\) (\(\times a\)), so in \(B=CM^{3/4}\) <strong>the coefficient moves as \(\times a^{5/4}\) while the exponent 3/4 is invariant</strong>. The gauge-invariant statement is "the ratio of two animals' metabolic rates = (mass ratio)\(^{3/4}\)" — exactly the surgery of Episodes 3, 9 and 12.</p>
<p>Then heartbeats per lifetime. Heart rate \(\propto M^{-1/4}\) and lifespan \(\propto M^{1/4}\), so the product is \(M^0\): <strong>about 1.5 billion, independent of mass</strong>. Dimensionless, hence the same value here. <em>Measure a life in seconds and it shrinks; measure it in heartbeats and it does not</em> — the same structure as Episode 9's Bohr radius.</p>
<p>List everything life can measure — concentration ratios, rate ratios, heartbeats, generations, bits of genetic information, body length ÷ cell size, metabolic ratios, temperature difference ÷ temperature. <strong>Dimensionless without exception.</strong> So <em>life cannot, in principle, know whether the universe is "expanding" or "growing in mass"</em>. Episode 9's "an atom has no comparison partner", pushed up to biological scale. And as an aside — the universe has made only 140 moves, while a human heart beats 1.5 billion times in a lifetime.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 16 (Part II finale)</span>
Part II's ten episodes fold into one table. Gravity, quantum mechanics, atoms, heat, light, the vacuum, fluids, phase transitions, chemistry and biology — wherever we substituted, <strong>only one thing ever moved</strong>. And listing everything that did not move gives, directly, <em>an inventory of what physics is</em>. Finally we draw a clear line between where this notation <strong>genuinely helps</strong> and where it is <strong>completely powerless</strong> — half the answer was already in Episode 13. <em>Only where dimensionful quantities are the protagonists.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sa=document.getElementById('sa'), va=document.getElementById('va'), ro=document.getElementById('ro');
  var X0=88, X1=690;
  var TOP=[['body mass M',-1],['body length L',1],['metabolic rate B',-2],['lifespan τ',1]];
  var BOT=['heartbeats / lifetime','genetic info (bits)','metabolic ratios','pH, concentration ratios'];

  function draw(){
    var la=parseInt(sa.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);

    var Y1=118, Y2=300;
    var scale=Math.min(52, 96/Math.max(2*Math.abs(la),1));

    ['top: dimensionful quantities (they move here)','bottom: what life actually measures (they do not)'].forEach(function(t,i){
      g.font='bold 12px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.fillStyle=(i===0?'#6b4a7a':'#a06020'); g.textAlign='left';
      g.fillText(t, X0-8, (i===0?Y1-92:Y2-64));
    });
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    [[Y1,'#e2d6e8'],[Y2,'#efe0cf']].forEach(function(q){
      g.strokeStyle=q[1]; g.lineWidth=1.6;
      g.beginPath(); g.moveTo(X0-8,q[0]); g.lineTo(X1,q[0]); g.stroke();
      g.fillStyle='#a08fa8'; g.textAlign='right';
      g.fillText('×1', X0-14, q[0]+4);
    });

    var n=4, w=88, gap=(X1-X0-n*w)/(n+1);
    for(var i=0;i<n;i++){
      var ex=-TOP[i][1]*la;
      var x=X0+gap+(w+gap)*i, h=ex*scale;
      g.fillStyle='#6b4a7a'; g.globalAlpha=0.85;
      g.fillRect(x, h>=0? Y1-h : Y1, w, Math.abs(h));
      g.globalAlpha=1;
      g.fillStyle='#4a3255'; g.textAlign='center';
      g.fillText(TOP[i][0], x+w/2, Y1+20);
      g.fillStyle='#7d6a88';
      g.fillText('×10'+(ex>=0?'+':'')+ex.toFixed(1), x+w/2, Y1+36);
    }
    for(var i=0;i<n;i++){
      var x=X0+gap+(w+gap)*i;
      g.fillStyle='#a06020'; g.globalAlpha=0.9;
      g.fillRect(x, Y2-3, w, 6);
      g.globalAlpha=1;
      g.fillStyle='#6d4416'; g.textAlign='center';
      g.fillText(BOT[i], x+w/2, Y2+22);
      g.fillStyle='#9a7a52';
      g.fillText('×1.000', x+w/2, Y2+38);
    }

    var a=Math.pow(10,la);
    va.textContent='a = '+(a<0.01? a.toExponential(2) : a.toFixed(3));
    ro.textContent='a = '+va.textContent+' (z = '+(1/a-1).toPrecision(3)+')　'+
      'mass ×10'+(la>=0?'+':'')+(la).toFixed(1)+'　'+
      'length ×10'+(-la>=0?'+':'')+(-la).toFixed(1)+'　'+
      'metabolic rate ×10'+(2*la>=0?'+':'')+(2*la).toFixed(1)+'　'+
      'lifespan ×10'+(-la>=0?'+':'')+(-la).toFixed(1)+
      '　→　everything life measures stays at ×1.000';
  }
  sa.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-15-life.html', acc='#6b4a7a', ops='#a06020',
      title='Substituting into chemistry and biology ── c·t = const, That Clicks, Episode 15',
      ep='EPISODE 15 ／ Part II, at the farthest remove',
      eyebrow='Everything life can measure turned out to be dimensionless',
      h1='Substituting into<br>chemistry and biology',
      sub='The Arrhenius factor, Kleiber\'s exponent, heartbeats per lifetime, the information in DNA — all invariant.<br><em>So life has no way of knowing which picture it is in.</em>',
      byline_l='What you need: adding weights, reading exponents',
      byline_r='\\(1.5\\times10^9\\) heartbeats — independent of mass',
      body=BODY + '\n\n<p class="foot">This document is Episode 15 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That dimensionless quantities are conformally invariant, and that weights follow from decomposing dimensions, are standard (Episode 13). The metabolic-rate weight \\(-2\\) and the Kleiber coefficient weight \\(-5/4\\) are computed here (kenshou/calc20.py). <strong>Kleiber\'s exponent 3/4 is disputed</strong> — some analyses support 2/3 (a surface-area law), and the effective exponent varies with taxon and mass range — so what is used here is only that whatever the exponent is, it is dimensionless and therefore invariant. "\\(1.5\\times10^9\\) heartbeats per lifetime" is a rough mammalian marker with species-level variation of a few, and humans sit above it; what matters is <em>the mass-independent, hence dimensionless, structure</em>, not the precision. The human genome\'s \\(3.1\\times10^9\\) base pairs × 2 bit \\(=6.2\\times10^9\\) bit is an upper bound for a naive encoding; the actual (compressed or functional) content is smaller and contested. Chemical and biological quantities are assumed to transform along with everything else, so this does not apply to fixed laboratory conditions (same caveat as Episode 8 ① and Episode 13 ①). "Life cannot know in principle" means, more precisely, "so long as only dimensionless quantities are measured, the two cannot be distinguished" — a limitation on every observer, not peculiar to life (final episode of the previous series). Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination and conflicts with nucleosynthesis when extrapolated into the early universe (Lewis, Barnes &amp; Kaushik 2016). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the epoch and only the top row moves. "Show the answer" opens each solution.')
