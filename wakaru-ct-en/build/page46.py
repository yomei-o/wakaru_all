# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Part VI <strong>puts the procedure itself under examination</strong>. First, we look head-on at the \(a\propto t\) this series has spent 45 episodes on — <em>how many different ways are there to say it?</em> We collect them all, count them, and count <strong>how many are independent</strong>. And what emerges is <em>why \(c\cdot t=\)const looked so plausible in the first place.</em></p>

<h2><span class="n">01</span>Collecting every way of saying \(a\propto t\)</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">No.</th><th>Statement</th><th class="mid">What it needs</th><th class="mid">Kind</th></tr></thead>
<tbody>
<tr><th class="mid">A1</th><td>\(a(t)\propto t\)</td><td class="mid">the definition itself</td><td class="mid">kinematic</td></tr>
<tr><th class="mid">A2</th><td>\(\ddot a=0\)</td><td class="mid">differentiate twice</td><td class="mid">kinematic</td></tr>
<tr><th class="mid">A3</th><td>deceleration parameter \(q=-\ddot aa/\dot a^2=0\)</td><td class="mid">a rewriting of A2</td><td class="mid">kinematic</td></tr>
<tr><th class="mid">A4</th><td>\(H=\dot a/a=1/t\)</td><td class="mid">differentiate once</td><td class="mid">kinematic</td></tr>
<tr class="hi"><th class="mid">A5</th><td>\(H\cdot t=1\)</td><td class="mid">a rewriting of A4 (<strong>dimensionless</strong>)</td><td class="mid">kinematic</td></tr>
<tr><th class="mid">A6</th><td>comoving Hubble radius \((aH)^{-1}\) constant</td><td class="mid">because \(aH=1\)</td><td class="mid">kinematic</td></tr>
<tr><th class="mid">A7</th><td>conformal time \(\eta=\int dt/a=\ln t\)</td><td class="mid">just integrate</td><td class="mid">kinematic</td></tr>
<tr><th class="mid">A8</th><td>Hubble radius \(c/H=c\,t\) exactly</td><td class="mid">a rewriting of A4</td><td class="mid">kinematic</td></tr>
<tr><th class="mid">A9</th><td>the particle horizon diverges</td><td class="mid">\(\int dt/t\) diverges</td><td class="mid">kinematic</td></tr>
<tr class="hi"><th class="mid">B1</th><td>equation of state \(w=-1/3\)</td><td class="mid"><strong>needs the Friedmann equations</strong></td><td class="mid">dynamical</td></tr>
<tr><th class="mid">C1</th><td>\(R=6(1+k)/t^2\) (Episode 33)</td><td class="mid"><strong>needs \(k\) as well</strong></td><td class="mid">geometric</td></tr>
<tr><th class="mid">C2</th><td>\(k=-1\) gives \(R=0\) (Milne)</td><td class="mid">a special case of C1</td><td class="mid">geometric</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0">Twelve in all. Of those, <strong>nine (A1–A9) are equivalent by kinematics alone</strong> — mere rewritings by differentiation and integration.<br>
── On Episode 19's scale, <em>A1 to A9 are 0 bits apart (identities)</em>.</p>
</div>

<h2><span class="n">02</span>How many independent inputs?</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>The expansion law \(a\propto t\)</strong><span>this alone yields all of A1–A9</span></div></div>
<div class="row"><div class="mk">2</div><div class="txt"><strong>The Einstein equations</strong><span>yields B1 (\(w=-1/3\)) — <em>dynamics are needed</em></span></div></div>
<div class="row hi"><div class="mk">3</div><div class="txt"><strong>The spatial curvature \(k\)</strong><span>yields C1 and C2 — <em>geometry as well</em></span></div></div>
</div>

<div class="calc">
<span class="tag">Compression</span>
$$\frac{12\ \text{statements}}{3\ \text{inputs}}=\mathbf{4.0\times}$$
</div>

<p>After Episode 26 (24 → 12), Episode 40 (three \(10^{122}\)s → one) and Episode 41 (four → one), this is <strong>the fourth compression</strong> — <em>and this time it is applied to the series' own subject.</em></p>

<h2><span class="n">03</span>The two \(a\propto t\)s are different things</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Which \(a\propto t\)</th><th class="mid">\(R\)</th><th class="mid">Riemann</th><th class="mid">In Episode 33</th></tr></thead>
<tbody>
<tr class="hi"><th>Milne (\(k=-1\), \(\rho=0\))</th><td class="mid">\(0\)</td><td class="mid"><strong>zero</strong></td><td class="mid">Step 1: Minkowski in disguise</td></tr>
<tr><th>\(k=0\) with \(w=-1/3\) matter</th><td class="mid">\(6/t^2\ne0\)</td><td class="mid">\(\ne0\)</td><td class="mid">Step 2: genuinely curved</td></tr>
</tbody>
</table>
</div>

<p><strong>"\(a\propto t\)" is one condition, but the spacetimes satisfying it are not one thing.</strong> <em>Empty, it is flat; with matter in it, it is curved</em> — the same expansion law, different spacetimes.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The core — which can be tested, and by how much do they miss?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Characterisation</th><th class="mid">Prediction</th><th class="mid">Observed</th><th class="mid">\(\sigma\)</th><th class="mid">bits</th></tr></thead>
<tbody>
<tr><th>\(q=0\) (A3)</th><td class="mid">\(0\)</td><td class="mid">\(-0.53\pm0.04\)</td><td class="mid">\(13.2\)</td><td class="mid">\(130\)</td></tr>
<tr><th>\(w=-1/3\) (B1)</th><td class="mid">\(-0.333\)</td><td class="mid">\(-1.03\pm0.03\)</td><td class="mid">\(23.2\)</td><td class="mid">\(395\)</td></tr>
<tr class="hi"><th>\(H_0t_0=1\) (A5, Planck)</th><td class="mid">\(1\)</td><td class="mid">\(0.951\pm0.007\)</td><td class="mid"><strong>\(6.8\)</strong></td><td class="mid"><strong>\(36\)</strong></td></tr>
<tr class="hi"><th>\(H_0t_0=1\) (A5, local)</th><td class="mid">\(1\)</td><td class="mid">\(1.030\pm0.014\)</td><td class="mid"><strong>\(2.1\)</strong></td><td class="mid"><strong>\(4.9\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>The Hubble tension straddles \(H_0t_0=1\) exactly.</strong><br>
Planck's value gives 0.951 (below); the local measurement gives 1.030 (above).<br>
── Meanwhile \(q=0\) misses by 13\(\sigma\) and \(w=-1/3\) by 23\(\sigma\) — <em>by orders of magnitude.</em></p>
</div>

<h2><span class="n">05</span>Why is \(H_0t_0=1\) the only near miss?</h2>

<div class="calc">
<span class="tag">Compute \(H_0t_0\) in \(\Lambda\)CDM</span>
$$H_0t_0=\frac{2}{3\sqrt{\Omega_\Lambda}}\,\mathrm{asinh}\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}=0.9510$$
<p class="lbl">\(a\propto t\) predicts 1 — <strong>a miss of only 4.9 per cent</strong></p>
</div>

<div class="seven">
<div class="row"><div class="mk">∫</div><div class="txt"><strong>\(H_0t_0\) integrates the whole history of the universe</strong><span>the decelerating and accelerating eras <em>cancel</em></span></div></div>
<div class="row"><div class="mk">now</div><div class="txt"><strong>\(q\) and \(w\) are quantities of this instant</strong><span>there is nothing for them to cancel against</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>Which is why \(c\cdot t=\)const looked plausible</strong><span>nearly right on the integrated observable, out by orders on the instantaneous ones — <em>and the previous series' verdict (it contradicts nucleosynthesis) was about that instantaneous side</em></span></div></div>
</div>

<div class="fig">
<p class="cap">Figure: \(\Lambda\)CDM's \(a(t)\) and the straight line \(a\propto t\). <strong>Match height and slope at today (right edge) and the middle still diverges</strong> — yet <em>by area (that is, by integral) they nearly agree</em>. Move the slider — <strong>\(q\) is the curvature of an instant; \(H_0t_0\) is the whole history.</strong></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>time \(t/t_0\)<input id="sq" type="range" min="5" max="100" value="100" step="1"></label>
  <span class="val" id="vq">1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6a4a2a"></i>\(\Lambda\)CDM \(a(t)\)</span>
  <span><i class="swatch" style="background:#2a4a5a"></i>\(a\propto t\) (\(q=0\))</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>today (\(t=t_0\))</span>
</div>
</div>

<h2><span class="n">06</span>The ledger</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Direction</th><th>What</th><th class="mid">Amount</th></tr></thead>
<tbody>
<tr><th class="mid">buys</th><td>the horizon problem disappears (A6 and A9)</td><td class="mid">──</td></tr>
<tr><th class="mid">buys</th><td>one fewer parameter</td><td class="mid">part of Episode 25's \(-148.3\)</td></tr>
<tr class="hi"><th class="mid">pays</th><td>\(q=0\) fails</td><td class="mid"><strong>\(130\) bits</strong></td></tr>
<tr class="hi"><th class="mid">pays</th><td>\(w=-1/3\) fails</td><td class="mid"><strong>\(395\) bits</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>The paying side is larger by orders of magnitude</strong> — <em>the same conclusion as Episode 25's ledger, reached by a different road.</em></p>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) §04's "1.030 with the local measurement" is not a calculation inside a consistent model.</strong> \(t_0=13.797\) Gyr comes from Planck's \(\Lambda\)CDM, and <em>multiplying a locally measured \(H_0\) by that \(t_0\) does not cohere</em> (change \(H_0\) and \(t_0\) changes too) — read it as <strong>an indication that a larger \(H_0\) can push \(H_0t_0\) above 1</strong>.</p>
<p style="margin:0 0 10px"><strong>(2) §04's \(\sigma\)s and bits simply combine the quoted errors.</strong> The \(\pm0.04\) on \(q_0\) and \(\pm0.03\) on \(w\) <em>depend on the analysis</em> and move with the treatment of systematics — the orders of magnitude (130, 395 bits) stand, but <strong>do not trust the significant figures</strong>. The value of \(q_0\) itself is obtained within \(\Lambda\)CDM.</p>
<p style="margin:0 0 10px"><strong>(3) §02's "4.0× compression" follows from having counted twelve statements.</strong> <em>The number of statements can be inflated or deflated at will</em> — the substance is the structure "nine are identities, three inputs are independent", and <strong>the number 4.0 itself means nothing</strong> (the same caution as Episode 26 §02).</p>
<p style="margin:0 0 10px"><strong>(4) §05's "integral versus instant" explains why it looks plausible; it does not defend \(a\propto t\).</strong> <em>Explaining why something looks plausible is not evidence that it is right</em> — if anything the opposite: <strong>knowing where the plausibility comes from makes the verdict clearer than before</strong>.</p>
<p style="margin:0"><strong>(5) This series' verdict has not changed since Episode 3.</strong> \(c\cdot t=\)const is <em>a notation, not new physics</em>, and extrapolated at face value to the early universe it contradicts nucleosynthesis (previous series). The academic standard is the \(\Lambda\)CDM model.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>Of the twelve statements, how many are identities of one another?
<details><summary>Show the answer</summary><div class="ans"><strong>Nine (A1–A9)</strong> — \(\ddot a=0\), \(q=0\), \(H=1/t\), \(Ht=1\), constant \((aH)^{-1}\), \(\eta=\ln t\), \(c/H=ct\), the diverging particle horizon. <em>They are rewritings by differentiation and integration, so 0 bits apart on Episode 19's scale.</em></div></details></li>

<li>How many independent inputs are there?
<details><summary>Show the answer</summary><div class="ans"><strong>Three</strong>: (i) the expansion law \(a\propto t\) (giving A1–A9), (ii) the Einstein equations (giving B1), (iii) the spatial curvature \(k\) (giving C1 and C2). <em>Twelve statements came from three inputs</em> — the fourth compression.</div></details></li>

<li>Are Milne and "\(k=0\) with \(w=-1/3\)" the same spacetime?
<details><summary>Show the answer</summary><div class="ans"><strong>No.</strong> Milne (\(k=-1\), \(\rho=0\)) has \(R=0\) and vanishing Riemann — <em>Minkowski in disguise</em> (Episode 33, Step 1). With \(k=0\) and \(w=-1/3\) matter, \(R=6/t^2\ne0\) and it is <em>genuinely curved</em> (Step 2).</div></details></li>

<li>Of \(q=0\), \(w=-1/3\) and \(H_0t_0=1\), which comes closest?
<details><summary>Show the answer</summary><div class="ans"><strong>\(H_0t_0=1\).</strong> Even with Planck's value it is 0.951 (<em>a 4.9 per cent miss</em>), and with the local measurement it becomes 1.030, straddling 1. Meanwhile \(q=0\) misses by 13\(\sigma\) and \(w=-1/3\) by 23\(\sigma\) — <em>by orders of magnitude.</em></div></details></li>

<li>(Harder) Why is \(H_0t_0\) the only near miss?
<details><summary>Show the answer</summary><div class="ans"><strong>Because it is an integral.</strong> \(H_0t_0\) integrates the whole history, so <em>the decelerating and accelerating eras cancel</em>. \(q\) and \(w\) are quantities of this instant, with nothing to cancel against — <strong>which is why \(c\cdot t=\)const looked plausible.</strong> Per caveat (4), this is not a defence of it.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: we found where the plausibility came from</h2>
<p>Collecting every way of saying \(a\propto t\) gives <strong>twelve statements</strong>, of which <strong>nine (A1–A9) are identities of one another</strong> — \(\ddot a=0\), \(q=0\), \(H=1/t\), \(Ht=1\), constant comoving Hubble radius, \(\eta=\ln t\), \(c/H=ct\), the diverging particle horizon. <em>All rewritings by differentiation and integration.</em> The rest are dynamical (\(w=-1/3\)) and geometric (\(R=6(1+k)/t^2\)), leaving <strong>three independent inputs</strong> — the <em>fourth compression</em>, after Episodes 26, 40 and 41.</p>
<p>And the same \(a\propto t\) covers two different spacetimes: <strong>Milne (\(k=-1\), empty) is flat, Minkowski in disguise; with \(k=0\) and matter it is genuinely curved</strong> — one condition does not fix one spacetime.</p>
<p>Only what sits in a dimensionless quantity can be tested. \(q=0\) misses by <strong>13\(\sigma\), 130 bits</strong>; \(w=-1/3\) by <strong>23\(\sigma\), 395 bits</strong> — <em>by orders of magnitude</em>. But \(H_0t_0=1\) is different — 0.951 with Planck's value (<strong>a 4.9 per cent miss</strong>), 1.030 with the local measurement. <strong>The Hubble tension straddles 1 exactly.</strong></p>
<p>Why is only one of them close? <strong>Because \(H_0t_0\) is an integral</strong> — integrating the whole history, <em>the decelerating and accelerating eras cancel</em>. \(q\) and \(w\) are quantities of this instant, with nothing to cancel against.</p>
<p><strong>Which is why \(c\cdot t=\)const looked plausible.</strong> Nearly right on the integrated observable, out by orders on the instantaneous ones — and the previous series' verdict (it contradicts nucleosynthesis) was about that instantaneous side. <em>Knowing where the plausibility comes from makes the verdict clearer than before.</em></p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 47</span>
This time only the characterisations placed in <strong>dimensionless quantities</strong> could be tested (\(q\), \(w\), \(H_0t_0\)). Next time we draw <strong>the map of dimensionless quantities</strong> — every one that appears in physics, laid out on one page, with the border between <em>what is physics and what is bookkeeping</em> drawn across it. And we look at <strong>where the International System of Units drew that line in 2019</strong> — the kilogram prototype was retired, and mass is now built from \(\hbar\). <em>The line this series drew by hand in Episode 3 turns out to be exactly where the world's metrology drew it too.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sq=document.getElementById('sq'), vq=document.getElementById('vq'), ro=document.getElementById('ro');
  var X0=76, X1=690, Y0=34, Y1=282;
  var Om=0.315, OL=0.685;
  var HT=2/(3*Math.sqrt(OL))*Math.log(Math.sqrt(OL/Om)+Math.sqrt(1+OL/Om));

  function aL(x){
    var k=Math.pow(Om/OL,1/3);
    var u=1.5*Math.sqrt(OL)*HT*x;
    var a=k*Math.pow((Math.exp(u)-Math.exp(-u))/2, 2/3);
    var u1=1.5*Math.sqrt(OL)*HT;
    var a1=k*Math.pow((Math.exp(u1)-Math.exp(-u1))/2, 2/3);
    return a/a1;
  }
  function px(x){ return X0+x*(X1-X0); }
  function py(a){ return Y1-a*(Y1-Y0); }

  function draw(){
    var xq=parseInt(sq.value,10)/100;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var v=0;v<=1.0001;v+=0.25){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(v)); g.lineTo(X1,py(v)); g.stroke();
      g.fillText(v.toFixed(2), X0-8, py(v)+4);
    }
    g.textAlign='center';
    for(var t=0;t<=1.0001;t+=0.2){ g.fillStyle='#9c96a4'; g.fillText(t.toFixed(1), px(t), Y1+20); }

    g.strokeStyle='#c8c2d0'; g.lineWidth=1.6; g.setLineDash([5,4]);
    g.beginPath(); g.moveTo(px(1),Y0); g.lineTo(px(1),Y1); g.stroke(); g.setLineDash([]);
    g.fillStyle='#a89fae'; g.textAlign='right'; g.fillText('today', px(1)-6, Y0+14);

    g.strokeStyle='#2a4a5a'; g.lineWidth=2.4; g.beginPath();
    g.moveTo(px(0),py(0)); g.lineTo(px(1),py(1)); g.stroke();
    g.strokeStyle='#6a4a2a'; g.lineWidth=2.8; g.beginPath();
    for(var i=0;i<=200;i++){ var x=i/200; if(i===0)g.moveTo(px(x),py(aL(x))); else g.lineTo(px(x),py(aL(x))); }
    g.stroke();

    g.textAlign='left';
    g.fillStyle='#6a4a2a'; g.fillText('LCDM a(t)', px(0.66), py(aL(0.66))-12);
    g.fillStyle='#2a4a5a'; g.fillText('a proportional to t  (q = 0)', px(0.26), py(0.26)+20);

    var aq=aL(xq);
    g.fillStyle='#6a4a2a'; g.beginPath(); g.arc(px(xq),py(aq),4.6,0,6.29); g.fill();
    g.fillStyle='#2a4a5a'; g.beginPath(); g.arc(px(xq),py(xq),4.6,0,6.29); g.fill();
    g.strokeStyle='#5a5262'; g.lineWidth=1.4; g.setLineDash([3,3]);
    g.beginPath(); g.moveTo(px(xq),Y0); g.lineTo(px(xq),Y1); g.stroke(); g.setLineDash([]);

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('time  t / t_0', (X0+X1)/2, Y1+44);
    g.save(); g.translate(22,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('scale factor a (today = 1)', 0,0); g.restore();

    vq.textContent=xq.toFixed(2);
    var d=(aq-xq);
    ro.textContent='t/t_0 = '+xq.toFixed(2)+
      '　→　LCDM a = '+aq.toFixed(3)+'　/　a proportional to t gives '+xq.toFixed(3)+
      '　/　difference '+(d>=0?'+':'')+d.toFixed(3)+
      (xq>0.98?'　★ height and slope are matched today — yet q is not 0':'')+
      (Math.abs(d)>0.05?'　※ the middle diverges, but the integral H_0 t_0 = 0.951 nearly agrees':'');
  }
  sq.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-46-characterisations.html', acc='#2a4a5a', ops='#6a4a2a',
      title='Every characterisation of a proportional to t ── c·t = const, That Clicks, Episode 46 (Part VI)',
      ep='EPISODE 46 ／ Part VI — examining the procedure',
      eyebrow='We found where the plausibility came from',
      h1='Twelve statements,<br>three inputs',
      sub='Collect every way of saying \\(a\\propto t\\) and count the independent ones.<br><em>And you find out why \\(c\\cdot t=\\)const looked so plausible.</em>',
      byline_l='What you need: Episode 19\'s scale, Episode 25\'s ledger, Episode 26\'s compression, Episode 33\'s three-step test',
      byline_r='Only \\(H_0t_0\\) misses by as little as 4.9 per cent',
      body=BODY + '\n\n<p class="foot">This document is Episode 46 of "c·t = const, That Clicks" (the first of Part VI), written for physics-minded high-school and university readers. The characterisations of \\(a\\propto t\\), the Milne universe and \\(H_0t_0\\) in \\(\\Lambda\\)CDM are all standard, and nothing here is a new claim — the numbers are computed in kenshou/calc50.py. <strong>§04\'s "1.030 with the local measurement" is not a calculation inside a consistent model</strong>: \\(t_0=13.797\\) Gyr comes from Planck\'s \\(\\Lambda\\)CDM, and multiplying a locally measured \\(H_0\\) by that \\(t_0\\) does not cohere (change \\(H_0\\) and \\(t_0\\) changes too) — <em>read it as an indication that a larger \\(H_0\\) can push \\(H_0t_0\\) above 1</em>. <strong>§04\'s significances simply combine the quoted errors</strong>; the \\(\\pm0.04\\) on \\(q_0\\) and \\(\\pm0.03\\) on \\(w\\) depend on the analysis, so the orders of magnitude stand but <em>the significant figures should not be trusted</em> (and \\(q_0\\) itself is obtained within \\(\\Lambda\\)CDM). <strong>§02\'s "4.0× compression" follows from having counted twelve statements</strong>, and <em>the count can be inflated or deflated at will</em> — the substance is the structure, not the number. <strong>§05\'s "integral versus instant" explains why it looks plausible and does not defend \\(a\\propto t\\)</strong> — knowing where plausibility comes from makes the verdict clearer, not weaker. <strong>This series\' verdict has not changed since Episode 3</strong>: \\(c\\cdot t=\\)const is a notation, not new physics, and extrapolated at face value to the early universe it contradicts nucleosynthesis. The academic standard is the \\(\\Lambda\\)CDM model. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the time and see the middle diverge while the integral nearly agrees. "Show the answer" opens each solution.')
