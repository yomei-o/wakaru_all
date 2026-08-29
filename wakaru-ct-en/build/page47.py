# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Last time only the characterisations placed in <strong>dimensionless quantities</strong> could be tested. This time we draw the map — every dimensionless quantity in physics on one page, with the border between <em>what is physics and what is bookkeeping</em> drawn across it. And what emerges is that <strong>in 2019 the International System of Units drew that line in exactly the same place.</strong></p>

<h2><span class="n">01</span>In 2019 the SI redrew the line</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Constant</th><th class="mid">Fixed value (exact)</th><th class="mid">Unit defined</th></tr></thead>
<tbody>
<tr><th class="mid">\(\Delta\nu_{\rm Cs}\)</th><td class="mid">9 192 631 770 Hz</td><td class="mid">second</td></tr>
<tr><th class="mid">\(c\)</th><td class="mid">299 792 458 m/s</td><td class="mid">metre</td></tr>
<tr class="hi"><th class="mid">\(h\)</th><td class="mid">\(6.62607015\times10^{-34}\) J·s</td><td class="mid"><strong>kilogram</strong></td></tr>
<tr><th class="mid">\(e\)</th><td class="mid">\(1.602176634\times10^{-19}\) C</td><td class="mid">ampere</td></tr>
<tr><th class="mid">\(k_B\)</th><td class="mid">\(1.380649\times10^{-23}\) J/K</td><td class="mid">kelvin</td></tr>
<tr><th class="mid">\(N_A\)</th><td class="mid">\(6.02214076\times10^{23}\) /mol</td><td class="mid">mole</td></tr>
<tr><th class="mid">\(K_{\rm cd}\)</th><td class="mid">683 lm/W</td><td class="mid">candela</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>The kilogram prototype was retired.</strong> Mass is now built from \(h\).<br>
── This is <em>an official, international declaration that dimensionful quantities are bookkeeping</em>.<br>
<strong>The line this series drew by hand in Episode 3 is exactly where the world's metrology drew it.</strong></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">02</span>The core — but \(\alpha\) could not be fixed</h2>

<div class="calc">
<span class="tag">\(e\), \(\hbar\) and \(c\) are now exact. Does that fix \(\alpha\)?</span>
$$\alpha=\frac{e^2}{4\pi\varepsilon_0\hbar c}\qquad\Longrightarrow\qquad \textbf{no}$$
<p class="lbl">because \(\varepsilon_0\) became a measured quantity — \(1/\alpha=137.035999177(21)\) still has to be <strong>measured</strong></p>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>Being dimensionless, it cannot be legislated.</strong><br>
── \(c\) can be decreed; \(\alpha\) cannot.<br>
<em>This is the sharpest form of Episode 3's line.</em></p>
</div>

<h2><span class="n">03</span>How many constants does it take to fix the units?</h2>

<div class="seven">
<div class="row"><div class="mk">3</div><div class="txt"><strong>Mechanics has three dimensions</strong><span>length, time, mass</span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>\(c\), \(\hbar\), \(G\) use them up exactly</strong><span>Planck units — <em>written there, every quantity is dimensionless</em></span></div></div>
<div class="row hi"><div class="mk">?</div><div class="txt"><strong>"How many fundamental constants are there?" is unsettled</strong><span>3, 2, 1 or 0, depending on the position (the Duff–Okun–Veneziano trialogue of 2002) — <em>but one thing all positions agree on</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §03</p>
<p style="margin:6px 0 0"><strong>What every position agrees on: the content of physics is on the dimensionless side.</strong></p>
</div>

<h2><span class="n">04</span>The map of dimensionless quantities</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Value</th><th class="mid">Is there an explanation?</th></tr></thead>
<tbody>
<tr class="hi"><th>Information processed by the universe, \(N\) (Ep. 24)</th><td class="mid">\(3.1\times10^{122}\)</td><td class="mid">the same number as Eps. 40, 41</td></tr>
<tr><th>\(m_p/m_e\)</th><td class="mid">\(1836.15\)</td><td class="mid">unexplained</td></tr>
<tr><th>\(1/\alpha\)</th><td class="mid">\(137.036\)</td><td class="mid">unexplained</td></tr>
<tr><th>Spectral index \(n_s\)</th><td class="mid">\(0.9649\)</td><td class="mid">inflation claims one</td></tr>
<tr><th>\(\Omega_\Lambda\)</th><td class="mid">\(0.685\)</td><td class="mid">unexplained</td></tr>
<tr><th>\(v/M_P\)</th><td class="mid">\(2.0\times10^{-17}\)</td><td class="mid"><strong>the hierarchy problem</strong></td></tr>
<tr><th>\(\alpha_G=Gm_p^2/\hbar c\)</th><td class="mid">\(5.9\times10^{-39}\)</td><td class="mid">unexplained</td></tr>
<tr class="hi"><th>\(\rho_\Lambda/\rho_{\rm Planck}\) (Ep. 32)</th><td class="mid">\(1.13\times10^{-123}\)</td><td class="mid"><strong>the cosmological constant problem</strong></td></tr>
</tbody>
</table>
</div>

<p>From the largest, \(3.1\times10^{122}\), to the smallest, \(1.13\times10^{-123}\), the map spans <strong>815 bits</strong>. <em>And all of it sits in the same column (weight 0); a conformal transformation moves none of it.</em></p>

<div class="fig">
<p class="cap">Figure: the dimensionless quantities of physics on a single logarithmic axis, spanning <strong>815 bits</strong>. Move the "window" to see how many fall inside it — <em>unexplained numbers sit at both the large and the small end.</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>window centre (\(\log_{10}\))<input id="sw" type="range" min="-130" max="130" value="0" step="1"></label>
  <span class="val" id="vw">0</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3a5a4a"></i>unexplained</span>
  <span><i class="swatch" style="background:#8a6a2a"></i>a candidate explanation exists</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>the window (40 decades wide)</span>
</div>
</div>

<h2><span class="n">05</span>How many are there, and how many are explained?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Framework</th><th class="mid">Count</th><th class="mid">Breakdown</th></tr></thead>
<tbody>
<tr class="hi"><th>Standard Model (excluding neutrino masses)</th><td class="mid">\(19\)</td><td class="mid">only \(\mu^2\) (the Higgs \(v\)) is dimensionful — <strong>one</strong></td></tr>
<tr><th>Neutrino masses and mixings</th><td class="mid">\(7\)</td><td class="mid">3 masses + 3 angles + 1 phase</td></tr>
<tr class="hi"><th>\(\Lambda\)CDM base parameters</th><td class="mid">\(6\)</td><td class="mid"><strong>all six dimensionless</strong></td></tr>
<tr><th>Total</th><td class="mid"><strong>\(32\)</strong></td><td class="mid">\(\times5.37=\mathbf{171.7}\) bits</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>In the Standard Model Lagrangian, exactly one constant is dimensionful: \(\mu^2\).</strong> Everything else is dimensionless — and so are all six \(\Lambda\)CDM parameters.<br>
── <em>Modern physics already writes its parameters in the physics column.</em><br>
And almost none are derived from first principles — <strong>171.7 bits are unexplained.</strong></p>
</div>

<h2><span class="n">06</span>Applying the procedure to ourselves</h2>

<p>Here is <em>something one is tempted to do</em>. The <strong>171.7 bits</strong> just obtained, and Episode 2's "the whole history of the universe = 140.24 log steps" — they look like the same sort of number. Does that mean anything?</p>

<div class="calc">
<span class="tag">Put it through Episode 19's procedure</span>
$$|171.7-140.24|=31.5\qquad\text{a relative difference of }\mathbf{22\ \text{per cent}}$$
<p class="lbl">calling it "agreement" would need ±5 per cent → <strong>it does not land. Surprise: 0 bits</strong></p>
</div>

<p>And <em>even if it had been close</em>, the surprise would have been small — a parameter count of 15 to 30 and a price of 5 to 6 bits are both plausible, so the product ranges over 75 to 180 (a width of 105). Landing within ±5 per cent (a width of 14) is worth <strong>2.9 bits</strong>, <em>the bottom of the coincidence band</em>.</p>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0"><strong>This is what having a procedure is worth.</strong><br>
An impression that two things "look alike" can be <em>turned into a number and rejected on the spot</em>.<br>
── Episode 36 said the band of coincidences is a selection effect; <strong>this is how the ones that fail the selection fall away.</strong></p>
</div>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) There are several conventions for counting parameters.</strong> The Standard Model's 19 is <em>the standard count excluding neutrino masses</em>; including them gives 26 to 28 (depending on whether Majorana phases are counted), and whether to count \(\theta_{\rm QCD}\) changes it too — <strong>"32" is the result of one convention</strong> and moves between the high twenties and the low thirties.</p>
<p style="margin:0 0 10px"><strong>(2) The 5.37 bits behind "171.7 bits unexplained" is Episode 5's price.</strong> That came from a particular dataset size (\(N=1701\)), and <em>there is no universal price for one parameter</em> — the substance is the structure "32 parameters, almost all unexplained", and <strong>the significant figures of 171.7 mean nothing</strong>.</p>
<p style="margin:0 0 10px"><strong>(3) §02's "\(\alpha\) cannot be fixed" is a statement about the design of the SI.</strong> Fixing \(e\), \(\hbar\) and \(c\) makes \(\varepsilon_0\) (and \(\mu_0\)) measured quantities whose uncertainty is set by that of \(\alpha\) — <em>"a dimensionless quantity cannot be legislated" is this series' phrasing</em>; more precisely, <strong>"defining units does not determine dimensionless quantities"</strong>.</p>
<p style="margin:0 0 10px"><strong>(4) §03's "how many fundamental constants" remains a matter of disagreement.</strong> The 2002 trialogue in which Duff, Okun and Veneziano argued for 0, 3 and 2 respectively is well known, and <em>it is not settled</em> — this document takes only the uncontested part.</p>
<p style="margin:0"><strong>(5) §04's "unexplained" means "not derived from first principles".</strong> Many of these quantities have <em>partial understanding, or relations within a model</em> (\(m_p/m_e\), for instance, should in principle be computable from QCD and the electroweak theory) — <strong>it does not mean nothing is known about them</strong>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>What did the 2019 SI fix in order to define the units?
<details><summary>Show the answer</summary><div class="ans"><strong>The exact values of seven constants</strong> — \(\Delta\nu_{\rm Cs}\), \(c\), \(h\), \(e\), \(k_B\), \(N_A\), \(K_{\rm cd}\). <em>The kilogram prototype was retired and mass is now built from \(h\)</em> — <strong>an official, international declaration that dimensionful quantities are bookkeeping.</strong></div></details></li>

<li>\(e\), \(\hbar\) and \(c\) are all exact, so why is \(\alpha\) not determined?
<details><summary>Show the answer</summary><div class="ans">Because \(\varepsilon_0\) <strong>became a measured quantity</strong>. The uncertainty in \(\alpha=e^2/4\pi\varepsilon_0\hbar c\) is carried entirely by \(\varepsilon_0\) — <em>defining units does not determine dimensionless quantities</em>. \(c\) can be decreed, \(\alpha\) cannot: <strong>the sharpest form of Episode 3's line.</strong></div></details></li>

<li>How many dimensionful constants does the Standard Model Lagrangian have?
<details><summary>Show the answer</summary><div class="ans"><strong>One: \(\mu^2\)</strong> (the Higgs mass term, which sets \(v\)). Every other coupling and Yukawa is dimensionless — <em>modern physics already writes its parameters in the physics column</em>. All six \(\Lambda\)CDM base parameters are dimensionless too.</div></details></li>

<li>Do 171.7 bits and 140.24 log steps agree?
<details><summary>Show the answer</summary><div class="ans"><strong>No</strong> — a 22 per cent relative difference. Calling it agreement would need ±5 per cent, so <em>it does not land and the surprise is 0 bits</em>. Even if it had, the surprise would be 2.9 bits, the bottom of the band — <strong>with a procedure, an impression can be rejected on the spot.</strong></div></details></li>

<li>(Harder) How wide is the map of dimensionless quantities?
<details><summary>Show the answer</summary><div class="ans">From \(3.1\times10^{122}\) to \(1.13\times10^{-123}\): <strong>815 bits</strong>. <em>And all of it is in the same column (weight 0), unmovable by any conformal transformation</em> — which is exactly why this column can serve as the arena for judging.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: the world's metrology drew the line in the same place</h2>
<p>Since 20 May 2019, the SI has defined its units by <strong>fixing the exact values of seven constants</strong> — \(\Delta\nu_{\rm Cs}\), \(c\), \(h\), \(e\), \(k_B\), \(N_A\), \(K_{\rm cd}\). <em>The kilogram prototype was retired; mass is built from \(h\).</em> This is <strong>an official, international declaration that dimensionful quantities are bookkeeping</strong> — the line this series drew by hand in Episode 3, drawn in the same place by the world's metrology.</p>
<p>But <strong>\(\alpha\) could not be fixed</strong>. Fixing \(e\), \(\hbar\) and \(c\) makes \(\varepsilon_0\) a measured quantity, and \(1/\alpha=137.035999177(21)\) still has to be measured — <em>being dimensionless, it cannot be legislated</em>. <strong>\(c\) can be decreed and \(\alpha\) cannot: the sharpest form of Episode 3's line.</strong></p>
<p>The map of dimensionless quantities runs from \(3.1\times10^{122}\) (Episode 24's \(N\)) to \(1.13\times10^{-123}\) (the cosmological constant), <strong>815 bits wide</strong>, all in the same column. Counting the parameters: 19 for the Standard Model, 7 for neutrinos, 6 for \(\Lambda\)CDM — <strong>32</strong>, of which <strong>exactly one, \(\mu^2\), is dimensionful</strong>, and almost none are derived from first principles: <strong>171.7 bits unexplained.</strong></p>
<p>Finally we applied the procedure to ourselves. The 171.7 bits and Episode 2's 140.24 log steps look like the same sort of number, but <strong>the relative difference is 22 per cent: it does not land, and the surprise is 0 bits.</strong> Even if it had, 2.9 bits — the bottom of the band. <em>An impression that two things look alike can be turned into a number and rejected on the spot.</em> <strong>That is what having a procedure is worth.</strong></p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 48</span>
Episode 5's balance measured two things: <strong>brevity</strong> (the price of a parameter) and <strong>fit</strong> (\(\Delta\chi^2\)). But physicists routinely invoke a third — "<em>it is beautiful</em>". Next time we take that head-on: <strong>is beauty a third currency, or a restatement of the first two?</strong> We try to measure beauty itself with the tools this series has used for 47 episodes — <em>and we write down honestly what we could not measure.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sw=document.getElementById('sw'), vw=document.getElementById('vw'), ro=document.getElementById('ro');
  var X0=60, X1=690, YB=190;
  var L0=-130, L1=130, W=20;

  var D=[
    ['rho_L/rho_P', -123, 0],
    ['alpha_G', -38.2, 0],
    ['v/M_P', -16.7, 0],
    ['alpha', -2.14, 0],
    ['Omega_L', -0.16, 0],
    ['n_s', -0.016, 1],
    ['m_p/m_e', 3.26, 0],
    ['N (Ep. 24)', 122.5, 1]
  ];

  function px(l){ return X0+(l-L0)/(L1-L0)*(X1-X0); }

  function draw(){
    var wc=parseInt(sw.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.fillStyle='#f0eef3';
    g.fillRect(px(wc-W), YB-92, px(wc+W)-px(wc-W), 184);

    g.strokeStyle='#cdc8d2'; g.lineWidth=1.6;
    g.beginPath(); g.moveTo(X0,YB); g.lineTo(X1,YB); g.stroke();

    g.textAlign='center'; g.fillStyle='#9c96a4';
    for(var t=L0;t<=L1;t+=40){
      var x=px(t);
      g.strokeStyle='#e6e2ea'; g.lineWidth=1;
      g.beginPath(); g.moveTo(x,YB-6); g.lineTo(x,YB+6); g.stroke();
      g.fillText('10^'+t, x, YB+24);
    }

    var cnt=0;
    for(var i=0;i<D.length;i++){
      var l=D[i][1], kind=D[i][2], x2=px(l);
      var inw = (l>=wc-W && l<=wc+W);
      if(inw) cnt++;
      var up = (i%2===0);
      var y = up ? YB-30-(i%4)*17 : YB+38+(i%4)*17;
      g.strokeStyle = inw ? (kind===1?'#8a6a2a':'#3a5a4a') : '#ddd8e2';
      g.lineWidth=1.4;
      g.beginPath(); g.moveTo(x2,YB); g.lineTo(x2,y+(up?6:-6)); g.stroke();
      g.fillStyle = inw ? (kind===1?'#8a6a2a':'#3a5a4a') : '#c4bece';
      g.beginPath(); g.arc(x2,YB,4.2,0,6.29); g.fill();
      g.textAlign='center';
      g.fillText(D[i][0], x2, y);
    }

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('dimensionless quantities (log scale) — 815 bits wide in all', (X0+X1)/2, YB+120);

    vw.textContent=String(wc);
    ro.textContent='window centred on 10^'+wc+' (±20 decades)　→　'+cnt+' of 8 fall inside'+
      (cnt===0?'　★ nothing here — the map is mostly empty':'')+
      (Math.abs(wc)<5?'　★ around 1 — alpha, Omega_Lambda and n_s cluster here':'');
  }
  sw.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-47-map.html', acc='#3a5a4a', ops='#8a6a2a',
      title='The map of dimensionless quantities ── c·t = const, That Clicks, Episode 47 (Part VI)',
      ep='EPISODE 47 ／ Part VI — examining the procedure',
      eyebrow='\\(c\\) can be decreed; \\(\\alpha\\) cannot',
      h1='Metrology drew the line<br>in the same place',
      sub='In 2019 the SI fixed seven constants and redefined the units — the kilogram prototype was retired.<br><em>An official, international declaration that dimensionful is bookkeeping.</em>',
      byline_l='What you need: Episode 3\'s procedure, Episode 5\'s balance, Episode 16\'s weight table, Episode 19\'s scale',
      byline_r='32 parameters, 171.7 bits unexplained',
      body=BODY + '\n\n<p class="foot">This document is Episode 47 of "c·t = const, That Clicks" (the second of Part VI), written for physics-minded high-school and university readers. The 2019 SI redefinition, the parameter counts of the Standard Model and \\(\\Lambda\\)CDM, and the list of dimensionless quantities are all standard, and nothing here is a new claim — the numbers are computed in kenshou/calc51.py. <strong>§05\'s parameter count follows one of several conventions</strong> — the Standard Model\'s 19 excludes neutrino masses; including them gives 26 to 28 (depending on Majorana phases), and counting \\(\\theta_{\\rm QCD}\\) changes it too. <strong>The 5.37 bits behind "171.7 bits" is Episode 5\'s price (from a dataset of \\(N=1701\\)), and there is no universal price for a parameter</strong> — the substance is the structure, not the significant figures. <strong>§02\'s "\\(\\alpha\\) cannot be fixed" is a statement about the SI\'s design</strong>; more precisely, "defining units does not determine dimensionless quantities" (fixing \\(e,\\hbar,c\\) makes \\(\\varepsilon_0\\) a measured quantity whose uncertainty is that of \\(\\alpha\\)). <strong>§03\'s "how many fundamental constants" remains disputed</strong> (the 2002 trialogue in which Duff, Okun and Veneziano argued for 0, 3 and 2 is well known), and this document takes only the uncontested part. <strong>§04\'s "unexplained" means "not derived from first principles"</strong> — many of these have partial understanding or relations within a model, and <em>it does not mean nothing is known about them</em>. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the window and see how empty the map is. "Show the answer" opens each solution.')
