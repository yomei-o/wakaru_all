# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Part IV’s nine theories, laid out on one table — inflation, VSL, MOND, measuring the constants, CCC, the cosmon, Milne, conformal gravity, asymptotic safety. <strong>The same surgery applied to all of them, and a list of where the dividing line fell.</strong> Then the most important thing this part turned up — <em>good theories have already performed Episode 3’s surgery.</em> <strong>Exactly one had not.</strong></p>

<h2><span class="n">01</span>Nine theories on one table</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Ep.</th><th>Theory</th><th class="mid">(A) notation</th><th class="mid">(B) observable claim</th><th class="mid">Surgery</th></tr></thead>
<tbody>
<tr><th class="mid">27</th><td>Inflation</td><td class="mid">connect things causally</td><td class="mid">\(n_s\approx1-2/N\)</td><td class="mid">done</td></tr>
<tr class="hi"><th class="mid">28</th><td><strong>VSL</strong></td><td class="mid">a change of units</td><td class="mid">\(\alpha\) varies</td><td class="mid"><strong>✗</strong></td></tr>
<tr><th class="mid">29</th><td>MOND</td><td class="mid">posit \(a_0\)</td><td class="mid">dynamics set by \(g/a_0\)</td><td class="mid">done</td></tr>
<tr><th class="mid">30</th><td>Measuring constants</td><td class="mid">(not a notation)</td><td class="mid">\(\alpha\) invariant to 26 bits</td><td class="mid">──</td></tr>
<tr><th class="mid">31</th><td>CCC</td><td class="mid">a conformal gluing</td><td class="mid">a previous aeon persists</td><td class="mid">done</td></tr>
<tr><th class="mid">32</th><td>Cosmon</td><td class="mid">a non-expanding picture</td><td class="mid">\(w(z)\ne-1\)</td><td class="mid">done</td></tr>
<tr><th class="mid">33</th><td>Milne</td><td class="mid">a coordinate change</td><td class="mid">(nothing inside)</td><td class="mid">──</td></tr>
<tr><th class="mid">34</th><td>Conformal gravity</td><td class="mid">a gauge symmetry</td><td class="mid">rotation curves, \(\alpha_g\)</td><td class="mid">nothing to cut</td></tr>
<tr><th class="mid">35</th><td>Asymptotic safety</td><td class="mid">making \(G\) dimensionless</td><td class="mid">\(m_H\), number of predictions</td><td class="mid">done</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01</p>
<p style="margin:6px 0 0"><strong>Exactly one theory failed to separate (A) from (B): VSL.</strong><br>
── <em>Good theories have already performed Episode 3’s surgery.</em></p>
</div>

<h2><span class="n">02</span>The dividing line was not the name</h2>

<div class="seven">
<div class="row"><div class="mk">✗</div><div class="txt"><strong>It is not "does the name point at (A)?"</strong><span>The cosmon paper is titled "A Universe without expansion" — (A) side. VSL is (A) side too. <em>They match that far</em></span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>It is "can the theory itself tell (A) from (B)?"</strong><span>Wetterich states outright that the two pictures are Weyl-equivalent; Penrose states that at the gluing there is no ruler left</span></div></div>
<div class="row"><div class="mk">✗</div><div class="txt"><strong>VSL alone did not separate them</strong><span>So "the speed of light varies" hid the content (\(\alpha\) varies) and <em>the 26-bit constraint stopped being visible head-on</em></span></div></div>
</div>

<h2><span class="n">03</span>Every prediction sat in a dimensionless quantity</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Theory</th><th class="mid">Where the prediction sits</th><th class="mid">Dimension</th></tr></thead>
<tbody>
<tr><th>Inflation</th><td class="mid">\(n_s\)</td><td class="mid">dimensionless</td></tr>
<tr><th>VSL</th><td class="mid">\(\Delta\alpha/\alpha\)</td><td class="mid">dimensionless</td></tr>
<tr><th>MOND</th><td class="mid">\(g/a_0\)</td><td class="mid">dimensionless</td></tr>
<tr><th>CCC</th><td class="mid">Hawking-point statistics</td><td class="mid">dimensionless</td></tr>
<tr><th>Cosmon</th><td class="mid">\(w\)</td><td class="mid">dimensionless</td></tr>
<tr><th>Conformal gravity</th><td class="mid">the shape of rotation curves</td><td class="mid">dimensionless</td></tr>
<tr class="hi"><th>Asymptotic safety</th><td class="mid">\(m_H/v\)</td><td class="mid"><strong>dimensionless</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §03</p>
<p style="margin:6px 0 0"><strong>There were no exceptions.</strong> This is the strongest confirmation of Episode 3’s procedure.<br>
── <em>A theory that puts its claim in a dimensionful quantity never reaches the arena where it can be judged.</em></p>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">04</span>The core — a band of coincidences</h2>

<p>Laying them side by side turned up something else. Here is every coincidence in this part, measured in Episode 19’s bits of surprise.</p>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Coincidence</th><th class="mid">Surprise</th><th class="mid">Class</th></tr></thead>
<tbody>
<tr><th>\(\rho_\Lambda^{1/4}\) and \(m_\nu\) (previous series, extra 5)</th><td class="mid">4.7 bit</td><td class="mid">coincidence</td></tr>
<tr class="hi"><th>Inflation’s \(N\) agreeing (Ep. 27)</th><td class="mid">4.8 bit</td><td class="mid">explained → physics</td></tr>
<tr class="hi"><th>Asymptotic safety’s Higgs prediction (Ep. 35)</th><td class="mid">5.3 bit</td><td class="mid">explained → physics</td></tr>
<tr class="hi"><th>Conformal gravity’s \(\gamma_0\simeq1/25R_H\) (Ep. 34)</th><td class="mid">5.4 bit</td><td class="mid">coincidence</td></tr>
<tr class="hi"><th>MOND’s \(a_0\simeq cH_0/2\pi\) (Ep. 29)</th><td class="mid">5.9 bit</td><td class="mid">coincidence</td></tr>
<tr><th>One bit ↔ 1.96 fm (Ep. 18)</th><td class="mid">7.4 bit</td><td class="mid">coincidence</td></tr>
<tr><th>Koide’s relation (previous series, extra 4)</th><td class="mid">15.7 bit</td><td class="mid">empirical formula</td></tr>
<tr><th>The uniformity of the CMB (Ep. 17)</th><td class="mid">\(1.6\times10^5\) bit</td><td class="mid">a real problem</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>Six of them fall in the band from 4 to 7.5 bits</strong> (mean 5.6, spread 2.7).<br>
Why should coincidences thrown up by entirely independent theories land in the same narrow band?</p>
</div>

<div class="fig">
<p class="cap">Figure: every "surprise" this series has measured, on one axis. <strong>They cluster between 4 and 7.5 bits.</strong> Move the "threshold for noticing" and read off how many survive — <em>the band is most likely a selection effect.</em></p>
<canvas id="cv" width="720" height="390"></canvas>
<div class="controls">
  <label>threshold for noticing (bits)<input id="sb" type="range" min="0" max="180" value="40" step="1"></label>
  <span class="val" id="vb">4.0 bit</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#38343f"></i>judged a coincidence</span>
  <span><i class="swatch" style="background:#8a6a3a"></i>has an explanation (physics)</span>
  <span><i class="swatch" style="background:#d8d2dc"></i>below threshold (nobody notices)</span>
</div>
</div>

<div class="seven">
<div class="row"><div class="mk">↓</div><div class="txt"><strong>Under 4 bits (looser than 1 in 16)</strong><span>nobody notices — it does not even get recorded</span></div></div>
<div class="row hi"><div class="mk">◆</div><div class="txt"><strong>4 to 7 bits</strong><span><em>enough for a paper, not enough for a consensus</em> — where "interesting but not decisive" lives</span></div></div>
<div class="row"><div class="mk">↑</div><div class="txt"><strong>Over 15 bits (Koide’s relation)</strong><span>it becomes famous and demands an explanation — forty years on, having no derivation is itself the problem</span></div></div>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0">The band is most likely a <strong>selection effect</strong> — <em>too loose and nobody looks; too tight and it gets explained.</em><br>
── <strong>The scale built in Episode 19 turns out to measure the practice of physics itself.</strong></p>
</div>

<h2><span class="n">05</span>The ledger, summed up</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Theory</th><th class="mid">Parameters</th><th class="mid">What it buys</th><th class="mid">Net [bits]</th></tr></thead>
<tbody>
<tr><th>Inflation (Ep. 27)</th><td class="mid">\(+2\)</td><td class="mid">\(n_s\) and much else</td><td class="mid">\(-6.5\) (an underestimate)</td></tr>
<tr class="hi"><th>c·t = const (Ep. 25)</th><td class="mid">\(-1\)</td><td class="mid">the horizon problem disappears</td><td class="mid"><strong>\(-148.3\)</strong></td></tr>
<tr class="hi"><th>MOND (rotation curves only, Ep. 29)</th><td class="mid">\(+4\)</td><td class="mid">rotation curves from baryons</td><td class="mid"><strong>\(+1971\)</strong></td></tr>
<tr class="hi"><th>Conformal gravity (rotation curves only, Ep. 34)</th><td class="mid">\(+3\)</td><td class="mid">the same, plus a forbidden \(\Lambda\)</td><td class="mid"><strong>\(+1977\)</strong></td></tr>
<tr><th>Cosmon (Ep. 32)</th><td class="mid">\(+2\)</td><td class="mid">the size of \(\rho_\Lambda\) (up to 408)</td><td class="mid">a large credit</td></tr>
<tr><th>Asymptotic safety (Ep. 35)</th><td class="mid">\(+3\)</td><td class="mid">\(m_H\), ultraviolet finiteness</td><td class="mid">not yet assessable</td></tr>
</tbody>
</table>
</div>

<p>The unit is Episode 5’s balance (one parameter = 5.37 bits). <strong>The datasets differ, so these cannot be compared directly</strong> — as Episode 29 showed, <em>which dataset you measure on decides who wins.</em> This table exists to show that all of it can be written in one currency; it is not a league table.</p>

<h2><span class="n">06</span>The reveal — all four follow from one procedure</h2>

<div class="seven">
<div class="row"><div class="mk">1</div><div class="txt"><strong>Good theories have already performed Episode 3’s surgery</strong><span>only VSL had not (§01, §02)</span></div></div>
<div class="row"><div class="mk">2</div><div class="txt"><strong>Predictions sit in dimensionless quantities without exception</strong><span>a claim placed in a dimensionful quantity never reaches the arena (§03)</span></div></div>
<div class="row hi"><div class="mk">3</div><div class="txt"><strong>Interesting coincidences cluster at 4 to 7 bits</strong><span>a selection effect — too loose and nobody looks, too tight and it gets explained (§04)</span></div></div>
<div class="row"><div class="mk">4</div><div class="txt"><strong>Who wins depends on the dataset</strong><span>"dark matter or MOND" was never one question (§05, Ep. 29)</span></div></div>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §06</p>
<p style="margin:6px 0 0"><strong>All four follow from the single procedure built in Episode 3.</strong><br>
<em>"Dimensionful is bookkeeping, dimensionless is physics. If you have not named what you are comparing to, you have not yet made a sentence."</em><br>
That alone accounts for every dividing line among the nine.</p>
</div>

<div class="aside">
<span class="tag">Parts I to IV, one line each</span>
<strong>Part I</strong>: \(c\cdot t=\)const is a notation, not a model.<br>
<strong>Part II</strong>: wherever you put it, only one thing moves, and only its size is touched.<br>
<strong>Part III</strong>: measured as information, it was one number restated in eight languages.<br>
<strong>Part IV</strong>: applied to other theories, <em>the good ones had already done the surgery.</em>
</div>

<div class="caveat">
<span class="tag">The honest line — for Part IV as a whole</span>
<p style="margin:0 0 10px"><strong>(1) "Has the surgery been done?" is this series’ reading.</strong> How aware each theory’s proposers were is inferred from how the papers are written; <em>their intent has not been verified</em>. For VSL, the point that the name hid the content follows Ellis &amp; Uzan (2005); it does not mean VSL researchers failed to understand the distinction.</p>
<p style="margin:0 0 10px"><strong>(2) §04’s "band" is an observation on a sample of eight.</strong> Worse, it collects <em>only the coincidences this series chose to write about</em>, so the selection itself is biased — <strong>the "it is a selection effect" explanation comes out of a sample subject to selection effects</strong>. Read it as a recorded pattern, <em>not a quantitative claim</em>.</p>
<p style="margin:0 0 10px"><strong>(3) Each surprise in bits depends on how the prior range is drawn</strong> (Episode 19 §01). The values 4.7 to 7.4 can move by a few bits, so the width of the "band" is correspondingly vague.</p>
<p style="margin:0 0 10px"><strong>(4) §05’s ledger does not use a common dataset.</strong> Episode 25 used supernovae, Episodes 29 and 34 galaxy rotation curves, Episode 27 the CMB — <em>the table shows that one currency suffices, not who ranks where</em>. The parameter counts are rough in each case.</p>
<p style="margin:0"><strong>(5) This document neither endorses nor rejects any theory covered in Part IV.</strong> All except inflation are minority hypotheses; the academic standard remains the \(\Lambda\)CDM model including inflation, together with unmodified general relativity.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (Part IV, wrap-up)</p>
<ol>
<li>Which of the nine theories had not had the surgery?
<details><summary>Show the answer</summary><div class="ans"><strong>VSL alone (Episode 28)</strong>. It claimed (B) "\(\alpha\) varies" while keeping the (A) name "the speed of light varies", so <em>the 26-bit constraint on \(\alpha\) stopped being visible head-on</em>.</div></details></li>

<li>Was the dividing line "does the name point at (A)?"
<details><summary>Show the answer</summary><div class="ans">No. The cosmon paper title "A Universe without expansion" is (A) side, and so is VSL. <strong>The line was "can the theory itself tell (A) from (B)?"</strong> — Wetterich states explicitly that the two pictures are Weyl-equivalent.</div></details></li>

<li>What do the seven theories’ predictions have in common?
<details><summary>Show the answer</summary><div class="ans"><strong>They all sit in dimensionless quantities</strong> — \(n_s\), \(\Delta\alpha/\alpha\), \(g/a_0\), \(w\), \(m_H/v\) and so on. It is the strongest confirmation of Episode 3’s procedure: <em>a claim placed in a dimensionful quantity never reaches the arena where it can be judged</em>.</div></details></li>

<li>What is the "band of coincidences", and what explains it?
<details><summary>Show the answer</summary><div class="ans">Six of the coincidences this series covered fall between <strong>4 and 7.5 bits</strong> (mean 5.6). The explanation is most likely a <strong>selection effect</strong> — <em>under 4 bits nobody notices; over 15 bits it becomes famous and demands an explanation. From 4 to 7 bits is where "enough for a paper, not enough for a consensus" lives.</em> But as caveat (2) says, the sample is small and biased.</div></details></li>

<li>(Harder) Where did Part IV’s four findings come from?
<details><summary>Show the answer</summary><div class="ans"><strong>The single procedure built in Episode 3</strong> — "dimensionful is bookkeeping, dimensionless is physics; if you have not named what you are comparing to, you have not yet made a sentence." Whether the surgery was done, where the prediction sits, how a coincidence’s surprise is measured, and that the winner depends on the dataset — <em>all four are consequences of that one procedure</em>.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: good theories have already had the surgery</h2>
<p>Part IV’s nine theories went onto one table. <strong>Exactly one failed to separate (A) notation from (B) an observable claim: VSL.</strong> And the dividing line was not "does the name point at (A)?" — the cosmon paper title and VSL are both (A) side, and they match that far. <em>The line was whether the theory itself could tell them apart.</em></p>
<p>The predictions went onto the table too — \(n_s\), \(\Delta\alpha/\alpha\), \(g/a_0\), Hawking-point statistics, \(w\), the shape of rotation curves, \(m_H/v\). <strong>Dimensionless without exception.</strong> It is the strongest confirmation of Episode 3’s procedure — <em>a theory that puts its claim in a dimensionful quantity never reaches the arena at all.</em></p>
<p>Laying them out turned up something new. Measured in Episode 19’s bits of surprise, <strong>six of the coincidences fall between 4 and 7.5 bits</strong> (mean 5.6). Coincidences from entirely independent theories landing in one narrow band — the cause is most likely a <strong>selection effect</strong>. <em>Under 4 bits nobody notices; over 15 bits (Koide’s relation) it becomes famous and demands an explanation. From 4 to 7 bits is where "enough for a paper, not enough for a consensus" lives.</em> <strong>The scale built in Episode 19 turns out to measure the practice of physics itself.</strong></p>
<p>And the reveal: whether the surgery was done, where the prediction sits, which band a coincidence lands in, and that the winner depends on the dataset. <strong>All four follow from the one procedure built in Episode 3</strong> — <em>"dimensionful is bookkeeping, dimensionless is physics; if you have not named what you are comparing to, you have not yet made a sentence."</em> That alone accounts for every dividing line among the nine.</p>
</div>

<div class="next">
<span class="lbl">Next time — Episode 37 (Part V begins)</span>
Part V goes <strong>looking head-on for the places where this tool breaks</strong>. Part IV met a <em>ghost</em> twice — the conformal factor of Einstein gravity in the previous series’ Episode 9, and the spin-2 ghost of conformal gravity in Episode 34. Part V goes to the source. First, <strong>quantum anomalies</strong> — when Episode 11 counted "nothing happens to light", that was a <em>classical</em> statement. Quantised, a resolution scale \(\mu\) enters and conformal symmetry breaks. <strong>We will measure that breaking in bits.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sb=document.getElementById('sb'), vb=document.getElementById('vb'), ro=document.getElementById('ro');
  var X0=300, X1=690, Y0=44;
  var D=[
    ['rho_L and m_nu', 4.7, 0],
    ['inflation\'s N', 4.8, 1],
    ['asympt. safety Higgs', 5.3, 1],
    ['conformal gravity gamma_0', 5.4, 0],
    ['MOND\'s a_0', 5.9, 0],
    ['one bit = 1.96 fm', 7.4, 0],
    ['Koide\'s relation', 15.7, 0],
    ['uniformity of the CMB', 20.0, 2]
  ];
  var XMAX=20;

  function px(b){ return X0+Math.min(b,XMAX)/XMAX*(X1-X0); }

  function draw(){
    var th=parseInt(sb.value,10)/10;
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.fillStyle='#f2eef4';
    g.fillRect(px(4.0), Y0-14, px(7.5)-px(4.0), 8*40+18);
    g.fillStyle='#9a8fa4'; g.textAlign='center';
    g.fillText('the 4-7.5 bit band', (px(4.0)+px(7.5))/2, Y0-20);

    g.textAlign='center';
    for(var b=0;b<=20;b+=5){
      var x=px(b);
      g.strokeStyle=(b===0?'#cdc8d2':'#f4f2f6'); g.lineWidth=(b===0?1.6:1);
      g.beginPath(); g.moveTo(x,Y0-14); g.lineTo(x,Y0+8*40+6); g.stroke();
      g.fillStyle='#9c96a4'; g.fillText(b+' bit', x, Y0+8*40+22);
    }

    var cnt=0;
    for(var i=0;i<D.length;i++){
      var b=D[i][1], kind=D[i][2];
      var below=(b<th);
      if(!below) cnt++;
      var y=Y0+i*40+8;
      var col = below ? '#d8d2dc' : (kind===1 ? '#8a6a3a' : '#38343f');
      g.fillStyle=col; g.globalAlpha=0.9;
      g.fillRect(X0, y, Math.max(px(b)-X0,3), 22);
      g.globalAlpha=1;
      g.fillStyle= below ? '#b0a8b6' : '#3a3640';
      g.textAlign='right';
      g.font='12px ui-sans-serif,system-ui,sans-serif';
      g.fillText(D[i][0], X0-12, y+16);
      g.font='11px ui-sans-serif,system-ui,sans-serif';
      g.textAlign='left'; g.fillStyle=col;
      if(kind===2) g.fillText('-> 1.6e5 bit (off the scale)', px(b)-170, y+16);
      else g.fillText(b.toFixed(1)+' bit', px(b)+6, y+16);
    }

    g.strokeStyle='#7a6a84'; g.lineWidth=1.8; g.setLineDash([4,4]);
    g.beginPath(); g.moveTo(px(th),Y0-14); g.lineTo(px(th),Y0+8*40+6); g.stroke();
    g.setLineDash([]);

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('surprise = -log2( width landed in / prior range )', (X0+X1)/2-80, Y0+8*40+46);

    vb.textContent=th.toFixed(1)+' bit';
    ro.textContent='threshold '+th.toFixed(1)+' bits　→　'+cnt+' of 8 get noticed'+
      '　/　six sit in the 4-7.5 band (mean 5.6, spread 2.7)'+
      (th<4?'　★ lowering it further picks nothing up — below the band is empty':'');
  }
  sb.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-36-partIV.html', acc='#38343f', ops='#8a6a3a',
      title='Onto the operating table ── c·t = const, That Clicks, Episode 36 (Part IV wrap-up)',
      ep='EPISODE 36 ／ Part IV — wrap-up',
      eyebrow='Exactly one had not done it',
      h1='Onto the<br>operating table',
      sub='The same surgery on nine theories, and a list of where the line fell.<br><em>Plus a "band of coincidences" that only showed up once they were side by side.</em>',
      byline_l='What you need: Part IV\'s nine episodes, Episode 19\'s scale, Episode 5\'s balance',
      byline_r='4 to 7 bits — where "interesting but not decisive" lives',
      body=BODY + '\n\n<p class="foot">This document is Episode 36 of "c·t = const, That Clicks" (Part IV wrap-up), written for physics-minded high-school and university readers. It collects results from Episodes 27 to 35; the only new computation is §04\'s tally (kenshou/calc40.py) — for the numbers and sources of each individual result, see the endnotes of the episode concerned. <strong>"Has the surgery been done?" is this series\' reading</strong>; how aware each theory\'s proposers were is inferred from how the papers are written and their intent has not been verified — for VSL, the point that the name hid the content follows Ellis &amp; Uzan (2005) and does not mean VSL researchers failed to understand the distinction. <strong>§04\'s "band of coincidences" is an observation on a sample of eight, and one collecting only the coincidences this series chose to write about</strong> — the "it is a selection effect" explanation itself comes out of a sample subject to selection effects, so read it as <em>a recorded pattern rather than a quantitative claim</em>. Each surprise in bits depends on how the prior range is drawn (Episode 19 §01). §05\'s ledger does not use a common dataset (Episode 25 supernovae, Episodes 29 and 34 galaxy rotation curves, Episode 27 the CMB) — <em>it shows that one currency suffices, not who ranks where</em>. <strong>This document neither endorses nor rejects any theory covered in Part IV</strong>; all except inflation are minority hypotheses, and the academic standard remains the \\(\\Lambda\\)CDM model including inflation, together with unmodified general relativity. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, move the threshold to see that below the band is empty. "Show the answer" opens each solution.')
