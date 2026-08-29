# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episodes 28 and 29 handled two theories of the "constants vary" kind. Today we look at <strong>the side that actually measures</strong> — atomic clocks, the Oklo natural reactor, quasar absorption lines. Three completely different pieces of physics, and yet <em>the same single line of skeleton</em>. And at the end, one number: <strong>we know \(\alpha\) to 26 bits over only 0.1% of the universe's logarithmic history.</strong></p>

<h2><span class="n">01</span>Three ways of measuring</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Method</th><th class="mid">\(\alpha\) of when</th><th class="mid">Bound on \(|\Delta\alpha/\alpha|\)</th><th class="mid">Bits pinned</th></tr></thead>
<tbody>
<tr class="hi"><th>Atomic clocks (Yb⁺ E3 vs Sr)</th><td class="mid">today (a rate)</td><td class="mid">\(1.4\times10^{-8}\)</td><td class="mid"><strong>26.1 bit</strong></td></tr>
<tr class="hi"><th>Oklo natural reactor</th><td class="mid">1.8 Gyr ago</td><td class="mid">\(1.1\times10^{-8}\)</td><td class="mid"><strong>26.4 bit</strong></td></tr>
<tr><th>Quasar absorption lines</th><td class="mid">\(z\sim2\) (10.5 Gyr ago)</td><td class="mid">\(1.0\times10^{-5}\)</td><td class="mid">16.6 bit</td></tr>
<tr><th>CMB</th><td class="mid">\(z=1100\)</td><td class="mid">\(4.0\times10^{-3}\)</td><td class="mid">8.0 bit</td></tr>
<tr><th>Nucleosynthesis</th><td class="mid">\(t=1\) s</td><td class="mid">\(1.0\times10^{-2}\)</td><td class="mid">6.6 bit</td></tr>
</tbody>
</table>
</div>

<p>The laboratory value of \(\alpha\) itself is far more precise — \(\alpha^{-1}=137.035999177(21)\), a relative precision of \(1.6\times10^{-10}\), <strong>32.5 bits</strong>. But that is "the value today", not evidence that it has not moved.</p>

<h2><span class="n">02</span>The heart — all three are built from the same line</h2>

<div class="calc">
<span class="tag">The form common to every measurement</span>
$$(\text{change in the observable})=K\times\frac{\Delta\alpha}{\alpha}\qquad\Longrightarrow\qquad \left|\frac{\Delta\alpha}{\alpha}\right|<\frac{\text{observational precision}}{K}$$
<p class="lbl">\(K\) is the <strong>amplification</strong> — the factor translating a tiny change in \(\alpha\) into a large change in the observable</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Method</th><th class="mid">Amplification \(K\)</th><th class="mid">Precision</th><th class="mid">What does the amplifying</th></tr></thead>
<tbody>
<tr><th>Atomic clocks</th><td class="mid">7</td><td class="mid">\(10^{-18}\)</td><td class="mid">the difference in \(\alpha\)-sensitivity between two transitions</td></tr>
<tr class="hi"><th>Oklo</th><td class="mid"><strong>\(10^{7}\)</strong></td><td class="mid">\(2\times10^{-2}\)</td><td class="mid"><strong>97.3 meV as a difference of MeV-scale quantities</strong></td></tr>
<tr><th>Quasars</th><td class="mid">0.3</td><td class="mid">\(3\times10^{-6}\)</td><td class="mid">statistics from bundling many lines</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>Oklo is strong not because the measurement is precise.</strong><br>
Its precision is 2% — \(10^{16}\) times coarser than an atomic clock — <em>and it yields the same bound because the amplification is \(10^7\)</em>.<br>
<strong>Finding a place that amplifies beats improving precision.</strong></p>
</div>

<h2><span class="n">03</span>Where does Oklo's amplification come from?</h2>

<p>1.8 billion years ago at Oklo in Gabon, <em>a natural uranium deposit spontaneously sustained a fission chain reaction</em>. The ashes remain. The key is a neutron capture resonance in \(^{149}\mathrm{Sm}\).</p>

<div class="calc">
<span class="tag">Why \(10^7\)</span>
<p class="lbl">the resonance energy \(E_r=97.3\) meV appears as <strong>a difference of MeV-scale quantities</strong></p>
$$E_r\ \sim\ (\text{nuclear binding energy})-(\text{Coulomb energy})\ \sim\ 10^6\ \mathrm{eV}-10^6\ \mathrm{eV}$$
<p class="lbl">moving \(\alpha\) shifts only the Coulomb term, so</p>
$$\frac{\Delta E_r}{E_r}\ \sim\ \frac{10^6\ \mathrm{eV}}{0.0973\ \mathrm{eV}}\times\frac{\Delta\alpha}{\alpha}\ \simeq\ 10^{7}\times\frac{\Delta\alpha}{\alpha}$$
</div>

<p>This is <em>exactly the inverse</em> of the situation when Episode 19 measured coincidences. There, "large numbers cancelling to something small" was the surprise. Here <strong>that smallness is being used as the amplifier in a measuring instrument</strong>. <em>A cancellation of orders can be a mystery or a tool.</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>Where on the logarithmic axis does the data sit?</h2>

<p>Episode 2 counted the whole history of the universe as <strong>140.24 logarithmic steps</strong>. Place the five measurements on that ruler.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Method</th><th class="mid">Step</th><th class="mid">Bits pinned</th></tr></thead>
<tbody>
<tr><th>Nucleosynthesis</th><td class="mid">99.63</td><td class="mid">6.6</td></tr>
<tr><th>CMB</th><td class="mid">129.74</td><td class="mid">8.0</td></tr>
<tr><th>Quasar absorption lines</th><td class="mid">138.81</td><td class="mid">16.6</td></tr>
<tr class="hi"><th>Oklo</th><td class="mid">140.10</td><td class="mid"><strong>26.4</strong></td></tr>
<tr class="hi"><th>Atomic clocks</th><td class="mid">140.24</td><td class="mid"><strong>26.1</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0">Data exist from step 99.63 to 140.24 — <strong>29% of the whole history</strong>.<br>
For the remaining <strong>71% there is not one measurement of \(\alpha\)</strong>.<br>
And precision above 20 bits covers steps 140.10 to 140.24 — <em>0.1% of the history</em>.</p>
</div>

<div class="fig">
<p class="cap">Figure: logarithmic step across (the whole history is 140.24), bits pinned about \(\alpha\) up. <strong>Grey is where no data exist.</strong> Move the slider through epochs to read how much we know — <em>all of it is piled at the right edge</em>.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Which epoch's \(\alpha\) do you want (logarithmic step)<input id="ss" type="range" min="0" max="1403" value="1403" step="1"></label>
  <span class="val" id="vs">140.3 (today)</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6a2a4a"></i>bits pinned</span>
  <span><i class="swatch" style="background:#3a6a2a"></i>measurements</span>
  <span><i class="swatch" style="background:#cfc6cc"></i>no data exists</span>
</div>
</div>

<h2><span class="n">05</span>The gaps</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Gap</th><th class="mid">Steps</th><th class="mid">Length</th><th class="mid">Why nothing can be measured</th></tr></thead>
<tbody>
<tr class="hi"><th>Nucleosynthesis → CMB</th><td class="mid">99.6 → 129.7</td><td class="mid"><strong>30.1 steps</strong></td><td class="mid">plasma; light does not get through</td></tr>
<tr><th>CMB → quasars</th><td class="mid">129.7 → 138.8</td><td class="mid">9.1 steps</td><td class="mid">the dark ages; nothing luminous yet</td></tr>
</tbody>
</table>
</div>

<p><strong>The data live on three islands</strong> — nucleosynthesis, the CMB, and \(z\lesssim4\) onwards. Between them there is only theoretical interpolation. Episode 28 noted that a phase-transition VSL escapes exclusion by hiding before nucleosynthesis; <em>in fact there are another 30 steps of hiding place between nucleosynthesis and the CMB</em>.</p>

<h2><span class="n">06</span>The reveal — measurement lives where this series' tool cannot reach</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">What it is</th><th class="mid">Weight</th></tr></thead>
<tbody>
<tr><th>Amplification \(K\)</th><td class="mid">a ratio of ratios</td><td class="mid">\(0\)</td></tr>
<tr><th>\(\Delta\alpha/\alpha\)</th><td class="mid">the fractional change of a dimensionless quantity</td><td class="mid">\(0\)</td></tr>
<tr class="hi"><th>Bits pinned</th><td class="mid">the log of a ratio</td><td class="mid"><strong>\(0\)</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0">Measurement of constants sits entirely in the <strong>zero column</strong> of Episode 16's map of weights.<br>
── <em>A place this series' tool cannot touch at all. Which is exactly why it can be the referee.</em></p>
</div>

<p>Episode 13 measured the tool's limit: "a conformal transformation touches only size". Today is the flip side — <strong>the referee sits entirely outside the tool</strong>. That is how VSL could be judged in Episode 28, MOND in Episode 29, and \(c\cdot t=\)const itself in Episode 3. <em>Judgement is possible because the yardstick does not move.</em></p>

<h2><span class="n">07</span>An aside — observation beats anthropics</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>What breaks if \(\alpha\) moves</th><th class="mid">Required \(|\Delta\alpha/\alpha|\)</th></tr></thead>
<tbody>
<tr><th>the 7.65 MeV carbon resonance (triple-alpha) disappears</th><td class="mid">\(4\times10^{-2}\)</td></tr>
<tr><th>the \(^4\)He yield departs from observation</th><td class="mid">\(1\times10^{-2}\)</td></tr>
<tr><th>the timing of recombination shifts</th><td class="mid">\(4\times10^{-3}\)</td></tr>
<tr class="hi"><th>the actual observational bound</th><td class="mid"><strong>\(1\times10^{-8}\)</strong></td></tr>
</tbody>
</table>
</div>

<p>The argument that "life could not exist unless \(\alpha\) had this value" (anthropics) demands at most <strong>4%</strong>. The actual observational bound is \(10^{-8}\) — <em>six orders tighter</em>. <strong>That \(\alpha\) has not moved is confirmed far beyond anything anthropics can explain.</strong></p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① The amplification \(K\) is an order-of-magnitude marker.</strong> Oklo's \(10^7\) is estimated from "the resonance energy is a difference of MeV-scale quantities"; the exact value depends on nuclear structure calculations and the literature spans \(10^7\)–\(10^8\). The atomic clocks' \(\Delta K\simeq7\) depends on which transitions are compared.</p>
<p style="margin:0 0 10px"><strong>② The Oklo analysis carries nuclear-physics assumptions.</strong> The reactor temperature, the neutron spectrum, and the treatment of simultaneous variation in constants other than \(\alpha\) (such as \(m_q/\Lambda_{\rm QCD}\)) move the bound by factors of a few — <em>\(10^{-8}\) is a representative value</em>.</p>
<p style="margin:0 0 10px"><strong>③ Quasar absorption lines remain disputed</strong> (same caveat as Episode 28 ②). Webb and collaborators claim a significant variation, with Keck and VLT disagreeing in sign. The \(10^{-5}\) here is a conservative bound, not a single measurement.</p>
<p style="margin:0 0 10px"><strong>④ "Bits pinned" is this document's quantity, defined as \(-\log_2|\Delta\alpha/\alpha|\).</strong> It reads as "how many leading binary digits of \(\alpha\) have not moved", and is <em>a different quantity</em> from Episode 19's surprise in bits (which is relative to a prior range). Do not conflate them.</p>
<p style="margin:0 0 10px"><strong>⑤ §04's "29% of the whole history" is a fraction measured in logarithmic steps.</strong> Measured in ordinary time, data exist for 99.99999...% of it — <em>only in a logarithmic measure does "71% blank" appear</em>. This is not a matter of which is correct but <strong>of what one chooses to treat as evenly spaced</strong> (as in Episodes 2 and 20).</p>
<p style="margin:0"><strong>⑥ §07's \(4\times10^{-2}\) is a representative estimate for the triple-alpha resonance.</strong> The tolerable tuning depends on the method of calculation, with the literature spanning 0.5%–4%. <em>The conclusion — observation is orders tighter — is unaffected.</em></p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Write the form common to all three measurements.
<details><summary>Show the answer</summary><div class="ans">(change in the observable) \(=K\times\Delta\alpha/\alpha\), hence \(|\Delta\alpha/\alpha|<\) (precision) \(/K\). <strong>\(K\) is the amplification</strong>, and the larger it is, the stronger the bound from the same precision.</div></details></li>

<li>Why is Oklo's amplification \(10^7\)?
<details><summary>Show the answer</summary><div class="ans">Because the \(^{149}\mathrm{Sm}\) resonance at 97.3 meV appears as <strong>a difference of MeV-scale quantities</strong>. Moving \(\alpha\) shifts only the Coulomb term, so \(\Delta E_r/E_r\sim(10^6\,\mathrm{eV}/0.0973\,\mathrm{eV})\times\Delta\alpha/\alpha\simeq10^7\times\Delta\alpha/\alpha\). <em>A cancellation of orders becomes the amplifier of an instrument.</em></div></details></li>

<li>Oklo's precision is a coarse 2%. Why does it still match an atomic clock?
<details><summary>Show the answer</summary><div class="ans">Because the amplification is \(10^7\): \(2\times10^{-2}/10^7=2\times10^{-9}\). An example of <strong>finding a place that amplifies beating improving precision</strong>.</div></details></li>

<li>Over what fraction of the universe's logarithmic history does \(\alpha\) data exist?
<details><summary>Show the answer</summary><div class="ans">From nucleosynthesis (step 99.63) to today (140.24), \((140.24-99.63)/140.24=\) <strong>29%</strong>. For the remaining 71% there is no data at all, and precision above 20 bits covers only 0.1%.</div></details></li>

<li>(Harder) Why can measurements of constants serve as the referee for this series' judgements?
<details><summary>Show the answer</summary><div class="ans">Because the amplification, \(\Delta\alpha/\alpha\) and the bits pinned are <strong>all dimensionless — weight 0</strong>, sitting in the zero column of Episode 16's map, where <em>this series' tool (the conformal transformation) cannot reach</em>. A yardstick that cannot be moved is what allows VSL (Episode 28), MOND (Episode 29) and \(c\cdot t=\)const itself (Episode 3) to be judged.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — whoever finds the amplifier wins</h2>
<p>Three ways of measuring — atomic clocks (today, 26.1 bits), the Oklo natural reactor (1.8 Gyr ago, 26.4 bits), quasar absorption lines (10.5 Gyr ago, 16.6 bits). Three different pieces of physics, one skeleton: <strong>(change in the observable) \(=K\times\Delta\alpha/\alpha\)</strong>.</p>
<p>The heart is the amplification \(K\). <strong>Oklo's precision is 2%, \(10^{16}\) times coarser than an atomic clock</strong>, and it gives the same bound — <em>because the amplification is \(10^7\)</em>. The \(^{149}\mathrm{Sm}\) resonance at 97.3 meV appears as a difference of MeV-scale quantities, so a tiny change in \(\alpha\) shows up by orders. <strong>A cancellation of orders can be a mystery or a tool</strong> — what Episode 19 measured as "surprise" is here an amplifier.</p>
<p>Placed on the logarithmic axis, the landscape changes. Data exist over <strong>29%</strong> of the 140.24 steps, and precision above 20 bits over <strong>0.1%</strong>. They sit on three islands, with a <strong>30-step gap</strong> between nucleosynthesis and the CMB. <em>We have confirmed \(\alpha\)'s constancy through a much narrower window than one imagines.</em></p>
<p>And the reveal — amplification, \(\Delta\alpha/\alpha\) and bits pinned are all weight 0. <strong>Measurement of constants sits entirely where this series' tool cannot reach.</strong> The flip side of Episode 13's "a conformal transformation touches only size" — <em>judgement is possible because the referee does not move</em>. As an aside, anthropics demands 4% while observation delivers \(10^{-8}\), <strong>six orders tighter</strong>.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 31</span>
The second half of Part IV takes up <strong>theories that put the conformal transformation at their foundation</strong>. First, Penrose's <strong>conformal cyclic cosmology (CCC)</strong>. Episode 6 rewrote the Weyl curvature hypothesis — "the universe began at \(C=0\)" — in the language of occupancy. CCC goes further: <em>it glues the end of the universe (a far future where all mass has gone) to the beginning of the next, by a conformal transformation</em>. <strong>What happens when this series' tool is placed at the centre of a theory?</strong> And we count the conditions the gluing requires, using Episode 11's "light is conformally invariant" and Episode 6's occupancy.
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=34, Y1=310;
  var NSTEP=140.24, SB=99.63;
  var P=[[99.63,6.6,'nucleosynthesis'],[129.74,8.0,'CMB'],[138.81,16.6,'quasars'],
         [140.10,26.4,'Oklo'],[140.24,26.1,'atomic clocks']];
  var xmin=0, xmax=145, ymin=0, ymax=34;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function bitsAt(s){
    if(s<SB) return 0;
    var b=0;
    for(var i=0;i<P.length;i++){ if(s>=P[i][0]) b=P[i][1]; }
    return b;
  }

  function draw(){
    var s=parseInt(ss.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.fillStyle='#f2eef1';
    g.fillRect(X0, Y0, px(SB)-X0, Y1-Y0);
    g.fillStyle='#a89aa2'; g.textAlign='center';
    g.fillText('no measurement of α exists (71% of the history)', (X0+px(SB))/2, Y0+18);

    g.textAlign='right';
    for(var e=0;e<=30;e+=10){
      var y=py(e);
      g.strokeStyle=(e===0?'#ddd2da':'#f5f0f4'); g.lineWidth=(e===0?1.5:1);
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a1959d'; g.fillText(e+' bit', X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=140;q+=20){
      var x=px(q);
      g.strokeStyle='#faf7f9'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a1959d'; g.fillText(String(q), x, Y1+16);
    }
    g.strokeStyle='#d6c8d2'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    g.fillStyle='rgba(106,42,74,0.16)';
    g.beginPath();
    g.moveTo(px(SB),py(0));
    for(var i=0;i<P.length;i++){
      g.lineTo(px(P[i][0]),py(i===0?0:P[i-1][1]));
      g.lineTo(px(P[i][0]),py(P[i][1]));
      var nx = (i+1<P.length)? P[i+1][0] : xmax;
      g.lineTo(px(nx),py(P[i][1]));
    }
    g.lineTo(px(xmax),py(0));
    g.closePath(); g.fill();

    g.strokeStyle='#6a2a4a'; g.lineWidth=3;
    g.beginPath();
    g.moveTo(px(SB),py(0));
    for(var i=0;i<P.length;i++){
      g.lineTo(px(P[i][0]),py(i===0?0:P[i-1][1]));
      g.lineTo(px(P[i][0]),py(P[i][1]));
      var nx = (i+1<P.length)? P[i+1][0] : xmax;
      g.lineTo(px(nx),py(P[i][1]));
    }
    g.stroke();

    for(var i=0;i<P.length;i++){
      g.fillStyle='#3a6a2a';
      g.beginPath(); g.arc(px(P[i][0]),py(P[i][1]),5,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=1.6;
      g.beginPath(); g.arc(px(P[i][0]),py(P[i][1]),5,0,6.2832); g.stroke();
      g.fillStyle='#2f5a22'; g.textAlign=(i>=3?'right':'left');
      g.fillText(P[i][2], px(P[i][0])+(i>=3?-10:10), py(P[i][1])-9-(i===4?14:0));
    }

    g.strokeStyle='#8a6a7a'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(s),Y0); g.lineTo(px(s),Y1); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#8a7a84'; g.textAlign='center';
    g.fillText('logarithmic step  ln(t / t_P)  ── the whole history is 140.24', (X0+X1)/2, Y1+36);

    var b=bitsAt(s);
    var t=Math.exp(s)*5.391247e-44;
    var tl = t<3.156e7 ? t.toExponential(2)+' s' : (t/3.156e16).toPrecision(3)+' Gyr';
    vs.textContent=s.toFixed(1)+(s>139.9?' (today)':'');
    ro.textContent='step '+s.toFixed(1)+' (age '+tl+')　→　'+
      (b>0 ? 'we know '+b.toFixed(1)+' bits about α (|Δα/α| < '+Math.pow(2,-b).toExponential(1)+')'
           : '★ about α at this epoch we know not one bit');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-30-measure.html', acc='#6a2a4a', ops='#3a6a2a',
      title='Measuring varying constants for real ── c·t = const, That Clicks, Episode 30',
      ep='EPISODE 30 ／ Part IV — looking at the side that measures',
      eyebrow='Finding a place that amplifies beats improving precision',
      h1='Measuring varying<br>constants for real',
      sub='Atomic clocks, the Oklo natural reactor, quasar absorption lines — three different physics, one skeleton.<br><em>And we know \\(\\alpha\\) to 26 bits over only 0.1% of the logarithmic history.</em>',
      byline_l='What you need: division, logarithms, the idea of amplification',
      byline_r='\\(|\\Delta\\alpha/\\alpha|<\\)(precision)\\(/K\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 30 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The atomic clock bound \\(|\\dot\\alpha/\\alpha|<1.0(1.1)\\times10^{-18}\\)/yr is Lange et al. (2021, PRL 126, 011102); the Oklo constraint follows a line of analyses since Shlyakhter (1976); the many-multiplet method for quasar absorption lines is due to Webb, Murphy, Flambaum and collaborators. CODATA 2022\'s \\(\\alpha^{-1}=137.035999177(21)\\) is standard. <strong>The amplification \\(K\\) is an order-of-magnitude marker</strong>: Oklo\'s \\(10^7\\) is estimated from the \\(^{149}\\mathrm{Sm}\\) 97.3 meV resonance being a difference of MeV-scale quantities, and the exact value depends on nuclear structure calculations, spanning \\(10^7\\)–\\(10^8\\) in the literature. <strong>The Oklo analysis assumes a reactor temperature, a neutron spectrum, and a treatment of simultaneous variation in constants other than \\(\\alpha\\), any of which moves the bound by factors of a few</strong>. <strong>Quasar absorption lines remain disputed</strong>: Webb and collaborators claim a significant variation, with Keck and VLT disagreeing in sign — the \\(10^{-5}\\) used here is a conservative bound, not a single measurement. "Bits pinned", defined as \\(-\\log_2|\\Delta\\alpha/\\alpha|\\), is this document\'s quantity and is <em>different</em> from Episode 19\'s surprise in bits (which is relative to a prior range). §04\'s "29% of the whole history" is measured in logarithmic steps; in ordinary time it would be essentially 100% — <em>this is a choice about what to treat as evenly spaced</em> (Episodes 2 and 20). §07\'s \\(4\\times10^{-2}\\) is a representative estimate for the triple-alpha resonance, with the literature spanning 0.5%–4%; the conclusion is unaffected. The 140.24 logarithmic steps are \\(\\ln(t_0/t_P)\\) (Episode 2). Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider moves through epochs and reads off how much we know. "Show the answer" opens each solution.')
