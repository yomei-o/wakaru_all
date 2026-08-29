# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 3 settled it: \(c\cdot t=\text{const}\) <strong>says nothing on its own</strong>, because it can be realised in any universe whatsoever. So why use it? The answer is simple — <em>because the equations get shorter</em>. This episode substitutes the conformal transformation into every cosmological formula in reach and <strong>counts what disappears</strong>. When the deleting is done, astonishingly little is left.</p>

<h2><span class="n">01</span>Deleting, one at a time</h2>

<p>Only one operation is used: \(\Omega=1/a\) from Episode 3 of the previous series. Following the weight table (length \(+1\); mass, energy, temperature \(-1\); \(c,\hbar,e,\alpha\) all \(0\)), transform the quantities of cosmology in turn.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Standard picture</th><th class="mid">After transforming</th><th class="mid">Result</th></tr></thead>
<tbody>
<tr><th>Expansion of space</th><td class="mid">stretches as \(a(t)\)</td><td class="mid">\(\tilde a=1\)</td><td class="mid">gone</td></tr>
<tr><th>Spacetime curvature</th><td class="mid">\(R=6/c^2t^2\) (diverges)</td><td class="mid">\(\tilde R=0\)</td><td class="mid">gone</td></tr>
<tr><th>Temperature</th><td class="mid">falls as \(T\propto1/a\)</td><td class="mid">\(\tilde T=aT=\text{const}\)</td><td class="mid">gone</td></tr>
<tr><th>Light (electromagnetism)</th><td class="mid">wavelength stretches</td><td class="mid">weight 0</td><td class="mid">nothing happens at all</td></tr>
<tr><th>\(\alpha,\ \hbar,\ c,\ e\)</th><td class="mid">constant</td><td class="mid">weight 0</td><td class="mid">does not move</td></tr>
<tr class="hi"><th>Mass</th><td class="mid">constant</td><td class="mid">\(\tilde m=a\,m\)</td><td class="mid"><strong>this alone survives</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0">Delete everything the conformal transformation can delete and <strong>exactly one time-varying thing is left</strong>.<br>
The container (Minkowski spacetime), the ticks on the ruler (\(\alpha\)), light, temperature — all frozen. The only thing moving is <em>mass</em>.</p>
</div>

<h2><span class="n">02</span>Which is why cosmology fits on one line</h2>

<div class="keybox">
<p class="lbl">The whole history of the universe</p>
<p style="margin:6px 0 0">A <strong>growing mass</strong> overtakes a <strong>fixed ruler</strong>, \(k_BT_0\), one threshold at a time.</p>
</div>

<p>The standard picture says "the temperature drops below some energy threshold". Here it is the other way round: <em>the temperature sits at 2.7255 K and never moves, while the thresholds grow up past it.</em> The previous series mentioned this phrasing once; carry it all the way and you get the following.</p>

<div class="calc">
<span class="tag">The fixed ruler</span>
$$k_BT_0=2.3487\times10^{-4}\ \mathrm{eV}\qquad(\text{in this picture, constant forever})$$
<p class="lbl">An "event" happens when the growing threshold (today's value \(\times\,t/t_0\)) exceeds this by the required factor</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Event</th><th class="mid">Threshold (today)</th><th class="mid">Factor</th><th class="mid">\(t/t_0\)</th><th class="mid">\(1+z\)</th></tr></thead>
<tbody>
<tr><th>Neutron–proton freeze-out</th><td class="mid">\(Q=1.293\) MeV</td><td class="mid">1.616</td><td class="mid">\(2.94\times10^{-10}\)</td><td class="mid">\(3.41\times10^{9}\)</td></tr>
<tr><th>Electron–positron annihilation</th><td class="mid">\(m_ec^2=0.511\) MeV</td><td class="mid">1.000</td><td class="mid">\(4.60\times10^{-10}\)</td><td class="mid">\(2.18\times10^{9}\)</td></tr>
<tr><th>Deuterium forms</th><td class="mid">2.22 MeV</td><td class="mid">22.2</td><td class="mid">\(2.35\times10^{-9}\)</td><td class="mid">\(4.26\times10^{8}\)</td></tr>
<tr class="hi"><th>Hydrogen recombination</th><td class="mid">Ry \(=13.6\) eV</td><td class="mid">52.6</td><td class="mid">\(9.08\times10^{-4}\)</td><td class="mid"><strong>1100.9</strong></td></tr>
</tbody>
</table>
</div>

<p>Look at the last row: <strong>1100.9</strong> — the standard "recombination at \(z=1100\)". Convert the freeze-out row back to a temperature and you get \(1.293/1.616=0.800\) MeV, again exact. <em>This picture is producing the same numbers as the standard one, in a different order.</em></p>

<h2><span class="n">03</span>Put in \(a\propto t\) and it becomes a single straight line</h2>

<p>Nothing so far fixed \(a(t)\); the "only mass moves" picture can be built for any universe (the same situation as Episode 3). But in general the \(a(t)\) inside \(\tilde m=a(t)\,m\) can only be written as an integral. Put in \(a\propto t\) and —</p>

<div class="calc">
<span class="tag">The simplest case</span>
$$\tilde m(t)=m\cdot\frac{t}{t_0}$$
<p class="lbl">on a log–log plot</p>
$$\log\tilde m=\log m+\log\frac{t}{t_0}\qquad\text{── a straight line of slope 1}$$
</div>

<div class="keybox">
<p class="lbl">The one line of this episode</p>
<p style="margin:6px 0 0">The history of the universe is <strong>one straight line crossing four horizontal lines in turn</strong>.<br>
Nothing else moves at all.</p>
</div>

<p>That is what \(c\cdot t=\text{const}\) gives you — <strong>not new physics, but the shortest way of writing it</strong>. What Episode 3 concluded was "zero claim" is here working at full stretch: <em>because it claims nothing, it can be substituted anywhere</em>.</p>

<div class="fig">
<p class="cap">Figure: horizontal axis, the age of the universe (\(t/t_0\), log); vertical axis, energy (log). The slider switches the <strong>way of speaking</strong> — far left is the standard picture (thresholds fixed, temperature falling), far right is the mass picture (temperature fixed, thresholds growing). <strong>Only the crossings never move.</strong></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Way of speaking \(s\) (left = temperature falls / right = mass grows)<input id="ss" type="range" min="0" max="1000" value="1000" step="5"></label>
  <span class="val" id="vs">s = 1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2b6b5f"></i>thermal energy \(k_BT\)</span>
  <span><i class="swatch" style="background:#6b3a2a"></i>four thresholds (masses, binding energies)</span>
  <span><i class="swatch" style="background:#9a8c80"></i>crossing = event (immovable)</span>
</div>
</div>

<p>Swing the slider and the teal line and the rust lines <strong>see-saw violently</strong>. At the left the rust lines are flat and the teal one dives; at the right the teal one is flat and the rust ones climb. And yet <strong>the four crossings stay nailed to their dashed verticals</strong>. We saw this picture again and again in the previous series; here it has become a statement about <em>the compression ratio of cosmology</em> — <strong>the far right is where the fewest things move</strong>.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The equations really do get shorter</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">\(\Lambda\)CDM</th><th class="mid">\(c\cdot t=\text{const}\)</th></tr></thead>
<tbody>
<tr><th>Hubble rate</th><td class="mid">\(H_0E(z)\), \(E=\sqrt{\Omega_r(1+z)^4+\Omega_m(1+z)^3+\Omega_\Lambda}\)</td><td class="mid">\(H_0(1+z)\)</td></tr>
<tr><th>Comoving distance</th><td class="mid">\((c/H_0)\int dz'/E\) — numerical</td><td class="mid">\((c/H_0)\ln(1+z)\)</td></tr>
<tr class="hi"><th>Luminosity distance</th><td class="mid">\((c/H_0)(1+z)\int dz'/E\)</td><td class="mid"><strong>\((c/H_0)(1+z)\ln(1+z)\)</strong></td></tr>
<tr><th>Angular diameter distance</th><td class="mid">\((c/H_0)\int dz'/E\,/(1+z)\)</td><td class="mid">\((c/H_0)\ln(1+z)/(1+z)\)</td></tr>
<tr><th>Age at that time</th><td class="mid">\(\int dz'/[(1+z')E]\)</td><td class="mid">\(t_0/(1+z)\)</td></tr>
<tr><th>Lookback time</th><td class="mid">\(\int dz'/[(1+z')E]\)</td><td class="mid">\(t_0\,z/(1+z)\)</td></tr>
<tr><th>Horizon radius</th><td class="mid">\((c/H_0)/E(z)\)</td><td class="mid">\(c\,t_0/(1+z)\)</td></tr>
</tbody>
</table>
</div>

<p>Every entry on the right is <strong>closed form</strong>, containing nothing but a logarithm and a division. Every entry on the left is a numerical integral. The quantities you meet on page one of a cosmology textbook shrink this far.</p>

<div class="aside">
<span class="tag">This is used in practice</span>
"Push the expansion into the time coordinate and light travels in straight lines, which makes the computation easy" — mentioned in passing in Episode 2 of the previous series. It is exactly why numerical cosmology codes work in conformal time. <strong>\(c\cdot t=\text{const}\) is the limiting case</strong>: conformal time becomes the plain logarithm \(\eta=t_0\ln(t/t_0)\) and the scale factor becomes an exponential. <em>It is the only expansion law with no special functions and no integrals anywhere.</em>
</div>

<h2><span class="n">05</span>Measuring the shortness in the language of information</h2>

<p>Rather than leave "the equations are shorter" as a matter of taste, count it. A model's description length can be measured by its number of dimensionless parameters — dimensionful quantities merely fix units, so they are not counted (the watchword of the previous series).</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Model</th><th class="mid">Dimensionless parameters</th><th class="mid">Count</th></tr></thead>
<tbody>
<tr><th>\(\Lambda\)CDM</th><td class="mid">\(\Omega_bh^2,\ \Omega_ch^2,\ \theta_*,\ \tau,\ A_s,\ n_s\)</td><td class="mid">6</td></tr>
<tr class="hi"><th>\(c\cdot t=\text{const}\)</th><td class="mid">none (\(H_0\) is dimensionful — it only fixes units)</td><td class="mid"><strong>0</strong></td></tr>
</tbody>
</table>
</div>

<p>So the right-hand column of §04 contains <strong>not one adjustable number</strong>. \(H_0d_L/c=(1+z)\ln(1+z)\) — <em>a prediction containing no constants at all</em>. Occam's razor at its limit.</p>

<div class="caveat">
<span class="tag">But shortness only counts once you have explained the data</span>
Minimal description length is worthless if the data are not accounted for. Parameter-free also means <strong>there is nowhere to move</strong>. And indeed, comparing \(H_0d_L/c\) with \(\Lambda\)CDM, the two differ by <strong>0.21 magnitudes</strong> at \(z\simeq1.1\) (\(\Lambda\)CDM being the more distant). Modern Type Ia supernova statistical errors are 0.01–0.02 mag, so this is an order-of-magnitude visible difference. <em>Shortness and goodness of fit are separate resources</em>, and trading them off is the job of the information criteria (AIC / BIC) — that is next episode.
</div>

<h2><span class="n">06</span>The reveal — why is it mass that survives?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Weight</th><th class="mid">What has it</th><th class="mid">Under the conformal transformation</th></tr></thead>
<tbody>
<tr><th>\(0\)</th><td class="mid">\(c,\ \hbar,\ e,\ \alpha\); the 4D Maxwell action; light cones</td><td class="mid">does not move</td></tr>
<tr><th>\(+1\)</th><td class="mid">length, time, wavelength</td><td class="mid">\(\div a\)</td></tr>
<tr class="hi"><th>\(-1\)</th><td class="mid">mass, energy, temperature, frequency</td><td class="mid">\(\times a\)</td></tr>
</tbody>
</table>
</div>

<p>The weight-0 row does not respond to the transformation at all. The weight \(+1\) row (length) <strong>moves together with the ruler</strong>, so it cancels in any ratio — which is why the expansion of space could be deleted. What is left is the weight \(-1\) row, and its representative is mass.</p>

<p>This is precisely the conclusion of Episode 7 of the previous series — <strong>"light is conformally invariant, mass is not"</strong>. There it led towards Penrose's CCC; here it is practical. <em>If mass is the only thing a conformal transformation catches, then mass is the only thing left after you tidy up with one.</em> Obvious, perhaps — but pursue the obvious to the end and cosmology becomes a single straight line.</p>

<div class="aside">
<span class="tag">Connecting to Episodes 1 and 2</span>
In Episode 1, dividing memory by operations produced the equation of state \(w\). In Episode 2, dividing two clocks produced the expansion index \(p\). Today, deleting everything deletable left mass. All three are the same move: <strong>move everything that can be moved, and look at what does not move</strong>. Take the decision procedure of the previous series and use it not for judgement but for <em>compression</em>, and this is what you get.
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① "Disappears" in §01 means "stops varying in time in that picture."</strong> The physics has not gone anywhere. The expansion and the cooling have both been pushed into the growth of mass. The counting of Episode 4 of the previous series (field \(+1\), symmetry \(-1\), net zero) applies, so <em>no information has been lost at all</em>. Only the length of the writing has shrunk.</p>
<p style="margin:0 0 10px"><strong>② The "factors" in §02 (1.616, 22.2, 52.6 …) are dimensionless ratios taken from standard cosmology.</strong> They are not predictions of this picture. What is being done here is <em>translation</em>, not derivation. The 52.6 for recombination is the value checked in both pictures in Episode 3 of the previous series.</p>
<p style="margin:0 0 10px"><strong>③ "Atoms shrink / mass grows" is phrasing relative to the comoving grid.</strong> Atoms are not growing in your room. Locally measured mass, light speed and \(\alpha\) are identical in every picture.</p>
<p style="margin:0 0 10px"><strong>④ The right-hand column of §04 is exact under \(a\propto t\), spatial flatness, and \(1+z=t_0/t\).</strong> The difference from the left column is a difference of <em>model</em>, not of notation — <em>short does not mean right, and long does not mean wrong</em>. The 0.21 mag of §05 is how large that difference is in the data.</p>
<p style="margin:0"><strong>⑤ "Zero dimensionless parameters" follows Melia's standard presentation of \(R_h=ct\).</strong> That counting is disputed: whether \(R_h=ct\) is a special case of \(\Lambda\)CDM or an independent model changes the tally.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>In this picture, what ratio is the redshift \(z\)?
<details><summary>Show the answer</summary><div class="ans">A ratio of masses: \(1+z=\tilde m_0/\tilde m_e=a_0/a_e\). Light is conformally invariant, so <strong>nothing happens to it in flight</strong> — what changed is the receiver (the laboratory hydrogen atom got heavier). Same number as the standard "the wavelength stretched", in different words.</div></details></li>

<li>Explain recombination at \(1+z=1101\) in the language of this picture.
<details><summary>Show the answer</summary><div class="ans">The Rydberg is 13.6 eV today and grows \(\propto t\) here. The thermal energy is fixed at \(k_BT_0=2.3487\times10^{-4}\) eV. The condition is a ratio of 52.6, so \(13.6\,(t/t_0)/2.3487\times10^{-4}=52.6\) gives \(t/t_0=9.08\times10^{-4}\), i.e. \(1+z=1101\). <strong>The temperature never dropped.</strong></div></details></li>

<li>With \(c\cdot t=\text{const}\), find the luminosity distance to a galaxy at \(z=1\) (\(c/H_0=1.30\times10^{26}\) m).
<details><summary>Show the answer</summary><div class="ans">\(d_L=(c/H_0)(1+z)\ln(1+z)=1.30\times10^{26}\times2\times\ln2=1.80\times10^{26}\) m. <strong>No integral needed.</strong> For \(\Lambda\)CDM, \(H_0d_L/c=1.529\), and the gap from \(1.386\) is the 0.21 mag.</div></details></li>

<li>Why do weight \(+1\) quantities (lengths) "disappear"?
<details><summary>Show the answer</summary><div class="ans">Because what is observable is not a length but a <strong>ratio of lengths</strong>. The ruler and the thing measured both pick up the same \(1/a\), so it cancels in the ratio. What survives is whatever carries a <em>different</em> weight from the ruler — the weight \(-1\) masses. <strong>"Intergalactic distance ÷ atomic radius" moves because numerator and denominator have different weights</strong> (the figure in Episode 4 of the previous series).</div></details></li>

<li>(Harder) This picture can be built for any \(a(t)\). So what is special about \(a\propto t\)?
<details><summary>Show the answer</summary><div class="ans">That the one surviving function \(\tilde m(t)=a(t)m\) takes <strong>the simplest possible form — proportionality</strong>. For \(\Lambda\)CDM, \(a(t)\) can only be written as an integral, so all this picture can say is "mass grows as \(a(t)\)". With \(a\propto t\) it becomes one straight line and all the closed forms of §04 fall out. <strong>The compression ratio is maximal at \(a\propto t\)</strong> — but that is a property of the <em>writing</em>, separate from correctness (Episode 3).</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — delete everything deletable and mass is left</h2>
<p>Episode 3 established that \(c\cdot t=\text{const}\) "says nothing on its own". This episode does what that makes possible: <em>substitute it into every cosmological formula and delete everything deletable</em>. The expansion of space (\(\tilde a=1\)), curvature (\(\tilde R=0\)), temperature (\(\tilde T=\text{const}\)), light (weight 0 from the start). One after another they go, and exactly one thing is left — \(\tilde m=a\,m\).</p>
<p>So the history of the universe fits on one line: <strong>a growing threshold overtakes the fixed ruler \(k_BT_0=2.3487\times10^{-4}\) eV, one event at a time</strong>. Neutron freeze-out, annihilation, deuterium, recombination — all of this form, and recombination comes back at \(1+z=1100.9\), freeze-out at \(0.800\) MeV, exactly the standard numbers. <em>A translation, not a different physics.</em></p>
<p>Put in \(a\propto t\) and the one surviving function becomes <strong>a straight line of slope 1</strong>. The history of the universe collapses into one line crossing four horizontal lines. The formulas collapse too — \(H(z)=H_0(1+z)\), \(d_C=(c/H_0)\ln(1+z)\), \(t(z)=t_0/(1+z)\), all closed form, one logarithm where \(\Lambda\)CDM demands a numerical integral. <em>The only expansion law with no special functions and no integrals.</em></p>
<p>In the language of information: \(\Lambda\)CDM has 6 dimensionless parameters, \(c\cdot t=\text{const}\) has <strong>0</strong>. Occam's razor at its limit — but shortness only counts once the data are explained, and at \(z\simeq1.1\) the gap is 0.21 mag. The reveal is Episode 7 of the previous series verbatim: <strong>if mass is the only thing a conformal transformation catches, mass is the only thing left after you tidy up with one</strong>. Pursue the obvious to the end and cosmology becomes a single straight line.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 5</span>
Zero description length and a 0.21 mag misfit have now collided head-on. <strong>How are shortness and fit traded against each other?</strong> That is precisely an information-theory question — Akaike's criterion charges "one parameter = one unit of log-likelihood", the Bayesian criterion makes the fine heavier with the number of data points. \(c\cdot t=\text{const}\) pays no fine at all, so we can compute <em>how badly it is allowed to lose on fit</em>. Next episode is the one time this series measures model selection in bits. The answer up front — <strong>the grace that six parameters can buy is smaller than you would think.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=70, X1=700, Y0=30, Y1=330;
  var xmin=-10.4, xmax=0.4;
  var ymin=-5.2, ymax=7.4;
  var LKT0=Math.log(2.3487e-4)/Math.LN10;

  var EV=[
    {n:'neutron freeze-out', E:0.8e6},
    {n:'pair annihilation',  E:0.511e6},
    {n:'deuterium',          E:0.1e6},
    {n:'recombination',      E:0.2586}
  ];

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function draw(){
    var s=parseInt(ss.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=-4;e<=6;e+=2){
      var y=py(e);
      g.strokeStyle='#f1ebe5'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a2968b';
      g.fillText((e<0?'10⁻':'10')+Math.abs(e), X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-10;q<=0;q+=2){
      var x=px(q);
      g.strokeStyle='#f6f1ec'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a2968b'; g.fillText(q===0?'now':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#dbcfc5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    EV.forEach(function(v){
      var xc=LKT0-Math.log(v.E)/Math.LN10;
      g.strokeStyle='#cdbfb2'; g.lineWidth=1; g.setLineDash([3,4]);
      g.beginPath(); g.moveTo(px(xc),Y0); g.lineTo(px(xc),Y1); g.stroke();
      g.setLineDash([]);
    });

    EV.forEach(function(v,i){
      var lE=Math.log(v.E)/Math.LN10;
      g.strokeStyle='#6b3a2a'; g.lineWidth=2.4;
      g.beginPath();
      g.moveTo(px(xmin), py(lE+s*xmin));
      g.lineTo(px(xmax), py(lE+s*xmax));
      g.stroke();
      g.fillStyle='#6b3a2a'; g.textAlign='left';
      var ylab=lE+s*xmax;
      if(ylab>ymin+0.3&&ylab<ymax-0.2) g.fillText(v.n, px(xmax)-4-g.measureText(v.n).width, py(ylab)-6);
    });

    g.strokeStyle='#2b6b5f'; g.lineWidth=3.4;
    g.beginPath();
    g.moveTo(px(xmin), py(LKT0+(s-1)*xmin));
    g.lineTo(px(xmax), py(LKT0+(s-1)*xmax));
    g.stroke();
    g.fillStyle='#2b6b5f'; g.textAlign='left';
    var ykt=LKT0+(s-1)*xmin;
    g.fillText('thermal energy k_BT', px(xmin)+8, py(Math.min(ykt,ymax-0.35))-8);

    EV.forEach(function(v){
      var xc=LKT0-Math.log(v.E)/Math.LN10;
      var yc=Math.log(v.E)/Math.LN10+s*xc;
      g.fillStyle='#9a8c80';
      g.beginPath(); g.arc(px(xc),py(yc),5,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=1.6;
      g.beginPath(); g.arc(px(xc),py(yc),5,0,6.2832); g.stroke();
    });

    g.fillStyle='#7a6a5e'; g.textAlign='center';
    g.fillText('age of the universe  t / t₀', (X0+X1)/2, Y1+36);

    vs.textContent='s = '+s.toFixed(2);
    var name = s>0.995 ? '(mass-grows picture: temperature fixed at 2.7255 K)'
             : (s<0.005 ? '(standard picture: thresholds fixed, temperature falling)' : '(an intermediate way of speaking — same physics)');
    ro.textContent='s = '+s.toFixed(2)+' '+name+
      '　threshold ∝ t^'+s.toFixed(2)+'　/　k_BT ∝ t^'+(s-1).toFixed(2)+
      '　→　the ratio goes as t^1 independently of s — the crossings do not move';
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-04-onemass.html', acc='#5a3a2a', ops='#2b6b5f',
      title='Everything becomes one mass ── c·t = const, That Clicks, Episode 4',
      ep='EPISODE 4 ／ The judging is over. This is the real subject',
      eyebrow='Why use a rewriting that says nothing? Because the equations get shorter',
      h1='Everything becomes<br>one mass',
      sub='Apply the conformal transformation and space, curvature, temperature and light vanish in turn.<br><em>One thing is left — and cosmology collapses into a single monotonic function.</em>',
      byline_l='What you need: the weight table, division',
      byline_r='\\(\\tilde m=a\\,m\\) — this alone survives',
      body=BODY + '\n\n<p class="foot">This document is Episode 4 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That under a conformal transformation \\(\\tilde g=\\Omega^2g\\) (\\(\\Omega=1/a\\)) length has weight \\(+1\\), mass, energy and temperature have weight \\(-1\\), and \\(c,\\hbar,e,\\alpha\\) together with the 4D Maxwell action have weight \\(0\\) — hence \\(\\tilde m=am\\), \\(\\tilde T=aT\\), \\(\\tilde R=0\\) (for \\(a\\propto t\\)) — is standard. Cosmology written as growing mass is due to Wetterich (2013, Phys. Dark Univ. 2, 184). The "factors" in §02 (freeze-out \\(Q/k_BT_f=1.616\\), deuterium 22.2, recombination 52.6) are <strong>values taken from standard cosmology and translated</strong>, not predictions of this model. The \\(1+z=1100.9\\) for recombination and the \\(0.800\\) MeV for freeze-out are computed here (\\(k_BT_0=2.3487\\times10^{-4}\\) eV, \\(T_0=2.7255\\) K). The closed forms of §04 are exact under \\(a\\propto t\\), spatial flatness and \\(1+z=t_0/t\\), and include \\(H_0d_L/c=(1+z)\\ln(1+z)\\). The \\(\\Lambda\\)CDM values come from a numerical integration here with \\(\\Omega_m=0.315\\), \\(\\Omega_r=9.2\\times10^{-5}\\); the two differ by at most 0.214 mag at \\(z=1.12\\) (\\(\\Lambda\\)CDM the more distant), against modern Type Ia statistical errors of 0.01–0.02 mag. The six \\(\\Lambda\\)CDM parameters are Planck\'s standard basis; "zero dimensionless parameters" for \\(R_h=ct\\) follows Melia\'s presentation, and that counting is itself disputed. "Atoms shrink / mass grows" is phrasing relative to the comoving grid — locally measured mass, light speed and \\(\\alpha\\) are unchanged in every picture. This document concerns the <em>concision</em> of a rewriting and does not argue that \\(a\\propto t\\) is correct; for the conflict with nucleosynthesis when extrapolated into the early universe see Lewis, Barnes &amp; Kaushik (2016, MNRAS 460, 291). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider switches the way of speaking and the crossings stay put. "Show the answer" opens each solution.')
