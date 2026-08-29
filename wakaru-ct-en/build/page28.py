# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">The second patient of Part IV is <strong>VSL (variable speed of light)</strong>. It is the theory closest to this series, <em>which is exactly why the surgery cuts so well</em>. Inside "the speed of light was faster in the past" there are again two different things — <strong>a change of units</strong> and <strong>a claim that a dimensionless quantity moves</strong>. Cut them apart and it becomes clear where VSL's surgery <em>went wrong</em>. The answer first: <strong>the failure was not moving \(c\), but continuing to call it \(c\).</strong></p>

<h2><span class="n">01</span>There are four \(c\)s to begin with</h2>

<p>Before cutting, check what is being cut. The \(c\) called "the speed of light" in fact appears <strong>four times, in four different roles</strong>.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Which \(c\)</th><th class="mid">What it does</th></tr></thead>
<tbody>
<tr><th>the \(c\) in Maxwell's equations</th><td class="mid">the propagation speed of electromagnetic waves</td></tr>
<tr><th>the \(c\) in the Lorentz transformation</th><td class="mid">causal structure — the tilt of the light cone</td></tr>
<tr><th>the \(c\) in \(E=mc^2\)</th><td class="mid">the conversion factor between mass and energy</td></tr>
<tr><th>the \(c\) in the Einstein equations</th><td class="mid">the coupling of curvature to matter, \(8\pi G/c^4\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0">In principle these four are <strong>separately movable quantities</strong>.<br>
So "\(c\) varies" <em>does not say which one varies</em> — the point made by Ellis &amp; Uzan (2005).<br>
<strong>There were not two things to operate on but four or more.</strong></p>
</div>

<h2><span class="n">02</span>What VSL actually claims is a variation of \(\alpha\)</h2>

<p>VSL (Albrecht &amp; Magueijo 1999, among others) makes the choice explicitly — <strong>hold \(e\) and \(\hbar\) fixed and move \(c\)</strong>. The fine structure constant then comes along.</p>

<div class="calc">
<span class="tag">The dimensionless quantity that follows</span>
$$\alpha=\frac{e^2}{4\pi\varepsilon_0\hbar c}\qquad\Longrightarrow\qquad \frac{\Delta\alpha}{\alpha}=-\frac{\Delta c}{c}$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0"><strong>The observable content of "the speed of light varies" is, entirely, "\(\alpha\) varies".</strong><br>
── When Extra 3 of the previous series said "VSL collides with atomic clocks", this one line was the substance.</p>
</div>

<h2><span class="n">03</span>How tightly is \(\alpha\) pinned?</h2>

<p>Following Episode 19's practice, convert to bits — <em>a bound of \(10^{-n}\) means \(\log_2(10^n)\) bits are pinned down</em>.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Measurement</th><th class="mid">Epoch</th><th class="mid">Bound on \(|\Delta\alpha/\alpha|\)</th><th class="mid">Bits pinned</th></tr></thead>
<tbody>
<tr class="hi"><th>Laboratory (CODATA 2022)</th><td class="mid">today</td><td class="mid">\(1.6\times10^{-10}\)</td><td class="mid"><strong>32.5 bit</strong></td></tr>
<tr><th>Atomic clocks (13.8 Gyr extrapolation)</th><td class="mid">\(z\simeq0\)</td><td class="mid">\(1.4\times10^{-8}\)</td><td class="mid">26.1 bit</td></tr>
<tr class="hi"><th>Oklo natural reactor</th><td class="mid">1.8 Gyr ago</td><td class="mid">\(1.1\times10^{-8}\)</td><td class="mid"><strong>26.4 bit</strong></td></tr>
<tr><th>Quasar absorption lines</th><td class="mid">\(z\sim2\)</td><td class="mid">\(1.0\times10^{-5}\)</td><td class="mid">16.6 bit</td></tr>
<tr><th>CMB</th><td class="mid">\(z=1100\)</td><td class="mid">\(4.0\times10^{-3}\)</td><td class="mid">8.0 bit</td></tr>
<tr><th>Nucleosynthesis</th><td class="mid">\(z=4\times10^{8}\)</td><td class="mid">\(1.0\times10^{-2}\)</td><td class="mid">6.6 bit</td></tr>
</tbody>
</table>
</div>

<p>In the recent universe <strong>26 bits</strong> are held down, and even at nucleosynthesis <strong>6.6 bits</strong>. On Episode 19's scale, this is a quantity <em>known not to move to a precision exceeding Koide's relation (15.7 bits)</em>.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The heart — how much must \(c\) change to solve the horizon problem?</h2>

<p>VSL's selling point is solving the horizon problem without inflation. How much change does that take? Rewrite Episode 27's particle horizon for a varying \(c\).</p>

<div class="calc">
<span class="tag">Two lines</span>
<p class="lbl">with \(c=c_0(a/a_0)^n\), in the radiation era (\(a\propto t^{1/2}\), \(dt\propto a\,da\))</p>
$$\chi=\int\frac{c\,dt}{a}\ \propto\ \int a^{n}\,da=\frac{a^{n+1}}{n+1}$$
<p class="lbl">divergence as \(a\to0\) requires</p>
$$\boxed{\ n<-1\ }\qquad(\text{the standard }n=0\text{ gives }\chi\propto a\text{, which does not diverge})$$
</div>

<p>So VSL requires that, going back, <strong>\(c\) grows at least as fast as \(1/a\)</strong>. Since \(\alpha\propto1/c\propto a^{-n}\) —</p>

<div class="calc">
<span class="tag">The required variation of \(\alpha\)</span>
$$\frac{\alpha(z)}{\alpha_0}\ \ge\ 1+z$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Epoch</th><th class="mid">\(1+z\)</th><th class="mid">Required \(\Delta\alpha/\alpha\)</th><th class="mid">Times the observational bound</th></tr></thead>
<tbody>
<tr><th>Oklo (1.8 Gyr ago)</th><td class="mid">1.14</td><td class="mid">0.14</td><td class="mid">\(1.3\times10^{7}\)×</td></tr>
<tr><th>Quasars (\(z\sim2\))</th><td class="mid">3.0</td><td class="mid">2.0</td><td class="mid">\(2.0\times10^{5}\)×</td></tr>
<tr><th>CMB (\(z=1100\))</th><td class="mid">1101</td><td class="mid">1100</td><td class="mid">\(2.8\times10^{5}\)×</td></tr>
<tr class="hi"><th>Nucleosynthesis (\(z=4\times10^8\))</th><td class="mid">\(4\times10^{8}\)</td><td class="mid">\(4\times10^{8}\)</td><td class="mid"><strong>\(4\times10^{10}\)×</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>Observation excludes solving the horizon problem with a smooth power-law VSL.</strong><br>
At nucleosynthesis the requirement is \(4\times10^8\) against a bound of \(10^{-2}\) — <em>ten orders of magnitude over</em>.<br>
And even at Oklo, 1.8 billion years ago, it is already seven orders short.</p>
</div>

<h2><span class="n">05</span>The VSL that survives — and the price of surviving</h2>

<p>Yet VSL is not dead, because Albrecht and Magueijo propose <em>not a power law but a phase transition</em> — <strong>\(c\) drops abruptly at some moment and is constant thereafter</strong>.</p>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>Put the transition before nucleosynthesis and none of §03's bounds apply</strong><span>there is no \(\alpha\) data at \(z>4\times10^8\)</span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>The horizon problem is still solved</strong><span>it suffices that \(c\) was large enough before the transition (\(10^{32}\)× if placed at the Planck era)</span></div></div>
<div class="row hi"><div class="mk">✗</div><div class="txt"><strong>The price: zero predictions in the observable era</strong><span>after nucleosynthesis \(\alpha\) is exactly constant — <em>indistinguishable from standard cosmology</em></span></div></div>
</div>

<div class="fig">
<p class="cap">Figure: redshift across, \(|\Delta\alpha/\alpha|\) up. <strong>Grey points are observational bounds, and the region above them is excluded.</strong> Move the transition epoch with the slider — <em>the instant it escapes the data, its predictions in the observable era go to zero as well</em>.</p>
<canvas id="cv" width="720" height="390"></canvas>
<div class="controls">
  <label>Where to put the transition, \(\log_{10}(1+z_t)\)<input id="sz" type="range" min="0" max="320" value="30" step="1"></label>
  <span class="val" id="vz">1+z = 1000</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3f2a4a"></i>\(\Delta\alpha/\alpha\) for phase-transition VSL</span>
  <span><i class="swatch" style="background:#7a8a2a"></i>power-law VSL (\(n=-1\))</span>
  <span><i class="swatch" style="background:#9a9098"></i>observational bounds (above is excluded)</span>
</div>
</div>

<p>Drag the slider right to make the transition earlier and the violet curve slips under the grey points. But <strong>the moment it does, the curve sits on the floor (\(\Delta\alpha/\alpha=0\)) across every observable epoch</strong>. <em>Escaping exclusion and losing predictions were the same operation.</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">06</span>The reveal — three fates</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">Does \(\alpha\) move?</th><th class="mid">Collision with observation</th><th class="mid">Predictions</th></tr></thead>
<tbody>
<tr><th>Power-law VSL</th><td class="mid">yes (\(O(1)\))</td><td class="mid">ten orders over at nucleosynthesis</td><td class="mid"><strong>falsified</strong></td></tr>
<tr><th>Phase-transition VSL</th><td class="mid">only before nucleosynthesis</td><td class="mid">none</td><td class="mid">zero in the observable era</td></tr>
<tr class="hi"><th>c·t=const (conformal)</th><td class="mid"><strong>exactly invariant</strong></td><td class="mid">none</td><td class="mid">notation; zero in itself</td></tr>
</tbody>
</table>
</div>

<p>The same words, "the speed of light varies", <strong>split three ways depending on what you hold fixed</strong>. Episode 9's Exercise 5 — "VSL is killed by atomic clocks and this picture is not" — was rows one and three of this table. Today the middle row is added.</p>

<div class="keybox">
<p class="lbl">Conclusion of §06 — the result of the surgery</p>
<p style="margin:6px 0 0">The contents of "the speed of light varies" are exactly Episode 3's two ──<br>
<strong>(A) a change of units</strong> (says nothing) and <strong>(B) a claim that a dimensionless quantity moves</strong> (observable).<br>
VSL chose (B) but <em>kept the name of (A)</em>.<br>
── <strong>The right name is "variable \(\alpha\) theory".</strong></p>
</div>

<div class="aside">
<span class="tag">Where the surgery went wrong</span>
VSL <strong>did the surgery halfway</strong>. It correctly recognised that "\(c\) alone is not enough" and fixed \(e\) and \(\hbar\) — that much matches Episode 3. But <em>it did not change the name</em>. As a result, the phrase "the speed of light varies" hides the content ("\(\alpha\) varies"), and the <strong>26 bits of constraint</strong> from measurements of \(\alpha\) stop being visible head on. <em>The failure was not moving \(c\), but continuing to call it \(c\).</em>
</div>

<h2><span class="n">07</span>Not to be confused — the running of \(\alpha\)</h2>

<div class="calc">
<span class="tag">This is not a time variation</span>
$$\alpha^{-1}(0)=137.036\ \longrightarrow\ \alpha^{-1}(M_Z)=127.951\qquad(\text{a difference of }6.6\%)$$
</div>

<p>This is the renormalisation-group running seen in Episodes 11 and 14. It is <strong>a dependence on energy scale</strong>, <em>not a variation in time</em>. Every bound in §03 asks whether \(\alpha\), measured at the same energy scale, has moved over cosmic time — <strong>a different axis</strong>, and confusing them means comparing 6.6% with \(10^{-8}\). The same separation Episode 21 made in putting the a-theorem on another axis.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① "There are four \(c\)s" is Ellis &amp; Uzan's (2005) account.</strong> Which \(c\) you vary changes the theory, and this document follows only the choice in which \(\alpha\) varies. A VSL that varies the Lorentz-transformation \(c\) — that is, the causal structure itself — requires a separate discussion.</p>
<p style="margin:0 0 10px"><strong>② §03's bounds are a summary of representative values.</strong> For quasar absorption lines, Webb and collaborators have claimed a <em>significant</em> variation of \(\Delta\alpha/\alpha\simeq-0.6\times10^{-5}\), with Keck and VLT disagreeing in sign, and <strong>the debate continues</strong>. The \(10^{-5}\) used here is a conservative summary bound, not a single measurement. The CMB and nucleosynthesis bounds also move by factors of a few depending on how degeneracies with other parameters are handled.</p>
<p style="margin:0 0 10px"><strong>③ The condition \(n<-1\) in §04 assumes radiation domination and a power-law \(c(a)\).</strong> Varying \(c\) also changes the equation for \(H\), so strictly one must solve a modified Friedmann equation — <em>this is an order-of-magnitude argument</em> looking only at whether the horizon diverges.</p>
<p style="margin:0 0 10px"><strong>④ "Phase-transition VSL has zero predictions in the observable era" concerns \(\alpha\).</strong> There are formulations giving VSL other predictions (fluctuation spectra, its approach to the flatness problem), which are tested separately — <em>the claim here is the single point that measurements of \(\alpha\) cannot distinguish it</em>.</p>
<p style="margin:0"><strong>⑤ This episode does not refute VSL.</strong> It counts that the power-law version is excluded and that the phase-transition version escapes the \(\alpha\) measurements. <em>The purpose of the surgery is to name the comparison hidden inside a name.</em></p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Why is "the speed of light varies" not a claim by itself?
<details><summary>Show the answer</summary><div class="ans">Because \(c\) is dimensionful — bookkeeping — so <strong>it means nothing until you say what is held fixed</strong>. And \(c\) appears in four separate places (Maxwell, the Lorentz transformation, \(E=mc^2\), the Einstein equations), so <em>you must also say which \(c\)</em>.</div></details></li>

<li>What does VSL actually claim?
<details><summary>Show the answer</summary><div class="ans">Holding \(e\) and \(\hbar\) fixed while moving \(c\) makes \(\alpha=e^2/4\pi\varepsilon_0\hbar c\) move as \(\Delta\alpha/\alpha=-\Delta c/c\). <strong>The observable content is entirely "\(\alpha\) varies"</strong> — the right name is "variable \(\alpha\) theory".</div></details></li>

<li>Find the variation of \(c\) needed to solve the horizon problem.
<details><summary>Show the answer</summary><div class="ans">With \(c=c_0(a/a_0)^n\), \(\chi=\int c\,dt/a\propto\int a^n da=a^{n+1}/(n+1)\). Divergence as \(a\to0\) requires <strong>\(n<-1\)</strong>, so with \(\alpha\propto a^{-n}\), \(\alpha(z)/\alpha_0\ge1+z\).</div></details></li>

<li>Compare requirement and bound at nucleosynthesis.
<details><summary>Show the answer</summary><div class="ans">At \(z=4\times10^8\) the requirement is \(\Delta\alpha/\alpha\ge4\times10^8\) against a bound of \(10^{-2}\) — a ratio of <strong>\(4\times10^{10}\)</strong>, ten orders over, so <em>smooth power-law VSL is excluded</em>. Even Oklo, 1.8 Gyr ago, is already seven orders short.</div></details></li>

<li>(Harder) Why is phase-transition VSL not excluded, and at what price?
<details><summary>Show the answer</summary><div class="ans">Confining the variation of \(c\) to before nucleosynthesis (\(z>4\times10^8\)) puts it in <strong>a region where no \(\alpha\) data exist</strong>, so no bound applies. The price is that <em>it has zero predictions for \(\alpha\) in the observable era</em> — indistinguishable from standard cosmology. <strong>Escaping exclusion and losing predictions are the same operation.</strong></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — the failure was not moving \(c\)</h2>
<p>First we checked what was being cut: the \(c\) called "the speed of light" appears <strong>four times in four roles</strong> — Maxwell's equations, the Lorentz transformation, \(E=mc^2\), the Einstein equations. So "\(c\) varies" does not say which one (Ellis &amp; Uzan 2005).</p>
<p>VSL makes the choice explicitly — hold \(e\) and \(\hbar\), move \(c\). Then \(\Delta\alpha/\alpha=-\Delta c/c\), and <strong>the observable content is entirely "\(\alpha\) varies"</strong>. And \(\alpha\) is pinned to 32.5 bits in the laboratory, 26.4 bits at Oklo 1.8 billion years ago, and 6.6 bits even at nucleosynthesis — <em>on Episode 19's scale, known not to move to a precision beyond Koide's relation</em>.</p>
<p>The heart was §04. Solving the horizon problem requires the particle horizon \(\chi\propto a^{n+1}/(n+1)\) to diverge, i.e. \(n<-1\), which demands \(\alpha(z)/\alpha_0\ge1+z\). At nucleosynthesis that is a <strong>requirement of \(4\times10^8\) against a bound of \(10^{-2}\) — ten orders over</strong>. <em>Observation excludes solving the horizon problem with a smooth power-law VSL.</em></p>
<p>VSL is not dead, though: the phase-transition version confines the change of \(c\) to before nucleosynthesis. <strong>But escaping exclusion and losing predictions turned out to be the same operation</strong> — after nucleosynthesis \(\alpha\) is exactly constant and it is indistinguishable from standard cosmology.</p>
<p>And the result of the surgery. The contents of "the speed of light varies" are exactly Episode 3's two — <strong>(A) a change of units</strong> (says nothing) and <strong>(B) a claim that a dimensionless quantity moves</strong> (observable). <em>VSL chose (B) but kept the name of (A).</em> The right name is "variable \(\alpha\) theory". <strong>The failure was not moving \(c\), but continuing to call it \(c\).</strong></p>
</div>

<div class="next">
<span class="lbl">Next — Episode 29</span>
The next patient is <strong>MOND</strong>. "Below an acceleration of \(a_0=1.2\times10^{-10}\ \mathrm{m/s^2}\), Newton's law changes" — and that \(a_0\) is <em>dimensionful</em>, so Episode 3's surgery applies directly: <strong>small compared with what?</strong> Amusingly, when you look for something to make \(a_0\) dimensionless with, <em>\(cH_0\) is sitting right next door</em> (\(a_0/cH_0=0.18\)). Identity, coincidence or physics — Episode 19's procedure will sort it. <strong>And we watch the question "dark matter or MOND?" turn into Episode 5's balance: which reduces the description length?</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sz=document.getElementById('sz'), vz=document.getElementById('vz'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=34, Y1=316;
  var xmin=0, xmax=33;
  var ymin=-12, ymax=34;
  var BND=[[Math.log(1.14)/Math.LN10,-7.96,'Oklo'],
           [Math.log(3.0)/Math.LN10,-5.0,'quasars'],
           [Math.log(1101)/Math.LN10,-2.40,'CMB'],
           [Math.log(4.0e8)/Math.LN10,-2.0,'nucleosynthesis']];
  var LBBN=Math.log(4.0e8)/Math.LN10;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function draw(){
    var lzt=parseInt(sz.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.fillStyle='#f6f4f7';
    g.fillRect(px(LBBN), Y0, X1-px(LBBN), Y1-Y0);
    g.fillStyle='#a49aa8'; g.textAlign='center';
    g.fillText('no α data exists here', (px(LBBN)+X1)/2, Y0+16);

    g.textAlign='right';
    for(var e=-10;e<=30;e+=10){
      var y=py(e);
      g.strokeStyle=(e===0?'#ddd2e0':'#f4f0f6'); g.lineWidth=(e===0?1.5:1);
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a1959f'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=30;q+=5){
      var x=px(q);
      g.strokeStyle='#faf7fb'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a1959f'; g.fillText(q===0?'now':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#d6c8dc'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    g.fillStyle='rgba(154,144,152,0.16)';
    g.beginPath();
    g.moveTo(px(BND[0][0]),py(BND[0][1]));
    for(var i=1;i<BND.length;i++) g.lineTo(px(BND[i][0]),py(BND[i][1]));
    g.lineTo(px(LBBN),Y0); g.lineTo(px(BND[0][0]),Y0);
    g.closePath(); g.fill();

    g.strokeStyle='#9a9098'; g.lineWidth=2; g.setLineDash([5,4]);
    g.beginPath();
    for(var i=0;i<BND.length;i++){
      if(i===0) g.moveTo(px(BND[i][0]),py(BND[i][1])); else g.lineTo(px(BND[i][0]),py(BND[i][1]));
    }
    g.stroke(); g.setLineDash([]);
    for(var i=0;i<BND.length;i++){
      g.fillStyle='#6f6670';
      g.beginPath(); g.arc(px(BND[i][0]),py(BND[i][1]),4.5,0,6.2832); g.fill();
      g.fillStyle='#7d7480'; g.textAlign='left';
      g.fillText(BND[i][2], px(BND[i][0])+8, py(BND[i][1])-8);
    }

    g.strokeStyle='#7a8a2a'; g.lineWidth=2.6; g.setLineDash([7,4]);
    g.beginPath();
    g.moveTo(px(0.02),py(-1.7));
    g.lineTo(px(xmax),py(xmax));
    g.stroke(); g.setLineDash([]);
    g.fillStyle='#5f6b1e'; g.textAlign='right';
    g.fillText('power-law VSL (n = −1)', px(28), py(28)+16);

    g.strokeStyle='#3f2a4a'; g.lineWidth=3.4;
    g.beginPath();
    g.moveTo(px(0), py(ymin+0.6));
    g.lineTo(px(lzt), py(ymin+0.6));
    g.lineTo(px(lzt), py(Math.max(lzt,0)));
    g.lineTo(px(xmax), py(xmax));
    g.stroke();
    g.fillStyle='#3f2a4a';
    g.beginPath(); g.arc(px(lzt),py(Math.max(lzt,0)),5.5,0,6.2832); g.fill();
    g.strokeStyle='#fff'; g.lineWidth=1.8;
    g.beginPath(); g.arc(px(lzt),py(Math.max(lzt,0)),5.5,0,6.2832); g.stroke();

    g.fillStyle='#8a7f90'; g.textAlign='center';
    g.fillText('redshift  1 + z', (X0+X1)/2, Y1+36);
    g.save(); g.translate(19,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('|Δα/α|', 0,0); g.restore();

    var viol=false, worst=0, name='';
    for(var i=0;i<BND.length;i++){
      if(lzt<=BND[i][0]){
        var req=Math.pow(10,BND[i][0])-1;
        var lim=Math.pow(10,BND[i][1]);
        if(req/lim>worst){ worst=req/lim; name=BND[i][2]; }
        viol=true;
      }
    }
    vz.textContent='1+z = '+(Math.pow(10,lzt)<1e4?Math.pow(10,lzt).toPrecision(3):Math.pow(10,lzt).toExponential(1));
    ro.textContent='transition at 1+z = '+vz.textContent+'　→　'+
      (viol
        ? '★ at the '+name+' epoch Δα/α exceeds the bound by '+worst.toExponential(1)+'× — excluded'
        : 'not excluded (hidden where no α data exists)'+
          '　/　and at the same time Δα/α = 0 across every observable epoch — zero predictions');
  }
  sz.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-28-vsl.html', acc='#3f2a4a', ops='#7a8a2a',
      title='VSL — where the surgery went wrong ── c·t = const, That Clicks, Episode 28',
      ep='EPISODE 28 ／ Part IV — the theory standing closest to this one',
      eyebrow='The failure was not moving c, but continuing to call it c',
      h1='VSL — where the<br>surgery went wrong',
      sub='"The speed of light was faster in the past" holds two different things.<br><em>Cut them apart and the observable content is, entirely, "\\(\\alpha\\) varies".</em>',
      byline_l='What you need: the particle horizon, logarithms, Episode 19\'s practice',
      byline_r='\\(\\Delta\\alpha/\\alpha=-\\Delta c/c\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 28 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That \\(c\\) appears in several places in different roles, so that a VSL is undefined until one says <em>which</em> \\(c\\) varies, is the point of Ellis &amp; Uzan (2005, Am. J. Phys. 73, 240). VSL is due to Albrecht &amp; Magueijo (1999, PRD 59, 043516), Barrow (1999) and others. \\(\\alpha=e^2/4\\pi\\varepsilon_0\\hbar c\\) and \\(\\Delta\\alpha/\\alpha=-\\Delta c/c\\) under fixed \\(e,\\hbar\\) follow from the definition. §03\'s bounds summarise representative values: CODATA 2022\'s \\(\\alpha^{-1}=137.035999177(21)\\), the atomic-clock bound \\(|\\dot\\alpha/\\alpha|<1.0(1.1)\\times10^{-18}\\)/yr (Lange et al. 2021, PRL 126, 011102), the Oklo natural reactor, quasar absorption lines, the CMB and nucleosynthesis — <strong>for quasar absorption lines Webb and collaborators have claimed a significant variation, with Keck and VLT disagreeing in sign, and the debate continues</strong>. The \\(10^{-5}\\) used here is a conservative summary bound rather than a single measurement, and the CMB and nucleosynthesis bounds move by factors of a few with the treatment of degeneracies. The relation \\(\\chi\\propto a^{n+1}/(n+1)\\), the condition \\(n<-1\\), the requirement \\(\\alpha(z)/\\alpha_0\\ge1+z\\) and the excess factors (\\(4\\times10^{10}\\) at nucleosynthesis) are computed here (kenshou/calc32.py) — <em>varying \\(c\\) also changes the equation for \\(H\\), so strictly a modified Friedmann equation is needed; this is an order-of-magnitude argument about whether the horizon diverges</em>. "Phase-transition VSL has zero predictions in the observable era" concerns \\(\\alpha\\); other formulations give VSL further predictions, tested separately. The running of \\(\\alpha^{-1}\\) from 137.036 to 127.951 at \\(M_Z\\) is energy-scale dependence, not time variation (Episodes 11 and 14). <strong>This document does not refute VSL</strong>: it counts that the power-law version is excluded and that the phase-transition version escapes the \\(\\alpha\\) measurements, and names the comparison hidden inside a name. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, moving the transition epoch shows predictions vanishing at the instant exclusion is escaped. "Show the answer" opens each solution.')
