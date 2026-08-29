# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">"What would change if \(1/\alpha\) were exactly 137?" — and "is changing this dimensionless quantity ever the same as changing that one?" These turned out to be <strong>one question</strong>: <em>is there hidden structure among the constants?</em> Digging led all the way to <strong>a 4.1-bit prediction beating a 15.7-bit discovery.</strong></p>

<h2><span class="n">01</span>First, 137 — a vast exclusion and almost no physical difference</h2>

<div class="calc">
<span class="tag">CODATA 2022</span>
$$\frac1\alpha=137.035999177(21)\qquad\Longrightarrow\qquad
\frac{0.035999}{2.1\times10^{-8}}=\mathbf{1.7\times10^{6}\,\sigma}$$
<p class="lbl">yet as a value of \(\alpha\) it differs by only <strong>0.026 per cent</strong></p>
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>What</th><th class="mid">Shift</th><th class="mid">\(\sigma\)</th></tr></thead>
<tbody>
<tr><th>Electron g−2</th><td class="mid">\(3.05\times10^{-7}\)</td><td class="mid">\(2.3\times10^{6}\)</td></tr>
<tr><th>Hydrogen 1S–2S</th><td class="mid">1.3 THz</td><td class="mid">\(1.3\times10^{11}\)</td></tr>
<tr class="hi"><th>Neutron lifetime</th><td class="mid"><strong>\(+1.53\) s</strong></td><td class="mid"><strong>\(3.1\)</strong></td></tr>
<tr><th>BBN helium \(Y_p\)</th><td class="mid">\(7.4\times10^{-5}\)</td><td class="mid">\(0.025\) (invisible)</td></tr>
<tr><th>The Hoyle state</th><td class="mid">──</td><td class="mid">needs 4 per cent; this is 1/152 of that</td></tr>
</tbody>
</table>
</div>

<p><strong>The only thing that bites in the world is the neutron lifetime</strong> (the electromagnetic part of the \(n\)–\(p\) mass difference, \(-1.04\) MeV, shifts by 0.27 keV; \(\tau\propto Q^{-5}\) gives 1.5 seconds) — and only at 3\(\sigma\). <em>The exclusion is vast because the measurements are precise, not because the physics is delicately balanced.</em></p>

<h2><span class="n">02</span>So why does 137 nag? — because it is an integer</h2>

<div class="seven">
<div class="row"><div class="mk">?</div><div class="txt"><strong>An integer would make \(\alpha\) a count, not a ratio</strong><span>in bonus ③'s four types, <em>type N rather than type R</em></span></div></div>
<div class="row"><div class="mk">1929</div><div class="txt"><strong>That is exactly what Eddington bet on</strong><span>first 136, then 137</span></div></div>
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>Measured by Episode 19's practice: 3.8 bits</strong><span>uniform on \([136.5,137.5]\), landing within \(\pm0.036\) of an integer has probability 0.072 — <em>the bottom of the band of coincidences</em></span></div></div>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §01–02</p>
<p style="margin:6px 0 0"><strong>Eddington's mistake was treating a 3.8-bit coincidence as a 0-bit identity.</strong><br>
And there is a sharper objection — <em>\(\alpha\) runs</em> (Episode 37; it is 128 at \(M_Z\)).<br>
<strong>Without saying at which scale it is an integer, the claim is not yet a sentence.</strong><br>
── In his day the running was unknown, so <em>it was a sentence then and is not one now.</em></p>
</div>

<h2><span class="n">03</span>The other question — degeneracy comes in three kinds</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th class="mid">Type</th><th>What it is</th><th class="mid">Really</th><th class="mid">Finding one tells you about</th></tr></thead>
<tbody>
<tr><th class="mid">A</th><td>indistinguishable in principle</td><td class="mid">redundancy of notation</td><td class="mid"><strong>your notation</strong></td></tr>
<tr><th class="mid">B</th><td>current instruments cannot separate them</td><td class="mid">limits of the tools</td><td class="mid"><strong>your instruments</strong></td></tr>
<tr class="hi"><th class="mid">C</th><td>thought independent, actually related</td><td class="mid">structure of nature</td><td class="mid"><strong>physics</strong></td></tr>
</tbody>
</table>
</div>

<h2><span class="n">04</span>Type A — the question itself is real</h2>

<div class="calc">
<span class="tag">The cleanest example</span>
$$\text{only the combination}\quad \bar\theta=\theta+\arg\det M_q\quad\text{is physical}$$
<p class="lbl">move \(\theta\) and rotate the quark phases at the same time — <strong>and nothing happens</strong></p>
</div>

<p>The CKM matrix is the same: of a 3×3 unitary matrix's nine parameters, rephasing removes <strong>five directions</strong> that are <em>unobservable in principle</em> (\(26.8\) bits' worth of pure notation).</p>

<div class="keybox">
<p class="lbl">Conclusion of §04</p>
<p style="margin:6px 0 0">But Episode 47's 19 parameters are the count <strong>after</strong> these are removed.<br>
"No exact degeneracies remain" is the answer, and <em>only because we constructed it that way</em>.<br>
── <strong>Finding a type A degeneracy tells you about your own notation, not about nature.</strong></p>
</div>

<div class="aside">
<span class="tag">The oddest thing that fell out</span>
\(\bar\theta\) is physical only because <strong>no quark mass is zero</strong>. Were \(m_u=0\), \(\bar\theta\) could be rotated away entirely and the strong CP problem would vanish (measured: \(m_u=2.16\pm0.11\) MeV, excluding zero at \(19.6\sigma\)).<br>
── <strong>The 19 parameters are not fully independent. Remove one Yukawa and \(\bar\theta\) goes with it. The <em>number</em> of constants depends on the <em>values</em> of the constants.</strong>
</div>

<h2><span class="n">05</span>Type B — and one that was a mirage</h2>

<div class="seven">
<div class="row"><div class="mk">◎</div><div class="txt"><strong>Real: the \(m_q\) direction in spectroscopy</strong><span>bonus ① — a condition number of 1196, still with us</span></div></div>
<div class="row hi"><div class="mk">✗</div><div class="txt"><strong>Mirage: \(\alpha\) and \(m_e\) in atomic physics</strong><span>gross structure \(\propto\alpha^2m_e\), fine \(\propto\alpha^4m_e\) — but <em>take the ratio and \(m_e\) drops out</em></span></div></div>
<div class="row"><div class="mk">3</div><div class="txt"><strong>In fact \(m_e\) never appears in a dimensionless observable</strong><span>the ratio of two transitions in one atom always kills it — <em>a mirage created by writing dimensionful quantities</em> (Episode 3)</span></div></div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">06</span>The core — searching for type C has a price</h2>

<p>A type C relation, if found, is a discovery in physics. So may one simply <strong>search</strong>? The instinct is to call that numerology — <em>but where exactly is the difference?</em></p>

<div class="calc">
<span class="tag">Look-elsewhere</span>
$$\text{having tried }M\text{ candidate relations, the threshold for meaning is }\log_2 M\text{ bits}$$
</div>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Reading</th><th class="mid">Search space \(M\)</th><th class="mid">Threshold</th><th class="mid">Koide (15.7 bits)</th></tr></thead>
<tbody>
<tr><th>Narrow (only Koide's form)</th><td class="mid">\(126\)</td><td class="mid">\(7.0\) bit</td><td class="mid">passes</td></tr>
<tr class="hi"><th>Wide (subsets of 12 masses, etc.)</th><td class="mid">\(1.4\times10^{8}\)</td><td class="mid">\(27.1\) bit</td><td class="mid"><strong>11.4 bits short</strong></td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The main point of this episode</p>
<p style="margin:6px 0 0"><strong>b–τ unification was predicted in advance by SU(5), so there was one candidate — a threshold of zero bits.</strong><br>
In raw surprise Koide (15.7) beats b–τ (4.1) by 11.6 bits, but<br>
<strong>subtract the price of the search and it reverses.</strong><br>
── <em>The difference between "theory first" and "numbers first" comes out as exactly \(\log_2M\) bits.</em><br>
Not a social convention — <strong>the result of a subtraction.</strong></p>
</div>

<div class="fig">
<p class="cap">Figure: subtract the price of the search from the raw surprise and the ranking flips. <strong>Move the slider for how widely you searched</strong> — raising \(M\) sinks Koide alone, while <em>b–τ, predicted in advance, does not move.</em></p>
<canvas id="cv" width="720" height="360"></canvas>
<div class="controls">
  <label>breadth of the search, \(\log_2 M\)<input id="sm" type="range" min="0" max="40" value="7" step="1"></label>
  <span class="val" id="vm">7</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#6a3a5a"></i>Koide's relation (found by searching)</span>
  <span><i class="swatch" style="background:#2a5a4a"></i>b–τ unification (predicted first)</span>
  <span><i class="swatch" style="background:#c8c2d0"></i>the line of meaning (0 bits)</span>
</div>
</div>

<h2><span class="n">07</span>And this was the same disease as naturalness</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Setting</th><th class="mid">The "space" required</th><th class="mid">Since</th></tr></thead>
<tbody>
<tr><th>Ep. 19: surprise</th><td class="mid">the quantity's <strong>prior range</strong></td><td class="mid">flagged in Ep. 19 §01</td></tr>
<tr><th>Ep. 48: naturalness</th><td class="mid">the parameter's <strong>prior</strong></td><td class="mid">became a theorem in bonus ③</td></tr>
<tr class="hi"><th>Here: numerical coincidence</th><td class="mid">the <strong>search space</strong></td><td class="mid">the verdict flips with the declaration</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">Conclusion of §07 — the sixth compression</p>
<p style="margin:6px 0 0"><strong>All three were one question: is there a canonical measure?</strong><br>
A probability needs a measure, and without one there is no probability.<br>
── A search space is finite <em>if you declare a bound</em>. <strong>Declaring it first is the only way to make the question well-posed.</strong><br>
<em>"Theory first" was never a social convention — it was fixing the measure in advance.</em></p>
</div>

<h2><span class="n">08</span>A bonus — Episode 36's "band" now has a threshold</h2>

<p>Episode 36 <strong>observed</strong> that interesting coincidences cluster at 4–7.5 bits and called it a selection effect. Now the <strong>threshold can be computed</strong> (7–27 bits) — <em>the band sits far below it, which is why none of them mean anything</em>. Koide alone escaped the band, and is still 11.4 bits short on the wide reading.</p>

<div class="keybox">
<p class="lbl">Conclusion of §08</p>
<p style="margin:6px 0 0"><strong>An observation became a subtraction.</strong></p>
</div>

<div class="caveat">
<span class="tag">The honest line</span>
<p style="margin:0 0 10px"><strong>(1) The weakest point is §06's estimate of the search space.</strong> The narrow and wide readings differ by <em>20 bits</em>, and there is no way to decide between them — <strong>which is precisely §07's claim.</strong></p>
<p style="margin:0 0 10px"><strong>(2) Koide's 15.7 bits is inherited from Episodes 19 and 36</strong> and depends on the prior range, as does b–τ's 4.1.</p>
<p style="margin:0 0 10px"><strong>(3) b–τ's "zero search space" is an idealisation.</strong> There are other grand unified candidates, and <em>counting which models were tried would add a few bits here too</em> — "small", not "zero".</p>
<p style="margin:0 0 10px"><strong>(4) §01's neutron-lifetime estimate is rough.</strong> The electromagnetic part of the \(n\)–\(p\) mass difference (\(\approx-1.04\) MeV) varies between lattice calculations, and \(\tau\propto Q^{-5}\) is a phase-space approximation — <em>do not read it more precisely than "of order 3\(\sigma\)"</em>.</p>
<p style="margin:0"><strong>(5) §07's unification is this series' reading</strong>, not the standard formulation in statistics — multiple-comparison corrections and Bayes factors are finer existing machinery.</p>
</div>

<div class="prob">
<p class="lbl">Exercises</p>
<ol>
<li>If \(1/\alpha\) were exactly 137, what in the world would change?
<details><summary>Show the answer</summary><div class="ans"><strong>The neutron lifetime alone</strong> (\(+1.53\) s, 3.1\(\sigma\)). In the laboratory g−2 sees it at \(2.3\times10^6\sigma\) and 1S–2S at \(1.3\times10^{11}\sigma\), but <em>BBN sees 0.025\(\sigma\) and the Hoyle state needs 152 times more</em>. <strong>The exclusion is vast because the measurements are precise.</strong></div></details></li>

<li>What was Eddington's mistake?
<details><summary>Show the answer</summary><div class="ans"><strong>Treating a 3.8-bit coincidence as a 0-bit identity.</strong> And today there is more: <em>\(\alpha\) runs</em> (128 at \(M_Z\)), so <strong>without naming the scale the claim is not a sentence</strong> — it was one in his day and is not one now.</div></details></li>

<li>What do the three types of degeneracy each tell you?
<details><summary>Show the answer</summary><div class="ans"><strong>A</strong> (exact) — about your notation; <strong>B</strong> (observational) — about your instruments; <strong>C</strong> (hidden relation) — <em>about physics</em>. The test is <strong>"could observation break it?"</strong> A cannot; C can (if b–τ failed, SU(5) would die).</div></details></li>

<li>Why does a 4.1-bit prediction beat a 15.7-bit discovery?
<details><summary>Show the answer</summary><div class="ans"><strong>Because you subtract \(\log_2M\), the price of the search.</strong> b–τ was predicted first, so one candidate and a threshold of zero; Koide was found by searching, with a threshold of 7–27 bits — <em>on the wide reading it falls 11.4 bits short</em>. <strong>The "theory first" difference comes out as exactly \(\log_2M\) bits.</strong></div></details></li>

<li>(Harder) What do surprise, naturalness and numerical coincidence share?
<details><summary>Show the answer</summary><div class="ans"><strong>All three require a "space"</strong> — a prior range, a prior, a search space. <em>All three were the one question "is there a canonical measure?"</em> (the sixth compression). And <strong>"theory first" means fixing the measure in advance.</strong></div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary: "theory first" meant fixing the measure first</h2>
<p>\(1/\alpha=137\) exactly is excluded at <strong>\(1.7\times10^6\sigma\)</strong>, yet the physical difference is only <strong>0.026 per cent</strong> — the sole effect in the world is a 3\(\sigma\) shift in the neutron lifetime. It nags because 137 is an integer, and the surprise of that nearness is <strong>3.8 bits</strong>, the bottom of the band. <em>Eddington's mistake was treating a 3.8-bit coincidence as a 0-bit identity</em> — and since \(\alpha\) runs, the claim today is <strong>not even a sentence</strong>.</p>
<p>"Changing this is the same as changing that" came in <strong>three kinds</strong>. <strong>Type A</strong> is real — \(\bar\theta=\theta+\arg\det M_q\), and the CKM's five directions. But the 19 parameters are the count after those are removed, so <em>finding a type A degeneracy tells you about your own notation</em>. <strong>Type B</strong> survives as bonus ①'s \(m_q\) direction, while atomic physics' \(\alpha\)–\(m_e\) was <em>a mirage made by writing dimensionful quantities</em>.</p>
<p>And <strong>searching for type C has a price</strong>. Having tried \(M\) candidates, the threshold is \(\log_2M\) — Koide's 15.7 bits passes the narrow reading (7.0) and falls 11.4 short of the wide one (27.1). But b–τ unification was <em>predicted first</em>: one candidate, zero threshold. <strong>A 4.1-bit prediction beats a 15.7-bit discovery.</strong></p>
<p>Finally — surprise (prior range), naturalness (prior) and numerical coincidence (search space) were <strong>one question: is there a canonical measure?</strong> (the sixth compression). <em>"Theory first" was never a social convention; it was fixing the measure in advance.</em> And Episode 36's band now has a threshold — <strong>an observation became a subtraction.</strong></p>
</div>

<div class="next">
<span class="lbl">On to bonus ⑤</span>
§07 collapsed everything onto "is there a canonical measure?". <strong>So — is there?</strong> Bonus ③ answered "compact gives Haar, non-compact gives nothing", but <em>that was too coarse</em>. Next we follow the thread that <strong>the renormalisation group hands out the measure</strong> — and score all 20 Standard Model parameters by the shape of their beta functions, <strong>hitting the three great fine-tuning problems with zero false positives.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sm=document.getElementById('sm'), vm=document.getElementById('vm'), ro=document.getElementById('ro');
  var X0=90, X1=690, Y0=40, Y1=280;
  var KO=15.7, BT=4.1;

  function py(v){ return Y1-(v+20)/40*(Y1-Y0); }

  function draw(){
    var M=parseInt(sm.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='11px ui-sans-serif,system-ui,sans-serif';

    g.textAlign='right'; g.fillStyle='#9c96a4';
    for(var v=-20;v<=20;v+=10){
      g.strokeStyle=(v===0?'#cdc8d2':'#f2f0f4'); g.lineWidth=(v===0?1.8:1);
      g.beginPath(); g.moveTo(X0,py(v)); g.lineTo(X1,py(v)); g.stroke();
      g.fillText((v>0?'+':'')+v+' bit', X0-8, py(v)+4);
    }
    g.fillStyle='#a89fae'; g.textAlign='left';
    g.fillText('above this line, or it means nothing', X0+10, py(0)-8);

    var bw=(X1-X0)/2;
    var items=[['Koide (found by searching)', KO-M, '#6a3a5a'],
               ['b-tau (predicted first)', BT, '#2a5a4a']];
    for(var i=0;i<2;i++){
      var x=X0+i*bw+50, val=items[i][1];
      g.fillStyle=items[i][2]; g.globalAlpha=0.9;
      var y0=py(0), y1=py(val);
      g.fillRect(x, Math.min(y0,y1), bw-100, Math.abs(y1-y0));
      g.globalAlpha=1;
      g.fillStyle='#3a3640'; g.textAlign='center';
      g.fillText(items[i][0], x+(bw-100)/2, Y1+20);
      g.fillStyle=items[i][2];
      g.font='13px ui-sans-serif,system-ui,sans-serif';
      g.fillText((val>0?'+':'')+val.toFixed(1), x+(bw-100)/2, y1+(val>0?-8:16));
      g.font='11px ui-sans-serif,system-ui,sans-serif';
    }

    g.fillStyle='#7d7686'; g.textAlign='center';
    g.font='12px ui-sans-serif,system-ui,sans-serif';
    g.fillText('raw surprise minus the price of the search (log2 M)', (X0+X1)/2, Y1+46);

    vm.textContent=String(M);
    var ko=KO-M, msg;
    if(ko>BT) msg='　Koide still ahead — it needs a declaration that the search was narrow';
    else if(ko>0) msg='　★ reversed — the prediction now beats the discovery';
    else msg='　★ Koide is below the line — it has lost its meaning';
    ro.textContent='log2 M = '+M+' ('+Math.round(Math.pow(2,M)).toLocaleString('en-US')+' candidates tried)'+
      '　→　Koide '+ko.toFixed(1)+' bit / b-tau '+BT.toFixed(1)+' bit'+msg;
  }
  sm.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-b4-relations.html', acc='#6a3a5a', ops='#2a5a4a',
      title='Bonus ④: is there hidden structure among the constants? ── c·t = const, That Clicks',
      ep='BONUS ④ ／ dug after the main series closed',
      eyebrow='A 4.1-bit prediction beats a 15.7-bit discovery',
      h1='"Theory first" meant<br>fixing the measure first',
      sub='Being near 137, degeneracies among constants, and the price of searching for relations.<br><em>All three collapsed onto one question.</em>',
      byline_l='What you need: Episode 19\'s scale, Episode 36\'s band, Episode 37\'s running, Episode 47\'s map, bonus ③\'s types',
      byline_r='The sixth compression — three questions into one',
      body=BODY + '\n\n<p class="foot">This document is bonus episode ④ of "c·t = const, That Clicks", written after the main 50 episodes closed, for physics-minded high-school and university readers. The numbers are computed in kenshou/calc60.py, calc61.py and calc62.py. Eddington\'s numerology, CKM rephasing, the \\(\\bar\\theta\\) combination, b–τ unification and the look-elsewhere effect are all standard material. <strong>The weakest point is §06\'s estimate of the search space</strong> — the narrow and wide readings differ by 20 bits and there is no way to decide between them (<em>which is precisely §07\'s claim</em>). <strong>Koide\'s 15.7 bits and b–τ\'s 4.1 both depend on the prior range</strong>, and b–τ\'s "zero search space" is an idealisation (counting other grand unified candidates would add a few bits). <strong>§01\'s neutron-lifetime estimate is rough</strong>: the electromagnetic part of the \\(n\\)–\\(p\\) mass difference varies between lattice calculations and \\(\\tau\\propto Q^{-5}\\) is a phase-space approximation — do not read it more precisely than "of order 3\\(\\sigma\\)". <strong>§07\'s unification is this series\' reading</strong> rather than the standard formulation in statistics, where multiple-comparison corrections and Bayes factors are finer existing machinery. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, widen the search space and watch the ranking flip. "Show the answer" opens each solution.')
