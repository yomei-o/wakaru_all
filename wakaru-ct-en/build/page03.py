# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
from mkpage import build

BODY = r'''<p class="lead">Twice now, in Episodes 1 and 2, we have written that \(c\cdot t=\text{const}\) does not agree with observation. There is an obvious objection: <em>"a rewriting moves no dimensionless quantity at all — so how could it possibly fail?"</em> The objection is right. <strong>Because it is right, we push it all the way.</strong> Push it hard enough and \(c\cdot t=\text{const}\) holds in <em>any</em> universe whatsoever — and exactly <em>one</em> claim is left standing. This episode identifies that one claim.</p>

<h2><span class="n">01</span>Position A — move no dimensionless quantity</h2>

<p>The decision procedure of the previous series was plain: if a dimensionless quantity moves it is physics, if not it is bookkeeping. A conformal transformation — swapping the ruler — moves none, so it is bookkeeping. All ten episodes proved that much.</p>

<div class="keybox">
<p class="lbl">Position A</p>
<p style="margin:6px 0 0">\(c\cdot t=\text{const}\) is a <strong>pure rewriting</strong> and moves not one dimensionless quantity.<br>
Therefore it cannot contradict any observation.</p>
</div>

<p>Grant this as an assumption. Having granted it, let us actually build the rewriting.</p>

<h2><span class="n">02</span>Constructing the time coordinate</h2>

<p>Redo the procedure of Episode 3 of the previous series, but without fixing \(a(t)\).</p>

<div class="calc">
<span class="tag">Calculation — three lines</span>
<p class="lbl">① Start, and conformally transform</p>
$$ds^2=-c_0^2dt^2+a(t)^2dx^2\ \xrightarrow{\ \Omega=1/a\ }\ d\tilde s^2=-\Big(\frac{c_0}{a}\Big)^2dt^2+dx^2$$
<p class="lbl">② Change the time coordinate to \(T(t)\) (with \(T'=dT/dt\))</p>
$$d\tilde s^2=-\Big(\frac{c_0}{a\,T'}\Big)^2dT^2+dx^2\qquad\Longrightarrow\qquad c_B(T)=\frac{c_0}{a\,T'}$$
<p class="lbl">③ Demand \(c_B\cdot T=C\) and solve</p>
$$\frac{c_0T}{aT'}=C\ \Longrightarrow\ \frac{d\ln T}{dt}=\frac{c_0}{a\,C}\ \Longrightarrow\ \ln T=\frac{c_0}{C}\int\!\frac{dt}{a}=\frac{c_0}{C}\,\eta$$
</div>

<div class="keybox">
<p class="lbl">The answer</p>
$$\boxed{\ T=\exp\!\left(\frac{\eta}{\eta_0}\right)\qquad\left(\eta=\int\frac{dt}{a}\ \text{is conformal time}\right)}$$
<p style="margin:10px 0 0"><strong>It solves whatever \(a(t)\) is.</strong> That is: \(c\cdot t=\text{const}\) can be realised in any universe.</p>
</div>

<p>The choice \(\Omega=1/a\) leaves no freedom — it is forced the moment you decide the spatial metric shall be the comoving grid itself. The only freedom left is the time coordinate, and using exactly that freedom up gives \(T=e^{\eta/\eta_0}\). <em>Precisely one such coordinate, and it always exists.</em></p>

<h2><span class="n">03</span>Checking it numerically</h2>

<p>Rather than take that on trust, we measure it. Build \(a=(t/t_0)^p\) numerically, integrate \(\eta\) numerically, form \(T=e^{\eta/\eta_0}\), differentiate numerically to get \(T'\), assemble \(c_B=c_0/(aT')\), and finally look at \(c_B\cdot T\).</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Universe</th><th class="mid">\(p\)</th><th class="mid">\(c_B\cdot T\) (measured)</th><th class="mid">verdict</th></tr></thead>
<tbody>
<tr><th>radiation</th><td class="mid">0.5</td><td class="mid">1.000000 ± 9×10⁻⁸</td><td class="mid">constant ✓</td></tr>
<tr><th>matter</th><td class="mid">0.667</td><td class="mid">1.000000 ± 1×10⁻⁷</td><td class="mid">constant ✓</td></tr>
<tr><th>an arbitrary power</th><td class="mid">0.3</td><td class="mid">1.000000 ± 3×10⁻⁸</td><td class="mid">constant ✓</td></tr>
<tr class="hi"><th>\(c\cdot t=\)const</th><td class="mid">1.0</td><td class="mid">1.000000 ± 1×10⁻¹³</td><td class="mid">constant ✓</td></tr>
</tbody>
</table>
</div>

<p>Every one passes. <strong>Even in a radiation-dominated universe, \(c\cdot t\) can be held exactly constant.</strong> Up to here, Position A is entirely correct.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>So what is that clock?</h2>

<p>What differs is the content of \(T\). For \(p\ne1\) we have \(\eta\propto t^{1-p}\); for \(p=1\), \(\eta\propto\ln t\). Hence —</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Universe</th><th class="mid">conformal time \(\eta\)</th><th class="mid">the clock \(T\) that realises \(c\cdot t=\)const</th></tr></thead>
<tbody>
<tr><th>radiation</th><td class="mid">\(\propto t^{1/2}\)</td><td class="mid">\(T\propto e^{\sqrt{t}}\)</td></tr>
<tr><th>matter</th><td class="mid">\(\propto t^{1/3}\)</td><td class="mid">\(T\propto e^{t^{1/3}}\)</td></tr>
<tr class="hi"><th>\(a\propto t\)</th><td class="mid">\(\propto\ln t\)</td><td class="mid">\(T\propto t\)　<strong>← the age of the universe itself</strong></td></tr>
</tbody>
</table>
</div>

<p>In a radiation universe the \(T\) that makes \(c\cdot t=\text{const}\) work is \(e^{\sqrt t}\). That is a perfectly good time coordinate, but <strong>it is nobody's clock</strong>. Atomic clocks tick proper time, and "how many seconds since the universe began" is \(t\).</p>

<h2><span class="n">05</span>The core — exactly one claim survives</h2>

<div class="calc">
<span class="tag">What is left</span>
$$\frac{d\ln T}{d\ln t}=\frac{c_0}{C}\cdot\frac{t}{a}\ \propto\ t^{\,1-p}$$
<p class="lbl">and this is constant (i.e. \(T\) proportional to the age) only when</p>
$$p=1$$
</div>

<p>And \(T/t\) is a <strong>ratio of two times</strong> — dimensionless. So without breaking Position A's premise by so much as a step, this one quantity is exposed to observation.</p>

<div class="keybox">
<p class="lbl">The result of this episode</p>
<p style="margin:6px 0 0"><strong>That the \(t\) in "\(c\cdot t=\text{const}\)" is the age of the universe — that single clause is the physics.</strong><br>
Everything else was bookkeeping.</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th>claim</th><th class="mid">verdict</th></tr></thead>
<tbody>
<tr><th>first half</th><td>there exists a time coordinate making \(c\cdot t\) constant</td><td class="mid"><strong>always true</strong> (today's \(T=e^{\eta/\eta_0}\))</td></tr>
<tr class="hi"><th>second half</th><td>that time coordinate is the age of the universe</td><td class="mid"><strong>equivalent to \(p=1\)</strong>; observation decides</td></tr>
</tbody>
</table>
</div>

<p>And every "selling point" this series and the last have listed uses <em>the second half, without exception</em> — the \(t\) in \(R_h=ct\), \(dR_H/dt=c\), the 140-step clock, \(\Omega/N\) (Ep.1), the two clocks (Ep.2). None of them can even be written without assuming \(t\) is the age of the universe.</p>

<div class="aside">
<span class="tag">So A and B were never in conflict</span>
Rearranged, the earlier argument comes out like this.<br>
Hold <strong>A</strong> (move no dimensionless quantity) and \(c\cdot t=\text{const}\) becomes the declaration "I have chosen the time coordinate \(e^{\eta/\eta_0}\)" — <em>content zero</em>. It cannot fail, but neither does it solve the horizon problem nor say \(R_h=ct\).<br>
Take <strong>B</strong> (assert the selling points) and you are saying that clock is the age of the universe, i.e. \(p=1\). The dimensionless \(T/t\) moves, so observation decides.<br>
They are not two positions but <strong>one equation, \(d\ln T/d\ln t=1\), either imposed or not</strong>.
</div>

<div class="fig">
<p class="cap">Figure: the upper panel is \(c_B\cdot T\) — turn the knob however you like and it stays <strong>perfectly flat</strong> (Position A is correct). The lower panel is \(d\ln T/d\ln t\) — it pins to 1, meaning <strong>that clock becomes the age of the universe</strong>, only at \(p=1\)</p>
<canvas id="cv" width="720" height="400"></canvas>
<div class="controls">
  <label>expansion index \(p\) (\(a\propto t^{p}\))<input id="sp" type="range" min="200" max="1400" value="500" step="1"></label>
  <span class="val" id="vp">p = 0.500</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3b3050"></i>\(c_B\cdot T\) (= 1, always)</span>
  <span><i class="swatch" style="background:#996515"></i>\(d\ln T/d\ln t\)</span>
  <span><i class="swatch" style="background:#9aa0ae"></i>"matches the age of the universe"</span>
</div>
</div>

<p>The upper band stays flat wherever you put the knob. <strong>That is what "a rewriting moves nothing" looks like.</strong> Only the lower band moves, and the gold curve lies exactly on the grey line only at \(p=1\); elsewhere its slope drifts with epoch — <em>meaning that clock runs at a different rate from the age of the universe</em>.</p>

<h2><span class="n">06</span>The tenth characterisation — three clocks coincide</h2>

<p>Something else happens at \(p=1\). As Episode 3 of the previous series showed, \(a\propto t\) gives conformal time \(\eta=t_0\ln(t/t_0)\), hence \(a=e^{\eta/t_0}\). The clock we built here is \(T=e^{\eta/\eta_0}\). Take \(\eta_0=t_0\) and —</p>

<div class="calc">
<span class="tag">All three line up</span>
$$a\;=\;e^{\eta/t_0}\;=\;T\;\propto\;t$$
</div>

<div class="seven">
<div class="row hi"><div class="mk">⑩</div><div class="txt"><strong>The scale factor, the \(c\cdot t=\)const clock, and the age of the universe are all proportional</strong><span>For any other expansion law the three come apart (radiation gives \(a\propto t^{1/2}\), \(T\propto e^{\sqrt t}\), and \(t\) — three different shapes)</span></div></div>
</div>

<p>Episode 1 added ⑧ (operations per bit) and Episode 2 added ⑨ (the two clocks meshing 1:1). ⑩ has the same shape ── <strong>every property \(a\propto t\) gathers is of the form "separate clocks falling into step"</strong>. That is why this auxiliary line is beautiful, and also why it is <em>making too many things agree</em>.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">07</span>The reveal — why "a constant length" is empty</h2>

<p>There is a plainer way to say all of this. \(c\cdot t\) is a <strong>length</strong>. Dimensionful. By the previous series' motto, dimensionful quantities are bookkeeping.</p>

<p>To call a bookkeeping quantity "constant" you must say <em>constant compared to what</em>. A length can only be compared to a length. And the moment you compare, the thing becomes dimensionless.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>compare \(c\cdot t\) to what?</th><th class="mid">the dimensionless quantity you get</th><th class="mid">its actual value</th></tr></thead>
<tbody>
<tr><th>nothing at all</th><td class="mid">──</td><td class="mid">no claim exists (§§01–05)</td></tr>
<tr class="hi"><th>the horizon radius \(R_H\)</th><td class="mid">\(ct/R_H=p\)</td><td class="mid">0.51 (\(c\cdot t=\)const demands 1)</td></tr>
<tr><th>the Bohr radius \(a_B\)</th><td class="mid">\(ct/a_B\)</td><td class="mid">growing through \(10^{60}\) — this <em>is</em> redshift</td></tr>
</tbody>
</table>
</div>

<p>The second row is what the model actually wanted to say — \(R_h=ct\). <strong>The comparison was inside the name from the beginning.</strong> Melia's own label says so. And the instant you name the comparison, the statement becomes one about a dimensionless quantity and falls under observation's jurisdiction.</p>

<div class="aside">
<span class="tag">The decision procedure came for the title itself</span>
The previous series' finale concluded that only dimensionless invariants are entitled to answer. This episode applied that procedure to <em>the title of the series</em>. "\(c\cdot t=\text{const}\)" — dimensionful, therefore bookkeeping on its own. It becomes physics only once "\(/R_H\)" is supplied. <strong>The tool built over ten episodes ended up judging its own name.</strong>
</div>

<div class="caveat">
<span class="tag">Being straight with you</span>
<p style="margin:0 0 10px">Calling \(\Omega=1/a\) "forced" in §02 follows from choosing to set the spatial metric to the comoving grid with coefficient 1. Under a different convention (preserving proper distance, say) \(\Omega\) changes and so does the form of \(T\). What is shown here is that <em>under one natural convention there always exists a clock making \(c\cdot t\) constant</em> — not that such a clock is unique.</p>
<p style="margin:0 0 10px">\(T=e^{\eta/\eta_0}\) still carries the freedom of an integration constant (overall scale and origin). Also, for \(p<1\) conformal time \(\eta\) is bounded below, so \(T\) never reaches 0 — the "origin" of \(T\) does not correspond to the beginning of the universe. Episode 6 of the previous series (\(\eta\to-\infty\) only for \(w\le-1/3\)) is at work here too.</p>
<p style="margin:0 0 10px">"Time coordinates may be chosen freely" is standard general relativity and nothing here is new. What is new is the observation that <em>using that freedom up exactly produces \(c\cdot t=\text{const}\)</em>, together with the accounting that <strong>exactly one claim — "that clock is the age of the universe" — survives</strong>. That accounting is this series' reading, not a standard formulation.</p>
<p style="margin:0">Physical clocks (atomic clocks) tick proper time, not \(T\). "The universe is 13.8 billion years old" is also proper time. So identifying \(T\) with the age of the universe is a claim exposed to observation — which is the point of §05. On low-redshift fits, Melia and collaborators argue in favour of \(R_h=ct\) and the matter is unsettled; the verdict here concerns extrapolation into the early universe.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (everything you need is above)</p>
<ol>
<li>Find the clock \(T\) that realises \(c\cdot t=\text{const}\) in a radiation-dominated universe.
<details><summary>Show the answer</summary><div class="ans">\(a\propto t^{1/2}\), so \(\eta=\int dt/a\propto t^{1/2}\), and \(T=e^{\eta/\eta_0}\propto e^{\sqrt t}\). <strong>The exponential of the square root of the age</strong> — neither an atomic clock nor the age of the universe.</div></details></li>

<li>Why is there no freedom in \(\Omega=1/a\)?
<details><summary>Show the answer</summary><div class="ans">Because the spatial part becomes \(\Omega^2a^2dx^2\), and deciding that this shall be \(dx^2\) (the comoving grid as it stands) fixes \(\Omega=1/a\). <em>The only freedom left is the time coordinate</em>, and \(c_B\cdot T=C\) uses exactly that one degree of freedom up.</div></details></li>

<li>Why is "\(c\cdot t\) is constant", by itself, not yet a claim?
<details><summary>Show the answer</summary><div class="ans">Because \(c\cdot t\) is a <strong>length</strong> — dimensionful. Whether a length is constant cannot be said without naming what it is compared to, and the moment you compare, the quantity is dimensionless and becomes physics. The previous series' motto — dimensionful is bookkeeping, dimensionless is physics — applies to the title of the series itself.</div></details></li>

<li>Name the three clocks that coincide at \(p=1\).
<details><summary>Show the answer</summary><div class="ans">① the scale factor \(a\); ② the clock \(T=e^{\eta/t_0}\) that realises \(c\cdot t=\text{const}\); ③ the age of the universe \(t\). For \(a\propto t\) we have \(\eta=t_0\ln(t/t_0)\), hence \(a=e^{\eta/t_0}=T\propto t\), all three proportional. For any other \(p\) they are three different functions.</div></details></li>

<li>(Harder) Can any of the model's selling points be asserted while holding Position A?
<details><summary>Show the answer</summary><div class="ans">None of them. Every selling point is a claim about a dimensionless quantity — \((dR_H/dt)/c=1\), one causal patch, \(w=-1/3\), \(\Omega/N=\ln2/2\pi^2\), \(\mathcal{N}_T/\mathcal{N}_t=1\). Hold A and they all revert to their observed values, and you are left <strong>writing the actual universe in odd units</strong>. <em>It cannot fail, and it says nothing.</em> That you cannot have both is the most awkward — and most interesting — property of this auxiliary line.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary　The comparison was hidden inside the name</h2>
<p>"A rewriting moves no dimensionless quantity, so it cannot fail" — we pushed that objection to the end. Pushed far enough, <strong>\(c\cdot t=\text{const}\) can be realised in any universe</strong>. Conformally transform with \(\Omega=1/a\), then take the time coordinate \(T=e^{\eta/\eta_0}\) (the exponential of conformal time), and \(c_B\cdot T\) is exactly constant. Verified numerically too — 1.000000 for radiation, for matter, for \(p=0.3\).</p>
<p>What differs is the content of \(T\): \(T\propto e^{\sqrt t}\) in a radiation universe, \(T\propto e^{t^{1/3}}\) in a matter universe — perfectly good coordinates, but nobody's clock. <strong>\(T\) is proportional to the age of the universe only at \(p=1\)</strong>, the condition being \(d\ln T/d\ln t\propto t^{1-p}\). And \(T/t\) is a ratio of two times — dimensionless. <em>Without breaking Position A's premise at all, that is the one thing observation can reach.</em></p>
<p>So the name folded two claims together. First half, "such a time coordinate exists" — <strong>always true, content zero</strong>. Second half, "that time coordinate is the age of the universe" — <strong>equivalent to \(p=1\), decided by observation</strong>. And every selling point in this series and the last uses the second half, without exception.</p>
<p>The reveal was simpler still. \(c\cdot t\) is a length: dimensionful, bookkeeping. <em>To call it constant you need something to compare it with.</em> Compare it to the horizon radius and you get \(ct/R_H=p\), the claim that this equals 1 ── which is exactly what Melia's label \(R_h=ct\) said all along. The decision procedure built over ten episodes ended by judging the series' own title. And as a bonus, at \(p=1\) <strong>the scale factor, this clock, and the age of the universe all become proportional</strong> (the tenth characterisation) — this auxiliary line is forever making too many things agree.</p>
</div>

<div class="next">
<span class="lbl">Next time ── Episode 4</span>
With the name sorted out, we return to what the notation is for. Erase everything a conformal transformation can erase — the expansion of space, the curvature, the temperature, the light — and <em>exactly one thing that varies in time is left</em>. Cosmic history collapses to "a growing mass overtaking a fixed \(k_BT_0\)", and distances and ages become closed forms with no integrals at all. <strong>A prediction with zero dimensionless parameters.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sp=document.getElementById('sp'), vp=document.getElementById('vp'), ro=document.getElementById('ro');
  var X0=76, X1=700;
  var A0=34, A1=140, B0=196, B1=330;
  var xmin=-3, xmax=0;
  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function pyA(v){ return A1-(v-0)/(1.6-0)*(A1-A0); }
  function pyB(v){ var lo=-2.2, hi=0.9; var l=Math.log(v)/Math.LN10;
                   l=Math.max(lo,Math.min(hi,l)); return B1-(l-lo)/(hi-lo)*(B1-B0); }
  function draw(){
    var p=parseInt(sp.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.fillStyle='#3b3050'; g.textAlign='left';
    g.font='bold 12px sans-serif';
    g.fillText('upper: c_B · T  —  what the rewriting does not move', X0, A0-12);
    g.font='11px sans-serif';
    g.strokeStyle='#ded8e6'; g.lineWidth=1;
    [0,0.5,1.0,1.5].forEach(function(v){
      var y=pyA(v); g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#9a93a8'; g.textAlign='right'; g.fillText(v.toFixed(1), X0-8, y+4);
    });
    g.strokeStyle='#3b3050'; g.lineWidth=3.2;
    g.beginPath(); g.moveTo(X0,pyA(1)); g.lineTo(X1,pyA(1)); g.stroke();
    g.fillStyle='#3b3050'; g.textAlign='left';
    g.fillText('1.000000 for every p (numerically verified)', X0+12, pyA(1)-9);
    g.strokeStyle='#cfc7dc'; g.lineWidth=1.1;
    g.beginPath(); g.moveTo(X0,A0-4); g.lineTo(X0,A1); g.lineTo(X1,A1); g.stroke();

    g.fillStyle='#996515'; g.font='bold 12px sans-serif';
    g.fillText('lower: d lnT / d lnt  —  is that clock the age of the universe?', X0, B0-12);
    g.font='11px sans-serif';
    [-2,-1,0].forEach(function(e){
      var y=pyB(Math.pow(10,e));
      g.strokeStyle='#ece7f2'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#9a93a8'; g.textAlign='right';
      g.fillText(e===0?'1':'0.'+(e===-1?'1':'01'), X0-8, y+4);
    });
    g.strokeStyle='#9aa0ae'; g.lineWidth=2; g.setLineDash([7,5]);
    g.beginPath(); g.moveTo(X0,pyB(1)); g.lineTo(X1,pyB(1)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#7d8492'; g.textAlign='right';
    g.fillText('T ∝ t  (matches the age of the universe)', X1-6, pyB(1)-8);
    g.strokeStyle='#996515'; g.lineWidth=3.2; g.beginPath();
    for(var i=0;i<=300;i++){
      var lx=xmin+(xmax-xmin)*i/300;
      var v=Math.pow(Math.pow(10,lx),1-p);
      if(i===0) g.moveTo(px(lx),pyB(v)); else g.lineTo(px(lx),pyB(v));
    }
    g.stroke();
    g.strokeStyle='#cfc7dc'; g.lineWidth=1.1;
    g.beginPath(); g.moveTo(X0,B0-4); g.lineTo(X0,B1); g.lineTo(X1,B1); g.stroke();
    g.textAlign='center'; g.fillStyle='#9a93a8';
    [-3,-2,-1,0].forEach(function(e){ g.fillText(e===0?'now':'10^'+e, px(e), B1+16); });
    g.fillStyle='#6a6280';
    g.fillText('age of the universe   t / t₀', (X0+X1)/2, B1+36);
    var early=Math.pow(1e-3,1-p);
    vp.textContent='p = '+p.toFixed(3);
    var tag = Math.abs(p-0.5)<0.0006?' (radiation)':(Math.abs(p-2/3)<0.0006?' (matter)':
              (Math.abs(p-1)<0.0006?' (c·t=const)':''));
    ro.textContent='p = '+p.toFixed(3)+tag+
      '　clock T = exp(η/η₀)'+
      (Math.abs(p-1)<0.0006
        ? '　→　T ∝ t　★ the age of the universe itself (d lnT/d lnt pinned at 1)'
        : '　→　T ∝ exp(t^'+(1-p).toFixed(3)+')　d lnT/d lnt runs from '+early.toPrecision(3)+' to 1 (not the age)')+
      '　／　c_B·T is constant either way';
  }
  sp.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-03-whichclock.html', acc='#3b3050', ops='#996515',
      title='c·t=const can be realised in any universe ── c·t = const, That Clicks, Episode 3',
      ep='EPISODE 3 ／ Questioning the name of the series head-on',
      eyebrow="From a reader: \"if it is only a change of coordinates, how can it fail?\"",
      h1='\\(c\\cdot t=\\)const can be<br>realised in any universe',
      sub='In a radiation universe, in a matter universe — \\(c\\cdot t\\) can be held exactly constant,<br>just by choosing the time coordinate. <em>So what was this model claiming?</em>',
      byline_l='What you need: one derivative, conformal time',
      byline_r='\\(T=e^{\\eta/\\eta_0}\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 3 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That FLRW metrics are conformally flat, the definition of conformal time \\(\\eta=\\int dt/a\\), and the freedom to change time coordinates in general relativity are all standard. The result \\(T=\\exp(\\eta/\\eta_0)\\) — that a time coordinate realising \\(c_B\\cdot T=\\text{const}\\) exists for any \\(a(t)\\) — and the fact that \\(d\\ln T/d\\ln t\\propto t^{1-p}\\) is constant only for \\(p=1\\), are derived here. The numerical check in §03 built \\(a=(t/t_0)^p\\) on 4001 points, integrated \\(\\eta\\) by the trapezoidal rule, differentiated \\(T\\) numerically and reassembled \\(c_B=c_0/(aT\')\\); the relative scatter in \\(c_B\\cdot T\\) was below \\(10^{-7}\\). That \\(\\Omega=1/a\\) is forced holds under the convention that the spatial metric is the comoving grid with unit coefficient; other conventions change it. For \\(p<1\\) conformal time is bounded below, so \\(T\\) never reaches 0 (corresponding to the \\(w\\le-1/3\\) condition of Episode 6 of the previous series). That the scale factor, \\(T\\), and the age of the universe all become proportional at \\(p=1\\) is also noted here. The label \\(R_h=ct\\) is due to Melia; on low-redshift fits Melia and collaborators argue in its favour, while extrapolation into the early universe conflicts with nucleosynthesis (Lewis, Barnes &amp; Kaushik 2016, MNRAS 460, 291). Physical clocks tick proper time, not the \\(T\\) of this episode. The reading that "two claims are folded into one name" is this series\' own, not a standard formulation. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the expansion law: the upper panel never moves, only the lower one does. "Show the answer" opens each solution.')
