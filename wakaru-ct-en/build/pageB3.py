# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">For 50 episodes the backbone was "dimensionless is physics, dimensionful is bookkeeping". <strong>But what <em>is</em> a dimensionless quantity?</strong> And <strong>are they really constants?</strong> Pressing on both questions gave: <em>the "zero column" is not homogeneous, the logarithm is not a discovery, and almost no constants survive.</em></p>

<h2><span class="n">01</span>A dimensionless quantity is what you can send by radio</h2>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>You cannot send "one metre"</strong><span>the receiver needs a ruler — nothing gets across without shipping an object</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>You can send "\(\alpha=1/137.036\)"</strong><span>the receiver can <em>check it with their own experiment</em></span></div></div>
<div class="row"><div class="mk">47</div><div class="txt"><strong>The same reason the SI could decree \(c\) but not \(\alpha\)</strong><span>Episode 47 — defining units does not touch what can be sent</span></div></div>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>A dimensionless quantity is one that can be conveyed without shipping anything.</strong><br>
── That was the content of "physics".</p>
</div>

<h2><span class="n">02</span>But the "zero column" is not homogeneous</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Type</th><th class="mid">Examples</th><th class="mid">Group</th><th class="mid">Natural (Haar) measure</th><th class="mid">Total measure</th></tr></thead>
<tbody>
<tr class="hi"><th>Ratios (scale-like)</th><td class="mid">\(\alpha\), \(m_p/m_e\), \(\rho_\Lambda/\rho_P\)</td><td class="mid">multiplicative \(\mathbb{R}_+\)</td><td class="mid">\(d(\ln x)\) = log-uniform</td><td class="mid"><strong>divergent</strong></td></tr>
<tr class="hi"><th>Angles and phases</th><td class="mid">\(\theta_{\rm QCD}\), CKM/PMNS</td><td class="mid">compact, \(U(1)\) etc.</td><td class="mid">\(d\theta\) = uniform</td><td class="mid"><strong>finite</strong></td></tr>
<tr><th>Counts</th><td class="mid">3 generations, 3 colours, \(D=4\)</td><td class="mid">discrete</td><td class="mid">counting</td><td class="mid">finite</td></tr>
<tr><th>Exponents (log-derivatives)</th><td class="mid">\(n_s\), \(\nu\), \(\eta\), \(\omega\)</td><td class="mid">a tangent space</td><td class="mid">hard to fix</td><td class="mid">──</td></tr>
</tbody>
</table>
</div>

<p><strong>For 50 episodes these were treated as one column.</strong> <em>They are at least four kinds, and the groups differ.</em></p>

<h2><span class="n">03</span>"Is it really a logarithm?" — the log is not a discovery, it is an isomorphism</h2>

<div class="calc">
<span class="tag">Ratios compose by multiplication — a multiplicative group</span>
$$\log:\ \mathbb{R}_+\ \xrightarrow{\ \cong\ }\ \mathbb{R}
\qquad\text{Haar measure}\ \frac{dx}{x}=d(\ln x)$$
<p class="lbl">log-uniform is "natural" because it <em>is</em> the Haar measure of the multiplicative group — <strong>not a discovery, an isomorphism</strong></p>
</div>

<div class="calc">
<span class="tag">Angles compose by addition and wrap at \(2\pi\) — a compact group</span>
$$\text{Haar measure}\ d\theta\ \text{(uniform)}\qquad\Longrightarrow\qquad \textbf{the log of an angle is meaningless}$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §03</p>
<p style="margin:6px 0 0"><strong>Bits are not the logarithm of the quantity. They are the logarithm of a probability.</strong><br>
To measure \(-\log_2(\text{probability})\) you need a measure, and <em>the group fixes the measure</em>.<br>
── That is what this series has been doing for 50 episodes.</p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The core — which turns Episode 48's criterion into a theorem</h2>

<div class="seven">
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>Compact group → finite Haar measure → normalisable</strong><span>the prior is <em>uniquely fixed</em> → the fine-tuning question is <strong>well-posed</strong></span></div></div>
<div class="row"><div class="mk">✗</div><div class="txt"><strong>Non-compact (\(\mathbb{R}_+\)) → infinite Haar measure → not normalisable</strong><span>the prior is <em>not fixed</em> (imposing a cutoff is a choice) → the question is <strong>ill-posed</strong></span></div></div>
</div>

<div class="keybox">
<p class="lbl">The first main point of this episode</p>
<p style="margin:6px 0 0">Episode 48's "<em>an angle has a reason for its prior, a mass ratio does not</em>" was —<br>
<strong>a restatement of compact versus non-compact.</strong><br>
── <em>Not a criterion. A theorem.</em></p>
</div>

<h2><span class="n">05</span>Testing it — within the compact class, do bits predict concern?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Angle</th><th class="mid">value [deg]</th><th class="mid">surprise [bits]</th><th class="mid">how it is actually treated</th></tr></thead>
<tbody>
<tr><th>PMNS \(\theta_{23}\)</th><td class="mid">\(49.0\)</td><td class="mid">\(0.88\)</td><td class="mid">near maximal mixing (a different kind of question)</td></tr>
<tr><th>PMNS \(\theta_{12}\)</th><td class="mid">\(33.4\)</td><td class="mid">\(1.43\)</td><td class="mid">not regarded as a problem</td></tr>
<tr><th>CKM \(\theta_{12}\) (Cabibbo)</th><td class="mid">\(13.04\)</td><td class="mid">\(2.79\)</td><td class="mid">not regarded as a problem</td></tr>
<tr><th>PMNS \(\theta_{13}\)</th><td class="mid">\(8.57\)</td><td class="mid">\(3.39\)</td><td class="mid">smallish; discussed</td></tr>
<tr><th>CKM \(\theta_{23}\)</th><td class="mid">\(2.38\)</td><td class="mid">\(5.24\)</td><td class="mid">part of the flavour hierarchy</td></tr>
<tr class="hi"><th>CKM \(\theta_{13}\)</th><td class="mid">\(0.201\)</td><td class="mid">\(8.81\)</td><td class="mid"><strong>the heart of the flavour puzzle</strong></td></tr>
<tr class="hi"><th>\(\theta_{\rm QCD}\)</th><td class="mid">\(<10^{-10}\)</td><td class="mid"><strong>\(35.87\)</strong></td><td class="mid"><strong>the only "crisis"</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>Within the compact class, bits track concern monotonically</strong> — 0 to 3 = nobody mentions it; 5 to 9 = the flavour puzzle; 36 = a crisis.<br>
And <strong>the one uncontested fine-tuning problem is the one angle, \(\theta_{\rm QCD}\)</strong>.<br>
── Everything contested (\(v/M_P\), \(\rho_\Lambda\)) is in the non-compact class.<br>
<em>They are not being argued over. The question is not well-posed, so it cannot settle.</em></p>
</div>

<div class="fig">
<p class="cap">Figure: the dimensionless quantities split into two classes. <strong>On the left (compact) bits are defined and track concern; on the right (non-compact) the bits themselves move with the prior.</strong> Move the prior-range slider — <em>the left does not budge; only the right does.</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>prior range on the non-compact side (decades)<input id="sd" type="range" min="10" max="300" value="123" step="1"></label>
  <span class="val" id="vd">123</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a5a"></i>compact (angles) — immovable</span>
  <span><i class="swatch" style="background:#8a4a2a"></i>non-compact (ratios) — moves with the prior</span>
</div>
</div>

<h2><span class="n">06</span>The next question — are they constants?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Category</th><th class="mid">count</th><th class="mid">constant with respect to what</th><th class="mid">verdict</th></tr></thead>
<tbody>
<tr class="hi"><th>Running couplings (3 gauge, 9 Yukawa, \(\lambda\), and the mixing angles run weakly)</th><td class="mid">\(\approx24\)</td><td class="mid"><strong>they change with scale</strong></td><td class="mid">not constants</td></tr>
<tr class="hi"><th>The six \(\Lambda\)CDM parameters</th><td class="mid">\(6\)</td><td class="mid">a description of this universe's <strong>state</strong></td><td class="mid">not constants of law</td></tr>
<tr><th>\(\theta_{\rm QCD}\)</th><td class="mid">\(1\)</td><td class="mid"><strong>an RG-invariant angle</strong></td><td class="mid"><strong>a genuine constant</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>Most of what we call constants are running functions.</strong> As Episode 37 showed, \(\alpha\) moves 7 per cent between \(0\) and \(M_Z\) — when we say "\(\alpha=1/137\)" that number <em>includes the convention of having chosen \(M_Z\)</em>. And the six \(\Lambda\)CDM parameters are different again: <em>they are initial conditions of this universe, not laws</em>. We do not call the Earth's orbital radius a constant of nature, for the same reason.</p>

<h2><span class="n">07</span>So what is genuinely invariant?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">independent of</th></tr></thead>
<tbody>
<tr><th>Critical exponent \(\nu=0.6300\)</th><td class="mid">scale, scheme, microscopic content (Ep. 44)</td></tr>
<tr><th>Anomalous dimension \(\eta=0.0363\)</th><td class="mid">the same (Ep. 14)</td></tr>
<tr><th>Correction exponent \(\omega=0.8303\)</th><td class="mid">the same</td></tr>
<tr><th>Anomaly coefficients \(a\), \(c\)</th><td class="mid">fixed by the field content alone (Ep. 37)</td></tr>
<tr class="hi"><th>\((D-1)(D-2)=6\)</th><td class="mid">fixed by the dimension alone (Ep. 38)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §07</p>
<p style="margin:6px 0 0">But — <strong>these are not constants of nature. They are theorems.</strong><br>
\(\nu=0.6300\) is a <em>mathematical fact</em> about the 3D Ising fixed point, not a measured input.<br>
── <strong>What is genuinely invariant turned out not to be a constant but a theorem.</strong></p>
</div>

<h2><span class="n">08</span>One remains — \(\theta_{\rm QCD}\). And then</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>Among independent inputs, only \(\theta_{\rm QCD}\) is a constant</strong><span>couplings are functions, \(\Lambda\)CDM is state, exponents are theorems</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>And \(\theta_{\rm QCD}\) is exactly what the axion turns into a field</strong><span>if Peccei–Quinn is right, \(\theta\) relaxes dynamically to \(0\)</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>If PQ is right, not a single constant remains</strong><span>running couplings, this universe's state, mathematical theorems, and a relaxing field — that is all there would be</span></div></div>
</div>

<div class="keybox">
<p class="lbl">The second main point of this episode</p>
<p style="margin:6px 0 0"><strong>"It cannot be that there are many constants — perhaps there is not a single one" is largely right.</strong><br>
More precisely — <em>among independent inputs, almost nothing is scale-independent. What looks like a constant is an output (a theorem), a fact about this universe, or the value of a running function.</em></p>
</div>

<h2><span class="n">09</span>And a correction to bonus ②</h2>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>Old: "the exponential map itself produces the 47× compression"</strong><span>too loose — for a bijective map with the induced prior, <em>the compression is exactly zero</em></span></div></div>
<div class="row hi"><div class="mk">○</div><div class="txt"><strong>New: the compression comes from \(\alpha\)'s prior being bounded to \(O(1)\)</strong><span>couplings are \(O(1)\) for a reason (perturbativity, dimensionlessness) — <em>ratios of scales are not</em></span></div></div>
<div class="row"><div class="mk">→</div><div class="txt"><strong>So the second criterion collapses into the first</strong><span>the exponential map is only a device for carrying the question to a quantity whose prior has a reason — <em>a fifth compression</em></span></div></div>
</div>

<p><strong>The numbers (\(408\to8.67\) bits) do not change. What changes is the subject of the sentence.</strong> ── Episode 3's practice exactly: <em>if you have not named what you are comparing to (here, the prior), you have not yet made a sentence.</em> Bonus ② was loose about that, so it is marked rather than deleted.</p>

<div class="caveat">
<span class="tag">The honest line — strongest objection first</span>
<p style="margin:0 0 10px"><strong>(1) Physical mass ratios really are RG-invariant.</strong> \(m_p/m_e\) is a ratio of pole masses and does not run — <em>it is a genuine dimensionless constant</em>. So "zero constants" is an overstatement, and §08 has to be restricted to "<strong>among independent inputs</strong>". The reply that \(m_p/m_e\) is an <em>output</em> (in principle computable from the Lagrangian) is <strong>a weak reply</strong> — in practice it is not computed, so for now it must be treated like an input.</p>
<p style="margin:0 0 10px"><strong>(2) "Running" is itself half a convention.</strong> Choosing \(\mu\) is a human act, and RG-invariant combinations can always be formed — but they tend to come out <em>dimensionful</em>, like \(\Lambda_{\rm QCD}\), and dimensionful is bookkeeping (Episode 3). That round trip is this series' whole subject.</p>
<p style="margin:0 0 10px"><strong>(3) Calling the six \(\Lambda\)CDM parameters "state" may be too strong.</strong> \(n_s\) is an initial condition but also a <em>prediction</em> of inflationary models — the border between law and state cannot be drawn sharply and depends on disciplinary custom.</p>
<p style="margin:0 0 10px"><strong>(4) §05's monotonicity is an observation on seven cases.</strong> The "how it is treated" column summarises the mood of the literature and <em>carries my bias</em> (the same caveat as Episode 36). PMNS \(\theta_{23}\) is discussed for being <em>near maximal</em>, not for being small — <strong>it is not measured on the same ruler.</strong></p>
<p style="margin:0"><strong>(5) §04's Haar-measure argument is standard mathematics</strong>, but <em>reading it as "therefore the fine-tuning question is well-posed or ill-posed" is this series' move</em> — statistics has finer machinery (invariant priors, Jeffreys priors). All that is claimed here is the single point that <strong>compact means normalisable and non-compact does not.</strong></p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>What is a dimensionless quantity, operationally?
<details><summary>Show the answer</summary><div class="ans"><strong>Something you can send by radio</strong> — conveyed without shipping an object. "One metre" cannot be sent; "\(\alpha=1/137.036\)" can. <em>The same reason the SI could decree \(c\) but not \(\alpha\)</em> (Episode 47).</div></details></li>

<li>Why is the logarithm natural for ratios but not for angles?
<details><summary>Show the answer</summary><div class="ans">Ratios form the <strong>multiplicative group \(\mathbb{R}_+\)</strong>, whose Haar measure is \(d(\ln x)\) — <em>the log is not a discovery but the isomorphism to the additive group</em>. Angles form a <strong>compact group</strong> whose Haar measure is \(d\theta\) — <em>taking a log has no meaning.</em></div></details></li>

<li>What was Episode 48's "is there a reason for the prior?" a restatement of?
<details><summary>Show the answer</summary><div class="ans"><strong>Compact versus non-compact.</strong> Compact → finite Haar measure → normalisable → the prior is uniquely fixed → the question is <strong>well-posed</strong>. Non-compact → not normalisable → <strong>ill-posed</strong>. <em>It was a theorem, not a criterion.</em></div></details></li>

<li>Why is \(\theta_{\rm QCD}\) the only uncontested fine-tuning problem?
<details><summary>Show the answer</summary><div class="ans"><strong>Because it is the only one in the compact class.</strong> For \(v/M_P\) and \(\rho_\Lambda\) the bit count itself moves with the prior — <em>they are not being argued over; the question is not well-posed, so it cannot settle.</em></div></details></li>

<li>(Harder) How far is "perhaps there is not a single constant" correct?
<details><summary>Show the answer</summary><div class="ans"><strong>Largely correct.</strong> Of the 32, about 24 are running functions, 6 are this universe's state, and what is genuinely invariant (\(\nu\), \(\eta\), \(\omega\)) is <em>a theorem, not a constant</em>. The remaining \(\theta_{\rm QCD}\) is precisely what the axion would make dynamical — <strong>if PQ is right, none remain.</strong> But per honest line (1), \(m_p/m_e\) really is RG-invariant, so the claim must be restricted to <em>independent inputs</em>.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: the zero column was not homogeneous, and almost no constants survived</h2>
<p><strong>A dimensionless quantity is what you can send by radio</strong> — conveyed without shipping anything. That was the content of "physics".</p>
<p>But the zero column is not homogeneous. There are <strong>ratios, angles, counts and exponents</strong>, and <em>the groups differ</em>. Ratios form the multiplicative group \(\mathbb{R}_+\); angles form a compact group. And <strong>the logarithm is not a discovery but the isomorphism from the multiplicative group to the additive one</strong> — log-uniform is natural because it is \(\mathbb{R}_+\)'s Haar measure, while taking the log of an angle means nothing. <em>Bits were never the log of the quantity; they were the log of a probability.</em></p>
<p>That turns Episode 48's criterion into a <strong>theorem</strong>: compact → finite Haar measure → normalisable → <em>the prior is uniquely fixed</em> (well-posed); non-compact → not normalisable → <em>not fixed</em> (ill-posed). Testing it, within the compact class <strong>bits track concern monotonically</strong> (PMNS \(\theta_{23}\) 0.88 → CKM \(\theta_{13}\) 8.81 → \(\theta_{\rm QCD}\) 35.87), and <strong>the one uncontested fine-tuning problem is the one angle</strong>. Everything contested is non-compact — <em>not argued over, but unable to settle.</em></p>
<p>And "are they constants?" Re-sorted, about 24 are <strong>running functions</strong>, 6 are <strong>this universe's state</strong>, and one remains: <strong>\(\theta_{\rm QCD}\)</strong>. What is genuinely invariant (\(\nu\), \(\eta\), \(\omega\), \(a\), \(c\)) is <em>a theorem, not a constant</em> — as \(\pi\) is a theorem about circles.</p>
<p>And finally — <strong>that \(\theta_{\rm QCD}\) is exactly what the axion would turn into a field. If Peccei–Quinn is right, not a single constant remains.</strong> <em>The intuition that "it cannot be that there are many constants" was largely right.</em></p>
</div>

<div class="next">
<span class="lbl">In closing — what the three bonus episodes found</span>
Bonus ①: <strong>whether the mass variation is universal can be measured</strong> (\(\mu\), 23.3 bits) — and a 10.2-bit degeneracy in the quark-mass direction.<br>
Bonus ②: <strong>a hierarchy shrinks to its own logarithm</strong> (the arithmetic stands; the reading is corrected here).<br>
Bonus ③: <strong>the zero column is not homogeneous, Episode 48's criterion was a theorem, and almost no constants survive.</strong><br>
── All three stand on the single procedure of Episode 3. And in the third, that procedure <em>deleted one of the criteria this series had built.</em> <strong>The tool is still working.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sd=document.getElementById('sd'), vd=document.getElementById('vd'), ro=document.getElementById('ro');
  var X0=64, X1=690, Y0=40, Y1=280, MID=372;

  var COMP=[
    ['PMNS t23',0.88],['PMNS t12',1.43],['CKM t12',2.79],
    ['PMNS t13',3.39],['CKM t23',5.24],['CKM t13',8.81],['theta_QCD',35.87]
  ];
  var NON=[['v/M_P',16.7],['rho_L/rho_P',123.0]];

  function py(b){ return Y1-Math.min(b,40)/40*(Y1-Y0); }

  function draw(){
    var dec=parseInt(sd.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.strokeStyle='#cdc8d2'; g.lineWidth=1.4;
    g.beginPath(); g.moveTo(MID,Y0-16); g.lineTo(MID,Y1+30); g.stroke();

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var b=0;b<=40;b+=10){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(b)); g.lineTo(X1,py(b)); g.stroke();
      g.fillText(b+' bit', X0-6, py(b)+4);
    }

    g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillStyle='#2a5a5a'; g.fillText('compact (angles) — the prior is fixed', (X0+MID)/2, Y0-22);
    g.fillStyle='#8a4a2a'; g.fillText('non-compact (ratios) — the prior is not', (MID+X1)/2, Y0-22);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    var bw=(MID-X0-24)/COMP.length;
    for(var i=0;i<COMP.length;i++){
      var x=X0+12+i*bw, b2=COMP[i][1];
      g.fillStyle='#2a5a5a'; g.globalAlpha=0.9;
      g.fillRect(x, py(b2), bw-8, Y1-py(b2));
      g.globalAlpha=1;
      g.save(); g.translate(x+(bw-8)/2, Y1+8); g.rotate(Math.PI/2.6);
      g.fillStyle='#5a7a7a'; g.textAlign='left'; g.fillText(COMP[i][0],0,0); g.restore();
      if(b2>30){ g.fillStyle='#2a5a5a'; g.textAlign='center'; g.fillText(b2.toFixed(1), x+(bw-8)/2, py(b2)-8); }
    }

    var bw2=(X1-MID-24)/NON.length;
    for(var j=0;j<NON.length;j++){
      var x2=MID+12+j*bw2;
      var bits=Math.log(dec)/Math.LN2;
      var bitsLin=NON[j][1]*Math.LN10/Math.LN2;
      g.fillStyle='#8a4a2a'; g.globalAlpha=0.9;
      g.fillRect(x2, py(bits), bw2-8, Y1-py(bits));
      g.globalAlpha=1;
      g.strokeStyle='#8a4a2a'; g.lineWidth=1.6; g.setLineDash([4,3]);
      g.beginPath(); g.moveTo(x2, py(bitsLin)); g.lineTo(x2+bw2-8, py(bitsLin)); g.stroke();
      g.setLineDash([]);
      g.save(); g.translate(x2+(bw2-8)/2, Y1+8); g.rotate(Math.PI/2.6);
      g.fillStyle='#8a6a4a'; g.textAlign='left'; g.fillText(NON[j][0],0,0); g.restore();
      g.fillStyle='#8a4a2a'; g.textAlign='center';
      g.fillText(bits.toFixed(1), x2+(bw2-8)/2, py(bits)-8);
    }
    g.fillStyle='#a08a6a'; g.textAlign='left';
    g.fillText('dashed = read with a linear prior (off the top)', MID+14, Y0+10);

    vd.textContent=String(dec);
    ro.textContent='prior range on the non-compact side: '+dec+' decades　→　log-uniform gives '+
      (Math.log(dec)/Math.LN2).toFixed(2)+' bits, linear gives 55 to 408'+
      '　★ the left half does not move by a single bit — only that half is well-posed';
  }
  sd.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-b3-dimensionless.html', acc='#2a5a5a', ops='#8a4a2a',
      title='Bonus ③: what a dimensionless quantity is, and whether constants exist ── c·t = const, That Clicks',
      ep='BONUS ③ ／ dug after the main series closed',
      eyebrow='The zero column was not homogeneous, and almost no constants survived',
      h1='Perhaps there is<br>not a single constant',
      sub='A dimensionless quantity is what you can send by radio — but there are four kinds, with different groups.<br><em>And most of what we call constants turned out to be running functions.</em>',
      byline_l='What you need: Episode 3\'s procedure, Episodes 14 and 44 on exponents, Episode 37 on running, Episode 47\'s map, Episode 48\'s priors',
      byline_r='One remains — and the axion would remove it',
      body=BODY + '\n\n<p class="foot">This document is bonus episode ③ of "c·t = const, That Clicks", written after the main 50 episodes closed, for physics-minded high-school and university readers. The numbers are computed in kenshou/calc58.py and calc59.py. Haar measure, the running of couplings under the renormalisation group, the universality of critical exponents and the Peccei–Quinn mechanism are all standard material. <strong>The strongest objection is honest line (1)</strong>: \\(m_p/m_e\\) is a ratio of pole masses and really is RG-invariant — <em>a genuine dimensionless constant</em> — so "zero constants" is an overstatement and the claim must be restricted to <strong>independent inputs</strong> (and the reply that it is an "output" is weak, since in practice it is not computed). <strong>"Running" is itself half a convention</strong>: RG-invariant combinations can always be formed, but they tend to come out dimensionful. <strong>Calling the six \\(\\Lambda\\)CDM parameters "state" may be too strong</strong> — \\(n_s\\) is also a prediction of inflationary models, and the law/state border cannot be drawn sharply. <strong>§05\'s monotonicity is an observation on seven cases</strong> whose "how it is treated" column carries my bias, and PMNS \\(\\theta_{23}\\) is discussed for being near maximal rather than small, so it is not on the same ruler. <strong>§04\'s Haar-measure argument is standard mathematics, but reading it as "therefore well-posed or ill-posed" is this series\' move</strong> — statistics has finer machinery (invariant and Jeffreys priors); the only claim made here is that compact means normalisable and non-compact does not. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the prior range and watch only the right half respond. "Show the answer" opens each solution.')
