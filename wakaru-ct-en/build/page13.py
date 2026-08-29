# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">From here the second half of Part II leaves cosmology entirely. Today: <strong>fluids and turbulence</strong>. Every dimensionless number engineering uses — Reynolds, Mach, Prandtl, Froude — is <em>invariant without exception</em>. So similarity laws, wind tunnel testing and Kolmogorov's \(-5/3\) law are unchanged to the letter here. The interesting part is <strong>the breakdown</strong>: the four quantities that make up the Reynolds number move with <em>completely different weights</em>, and always come back to zero when combined.</p>

<h2><span class="n">01</span>First, count the weights mechanically</h2>

<p>The procedure is simple. Any quantity decomposes as "length\(^{n_L}\) × time\(^{n_T}\) × mass\(^{n_M}\)", so substitute length \(+1\), time \(+1\), mass \(-1\) and add.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Dimensions</th><th class="mid">Weight</th><th class="mid">In this picture</th></tr></thead>
<tbody>
<tr><th>Length \(L\)</th><td class="mid">\(L\)</td><td class="mid">\(+1\)</td><td class="mid">\(\div a\)</td></tr>
<tr class="hi"><th>Velocity \(v\)</th><td class="mid">\(L/T\)</td><td class="mid">\(0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Mass density \(\rho\)</th><td class="mid">\(M/L^3\)</td><td class="mid">\(-4\)</td><td class="mid">\(\times a^4\)</td></tr>
<tr><th>Pressure \(p\)</th><td class="mid">\(M/LT^2\)</td><td class="mid">\(-4\)</td><td class="mid">\(\times a^4\)</td></tr>
<tr><th>Viscosity \(\eta\)</th><td class="mid">\(M/LT\)</td><td class="mid">\(-3\)</td><td class="mid">\(\times a^3\)</td></tr>
<tr><th>Kinematic viscosity \(\nu=\eta/\rho\)</th><td class="mid">\(L^2/T\)</td><td class="mid">\(+1\)</td><td class="mid">\(\div a\)</td></tr>
<tr><th>Dissipation rate \(\varepsilon\)</th><td class="mid">\(L^2/T^3\)</td><td class="mid">\(-1\)</td><td class="mid">\(\times a\)</td></tr>
<tr><th>Surface tension \(\sigma\)</th><td class="mid">\(M/T^2\)</td><td class="mid">\(-3\)</td><td class="mid">\(\times a^3\)</td></tr>
</tbody>
</table>
</div>

<p>Look at the second row — <strong>velocity has weight 0</strong>. Length and time share a weight, so they cancel in the quotient. This is the plainest reason behind everything this series has said about \(c\) not moving.</p>

<h2><span class="n">02</span>Run every dimensionless number through it</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Dimensionless number</th><th class="mid">Definition</th><th class="mid">Sum of weights</th><th class="mid">Result</th></tr></thead>
<tbody>
<tr class="hi"><th>Reynolds number</th><td class="mid">\(\rho vL/\eta\)</td><td class="mid">\(-4+0+1-(-3)=0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Mach number</th><td class="mid">\(v/c_s\)</td><td class="mid">\(0-0=0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Prandtl number</th><td class="mid">\(\nu/\kappa\)</td><td class="mid">\(1-1=0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Froude number</th><td class="mid">\(v/\sqrt{gL}\)</td><td class="mid">\(0-\tfrac{-1+1}{2}=0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Weber number</th><td class="mid">\(\rho v^2L/\sigma\)</td><td class="mid">\(-4+0+1-(-3)=0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Strouhal number</th><td class="mid">\(\Omega L/v\)</td><td class="mid">\(-1+1-0=0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Kolmogorov length</th><td class="mid">\((\nu^3/\varepsilon)^{1/4}\)</td><td class="mid">\((3\cdot1-(-1))/4=1\)</td><td class="mid">same as a length (\(\div a\))</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0"><strong>Every dimensionless number of fluid mechanics is invariant.</strong><br>
So similarity laws hold unchanged — <em>wind tunnels and ship model basins work exactly as before in this picture</em>.</p>
</div>

<h2><span class="n">03</span>The heart — the breakdown is thrashing about</h2>

<div class="calc">
<span class="tag">The four parts of the Reynolds number</span>
$$\mathrm{Re}=\frac{\rho\,v\,L}{\eta}$$
<p class="lbl">how each one moves</p>
$$\tilde\rho=a^4\rho,\qquad \tilde v=v,\qquad \tilde L=\frac{L}{a},\qquad \tilde\eta=a^3\eta$$
<p class="lbl">assembled</p>
$$\widetilde{\mathrm{Re}}=\frac{(a^4\rho)(v)(L/a)}{a^3\eta}=a^{4-1-3}\,\frac{\rho vL}{\eta}=\mathrm{Re}$$
</div>

<p><strong>The four parts move by \(a^4\), \(a^0\), \(a^{-1}\), \(a^3\) — utterly different factors — and the exponents come to exactly \(4-1-3=0\).</strong> Not a coincidence, of course: it restates that the Reynolds number is dimensionless. But <em>watching the restatement happen is quite a sight</em>.</p>

<div class="fig">
<p class="cap">Figure: how much each part of the Reynolds number moves in this picture. Drag back in time and <strong>the bars stretch and shrink independently</strong> (\(\rho\) as \(a^4\), \(\eta\) as \(a^3\), \(L\) as \(1/a\)). And the rightmost bar — the total, Re — <em>stays pinned to zero</em>.</p>
<canvas id="cv" width="720" height="360"></canvas>
<div class="controls">
  <label>Which epoch, \(\log_{10}a\) (right edge = today)<input id="sa" type="range" min="-3000" max="0" value="-1000" step="1"></label>
  <span class="val" id="va">a = 0.100</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#5a5a2a"></i>factor for each part</span>
  <span><i class="swatch" style="background:#7a2f5a"></i>total = factor for the Reynolds number</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>Turbulence and critical phenomena too — exponents are just numbers</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>What is measured</th><th class="mid">Value</th><th class="mid">In this picture</th></tr></thead>
<tbody>
<tr><th>Kolmogorov law \(E(k)\propto k^{-5/3}\)</th><td class="mid">\(-5/3\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>3D Ising \(\nu\)</th><td class="mid">0.629971</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Scaling dimension \(\Delta_\sigma\)</th><td class="mid">0.5181489</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Fractal dimension</th><td class="mid">──</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Lyapunov exponent × elapsed time \(\lambda t\)</th><td class="mid">──</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Kleiber's law exponent</th><td class="mid">3/4</td><td class="mid"><strong>invariant</strong></td></tr>
</tbody>
</table>
</div>

<p>The Lyapunov exponent \(\lambda\) alone has weight \(-1\) on its own (inverse time), but what has meaning is the <em>product with elapsed time</em>, \(\lambda t\). Since \(t\) has weight \(+1\), it cancels. <strong>"How much predictability has been lost" has the same value in this picture.</strong></p>

<h2><span class="n">05</span>The reveal — the tool only touches "size"</h2>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>A conformal transformation touches only "size".</strong><br>
Every measure of structure, complexity and information is dimensionless — <em>out of reach</em>.</p>
</div>

<p>This is the complex-systems version of Episode 6's conclusion. There we counted "it cannot reach the memory in use (= black hole entropy)". Here: "it cannot reach turbulence exponents, critical exponents or fractal dimensions either".</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>What it touches: size</strong><span>lengths, masses, energies, temperatures, densities, viscosities — everything dimensionful moves</span></div></div>
<div class="row hi"><div class="mk">②</div><div class="txt"><strong>What it cannot touch: shape</strong><span>dimensionless numbers, exponents, ratios, information measures, complexity measures — not one of them moves</span></div></div>
</div>

<p>So while cosmology collapsed into "one mass" under this notation (Episode 4), <em>fluid mechanics does not collapse by a single character</em>. There is nothing in it to collapse. <strong>The Navier–Stokes equations are completely untouched here.</strong></p>

<div class="aside">
<span class="tag">Read the other way, this is the tool's limit</span>
Since Episode 1 we have repeated "divide and out comes the expansion law" — but that only ever applied <em>when two dimensionful quantities were brought together</em>. To any field already written dimensionlessly — the similarity laws of fluid mechanics, critical phenomena, information theory — this tool gives <strong>no information at all</strong>. <em>A conformal transformation says something new only where dimensionful quantities are the protagonists</em>, and that is almost exclusively cosmology and gravity.
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① The weight counting assumes material properties (viscosity and the like) are transformed along with everything else.</strong> A fluid fixed in a laboratory (water of a given viscosity) does not transform by itself — what is treated here is <em>rewriting the whole universe at once</em>. Same caveat as Episode 8 ①.</p>
<p style="margin:0 0 10px"><strong>② "Wind tunnels still work" restates the fact that similarity laws are written with dimensionless numbers only.</strong> Real wind tunnel testing works independently of conformal transformations; this document merely <em>reconfirms</em> that and claims nothing new.</p>
<p style="margin:0 0 10px"><strong>③ Kolmogorov's \(-5/3\) law has intermittency corrections</strong> and deviates slightly from \(-5/3\) in reality. The corrected exponent is also dimensionless, so the conclusion is unchanged.</p>
<p style="margin:0"><strong>④ "A conformal transformation touches only size" is a classical statement.</strong> Quantised, the trace anomaly makes dimensionless quantities (couplings, scaling dimensions) run — treated in Episode 8 and Extra 6 of the previous series, and in Part V here. <em>Dimensionless does not mean absolutely safe.</em></p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Why does velocity have weight 0?
<details><summary>Show the answer</summary><div class="ans">Because length and time both have weight \(+1\), so they cancel in the quotient. <em>This is the plainest reason the speed of light does not move in this picture</em> — \(c\) is a velocity, hence weight 0 from the start.</div></details></li>

<li>Find the weight of viscosity \(\eta\) (dimensions \(M/LT\)).
<details><summary>Show the answer</summary><div class="ans">\(M\) is \(-1\), \(L\) is \(+1\), \(T\) is \(+1\), so \(-1-1-1=-3\), giving \(\tilde\eta=a^3\eta\). <em>The younger the universe, the runnier the fluid in this picture.</em></div></details></li>

<li>Show the Reynolds number is invariant from the four parts' exponents.
<details><summary>Show the answer</summary><div class="ans">\(\tilde\rho=a^4\rho\), \(\tilde v=v\), \(\tilde L=L/a\), \(\tilde\eta=a^3\eta\). Assembled: \(a^{4}\cdot a^{0}\cdot a^{-1}/a^{3}=a^{0}\). <strong>Four parts moving independently, exponents summing to zero.</strong></div></details></li>

<li>What is the weight of the Kolmogorov length \((\nu^3/\varepsilon)^{1/4}\), and what does it mean?
<details><summary>Show the answer</summary><div class="ans">\(\nu\) is \(+1\) and \(\varepsilon\) is \(-1\), so \((3\cdot1-(-1))/4=+1\) — <strong>the same weight as a length</strong>. The Kolmogorov scale shrinks as \(1/a\) like every other length here. <em>The hierarchy of eddies shrinks similarly, whole</em>, without changing shape.</div></details></li>

<li>(Harder) Does this series' tool say anything about complex systems?
<details><summary>Show the answer</summary><div class="ans"><strong>Nothing at all.</strong> Every measure of complexity (dimensionless numbers, exponents, fractal dimensions, information measures) has weight 0, so a conformal transformation moves none of them. <em>This tool touches only "size"</em> and cannot reach "shape" — the same structure as Episode 6's "it cannot reach the memory in use". And <strong>that is a precise statement of the tool's limit</strong>.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — it touches size and cannot reach shape</h2>
<p>Decompose any quantity as "length\(^{n_L}\)×time\(^{n_T}\)×mass\(^{n_M}\)", add \(+1,+1,-1\), and out comes the weight. Doing so: velocity 0, mass density \(-4\), viscosity \(-3\), kinematic viscosity \(+1\). And <strong>Reynolds, Mach, Prandtl, Froude, Weber and Strouhal numbers are all 0 without exception</strong>. Similarity laws hold unchanged; wind tunnels and ship model basins work exactly as before.</p>
<p>The breakdown was the interesting part. The Reynolds number's four parts move by \(a^4\), \(a^0\), \(a^{-1}\), \(a^3\) — <em>utterly different factors</em> — and the exponents sum to \(4-1-3=0\) exactly. <strong>That the result is invariant is obvious; watching the innards thrash about this much is a sight.</strong></p>
<p>A level up is the same: Kolmogorov's \(-5/3\), the 3D Ising \(\nu=0.629971\), the scaling dimension \(\Delta_\sigma=0.518\), fractal dimensions, Lyapunov exponent × elapsed time, Kleiber's \(3/4\). <em>Exponents are just numbers</em>, so not one of them moves.</p>
<p>And the reveal — <strong>a conformal transformation touches only "size"</strong>. Measures of structure, complexity and information are all dimensionless and out of reach. So while cosmology collapsed to "one mass" (Episode 4), <em>fluid mechanics does not collapse by a character</em>. Navier–Stokes stands completely untouched. <strong>Which is also a precise measurement of the tool's limit</strong>: a conformal transformation says something new only where dimensionful quantities are the protagonists — almost exclusively cosmology and gravity.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 14</span>
We leaned hard on "dimensionless means invariant" today, but <strong>there is exactly one place where it breaks</strong>: phase transitions. At a critical point the dimensionless exponents <em>depart from their classical values</em> (anomalous dimensions). As Extra 6 of the previous series showed, the 3D Ising \(\Delta_\sigma=0.5181489\) sits slightly off the free-field \(0.5\), and that offset \(\gamma_\sigma=0.0181489\) is precisely a seven-digit measurement of <strong>how wrong the conformal weights are</strong>. Next time: <strong>the weights of this notation have been measured in the laboratory</strong>. <em>The bookkeeping gets error bars.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sa=document.getElementById('sa'), va=document.getElementById('va'), ro=document.getElementById('ro');
  var X0=70, X1=700, Y0=34, YB=250;
  var PARTS=[['ρ',4,'#5a5a2a'],['v',0,'#5a5a2a'],['L',-1,'#5a5a2a'],['η (denominator)',-3,'#5a5a2a']];

  function draw(){
    var la=parseInt(sa.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';

    var maxexp=4*Math.abs(la);
    var scale=Math.min(95, 190/Math.max(maxexp,1));
    g.textAlign='right';
    for(var e=-12;e<=12;e+=4){
      var y=YB-e*scale;
      if(y<Y0-4||y>YB+96) continue;
      g.strokeStyle=(e===0?'#c9c9a8':'#f1f1e4'); g.lineWidth=(e===0?1.6:1);
      g.beginPath(); g.moveTo(X0-8,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#9c9c7c'; g.font='11px sans-serif';
      g.fillText(e===0?'×1':'10'+e, X0-12, y+4);
      g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    }

    var n=5, w=64, gap=(X1-X0-n*w)/(n+1);
    var total=0;
    for(var i=0;i<PARTS.length;i++){
      var ex=-PARTS[i][1]*la;
      total+= (i===3? -ex : ex);
      var x=X0+gap+(w+gap)*i;
      var h=ex*scale;
      g.fillStyle=PARTS[i][2];
      g.globalAlpha=0.85;
      g.fillRect(x, h>=0? YB-h : YB, w, Math.abs(h));
      g.globalAlpha=1;
      g.fillStyle='#3f3f1c'; g.textAlign='center';
      g.fillText(PARTS[i][0], x+w/2, YB+22);
      g.font='11px sans-serif'; g.fillStyle='#6a6a48';
      g.fillText('×10'+(ex>=0?'+':'')+ex.toFixed(1), x+w/2, YB+40);
      g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    }
    var x=X0+gap+(w+gap)*4;
    g.fillStyle='#7a2f5a'; g.globalAlpha=0.9;
    g.fillRect(x, YB-2, w, 4);
    g.globalAlpha=1;
    g.fillStyle='#7a2f5a'; g.textAlign='center';
    g.fillText('Re', x+w/2, YB+22);
    g.font='11px sans-serif';
    g.fillText('×10'+total.toFixed(1), x+w/2, YB+40);
    g.font='bold 12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText('does not move', x+w/2, YB-14);

    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillStyle='#7d7d5c'; g.textAlign='center';
    g.fillText('Reynolds number Re = ρ v L / η  ── factor for each part', (X0+X1)/2, YB+72);

    var a=Math.pow(10,la);
    va.textContent='a = '+(a<0.01? a.toExponential(2) : a.toFixed(3));
    ro.textContent='a = '+va.textContent+' (z = '+(1/a-1).toPrecision(3)+')　'+
      'ρ ×10'+(-4*la>=0?'+':'')+(-4*la).toFixed(1)+'　'+
      'v ×1　'+
      'L ×10'+(la>=0?'+':'')+(la).toFixed(1)+'　'+
      'η ×10'+(-3*la>=0?'+':'')+(-3*la).toFixed(1)+
      '　→　total ×10'+total.toFixed(1)+'　★ the Reynolds number does not move';
  }
  sa.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-13-fluid.html', acc='#5a5a2a', ops='#7a2f5a',
      title='Substituting into fluids and turbulence ── c·t = const, That Clicks, Episode 13',
      ep='EPISODE 13 ／ Leaving cosmology entirely',
      eyebrow='Every dimensionless number is invariant — so what does the breakdown look like?',
      h1='Substituting into<br>fluids and turbulence',
      sub='The four quantities in the Reynolds number move as \\(a^4,\\ a^0,\\ a^{-1},\\ a^3\\), all differently.<br><em>And combined, they always come back to zero.</em>',
      byline_l='What you need: adding weights, nothing else',
      byline_r='\\(-4+0+1-(-3)=0\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 13 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That lengths and times carry conformal weight \\(+1\\) and mass \\(-1\\), so that any quantity\'s weight follows mechanically from its dimensions, is standard. The weights given here (velocity 0, mass density \\(-4\\), pressure \\(-4\\), viscosity \\(-3\\), kinematic viscosity \\(+1\\), dissipation rate \\(-1\\), surface tension \\(-3\\)), the vanishing weight of the Reynolds, Mach, Prandtl, Froude, Weber and Strouhal numbers, and the weight \\(+1\\) of the Kolmogorov length, are mechanical checks performed here (kenshou/calc18.py). They are instances of the general rule that dimensionless numbers are conformally invariant and claim no new physics — <strong>similarity laws and wind tunnel testing hold independently of conformal transformations, and this document merely reconfirms that</strong>. The weight counting assumes material properties (viscosity and so on) transform along with everything else and does not apply to a fluid fixed in a laboratory. Kolmogorov\'s \\(-5/3\\) law has intermittency corrections and deviates slightly in reality; the corrected exponent is also dimensionless, so the conclusion is unchanged. The 3D Ising values \\(\\nu=0.629971\\) and \\(\\Delta_\\sigma=0.5181489\\) are conformal bootstrap results (Extra 6 of the previous series). "A conformal transformation touches only size" is a classical claim; quantised, the trace anomaly makes couplings and scaling dimensions run (Episode 8 and Extra 6 of the previous series; Part V here). Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination and conflicts with nucleosynthesis when extrapolated into the early universe (Lewis, Barnes &amp; Kaushik 2016). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the epoch; the four bars thrash while the total stays put. "Show the answer" opens each solution.')
