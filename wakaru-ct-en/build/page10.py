# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Temperature does not move in this picture. \(\tilde T=aT\) cancels the standard \(T\propto1/a\) exactly — <strong>the universe sits at 2.7255 K and never cools</strong>. So the energy needed to erase one bit (the Landauer limit \(k_BT\ln2\)) is constant across the whole history of the universe. A quantity that falls as \(1/a\) in the standard picture is pinned here. <em>Which is the "real" cost of erasure?</em> As usual, that is not yet a sentence.</p>

<h2><span class="n">01</span>Temperature is pinned, so the price is pinned</h2>

<div class="calc">
<span class="tag">The Landauer limit in this picture</span>
$$\tilde T=aT=\text{const}=2.7255\ \mathrm{K}$$
$$k_B\tilde T\ln2=2.61\times10^{-23}\ \mathrm{J}=1.63\times10^{-4}\ \mathrm{eV}\qquad(\text{forever})$$
</div>

<p>In the standard picture this quantity was larger in the past and has fallen as \(1/a\). Here it has been \(1.63\times10^{-4}\) eV from the beginning until today. <strong>Two exactly opposite statements about exactly the same universe.</strong></p>

<h2><span class="n">02</span>Applying Episode 3's surgery to a price</h2>

<p>\(k_BT\ln2\) is an energy — <em>dimensionful</em>. Run it through the decision procedure and it lands in the left column: bookkeeping. So "erasing one bit costs \(1.63\times10^{-4}\) eV" is not by itself a claim. You must say <strong>compared with what</strong>.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Compare the erasure cost with…</th><th class="mid">Today</th><th class="mid">Time dependence</th></tr></thead>
<tbody>
<tr><th>Electron rest mass \(m_ec^2\)</th><td class="mid">\(4.6\times10^{-10}\)</td><td class="mid">\(\propto1/t\) (<strong>gets cheaper</strong>)</td></tr>
<tr><th>One CMB photon's energy</th><td class="mid">\(\sim1\)</td><td class="mid">constant</td></tr>
<tr><th>The Planck energy</th><td class="mid">\(1.9\times10^{-32}\)</td><td class="mid">changes with epoch</td></tr>
<tr class="hi"><th>nothing at all</th><td class="mid">──</td><td class="mid"><strong>there is no claim</strong></td></tr>
</tbody>
</table>
</div>

<p>Against particle masses, erasing information <em>gets relatively cheaper with time</em>. Against a single photon it is eternally the same. Both are right. <strong>Only the comparison partner differs.</strong></p>

<div class="aside">
<span class="tag">"Conformally invariant" and "constant in time" are different</span>
The ratio \(k_BT/E_P\) is <em>conformally invariant</em> (both weight \(-1\)) — and it <em>does vary in time</em>. This is the same trap as Exercise 5 of Episode 8, and the easiest mistake in the whole series: <strong>not moving under a gauge choice and not moving in time are different things</strong>. The first asks "physics or bookkeeping?"; the second asks "what is happening in the universe?".
</div>

<h2><span class="n">03</span>One more thing that has to be named</h2>

<p>Naming the comparison partner is still not enough. The Landauer limit contains a \(T\) — <strong>you must say which heat bath you are dumping into</strong>. That is a demand of thermodynamics itself, nothing to do with conformal transformations.</p>

<p>So let us line up every bath the universe offers and ask the same question: <em>using the entire energy of the universe, how many bits could be erased?</em></p>

<div class="calc">
<span class="tag">Just a division</span>
<p class="lbl">Total energy inside the horizon (the identity used in Episode 1)</p>
$$E=\frac{c^4R_H}{2G}=7.90\times10^{69}\ \mathrm{J}$$
<p class="lbl">Bits erasable</p>
$$N_{\rm erase}=\frac{E}{k_BT\ln2}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Erase at which temperature</th><th class="mid">\(T\)</th><th class="mid">Price per bit</th><th class="mid">Bits erasable</th><th class="mid">Ratio to memory \(N\)</th></tr></thead>
<tbody>
<tr class="hi"><th>Hubble (horizon) temperature</th><td class="mid">\(2.79\times10^{-30}\) K</td><td class="mid">\(2.67\times10^{-53}\) J</td><td class="mid"><strong>\(2.96\times10^{122}\)</strong></td><td class="mid"><strong>1.0000</strong></td></tr>
<tr><th>CMB temperature</th><td class="mid">2.7255 K</td><td class="mid">\(2.61\times10^{-23}\) J</td><td class="mid">\(3.03\times10^{92}\)</td><td class="mid">\(1.0\times10^{-30}\)</td></tr>
<tr><th>Room temperature</th><td class="mid">300 K</td><td class="mid">\(2.87\times10^{-21}\) J</td><td class="mid">\(2.75\times10^{90}\)</td><td class="mid">\(9.3\times10^{-33}\)</td></tr>
<tr><th>Planck temperature</th><td class="mid">\(1.42\times10^{32}\) K</td><td class="mid">\(1.36\times10^{9}\) J</td><td class="mid">\(5.83\times10^{60}\)</td><td class="mid">\(2.0\times10^{-62}\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0">Spending the entire energy of the universe, <strong>erasing at the CMB temperature clears only \(10^{-30}\) of the memory.</strong><br>
Writable \(10^{122}\) bits, erasable \(10^{92}\) — <em>thirty orders short.</em></p>
</div>

<p>Episode 1 counted "one operation per 28.5 bits". This is far more extreme: <strong>the universe can erase only \(10^{-30}\) of what it can write</strong>. A nearly write-once medium.</p>

<div class="fig">
<p class="cap">Figure: which bath you dump into, across; bits erasable with the entire energy of the universe, up. <strong>The grey horizontal line is the writable count \(N=2.96\times10^{122}\)</strong>. The two meet at exactly one point — <em>the Hubble temperature</em>.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Bath temperature \(T\) (log)<input id="st" type="range" min="0" max="1000" value="484" step="1"></label>
  <span class="val" id="vt">2.73 K</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6b5320"></i>bits erasable \(E/k_BT\ln2\)</span>
  <span><i class="swatch" style="background:#9aa0a8"></i>bits writable \(N\)</span>
  <span><i class="swatch" style="background:#2f5f6b"></i>landmarks (horizon, CMB, room, Planck)</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The reveal — what "exactly at the Landauer limit" really was</h2>

<p>Extra 2 of the previous series contained the most striking number in the whole series — <strong>the universe's energy per bit matches the Landauer limit at a ratio of 1.000000</strong>.</p>

<div class="calc">
<span class="tag">That coincidence</span>
$$\frac{E}{N}=2.672\times10^{-53}\ \mathrm{J},\qquad k_BT_H\ln2=2.672\times10^{-53}\ \mathrm{J}$$
</div>

<p>That is the first row of the table. And now it is clear — <strong>it was an identity</strong>. \(E=T_HS\) holds in any FLRW, so it is <em>not a physical claim</em> that the universe runs at the limit. It is the horizon's energy divided by the horizon's temperature and the horizon's entropy.</p>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0">"The universe sits exactly at the Landauer limit" is <strong>just reading off an identity</strong>.<br>
Meaning appears only <em>when you choose a different temperature</em> — and the moment you do, out comes a <strong>real number</strong>: \(10^{-30}\).</p>
</div>

<p>This applies the previous series' decision procedure to a "beautiful coincidence". <em>An identity is not physics</em> — exactly the verdict Extra 3 delivered on Dirac's large numbers.</p>

<h2><span class="n">05</span>Comparing with real machines</h2>

<div class="calc">
<span class="tag">Computers on the ground</span>
<p class="lbl">Landauer limit at room temperature</p>
$$k_B\!\cdot\!300\,\mathrm{K}\cdot\ln2=2.87\times10^{-21}\ \mathrm{J}=0.0179\ \mathrm{eV}$$
<p class="lbl">A modern CPU per operation (roughly)</p>
$$\sim10^{-15}\ \mathrm{J}\qquad\Longrightarrow\qquad \text{about }3.5\times10^{5}\ \text{times the limit}$$
</div>

<p>Human computers are still five and a half orders from the limit. The universe (measured at the horizon temperature) sits exactly on it — <em>though we have just seen that this is an identity</em>.</p>

<h2><span class="n">06</span>Entropy itself does not move</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Weight</th><th class="mid">In this picture</th></tr></thead>
<tbody>
<tr class="hi"><th>Entropy \(S/k_B\)</th><td class="mid">\(0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr class="hi"><th>The second law</th><td class="mid">──</td><td class="mid"><strong>untouched</strong></td></tr>
<tr><th>Temperature \(T\)</th><td class="mid">\(-1\)</td><td class="mid">\(\times a\) (constant here)</td></tr>
<tr><th>Landauer cost \(k_BT\ln2\)</th><td class="mid">\(-1\)</td><td class="mid">\(\times a\) (likewise)</td></tr>
<tr><th>Boltzmann factor \(e^{-E/k_BT}\)</th><td class="mid">\(0\)</td><td class="mid"><strong>invariant</strong></td></tr>
</tbody>
</table>
</div>

<p>The \(3.1\times10^{104}\) counted in Episode 6 and the recombination factor \(52.6\) used in Episode 4 are both unchanged to the letter. <strong>Thermodynamics comes through entirely intact, so long as it is written dimensionlessly.</strong></p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① The Landauer limit is a lower bound per logically irreversible operation.</strong> Reversible computation can in principle cost nothing. The "bits erasable" here assumes every erasure is irreversible; it is not a claim about how the universe actually operates.</p>
<p style="margin:0 0 10px"><strong>② \(E=c^4R_H/2G\) is an identity of flat FLRW</strong> (Episode 1; Extra 3 of the previous series). Defining the "total energy" inside the horizon this way is natural, but energy in general relativity has no unique definition — quasi-local energies differ, and so do the values.</p>
<p style="margin:0 0 10px"><strong>③ The "bits erasable" column is an upper bound assuming all the energy can be spent on erasure.</strong> In practice you need machinery to extract the energy and dump the heat, whose efficiency is not included. Read it as an order-of-magnitude argument.</p>
<p style="margin:0 0 10px"><strong>④ Using the Hubble temperature \(T_H=\hbar H/2\pi k_B\) as the Landauer \(T\) does not go beyond metaphor.</strong> It corresponds to the Gibbons–Hawking temperature of a de Sitter horizon, and whether it acts as a heat bath in a general FLRW is not obvious. <em>The first row is "exact" because of an identity, not because of a physical mechanism</em> — which is the whole point of §04.</p>
<p style="margin:0"><strong>⑤ The \(10^{-15}\) J per CPU operation is an order-of-magnitude marker.</strong> It shifts by orders depending on what counts as an operation (a logic gate, an instruction).</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Why is the Landauer cost constant in this picture?
<details><summary>Show the answer</summary><div class="ans">Temperature has weight \(-1\), so \(\tilde T=aT\); in the standard picture \(T\propto1/a\), and the two cancel to \(\tilde T=\)const. Hence \(k_B\tilde T\ln2\) is constant too (\(1.63\times10^{-4}\) eV). <em>It is the same quantity that falls as \(1/a\) in the standard picture.</em></div></details></li>

<li>Is "erasing one bit costs \(1.63\times10^{-4}\) eV" a claim by itself?
<details><summary>Show the answer</summary><div class="ans">No. Energy is dimensionful — bookkeeping — so it means nothing until you say <strong>compared with what</strong>. Against the electron mass it is \(4.6\times10^{-10}\) and gets cheaper with time; against one CMB photon it is constant. The same surgery Episode 3 applied to the series title.</div></details></li>

<li>With the whole energy of the universe, how many bits can be erased at CMB temperature? Compare with the memory.
<details><summary>Show the answer</summary><div class="ans">\(E/(k_BT_0\ln2)=7.90\times10^{69}/2.61\times10^{-23}=3.03\times10^{92}\) bits — <strong>\(10^{-30}\)</strong> of the memory \(2.96\times10^{122}\). <em>It can erase one billionth of one billionth of one billionth of what it can write.</em></div></details></li>

<li>Is "the universe runs exactly at the Landauer limit" a physical claim?
<details><summary>Show the answer</summary><div class="ans">No — it is an <strong>identity</strong>. \(E=T_HS\) holds in any FLRW, so \(E/N=k_BT_H\ln2\) is automatically 1.000000. <em>Meaning appears only when you choose a different temperature</em>, and at the CMB temperature out comes the real number \(10^{-30}\). The same verdict Extra 3 of the previous series gave Dirac's large numbers: an identity is not physics.</div></details></li>

<li>(Harder) Entropy is conformally invariant but temperature moves. Is that a contradiction?
<details><summary>Show the answer</summary><div class="ans">No. \(S/k_B\) is <strong>a bit count, dimensionless</strong>, so it cannot move; \(T\) is <strong>an energy, dimensionful</strong>, so it does. Both hold at once. Indeed in \(E=TS\) the left side has weight \(-1\), matching \(T\) (\(-1\)) \(\times S\) (\(0\)). <em>The very fact that entropy is an amount of information is what shields it from the bookkeeping.</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — the price is undefined until you name the temperature</h2>
<p>Temperature is pinned here (\(\tilde T=aT=\)const \(=2.7255\) K), so the Landauer limit \(k_BT\ln2=1.63\times10^{-4}\) eV is <strong>constant</strong> across the whole history of the universe — the same quantity that falls as \(1/a\) in the standard picture. Which is true? <em>Not yet a sentence.</em> Energy is dimensionful, so nothing is claimed until a comparison is named: against the electron mass it gets cheaper with time, against one CMB photon it is eternally the same.</p>
<p>And this episode found a second thing that must be named — <strong>which bath you dump into</strong>. Counting how many bits the universe's entire energy \(E=7.90\times10^{69}\) J could erase: \(2.96\times10^{122}\) at the Hubble temperature, \(3.03\times10^{92}\) at CMB temperature, \(2.75\times10^{90}\) at room temperature, \(5.83\times10^{60}\) at the Planck temperature. <em>Sixty orders of magnitude depending on the choice.</em></p>
<p>The second row bites hardest: <strong>erasing at CMB temperature, the universe can clear only \(10^{-30}\) of what it can write.</strong> Writable \(10^{122}\), erasable \(10^{92}\) — an asymmetry far more extreme than Episode 1's "one operation per 28.5 bits". <em>The universe is a nearly write-once medium.</em></p>
<p>And the reveal. The most striking number of the previous series — energy per bit matching the Landauer limit at 1.000000 — is the first row of that table, and it was <strong>an identity</strong>. \(E=T_HS\) holds in any FLRW, so measuring at the horizon temperature always gives exactly one. <em>Meaning appears only at another temperature.</em> An identity is not physics — the same verdict passed on Dirac's large numbers in Episode 7. Entropy itself, being dimensionless, does not move at all here: thermodynamics comes through intact so long as it is written dimensionlessly.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 11</span>
Next: <strong>light</strong>. We have written many times that light passes straight through a conformal transformation, but never treated it head on. Look at a photon gas in this picture and — <em>number density, energy density, temperature, all constant</em>. <strong>Completely at rest.</strong> Nothing has happened to light in the entire history of the universe; only matter has been growing. The result of Episode 7 of the previous series — that the 4D Maxwell action is exactly conformally invariant, going as \(\Omega^{D-4}\) — shows itself in its most naked form. And we watch, in numbers, the moment redshift stops being "light stretched" and becomes entirely "<strong>the receiver grew</strong>".
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var st=document.getElementById('st'), vt=document.getElementById('vt'), ro=document.getElementById('ro');
  var X0=78, X1=700, Y0=30, Y1=318;
  var kB=1.380649e-23, ln2=Math.log(2);
  var E=7.8980e69, N=2.9556e122;
  var xmin=-31, xmax=33;
  var ymin=55, ymax=126;
  var MARKS=[[-29.554,'horizon'],[0.435,'CMB'],[2.477,'room'],[32.151,'Planck']];

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function lg(v){ return Math.log(v)/Math.LN10; }

  function draw(){
    var f=parseInt(st.value,10)/1000;
    var T=Math.pow(10, xmin+ (xmax-xmin)*f);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=60;e<=125;e+=10){
      var y=py(e);
      g.strokeStyle='#f2efe6'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a49a86'; g.fillText('10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-30;q<=30;q+=10){
      var x=px(q);
      g.strokeStyle='#f8f6f1'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a49a86'; g.fillText('10'+q, x, Y1+16);
    }
    g.strokeStyle='#cdc6b5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    g.strokeStyle='#9aa0a8'; g.lineWidth=2.4; g.setLineDash([7,5]);
    g.beginPath(); g.moveTo(X0,py(lg(N))); g.lineTo(X1,py(lg(N))); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#7f858c'; g.textAlign='right';
    g.fillText('bits writable  N = 2.96×10¹²²', X1-8, py(lg(N))-8);

    g.strokeStyle='#6b5320'; g.lineWidth=3.4; g.beginPath();
    var first=true;
    for(var i=0;i<=300;i++){
      var lx=xmin+(xmax-xmin)*i/300;
      var y=lg(E/(kB*Math.pow(10,lx)*ln2));
      if(y<ymin||y>ymax){ first=true; continue; }
      if(first){ g.moveTo(px(lx),py(y)); first=false; } else g.lineTo(px(lx),py(y));
    }
    g.stroke();

    MARKS.forEach(function(m){
      var y=lg(E/(kB*Math.pow(10,m[0])*ln2));
      if(y<ymin||y>ymax) return;
      g.fillStyle='#2f5f6b';
      g.beginPath(); g.arc(px(m[0]),py(y),4.5,0,6.2832); g.fill();
      g.fillStyle='#2f5f6b'; g.textAlign='left';
      g.fillText(m[1], px(m[0])+8, py(y)-7);
    });

    g.strokeStyle='#6b5320'; g.lineWidth=1.5; g.setLineDash([3,3]);
    g.beginPath(); g.moveTo(px(lg(T)),Y0); g.lineTo(px(lg(T)),Y1); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#8a8272'; g.textAlign='center';
    g.fillText('bath temperature  T [K]', (X0+X1)/2, Y1+36);

    var nb=E/(kB*T*ln2);
    vt.textContent = (T<1e-3||T>1e5) ? T.toExponential(2)+' K' : T.toPrecision(3)+' K';
    ro.textContent='T = '+vt.textContent+
      '　price per bit '+(kB*T*ln2).toExponential(2)+' J'+
      '　→　bits erasable '+nb.toExponential(3)+
      '　/　'+(nb/N).toExponential(2)+' of what is writable'+
      (Math.abs(nb/N-1)<0.02 ? '　★ exactly equal (an identity)' : '');
  }
  st.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-10-erase.html', acc='#6b5320', ops='#2f5f6b',
      title='Substituting into heat and information ── c·t = const, That Clicks, Episode 10',
      ep='EPISODE 10 ／ In a universe that never cools, what does one bit cost?',
      eyebrow='"Exactly at the Landauer limit" was just reading off an identity',
      h1='Substituting into<br>heat and information',
      sub='Temperature is pinned here — the universe sits at 2.7255 K and never cools,<br>so the cost of erasing a bit is fixed. <em>Is that expensive, or cheap?</em>',
      byline_l='What you need: division, the Landauer limit',
      byline_r='writable \\(10^{122}\\), erasable \\(10^{92}\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 10 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. Landauer\'s principle (at least \\(k_BT\\ln2\\) is dissipated per logically irreversible bit erasure), the dimensionlessness of entropy, and the weight \\(-1\\) of temperature under a conformal transformation are all standard. Reversible computation can in principle erase at zero cost — the "bits erasable" here assumes every operation is irreversible and is an upper bound, not a claim about how the universe operates. \\(E=c^4R_H/2G\\) is an identity of flat FLRW (Extra 3 of the previous series), and quasi-local energy in general relativity has no unique definition. The Hubble temperature \\(T_H=\\hbar H/2\\pi k_B\\) corresponds to the Gibbons–Hawking temperature of a de Sitter horizon; whether it acts as a heat bath in a general FLRW is not obvious, and the "exact match" in the first row follows from the identity \\(E=T_HS\\) rather than from any physical mechanism (this is the point of §04). The numbers (\\(k_BT_0\\ln2=2.61\\times10^{-23}\\) J \\(=1.63\\times10^{-4}\\) eV, \\(E=7.90\\times10^{69}\\) J, erasable counts \\(2.96\\times10^{122}\\)/\\(3.03\\times10^{92}\\)/\\(2.75\\times10^{90}\\)/\\(5.83\\times10^{60}\\), and \\(1.0\\times10^{-30}\\) of memory at CMB temperature) are computed here; extraction and heat-rejection machinery and efficiency are not included. The \\(10^{-15}\\) J per CPU operation is an order-of-magnitude marker that shifts by orders with the definition of an operation. Extra 2 of the previous series also states explicitly that the 1.0000 match of energy per bit with the Landauer limit is an identity. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination and conflicts with nucleosynthesis when extrapolated into the early universe (Lewis, Barnes &amp; Kaushik 2016). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the bath temperature and the two lines meet only at the horizon temperature. "Show the answer" opens each solution.')
