# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Bonus ④ collapsed surprise, naturalness and numerical coincidence onto one question: <strong>is there a canonical measure?</strong> Bonus ③ answered "compact gives Haar, non-compact gives nothing" — but <em>that was too coarse</em>. <strong>Something besides group symmetry hands out measures.</strong> And following it, the three great fine-tuning problems come out <em>with zero false positives.</em></p>

<h2><span class="n">01</span>The renormalisation group hands out the measure</h2>

<div class="calc">
<span class="tag">For a one-dimensional flow \(dg/dt=\beta(g)\), the measure invariant under the flow</span>
$$\frac{d}{dt}\int\rho\,dg=0
\iff \frac{d(\rho\beta)}{dg}=0
\iff \rho\beta=\text{const}
\iff \boxed{\rho\propto\frac1\beta}$$
<p class="lbl"><strong>unique</strong> up to normalisation — and \(\int dg/\beta\) is <strong>RG time</strong> itself</p>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>"The prior probability = the RG time the theory spends near that value."</strong><br>
── This is not a choice. <em>The invariant measure of a flow is unique.</em></p>
</div>

<h2><span class="n">02</span>Why must the prior be RG-invariant?</h2>

<div class="seven">
<div class="row"><div class="mk">?</div><div class="txt"><strong>A parameter's value depends on the scale you quote it at</strong><span>Episode 37 — \(\alpha\) is 128 at \(M_Z\) and 137 at low energy</span></div></div>
<div class="row"><div class="mk">!</div><div class="txt"><strong>If the verdict changed with the scale, it would depend on a convention</strong><span>Episode 3: <em>an answer that changes with a convention is not an answer</em></span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>So the prior must be RG-invariant — and by §01 that fixes it uniquely</strong><span>the reading was <em>derived</em>, not assumed</span></div></div>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Scale</th><th class="mid">\(\alpha_s\)</th><th class="mid">"unnaturalness" under a uniform prior</th></tr></thead>
<tbody>
<tr><th>around 1 GeV</th><td class="mid">\(0.500\)</td><td class="mid">\(1.00\) bit</td></tr>
<tr><th>around \(m_b\)</th><td class="mid">\(0.214\)</td><td class="mid">\(2.22\) bit</td></tr>
<tr><th>\(M_Z\)</th><td class="mid">\(0.118\)</td><td class="mid">\(3.08\) bit</td></tr>
<tr class="hi"><th>\(M_{\rm Planck}\) (one-loop)</th><td class="mid">\(0.0191\)</td><td class="mid"><strong>\(5.71\) bit</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>The same coupling of the same theory moves by 4.71 bits just by changing the scale.</strong> <em>A uniform prior is not RG-invariant — so it cannot serve as a verdict.</em></p>

<h2><span class="n">03</span>The shape of the measure is fixed by the shape of \(\beta\)</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Shape of \(\beta\)</th><th class="mid">\(dg/\beta\)</th><th class="mid">Induced measure</th><th class="mid">Price</th></tr></thead>
<tbody>
<tr><th class="mid">\(\beta=0\)</th><td class="mid">degenerate</td><td class="mid">fall back to the group (Haar)</td><td class="mid">depends</td></tr>
<tr class="hi"><th class="mid">\(\beta\propto g\) (multiplicative)</th><td class="mid">\(dg/g\)</td><td class="mid"><strong>log-uniform</strong></td><td class="mid"><strong>cheap</strong></td></tr>
<tr><th class="mid">\(\beta\propto g^2\)</th><td class="mid">\(dg/g^2\)</td><td class="mid">\(1/g^2\) weighting</td><td class="mid">cheap</td></tr>
<tr class="hi"><th class="mid">\(\beta=\)const (additive)</th><td class="mid">\(dg\)</td><td class="mid"><strong>linear</strong></td><td class="mid"><strong>expensive</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §03</p>
<p style="margin:6px 0 0">And <strong>\(\beta\propto g\) happens exactly when \(g=0\) has enhanced symmetry</strong> —<br>
with a symmetry at \(g=0\), \(g\) can only be generated in proportion to itself; without one, other masses generate it additively.<br>
── <em>This is 't Hooft's naturalness criterion itself.</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The core — scoring all 20 Standard Model parameters by the shape of \(\beta\)</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Parameter</th><th class="mid">Count</th><th class="mid">Shape of \(\beta\)</th><th class="mid">Protecting symmetry</th><th class="mid">Price</th><th class="mid">How it is treated</th></tr></thead>
<tbody>
<tr><th>Gauge couplings \(g_1,g_2,g_3\)</th><td class="mid">3</td><td class="mid">\(\propto g^3\) (multiplicative)</td><td class="mid">gauge symmetry</td><td class="mid">cheap</td><td class="mid">not a problem</td></tr>
<tr><th>Yukawa couplings</th><td class="mid">9</td><td class="mid">\(\propto y\) (multiplicative)</td><td class="mid"><strong>chiral symmetry</strong></td><td class="mid">cheap</td><td class="mid">'t Hooft's own example</td></tr>
<tr><th>CKM: 3 angles + 1 phase</th><td class="mid">4</td><td class="mid">multiplicative, compact</td><td class="mid">compactness</td><td class="mid">cheap</td><td class="mid">only \(\theta_{13}\) at 8.8 bits</td></tr>
<tr><th>Higgs quartic \(\lambda\)</th><td class="mid">1</td><td class="mid">\(\supset-6y_t^4\) (<strong>additive</strong>)</td><td class="mid">none</td><td class="mid"><strong>flagged</strong></td><td class="mid">→ vacuum metastability</td></tr>
<tr class="hi"><th>Higgs mass\(^2\) \(m^2\)</th><td class="mid">1</td><td class="mid">\(\supset M^2\) (if new physics)</td><td class="mid">none</td><td class="mid"><strong>expensive</strong></td><td class="mid"><strong>the hierarchy problem</strong></td></tr>
<tr class="hi"><th>\(\theta_{\rm QCD}\)</th><td class="mid">1</td><td class="mid">\(\beta=0\)</td><td class="mid">compactness only</td><td class="mid"><strong>expensive</strong></td><td class="mid"><strong>the strong CP problem</strong></td></tr>
<tr class="hi"><th>Cosmological constant \(\Lambda\)</th><td class="mid">1</td><td class="mid">\(\supset m^4\) (<strong>additive</strong>)</td><td class="mid">none</td><td class="mid"><strong>expensive</strong></td><td class="mid"><strong>the CC problem</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>Scoring by the shape of \(\beta\) alone, exactly 3 come out "expensive".</strong><br>
They are <strong>the hierarchy, strong CP and the cosmological constant</strong> — <em>the three known fine-tuning problems.</em><br>
── <strong>Twenty cases, three hits, zero false positives and zero false negatives.</strong><br>
And \(\lambda\) being "flagged" is not a miss — <em>it correctly catches vacuum metastability, a problem of a different kind.</em></p>
</div>

<div class="fig">
<p class="cap">Figure: the 20 parameters sorted by the shape of \(\beta\). <strong>Left is multiplicative (log measure, cheap); right is additive or zero (linear or Haar, expensive).</strong> Move the slider for where you put new physics — <em>only the Higgs mass jumps from left to right the moment you place it.</em></p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>scale of new physics, \(\log_{10}(M/\text{GeV})\)<input id="sn" type="range" min="3" max="19" value="19" step="1"></label>
  <span class="val" id="vn">19</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a4a"></i>multiplicative (log measure) — cheap</span>
  <span><i class="swatch" style="background:#8a3a3a"></i>additive or \(\beta=0\) — expensive</span>
</div>
</div>

<h2><span class="n">05</span>The remaining freedom turns into a question of physics</h2>

<div class="seven">
<div class="row"><div class="mk">?</div><div class="txt"><strong>\(\int dg/\beta\) diverges at a fixed point</strong><span>\(\beta\to0\), so a range must still be cut</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>But that cut is not arbitrary</strong><span>it is <em>"how far does the theory remain valid?"</em> — where new physics enters</span></div></div>
<div class="row"><div class="mk">→</div><div class="txt"><strong>And that is exactly what decides whether the hierarchy problem exists</strong><span>the \(m^2\) row of §04 — <em>the only freedom left in the prior coincided with a question of physics</em></span></div></div>
</div>

<h2><span class="n">06</span>The seventh and eighth compressions</h2>

<div class="calc">
<span class="tag">Seventh</span>
$$\underbrace{\text{Ep.48 "is there a reason for the prior?"}}_{\text{criterion}}
=\underbrace{\text{bonus ③ "is it compact?"}}_{\text{theorem}}
=\underbrace{\text{"is }\beta\text{ multiplicative?"}=\text{"is }g=0\text{ a symmetry point?"}}_{\textbf{mechanism}}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>The three faces of \(\theta_{\rm QCD}\)</th><th class="mid">Consequence</th></tr></thead>
<tbody>
<tr><th>\(\beta=0\), so it does not run</th><td class="mid">the RG cannot hand out a measure</td></tr>
<tr><th>Not running, it is RG-invariant</th><td class="mid">the only constant among independent inputs (bonus ③)</td></tr>
<tr class="hi"><th>Being an angle, it is compact</th><td class="mid">only the Haar measure is available</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §06 — the eighth compression</p>
<p style="margin:6px 0 0"><strong>The three are not independent facts but three faces of \(\beta=0\).</strong><br>
── And its being "the one uncontested fine-tuning problem" follows from the same single reason.</p>
</div>

<h2><span class="n">07</span>Closing two of my own escape routes</h2>

<div class="seven">
<div class="row"><div class="mk">③</div><div class="txt"><strong>Correcting bonus ③: non-compact spaces do get a measure, from the RG</strong><span>a measure is missing only when \(\beta=0\) <em>and</em> non-compact, and <em>the Standard Model has no such case</em> — <strong>naturalness is more well-posed than I said</strong></span></div></div>
<div class="row hi"><div class="mk">48</div><div class="txt"><strong>Correcting Episode 48: \(\rho_\Lambda\)'s \(\beta\) has \(m^4\) additively</strong><span>so <em>the canonical measure is linear</em>, not log-uniform — <strong>408 bits is the right answer, and the cosmological constant problem has no escape</strong></span></div></div>
<div class="row"><div class="mk">!</div><div class="txt"><strong>"It moves 400 bits with the prior" came from not knowing the canonical measure</strong><span>── <em>I closed an escape route I had built myself</em></span></div></div>
</div>

<div class="aside">
<span class="tag">Is bonus ② safe? — a robustness check</span>
The value of \(\log_2B\): <strong>8.67 under a uniform measure, 8.66 under the RG measure</strong> — <em>a difference of 0.01 bits</em>.<br>
(Only log-uniform differs, at 11.46 — still the same order.) <strong>The compression law does not depend on the choice of measure.</strong>
</div>

<h2><span class="n">08</span>What can now be said that could not before</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Model</th><th class="mid">What to look at</th><th class="mid">Consequence</th></tr></thead>
<tbody>
<tr><th>Adding a new scalar</th><td class="mid">does its mass \(\beta\) gain an additive term?</td><td class="mid">if so, it creates a new hierarchy problem</td></tr>
<tr class="hi"><th>Supersymmetry</th><td class="mid">boson–fermion cancellation removes the additive term</td><td class="mid"><strong>which is why it solves the hierarchy problem</strong></td></tr>
<tr><th>The axion</th><td class="mid">gives \(\theta\) a \(\beta\) and makes it move</td><td class="mid">solves it by breaking the \(\beta=0\) degeneracy</td></tr>
<tr class="hi"><th>Any CC mechanism</th><td class="mid">how to remove the additive \(m^4\)</td><td class="mid"><strong>nobody has managed it</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §08</p>
<p style="margin:6px 0 0"><strong>Supersymmetry "solving" the hierarchy problem means removing the additive term in \(\beta\) and turning a linear measure back into a logarithmic one</strong> (408 → about 7 bits).<br>
── <em>Write down a model's \(\beta\) and you know on the spot whether it has a fine-tuning problem.</em></p>
</div>

<div class="caveat">
<span class="tag">The honest line — and the hole that is not filled</span>
<p style="margin:0 0 10px"><strong>(1) §01's uniqueness holds only for a one-dimensional flow.</strong> In several dimensions the invariant measure is not unique (many \(\rho\) satisfy \(\nabla\!\cdot\!(\rho\beta)=0\)) — gauge couplings run independently at one loop so the 1-D argument applies to them, but <em>not to all parameters</em>. This is the most technical weakness here.</p>
<p style="margin:0 0 10px"><strong>(2) \(\beta\) is scheme-dependent</strong> (the same weakness as Episode 35's account of asymptotic safety). <em>Whether it is multiplicative or additive is scheme-independent; the coefficients are not.</em></p>
<p style="margin:0 0 10px"><strong>(3) §07's "linear is canonical for \(\rho_\Lambda\)" is not settled physics.</strong> In dimensional regularisation the \(m^4\) terms appear differently, and <em>it depends on the renormalisation conditions</em> — doubt this and you return to Episode 48's "it cannot be decided".</p>
<p style="margin:0 0 10px"><strong>(4) §04's table restates 't Hooft naturalness in the language of measures.</strong> <em>The physics is known</em>; what is new is only the reading that it closes as a question about priors — and twenty cases is a small sample, with "the three great problems" itself a convention of the literature.</p>
<p style="margin:0"><strong>(5) And the biggest hole.</strong> §02 establishes that the prior must be RG-invariant. But — <em><strong>having a measure and that measure being a probability are two different things</strong></em>. Reading "values where more RG time is spent are more likely" is natural but <strong>not proved</strong>. That hole is not filled. The same requirement does yield the Jeffreys prior in statistics, so it is not an isolated position — but <em>it is still a position</em>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>Why must the prior be RG-invariant?
<details><summary>Show the answer</summary><div class="ans"><strong>Otherwise the verdict changes with the scale.</strong> Under a uniform prior, \(\alpha_s\) reads 1.00 bits at 1 GeV and 5.71 at \(M_{\rm P}\) — <em>the same coupling moving by 4.71 bits</em>. Episode 3: <strong>an answer that changes with a convention is not an answer.</strong></div></details></li>

<li>How many RG-invariant measures are there?
<details><summary>Show the answer</summary><div class="ans">For a one-dimensional flow, <strong>exactly one</strong>: \(\rho\beta=\)const, i.e. \(\rho\propto1/\beta\), which is \(\int dg/\beta=\) <em>RG time</em>. ── But per caveat (1), <strong>in several dimensions it is not unique.</strong></div></details></li>

<li>How does the shape of \(\beta\) map to the price?
<details><summary>Show the answer</summary><div class="ans"><strong>\(\beta\propto g\) (multiplicative) → log measure → cheap. \(\beta=\)const (additive) → linear measure → expensive. \(\beta=0\) → back to the group.</strong> And \(\beta\propto g\) happens exactly when <em>\(g=0\) has enhanced symmetry</em> — <strong>'t Hooft's criterion.</strong></div></details></li>

<li>Scoring the 20, how many come out "expensive"?
<details><summary>Show the answer</summary><div class="ans"><strong>Three</strong> — \(m^2\) (with new physics), \(\theta_{\rm QCD}\) and \(\Lambda\). They are <em>the hierarchy, strong CP and the cosmological constant</em>: the three known problems, with <strong>zero false positives and zero false negatives</strong>. \(\lambda\)'s "flagged" correctly catches vacuum metastability.</div></details></li>

<li>(Harder) What is the biggest unfilled hole here?
<details><summary>Show the answer</summary><div class="ans"><strong>That having a measure and that measure being a probability are different things.</strong> RG-invariance fixes the measure uniquely, but <em>the reading "values where more RG time is spent are more likely" is not proved</em>. If that fails, everything from §04 onward fails with it.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: the prior was never ours to choose</h2>
<p>For a one-dimensional flow \(dg/dt=\beta(g)\), the invariant measure is <strong>\(\rho\propto1/\beta\), and it is unique</strong> — it is <strong>RG time</strong>. And <em>why</em> it must be RG-invariant can be said too: <strong>a verdict that changes with the scale depends on a convention, and is therefore not a verdict</strong> (Episode 3). Under a uniform prior, \(\alpha_s\)'s "unnaturalness" moves by <strong>4.71 bits</strong>.</p>
<p>The shape of the measure follows from the shape of \(\beta\) alone — <strong>multiplicative gives a log measure and is cheap; additive gives a linear one and is expensive</strong>. And \(\beta\propto g\) happens exactly when \(g=0\) carries a symmetry: <em>'t Hooft's criterion itself.</em></p>
<p>Scoring <strong>all 20 Standard Model parameters by the shape of \(\beta\)</strong>, only <strong>three</strong> come out expensive — <em>the hierarchy, strong CP and the cosmological constant</em>, the three known problems, with <strong>zero false positives and zero false negatives</strong>. \(\lambda\)'s flag is not a miss either: it correctly catches vacuum metastability.</p>
<p>Even the remaining freedom — the range of integration — was not arbitrary. It is <strong>"how far does the theory remain valid?"</strong>, i.e. where new physics enters, <em>which is precisely what decides whether the hierarchy problem exists</em>. <strong>The one freedom left in the prior coincided with a question of physics.</strong></p>
<p>And two of my own escape routes closed. Bonus ③'s "non-compact means ill-posed" was too coarse — <strong>naturalness is more well-posed than I said</strong>. Episode 48's "it moves 400 bits with the prior" too — <strong>\(\rho_\Lambda\)'s \(\beta\) is additive, so the canonical measure is linear, 408 bits is the right answer, and the cosmological constant problem has no escape.</strong></p>
<p>But — <em>having a measure and that measure being a probability are two different things.</em> That hole is still open.</p>
</div>

<div class="next">
<span class="lbl">In closing — what the five bonus episodes found</span>
①: <strong>whether the mass variation is universal can be measured</strong> (\(\mu\), 23.3 bits) + a 10.2-bit degeneracy in the quark-mass direction.<br>
②: <strong>a hierarchy shrinks to its own logarithm</strong> (\(B\to\log_2B\); robustness confirmed in ⑤).<br>
③: <strong>the zero column is not homogeneous, and almost no constants survive</strong> (only \(\theta_{\rm QCD}\) remains).<br>
④: <strong>a 4.1-bit prediction beats a 15.7-bit discovery</strong> — "theory first" means fixing the measure first.<br>
⑤: <strong>and that measure was being handed out by the renormalisation group</strong> — the shape of \(\beta\) alone hits the three great problems.<br>
── All five stand on the single procedure of Episode 3. And in ③ and ⑤ that procedure <em>deleted two of the criteria this series had built and closed two of its escape routes.</em> <strong>The tool is still working.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sn=document.getElementById('sn'), vn=document.getElementById('vn'), ro=document.getElementById('ro');
  var X0=60, X1=690, Y0=48, MID=375;

  var LEFT=[['Gauge couplings (3)',3],['Yukawa couplings (9)',9],['CKM: 3 angles + 1 phase',4]];
  var RIGHT=[['lambda (flagged)',1],['theta_QCD',1],['Cosmological constant',1]];

  function draw(){
    var M=parseInt(sn.value,10);
    var higgsRight = (M < 19);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.strokeStyle='#cdc8d2'; g.lineWidth=1.6;
    g.beginPath(); g.moveTo(MID,Y0-20); g.lineTo(MID,300); g.stroke();
    g.textAlign='center';
    g.font='13px ui-sans-serif,system-ui,sans-serif';
    g.fillStyle='#2a5a4a'; g.fillText('multiplicative → log measure → cheap', (X0+MID)/2, Y0-26);
    g.fillStyle='#8a3a3a'; g.fillText('additive or beta = 0 → expensive', (MID+X1)/2, Y0-26);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    var y=Y0+6;
    for(var i=0;i<LEFT.length;i++){
      g.fillStyle='#2a5a4a'; g.globalAlpha=0.88;
      g.fillRect(X0+16, y, MID-X0-40, 30); g.globalAlpha=1;
      g.fillStyle='#fff'; g.textAlign='left';
      g.fillText(LEFT[i][0], X0+26, y+19);
      y+=38;
    }
    var hx = higgsRight ? MID+16 : X0+16;
    var hw = higgsRight ? (X1-MID-40) : (MID-X0-40);
    g.fillStyle = higgsRight ? '#8a3a3a' : '#2a5a4a';
    g.globalAlpha=0.95; g.fillRect(hx, y, hw, 30); g.globalAlpha=1;
    g.fillStyle='#fff'; g.textAlign='left';
    g.fillText('Higgs mass^2 (1)'+(higgsRight?'　← new physics made it additive':''), hx+10, y+19);
    g.strokeStyle='#5a5262'; g.lineWidth=1.4; g.setLineDash([3,3]);
    g.beginPath(); g.moveTo(X0+16, y+15); g.lineTo(X1-16, y+15); g.stroke(); g.setLineDash([]);

    var y2=Y0+6;
    for(var j=0;j<RIGHT.length;j++){
      g.fillStyle='#8a3a3a'; g.globalAlpha=0.88;
      g.fillRect(MID+16, y2, X1-MID-40, 30); g.globalAlpha=1;
      g.fillStyle='#fff'; g.textAlign='left';
      g.fillText(RIGHT[j][0], MID+26, y2+19);
      y2+=38;
    }

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('the 20 Standard Model parameters, sorted by the shape of beta', (X0+X1)/2, 316);

    vn.textContent=String(M);
    var n_high = 2 + (higgsRight?1:0);
    ro.textContent='new physics at 10^'+M+' GeV　→　'+n_high+' parameters are "expensive"'+
      (higgsRight
        ? '　★ hierarchy, strong CP and the cosmological constant — the three known problems, zero false positives'
        : '　★ with no new physics the Higgs mass stays on the left — the pure Standard Model has no hierarchy problem');
  }
  sn.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-b5-measure.html', acc='#2a5a4a', ops='#8a3a3a',
      title='Bonus ⑤: the prior was never ours to choose ── c·t = const, That Clicks',
      ep='BONUS ⑤ ／ dug after the main series closed',
      eyebrow='The shape of beta alone hits all three problems, with zero false positives',
      h1='The prior was never<br>ours to choose',
      sub='The renormalisation group hands out the measure — and for a flow it is unique.<br><em>And I ended up closing two escape routes I had built myself.</em>',
      byline_l='What you need: Episode 3\'s procedure, Episode 35 on schemes, Episode 37 on running, Episode 48\'s priors, bonuses ②③④',
      byline_r='Twenty cases, three hits, no false positives',
      body=BODY + '\n\n<p class="foot">This document is bonus episode ⑤ of "c·t = const, That Clicks", written after the main 50 episodes closed, for physics-minded high-school and university readers. The numbers are computed in kenshou/calc63.py and calc64.py. The renormalisation group, invariant measures of flows, \'t Hooft naturalness and vacuum metastability are all standard material, and <strong>§04\'s table restates \'t Hooft naturalness in the language of measures</strong> — <em>the physics is known</em>; what is new is only the reading that it closes as a question about priors. <strong>§01\'s uniqueness holds only for a one-dimensional flow</strong>; in several dimensions the invariant measure is not unique (gauge couplings run independently at one loop, so the argument applies to them, but not to all parameters) — this is the most technical weakness here. <strong>\\(\\beta\\) is scheme-dependent</strong>: whether it is multiplicative or additive is not, but the coefficients are. <strong>§07\'s "linear is canonical for \\(\\rho_\\Lambda\\)" is not settled physics</strong> — in dimensional regularisation the \\(m^4\\) terms appear differently and it depends on the renormalisation conditions; doubt it and you return to Episode 48\'s "it cannot be decided". Twenty cases is a small sample and "the three great problems" is itself a convention of the literature. <strong>And the biggest hole</strong>: RG-invariance fixes the measure uniquely, but <em>having a measure and that measure being a probability are two different things</em>, and the reading "values where more RG time is spent are more likely" is <strong>not proved</strong> (the same requirement yields the Jeffreys prior in statistics, so it is not isolated — but it is still a position). ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the scale of new physics and watch the Higgs mass change sides. "Show the answer" opens each solution.')
