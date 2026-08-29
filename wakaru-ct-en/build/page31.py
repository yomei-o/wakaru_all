# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">The second half of Part IV takes up <strong>theories that put the conformal transformation at their foundation</strong>. First, Penrose's <strong>conformal cyclic cosmology (CCC)</strong> — <em>gluing the end of the universe to the beginning of the next by a conformal transformation</em>. What happens when the operation this series has called "mere notation" is placed at the centre of a theory? <strong>And the move at CCC's centre is precisely the one we counted in Episode 11.</strong></p>

<h2><span class="n">01</span>At the centre is Episode 11's result</h2>

<p>Episode 11 transformed every quantity of a photon gas — number density, energy density, temperature, wavelength. <strong>All invariant</strong>, because the power of \(a\) in the standard picture and the quantity's weight were the same number.</p>

<div class="keybox">
<p class="lbl">Episode 11's conclusion, restated in one line</p>
<p style="margin:6px 0 0"><strong>With no mass there is no ruler; with no ruler the conformal factor has no meaning.</strong></p>
</div>

<p>Penrose starts here — <em>a far future in which all mass has gone, and a big bang consisting only of radiation, both have no "size"</em>. So why not glue them with a conformal transformation? <strong>That is CCC's central move.</strong></p>

<p>Episode 11 wrote that light carries neither ruler nor clock (infinite Compton wavelength, zero proper time). CCC is <em>that fact applied to the universe as a whole</em>.</p>

<h2><span class="n">02</span>Three conditions the gluing requires</h2>

<div class="seven">
<div class="row"><div class="mk">a</div><div class="txt"><strong>All rest mass must disappear</strong><span>any surviving mass leaves a ruler, which gives the conformal factor meaning</span></div></div>
<div class="row"><div class="mk">b</div><div class="txt"><strong>The Weyl curvature \(C\) must go to zero</strong><span>the Weyl curvature hypothesis (Episode 6) — \(C\) is conformally invariant and survives the gluing</span></div></div>
<div class="row hi"><div class="mk">c</div><div class="txt"><strong>Entropy must be cancelled</strong><span>the heaviest condition. \(3.1\times10^{104}\) has already accumulated</span></div></div>
</div>

<p>All three can be measured with quantities this series has already counted. In order.</p>

<h2><span class="n">03</span>(a) How much mass must be removed</h2>

<div class="calc">
<span class="tag">From today's energy budget</span>
$$\text{baryons }4.9\%\ +\ \text{dark matter }26.5\%\ =\ 31.4\%$$
<p class="lbl">all of which must lose its rest mass</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Process</th><th class="mid">Timescale</th><th class="mid">Basis</th></tr></thead>
<tbody>
<tr><th>Proton decay</th><td class="mid">\(>2.4\times10^{34}\) yr</td><td class="mid">Super-Kamiokande lower bound</td></tr>
<tr><th>Stellar-mass BH evaporation (10 M☉)</th><td class="mid">\(2\times10^{70}\) yr</td><td class="mid">\(t=2.1\times10^{67}(M/M_\odot)^3\) yr</td></tr>
<tr><th>Galactic centre BH (\(10^9\) M☉)</th><td class="mid">\(2\times10^{94}\) yr</td><td class="mid">as above</td></tr>
<tr class="hi"><th>Largest BHs (\(10^{11}\) M☉)</th><td class="mid"><strong>\(2\times10^{100}\) yr</strong></td><td class="mid">as above — this is the gluing time</td></tr>
</tbody>
</table>
</div>

<div class="caveat" style="margin-top:14px">
<span class="tag">CCC's weakest point</span>
<strong>The electron has no known decay channel.</strong> Charge conservation makes it stable as the lightest charged particle. CCC assumes that "in the far future rest mass itself is lost", but <em>there is no established mechanism supporting this</em> — Penrose states it as a conjecture.
</div>

<h2><span class="n">04</span>Where on the logarithmic axis does the gluing fall?</h2>

<div class="calc">
<span class="tag">In logarithmic steps</span>
$$\text{today}=\ln\frac{t_0}{t_P}=140.2,\qquad \text{gluing}=\ln\frac{2\times10^{100}\ \text{yr}}{t_P}=347.9$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0">In CCC's story the universe has made <strong>140 of 348 moves</strong> —<br>
<em>only 40% of the way through its logarithmic run.</em><br>
Episode 2 called the universe "a 140-move program"; in CCC it is <strong>still the first half</strong>.</p>
</div>

<div class="fig">
<p class="cap">Figure: CCC's story in logarithmic steps. <strong>Events on top, occupancy below</strong> (Episode 6). Move the slider to read what remains at each epoch — <em>today sits 40% of the way from the left</em>.</p>
<canvas id="cv" width="720" height="390"></canvas>
<div class="controls">
  <label>Logarithmic step \(\ln(t/t_P)\)<input id="ss" type="range" min="0" max="3600" value="1402" step="1"></label>
  <span class="val" id="vs">140.2 (today)</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#5a1a2a"></i>occupancy (emptying)</span>
  <span><i class="swatch" style="background:#1a5a6a"></i>events</span>
  <span><i class="swatch" style="background:#c9b6bc"></i>today</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">05</span>(b) How empty does it get — measured by occupancy</h2>

<div class="calc">
<span class="tag">The far-future (de Sitter) horizon</span>
$$H_\Lambda=H_0\sqrt{\Omega_\Lambda}=1.81\times10^{-18}\ \mathrm{s^{-1}},\qquad R=\frac{c}{H_\Lambda}=1.66\times10^{26}\ \mathrm{m}$$
$$\frac{S_{\rm dS}}{k_B}=\frac{A}{4\ell_P^2}=3.31\times10^{122}$$
<p class="lbl">what remains inside it (taking the Local Group to become one black hole)</p>
$$M=10^{12}M_\odot\ \Longrightarrow\ \frac{S}{k_B}=\frac{4\pi GM^2}{\hbar c}=1.05\times10^{101}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">Occupancy</th><th class="mid">From</th></tr></thead>
<tbody>
<tr><th>Today</th><td class="mid">\(1.5\times10^{-18}\)</td><td class="mid">Episode 6</td></tr>
<tr class="hi"><th>Far future (de Sitter)</th><td class="mid"><strong>\(3.2\times10^{-22}\)</strong></td><td class="mid">today — 3.7 orders emptier still</td></tr>
<tr><th>The moment of gluing</th><td class="mid">\(0\)</td><td class="mid">CCC's requirement (\(C=0\))</td></tr>
</tbody>
</table>
</div>

<p>Episode 6 counted that the universe began thermally full and gravitationally empty and is now emptying. <strong>That direction continues all the way to the end</strong> — and CCC connects to the next universe at that endpoint (completely empty). <em>Episode 6's "how badly the tool is breaking is the arrow of time" inverts in CCC into "when the tool works perfectly again, the universe ends".</em></p>

<h2><span class="n">06</span>(c) Cancelling the entropy — where the bet is placed</h2>

<p>The third condition is the heaviest. \(S/k_B=3.1\times10^{104}\) has already accumulated, and the next universe must begin with low entropy. <strong>Where does it go?</strong></p>

<div class="keybox">
<p class="lbl">Penrose's answer</p>
<p style="margin:6px 0 0"><strong>Information is lost in black hole evaporation.</strong><br>
The phase space itself shrinks, so the ceiling on entropy comes down.</p>
</div>

<p>This <strong>places a clear bet on one side of the black hole information problem</strong>. The mainstream position, grounded in AdS/CFT, is that information is not lost (unitarity); CCC does not take it. <em>This document does not adjudicate that debate, but it does make explicit where CCC has bet.</em></p>

<div class="aside">
<span class="tag">A warning from this series' tool</span>
Episode 16 measured that "a conformal transformation can move only <em>the unused side</em>". Episode 6 counted that "the memory in use today, \(3.1\times10^{104}\), is almost entirely black holes — the Weyl side". Put together — <strong>the conformal transformation used for the gluing cannot reach that \(3.1\times10^{104}\)</strong>. So condition (c) cannot be explained by a conformal transformation and <em>needs a separate mechanism</em>. <strong>That CCC has to bet on information loss is a consequence of this structure.</strong>
</div>

<h2><span class="n">07</span>An observational claim — Hawking points</h2>

<p>This is the important part about CCC: <strong>it carries an observable prediction.</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Claim</th><th class="mid">Content</th></tr></thead>
<tbody>
<tr><th>Hawking points</th><td class="mid">black hole evaporation in the previous aeon leaves circular marks in the CMB</td></tr>
<tr><th>Reports</th><td class="mid">Gurzadyan &amp; Penrose (2010, 2013), Penrose et al. (2018)</td></tr>
<tr class="hi"><th>Rebuttals</th><td class="mid"><strong>Wehus &amp; Eriksen (2011), DeAbreu et al. (2015), Jow &amp; Scott (2020)</strong></td></tr>
<tr><th>Substance of the rebuttals</th><td class="mid">the same statistics appear in Gaussian \(\Lambda\)CDM simulations</td></tr>
</tbody>
</table>
</div>

<p>Unsettled. <em>But carrying an observable claim at all matters</em> — <strong>Episode 28's phase-transition VSL escaped exclusion and lost every prediction in the observable era at the same stroke</strong>. CCC has not done that.</p>

<h2><span class="n">08</span>The surgery — CCC's name matches its content</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Ep.</th><th>Theory</th><th class="mid">(A) notation</th><th class="mid">(B) observable claim</th><th class="mid">Result of the surgery</th></tr></thead>
<tbody>
<tr><th>27</th><td>Inflation</td><td class="mid">establishing causal contact</td><td class="mid">\(n_s\)</td><td class="mid">(B) survives</td></tr>
<tr><th>28</th><td>VSL</td><td class="mid">a change of units</td><td class="mid">\(\alpha\) varies</td><td class="mid"><strong>chose (B), kept (A)'s name</strong></td></tr>
<tr><th>29</th><td>MOND</td><td class="mid">positing \(a_0\)</td><td class="mid">dynamics set by \(g/a_0\)</td><td class="mid">(B) is the substance</td></tr>
<tr class="hi"><th>31</th><td><strong>CCC</strong></td><td class="mid">the conformal gluing</td><td class="mid">the previous aeon continues (Hawking points)</td><td class="mid"><strong>uses (A) openly as a tool and places its claim in (B)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>CCC is the theory in Part IV that best withstands the surgery.</strong><br>
Its name (conformal cyclic cosmology) correctly points at both (A) and (B) —<br>
<em>it uses the conformal transformation as a tool, knowing it is "mere notation".</em></p>
</div>

<p>Episode 28's VSL claimed (B) while keeping (A)'s name, and the 26 bits of constraint on \(\alpha\) stopped being visible. CCC does the reverse: <strong>it states explicitly that at the moment of gluing there is no ruler, so the conformal factor is meaningless</strong>, and places (B) on top of that. <em>The surgery this series has used since Episode 3 has already been performed by the theory itself.</em></p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① CCC is a minority hypothesis</strong> and is not widely accepted as an alternative to standard cosmology. This document neither supports nor refutes it, and <em>measures only what this series' tools (conformal weights, occupancy, logarithmic steps) can measure</em>.</p>
<p style="margin:0 0 10px"><strong>② The mechanism by which the electron loses its rest mass is unverified.</strong> Charge conservation makes the electron stable as the lightest charged particle, with no known decay channel — <strong>a known weak point of CCC</strong>, stated by Penrose as a conjecture. Condition (a) stops here.</p>
<p style="margin:0 0 10px"><strong>③ §04's "348 moves" uses \(t=2.1\times10^{67}(M/M_\odot)^3\) yr with \(M=10^{11}M_\odot\).</strong> The actual gluing time depends on the mass of the heaviest black hole in the universe and moves by tens of steps. <em>Read "today is at 40%" with the same precision.</em></p>
<p style="margin:0 0 10px"><strong>④ §05's \(3.2\times10^{-22}\) assumes crudely that the Local Group (\(10^{12}M_\odot\)) becomes one black hole.</strong> How much mass actually remains inside the horizon depends on the nature of dark energy and the dynamics of the Local Group — an order-of-magnitude argument.</p>
<p style="margin:0 0 10px"><strong>⑤ The Hawking point claim is disputed.</strong> This document does not adjudicate. The rebuttals (the same statistics appear in Gaussian \(\Lambda\)CDM simulations) come from several independent groups, and there is no positive consensus at present.</p>
<p style="margin:0"><strong>⑥ §06's "betting on information loss" summarises CCC's position.</strong> The black hole information problem is unresolved and this document does not judge it, including the unitarity side — <em>it only makes explicit which way CCC has bet</em>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>State CCC's central move in Episode 11's language.
<details><summary>Show the answer</summary><div class="ans">Episode 11 counted that every quantity of a photon gas is conformally invariant — that is, <strong>with no mass there is no ruler, and with no ruler the conformal factor has no meaning</strong>. So "a far future with all mass gone" and "a big bang of radiation only" both have no size, and can be glued by a conformal transformation.</div></details></li>

<li>Name the three conditions the gluing requires.
<details><summary>Show the answer</summary><div class="ans">(a) all rest mass disappears, (b) the Weyl curvature \(C\) goes to zero (the Weyl curvature hypothesis), (c) entropy is cancelled. <em>All three can be measured with quantities this series has already counted.</em></div></details></li>

<li>Where does the gluing fall in logarithmic steps, and what fraction is today?
<details><summary>Show the answer</summary><div class="ans">The largest BHs (\(10^{11}M_\odot\)) evaporate in \(2\times10^{100}\) yr, so \(\ln(t/t_P)=347.9\). Today is 140.2, i.e. <strong>40%</strong>. Episode 2's "140 moves" is, in CCC's story, <em>still the first half</em>.</div></details></li>

<li>Find the far-future occupancy.
<details><summary>Show the answer</summary><div class="ans">The de Sitter horizon gives \(S_{\rm dS}/k_B=3.31\times10^{122}\), and the remaining Local Group black hole \(1.05\times10^{101}\). The ratio is <strong>\(3.2\times10^{-22}\)</strong> — 3.7 orders emptier than today's \(1.5\times10^{-18}\). Episode 6's emptying continues to the end.</div></details></li>

<li>(Harder) Why must CCC bet on information loss?
<details><summary>Show the answer</summary><div class="ans">Episode 16 counted that "a conformal transformation can move only <strong>the unused side</strong>", and Episode 6 that "the memory in use today is almost entirely black holes — the Weyl side". Together — <em>the conformal transformation used for the gluing cannot reach that \(3.1\times10^{104}\)</em>. So condition (c) cannot be explained conformally and needs another mechanism. <strong>CCC's bet on information loss is a consequence of this structure.</strong></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — when the tool is placed at the centre of a theory</h2>
<p>The move at CCC's centre is exactly the one we counted in Episode 11 — every quantity of a photon gas is conformally invariant, so <strong>with no mass there is no ruler, and with no ruler the conformal factor has no meaning</strong>. Hence "a far future with all mass gone" and "a big bang of radiation only" can be glued.</p>
<p>We measured the three conditions with this series' quantities. (a) The rest mass to be removed is <strong>31.4%</strong> of today's energy, and the largest black holes evaporate in \(2\times10^{100}\) yr — <strong>step 348</strong> on the logarithmic axis, with today still at <strong>40%</strong>. (b) Occupancy falls from today's \(1.5\times10^{-18}\) to <strong>\(3.2\times10^{-22}\)</strong>, 3.7 orders emptier — Episode 6's direction continuing to the end.</p>
<p>(c) is where the bet sits. Where does the \(3.1\times10^{104}\) already accumulated go? Penrose's answer is <strong>information loss in black hole evaporation</strong>, a clear side of the black hole information problem. <em>And this series' tools show why he has no choice</em> — Episode 16 ("a conformal transformation moves only the unused side") plus Episode 6 ("the memory in use is almost entirely the Weyl side") equals <strong>the gluing transformation cannot reach that \(3.1\times10^{104}\)</strong>.</p>
<p>And the surgery — <strong>CCC withstands it best of anything in Part IV</strong>. Episode 28's VSL failed by claiming (B) while keeping (A)'s name; CCC states explicitly that at the moment of gluing there is no ruler and hence no meaningful conformal factor, and places its claim in (B) — Hawking points. <em>The surgery this series has used since Episode 3 was already performed by the theory itself.</em> The Hawking point claim is unsettled, but <strong>carrying an observable claim at all is the decisive difference from phase-transition VSL</strong>.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 32</span>
Next: <strong>Wetterich's cosmon</strong>. Episode 4 counted "delete everything deletable and one mass is left" and named him only as the source of that picture — <em>the person who actually wrote "a universe that does not expand" as a field theory</em>. Now we go inside. <strong>In Wetterich's model the thing that grows the masses is a scalar field (the cosmon), which itself plays the role of dark energy.</strong> Where Episode 4's picture was <em>notation</em>, the cosmon is <em>a dynamical theory implementing that notation</em> — so it has predictions. <strong>What does a notation gain when it becomes a theory?</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=76, X1=700, YT=88, YB=300;
  var NOW=140.2, CROSS=347.9;
  var xmin=0, xmax=360;
  var ymin=-24, ymax=1;
  var EV=[[99.6,'nucleosynthesis'],[140.2,'today'],[219.6,'proton decay bound'],
          [302.2,'stellar BHs evaporate'],[347.9,'the gluing']];

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return YB-(y-ymin)/(ymax-ymin)*(YB-YT); }
  function occ(s){
    if(s<99.6) return null;
    if(s<=NOW) return -18.0 + (NOW-s)*0.127;
    if(s<=320) return -18.0 - (s-NOW)*(3.7/(320-NOW));
    return -21.7 - (s-320)*0.08;
  }

  function draw(){
    var s=parseInt(ss.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.fillStyle='#faf6f7';
    g.fillRect(px(NOW), 30, X1-px(NOW), YB-30);
    g.fillStyle='#c2a8b0'; g.textAlign='center';
    g.fillText('still to come (60% of the logarithmic run)', (px(NOW)+X1)/2, 46);

    g.textAlign='right';
    for(var e=0;e>=-24;e-=6){
      var y=py(e);
      g.strokeStyle='#f4eef0'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a89099'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=350;q+=50){
      var x=px(q);
      g.strokeStyle='#fbf7f8'; g.beginPath(); g.moveTo(x,YT-16); g.lineTo(x,YB); g.stroke();
      g.fillStyle='#a89099'; g.fillText(String(q), x, YB+16);
    }
    g.strokeStyle='#d8c6cc'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,YT-16); g.lineTo(X0,YB); g.lineTo(X1,YB); g.stroke();

    for(var i=0;i<EV.length;i++){
      var x=px(EV[i][0]);
      var isNow = Math.abs(EV[i][0]-NOW)<0.5;
      g.strokeStyle= isNow ? '#c9b6bc' : '#bcd4da';
      g.lineWidth= isNow ? 2.4 : 1.4;
      g.setLineDash(isNow?[]:[4,4]);
      g.beginPath(); g.moveTo(x,30); g.lineTo(x,YB); g.stroke();
      g.setLineDash([]);
      g.fillStyle= isNow ? '#8a5a68' : '#1a5a6a';
      g.save(); g.translate(x-4, 78); g.rotate(-Math.PI/2.6);
      g.textAlign='right'; g.font=(isNow?'bold ':'')+'11px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.fillText(EV[i][1], 0, 0); g.restore();
      g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';
    }

    g.strokeStyle='#5a1a2a'; g.lineWidth=3.2;
    g.beginPath();
    var first=true;
    for(var i=0;i<=400;i++){
      var x=xmin+(xmax-xmin)*i/400;
      var y=occ(x);
      if(y===null||y<ymin){ first=true; continue; }
      if(first){ g.moveTo(px(x),py(y)); first=false; } else g.lineTo(px(x),py(y));
    }
    g.stroke();

    g.strokeStyle='#8a6a74'; g.lineWidth=1.5; g.setLineDash([3,3]);
    g.beginPath(); g.moveTo(px(s),30); g.lineTo(px(s),YB); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#8a7078'; g.textAlign='center';
    g.fillText('logarithmic step  ln(t / t_P)  ── today 140, the gluing 348', (X0+X1)/2, YB+38);
    g.save(); g.translate(19,(YT+YB)/2); g.rotate(-Math.PI/2);
    g.fillText('occupancy', 0,0); g.restore();

    var o=occ(s);
    var pct=100*s/CROSS;
    var yrs=Math.exp(s)*5.391247e-44/3.155693e7;
    var what = s<99.6 ? ' (before nucleosynthesis)'
             : s<NOW ? ' (the past)'
             : s<219.6 ? ' (a dark universe after the stars burn out)'
             : s<302.2 ? ' (the era when protons may decay)'
             : s<347.9 ? ' (the era of evaporating black holes)'
             : ' (the gluing)';
    vs.textContent=s.toFixed(1)+(Math.abs(s-NOW)<0.6?' (today)':'');
    ro.textContent='step '+s.toFixed(1)+' ('+(yrs<1e6?yrs.toPrecision(3)+' yr':yrs.toExponential(2)+' yr')+')'+what+
      '　'+pct.toFixed(0)+'% of the run'+
      (o!==null? '　/　occupancy '+Math.pow(10,o).toExponential(2) : '　/　occupancy: not counted for this epoch');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-31-ccc.html', acc='#5a1a2a', ops='#1a5a6a',
      title='Penrose\'s conformal cyclic cosmology ── c·t = const, That Clicks, Episode 31',
      ep='EPISODE 31 ／ Part IV — when the tool sits at the centre of a theory',
      eyebrow='CCC\'s central move is the one we counted in Episode 11',
      h1='Penrose\'s conformal<br>cyclic cosmology',
      sub='Gluing the end of the universe to the beginning of the next by a conformal transformation.<br><em>What happens when "mere notation" is placed at a theory\'s centre?</em>',
      byline_l='What you need: Episode 6\'s occupancy, Episode 11\'s invariance, logarithmic steps',
      byline_r='today is move 140 ／ the gluing is move 348',
      body=BODY + '\n\n<p class="foot">This document is Episode 31 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. Conformal cyclic cosmology is due to Penrose (2010, <em>Cycles of Time</em>). The conformal invariance of massless fields, the Weyl curvature hypothesis, the black hole evaporation time \\(t\\simeq2.1\\times10^{67}(M/M_\\odot)^3\\) yr, and the Bekenstein–Hawking entropy \\(S=4\\pi GM^2/\\hbar c\\,k_B\\) are all standard, as is the Super-Kamiokande proton lifetime bound \\(>2.4\\times10^{34}\\) yr. The logarithmic steps (today 140.2, gluing 347.9, today at 40% of the run), the far-future occupancy \\(3.2\\times10^{-22}\\), and the 31.4% of rest mass to be removed are computed here (kenshou/calc35.py). <strong>CCC is a minority hypothesis and is not widely accepted as an alternative to standard cosmology</strong> — this document neither supports nor refutes it and measures only what this series\' tools can measure. <strong>The mechanism by which the electron loses its rest mass is unverified, and this is a known weak point of CCC</strong> (Penrose states it as a conjecture). §04\'s 348 steps depend on the mass of the heaviest black hole and move by tens of steps. §05\'s \\(3.2\\times10^{-22}\\) assumes crudely that the Local Group (\\(10^{12}M_\\odot\\)) becomes one black hole — an order-of-magnitude argument. <strong>The Hawking point claim is disputed</strong>: against the reports of Gurzadyan &amp; Penrose (2010, 2013) and Penrose et al. (2018), Wehus &amp; Eriksen (2011), DeAbreu et al. (2015) and Jow &amp; Scott (2020) argue that the same statistics appear in Gaussian \\(\\Lambda\\)CDM simulations, and there is no positive consensus at present. §06\'s "betting on information loss" summarises CCC\'s position; the black hole information problem is unresolved and is not judged here. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider moves through epochs and shows today at 40% of the run. "Show the answer" opens each solution.')
