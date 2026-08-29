# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">We now have <strong>four scales</strong> for the direction of time — total entropy (Episode 6), memory occupancy (Episode 6), holographic margin (Episode 20), and the degrees of freedom \(a\) (Episode 2). Oddly, <em>two of them increase and two decrease</em>. They measure the same arrow, and point opposite ways. <strong>Today we set the four side by side and locate where the arrow of time actually lives.</strong></p>

<h2><span class="n">01</span>The four scales</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Scale</th><th class="mid">Change</th><th class="mid">Orders</th><th class="mid">Direction</th><th class="mid">From</th></tr></thead>
<tbody>
<tr><th>① Total entropy \(S/k_B\)</th><td class="mid">\(\sim1\to3.1\times10^{104}\)</td><td class="mid">\(+104\)</td><td class="mid"><strong>up</strong></td><td class="mid">Episode 6</td></tr>
<tr><th>② Memory occupancy \(S/S_{\max}\)</th><td class="mid">\(1\to1.5\times10^{-18}\)</td><td class="mid">\(-18\)</td><td class="mid"><strong>down</strong></td><td class="mid">Episode 6</td></tr>
<tr><th>③ Holographic margin</th><td class="mid">0 orders \(\to\) 33 orders</td><td class="mid">\(+33\)</td><td class="mid"><strong>up</strong></td><td class="mid">Episode 20</td></tr>
<tr><th>④ Degrees of freedom \(a\) (a-theorem)</th><td class="mid">\(995.5\to62.0\)</td><td class="mid">\(-1.2\)</td><td class="mid"><strong>down</strong></td><td class="mid">Episode 2</td></tr>
</tbody>
</table>
</div>

<p>① and ③ up, ② and ④ down. <strong>It looks contradictory.</strong> But —</p>

<h2><span class="n">02</span>All four are conformally invariant</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Scale</th><th class="mid">What it is</th><th class="mid">Under a conformal transformation</th></tr></thead>
<tbody>
<tr><th>Total entropy</th><td class="mid">a bit count</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Memory occupancy</th><td class="mid">bits ÷ bits</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Holographic margin</th><td class="mid">log of a ratio</td><td class="mid"><strong>invariant</strong></td></tr>
<tr><th>Degrees of freedom \(a\)</th><td class="mid">a pure number</td><td class="mid"><strong>invariant</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0"><strong>The arrow of time sits entirely in the "physics" column.</strong><br>
On Episode 16's map of weights, all four are in the <em>weight-0 column</em>.<br>
── <strong>Rewriting the books cannot touch the direction of time at all.</strong></p>
</div>

<p>This backs up, with four scales, the table from Extra 2 of the previous series: the conformal-factor side has no arrow of time; only the Weyl side does.</p>

<h2><span class="n">03</span>The heart — compare numerator and denominator at the same rate</h2>

<p>The directions look opposed because <strong>some of these are ratios and some are not</strong>. Separate them and put them in the same units — orders of magnitude per logarithmic step.</p>

<div class="calc">
<span class="tag">Divide by the 140 steps</span>
<p class="lbl">Denominator (capacity): from \(\sim1\) at the Planck era to \(2.05\times10^{122}\) today</p>
$$\frac{122.31\ \text{orders}}{140.24\ \text{steps}}=0.872\ \text{orders/step}$$
<p class="lbl">Numerator (actual entropy): from \(\sim1\) to \(3.1\times10^{104}\)</p>
$$\frac{104.49\ \text{orders}}{140.24\ \text{steps}}=0.745\ \text{orders/step}$$
<p class="lbl">Difference</p>
$$0.127\ \text{orders/step}$$
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0">Numerator and denominator are both growing furiously. <strong>The denominator is merely slightly faster — by 0.13 orders per step.</strong><br>
Stack that 0.13 over 140 steps and you get <em>18 orders of empty space</em>.</p>
</div>

<div class="calc">
<span class="tag">Check</span>
$$0.127\times140.24=17.8\ \text{orders}\qquad\Longrightarrow\qquad \text{occupancy}=1.5\times10^{-18}$$
<p class="lbl">matching the measured value of Episode 6</p>
</div>

<p>So "two up and two down" is no contradiction — <strong>① (the numerator) goes up, while ② and ③ (ratios) are decided by which side wins</strong>. The denominator is set by the expansion, so <em>the direction of the ratio depends on the expansion law</em>.</p>

<div class="fig">
<p class="cap">Figure: how the numerator (actual entropy) and denominator (holographic capacity) grow per logarithmic step. <strong>Both grow furiously, and the slopes differ by only 0.13 orders per step.</strong> The shaded region is the "empty space", reaching 18 orders after 140 steps.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Which step to look at (right edge = today)<input id="sn" type="range" min="0" max="1402" value="1402" step="1"></label>
  <span class="val" id="vn">140.2 steps</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1f5a6b"></i>denominator: capacity \(S_{\max}\) (0.872 orders/step)</span>
  <span><i class="swatch" style="background:#8a6a2a"></i>numerator: entropy \(S_{\rm obs}\) (0.745 orders/step)</span>
  <span><i class="swatch" style="background:#c8dde2"></i>empty space</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>So where is the arrow of time?</h2>

<div class="seven">
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>In the numerator</strong><span>the second law constrains \(S_{\rm obs}\), which <em>never decreases</em>. The arrow itself lives here</span></div></div>
<div class="row"><div class="mk">△</div><div class="txt"><strong>The denominator is the stage</strong><span>capacity \(S_{\max}\propto R_H^2\) is set by geometry; change the expansion law and its direction changes (constant in de Sitter)</span></div></div>
<div class="row"><div class="mk">△</div><div class="txt"><strong>Ratios are the result of a race</strong><span>occupancy and margin are both "numerator ÷ denominator", so their direction depends on <em>which grows faster</em> — not the arrow itself</span></div></div>
</div>

<p>Episode 6 wrote that "<em>how badly the tool is breaking is the arrow of time</em>". In today's terms — <strong>that was the statement measured by the ratio (②)</strong>. Precisely, the tool breaks because the numerator grows, and it looks diluted because the denominator grows faster. <em>Unmixed, the arrow of time lives only in the numerator.</em></p>

<h2><span class="n">05</span>The a-theorem is on a different axis</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>　</th><th class="mid">①②③</th><th class="mid">④ the a-theorem</th></tr></thead>
<tbody>
<tr><th>Direction of what</th><td class="mid">cosmic time</td><td class="mid"><strong>the renormalisation group (energy)</strong></td></tr>
<tr><th>Axis</th><td class="mid">\(\ln t\) (140 steps)</td><td class="mid">\(\ln\mu\) (73 steps)</td></tr>
<tr><th>Why it decreases</th><td class="mid">expansion widens the capacity</td><td class="mid">coarse-graining discards information</td></tr>
<tr class="hi"><th>In common</th><td class="mid" colspan="2"><strong>both are forgetting — a direction you cannot go back along</strong></td></tr>
</tbody>
</table>
</div>

<p>As Episode 2 showed, the two axes are linked by \(d\ln T/d\ln t=-p\). <strong>One step of cosmic time is \(p=0.513\) steps of renormalisation group flow.</strong> So the decrease of \(a\) can be converted into cosmic time, giving <em>4.8% of forgetting per step</em> over the active range (steps 74–132).</p>

<div class="aside">
<span class="tag">The four in one line</span>
<strong>The numerator (entropy) grows, the denominator (capacity) grows faster, and the degrees of freedom decrease on a different axis.</strong><br>
All three have a direction you cannot reverse, all three are dimensionless, and all three are untouched by a conformal transformation — <em>the arrow of time sits entirely in the column this series has been calling "physics"</em>.
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① "\(S_{\rm obs}\sim1\) at the Planck era" is an indicative value.</strong> How to count the entropy of the early universe is not obvious (particles inside the horizon? horizon entropy?), so read it as an order-of-magnitude argument. The 0.745 orders/step of §03 depends on it.</p>
<p style="margin:0 0 10px"><strong>② \(S_{\rm obs}=3.1\times10^{104}k_B\) is the Egan &amp; Lineweaver (2010) census and depends strongly on the supermassive black hole mass function</strong> (same caveat as Episode 6 ①). Most of the numerator's growth is black hole formation, so <em>that uncertainty passes straight into the 0.745</em>.</p>
<p style="margin:0 0 10px"><strong>③ "The numerator never decreases" is the second law for a closed system.</strong> Whether the universe is a closed system, and whether the interior of the horizon may be treated as one, are themselves unsettled questions — there is flow across the horizon, so naive application needs care.</p>
<p style="margin:0 0 10px"><strong>④ \(a\) is defined only at conformal fixed points</strong> (Episode 2; Extra 7 of the previous series). "\(a\) falls from 995.5 to 62" is a schematic free-field count, not a test of the a-theorem, and "4.8% per step" likewise.</p>
<p style="margin:0"><strong>⑤ "The arrow of time is in the numerator" is this series' own account.</strong> The debate over the origin of the arrow (the past hypothesis, the Weyl curvature hypothesis, decoherence, cosmological initial conditions) is unsettled and this document endorses none of them — <em>its scope is confirming that the four scales do not contradict each other</em>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Of the four scales, which increase and which decrease?
<details><summary>Show the answer</summary><div class="ans">Up: total entropy (\(+104\) orders), holographic margin (\(+33\)). Down: memory occupancy (\(-18\)), degrees of freedom \(a\) (\(-1.2\)). <em>No contradiction</em> — some are ratios and some are not.</div></details></li>

<li>Find the growth of numerator and denominator in orders per step.
<details><summary>Show the answer</summary><div class="ans">Denominator \(122.31/140.24=0.872\), numerator \(104.49/140.24=0.745\) orders per step. <strong>Difference 0.127</strong>, which over 140 steps is 17.8 orders, matching the occupancy \(1.5\times10^{-18}\).</div></details></li>

<li>Why are all four untouched by a conformal transformation?
<details><summary>Show the answer</summary><div class="ans">Because all four are dimensionless (a bit count, a ratio, the log of a ratio, a pure number) — the <strong>weight-0 column</strong> of Episode 16's map. <em>Rewriting the books cannot touch the direction of time.</em></div></details></li>

<li>Restate Episode 6's "how badly the tool is breaking is the arrow of time" in today's terms.
<details><summary>Show the answer</summary><div class="ans">That was <strong>the statement measured by the ratio (occupancy)</strong>. Precisely, the tool breaks (the Weyl side grows) because the numerator grows, and it looks diluted because the denominator grows faster. <em>Unmixed, the arrow lives only in the numerator.</em></div></details></li>

<li>(Harder) Is the a-theorem the same arrow as the other three?
<details><summary>Show the answer</summary><div class="ans">The direction is the same (irreversible) but <strong>the axis differs</strong> — ①②③ live on cosmic time \(\ln t\) (140 steps), \(a\) on the renormalisation-group energy axis \(\ln\mu\) (73 steps). Episode 2's \(d\ln T/d\ln t=-p\) converts between them, giving 4.8% of forgetting per step over the active range. <em>What they share is the shape: coarse-grain and you cannot go back.</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — the arrow is in the numerator; the denominator is the stage</h2>
<p>Four scales for the direction of time: total entropy (\(+104\) orders), memory occupancy (\(-18\)), holographic margin (\(+33\)), degrees of freedom \(a\) (\(-1.2\)). Two up, two down. <strong>The first thing to confirm was that all four are dimensionless — conformally invariant</strong>: <em>the arrow of time sits entirely in the "physics" column</em>, untouchable by rewriting the books.</p>
<p>The apparent opposition came from mixing ratios with non-ratios. In the same units — <strong>denominator (capacity) 0.872 orders/step, numerator (entropy) 0.745</strong>. <em>Both furious; the difference is only 0.127 orders per step.</em> Stacked over 140 steps that is 17.8 orders, exactly Episode 6's occupancy \(1.5\times10^{-18}\).</p>
<p>So the arrow's home is clear — <strong>it is in the numerator</strong>. The second law constrains \(S_{\rm obs}\), which never decreases. The denominator is a stage set by geometry (expansion), and ratios are just the outcome of the race. Episode 6's "how badly the tool is breaking is the arrow of time" was <em>the version measured by a ratio</em>.</p>
<p>The fourth scale, \(a\), lives on a different axis — <strong>the renormalisation-group energy axis</strong>, not cosmic time. Episode 2's \(d\ln T/d\ln t=-p\) converts between them, giving 4.8% of forgetting per step over the active range. <em>Different axis, same shape: coarse-grain and you cannot go back.</em></p>
</div>

<div class="next">
<span class="lbl">Next — Episode 22</span>
The second half of Part III writes the universe-as-computer <strong>one level more concretely</strong> — its <em>instruction set</em>. Episode 1 took the spec (memory, clock, operations) but left the content of "operations" blank. The Margolus–Levitin limit counts only <strong>transitions to orthogonal states</strong> and does not ask what is being done. So what operations does the universe actually perform — <em>propagation, interaction, measurement (decoherence)</em>? We estimate the cost of each in bits and build a breakdown of the \(10^{121}\) operations. <strong>Most of it should be spent on doing nothing.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sn=document.getElementById('sn'), vn=document.getElementById('vn'), ro=document.getElementById('ro');
  var X0=76, X1=700, Y0=30, Y1=316;
  var A=0.872, B=0.745, NMAX=140.24;
  var xmin=0, xmax=145, ymin=0, ymax=130;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function draw(){
    var n=parseInt(sn.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=0;e<=130;e+=20){
      var y=py(e);
      g.strokeStyle='#eef4f5'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#93a8ad'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=140;q+=20){
      var x=px(q);
      g.strokeStyle='#f5f9fa'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#93a8ad'; g.fillText(String(q), x, Y1+16);
    }
    g.strokeStyle='#c3d6da'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    g.fillStyle='#c8dde2'; g.globalAlpha=0.55;
    g.beginPath();
    g.moveTo(px(0),py(0));
    g.lineTo(px(n),py(A*n));
    g.lineTo(px(n),py(B*n));
    g.closePath(); g.fill();
    g.globalAlpha=1;

    g.strokeStyle='#1f5a6b'; g.lineWidth=3.2;
    g.beginPath(); g.moveTo(px(0),py(0)); g.lineTo(px(NMAX),py(A*NMAX)); g.stroke();
    g.strokeStyle='#8a6a2a'; g.lineWidth=3.2;
    g.beginPath(); g.moveTo(px(0),py(0)); g.lineTo(px(NMAX),py(B*NMAX)); g.stroke();

    g.textAlign='left';
    g.fillStyle='#1f5a6b'; g.fillText('capacity S_max (0.872 orders/step)', px(84), py(A*84)-10);
    g.fillStyle='#8a6a2a'; g.fillText('entropy S_obs (0.745)', px(92), py(B*92)+18);

    g.strokeStyle='#5a7a80'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(n),Y0); g.lineTo(px(n),Y1); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#1f5a6b';
    g.beginPath(); g.arc(px(n),py(A*n),4.5,0,6.2832); g.fill();
    g.fillStyle='#8a6a2a';
    g.beginPath(); g.arc(px(n),py(B*n),4.5,0,6.2832); g.fill();

    g.fillStyle='#6b858a'; g.textAlign='center';
    g.fillText('logarithmic step  ln(t / t_P)', (X0+X1)/2, Y1+36);

    var gap=(A-B)*n;
    vn.textContent=n.toFixed(1)+' steps';
    ro.textContent='step '+n.toFixed(1)+
      '　capacity 10^'+(A*n).toFixed(1)+
      '　entropy 10^'+(B*n).toFixed(1)+
      '　→　empty '+gap.toFixed(1)+' orders　=　occupancy '+Math.pow(10,-gap).toExponential(2)+
      (n>139?'　★ matches today’s 1.5×10⁻¹⁸':'');
  }
  sn.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-21-arrows.html', acc='#1f5a6b', ops='#8a6a2a',
      title='There are four scales for the arrow of time ── c·t = const, That Clicks, Episode 21',
      ep='EPISODE 21 ／ Setting four scales side by side',
      eyebrow='Two go up and two go down — and it was no contradiction',
      h1='There are four scales<br>for the arrow of time',
      sub='Total entropy, memory occupancy, holographic margin, degrees of freedom \\(a\\).<br><em>Do they point the same way? We check.</em>',
      byline_l='What you need: subtracting orders of magnitude',
      byline_r='0.872 − 0.745 = 0.127 orders/step',
      body=BODY + '\n\n<p class="foot">This document is Episode 21 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. It sets side by side the results of Episodes 2, 6 and 20 and makes no new claim of physics. From the denominator \\(S_{\\max}=2.05\\times10^{122}\\) (the horizon\'s holographic bound), the numerator \\(S_{\\rm obs}=3.1\\times10^{104}k_B\\) (Egan &amp; Lineweaver 2010, ApJ 710, 1825) and the logarithmic step count \\(\\ln(t_0/t_P)=140.24\\), the figures 0.872 and 0.745 orders per step, their difference 0.127, and 17.8 orders over 140 steps are computed here (kenshou/calc25.py). <strong>"\\(S_{\\rm obs}\\sim1\\) at the Planck era" is indicative, and how to count early-universe entropy is not obvious</strong> — the 0.745 depends on it. \\(S_{\\rm obs}\\) depends strongly on the supermassive black hole mass function, and that uncertainty passes into the numerator\'s growth. "The numerator never decreases" is the second law for a closed system, and <strong>whether the interior of the horizon may be treated as one is unsettled</strong> (there is flow across the horizon). \\(a\\) is defined only at conformal fixed points; "995.5 → 62" is a schematic free-field count rather than a test of the a-theorem (Extra 7 of the previous series), and "4.8% per step" likewise. The link between the axes, \\(d\\ln T/d\\ln t=-p\\), was derived in Episode 2. <strong>"The arrow of time is in the numerator" is this series\' own account</strong>; the debate over the arrow\'s origin (the past hypothesis, the Weyl curvature hypothesis, decoherence, cosmological initial conditions) is unsettled and none is endorsed here — the scope is confirming that the four scales do not contradict each other. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider moves through the steps and the gap between the two lines opens. "Show the answer" opens each solution.')
