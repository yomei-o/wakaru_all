# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">This series has sorted "coincidences" again and again — Dirac's large numbers were an <em>identity</em>, being exactly at the Landauer limit an <em>identity</em>, \(\alpha+2\beta+\gamma=2\) an <em>identity</em>. Last episode's 1.96 fm was a <em>coincidence</em>. And \(\Omega/N=\ln2/3\pi^2(1+w)\) was <em>physics</em>. <strong>But is that sorting actually a procedure?</strong> Today we build it head on. The answer was on the information-theory side — <em>measure the surprise in bits.</em></p>

<h2><span class="n">01</span>What we have sorted so far</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Coincidence</th><th class="mid">From</th><th class="mid">Verdict given</th></tr></thead>
<tbody>
<tr><th>\(M/m_P=R_H/2\ell_P\) (Dirac's large numbers)</th><td class="mid">prev. Extra 3</td><td class="mid">identity</td></tr>
<tr><th>\(E/N=k_BT_H\ln2\) (Landauer)</th><td class="mid">Episode 10</td><td class="mid">identity</td></tr>
<tr><th>\(\alpha+2\beta+\gamma=2\) (critical exponents)</th><td class="mid">Episode 14</td><td class="mid">identity</td></tr>
<tr><th>\(\rho_\Lambda^{1/4}\) and \(m_\nu\) within a factor 22</th><td class="mid">prev. Extra 5</td><td class="mid">coincidence</td></tr>
<tr><th>Side of a bit's volume ≈ a nucleon</th><td class="mid">Episode 18</td><td class="mid">coincidence</td></tr>
<tr><th>Koide's relation \(Q=2/3\)</th><td class="mid">prev. Extra 4</td><td class="mid">unexplained empirical formula</td></tr>
<tr class="hi"><th>\(\Omega/N=\ln2/3\pi^2(1+w)\)</th><td class="mid">Episode 1</td><td class="mid"><strong>physics</strong></td></tr>
</tbody>
</table>
</div>

<p>Each verdict looked plausible, but <strong>the criterion was never stated</strong>. Today we state it.</p>

<h2><span class="n">02</span>Measuring surprise in bits</h2>

<p>How surprising a coincidence is can be measured as: <em>how narrow a place did it land in, out of the range that was allowed beforehand?</em></p>

<div class="calc">
<span class="tag">Definition</span>
$$\text{surprise}=-\log_2\frac{\text{width it landed in}}{\text{range allowed beforehand}}\ \ [\text{bits}]$$
<p class="lbl">meaning</p>
$$1\ \text{bit}=\text{one coin flip},\qquad 20\ \text{bits}=\text{one in a million}$$
</div>

<p>This is exactly information theory's surprisal. And by this definition an identity comes out at precisely <strong>0 bits</strong> — <em>because, following from a definition, there was only ever one place for it to land</em>.</p>

<h2><span class="n">03</span>Actually measuring</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Coincidence</th><th class="mid">Surprise</th><th class="mid">Feel</th><th class="mid">Class</th></tr></thead>
<tbody>
<tr><th>Dirac's large numbers</th><td class="mid"><strong>0 bit</strong></td><td class="mid">──</td><td class="mid">identity</td></tr>
<tr><th>Exactly at the Landauer limit</th><td class="mid"><strong>0 bit</strong></td><td class="mid">──</td><td class="mid">identity</td></tr>
<tr><th>\(\alpha+2\beta+\gamma=2\)</th><td class="mid"><strong>0 bit</strong></td><td class="mid">──</td><td class="mid">identity</td></tr>
<tr><th>\(\rho_\Lambda^{1/4}\) and \(m_\nu\)</th><td class="mid">4.7 bit</td><td class="mid">5 coin flips</td><td class="mid">coincidence</td></tr>
<tr><th>A bit's volume ≈ a nucleon</th><td class="mid">7.4 bit</td><td class="mid">7 coin flips</td><td class="mid">coincidence</td></tr>
<tr class="hi"><th>Koide's relation \(Q=2/3\)</th><td class="mid"><strong>15.7 bit</strong></td><td class="mid">one in 30,000</td><td class="mid">empirical formula</td></tr>
<tr class="hi"><th>CMB uniform across 9,600 patches</th><td class="mid"><strong>\(1.6\times10^{5}\) bit</strong></td><td class="mid">another world</td><td class="mid">a real problem</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §03</p>
<p style="margin:6px 0 0">As numbers, the strata separate cleanly — <strong>identities at 0, coincidences at a few bits, real problems at \(10^5\).</strong><br>
<em>"The cosmological constant and the neutrino mass agree within a factor 22" is no more surprising than flipping five heads in a row.</em></p>
</div>

<p>This probably runs against intuition. Hearing that \(10^{-31}\) and \(10^{-30}\) — <em>absurdly small numbers</em> — are close sounds momentous, but <strong>counted logarithmically it is 1.3 orders out of 35</strong>. Last episode's 1.96 fm is the same: 0.36 orders out of 61 — <em>7.4 bits</em>.</p>

<div class="aside">
<span class="tag">Only Koide's relation is surprising by orders</span>
The one entry at 15.7 bits is Koide's relation. Out of the range \([1/3,1]\) that \(Q\) can take, the measured value departs from \(2/3\) by only \(6.2\times10^{-6}\) — <strong>an agreement of one part in 30,000</strong>. Which is why, with no theoretical derivation at all, it has been taken seriously for over forty years. <em>This table explains why certain coincidences alone get treated seriously.</em>
</div>

<div class="fig">
<p class="cap">Figure: the surprises of the coincidences handled so far, in bits. The slider changes <strong>how the prior range is chosen</strong> — <em>surprise depends on how much you consider could have happened</em>. That is the weakest point of this measure.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Range allowed beforehand (orders of magnitude)<input id="ss" type="range" min="5" max="80" value="35" step="1"></label>
  <span class="val" id="vs">35 orders</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3f4a6b"></i>depends on the prior range (coincidences)</span>
  <span><i class="swatch" style="background:#8a5a2a"></i>independent of the prior range</span>
</div>
</div>

<p>Move the slider and only the top two bars stretch — <strong>"coincidence surprise" shifts by a few bits with the prior range</strong>. Identities (0 bits), Koide (whose \(Q\) range is mathematically fixed) and the CMB (whose patch count and precision are fixed by observation) do not move. <em>So the former are "weak" coincidences and the latter "strong" ones.</em></p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The sorting procedure — count inputs and outputs</h2>

<p>Apart from measuring bits, there is a more structural sort: <strong>what does the relation take in, and what does it put out?</strong></p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Class</th><th class="mid">Inputs</th><th class="mid">Outputs</th><th class="mid">Falsifiable?</th><th class="mid">Surprise</th></tr></thead>
<tbody>
<tr><th>Identity</th><td class="mid">0 (follows from definitions)</td><td class="mid">0</td><td class="mid">no</td><td class="mid">0 bit</td></tr>
<tr><th>Coincidence</th><td class="mid">2 or more independent measurements</td><td class="mid">0</td><td class="mid">no</td><td class="mid">a few bits</td></tr>
<tr class="hi"><th>Physics</th><td class="mid">\(n\) measurements</td><td class="mid"><strong>\(m\) predictions</strong></td><td class="mid">yes</td><td class="mid">large</td></tr>
</tbody>
</table>
</div>

<p>Apply it to Episode 1's \(\Omega/N=\ln2/3\pi^2(1+w)\): the input is one expansion law \(w\), the output is "operations per bit". <strong>It produces a quantity another measurement can reach, so it is physics.</strong> Whereas \(E/N=k_BT_H\ln2\) is the horizon's energy divided by the horizon's temperature and entropy — <em>no input, no output</em>.</p>

<h2><span class="n">05</span>Rewritten as description length, it returns to Episode 5</h2>

<p>This sorting is in fact what Episode 5 did. There we counted <strong>description length</strong> — a model is good if it lets you write the data shorter.</p>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>A good relation is one that reduces the description length of the data.</strong><br>
An identity reduces it by 0 bits. A coincidence reduces it by a few, and has <em>no mechanism to do the reducing</em>.<br>
Physics reduces it by orders — \(\Lambda\)CDM explains \(6.3\times10^6\) multipoles up to \(\ell\le2500\) with six parameters.</p>
</div>

<p>Episode 5 saw that "shortness buys only \(\log N\) while misfit costs \(N\)". Today the same balance is applied <em>not to models but to coincidences</em>. <strong>A coincidence demands explanation only when it could greatly reduce the description length.</strong></p>

<h2><span class="n">06</span>So is there nothing left in an identity?</h2>

<p>This needs care. <strong>"An identity is not physics" does not mean "an identity is meaningless".</strong></p>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>It is not a prediction</strong><span>it produces no quantity a new measurement can reach, so it is not a "discovery"</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>It is a consistency check</strong><span>\(E=T_HS\) holds because <em>holography and thermodynamics do not contradict each other</em>. If it failed, one of them would be wrong</span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>Breaking it would be a major discovery</strong><span>identities are not unfalsifiable; they fail <em>exactly when a premise of their derivation fails</em>, and the failure means that premise has failed</span></div></div>
</div>

<p>So the accurate phrasing is: <strong>an identity is not a "prediction" but a "check"</strong>. Every time this series has found one and written "not physics", it meant <em>do not treat it as a mystery</em> — not throw it away.</p>

<div class="aside">
<span class="tag">In Dirac's defence</span>
In 1937 Dirac did not know that \(M/m_P=R_H/2\ell_P\) is a consequence of the Friedmann equations (Friedmann cosmology was not yet established). <em>With the knowledge of the time, it genuinely looked like a mystery.</em> Recognising an identity is hindsight, and <strong>discovering that something "was an identity" is itself progress</strong> — one mystery fewer. Episode 7's "his prescription spins freely" was said with today's knowledge.
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① "Surprise in bits" shifts by a few bits with the choice of prior range.</strong> That is exactly what the figure's slider shows: the 4.7 bits for \(\rho_\Lambda^{1/4}\) and \(m_\nu\) assumes a 35-order range. Twenty orders gives 3.9 bits, sixty gives 5.5. <em>The procedure can rank things but is not an absolute number</em> — in Bayesian terms, it is the choice of prior.</p>
<p style="margin:0 0 10px"><strong>② A log-uniform prior is assumed.</strong> Natural for a scale (a Jeffreys prior), but not the only choice.</p>
<p style="margin:0 0 10px"><strong>③ The CMB value (\(1.6\times10^5\) bits) uses Episode 17's naive count</strong> of "17 independent bits × 9,600". Real fluctuations are structured by acoustic oscillations, so it is not an exact information content (Episode 17 ②). <em>Read it as an order-of-magnitude comparison.</em></p>
<p style="margin:0 0 10px"><strong>④ Koide's 15.7 bits takes \(Q\in[1/3,1]\) as the prior range.</strong> That is the mathematical range of \(Q\) for three positive masses, so the prior is barely arbitrary — which is part of what makes this coincidence "strong". But as Extra 4 of the previous series showed, the relation holds only for pole masses and the discrepancy grows 205-fold when run to \(M_Z\). <strong>Being surprising and being right are different things.</strong></p>
<p style="margin:0"><strong>⑤ The "\(n\) inputs → \(m\) outputs" sort is this series' own.</strong> Philosophy of science offers many criteria — falsifiability, predictive power, unifying power — and this extracts only the part expressible in information terms.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Why is an identity's surprise 0 bits?
<details><summary>Show the answer</summary><div class="ans">Because, following from definitions, <strong>there was only one place for it to land</strong>. The "range allowed beforehand" is a single point, so \(-\log_2(1)=0\). <em>There is nothing to be surprised by.</em></div></details></li>

<li>Find the surprise that \(\rho_\Lambda^{1/4}\) and \(m_\nu\) agree within a factor 22, with a 35-order prior.
<details><summary>Show the answer</summary><div class="ans">\(\log_{10}22.3=1.35\) orders; probability \(1.35/35=0.0385\); \(-\log_2 0.0385=\) <strong>4.7 bits</strong> — five coin flips. <em>Agreement between absurdly small numbers is, counted logarithmically, not much of a surprise.</em></div></details></li>

<li>Why is Koide's relation alone so surprising?
<details><summary>Show the answer</summary><div class="ans">Because \(Q\)'s range \([1/3,1]\) is mathematically fixed, yet the measurement departs from \(2/3\) by only \(6.2\times10^{-6}\). Probability \(1.85\times10^{-5}\), i.e. <strong>15.7 bits = one in 30,000</strong>. With little arbitrariness in the prior, the coincidence is "strong" — which is why it is taken seriously despite having no derivation.</div></details></li>

<li>Is "an identity is not physics" the same as "an identity is meaningless"?
<details><summary>Show the answer</summary><div class="ans">No. An identity is <strong>not a prediction but a consistency check</strong>. \(E=T_HS\) holds because holography and thermodynamics do not contradict each other, and <em>if it broke, one of the premises would be wrong</em>. "Not physics" means <strong>do not treat it as a mystery</strong>, not discard it.</div></details></li>

<li>(Harder) What is the greatest weakness of this measure?
<details><summary>Show the answer</summary><div class="ans"><strong>Dependence on the prior range.</strong> As the slider shows, the \(\rho_\Lambda\)/\(m_\nu\) surprise is 3.9 bits at 20 orders and 5.5 at 60. In Bayesian terms it is the choice of prior: <em>usable for ranking, not as an absolute number</em>. Conversely, where the prior is fixed by mathematics or observation — Koide, the CMB — the weakness shrinks.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — measured in bits, surprise falls into three strata</h2>
<p>We turned this series' repeated sorting — identity, coincidence or physics — into a procedure, using information theory's <strong>surprisal</strong>: \(-\log_2(\text{width}/\text{prior range})\).</p>
<p>Measured, the strata separate cleanly. <strong>Identities at 0 bits</strong> (Dirac's large numbers, the Landauer limit, \(\alpha+2\beta+\gamma=2\), Episode 18's \(N/(R/\ell_P)^3\)). <strong>Coincidences at a few bits</strong> — the factor-22 agreement of \(\rho_\Lambda^{1/4}\) and \(m_\nu\) is <em>five coin flips (4.7 bits)</em>, last episode's 1.96 fm is 7.4. <em>Agreement between absurdly small numbers is, logarithmically, not much of a surprise.</em> And <strong>real problems at \(10^5\) bits</strong> (CMB uniformity). The one entry at 15.7 bits is Koide's relation, which is why it has been taken seriously without a derivation.</p>
<p>We built a structural sort too — <strong>identities take 0 inputs and give 0 outputs; coincidences take 2 or more and give 0; physics takes \(n\) and gives \(m\) predictions</strong>. It is the same balance as Episode 5's description length: <em>a good relation reduces the description length of the data</em>, and \(\Lambda\)CDM explains \(6.3\times10^6\) multipoles with six parameters.</p>
<p>One point of care at the end. <strong>"An identity is not physics" does not mean "meaningless"</strong> — an identity is <em>a check, not a prediction</em>, and breaking it would mean a premise had failed. Dirac in 1937 did not know the Friedmann equations, so with the knowledge of the time it <em>genuinely looked like a mystery</em>. <strong>Discovering that something was an identity is itself progress</strong> — one mystery fewer.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 20</span>
With the sorting tool in hand, we go through <strong>the door the previous series left open</strong>. The last line of Extra 2 was: <em>"if you write the universe as a computer with finite resources, what should be constrained is not \(a(t)\) but the information on the light sheets. Nobody has done that calculation."</em> Extra 3 applied Bousso's covariant entropy bound to the apparent horizon to get \(s\le3H/4\ell_P^2\), and got as far as showing that <strong>saturating it identically gives \(a\propto t^{1/3}\)</strong>. Next time, further — <em>imposed as a constraint rather than a saturation, can it make a universe that matches observation?</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=270, X1=690, Y0=34;
  var ROWS=[
    ['Dirac\u2019s large numbers', 'id', 0],
    ['exactly at the Landauer limit', 'id', 0],
    ['α+2β+γ = 2', 'id', 0],
    ['ρ_Λ^(1/4) and m_ν (factor 22)', 'span', Math.log10(22.3)],
    ['a bit\u2019s volume ≈ a nucleon', 'span61', Math.log10(1.96/0.84)],
    ['Koide\u2019s relation Q=2/3', 'fix', 15.7],
    ['CMB uniform, 9,600 patches', 'fix', 1.595e5]
  ];
  var XMAX=30;

  function px(b){ return X0+Math.min(b,XMAX)/XMAX*(X1-X0); }

  function draw(){
    var span=parseInt(ss.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='center';
    for(var b=0;b<=30;b+=5){
      var x=px(b);
      g.strokeStyle=(b===0?'#c8cbd8':'#f0f1f6'); g.lineWidth=(b===0?1.6:1);
      g.beginPath(); g.moveTo(x,Y0-6); g.lineTo(x,Y0+7*40+6); g.stroke();
      g.fillStyle='#9a9db0'; g.fillText(b+' bit', x, Y0+7*40+22);
    }

    var vals=[];
    for(var i=0;i<ROWS.length;i++){
      var r=ROWS[i], b;
      if(r[1]==='id') b=0;
      else if(r[1]==='span') b=-Math.log2(r[2]/span);
      else if(r[1]==='span61') b=-Math.log2(r[2]/61);
      else b=r[2];
      vals.push(b);
      var y=Y0+i*40+8, h=22;
      var col=(r[1]==='span'||r[1]==='span61')?'#3f4a6b':'#8a5a2a';
      g.fillStyle=col; g.globalAlpha=(b===0?0.25:0.88);
      var w=px(b)-X0;
      g.fillRect(X0, y, Math.max(w,3), h);
      g.globalAlpha=1;
      g.fillStyle='#3a3d4a'; g.textAlign='right';
      g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.fillText(r[0], X0-12, y+16);
      g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.textAlign='left'; g.fillStyle=col;
      if(b>XMAX){
        g.fillText('→ '+(b/1000).toFixed(0)+',000 bit (another world)', X1-210, y+16);
      } else {
        g.fillText(b.toFixed(1)+' bit', px(b)+6, y+16);
      }
    }

    g.fillStyle='#7d8090'; g.textAlign='center';
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText('surprise = −log₂( width it landed in ÷ range allowed beforehand )', (X0+X1)/2-90, Y0+7*40+46);

    vs.textContent=span+' orders';
    ro.textContent='prior range '+span+' orders　→　ρ_Λ vs m_ν surprise '+vals[3].toFixed(1)+' bit, '+
      'a bit\u2019s volume ≈ a nucleon '+vals[4].toFixed(1)+' bit'+
      '　/　identities 0 bit, Koide 15.7 bit, CMB 1.6×10⁵ bit (none of them prior-dependent)';
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-19-surprise.html', acc='#3f4a6b', ops='#8a5a2a',
      title='Is an identity really not physics? ── c·t = const, That Clicks, Episode 19',
      ep='EPISODE 19 ／ Building the sorting procedure itself',
      eyebrow='Measured in bits, surprise falls into three clean strata',
      h1='Is an identity really<br>not physics?',
      sub='This series has sorted coincidences again and again.<br><em>Here the criterion is stated, in the language of information theory.</em>',
      byline_l='What you need: one logarithm',
      byline_r='surprise \\(=-\\log_2(\\text{width}/\\text{range})\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 19 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. Surprisal \\(-\\log_2 p\\) is a standard information-theoretic quantity. The surprise values given here (4.7 bits for \\(\\rho_\\Lambda^{1/4}\\) and \\(m_\\nu\\), 7.4 for a bit\'s volume against a nucleon, 15.7 for Koide\'s relation, \\(1.6\\times10^5\\) for CMB uniformity) are computed here (kenshou/calc23.py). <strong>They depend on the choice of prior range</strong>: the 4.7 bits assumes a 35-order log-uniform (Jeffreys) prior, becoming 3.9 at twenty orders and 5.5 at sixty. <em>The procedure ranks; it is not an absolute number.</em> The CMB\'s \\(1.6\\times10^5\\) bits uses Episode 17\'s naive count of "17 independent bits × 9,600"; real fluctuations are structured by acoustic oscillations, so it is not an exact information content. Koide\'s 15.7 bits takes \\(Q\\in[1/3,1]\\) (the mathematical range for three positive masses) as the prior, with \\(Q=0.66666051\\) departing from \\(2/3\\) by \\(6.2\\times10^{-6}\\) — though the relation has no theoretical derivation, holds only for pole masses, and its discrepancy grows 205-fold when run to \\(M_Z\\) (Extra 4 of the previous series). <strong>Being surprising and being right are different things.</strong> The "\\(n\\) inputs → \\(m\\) outputs" sort is this series\' own, extracting from the philosophy of science (falsifiability, predictive power, unifying power) only what can be written in information terms. The remark that Dirac (1937) did not know \\(M/m_P=R_H/2\\ell_P\\) to be a consequence of the Friedmann equations is a point about historical context. The six \\(\\Lambda\\)CDM parameters and the \\(6.3\\times10^6\\) \\(a_{\\ell m}\\) modes up to \\(\\ell\\le2500\\) are indicative. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the prior range and only the coincidence bars move. "Show the answer" opens each solution.')
