# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 11 counted "nothing happens to light". <strong>That was a classical statement.</strong> Quantised, a resolution scale \(\mu\) enters and conformal symmetry breaks — and the breaking is <em>exactly the exponent \(\Omega^{D-4}\) from Episode 34</em>. This time we measure the breaking <strong>in bits</strong>. And we find that its size is nothing but <em>a count of the degrees of freedom.</em></p>

<h2><span class="n">01</span>Quantum theory cannot stay at \(D=4\)</h2>

<div class="calc">
<span class="tag">The exponent counted in Episode 34, once more</span>
$$S_{\text{Maxwell}}\;\to\;\Omega^{\,D-4}\,S_{\text{Maxwell}}$$
<p class="lbl">the exponent vanishes only at \(D=4\) — this is Episode 11's "nothing happens"</p>
</div>

<p>But <strong>a quantum calculation cannot stay at \(D=4\)</strong>.</p>

<div class="seven">
<div class="row"><div class="mk">A</div><div class="txt"><strong>Dimensional regularisation</strong><span>compute at \(D=4-\varepsilon\) and take \(\varepsilon\to0\) last — <em>throughout the calculation the dimension is not 4</em></span></div></div>
<div class="row"><div class="mk">B</div><div class="txt"><strong>Lattice or cutoff</strong><span>bring in a resolution scale \(\mu\) — <em>without deciding how finely you look, the integral is not defined</em></span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>Either way \(\Omega^{D-4}=\Omega^{-\varepsilon}\ne1\)</strong><span>the exponent from Episode 34 <em>becomes the breaking itself</em></span></div></div>
</div>

<div class="calc">
<span class="tag">Count the dimensions</span>
$$[\,e^2\,]=\text{mass}^{\,4-D}=\text{mass}^{\,\varepsilon}$$
<p class="lbl">\(\alpha\) is dimensionless only at \(D=4\); at \(\varepsilon\ne0\) it carries a dimension</p>
</div>

<p>Once it carries a dimension, <strong>it needs exactly the treatment of Episode 35</strong> — <em>pair it with a scale to make it dimensionless</em>. What asymptotic safety does by forming \(g=Gk^2\), QED does by writing \(\alpha(\mu)\).</p>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>\(\alpha\), which sat in the "zero column" of Episode 16's weight map, acquires a \(\mu\) once quantised.</strong><br>
── <em>Quantum theory writes a number into the column this series has been calling untouchable.</em></p>
</div>

<h2><span class="n">02</span>How much does it move?</h2>

<div class="calc">
<span class="tag">One-loop QED</span>
$$\frac{1}{\alpha(\mu)}=\frac{1}{\alpha(0)}-\frac{2}{3\pi}\sum_f N_c Q_f^2\,\ln\frac{\mu}{m_f}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">\(1/\alpha\)</th><th class="mid">where it comes from</th></tr></thead>
<tbody>
<tr><th>Low energy (\(q\to0\))</th><td class="mid">\(137.036\)</td><td class="mid">CODATA 2022</td></tr>
<tr><th>Electron loop alone, up to \(M_Z\)</th><td class="mid">\(134.47\)</td><td class="mid">\(\ln(M_Z/m_e)=12.09\), \(\Delta=2.566\)</td></tr>
<tr class="hi"><th>Measured \(1/\alpha(M_Z)\)</th><td class="mid"><strong>\(127.951\)</strong></td><td class="mid">PDG (\(\overline{\text{MS}}\))</td></tr>
</tbody>
</table>
</div>

<p>The electron loop alone accounts for <strong>28 per cent</strong> of the total shift. The muon, tau and quarks fill in the rest — <em>except that the hadronic part cannot be computed perturbatively and is put in from measured \(e^+e^-\to\)hadrons data</em>. <strong>That piece is an experimental input, not a prediction.</strong></p>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0">$$\frac{\alpha(M_Z)}{\alpha(0)}=1.0710\qquad\text{── }\textbf{7.1 per cent larger}$$</p>
</div>

<h2><span class="n">03</span>Measuring the "effective weight"</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Charged fermions included</th><th class="mid">\(d\ln\alpha/d\ln\mu\)</th></tr></thead>
<tbody>
<tr><th>The electron only</th><td class="mid">\(1.55\times10^{-3}\)</td></tr>
<tr><th>Three charged leptons</th><td class="mid">\(4.65\times10^{-3}\)</td></tr>
<tr class="hi"><th>All Standard Model charged fermions</th><td class="mid"><strong>\(1.03\times10^{-2}\)</strong></td></tr>
</tbody>
</table>
</div>

<p>The classical weight is <strong>0</strong>. Quantised, an "effective weight" of order \(10^{-3}\) appears. Per e-fold it is small, but <em>accumulated over 12.1 e-folds it becomes 7.1 per cent.</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The core — measuring the breaking in bits</h2>

<div class="calc">
<span class="tag">Episode 19's practice</span>
<p class="lbl">the laboratory precision on \(\alpha\) (CODATA 2022) = the noise floor</p>
$$1.6\times10^{-10}\;\to\;32.5\ \text{bits}$$
<p class="lbl">measure the \(m_e\to M_Z\) running in units of that floor</p>
$$\frac{7.10\times10^{-2}}{1.6\times10^{-10}}=4.44\times10^{8}\;\to\;\mathbf{28.7\ bits}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>On Episode 19's scale</th><th class="mid">Surprise</th></tr></thead>
<tbody>
<tr><th>An identity (Episode 24's \(C\cdot t=N\))</th><td class="mid">\(0\) bit</td></tr>
<tr><th>The band of coincidences (Episode 36)</th><td class="mid">\(5.6\) bit</td></tr>
<tr><th>Koide's relation</th><td class="mid">\(15.7\) bit</td></tr>
<tr class="hi"><th><strong>The breaking of conformal symmetry in QED</strong></th><td class="mid"><strong>\(28.7\) bit</strong></td></tr>
<tr><th>The uniformity of the CMB (Episode 17)</th><td class="mid">\(1.6\times10^5\) bit</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>The breaking sits 29 bits above the noise.</strong><br>
── Far above the band of coincidences (4 to 7), <em>a measured effect that cannot possibly be chance.</em><br>
<strong>Episode 11's "nothing happens" does not survive quantisation.</strong></p>
</div>

<div class="fig">
<p class="cap">Figure: the running of \(1/\alpha\). <strong>Classically it would be a horizontal line</strong> (weight 0); quantised it acquires a slope. Move the slider to change how many charged fermions are counted — <em>the slope is nothing but a count of the fields.</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>charged fermions counted, \(\sum N_cQ^2\)<input id="sf" type="range" min="0" max="80" value="10" step="1"></label>
  <span class="val" id="vf">1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a4a7a"></i>one-loop running</span>
  <span><i class="swatch" style="background:#b8b2c0"></i>classical (weight 0 = horizontal)</span>
  <span><i class="swatch" style="background:#a03a3a"></i>measured 1/α(M_Z) = 127.95</span>
</div>
</div>

<h2><span class="n">05</span>Does this contradict Episode 30?</h2>

<div class="seven">
<div class="row"><div class="mk">30</div><div class="txt"><strong>\(\alpha\) is constant in cosmic time to 26 bits</strong><span>Oklo and atomic clocks — <em>same \(\mu\), change the epoch</em>: \(\partial\alpha/\partial t=0\)</span></div></div>
<div class="row"><div class="mk">37</div><div class="txt"><strong>\(\alpha\) moves by 28.7 bits across energy scale</strong><span><em>same epoch, change \(\mu\)</em>: \(\partial\alpha/\partial\mu\ne0\)</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>No contradiction — they are different questions</strong><span>"\(\alpha\) is constant" <em>is not yet a sentence until you say constant with respect to what</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>Episode 3's procedure applies directly.</strong><br>
── <em>"If you have not named what you are comparing to, you have not yet made a sentence."</em> Here, whether the comparison is across epochs or across scales flips the answer to its opposite.</p>
</div>

<h2><span class="n">06</span>The size of the breaking counts the degrees of freedom</h2>

<div class="calc">
<span class="tag">The trace anomaly in curved spacetime</span>
$$\langle T^\mu{}_\mu\rangle=\frac{1}{16\pi^2}\left(c\,C^2-a\,E_4\right)$$
<p class="lbl">\(C^2\) = the square of the Weyl curvature, \(E_4\) = the Gauss–Bonnet term</p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Field content</th><th class="mid">\(a\)</th><th class="mid">\(c\)</th><th class="mid">\(c/a\)</th></tr></thead>
<tbody>
<tr><th>One real scalar</th><td class="mid">\(0.0028\)</td><td class="mid">\(0.0083\)</td><td class="mid">\(3.000\)</td></tr>
<tr><th>One Weyl fermion</th><td class="mid">\(0.0306\)</td><td class="mid">\(0.0500\)</td><td class="mid">\(1.636\)</td></tr>
<tr><th>One vector field (the photon)</th><td class="mid">\(0.1722\)</td><td class="mid">\(0.1000\)</td><td class="mid">\(0.581\)</td></tr>
<tr class="hi"><th>The Standard Model (\(N_0=4,\ N_{1/2}=45,\ N_1=12\))</th><td class="mid"><strong>\(3.4528\)</strong></td><td class="mid">\(3.4833\)</td><td class="mid">\(1.009\)</td></tr>
</tbody>
</table>
</div>

<p>The coefficients are fixed by the field content alone — \(a=(N_0+11N_{1/2}+62N_1)/360\), \(c=(N_0+6N_{1/2}+12N_1)/120\). <strong>The anomaly coefficient is just a count of the fields.</strong></p>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0"><strong>The size of the breaking = the number of degrees of freedom.</strong> The same currency Episode 24 counted information in.<br>
And the <strong>\(a\)-theorem</strong> (Komargodski–Schwimmer 2011) — <em>\(a\) only decreases along the renormalisation-group flow</em> (\(a_{\rm UV}>a_{\rm IR}\)).<br>
── <strong>What Episode 4 called "coarse-graining is irreversible" has a field-theory counterpart, and it is a theorem.</strong></p>
</div>

<h2><span class="n">07</span>Was Episode 11 wrong?</h2>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>No — it is exactly right within classical physics</strong><span>the Maxwell action is precisely conformally invariant at \(D=4\)</span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>The photon's own weight is unchanged by quantisation</strong><span>Episode 16's table stands</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>What broke was not the field but the coupling</strong><span>\(\alpha\) acquired a \(\mu\) — <em>the footnote is one line</em>: "classically, that is"</span></div></div>
</div>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) §02's \(1/\alpha(M_Z)=127.951\) is a measured value, not a result computed here.</strong> Only the electron loop's \(134.47\) comes from the one-loop formula; <em>of the remaining contributions the hadronic part cannot be computed perturbatively</em> and is taken from \(e^+e^-\to\)hadrons cross-section data. That is an experimental input, not a prediction of the theory.</p>
<p style="margin:0 0 10px"><strong>(2) The value of \(\alpha(\mu)\) is scheme-dependent.</strong> \(127.951\) is the \(\overline{\text{MS}}\) value and other schemes give other numbers — <em>so "\(\alpha\) moves by 7.1 per cent" is itself not strictly a sentence until the scheme is named</em> (the same structure as §05). Physical scattering amplitudes are scheme-independent, and that the running shows up in experiment is well established.</p>
<p style="margin:0 0 10px"><strong>(3) §04's 28.7 bits depends on choosing the laboratory precision on \(\alpha\) as the noise floor.</strong> Taking the floor to be the precision of \(\alpha(M_Z)\) (about \(10^{-4}\)) gives roughly 9.5 bits instead — <em>the point is the placement "far above the band of coincidences", not the digits</em>.</p>
<p style="margin:0 0 10px"><strong>(4) Normalisations of \(a\) and \(c\) differ between references.</strong> Here we take \(a=(N_0+11N_{1/2}+62N_1)/360\) and \(c=(N_0+6N_{1/2}+12N_1)/120\). <em>The ratio \(c/a\) and the structure "it counts fields" are normalisation-independent; the absolute values belong to this choice.</em> \(N_{1/2}=45\) counts Weyl fermions without right-handed neutrinos. Also, this form of \(a,c\) is for <strong>conformally invariant field theories</strong>, so the value 3.45 obtained by applying it to the massive Standard Model should be read as <em>an indication of size</em>.</p>
<p style="margin:0"><strong>(5) The \(a\)-theorem is proved in four dimensions, but there is no corresponding theorem for \(c\)</strong> (this is distinct from the two-dimensional \(c\)-theorem). §06's link to "coarse-graining is irreversible" is <em>this series' reading</em>, not a claim of Komargodski and Schwimmer.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>Why does quantisation break conformal symmetry? Put it in Episode 34's language.
<details><summary>Show the answer</summary><div class="ans">As Episode 34 counted, the Maxwell action goes as \(S\to\Omega^{D-4}S\), and <strong>the exponent vanishes only at \(D=4\)</strong>. But a quantum calculation uses \(D=4-\varepsilon\) (dimensional regularisation) or brings in a \(\mu\) (a cutoff), so <em>it cannot stay at \(D=4\)</em>. The breaking is \(\Omega^{-\varepsilon}\ne1\) itself.</div></details></li>

<li>What is \(1/\alpha(M_Z)\) from the electron loop alone, and where does the rest come from?
<details><summary>Show the answer</summary><div class="ans">\(137.036-\frac{2}{3\pi}\ln(M_Z/m_e)=137.036-2.566=\mathbf{134.47}\). The measured value is \(127.951\), so the electron supplies only <strong>28 per cent</strong> of the shift. The rest is the muon, tau and quarks — but <em>the hadronic part cannot be computed perturbatively and comes from \(e^+e^-\to\)hadrons data</em>.</div></details></li>

<li>Do "\(\alpha\) is constant" (Episode 30) and "\(\alpha\) runs" (this episode) contradict each other?
<details><summary>Show the answer</summary><div class="ans">No, because <strong>they are different questions</strong>. Episode 30 states \(\partial\alpha/\partial t=0\) (same \(\mu\), change the epoch); this episode states \(\partial\alpha/\partial\mu\ne0\) (same epoch, change \(\mu\)). <em>"Constant" is not yet a sentence until you say constant with respect to what</em> (Episode 3).</div></details></li>

<li>What does the trace-anomaly coefficient \(a\) count?
<details><summary>Show the answer</summary><div class="ans"><strong>The number of fields</strong> — \(a=(N_0+11N_{1/2}+62N_1)/360\). The size of the breaking is the number of degrees of freedom itself, <em>the same currency Episode 24 counted information in</em>. And by the \(a\)-theorem, <strong>\(a\) only decreases along the RG flow</strong>, which corresponds to Episode 4's "coarse-graining is irreversible".</div></details></li>

<li>(Harder) How long is the footnote Episode 11 needs?
<details><summary>Show the answer</summary><div class="ans"><strong>One line</strong> — "classically, that is". <em>The photon's own weight is unchanged by quantisation and Episode 16's table stands.</em> What broke was not the field but the <strong>coupling</strong>: \(\alpha\) acquired a \(\mu\). Episode 11's claim does not have to be withdrawn.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: quantum theory writes a number into the zero column</h2>
<p>The exponent counted in Episode 34, \(S\to\Omega^{D-4}S\), <strong>vanishes only at \(D=4\)</strong>. And <strong>quantum theory cannot stay at \(D=4\)</strong> — \(D=4-\varepsilon\) with dimensional regularisation, a \(\mu\) with a cutoff. Either way \(\Omega^{-\varepsilon}\ne1\), and <em>the exponent from Episode 34 becomes the breaking itself</em>. Counting dimensions, \([e^2]=\)mass\(^{\,\varepsilon}\): <strong>\(\alpha\) is dimensionless only at \(D=4\)</strong>. So it needs exactly Episode 35's treatment — pair it with a scale and write \(\alpha(\mu)\).</p>
<p>How much does it move? The electron loop alone takes \(1/\alpha\) from \(137.04\) to \(134.47\); the measured value at \(M_Z\) is \(127.951\). <strong>\(\alpha(M_Z)/\alpha(0)=1.0710\)</strong>, 7.1 per cent larger. The "effective weight" per e-fold is only of order \(10^{-3}\), but twelve e-folds accumulate to that — <em>quantum theory has written a small number into the "zero column" where \(\alpha\) sat on Episode 16's map.</em></p>
<p>Measure the breaking in bits. Taking the laboratory precision \(1.6\times10^{-10}\) (32.5 bits) as the noise floor, the 7.1 per cent running sits <strong>28.7 bits above the noise</strong> — far above the band of coincidences (4 to 7 bits) found in Episode 36, and <em>a measured effect that cannot possibly be chance</em>.</p>
<p>Does that contradict Episode 30's "\(\alpha\) is constant to 26 bits"? No — <strong>they are different questions</strong>. Episode 30 holds \(\mu\) fixed and changes the epoch; this episode holds the epoch fixed and changes \(\mu\). <em>"Constant" is not yet a sentence until you say constant with respect to what</em> — Episode 3's procedure applies directly.</p>
<p>And what does the size of the breaking measure? The trace-anomaly coefficients \(a\) and \(c\) turn out to be <strong>nothing but counts of the fields</strong> (3.45 for the Standard Model). The size of the breaking = the number of degrees of freedom — the same currency Episode 24 counted information in. Further, by the <strong>\(a\)-theorem</strong>, \(a\) only decreases along the RG flow. <em>What Episode 4 called "coarse-graining is irreversible" has a field-theory counterpart, and it is a theorem.</em></p>
<p>Was Episode 11 wrong? <strong>No</strong> — the footnote it needs is one line, "classically, that is". What broke was not the field but the coupling.</p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 38</span>
This time the breaking came from quantum theory being unable to stay at \(D=4\). Next time we look at something <em>worse</em>, which happens when you try to apply conformal transformations to <strong>gravity</strong> — the <strong>conformal factor problem</strong>. Split the Einstein action by its conformal factor and that factor's kinetic term comes out with <strong>the wrong sign</strong>. The energy has no lower bound and the path integral diverges. We go to the <em>source</em> of the ghost met twice in Episode 34. And <strong>we measure that divergence in bits as well.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sf=document.getElementById('sf'), vf=document.getElementById('vf'), ro=document.getElementById('ro');
  var X0=86, X1=690, Y0=34, Y1=306;
  var A0=137.035999, ME=0.51099895e-3, MZ=91.1876;
  var L0=Math.log(ME), L1=Math.log(500.0);
  var YT=138.5, YB=124.0;

  function px(l){ return X0+(l-L0)/(L1-L0)*(X1-X0); }
  function py(v){ return Y1-(v-YB)/(YT-YB)*(Y1-Y0); }

  function draw(){
    var S=parseInt(sf.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var v=126;v<=138;v+=2){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(v)); g.lineTo(X1,py(v)); g.stroke();
      g.fillText(v.toFixed(0), X0-8, py(v)+4);
    }
    g.textAlign='center';
    var marks=[[ME,'m_e'],[0.10566,'m_mu'],[1.77686,'m_tau'],[MZ,'M_Z']];
    for(var i=0;i<marks.length;i++){
      var x=px(Math.log(marks[i][0]));
      g.strokeStyle='#eceaf0'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#9c96a4'; g.fillText(marks[i][1], x, Y1+18);
    }

    g.strokeStyle='#b8b2c0'; g.lineWidth=2; g.setLineDash([5,4]);
    g.beginPath(); g.moveTo(X0,py(A0)); g.lineTo(X1,py(A0)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#a09aa8'; g.textAlign='left';
    g.fillText('classical: weight 0, so it does not move', X0+8, py(A0)-8);

    g.strokeStyle='#a03a3a'; g.lineWidth=1.4; g.setLineDash([3,3]);
    g.beginPath(); g.moveTo(X0,py(127.951)); g.lineTo(X1,py(127.951)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#a03a3a'; g.textAlign='left';
    g.fillText('measured 1/alpha(M_Z) = 127.95', X0+8, py(127.951)-7);

    g.strokeStyle='#2a4a7a'; g.lineWidth=2.6; g.beginPath();
    for(var k=0;k<=260;k++){
      var l=L0+(L1-L0)*k/260;
      var v=A0-(2/(3*Math.PI))*S*(l-L0);
      var X=px(l), Y=py(v);
      if(k===0) g.moveTo(X,Y); else g.lineTo(X,Y);
    }
    g.stroke();

    var vz=A0-(2/(3*Math.PI))*S*(Math.log(MZ)-L0);
    g.fillStyle='#2a4a7a';
    g.beginPath(); g.arc(px(Math.log(MZ)),py(vz),4.5,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('energy scale  mu  (log)', (X0+X1)/2, Y1+40);
    g.save(); g.translate(22,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('1 / alpha(mu)', 0,0); g.restore();

    vf.textContent=S.toFixed(2);
    var pct=100*(A0/vz-1);
    ro.textContent='sum N_cQ^2 = '+S.toFixed(2)+
      '　→　1/alpha = '+vz.toFixed(2)+' at M_Z'+
      '　(alpha larger by '+pct.toFixed(1)+' per cent)'+
      (S===0?'　★ set it to 0 and the line is flat — this is the classical "nothing happens"':'')+
      (Math.abs(S-1)<0.06?'　← the electron alone':'')+
      (Math.abs(S-6.67)<0.06?'　← all Standard Model charged fermions':'')+
      (S>3.2?'　※ running everything from m_e is a crude approximation — each particle really starts at its own mass':'');
  }
  sf.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-37-anomaly.html', acc='#2a4a7a', ops='#a03a3a',
      title='Quantum anomalies ── c·t = const, That Clicks, Episode 37 (Part V)',
      ep='EPISODE 37 ／ Part V — where the tool breaks',
      eyebrow='"Nothing happens to light" was a classical statement',
      h1='Quantum theory writes<br>into the zero column',
      sub='Quantum theory cannot stay at \\(D=4\\) — Episode 34\'s \\(\\Omega^{D-4}\\) becomes the breaking itself.<br><em>And we measure that breaking in bits.</em>',
      byline_l='What you need: Episode 11, Episode 16\'s weight table, Episode 19\'s scale, Episodes 34 and 35',
      byline_r='28.7 bits above the noise — not chance',
      body=BODY + '\n\n<p class="foot">This document is Episode 37 of "c·t = const, That Clicks" (the first of Part V), written for physics-minded high-school and university readers. The trace (conformal) anomaly, the running of the QED coupling, and the \\(a\\)-theorem are all standard, established material and nothing here is a new claim — the numbers are computed in kenshou/calc41.py. <strong>\\(1/\\alpha(M_Z)=127.951\\) is a measured value (PDG, \\(\\overline{\\text{MS}}\\)), not a result computed here</strong> — only the electron loop\'s 134.47 comes from the one-loop formula, and <em>of the remaining contributions the hadronic part cannot be computed perturbatively and is taken from \\(e^+e^-\\to\\)hadrons cross-section data</em>. The value of \\(\\alpha(\\mu)\\) is scheme-dependent, so "it moves by 7.1 per cent" is not strictly a sentence until the scheme is named (physical amplitudes are scheme-independent, and the running is well established experimentally). <strong>The figure of 28.7 bits depends on choosing the laboratory precision on \\(\\alpha\\) as the noise floor</strong>; taking the precision of \\(\\alpha(M_Z)\\) (\\(\\sim10^{-4}\\)) instead gives roughly 9.5 bits — <em>the placement "far above the band of coincidences" is the point, not the digits</em>. Normalisations of \\(a\\) and \\(c\\) differ between references; here \\(a=(N_0+11N_{1/2}+62N_1)/360\\) and \\(c=(N_0+6N_{1/2}+12N_1)/120\\) — <strong>this form is for conformally invariant field theories, so the value 3.45 obtained by applying it to the massive Standard Model is an indication of size</strong> (\\(N_{1/2}=45\\) counts Weyl fermions without right-handed neutrinos). The \\(a\\)-theorem (Komargodski &amp; Schwimmer 2011) is proved in four dimensions but there is no corresponding theorem for \\(c\\), and <strong>the link drawn to Episode 4\'s "coarse-graining is irreversible" is this series\' reading</strong>, not a claim of the original paper. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, set the slider to 0 for a flat line — the classical "nothing happens". "Show the answer" opens each solution.')
