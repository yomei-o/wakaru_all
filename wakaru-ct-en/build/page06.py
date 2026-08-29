# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 1 divided memory by operations, Episode 2 divided two clocks, Episode 5 divided fit by parameters. This time we do not divide — <strong>we open the memory and look inside</strong>. Capacity: \(10^{122}\) bits. In use: \(1.5\times10^{-18}\) of it. Essentially empty. And chasing that emptiness lands us on <em>why the conformal transformation works on the universe at all</em> — the foundation this whole series stands on.</p>

<h2><span class="n">01</span>Capacity, and how much is used</h2>

<div class="calc">
<span class="tag">Two numbers</span>
<p class="lbl">Capacity (the holographic bound on the horizon)</p>
$$\frac{S_{\max}}{k_B}=\frac{A_H}{4\ell_P^2}=2.05\times10^{122}\qquad(=2.96\times10^{122}\ \text{bit})$$
<p class="lbl">In use (the census of Egan &amp; Lineweaver 2010)</p>
$$\frac{S_{\rm obs}}{k_B}=3.1\times10^{104}$$
<p class="lbl">Divide</p>
$$\text{occupancy}=1.51\times10^{-18}$$
</div>

<p>Written out in zeros, <strong>99.9999999999999998%</strong> of it is free. The previous series quoted this number once; here we dig past it.</p>

<h2><span class="n">02</span>The occupancy was a ratio of areas all along</h2>

<p>Today's entropy is almost entirely supermassive black holes. And a black hole's entropy and the cosmic horizon's entropy are written by <em>exactly the same formula</em> — \(S=k_BA/4\ell_P^2\). So the division cancels \(\ell_P\) and leaves <strong>a bare ratio of areas</strong>.</p>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
$$\text{occupancy}=\frac{\sum A_{\rm BH}}{A_H}=1.51\times10^{-18}$$
<p style="margin:10px 0 0">Add up the horizons of every black hole in the universe and divide by the area of the cosmic horizon — <em>that</em> is what "memory occupancy" is.</p>
</div>

<div class="calc">
<span class="tag">Glue them into a single sphere</span>
$$A_H=4\pi R_H^2=2.14\times10^{53}\ \mathrm{m^2}\qquad\Longrightarrow\qquad \sum A_{\rm BH}=3.24\times10^{35}\ \mathrm{m^2}$$
<p class="lbl">as a radius</p>
$$r=\sqrt{\frac{\sum A_{\rm BH}}{4\pi}}=1.61\times10^{17}\ \mathrm{m}=\mathbf{17\ \text{light years}}$$
</div>

<p>Sew together the horizons of every black hole in the observable universe and you get a sphere of radius 17 light years — 34 across, about far enough from the Sun to just include Vega and Arcturus. <strong>Nearly all of the universe's information is written on that.</strong></p>

<h2><span class="n">03</span>Which side is in use?</h2>

<p>Extra 2 of the previous series had a table splitting the gravitational field in two — <em>the conformal-factor side</em> (gauge, bookkeeping, no arrow of time) and <em>the Weyl-tensor side</em> (physics, gravitational entropy, arrow of time). That was structure only. Now we can put numbers in.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Contents</th><th class="mid">\(S/k_B\)</th><th class="mid">Share</th><th class="mid">Which side</th></tr></thead>
<tbody>
<tr class="hi"><th>Supermassive black holes</th><td class="mid">\(3.1\times10^{104}\)</td><td class="mid">≈ 1</td><td class="mid"><strong>Weyl side</strong></td></tr>
<tr><th>CMB photons</th><td class="mid">\(2.03\times10^{88}\)</td><td class="mid">\(6.5\times10^{-17}\)</td><td class="mid">matter/radiation</td></tr>
<tr><th>Neutrinos</th><td class="mid">\(1.93\times10^{88}\)</td><td class="mid">\(6.2\times10^{-17}\)</td><td class="mid">matter/radiation</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §03</p>
<p style="margin:6px 0 0"><strong>99.999999999999986%</strong> of today's cosmic entropy sits on the gravitational side.</p>
</div>

<p>The table from Extra 2 has acquired numbers. <strong>The memory in use is almost entirely the Weyl side.</strong> The conformal-factor side — the \(\phi\) this series has been moving all along, the expansion, the scale factor — carries <em>no entropy whatsoever</em>.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>Following the history — full at the start, then empty</h2>

<div class="calc">
<span class="tag">How the ratio moves in time</span>
<p class="lbl">Entropy density \(s\propto a^{-3}\), bound \(\propto H\propto1/t\)</p>
$$\frac{s}{3H/4\ell_P^2}\ \propto\ t^{\,1-3p}$$
<p class="lbl">\(t^{-1/2}\) in radiation (\(p=1/2\)), \(t^{-1}\) in matter (\(p=2/3\)); stacking from the Planck era</p>
$$\underbrace{1.84\times10^{-28}}_{\text{Planck}\to\text{equality}}\times\underbrace{3.68\times10^{-6}}_{\text{equality}\to\text{today}}=6.7\times10^{-34}$$
</div>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>Planck era: occupancy ≈ 1</strong><span>the memory was full. Matter was in thermal equilibrium and everything writable was written</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>Today, matter and radiation only: ≈ \(7\times10^{-34}\)</strong><span>capacity grew as \(t^2\) and the contents could not keep up. <em>It emptied out</em></span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>Today, including black holes: \(1.5\times10^{-18}\)</strong><span>gravity has <strong>refilled 15.4 orders of magnitude</strong></span></div></div>
</div>

<p>Entropy itself really has grown — from \(2\times10^{88}\) around recombination to \(3.1\times10^{104}\) today, <strong>16.2 orders</strong>. But <em>almost all of that increase is on the gravitational side</em>.</p>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0">The universe began <strong>thermally full and gravitationally empty</strong>.<br>
Expansion widened the capacity and the thermal occupancy kept falling.<br>
And <strong>only black holes are filling it back in</strong> — that is what the arrow of time is.</p>
</div>

<div class="fig">
<p class="cap">Figure: age of the universe (in orders of magnitude above the Planck time) across, memory occupancy up. Blue-grey is <strong>the thermal side</strong> (falling from full), old-gold is <strong>the gravitational side</strong> (refilling once structure forms). The slider picks an epoch and reports the breakdown.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Age of the universe \(\log_{10}(t/t_P)\) (right edge = today)<input id="st" type="range" min="0" max="609" value="609" step="1"></label>
  <span class="val" id="vt">today</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#4a6478"></i>thermal side (matter and radiation)</span>
  <span><i class="swatch" style="background:#8a6a2f"></i>gravitational side (black holes; schematic)</span>
  <span><i class="swatch" style="background:#9c9890"></i>capacity full (occupancy 1)</span>
</div>
</div>

<p>The blue-grey line touches the ceiling at the far left (the Planck era) and falls from there without stopping. <strong>The thermal history of the universe is a history of memory emptying out.</strong> The old-gold line rises only near the right edge and overtakes the blue-grey by 16 orders — <em>the universe only started remembering anything very recently</em>.</p>

<h2><span class="n">05</span>The reveal — the tool works because that side is empty</h2>

<p>Here is the point of the episode: why does the conformal transformation work so well on the universe?</p>

<p>An FLRW universe is <strong>exactly conformally flat</strong> — its Weyl tensor vanishes identically. That is what let Episode 3 of the previous series transform a \(c\cdot t=\text{const}\) universe into Minkowski. But the Weyl tensor <em>is</em> gravitational entropy, so <strong>\(C=0\) means "the gravitational memory is empty"</strong>.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">Conformal-factor side</th><th class="mid">Weyl-tensor side</th></tr></thead>
<tbody>
<tr><th>Under a conformal transformation</th><td class="mid">moves (this is the gauge)</td><td class="mid"><strong>does not move</strong> (\(C\) is conformally invariant)</td></tr>
<tr><th>Entropy</th><td class="mid">none</td><td class="mid">yes (= gravitational entropy)</td></tr>
<tr><th>In use today</th><td class="mid">\(0\)</td><td class="mid">\(3.1\times10^{104}\) (essentially all of it)</td></tr>
<tr class="hi"><th>This series' tool</th><td class="mid"><strong>moves only this</strong></td><td class="mid">cannot touch it</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0">A conformal transformation can only move <strong>the unused side</strong> of the universe's memory.<br>
The occupancy \(1.5\times10^{-18}\) is, directly, <em>a measurement of this tool's range</em>.</p>
</div>

<p>So when Episode 4 deleted everything deletable and was left with one mass, <strong>everything that vanished lay on the empty side</strong> — expansion, curvature, temperature. Conversely, everything that could <em>not</em> be deleted — the conformal factor problem of Episode 9 of the previous series, the \(N=mc^2t/\hbar\) of Episode 6, black hole entropy — sits on the side that does not move.</p>

<div class="aside">
<span class="tag">How badly the tool is breaking is the arrow of time</span>
Penrose's <strong>Weyl curvature hypothesis</strong> says the universe began with \(C=0\). And \(C=0\) is exactly the condition that let Episode 3 of the previous series transform to Minkowski — <em>conformal flatness</em>. So <strong>this series' tool worked perfectly at the beginning of the universe and stops working in proportion to the gravitational entropy that has since accumulated</strong>. Today's \(1.5\times10^{-18}\) is also a number for <em>how broken the tool now is</em>. <strong>The degree of breakage is the arrow of time.</strong> What Extra 2 of the previous series wrote as structure has finally been given a scale.
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① The usage figure is the census of Egan &amp; Lineweaver (2010)</strong> (\(S_{\rm obs}=3.1\times10^{104}k_B\), dominated by supermassive black holes). It depends strongly on the SMBH mass function, and the authors themselves acknowledge order-of-magnitude uncertainty.</p>
<p style="margin:0 0 10px"><strong>② "Capacity" means \(A/4\ell_P^2\) on the horizon</strong>, not what can actually be stored. The holographic bound is an inequality saying "no more than this fits", not a guarantee that this much is usable. <em>Free space does not mean usable space.</em></p>
<p style="margin:0 0 10px"><strong>③ "Conformally flat" means the Weyl tensor vanishes</strong>, not that curvature vanishes. FLRW has \(C=0\) but \(R\ne0\) (Episode 6 of the previous series).</p>
<p style="margin:0 0 10px"><strong>④ The Weyl curvature hypothesis is a proposal, not a theorem.</strong> It is Penrose's conjecture and is neither proved nor disproved.</p>
<p style="margin:0"><strong>⑤ Gravitational entropy has no established definition</strong> — there is still no standard prescription for how to count \(C\). What the text calls "entropy on the Weyl side" is in fact the sum of black hole entropies, not a quantity computed from \(C\). In addition, the history in §04 assumes <em>comoving conservation of entropy</em> (no reheating production), and the gold curve in the figure is <em>schematic</em> — Egan &amp; Lineweaver give only today's value.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Why does "memory occupancy" reduce to a ratio of areas?
<details><summary>Show the answer</summary><div class="ans">Because a black hole and the cosmic horizon carry entropy by the same formula \(S=k_BA/4\ell_P^2\). Dividing cancels \(4\ell_P^2\) and leaves \(\sum A_{\rm BH}/A_H\). <strong>Even the Planck length disappears</strong> — occupancy is a pure geometric ratio.</div></details></li>

<li>Glue every black hole horizon into one sphere: what radius, in light years?
<details><summary>Show the answer</summary><div class="ans">\(\sum A_{\rm BH}=1.51\times10^{-18}\times2.14\times10^{53}=3.24\times10^{35}\ \mathrm{m^2}\), so \(r=\sqrt{A/4\pi}=1.61\times10^{17}\) m = <strong>17 light years</strong>. Nearly all of the universe's information is written on a surface 34 light years across.</div></details></li>

<li>Why does occupancy fall with time even though entropy is rising?
<details><summary>Show the answer</summary><div class="ans"><strong>Because the denominator rises faster.</strong> Capacity grows as \(A_H\propto R_H^2\propto t^2\), while thermal entropy is comoving-conserved (roughly constant). So the ratio falls. <em>Rising entropy and falling occupancy are perfectly compatible</em> — the second law is about the numerator, expansion is about the denominator.</div></details></li>

<li>Which side of the memory can a conformal transformation move?
<details><summary>Show the answer</summary><div class="ans">The conformal-factor side — i.e. <strong>the unused side only</strong>. The Weyl tensor is conformally invariant and cannot be touched. Since today's \(3.1\times10^{104}\) is essentially all on the Weyl side, <strong>this series' tool cannot reach the memory that is actually in use.</strong></div></details></li>

<li>(Harder) What does "how badly the tool is breaking is the arrow of time" mean?
<details><summary>Show the answer</summary><div class="ans">The conformal transformation works perfectly when \(C=0\) (conformal flatness), and by the Weyl curvature hypothesis the universe started there. Growing gravitational entropy = growing \(C\) = <strong>a growing component that cannot be rewritten conformally</strong>. So "the direction in which the tool's range narrows" is itself the direction of time, and \(1.5\times10^{-18}\) is the current reading. <em>Note, per caveat ⑤, that gravitational entropy has no settled definition, so this correspondence is not a rigorous theorem.</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — being empty is why the tool works</h2>
<p>The universe's memory: capacity \(2.96\times10^{122}\) bits, usage \(3.1\times10^{104}\), occupancy <strong>\(1.51\times10^{-18}\)</strong> — essentially empty. And because black holes and horizons obey the same \(S=k_BA/4\ell_P^2\), that occupancy reduces to a bare area ratio \(\sum A_{\rm BH}/A_H\) — glue every black hole horizon together and you get <strong>a sphere of radius 17 light years</strong>, carrying nearly all the information in the universe.</p>
<p>Counting which side that "nearly all" is on gives <strong>99.999999999999986% gravitational (Weyl)</strong>. The table from Extra 2 of the previous series — the gravitational field splitting into conformal factor and Weyl tensor — now has numbers in it. The conformal-factor side, the \(\phi\) this series keeps moving, carries no entropy at all.</p>
<p>The history came in three stages: <strong>occupancy ≈ 1 in the Planck era</strong> (full); \(7\times10^{-34}\) today counting only matter and radiation (<em>emptied out</em>); \(1.5\times10^{-18}\) once black holes are included (<em>gravity refilled 15.4 orders</em>). Entropy itself rose 16.2 orders, almost all of it gravitational. The universe began <strong>thermally full and gravitationally empty</strong>.</p>
<p>And the reveal: <strong>a conformal transformation can only move the unused side of the memory</strong>. The Weyl tensor is invariant and untouchable. So everything Episode 4 could delete lay on the empty side, and everything it could not (the conformal factor problem, \(N=mc^2t/\hbar\), black hole entropy) lay on the used side. If the universe began at \(C=0\) as Penrose's hypothesis says, then <em>this tool worked perfectly at the beginning and fails in proportion to the gravitational entropy since accumulated</em>. <strong>The breakage of the tool is the arrow of time.</strong></p>
</div>

<div class="next">
<span class="lbl">Next — Episode 7</span>
The memory turned out to be nearly empty, with everything written on black holes. Next we look at <strong>communication</strong>. The CMB is uniform to \(\Delta T/T\sim10^{-5}\) across \(10^4\) causally disconnected patches. In the language of information: <em>\(10^4\) nodes that have exchanged not one message agree to 17 bits</em>. In distributed systems this is held to be impossible. \(c\cdot t=\text{const}\) is the only expansion law that never adds nodes, so in principle it does not have this problem — <strong>or it would not have, until you put the radiation back in.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var st=document.getElementById('st'), vt=document.getElementById('vt'), ro=document.getElementById('ro');
  var X0=74, X1=700, Y0=30, Y1=318;
  var xmin=0, xmax=62;
  var ymin=-36, ymax=1.5;
  var X_EQ=55.47, X_NOW=60.91, X_STR=59.2;
  var Y_NOW_G=Math.log(1.51e-18)/Math.LN10;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function thermal(x){
    if(x<=X_EQ) return -0.5*x;
    return -0.5*X_EQ - 1.0*(x-X_EQ);
  }
  function grav(x){
    if(x<=X_STR) return null;
    var f=(x-X_STR)/(X_NOW-X_STR);
    return ymin + (Y_NOW_G-ymin)*Math.pow(f,0.42);
  }

  function draw(){
    var xc=parseInt(st.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=0;e>=-35;e-=5){
      var y=py(e);
      g.strokeStyle='#f0eeea'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#9c9890'; g.fillText(e===0?'1':'10⁻'+Math.abs(e), X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=60;q+=10){
      var x=px(q);
      g.strokeStyle='#f6f4f1'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#9c9890'; g.fillText('10'+q, x, Y1+16);
    }
    g.strokeStyle='#cfccc5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    g.strokeStyle='#9c9890'; g.lineWidth=1.8; g.setLineDash([6,5]);
    g.beginPath(); g.moveTo(X0,py(0)); g.lineTo(X1,py(0)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#8a8680'; g.textAlign='left';
    g.fillText('capacity full', X0+8, py(0)-7);

    g.strokeStyle='#4a6478'; g.lineWidth=3.2; g.beginPath();
    for(var i=0;i<=400;i++){
      var x=xmin+(X_NOW-xmin)*i/400, y=thermal(x);
      if(y<ymin) break;
      if(i===0) g.moveTo(px(x),py(y)); else g.lineTo(px(x),py(y));
    }
    g.stroke();
    g.strokeStyle='#8a6a2f'; g.lineWidth=3.2; g.setLineDash([6,4]); g.beginPath();
    var started=false;
    for(var i=0;i<=200;i++){
      var x=X_STR+(X_NOW-X_STR)*i/200, y=grav(x);
      if(y===null||y<ymin) continue;
      if(!started){ g.moveTo(px(x),py(y)); started=true; } else g.lineTo(px(x),py(y));
    }
    g.stroke(); g.setLineDash([]);

    g.fillStyle='#8a6a2f';
    g.beginPath(); g.arc(px(X_NOW),py(Y_NOW_G),5.5,0,6.2832); g.fill();
    g.strokeStyle='#fff'; g.lineWidth=1.8;
    g.beginPath(); g.arc(px(X_NOW),py(Y_NOW_G),5.5,0,6.2832); g.stroke();
    g.fillStyle='#8a6a2f'; g.textAlign='right';
    g.fillText('today  1.5×10⁻¹⁸', px(X_NOW)-10, py(Y_NOW_G)-9);

    g.strokeStyle='#ddd9d2'; g.lineWidth=1; g.setLineDash([3,4]);
    g.beginPath(); g.moveTo(px(X_EQ),Y0); g.lineTo(px(X_EQ),Y1); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#a8a49c'; g.textAlign='center';
    g.fillText('matter–radiation equality', px(X_EQ), Y0-8);

    g.strokeStyle='#33353d'; g.lineWidth=1.6;
    g.beginPath(); g.moveTo(px(xc),Y0); g.lineTo(px(xc),Y1); g.stroke();

    g.fillStyle='#6d6a63'; g.textAlign='center';
    g.fillText('age of the universe  t / t_P', (X0+X1)/2, Y1+36);

    var th=thermal(xc), gr=grav(xc);
    var thv=Math.pow(10,th);
    var grv=(gr===null?0:Math.pow(10,gr));
    var tot=thv+grv;
    var tsec=Math.pow(10,xc)*5.391e-44;
    var tlabel = tsec<3.156e7 ? tsec.toExponential(2)+' s' : (tsec/3.156e7).toExponential(2)+' yr';
    vt.textContent = (xc>=X_NOW-0.05 ? 'today' : 'log₁₀(t/t_P) = '+xc.toFixed(1));
    ro.textContent =
      'age '+tlabel+' (log₁₀ t/t_P = '+xc.toFixed(1)+')　/　'+
      'thermal side '+thv.toExponential(1)+'　'+
      'gravitational side '+(gr===null?'0 (no objects yet)':grv.toExponential(1))+'　'+
      'total '+tot.toExponential(1)+
      '　→　free '+(100*(1-tot)).toFixed(12)+' %';
  }
  st.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-06-empty.html', acc='#33454f', ops='#8a6a2f',
      title='Only 10⁻¹⁸ of the memory is in use ── c·t = const, That Clicks, Episode 6',
      ep='EPISODE 6 ／ Three episodes of dividing — now open the contents',
      eyebrow='Being empty turned out to be why this tool works',
      h1='Only \\(10^{-18}\\) of the<br>memory is in use',
      sub='A machine that performs one operation per 28.5 bits holds that memory almost entirely empty.<br><em>Count the emptiness and out falls the reason this series exists at all.</em>',
      byline_l='What you need: division, area, logarithms',
      byline_r='occupancy \\(=\\sum A_{\\rm BH}/A_H=1.5\\times10^{-18}\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 6 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The horizon entropy \\(S=k_BA/4\\ell_P^2\\), the identical form of the Bekenstein–Hawking entropy of a black hole, and the fact that FLRW spacetimes are conformally flat with vanishing Weyl tensor are all standard. The entropy budget of the observable universe — \\(S_{\\rm obs}=3.1\\times10^{104}k_B\\) (dominated by supermassive black holes), CMB photons \\(2.03\\times10^{88}k_B\\), neutrinos \\(1.93\\times10^{88}k_B\\) — is from Egan &amp; Lineweaver (2010, ApJ 710, 1825). <strong>These values depend on the supermassive black hole mass function, and the authors themselves state an order-of-magnitude uncertainty.</strong> The occupancy \\(1.51\\times10^{-18}\\), its reduction to the area ratio \\(\\sum A_{\\rm BH}/A_H\\), the equivalent radius of 17 light years, the gravitational share 99.999999999999986%, and the three-stage history (Planck era \\(O(1)\\), today\'s thermal side \\(7\\times10^{-34}\\)) are all computed here. The history in §04 rests on \\(s\\le3H/4\\ell_P^2\\) from Extra 3 of the previous series (Bousso\'s 1999 covariant entropy bound applied to the apparent horizon) and assumes <em>comoving conservation of entropy</em>; the "\\(O(1)\\) at the Planck era" comes from the same one-loop estimate. The gravitational curve in the figure is <em>schematic</em> — Egan &amp; Lineweaver give only today\'s value. The Weyl curvature hypothesis is Penrose\'s <em>proposal</em>, not a theorem, and gravitational entropy has no established definition — what the text calls "entropy on the Weyl side" is the sum of black hole entropies, not a quantity computed from \\(C\\). The holographic bound is an inequality on what fits, not a guarantee of storable capacity. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider picks an epoch and reports the breakdown. "Show the answer" opens each solution.')
