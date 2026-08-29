# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 5's balance measured two things: <strong>brevity</strong> (the price of a parameter) and <strong>fit</strong> (\(\Delta\chi^2\)). But physicists routinely invoke a third — "<em>it is beautiful</em>". This time we take it head-on: <strong>is beauty a third currency, or a restatement of the first two?</strong> And <em>we write down honestly what we could not measure.</em></p>

<h2><span class="n">01</span>Taking "beauty" apart</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Component</th><th class="mid">What it is</th><th class="mid">Which currency</th></tr></thead>
<tbody>
<tr><th>Symmetry</th><td class="mid">reduces the independent parameters</td><td class="mid">reduces to <strong>brevity</strong></td></tr>
<tr><th>Unification</th><td class="mid">reduces the number of inputs</td><td class="mid">reduces to <strong>brevity</strong></td></tr>
<tr><th>Rigidity (no other choice available)</th><td class="mid">reduces free choices</td><td class="mid">reduces to <strong>brevity</strong></td></tr>
<tr><th>Depth (hits what it was not built for)</th><td class="mid">fits data it was not fitted to</td><td class="mid">reduces to <strong>fit</strong></td></tr>
<tr class="hi"><th>Naturalness</th><td class="mid"><strong>a claim about the prior</strong></td><td class="mid"><strong>does not reduce</strong></td></tr>
<tr class="hi"><th>Sensory pleasure</th><td class="mid">how the equation feels to look at</td><td class="mid"><strong>not measurable</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>Four of the six reduce to the two existing currencies.</strong><br>
What remains is <em>naturalness</em> (measured in §03) and <em>sensory pleasure</em> (§06).</p>
</div>

<h2><span class="n">02</span>What does symmetry buy? — counting with the CKM matrix</h2>

<div class="calc">
<span class="tag">A 3×3 unitary matrix</span>
$$\underbrace{9}_{\text{independent parameters}}\;-\;\underbrace{5}_{\text{removed by rephasing}}\;=\;\underbrace{4}_{\text{3 angles + 1 phase}}$$
<p class="lbl">a compression of 2.25×, worth <strong>26.8 bits</strong> at Episode 5's price</p>
</div>

<p><strong>Symmetry is measurable as brevity.</strong> <em>There is no mystery here.</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>The core — "naturalness" was a claim about the prior</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">With a linear prior</th><th class="mid">With a log-uniform prior</th><th class="mid">Difference</th></tr></thead>
<tbody>
<tr><th>\(v/M_{\rm Planck}\) (the hierarchy problem)</th><td class="mid">\(55.5\) bit</td><td class="mid">\(6.3\) bit</td><td class="mid">\(49.1\)</td></tr>
<tr><th>\((v/M_{\rm Planck})^2\) (Higgs tuning)</th><td class="mid">\(110.9\) bit</td><td class="mid">\(6.3\) bit</td><td class="mid">\(104.6\)</td></tr>
<tr class="hi"><th>\(\rho_\Lambda/\rho_{\rm Planck}\) (Ep. 32)</th><td class="mid"><strong>\(408.4\) bit</strong></td><td class="mid"><strong>\(8.2\) bit</strong></td><td class="mid">\(400.2\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>The same number is either 55 bits surprising or 6 bits surprising.</strong><br>
Saying "that is unnatural" is the same as <em>declaring that the prior is linear</em> —<br>
exactly the place Episode 19 §01 flagged as "depends on how the prior range is drawn".<br>
── So: <strong>naturalness is not a third currency; it is a choice of prior.</strong></p>
</div>

<div class="fig">
<p class="cap">Figure: the surprise attached to the same small number under two priors. <strong>A linear prior turns orders of magnitude straight into bits; a log-uniform prior only takes the logarithm of the number of decades.</strong> Move the slider — <em>"unnaturalness" is decided by which ruler you apply.</em></p>
<canvas id="cv" width="720" height="360"></canvas>
<div class="controls">
  <label>smallness of the quantity, \(\log_{10}\)<input id="sx" type="range" min="-300" max="-1" value="-17" step="1"></label>
  <span class="val" id="vx">-17</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#7a3a4a"></i>linear prior ("unnatural")</span>
  <span><i class="swatch" style="background:#2a5a6a"></i>log-uniform prior ("ordinary")</span>
</div>
</div>

<h2><span class="n">04</span>But sometimes a linear prior is justified</h2>

<div class="calc">
<span class="tag">The strong CP problem</span>
$$\theta_{\rm QCD}<10^{-10}\qquad\text{(from the neutron electric dipole moment)}$$
<p class="lbl">\(\theta\) is an <strong>angle</strong>, so there is a reason for a uniform prior on \([0,2\pi)\)</p>
$$-\log_2\frac{10^{-10}}{2\pi}=\mathbf{35.9\ \text{bits}}$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0"><strong>This is a genuine fine-tuning</strong> — there is no escaping into a log-uniform prior.<br>
── When invoking "naturalness", ask <em>whether there is a reason for the prior</em>.<br>
<strong>An angle has a reason. A ratio of masses, so far, does not.</strong></p>
</div>

<h2><span class="n">05</span>Taking famous "beautiful theories" apart</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Theory</th><th class="mid">What the beauty consists of</th><th class="mid">Currency</th><th class="mid">Measurable?</th></tr></thead>
<tbody>
<tr class="hi"><th>General relativity</th><td class="mid">rigidity (nearly unique given the assumptions)</td><td class="mid">brevity</td><td class="mid"><strong>yes</strong></td></tr>
<tr class="hi"><th>The Dirac equation</th><td class="mid">it predicted the positron (unbuilt-for)</td><td class="mid">fit</td><td class="mid"><strong>yes</strong></td></tr>
<tr><th>The Standard Model</th><td class="mid">32 parameters</td><td class="mid">not brief</td><td class="mid">not called beautiful</td></tr>
<tr><th>Supersymmetry</th><td class="mid">solves the hierarchy problem (naturalness)</td><td class="mid">the prior</td><td class="mid">depends on the prior</td></tr>
<tr><th>String theory</th><td class="mid">a uniqueness claim → the landscape</td><td class="mid">the brevity claim collapsed</td><td class="mid">unsettled</td></tr>
</tbody>
</table>
</div>

<p><strong>The reasons a theory is called beautiful usually decompose into brevity or fit.</strong> <em>When they do not, suspect the prior.</em></p>

<h2><span class="n">06</span>What we could not measure</h2>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>Description length cannot measure it</strong><span>a short equation is not necessarily beautiful</span></div></div>
<div class="row"><div class="mk">✗</div><div class="txt"><strong>Fit cannot measure it</strong><span>an equation that works is not necessarily beautiful</span></div></div>
<div class="row hi"><div class="mk">!</div><div class="txt"><strong>Nor can the prior</strong><span>that is naturalness — <em>sensory pleasure lies outside this series' tools</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0"><strong>Written down honestly: this cannot be measured here.</strong><br>
── <em>Not measurable is not the same as not real.</em> It simply falls outside this series' currencies.<br>
And <strong>"do not use in a verdict what you cannot measure" has been the practice since Episode 3.</strong></p>
</div>

<h2><span class="n">07</span>Holding the series itself against this ruler</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Currency</th><th>For \(c\cdot t=\)const</th><th class="mid">Verdict</th></tr></thead>
<tbody>
<tr><th class="mid">brevity</th><td>one fewer parameter (Ep. 25)</td><td class="mid"><strong>it buys</strong></td></tr>
<tr class="hi"><th class="mid">fit</th><td>\(q\) and \(w\) miss by orders (Ep. 46)</td><td class="mid"><strong>it pays heavily</strong></td></tr>
<tr><th class="mid">naturalness</th><td>contains no unnatural numbers</td><td class="mid">a prior question — does not bite</td></tr>
<tr class="hi"><th class="mid">sensory pleasure</th><td>the appeal of the word "constant"</td><td class="mid"><strong>not measurable</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>It buys with brevity and pays heavily with fit</strong> — the verdict does not change. And <em>"the shape of it is pleasing" does not enter the verdict</em> — <strong>that was the procedure.</strong></p>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) §01's "six components" is this series' decomposition.</strong> Discussion of beauty in physics has a long history (Dirac, Weinberg, and more recently Hossenfelder's critical account), and <em>there is no settled way to divide it up</em> — the six here are <strong>a convenience, sorted by whether this tool can handle them</strong>.</p>
<p style="margin:0 0 10px"><strong>(2) The 80 decades behind §03's "6.3 bits log-uniform" are arbitrary.</strong> The value moves with where the prior range is drawn — <em>the point is the structure "linear versus log-uniform moves it by 50 bits"</em>, not the number 6.3 (the same caution as Episode 19 §01).</p>
<p style="margin:0 0 10px"><strong>(3) §04's "an angle justifies a linear prior" is not absolute either.</strong> Depending on how a high-energy theory generates \(\theta\), <em>non-uniform priors are arguable</em> (in axion models \(\theta\) relaxes dynamically) — read it as <strong>"a linear prior is easier to justify here"</strong>.</p>
<p style="margin:0 0 10px"><strong>(4) §05's assessments are summaries.</strong> "General relativity is nearly unique" is a statement in the sense of Lovelock's theorem and depends on the assumptions; "string theory's uniqueness claim collapsed" is a <em>point on which views differ depending on how one assesses the landscape</em> — this document endorses none of these theories.</p>
<p style="margin:0"><strong>(5) §06's "cannot be measured" is a statement about this series' tools.</strong> <em>It is not a claim that aesthetic judgement cannot be treated in any framework</em> — cognitive science and philosophy of science have their own approaches. All that is claimed here is that it is <strong>none of description length, fit, or prior</strong>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>How many of the six components of "beauty" reduce to the two existing currencies?
<details><summary>Show the answer</summary><div class="ans"><strong>Four</strong> — symmetry, unification and rigidity reduce to <em>brevity</em>; depth (hitting what it was not built for) reduces to <em>fit</em>. What remains is <strong>naturalness</strong> (a prior question) and <strong>sensory pleasure</strong> (not measurable).</div></details></li>

<li>How much does symmetry buy in the CKM matrix?
<details><summary>Show the answer</summary><div class="ans">Nine parameters of a 3×3 unitary matrix, minus five removed by rephasing, leaves <strong>four</strong> (3 angles + 1 phase) — worth <strong>26.8 bits</strong> at Episode 5's price. <em>Symmetry is measurable as brevity, and there is no mystery here.</em></div></details></li>

<li>How surprising is \(\rho_\Lambda/\rho_{\rm Planck}=1.13\times10^{-123}\)?
<details><summary>Show the answer</summary><div class="ans"><strong>It depends on the prior</strong> — <strong>408.4 bits</strong> under a linear prior (Episode 32's number), <strong>8.2 bits</strong> under a log-uniform one over 300 decades. A difference of 400 bits. <em>Saying "that is unnatural" is the same as declaring a linear prior.</em></div></details></li>

<li>Why is the strong CP problem different from the two in §03?
<details><summary>Show the answer</summary><div class="ans">Because \(\theta\) is an <strong>angle</strong> — a uniform prior on \([0,2\pi)\) has a reason, and <em>there is no escaping into a log-uniform prior</em>. So <strong>35.9 bits</strong> is a genuine fine-tuning. <em>When invoking naturalness, ask whether there is a reason for the prior.</em></div></details></li>

<li>(Harder) What could this series' tools not measure?
<details><summary>Show the answer</summary><div class="ans"><strong>Sensory pleasure</strong> — not description length, not fit, not the prior. <em>Not measurable is not the same as not real</em>, but it falls outside these currencies — and <strong>"do not use in a verdict what you cannot measure" has been the practice since Episode 3.</strong></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: beauty was not a third currency</h2>
<p>Taking "beauty" apart into six components, <strong>four reduce to the two existing currencies</strong> — symmetry, unification and rigidity to <em>brevity</em>, depth to <em>fit</em>. And what symmetry buys can actually be counted: the CKM matrix's nine parameters become four under rephasing, <strong>a saving of 26.8 bits</strong>.</p>
<p>What remained was <strong>naturalness</strong> — and it turned out not to be a third currency but <em>a choice of prior</em>. \(v/M_P=2\times10^{-17}\) is 55.5 bits surprising under a linear prior and 6.3 under a log-uniform one; \(\rho_\Lambda/\rho_{\rm Planck}\) is <strong>408.4 bits versus 8.2</strong>, a difference of 400. <strong>Saying "that is unnatural" is the same as declaring the prior to be linear</strong> — exactly the place Episode 19 §01 flagged from the start.</p>
<p>But <em>a linear prior is sometimes justified</em> — the strong CP problem's \(\theta_{\rm QCD}<10^{-10}\) concerns an <strong>angle</strong>, so a uniform prior on \([0,2\pi)\) has a reason and there is no escape. <strong>35.9 bits, a genuine fine-tuning.</strong> <em>When invoking naturalness, ask whether there is a reason for the prior</em> — an angle has one; a ratio of masses, so far, does not.</p>
<p>And there was something <strong>we could not measure</strong> — <em>sensory pleasure</em>. Not description length, not fit, not the prior. <strong>Written down honestly: this cannot be measured here.</strong> Not measurable is not the same as not real, but it falls outside these currencies — and <em>"do not use in a verdict what you cannot measure" has been the practice since Episode 3.</em></p>
<p>Finally we held the series against its own ruler. \(c\cdot t=\)const <strong>buys with brevity and pays heavily with fit</strong> — the verdict does not change. The pleasing shape of the word "constant" <em>does not enter the verdict.</em></p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 49</span>
Two episodes remain. Next time: <strong>the doors left open</strong> — every question opened in 48 episodes and <em>not closed</em>. What Part II deferred, what Part IV called unresolved, what Part V called unsettled, and what this episode called unmeasurable. <strong>We write down the things we could not answer, as things we could not answer.</strong> ── <em>Because that is the most honest thing this series can do at the end.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sx=document.getElementById('sx'), vx=document.getElementById('vx'), ro=document.getElementById('ro');
  var X0=76, X1=690, Y0=34, Y1=272;
  var A0=-300, A1=0, B1=1000;

  function px(v){ return X0+(v-A0)/(A1-A0)*(X1-X0); }
  function py(b){ return Y1-b/B1*(Y1-Y0); }
  function lin(v){ return -v*Math.LN10/Math.LN2; }
  function logu(v){ return Math.log(Math.abs(v)+20)/Math.LN2; }

  function draw(){
    var v=parseInt(sx.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var b=0;b<=B1;b+=200){
      g.strokeStyle='#f2f0f4'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(b)); g.lineTo(X1,py(b)); g.stroke();
      g.fillText(b+' bit', X0-8, py(b)+4);
    }
    g.textAlign='center';
    for(var t=A0;t<=A1;t+=50){ g.fillStyle='#9c96a4'; g.fillText('10^'+t, px(t), Y1+20); }

    g.strokeStyle='#7a3a4a'; g.lineWidth=2.8; g.beginPath();
    for(var i=0;i<=200;i++){ var x=A0+(A1-A0)*i/200; if(i===0)g.moveTo(px(x),py(lin(x))); else g.lineTo(px(x),py(lin(x))); }
    g.stroke();
    g.strokeStyle='#2a5a6a'; g.lineWidth=2.8; g.beginPath();
    for(var j=0;j<=200;j++){ var x2=A0+(A1-A0)*j/200; if(j===0)g.moveTo(px(x2),py(logu(x2))); else g.lineTo(px(x2),py(logu(x2))); }
    g.stroke();

    g.textAlign='left';
    g.fillStyle='#7a3a4a'; g.fillText('linear prior: orders become bits', px(-230), py(lin(-230))-12);
    g.fillStyle='#2a5a6a'; g.fillText('log-uniform prior: only the log of the decade count', px(-230), py(logu(-230))-12);

    var Xc=px(v);
    g.strokeStyle='#5a5262'; g.lineWidth=1.6; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(Xc,Y0); g.lineTo(Xc,Y1); g.stroke(); g.setLineDash([]);
    g.fillStyle='#7a3a4a'; g.beginPath(); g.arc(Xc,py(Math.min(lin(v),B1)),4.8,0,6.29); g.fill();
    g.fillStyle='#2a5a6a'; g.beginPath(); g.arc(Xc,py(logu(v)),4.8,0,6.29); g.fill();

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('smallness of the quantity (power of ten)', (X0+X1)/2, Y1+44);

    vx.textContent=String(v);
    var tag='';
    if(v===-17) tag='　★ v/M_Planck (the hierarchy problem)';
    if(v===-123) tag='　★ rho_Lambda/rho_Planck (the cosmological constant problem)';
    ro.textContent='10^'+v+'　→　linear prior '+lin(v).toFixed(1)+' bits　/　log-uniform '+
      logu(v).toFixed(1)+' bits　/　difference '+(lin(v)-logu(v)).toFixed(1)+' bits'+tag;
  }
  sx.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-48-beauty.html', acc='#7a3a4a', ops='#2a5a6a',
      title='Brevity, fit and beauty ── c·t = const, That Clicks, Episode 48 (Part VI)',
      ep='EPISODE 48 ／ Part VI — examining the procedure',
      eyebrow='"That is unnatural" was a declaration about the prior',
      h1='Beauty was not<br>a third currency',
      sub='Take it apart into six components and four reduce to brevity and fit.<br><em>What remained was a choice of prior — and one thing we could not measure.</em>',
      byline_l='What you need: Episode 5\'s balance, Episode 19\'s scale, Episode 32, Episode 47\'s map',
      byline_r='The same number is either 408 bits or 8',
      body=BODY + '\n\n<p class="foot">This document is Episode 48 of "c·t = const, That Clicks" (the third of Part VI), written for physics-minded high-school and university readers. Minimum description length, the relation between naturalness and priors, and the strong CP problem are all standard, and nothing here is a new claim — the numbers are computed in kenshou/calc52.py. <strong>§01\'s "six components" is this series\' decomposition</strong>; discussion of beauty in physics has a long history (Dirac, Weinberg, and more recently Hossenfelder\'s critical account) and <em>there is no settled way to divide it up</em> — these six are a convenience, sorted by what this tool can handle. <strong>The 80 decades behind §03\'s log-uniform figure are arbitrary</strong> and the value moves with the prior range — <em>the point is that linear versus log-uniform moves it by 50 bits</em>, not the number itself. <strong>§04\'s "an angle justifies a linear prior" is not absolute</strong>: depending on how a high-energy theory generates \\(\\theta\\), non-uniform priors are arguable (in axion models \\(\\theta\\) relaxes dynamically). <strong>§05\'s assessments are summaries</strong> — "general relativity is nearly unique" is meant in the sense of Lovelock\'s theorem and depends on the assumptions, and how one assesses the string landscape is a matter on which views differ; this document endorses none of these theories. <strong>§06\'s "cannot be measured" is a statement about this series\' tools</strong>, not a claim that aesthetic judgement is beyond every framework. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the smallness and watch the two rulers diverge. "Show the answer" opens each solution.')
