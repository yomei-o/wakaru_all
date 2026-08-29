# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Part I (Episodes 1–6) established that \(c\cdot t=\text{const}\) is <strong>notation</strong>. It says nothing on its own, and in exchange it can be substituted safely into anything. Part II carries that notation <em>out of cosmology</em>. First stop: gravity. And something satisfying appears immediately — <strong>this notation lets us actually run the hypothesis Dirac proposed in 1937</strong>.</p>

<h2><span class="n">01</span>\(G\) was bookkeeping</h2>

<p>Start where Extra 5 of the previous series started. Newton's constant has units \(\mathrm{m^3\,kg^{-1}\,s^{-2}}\) — thoroughly dimensionful. Run it through the decision procedure and it lands in the left column: <strong>bookkeeping</strong>. The physics is the dimensionless gravitational coupling.</p>

<div class="calc">
<span class="tag">The dimensionless coupling of gravity</span>
$$\alpha_G=\frac{Gm^2}{\hbar c}=\left(\frac{m}{M_{\rm Pl}}\right)^2$$
</div>

<p>In this picture mass grows as \(\tilde m=am\). But \(\alpha_G\) is dimensionless and therefore must not move. So it is \(G\) that moves, to keep the books balanced.</p>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
$$\tilde G=\frac{G}{a^2}\qquad\Longrightarrow\qquad \frac{\dot G}{G}=-\frac{2}{t}=-2H_0$$
</div>

<h2><span class="n">02</span>As a number, it is outrageous</h2>

<div class="calc">
<span class="tag">The rate</span>
$$\frac{\dot G}{G}=-2H_0=-1.45\times10^{-10}\ /\text{yr}$$
<p class="lbl">Lunar laser ranging bound</p>
$$\left|\frac{\dot G}{G}\right|<10^{-13}\ /\text{yr}$$
<p class="lbl">Ratio</p>
$$\mathbf{1450}\times\ \text{faster than the observational limit}$$
</div>

<p>Read naively, this picture is <strong>falsified by three orders of magnitude</strong>. And yet it is not falsified at all.</p>

<h2><span class="n">03</span>Nobody could notice anyway</h2>

<p>Because only dimensionless quantities are measurable. In \(\alpha_G=Gm^2/\hbar c\), the \(G\) falls as \(1/a^2\) while \(m^2\) grows as \(a^2\) — <strong>they cancel exactly</strong>.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Particle</th><th class="mid">\(\alpha_G=(m/M_{\rm Pl})^2\)</th><th class="mid">In this picture</th></tr></thead>
<tbody>
<tr><th>Neutrino (0.05 eV)</th><td class="mid">\(1.68\times10^{-59}\)</td><td class="mid">unchanged</td></tr>
<tr><th>Electron</th><td class="mid">\(1.75\times10^{-45}\)</td><td class="mid">unchanged</td></tr>
<tr><th>Proton</th><td class="mid">\(5.91\times10^{-39}\)</td><td class="mid">unchanged</td></tr>
<tr class="hi"><th>Planck mass</th><td class="mid">\(1\)</td><td class="mid"><strong>unchanged</strong></td></tr>
</tbody>
</table>
</div>

<p>What lunar laser ranging actually measures are <em>dimensionless ratios</em> of the lunar orbit (period ÷ atomic clock tick, distance ÷ \(c\times\)time). Not one of them moves. <strong>"\(G\) changed" does not register, because the measuring apparatus changed with it.</strong></p>

<div class="aside">
<span class="tag">The gravitational version of Extra 3</span>
Variable-speed-of-light theories move \(c\) alone while holding \(e\) and \(\hbar\) fixed, so \(\alpha\) moves and collides with atomic clocks. <strong>What happens here is the exact inverse</strong> — \(G\) moves and \(m\) moves with it, so \(\alpha_G\) is preserved and nothing is observable. <em>When you move a dimensionful constant, you must move the whole set.</em> The "second equivalence condition" of Extra 4 applies to gravity unchanged.
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The heart — actually testing Dirac's large numbers</h2>

<div class="calc">
<span class="tag">Dirac's two large numbers (1937)</span>
<p class="lbl">① electric force ÷ gravitational force inside a hydrogen atom</p>
$$N_1=\frac{e^2}{4\pi\varepsilon_0\,G\,m_p m_e}=2.27\times10^{39}$$
<p class="lbl">② age of the universe ÷ classical electron time (\(r_e/c=9.40\times10^{-24}\) s)</p>
$$N_2=\frac{t_0}{r_e/c}=4.63\times10^{40}$$
<p class="lbl">ratio</p>
$$\frac{N_2}{N_1}=20.4\qquad(\text{both around }10^{40})$$
</div>

<p>Dirac's reasoning was: <em>\(N_2\) grows with the age of the universe. It would be unnatural for the two to coincide today by accident, so \(N_1\) must be growing too. The only thing in \(N_1\) that can change is \(G\). Therefore \(G\propto1/t\).</em> Bold, and beautiful. <strong>And this notation does make \(G\) vary in time.</strong> So let us run it.</p>

<div class="calc">
<span class="tag">Actually doing it</span>
<p class="lbl">Transform the denominator of \(N_1\) (\(e,\varepsilon_0\) have weight 0)</p>
$$\left(\frac{G}{a^2}\right)\cdot(a\,m_p)\cdot(a\,m_e)=G\,m_p m_e\qquad\Longrightarrow\qquad \tilde N_1=N_1$$
<p class="lbl">\(N_2\) is a ratio of times (\(r_e\) is a length)</p>
$$\tilde N_2=\frac{t/a}{(r_e/a)/c}=N_2$$
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0">Make \(G\) genuinely vary in time and <strong>neither of Dirac's large numbers budges</strong>.<br>
The coincidence gets neither better nor worse. <em>Dirac's prescription spins freely.</em></p>
</div>

<p>The reason is §03 again: <strong>you cannot move \(G\) alone</strong>. If you do, it is not a conformal transformation but a VSL-type operation, \(\alpha_G\) moves and observation objects. Do it properly and \(m\) moves too, preserving \(N_1\).</p>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>\(M/m_P=R_H/2\ell_P\) — an identity</strong><span>always true in flat FLRW. Not a coincidence, but not physics either (Extra 3)</span></div></div>
<div class="row hi"><div class="mk">②</div><div class="txt"><strong>\(N_1,\ N_2\) — conformally invariant</strong><span>they do not move when \(G\) does. So "explain it by varying \(G\)" cannot get started (this episode)</span></div></div>
</div>

<div class="fig">
<p class="cap">Figure: the slider switches the <strong>way of speaking</strong> — far left is the standard picture (\(G\) and \(m\) both constant), far right is this one (\(G\propto t^{-2}\), \(m\propto t\)). The plum and grey lines swing violently while <strong>the gold line (\(\alpha_G\)) does not twitch</strong>.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Way of speaking \(s\) (left = standard / right = mass grows)<input id="ss" type="range" min="0" max="1000" value="1000" step="5"></label>
  <span class="val" id="vs">s = 1.00</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#4a2740"></i>\(G\) (\(\propto t^{-2s}\))</span>
  <span><i class="swatch" style="background:#8a8a94"></i>mass \(m\) (\(\propto t^{s}\))</span>
  <span><i class="swatch" style="background:#96702a"></i>\(\alpha_G=Gm^2/\hbar c\)</span>
</div>
</div>

<p>At the right edge \(G\) rockets up towards the past while mass sinks. At the left edge both are flat. And the gold line stays perfectly horizontal everywhere — <strong>and the gold line is the only one observation can see</strong>.</p>

<h2><span class="n">05</span>Transforming every gravitational quantity in sight</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Weight</th><th class="mid">In this picture</th></tr></thead>
<tbody>
<tr><th>Newton's constant \(G\)</th><td class="mid">──</td><td class="mid">\(\div a^2\)</td></tr>
<tr><th>Gravitational acceleration \(g=GM/r^2\)</th><td class="mid">\(-1\)</td><td class="mid">\(\times a\)</td></tr>
<tr><th>Schwarzschild radius \(2GM/c^2\)</th><td class="mid">\(+1\)</td><td class="mid">\(\div a\)</td></tr>
<tr><th>Hawking temperature \(\hbar c^3/8\pi GMk_B\)</th><td class="mid">\(-1\)</td><td class="mid">\(\times a\)</td></tr>
<tr><th>Tidal force (geodesic deviation)</th><td class="mid">\(-2\)</td><td class="mid">\(\times a^2\)</td></tr>
<tr class="hi"><th>Black hole entropy \(A/4\ell_P^2\)</th><td class="mid">\(0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr class="hi"><th>Gravitational wave strain \(h\)</th><td class="mid">\(0\)</td><td class="mid"><strong>invariant</strong></td></tr>
<tr class="hi"><th>Kepler's third law \(T^2=4\pi^2r^3/GM\)</th><td class="mid">──</td><td class="mid"><strong>form invariant</strong></td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">Checking that Kepler keeps its form</span>
$$\underbrace{\frac{T^2}{a^2}}_{\text{LHS}}\qquad\text{and}\qquad \underbrace{\frac{4\pi^2(r/a)^3}{(G/a^2)(aM)}=\frac{1}{a^2}\cdot\frac{4\pi^2r^3}{GM}}_{\text{RHS}}$$
<p class="lbl">Both sides pick up \(1/a^2\), so</p>
$$T^2=\frac{4\pi^2r^3}{GM}\qquad\text{holds identically; orbits merely shrink similarly}$$
</div>

<p>In this picture planetary orbits <em>shrink with time</em> (\(\div a\)). But the periods shrink by the same factor, so Kepler's law is not rewritten by a single character. <strong>Point a telescope at the solar system and you can never tell the difference.</strong></p>

<h2><span class="n">06</span>The reveal — what the invariant things have in common</h2>

<p>The bottom three rows (BH entropy, strain \(h\), Kepler) are invariant because they are dimensionless. But the first of them carries a deeper meaning.</p>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0">Episode 6 counted that <strong>the memory actually in use is almost entirely black holes</strong>.<br>
And black hole entropy <strong>does not move at all</strong> in this picture.<br>
<em>A conformal transformation cannot reach the memory in use</em> — the same conclusion, now from the gravitational side.</p>
</div>

<p>Episode 6 said it geometrically ("the conformal-factor side is empty, the Weyl side is in use"). This episode transformed gravitational quantities one at a time and <strong>arrived at the same place by another road</strong>. \(G\), \(g\), \(r_s\), \(T_H\) all move — <em>only the entropy stands still</em>.</p>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① \(\tilde G=G/a^2\) follows from demanding that \(\alpha_G\) be invariant.</strong> As Episode 4 of the previous series showed, in a Weyl-invariant formulation \(M_{\rm Pl}^2=\xi\phi^2\), so \(G\) alone has no physical meaning — this "variation" of \(G\) is pure bookkeeping.</p>
<p style="margin:0 0 10px"><strong>② The lunar laser ranging bound \(|\dot G/G|<10^{-13}\)/yr constrains theories in which \(G\) alone varies.</strong> This picture is not such a theory, so <em>the bound simply does not apply</em>. The factor 1450 is there to show how it looks read naively, not to say the model is falsified.</p>
<p style="margin:0 0 10px"><strong>③ Only \(N_1\) and \(N_2\) are treated here.</strong> Dirac's own argument was broader, including the particle number \(\sim10^{80}\simeq N^2\). And his claim was a <em>naturalness</em> argument — "coincidence today would be unnatural" — not something derived from observation. Whether naturalness arguments are sound is itself an open question.</p>
<p style="margin:0 0 10px"><strong>④ "Kepler keeps its form" holds under a conformal transformation.</strong> Theories in which \(G\) genuinely varies (Brans–Dicke type) do produce observable orbital effects — those are different from this picture and are constrained by lunar laser ranging among other things.</p>
<p style="margin:0"><strong>⑤ The Hawking temperature and BH entropy transformations assume a quasi-static black hole.</strong> The interplay between cosmological time variation and black hole interior structure is not treated here.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Why does \(G\) transform as \(1/a^2\)?
<details><summary>Show the answer</summary><div class="ans">Because \(\alpha_G=Gm^2/\hbar c\) is dimensionless and must be invariant, and \(m\to am\) multiplies \(m^2\) by \(a^2\). The only way to cancel is \(G\to G/a^2\). <strong>The transformation law is not chosen — it is forced by the invariance of a dimensionless quantity.</strong></div></details></li>

<li>Compute \(\dot G/G\) and compare with lunar laser ranging.
<details><summary>Show the answer</summary><div class="ans">\(\dot G/G=-2/t=-2H_0=-1.45\times10^{-10}\)/yr — <strong>1450 times</strong> the \(10^{-13}\)/yr bound. <strong>And still not falsified</strong>: that bound applies to theories in which \(G\) alone varies, whereas here \(m\) varies too, \(\alpha_G\) is preserved, and not one dimensionless ratio of the lunar orbit changes.</div></details></li>

<li>Show that Dirac's \(N_1\) is conformally invariant.
<details><summary>Show the answer</summary><div class="ans">The denominator of \(N_1=e^2/(4\pi\varepsilon_0Gm_pm_e)\) becomes \((G/a^2)(am_p)(am_e)=Gm_pm_e\), unchanged; the numerator's \(e,\varepsilon_0\) have weight 0. So \(N_1\) does not move. <strong>Varying \(G\) does not move the large numbers</strong> — which is why Dirac's strategy spins freely.</div></details></li>

<li>What happens to orbital radius and period here, and to Kepler's law?
<details><summary>Show the answer</summary><div class="ans">Radius is a length, so \(\div a\); period is a time, so \(\div a\). Both sides of \(T^2=4\pi^2r^3/GM\) pick up \(1/a^2\), so <strong>the law is unchanged to the letter</strong>. The solar system shrinks similarly with time, and the shrinking cannot be measured from inside.</div></details></li>

<li>(Harder) How does the invariance of BH entropy connect to Episode 6?
<details><summary>Show the answer</summary><div class="ans">Episode 6 counted the universe's memory in use (\(3.1\times10^{104}k_B\)) as almost entirely black holes. That entropy \(A/4\ell_P^2\) is a ratio of an area to the Planck area — <strong>dimensionless, hence conformally invariant</strong>. So <em>a conformal transformation cannot touch the memory actually in use</em>. Episode 6 got there from geometry (the Weyl tensor is conformally invariant); this episode got there by transforming gravitational quantities one at a time.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — we really did vary \(G\), and nothing happened</h2>
<p>\(G\) is dimensionful — bookkeeping. The physics is the dimensionless \(\alpha_G=(m/M_{\rm Pl})^2\). Since mass grows as \(\tilde m=am\) here, preserving \(\alpha_G\) <strong>forces</strong> \(\tilde G=G/a^2\), giving \(\dot G/G=-2H_0=-1.45\times10^{-10}\)/yr — <strong>1450 times</strong> the lunar laser ranging bound of \(10^{-13}\)/yr. Read naively, a three-order falsification.</p>
<p>And yet nothing is falsified, because only dimensionless quantities are measurable and \(\alpha_G\) does not move for neutrinos, electrons, protons or anything else. The lunar orbit measures only dimensionless ratios. <strong>"\(G\) changed" does not register, because the apparatus changed with it</strong> — the VSL critique of Extra 3, turned exactly inside out.</p>
<p>Then the heart of it. In 1937 Dirac saw that \(N_1=e^2/4\pi\varepsilon_0Gm_pm_e=2.27\times10^{39}\) and \(N_2=t_0/(r_e/c)=4.63\times10^{40}\) are close, and <strong>predicted \(G\propto1/t\)</strong>. This notation does vary \(G\), so we ran it — and <strong>neither number budges</strong>. The denominator of \(N_1\) becomes \((G/a^2)(am_p)(am_e)=Gm_pm_e\); \(N_2\) is a ratio of times. <em>You cannot vary \(G\) alone, so Dirac's prescription spins freely.</em> Next to Extra 3's verdict that \(M/m_P=R_H/2\ell_P\) is an identity, we can now write a second line.</p>
<p>Transforming everything gravitational: \(g\times a\), \(r_s\div a\), \(T_H\times a\), tides \(\times a^2\). Kepler's law picks up \(1/a^2\) on both sides and is <strong>form invariant</strong> (the solar system merely shrinks similarly). And the strain \(h\) and <strong>black hole entropy alone are completely invariant</strong>. The very quantity Episode 6 counted as "essentially all the memory in use" does not move here — <em>a conformal transformation cannot reach the memory in use</em>. What was said from geometry now comes out from counting gravitational quantities as well.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 8</span>
Next we substitute into <strong>quantum mechanics</strong>. The Schrödinger equation is form invariant, becoming the same equation with \(m(t)=m_0\,t/t_0\). A free wave packet then spreads not as \(\Delta x\propto t\) but only as <strong>\(\Delta x\propto\ln t\)</strong> — because the growing mass drops the velocity as \(1/t\). Integrate and <strong>the comoving reach of anything massive is finite</strong> (a galaxy with peculiar velocity 600 km/s has 8.5 Mpc left, forever). Light meanwhile travels \(\int c\,dt/a\propto\ln t\), without bound. <em>Matter stops being able to walk; light keeps walking.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=74, X1=700, Y0=30, Y1=318;
  var xmin=-3, xmax=0.3;
  var ymin=-3.2, ymax=6.6;
  var H0yr=1/(4.3536e17/3.1557e7);

  function px(x){ return X0+(x-xmin)/(xmax-xmin)*(X1-X0); }
  function py(y){ return Y1-(y-ymin)/(ymax-ymin)*(Y1-Y0); }

  function line(slope,color,w,dash){
    g.strokeStyle=color; g.lineWidth=w;
    if(dash) g.setLineDash(dash);
    g.beginPath();
    g.moveTo(px(xmin),py(slope*xmin));
    g.lineTo(px(xmax),py(slope*xmax));
    g.stroke(); g.setLineDash([]);
  }

  function draw(){
    var s=parseInt(ss.value,10)/1000;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px system-ui,-apple-system,"Segoe UI",sans-serif';

    g.textAlign='right';
    for(var e=-3;e<=6;e++){
      var y=py(e);
      g.strokeStyle=(e===0?'#ddd0d8':'#f4ecf0'); g.lineWidth=1;
      g.beginPath(); g.moveTo(X0,y); g.lineTo(X1,y); g.stroke();
      if(e%2===0){ g.fillStyle='#a9959f';
        g.fillText(e===0?'1':(e<0?'10⁻'+Math.abs(e):'10'+e), X0-8, y+4); }
    }
    g.textAlign='center';
    for(var q=-3;q<=0;q++){
      var x=px(q);
      g.strokeStyle='#f8f2f5'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#a9959f'; g.fillText(q===0?'now':'10'+q, x, Y1+16);
    }
    g.strokeStyle='#dccdd5'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y0); g.lineTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();

    line(-2*s, '#4a2740', 3.2);
    line( 1*s, '#8a8a94', 2.6, [6,4]);
    line( 0,   '#96702a', 3.6);

    g.textAlign='left';
    g.fillStyle='#4a2740'; g.fillText('G', px(xmin)+8, py(-2*s*xmin)-8);
    g.fillStyle='#8a8a94'; g.fillText('mass m', px(xmin)+8, py(1*s*xmin)+16);
    g.fillStyle='#96702a'; g.fillText('α_G = Gm²/ħc　(flat all the way)', px(-1.45), py(0)-10);

    g.fillStyle='#7a6570'; g.textAlign='center';
    g.fillText('age of the universe  t / t₀', (X0+X1)/2, Y1+36);

    var rate=2*s*H0yr;
    vs.textContent='s = '+s.toFixed(2);
    var tag = s>0.995?'(mass-grows picture)':(s<0.005?'(standard picture)':'(intermediate)');
    ro.textContent='s = '+s.toFixed(2)+' '+tag+
      '　G ∝ t^'+(-2*s).toFixed(2)+'　m ∝ t^'+s.toFixed(2)+
      '　→　|Ġ/G| = '+rate.toExponential(2)+' /yr'+
      (rate>1e-13 ? ' ('+(rate/1e-13).toFixed(0)+'× the lunar-laser bound)' : ' (inside the bound)')+
      '　/　α_G unchanged';
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-07-gravity.html', acc='#4a2740', ops='#96702a',
      title='Substituting into gravity ── c·t = const, That Clicks, Episode 7',
      ep='EPISODE 7 ／ Part II begins — carrying the notation out of cosmology',
      eyebrow='\\(G\\) varies 1450× faster than the observational bound, and nobody can tell',
      h1='Substituting<br>into gravity',
      sub='The first destination is gravity, where \\(G\\) falls as \\(1/t^2\\).<br><em>Dirac dreamed that varying \\(G\\) would explain the large-number coincidence. Let us actually try it.</em>',
      byline_l='What you need: the weight table, division',
      byline_r='\\(\\alpha_G=(m/M_{\\rm Pl})^2\\) is invariant',
      body=BODY + '\n\n<p class="foot">This document is Episode 7 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. That \\(\\alpha_G=Gm^2/\\hbar c=(m/M_{\\rm Pl})^2\\) is the dimensionless coupling of gravity, and that under a conformal transformation mass carries weight \\(-1\\), lengths and times \\(+1\\), and \\(c,\\hbar,e,\\varepsilon_0\\) weight \\(0\\), are standard. The \\(\\tilde G=G/a^2\\), the rate \\(\\dot G/G=-2H_0=-1.45\\times10^{-10}\\)/yr, and the comparison with the lunar laser ranging bound \\(|\\dot G/G|<10^{-13}\\)/yr are this document\'s calculation. <strong>That bound constrains theories in which \\(G\\) alone varies, and does not apply to the picture here, in which mass is transformed at the same time.</strong> The large number hypothesis is Dirac (1937, Nature 139, 323). The values \\(N_1=e^2/(4\\pi\\varepsilon_0Gm_pm_e)=2.27\\times10^{39}\\), \\(r_e=2.818\\times10^{-15}\\) m, \\(N_2=t_0/(r_e/c)=4.63\\times10^{40}\\), the ratio 20.4, and the conformal invariance of both, are computed and pointed out here. Dirac\'s own argument was broader (including the particle number \\(\\sim10^{80}\\)) and rested on a naturalness claim — that coincidence today would be unnatural — rather than on observation. That \\(M/m_P=R_H/2\\ell_P\\) is an identity of flat FLRW was shown in Extra 3 of the previous series. The form invariance of Kepler\'s third law, and the invariance of the black hole entropy \\(A/4\\ell_P^2\\) and the gravitational wave strain \\(h\\) by dimensionlessness, are checked here. The Hawking temperature and BH entropy transformations assume a quasi-static black hole. Theories in which \\(G\\) genuinely varies (Brans–Dicke type) are different from this picture and are observationally constrained. The academic standard remains the \\(\\Lambda\\)CDM model including inflation, together with unmodified general relativity. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider switches the way of speaking and only α_G stays put. "Show the answer" opens each solution.')
