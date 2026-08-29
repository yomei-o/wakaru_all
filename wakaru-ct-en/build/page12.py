# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">The last episode of Part II's cosmology run. Substituting into the vacuum energy produces something rather amusing — <strong>in this picture the cosmological constant grows fastest of all</strong> (\(\propto t^4\)). And the thing that is genuinely constant is <em>radiation</em>, which diluted fastest in the standard picture. <strong>The ranking flips completely.</strong> Which is to say: the name "cosmological constant" was itself picture-dependent.</p>

<h2><span class="n">01</span>Transforming all three components at once</h2>

<p>Energy density has weight \(-4\), so here \(\tilde\rho=a^4\rho\). Just multiply by the standard dilution.</p>

<div class="calc">
<span class="tag">Just multiplication</span>
$$\tilde\rho_r=a^4\cdot a^{-4}=\text{const}$$
$$\tilde\rho_m=a^4\cdot a^{-3}=a\ \propto t$$
$$\tilde\rho_\Lambda=a^4\cdot 1=a^4\ \propto t^4$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Component</th><th class="mid">Standard picture</th><th class="mid">This picture</th><th class="mid">Rank</th></tr></thead>
<tbody>
<tr><th>Radiation</th><td class="mid">\(\propto a^{-4}\) (dilutes fastest)</td><td class="mid"><strong>constant</strong></td><td class="mid">1st ↔ 3rd</td></tr>
<tr><th>Matter</th><td class="mid">\(\propto a^{-3}\)</td><td class="mid">\(\propto t\)</td><td class="mid">2nd ↔ 2nd</td></tr>
<tr class="hi"><th>Cosmological constant \(\Lambda\)</th><td class="mid">constant (hence "constant")</td><td class="mid"><strong>\(\propto t^4\)</strong> (grows fastest)</td><td class="mid">3rd ↔ 1st</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>The name "cosmological constant" depends on the picture.</strong><br>
What is genuinely constant here is <em>radiation</em>, the component that diluted fastest in the standard picture.<br>
── Episode 3's surgery on the series title reaches even this far.</p>
</div>

<p>Episode 11 counted "the photon gas is completely at rest". The first row here is the <em>energy-density version</em> of that: \(\rho_r=7.05\times10^{-14}\ \mathrm{J/m^3}\), the same value throughout cosmic history.</p>

<h2><span class="n">02</span>And the cosmological constant problem does not move a millimetre</h2>

<p>The cosmological constant problem is the \(10^{120}\) gap between the naive field-theory estimate and the observed value. If \(\rho_\Lambda\) grows as \(t^4\) here, does the problem move?</p>

<div class="calc">
<span class="tag">Make it dimensionless</span>
$$\rho_\Lambda^{1/4}=2.240\ \mathrm{meV}\qquad\Longrightarrow\qquad \frac{\rho_\Lambda^{1/4}}{M_{\rm Pl}}=1.835\times10^{-31}$$
<p class="lbl">to the fourth power, the famous number</p>
$$\frac{\rho_\Lambda}{M_{\rm Pl}^4}=1.13\times10^{-123}$$
</div>

<p>\(\rho_\Lambda\) grows as \(t^4\) — and so does \(M_{\rm Pl}^4\), since \(M_{\rm Pl}\) is a mass of weight \(-1\). <strong>They cancel exactly in the ratio.</strong></p>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0">The cosmological constant problem (\(10^{-123}\)) <strong>does not move a millimetre when the picture changes</strong>.<br>
The ratio is dimensionless — exactly the structure of Episode 10's Landauer cost.</p>
</div>

<h2><span class="n">03</span>The "why now?" problem does not vanish either</h2>

<div class="calc">
<span class="tag">The ratio's time dependence, in both pictures</span>
<p class="lbl">Standard picture</p>
$$\frac{\rho_\Lambda}{\rho_m}=\frac{1}{a^{-3}}\propto a^3$$
<p class="lbl">This picture</p>
$$\frac{\tilde\rho_\Lambda}{\tilde\rho_m}=\frac{a^4}{a}=a^3\qquad\text{── the same}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th class="mid">Value</th><th class="mid">In this picture</th></tr></thead>
<tbody>
<tr><th>Today's \(\rho_\Lambda/\rho_m\)</th><td class="mid">2.175</td><td class="mid">invariant</td></tr>
<tr class="hi"><th>When \(\Lambda\) equals matter</th><td class="mid">\(a=0.772\) (\(z=0.30\))</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>When radiation equals matter</th><td class="mid">\(a=2.9\times10^{-4}\) (\(z=3400\))</td><td class="mid"><strong>invariant</strong></td></tr>
</tbody>
</table>
</div>

<p>Not only the ratio but <strong>its time dependence</strong> is the same. So the degree of strangeness in "why exactly now?" is untouched. <em>Change the picture and the puzzle remains a puzzle.</em></p>

<div class="aside">
<span class="tag">Puzzles that vanish, and puzzles that do not</span>
Nothing in this series has actually vanished on changing pictures. The one thing that looked as if it had — the geometric singularity (Episode 6 of the previous series) — came back the moment a dimensionless ratio was formed. The same here. <strong>Both the cosmological constant problem and the "why now" problem are written dimensionlessly from the start, so rewriting cannot reach them.</strong> <em>Good puzzles are written dimensionlessly.</em>
</div>

<div class="fig">
<p class="cap">Figure: the three energy densities. Switching the way of speaking <strong>rotates the three lines and reverses their ranking</strong> (at the right, radiation is flat and \(\Lambda\) is steepest). And yet <em>the two crossings — the equality epochs — do not move at all</em>.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Way of speaking \(s\) (left = standard / right = mass grows)<input id="ss" type="range" min="0" max="1000" value="1000" step="1"></label>
  <span class="val" id="vs">s = 1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#9a3a5a"></i>radiation</span>
  <span><i class="swatch" style="background:#1f4a2a"></i>matter</span>
  <span><i class="swatch" style="background:#4a7a3a"></i>cosmological constant \(\Lambda\)</span>
  <span><i class="swatch" style="background:#9aa89a"></i>equality epochs (immovable)</span>
</div>
</div>

<p>At the left (standard) the red plunges and the green is flat — the familiar textbook figure. Drag right and the three rotate until, at the far right, <strong>red is flat, dark green is \(+1\), light green is \(+4\)</strong>. It looks like a different universe, and yet <em>not one crossing has moved</em>.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The reveal — "constant" is a word with a hidden comparison</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Compare \(\rho_\Lambda\) with…</th><th class="mid">Result</th></tr></thead>
<tbody>
<tr><th>energy per comoving volume (standard)</th><td class="mid">constant → "cosmological constant"</td></tr>
<tr><th>particle masses (this picture)</th><td class="mid">\(\propto t^4/t^4=\)constant</td></tr>
<tr><th>a fixed ruler's volume (this picture)</th><td class="mid">\(\propto t^4\) → not a constant</td></tr>
<tr class="hi"><th>\(M_{\rm Pl}^4\)</th><td class="mid"><strong>\(1.13\times10^{-123}\), invariant</strong> ← this is the physics</td></tr>
</tbody>
</table>
</div>

<p>Only the last row is a genuinely invariant statement. That, and the equation of state \(w=-1\), which is also dimensionless and therefore the same in every picture. <strong>Those two are all that can be said physically about \(\Lambda\).</strong></p>

<h2><span class="n">05</span>An aside — the two smallest numbers in nature</h2>

<div class="calc">
<span class="tag">Side by side</span>
$$\frac{\rho_\Lambda^{1/4}}{M_{\rm Pl}}=1.83\times10^{-31},\qquad \frac{m_\nu}{M_{\rm Pl}}=4.10\times10^{-30}$$
<p class="lbl">ratio</p>
$$\frac{m_\nu}{\rho_\Lambda^{1/4}}=22.3$$
</div>

<p>The <em>two smallest scales known in nature</em> are only 22 apart, when everything else is separated by factors of \(10^{25}\). This coincidence, pointed out in Extra 5 of the previous series, is of course dimensionless — <strong>so it does not move with the picture either</strong>. No theory currently explains it.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① \(\tilde\rho=a^4\rho\) follows from energy density having weight \(-4\)</strong> (energy \(-1\) plus volume \(+3\)). Standard counting.</p>
<p style="margin:0 0 10px"><strong>② "The cosmological constant problem is \(10^{120}\)" is the ratio of a naive cutoff estimate (\(\rho_{\rm vac}\sim M_{\rm Pl}^4\)) to the observed value.</strong> Whether that estimate is legitimate is disputed, and supersymmetry or the treatment of renormalisation change the number substantially. The claim here is only that <em>whatever the ratio is, swapping pictures does not move it</em>.</p>
<p style="margin:0 0 10px"><strong>③ The "why now" problem is quantified via the time dependence of \(\rho_\Lambda/\rho_m\).</strong> That is one formulation among several, and whether the coincidence problem is a problem at all is itself debated (anthropic explanations, dynamical dark energy, and so on).</p>
<p style="margin:0 0 10px"><strong>④ \(\Lambda\) is treated as a perfect fluid with \(w=-1\).</strong> With dynamical dark energy (quintessence and the like) \(\rho_\Lambda\) varies in time and the third row of §01 changes — though the conclusion that <em>it does not move with the picture</em> is the same.</p>
<p style="margin:0"><strong>⑤ \(m_\nu=0.05\) eV is the indicative lower bound on the heaviest neutrino from oscillation experiments.</strong> Its factor-of-22 proximity to \(\rho_\Lambda^{1/4}\) is <strong>an unexplained numerical coincidence</strong>, with no known theoretical relation (Extra 5 of the previous series).</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>How do the three energy densities behave here, and what happens to the ranking?
<details><summary>Show the answer</summary><div class="ans">\(\tilde\rho=a^4\rho\), so radiation \(a^4a^{-4}=\)const, matter \(a^4a^{-3}=a\propto t\), \(\Lambda\) \(a^4\propto t^4\). <strong>The ranking reverses completely</strong>: the "constant" \(\Lambda\) grows fastest, and the fastest-diluting radiation becomes the genuine constant.</div></details></li>

<li>\(\rho_\Lambda\) grows as \(t^4\); why does the cosmological constant problem not move?
<details><summary>Show the answer</summary><div class="ans">Because \(M_{\rm Pl}^4\), the thing it is compared with, grows as the same \(t^4\) (\(M_{\rm Pl}\) is a mass, weight \(-1\)). Dividing cancels it, leaving \(\rho_\Lambda/M_{\rm Pl}^4=1.13\times10^{-123}\) <strong>invariant</strong>.</div></details></li>

<li>Is the "why now" problem eased in this picture?
<details><summary>Show the answer</summary><div class="ans">No. \(\rho_\Lambda/\rho_m\) goes as \(\propto a^3\) in the standard picture and as \(a^4/a=a^3\) here — <strong>even the time dependence is identical</strong>. Today's 2.175 and the equality at \(z=0.30\) do not move. <em>Good puzzles are written dimensionlessly, so rewriting cannot reach them.</em></div></details></li>

<li>What is genuinely "constant" in this picture?
<details><summary>Show the answer</summary><div class="ans"><strong>The radiation energy density</strong> (\(7.05\times10^{-14}\ \mathrm{J/m^3}\)) — the energy-density version of Episode 11's "the photon gas is completely at rest". <em>The name "cosmological constant" was picture-dependent.</em></div></details></li>

<li>(Harder) List everything about \(\Lambda\) that can be said independently of the picture.
<details><summary>Show the answer</summary><div class="ans">Two things only: ① the equation of state \(w=-1\) (dimensionless), and ② \(\rho_\Lambda/M_{\rm Pl}^4=1.13\times10^{-123}\) (dimensionless). The value and time dependence of \(\rho_\Lambda/\rho_m\) follow and are also invariant. <strong>That it "is constant" cannot be said independently of the picture</strong> — which is the most amusing part of this episode.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — the name "constant" was bookkeeping</h2>
<p>Energy density has weight \(-4\), so \(\tilde\rho=a^4\rho\). Applied to the three components: radiation <strong>constant</strong>, matter \(\propto t\), cosmological constant <strong>\(\propto t^4\)</strong>. <em>The ranking reverses completely.</em> The fastest-diluting radiation becomes the genuine constant, and the thing called "constant" grows fastest. <strong>The name "cosmological constant" was itself picture-dependent.</strong></p>
<p>And still the puzzles do not move. \(\rho_\Lambda\) grows as \(t^4\), \(M_{\rm Pl}^4\) grows by the same factor, so <strong>\(\rho_\Lambda/M_{\rm Pl}^4=1.13\times10^{-123}\) is invariant</strong>. The cosmological constant problem does not shift a millimetre. Nor does "why now": \(\rho_\Lambda/\rho_m\) goes as \(\propto a^3\) in both pictures, today's 2.175 and the equality at \(z=0.30\) unchanged. <em>Good puzzles are written dimensionlessly from the start, so rewriting cannot reach them.</em></p>
<p>The reveal is Episode 3's again — <strong>"is constant" means nothing until you say constant relative to what</strong>. What can be said about \(\Lambda\) independently of the picture is exactly two things: \(w=-1\) and \(\rho_\Lambda/M_{\rm Pl}^4\). And as an aside, the two smallest scales in nature (\(\rho_\Lambda^{1/4}/M_{\rm Pl}=1.83\times10^{-31}\) and \(m_\nu/M_{\rm Pl}=4.10\times10^{-30}\)) sit only a factor 22 apart — a coincidence that, being dimensionless, likewise stays put.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 13</span>
The rest of Part II leaves cosmology entirely. Next: <strong>fluids and turbulence</strong> — Reynolds number, Mach number, Prandtl number, Strouhal number. Every dimensionless number engineering uses is <em>invariant without exception</em>. So similarity laws, wind tunnel testing and Kolmogorov's turbulence law are unchanged to the letter. What does change? <strong>Viscosity, and the three quantities that make up the Reynolds number, each move with a different weight.</strong> Look only at what moves and it is another world; combine them and you always come back. <em>An episode testing how far "only dimensionless is physics" carries outside cosmology.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=318;
  var xmin=-4.2, xmax=0.4;
  var ymin=-6, ymax=18;
  var Om=0.315, OL=0.685, Or=9.2e-5;
  var A_EQ1=Math.log(Or/Om)/Math.LN10;
  var A_EQ2=Math.log(Math.pow(Om/OL,1/3))/Math.LN10;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function lg(v){ return Math.log(v)/Math.LN10; }

  function seg(sl,off,col,w){
    g.strokeStyle=col; g.lineWidth=w; g.beginPath();
    var first=true;
    for(var i=0;i<=200;i++){
      var lx=xmin+(xmax-xmin)*i/200, y=off+sl*lx;
      if(y<ymin||y>ymax){ first=true; continue; }
      if(first){ g.moveTo(px(lx),py(y)); first=false; } else g.lineTo(px(lx),py(y));
    }
    g.stroke();
  }

  function draw(){
    var s=parseInt(ss.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=-6;e<=18;e+=4){
      var y=py(e);
      g.strokeStyle='#eef2ee'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#95a595'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-4;q<=0;q++){
      var x=px(q);
      g.strokeStyle='#f5f8f5'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#95a595'; g.fillText(q===0?'now':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#c6d2c6'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    [[A_EQ1,'radiation = matter'],[A_EQ2,'matter = Λ']].forEach(function(q){
      g.strokeStyle='#9aa89a'; g.lineWidth=1.5; g.setLineDash([5,4]);
      g.beginPath(); g.moveTo(px(q[0]),Y0); g.lineTo(px(q[0]),Y1); g.stroke();
      g.setLineDash([]);
      g.fillStyle='#7f8d7f'; g.textAlign='center';
      g.fillText(q[1], px(q[0]), Y0-8);
    });

    seg(-4*(1-s), lg(Or/OL), '#9a3a5a', 3.2);
    seg(-3*(1-s), lg(Om/OL), '#1f4a2a', 3.2);
    seg( 0*(1-s)+4*s, 0,     '#4a7a3a', 3.2);

    g.textAlign='left'; g.font='bold 12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillStyle='#9a3a5a'; g.fillText('radiation', px(xmin)+8, py(Math.min(lg(Or/OL)-4*(1-s)*xmin,ymax))-6);
    g.fillStyle='#1f4a2a'; g.fillText('matter', px(xmin)+72, py(Math.min(lg(Om/OL)-3*(1-s)*xmin,ymax))+16);
    g.fillStyle='#4a7a3a'; g.fillText('Λ',    px(xmin)+8, py(Math.max(4*s*xmin,ymin))+16);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.fillStyle='#7a8a7a'; g.textAlign='center';
    g.fillText('scale factor  a', (X0+X1)/2, Y1+36);

    vs.textContent='s = '+s.toFixed(2);
    var tag = s>0.995?'(mass-grows picture)':(s<0.005?'(standard picture)':'(intermediate)');
    ro.textContent='s = '+s.toFixed(2)+' '+tag+
      '　radiation ∝ a^'+(-4*(1-s)).toFixed(2)+
      '　matter ∝ a^'+(-3*(1-s)).toFixed(2)+
      '　Λ ∝ a^'+(4*s).toFixed(2)+
      '　/　crossings nailed at z=3400 and z=0.30'+
      (s>0.995?'　★ the ranking has completely reversed':'');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-12-vacuum.html', acc='#1f4a2a', ops='#9a3a5a',
      title='Substituting into the vacuum ── c·t = const, That Clicks, Episode 12',
      ep='EPISODE 12 ／ Closing Part II\'s cosmology run',
      eyebrow='In this picture the cosmological constant grows fastest of all',
      h1='Substituting<br>into the vacuum',
      sub='\\(\\tilde\\rho_\\Lambda\\propto t^4\\), \\(\\tilde\\rho_m\\propto t\\), \\(\\tilde\\rho_r=\\)const.<br><em>The ranking reverses completely, and the word "constant" turns out to be bookkeeping.</em>',
      byline_l='What you need: weight \\(-4\\), multiplication',
      byline_r='\\(\\rho_\\Lambda/M_{\\rm Pl}^4=1.13\\times10^{-123}\\) is invariant',
      body=BODY + '\n\n<p class="foot">This document is Episode 12 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That energy density has conformal weight \\(-4\\) (energy \\(-1\\) plus volume \\(+3\\)), and that standard cosmology has \\(\\rho_r\\propto a^{-4}\\), \\(\\rho_m\\propto a^{-3}\\), \\(\\rho_\\Lambda=\\)const, are standard. The results \\(\\tilde\\rho_r=\\)const, \\(\\tilde\\rho_m\\propto t\\), \\(\\tilde\\rho_\\Lambda\\propto t^4\\) (the reversal of ranking) are this document\'s calculation from those two. \\(\\rho_\\Lambda^{1/4}=2.240\\) meV, \\(\\rho_\\Lambda^{1/4}/M_{\\rm Pl}=1.835\\times10^{-31}\\) and \\(\\rho_\\Lambda/M_{\\rm Pl}^4=1.13\\times10^{-123}\\) are computed here from \\(h=0.674\\), \\(\\Omega_\\Lambda=0.685\\). <strong>The statement "the cosmological constant problem is \\(10^{120}\\)" is the ratio of a naive cutoff estimate \\(\\rho_{\\rm vac}\\sim M_{\\rm Pl}^4\\) to the observed value, and the legitimacy of that estimate is disputed</strong> — the claim made here is only that whatever the ratio is, swapping pictures does not move it. Likewise, whether the coincidence problem ("why now") is a problem at all is debated. \\(\\Lambda\\) is treated as a perfect fluid with \\(w=-1\\); with dynamical dark energy the third row of §01 changes, though the picture-independence conclusion does not. The equality epochs \\(a=(\\Omega_m/\\Omega_\\Lambda)^{1/3}=0.772\\) (\\(z=0.30\\)) and \\(a=\\Omega_r/\\Omega_m=2.9\\times10^{-4}\\) (\\(z=3400\\)) are computed here. \\(m_\\nu=0.05\\) eV is the indicative lower bound on the heaviest neutrino from oscillation experiments, and its factor-of-22 proximity to \\(\\rho_\\Lambda^{1/4}\\) is an unexplained numerical coincidence (Extra 5 of the previous series). Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination and conflicts with nucleosynthesis when extrapolated into the early universe (Lewis, Barnes &amp; Kaushik 2016). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider switches the way of speaking; the ranking reverses while the crossings stay put. "Show the answer" opens each solution.')
