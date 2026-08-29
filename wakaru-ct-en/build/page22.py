# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">When Episode 1 took the universe's spec sheet, the operation count was left blank inside — the Margolus–Levitin limit counts only <em>transitions to orthogonal states</em> and does not ask what is being done. Today we fill that blank. <strong>The ML rate is proportional to energy, so operations are allocated exactly as energy is.</strong> Counted, the result is fairly exasperating — <em>95% of the operational budget goes to components in which nothing happens.</em></p>

<h2><span class="n">01</span>Operations are allocated as energy is</h2>

<div class="calc">
<span class="tag">Splitting the rate</span>
$$\frac{d\Omega}{dt}=\frac{2E}{\pi\hbar}\qquad\Longrightarrow\qquad \frac{d\Omega_i}{dt}=\frac{2E_i}{\pi\hbar}=\Omega_i\text{(energy fraction)}\times\frac{2E}{\pi\hbar}$$
</div>

<p>Since the rate is proportional to \(E\), <strong>the allocation of operational resources is exactly the universe's energy budget</strong>.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Component</th><th class="mid">Energy fraction</th><th class="mid">Operation rate today</th></tr></thead>
<tbody>
<tr class="hi"><th>Dark energy</th><td class="mid"><strong>68.5%</strong></td><td class="mid">\(3.27\times10^{103}\) /s</td></tr>
<tr><th>Dark matter</th><td class="mid">26.5%</td><td class="mid">\(1.26\times10^{103}\) /s</td></tr>
<tr><th>Baryons</th><td class="mid">4.9%</td><td class="mid">\(2.34\times10^{102}\) /s</td></tr>
<tr><th>Photons</th><td class="mid">0.0054%</td><td class="mid">\(2.58\times10^{99}\) /s</td></tr>
<tr><th>Neutrinos</th><td class="mid">0.0038%</td><td class="mid">\(1.81\times10^{99}\) /s</td></tr>
</tbody>
</table>
</div>

<h2><span class="n">02</span>The vacuum has nowhere to transition to</h2>

<p>One remark bites here. The \(E\) in the Margolus–Levitin limit is <strong>energy measured from the ground state</strong>. But the vacuum energy <em>is</em> that ground state.</p>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0"><strong>The vacuum has nowhere to transition to.</strong><br>
So it should not be counted as operations — <em>and with that one remark, 68.5% of the budget disappears.</em></p>
</div>

<p>That leaves 31.5%, of which <strong>84.1% is dark matter</strong>. As far as we know, dark matter <em>interacts only gravitationally</em> — there is nothing to change its state.</p>

<div class="calc">
<span class="tag">How much is actually doing something?</span>
$$\text{baryons}+\text{radiation}=4.909\%\qquad(\text{even excluding the vacuum, }15.6\%)$$
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>The universe allocates 95.0% of its operational budget to components in which nothing happens.</strong><br>
Vacuum (68.5%) + dark matter (26.5%) — <em>neither of which changes state.</em></p>
</div>

<div class="fig">
<p class="cap">Figure: the universe's energy = its allocation of operational resources. Raise the <strong>strictness of "what counts as an operation"</strong> with the slider and the surviving budget collapses in stages — from \(10^{121}\) counting everything, to \(10^{115}\) counting only starlight.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>What counts as an "operation" (stricter to the right)<input id="ss" type="range" min="0" max="3" value="1" step="1"></label>
  <span class="val" id="vs">excluding the vacuum</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#0f4a5a"></i>counted</span>
  <span><i class="swatch" style="background:#c3cfd4"></i>not counted</span>
  <span><i class="swatch" style="background:#a8622a"></i>surviving operation count</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>So what are the baryons doing?</h2>

<p>Look inside the surviving 4.9%. The most spectacular thing baryons do is <strong>stellar fusion</strong>. Estimate the total energy the universe has radiated as starlight since it began.</p>

<div class="calc">
<span class="tag">From the luminosity density</span>
<p class="lbl">Hubble volume × cosmic luminosity density</p>
$$3.17\times10^{11}\ \mathrm{Mpc^3}\times2\times10^{8}\ L_\odot/\mathrm{Mpc^3}=2.43\times10^{46}\ \mathrm{W}$$
<p class="lbl">integrate over the age and compare with the total energy</p>
$$\frac{1.06\times10^{64}\ \mathrm{J}}{7.90\times10^{69}\ \mathrm{J}}=1.3\times10^{-6}$$
</div>

<p><strong>The energy the universe has ever shone as starlight is one millionth of the total.</strong> Fusion, the most conspicuous activity in the universe, at that scale.</p>

<h2><span class="n">04</span>The instruction set</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Component</th><th class="mid">Fraction</th><th>What it actually does</th><th class="mid">An operation?</th></tr></thead>
<tbody>
<tr><th>Vacuum</th><td class="mid">68.5%</td><td>sits in the ground state; nowhere to go</td><td class="mid"><strong>×</strong></td></tr>
<tr><th>Dark matter</th><td class="mid">26.5%</td><td>gathers gravitationally; does not interact</td><td class="mid"><strong>×</strong></td></tr>
<tr class="hi"><th>Baryons</th><td class="mid">4.9%</td><td>chemistry, fusion, life</td><td class="mid"><strong>○</strong></td></tr>
<tr><th>Radiation</th><td class="mid">0.009%</td><td>free propagation (Episode 11: completely at rest)</td><td class="mid">△</td></tr>
</tbody>
</table>
</div>

<p>Episode 11 counted that "in this picture the photon gas is completely at rest". The fourth row restates it — <em>radiation propagates without changing state</em>. So calling it an "operation" in the ML sense is doubtful.</p>

<div class="aside">
<span class="tag">Connecting to Episode 1's 0.035</span>
Episode 1 counted "the universe performs only 0.035 operations per bit". Today we learn that <strong>95% of those 0.035 go to components in which nothing happens</strong>. <em>Effectively \(0.035\times0.049=1.7\times10^{-3}\) operations per bit</em> — <strong>one operation per 580 bits</strong>. The universe as a computer is working even less than we thought.
</div>

<h2><span class="n">05</span>The reveal — the ML limit counts only an upper bound</h2>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>ML looks only at energy</strong><span>an upper bound on how many times that energy could in principle change the state. <em>Whether it did is not asked</em></span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>So vacuum and dark matter contribute to the bound</strong><span>they have energy. They just do not actually transition</span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>There is a 95% gap between bound and performance</strong><span>the content of the gap Episode 1 flagged when it wrote <em>"this is a spec sheet, not a benchmark"</em></span></div></div>
</div>

<p>Episode 1's honest line said <em>"this is a spec sheet, not a benchmark"</em>. Today we measured that gap — <strong>95% of the spec is allocated to components with no prospect of being used.</strong></p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① "The vacuum has nowhere to go, so do not count it" is this document's judgement.</strong> It follows the standard reading of ML's \(E\) as energy above the ground state, but whether cosmological vacuum energy counts as that ground state is not obvious — de Sitter space has a horizon temperature and fluctuations. <em>What is solid in §02 is the observation that naively feeding in the total energy is wrong.</em></p>
<p style="margin:0 0 10px"><strong>② "Dark matter does nothing" reflects current knowledge.</strong> It changes if a non-gravitational interaction is found. And gravitational structure formation is a genuine change of state, so <em>"does nothing" applies only in the ML sense</em>.</p>
<p style="margin:0 0 10px"><strong>③ The luminosity density \(2\times10^8\,L_\odot/\mathrm{Mpc^3}\) is indicative</strong>, shifting by factors of a few with waveband and redshift dependence. Past star formation was higher, so multiplying by \(t_0\) is crude — <em>read \(10^{-6}\) as an order-of-magnitude claim</em>.</p>
<p style="margin:0 0 10px"><strong>④ The energy fractions are today's values.</strong> The operation count \(\Omega=\int(2E/\pi\hbar)dt\) integrates over the past, so an exact breakdown needs \(\int\rho_i V\,dt\) per component (radiation's share is far larger in the radiation era). §04's table is <em>a snapshot of today</em>.</p>
<p style="margin:0"><strong>⑤ "Operations" remains an upper bound on transitions permitted by energy, not meaningful computation</strong> (same caveat as Episode 1 ①). All this document did was decompose that bound by component.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Why is the operational budget "exactly the energy budget"?
<details><summary>Show the answer</summary><div class="ans">Because the Margolus–Levitin rate \(2E/\pi\hbar\) is <strong>proportional to \(E\)</strong>. So each component's operation rate is just its energy fraction.</div></details></li>

<li>Why should the vacuum not be counted, and how much disappears?
<details><summary>Show the answer</summary><div class="ans">ML's \(E\) is <strong>energy above the ground state</strong>, and the vacuum energy is that ground state — there is nowhere to transition to. That removes <strong>68.5%</strong>, leaving 31.5%.</div></details></li>

<li>What fraction is "doing something"?
<details><summary>Show the answer</summary><div class="ans">Baryons 4.9% + radiation 0.009% = <strong>4.91%</strong> (15.6% even excluding the vacuum). So <em>95.0% of the operational budget goes to components in which nothing happens</em> (vacuum + dark matter).</div></details></li>

<li>What fraction of the total has been radiated as starlight?
<details><summary>Show the answer</summary><div class="ans">Hubble volume \(3.17\times10^{11}\) Mpc³ × luminosity density \(2\times10^8L_\odot/\mathrm{Mpc^3}\) = \(2.4\times10^{46}\) W; over the age of the universe, \(1.1\times10^{64}\) J, or <strong>\(1.3\times10^{-6}\)</strong> of the total. <em>Fusion, the most conspicuous activity there is, at one part in a million.</em></div></details></li>

<li>(Harder) How does today revise Episode 1's "0.035 operations per bit"?
<details><summary>Show the answer</summary><div class="ans">95% of those 0.035 go to components in which nothing happens, so effectively \(0.035\times0.049=1.7\times10^{-3}\) — <strong>one operation per 580 bits</strong>. This is the content of the gap Episode 1 flagged as "a spec sheet, not a benchmark".</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — 95% went to components in which nothing happens</h2>
<p>We filled the blank Episode 1 left in "what the operations are". The Margolus–Levitin rate \(2E/\pi\hbar\) is <strong>proportional to energy</strong>, so the allocation of operational resources is exactly the universe's energy budget — dark energy 68.5%, dark matter 26.5%, baryons 4.9%, radiation 0.009%.</p>
<p>Then one remark bit. <strong>ML's \(E\) is energy above the ground state, and the vacuum energy is that ground state</strong> — nowhere to transition to. That removes 68.5%, and of the remaining 31.5%, 84.1% is dark matter (gravitational interaction only). <em>Only 4.91% can be said to be doing anything.</em></p>
<div class="keybox" style="margin:18px 0 0">
<p style="margin:0;text-align:center;font-size:19px">The universe allocates <strong>95.0%</strong> of its operational budget<br>to components in which nothing happens</p>
</div>
<p style="margin-top:22px">We looked inside the surviving 4.9% too — the energy the universe has ever shone as starlight is <strong>\(1.3\times10^{-6}\)</strong> of the total. Fusion, the most conspicuous activity in the universe, at one part in a million. And Episode 1's "0.035 operations per bit" falls to an effective <strong>one per 580 bits</strong>.</p>
<p>The reveal was the nature of the ML limit itself — <em>it looks only at energy and does not ask whether a transition occurred</em>. So vacuum and dark matter contribute to the bound. Today we measured the gap Episode 1 flagged with "this is a spec sheet, not a benchmark". <strong>95% of the spec is allocated to components with no prospect of being used.</strong></p>
</div>

<div class="next">
<span class="lbl">Next — Episode 23</span>
Next: <strong>error correction</strong>. Episode 18 counted that "volume cells were never given addresses". So how are the \(10^{122}\) bits written on the horizon <em>protected</em>? Holographic codes (the reading of AdS/CFT as quantum error correction) formulate the reconstruction of the bulk from boundary information as <strong>an error-correcting code</strong>. Brought into this picture — <em>"damage one point of the bulk and it is still recoverable from the boundary"</em>. It meets Episode 6's "the tool cannot reach the memory in use" head on.
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=60, X1=690;
  var COMP=[['vacuum',0.685,'#0f4a5a'],['dark matter',0.265,'#1f6a7a'],
            ['baryons',0.049,'#3f8a9a'],['radiation',0.000092,'#7fb4be']];
  var STAGE=['count everything','excluding the vacuum','also excluding dark matter','starlight only'];
  var KEEP=[4,3,2,1];
  var TOT=1.04e121;

  function draw(){
    var s=parseInt(ss.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);

    var Y=90, H=64, x=X0;
    var frac=0;
    for(var i=0;i<COMP.length;i++){
      var w=(X1-X0)*COMP[i][1];
      var counted = (i>= (4-KEEP[s]));
      if(s===3) counted=false;
      g.fillStyle = counted ? COMP[i][2] : '#c3cfd4';
      g.fillRect(x, Y, Math.max(w,2), H);
      if(counted) frac+=COMP[i][1];
      if(COMP[i][1]>0.03){
        g.fillStyle='#fff'; g.textAlign='center';
        g.font='bold 13px system-ui,-apple-system,"Segoe UI",sans-serif';
        g.fillText(COMP[i][0], x+w/2, Y+H/2+5);
        g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';
        g.fillText((COMP[i][1]*100).toFixed(1)+'%', x+w/2, Y+H/2+22);
      }
      x+=w;
    }
    if(s===3) frac=1.338e-6;
    g.strokeStyle='#93a8ae'; g.lineWidth=1.2;
    g.strokeRect(X0,Y,X1-X0,H);

    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillStyle='#5a7a84'; g.textAlign='left';
    g.fillText('the universe’s energy = its allocation of operational resources', X0, Y-16);

    var Y2=210, H2=40;
    var lg=Math.log10(TOT*frac), lg0=Math.log10(TOT);
    var w2=(X1-X0)*(lg/lg0);
    g.fillStyle='#e6dcd0';
    g.fillRect(X0,Y2,X1-X0,H2);
    g.fillStyle='#a8622a';
    g.fillRect(X0,Y2,Math.max(w2,2),H2);
    g.strokeStyle='#c9b6a2'; g.lineWidth=1.2;
    g.strokeRect(X0,Y2,X1-X0,H2);
    g.fillStyle='#7a4418'; g.textAlign='left';
    g.fillText('surviving operation count', X0, Y2-12);
    g.fillStyle='#fff'; g.textAlign='right';
    g.font='bold 14px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText((TOT*frac).toExponential(2), X0+Math.max(w2,140)-12, Y2+26);
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillStyle='#9a8674'; g.textAlign='right';
    g.fillText('counting everything: 1.04×10¹²¹', X1, Y2+H2+20);

    g.textAlign='center';
    for(var i=0;i<4;i++){
      var xx=X0+(X1-X0)*(i+0.5)/4;
      g.fillStyle = (i===s)?'#0f4a5a':'#a8bcc2';
      g.font=(i===s?'bold ':'')+'12px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.fillText(STAGE[i], xx, 320);
    }

    vs.textContent=STAGE[s];
    var pct=frac*100;
    ro.textContent=STAGE[s]+'　→　surviving fraction '+(pct<0.01?pct.toExponential(2):pct.toFixed(3))+'%'+
      '　operations '+(TOT*frac).toExponential(2)+
      '　/　per bit '+(0.0351*frac).toExponential(2)+
      (s===1?'　★ the vacuum is the ground state — nowhere to go':'')+
      (s===2?'　★ dark matter interacts only gravitationally':'')+
      (s===3?'　★ starlight is one millionth of the total':'');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-22-instruction.html', acc='#0f4a5a', ops='#a8622a',
      title='The instruction set of the universe-as-computer ── c·t = const, That Clicks, Episode 22',
      ep='EPISODE 22 ／ Filling the blank Episode 1 left in "what the operations are"',
      eyebrow='95% of the operational budget goes to components in which nothing happens',
      h1='The instruction set of<br>the universe-as-computer',
      sub='The ML rate is proportional to energy, so the allocation of operations<br>is exactly the universe\'s energy budget. <em>Counted, the result is exasperating.</em>',
      byline_l='What you need: multiplying fractions',
      byline_r='vacuum 68.5% + dark matter 26.5% = 95.0%',
      body=BODY + '\n\n<p class="foot">This document is Episode 22 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The Margolus–Levitin limit (rate \\(2E/\\pi\\hbar\\)) and its measurement of energy above the ground state are standard. The energy fractions \\(\\Omega_\\Lambda=0.685\\), \\(\\Omega_c=0.265\\), \\(\\Omega_b=0.049\\), \\(\\Omega_\\gamma=5.4\\times10^{-5}\\), \\(\\Omega_\\nu=3.8\\times10^{-5}\\) are standard Planck-era values. The per-component operation rates, "excluding the vacuum leaves 31.5%, of which 84.1% is dark matter", "4.91% is doing something", "95.0% of the operational budget goes to components in which nothing happens", and the \\(1.3\\times10^{-6}\\) fraction radiated as starlight are computed here (kenshou/calc26.py). <strong>"The vacuum has nowhere to go, so do not count it" is this document\'s judgement</strong> — it follows the standard reading of ML\'s \\(E\\) as energy above the ground state, but whether cosmological vacuum energy is that ground state is not obvious (de Sitter space has a horizon temperature and fluctuations). What is solid in §02 is the observation that naively feeding in the total energy is wrong. <strong>"Dark matter does nothing" reflects current knowledge and applies only in the ML sense</strong> — gravitational structure formation is a genuine change of state. The luminosity density \\(2\\times10^8\\,L_\\odot/\\mathrm{Mpc^3}\\) is indicative, shifts by factors of a few with waveband and redshift dependence, and past star formation was higher (so \\(10^{-6}\\) is an order-of-magnitude claim). The energy fractions are today\'s; an exact breakdown of \\(\\Omega=\\int(2E/\\pi\\hbar)dt\\) needs \\(\\int\\rho_iV\\,dt\\) per component (radiation\'s share is far larger in the radiation era). "Operations" remains an upper bound on transitions permitted by energy, not meaningful computation. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes what counts as an operation and the surviving budget collapses. "Show the answer" opens each solution.')
