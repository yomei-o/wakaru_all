# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">In this picture atoms shrink as \(1/t\). The Bohr radius is \(\hbar/(mc\alpha)\), so it gets smaller as the mass grows. <strong>Doesn't that blur the spectral lines?</strong> This is not idle worry: it is <em>exactly the argument</em> with which Einstein killed Weyl's theory in 1918. This episode says, in two numbers, why that blade cannot reach the modern conformal transformation.</p>

<h2><span class="n">01</span>The blade Einstein used in 1918</h2>

<p>A recap of Episode 1 of the previous series. Weyl proposed \(g_{\mu\nu}\to\Omega(x)^2g_{\mu\nu}\), letting the standard of length be re-chosen at every point, and identified the compensating field with the electromagnetic potential. Einstein objected in an appendix to the same paper.</p>

<div class="aside">
<span class="tag">Einstein's objection (1918)</span>
If the ruler differs from place to place and <strong>carrying the difference requires a path</strong>, then joining the same two points by different routes gives different answers. The same atom would emit light of a wavelength depending on <em>the history it had travelled</em> (the second clock effect). But real spectral lines are sharp. Hydrogen is the colour of hydrogen everywhere in the universe.
</div>

<p>The objection was decisive; Weyl withdrew the theory. <strong>One observational fact — that atoms do not remember their history — killed an entire unified theory.</strong></p>

<h2><span class="n">02</span>The modern conformal transformation is doubly protected</h2>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>There is no path dependence to begin with</strong><span>\(\Omega(x)\) is a <em>single-valued</em> function with one value at each point. The change of length depends only on the endpoint, so the second clock effect cannot occur in principle (Episode 1 of the previous series)</span></div></div>
<div class="row hi"><div class="mk">②</div><div class="txt"><strong>Even with time variation, adiabaticity protects it</strong><span>Mass really does grow as \(\propto t\). But the change is <em>orders of magnitude slower</em> than the level spacing, so not one transition is induced — this is what we compute today</span></div></div>
</div>

<p>Point ① is history, settled in the previous series. Today is ②: <strong>even if atoms really are shrinking, why the lines do not blur</strong>, in numbers.</p>

<h2><span class="n">03</span>Computing the adiabatic parameter</h2>

<p>The adiabatic theorem says: if the Hamiltonian changes slowly enough <em>compared with the level spacing</em>, the system follows its level without jumping out. The test is a ratio of two rates.</p>

<div class="calc">
<span class="tag">Dividing two rates</span>
<p class="lbl">Rate of change of the Hamiltonian (here, the growth rate of mass)</p>
$$\frac{\dot m}{m}=\frac{1}{t}=H$$
<p class="lbl">Rate at which a level can respond</p>
$$\frac{\Delta E}{\hbar}$$
<p class="lbl">The ratio — the adiabatic parameter</p>
$$\varepsilon=\frac{\hbar H}{\Delta E}\qquad(\varepsilon\ll1\ \text{means adiabatic})$$
</div>

<p>Put in today's \(\hbar H_0=1.51\times10^{-33}\) eV.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Transition</th><th class="mid">\(\Delta E\)</th><th class="mid">\(\varepsilon=\hbar H_0/\Delta E\)</th><th class="mid">Adiabaticity fails at \(t=\hbar/\Delta E\)</th></tr></thead>
<tbody>
<tr class="hi"><th>Hydrogen Rydberg</th><td class="mid">13.6 eV</td><td class="mid"><strong>\(1.1\times10^{-34}\)</strong></td><td class="mid">\(4.8\times10^{-17}\) s</td></tr>
<tr><th>Lyman α</th><td class="mid">10.2 eV</td><td class="mid">\(1.5\times10^{-34}\)</td><td class="mid">\(6.5\times10^{-17}\) s</td></tr>
<tr><th>Visible light</th><td class="mid">2 eV</td><td class="mid">\(7.6\times10^{-34}\)</td><td class="mid">\(3.3\times10^{-16}\) s</td></tr>
<tr><th>Caesium clock (9.19 GHz)</th><td class="mid">\(3.8\times10^{-5}\) eV</td><td class="mid">\(4.0\times10^{-29}\)</td><td class="mid">\(1.7\times10^{-11}\) s</td></tr>
<tr><th>21 cm hyperfine</th><td class="mid">\(5.9\times10^{-6}\) eV</td><td class="mid">\(2.6\times10^{-28}\)</td><td class="mid">\(1.1\times10^{-10}\) s</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §03</p>
<p style="margin:6px 0 0">Even the <em>slackest</em> transition (21 cm) loses adiabaticity before <strong>\(10^{-10}\) s</strong>.<br>
Atoms only form at recombination (\(1.2\times10^{13}\) s = 380,000 yr).<br>
<strong>Perfectly adiabatic throughout the entire era in which atoms exist.</strong></p>
</div>

<div class="fig">
<p class="cap">Figure: age of the universe across, adiabatic parameter \(\hbar H/\Delta E\) up. Adiabaticity fails where the curve rises above the vermilion line (\(\varepsilon=1\)). <strong>The grey band is "the era in which atoms exist"</strong> — however you move the transition energy, the crossing stays far to the left of it.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Transition energy \(\Delta E\) (log)<input id="se" type="range" min="0" max="1000" value="742" step="1"></label>
  <span class="val" id="ve">13.6 eV</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2c4a45"></i>adiabatic parameter \(\hbar H/\Delta E\)</span>
  <span><i class="swatch" style="background:#a35a1f"></i>\(\varepsilon=1\) (adiabaticity fails)</span>
  <span><i class="swatch" style="background:#9fb0ab"></i>era in which atoms exist</span>
</div>
</div>

<p>Push the slider to the far left (\(10^{-10}\) eV, slacker than any transition one can imagine) and the crossing still does not reach the band. <em>Between the formation of atoms and today, adiabaticity never fails once.</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>So how much do the lines blur?</h2>

<div class="calc">
<span class="tag">Comparing with the natural width</span>
<p class="lbl">Natural width of Lyman α (spontaneous emission \(A=6.27\times10^8\ \mathrm{s^{-1}}\))</p>
$$\frac{\Delta\nu}{\nu}=\frac{A/2\pi}{\nu}=\frac{9.97\times10^{7}}{2.47\times10^{15}}=4.04\times10^{-8}$$
<p class="lbl">Fractional change in frequency during the emission (\(1/A\) seconds) in this picture</p>
$$\frac{\dot\nu}{\nu}\cdot\frac{1}{A}=\frac{H_0}{A}=\frac{2.30\times10^{-18}}{6.27\times10^{8}}=3.67\times10^{-27}$$
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0">The blurring from shrinking atoms is <strong>\(9\times10^{-20}\)</strong> times the natural width.<br>
── <em>Nineteen orders below.</em> Einstein's blade does not reach.</p>
</div>

<h2><span class="n">05</span>Atomic clock limits are satisfied exactly, by zero</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Observational bound</th><th class="mid">This picture predicts</th></tr></thead>
<tbody>
<tr><th>\(\dot\alpha/\alpha\)</th><td class="mid">\(1.0(1.1)\times10^{-18}\)/yr (Lange 2021)</td><td class="mid"><strong>exactly 0</strong></td></tr>
<tr><th>\(\dot\mu/\mu\) (\(\mu=m_p/m_e\))</th><td class="mid">\(\sim10^{-17}\)/yr (molecular clocks)</td><td class="mid"><strong>exactly 0</strong></td></tr>
<tr><th>Every mass ratio and charge ratio</th><td class="mid">various</td><td class="mid"><strong>exactly 0</strong></td></tr>
</tbody>
</table>
</div>

<p>The reason is the usual one — <strong>numerator and denominator carry the same weight</strong>. In \(\alpha=e^2/4\pi\varepsilon_0\hbar c\), all of \(e,\hbar,c\) have weight 0. In \(\mu=m_p/m_e\), both are weight \(-1\). They cancel; there is no way for them to move.</p>

<h2><span class="n">06</span>The reveal — there is no comparison partner</h2>

<div class="calc">
<span class="tag">The shrinking rate</span>
$$\frac{\dot a_B}{a_B}=-H_0=-7.25\times10^{-11}\ /\text{yr}$$
</div>

<p>As with \(G\) in Episode 7, read naively that is an outrageous rate. So why is it not measurable? <strong>Because when you look for something to compare against, everything has the same weight.</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Compare the size of an atom against…</th><th class="mid">Its weight</th><th class="mid">The ratio</th></tr></thead>
<tbody>
<tr><th>another atom</th><td class="mid">\(+1\)</td><td class="mid">invariant</td></tr>
<tr><th>a wavelength of light</th><td class="mid">\(+1\)</td><td class="mid">invariant</td></tr>
<tr><th>a ruler (made of atoms)</th><td class="mid">\(+1\)</td><td class="mid">invariant</td></tr>
<tr><th>\(c\times\) a clock tick</th><td class="mid">\(+1\)</td><td class="mid">invariant</td></tr>
<tr class="hi"><th>nothing at all</th><td class="mid">──</td><td class="mid"><strong>there is no claim</strong></td></tr>
</tbody>
</table>
</div>

<p>Do to the atom what Episode 3 did to the title of the series and you get this: <em>"atoms are shrinking" is not a sentence until you name what they are shrinking relative to</em>. And when you look, there is no ruler outside atoms that is independent of atoms. The starting point of Episode 2 of the previous series — <strong>every ruler bottoms out in atoms</strong> — closes here.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① Writing the adiabatic parameter as \(\hbar H/\Delta E\) is the crudest estimate.</strong> The exact condition is \(|\langle m|\partial_t H|n\rangle|/(E_n-E_m)^2\ll1\), with matrix elements. This document evaluates only "rate of change of the Hamiltonian ÷ level spacing" by dimensional analysis — but matrix elements are dimensionless \(O(1)\) numbers, so <em>the conclusion at 34 orders does not move</em>.</p>
<p style="margin:0 0 10px"><strong>② The "blurring" is estimated as the frequency change during the radiative lifetime \(1/A\).</strong> It is not a full line-shape calculation (natural, Doppler and pressure widths). Read it as an order-of-magnitude argument; laboratory lines are buried under Doppler and collisional widths far larger than this effect.</p>
<p style="margin:0 0 10px"><strong>③ "Satisfies the atomic clock limits exactly by zero" holds when \(c\cdot t=\text{const}\) is implemented <em>as a conformal transformation</em>.</strong> In a VSL-type implementation that moves only \(c\), \(\alpha\) moves and collides with these bounds (Extra 3 of the previous series). <em>The same words "the speed of light varies" live or die on the implementation.</em></p>
<p style="margin:0 0 10px"><strong>④ Weyl's 1918 theory and this operation are different things.</strong> Weyl proposed a geometry with a non-integrable length connection (Weyl geometry). Here \(\Omega\) is single-valued and the connection integrable, so there is no second clock effect from the start. <em>The objection was not dodged; there is nothing for it to hit</em> — exactly the account in Episode 1 of the previous series. Non-integrable Weyl geometry, incidentally, remains a live research topic in gravity.</p>
<p style="margin:0"><strong>⑤ Recombination is taken as "when atoms form".</strong> In fact hydrogen forms in bulk at \(z\simeq1100\), and short-lived bound states existed earlier. The band in the figure is an indication.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>State in one line the argument with which Einstein killed Weyl's theory in 1918.
<details><summary>Show the answer</summary><div class="ans">If carrying the standard of length <strong>requires a path</strong>, the same atom emits light of different wavelength depending on the route it took (the second clock effect). But real spectral lines are sharp — so it is refuted immediately.</div></details></li>

<li>Give two reasons the modern conformal transformation is not cut by the same argument.
<details><summary>Show the answer</summary><div class="ans">① \(\Omega(x)\) is <strong>single-valued</strong>, so the change of length is path-independent (integrable) and the second clock effect cannot occur. ② Even with time-varying mass, the adiabatic parameter \(\hbar H/\Delta E\sim10^{-34}\) induces no transitions. <em>Doubly protected.</em></div></details></li>

<li>When does adiabaticity fail for the 21 cm line (\(\Delta E=5.9\times10^{-6}\) eV)?
<details><summary>Show the answer</summary><div class="ans">\(t=\hbar/\Delta E=6.58\times10^{-16}/5.9\times10^{-6}=1.1\times10^{-10}\) s — <strong>23 orders of magnitude before</strong> atoms form at recombination (\(1.2\times10^{13}\) s). It never fails in an era with atoms.</div></details></li>

<li>The Bohr radius shrinks at \(7.2\times10^{-11}\)/yr. Why is that not measurable?
<details><summary>Show the answer</summary><div class="ans">Because everything to compare against has weight \(+1\) — other atoms, wavelengths of light, rulers, \(c\times\)clock ticks all shrink by the same factor. <strong>There is no ruler outside atoms that is independent of atoms</strong> (Episode 2 of the previous series). So "atoms are shrinking" is not a sentence until you name the comparison.</div></details></li>

<li>(Harder) Both say "the speed of light varies", yet VSL is killed by atomic clocks and this picture is not. What is the difference?
<details><summary>Show the answer</summary><div class="ans">VSL moves \(c\) alone while fixing \(e,\hbar\), so \(\alpha\) moves and collides with the atomic clock bound (\(\dot\alpha/\alpha<10^{-18}\)/yr). This picture <strong>moves the whole set together</strong>, so \(\alpha\) is exactly invariant. <em>Life or death turns not on how you move dimensionful quantities but on whether you protect the dimensionless ones</em> (Extras 3 and 4 of the previous series). The same pattern as \(G\) in Episode 7.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — Einstein's blade is stopped twice</h2>
<p>Atoms shrink as \(1/t\) here. In 1918 Einstein killed Weyl's unified theory by attacking precisely this kind of variation — <strong>if carrying a standard of length needs a path, atoms remember their history and spectral lines blur</strong>. A decisive objection.</p>
<p>The same blade cannot reach the modern conformal transformation, for two reasons. ① \(\Omega(x)\) is single-valued, so <strong>there is no path dependence at all</strong> (Episode 1 of the previous series). ② And the second is today's calculation: the adiabatic parameter \(\varepsilon=\hbar H/\Delta E\) is <strong>\(1.1\times10^{-34}\)</strong> for the hydrogen Rydberg. Adiabaticity would fail at \(t=\hbar/\Delta E=4.8\times10^{-17}\) s, and even for the slackest 21 cm line at \(1.1\times10^{-10}\) s. <em>Atoms only form at \(1.2\times10^{13}\) s (380,000 yr), so the entire era of atoms is perfectly adiabatic.</em></p>
<p>We also counted the blurring: the frequency change over a radiative lifetime is \(H_0/A=3.7\times10^{-27}\) — <strong>\(9\times10^{-20}\)</strong> of Lyman α's natural width \(4.0\times10^{-8}\), nineteen orders below. And the atomic-clock bounds on \(\dot\alpha/\alpha\) and \(\dot\mu/\mu\) are met by predictions of <strong>exactly zero</strong> (numerator and denominator share a weight).</p>
<p>The reveal took its usual shape. The Bohr radius really does shrink at \(7.2\times10^{-11}\)/yr and still cannot be measured — <strong>because everything to compare against has weight \(+1\)</strong>. Other atoms, wavelengths, rulers, all shrink alike. <em>"Atoms are shrinking" is not a sentence until you name the comparison.</em> Apply Episode 3's surgery to the atom and you arrive right back at Episode 2 of the previous series: every ruler bottoms out in atoms.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 10</span>
Next: <strong>heat and information</strong>. Temperature does not move in this picture (\(\tilde T=aT=\)const) — the universe sits at 2.7255 K and never cools. So <em>the Landauer limit, the energy \(k_BT\ln2\) needed to erase one bit, is constant across the whole history of the universe</em> (\(1.63\times10^{-4}\) eV). A quantity that falls as \(1/a\) in the standard picture is pinned here. Which then is the "real" cost of erasure? The answer is Episode 3's: <strong>it is not a question until you say what you are comparing against</strong>. Against a particle mass it gets cheaper as \(1/t\); against a single photon it is constant. <em>Even the price of erasing information had a hidden comparison partner.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var se=document.getElementById('se'), ve=document.getElementById('ve'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=318;
  var hbar=6.582119569e-16;
  var xmin=-44, xmax=18;
  var ymin=-40, ymax=12;
  var LREC=Math.log(1.2e13)/Math.LN10, LNOW=Math.log(4.3536e17)/Math.LN10;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function draw(){
    var f=parseInt(se.value,10)/1000;
    var dE=1e-10*Math.pow(1e17,f);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.fillStyle='#eef2f1';
    g.fillRect(px(LREC), Y0, px(xmax)-px(LREC), Y1-Y0);
    g.fillStyle='#8b9c97'; g.textAlign='center';
    g.fillText('era in which atoms exist', (px(LREC)+px(xmax))/2, Y0+16);

    g.textAlign='right';
    for(var e=-40;e<=10;e+=10){
      var y=py(e);
      g.strokeStyle='#eef2f1'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#93a5a0'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-40;q<=10;q+=10){
      var x=px(q);
      g.strokeStyle='#f4f7f6'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#93a5a0'; g.fillText('10'+q, x, Y1+16);
    }
    g.strokeStyle='#c3d0cc'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    g.strokeStyle='#a35a1f'; g.lineWidth=2.2; g.setLineDash([7,5]);
    g.beginPath(); g.moveTo(X0,py(0)); g.lineTo(X1,py(0)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#a35a1f'; g.textAlign='left';
    g.fillText('ε = 1 (above this, adiabaticity fails)', X0+8, py(0)-7);

    var A=Math.log(hbar/dE)/Math.LN10;
    g.strokeStyle='#2c4a45'; g.lineWidth=3.2;
    g.beginPath();
    g.moveTo(px(xmin),py(Math.min(Math.max(A-xmin,ymin),ymax)));
    g.lineTo(px(xmax),py(Math.min(Math.max(A-xmax,ymin),ymax)));
    g.stroke();

    var xc=A;
    if(xc>xmin&&xc<xmax){
      g.fillStyle='#a35a1f';
      g.beginPath(); g.arc(px(xc),py(0),5.5,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=1.7;
      g.beginPath(); g.arc(px(xc),py(0),5.5,0,6.2832); g.stroke();
    }

    [[LREC,'recombination'],[LNOW,'now']].forEach(function(q){
      g.strokeStyle='#b6c4c0'; g.lineWidth=1.3; g.setLineDash([4,4]);
      g.beginPath(); g.moveTo(px(q[0]),Y0); g.lineTo(px(q[0]),Y1); g.stroke();
      g.setLineDash([]);
      g.fillStyle='#7d8f8a'; g.textAlign='center';
      g.fillText(q[1], px(q[0]), Y1-8);
    });

    g.fillStyle='#6b7d78'; g.textAlign='center';
    g.fillText('age of the universe  t [s]', (X0+X1)/2, Y1+36);

    var eps_now=hbar/(4.3536e17*dE);
    ve.textContent = dE>=1 ? dE.toPrecision(3)+' eV' : dE.toExponential(2)+' eV';
    ro.textContent='ΔE = '+ve.textContent+
      '　→　adiabatic parameter today ε = '+eps_now.toExponential(2)+
      '　/　adiabaticity fails at t = ħ/ΔE = '+(hbar/dE).toExponential(2)+' s'+
      '　/　that is '+(Math.abs(LREC-xc)).toFixed(0)+' orders before recombination (1.2×10¹³ s)';
  }
  se.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-09-atom.html', acc='#2c4a45', ops='#a35a1f',
      title='Substituting into the atom ── c·t = const, That Clicks, Episode 9',
      ep='EPISODE 9 ／ Why the blade of 1918 does not reach',
      eyebrow='Atoms shrink, and the spectral lines do not blur',
      h1='Substituting<br>into the atom',
      sub='Einstein killed Weyl\'s unified theory with exactly this argument.<br><em>Two numbers say why the same blade misses the modern conformal transformation.</em>',
      byline_l='What you need: division, an intuition for the adiabatic theorem',
      byline_r='\\(\\varepsilon=\\hbar H/\\Delta E=1.1\\times10^{-34}\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 9 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. Weyl\'s (1918) gauge theory of length, Einstein\'s objection to it (a non-integrable length connection produces a second clock effect, yet atomic spectra are sharp), and the fact that the modern conformal transformation restricts \\(\\Omega\\) to a single-valued function — the integrable case, with no second clock effect — are established history and physics (Episode 1 of the previous series). The adiabatic theorem, and the fact that adiabaticity is governed by the ratio of the Hamiltonian\'s rate of change to the level spacing, are standard. The \\(\\varepsilon=\\hbar H/\\Delta E\\) used here is <strong>a crude dimensional estimate</strong>; the exact condition involves the matrix element \\(\\langle m|\\partial_tH|n\\rangle/(E_n-E_m)^2\\) — but those are dimensionless \\(O(1)\\) numbers, so the order of magnitude of the conclusion is unaffected. The table (\\(\\hbar H_0=1.51\\times10^{-33}\\) eV, \\(1.1\\times10^{-34}\\) for the Rydberg, failure time \\(t=\\hbar/\\Delta E\\)) and the line-width comparison (\\(H_0/A=3.7\\times10^{-27}\\) against Lyman α\'s natural width \\(4.04\\times10^{-8}\\), a ratio of \\(9\\times10^{-20}\\)) are computed here. Lyman α\'s \\(A=6.265\\times10^8\\ \\mathrm{s^{-1}}\\) and \\(\\nu=2.466\\times10^{15}\\) Hz are standard values. The width estimate uses the frequency change over the radiative lifetime and is not a full line-shape calculation (Doppler and collisional widths dominate in the laboratory). The atomic clock bound \\(\\dot\\alpha/\\alpha=1.0(1.1)\\times10^{-18}\\)/yr is Lange et al. (2021, PRL 126, 011102). "Satisfies the bounds exactly by zero" applies when \\(c\\cdot t=\\text{const}\\) is implemented <em>as a conformal transformation</em>; a VSL-type implementation moving only \\(c\\) makes \\(\\alpha\\) vary and collides with these bounds (Extra 3 of the previous series). Non-integrable Weyl geometry remains a research topic today. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination and conflicts with nucleosynthesis when extrapolated into the early universe (Lewis, Barnes &amp; Kaushik 2016). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the transition energy and the crossing never enters the era of atoms. "Show the answer" opens each solution.')
