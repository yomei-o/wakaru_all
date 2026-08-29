# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 18 counted that "volume cells were never given addresses". So how are the \(10^{122}\) bits written on the horizon <em>protected</em>? Today we reread them <strong>in the language of codes</strong>. Episode 6's "occupancy \(1.5\times10^{-18}\)" then reappears wearing a completely different face — <strong>a redundancy of \(6.6\times10^{17}\)</strong>. <em>Not empty, but the same information written over and over.</em></p>

<h2><span class="n">01</span>Reading it as a code</h2>

<p>An error-correcting code is characterised by two numbers — <strong>physical bits \(n\)</strong> (the storage elements actually used) and <strong>logical bits \(k\)</strong> (the information to be protected). Apply them to the universe.</p>

<div class="calc">
<span class="tag">Putting in the two numbers</span>
<p class="lbl">physical bits (writable on the horizon, Episode 1)</p>
$$n=2.96\times10^{122}$$
<p class="lbl">logical bits (the entropy actually in use, Episode 6)</p>
$$k=\frac{S_{\rm obs}/k_B}{\ln2}=\frac{3.1\times10^{104}}{0.693}=4.47\times10^{104}$$
<p class="lbl">code rate and redundancy</p>
$$R=\frac{k}{n}=1.51\times10^{-18},\qquad \frac{n}{k}=6.61\times10^{17}$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0">Episode 6's "occupancy \(1.5\times10^{-18}\)" is, in the language of codes, <strong>"redundancy \(6.6\times10^{17}\)"</strong>.<br>
<em>The same number, read the opposite way round.</em></p>
</div>

<h2><span class="n">02</span>Comparing with real codes</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Code</th><th class="mid">Redundancy \(n/k\)</th><th class="mid">Note</th></tr></thead>
<tbody>
<tr><th>QR code (highest level)</th><td class="mid">1.4</td><td class="mid">recovers up to 30% damage</td></tr>
<tr><th>RAID6</th><td class="mid">1.5</td><td class="mid">survives two disk failures</td></tr>
<tr><th>Low-rate channel codes</th><td class="mid">10</td><td class="mid">deep space communication and the like</td></tr>
<tr><th>Quantum error correction, surface code</th><td class="mid">\(10^{3}\)</td><td class="mid">1000 physical qubits per logical one</td></tr>
<tr class="hi"><th>The cosmic horizon</th><td class="mid"><strong>\(6.6\times10^{17}\)</strong></td><td class="mid"><strong>\(6.6\times10^{14}\) times the surface code</strong></td></tr>
</tbody>
</table>
</div>

<p><strong>Fourteen orders more redundant</strong> than any code humans build. Where quantum error correction is lamented for needing 1000 physical qubits per logical one, the universe uses \(10^{18}\).</p>

<h2><span class="n">03</span>Estimating the correction capability</h2>

<div class="calc">
<span class="tag">Upper bounds</span>
<p class="lbl">classical code</p>
$$d\le n-k+1=2.96\times10^{122}\qquad(\text{essentially }n\text{ itself})$$
<p class="lbl">quantum code</p>
$$d\le\frac{n-k}{2}+1=1.48\times10^{122}=\frac{n}{2}$$
</div>

<div class="keybox">
<p class="lbl">Conclusion of §03</p>
<p style="margin:6px 0 0">In principle — <strong>about half the horizon's bits could be destroyed and the contents still recovered.</strong><br>
(This is an <em>upper bound</em>; there is no guarantee that the universe is such a code.)</p>
</div>

<div class="fig">
<p class="cap">Figure: redundancies compared (log). Human codes cluster at the left; only the universe is orders to the right. The slider moves <strong>the estimate of the entropy in use</strong> — \(S_{\rm obs}\) has order-of-magnitude uncertainty, and the redundancy moves with it.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Entropy in use \(\log_{10}(S_{\rm obs}/k_B)\) (default 104.5)<input id="ss" type="range" min="1000" max="1100" value="1045" step="1"></label>
  <span class="val" id="vs">10^104.5</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a5a4a"></i>codes humans build</span>
  <span><i class="swatch" style="background:#8a4a2a"></i>the cosmic horizon</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The heart — empty, or redundant?</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Reading</th><th>What it says</th><th class="mid">From</th></tr></thead>
<tbody>
<tr><th>① Empty</th><td>only \(1.5\times10^{-18}\) of the capacity is used</td><td class="mid">Episode 6</td></tr>
<tr class="hi"><th>② Redundant</th><td>the same information is written \(6.6\times10^{17}\) times over</td><td class="mid">today</td></tr>
</tbody>
</table>
</div>

<p>Can observation tell these apart? — <strong>Episode 3's procedure applies directly.</strong></p>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>"Empty" and "redundant" cannot be distinguished until you name the comparison.</strong><br>
<em>Against the capacity it is empty; against the information it is redundant</em> — two readings of one ratio.</p>
</div>

<p>Episode 3 applied this surgery to "\(c\cdot t\) is constant", Episode 9 to "atoms are shrinking", Episode 12 to "the cosmological constant". Today it applies to <strong>a number this series produced itself</strong> — <em>saying "it is empty" without naming the comparison is not yet a sentence.</em></p>

<h2><span class="n">05</span>Holographic codes as a precedent</h2>

<p>"Protect the bulk with boundary information" is not a whim. AdS/CFT admits <strong>a reading as a quantum error-correcting code</strong> (Almheiri, Dong &amp; Harlow 2015).</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>Local bulk operators can be reconstructed from boundary subregions</strong><span>lose part of the boundary and the information at the bulk centre survives</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>That is the definition of an error-correcting code</strong><span>"information in the code space survives erasure of subsystems" — mathematically the same structure</span></div></div>
<div class="row hi"><div class="mk">✗</div><div class="txt"><strong>But it is not established for a cosmological horizon</strong><span>the AdS boundary and the cosmic horizon are different things; de Sitter / FLRW holography is unsettled — <em>this episode goes only as far as analogy</em></span></div></div>
</div>

<p>So what we can do here is <strong>translate numbers into the language of codes, and no further</strong> — we cannot say "the universe is in fact an error-correcting code". That line is drawn clearly.</p>

<h2><span class="n">06</span>Restraint — the size of one logical bit</h2>

<p>Episode 18 produced the coincidence "the side of a physical bit's volume is 1.96 fm — the size of a proton". Do the same for a <em>logical</em> bit.</p>

<div class="calc">
<span class="tag">Area occupied by one logical bit</span>
$$\frac{A}{k}=\frac{2.14\times10^{53}}{4.47\times10^{104}}=4.79\times10^{-52}\ \mathrm{m^2}\qquad\Longrightarrow\qquad \text{side}\ 2.19\times10^{-26}\ \mathrm{m}$$
</div>

<p>Following Episode 19's practice, check whether it matches anything.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Candidate</th><th class="mid">Length</th><th class="mid">Ratio</th></tr></thead>
<tbody>
<tr><th>Proton</th><td class="mid">\(10^{-15}\) m</td><td class="mid">\(2.2\times10^{-11}\)</td></tr>
<tr><th>Electroweak scale</th><td class="mid">\(2.5\times10^{-18}\) m</td><td class="mid">\(8.8\times10^{-9}\)</td></tr>
<tr><th>Grand unification scale</th><td class="mid">\(2\times10^{-32}\) m</td><td class="mid">\(1.1\times10^{6}\)</td></tr>
<tr class="hi"><th>Planck length</th><td class="mid">\(1.6\times10^{-35}\) m</td><td class="mid">\(1.4\times10^{9}\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0"><strong>It matches nothing. So there is nothing to say.</strong><br>
── Unlike Episode 18's 1.96 fm, this number has no near neighbour. <em>Silence is the right answer.</em></p>
</div>

<p>This is exactly why Episode 19 built the sorting procedure. <strong>Not every number a calculation produces means something</strong> — with no near neighbour, the surprise is 0 bits and there is nothing to say.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① This does not claim "the universe is an error-correcting code".</strong> All it does is <em>translate two numbers</em> from Episodes 1 and 6 into the language of codes. The reading of AdS/CFT as quantum error correction (Almheiri, Dong &amp; Harlow 2015) concerns the AdS boundary, and <strong>whether a cosmological horizon has the same structure is unsettled</strong> (de Sitter/FLRW holography is not established).</p>
<p style="margin:0 0 10px"><strong>② Setting \(k=S_{\rm obs}/\ln2\) is a crude identification.</strong> Reading thermodynamic entropy as "logical bits to be protected" is not obvious — entropy is arguably a measure of <em>lost</em> information, so one could argue for the opposite reading. And \(S_{\rm obs}\) itself has order-of-magnitude uncertainty (Episode 6 ①), which the slider illustrates.</p>
<p style="margin:0 0 10px"><strong>③ The Singleton bound is an upper bound; achievability is another matter.</strong> "Half the horizon could be destroyed and still recovered" means <em>such a code could exist</em>, not that the universe is one.</p>
<p style="margin:0 0 10px"><strong>④ The surface code's \(10^3\) is indicative</strong>, moving between \(10^2\) and \(10^4\) with the physical error rate and the target logical error rate.</p>
<p style="margin:0"><strong>⑤ §04's "empty or redundant" is this series' reading.</strong> It is not a rigorous demonstration that the two readings are observationally equivalent — only the procedural point that <em>without naming a comparison, no distinction can be drawn</em>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Find the code rate and redundancy of the cosmic horizon read as a code.
<details><summary>Show the answer</summary><div class="ans">Physical bits \(n=2.96\times10^{122}\), logical bits \(k=3.1\times10^{104}/\ln2=4.47\times10^{104}\). Rate \(R=k/n=1.51\times10^{-18}\), redundancy \(n/k=\) <strong>\(6.6\times10^{17}\)</strong> — <em>the flip side of Episode 6's occupancy</em>.</div></details></li>

<li>How much more redundant is it than the quantum surface code?
<details><summary>Show the answer</summary><div class="ans">The surface code is around \(10^3\), so \(6.6\times10^{17}/10^3=\) <strong>\(6.6\times10^{14}\) times</strong> — fourteen orders beyond any human code.</div></details></li>

<li>State the two readings of \(1.5\times10^{-18}\) and say whether they can be distinguished.
<details><summary>Show the answer</summary><div class="ans">① "only \(1.5\times10^{-18}\) of the capacity is used (empty)" and ② "the same information is written \(6.6\times10^{17}\) times over (redundant)". <strong>They cannot be distinguished until you name the comparison</strong> — against capacity it is empty, against information it is redundant. Episode 3's surgery, applied to the series' own number.</div></details></li>

<li>Find the side of the area one logical bit occupies, and check whether it matches anything.
<details><summary>Show the answer</summary><div class="ans">\(A/k=4.79\times10^{-52}\ \mathrm{m^2}\), side \(2.19\times10^{-26}\) m — eleven orders smaller than a proton, nine orders larger than the Planck length. <strong>It matches nothing.</strong> By Episode 19's practice the surprise is 0 bits and <em>there is nothing to say</em>. Not every number a calculation produces means something.</div></details></li>

<li>(Harder) Can we say "the universe is an error-correcting code"?
<details><summary>Show the answer</summary><div class="ans">No. The formulation of AdS/CFT as a quantum error-correcting code concerns <strong>the AdS boundary</strong>, and whether the same structure holds for a cosmological horizon is unsettled (de Sitter/FLRW holography is not established). <em>This document goes only as far as translating two numbers into the language of codes.</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — the same number, read inside out</h2>
<p>We read the horizon as a code: physical bits \(n=2.96\times10^{122}\), logical bits \(k=4.47\times10^{104}\), rate \(R=1.51\times10^{-18}\). Inverted, a <strong>redundancy of \(6.6\times10^{17}\)</strong> — the flip side of Episode 6's occupancy. Fourteen orders beyond any human code, dwarfing the quantum surface code (\(10^3\)). By the Singleton bound, in principle <em>half the horizon's bits could be destroyed and the contents recovered</em> (as an upper bound only).</p>
<p>The heart was the reading. <strong>The same \(1.5\times10^{-18}\) can be read as "empty" or as "redundant"</strong> — against capacity, empty; against information, redundant. <em>Until you name the comparison, the two cannot be distinguished.</em> The surgery applied to \(c\cdot t\) in Episode 3, to atoms in Episode 9 and to the cosmological constant in Episode 12 has now landed on <strong>a number this series produced itself</strong>.</p>
<p>There is a precedent: AdS/CFT read as a quantum error-correcting code, where "lose part of the boundary and the bulk centre survives" is the definition of a code. <strong>But whether the same holds for a cosmological horizon is unsettled</strong>, so all this episode could do was <em>translate numbers into the language of codes</em>. That line is drawn clearly.</p>
<p>And one act of restraint at the end. The side of the area one logical bit occupies is \(2.19\times10^{-26}\) m — checked by Episode 19's practice, it <strong>matches nothing</strong>. Unlike Episode 18's 1.96 fm, it has no near neighbour. <em>Not every number a calculation produces means something, and with no near neighbour there is nothing to say</em> — which is why the sorting procedure was built.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 24</span>
Next: <strong>channel capacity</strong>. Episode 17 counted "the agreement needed 20 KB; the problem was that there was no channel". So how wide is the channel — <em>how many bits per second can cross the horizon?</em> Episode 1 counted \(dN/dt=1.36\times10^{105}\) bit/s, but that is <strong>the rate at which capacity grows</strong>, not a communication speed. From the Bremermann limit and the Bekenstein bound we estimate <em>the bandwidth information can actually cross at</em>. And we add <strong>a bandwidth constraint</strong> to Episode 2's conclusion that "the universe has made only 140 moves".
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=230, X1=690, Y0=40;
  var n=2.9556e122, ln2=Math.log(2);
  var CODES=[['QR code',1.4286],['RAID6',1.5],['channel codes',10],['surface code',1e3]];
  var XMAX=20;

  function px(v){ return X0+Math.min(Math.max(v,0),XMAX)/XMAX*(X1-X0); }

  function draw(){
    var lS=parseInt(ss.value,10)/10;
    var k=Math.pow(10,lS)/ln2;
    var red=n/k;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='center';
    for(var b=0;b<=20;b+=4){
      var x=px(b);
      g.strokeStyle=(b===0?'#c2d2cc':'#eef4f1'); g.lineWidth=(b===0?1.6:1);
      g.beginPath(); g.moveTo(x,Y0-8); g.lineTo(x,Y0+5*46+8); g.stroke();
      g.fillStyle='#93a89f'; g.fillText(b===0?'1×':'10'+b, x, Y0+5*46+24);
    }

    for(var i=0;i<CODES.length;i++){
      var v=Math.log(CODES[i][1])/Math.LN10;
      var y=Y0+i*46+10;
      g.fillStyle='#2a5a4a'; g.globalAlpha=0.85;
      g.fillRect(X0, y, Math.max(px(v)-X0,3), 26);
      g.globalAlpha=1;
      g.fillStyle='#2b3d36'; g.textAlign='right';
      g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.fillText(CODES[i][0], X0-14, y+18);
      g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';
      g.textAlign='left'; g.fillStyle='#4a6a5c';
      g.fillText(CODES[i][1]<100?CODES[i][1].toFixed(1)+'×':CODES[i][1].toExponential(0)+'×', px(v)+8, y+18);
    }
    var vu=Math.log(red)/Math.LN10, yu=Y0+4*46+10;
    g.fillStyle='#8a4a2a'; g.globalAlpha=0.9;
    g.fillRect(X0, yu, Math.max(px(vu)-X0,3), 26);
    g.globalAlpha=1;
    g.fillStyle='#6d3a1e'; g.textAlign='right';
    g.font='bold 12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText('the cosmic horizon', X0-14, yu+18);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.textAlign='left';
    g.fillText(red.toExponential(2)+'×', px(vu)+8, yu+18);

    g.fillStyle='#7d9188'; g.textAlign='center';
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText('redundancy  n / k  (physical bits ÷ logical bits)', (X0+X1)/2, Y0+5*46+48);

    vs.textContent='10^'+lS.toFixed(1);
    ro.textContent='S_obs/k_B = 10^'+lS.toFixed(1)+
      '　→　logical bits k = '+k.toExponential(2)+
      '　redundancy '+red.toExponential(2)+'　rate '+(1/red).toExponential(2)+
      '　/　'+(red/1e3).toExponential(2)+'× the surface code'+
      (Math.abs(lS-104.5)<0.06?'　★ default (Egan & Lineweaver 2010)':'');
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-23-code.html', acc='#2a5a4a', ops='#8a4a2a',
      title='The horizon as error correction ── c·t = const, That Clicks, Episode 23',
      ep='EPISODE 23 ／ The same number, read inside out',
      eyebrow='An occupancy of \\(10^{-18}\\) is, in the language of codes, a redundancy of \\(10^{18}\\)',
      h1='The horizon as<br>error correction',
      sub='Is it empty, or is the same information written over and over?<br><em>Until you name the comparison, the two cannot be distinguished.</em>',
      byline_l='What you need: division, the definition of code rate',
      byline_r='redundancy \\(n/k=6.6\\times10^{17}\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 23 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The code rate \\(R=k/n\\) and the Singleton bound (classical \\(d\\le n-k+1\\); quantum \\(d\\le(n-k)/2+1\\)) are standard. The values \\(n=2.96\\times10^{122}\\) (Episode 1), \\(k=S_{\\rm obs}/\\ln2=4.47\\times10^{104}\\) (Episode 6, from \\(S_{\\rm obs}=3.1\\times10^{104}k_B\\), Egan &amp; Lineweaver 2010), the rate \\(1.51\\times10^{-18}\\), the redundancy \\(6.61\\times10^{17}\\), and the area per logical bit \\(4.79\\times10^{-52}\\ \\mathrm{m^2}\\) (side \\(2.19\\times10^{-26}\\) m) are computed here (kenshou/calc27.py). <strong>This document does not claim that the universe is an error-correcting code</strong> — the formulation of AdS/CFT as quantum error correction (Almheiri, Dong &amp; Harlow 2015) concerns the AdS boundary, and <em>whether a cosmological horizon has the same structure is unsettled</em> (de Sitter/FLRW holography is not established). Setting \\(k=S_{\\rm obs}/\\ln2\\) is a crude identification, and reading thermodynamic entropy as "logical bits to be protected" is not obvious (entropy is arguably a measure of lost information). \\(S_{\\rm obs}\\) carries order-of-magnitude uncertainty, which the slider illustrates. The Singleton bound is an upper bound, distinct from achievability. The surface code\'s \\(10^3\\) is indicative and moves between \\(10^2\\) and \\(10^4\\). §04\'s "empty or redundant" is this series\' reading, not a rigorous demonstration of observational equivalence. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the entropy estimate and the redundancy moves with it. "Show the answer" opens each solution.')
