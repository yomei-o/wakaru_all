# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">We have written many times that light passes straight through a conformal transformation, but never treated it head on. Today we do. Look at a photon gas in this picture and — <strong>number density, energy density, temperature, wavelength, all constant</strong>. <em>Completely at rest.</em> Nothing has happened to light in the entire history of the universe; only matter has been growing. The result of Episode 7 of the previous series — that only the 4D Maxwell action is exactly conformally invariant — shows itself in its most naked form.</p>

<h2><span class="n">01</span>Transforming the photon gas, item by item</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Weight</th><th class="mid">Standard picture</th><th class="mid">This picture</th></tr></thead>
<tbody>
<tr class="hi"><th>Photon number density \(n_\gamma\)</th><td class="mid">\(+3\)</td><td class="mid">\(\propto a^{-3}\)</td><td class="mid"><strong>constant</strong></td></tr>
<tr class="hi"><th>Energy density \(\rho_\gamma\)</th><td class="mid">\(-4\)</td><td class="mid">\(\propto a^{-4}\)</td><td class="mid"><strong>constant</strong></td></tr>
<tr class="hi"><th>Temperature \(T\)</th><td class="mid">\(-1\)</td><td class="mid">\(\propto a^{-1}\)</td><td class="mid"><strong>constant</strong></td></tr>
<tr class="hi"><th>Energy of one photon \(\hbar\omega\)</th><td class="mid">\(-1\)</td><td class="mid">\(\propto a^{-1}\)</td><td class="mid"><strong>constant</strong></td></tr>
<tr class="hi"><th>Wavelength \(\lambda\)</th><td class="mid">\(+1\)</td><td class="mid">\(\propto a\)</td><td class="mid"><strong>constant</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>Nothing about light moves at all.</strong><br>
Today's photon number density \(4.11\times10^{8}\ \mathrm{m^{-3}}\) is the same value throughout the history of the universe.<br>
<em>The photon gas in this picture is completely at rest.</em></p>
</div>

<p>This is no accident. The power of \(a\) by which each photon quantity varies in the standard picture, and that quantity's weight, are <strong>exactly the same number</strong>. Multiply and they must cancel. <em>Light is built to fit a conformal transformation with nothing left over.</em></p>

<h2><span class="n">02</span>And not one observation changes</h2>

<p>"Everything about light is constant" sounds as if something must break. Nothing does — <strong>because only two dimensionless numbers fix the CMB</strong>.</p>

<div class="calc">
<span class="tag">The two numbers that fix the CMB</span>
<p class="lbl">① entropy per photon</p>
$$\frac{s_\gamma}{n_\gamma}=\frac{1.478\times10^{9}}{4.111\times10^{8}}=3.60\ k_B\qquad(\text{blackbody theory: }3.602)$$
<p class="lbl">② baryon-to-photon ratio</p>
$$\eta=\frac{n_b}{n_\gamma}=6.1\times10^{-10}$$
</div>

<p>Both are dimensionless, hence identical in this picture and the standard one. And the blackbody spectral shape is fixed by the dimensionless combination \(\hbar\omega/k_BT\) alone, so it too is <strong>invariant</strong>. <em>The Planck distribution is unchanged to the letter.</em></p>

<div class="aside">
<span class="tag">What "nucleosynthesis depends only on \(\eta\)" means</span>
The predictions of big bang nucleosynthesis reduce to a function of \(\eta\) alone. \(\eta\) is dimensionless and does not move here — so <strong>the helium prediction does not budge a millimetre when you swap pictures</strong>. When Extra 1 of the previous series wrote "defend it in whichever of the three pictures you like, the verdict is the same", this one line was the substance of it. <em>The picture changes, \(\eta\) does not, so the verdict does not.</em>
</div>

<h2><span class="n">03</span>Redshift turns completely inside out</h2>

<p>If nothing happens to light, where does redshift come from? <strong>From the receiver.</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th>Standard picture</th><th>This picture</th></tr></thead>
<tbody>
<tr><th>Light in flight</th><td>space stretches, so the wavelength stretches</td><td><strong>nothing happens</strong></td></tr>
<tr><th>Laboratory hydrogen atom</th><td>always the same</td><td><strong>getting heavier</strong> (\(\tilde m=am\))</td></tr>
<tr><th>Reference Lyman α</th><td>always the same wavelength</td><td>gets shorter with time</td></tr>
<tr class="hi"><th>What the spectrograph reads, \(1+z\)</th><td class="mid">\(\lambda_{\rm obs}/\lambda_{\rm lab}\)</td><td class="mid">the same value</td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">One number, two readings</span>
<p class="lbl">Lyman α from a galaxy at \(z=7\)</p>
$$\text{standard: the wavelength stretched }8\times\qquad\text{here: the laboratory reference got }8\times\text{ finer}$$
<p class="lbl">The CMB at \(z=1100\)</p>
$$1101\times\qquad\text{either reading gives the same spectrograph scale}$$
</div>

<p><em>Not "the light stretched" but "the ruler grew"</em> — what Episodes 2 and 3 of the previous series said in words is now fully backed by §01's table. <strong>There is no room on the light's side for anything to stretch.</strong></p>

<div class="fig">
<p class="cap">Figure: the slider switches the way of speaking. At the left (standard) the photon quantities scatter in all directions; at the right (this picture) <strong>all four go perfectly flat</strong>. The dimensionless ratios (\(s/n\) and \(\eta\)) never move anywhere.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Way of speaking \(s\) (left = standard / right = mass grows)<input id="ss" type="range" min="0" max="1000" value="1000" step="1"></label>
  <span class="val" id="vs">s = 1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6b2f2f"></i>number density \(n_\gamma\)</span>
  <span><i class="swatch" style="background:#a85a3a"></i>energy density \(\rho_\gamma\)</span>
  <span><i class="swatch" style="background:#8a6a6a"></i>temperature \(T\)</span>
  <span><i class="swatch" style="background:#b09090"></i>wavelength \(\lambda\)</span>
  <span><i class="swatch" style="background:#1f5f5a"></i>dimensionless ratios (\(s/n\), \(\eta\))</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The reveal — it balances exactly, only in four dimensions</h2>

<div class="calc">
<span class="tag">Counting the Maxwell action</span>
$$S_{\rm EM}=-\frac{1}{4\mu_0}\int\!\sqrt{-g}\;F_{\mu\nu}F_{\alpha\beta}\,g^{\mu\alpha}g^{\nu\beta}\;d^Dx$$
<p class="lbl">the volume element produces \(D\) factors of \(\Omega\); two inverse metrics eat 4</p>
$$S_{\rm EM}\ \longrightarrow\ \Omega^{\,D-4}\,S_{\rm EM}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Dimension \(D\)</th><th class="mid">2</th><th class="mid">3</th><th class="mid">4</th><th class="mid">5</th><th class="mid">6</th></tr></thead>
<tbody>
<tr><th>Residual factor</th><td class="mid">\(\Omega^{-2}\)</td><td class="mid">\(\Omega^{-1}\)</td><td class="mid"><strong>\(\Omega^{0}=1\)</strong></td><td class="mid">\(\Omega^{+1}\)</td><td class="mid">\(\Omega^{+2}\)</td></tr>
</tbody>
</table>
</div>

<p>What is produced balances what is eaten only at \(D=4\). <strong>That we live in four dimensions is why the photon gas looks stationary here.</strong> In five dimensions, light would move even in this picture, and "push the whole expansion into mass" would fail.</p>

<h2><span class="n">05</span>The plainer statement — light has nothing to compare against</h2>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>It carries no ruler</strong><span>the Compton wavelength \(\hbar/mc\) diverges as \(m\to0\) — it specifies no length</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>It carries no clock</strong><span>proper time along a light ray is zero — it specifies no duration</span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>So it cannot notice</strong><span>swap the ruler and light has nothing to compare against, so no change is detectable</span></div></div>
</div>

<p>Episode 3 said "you need a comparison to call \(c\cdot t\) constant"; Episode 9 said "you need a comparison to say atoms are shrinking". <em>Light has no comparison partner at all</em> — so it has nothing to say about a conformal transformation. <strong>That is the everyday translation of "conformally invariant".</strong></p>

<h2><span class="n">06</span>Except that quantum theory breaks it</h2>

<p>All of the above is classical. Quantise and conformal symmetry breaks even in a massless theory, because defining a field theory requires a scale \(\mu\) (Episode 8 of the previous series).</p>

<div class="calc">
<span class="tag">The size of the breaking</span>
$$T^\mu{}_\mu=\frac{\beta(g)}{2g}F_{\mu\nu}F^{\mu\nu}$$
<p class="lbl">measured in experiment</p>
$$\frac{1}{\alpha}:\ 137.036\ \longrightarrow\ 127.95\quad(\text{from the electron mass to }M_Z)$$
</div>

<p>So <strong>"nothing happens to light" is a classical statement</strong>. Quantum theory forces a ruler onto light after all. Part V (Episode 37) treats this breaking head on — <em>the first of the places where this series' tool breaks</em>.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① "The photon gas is at rest" refers to the coordinates after the conformal transformation.</strong> The locally measured speed of light is \(c_0\) in every picture, and a CMB thermometer reads 2.7255 K in every picture. <em>No observation changes when the picture is swapped.</em></p>
<p style="margin:0 0 10px"><strong>② \(n_\gamma\propto a^{-3}\) and \(T\propto a^{-1}\) hold for adiabatic expansion.</strong> During epochs when annihilation dumps entropy there are corrections from the change in \(g_{*s}\) (Episode 2 computed 1.10 nat). The table shows the plain dependence with those corrections removed.</p>
<p style="margin:0 0 10px"><strong>③ "Nucleosynthesis is a function of \(\eta\) alone" is a simplification.</strong> Strictly, the effective relativistic degrees of freedom \(g_*\), the neutron lifetime, and the expansion rate also matter — <em>and it was the expansion rate that ruled out \(a\propto t\) in Extra 1 of the previous series</em>. The claim here is only that swapping pictures does not move \(\eta\), so the verdict does not change because of the picture.</p>
<p style="margin:0 0 10px"><strong>④ \(s_\gamma/n_\gamma=3.60\) is computed here from the numbers;</strong> the exact blackbody value is \(4\pi^4/(45\zeta(3))=3.6017\). The \(n_\gamma=4.11\times10^8\ \mathrm{m^{-3}}\) and \(s_\gamma=1.478\times10^9\ k_B\,\mathrm{m^{-3}}\) used are standard values at \(T_0=2.7255\) K.</p>
<p style="margin:0"><strong>⑤ The \(\Omega^{D-4}\) counting takes \(A_\mu\) (lower index) to have weight 0.</strong> That is the standard convention; writing \(A^\mu\) obviously changes the weight — <em>whether the action is invariant does not depend on how you write it</em>, but the intermediate bookkeeping does.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Explain by weights why the photon number density is constant here.
<details><summary>Show the answer</summary><div class="ans">\(n_\gamma\) has weight \(+3\) (inverse volume), so \(\tilde n=a^3n\); in the standard picture \(n\propto a^{-3}\). Multiplying, \(a^3\cdot a^{-3}=1\) — <strong>exact cancellation</strong>. Energy density (\(-4\) with \(a^{-4}\)), temperature (\(-1\) with \(a^{-1}\)) and wavelength (\(+1\) with \(a\)) have the same structure.</div></details></li>

<li>Name the two dimensionless numbers that fix the CMB and say what happens to them here.
<details><summary>Show the answer</summary><div class="ans">Entropy per photon \(s/n=3.60\,k_B\) and the baryon-to-photon ratio \(\eta=6.1\times10^{-10}\). Both are dimensionless, so <strong>they do not move at all</strong>. The blackbody shape depends only on \(\hbar\omega/k_BT\) and is likewise invariant.</div></details></li>

<li>In what dimension is the Maxwell action conformally invariant, and why?
<details><summary>Show the answer</summary><div class="ans">\(D=4\) only. \(\sqrt{-g}\) produces \(D\) factors of \(\Omega\) and two inverse metrics eat 4, leaving \(\Omega^{D-4}\). <em>That we live in four dimensions is why the photon gas looks stationary in this picture.</em></div></details></li>

<li>Explain the Lyman α of a \(z=7\) galaxy in both pictures.
<details><summary>Show the answer</summary><div class="ans">Standard: space stretched 8-fold, so the wavelength in flight stretched 8-fold. Here: <strong>the light arrives unchanged</strong>, and laboratory hydrogen got heavier so the reference Lyman α became 8 times finer. The spectrograph reads \(\lambda_{\rm obs}/\lambda_{\rm lab}=8\) either way.</div></details></li>

<li>(Harder) How far is "nothing happens to light" correct?
<details><summary>Show the answer</summary><div class="ans"><strong>As far as classical physics.</strong> Quantisation requires a scale \(\mu\), so conformal symmetry breaks even in a massless theory (the trace anomaly \(T^\mu{}_\mu=(\beta/2g)F^2\)). The breaking is measured: \(1/\alpha\) running from 137.036 to 127.95. <em>Quantum theory forces a ruler onto light after all.</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — light had no room to stretch</h2>
<p>Transform the CMB quantities by the weight table and <strong>number density, energy density, temperature, per-photon energy and wavelength are all constant</strong>, because the power of \(a\) in the standard picture and the weight of each quantity are exactly the same number. <em>The photon gas in this picture is completely at rest</em> — today's \(4.11\times10^8\ \mathrm{m^{-3}}\) is its value throughout cosmic history.</p>
<p>And no observation changes. Only two dimensionless numbers fix the CMB — entropy per photon \(3.60\,k_B\) and the baryon-to-photon ratio \(\eta=6.1\times10^{-10}\). Neither moves, and the blackbody shape depends only on \(\hbar\omega/k_BT\). <strong>Since the nucleosynthesis prediction is a function of \(\eta\), swapping pictures cannot move the verdict</strong> — which is what Extra 1's "defend it in any of the three pictures, same result" came down to.</p>
<p>And redshift turns inside out. With no room on the light's side, <em>what changed is the receiver</em>. At \(z=7\), not "the wavelength stretched 8-fold" but "the laboratory reference got 8 times finer". The spectrograph reads the same 8.</p>
<p>The reveal was dimensional: the Maxwell action picks up \(\Omega^{D-4}\), so <strong>it is exactly conformally invariant only at \(D=4\)</strong>. That we live in four dimensions is why this picture works at all. More plainly, light carries <em>neither ruler nor clock</em> (infinite Compton wavelength, zero proper time) — so when the ruler is swapped it has nothing to compare against and cannot notice. All classical, though: quantise and a scale \(\mu\) enters, and the breaking shows up in experiment as \(1/137\to1/128\). <strong>The first place the tool breaks.</strong></p>
</div>

<div class="next">
<span class="lbl">Next — Episode 12</span>
A few episodes left in Part II. Next: <strong>the vacuum</strong>. Energy density has weight \(-4\), so here the vacuum energy is \(\tilde\rho_\Lambda=a^4\rho_\Lambda\propto t^4\) — <em>the cosmological constant alone grows as \(t^4\)</em>. Matter goes as \(\propto t\), radiation is constant. <strong>Three different behaviours, and \(\Lambda\) is the fastest.</strong> Yet made dimensionless, \(\rho_\Lambda^{1/4}/M_{\rm Pl}=1.84\times10^{-31}\) is invariant. We look at how the cosmological constant problem (the \(10^{120}\) discrepancy) appears in this picture — and confirm that <em>the "why now?" problem alone does not go away when you change pictures</em>.
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=318;
  var xmin=-3, xmax=0.3;
  var ymin=-4, ymax=13;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function line(sl,col,w,dash){
    g.strokeStyle=col; g.lineWidth=w; if(dash) g.setLineDash(dash);
    g.beginPath();
    var y0=sl*xmin, y1=sl*xmax;
    g.moveTo(px(xmin),py(Math.max(Math.min(y0,ymax),ymin)));
    g.lineTo(px(xmax),py(Math.max(Math.min(y1,ymax),ymin)));
    g.stroke(); g.setLineDash([]);
  }

  function draw(){
    var s=parseInt(ss.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=-4;e<=12;e+=2){
      var y=py(e);
      g.strokeStyle=(e===0?'#e0d2d2':'#f6efef'); g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a89494'; g.fillText(e===0?'1':(e<0?'10⁻'+Math.abs(e):'10'+e), X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-3;q<=0;q++){
      var x=px(q);
      g.strokeStyle='#faf5f5'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a89494'; g.fillText(q===0?'now':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#d2c0c0'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    line(-3*(1-s), '#6b2f2f', 3.2);
    line(-4*(1-s), '#a85a3a', 2.8);
    line(-1*(1-s), '#8a6a6a', 2.4);
    line(+1*(1-s), '#b09090', 2.4);
    line(0,        '#1f5f5a', 3.6);

    g.textAlign='left';
    if(s<0.9){
      g.fillStyle='#6b2f2f'; g.fillText('n', px(xmin)+6, py(Math.min(-3*(1-s)*xmin,ymax))-6);
      g.fillStyle='#a85a3a'; g.fillText('ρ', px(xmin)+22, py(Math.min(-4*(1-s)*xmin,ymax))+14);
      g.fillStyle='#8a6a6a'; g.fillText('T', px(xmin)+6, py(-1*(1-s)*xmin)-6);
      g.fillStyle='#b09090'; g.fillText('λ', px(xmin)+6, py(1*(1-s)*xmin)+14);
    }
    g.fillStyle='#1f5f5a';
    g.fillText('dimensionless ratios s/n, η (flat everywhere)', px(-1.9), py(0)-10);
    if(s>0.985){
      g.fillStyle='#6b2f2f'; g.textAlign='right';
      g.fillText('n, ρ, T, λ all collapse onto this line', X1-8, py(0)+18);
    }

    g.fillStyle='#8a7070'; g.textAlign='center';
    g.fillText('scale factor  a', (X0+X1)/2, Y1+36);

    vs.textContent='s = '+s.toFixed(2);
    var tag = s>0.995?'(mass-grows picture)':(s<0.005?'(standard picture)':'(intermediate)');
    ro.textContent='s = '+s.toFixed(2)+' '+tag+
      '　n ∝ a^'+(-3*(1-s)).toFixed(2)+
      '　ρ ∝ a^'+(-4*(1-s)).toFixed(2)+
      '　T ∝ a^'+(-1*(1-s)).toFixed(2)+
      '　λ ∝ a^'+(1*(1-s)).toFixed(2)+
      (s>0.995 ? '　★ all four exponents zero — the photon gas is completely at rest' : '');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-11-light.html', acc='#6b2f2f', ops='#1f5f5a',
      title='Substituting into light ── c·t = const, That Clicks, Episode 11',
      ep='EPISODE 11 ／ The photon gas is completely at rest',
      eyebrow='Light had no room to stretch in the first place',
      h1='Substituting<br>into light',
      sub='Number density, energy density, temperature, wavelength — all constant.<br><em>Nothing has happened to light in the entire history of the universe.</em>',
      byline_l='What you need: adding weights, matching exponents',
      byline_r='\\(\\Omega^{D-4}\\) — exact only in four dimensions',
      body=BODY + '\n\n<p class="foot">This document is Episode 11 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That adiabatic expansion gives \\(n_\\gamma\\propto a^{-3}\\), \\(\\rho_\\gamma\\propto a^{-4}\\), \\(T\\propto a^{-1}\\) and \\(\\lambda\\propto a\\); that their conformal weights are \\(+3,-4,-1,+1\\); and that the Maxwell action picks up \\(\\Omega^{D-4}\\) and is conformally invariant only at \\(D=4\\), are all standard results (Episode 7 of the previous series). Today\'s CMB values \\(T_0=2.7255\\) K, \\(n_\\gamma=4.11\\times10^8\\ \\mathrm{m^{-3}}\\), \\(s_\\gamma=1.478\\times10^9\\,k_B\\,\\mathrm{m^{-3}}\\) and \\(\\eta=6.1\\times10^{-10}\\) are standard; \\(s_\\gamma/n_\\gamma=3.60\\,k_B\\) is computed here (exact blackbody value \\(4\\pi^4/45\\zeta(3)=3.6017\\)). During epochs of entropy release by annihilation there are corrections from the change in \\(g_{*s}\\) (Episode 2 computed 1.10 nat). "Nucleosynthesis is a function of \\(\\eta\\) alone" is a simplification: \\(g_*\\), the neutron lifetime and the expansion rate also matter — <strong>and it was the expansion rate that ruled out \\(a\\propto t\\) in Extra 1 of the previous series</strong>. The claim made here is only that swapping pictures does not move \\(\\eta\\), so the picture cannot change the verdict. Taking \\(A_\\mu\\) (lower index) to have weight 0 is the standard convention; the intermediate counting depends on the convention but the invariance of the action does not. That quantisation breaks conformal symmetry (the trace anomaly \\(T^\\mu{}_\\mu=(\\beta/2g)F_{\\mu\\nu}F^{\\mu\\nu}\\)) and that \\(\\alpha^{-1}\\) runs from 137.036 to 127.95 at \\(M_Z\\) are standard (Episode 8 of the previous series). The locally measured speed of light and the reading of a CMB thermometer are the same in every picture. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination and conflicts with nucleosynthesis when extrapolated into the early universe (Lewis, Barnes &amp; Kaushik 2016). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider switches the way of speaking and at the right all four photon curves go flat. "Show the answer" opens each solution.')
