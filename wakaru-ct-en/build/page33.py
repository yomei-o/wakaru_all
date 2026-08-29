# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Part IV's two most easily confused cases, side by side — <strong>the Milne universe</strong> and <strong>\(R_h=ct\)</strong>. Both have "\(a\propto t\)" and both are described as "neither decelerating nor accelerating". And they are <em>entirely different things</em>. Episode 3 said "\(c\cdot t=\)const is not a coordinate change but a conformal transformation"; here we apply that distinction to <strong>the hardest case to tell apart</strong>, and build <em>a procedure for telling them apart</em>.</p>

<h2><span class="n">01</span>Both have \(a\propto t\); only \(k\) and the contents differ</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">Milne universe</th><th class="mid">\(R_h=ct\)</th></tr></thead>
<tbody>
<tr><th>Scale factor</th><td class="mid">\(a\propto t\)</td><td class="mid">\(a\propto t\)</td></tr>
<tr class="hi"><th>Contents</th><td class="mid"><strong>empty (\(\rho=0\))</strong></td><td class="mid"><strong>contains matter</strong></td></tr>
<tr class="hi"><th>Spatial curvature</th><td class="mid"><strong>\(k=-1\)</strong></td><td class="mid"><strong>\(k=0\)</strong></td></tr>
<tr><th>Total equation of state</th><td class="mid">──</td><td class="mid">\(w=-1/3\)</td></tr>
</tbody>
</table>
</div>

<p>The visible \(a(t)\) is identical. Only \(k\) and the contents differ — <strong>and that turned out to be decisive.</strong></p>

<h2><span class="n">02</span>Compute the scalar curvature and it is settled</h2>

<div class="calc">
<span class="tag">One line</span>
<p class="lbl">the scalar curvature of FLRW (\(c=1\))</p>
$$R=6\left[\frac{\ddot a}{a}+\left(\frac{\dot a}{a}\right)^2+\frac{k}{a^2}\right]$$
<p class="lbl">with \(a=t\), so \(\ddot a=0\) and \(\dot a/a=1/t\)</p>
$$R=\frac{6(1+k)}{t^2}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(k\)</th><th class="mid">\(R\)</th><th class="mid">What it is</th></tr></thead>
<tbody>
<tr class="hi"><th class="mid">\(-1\)</th><td class="mid"><strong>\(0\)</strong></td><td class="mid"><strong>Milne — exactly flat</strong></td></tr>
<tr><th class="mid">\(0\)</th><td class="mid">\(6/t^2\)</td><td class="mid">\(R_h=ct\)</td></tr>
<tr><th class="mid">\(+1\)</th><td class="mid">\(12/t^2\)</td><td class="mid">(for reference: the closed case)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0"><strong>Exactly zero at \(k=-1\).</strong> And not only the scalar curvature — <em>the entire Riemann tensor vanishes identically</em>.<br>
── <strong>The Milne universe is Minkowski spacetime in different coordinates.</strong></p>
</div>

<div class="calc">
<span class="tag">Today's values</span>
$$R_{h}=ct:\quad R=\frac{6}{(ct_0)^2}=3.52\times10^{-52}\ \mathrm{m^{-2}}\qquad\Longrightarrow\qquad \frac{1}{\sqrt R}=1.73\ \mathrm{Gpc}$$
$$\text{Milne}:\quad R=0\ (\text{exactly})$$
</div>

<h2><span class="n">03</span>The heart — a three-step test</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>Does the Riemann tensor vanish identically?</strong><span>Yes → <em>a change of coordinates returns it to flat spacetime</em>. There is no physical content</span></div></div>
<div class="row hi"><div class="mk">2</div><div class="txt"><strong>If not, does the Weyl tensor \(C\) vanish?</strong><span>Yes → <em>a conformal transformation can make it Minkowski</em>, but that transformation moves masses (Episode 4)</span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>If \(C\) does not vanish either</strong><span>neither can remove it. Episode 6's "Weyl side" — a real gravitational field</span></div></div>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Spacetime</th><th class="mid">Riemann</th><th class="mid">Weyl \(C\)</th><th class="mid">What is required</th></tr></thead>
<tbody>
<tr><th>Minkowski</th><td class="mid">\(0\)</td><td class="mid">\(0\)</td><td class="mid">nothing at all</td></tr>
<tr class="hi"><th>Milne</th><td class="mid">\(0\)</td><td class="mid">\(0\)</td><td class="mid"><strong>coordinates only (Step 1)</strong></td></tr>
<tr class="hi"><th>\(R_h=ct\)</th><td class="mid">\(\ne0\)</td><td class="mid">\(0\)</td><td class="mid"><strong>a conformal transformation (Step 2)</strong></td></tr>
<tr><th>\(\Lambda\)CDM</th><td class="mid">\(\ne0\)</td><td class="mid">\(0\)</td><td class="mid">a conformal transformation (Step 2)</td></tr>
<tr><th>Schwarzschild</th><td class="mid">\(\ne0\)</td><td class="mid">\(\ne0\)</td><td class="mid">neither can remove it (Step 3)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>Every FLRW falls in Step 2</strong> (Weyl zero, Ricci non-zero).<br>
── <em>The place this series has occupied since Episode 1 is pinned down by that one line.</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>Compare luminosity distances and something surprising happens</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">\(z\)</th><th class="mid">\(\Lambda\)CDM</th><th class="mid">Milne</th><th class="mid">\(R_h=ct\)</th><th class="mid">\(\Delta\mu\) Milne</th><th class="mid">\(\Delta\mu\) \(R_h=ct\)</th></tr></thead>
<tbody>
<tr><th class="mid">0.3</th><td class="mid">0.3613</td><td class="mid">0.3450</td><td class="mid">0.3411</td><td class="mid">−0.101</td><td class="mid">−0.125</td></tr>
<tr><th class="mid">0.5</th><td class="mid">0.6580</td><td class="mid">0.6250</td><td class="mid">0.6082</td><td class="mid">−0.112</td><td class="mid">−0.171</td></tr>
<tr class="hi"><th class="mid">1.0</th><td class="mid">1.5292</td><td class="mid"><strong>1.5000</strong></td><td class="mid">1.3863</td><td class="mid"><strong>−0.042</strong></td><td class="mid">−0.213</td></tr>
<tr><th class="mid">1.5</th><td class="mid">2.5188</td><td class="mid">2.6250</td><td class="mid">2.2907</td><td class="mid">+0.090</td><td class="mid">−0.206</td></tr>
<tr><th class="mid">2.0</th><td class="mid">3.6837</td><td class="mid">4.0000</td><td class="mid">3.2958</td><td class="mid">+0.179</td><td class="mid">−0.181</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0">Remarkably, at \(z=1\) <strong>Milne is closer to \(\Lambda\)CDM</strong> (1.500 against 1.529, a gap of 0.042 mag).<br>
<em>An empty spacetime fits the Hubble diagram better than \(R_h=ct\) does.</em><br>
── <strong>"Fits the Hubble diagram" is a weak test of a model.</strong></p>
</div>

<div class="fig">
<p class="cap">Figure: departure from \(\Lambda\)CDM in magnitudes. <strong>The grey band is one supernova's intrinsic scatter (0.15 mag)</strong>. Move the slider through redshift to read <em>how many supernovae are needed for a 5σ distinction at that \(z\)</em>.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Redshift \(z\)<input id="sz" type="range" min="5" max="200" value="100" step="1"></label>
  <span class="val" id="vz">z = 1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a3a4a"></i>Milne</span>
  <span><i class="swatch" style="background:#9a6a2a"></i>\(R_h=ct\)</span>
  <span><i class="swatch" style="background:#d5d9dd"></i>one supernova's scatter</span>
</div>
</div>

<h2><span class="n">05</span>And yet Milne is decisively excluded</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Observation</th><th class="mid">Why it fails</th></tr></thead>
<tbody>
<tr><th>CMB acoustic peaks</th><td class="mid">no baryons, so no sound waves</td></tr>
<tr><th>Nucleosynthesis</th><td class="mid">no matter, so no \(^4\)He and no D</td></tr>
<tr><th>Structure formation</th><td class="mid">no matter to gather gravitationally</td></tr>
<tr class="hi"><th>Measurement of \(\Omega_m\)</th><td class="mid"><strong>\(\Omega_m=0.315\pm0.007\)</strong> — more than 45σ from \(\Omega_m=0\)</td></tr>
</tbody>
</table>
</div>

<p><strong>Good geometry with nothing in it is not physics.</strong> In Episode 25's terms — <em>\(L(\text{residual})\) is not determined by the Hubble diagram alone</em>. On that one dataset Milne looks preferable, and the moment other datasets enter it evaporates (the same structure as MOND in Episode 29).</p>

<h2><span class="n">06</span>The reveal — the source of the confusion, and how to resolve it</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">Milne</th><th class="mid">\(R_h=ct\)</th></tr></thead>
<tbody>
<tr><th>How it is described</th><td class="mid">"\(a\propto t\), neither decelerating nor accelerating"</td><td class="mid">the same</td></tr>
<tr class="hi"><th>\(k\)</th><td class="mid">\(-1\)</td><td class="mid">\(0\)</td></tr>
<tr class="hi"><th>Riemann</th><td class="mid">\(0\)</td><td class="mid">\(\ne0\)</td></tr>
<tr class="hi"><th>Operation required</th><td class="mid"><strong>a coordinate change</strong></td><td class="mid"><strong>a conformal transformation</strong></td></tr>
<tr><th>Physical content</th><td class="mid">zero</td><td class="mid">masses move</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0">There is one way to tell them apart — <strong>look at \(k\).</strong><br>
\(k=-1\) (and empty) means coordinates suffice and <em>the physical content is zero</em>.<br>
\(k=0\) (with matter) means a conformal transformation is required and <em>masses move</em>.<br>
── <strong>This is the most concrete meaning of Episode 3's "not a coordinate change but a conformal transformation".</strong></p>
</div>

<h2><span class="n">07</span>Where has this series been?</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>Milne would be Step 1</strong><span>already flat, so <em>not even the masses need to move</em></span></div></div>
<div class="row hi"><div class="mk">2</div><div class="txt"><strong>Every FLRW is Step 2</strong><span>Weyl \(=0\), Ricci \(\ne0\) — which is why Episode 4 could "delete everything deletable and be left with one mass"</span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>Schwarzschild would be Step 3</strong><span>a conformal transformation cannot flatten it — which is why black holes were on "the side that does not move" in Episode 6</span></div></div>
</div>

<p><strong>The range where this series' tool works coincides exactly with the Step 2 row.</strong> Episode 13 measured "a conformal transformation touches only size" and Episode 16 "it can move only the unused side" — <em>today restates those in the language of geometry</em>.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① That the Milne universe is flat spacetime is an exact result.</strong> The coordinate change \(T=t\cosh\chi,\ R=ct\sinh\chi\) makes it a portion of Minkowski spacetime (inside the light cone) — <em>"a portion" matters: Milne coordinates do not cover all of Minkowski spacetime</em>.</p>
<p style="margin:0 0 10px"><strong>② "Every FLRW has Weyl \(=0\)" follows from homogeneity and isotropy.</strong> Add perturbations and \(C\ne0\), moving it to Step 3 — <strong>the real universe is not exactly FLRW, which is why Episode 6's occupancy is not zero</strong> (\(1.5\times10^{-18}\)). The tables in §02 and §03 are <em>statements about the background spacetime</em>.</p>
<p style="margin:0 0 10px"><strong>③ §04's \(\Lambda\)CDM comes from a numerical integration here with \(\Omega_m=0.315\), \(\Omega_r=9.2\times10^{-5}\).</strong> Milne's \(H_0d_L/c=z(1+z/2)\) and \(R_h=ct\)'s \((1+z)\ln(1+z)\) are closed forms. <em>Real supernova analyses leave the absolute magnitude (a constant offset) free, so the \(\Delta\mu\) here cannot be converted directly into significance</em> — the figure's "supernovae needed" is <strong>an indication for a fixed constant offset</strong>.</p>
<p style="margin:0 0 10px"><strong>④ "Milne is closer to \(\Lambda\)CDM" holds near \(z\simeq1\).</strong> At \(z=0.5\) it is not much different from \(R_h=ct\), and at \(z=2\) Milne is the further one (\(+0.179\) mag). <em>Picking a particular \(z\) changes the story</em>, so read it as an order and a trend.</p>
<p style="margin:0"><strong>⑤ The verdict on \(R_h=ct\) was handled in Episode 3.</strong> This document does not re-examine it and treats only <em>its structural difference from Milne</em>. The academic standard remains \(\Lambda\)CDM.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Find the scalar curvature of an FLRW with \(a=t\) and show it vanishes at \(k=-1\).
<details><summary>Show the answer</summary><div class="ans">Into \(R=6[\ddot a/a+(\dot a/a)^2+k/a^2]\) put \(a=t\): \(\ddot a=0\), \(\dot a/a=1/t\), \(k/a^2=k/t^2\), so \(R=6(1+k)/t^2\). <strong>Exactly zero at \(k=-1\).</strong></div></details></li>

<li>What is the essential difference between Milne and \(R_h=ct\)?
<details><summary>Show the answer</summary><div class="ans"><strong>Whether the Riemann tensor vanishes.</strong> Milne's vanishes identically (it is Minkowski in other coordinates); \(R_h=ct\) has \(R=6/(ct)^2\ne0\). <em>So Milne needs only a coordinate change, and \(R_h=ct\) needs a conformal transformation.</em></div></details></li>

<li>State the three-step test and classify \(\Lambda\)CDM and Schwarzschild.
<details><summary>Show the answer</summary><div class="ans">Step 1: Riemann \(=0\) → coordinates suffice. Step 2: Riemann \(\ne0\) but Weyl \(=0\) → a conformal transformation is required. Step 3: Weyl \(\ne0\) → neither works. <strong>\(\Lambda\)CDM is Step 2</strong> (as is every FLRW); <strong>Schwarzschild is Step 3</strong>.</div></details></li>

<li>At \(z=1\), which is closer to \(\Lambda\)CDM?
<details><summary>Show the answer</summary><div class="ans"><strong>Milne</strong> (1.500 against \(\Lambda\)CDM's 1.529, a gap of 0.042 mag); \(R_h=ct\) gives 1.386, a gap of 0.213. <em>An empty spacetime fits the Hubble diagram better than \(R_h=ct\)</em> — which is why "fits the Hubble diagram" is a weak test.</div></details></li>

<li>(Harder) State the range where this series' tool works, in the language of the three-step test.
<details><summary>Show the answer</summary><div class="ans"><strong>It coincides exactly with the Step 2 row.</strong> At Step 1 (Milne) the spacetime is already flat and not even the masses need to move; at Step 3 (Schwarzschild) a conformal transformation cannot flatten it. <em>Every FLRW being at Step 2 is precisely what allowed Episode 4's "delete everything deletable and be left with one mass"</em> — a geometric restatement of the tool's limit as measured in Episodes 13 and 16.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — look at \(k\) and it is settled</h2>
<p>The Milne universe and \(R_h=ct\) both have \(a\propto t\) and are both described as "neither decelerating nor accelerating". Only \(k\) and the contents differ — <strong>and computing the scalar curvature settles it</strong>. With \(a=t\), \(R=6(1+k)/t^2\), which is <em>exactly zero at \(k=-1\)</em>. The whole Riemann tensor vanishes identically, so <strong>Milne is Minkowski spacetime in different coordinates</strong>. \(R_h=ct\) has \(R=3.5\times10^{-52}\ \mathrm{m^{-2}}\) (curvature radius 1.73 Gpc), which is not zero.</p>
<p>From this a general <strong>three-step test</strong> follows — Step 1: Riemann \(=0\), coordinates suffice and there is no physical content. Step 2: Weyl \(=0\), a conformal transformation is required and masses move. Step 3: Weyl \(\ne0\), neither works. <strong>Every FLRW falls in Step 2</strong> — <em>the place this series has occupied since Episode 1, pinned down by one line.</em></p>
<p>Comparing luminosity distances gives a surprise. At \(z=1\), <strong>Milne is closer to \(\Lambda\)CDM</strong> (0.042 mag against \(R_h=ct\)'s 0.213) — <em>an empty spacetime fits the Hubble diagram better</em>. And yet Milne is decisively excluded by the CMB, nucleosynthesis, structure formation and the measurement of \(\Omega_m\) (over 45σ). <strong>Good geometry with nothing in it is not physics</strong> — the same structure as Episode 25's "\(L(\text{residual})\) is not the Hubble diagram alone" and Episode 29's "the question is not one question".</p>
<p>And the reveal — <strong>tell them apart by looking at \(k\)</strong>. \(k=-1\) (and empty) means coordinates suffice and the physical content is zero; \(k=0\) (with matter) means a conformal transformation is required and masses move. <em>This is the most concrete meaning of Episode 3's "not a coordinate change but a conformal transformation".</em></p>
</div>

<div class="next">
<span class="lbl">Next — Episode 34</span>
Next: <strong>conformal gravity (Mannheim)</strong>. Every theory so far has used the conformal transformation as <em>a rewriting bolted on afterwards</em>. Mannheim does not — <strong>he puts conformal symmetry itself at the foundation of gravity</strong>. Replace the Einstein–Hilbert action with the square of the Weyl tensor, \(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\), and the whole theory is conformally invariant from the start. <em>The cosmological constant problem then disappears structurally, and rotation curves come out without dark matter</em> — at a price. <strong>The ghosts scheduled for Part V arrive early.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sz=document.getElementById('sz'), vz=document.getElementById('vz'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=34, Y1=310;
  var xmin=0.05, xmax=2.0, ymin=-0.30, ymax=0.25;
  var SIG=0.15;
  var Om=0.315, Or=9.2e-5, OL=0.685;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function dlR(z){ return (1+z)*Math.log(1+z); }
  function dlM(z){ return z*(1+z/2); }
  function dlL(z){
    var n=600, s=0, dz=z/n;
    for(var i=0;i<=n;i++){
      var zz=i*dz;
      var E=Math.sqrt(Or*Math.pow(1+zz,4)+Om*Math.pow(1+zz,3)+OL);
      var w=(i===0||i===n)?0.5:1;
      s+=w/E;
    }
    return (1+z)*s*dz;
  }
  function dmu(f,z){ return 5*Math.log(f(z)/dlL(z))/Math.LN10; }

  function draw(){
    var z=parseInt(sz.value,10)/100;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.fillStyle='#eef0f2';
    g.fillRect(X0, py(SIG), X1-X0, py(-SIG)-py(SIG));
    g.fillStyle='#a6adb4'; g.textAlign='left';
    g.fillText('intrinsic scatter of one supernova, ±0.15 mag', X0+10, py(SIG)-7);

    g.textAlign='right';
    for(var e=-0.3;e<=0.25;e+=0.1){
      var y=py(e);
      g.strokeStyle=(Math.abs(e)<1e-9?'#ccd2d8':'#f3f5f7'); g.lineWidth=(Math.abs(e)<1e-9?1.6:1);
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#96a0a8'; g.fillText(e.toFixed(1), X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0.5;q<=2.0;q+=0.5){
      var x=px(q);
      g.strokeStyle='#f8fafb'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#96a0a8'; g.fillText('z = '+q.toFixed(1), x, Y1+16);
    }
    g.strokeStyle='#c8d0d6'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    function curve(f,col){
      g.strokeStyle=col; g.lineWidth=3.2; g.beginPath();
      for(var i=0;i<=160;i++){
        var zz=xmin+(xmax-xmin)*i/160;
        var y=dmu(f,zz);
        if(i===0) g.moveTo(px(zz),py(Math.min(Math.max(y,ymin),ymax)));
        else g.lineTo(px(zz),py(Math.min(Math.max(y,ymin),ymax)));
      }
      g.stroke();
    }
    curve(dlM,'#2a3a4a');
    curve(dlR,'#9a6a2a');

    g.textAlign='left';
    g.fillStyle='#2a3a4a'; g.fillText('Milne', px(1.75), py(dmu(dlM,1.75))-10);
    g.fillStyle='#9a6a2a'; g.fillText('R_h=ct', px(1.75), py(dmu(dlR,1.75))+18);

    g.strokeStyle='#7a848c'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(z),Y0); g.lineTo(px(z),Y1); g.stroke();
    g.setLineDash([]);
    var ym=dmu(dlM,z), yr=dmu(dlR,z);
    [[ym,'#2a3a4a'],[yr,'#9a6a2a']].forEach(function(q){
      g.fillStyle=q[1];
      g.beginPath(); g.arc(px(z),py(Math.min(Math.max(q[0],ymin),ymax)),5,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=1.6;
      g.beginPath(); g.arc(px(z),py(Math.min(Math.max(q[0],ymin),ymax)),5,0,6.2832); g.stroke();
    });

    g.fillStyle='#7d868e'; g.textAlign='center';
    g.fillText('redshift  z', (X0+X1)/2, Y1+38);
    g.save(); g.translate(19,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('departure from ΛCDM,  Δμ [mag]', 0,0); g.restore();

    function need(d){ return d===0?Infinity:Math.pow(5*SIG/Math.abs(d),2); }
    vz.textContent='z = '+z.toFixed(2);
    ro.textContent='z = '+z.toFixed(2)+
      '　Milne Δμ = '+ym.toFixed(3)+' mag ('+Math.ceil(need(ym))+' SNe for 5σ)'+
      '　/　R_h=ct Δμ = '+yr.toFixed(3)+' mag ('+Math.ceil(need(yr))+' SNe for 5σ)'+
      (Math.abs(ym)<Math.abs(yr) ? '　★ Milne is closer to ΛCDM' : '');
  }
  sz.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-33-milne.html', acc='#2a3a4a', ops='#9a6a2a',
      title='Milne versus R_h=ct ── c·t = const, That Clicks, Episode 33',
      ep='EPISODE 33 ／ Part IV — the two hardest cases to tell apart',
      eyebrow='There is one way to tell them apart — look at \\(k\\)',
      h1='Milne versus<br>\\(R_h=ct\\)',
      sub='Both have \\(a\\propto t\\). Yet Milne returns to flat spacetime by a change of coordinates and \\(R_h=ct\\) does not.<br><em>Coordinate change, or conformal transformation? We build the procedure.</em>',
      byline_l='What you need: the FLRW scalar curvature, division',
      byline_r='\\(R=6(1+k)/t^2\\) — zero at \\(k=-1\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 33 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That the Milne universe (Milne 1935) is an empty open FLRW (\\(\\rho=0\\), \\(k=-1\\), \\(a\\propto t\\)) and becomes a portion of Minkowski spacetime under the coordinate change \\(T=t\\cosh\\chi,\\ R=ct\\sinh\\chi\\) is a standard result — <em>"a portion" matters: Milne coordinates do not cover all of Minkowski spacetime</em>. The FLRW scalar curvature \\(R=6[\\ddot a/a+(\\dot a/a)^2+k/a^2]\\) and the conformal flatness of FLRW (vanishing Weyl tensor) are also standard. The relation \\(R=6(1+k)/t^2\\), today\'s value \\(3.52\\times10^{-52}\\ \\mathrm{m^{-2}}\\) for \\(R_h=ct\\) (curvature radius 1.73 Gpc), and the luminosity distance comparison are computed here (kenshou/calc37.py). <strong>"Every FLRW has Weyl \\(=0\\)" is a statement about the homogeneous, isotropic background; perturbations give \\(C\\ne0\\)</strong> — the real universe is not exactly FLRW, which is why Episode 6\'s occupancy is not zero. The \\(\\Lambda\\)CDM values come from a numerical integration here with \\(\\Omega_m=0.315\\), \\(\\Omega_r=9.2\\times10^{-5}\\); Milne\'s \\(H_0d_L/c=z(1+z/2)\\) and \\(R_h=ct\\)\'s \\((1+z)\\ln(1+z)\\) are closed forms. <strong>Real supernova analyses leave the absolute magnitude free, so the \\(\\Delta\\mu\\) here cannot be converted directly into significance</strong> — the figure\'s "SNe for 5σ" assumes a fixed constant offset. "Milne is closer to \\(\\Lambda\\)CDM" holds near \\(z\\simeq1\\) and reverses by \\(z=2\\). \\(\\Omega_m=0.315\\pm0.007\\) is the Planck value. The verdict on \\(R_h=ct\\) was handled in Episode 3; this document treats only its structural difference from Milne. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination, and the academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider moves through redshift and reads off the supernovae needed for a 5σ distinction. "Show the answer" opens each solution.')
