# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 7 substituted into gravity. This time, quantum mechanics. The conclusion first: <strong>the Schrödinger equation is not rewritten by a single character</strong> — except that the mass becomes \(m(t)=m_0\,t/t_0\). And out of that comes something rather hard to believe. <em>A free wave packet spreads not in proportion to time, but only logarithmically.</em> Integrate it up and you get one line: <strong>matter stops being able to walk; light keeps walking</strong>.</p>

<h2><span class="n">01</span>First, check that the equation keeps its form</h2>

<div class="calc">
<span class="tag">What we are transforming</span>
$$i\hbar\frac{\partial\psi}{\partial t}=\left[-\frac{\hbar^2}{2m}\nabla^2+V\right]\psi$$
</div>

<p>The weight of \(\psi\) is fixed by normalisation: \(\int|\psi|^2d^3x=1\) with \(d^3x\) of weight \(+3\) makes \(|\psi|^2\) weight \(-3\), so \(\psi\) is \(-3/2\). The rest is counting.</p>

<div class="calc">
<span class="tag">Counting the weight on both sides</span>
<p class="lbl">Left side \(i\hbar\,\partial\psi/\partial t\)</p>
$$\underbrace{0}_{\hbar}+\underbrace{(-3/2)}_{\psi}+\underbrace{(-1)}_{\partial/\partial t}=-\frac52$$
<p class="lbl">Right side \(\hbar^2\nabla^2\psi/2m\)</p>
$$\underbrace{0}_{\hbar^2}-\underbrace{(-1)}_{1/m}+\underbrace{(-2)}_{\nabla^2}+\underbrace{(-3/2)}_{\psi}=+1-2-\frac32=-\frac52$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0">Both sides come to \(-5/2\). <strong>The Schrödinger equation is unchanged to the letter in this picture too.</strong><br>
The only thing that changes is the mass inside it — \(m(t)=m_0\,t/t_0\).</p>
</div>

<p>This is the quantum-mechanical version of Episode 4's "delete everything deletable and one mass is left". <em>Quantum mechanics has nothing but mass for a conformal transformation to catch.</em></p>

<h2><span class="n">02</span>The heart — the wave packet spreads only logarithmically</h2>

<p>Take a free particle. With no force the momentum is conserved and \(v=p/m\). But \(m\) grows in proportion to \(t\), so —</p>

<div class="calc">
<span class="tag">Two lines</span>
$$v(t)=\frac{p}{m_0\,t/t_0}=\frac{p\,t_0}{m_0\,t}\ \propto\ \frac{1}{t}$$
<p class="lbl">integrating</p>
$$\Delta x(t)=\int v\,dt\ \propto\ \ln t$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th class="mid">Standard picture</th><th class="mid">This picture</th></tr></thead>
<tbody>
<tr><th>Mass</th><td class="mid">constant</td><td class="mid">\(\propto t\)</td></tr>
<tr><th>Free particle velocity</th><td class="mid">constant</td><td class="mid">\(\propto 1/t\)</td></tr>
<tr class="hi"><th>Wave packet spreading</th><td class="mid">\(\Delta x\propto t\)</td><td class="mid"><strong>\(\Delta x\propto\ln t\)</strong></td></tr>
</tbody>
</table>
</div>

<p>You cannot notice this in a laboratory. \(\dot m/m=H_0\) means one e-fold in 13.8 billion years, utterly negligible for an electron wave packet that spreads in \(10^{-14}\) s. <strong>It matters only when integrated on cosmic scales.</strong></p>

<h2><span class="n">03</span>Integrating up — the reach of matter is finite</h2>

<p>A particle set moving at time \(t_1\) with velocity \(v_1\), travelling <em>forever</em> after: how far does it get in comoving coordinates?</p>

<div class="calc">
<span class="tag">Matter and light, integrated side by side</span>
<p class="lbl">Anything with mass (velocity decaying as \(1/a\))</p>
$$\Delta\chi=\int_{t_1}^{\infty}\frac{v_1(t_1/t)}{t/t_1}\,dt=v_1t_1^2\int_{t_1}^{\infty}\frac{dt}{t^2}=\boxed{\,v_1t_1\,}$$
<p class="lbl">Light</p>
$$\Delta\chi=\int_{t_1}^{\infty}\frac{c\,dt}{t/t_1}=c\,t_1\ln\frac{t}{t_1}\ \longrightarrow\ \infty$$
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>Matter stops being able to walk. Light keeps walking.</strong><br>
The comoving reach of anything massive saturates at \(v_1t_1\) — <em>the distance covered in the first Hubble time is the ceiling for all eternity</em>.</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>What sets out</th><th class="mid">Initial speed</th><th class="mid">Departure</th><th class="mid">Reach for all eternity, \(v_1t_1\)</th></tr></thead>
<tbody>
<tr class="hi"><th>Hydrogen atom at recombination</th><td class="mid">5 km/s</td><td class="mid">380,000 yr</td><td class="mid"><strong>1.9 parsecs</strong></td></tr>
<tr><th>Galaxy (today's peculiar velocity)</th><td class="mid">600 km/s</td><td class="mid">today</td><td class="mid">8.5 Mpc</td></tr>
<tr><th>Hot electron (today)</th><td class="mid">1000 km/s</td><td class="mid">today</td><td class="mid">14.1 Mpc</td></tr>
<tr><th>Light (today)</th><td class="mid">\(c\)</td><td class="mid">today</td><td class="mid"><strong>infinite</strong> (\(4230\,\mathrm{Mpc}\times\ln(t/t_0)\))</td></tr>
</tbody>
</table>
</div>

<p>The first row is the one that bites. <strong>A hydrogen atom present at recombination can move only 2 comoving parsecs in the entire history of the universe.</strong> The pattern burned into the CMB stays frozen where it is, with nothing left but gravitational growth — and this integral is why.</p>

<div class="aside">
<span class="tag">Set out at light speed and you are still overtaken</span>
Even with \(v_1=c\) the reach saturates at \(c\,t_1\) (a massive particle cannot actually reach \(c\); take it as a ceiling). Light departing at the same moment goes \(c\,t_1\ln(t/t_1)\). It overtakes at \(\ln(t/t_1)=1\) — that is, <strong>when the universe is \(e=2.72\) times older</strong>. <em>However fast you set out, light leaves you behind before a single order of magnitude has passed.</em>
</div>

<div class="fig">
<p class="cap">Figure: how far a particle departing today ever reaches, in comoving distance. <strong>The matter curve always saturates; the light curve keeps climbing.</strong> The slider changes the initial speed, which moves only the height of the ceiling.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Initial speed \(v_1\) (log; right edge is \(c\))<input id="sv" type="range" min="0" max="1000" value="270" step="1"></label>
  <span class="val" id="vv">600 km/s</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1d3f56"></i>anything with mass (saturates)</span>
  <span><i class="swatch" style="background:#9a5a1e"></i>light (keeps climbing)</span>
  <span><i class="swatch" style="background:#94a3ac"></i>ceiling height \(v_1t_0\)</span>
</div>
</div>

<p>Push the slider all the way to \(c\) and the blue line still goes flat. <em>Whether it saturates is not a question of speed</em> — it is a question of having mass. With mass the velocity decays as \(1/a\) and the integral converges; without mass it does not decay and the integral diverges logarithmically.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>A table of what moves and what does not</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Weight</th><th class="mid">In this picture</th></tr></thead>
<tbody>
<tr class="hi"><th>Uncertainty \(\Delta x\Delta p\ge\hbar/2\)</th><td class="mid">\(0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr class="hi"><th>Action \(S/\hbar\)</th><td class="mid">\(0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr class="hi"><th>Tunnelling probability \(e^{-2\int\kappa\,dx}\)</th><td class="mid">\(0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>de Broglie wavelength \(h/p\)</th><td class="mid">\(+1\)</td><td class="mid">\(\div a\)</td></tr>
<tr><th>Compton wavelength \(\hbar/mc\)</th><td class="mid">\(+1\)</td><td class="mid">\(\div a\)</td></tr>
<tr><th>Thermal de Broglie wavelength \(h/\sqrt{2\pi mk_BT}\)</th><td class="mid">\(+1\)</td><td class="mid">\(\div a\)</td></tr>
<tr><th>Energy levels</th><td class="mid">\(-1\)</td><td class="mid">\(\times a\)</td></tr>
</tbody>
</table>
</div>

<p>Savour the third row. <strong>The tunnelling probability is completely invariant.</strong> Inside the exponent, \(\int\kappa\,dx\) has \(\kappa=\sqrt{2m(V-E)}/\hbar\) of weight \(-1\) and \(dx\) of weight \(+1\), so the product is \(0\). Therefore —</p>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0">The rate at which the Sun burns, the half-life of \(\alpha\) decay, the image in a scanning tunnelling microscope —<br>
<strong>none of them change at all</strong> in this picture. All are fixed by dimensionless exponents alone.</p>
</div>

<h2><span class="n">05</span>The reveal — the world grows more classical with time</h2>

<p>So much is invariant, yet one dimensionless quantity moves steadily. It is the one from Episode 6 of the previous series.</p>

<div class="calc">
<span class="tag">The dimensionless quantity that moves</span>
$$N=\frac{\text{size of the system considered}}{\text{Compton wavelength}}=\frac{mc^2t}{\hbar}$$
<p class="lbl">today</p>
$$N(\text{electron})=3.38\times10^{38},\qquad N(\text{hydrogen atom})=6.21\times10^{41}$$
</div>

<p>The standard picture reads this as "\(N\) grows because the universe grows". Here <strong>the universe is not expanding</strong>, so the reading changes — <em>\(N\) grows because the Compton wavelength is shrinking</em>. The ruler fattens and the quantum graininess gets finer.</p>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>The universe becomes more classical with time.</strong><br>
\(N\propto t\) is a scale for how well a classical description works, and it alone cannot be moved by a conformal transformation.<br>
── It is the ratio Episode 6 of the previous series meant by "the geometry vanished, the ratio survived".</p>
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① The Schrödinger equation is a non-relativistic approximation.</strong> The weights match on both sides provided \(V\) is transformed along with everything else as an energy (weight \(-1\)). An externally fixed potential (laboratory electrodes, say) does not transform by itself, and the story changes — what is treated here is <em>rewriting the whole universe at once</em>.</p>
<p style="margin:0 0 10px"><strong>② "The packet spreads only as \(\ln t\)" is a statement about cosmological timescales.</strong> In the laboratory \(\dot m/m=H_0\simeq10^{-18}\)/s, beyond any measurement. And this is <em>the same fact the standard picture states as "peculiar velocities decay as \(1/a\)"</em> — not new physics.</p>
<p style="margin:0 0 10px"><strong>③ The reach \(v_1t_1\) assumes \(a\propto t\) at all epochs.</strong> In the real universe (radiation → matter → \(\Lambda\)) the integral and its coefficients change — though the qualitative conclusion, <em>massive things converge and light diverges, holds for any decelerating expansion</em>. Read the table as an order-of-magnitude argument.</p>
<p style="margin:0 0 10px"><strong>④ The 5 km/s for a recombination-era hydrogen atom is the thermal speed at \(T=3000\) K.</strong> Real baryons move collectively on acoustic waves, so treating them as free single particles is a coarse approximation.</p>
<p style="margin:0"><strong>⑤ The invariance of the tunnelling probability concerns the exponent in the WKB approximation.</strong> It is not a claim of complete invariance including prefactors and resonance conditions (though those too are invariant for the same reason wherever they can be written as dimensionless ratios).</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Why does \(\psi\) have weight \(-3/2\)?
<details><summary>Show the answer</summary><div class="ans">From normalisation \(\int|\psi|^2d^3x=1\). Since \(d^3x\) has weight \(+3\), \(|\psi|^2\) has \(-3\), so \(\psi\) has \(-3/2\). <em>The weight of the wave function is not chosen — normalisation fixes it.</em></div></details></li>

<li>How does a free particle's velocity change here, and what does that give for the wave packet?
<details><summary>Show the answer</summary><div class="ans">No force, so \(p\) is conserved; mass \(\propto t\) gives \(v=p/m\propto1/t\). Integrating, \(\Delta x=\int v\,dt\propto\ln t\). <strong>Logarithmic, not linear.</strong></div></details></li>

<li>Find the eternal comoving reach of a particle set moving at \(t_1\) with velocity \(v_1\).
<details><summary>Show the answer</summary><div class="ans">\(\Delta\chi=\int_{t_1}^\infty v_1(t_1/t)/(t/t_1)\,dt=v_1t_1^2\int_{t_1}^\infty dt/t^2=v_1t_1\). <strong>The distance covered in the first Hubble time is the eternal ceiling.</strong> Only light diverges, as \(\int c\,dt/a\propto\ln t\).</div></details></li>

<li>Why is the tunnelling probability invariant?
<details><summary>Show the answer</summary><div class="ans">Because the exponent \(\int\kappa\,dx\) is dimensionless: \(\kappa=\sqrt{2m(V-E)}/\hbar\) has weight \(-1\) (inverse length) and \(dx\) has \(+1\), summing to \(0\). <em>The Sun's burning rate and \(\alpha\)-decay half-lives are untouched in this picture.</em></div></details></li>

<li>(Harder) With so much invariant, why does \(N=mc^2t/\hbar\) move?
<details><summary>Show the answer</summary><div class="ans">\(N\) is "size of system ÷ Compton wavelength", and <strong>numerator and denominator draw their length from different places</strong> — \(t\) is the length the universe brings, \(\hbar/mc\) the length the particle brings. Strictly, in \(N=mc^2t/\hbar\) the \(m\) (\(-1\)) and \(t\) (\(+1\)) cancel, so \(N\) is invariant; but <em>the fact that its value grows with time</em> is the same in any gauge — as Episode 6 of the previous series confirmed by deriving the same formula from both pictures. <strong>Being invariant and being constant in time are different things.</strong></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — matter stops walking, light keeps walking</h2>
<p>Substituted into the Schrödinger equation, both sides come to weight \(-5/2\) and <strong>the equation is unchanged to the letter</strong>. Only the mass changes — \(m(t)=m_0t/t_0\). It is the quantum-mechanical version of Episode 4's "delete everything and one mass is left".</p>
<p>But that one thing bites. A free particle conserves momentum, so \(v=p/m\propto1/t\), and <strong>the packet spreads as \(\Delta x\propto\ln t\), not \(\propto t\)</strong>. Integrated up, the comoving reach of anything massive <em>saturates</em> at \(v_1t_1\) — the distance covered in the first Hubble time is the eternal ceiling. For a hydrogen atom at recombination, <strong>1.9 parsecs</strong>. That integral is why the CMB pattern stays frozen where it is. Light meanwhile diverges as \(c\,t_1\ln(t/t_1)\). <em>Set out at light speed and you are overtaken once the universe is \(e=2.72\) times older.</em></p>
<p>We also counted the invariants: uncertainty, the action \(S/\hbar\), and <strong>tunnelling</strong> — since the exponent \(\int\kappa\,dx\) is dimensionless, the Sun's burning rate and \(\alpha\)-decay half-lives do not shift at all. What moves is de Broglie and Compton wavelengths and energy levels, differing only in whether they are a length or an energy.</p>
<p>And one quantity keeps rising: \(N=mc^2t/\hbar\) (\(3.4\times10^{38}\) for an electron). The standard picture says it rises because the universe grows; here it rises <strong>because the Compton wavelength shrinks</strong>. <em>The universe is not expanding so much as growing coarse relative to the quantum graininess</em> — the world becomes more classical with time.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 9</span>
Quantum mechanics passed, so next we substitute into <strong>the atom</strong>. Atoms shrink as \(1/t\) here, and yet spectral lines do not blur at all. Why? Compute the <em>adiabatic parameter</em> and for hydrogen it is \(\hbar H/E_{\rm Ry}=1.1\times10^{-34}\). It is so many orders too slow that not a single transition is induced. This is precisely the inverse of <strong>the argument with which Einstein killed Weyl's theory in 1918</strong> (the second clock effect blurring spectral lines) — one number says why the modern conformal transformation is not cut by the same blade.
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sv=document.getElementById('sv'), vv=document.getElementById('vv'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=318;
  var c=299792458.0, t0=4.3536e17, Mpc=3.0857e22;
  var xmin=0, xmax=6;
  var ymin=-2, ymax=5;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function lg(v){ return Math.log(v)/Math.LN10; }

  function draw(){
    var f=parseInt(sv.value,10)/1000;
    var v=1e3*Math.pow(c/1e3, f);
    var sat=v*t0/Mpc;
    var cl =c*t0/Mpc;

    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=-2;e<=5;e++){
      var y=py(e);
      g.strokeStyle='#eef1f3'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#93a2ab';
      g.fillText((e<0?'10⁻'+Math.abs(e):(e===0?'1':'10'+e))+' Mpc', X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=6;q++){
      var x=px(q);
      g.strokeStyle='#f5f7f9'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#93a2ab'; g.fillText(q===0?'now':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#c3ced5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    if(lg(sat)>ymin&&lg(sat)<ymax){
      g.strokeStyle='#94a3ac'; g.lineWidth=1.6; g.setLineDash([6,5]);
      g.beginPath(); g.moveTo(X0,py(lg(sat))); g.lineTo(X1,py(lg(sat))); g.stroke();
      g.setLineDash([]);
    }

    g.strokeStyle='#1d3f56'; g.lineWidth=3.4; g.beginPath();
    var first=true;
    for(var i=0;i<=400;i++){
      var lx=xmin+(xmax-xmin)*i/400, T=Math.pow(10,lx);
      var d=sat*(1-1/T);
      if(d<=0){ first=true; continue; }
      var yy=lg(d);
      if(yy<ymin){ first=true; continue; }
      if(first){ g.moveTo(px(lx),py(Math.min(yy,ymax))); first=false; }
      else g.lineTo(px(lx),py(Math.min(yy,ymax)));
    }
    g.stroke();

    g.strokeStyle='#9a5a1e'; g.lineWidth=3.4; g.beginPath();
    first=true;
    for(var i=0;i<=400;i++){
      var lx=xmin+(xmax-xmin)*i/400, T=Math.pow(10,lx);
      var d=cl*Math.log(T);
      if(d<=0){ first=true; continue; }
      var yy=lg(d);
      if(yy<ymin){ first=true; continue; }
      if(first){ g.moveTo(px(lx),py(Math.min(yy,ymax))); first=false; }
      else g.lineTo(px(lx),py(Math.min(yy,ymax)));
    }
    g.stroke();

    g.fillStyle='#1d3f56'; g.textAlign='right';
    if(lg(sat)>ymin+0.3&&lg(sat)<ymax-0.2)
      g.fillText('matter (ceiling '+(sat<0.01?sat.toExponential(1):sat.toPrecision(3))+' Mpc)', X1-8, py(lg(sat))-9);
    g.fillStyle='#9a5a1e'; g.textAlign='left';
    g.fillText('light (keeps climbing)', px(4.1), py(lg(cl*Math.log(Math.pow(10,4.1))))-10);

    g.fillStyle='#6b7c86'; g.textAlign='center';
    g.fillText('elapsed age of the universe  t / t₀', (X0+X1)/2, Y1+36);

    var vk=v/1e3;
    vv.textContent = (v>0.5*c) ? (v/c).toFixed(3)+' c' : (vk>1e4? (vk/1e3).toPrecision(3)+'  thousand km/s' : vk.toPrecision(3)+' km/s');
    var overtake=Math.exp(v/c);
    ro.textContent='initial speed '+vv.textContent+
      '　→　eternal reach v₁t₀ = '+(sat<0.01?sat.toExponential(2):sat.toPrecision(3))+' Mpc'+
      '　/　light gets there at t = '+overtake.toPrecision(3)+' t₀'+
      '　/　matter stops there; light goes on without bound';
  }
  sv.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-08-quantum.html', acc='#1d3f56', ops='#9a5a1e',
      title='Substituting into quantum mechanics ── c·t = const, That Clicks, Episode 8',
      ep='EPISODE 8 ／ The equation does not change a letter. Only the mass does',
      eyebrow='Matter stops being able to walk; light keeps walking',
      h1='Substituting into<br>quantum mechanics',
      sub='The Schrödinger equation keeps its form — with \\(m(t)=m_0\\,t/t_0\\).<br><em>And out of that: a free wave packet spreads only logarithmically.</em>',
      byline_l='What you need: adding up weights, one integral',
      byline_r='\\(\\Delta\\chi=v_1t_1\\) (finite) vs \\(c\\,t_1\\ln(t/t_1)\\) (infinite)',
      body=BODY + '\n\n<p class="foot">This document is Episode 8 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That under a conformal transformation lengths and times carry weight \\(+1\\), mass and energy \\(-1\\), \\(\\hbar\\) and \\(c\\) weight \\(0\\), and that normalisation gives the wave function \\(-3/2\\), is standard. That both sides of the Schrödinger equation come to weight \\(-5/2\\) so the equation keeps its form, and that a free particle\'s velocity decays as \\(v\\propto1/a\\) (the standard redshifting of peculiar velocity), are also standard results. The \\(\\Delta\\chi=v_1t_1\\) — the finiteness of the comoving reach of a massive particle when \\(a\\propto t\\) — together with the divergence of \\(c\\,t_1\\ln(t/t_1)\\) for light and the fact that even a particle setting out at \\(c\\) is overtaken at \\(t=e\\,t_1\\), are calculated here. The table values (1.9 pc for a recombination-era hydrogen atom, 8.5 Mpc for a galaxy, 14.1 Mpc for an electron, \\(c\\,t_0=4230\\) Mpc) are also computed here and <strong>assume \\(a\\propto t\\) at all epochs</strong> — the coefficients change in the real universe, but the conclusion that massive things converge while light diverges holds for any decelerating expansion. The 5 km/s thermal speed at recombination is the \\(T=3000\\) K estimate; real baryons move collectively on acoustic oscillations. The invariance of the tunnelling probability is a claim about the exponent in the WKB approximation. That \\(N=mc^2t/\\hbar\\) takes the same form in both pictures was shown in Episode 6 of the previous series. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination, and conflicts with nucleosynthesis when extrapolated into the early universe (Lewis, Barnes &amp; Kaushik 2016). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the initial speed and the matter curve always flattens. "Show the answer" opens each solution.')
