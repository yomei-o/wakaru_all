# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 17 was communication. Today: <strong>addressing</strong>. The universe has \((R_H/\ell_P)^3=5.27\times10^{182}\) spatial cells but can write only \(2.96\times10^{122}\) bits. <em>Far from one bit per cell, there is \(10^{-61}\) of one.</em> Read holography not as "written on the area" but as <strong>"there are not enough addresses"</strong>, and a curiously specific length falls out along the way — <em>the volume one bit is responsible for has a side about the size of a proton</em>.</p>

<h2><span class="n">01</span>Counting three numbers</h2>

<div class="calc">
<span class="tag">Just counting</span>
<p class="lbl">today's universe in Planck lengths</p>
$$\frac{R_H}{\ell_P}=8.075\times10^{60}$$
<p class="lbl">spatial cells (Planck volumes)</p>
$$\left(\frac{R_H}{\ell_P}\right)^3=5.27\times10^{182}$$
<p class="lbl">four-volume cells (Planck spacetime points)</p>
$$\left(\frac{ct_0}{\ell_P}\right)^4=4.25\times10^{243}$$
<p class="lbl">bits writable (Episode 1)</p>
$$N=\frac{\pi}{\ln2}\left(\frac{R_H}{\ell_P}\right)^2=2.96\times10^{122}$$
</div>

<p>The exponents are \(3\), \(4\) and \(2\). <strong>Only the bits go as a square</strong> — that is the whole of holography.</p>

<h2><span class="n">02</span>The ratio is a clean identity</h2>

<div class="calc">
<span class="tag">Divide</span>
$$\frac{N}{(R_H/\ell_P)^3}=\frac{\pi/\ln2}{R_H/\ell_P}=\frac{4.5324}{8.075\times10^{60}}=5.61\times10^{-61}$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
$$\boxed{\ \frac{\text{bits writable}}{\text{spatial cells}}=\frac{\pi/\ln2}{R_H/\ell_P}\ }$$
<p style="margin:10px 0 0"><strong>Holography means "only \(10^{-61}\) of the spatial cells can be given an address".</strong><br>
And since the ratio goes as \(1/R_H\), <em>the shortage worsens as the universe grows</em>.</p>
</div>

<p>Conversely, it was better in the past. Solving \(N=(R_H/\ell_P)^3\) gives \(R_H/\ell_P=\pi/\ln2=4.53\). <strong>Addresses sufficed only while the universe was smaller than 4.5 Planck lengths.</strong></p>

<h2><span class="n">03</span>The heart — the volume one bit is responsible for</h2>

<div class="calc">
<span class="tag">Just invert the ratio</span>
$$\frac{(R_H/\ell_P)^3}{N}=\frac{\ln2}{\pi}\cdot\frac{R_H}{\ell_P}=1.78\times10^{60}\ \text{Planck volumes}$$
<p class="lbl">as a volume</p>
$$7.52\times10^{-45}\ \mathrm{m^3}\qquad\Longrightarrow\qquad \text{side}\ \ell_{\rm bit}=1.96\times10^{-15}\ \mathrm{m}$$
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0">The volume one bit is responsible for is a cube of side <strong>1.96 femtometres</strong>.<br>
── <em>The size of a proton</em> (charge radius 0.84 fm, diameter 1.68 fm).</p>
</div>

<p>Distribute the universe's holographic memory across space and <strong>one bit corresponds to exactly one nucleon's worth of volume</strong>. This does not mean "one proton is one bit", of course — <em>the numbers simply happen to agree</em>. Still, the coincidence stops you in your tracks.</p>

<h2><span class="n">04</span>What scale is this?</h2>

<div class="calc">
<span class="tag">An intermediate scale</span>
$$\ell_{\rm bit}=\left(\frac{\ln2}{\pi}\right)^{1/3}\left(R_H\,\ell_P^2\right)^{1/3}$$
<p class="lbl">the bare value without the coefficient</p>
$$\left(R_H\,\ell_P^2\right)^{1/3}=3.24\ \mathrm{fm}\qquad(\times\,0.604\ \text{gives }1.96\ \mathrm{fm})$$
</div>

<p>So it is <strong>the "cube-root intermediate scale" between the horizon radius and the Planck length</strong>. Blend the largest and smallest lengths in the universe with these weights and out comes the size of a nucleon — <em>an unexplained numerical coincidence</em>, of the same kind as Extra 5's "\(\rho_\Lambda^{1/4}\) and the neutrino mass differ by only a factor 22".</p>

<div class="aside">
<span class="tag">How to handle coincidences like this</span>
This series has always used the same procedure on numerical coincidences — <strong>identity, coincidence or physics</strong>. Dirac's large numbers (Episode 7) were an <em>identity</em>. Being exactly at the Landauer limit (Episode 10) was an <em>identity</em>. Today's 1.96 fm is not an identity (give \(R_H\) and \(\ell_P\) independently and it takes any value), and no physical mechanism is known. <strong>For now it can only go in the "coincidence" column</strong> — and saying so explicitly is this series' practice.
</div>

<div class="fig">
<p class="cap">Figure: how the three numbers grow as the universe grows. <strong>Cells go as slope 3, four-volumes as slope 4, bits as slope 2.</strong> Only the bits are slow, so the address shortage widens with size — <em>they sufficed only while the universe was under 4.5 Planck lengths</em>.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Size of the universe \(\log_{10}(R_H/\ell_P)\) (right edge = today)<input id="sr" type="range" min="0" max="609" value="609" step="1"></label>
  <span class="val" id="vr">today</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#4a3a1f"></i>spatial cells (slope 3)</span>
  <span><i class="swatch" style="background:#8a7a4a"></i>four-volume cells (slope 4)</span>
  <span><i class="swatch" style="background:#2a6b5a"></i>bits writable (slope 2)</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">05</span>The address table itself will not fit in memory</h2>

<div class="calc">
<span class="tag">Address width</span>
$$\log_2\left(5.27\times10^{182}\right)=607\ \text{bits}$$
<p class="lbl">addressing every cell</p>
$$5.27\times10^{182}\times607=3.20\times10^{185}\ \text{bits}$$
<p class="lbl">against the memory</p>
$$\frac{3.20\times10^{185}}{2.96\times10^{122}}=1.1\times10^{63}\ \text{times}$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>Merely addressing every cell would take \(10^{63}\) times the memory.</strong><br>
── <em>The address table will not fit in memory.</em> The address space exceeds anything the universe can handle.</p>
</div>

<p>This is <strong>a different shortage</strong> from Episode 6's occupancy of \(10^{-18}\). That was "the capacity is there and unused". This is "<em>there are not enough addresses in the first place</em>" — a problem prior to use.</p>

<h2><span class="n">06</span>The time direction is a further 61 orders short</h2>

<div class="calc">
<span class="tag">Counting in four-volumes</span>
$$\frac{N}{(ct_0/\ell_P)^4}=\frac{2.96\times10^{122}}{4.25\times10^{243}}=7.0\times10^{-122}$$
</div>

<p>Space alone gives \(10^{-61}\); include time and it is \(10^{-122}\) — exactly twice the orders (as it must be, \(N\propto R^2\) against \(R^4\)). The meaning is clear: <strong>"recording the entire history of the universe" is impossible in principle</strong>.</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>Write down everything happening now</strong><span>only \(10^{-61}\) of the spatial cells have addresses → <em>impossible</em></span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>Write down everything that has happened</strong><span>\(10^{-122}\) of the four-volume cells → <em>a further 61 orders impossible</em></span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>The bound is what fits on the horizon</strong><span>and that grows only as \(R^2\) — <em>which is the entire content of holography</em></span></div></div>
</div>

<h2><span class="n">07</span>The reveal — this is not compression</h2>

<p>Holography is sometimes described as "the information of a volume compressed onto an area". <strong>Read in the language of addresses, that phrasing misleads.</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th>If it were compression</th><th class="mid">Actual holography</th></tr></thead>
<tbody>
<tr><th>Original information</th><td>a volume's worth</td><td class="mid"><strong>only ever an area's worth</strong></td></tr>
<tr><th>Operation</th><td>squeeze out redundancy</td><td class="mid">nothing is squeezed</td></tr>
<tr><th>Recovery</th><td>you can restore it</td><td class="mid">there is no "original" to restore</td></tr>
<tr class="hi"><th>The right phrasing</th><td>──</td><td class="mid"><strong>volume cells were never given addresses</strong></td></tr>
</tbody>
</table>
</div>

<p>Episode 13 drew the line "a conformal transformation touches only size". Today's line is more basic — <em>the universe as a storage device has its addresses set by area, not volume</em>. So of \(10^{182}\) cells only \(10^{122}\) can be designated, and the gap widens as the universe grows.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① Counting "spatial cells" as \((R_H/\ell_P)^3\) is not a claim that spacetime is a discrete lattice.</strong> It is <em>an indicative count</em> in units of the Planck volume — the same metaphorical use as "cells / ticks" in Extra 3 of the previous series.</p>
<p style="margin:0 0 10px"><strong>② The holographic bound is an inequality on what fits</strong>, not a guarantee of usable capacity (same caveat as Episode 6 ②). So "not enough addresses" is <em>a statement about the bound</em>, not a report of a failed attempt to record something.</p>
<p style="margin:0 0 10px"><strong>③ There is no known explanation for \(\ell_{\rm bit}=1.96\) fm.</strong> It is not an identity (give \(R_H\) and \(\ell_P\) independently and it takes any value) and no mechanism is known. <em>It belongs in the "coincidence" column.</em> The observation that \((R_H\ell_P^2)^{1/3}\) lands on the nucleon scale is of a kind found in the literature and is not a discovery of this document.</p>
<p style="margin:0 0 10px"><strong>④ The address-width argument of §05 assumes a naive encoding.</strong> In practice cells need no individual addresses (the coordinates are the address), and "building an address table" is not physically required — <em>read it as a way of feeling the size of the address space</em>.</p>
<p style="margin:0"><strong>⑤ \(R_H=ct_0\) is the \(c\cdot t=\text{const}\) convention.</strong> In \(\Lambda\)CDM, \(R_H=c/H_0\) differs from the particle horizon and the numbers shift by factors of a few — read this as an order-of-magnitude argument.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Express the ratio of bits to spatial cells in terms of \(R_H/\ell_P\).
<details><summary>Show the answer</summary><div class="ans">\(N/(R_H/\ell_P)^3=[\pi(R_H/\ell_P)^2/\ln2]/(R_H/\ell_P)^3=(\pi/\ln2)/(R_H/\ell_P)\). <strong>Proportional to \(1/R_H\)</strong>, so the shortage worsens as the universe grows.</div></details></li>

<li>When were there enough addresses?
<details><summary>Show the answer</summary><div class="ans">Solve \(N=(R_H/\ell_P)^3\): \(R_H/\ell_P=\pi/\ln2=4.53\). <strong>Only while the universe was smaller than 4.5 Planck lengths</strong>; never since.</div></details></li>

<li>Find the side of the volume one bit is responsible for.
<details><summary>Show the answer</summary><div class="ans">\((R_H/\ell_P)^3/N=(\ln2/\pi)(R_H/\ell_P)=1.78\times10^{60}\) Planck volumes \(=7.52\times10^{-45}\ \mathrm{m^3}\). The cube root is <strong>1.96 fm</strong> — <em>the size of a proton</em>.</div></details></li>

<li>What kind of scale is that?
<details><summary>Show the answer</summary><div class="ans">\(\ell_{\rm bit}\propto(R_H\ell_P^2)^{1/3}\), <strong>the cube-root intermediate scale between horizon radius and Planck length</strong>. Bare value 3.24 fm, times the coefficient \((\ln2/\pi)^{1/3}=0.604\) gives 1.96 fm. <em>An unexplained numerical coincidence</em> — neither an identity nor physics.</div></details></li>

<li>(Harder) Why is calling holography "compression" misleading?
<details><summary>Show the answer</summary><div class="ans">Compression would mean squeezing a volume's worth of information by removing redundancy, but in fact <strong>only an area's worth ever exists</strong>. Nothing is squeezed and there is no "original" to restore. The right phrasing is <em>"volume cells were never given addresses"</em> — a statement about <strong>the structure of the address space</strong>, not the amount of information.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — addresses grow only with area</h2>
<p>Three numbers: spatial cells \((R_H/\ell_P)^3=5.27\times10^{182}\), four-volume cells \(4.25\times10^{243}\), bits writable \(2.96\times10^{122}\). Exponents \(3\), \(4\), \(2\) — <strong>only the bits go as a square</strong>, which is the entire content of holography.</p>
<p>The ratio came out a clean identity: \(N/(R_H/\ell_P)^3=(\pi/\ln2)/(R_H/\ell_P)=5.61\times10^{-61}\). <strong>"Only \(10^{-61}\) of the spatial cells can be addressed"</strong>, and since it goes as \(1/R_H\), <em>the gap widens as the universe grows</em>. Addresses sufficed only while the universe was under 4.5 Planck lengths.</p>
<p>Inverted, it gives the volume per bit — \(1.78\times10^{60}\) Planck volumes, side <strong>1.96 femtometres</strong>. <em>The size of a proton.</em> It is \((R_H\ell_P^2)^{1/3}\), the cube-root intermediate between the largest and smallest lengths in the universe — neither identity nor physics, and for now <strong>a coincidence and nothing more</strong>.</p>
<p>Beyond that, the address table itself will not fit in memory (addressing every cell takes \(10^{63}\) times it). Counting time as well widens the shortage to \(10^{-122}\), so <strong>"recording the entire history of the universe" is impossible in principle</strong>. And finally a matter of words — holography is <em>not compression</em>. Nothing is squeezed and there is no original. Properly: <strong>"volume cells were never given addresses"</strong>. Where Episode 6's \(10^{-18}\) was "there and unused", this was <em>a shortage prior to use</em>.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 19</span>
We return to the homework Episode 10 left unfinished — <strong>"the universe runs exactly at the Landauer limit"</strong>. That ratio of 1.000000 was the identity \(E=T_HS\). So: <em>once a number is known to be an identity, is there anything left to say about it?</em> Dirac's large numbers (Episode 7), \(\alpha+2\beta+\gamma=2\) (Episode 14), today's 1.96 fm — this series has sorted identities, coincidences and physics again and again. Next time we build <strong>the sorting procedure itself</strong>, head on. <em>Is an identity really "not physics"?</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sr=document.getElementById('sr'), vr=document.getElementById('vr'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=316;
  var ln2=Math.log(2), PI=Math.PI;
  var xmin=0, xmax=62, ymin=0, ymax=250;
  var CROSS=Math.log(PI/ln2)/Math.LN10;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function line(sl,off,col,w){
    g.strokeStyle=col; g.lineWidth=w; g.beginPath();
    var first=true;
    for(var i=0;i<=200;i++){
      var x=xmin+(xmax-xmin)*i/200, y=off+sl*x;
      if(y<ymin||y>ymax){ first=true; continue; }
      if(first){ g.moveTo(px(x),py(y)); first=false; } else g.lineTo(px(x),py(y));
    }
    g.stroke();
  }

  function draw(){
    var lr=parseInt(sr.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=0;e<=250;e+=50){
      var y=py(e);
      g.strokeStyle='#f2efe6'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#a49a86'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=60;q+=10){
      var x=px(q);
      g.strokeStyle='#f8f6f1'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a49a86'; g.fillText('10'+q, x, Y1+16);
    }
    g.strokeStyle='#cdc6b5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    line(4,0,'#8a7a4a',2.6);
    line(3,0,'#4a3a1f',3.2);
    line(2,Math.log(PI/ln2)/Math.LN10,'#2a6b5a',3.4);

    if(CROSS>xmin&&CROSS<xmax){
      var yc=3*CROSS;
      g.fillStyle='#2a6b5a';
      g.beginPath(); g.arc(px(CROSS),py(yc),5,0,6.2832); g.fill();
      g.fillStyle='#2a6b5a'; g.textAlign='left';
      g.fillText('addresses sufficed up to here (R/ℓ_P = 4.5)', px(CROSS)+10, py(yc)+18);
    }

    g.strokeStyle='#7a6a48'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(lr),Y0); g.lineTo(px(lr),Y1); g.stroke();
    g.setLineDash([]);

    g.textAlign='left';
    g.fillStyle='#8a7a4a'; g.fillText('four-volume cells (slope 4)', px(34), py(4*34)-8);
    g.fillStyle='#4a3a1f'; g.fillText('spatial cells (slope 3)', px(48), py(3*48)-8);
    g.fillStyle='#2a6b5a'; g.fillText('bits writable (slope 2)', px(50), py(2*50)+18);

    g.fillStyle='#8a8272'; g.textAlign='center';
    g.fillText('size of the universe  R_H / ℓ_P', (X0+X1)/2, Y1+36);

    var R=Math.pow(10,lr);
    var cells=Math.pow(R,3), bits=(PI/ln2)*R*R, v4=Math.pow(R,4);
    vr.textContent = (lr>60.5?'today':'10^'+lr.toFixed(1));
    ro.textContent='R_H/ℓ_P = '+R.toExponential(2)+
      '　cells '+cells.toExponential(2)+
      '　bits '+bits.toExponential(2)+
      '　→　ratio '+(bits/cells).toExponential(2)+
      '　/　'+(cells/bits).toExponential(2)+' Planck volumes per bit'+
      (bits>cells?'　★ addresses suffice':'');
  }
  sr.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-18-address.html', acc='#4a3a1f', ops='#2a6b5a',
      title='There are not enough address lines ── c·t = const, That Clicks, Episode 18',
      ep='EPISODE 18 ／ Holography read in the language of addressing',
      eyebrow='The volume one bit is responsible for has a side about the size of a proton',
      h1='There are not enough<br>address lines',
      sub='\\(5.27\\times10^{182}\\) spatial cells, \\(2.96\\times10^{122}\\) bits writable.<br><em>Only \\(10^{-61}\\) of the cells can be addressed — and the gap keeps widening.</em>',
      byline_l='What you need: division, a cube root',
      byline_r='\\(\\ell_{\\rm bit}=1.96\\ \\mathrm{fm}\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 18 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The holographic bound \\(N=A/(4\\ell_P^2\\ln2)\\) is standard. The values \\((R_H/\\ell_P)^3=5.27\\times10^{182}\\), \\((ct_0/\\ell_P)^4=4.25\\times10^{243}\\), \\(N/(R_H/\\ell_P)^3=(\\pi/\\ln2)/(R_H/\\ell_P)=5.61\\times10^{-61}\\), \\(1.78\\times10^{60}\\) Planck volumes per bit (side \\(1.96\\) fm), the 607-bit address width and the factor \\(10^{63}\\) for an address table, \\(N/(ct_0/\\ell_P)^4=7.0\\times10^{-122}\\), and "addresses sufficed only for \\(R_H/\\ell_P<\\pi/\\ln2=4.53\\)" are all computed here (kenshou/calc22.py). <strong>Counting "spatial cells" in Planck volumes is indicative and not a claim that spacetime is a discrete lattice</strong> (the same metaphorical use as "cells / ticks" in Extra 3 of the previous series). The holographic bound is an inequality on what fits, not a guarantee of usable capacity, so "not enough addresses" is a statement about the bound. <strong>There is no known explanation for \\(\\ell_{\\rm bit}\\simeq1.96\\) fm landing on the nucleon scale; it is neither an identity nor a mechanism</strong> — the observation that \\((R_H\\ell_P^2)^{1/3}\\) lands there is of a kind found in the literature and is not a discovery of this document. The address-width argument in §05 assumes a naive encoding; in practice coordinates are the address and no table is physically required. \\(R_H=ct_0\\) is the \\(c\\cdot t=\\)const convention; in \\(\\Lambda\\)CDM \\(R_H=c/H_0\\) differs from the particle horizon and the numbers shift by factors of a few. Linear expansion is a minority model under examination and conflicts with nucleosynthesis when extrapolated into the early universe (Lewis, Barnes &amp; Kaushik 2016). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the size of the universe and only the bits line falls behind. "Show the answer" opens each solution.')
