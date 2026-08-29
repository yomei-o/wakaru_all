# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
from mkpage import build

BODY = r'''<p class="lead">The previous series, "Conformal Transformations That Click", closed by ruling that \(c\cdot t=\text{const}\) was <em>flawless as a way of speaking, disqualified as a model</em>. This new series digs into the one thing left over there — <strong>that \(c\cdot t=\text{const}\) is what physics looks like seen through information theory</strong>. We begin by taking the specifications of the machine: memory, clock, operation count. Line all three up, divide them, and the most basic quantity in cosmology comes back wearing a completely different face.</p>

<h2><span class="n">01</span>Memory — how many bits fit on the horizon</h2>

<p>The first specification of any computer is its memory. For the universe, the holographic principle already has the answer: information is written not on the volume but on the <strong>area</strong>. Divide the horizon area \(A\) by the Planck area, then by \(4\ln 2\), and you have a bit count.</p>

<div class="calc">
<span class="tag">Calculation — memory</span>
<p class="lbl">Bits on the horizon</p>
$$N=\frac{A}{4\ell_P^2\ln 2}=\frac{\pi}{\ln 2}\left(\frac{R_H}{\ell_P}\right)^2$$
<p class="lbl">Numbers (\(R_H=c\,t_0=1.305\times10^{26}\) m, \(\ell_P=1.616\times10^{-35}\) m)</p>
$$\frac{R_H}{\ell_P}=8.075\times10^{60}\qquad\Longrightarrow\qquad N=2.956\times10^{122}\ \text{bit}$$
</div>

<p>That is the entire memory of the universe. All the storage on Earth comes to something like \(10^{22}\) bits, so this is \(10^{100}\) times more.</p>

<h2><span class="n">02</span>Clock — how many ticks have gone by</h2>

<p>The second specification is the clock. Count one Planck time as one tick.</p>

<div class="calc">
<span class="tag">Calculation — clock</span>
$$\frac{t_0}{t_P}=\frac{4.354\times10^{17}\,\mathrm{s}}{5.391\times10^{-44}\,\mathrm{s}}=8.075\times10^{60}\ \text{ticks}$$
<p class="lbl">Counted logarithmically</p>
$$\ln\frac{t_0}{t_P}=140.2$$
</div>

<p>You will have noticed that \(R_H/\ell_P\) for the memory and \(t_0/t_P\) for the clock came out as the same \(8.075\times10^{60}\). That is <strong>"one cell per tick"</strong> from bonus episode ③ of the previous series — \(dR_H/dt=c\), which is to say \(c\cdot t=\text{const}\) itself. We leave that alone here and press on.</p>

<div class="aside">
<span class="tag">The logarithm may be the real clock</span>
The number 8×10⁶⁰ is less meaningful, as a machine specification, than \(\ln(t_0/t_P)=140\). The history of the universe is not "10⁶⁰ repetitions of the same operation" but <strong>140 doublings</strong>. Indeed, memory grows by a factor of \(e^2=7.39\) per logarithmic tick (since \(N\propto t^2\)); raise that to the 140th and you get \(e^{280}\approx10^{122}\) — the memory figure comes back exactly. <strong>The universe is a machine that has run only 140 steps.</strong>
</div>

<h2><span class="n">03</span>Operations — how many times has the state changed</h2>

<p>The third specification is the operation count. The physical floor on "one operation" is the <strong>Margolus–Levitin limit</strong>: a system of energy \(E\) needs at least \(\pi\hbar/2E\) to move to an orthogonal state. So the rate of operations is bounded by \(2E/\pi\hbar\).</p>

<p>The total energy inside the horizon is, in any flat FLRW universe, \(E=Mc^2=c^4R_H/2G\) — the identity from §06 of bonus episode ③ (the one that turned out to be the real content of Dirac's large-number hypothesis). Writing the expansion law as \(a\propto t^{p}\) gives \(R_H=ct/p\), so the rate grows in proportion to time.</p>

<div class="calc">
<span class="tag">Calculation — operations, in three lines</span>
<p class="lbl">① The rate</p>
$$\frac{d\Omega}{dt}=\frac{2E}{\pi\hbar}=\frac{c^4R_H}{\pi\hbar G}=\frac{c^5\,t}{\pi\hbar G\,p}$$
<p class="lbl">② Integrate</p>
$$\Omega=\frac{c^5t^2}{2\pi\hbar G\,p}$$
<p class="lbl">③ Use \(\ell_P^2=\hbar G/c^3\) and every unit cancels</p>
$$\Omega=\frac{1}{2\pi p}\left(\frac{ct}{\ell_P}\right)^2$$
</div>

<p>Putting in numbers for \(p=1\) (that is, \(c\cdot t=\text{const}\)) gives \(\Omega=1.038\times10^{121}\) operations — the same order as Lloyd's well-known estimate (2002) that the universe has performed \(10^{120}\) operations.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The core — divide the memory by the operations</h2>

<p>Three specifications in hand. When you judge a computer, this is the number you most want to see: <strong>how many operations per bit?</strong> Is it a machine that is all memory and no work, or the other way round?</p>

<p>Try it, and something surprising happens.</p>

<div class="calc">
<span class="tag">Calculation — just divide</span>
$$\frac{\Omega}{N}=\frac{1}{2\pi p}\left(\frac{ct}{\ell_P}\right)^{2}\ \Bigg/\ \frac{\pi}{\ln 2}\left(\frac{ct}{p\,\ell_P}\right)^{2}
=\frac{p\,\ln 2}{2\pi^{2}}$$
</div>

<p><strong>The \(t\) has cancelled cleanly.</strong> Memory and operation count both grow as \(t^2\), so the ratio does not depend on the age of the universe. One second after the beginning, today, or \(10^{100}\) years from now, the number of operations per bit is <em>exactly the same</em>.</p>

<p>And what is left, \(p\), is the expansion law itself. Substituting the relation to the equation of state, \(p=2/3(1+w)\) —</p>

<div class="keybox">
<p class="lbl">The result of this episode</p>
$$\boxed{\ \frac{\Omega}{N}=\frac{\ln 2}{3\pi^{2}\,(1+w)}\ }$$
<p style="margin:10px 0 0">The number of operations per bit is <strong>a pure number fixed by the equation of state alone</strong>. It does not depend on the age of the universe, nor its size, nor any detail of its contents.</p>
</div>

<p>The most basic quantity in cosmology (the equation of state) and the most basic ratio in computer science (operations divided by memory) are one and the same number.</p>

<div class="aside">
<span class="tag">Run it through the decision procedure</span>
Following the method of the previous series' finale, sort this quantity into one of two columns. Both \(\Omega\) and \(N\) are <strong>plain counts</strong>; they have no dimensions. So a conformal transformation — a change of ruler — leaves them alone: <strong>right-hand column, physics</strong>. And not merely unmoved: it reads off \(w\) directly. Which means <em>"measuring the expansion law of the universe" and "measuring its computational efficiency" are the same job</em>.
</div>

<h2><span class="n">05</span>Four universes, side by side</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Universe</th><th class="mid">\(w\)</th><th class="mid">\(p\)</th><th class="mid">\(\Omega/N\)</th><th class="mid">one operation per…</th></tr></thead>
<tbody>
<tr><th>stiff (kination)</th><td class="mid">\(+1\)</td><td class="mid">1/3</td><td class="mid">0.01171</td><td class="mid">85.4 bits</td></tr>
<tr><th>radiation</th><td class="mid">\(+1/3\)</td><td class="mid">1/2</td><td class="mid">0.01756</td><td class="mid">57.0 bits</td></tr>
<tr><th>matter</th><td class="mid">\(0\)</td><td class="mid">2/3</td><td class="mid">0.02341</td><td class="mid">42.7 bits</td></tr>
<tr class="hi"><th>\(c\cdot t=\)const</th><td class="mid">\(-1/3\)</td><td class="mid">1</td><td class="mid"><strong>0.03512</strong></td><td class="mid"><strong>28.5 bits</strong></td></tr>
<tr><th>de Sitter</th><td class="mid">\(-1\)</td><td class="mid">∞</td><td class="mid">diverges</td><td class="mid">grows with time</td></tr>
</tbody>
</table>
</div>

<p>Not one of them comes close to 1. <strong>In 13.8 billion years the universe has never once performed one operation per bit.</strong> Nor is that because it is young: the ratio does not depend on time, so <em>it has always been like this</em>.</p>

<h2><span class="n">06</span>The eighth characterisation</h2>

<p>Let us restate the \(c\cdot t=\text{const}\) row a little more precisely. Since \(p=ct/R_H\), the boxed result can be written like this:</p>

<div class="calc">
<span class="tag">The same formula, as a ratio</span>
$$\frac{\Omega}{N}=\frac{\ln 2}{2\pi^{2}}\cdot\frac{ct}{R_H}$$
<p class="lbl">and therefore</p>
$$R_h=ct\qquad\Longleftrightarrow\qquad \frac{\Omega}{N}=\frac{\ln 2}{2\pi^{2}}=0.0351152\cdots$$
</div>

<p>Bonus episode ③ of the previous series listed seven characterisations of \(a\propto t\) and remarked that "having this many properties meet at a single point is itself remarkable". We can add an eighth.</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>The potential is a pure quadratic</strong><span>\(U=-\phi^2/2t_0^2\) (Conformal Transformations, Ep.5)</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>Conformal time spans all of \((-\infty,\infty)\)</strong><span>it covers the whole of Minkowski space (Ep.6)</span></div></div>
<div class="row"><div class="mk">③</div><div class="txt"><strong>Zero acceleration</strong><span>\(\ddot a=0\); the watershed for the horizon problem (Ep.5)</span></div></div>
<div class="row"><div class="mk">④</div><div class="txt"><strong>The comoving Hubble radius is constant</strong><span>the address space does not move (bonus ②)</span></div></div>
<div class="row"><div class="mk">⑤</div><div class="txt"><strong>Both the particle horizon and the event horizon are infinite</strong><span>read and write access to the whole memory</span></div></div>
<div class="row"><div class="mk">⑥</div><div class="txt"><strong>\(dR_H/dt=c\), cell count = tick count</strong><span>one cell per tick (bonus ③)</span></div></div>
<div class="row"><div class="mk">⑦</div><div class="txt"><strong>Saturation of the strong energy condition</strong><span>\(\rho+3p=0\); the boundary of the singularity theorems (bonus ③)</span></div></div>
<div class="row hi"><div class="mk">⑧</div><div class="txt"><strong>Operations per bit equal \(\ln 2/2\pi^2\)</strong><span>the ratio of operations to memory matches the ratio of distance-light-has-travelled to horizon radius (this episode)</span></div></div>
</div>

<p>⑥ and ⑧ are two faces of the same fact. What ⑥ says in "lengths and times", ⑧ says in "operations and bits" — <em>the dimensionful phrasing and the dimensionless one</em>. By the decision procedure of the previous series, ⑧ sits in the right-hand column.</p>

<h2><span class="n">07</span>So is there a universe that reaches "1"?</h2>

<p>Solve the boxed result backwards. Demanding \(\Omega/N=1\) gives —</p>

<div class="calc">
<span class="tag">Solving backwards</span>
$$1+w=\frac{\ln 2}{3\pi^{2}}=0.02341\qquad\Longrightarrow\qquad \boxed{\,w=-0.97659\,}$$
</div>

<p>Almost exactly \(-1\): <strong>just short of a cosmological constant</strong>. And the equation of state observed for dark energy is \(w=-1.03\pm0.03\) — <em>already on the far side of it</em>.</p>

<p>The universe has just entered its dark-energy-dominated era. Under de Sitter-like expansion \(N\) saturates to a constant while the operation rate does not fall off, so the ratio grows without bound.</p>

<div class="calc">
<span class="tag">The ratio in de Sitter</span>
$$\frac{\Omega}{N}=\frac{\ln 2}{\pi^{2}}\,Ht\qquad\Longrightarrow\qquad
\frac{\Omega}{N}=1\ \text{at}\ Ht=\frac{\pi^{2}}{\ln 2}=14.24$$
<p class="lbl">with \(H_\Lambda=H_0\sqrt{\Omega_\Lambda}=1.81\times10^{-18}\,\mathrm{s^{-1}}\)</p>
$$t\approx2.5\times10^{11}\ \text{years}\qquad(\text{about 250 billion years from now})$$
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0">In 13.8 billion years the universe has <strong>never once performed one operation per bit</strong>.<br>
And it has only just now entered the expansion law that will carry it across that line.</p>
</div>

<div class="fig">
<p class="cap">Figure: the horizontal axis is the logarithmic age of the universe (\(\ln(t/t_P)\); today is 140.2). In a power-law universe the operations-per-bit line is <strong>perfectly flat</strong>, and turning the \(w\) knob only raises or lowers it. The copper dashed line marks one operation per bit — a power-law universe reaches it only once \(w<-0.977\), that is, only just short of a cosmological constant</p>
<canvas id="cv" width="720" height="360"></canvas>
<div class="controls">
  <label>equation of state \(w\) (left = just short of a cosmological constant / right = stiffer than radiation)<input id="sw" type="range" min="-990" max="1000" value="-333" step="1"></label>
  <span class="val" id="vw">w = −0.333</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1c3f63"></i>operations per bit (power law)</span>
  <span><i class="swatch" style="background:#a85a12"></i>one operation per bit</span>
  <span><i class="swatch" style="background:#7a8ba0"></i>the Λ-dominated future</span>
</div>
</div>

<p>Push the knob <strong>left</strong> (\(w\to-1\)) and the flat line rises slowly. Even so it only touches the copper dashes once \(w=-0.977\) is passed — <strong>only just short of a cosmological constant does the machine stop being a bad deal</strong>. Push it right (matter, radiation, stiff) and the line only sinks. The grey dashes are the \(\Lambda\)-dominated future, the one place that is not flat.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">08</span>The reveal — why both were \(t^2\)</h2>

<p>The ratio came out independent of time because both \(N\) and \(\Omega\) went as \(t^2\). That is no accident.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>quantity</th><th>why \(t^2\)</th></tr></thead>
<tbody>
<tr><th>memory \(N\)</th><td>because it is an area: \(N\propto R_H^2\) and \(R_H\propto t\). This <strong>is</strong> the holographic principle</td></tr>
<tr><th>operations \(\Omega\)</th><td>because the rate goes as \(E\propto R_H\propto t\) and you integrate it. The identity <strong>\(E=(c^2R_H/2G)\,c^2\)</strong> is what is doing the work</td></tr>
</tbody>
</table>
</div>

<p>That second identity is the one bonus episode ③ used to dispose of Dirac's large-number hypothesis as "just an identity". <strong>The Hubble radius always equals the Schwarzschild radius of what is inside it.</strong> So the energy of the universe is proportional to its radius, and so is its operation rate.</p>

<div class="calc">
<span class="tag">The chain</span>
$$\underbrace{N\propto R_H^{2}}_{\text{holography}}\qquad
\underbrace{\frac{d\Omega}{dt}\propto E\propto R_H}_{\text{the large-number identity}}\qquad\Longrightarrow\qquad
\frac{\Omega}{N}\propto\frac{\int R_H\,dt}{R_H^{2}}=\text{(a function of the expansion law alone)}$$
</div>

<p><em>"Operations are proportional to memory" is the product of holography and the large-number identity.</em> Neither is special to \(c\cdot t=\text{const}\); both hold in any flat FLRW universe — which is why the division leaves nothing behind but the expansion law.</p>

<h2><span class="n">09</span>An aside — memory is installed faster than work is done</h2>

<div class="calc">
<span class="tag">Today's values (\(p=1\))</span>
$$\frac{dN}{dt}=\frac{2N}{t_0}=1.36\times10^{105}\ \mathrm{bit/s},\qquad
\frac{d\Omega}{dt}=\frac{2\Omega}{t_0}=4.77\times10^{103}\ \mathrm{ops/s}$$
$$\frac{dN/dt}{d\Omega/dt}=\frac{2\pi^{2}}{p\ln 2}=28.5$$
</div>

<p><strong>In the time it takes the universe to perform one operation, it installs 28.5 bits of memory.</strong> As a computer design that is bizarre — memory keeps piling up while the speed of processing what is written on it never comes close to keeping pace. When bonus episode ② of the previous series called the universe <em>extremely memory-rich and clock-poor</em>, this ratio is what it meant. Today that "richness" has a value: \(2\pi^2/\ln2\).</p>

<div class="aside">
<span class="tag">And almost entirely empty</span>
By the count in bonus episode ②, the entropy the universe actually uses is \(1.5\times10^{-18}\) of its capacity. Which is to say — <strong>a machine that performs one operation per 28.5 bits is using \(10^{-18}\) of that memory</strong>. Both writing and computing are nowhere near their limits. The universe is indeed a computer with finite resources, but <em>it is not remotely using up the finite resources it has</em>. What that emptiness means is the subject of Episode 6.
</div>

<div class="caveat">
<span class="tag">Being straight with you</span>
<p style="margin:0 0 10px">"Operation" is defined by the Margolus–Levitin limit as <strong>an upper bound on transitions to orthogonal states</strong>. It is not a claim that meaningful computation is going on, nor that the universe actually runs at that bound — this is <em>a specification sheet, not a benchmark</em>.</p>
<p style="margin:0 0 10px">The coefficients are sensitive to convention. Taking the rate as \(2E/\pi\hbar\) and \(E\) as the total energy inside the horizon \(Mc^2=c^4R_H/2G\) gives \(\Omega=1.04\times10^{121}\); the difference from Lloyd's (2002) \(\sim10^{120}\) is exactly this choice. Whether bits are divided by \(\ln2\) (bits) or not (nats) shifts \(\Omega/N\) by a further factor of 1.44. <strong>So the structure — that it does not depend on time and is fixed by \(w\) alone — is the substance here, not the digits.</strong></p>
<p style="margin:0 0 10px">\(w\) is the effective equation of state of the universe as a whole, not of a single component. The real universe hands off from radiation to matter to \(\Lambda\), so \(\Omega/N\) takes different values over different intervals and would need \(\int R_H dt/R_H^2\) followed numerically. The table idealises "if that \(w\) held forever".</p>
<p style="margin:0">The "about 250 billion years" in §07 approximates everything after today as pure de Sitter. And \(w=-1.03\pm0.03\) comes from a fit assuming constant \(w\); the phantom side (\(w<-1\)) is a region future measurements may still move. "Already on the far side" is <em>a statement about the central value</em>, not a settled fact.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (everything you need is above)</p>
<ol>
<li>How many operations per bit in a radiation-dominated universe (\(w=1/3\))?
<details><summary>Show the answer</summary><div class="ans">\(\Omega/N=\ln2/(3\pi^2\cdot4/3)=\ln2/(4\pi^2)=0.01756\), i.e. <strong>one operation per 57 bits</strong>. Exactly half the \(c\cdot t=\text{const}\) value — radiation is an even less computational universe.</div></details></li>

<li>Why does \(\Omega/N\) not depend on the age of the universe? One line.
<details><summary>Show the answer</summary><div class="ans">Because \(N\propto R_H^2\propto t^2\) (holography) and \(\Omega\propto\int E\,dt\propto\int R_H\,dt\propto t^2\) (from the identity \(E=c^4R_H/2G\)). <strong>Both are the same \(t^2\)</strong>, so all that survives the ratio is information about the expansion law.</div></details></li>

<li>Is \(\Omega/N\) bookkeeping or physics?
<details><summary>Show the answer</summary><div class="ans"><strong>Physics.</strong> \(\Omega\) and \(N\) are plain counts and therefore dimensionless, so a conformal transformation cannot move them. Moreover it determines \(w\) uniquely, so if it did move you would genuinely be in a different universe — right-hand column, by the decision procedure of the previous series' finale.</div></details></li>

<li>Find the \(w\) that gives \(\Omega/N=1\) and say what it means.
<details><summary>Show the answer</summary><div class="ans">\(1+w=\ln2/3\pi^2=0.0234\), so \(w=-0.9766\) — <strong>just short of a cosmological constant</strong>. For a power-law universe to reach one operation per bit it must already be almost fully accelerating; conversely, a universe dominated by matter or radiation is, in principle, a bad computational deal.</div></details></li>

<li>(Harder) Show that ⑥ "one cell per tick" and ⑧ "\(\Omega/N=\ln2/2\pi^2\)" are the same fact.
<details><summary>Show the answer</summary><div class="ans">Write \(\Omega/N=(\ln2/2\pi^2)(ct/R_H)\). Statement ⑥ is \(dR_H/dt=c\); integrating gives \(R_H=ct\), i.e. \(ct/R_H=1\). Substituting yields \(\Omega/N=\ln2/2\pi^2\), and the converse likewise. <strong>"The horizon advances at the speed of light" and "the ratio of operations to memory is \(\ln2/2\pi^2$" are two readings of the single equation \(ct/R_H=1\)</strong> — the first dimensionful, the second dimensionless.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary　Divide, and out comes the equation of state</h2>
<p>Written out as a specification sheet, the universe has memory \(N=\pi(R_H/\ell_P)^2/\ln2=2.96\times10^{122}\) bits, a clock of \(8.08\times10^{60}\) ticks (140 in the logarithm), and \(\Omega=(ct/\ell_P)^2/2\pi p=1.04\times10^{121}\) operations. So far this only re-confirms known estimates. <strong>What was interesting was dividing the memory by the operations.</strong></p>
<p>Both grow as \(t^2\), so time cancels and only the expansion law is left: \(\Omega/N=\ln2/3\pi^2(1+w)\). The number of operations per bit <em>is</em> the equation of state. 1/57 for radiation, 1/42.7 for matter, <strong>1/28.5</strong> for \(c\cdot t=\text{const}\). <em>In 13.8 billion years the universe has never once reached one operation per bit</em> — and since the ratio does not depend on time, it never has at any epoch.</p>
<p>Writing it as \(\Omega/N=(\ln2/2\pi^2)(ct/R_H)\) shows that \(R_h=ct\) is exactly the statement that this ratio equals \(\ln2/2\pi^2\) — an <strong>eighth</strong> entry for the seven characterisations of bonus episode ③, the dimensionless counterpart of ⑥ "one cell per tick". Reaching "1" would require \(w=-0.977\), and the dark energy we observe is on the far side of that. Under a pure de Sitter approximation the universe first exceeds one operation per bit in about 250 billion years.</p>
<p>The reveal was two identities — memory goes as \(t^2\) because of <strong>holography</strong>, operations go as \(t^2\) because the <strong>Hubble radius equals the Schwarzschild radius of its contents</strong> (Dirac's large numbers). Both hold in any flat FLRW universe, so the division leaves nothing but the expansion law. And as an aside: memory is installed \(2\pi^2/\ln2=28.5\) times faster than operations are performed, on memory that is only \(10^{-18}\) used.</p>
</div>

<div class="next">
<span class="lbl">Next time ── Episode 2</span>
This time the universe turned out to be "a machine that performs one operation per 28.5 bits". Next we dig into the clock — <strong>why 140?</strong> The number \(\ln(t_0/t_P)=140.2\) is the step count of the universe measured logarithmically. And in bonus episode ⑦ of the previous series we counted the renormalisation-group anomaly coefficient \(a\) falling by a factor of 16.06 from the Planck scale to today. Divide the two and you get <strong>2% per step</strong> — the universe forgets 2% of its degrees of freedom every logarithmic tick. The a-theorem ("coarse-graining reduces entanglement") acquires a clock.
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sw=document.getElementById('sw'), vw=document.getElementById('vw'), ro=document.getElementById('ro');
  var LN2=Math.log(2), PI=Math.PI;
  var X0=64, X1=696, Y0=28, Y1=316;
  var xmin=0, xmax=200, ymin=-2.6, ymax=0.7, TODAY=140.24;
  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }
  function opsbit(w){ return LN2/(3*PI*PI*(1+w)); }
  function draw(){
    var w=parseInt(sw.value,10)/1000, p=2/(3*(1+w)), v=opsbit(w);
    var ly=Math.log(v)/Math.LN10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px sans-serif';
    for(var e=-3;e<=0;e++){
      if(e<ymin) continue;
      var y=py(e);
      g.strokeStyle='#e8eef5'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      g.fillStyle='#8a93a3'; g.textAlign='right';
      g.fillText(e===0?'1':'10'+e, X0-8, y+4);
    }
    g.textAlign='center';
    [0,40,80,120,160,200].forEach(function(t){
      var x=px(t);
      g.strokeStyle='#eef3f8'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#8a93a3'; g.fillText(String(t), x, Y1+16);
    });
    g.strokeStyle='#c9d4e2'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();
    g.strokeStyle='#a85a12'; g.lineWidth=2; g.setLineDash([7,5]);
    g.beginPath(); g.moveTo(X0,py(0)); g.lineTo(X1,py(0)); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#a85a12'; g.textAlign='left';
    g.fillText('one operation per bit', X0+8, py(0)-7);
    g.strokeStyle='#7a8ba0'; g.lineWidth=2; g.setLineDash([3,4]);
    g.beginPath(); var started=false;
    for(var x=TODAY;x<=xmax;x+=0.5){
      var val=(LN2/(PI*PI))*(x-TODAY);
      if(val<=0) continue;
      var yy=Math.log(val)/Math.LN10;
      if(yy<ymin) continue;
      if(!started){ g.moveTo(px(x),py(Math.min(yy,ymax))); started=true; }
      else g.lineTo(px(x),py(Math.min(yy,ymax)));
    }
    g.stroke(); g.setLineDash([]);
    g.fillStyle='#7a8ba0'; g.fillText('Λ-dominated future', px(153), py(-0.62));
    var yh=Math.max(Math.min(ly,ymax),ymin);
    g.strokeStyle='#1c3f63'; g.lineWidth=3;
    g.beginPath(); g.moveTo(X0,py(yh)); g.lineTo(px(TODAY),py(yh)); g.stroke();
    g.strokeStyle='rgba(28,63,99,.28)'; g.lineWidth=3; g.setLineDash([4,5]);
    g.beginPath(); g.moveTo(px(TODAY),py(yh)); g.lineTo(X1,py(yh)); g.stroke();
    g.setLineDash([]);
    g.strokeStyle='#3c4b5f'; g.lineWidth=1.4; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(TODAY),Y0); g.lineTo(px(TODAY),Y1); g.stroke();
    g.setLineDash([]);
    g.fillStyle='#3c4b5f'; g.textAlign='center';
    g.fillText('now (140.2)', px(TODAY), Y0-8);
    [[1/3,'radiation',13],[0,'matter',-4]].forEach(function(q){
      var yv=Math.log(opsbit(q[0]))/Math.LN10;
      g.strokeStyle='rgba(28,63,99,.18)'; g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,py(yv)); g.lineTo(px(TODAY),py(yv)); g.stroke();
      g.fillStyle='rgba(60,75,95,.6)'; g.textAlign='left';
      g.fillText(q[1], X0+6, py(yv)+q[2]);
    });
    g.fillStyle='#5f6a7a'; g.textAlign='center';
    g.fillText('logarithmic age of the universe   ln(t / t_P)', (X0+X1)/2, Y1+34);
    vw.textContent='w = '+(w<0?'−':'')+Math.abs(w).toFixed(3);
    var name = Math.abs(w+1/3)<0.0006 ? ' (c·t=const)' : (Math.abs(w-1/3)<0.0006?' (radiation)':(Math.abs(w)<0.0006?' (matter)':''));
    ro.textContent='w = '+(w<0?'−':'')+Math.abs(w).toFixed(3)+name+
      '　p = '+p.toFixed(3)+'　→　'+v.toFixed(5)+' operations per bit = one per '+(1/v).toFixed(1)+' bits'+
      (v>=1?'　★ past 1':'　(a factor '+(1/v).toFixed(1)+' short of 1)');
  }
  sw.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-01-opsbit.html', acc='#1c3f63', ops='#a85a12',
      title='The universe has computed 0.035 operations per bit ── c·t = const, That Clicks, Episode 1',
      ep='EPISODE 1 ／ Starting from the specification sheet',
      eyebrow='Divide the memory by the operations and out comes the equation of state',
      h1='The universe has computed<br>0.035 operations per bit',
      sub='"The universe is a computer with finite resources" — we take that view and write it out<br>to the end, not as a metaphor but as a specification sheet. The very first sheet already goes strange.',
      byline_l='What you need: division, Planck units, logarithms',
      byline_r='\\(\\Omega/N=\\dfrac{\\ln 2}{3\\pi^2(1+w)}\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 1 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The horizon entropy \\(S=k_BA/4\\ell_P^2\\), the Margolus–Levitin limit (an upper bound \\(2E/\\pi\\hbar\\) on the rate of transitions to orthogonal states), and the estimate that the universe has performed \\(\\sim10^{120}\\) operations are standard since Lloyd (2002, PRL 88, 237901). \\(M=c^2R_H/2G\\) is an identity in flat FLRW, and that Dirac\'s large-number hypothesis is isomorphic to it was shown in bonus episode ③ of the previous series. The results \\(\\Omega=(ct/\\ell_P)^2/2\\pi p\\), \\(\\Omega/N=p\\ln2/2\\pi^2=\\ln2/3\\pi^2(1+w)\\), the value \\(w=-0.97659\\) giving \\(\\Omega/N=1\\), and the de Sitter form \\(\\Omega/N=(\\ln2/\\pi^2)Ht\\) (reaching 1 at \\(Ht=\\pi^2/\\ln2=14.24\\)) are all derived and computed here. Numbers use \\(t_0=4.3536\\times10^{17}\\) s, \\(\\ell_P=1.6163\\times10^{-35}\\) m, \\(t_P=5.3912\\times10^{-44}\\) s. <strong>"Operations" means the upper bound on transitions permitted by the energy, not meaningful computation.</strong> Conventions (whether the rate is \\(2E/\\pi\\hbar\\) or \\(4E/h\\), how \\(E\\) is taken, bits versus nats) shift \\(\\Omega/N\\) by around a factor of 1.5 — the claim here is the structure (independent of time, fixed by \\(w\\)), not the digits. \\(w\\) is the effective equation of state of the universe as a whole, and the table idealises "if that \\(w\\) held for all time". The 250-billion-year figure assumes pure de Sitter after today (\\(H_\\Lambda=H_0\\sqrt{\\Omega_\\Lambda}\\), \\(H_0=67.66\\) km/s/Mpc, \\(\\Omega_\\Lambda=0.685\\)). The dark-energy value \\(w=-1.03\\pm0.03\\) comes from a constant-\\(w\\) fit. The entropy occupancy \\(1.5\\times10^{-18}\\) uses \\(S_{\\rm obs}=3.1\\times10^{104}k_B\\) from Egan &amp; Lineweaver (2010, ApJ 710, 1825). Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model still under test; extrapolated into the early universe it contradicts nucleosynthesis (Lewis, Barnes &amp; Kaushik 2016, MNRAS 460, 291). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider changes the equation of state and moves the operations-per-bit line. "Show the answer" opens each solution.')
