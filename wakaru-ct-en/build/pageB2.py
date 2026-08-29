# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">In bonus episode ①, the source of the amplification was that \(\Lambda_{\rm QCD}\) is born of <strong>dimensional transmutation</strong>. Here we measure that exponential map itself, as information. What comes out is a short law — <strong>a hierarchy of \(B\) bits shrinks to a description length of \(\log_2 B\) bits.</strong> And out of it comes <em>a second criterion for whether a fine-tuning is a real problem.</em></p>

<h2><span class="n">01</span>Dimensional transmutation is an exponential map</h2>

<div class="calc">
<span class="tag">A coupling runs, and a scale is born</span>
$$\Lambda=M\exp\!\left(-\frac{2\pi}{b_0\,\alpha(M)}\right)
\qquad\Longrightarrow\qquad
\ln\frac{M}{\Lambda}=\frac{2\pi}{b_0\alpha(M)}\equiv H$$
<p class="lbl">differentiate with respect to \(\ln\alpha\): <strong>\(d\ln\Lambda/d\ln\alpha=+H\)</strong> — the gain is exactly the size of the hierarchy</p>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>One bit of \(\alpha\) becomes \(H\) bits of \(\Lambda\).</strong><br>
── <em>The bigger the hierarchy, the bigger the gain.</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">02</span>The core — so a hierarchy costs its own logarithm</h2>

<div class="calc">
<span class="tag">Let the hierarchy be \(B\) bits (\(B=H/\ln2\))</span>
$$\text{to fix }\Lambda\text{ within a factor of two}
\ \Longrightarrow\ \delta(\ln\Lambda)=\ln2
\ \Longrightarrow\ \frac{\delta\alpha}{\alpha}=\frac{\ln2}{H}=\frac1B$$
$$\therefore\quad\text{precision needed on }\alpha=\log_2\frac{1}{\delta\alpha/\alpha}=\boxed{\log_2 B}$$
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>A hierarchy of \(B\) bits can be bought for \(\log_2 B\) bits, through the exponential map.</strong><br>
── A compression of \(B/\log_2 B\). <em>This is exact: no approximation, no convention.</em><br>
It is a statement about <strong>description length</strong> in the sense of Episode 5's MDL.</p>
</div>

<h2><span class="n">03</span>Applied to the actual hierarchies</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Hierarchy</th><th class="mid">raw \(B\)</th><th class="mid">\(\log_2 B\)</th><th class="mid">compression</th><th class="mid">exponential map?</th></tr></thead>
<tbody>
<tr><th>\(\Lambda_{\rm QCD}/M_{\rm Planck}\)</th><td class="mid">\(65.0\)</td><td class="mid">\(6.02\)</td><td class="mid">\(10.8\)</td><td class="mid"><strong>yes</strong> (QCD running)</td></tr>
<tr><th>\(v/M_{\rm Planck}\) (the hierarchy problem)</th><td class="mid">\(55.5\)</td><td class="mid">\(5.79\)</td><td class="mid">\(9.6\)</td><td class="mid">no</td></tr>
<tr><th>\(\Lambda_{\rm QCD}/v\)</th><td class="mid">\(9.5\)</td><td class="mid">\(3.25\)</td><td class="mid">\(2.9\)</td><td class="mid"><strong>yes</strong></td></tr>
<tr class="hi"><th>\(\rho_\Lambda/\rho_{\rm Planck}\) (the CC problem)</th><td class="mid"><strong>\(408.4\)</strong></td><td class="mid"><strong>\(8.67\)</strong></td><td class="mid"><strong>\(47.1\)</strong></td><td class="mid">no</td></tr>
</tbody>
</table>
</div>

<p><strong>Even the cosmological constant problem's 408 bits would cost only 8.7 with an exponential map</strong> (a compression of 47) — <em>which is exactly why everyone goes looking for exponential mechanisms.</em></p>

<div class="fig">
<p class="cap">Figure: the size of a hierarchy \(B\) against its price after the exponential map, \(\log_2 B\). <strong>Blue is without an exponential (the diagonal — the raw price); red is with one (flattened to \(\log_2 B\)).</strong> Move the slider — <em>however large you make it, the red line barely rises.</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>size of the hierarchy \(B\) (bits)<input id="sb" type="range" min="5" max="500" value="408" step="1"></label>
  <span class="val" id="vb">408</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3a4a7a"></i>no exponential (price = \(B\))</span>
  <span><i class="swatch" style="background:#8a3a5a"></i>with one (price = \(\log_2B\))</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>one parameter's worth (5.37 bits)</span>
</div>
</div>

<h2><span class="n">04</span>Which gives a second criterion for fine-tuning</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Fine-tuning</th><th class="mid">reason for the prior (Ep. 48)</th><th class="mid">exponential map (here)</th><th class="mid">price [bits]</th><th class="mid">how it is actually treated</th></tr></thead>
<tbody>
<tr class="hi"><th>Strong CP (\(\theta_{\rm QCD}\))</th><td class="mid"><strong>yes</strong> (an angle)</td><td class="mid">no</td><td class="mid">\(35.9\)</td><td class="mid"><strong>a real problem</strong></td></tr>
<tr><th>\(\Lambda_{\rm QCD}/v\)</th><td class="mid">no</td><td class="mid"><strong>yes</strong></td><td class="mid">\(9.5\to3.2\)</td><td class="mid">nobody calls it a problem</td></tr>
<tr><th>\(v/M_{\rm Planck}\)</th><td class="mid">no</td><td class="mid">no</td><td class="mid">\(55.5\)</td><td class="mid">contested</td></tr>
<tr><th>\(\rho_\Lambda/\rho_{\rm Planck}\)</th><td class="mid">no</td><td class="mid">no</td><td class="mid">\(408.4\)</td><td class="mid">contested</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0"><strong>Two criteria alone reproduce which fine-tunings physicists actually treat as problems.</strong><br>
── We built the test and then went to look: <em>the community had already drawn the same line.</em><br>
The same shape as Episode 47, where the SI had drawn Episode 3's line.</p>
</div>

<h2><span class="n">05</span>The cosmon against this ruler</h2>

<div class="calc">
<span class="tag">Episode 32's cosmon (an exponential potential explaining the cosmological constant)</span>
$$\text{theoretical floor}=\log_2(408.4)=\mathbf{8.67\ \text{bits}}
\qquad
\text{what it actually paid}=2\times5.37=\mathbf{10.73\ \text{bits}}$$
<p class="lbl">an overhead of only <strong>\(2.06\) bits</strong> (24 per cent)</p>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>The cosmon sits only 2 bits above the information-theoretic floor for any exponential mechanism.</strong><br>
Episode 32 said "it pays 10.7 and buys up to 408" —<br>
<em>what we can now see is that the price of 10.7 was itself nearly minimal.</em><br>
※ This does not mean the cosmon is right. It is a statement about a <strong>floor</strong>: no exponential mechanism can be cheaper.</p>
</div>

<h2><span class="n">06</span>Converting the floor into a parameter count</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Problem</th><th class="mid">\(B\) [bits]</th><th class="mid">floor \(\log_2B\)</th><th class="mid">= how many parameters</th><th class="mid">the actual mechanism</th></tr></thead>
<tbody>
<tr class="hi"><th>Strong CP</th><td class="mid">\(35.9\)</td><td class="mid">\(5.17\)</td><td class="mid"><strong>\(0.96\)</strong></td><td class="mid">the axion = <strong>1</strong></td></tr>
<tr><th>Hierarchy</th><td class="mid">\(55.5\)</td><td class="mid">\(5.79\)</td><td class="mid">\(1.08\)</td><td class="mid">transmutation = 1</td></tr>
<tr class="hi"><th>Cosmological constant</th><td class="mid">\(408.4\)</td><td class="mid">\(8.67\)</td><td class="mid"><strong>\(1.62\)</strong></td><td class="mid">the cosmon = <strong>2</strong></td></tr>
</tbody>
</table>
</div>

<div class="seven">
<div class="row"><div class="mk">✓</div><div class="txt"><strong>Strong CP: floor 0.96 → one is enough → the axion uses one</strong><span>it matches</span></div></div>
<div class="row"><div class="mk">✓</div><div class="txt"><strong>The CC: floor 1.61 → two are needed → the cosmon uses two</strong><span>it matches</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>Since it is \(\log_2 B\), the floor saturates at one or two parameters however large the hierarchy</strong><span><em>408 bits, 55 bits and 36 bits all need one or two</em> — with an exponential map, the size of the hierarchy barely affects the price</span></div></div>
</div>

<p>Without an exponential map, you pay \(B\) in full — and \(408\) bits is <strong>76 parameters' worth</strong> at Episode 5's price. <em>Which is why it is not solved.</em></p>

<div class="caveat">
<span class="tag">The honest line — what is strong here and what is weak</span>
<p style="margin:0 0 10px"><strong>(1) Strong (exact): \(d\ln\Lambda/d\ln\alpha=H\), and \(B\to\log_2B\).</strong> The first follows directly from one-loop dimensional transmutation. The second is a statement about <em>description length</em> — "the precision on \(\alpha\) needed to fix a \(B\)-bit hierarchy to within one bit is \(\log_2B\) bits" — with no approximation and no convention. <strong>Everything up to §03 is strong in this sense.</strong></p>
<p style="margin:0 0 10px"><strong>(2) Medium: §04's table.</strong> Whether an exponential map exists is objective, but <em>the "how it is actually treated" column summarises the mood of the literature</em> — four cases only, and the selection is mine.</p>
<p style="margin:0 0 10px"><strong>(3) Weak — the weakest point here: §05 and §06 divide \(\log_2B\) by Episode 5's 5.37 bits per parameter.</strong> That 5.37 came from a particular dataset size (\(N=1701\)) and is <em>the price of a parameter</em>; <strong>there is no guarantee it is the same currency as bits of description precision</strong> (the same weakness as Episode 48, caveat 2). Reject that conversion and §05 and §06 do not stand.</p>
<p style="margin:0 0 10px"><strong>(4) §06's agreement (0.96 → axion 1, 1.61 → cosmon 2) rests on two cases.</strong> As in Episode 36, caveat 2 — <em>it is a recorded pattern, not a result</em>. A third and fourth case that missed would end it.</p>
<p style="margin:0"><strong>(5) "No exponential map" means "none found so far".</strong> No one has shown that an exponential mechanism for the cosmological constant or the hierarchy is impossible — <em>indeed, the compression of 47 in §03 is precisely the reason people keep looking.</em></p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>What is the "gain" of dimensional transmutation?
<details><summary>Show the answer</summary><div class="ans"><strong>\(H=\ln(M/\Lambda)\) — the hierarchy itself.</strong> Differentiating \(\Lambda=M\exp(-2\pi/b_0\alpha)\) with respect to \(\ln\alpha\) gives \(d\ln\Lambda/d\ln\alpha=2\pi/(b_0\alpha)=H\). <em>One bit of \(\alpha\) becomes \(H\) bits of \(\Lambda\).</em></div></details></li>

<li>What does a \(B\)-bit hierarchy cost through the exponential map?
<details><summary>Show the answer</summary><div class="ans"><strong>\(\log_2 B\) bits.</strong> Fixing \(\Lambda\) within a factor of two needs \(\delta\alpha/\alpha=\ln2/H=1/B\), and specifying that precision takes \(\log_2B\) bits. <em>A compression of \(B/\log_2B\), and this is exact.</em></div></details></li>

<li>What do the CC problem's 408 bits become with an exponential map?
<details><summary>Show the answer</summary><div class="ans"><strong>\(\log_2(408.4)=8.67\) bits</strong> — a compression of 47. <em>Which is exactly why everyone goes looking for exponential mechanisms.</em></div></details></li>

<li>What are the two criteria for whether a fine-tuning is a problem?
<details><summary>Show the answer</summary><div class="ans">(i) <strong>Is there a reason for the prior?</strong> (Episode 48 — an angle has one, a mass ratio does not.) (ii) <strong>Is an exponential map available?</strong> (here.) <em>Strong CP has (i) and lacks (ii), so it is real; \(\Lambda_{\rm QCD}/v\) has (ii), so it is not a problem</em> — <strong>and that reproduces how they are actually treated.</strong></div></details></li>

<li>(Harder) What is the weakest part of this episode?
<details><summary>Show the answer</summary><div class="ans"><strong>Dividing \(\log_2B\) by 5.37 bits per parameter</strong> (§05, §06). That 5.37 came from \(N=1701\) and is the price of a parameter — <em>there is no guarantee it is the same currency as bits of description precision</em>. Everything up to §03 is exact; beyond that it leans on the conversion.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: a hierarchy shrinks to its own logarithm</h2>
<p>Differentiate dimensional transmutation \(\Lambda=M\exp(-2\pi/b_0\alpha)\) with respect to \(\ln\alpha\) and you get <strong>\(d\ln\Lambda/d\ln\alpha=H\)</strong> — the gain is exactly the size of the hierarchy. One bit of \(\alpha\) becomes \(H\) bits of \(\Lambda\).</p>
<p>So <strong>a hierarchy of \(B\) bits shrinks to a description length of \(\log_2B\) bits</strong> (a compression of \(B/\log_2B\), exactly). \(\Lambda_{\rm QCD}/M_P\)'s 65 bits become 6.0, \(v/M_P\)'s 55.5 become 5.8, and <strong>the cosmological constant problem's 408 bits become 8.7</strong> — a compression of 47. <em>Which is exactly why everyone goes looking for exponential mechanisms.</em></p>
<p>From this comes a second criterion for fine-tuning — alongside Episode 48's "<strong>is there a reason for the prior?</strong>", now "<strong>is an exponential map available?</strong>". Strong CP has the first and lacks the second, so it is a real problem; \(\Lambda_{\rm QCD}/v\) has the second, so nobody calls it one; \(v/M_P\) and \(\rho_\Lambda\) have neither, and both are contested — <em>exactly the distribution of what physicists actually treat as problems.</em></p>
<p>Then Episode 32's cosmon. The floor for an exponential mechanism is \(\log_2(408.4)=8.67\) bits, and the cosmon paid \(10.73\) — <strong>an overhead of only 2.06 bits</strong>. Episode 32 said "it pays 10.7 and buys up to 408"; <em>what we can now see is that the 10.7 was itself nearly minimal.</em></p>
<p>And finally, how \(\log_2B\) behaves. <strong>However large the hierarchy, the floor saturates at one or two parameters</strong> — 408 bits, 55 bits and 36 bits all need one or two. <em>With an exponential map, the size of the hierarchy barely affects the price.</em> Without one you pay \(B\) in full — and 408 bits is 76 parameters' worth. <strong>Which is why it is not solved.</strong></p>
</div>

<div class="next">
<span class="lbl">In closing — what the two bonus episodes found</span>
Bonus ①: "expanded or shrank" cannot be told apart, but <strong>whether the mass variation is universal can be measured</strong> (\(\mu\), currently 23.3 bits) — and digging turned up <em>a 10.2-bit degeneracy in the quark-mass direction</em>.<br>
Bonus ②: <strong>a hierarchy shrinks to its own logarithm</strong>, so the price of a fine-tuning is set almost entirely by whether an exponential map exists.<br>
── Both stand on the single procedure of Episode 3 (<em>dimensionful is bookkeeping, dimensionless is physics; name what you compare to</em>). <strong>The tool built over 50 episodes still worked.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sb=document.getElementById('sb'), vb=document.getElementById('vb'), ro=document.getElementById('ro');
  var X0=76, X1=690, Y0=34, Y1=290;
  var B0=5, B1=500, C0=0, C1=500;

  function px(b){ return X0+(b-B0)/(B1-B0)*(X1-X0); }
  function py(c){ return Y1-(c-C0)/(C1-C0)*(Y1-Y0); }

  function draw(){
    var B=parseInt(sb.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var c=0;c<=500;c+=100){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(c)); g.lineTo(X1,py(c)); g.stroke();
      g.fillText(c+' bit', X0-8, py(c)+4);
    }
    g.textAlign='center';
    for(var t=100;t<=500;t+=100){ g.fillStyle='#9c96a4'; g.fillText(t, px(t), Y1+20); }

    g.strokeStyle='#c8c2d0'; g.lineWidth=1.6; g.setLineDash([5,4]);
    g.beginPath(); g.moveTo(X0,py(5.37)); g.lineTo(X1,py(5.37)); g.stroke(); g.setLineDash([]);
    g.fillStyle='#a89fae'; g.textAlign='left';
    g.fillText("one parameter's worth (5.37 bits)", X0+8, py(5.37)-7);

    g.strokeStyle='#3a4a7a'; g.lineWidth=2.8; g.beginPath();
    g.moveTo(px(B0),py(B0)); g.lineTo(px(B1),py(B1)); g.stroke();
    g.strokeStyle='#8a3a5a'; g.lineWidth=2.8; g.beginPath();
    for(var i=0;i<=300;i++){ var b=B0+(B1-B0)*i/300, y=Math.log(b)/Math.LN2;
      if(i===0) g.moveTo(px(b),py(y)); else g.lineTo(px(b),py(y)); }
    g.stroke();

    g.textAlign='left';
    g.fillStyle='#3a4a7a'; g.fillText('no exponential: price = B', px(320), py(345));
    g.fillStyle='#8a3a5a'; g.fillText('with one: price = log2 B', px(140), py(40));

    var pts=[[65.0,'Lambda_QCD/M_P'],[55.5,'v/M_P'],[408.4,'rho_L/rho_P']];
    for(var k=0;k<pts.length;k++){
      var b2=pts[k][0];
      g.strokeStyle='#e6e2ea'; g.lineWidth=1; g.setLineDash([2,3]);
      g.beginPath(); g.moveTo(px(b2),Y0); g.lineTo(px(b2),Y1); g.stroke(); g.setLineDash([]);
      g.save(); g.translate(px(b2)-4,Y0+116); g.rotate(-Math.PI/2);
      g.fillStyle='#a89fae'; g.textAlign='left'; g.fillText(pts[k][1],0,0); g.restore();
    }

    var Xc=px(B), lg=Math.log(B)/Math.LN2;
    g.strokeStyle='#5a5262'; g.lineWidth=1.8; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(Xc,Y0); g.lineTo(Xc,Y1); g.stroke(); g.setLineDash([]);
    g.fillStyle='#3a4a7a'; g.beginPath(); g.arc(Xc,py(B),5,0,6.29); g.fill();
    g.fillStyle='#8a3a5a'; g.beginPath(); g.arc(Xc,py(lg),5,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('size of the hierarchy  B  (bits)', (X0+X1)/2, Y1+44);

    vb.textContent=String(B);
    ro.textContent='B = '+B+' bits　→　without an exponential '+B+
      ' bits, with one '+lg.toFixed(2)+' bits　/　compression '+(B/lg).toFixed(1)+'x'+
      '　('+(lg/5.37).toFixed(2)+" parameters' worth)"+
      (B>=400?'　★ this is the cosmological constant problem — 47x':'');
  }
  sb.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-b2-hierarchy.html', acc='#8a3a5a', ops='#3a4a7a',
      title='Bonus ②: a hierarchy shrinks to its own logarithm ── c·t = const, That Clicks',
      ep='BONUS ② ／ dug after the main series closed',
      eyebrow='A 408-bit problem becomes 8.7 bits',
      h1='A hierarchy shrinks<br>to its own logarithm',
      sub='Dimensional transmutation is a compressor, and its gain is exactly the hierarchy.<br><em>Out of which comes a second criterion for whether a fine-tuning is a problem.</em>',
      byline_l='What you need: Episode 5\'s balance, Episode 32\'s cosmon, Episode 48\'s priors, bonus ①',
      byline_r='\\(B\\to\\log_2 B\\) — exact, no conventions',
      body=BODY + '\n\n<p class="foot">This document is bonus episode ② of "c·t = const, That Clicks", written after the main 50 episodes closed, for physics-minded high-school and university readers. The numbers are computed in kenshou/calc57.py. Dimensional transmutation, running couplings, the hierarchy problem and the cosmological constant problem are all standard material. <strong>Sections 01 to 03 are strong</strong>: \\(d\\ln\\Lambda/d\\ln\\alpha=H\\) follows directly from one-loop transmutation, and \\(B\\to\\log_2B\\) is a statement about <em>description length</em> — "the precision on \\(\\alpha\\) needed to fix a \\(B\\)-bit hierarchy to within one bit is \\(\\log_2B\\) bits" — with no approximation and no convention. <strong>§04\'s table is medium</strong>: whether an exponential map exists is objective, but the "how it is actually treated" column summarises the mood of the literature, with four cases and a selection that is mine. <strong>§05 and §06 are the weakest part</strong>: dividing \\(\\log_2B\\) by Episode 5\'s 5.37 bits per parameter assumes that a parameter\'s price (from \\(N=1701\\)) is the same currency as bits of description precision, and <strong>there is no guarantee that it is</strong> (the same weakness as Episode 48, caveat 2). §06\'s agreement rests on two cases and is <em>a recorded pattern, not a result</em>. <strong>"No exponential map" means "none found so far"</strong> — nobody has shown such a mechanism to be impossible, and the compression of 47 is precisely why people keep looking. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, enlarge the hierarchy and watch the red line refuse to rise. "Show the answer" opens each solution.')
