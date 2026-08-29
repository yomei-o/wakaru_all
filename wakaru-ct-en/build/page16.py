# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Part II's ten episodes fold into one page. Gravity, quantum mechanics, atoms, heat and information, light, the vacuum, fluids, phase transitions, chemistry and biology — <strong>wherever we substituted, only one thing ever moved</strong>. And listing everything that did not move gives, directly, <em>an inventory of what physics is</em>. Finally we draw the line between where this notation <strong>genuinely helps</strong> and where it is <strong>completely powerless</strong>, and close Part II.</p>

<h2><span class="n">01</span>Ten episodes, one line each</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Ep.</th><th>Substituted into</th><th>What moved</th><th>What did not</th></tr></thead>
<tbody>
<tr><th class="mid">7</th><td>gravity</td><td>\(G\) (\(\div a^2\)), \(g\), \(r_s\), \(T_H\)</td><td><strong>\(\alpha_G\), Dirac's large numbers, BH entropy, strain \(h\)</strong></td></tr>
<tr><th class="mid">8</th><td>quantum mechanics</td><td>de Broglie wavelength, levels, Compton wavelength</td><td><strong>the equation's form, \(\Delta x\Delta p\), \(S/\hbar\), tunnelling</strong></td></tr>
<tr><th class="mid">9</th><td>the atom</td><td>Bohr radius (\(7.2\times10^{-11}\)/yr)</td><td><strong>spectral lines, \(\alpha\), \(\mu=m_p/m_e\)</strong></td></tr>
<tr><th class="mid">10</th><td>heat and information</td><td>temperature, Landauer cost</td><td><strong>entropy, Boltzmann factor, the second law</strong></td></tr>
<tr><th class="mid">11</th><td>light</td><td>(nothing moves)</td><td><strong>\(n_\gamma\), \(\rho_\gamma\), \(T\), \(\lambda\), \(s/n\), \(\eta_b\)</strong></td></tr>
<tr><th class="mid">12</th><td>the vacuum</td><td>\(\rho_\Lambda\) (\(\propto t^4\)), \(\rho_m\), the ranking</td><td><strong>\(\rho_\Lambda/M_{\rm Pl}^4\), \(w=-1\), equality epochs</strong></td></tr>
<tr><th class="mid">13</th><td>fluids and turbulence</td><td>\(\rho\), \(\eta\), \(L\) (all differently)</td><td><strong>Re, Ma, Pr, Fr, We, St, the \(-5/3\) law</strong></td></tr>
<tr><th class="mid">14</th><td>phase transitions</td><td>──</td><td><strong>critical exponents, \(\Delta\)</strong> (but <em>the weight table itself gets error bars</em>)</td></tr>
<tr><th class="mid">15</th><td>chemistry and biology</td><td>mass, length, metabolic rate, lifespan</td><td><strong>Arrhenius factor, lifetime heartbeats, genetic information</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0">The left column is <strong>entirely dimensionful</strong>; the right column <strong>entirely dimensionless</strong>.<br>
Across nine different fields, not one exception.</p>
</div>

<h2><span class="n">02</span>A map of the weights</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Weight</th><th class="mid">In this picture</th><th>What lives there</th></tr></thead>
<tbody>
<tr><th class="mid">\(+3\)</th><td class="mid">\(\times a^3\)</td><td>number density</td></tr>
<tr><th class="mid">\(+2\)</th><td class="mid">\(\times a^2\)</td><td>area, \(1/G\)</td></tr>
<tr><th class="mid">\(+1\)</th><td class="mid">\(\times a\)</td><td>length, time, wavelength, Bohr radius, Compton wavelength, lifespan, kinematic viscosity, Kolmogorov length</td></tr>
<tr class="hi"><th class="mid">\(0\)</th><td class="mid"><strong>invariant</strong></td><td><strong>velocity, \(c\), \(\hbar\), \(e\), \(\alpha\), \(\alpha_G\), entropy, bits, phase, every ratio, every exponent</strong></td></tr>
<tr><th class="mid">\(-1\)</th><td class="mid">\(\div a\)</td><td>mass, energy, temperature, frequency, gravitational acceleration, Lyapunov exponent, dissipation rate</td></tr>
<tr><th class="mid">\(-2\)</th><td class="mid">\(\div a^2\)</td><td>curvature \(R\), metabolic rate, tidal force</td></tr>
<tr><th class="mid">\(-3\)</th><td class="mid">\(\div a^3\)</td><td>viscosity, surface tension</td></tr>
<tr><th class="mid">\(-4\)</th><td class="mid">\(\div a^4\)</td><td>energy density, mass density, pressure</td></tr>
</tbody>
</table>
</div>

<p>(The "in this picture" column is written in the direction \(\tilde X=a^{-w}X\). A length of weight \(+1\) shrinks as \(\div a\); a mass of weight \(-1\) grows as \(\times a\) — <em>sign and direction are opposite, which is always the confusing part</em>.)</p>

<div class="fig">
<p class="cap">Figure: the map of weights. Drag back in time and <strong>only the weight-0 column stays still</strong>; the others scatter as \(a^{-w}\) — and only the still column is observable.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Which epoch, \(\log_{10}a\) (right edge = today)<input id="sa" type="range" min="-2000" max="0" value="-800" step="1"></label>
  <span class="val" id="va">a = 0.158</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1a3a3a"></i>dimensionful (moves)</span>
  <span><i class="swatch" style="background:#9a5a2a"></i>weight 0 (does not move = physics)</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>Where it helps, and where it is powerless</h2>

<div class="seven">
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>Helps: where dimensionful quantities are the protagonists</strong><span>cosmology and gravity. Expansion, curvature, \(G\), mass scales — change the notation and <em>the equations shorten and the view changes</em> (Episode 4: distances and ages in closed form)</span></div></div>
<div class="row"><div class="mk">△</div><div class="txt"><strong>Neutral: where dimensionless and dimensionful mix</strong><span>quantum mechanics, atoms, heat. Good <em>training in separating the invariant from the moving</em>, but no new conclusions</span></div></div>
<div class="row"><div class="mk">✗</div><div class="txt"><strong>Powerless: where everything is dimensionless from the start</strong><span>fluid similarity laws, critical phenomena, information theory, biological scaling. <em>The tool gives no information at all</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>A conformal transformation is a tool that touches only "size".</strong><br>
So it is powerful where size is the protagonist and powerless where shape is.<br>
<em>And that boundary is not a defect of the tool but its very definition.</em></p>
</div>

<h2><span class="n">04</span>Except that the weight table itself gets error bars</h2>

<p>The proviso found in Episode 14 belongs here. §02's table is <strong>a classical approximation built by dimensional analysis</strong>. In field theory \(\Delta=\Delta_{\text{classical}}+\gamma\), and \(\gamma\) is an object of measurement — \(\gamma_\sigma=0.0181489(10)\) in the 3D Ising model, seven digits.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Layer</th><th>Does it break?</th><th class="mid">Why</th></tr></thead>
<tbody>
<tr><th>Measured dimensionless quantities (ratios, exponents, bits)</th><td>no</td><td class="mid">they are observables</td></tr>
<tr class="hi"><th>The values of the weights themselves</th><td><strong>yes (quantum corrections)</strong></td><td class="mid">Episode 14, \(\gamma_\sigma\)</td></tr>
<tr><th>Geometric weights (length, time)</th><td>no</td><td class="mid">they define the metric</td></tr>
</tbody>
</table>
</div>

<p>So precisely — <em>not "safe because dimensionless" but "safe because observable"</em>. Part V digs into the places where this distinction bites (anomalies, ghosts, rotating spacetimes).</p>

<h2><span class="n">05</span>The map so far, with Part I</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Part</th><th>What it did</th><th class="mid">Conclusion</th></tr></thead>
<tbody>
<tr><th class="mid">I</th><td>build the notation (Episodes 1–6)</td><td class="mid">\(c\cdot t=\)const is <strong>notation</strong>, not a model</td></tr>
<tr class="hi"><th class="mid">II</th><td>substitute it into every equation in reach (Episodes 7–16)</td><td class="mid">everywhere, <strong>only one thing moves</strong>. It touches only size</td></tr>
<tr><th class="mid">III</th><td>measure as information (Episodes 17–26)</td><td class="mid">to come</td></tr>
</tbody>
</table>
</div>

<div class="caveat">
<span class="tag">The honest line — about Part II as a whole</span>
<p style="margin:0 0 10px"><strong>① Part II derived no new physics whatsoever.</strong> All it did was rewrite known laws in a different notation and count what moves and what does not. <em>The reason it still seems worth doing is that the inventory "what does not move = physics" was confirmed without exception across nine fields.</em></p>
<p style="margin:0 0 10px"><strong>② The "moved / did not move" classification is for rewriting the whole universe at once.</strong> Fixed laboratory conditions (a liquid of given viscosity, a thermostat, an external field) do not transform by themselves — the caveat repeated in Episodes 8 ①, 13 ① and 15 ③.</p>
<p style="margin:0 0 10px"><strong>③ The sign convention for weights is a convention.</strong> This series takes \(\tilde X=\Omega^{w}X\) (\(\Omega=1/a\)), with lengths at \(w=+1\) and masses at \(-1\). Other sources use the opposite sign, or write \(\Delta=-w\) — <em>always check the convention before comparing</em>.</p>
<p style="margin:0"><strong>④ The "helps / powerless" line is this series' own assessment.</strong> There are fields — conformal field theory above all — where dimensionless quantities are the protagonists and conformal transformations are nonetheless decisive (Extra 6 of the previous series); there it is <em>invariance under the transformation (a symmetry), not the transformation itself</em>, that does the work. What is called "powerless" here is <strong>this notation, the operation of rewriting by a Weyl transformation</strong>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (a wrap-up of Part II)</p>
<ol>
<li>What do all the quantities that "moved" in Part II have in common?
<details><summary>Show the answer</summary><div class="ans"><strong>They are all dimensionful.</strong> \(G\), the Bohr radius, temperature, \(\rho_\Lambda\), viscosity, body mass — across nine fields, not one exception. Conversely, everything that did not move is dimensionless.</div></details></li>

<li>Name three quantities of weight \(+1\) and three of weight \(-1\).
<details><summary>Show the answer</summary><div class="ans">\(+1\) (\(\div a\)): length, time, wavelength, Bohr radius, lifespan, Kolmogorov length. \(-1\) (\(\times a\)): mass, energy, temperature, frequency, gravitational acceleration, Lyapunov exponent. <em>Sign and direction are opposite, which is where confusion creeps in.</em></div></details></li>

<li>In what kind of field is this notation powerless, and why?
<details><summary>Show the answer</summary><div class="ans"><strong>Fields already written dimensionlessly</strong> — fluid similarity laws, critical phenomena, information theory, biological scaling. The tool touches only "size", so where nothing but dimensionless quantities appear it gives no information (Episode 13). <em>Not a defect but the tool's definition.</em></div></details></li>

<li>Is "safe because dimensionless" an accurate statement?
<details><summary>Show the answer</summary><div class="ans">No. As Episode 14 showed, <strong>the values of the weights themselves take quantum corrections (anomalous dimensions)</strong>, measured to seven digits as \(\gamma_\sigma=0.0181489\) in the 3D Ising model. Precisely: <em>"safe because observable"</em> — measured dimensionless quantities do not move, but classically predicted weights can be wrong.</div></details></li>

<li>(Harder) Did Part II produce new physics? Then what was it for?
<details><summary>Show the answer</summary><div class="ans"><strong>None at all.</strong> It rewrote known laws in a different notation and counted what moves. Its value, if any, is that <em>the inventory "what does not move = physics" held without exception across nine fields from gravity to biology</em> — and that <strong>the tool's range of application was measured precisely</strong>. It gives the previous series' decision procedure an actual service record.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — only one thing ever moved</h2>
<p>Part II put the same notation into nine fields: gravity, quantum mechanics, atoms, heat and information, light, the vacuum, fluids, phase transitions, chemistry and biology. The result always had the same shape — <strong>everything that moved was dimensionful, everything that did not was dimensionless</strong>. Across nine fields, not one exception.</p>
<p>The map of weights is complete too: number density at \(+3\); length, time and lifespan at \(+1\); velocity, \(\hbar\), entropy and every ratio at \(0\); mass, energy and temperature at \(-1\); energy density at \(-4\). <strong>And only the \(0\) column is observable.</strong></p>
<p>What became clearest was <em>the tool's range</em>. A conformal transformation touches only "size", so it is <strong>powerful where size is the protagonist (cosmology, gravity) and completely powerless where shape is (fluids, critical phenomena, information, biology)</strong>. Not a defect but the definition. With the same force that collapsed cosmology into "one mass" in Episode 4, Episode 13's Navier–Stokes equations did not collapse by a single character.</p>
<p>One proviso — as Episode 14 found, <strong>the weight table itself is a classical approximation</strong> carrying an error bar of \(\gamma_\sigma=0.0181489(10)\). So precisely, not "safe because dimensionless" but <em>"safe because observable"</em>. Part V takes up the places where that distinction bites.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 17 (Part III begins)</span>
Part III measures <strong>as information</strong>. First, communication. The CMB is uniform to \(\Delta T/T\sim10^{-5}\) across \(10^4\) causally disconnected patches. In information terms: <em>\(10^4\) nodes that have exchanged not one message agree to 17 bits</em>. In distributed systems this is held to be impossible. \(c\cdot t=\text{const}\) is the only expansion law that never adds nodes, so in principle it does not have this problem — <strong>or it would not have, until you put the radiation back in.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sa=document.getElementById('sa'), va=document.getElementById('va'), ro=document.getElementById('ro');
  var X0=54, X1=700, YB=250;
  var COLS=[[3,'number density'],[2,'area'],[1,'length, time'],[0,'ratios, exponents, bits'],[-1,'mass, temperature'],[-2,'curvature'],[-3,'viscosity'],[-4,'density, pressure']];

  function draw(){
    var la=parseInt(sa.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);

    var maxexp=4*Math.abs(la);
    var scale=Math.min(46, 150/Math.max(maxexp,1));

    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.textAlign='right';
    for(var e=-8;e<=8;e+=2){
      var y=YB-e*scale;
      if(y<24||y>YB+8) continue;
      g.strokeStyle=(e===0?'#c2d0d0':'#eef3f3'); g.lineWidth=(e===0?1.6:1);
      g.beginPath(); g.moveTo(X0-6,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#8fa3a3'; g.fillText(e===0?'×1':'10'+e, X0-10, y+4);
    }

    var n=COLS.length, w=62, gap=(X1-X0-n*w)/(n+1);
    for(var i=0;i<n;i++){
      var wt=COLS[i][0], ex=-wt*la;
      var x=X0+gap+(w+gap)*i, h=ex*scale;
      var zero=(wt===0);
      g.fillStyle=zero?'#9a5a2a':'#1a3a3a';
      g.globalAlpha=zero?0.95:0.8;
      if(zero) g.fillRect(x, YB-3, w, 6);
      else g.fillRect(x, h>=0? YB-h : YB, w, Math.abs(h));
      g.globalAlpha=1;
      g.fillStyle=zero?'#7a4418':'#12292a'; g.textAlign='center';
      g.font='bold 12px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.fillText((wt>0?'+':'')+wt, x+w/2, YB+20);
      g.font='10px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.fillStyle=zero?'#9a6a3a':'#5a7070';
      var lab=COLS[i][1];
      var parts=lab.split(', ');
      if(parts.length>1){ g.fillText(parts[0], x+w/2, YB+36); g.fillText(parts.slice(1).join(', '), x+w/2, YB+48); }
      else g.fillText(lab, x+w/2, YB+36);
      g.font='10px sans-serif'; g.fillStyle=zero?'#7a4418':'#6a8080';
      g.fillText('×10'+(ex>=0?'+':'')+ex.toFixed(1), x+w/2, YB-Math.max(h,0)-8);
    }

    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillStyle='#5a7070'; g.textAlign='center';
    g.fillText('weight w  ── the factor here is a^(−w)', (X0+X1)/2, YB+76);
    g.fillStyle='#9a5a2a'; g.font='bold 12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText('only this column is observable', X0+gap+(w+gap)*3+w/2, YB+64);

    var a=Math.pow(10,la);
    va.textContent='a = '+(a<0.01? a.toExponential(2) : a.toFixed(3));
    ro.textContent='a = '+va.textContent+' (z = '+(1/a-1).toPrecision(3)+')　'+
      'length ×10'+(-la).toFixed(1)+'　mass ×10'+(la).toFixed(1)+'　density ×10'+(4*la).toFixed(1)+
      '　→　the weight-0 column stays at ×1.000';
  }
  sa.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-16-partII.html', acc='#1a3a3a', ops='#9a5a2a',
      title='Only one thing ever moves ── c·t = const, That Clicks, Episode 16 (Part II wrap-up)',
      ep='EPISODE 16 ／ Part II wrap-up',
      eyebrow='Across nine fields, not one exception',
      h1='Only one thing<br>ever moves',
      sub='From gravity to biology, the same notation, counting what moves.<br><em>Everything that moved was dimensionful; everything that did not was dimensionless.</em>',
      byline_l='What you need: the previous fifteen episodes',
      byline_r='it touches only "size"',
      body=BODY + '\n\n<p class="foot">This document is Episode 16 of "c·t = const, That Clicks" (Part II wrap-up), written for physics-minded high-school and university readers. It summarises Episodes 7–15 and contains no new calculations — see the endnotes of each episode for its numbers and sources. The weight convention is \\(\\tilde X=\\Omega^{w}X\\) (\\(\\Omega=1/a\\)), with lengths and times at \\(w=+1\\), mass, energy and temperature at \\(-1\\), and \\(c,\\hbar,e,\\alpha\\) and all dimensionless quantities at \\(0\\) — <strong>other sources use the opposite sign or write \\(\\Delta=-w\\), so the convention must be checked before comparing</strong>. The "moved / did not move" classification applies to rewriting the whole universe at once and not to fixed laboratory conditions. The weight table is a classical approximation from dimensional analysis; in field theory an anomalous dimension is added, \\(\\Delta=\\Delta_{\\text{classical}}+\\gamma\\) (Episode 14; \\(\\gamma_\\sigma=0.0181489(10)\\) for the 3D Ising model) — so the accurate statement is "safe because observable", not "safe because dimensionless". The "helps / powerless" line is this series\' own assessment; there are fields such as conformal field theory where dimensionless quantities are the protagonists and conformal <em>invariance</em> is nonetheless decisive (Extra 6 of the previous series) — what is called powerless here is <strong>the operation of rewriting by a Weyl transformation</strong>. <strong>Part II derives no new physics.</strong> Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination and conflicts with nucleosynthesis when extrapolated into the early universe (Lewis, Barnes &amp; Kaushik 2016). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the epoch and only the weight-0 column stays put. "Show the answer" opens each solution.')
