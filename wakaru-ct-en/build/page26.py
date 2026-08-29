# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, '.')
from mkpage import build

BODY = r'''<p class="lead">Part III measured the universe with eight rulers — distributed consensus, addressing, surprise, light sheets, arrows of time, instruction set, codes, bandwidth, description length. Laid out together, <strong>the same numbers keep reappearing</strong>. \(1.5\times10^{-18}\) three times, \(140\) four times, \(0.035\) twice. <em>When different rulers give the same number, is that a discovery, or were they measuring the same thing all along?</em> We turn Episode 19's procedure on the series itself.</p>

<h2><span class="n">01</span>\(1.5\times10^{-18}\) appeared three times</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Source</th><th class="mid">Formula</th><th class="mid">Value</th></tr></thead>
<tbody>
<tr><th>Episode 6 · occupancy</th><td class="mid">\((S/\ln2)/N\)</td><td class="mid">\(1.5132\times10^{-18}\)</td></tr>
<tr><th>Episode 6 · black hole share</th><td class="mid">\(\sum A_{BH}/A_H\)</td><td class="mid">\(1.5132\times10^{-18}\)</td></tr>
<tr><th>Episode 21 · arrow of time</th><td class="mid">\(10^{-0.127\times140.24}\)</td><td class="mid">\(1.55\times10^{-18}\)</td></tr>
</tbody>
</table>
</div>

<div class="calc">
<span class="tag">The answer — one line</span>
<p class="lbl">straight from the definition of holography</p>
$$N=\frac{A}{4\ell_P^2\ln2}\qquad\Longrightarrow\qquad \frac{S/\ln2}{N}=\frac{4\ell_P^2 S}{A}=\frac{\sum A_{BH}}{A_H}$$
<p class="lbl">the ratio is 1.000000: as long as black holes dominate \(S\), this is an <strong>identity</strong></p>
</div>

<p>Nor is the third independent — Episode 21's \(0.127\) decades per step was itself obtained by taking a difference that would land on \(1.5\times10^{-18}\). <strong>The \(1.5\times10^{-18}\) that appeared three times is one number.</strong></p>

<h2><span class="n">02</span>\(140\) appeared four times</h2>

<div class="seven">
<div class="row"><div class="mk">①</div><div class="txt"><strong>Episode 2 · the clock \(N_t\)</strong><span>\(\ln(t_0/t_P)=140.24\)</span></div></div>
<div class="row"><div class="mk">②</div><div class="txt"><strong>Episode 20 · logarithmic steps</strong><span>the same \(\ln(t_0/t_P)\)</span></div></div>
<div class="row"><div class="mk">③</div><div class="txt"><strong>Episode 21 · "a 140-move program"</strong><span>the same</span></div></div>
<div class="row"><div class="mk">④</div><div class="txt"><strong>Episode 21 · the 140.24 multiplying \(0.127\)</strong><span>the same</span></div></div>
<div class="row hi"><div class="mk">◆</div><div class="txt"><strong>Only the temperature one is independent</strong><span>\(N_T=\ln(T_P/T_0)=73.03\), giving \(N_T/N_t=0.5207\approx1/2\) — a reflection of radiation domination \(T\propto t^{-1/2}\) covering most of the logarithmic range</span></div></div>
</div>

<div class="divider">◇　◇　◇</div>

<h2><span class="n">03</span>Every headline number of Part III</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Quantity</th><th class="mid">Value</th><th class="mid">Origin</th></tr></thead>
<tbody>
<tr><th>Horizon capacity \(N\)</th><td class="mid">\(2.956\times10^{122}\) bit</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr><th>Capacity growth \(dN/dt\)</th><td class="mid">\(1.358\times10^{105}\) bit/s</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr><th>Operations per bit \(\Omega/N\)</th><td class="mid">0.0351</td><td class="mid">\(p\)</td></tr>
<tr><th>Occupancy</th><td class="mid">\(1.513\times10^{-18}\)</td><td class="mid">\(t_0,\ \ell_P,\ S\)</td></tr>
<tr class="hi"><th>Black hole share</th><td class="mid">\(1.513\times10^{-18}\)</td><td class="mid"><strong>= occupancy</strong></td></tr>
<tr class="hi"><th>Arrow of time</th><td class="mid">\(1.55\times10^{-18}\)</td><td class="mid"><strong>= occupancy</strong></td></tr>
<tr class="hi"><th>Redundancy \(n/k\)</th><td class="mid">\(6.61\times10^{17}\)</td><td class="mid"><strong>= 1/occupancy</strong></td></tr>
<tr><th>Logarithmic steps</th><td class="mid">140.24</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr><th>Temperature steps \(N_T\)</th><td class="mid">73.03</td><td class="mid">\(T_0\)</td></tr>
<tr><th>Channel capacity \(C\)</th><td class="mid">\(6.789\times10^{104}\) bit/s</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr class="hi"><th>\(C\cdot t/N\)</th><td class="mid">1.000000</td><td class="mid"><strong>identity</strong></td></tr>
<tr class="hi"><th>\((dN/dt)/C\)</th><td class="mid">2.000000</td><td class="mid"><strong>identity</strong></td></tr>
<tr><th>Price of one parameter</th><td class="mid">5.37 bit</td><td class="mid">\(N_{\rm data}\)</td></tr>
<tr><th>Cost of misfit</th><td class="mid">153.6 bit</td><td class="mid">\(\Delta\chi^2\)</td></tr>
<tr><th>CMB modes</th><td class="mid">\(6.255\times10^{6}\)</td><td class="mid">\(l_{\max}\)</td></tr>
<tr><th>One bit ↔ a length</th><td class="mid">1.96 fm</td><td class="mid">\(t_0,\ \ell_P\)</td></tr>
<tr><th>Share doing nothing</th><td class="mid">95.0 %</td><td class="mid">\(\Omega_\Lambda,\ \Omega_{\rm dm}\)</td></tr>
<tr><th>Horizon problem's information</th><td class="mid">20 KB</td><td class="mid">CMB patch count</td></tr>
<tr><th>Time to send 20 KB</th><td class="mid">\(8.55\times10^{-96}\) s</td><td class="mid">\(t_{\rm rec},\ \ell_P\)</td></tr>
</tbody>
</table>
</div>

<div class="keybox">
<p class="lbl">The thing this episode most wants to say</p>
<p style="margin:6px 0 0">Headline numbers: <strong>24</strong>. Independent inputs: <strong>12</strong> (\(t_0,\ \ell_P,\ S,\ p,\ T_0,\ N_{\rm data},\ \Delta\chi^2,\ l_{\max},\ \Omega_\Lambda{+}\Omega_{\rm dm}\), CMB patch count, \(t_{\rm rec}\), internet traffic).<br>
<strong>Part III's own compression ratio is 2.0×</strong>. Turned on itself, Episode 25's ruler gives <em>not even an order of magnitude</em>.</p>
</div>

<div class="fig">
<p class="cap">Figure: the headline numbers and their independent inputs. <strong>Points of the same colour come from the same input.</strong> The slider "folds away" numbers linked by identities, showing how far 24 shrinks.</p>
<canvas id="cv" width="720" height="400"></canvas>
<div class="controls">
  <label>How far to fold the identities<input id="sl" type="range" min="0" max="4" value="0" step="1"></label>
  <span class="val" id="vl">no folding</span>
</div>
<div class="readout" id="ro"></div>
<div class="legend">
  <span><i class="swatch" style="background:#2a4a5a"></i>from \(t_0,\ell_P\) alone</span>
  <span><i class="swatch" style="background:#b0552a"></i>uses one more observation</span>
  <span><i class="swatch" style="background:#8fa8b4"></i>folded away</span>
</div>
</div>

<h2><span class="n">04</span>Turning Episode 19's procedure on the series</h2>

<div class="tblwrap">
<table class="ce">
<thead><tr><th>Coincidence</th><th class="mid">What it is</th><th class="mid">Surprise</th></tr></thead>
<tbody>
<tr><th>occupancy = black hole share</th><td class="mid">identity (from \(N=A/4\ell_P^2\ln2\))</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>\(C\cdot t=N\)</th><td class="mid">identity (from \(E=c^4R/2G\) and holography)</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>\(dN/dt=2C\)</th><td class="mid">identity (from \(N\propto t^2\))</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>140 four times</th><td class="mid">all \(\ln(t_0/t_P)\)</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>\(\Omega/N=p\ln2/2\pi^2\)</th><td class="mid">fixed by the equation of state alone (derived)</td><td class="mid"><strong>0.0 bit</strong></td></tr>
<tr><th>\(N_T/N_t\approx1/2\)</th><td class="mid">radiation dominates the logarithmic range</td><td class="mid">1.0 bit</td></tr>
<tr class="hi"><th>one bit ↔ 1.96 fm</th><td class="mid">coincidence (judged in Episode 18)</td><td class="mid"><strong>7.4 bit</strong></td></tr>
</tbody>
</table>
</div>

<p>Total 8.4 bits — of which 7.4 is the single case already judged a coincidence in Episode 18. <strong>Almost every agreement in Part III was 0 bits of surprise: an identity.</strong></p>

<h2><span class="n">05</span>The reveal — so what did Part III do?</h2>

<div class="keybox">
<p class="lbl">Conclusion of §05</p>
<p style="margin:6px 0 0"><strong>It did not discover. It restated the same numbers in eight languages.</strong></p>
</div>

<p>This is not self-criticism but the series' subject. In Episode 25's terms: <em>what we were doing was shortening \(L(\text{law})\), which is language dependent and therefore unusable for judging</em>. So why do it?</p>

<div class="seven">
<div class="row hi"><div class="mk">◎</div><div class="txt"><strong>Without restating, you cannot see which two are linked by an identity</strong><span>noticing that "occupancy" and "black hole share" are the same number requires writing it both ways</span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>Five identities were found</strong><span>a map of structure, not new physics</span></div></div>
<div class="row"><div class="mk">◎</div><div class="txt"><strong>The one that remains is the genuine puzzle</strong><span>1.96 fm, 7.4 bits. Drawing the map showed that <em>there is exactly one place we cannot explain</em></span></div></div>
</div>

<p>Before the map there seemed to be 24 numbers. After it, there are <strong>12 inputs and one unexplained agreement</strong>. <em>That is the honest yield of reading physics through information theory.</em></p>

<div class="aside">
<span class="tag">Where did c·t=const matter?</span>
In all of Part III, \(c\cdot t=\)const mattered in exactly one place — the \(p=1\) in \(\Omega/N=p\ln2/2\pi^2\), i.e. 0.0351. The other 23 numbers <strong>come out the same without assuming the expansion law</strong> (they use the convention \(R_H=ct_0\), but that is a notation fixed in Episode 2). <em>So Part III was not a test of the model but a test of the notation.</em> Which is as it should be — this series' subject is compression, not judgement, and the judgement was settled in Episode 3.
</div>

<div class="caveat">
<span class="tag">The honest line — what this episode assumes</span>
<p style="margin:0 0 10px"><strong>① "12 independent inputs" is not a unique count.</strong> Count \(\ell_P\) as the three constants \(\hbar,G,c\) and it is 14; bundle \(N_{\rm data}\) and \(\Delta\chi^2\) as "one Planck dataset" and it is 11. <em>The 2.0× compression ratio itself depends on the counting, for exactly the reason Episode 25 demolished</em> — read it only as an order of magnitude.</p>
<p style="margin:0 0 10px"><strong>② "Occupancy = black hole share" is an identity only so long as black holes dominate \(S\).</strong> The CMB photon contribution is below \(10^{-15}\) of it, but that is an observational fact, not an identity. <em>What is an identity is only the part \((S/\ln2)/N=4\ell_P^2S/A\).</em></p>
<p style="margin:0 0 10px"><strong>③ Episode 21's \(0.127\) was obtained by working backwards.</strong> The text said so, and to repeat: it was not an independent confirmation but the same \(1.5\times10^{-18}\) restated in logarithmic steps.</p>
<p style="margin:0 0 10px"><strong>④ "0.0 bits of surprise" is Episode 19's classification and depends on a subjective prior range.</strong> Assigning 0 to identities is close to definitional; the 7.4 moves by a few bits with the choice of prior.</p>
<p style="margin:0"><strong>⑤ Episode 3's judgement is not moved.</strong> §05 says that Part III did no judging, not that the judgement is withdrawn.</p>
</div>

<div class="prob">
<p class="lbl">Exercises (solvable with this episode's formulas alone)</p>
<ol>
<li>Show that occupancy and black hole share are the same number.
<details><summary>Show the answer</summary><div class="ans">With \(N=A/(4\ell_P^2\ln2)\), \((S/\ln2)/N=(S/\ln2)\cdot4\ell_P^2\ln2/A=4\ell_P^2S/A\). For black holes \(S=A_{BH}/(4\ell_P^2)\), so this is \(\sum A_{BH}/A_H\). <strong>One line from the definition of holography.</strong></div></details></li>

<li>Why is \(N_T/N_t=0.52\) close to \(1/2\)?
<details><summary>Show the answer</summary><div class="ans">Most of the logarithmic range (Planck era to matter–radiation equality) is radiation dominated, where \(T\propto t^{-1/2}\), i.e. \(d\ln T/d\ln t=-1/2\) over most of the 140 steps. <strong>An agreement with an explanation</strong>, so the surprise is about 1 bit.</div></details></li>

<li>Compute Part III's compression ratio counting \(\ell_P\) as three constants.
<details><summary>Show the answer</summary><div class="ans">14 inputs, so \(24/14=1.7\)×. <strong>It changes with the counting</strong> — the same phenomenon Episode 25 found for \(L(\text{law})\).</div></details></li>

<li>Which number in Part III genuinely depended on \(c\cdot t=\)const?
<details><summary>Show the answer</summary><div class="ans">Just one: the \(p=1\) in \(\Omega/N=p\ln2/2\pi^2\), i.e. <strong>0.0351</strong>. The rest use only the notational convention \(R_H=ct_0\) and do not depend on the expansion law itself.</div></details></li>

<li>(Harder) Was there value in "restating the same numbers in eight languages"?
<details><summary>Show the answer</summary><div class="ans">Yes — because without restating, <strong>you cannot see which two are linked by an identity</strong>. What looked like 24 independent findings became, after the map, 12 inputs and one unexplained agreement. <em>Knowing that "there is exactly one place we cannot explain" is the yield</em> — though it is a map of structure, not new physics.</div></details></li>
</ol>
</div>

<div class="record">
<h2 style="margin-top:0">Summary — the same numbers, in eight languages</h2>
<p>We chased the numbers that kept reappearing in Part III. \(1.5\times10^{-18}\) appeared three times, but occupancy and black hole share are an <strong>identity</strong> derivable in one line from \(N=A/(4\ell_P^2\ln2)\), and Episode 21's arrow of time was worked backwards from it — <em>the \(1.5\times10^{-18}\) that appeared three times is one number</em>. \(140\) appeared four times, all of them \(\ln(t_0/t_P)\); only the temperature's \(N_T=73.03\) is independent, and the ratio 0.52 reflects radiation dominating the logarithmic range.</p>
<p>Against 24 headline numbers there are 12 independent inputs. <strong>Part III's own compression ratio is 2.0×</strong> — turned on itself, Episode 25's ruler gives not even an order of magnitude. Sorted by Episode 19's procedure, five of seven agreements are 0 bits (identities), one is 1 bit (explained), and the remaining one is 7.4 bits — Episode 18's <strong>1.96 fm</strong>.</p>
<p>So what Part III did was not discovery but <em>restating the same numbers in eight languages</em>. There is value in that all the same: without restating, you cannot see which two are linked by an identity. Five identities were found, and <strong>exactly one place remains unexplained</strong>. What looked like 24 independent numbers became, after the map, 12 inputs and one puzzle.</p>
<p>And of those 24, \(c\cdot t=\)const genuinely mattered in <strong>one</strong> (\(\Omega/N=0.0351\)). Part III was not a test of the model but <em>a test of the notation</em> — which is as it should be, since this series' subject is compression rather than judgement.</p>
</div>

<div class="next">
<span class="lbl">Next — Part IV, Episode 27</span>
Part III ends here. In Part IV we <strong>apply Episode 3's surgery — naming the comparison hidden inside a name — to other theories</strong>. First, <em>inflation</em>. <strong>Inside the phrase "it solves the horizon problem" sit two different things</strong> — <em>establishing causal contact</em>, and <em>producing a fluctuation spectrum</em>. Using Episode 17's 20 KB we find the former demands surprisingly little. <strong>And we recount, in bits, where the number \(N=60\) e-folds comes from.</strong>
</div>'''

SCRIPT = r'''<script>
(function(){
  var cv=document.getElementById('cv'), g=cv.getContext('2d');
  var sl=document.getElementById('sl'), vl=document.getElementById('vl'), ro=document.getElementById('ro');
  var items=[
    {n:'N',                g:0, f:-1},
    {n:'dN/dt',            g:0, f:-1},
    {n:'C',                g:0, f:2},
    {n:'C·t/N=1',          g:0, f:2},
    {n:'(dN/dt)/C=2',      g:0, f:2},
    {n:'140.24',           g:0, f:-1},
    {n:'1.96 fm',          g:0, f:-1},
    {n:'occupancy',        g:1, f:-1},
    {n:'BH share',         g:1, f:1},
    {n:'arrow of time',    g:1, f:1},
    {n:'redundancy',       g:1, f:1},
    {n:'Ω/N=0.0351',       g:1, f:-1},
    {n:'N_T=73.03',        g:1, f:-1},
    {n:'N_T/N_t',          g:1, f:3},
    {n:'5.37 bit',         g:1, f:-1},
    {n:'153.6 bit',        g:1, f:-1},
    {n:'−148.3 bit',       g:1, f:4},
    {n:'6.26e6 modes',     g:1, f:-1},
    {n:'ratio 1.0e6',      g:1, f:4},
    {n:'95.0 %',           g:1, f:-1},
    {n:'20 KB',            g:1, f:-1},
    {n:'8.55e-96 s',       g:1, f:-1},
    {n:'1.91e-90',         g:1, f:-1},
    {n:'7.4 bit',          g:1, f:-1}
  ];
  var LAB=['no folding','fold the occupancy identity','+ C·t=N, dN/dt=2C','+ the ratios','+ the divisions'];
  var X0=48, Y0=52, CW=168, CH=30;
  function draw(){
    var lv=parseInt(sl.value,10);
    g.clearRect(0,0,cv.width,cv.height);
    g.fillStyle='#fff'; g.fillRect(0,0,cv.width,cv.height);
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    var alive=0;
    for(var i=0;i<items.length;i++){
      var it=items[i];
      var gone = it.f>=1 && it.f<=lv;
      if(!gone) alive++;
      var col = Math.floor(i/8), row = i%8;
      var x=X0+col*CW, y=Y0+row*(CH+8);
      g.fillStyle = gone ? '#eef2f4' : (it.g===0 ? '#2a4a5a' : '#b0552a');
      g.fillRect(x,y,150,CH);
      g.fillStyle = gone ? '#8fa8b4' : '#fff';
      g.textAlign='left';
      g.fillText(it.n, x+10, y+20);
      if(gone){
        g.strokeStyle='#8fa8b4'; g.lineWidth=1.4;
        g.beginPath(); g.moveTo(x+6,y+CH/2); g.lineTo(x+144,y+CH/2); g.stroke();
      }
    }
    g.fillStyle='#2a4a5a'; g.textAlign='left';
    g.font='bold 15px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillText('Part III headline numbers: '+items.length+'  →  '+alive+' remain', X0, 30);
    g.font='12px system-ui,-apple-system,"Segoe UI",sans-serif';
    g.fillStyle='#6b8794';
    g.fillText('12 independent inputs. Even folded this far there are more — the rest come from separate observations', X0, 386);
    vl.textContent=LAB[lv];
    ro.textContent=LAB[lv]+'　→　'+alive+' of '+items.length+' remain'+
      ' (all '+(items.length-alive)+' folded away were identities at 0 bits of surprise)';
  }
  sl.addEventListener('input',draw);
  draw();
})();
</script>'''

build(out='../wakaru-ct-26-partIII.html', acc='#2a4a5a', ops='#b0552a',
      title='The same numbers, in eight languages ── c·t = const, That Clicks, Episode 26 (Part III wrap-up)',
      ep='EPISODE 26 ／ Part III wrap-up',
      eyebrow='How many numbers did eight rulers actually produce?',
      h1='The same numbers,<br>in eight languages',
      sub='\\(1.5\\times10^{-18}\\) three times, \\(140\\) four times.<br><em>We turn Episode 19\'s procedure on the series itself.</em>',
      byline_l='What you need: all of Part III, and subtraction',
      byline_r='24 numbers → 12 inputs',
      body=BODY + '\n\n<p class="foot">This document is Episode 26 of "c·t = const, That Clicks" (Part III wrap-up), written for physics-minded high-school and university readers. The holographic bound \\(N=A/(4\\ell_P^2\\ln2)\\), the Bekenstein–Hawking entropy \\(S_{BH}=A/(4\\ell_P^2)\\), and \\(T\\propto t^{-1/2}\\) in the radiation era are all standard. <strong>The claims made here — that occupancy equals black hole share as an identity, that Part III\'s 24 headline numbers reduce to 12 independent inputs, and that the surprises total 8.4 bits — are this document\'s own tally</strong> (kenshou/calc30.py). "12 independent inputs" is not a unique count: treat \\(\\ell_P\\) as \\(\\hbar,G,c\\) and it is 14; bundle the Planck data and it is 11 — <em>the 2.0× compression ratio itself depends on the counting, for the reason Episode 25 demolished</em>. "Occupancy = black hole share" is an identity only while black holes dominate \\(S\\), and that dominance is an observational fact rather than an identity. "0.0 bits of surprise" is Episode 19\'s classification and depends on a subjective prior range. Linear expansion (\\(c\\cdot t=\\)const) is a minority model under examination whose judgement was handled in Episode 3 — this document does not withdraw that judgement but confirms that <em>Part III addressed notation rather than judgement</em>. \\(R_H=ct_0\\) is that notational convention (in \\(\\Lambda\\)CDM, \\(R_H=c/H_0\\) differs from the particle horizon). The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── To make a PDF, use your browser\'s Print dialogue (sliders freeze and answers are hidden in the print version).</p>',
      script=SCRIPT,
      hint='Print / PDF: ⌘+P (Ctrl+P on Windows). On screen, folding the identities shows how far 24 shrinks. "Show the answer" opens each solution.')
