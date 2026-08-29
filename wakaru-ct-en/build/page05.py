# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 4 ended in a clean opposition: \(\Lambda\)CDM has 6 dimensionless parameters, \(c\cdot t=\text{const}\) has 0. <strong>The description length is overwhelmingly shorter.</strong> And yet the two \(H_0d_L/c\) curves differ by 0.21 magnitudes at \(z\simeq1.1\). <em>Is the shorter one right, or the one that fits?</em> This is not a matter of taste — information theory keeps a price list. This episode goes and reads it.</p>

<h2><span class="n">01</span>Splitting description length in two</h2>

<p>Imagine posting both a model and a data set to someone. Two things go in the envelope: <em>the description of the model</em> and <em>the deviations from it</em>. The best model is the one for which the total is shortest — that is the minimum description length (MDL) idea.</p>

<div class="calc">
<span class="tag">What goes in the envelope</span>
$$\underbrace{L_{\text{total}}}_{\text{total bits}}=\underbrace{-\log_2 L(\text{data}\mid\text{model})}_{\text{cost of misfit}}+\underbrace{\frac{k}{2}\log_2 N}_{\text{price of parameters}}$$
<p class="lbl">\(k\) is the number of parameters, \(N\) the number of data points</p>
</div>

<p>Holding one parameter lengthens the message by however many bits it takes to send its value — that is the right-hand term. Multiply that term by 2 and write it in natural logs and you get \(k\ln N\), <strong>which is exactly the BIC penalty</strong>. MDL and BIC were the same accounting in different units.</p>

<h2><span class="n">02</span>The price list for one parameter</h2>

<div class="calc">
<span class="tag">The price list</span>
<p class="lbl">AIC (Akaike) — penalty \(2k\) in natural-log \(\chi^2\) units</p>
$$\frac{2}{2\ln 2}=\frac{1}{\ln 2}=1.443\ \text{bits per parameter}\qquad(\text{independent of }N)$$
<p class="lbl">BIC (Bayesian) — penalty \(k\ln N\)</p>
$$\frac{\ln N}{2\ln 2}=\tfrac12\log_2 N\ \text{bits per parameter}\qquad(\text{rises with more data})$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Data points \(N\)</th><th class="mid">AIC price</th><th class="mid">BIC price</th><th class="mid">BIC's \(\Delta\chi^2\) budget</th></tr></thead>
<tbody>
<tr><th>100</th><td class="mid">1.443 bit</td><td class="mid">3.32 bit</td><td class="mid">4.61</td></tr>
<tr><th>1000</th><td class="mid">1.443 bit</td><td class="mid">4.98 bit</td><td class="mid">6.91</td></tr>
<tr class="hi"><th>1701 (Pantheon+ scale)</th><td class="mid">1.443 bit</td><td class="mid"><strong>5.37 bit</strong></td><td class="mid">7.44</td></tr>
<tr><th>10000</th><td class="mid">1.443 bit</td><td class="mid">6.64 bit</td><td class="mid">9.21</td></tr>
</tbody>
</table>
</div>

<p>Read it like this: <strong>saving one parameter earns you 5.4 bits</strong>. So as long as you lose less than 5.4 bits on fit, the shorter model wins.</p>

<h2><span class="n">03</span>Converting misfit into bits too</h2>

<div class="calc">
<span class="tag">The exchange rate</span>
<p class="lbl">For Gaussian errors \(-2\ln L=\chi^2+\text{const}\), so</p>
$$\text{bits lost to misfit}=\frac{\Delta\chi^2}{2\ln 2}=0.7213\,\Delta\chi^2$$
</div>

<p>The currencies now match. All that remains is to compute \(\Delta\chi^2\).</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>Doing the accounts</h2>

<p>Compare on the supernova distance modulus. In magnitudes, the difference between Episode 4's closed form \(H_0d_L/c=(1+z)\ln(1+z)\) and the \(\Lambda\)CDM numerical integral is:</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>\(z\)</th><th class="mid">0.05</th><th class="mid">0.1</th><th class="mid">0.3</th><th class="mid">0.5</th><th class="mid">1.0</th><th class="mid">1.5</th><th class="mid">2.0</th></tr></thead>
<tbody>
<tr><th>\(\Delta\mu\) [mag]</th><td class="mid">−0.027</td><td class="mid">−0.052</td><td class="mid">−0.126</td><td class="mid">−0.171</td><td class="mid">−0.213</td><td class="mid">−0.206</td><td class="mid">−0.181</td></tr>
</tbody>
</table>
</div>

<p>A supernova's absolute magnitude is unknown, so <strong>any constant offset can simply be absorbed</strong> (this is the practical version of "\(H_0\) is dimensionful, so we do not count it"). What survives absorption is the <em>difference in shape</em>. Computing on a Pantheon+-like redshift distribution (median \(z=0.27\), 1701 supernovae, \(\sigma=0.15\) mag each):</p>

<div class="calc">
<span class="tag">The accounts</span>
<p class="lbl">Residual after absorbing the constant</p>
$$\text{RMS}=0.053\ \text{mag}\qquad\Longrightarrow\qquad \Delta\chi^2=N\left(\frac{0.053}{0.15}\right)^2=213$$
<p class="lbl">In bits</p>
$$\text{cost of misfit}=\frac{213}{2\ln2}=154\ \text{bits}$$
<p class="lbl">Against the saving</p>
$$\text{one parameter}=5.4\ \text{bits}$$
</div>

<div class="keybox">
<p class="lbl">The bill for this episode</p>
<p style="margin:6px 0 0">Earned: <strong>+5.4 bits</strong>　　Lost: <strong>−154 bits</strong>　　Net: <strong>−149 bits</strong><br>
The shortness bought by dropping one parameter is about <em>1/29</em> of what is paid on fit.</p>
</div>

<h2><span class="n">05</span>From the other side — how well would it have to fit?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Criterion</th><th class="mid">\(\Delta\chi^2\) budget</th><th class="mid">Residual RMS allowed</th><th class="mid">Actual</th></tr></thead>
<tbody>
<tr><th>AIC</th><td class="mid">2</td><td class="mid">5.1 mmag</td><td class="mid" rowspan="2"><strong>53 mmag</strong></td></tr>
<tr class="hi"><th>BIC</th><td class="mid">7.44</td><td class="mid"><strong>9.9 mmag</strong></td></tr>
</tbody>
</table>
</div>

<p>After averaging over 1701 supernovae, the two curves would have to agree to <strong>10 millimagnitudes per supernova</strong> — one fifteenth of the intrinsic scatter (150 mmag). The actual discrepancy is 53 mmag. <em>Short by an order of magnitude.</em></p>

<h2><span class="n">06</span>So how many supernovae settle it?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Count \(N\)</th><th class="mid">Misfit \(\Delta\chi^2\)</th><th class="mid">BIC budget \(\ln N\)</th><th class="mid">Winner</th></tr></thead>
<tbody>
<tr class="hi"><th>10</th><td class="mid">1.25</td><td class="mid">2.30</td><td class="mid"><strong>\(c\cdot t=\text{const}\)</strong></td></tr>
<tr><th>≈ 26</th><td class="mid">3.26</td><td class="mid">3.26</td><td class="mid">a draw</td></tr>
<tr><th>100</th><td class="mid">12.5</td><td class="mid">4.61</td><td class="mid">\(\Lambda\)CDM</td></tr>
<tr><th>1000</th><td class="mid">125</td><td class="mid">6.91</td><td class="mid">\(\Lambda\)CDM</td></tr>
</tbody>
</table>
</div>

<p><strong>With fewer than 26 supernovae, \(c\cdot t=\text{const}\) is the better model.</strong> This is not sour grapes — information theory really does say so. <em>When data are scarce, the short theory is the correct choice.</em> When accelerated expansion was found in 1998, the two teams had 42 and 16 supernovae. <strong>Back then this contest would have been close.</strong></p>

<div class="fig">
<p class="cap">Figure: data points along the horizontal axis, bits up the vertical. <strong>The price of a parameter grows only as \(\log N\)</strong>, while <strong>the cost of misfit grows as \(N\)</strong>. So the two lines must cross, and past the crossing they never swap back.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Model discrepancy (residual RMS after absorbing the constant)<input id="sr" type="range" min="1" max="120" value="53" step="1"></label>
  <span class="val" id="vr">53 mmag</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#17454a"></i>price of one parameter (\(\tfrac12\log_2 N\))</span>
  <span><i class="swatch" style="background:#8c3a52"></i>cost of misfit (\(\propto N\))</span>
</div>
</div>

<p>Drag the discrepancy down and the crimson line slides right, taking the crossing with it. <strong>But they always cross</strong> — the slopes differ. Even at 1 mmag the crossing is only around \(N\simeq10^4\). <em>Keep adding data and shortness must eventually lose.</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">07</span>The reveal — Occam's razor has an expiry date</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">How it grows</th><th class="mid">Why</th></tr></thead>
<tbody>
<tr><th>Price of a parameter</th><td class="mid">\(\propto\log N\)</td><td class="mid">more data demands more precision in the value you send — but only logarithmically more</td></tr>
<tr class="hi"><th>Cost of misfit</th><td class="mid">\(\propto N\)</td><td class="mid">each point's residual must be re-sent, so it piles up in direct proportion</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The one line of this episode</p>
<p style="margin:6px 0 0">The gain from shortness goes as \(\log N\); the loss from misfit goes as \(N\).<br>
So with enough data the short model <strong>must</strong> lose — <em>unless it is actually right</em>.</p>
</div>

<p>Occam's razor is neither superstition nor aesthetics but <strong>a computable discount voucher</strong>. Its face value is merely \(\log N\), however, and it gets <em>relatively cheaper as data accumulate</em>. "Simpler theories are better" turned out to be a theorem with the proviso <em>if the fits are comparable</em>.</p>

<div class="aside">
<span class="tag">Connecting to Episode 4</span>
Episode 4 called "zero dimensionless parameters" the limit of Occam's razor. Today <strong>that zero acquired a price tag — 5.4 bits</strong>. And note that everything \(c\cdot t=\text{const}\) bought us in Episode 4 (an integral collapsing to one logarithm, closed forms throughout) counts for <em>nothing whatsoever</em> in this ledger. <strong>Ease of computation is worth zero bits to an information criterion.</strong> Episode 4 keeps its value all the same — that was about <em>notation</em>, this is about <em>models</em> (the two things Episode 3 separated, still doing their work).
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① The \(\Delta\chi^2=213\) of §04 is the expectation value on the assumption that \(\Lambda\)CDM (\(\Omega_m=0.315\)) is correct.</strong> It is not a fit to real data. The redshift distribution is a Pantheon+-<em>like</em> mock (median 0.27), not the real one, and \(\sigma=0.15\) mag is a representative intrinsic scatter. Including correlated systematics reduces the effective count and shrinks \(\Delta\chi^2\). <em>Read it as an order-of-magnitude argument.</em></p>
<p style="margin:0 0 10px"><strong>② The literature does not agree on the comparison with real data.</strong> Melia and collaborators argue that model-independent distance indicators favour \(R_h=ct\); other analyses (Shafer 2015 and others) report a strong preference for \(\Lambda\)CDM. <em>This is a conditional calculation — "here is what follows if \(\Lambda\)CDM is right" — not an observational verdict.</em></p>
<p style="margin:0 0 10px"><strong>③ The parameter counting is disputed too.</strong> For supernovae alone, \(H_0\) is degenerate with absolute magnitude, so it is effectively 1 parameter (\(\Omega_m\)) against 0. The "6" of Episode 4 is the standard \(\Lambda\)CDM basis including the CMB — a different arena. The 5.4 bits here is the price of <em>one</em>.</p>
<p style="margin:0"><strong>④ The \(\tfrac{k}{2}\log_2 N\) of MDL is asymptotic</strong>; exactly, there is a further term depending on the model's geometry (the volume of Fisher information). AIC and BIC derive from different premises (minimising prediction error vs maximising posterior probability), and which to use depends on the purpose — <em>there is no single correct price list.</em></p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>At \(N=100\), what is the BIC price of one parameter in bits?
<details><summary>Show the answer</summary><div class="ans">\(\tfrac12\log_2 100=3.32\) bits; in \(\Delta\chi^2\), \(\ln100=4.61\). <strong>Multiply the data by 17 (to 1701) and the price only goes 3.32 → 5.37 bits</strong> — because it is a logarithm.</div></details></li>

<li>How many bits is \(\Delta\chi^2=213\)?
<details><summary>Show the answer</summary><div class="ans">\(213/(2\ln2)=154\) bits — about <strong>29 times</strong> the 5.37 bits saved by dropping a parameter. A net loss of 149 bits.</div></details></li>

<li>Why is the AIC price independent of \(N\), and what does the difference from BIC reflect?
<details><summary>Show the answer</summary><div class="ans">Because AIC's penalty \(2k\) contains no \(N\). AIC minimises <strong>prediction error</strong>: adding one parameter worsens the expected prediction error by 2 in \(\chi^2\). BIC maximises <strong>posterior probability</strong>: as \(N\) grows, "it fitted by luck" becomes less likely, so the fine gets heavier. <em>Different purpose, different price list.</em></div></details></li>

<li>If the residual RMS were 20 mmag, up to how many supernovae would \(c\cdot t=\text{const}\) win?
<details><summary>Show the answer</summary><div class="ans">Solve \(\ln N=N(0.020/0.15)^2=0.01778\,N\) numerically: \(N\simeq325\). <strong>Cutting the discrepancy by 2.7 multiplies the winnable count by about 12</strong> — and still only reaches the low hundreds. \(\log N\) versus \(N\) was a losing contest from the start.</div></details></li>

<li>(Harder) Under what condition is "the shorter theory is better" correct?
<details><summary>Show the answer</summary><div class="ans"><strong>As long as the difference in fit stays within about \(\log N\).</strong> A parameter costs only \(\tfrac12\log_2 N\) bits, so the moment the misfit exceeds that (\(\Delta\chi^2>\ln N\)) the ranking flips. And since misfit grows \(\propto N\), <em>adding data must flip it eventually</em>. Occam's razor is a theorem — but a theorem with an expiry date.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — the price tag read 5.4 bits</h2>
<p>"Is the shorter one right, or the one that fits?" Information theory answers with a price list. Description length splits into <em>cost of misfit</em> plus <em>price of parameters</em>, the latter being \(\tfrac{k}{2}\log_2 N\) bits — the same thing as BIC's \(k\ln N\) penalty. Under AIC it is <strong>1.443 bits each, independent of \(N\)</strong>; under BIC, \(\tfrac12\log_2 N\) — <strong>5.37 bits</strong> at Pantheon+ scale (1701).</p>
<p>Misfit converts at \(\Delta\chi^2/(2\ln2)\) bits. Doing the accounts on the supernova distance modulus, the residual RMS after absorbing the absolute magnitude is <strong>53 millimagnitudes</strong>, \(\Delta\chi^2=213\), i.e. <strong>154 bits lost</strong> — about <em>29 times</em> the 5.4 bits earned. A net loss of 149 bits. To break even the two would have to agree to <strong>10 millimagnitudes</strong> per supernova, one fifteenth of the intrinsic scatter.</p>
<p>The interesting part came from varying the count: <strong>below 26 supernovae, \(c\cdot t=\text{const}\) is the better model</strong>. Not sour grapes — information theory says so. The 1998 discovery of accelerated expansion used 42 and 16 supernovae. <em>When data are scarce, the short theory is the correct choice.</em></p>
<p>The reveal was in the slopes: <strong>gain from shortness \(\propto\log N\), loss from misfit \(\propto N\)</strong>. The lines must cross and never swap back. Occam's razor is neither superstition nor aesthetics but a computable discount voucher — whose face value grows only logarithmically. "Simpler is better" was a theorem with the proviso <em>if the fits are comparable</em>.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 6</span>
Three episodes of dividing things (memory ÷ operations, time ÷ energy, fit ÷ parameters). Next we look <em>inside</em> the memory — today's universe uses only \(1.5\times10^{-18}\) of its \(10^{122}\)-bit capacity. It is essentially empty. And that emptiness is not a defect: it is another way of saying <strong>the universe is still 99.9999999999999998% conformally flat</strong> — <em>which is exactly why this series' tools work at all</em>. We rewrite Penrose's Weyl curvature hypothesis, and the table from Extra 2 of the previous series (the gravitational field splitting into a conformal factor — bookkeeping, no arrow of time — and a Weyl tensor — physics, with an arrow), in the language of occupancy. <strong>How badly the tool is breaking down turns out to be the arrow of time.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sr=document.getElementById('sr'), vr=document.getElementById('vr'), ro=document.getElementById('ro');
  var X0=70, X1=700, Y0=28, Y1=318;
  var LN2=Math.log(2), SIG=0.15;
  var xmin=0, xmax=5;
  var ymin=-1, ymax=4;

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function priceBits(N){ return 0.5*Math.log(N)/LN2; }
  function fitBits(N,r){ return N*(r/SIG)*(r/SIG)/(2*LN2); }

  function draw(){
    var r=parseInt(sr.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=-1;e<=4;e++){
      var y=py(e);
      g.strokeStyle='#e9f0f0'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#8fa0a0';
      g.fillText(e<0?'0.1':(e===0?'1':'10'+e), X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=0;q<=5;q++){
      var x=px(q);
      g.strokeStyle='#f0f6f6'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#8fa0a0'; g.fillText(q===0?'1':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#c2d5d5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    var lx=Math.log(1701)/Math.LN10;
    g.strokeStyle='#9aa8a8'; g.lineWidth=1.4; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(lx),Y0); g.lineTo(px(lx),Y1); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#778888'; g.textAlign='center';
    g.fillText('Pantheon+  1701 SNe', px(lx), Y0-8);

    function curve(fn,color,w){
      g.strokeStyle=color; g.lineWidth=w; g.beginPath();
      var first=true;
      for(var i=0;i<=340;i++){
        var lN=xmin+(xmax-xmin)*i/340, N=Math.pow(10,lN);
        var v=fn(N); if(v<=0) continue;
        var yy=Math.log(v)/Math.LN10;
        if(yy<ymin-0.5||yy>ymax+0.5){ first=true; continue; }
        if(first){ g.moveTo(px(lN),py(yy)); first=false; } else g.lineTo(px(lN),py(yy));
      }
      g.stroke();
    }
    curve(function(N){return fitBits(N,r);}, '#8c3a52', 3.2);
    curve(function(N){return priceBits(N);}, '#17454a', 3.2);

    var k=(r/SIG)*(r/SIG), Ncross=null;
    var peak=1/k;
    if(Math.log(peak)-1>0){
      var lo=peak, hi=1e12;
      for(var it=0;it<300;it++){
        var mid=Math.sqrt(lo*hi);
        if(Math.log(mid)-mid*k>0) lo=mid; else hi=mid;
      }
      Ncross=Math.sqrt(lo*hi);
    }
    if(Ncross&&Ncross>1&&Ncross<1e5){
      var cx=Math.log(Ncross)/Math.LN10, cy=Math.log(priceBits(Ncross))/Math.LN10;
      g.fillStyle='#3d5a5a';
      g.beginPath(); g.arc(px(cx),py(cy),5.5,0,6.2832); g.fill();
      g.strokeStyle='#fff'; g.lineWidth=1.8;
      g.beginPath(); g.arc(px(cx),py(cy),5.5,0,6.2832); g.stroke();
      g.fillStyle='#3d5a5a'; g.textAlign='left';
      g.fillText('a draw at N≈'+Math.round(Ncross), px(cx)+10, py(cy)-8);
    }

    g.fillStyle='#17454a'; g.textAlign='left';
    g.fillText('price of one parameter ∝ log N', X0+10, py(Math.log(priceBits(30))/Math.LN10)-26);
    g.fillStyle='#8c3a52'; g.textAlign='right';
    g.fillText('cost of misfit ∝ N', X1-8, py(3.3));

    g.fillStyle='#5f7272'; g.textAlign='center';
    g.fillText('number of data points  N', (X0+X1)/2, Y1+36);
    g.save(); g.translate(18,(Y0+Y1)/2); g.rotate(-Math.PI/2);
    g.fillText('bits', 0,0); g.restore();

    var fb=fitBits(1701,r), pb=priceBits(1701);
    vr.textContent=Math.round(r*1000)+' mmag';
    ro.textContent='residual RMS = '+Math.round(r*1000)+' mmag　/　at Pantheon+ scale: misfit '+
      fb.toFixed(1)+' bit　vs　parameter price '+pb.toFixed(2)+' bit　→　'+
      (fb>pb ? 'net '+(fb-pb).toFixed(1)+' bit loss (ΛCDM wins)' : 'net '+(pb-fb).toFixed(2)+' bit gain (c·t=const wins)')+
      '　/　the draw sits at '+(!Ncross ? '(ΛCDM wins at every N)' : (Ncross<1e5 ? 'N≈'+Math.round(Ncross) : 'N above 10⁵'));
  }
  sr.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-05-price.html', acc='#17454a', ops='#8c3a52',
      title='What does shortness cost? ── c·t = const, That Clicks, Episode 5',
      ep='EPISODE 5 ／ Shortness and fit, priced in one currency',
      eyebrow='Zero description length — so how many bits is that zero worth?',
      h1='What does<br>shortness cost?',
      sub='Episode 4 found \\(c\\cdot t=\\)const has zero dimensionless parameters — Occam at the limit.<br><em>But it loses on fit. Here both are converted into bits.</em>',
      byline_l='What you need: logarithms, \\(\\chi^2\\), division',
      byline_r='one parameter \\(=\\tfrac12\\log_2 N\\) bits',
      body=BODY + '\n\n<p class="foot">This document is Episode 5 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The two-part MDL code \\(-\\log_2 L+\\tfrac{k}{2}\\log_2 N\\), Akaike\'s criterion \\(\\mathrm{AIC}=-2\\ln L+2k\\), the Bayesian criterion \\(\\mathrm{BIC}=-2\\ln L+k\\ln N\\), and \\(-2\\ln L=\\chi^2+\\text{const}\\) for Gaussian errors are all standard. The conversion into bits (one parameter costing \\(1/\\ln2=1.443\\) bits under AIC and \\(\\tfrac12\\log_2 N\\) under BIC, misfit costing \\(\\Delta\\chi^2/(2\\ln2)\\) bits) is this document\'s own rewriting. The numbers in §04–§06 are computed here and are <strong>expectation values on the assumption that \\(\\Lambda\\)CDM (\\(\\Omega_m=0.315\\), \\(\\Omega_r=9.2\\times10^{-5}\\)) is correct</strong> — not fits to real data. The redshift distribution is a Pantheon+-like mock (\\(N=1701\\), median \\(z=0.27\\)) with \\(\\sigma=0.15\\) mag per supernova (a representative intrinsic scatter); correlated systematics are not included, and including them lowers the effective count and \\(\\Delta\\chi^2\\). Comparisons of \\(R_h=ct\\) and \\(\\Lambda\\)CDM on real data do not agree in the literature: Melia and collaborators argue in favour of \\(R_h=ct\\), while other analyses (Shafer 2015 and others) report a strong preference for \\(\\Lambda\\)CDM. Using supernovae alone, \\(H_0\\) is degenerate with absolute magnitude, so the effective parameter count is 1 for \\(\\Lambda\\)CDM against 0 for \\(R_h=ct\\); the "6" quoted in Episode 4 is the standard basis including the CMB. The \\(\\tfrac{k}{2}\\log_2 N\\) of MDL is asymptotic, with a further term depending on the volume of Fisher information. AIC and BIC rest on different premises (minimising prediction error vs maximising posterior probability) and no single criterion is uniquely correct. The 1998 discovery of accelerated expansion used 16 supernovae (High-z Supernova Search Team) and 42 (Supernova Cosmology Project). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the discrepancy and moves the crossing. "Show the answer" opens each solution.')
