# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Last episode leaned hardest on "dimensionless means invariant". Today we go to <strong>the one place where that gets shaky</strong> — phase transitions. At a critical point the dimensionless exponents <em>depart from their classical values</em> (anomalous dimensions). And that departure is also <strong>the error in the very weight table this series has used for thirteen episodes</strong>. Better still, it has been measured in the 3D Ising model <em>to seven digits</em>. <strong>The bookkeeping gets error bars.</strong></p>

<h2><span class="n">01</span>The weight table was a classical approximation</h2>

<p>Since Episode 1 we have used a table: length \(+1\), mass \(-1\), velocity \(0\). It is built by <strong>dimensional analysis</strong> — decompose into \(L^{n_L}T^{n_T}M^{n_M}\) and add (as in Episode 13). But in field theory the scaling dimension of an operator is not determined by that alone.</p>

<div class="calc">
<span class="tag">The true weight</span>
$$\Delta=\underbrace{\Delta_{\text{classical}}}_{\text{dimensional analysis}}+\underbrace{\gamma}_{\text{anomalous dimension}}$$
<p class="lbl">As Extra 6 of the previous series showed, \(\Delta\) <em>is</em> the Weyl weight</p>
$$\mathcal{O}\ \longrightarrow\ \Omega^{-\Delta}\mathcal{O}$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>\(\gamma\ne0\) means "the classically counted weight is wrong".</strong><br>
The table this series has used was <em>an approximation that ignored that error</em>.</p>
</div>

<h2><span class="n">02</span>Looking at the size of the error</h2>

<p>The most precisely measured case is the spin operator of the 3D Ising model. A free field would give exactly \(\Delta=(d-2)/2\). It does not.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Dimension \(d\)</th><th class="mid">Free field \((d-2)/2\)</th><th class="mid">Actual \(\Delta_\sigma\)</th><th class="mid">Anomalous \(\gamma_\sigma\)</th><th class="mid">Relative error</th></tr></thead>
<tbody>
<tr><th class="mid">2</th><td class="mid">0</td><td class="mid">0.125 (exact)</td><td class="mid">0.125</td><td class="mid">──</td></tr>
<tr class="hi"><th class="mid">3</th><td class="mid">0.5</td><td class="mid"><strong>0.5181489(10)</strong></td><td class="mid"><strong>0.0181489</strong></td><td class="mid">3.6%</td></tr>
<tr><th class="mid">4</th><td class="mid">1.0</td><td class="mid">1.0</td><td class="mid"><strong>0</strong></td><td class="mid">0%</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0"><strong>In four dimensions the classical weight table is exactly right (\(\gamma=0\)).</strong><br>
Lower the dimension and the error grows — 3.6% in three dimensions, 12.5% in two.</p>
</div>

<p>Four is the <em>upper critical dimension</em>, above which mean-field theory becomes exact. That our spacetime is four-dimensional matters here too — the same place where the Maxwell action was conformally invariant only at \(D=4\) (Episode 11).</p>

<div class="fig">
<p class="cap">Figure: spatial dimension across, anomalous dimension \(\gamma_\sigma\) = <strong>the error in the weight table</strong> up. Circles are known values (exact in 2D, bootstrap in 3D, zero in 4D); the dashed line is the leading \(\varepsilon\)-expansion term. <em>The error vanishes exactly at four dimensions.</em></p>
<canvas id="cv" width="720" height="360"></canvas>
<div class="controls">
  <label>Spatial dimension \(d\)<input id="sd" type="range" min="2000" max="4000" value="3000" step="1"></label>
  <span class="val" id="vd">d = 3.000</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#5c1f3f"></i>anomalous dimension \(\gamma_\sigma\) (known values)</span>
  <span><i class="swatch" style="background:#1f6b4a"></i>leading \(\varepsilon\)-expansion term</span>
  <span><i class="swatch" style="background:#9a8a92"></i>where the classical table is right (\(\gamma=0\))</span>
</div>
</div>

<p>The dashed line (the leading term \(\gamma=\varepsilon^2/108\)) gives only <strong>half</strong> the true value in three dimensions. <em>Estimating the size of the error perturbatively is hard</em> — which is why the seven digits of the next section matter.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>The error has been measured to seven digits</h2>

<p>The conformal bootstrap determines \(\Delta\) without a single dimensionful input (Extra 6 of the previous series). For the 3D Ising model the result is just two numbers.</p>

<div class="calc">
<span class="tag">Two numbers out of zero input</span>
$$\Delta_\sigma=0.5181489(10),\qquad \Delta_\varepsilon=1.412625(10)$$
</div>

<p>Every critical exponent of statistical physics follows from those two. Computed, and set beside experiment and Monte Carlo:</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Exponent</th><th class="mid">From the two \(\Delta\)</th><th class="mid">Experiment / MC</th><th class="mid">What it measures</th></tr></thead>
<tbody>
<tr><th>\(\eta\)</th><td class="mid">0.036298</td><td class="mid">0.0363(2)</td><td class="mid">decay of correlations</td></tr>
<tr><th>\(\nu\)</th><td class="mid">0.629971</td><td class="mid">0.6300(17)</td><td class="mid">divergence of correlation length</td></tr>
<tr><th>\(\alpha\)</th><td class="mid">0.110087</td><td class="mid">0.110(5)</td><td class="mid">divergence of specific heat</td></tr>
<tr><th>\(\beta\)</th><td class="mid">0.326419</td><td class="mid">0.3265(15)</td><td class="mid">shape of the coexistence curve</td></tr>
<tr><th>\(\gamma\)</th><td class="mid">1.237075</td><td class="mid">1.2372(5)</td><td class="mid">divergence of susceptibility</td></tr>
<tr><th>\(\delta\)</th><td class="mid">4.789841</td><td class="mid">4.789(2)</td><td class="mid">critical isotherm</td></tr>
<tr class="hi"><th>\(\alpha+2\beta+\gamma\)</th><td class="mid"><strong>2.0000000000</strong></td><td class="mid">──</td><td class="mid">an identity (independent of \(\Delta\))</td></tr>
</tbody>
</table>
</div>

<p>And since \(\eta=2\gamma_\sigma\) — <strong>the error in the weight table, \(\gamma_\sigma=0.0181489\), is a quantity you can measure in water and magnets</strong>. Water, carbon dioxide and uniaxial magnets all obey this same number at their critical points.</p>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0">This series' <strong>bookkeeping has acquired error bars</strong>.<br>
\(\gamma_\sigma=0.0181489(10)\) — <em>how wrong the weights are, measured to seven digits.</em></p>
</div>

<h2><span class="n">04</span>And yet dimensionless quantities remain invariant</h2>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>What moves: the classically predicted weight</strong><span>what dimensional analysis said was \(\Delta=(d-2)/2\) turns out to be \(0.5181489\) — <em>the prediction was wrong</em></span></div></div>
<div class="row hi"><div class="mk">✓</div><div class="txt"><strong>What does not move: the measured dimensionless quantities</strong><span>critical exponents and \(\Delta\) itself are observables (dimensionless), so a conformal transformation moves neither</span></div></div>
</div>

<p>So <strong>Episode 13's "dimensionless is invariant" stands unchanged</strong>. What collapsed today is something else — <em>the premise that "weights are fixed by dimensional analysis"</em>. A weight is not a settled number: it is <strong>a quantity a theory determines</strong>, and an object of measurement.</p>

<div class="aside">
<span class="tag">The same single thing as Episode 8 of the previous series</span>
An anomalous dimension is the trace anomaly seen <em>operator by operator</em>. Episode 8 of the previous series measured it as "couplings run = conformal symmetry is quantum-broken", via the \(\beta\) function. Extra 6 measured it per operator as \(\Delta=\Delta_{\text{classical}}+\gamma\). <strong>Both are consequences of the scale \(\mu\) that quantisation drags in</strong> — and \(1/137\to1/128\) and \(\gamma_\sigma=0.0181489\) are the same breaking measured in different experiments.
</div>

<h2><span class="n">05</span>So what about the cosmological weights?</h2>

<p>Which raises the question. When Episode 4 said "only mass grows as \(\propto t\)", it took mass to have weight \(-1\). <strong>Does that \(-1\) get an anomalous dimension too?</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>What carries the weight</th><th class="mid">Classical</th><th class="mid">Quantum correction</th></tr></thead>
<tbody>
<tr><th>Spacetime lengths and times (the metric itself)</th><td class="mid">\(+1\)</td><td class="mid">none (it is the definition of the geometry)</td></tr>
<tr><th>Gauge fields, photons</th><td class="mid">\(0\)</td><td class="mid">breaking of order the \(\beta\) function (Episode 11)</td></tr>
<tr class="hi"><th>Field operators (\(\bar\psi\psi\) and the like)</th><td class="mid">classical dimension</td><td class="mid"><strong>gets an anomalous dimension</strong></td></tr>
<tr><th>Measured dimensionless ratios</th><td class="mid">\(0\)</td><td class="mid">none (they are observables)</td></tr>
</tbody>
</table>
</div>

<p>The geometric side (lengths, times) does not move, being definitional. What moves are <strong>field operators</strong> — the quark mass operator has an anomalous dimension and runs. So "mass grows as \(\propto t\)" is, strictly, <em>undetermined until you say at what scale the mass is measured</em>.</p>

<p>But — as Episode 3 of the previous series confirmed — <strong>the observable dimensionless ratios (\(1+z\), the 52.6 of recombination, \(Q/k_BT\)) are the same in every picture and at every scale</strong>. So the conclusions of Episodes 4 through 13 all survive intact.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① The "dimension \(d\)" of critical phenomena is the spatial dimension of statistical mechanics, not the dimension of spacetime.</strong> The upper critical dimension 4 and the \(D=4\) of the Maxwell action are both "4" because both come from a balance of dimensional analysis, but they are <em>not the same phenomenon</em>. They are placed side by side to show the structural similarity.</p>
<p style="margin:0 0 10px"><strong>② \(\Delta_\sigma=0.5181489(10)\) is a conformal bootstrap value</strong> (El-Showk, Simmons-Duffin et al., 2012–2016). The error is numerical and includes estimated systematics. The 2D value \(0.125\) is exact since Onsager; the 4D \(0\) follows from mean-field theory becoming exact.</p>
<p style="margin:0 0 10px"><strong>③ The leading \(\varepsilon\)-expansion term is \(\eta=\varepsilon^2(N+2)/[2(N+8)^2]\)</strong> (\(\varepsilon^2/54\) at \(N=1\)). In three dimensions (\(\varepsilon=1\)) it gives only about half the true value, so higher orders matter — the dashed line is a reference for "what the leading term alone would say".</p>
<p style="margin:0 0 10px"><strong>④ The "experiment / MC" column gives approximate representative values from several measurements and computations, not a single source.</strong> Real fluids and magnets are not exact CFTs; these exponents appear only sufficiently close to the critical point (there are correction terms).</p>
<p style="margin:0"><strong>⑤ §05's "the mass weight gets an anomalous dimension" is a qualitative account.</strong> How it actually enters depends on the renormalisation scheme and on what one calls "mass" (pole mass or \(\overline{\rm MS}\) mass) — continuous with the observation in Extra 4 of the previous series that Koide's relation holds only for pole masses. <em>This document claims only that weights are objects of measurement.</em></p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Restate the anomalous dimension \(\gamma\) in this series' language.
<details><summary>Show the answer</summary><div class="ans"><strong>The error in the weight table.</strong> The gap between the weight predicted by dimensional analysis, \(\Delta_{\text{classical}}\), and the actual weight \(\Delta\): \(\Delta=\Delta_{\text{classical}}+\gamma\). <em>The table used in Episodes 1–13 was an approximation ignoring \(\gamma\).</em></div></details></li>

<li>Find \(\gamma_\sigma\) for the 3D Ising model, given the free-field weight \((d-2)/2\).
<details><summary>Show the answer</summary><div class="ans">\(\gamma_\sigma=\Delta_\sigma-(d-2)/2=0.5181489-0.5=\) <strong>0.0181489</strong>, a 3.6% error. Via \(\eta=2\gamma_\sigma=0.0362978\) it is measurable in water and magnets.</div></details></li>

<li>Why is \(\gamma=0\) in four dimensions?
<details><summary>Show the answer</summary><div class="ans">Because four is the <strong>upper critical dimension</strong>, above which mean-field theory becomes exact and interactions stop affecting the long-distance behaviour. <em>That our spacetime is four-dimensional matters here as it did for the Maxwell action in Episode 11</em> — though, per caveat ①, they are different phenomena wearing the same "4".</div></details></li>

<li>Does this episode contradict Episode 13's "dimensionless is invariant"?
<details><summary>Show the answer</summary><div class="ans">No. <strong>The measured dimensionless quantities (critical exponents, \(\Delta\) itself) are still conformally invariant.</strong> What collapsed is a different premise — <em>that weights are fixed by dimensional analysis</em>. A weight is not a settled number; a theory determines it and experiment measures it.</div></details></li>

<li>(Harder) Why does \(\alpha+2\beta+\gamma=2\) hold independently of \(\Delta\)?
<details><summary>Show the answer</summary><div class="ans">Because the six exponents are functions of two numbers (\(\eta,\nu\)). Substituting, \((2-d\nu)+\nu(d-2+\eta)+\nu(2-\eta)=2\), and \(\nu\), \(\eta\), \(d\) all cancel. <strong>This is not physics but a consequence of six quantities being functions of two</strong> — as Extra 6 of the previous series showed. <em>An identity is not physics</em>, the series' watchword, applies here too (Episodes 7 and 10).</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — the bookkeeping acquired error bars</h2>
<p>The weight table used since Episode 1 was a <strong>classical approximation</strong> built by dimensional analysis. In field theory \(\Delta=\Delta_{\text{classical}}+\gamma\), and \(\gamma\ne0\) means the classically counted weight is wrong. That error has actually been measured.</p>
<p>The 3D Ising spin operator, which a free field would put at \(\Delta=0.5\), sits at <strong>0.5181489(10)</strong> — an offset \(\gamma_\sigma=0.0181489\), 3.6%. In two dimensions it is 12.5% (exactly \(1/8\)), and <strong>exactly zero in four</strong> (the upper critical dimension). The leading \(\varepsilon\)-expansion term gives only half the 3D value, so these seven digits are out of perturbation theory's reach.</p>
<p>And through \(\eta=2\gamma_\sigma\), that error is <em>measurable at the critical point of water and magnets</em>. Two \(\Delta\)s give all six critical exponents, matching experiment. And \(\alpha+2\beta+\gamma=2.0000000000\) is an identity independent of \(\Delta\) — <strong>an identity is not physics</strong>, the same verdict as Episodes 7 and 10.</p>
<p>What matters is that none of this contradicts Episode 13's "dimensionless is invariant". <em>Measured dimensionless quantities are still invariant.</em> What collapsed was <strong>the premise that weights are fixed by dimensional analysis</strong>. A weight is not a settled number: a theory determines it and experiment measures it — <em>this series' own bookkeeping has become an object of observation</em>.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 15</span>
Part II closes at the farthest remove: <strong>chemistry and biology</strong>. Bond energy ÷ \(k_BT\), the Arrhenius factor, an enzyme's \(K_M\), Kleiber's \(3/4\), the information content of DNA. <em>All dimensionless without exception</em>, so nothing changes by a character in this picture. Which means <strong>life cannot, in principle, know whether the universe is "expanding" or "growing in mass"</strong>. Episode 9's "an atom has no comparison partner" pushed all the way up to the scale of biology. And Part II closes on: <em>only one thing ever moves.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sd=document.getElementById('sd'), vd=document.getElementById('vd'), ro=document.getElementById('ro');
  var X0=80, X1=690, Y0=34, Y1=280;
  var xmin=1.9, xmax=4.15, ymin=-0.012, ymax=0.145;
  var PTS=[[2,0.125,'2D (exact)'],[3,0.0181489,'3D (bootstrap)'],[4,0,'4D (mean field exact)']];

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function epsLead(d){ var e=4-d; return e*e*3/(4*81); }

  function draw(){
    var d=parseInt(sd.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    [0,0.025,0.05,0.075,0.1,0.125].forEach(function(v){
      var y=py(v);
      g.strokeStyle=(v===0?'#d8cbd2':'#f5eef1'); g.lineWidth=(v===0?1.6:1);
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a8909c'; g.fillText(v.toFixed(3), X0-10, y+4);
    });
    g.textAlign='center';
    [2,2.5,3,3.5,4].forEach(function(v){
      var x=px(v);
      g.strokeStyle='#faf5f7'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a8909c'; g.fillText(v.toFixed(1), x, Y1+16);
    });
    g.strokeStyle='#d4c3cc'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    g.fillStyle='#9a8a92'; g.textAlign='left';
    g.fillText('γ = 0 ── where the classical weight table is right', X0+8, py(0)+16);

    g.strokeStyle='#1f6b4a'; g.lineWidth=2.2; g.setLineDash([6,4]);
    g.beginPath();
    for(var i=0;i<=200;i++){
      var x=2+2*i/200, y=epsLead(x);
      if(i===0) g.moveTo(px(x),py(y)); else g.lineTo(px(x),py(y));
    }
    g.stroke(); g.setLineDash([]);
    g.fillStyle='#1f6b4a'; g.textAlign='left';
    g.fillText('leading ε-expansion term', px(2.15), py(epsLead(2.15))+16);

    g.strokeStyle='#5c1f3f'; g.lineWidth=1.4; g.setLineDash([2,4]);
    g.beginPath(); g.moveTo(px(2),py(0.125));
    g.quadraticCurveTo(px(2.6),py(0.055),px(3),py(0.0181489));
    g.quadraticCurveTo(px(3.5),py(0.004),px(4),py(0));
    g.stroke(); g.setLineDash([]);

    PTS.forEach(function(p){
      g.fillStyle='#5c1f3f';
      g.beginPath(); g.arc(px(p[0]),py(p[1]),6.5,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=2;
      g.beginPath(); g.arc(px(p[0]),py(p[1]),6.5,0,6.2832); g.stroke();
      g.fillStyle='#5c1f3f'; g.textAlign=(p[0]>3.5?'right':'left');
      g.fillText(p[2], px(p[0])+(p[0]>3.5?-12:12), py(p[1])-10);
    });

    g.strokeStyle='#8a6a7a'; g.lineWidth=1.4; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(d),Y0); g.lineTo(px(d),Y1); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#8a7580'; g.textAlign='center';
    g.fillText('spatial dimension  d', (X0+X1)/2, Y1+38);
    g.save(); g.translate(20,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('anomalous dimension γ_σ = error in the weight table', 0,0); g.restore();

    vd.textContent='d = '+d.toFixed(3);
    var known = Math.abs(d-3)<0.02 ? '　★ bootstrap value γ_σ = 0.0181489 (7 digits)'
              : (Math.abs(d-2)<0.02 ? '　★ exact γ_σ = 0.125'
              : (Math.abs(d-4)<0.02 ? '　★ γ_σ = 0 (the classical weight table is exactly right)' : ''));
    ro.textContent='d = '+d.toFixed(3)+
      '　free-field weight (d−2)/2 = '+((d-2)/2).toFixed(4)+
      '　/　leading ε term γ ≈ '+epsLead(d).toFixed(5)+known;
  }
  sd.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-14-critical.html', acc='#5c1f3f', ops='#1f6b4a',
      title='Substituting into phase transitions ── c·t = const, That Clicks, Episode 14',
      ep='EPISODE 14 ／ The weight table itself becomes an object of measurement',
      eyebrow='The bookkeeping gets error bars',
      h1='Substituting into<br>phase transitions',
      sub='The weight table this series has used for thirteen episodes was a classical approximation.<br><em>Its error has been measured to seven digits in the 3D Ising model.</em>',
      byline_l='What you need: one subtraction',
      byline_r='\\(\\gamma_\\sigma=0.0181489(10)\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 14 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That the scaling dimension decomposes as \\(\\Delta=\\Delta_{\\text{classical}}+\\gamma\\), that \\(\\Delta\\) is the Weyl weight (\\(\\mathcal{O}\\to\\Omega^{-\\Delta}\\mathcal{O}\\)), that the free scalar unitarity value is \\(\\Delta=(d-2)/2\\), and that 4 is the upper critical dimension above which mean-field theory is exact, are all standard. The 3D Ising CFT values \\(\\Delta_\\sigma=0.5181489(10)\\) and \\(\\Delta_\\varepsilon=1.412625(10)\\) are conformal bootstrap results (El-Showk, Paulos, Poland, Rychkov, Simmons-Duffin, Vichi et al., 2012–2016); the 2D \\(\\Delta_\\sigma=1/8\\) is exact. The conversions to critical exponents (\\(\\eta=2\\Delta_\\sigma-d+2\\), \\(\\nu=1/(d-\\Delta_\\varepsilon)\\) and so on) are standard, and the six exponent values together with the identity \\(\\alpha+2\\beta+\\gamma=2\\) are computed here (kenshou/calc19.py). The "experiment / MC" column gives approximate representative values from several sources, not a single one. The leading \\(\\varepsilon\\)-expansion term \\(\\eta=\\varepsilon^2(N+2)/[2(N+8)^2]\\) gives only about half the true value in three dimensions, so higher orders matter. <strong>The spatial dimension \\(d\\) of critical phenomena is distinct from the dimension of spacetime; the upper critical dimension 4 and the \\(D=4\\) of the Maxwell action are placed side by side to show a structural similarity, not because they are the same phenomenon.</strong> §05\'s "the mass weight acquires an anomalous dimension" is qualitative; how it enters depends on the renormalisation scheme and the definition of mass (pole or \\(\\overline{\\rm MS}\\)). Real materials are not exact CFTs and show these exponents only near criticality. For the relation between anomalous dimensions and the trace anomaly see Episode 8 and Extra 6 of the previous series. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the dimension and the error vanishes at four. "Show the answer" opens each solution.')
