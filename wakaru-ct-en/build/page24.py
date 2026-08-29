# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Episode 17 counted "the agreement needed 20 KB; the problem was that there was no channel". So how <em>wide</em> is the channel? Episode 1 gave \(dN/dt=1.36\times10^{105}\) bit/s, but that is <strong>the rate at which capacity grows</strong>, not a communication speed. Today we compute the bandwidth itself — and between the two numbers there falls out <em>a rather clean identity</em>.</p>

<h2><span class="n">01</span>Two different "bits per second"</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Meaning</th><th class="mid">Value</th></tr></thead>
<tbody>
<tr><th>\(dN/dt\)</th><td class="mid">rate at which capacity grows (Episode 1)</td><td class="mid">\(1.36\times10^{105}\) bit/s</td></tr>
<tr class="hi"><th>\(C\)</th><td class="mid"><strong>channel capacity</strong> (today)</td><td class="mid"><strong>\(6.79\times10^{104}\) bit/s</strong></td></tr>
</tbody>
</table>
</div>

<p>The bandwidth comes from dividing the Bekenstein bound by the time a signal takes to cross. Information in a system of radius \(R\) is at most \(S\le2\pi ER/\hbar c\), and the crossing time is \(R/c\), so —</p>

<div class="calc">
<span class="tag">Channel capacity</span>
$$C\ \le\ \frac{2\pi ER/\hbar c}{R/c}=\frac{2\pi E}{\hbar}\ [\text{nat/s}]\qquad\Longrightarrow\qquad C=\frac{2\pi E}{\hbar\ln2}\ [\text{bit/s}]$$
<p class="lbl">with the total energy inside the horizon \(E=7.90\times10^{69}\) J</p>
$$C=6.79\times10^{104}\ \mathrm{bit/s}$$
</div>

<h2><span class="n">02</span>The heart — bandwidth × age = memory</h2>

<p>The ratio of the two numbers is exactly 2.000000. Not a coincidence.</p>

<div class="calc">
<span class="tag">Three lines</span>
<p class="lbl">substituting \(E=c^4R/2G\) and \(\ell_P^2=\hbar G/c^3\)</p>
$$C=\frac{2\pi}{\hbar\ln2}\cdot\frac{c^4R}{2G}=\frac{\pi cR}{\ell_P^2\ln2}$$
<p class="lbl">while \(N=\pi R^2/(\ell_P^2\ln2)\) with \(R=ct\), so</p>
$$C\cdot t=\frac{\pi cR}{\ell_P^2\ln2}\cdot\frac{R}{c}=\frac{\pi R^2}{\ell_P^2\ln2}=N$$
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
$$\boxed{\ C\cdot t=N\ }$$
<p style="margin:10px 0 0"><strong>The universe has exactly enough bandwidth to move its entire memory once per Hubble time.</strong><br>
── No more and no less: <em>exactly once</em>.</p>
</div>

<p>And since \(N\propto t^2\), \(dN/dt=2N/t=2C\) — the factor of two between Episode 1's number and today's was <strong>two faces of the same identity</strong>.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Reading</th><th class="mid">Formula</th><th class="mid">Meaning</th></tr></thead>
<tbody>
<tr class="hi"><th>as bandwidth</th><td class="mid">\(C\cdot t=N\)</td><td class="mid">one full pass of memory per Hubble time</td></tr>
<tr><th>as capacity growth</th><td class="mid">\(dN/dt=2C\)</td><td class="mid">memory grows at twice the rate it can be moved</td></tr>
</tbody>
</table>
</div>

<p>By Episode 19's classification this is an <strong>identity — 0 bits of surprise</strong>. It follows automatically from \(E=c^4R/2G\) (Dirac's large numbers) and holography. <em>It can still be used to read the design of the universe-as-computer.</em></p>

<h2><span class="n">03</span>Episode 17's 20 KB could have been sent instantly</h2>

<p>With bandwidth in hand we can settle Episode 17's homework — how long would the "20 KB to be agreed on" have taken to send?</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Epoch</th><th class="mid">Bandwidth \(C\)</th><th class="mid">Time to send 20 KB</th></tr></thead>
<tbody>
<tr><th>Nucleosynthesis (\(t=1\) s)</th><td class="mid">\(1.56\times10^{87}\) bit/s</td><td class="mid">\(1.0\times10^{-82}\) s</td></tr>
<tr class="hi"><th>Recombination (380,000 yr)</th><td class="mid">\(1.87\times10^{100}\) bit/s</td><td class="mid"><strong>\(8.6\times10^{-96}\) s</strong></td></tr>
<tr><th>Today</th><td class="mid">\(6.79\times10^{104}\) bit/s</td><td class="mid">\(2.4\times10^{-100}\) s</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §03</p>
<p style="margin:6px 0 0">Given a channel, the horizon problem's 20 KB could have been sent in <strong>\(10^{-96}\) seconds</strong>.<br>
<em>The problem was never bandwidth but the absence of a channel</em> — Episode 17's conclusion, confirmed numerically.</p>
</div>

<div class="fig">
<p class="cap">Figure: bandwidth \(C\) by epoch (slope 1) against the memory \(N\) at that time (slope 2). <strong>Since \(C\cdot t=N\), the two lines are always separated by exactly \(t\)</strong>. Move the slider to read off how long 20 KB takes to send.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Which epoch, \(\log_{10}(t/\mathrm{s})\) (right edge = today)<input id="st" type="range" min="-440" max="180" value="180" step="1"></label>
  <span class="val" id="vt">today</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1a4a3a"></i>memory \(N\) (slope 2)</span>
  <span><i class="swatch" style="background:#a04a2a"></i>bandwidth \(C\) (slope 1)</span>
  <span><i class="swatch" style="background:#9ab0a6"></i>Episode 17's 20 KB</span>
</div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>Bandwidth per particle</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>System</th><th class="mid">Energy</th><th class="mid">Bandwidth in principle</th></tr></thead>
<tbody>
<tr class="hi"><th>One CMB photon</th><td class="mid">\(2.35\times10^{-4}\) eV</td><td class="mid"><strong>\(3.2\times10^{12}\) bit/s</strong></td></tr>
<tr><th>One proton</th><td class="mid">938 MeV</td><td class="mid">\(1.3\times10^{25}\) bit/s</td></tr>
<tr><th>1 kg of matter</th><td class="mid">\(9.0\times10^{16}\) J</td><td class="mid">\(7.7\times10^{51}\) bit/s</td></tr>
</tbody>
</table>
</div>

<p><strong>A single CMB photon could in principle carry three trillion bits per second.</strong> What it actually carries is a few bits (temperature and polarisation) — the same picture again of "capability entirely unused".</p>

<div class="calc">
<span class="tag">Comparing with what humans built</span>
<p class="lbl">total world internet traffic (roughly)</p>
$$1.3\times10^{15}\ \mathrm{bit/s}$$
<p class="lbl">against the in-principle bandwidth of 1 kg of matter</p>
$$1.7\times10^{-37}\qquad(\text{against the horizon, }1.9\times10^{-90})$$
</div>

<h2><span class="n">05</span>The reveal — the underuse is not a shortfall of capability</h2>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>Bandwidth is one memory pass per Hubble time</strong><span>\(C\cdot t=N\). The power to move things is provided exactly as needed</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>Yet only 0.035 operations per bit are performed</strong><span>Episode 1 — and 95% of that goes to components in which nothing happens (Episode 22)</span></div></div>
<div class="row hi"><div class="mk">③</div><div class="txt"><strong>So "unused" is not a shortfall of capability</strong><span>bandwidth and capacity both suffice; they are simply not used — <em>the universe has power to spare</em></span></div></div>
</div>

<p>Episode 6: "only \(10^{-18}\) of the memory is used". Episode 22: "95% of the operational budget goes to components in which nothing happens". Today: "bandwidth is one memory pass". <strong>Three routes to the same conclusion</strong> — the universe as a computer is <em>doing overwhelmingly little relative to its specification</em>.</p>

<div class="aside">
<span class="tag">Then what is the bottleneck?</span>
If not performance, what limits it? Episode 17 had the answer — <strong>not the channel's width but its existence</strong>. Cut causally, not one bit crosses even with \(10^{100}\) bit/s available. <em>The bottleneck of the universe-as-computer is neither bandwidth nor capacity but wiring — the causal structure.</em> And the wiring is set by the expansion law — as Episode 17 showed, only \(a\propto t\) adds no nodes.
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① \(C=2\pi E/(\hbar\ln2)\) is the Bekenstein bound divided by a crossing time.</strong> It is the same kind of quantity as the Bremermann limit, but the coefficient depends on how the derivation is set up (the shape of the boundary, the choice of \(R\)) — factors of order \(\pi\) move. It differs from Episode 1's Margolus–Levitin limit (\(2E/\pi\hbar\)) by \(\pi^2\), which is also a matter of convention.</p>
<p style="margin:0 0 10px"><strong>② \(C\cdot t=N\) is an identity</strong> (0 bits of surprise by Episode 19). It follows automatically from the Dirac large-number identity \(E=c^4R/2G\) and holography \(N\propto R^2\). <em>It is not a physical claim that the universe "provides exactly the right bandwidth".</em></p>
<p style="margin:0 0 10px"><strong>③ The send times in §03 divide by bandwidth alone.</strong> In reality the signal also needs time to cross the distance (\(R/c\) — 380,000 years at recombination). <em>The calculation is there to show that bandwidth is not the bottleneck</em>, not to say that 20 KB arrives in \(10^{-96}\) s.</p>
<p style="margin:0 0 10px"><strong>④ "Three trillion bits per second per CMB photon" is likewise an in-principle bound.</strong> A real photon carries its frequency, polarisation and direction of arrival — a few bits.</p>
<p style="margin:0"><strong>⑤ The \(1.3\times10^{15}\) bit/s of internet traffic is an order-of-magnitude marker</strong>, moving by factors of a few with what counts as traffic.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>State the difference between \(dN/dt\) and \(C\).
<details><summary>Show the answer</summary><div class="ans">\(dN/dt\) is <strong>the rate at which capacity grows</strong> (how much new writable space appears); \(C\) is <strong>the channel capacity</strong> (how much existing information can be moved). Entirely different quantities, joined by the identity \(dN/dt=2C\).</div></details></li>

<li>Show that \(C\cdot t=N\).
<details><summary>Show the answer</summary><div class="ans">Substituting \(E=c^4R/2G\) and \(\ell_P^2=\hbar G/c^3\) into \(C=2\pi E/(\hbar\ln2)\) gives \(C=\pi cR/(\ell_P^2\ln2)\). Multiplying by \(t=R/c\) gives \(\pi R^2/(\ell_P^2\ln2)=N\). <strong>One full memory pass per Hubble time.</strong></div></details></li>

<li>How long does 20 KB take to send at recombination?
<details><summary>Show the answer</summary><div class="ans">\(C=1.87\times10^{100}\) bit/s, so \(1.6\times10^5/1.87\times10^{100}=8.6\times10^{-96}\) s. <strong>Bandwidth is not remotely the bottleneck</strong> — confirming Episode 17's "the problem is the existence of a channel".</div></details></li>

<li>What is one CMB photon's in-principle bandwidth?
<details><summary>Show the answer</summary><div class="ans">\(C=2\pi E/(\hbar\ln2)\) with \(E=2.35\times10^{-4}\) eV \(=3.76\times10^{-23}\) J gives <strong>\(3.2\times10^{12}\) bit/s</strong>. What it actually carries is a few bits.</div></details></li>

<li>(Harder) What is the bottleneck of the universe-as-computer?
<details><summary>Show the answer</summary><div class="ans"><strong>The wiring (causal structure).</strong> Only \(10^{-18}\) of the capacity is used (Episode 6), 95% of the operational budget goes to components in which nothing happens (Episode 22), and bandwidth provides one memory pass (today) — <em>performance is everywhere in surplus</em>. What limits it is that with no causal connection not one bit crosses however much bandwidth there is (Episode 17). And the wiring is set by the expansion law.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — bandwidth × age = memory</h2>
<p>We distinguished two "bits per second" — \(dN/dt=1.36\times10^{105}\) bit/s is <em>the rate at which capacity grows</em>, while \(C=2\pi E/(\hbar\ln2)=6.79\times10^{104}\) bit/s is <em>the channel capacity</em>, obtained by dividing the Bekenstein bound by a crossing time.</p>
<p>The ratio is exactly 2.000000, and it is an identity — \(E=c^4R/2G\) and holography give \(C=\pi cR/(\ell_P^2\ln2)\), hence <strong>\(C\cdot t=N\)</strong>. <em>The universe has exactly enough bandwidth to move its entire memory once per Hubble time</em> — no more, no less. The factor of two against Episode 1 is just the flip side of \(N\propto t^2\).</p>
<p>That settles Episode 17's homework. At recombination's bandwidth, the horizon problem's 20 KB could be sent in <strong>\(10^{-96}\) seconds</strong>. <em>Bandwidth is not remotely the bottleneck</em> — the problem was not the channel's width but its <strong>existence</strong>.</p>
<p>And three routes converge: only \(10^{-18}\) of the capacity is used (Episode 6), 95% of the operational budget goes to components in which nothing happens (Episode 22), and bandwidth provides a full memory pass (today). <strong>"Unused" is not a shortfall of capability.</strong> The bottleneck of the universe-as-computer is neither bandwidth nor capacity but <em>wiring — the causal structure</em>, which the expansion law determines.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 25</span>
Two episodes left in Part III. Next we take seriously the question <strong>whether physical laws are a compression algorithm</strong>. Episode 5 noted that "\(\Lambda\)CDM explains \(6.3\times10^6\) multipoles with six parameters" — <em>a compression ratio of \(10^6\)</em>. And the Standard Model? Nineteen parameters for every cross section ever measured. And general relativity? <strong>Zero parameters.</strong> <em>Rank physical laws by compression ratio and which comes out best</em> — and <strong>theories that compress too well share a common weakness.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var st=document.getElementById('st'), vt=document.getElementById('vt'), ro=document.getElementById('ro');
  var X0=78, X1=700, Y0=30, Y1=314;
  var c=299792458.0, lP=1.616255e-35, ln2=Math.log(2), PI=Math.PI;
  var xmin=-45, xmax=19, ymin=-5, ymax=130;
  var BITS=1.6e5;
  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function lg(v){ return Math.log(v)/Math.LN10; }
  function Nof(t){ var R=c*t; return PI*R*R/(lP*lP*ln2); }
  function Cof(t){ var R=c*t; return PI*c*R/(lP*lP*ln2); }
  function draw(){
    var lt=parseInt(st.value,10)/10;
    var t=Math.pow(10,lt);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.textAlign='right';
    for(var e=0;e<=130;e+=20){
      var y=py(e);
      g.strokeStyle='#eef3f0'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#93a89c'; g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    for(var q=-40;q<=10;q+=10){
      var x=px(q);
      g.strokeStyle='#f5f9f6'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#93a89c'; g.fillText('10'+q, x, Y1+16);
    }
    g.strokeStyle='#c3d6c9'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();
    g.strokeStyle='#9ab0a6'; g.lineWidth=1.8; g.setLineDash([6,5]);
    g.beginPath(); g.moveTo(X0,py(lg(BITS))); g.lineTo(X1,py(lg(BITS))); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#7d938a'; g.textAlign='left';
    g.fillText('Episode 17’s 20 KB (1.6×10⁵ bit)', X0+10, py(lg(BITS))-7);
    function curve(fn,col,w){
      g.strokeStyle=col; g.lineWidth=w; g.beginPath();
      var first=true;
      for(var i=0;i<=300;i++){
        var lx=xmin+(xmax-xmin)*i/300;
        var y=lg(fn(Math.pow(10,lx)));
        if(y<ymin||y>ymax){ first=true; continue; }
        if(first){ g.moveTo(px(lx),py(y)); first=false; } else g.lineTo(px(lx),py(y));
      }
      g.stroke();
    }
    curve(Nof,'#1a4a3a',3.2);
    curve(Cof,'#a04a2a',3.2);
    g.textAlign='left';
    g.fillStyle='#1a4a3a'; g.fillText('memory N (slope 2)', px(-8), py(lg(Nof(1e-8)))-10);
    g.fillStyle='#a04a2a'; g.fillText('bandwidth C (slope 1)', px(-8), py(lg(Cof(1e-8)))+18);
    g.strokeStyle='#5a7a68'; g.lineWidth=1.5; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(lt),Y0); g.lineTo(px(lt),Y1); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#7d938a'; g.textAlign='center';
    g.fillText('age of the universe  t [s]', (X0+X1)/2, Y1+36);
    var C=Cof(t), N=Nof(t);
    vt.textContent = (lt>17.5?'today':'10^'+lt.toFixed(1)+' s');
    ro.textContent='t = '+t.toExponential(2)+' s　'+
      'memory '+N.toExponential(2)+' bit　bandwidth '+C.toExponential(2)+' bit/s'+
      '　→　C×t = '+(C*t).toExponential(2)+' (= N)'+
      '　/　20 KB takes '+(BITS/C).toExponential(2)+' s';
  }
  st.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-24-channel.html', acc='#1a4a3a', ops='#a04a2a',
      title='How many bits per second cross the horizon? ── c·t = const, That Clicks, Episode 24',
      ep='EPISODE 24 ／ The rate capacity grows is not a communication speed',
      eyebrow='Bandwidth × age = memory — exactly one pass',
      h1='How many bits per second<br>cross the horizon?',
      sub='Episode 17 said "there was no way to send the 20 KB". Here is the bandwidth.<br><em>And bandwidth turns out not to be the bottleneck at all.</em>',
      byline_l='What you need: the Bekenstein bound, division',
      byline_r='\\(C\\cdot t=N\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 24 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The Bekenstein bound \\(S\\le2\\pi ER/\\hbar c\\) is standard, and dividing it by a crossing time \\(R/c\\) to obtain a channel capacity \\(C=2\\pi E/(\\hbar\\ln2)\\) is the same kind of construction as the Bremermann limit, but <strong>the coefficient depends on how the derivation is set up</strong> (the shape of the boundary, the choice of \\(R\\)) — the \\(\\pi^2\\) difference from Episode 1\'s Margolus–Levitin limit (\\(2E/\\pi\\hbar\\)) is likewise conventional. The values \\(C=6.79\\times10^{104}\\) bit/s, \\(C=\\pi cR/(\\ell_P^2\\ln2)\\), and the identities \\(C\\cdot t=N\\) and \\(dN/dt=2C\\) are derived here (kenshou/calc28.py). <strong>These are identities</strong> — they follow automatically from the Dirac large-number identity \\(E=c^4R/2G\\) and holography \\(N\\propto R^2\\) — and are not a physical claim that the universe "provides exactly the right bandwidth" (0 bits of surprise by Episode 19\'s classification). The send times in §03 divide by bandwidth alone; <em>the time for a signal to cross the distance (380,000 years at recombination) is additional</em> — the calculation is there to show bandwidth is not the bottleneck. The per-particle bandwidths are likewise in-principle bounds; a real CMB photon carries a few bits (frequency, polarisation, direction). The internet\'s \\(1.3\\times10^{15}\\) bit/s is an order-of-magnitude marker. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination, and \\(R_H=ct\\) is its convention (in \\(\\Lambda\\)CDM, \\(R_H=c/H_0\\) differs from the particle horizon). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider moves through epochs while C×t=N is preserved. "Show the answer" opens each solution.')
