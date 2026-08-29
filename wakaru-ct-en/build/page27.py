# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Remember the surgery from Episode 3 — <strong>check whether one name contains two different things</strong>. The watchword held both "an equivalent rewriting" and "a claim observation can judge", under a single label. In Part IV we apply that surgery to other theories. <em>The first patient is inflation.</em></p>

<h2><span class="n">01</span>Splitting "inflation solves the horizon problem"</h2>

<div class="seven">
<div class="row"><div class="mk">A</div><div class="txt"><strong>Establishing causal contact</strong><span>a matter of geometry; a change in the shape of the conformal diagram will do — <em>the kind of claim an equivalent rewriting can also achieve</em></span></div></div>
<div class="row hi"><div class="mk">B</div><div class="txt"><strong>Producing a fluctuation spectrum</strong><span>\(n_s\), \(r\), adiabaticity, gaussianity — <em>the kind of claim observation judges</em></span></div></div>
</div>

<p>Exactly the structure of Episode 3. So how "cheap" is (A)? That is where we start counting.</p>

<h2><span class="n">02</span>(A) costs zero e-folds if \(a\propto t\)</h2>

<div class="calc">
<span class="tag">The particle horizon</span>
<p class="lbl">for \(a\propto t^p\)</p>
$$d_p=a(t)\int_0^t\frac{c\,dt'}{a(t')}=\frac{ct}{1-p}$$
<p class="lbl">at \(p=1\), \(\int dt'/t'\) diverges logarithmically, so</p>
$$d_p=\infty$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Expansion law</th><th class="mid">\(d_p\)</th><th class="mid">Horizon problem?</th></tr></thead>
<tbody>
<tr><th>\(p=1/2\) (radiation)</th><td class="mid">\(2ct\)</td><td class="mid">yes</td></tr>
<tr><th>\(p=2/3\) (matter)</th><td class="mid">\(3ct\)</td><td class="mid">yes</td></tr>
<tr><th>\(p=0.99\)</th><td class="mid">\(100\,ct\)</td><td class="mid">yes</td></tr>
<tr class="hi"><th>\(p=1\) (c·t=const)</th><td class="mid"><strong>\(\infty\)</strong></td><td class="mid"><strong>no</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §02</p>
<p style="margin:6px 0 0"><strong>\(c\cdot t=\)const removes the horizon problem with zero e-folds and zero parameters.</strong><br>
So (A) is not an achievement peculiar to inflation — <em>the horizon problem was never "the universe's problem" but "the decelerating universe's problem"</em>.</p>
</div>

<p>Episode 17 counted the information this problem needs — about \(10^4\) causally disconnected patches at recombination, 20 KB to be agreed on. At \(p=1\) there is one patch, so <em>the information needed is 0 bits</em>.</p>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>What (A) demands of inflation in e-folds</h2>

<div class="calc">
<span class="tag">The condition</span>
<p class="lbl">today's comoving Hubble radius must lie inside the one at the start of inflation</p>
$$e^N\ \ge\ \frac{a_e}{a_0}\cdot\frac{H_{\rm inf}}{H_0}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>\(V^{1/4}\)</th><th class="mid">\(H_{\rm inf}\) [1/s]</th><th class="mid">\(T_{\rm reh}\) [GeV]</th><th class="mid">\(N_{\min}\)</th></tr></thead>
<tbody>
<tr class="hi"><th>\(10^{16}\) GeV (GUT)</th><td class="mid">\(3.6\times10^{37}\)</td><td class="mid">\(4.1\times10^{15}\)</td><td class="mid"><strong>62.1</strong></td></tr>
<tr><th>\(10^{13}\) GeV</th><td class="mid">\(3.6\times10^{31}\)</td><td class="mid">\(4.1\times10^{12}\)</td><td class="mid">55.2</td></tr>
<tr><th>\(10^{10}\) GeV</th><td class="mid">\(3.6\times10^{25}\)</td><td class="mid">\(4.1\times10^{9}\)</td><td class="mid">48.3</td></tr>
<tr><th>\(10^{6}\) GeV</th><td class="mid">\(3.6\times10^{17}\)</td><td class="mid">\(4.1\times10^{5}\)</td><td class="mid">39.1</td></tr>
</tbody>
</table>
</div>

<p>The commonly quoted "\(N\approx60\)" is the GUT-scale value. <strong>Here is the crux of the surgery: \(N\) is not a free parameter — it is fixed by requirement (A).</strong></p>

<h2><span class="n">04</span>And the same \(N\) predicts \(n_s\)</h2>

<div class="calc">
<span class="tag">The standard slow-roll result</span>
$$n_s\approx1-\frac{2}{N}$$
<p class="lbl">put in the \(N=62.1\) fixed by (A)</p>
$$n_s=0.9678$$
<p class="lbl">observed (Planck 2018)</p>
$$n_s=0.9649\pm0.0042\qquad\Longrightarrow\qquad N=57.0\pm6.8$$
<p class="lbl">discrepancy</p>
$$0.75\sigma$$
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0"><strong>Two \(N\) values fixed by entirely different requirements agree within \(1\sigma\).</strong><br>
One from "today's universe fitting inside one causal patch", the other from the tilt of the CMB fluctuations. <em>Why those two should be connected emerges only once inflation is assumed.</em></p>
</div>

<div class="fig">
<p class="cap">Figure: e-folds \(N\) across. <strong>Blue</strong> is the \(N_{\min}\) demanded by (A) (which moves with the reheating scale); <strong>orange</strong> is the \(N\) implied by (B)'s \(n_s\). Move the slider through reheating scales to see where they overlap.</p>
<canvas id="cv" width="720" height="380"></canvas>
<div class="controls">
  <label>Reheating scale \(\log_{10}(V^{1/4}/\mathrm{GeV})\)<input id="ss" type="range" min="60" max="165" value="160" step="1"></label>
  <span class="val" id="vs">10¹⁶ GeV</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#1e3f6e"></i>(A) the \(N_{\min}\) the horizon demands</span>
  <span><i class="swatch" style="background:#c06a1e"></i>(B) \(n_s\) implies \(N=57.0\pm6.8\)</span>
</div>
</div>

<h2><span class="n">05</span>Measuring the surprise with Episode 19's procedure</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Method</th><th class="mid">Content</th><th class="mid">Surprise</th></tr></thead>
<tbody>
<tr><th>A: relative width from \(n_s\)</th><td class="mid">\(\sigma_N/N=0.120\), prior \(\ln\) range 4.61</td><td class="mid">5.3 bit</td></tr>
<tr><th>B: probability of the band</th><td class="mid">probability of \(N\in[55,70]\) is 0.052</td><td class="mid">4.3 bit</td></tr>
</tbody>
</table>
</div>

<p>About 4–5 bits. On Episode 19's scale that falls in the <em>coincidence</em> band (4.7–7.4 bits), but <strong>this one has an explanation</strong> — the structure whereby a single \(N\) fixes both. In Episode 19's classification, an explained agreement moves to <em>physics</em>. That is the difference from Episode 18's 1.96 fm (7.4 bits, unexplained).</p>

<h2><span class="n">06</span>The reveal — same surgery, different outcome</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th></th><th class="mid">Pays</th><th class="mid">Buys</th><th class="mid">Net</th></tr></thead>
<tbody>
<tr class="hi"><th>Inflation</th><td class="mid">\(N\) + the shape of \(V\) ≈ 2 parameters<br>(\(-10.7\) bit)</td><td class="mid">predicts \(n_s\) at 4.3 bit</td><td class="mid"><strong>\(-6.5\) bit</strong><br><em>(an underestimate)</em></td></tr>
<tr><th>c·t=const</th><td class="mid">one fewer parameter<br>(\(+5.4\) bit)</td><td class="mid">the horizon problem disappears</td><td class="mid">\(-148.3\) bit<br>(Episode 25)</td></tr>
</tbody>
</table>
</div>

<p>Inflation's \(-6.5\) is <strong>an underestimate</strong> — only \(n_s\) is credited here, while the same two parameters also buy the bound on \(r\), adiabaticity, gaussianity, <em>the super-horizon TE anticorrelation</em>, flatness and the monopole problem. Whereas \(c\cdot t=\)const's \(-148.3\) is the loss on fit itself, and is not an underestimate.</p>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0">The same surgery, and <strong>what survives is different</strong>.<br>
Discard (A) and inflation still has (B).<br>
\(c\cdot t=\)const solves (A) <em>for free</em> but has nothing corresponding to (B).</p>
</div>

<div class="aside">
<span class="tag">Why (A) should be discarded</span>
"Inflation solves the horizon problem" is the first motivation in every textbook. What this surgery shows is that <strong>it is the weakest argument available</strong> — \(a\propto t\) does the same thing with zero parameters. <em>What supports inflation is not (A) but (B).</em> The same was true of \(c\cdot t=\)const: the previous series' "move \(c\) and \(\hbar\) together and it is the same" is correct, and correct is all it is — it buys nothing. <strong>The point of the surgery is to name which argument is actually paying.</strong>
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① \(N=60\) depends strongly on the reheating scale.</strong> As the table shows, \(V^{1/4}=10^6\) GeV gives \(N_{\min}=39\) and the GUT scale gives 62 — <em>a spread of 23</em>. The agreement with \(n_s\) assumes the GUT scale, and does not hold for low-scale models.</p>
<p style="margin:0 0 10px"><strong>② \(n_s\approx1-2/N\) is model dependent.</strong> It holds for \(R^2\) (Starobinsky) type and α-attractors, but not for every inflationary model. This is a prediction of a well-used family of models, not "the prediction of inflation".</p>
<p style="margin:0 0 10px"><strong>③ Instantaneous reheating is assumed.</strong> Prolonged reheating moves \(N_{\min}\) by several to tens more.</p>
<p style="margin:0 0 10px"><strong>④ §06's ledger is a rough calculation to put things in common units.</strong> The parameter price uses Episode 5's \(N_{\rm data}=1701\), and only \(n_s\) is credited on inflation's side. <em>Read "\(-6.5\) versus \(-148\)" only as a comparison of orders.</em></p>
<p style="margin:0 0 10px"><strong>⑤ That the horizon problem vanishes at \(p=1\) does not support that expansion law.</strong> Episode 3's judgement (helium abundance from nucleosynthesis) is unchanged. §02 says only that (A) is cheap.</p>
<p style="margin:0"><strong>⑥ This episode does not refute inflation.</strong> Quite the opposite — it confirms that <em>(B) survives the surgery</em>.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Find the particle horizon for \(a\propto t^p\) and show it diverges at \(p=1\).
<details><summary>Show the answer</summary><div class="ans">\(d_p=a\int_0^t c\,dt'/a=ct^p\int_0^t t'^{-p}dt'=ct^p\cdot t^{1-p}/(1-p)=ct/(1-p)\). As \(p\to1\), \(\int dt'/t'=[\ln t']_0^t\) <strong>diverges logarithmically</strong> at the lower limit.</div></details></li>

<li>From \(n_s=0.9649\), find \(N\) and its error.
<details><summary>Show the answer</summary><div class="ans">\(N=2/(1-n_s)=2/0.0351=57.0\); the error is \(dN/dn_s=2/(1-n_s)^2=1623\) times \(0.0042\), i.e. \(\pm6.8\). <strong>\(N=57.0\pm6.8\)</strong>.</div></details></li>

<li>How many \(\sigma\) is the agreement with the GUT-scale \(N_{\min}=62.1\)?
<details><summary>Show the answer</summary><div class="ans">\((62.1-57.0)/6.8=0.75\sigma\) — <strong>within \(1\sigma\)</strong>.</div></details></li>

<li>Convert the agreement into bits using Episode 19's procedure.
<details><summary>Show the answer</summary><div class="ans">With a log-uniform prior \(N\in[10,1000]\), the \(\ln\) range is 4.61 and the probability of \(N\in[55,70]\) is \(\ln(70/55)/4.61=0.052\), so \(-\log_2 0.052=\) <strong>4.3 bits</strong>; by relative width, 5.3. <em>Having an explanation, it classifies as physics rather than coincidence.</em></div></details></li>

<li>(Harder) Why is "inflation solves the horizon problem" a weak argument?
<details><summary>Show the answer</summary><div class="ans">Because \(a\propto t\) does the same with <strong>zero e-folds and zero parameters</strong>. So (A) does not distinguish inflation from the alternatives. What supports inflation is (B) — \(n_s\), adiabaticity, gaussianity, super-horizon correlations. <em>The point of the surgery is to name which argument is actually paying.</em></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — (A) is cheap; what survives is (B)</h2>
<p>We cut "inflation solves the horizon problem" in two with Episode 3's surgery — (A) establishing causal contact, (B) producing a fluctuation spectrum.</p>
<p>(A) proved cheap. The particle horizon of \(a\propto t^p\) is \(ct/(1-p)\), which at \(p=1\) diverges logarithmically to <strong>infinity</strong>. So \(c\cdot t=\)const removes the horizon problem with <em>zero e-folds and zero parameters</em> — and Episode 17's 20 KB becomes 0 bits when there is one patch. <strong>The horizon problem was never "the universe's problem" but "the decelerating universe's problem".</strong></p>
<p>For inflation, (A) fixes \(N\) — \(N_{\min}=62.1\) at the GUT scale. And <em>the same \(N\)</em> predicts \(n_s\approx1-2/N=0.968\), against an observed \(0.9649\pm0.0042\), i.e. \(N=57.0\pm6.8\) — <strong>an agreement at 0.75σ</strong>. Measured by Episode 19's procedure that is 4–5 bits of surprise, classified as physics rather than coincidence because it has an explanation.</p>
<p>As a ledger, inflation comes to \(-6.5\) bits (an underestimate, crediting only \(n_s\)) against \(c\cdot t=\)const's \(-148.3\). <strong>The same surgery, and what survives is different</strong> — discard (A) and inflation still has (B), while \(c\cdot t=\)const solves (A) for free and has nothing corresponding to (B). <em>And the most famous motivation of all, "it solves the horizon problem", turns out to be the weakest argument</em> — that is the yield of the surgery.</p>
</div>

<div class="next">
<span class="lbl">Next — Episode 28</span>
The next patient is <strong>VSL (variable speed of light)</strong>. It is the theory closest to \(c\cdot t=\)const, <em>which is exactly why the surgery cuts so well</em>. Inside "the speed of light was faster in the past" there are again two different things — <strong>a change of units</strong> and <strong>a claim that a dimensionless quantity moves</strong>. Recall Episode 2's convention that \(c,\hbar,e,\alpha\) have \(w=0\). <em>We count the measurements of \(\alpha\) in bits and pin down exactly where the surgery on VSL went wrong.</em>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var ss=document.getElementById('ss'), vs=document.getElementById('vs'), ro=document.getElementById('ro');
  var X0=72, X1=700, Y0=40, Y1=300;
  var Nmin=25, Nmax=80;
  var Mpl=2.435e18, hb=6.582119569e-25, GeVK=1.16045e13, T0=2.725, H0=2.184e-18, gs=106.75;
  function px(n){ return X0+(n-Nmin)/(Nmax-Nmin)*(X1-X0); }
  function Nreq(lv){
    var V4=Math.pow(10,lv), V=Math.pow(V4,4);
    var H=Math.sqrt(V/(3*Mpl*Mpl))/hb;
    var Tr=Math.pow(30*V/(Math.PI*Math.PI*gs),0.25);
    var ae=T0/(Tr*GeVK);
    return Math.log(ae*H/H0);
  }
  function draw(){
    var lv=parseFloat(ss.value)/10;
    var Nq=Nreq(lv);
    var Nns=57.0, sN=6.8;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.strokeStyle='#c8d2e0'; g.lineWidth=1.2;
    g.beginPath(); g.moveTo(X0,Y1); g.lineTo(X1,Y1); g.stroke();
    g.textAlign='center'; g.fillStyle='#8494a8';
    for(var n=30;n<=80;n+=10){
      var x=px(n);
      g.strokeStyle='#eef2f7'; g.beginPath(); g.moveTo(x,Y0); g.lineTo(x,Y1); g.stroke();
      g.fillStyle='#8494a8'; g.fillText('N='+n, x, Y1+18);
    }
    g.fillStyle='#8494a8'; g.fillText('e-folds  N', (X0+X1)/2, Y1+42);
    var yB=Y1-70;
    for(var i=0;i<=240;i++){
      var n=Nmin+(Nmax-Nmin)*i/240;
      var z=(n-Nns)/sN;
      var h=110*Math.exp(-0.5*z*z);
      g.strokeStyle='rgba(192,106,30,0.30)'; g.lineWidth=2.6;
      g.beginPath(); g.moveTo(px(n),yB); g.lineTo(px(n),yB-h); g.stroke();
    }
    g.strokeStyle='#c06a1e'; g.lineWidth=2.6; g.beginPath();
    for(var i=0;i<=240;i++){
      var n=Nmin+(Nmax-Nmin)*i/240;
      var z=(n-Nns)/sN;
      var y=yB-110*Math.exp(-0.5*z*z);
      if(i===0) g.moveTo(px(n),y); else g.lineTo(px(n),y);
    }
    g.stroke();
    g.fillStyle='#a35a19'; g.textAlign='left';
    g.fillText('(B) n_s = 0.9649±0.0042  →  N = 57.0 ± 6.8', px(56), yB-124);
    g.strokeStyle='#1e3f6e'; g.lineWidth=3.2;
    g.beginPath(); g.moveTo(px(Nq),Y0-6); g.lineTo(px(Nq),Y1); g.stroke();
    g.fillStyle='#1e3f6e'; g.textAlign='center';
    g.font='bold 13px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText('(A) N_min = '+Nq.toFixed(1), px(Nq), Y0-12);
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    var sig=Math.abs(Nq-Nns)/sN;
    var okc = sig<1 ? '#1a7a4a' : (sig<2 ? '#b07a1e' : '#a03a2a');
    g.fillStyle=okc; g.textAlign='left';
    g.font='bold 14px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText('discrepancy '+sig.toFixed(2)+'σ', px(29), Y0+8);
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillStyle='#8494a8';
    g.fillText('c·t=const arrives here at N=0 (there is no horizon problem)', px(28), Y1-14);
    var lab = lv>=15.5?'10¹⁶ GeV (GUT)':(lv>=12.5?'10¹³ GeV':(lv>=9.5?'10¹⁰ GeV':'10^'+lv.toFixed(1)+' GeV'));
    vs.textContent=lab;
    ro.textContent='V^(1/4) = 10^'+lv.toFixed(1)+' GeV　→　(A) demands N_min = '+Nq.toFixed(1)+
      '　/　(B) n_s implies N = 57.0 ± 6.8　→　discrepancy '+sig.toFixed(2)+'σ';
  }
  ss.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-27-inflation.html', acc='#1e3f6e', ops='#c06a1e',
      title='Inflation, on the same operating table ── c·t = const, That Clicks, Episode 27',
      ep='EPISODE 27 ／ Part IV — the same surgery, applied to other theories',
      eyebrow='The most famous motivation turned out to be the weakest argument',
      h1='Inflation, on the<br>same operating table',
      sub='"It solves the horizon problem" holds two different things under one name.<br><em>Cut them apart and what survives is \\(n_s\\).</em>',
      byline_l='What you need: the particle horizon, e-folds, Episode 19\'s procedure',
      byline_r='\\(N_{\\min}=62.1\\) vs \\(N_{n_s}=57.0\\pm6.8\\)',
      body=BODY + '\n\n<p class="foot">This document is Episode 27 of "c·t = const, That Clicks", written for physics-minded high-school and university readers. The particle horizon \\(d_p=ct/(1-p)\\), the e-fold requirement \\(e^N\\ge(a_e/a_0)(H_{\\rm inf}/H_0)\\), the slow-roll result \\(n_s\\approx1-2/N\\), and Planck 2018\'s \\(n_s=0.9649\\pm0.0042\\) are all standard. <strong>Computed here are the \\(N_{\\min}\\) per reheating scale (62.1 at the GUT scale, 39.1 at \\(10^6\\) GeV), the inversion \\(N=57.0\\pm6.8\\) from \\(n_s\\), the 0.75σ discrepancy, and the 4.3–5.3 bits of surprise by Episode 19\'s procedure</strong> (kenshou/calc31.py). <em>\\(N=60\\) depends strongly on the reheating scale (a spread of 23), and \\(n_s\\approx1-2/N\\) is a result for a family of models (\\(R^2\\), α-attractors) rather than a prediction of every inflationary model.</em> Instantaneous reheating is assumed; prolonged reheating moves \\(N_{\\min}\\) further. §06\'s ledger is a rough calculation for common units, with the parameter price from Episode 5\'s \\(N_{\\rm data}=1701\\) and only \\(n_s\\) credited on inflation\'s side — an underestimate, to be read only as a comparison of orders. <strong>That the horizon problem vanishes at \\(p=1\\) does not support that expansion law</strong> (Episode 3\'s judgement is unchanged). Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model under examination, and the academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, the slider moves the reheating scale and shows where the two N values overlap. "Show the answer" opens each solution.')
