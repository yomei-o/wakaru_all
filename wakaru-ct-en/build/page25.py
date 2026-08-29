# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Physical laws are machines for rewriting the world more shortly. Kepler's three laws fold tables of planetary positions into equations; \(\Lambda\)CDM produces six million multipoles from six numbers. <strong>So does ranking theories by compression ratio order them by quality?</strong> Today we compute that seriously — <em>and watch it break down along the way</em>.</p>

<h2><span class="n">01</span>First, measure the length of the law itself</h2>

<p>Write each equation in LaTeX and count at \(\log_2 95=6.57\) bits per character (95 printable ASCII characters).</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Law</th><th class="mid">Characters</th><th class="mid">Bits</th></tr></thead>
<tbody>
<tr class="hi"><th>c·t=const (expansion law) \(a\propto t\)</th><td class="mid"><strong>10</strong></td><td class="mid"><strong>66</strong></td></tr>
<tr><th>Newtonian gravity</th><td class="mid">13</td><td class="mid">85</td></tr>
<tr><th>Schrödinger equation</th><td class="mid">31</td><td class="mid">204</td></tr>
<tr><th>Dirac equation</th><td class="mid">33</td><td class="mid">217</td></tr>
<tr><th>Friedmann equation</th><td class="mid">63</td><td class="mid">414</td></tr>
<tr><th>Maxwell's equations (tensor form)</th><td class="mid">66</td><td class="mid">434</td></tr>
<tr><th>Einstein field equations</th><td class="mid">78</td><td class="mid">512</td></tr>
<tr><th>Standard Model Lagrangian (expanded)</th><td class="mid">≈ 5000</td><td class="mid">≈ 33000</td></tr>
</tbody>
</table>
</div>

<p><strong>The shortest is \(a\propto t\) at 66 bits</strong> — the entire expansion history of the universe in one fortieth of a tweet.</p>

<h2><span class="n">02</span>Next, count the numbers explained</h2>

<div class="calc">
<span class="tag">Counting the CMB</span>
<p class="lbl">spherical harmonic modes from \(l=2\) to \(2500\)</p>
$$\sum_{l=2}^{2500}(2l+1)=6{,}254{,}997\quad(\text{TT only})\qquad\times3=1.88\times10^7\quad(\text{TT+TE+EE})$$
<p class="lbl">\(\Lambda\)CDM has six parameters, so</p>
$$\text{compression ratio}=\frac{6{,}254{,}997}{6}=1.0\times10^6$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Theory</th><th class="mid">Parameters</th><th class="mid">Numbers explained</th><th class="mid">Compression ratio</th></tr></thead>
<tbody>
<tr><th>Rydberg formula</th><td class="mid">1 (\(R_\infty\))</td><td class="mid">4,950 lines for \(n\le100\)</td><td class="mid">4,950×</td></tr>
<tr><th>\(\Lambda\)CDM</th><td class="mid">6</td><td class="mid">\(6.3\times10^6\) modes</td><td class="mid">\(1.0\times10^6\)×</td></tr>
<tr><th>Standard Model</th><td class="mid">19</td><td class="mid">every cross section</td><td class="mid">(depends how you count)</td></tr>
<tr class="hi"><th>General relativity</th><td class="mid"><strong>0</strong></td><td class="mid">every spacetime</td><td class="mid"><strong>formally infinite</strong></td></tr>
</tbody>
</table>
</div>

<p>So far it is a pleasing story: <em>fewer parameters, better theory</em>. And then —</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>Where it breaks — the same calculation reverses the verdict</h2>

<p>Total it up properly with MDL (minimum description length). The total is a sum of three things.</p>

<div class="calc">
<span class="tag">MDL</span>
$$L=\underbrace{L(\text{law})}_{\text{length of the equation}}+\underbrace{L(\text{parameters})}_{\tfrac12\log_2N\ \text{bit each}}+\underbrace{L(\text{residual})}_{\Delta\chi^2/(2\ln2)}$$
<p class="lbl">reusing Episode 5's values: \(\tfrac12\log_2N=5.37\) bit per parameter at \(N=1701\), and a residual of 153.6 bit for \(\Delta\chi^2=213\)</p>
</div>

<p>The problem is that \(L(\text{law})\) changes depending on whether \(a\propto t\) is counted as <strong>a constraint added to the Friedmann equation</strong> or as <strong>something replacing it wholesale</strong>.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Reading A: an added constraint</th><th class="mid">L(law)</th><th class="mid">L(param)</th><th class="mid">L(residual)</th><th class="mid">Total</th></tr></thead>
<tbody>
<tr><th>\(\Lambda\)CDM</th><td class="mid">414</td><td class="mid">32.2</td><td class="mid">0.0</td><td class="mid"><strong>446</strong></td></tr>
<tr><th>c·t=const</th><td class="mid">414+66</td><td class="mid">26.8</td><td class="mid">153.6</td><td class="mid">660</td></tr>
</tbody>
</table>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Reading B: a replacement</th><th class="mid">L(law)</th><th class="mid">L(param)</th><th class="mid">L(residual)</th><th class="mid">Total</th></tr></thead>
<tbody>
<tr><th>\(\Lambda\)CDM</th><td class="mid">414</td><td class="mid">32.2</td><td class="mid">0.0</td><td class="mid">446</td></tr>
<tr class="hi"><th>c·t=const</th><td class="mid">66</td><td class="mid">26.8</td><td class="mid">153.6</td><td class="mid"><strong>246</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>Same model, same data, and the verdict flips from losing by 214 bits to winning by 200.</strong><br>
All that moved was 414 bits of \(L(\text{law})\) — <em>and that is set by which language you write the equation in.</em></p>
</div>

<p>This is Kolmogorov complexity's <strong>invariance theorem</strong> itself: description length is defined only up to a constant depending on the description language. Textbooks treat that constant as "large but finite, and irrelevant once you have enough data". But <em>for the purpose of comparing theories, it turned out large enough to flip the result</em>.</p>

<div class="fig">
<p class="cap">Figure: MDL's three pillars. Moving \(L(\text{law})\) with the slider swaps the totals, while <strong>the comparison using only \(L(\text{param})\) and \(L(\text{residual})\) (the narrow bars at right) does not move</strong>.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>How to count \(L(\text{law})\) for c·t=const [bit]<input id="sl" type="range" min="0" max="600" value="480" step="5"></label>
  <span class="val" id="vl">480</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#3a2f5a"></i>L(law): language dependent</span>
  <span><i class="swatch" style="background:#b06a2a"></i>L(param): invariant</span>
  <span><i class="swatch" style="background:#8a7fa8"></i>L(residual): fixed by the data</span>
</div>
</div>

<h2><span class="n">04</span>So which part of the compression ratio is trustworthy?</h2>

<div class="seven">
<div class="row"><div class="mk">✕</div><div class="txt"><strong>L(law) — not usable</strong><span>depends on the description language; it moved 414 bits in this example. "Short equation, good theory" cannot be supported in information terms</span></div></div>
<div class="row hi"><div class="mk">○</div><div class="txt"><strong>L(parameters) — usable</strong><span>the number of parameters is invariant under reparametrisation. 5.37 bits each</span></div></div>
<div class="row hi"><div class="mk">○</div><div class="txt"><strong>L(residual) — usable</strong><span>the likelihood is fixed by the data. 153.6 bits</span></div></div>
</div>

<div class="calc">
<span class="tag">Comparing with only the trustworthy parts</span>
$$\Delta L=\underbrace{+5.37}_{\text{gain from one fewer parameter}}-\underbrace{153.6}_{\text{loss on fit}}=-148.3\ \text{bit}$$
$$\text{odds ratio}\ 2^{148}=4.3\times10^{44}$$
</div>

<p>Episode 3's verdict <strong>depends only on these two terms</strong>. Throw away the vague business of equation length entirely and the conclusion is unchanged — <em>not a re-litigation of the verdict, but a check on how narrow a foundation it rests on</em>.</p>

<h2><span class="n">05</span>The reveal — compression ratio is not "quality" but "stake"</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Parameters \(k\)</th><th class="mid">Room to manoeuvre</th></tr></thead>
<tbody>
<tr class="hi"><th>\(k=0\)</th><td class="mid"><strong>it is impossible in principle to fit to anything</strong></td></tr>
<tr><th>\(k=1\)</th><td class="mid">can move in one direction</td></tr>
<tr><th>\(k=6\) (\(\Lambda\)CDM)</th><td class="mid">six directions</td></tr>
<tr><th>\(k=25\) (\(\Lambda\)CDM + Standard Model)</th><td class="mid">twenty-five directions</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0">High compression ratio ⟺ few parameters ⟺ <strong>nowhere to hide</strong> ⟺ easily falsified.<br>
MDL's compression ratio and Popper's falsifiability were <em>two sides of the same axis</em>.</p>
</div>

<p>So \(a\propto t\) being "shortest, zero parameters" is <strong>not good news but news of a large bet</strong>. The stake was big, so losing cost 148 bits. <em>That is what "the common weakness of theories that compress too well" means</em> — there is no room to absorb.</p>

<div class="aside">
<span class="tag">And yet shortness has a use</span>
Not for judging, as we said. <strong>But for rewriting.</strong> What this series has been doing all along is not judging but compressing — \(H_0d_L/c=(1+z)\ln(1+z)\) (Episode 9, zero parameters), \(\Omega/N=p\ln2/2\pi^2\) (Episode 1), \(C\cdot t=N\) (Episode 24). <em>These are not claims that "short means true" but that "short reveals structure".</em> Whether the structure revealed is real is always decided by \(L(\text{residual})\).
</div>

<h2><span class="n">06</span>The universe's own compression ratio</h2>

<div class="calc">
<span class="tag">What the laws do not compress</span>
<p class="lbl">information actually in use (Episodes 6 and 23)</p>
$$k=S/\ln2=4.47\times10^{104}\ \text{bit}$$
<p class="lbl">parameters used by physical law (\(\Lambda\)CDM + Standard Model)</p>
$$25\ \text{parameters}\approx134\ \text{bit}$$
</div>

<p>It looks as though 134 bits of law explain a \(4.5\times10^{104}\)-bit world, but <strong>laws do not compress initial conditions</strong>. What holds the breakdown of those \(10^{104}\) bits is not the law but <em>the history</em>. Episode 20's "the universe is a 140-move program" was exactly about that history.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① "One character = 6.57 bits" is an arbitrary way of counting.</strong> That is in fact the subject of this episode. Choose a notation other than LaTeX and every equation becomes shorter or longer — so §01's table is <em>not a claim about ranking but material to be demolished in §03</em>.</p>
<p style="margin:0 0 10px"><strong>② The compression ratio (numbers explained ÷ parameters) also depends on how the numerator is counted.</strong> \(\Lambda\)CDM's \(6.3\times10^6\) is the number of TT \(a_{lm}\) modes; the genuinely independent information is smaller (Planck's binned \(C_l\) are 1701 points) and larger if TT+TE+EE and other observations are added. The Standard Model row was left blank for the same reason — <em>there was no honest way to count it</em>.</p>
<p style="margin:0 0 10px"><strong>③ \(\Delta\chi^2=213\) is the value used in Episode 5 and depends on the observational set compared.</strong> More robust than the number is the structure: the residual term exceeds the parameter term by two orders.</p>
<p style="margin:0 0 10px"><strong>④ Using \(\Delta\chi^2/(2\ln2)\) for MDL's residual term is a Gaussian approximation.</strong> Strictly one should take the likelihood ratio itself; for non-Gaussian likelihoods the coefficient changes.</p>
<p style="margin:0 0 10px"><strong>⑤ "General relativity has zero parameters" excludes \(\Lambda\).</strong> Count \(\Lambda\) as part of the theory and it is one; \(G\) and \(c\) are unit conversions and are not counted (Episode 2's convention).</p>
<p style="margin:0"><strong>⑥ Episode 3's verdict is not moved.</strong> §04 is not a re-judgement but <em>a confirmation that the verdict does not depend at all on the vague term \(L(\text{law})\)</em>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Count \(\Lambda\)CDM's compression ratio using TT+TE+EE.
<details><summary>Show the answer</summary><div class="ans">\(3\times6{,}254{,}997/6=3.1\times10^6\)×. But the numerator is a mode count rather than independent information, so <strong>this is the generous way of counting</strong>.</div></details></li>

<li>In one line, why do readings A and B give opposite verdicts?
<details><summary>Show the answer</summary><div class="ans">Because \(L(\text{law})\) depends on the description language. A and B differ by the Friedmann equation's 414 bits, <strong>which more than cancels the 148-bit difference</strong>. The "language-dependent constant" of Kolmogorov's invariance theorem bites here.</div></details></li>

<li>By how much must \(\Delta\chi^2\) fall for an added parameter to pay for itself (\(N=1701\))?
<details><summary>Show the answer</summary><div class="ans">The price is \(\tfrac12\log_2 1701=5.37\) bit, so it pays if \(\Delta\chi^2/(2\ln2)>5.37\), i.e. <strong>\(\Delta\chi^2>7.44\)</strong> — a far stricter criterion than the naive "\(\Delta\chi^2>1\)".</div></details></li>

<li>Is "a theory with a higher compression ratio is better" correct?
<details><summary>Show the answer</summary><div class="ans">No. High compression ⟺ few parameters ⟺ <strong>nowhere to hide</strong> ⟺ easily falsified. Compression ratio measures not <em>quality</em> but <em>the size of the bet</em>. \(a\propto t\) is shortest with zero parameters, which is exactly why it missed by so much.</div></details></li>

<li>(Harder) How can 134 bits of law explain a \(4.5\times10^{104}\)-bit world?
<details><summary>Show the answer</summary><div class="ans"><strong>It cannot.</strong> Laws compress the rules of time evolution but not the initial conditions. What holds the breakdown of \(10^{104}\) bits is the history — Episode 20's "140-move program" — and the law is merely its rule of execution.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — compression ratio is a stake, not a quality</h2>
<p>Counting the length of laws in LaTeX characters, the shortest is \(a\propto t\) at <strong>66 bits</strong>, the Einstein equations at 512, the Standard Model at about 33,000. Divided by the numbers explained, \(\Lambda\)CDM compresses \(10^6\)-fold and general relativity formally infinitely.</p>
<p>Totalled properly with MDL, it broke down. Counting \(a\propto t\) as "a constraint added to the Friedmann equation" or as "a replacement" flips <strong>the same model on the same data from losing by 214 bits to winning by 200</strong>. All that moved was \(L(\text{law})\)'s 414 bits, a language-dependent quantity. The "language-dependent constant" of Kolmogorov's invariance theorem turned out, for the purpose of comparing theories, <em>large enough to decide the outcome</em>.</p>
<p>What is trustworthy is the other two: the parameter count (reparametrisation invariant, 5.37 bit each) and the residual (fixed by the data, 153.6 bits). Compared with those alone, \(-148\) bits, an odds ratio of \(4.3\times10^{44}\). <strong>Episode 3's verdict stands on that narrow foundation alone.</strong></p>
<p>And the reveal — high compression ⟺ few parameters ⟺ nowhere to hide ⟺ easily falsified. <em>MDL's compression ratio and Popper's falsifiability are two sides of one axis.</em> That \(a\propto t\) is shortest with zero parameters is not good news but <strong>news of a large bet</strong>. The weakness of theories that compress too well is having no room to absorb — though that concerns <em>judging</em>; the value of shortness for <em>rewriting</em> remains untouched.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 26 (Part III finale)</span>
Part III closes with <strong>a reckoning of "measuring as information"</strong>. From Episode 17 to today we have measured the universe with eight rulers — horizon, parameters, surprise, coincidence, operations, codes, bandwidth, description length. Laid out in one table, <strong>the same numbers keep reappearing</strong> — \(1.5\times10^{-18}\) three times, \(140\) four times, \(0.035\) twice. <em>When different rulers give the same number, is that a discovery, or were they measuring the same thing all along?</em> We apply Episode 19's surprisal procedure to the series itself.
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sl=document.getElementById('sl'), vl=document.getElementById('vl'), ro=document.getElementById('ro');
  var LF=414.0, PA=32.2, PB=26.8, RES=153.6;
  var X0=70, X1=700, Y0=34, Y1=300;
  function draw(){
    var Lct=parseFloat(sl.value);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    var lcdm=[LF,PA,0], ct=[Lct,PB,RES];
    var tl=LF+PA, tc=Lct+PB+RES;
    var max=Math.max(tl,tc,700);
    function bar(x,w,parts,label,total,sub){
      var y=Y1;
      var cols=['#3a2f5a','#b06a2a','#8a7fa8'];
      for(var i=0;i<3;i++){
        var h=parts[i]/max*(Y1-Y0);
        g.fillStyle=cols[i];
        g.fillRect(x,y-h,w,h);
        if(h>16){
          g.fillStyle='#fff'; g.textAlign='center';
          g.fillText(parts[i].toFixed(0), x+w/2, y-h/2+4);
        }
        y-=h;
      }
      g.strokeStyle='#cfc7dd'; g.lineWidth=1; g.strokeRect(x,y,w,Y1-y);
      g.fillStyle='#3a2f5a'; g.textAlign='center';
      g.font='bold 13px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.fillText(total.toFixed(0)+' bit', x+w/2, y-9);
      g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.fillStyle='#5a4f78';
      g.fillText(label, x+w/2, Y1+20);
      if(sub){ g.fillStyle='#9088a8'; g.fillText(sub, x+w/2, Y1+37); }
    }
    bar(120,110,lcdm,'ΛCDM',tl,'(reference)');
    bar(275,110,ct,'c·t=const',tc,'L(law) varies');
    g.strokeStyle='#e4dff0'; g.lineWidth=1; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(440,Y0-14); g.lineTo(440,Y1+44); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#8a7fa8'; g.textAlign='left';
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText('with L(law) discarded — immovable', 462, Y0-2);
    bar(500,64,[0,PA,0],'ΛCDM',PA,'');
    bar(600,64,[0,PB,RES],'c·t',PB+RES,'');
    g.strokeStyle='#c3b8d8'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();
    vl.textContent=Lct.toFixed(0)+' bit';
    var w = tc<tl ? 'c·t=const wins' : 'ΛCDM wins';
    ro.textContent='L(law)='+Lct.toFixed(0)+'　→　totals '+tc.toFixed(0)+' vs '+tl.toFixed(0)+
      '　'+w+' (by '+Math.abs(tc-tl).toFixed(0)+' bit)'+
      '　/　discard L(law) and the gap is always '+(PB+RES-PA).toFixed(1)+' bit in ΛCDM’s favour';
  }
  sl.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-25-mdl.html', acc='#3a2f5a', ops='#b06a2a',
      title='Are physical laws a compression algorithm? ── c·t = const, That Clicks, Episode 25',
      ep='EPISODE 25 ／ Ranking theories by description length, and where it breaks',
      eyebrow='Compression ratio turned out to be a stake, not a quality',
      h1='Are physical laws a<br>compression algorithm?',
      sub='\\(a\\propto t\\) is 66 bits; the Einstein equations are 512.<br><em>So is shorter better? Compute it seriously and it breaks down along the way.</em>',
      byline_l='What you need: MDL, \\(\\tfrac12\\log_2N\\), multiplication',
      byline_r='compression ratio = falsifiability',
      body=BODY + '\n\n<p class="foot">This document is Episode 25 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The minimum description length principle (Rissanen), the invariance theorem of Kolmogorov complexity, and BIC\'s \\(\\tfrac12\\log_2N\\) are all standard. <strong>The convention "one character = \\(\\log_2 95\\) bits" is arbitrary and is itself the subject of this episode</strong> — §01\'s table is material for §03 to demolish, not a claim about ranking. The A/B comparison (losing by 214 bits versus winning by 200) and the comparison with \\(L(\\text{law})\\) discarded (\\(-148.3\\) bit) are computed here (kenshou/calc29.py). The numerator of a compression ratio (the count of numbers explained) depends strongly on how it is counted: \\(\\Lambda\\)CDM\'s \\(6.3\\times10^6\\) is the number of TT \\(a_{lm}\\) modes (the independent information is closer to Planck\'s 1701 binned \\(C_l\\)). The Standard Model row was left blank because there was no honest way to count it. \\(\\Delta\\chi^2=213\\) is the value used in Episode 5 and depends on the observational set compared; the residual term \\(\\Delta\\chi^2/(2\\ln2)\\) is a Gaussian approximation. "General relativity has zero parameters" is the counting that excludes \\(\\Lambda\\). Linear expansion (\\(c\\cdot t=\\)const) is a minority model under examination whose judgement was handled in Episode 3 — this document does not re-examine it but confirms that the judgement does not depend on \\(L(\\text{law})\\). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, moving L(law) flips the verdict. "Show the answer" opens each solution.')
