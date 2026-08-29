# -*- coding: utf-8 -*-
"""日本語版 index.html の CSS を再利用して、英語版の目次を組み立てる。"""
import io, re

ja = io.open('../../wakaru-ct/index.html', encoding='utf-8').read()
css = re.search(r'<style>(.*?)</style>', ja, re.S).group(1)

import os
def card(n, href, title, desc, key, tag=''):
    """英訳済みならリンク、未訳なら非リンクで表示する。"""
    if os.path.exists('../'+href):
        return f'''<a class="ep" href="{href}">
  <span class="no">EPISODE {n} <span class="badge b-new">LIVE</span> <span style="color:#5f6a7a;font-weight:600">interactive figure</span>{tag}</span>
  <h3>{title}</h3>
  <p>{desc}</p>
  <span class="key">{key}</span>
</a>

'''
    ja = '../../wakaru-ct/'+href
    return f'''<div class="ep">
  <span class="no">EPISODE {n} <span class="badge b-soon">TRANSLATING</span>{tag}</span>
  <h3>{title}</h3>
  <p>{desc}</p>
  <span class="key">{key}　·　<a href="{ja}" style="color:inherit">read the Japanese original</a></span>
</div>

'''

def mini(items):
    out=['<ol class="mini">']
    for n,t in items:
        out.append(f'<li><span class="num">Ep.{n}</span><span class="ttl">{t}</span></li>')
    out.append('</ol>')
    return '\n'.join(out)

def part(no, title, desc):
    return f'''<div class="part">
  <div class="pn">PART {no}</div>
  <div class="pt">{title}</div>
  <div class="pd">{desc}</div>
</div>

'''

BODY = part('I', 'Building the notation',
  'Count, then <strong>divide</strong>. Doing only that, the expansion law keeps falling out — and by the end \\(c\\cdot t=\\text{const}\\) is pinned down as a <em>notation</em>, not a model.')

BODY += card(1,'wakaru-ct-01-opsbit.html','The universe has computed 0.035 operations per bit',
  'Count the memory, count the operations, divide. Time cancels cleanly and only the equation of state is left standing — the number of operations per bit does not depend on the age of the universe, nor on its size. Radiation gives 1/57, matter 1/42.7, \\(c\\cdot t=\\text{const}\\) gives 1/28.5. Reaching "1" would need \\(w=-0.977\\), and the dark energy we observe already sits on the far side of that.',
  '\\(\\Omega/N=\\dfrac{\\ln 2}{3\\pi^{2}(1+w)}\\) — the <strong>8th characterisation</strong> of \\(a\\propto t\\)')

BODY += card(2,'wakaru-ct-02-clocks.html','Two clocks that do not mesh',
  'The universe carries two logarithmic rulers: time, \\(\\ln(t_0/t_P)=140.24\\) steps, and the renormalisation group, \\(\\ln(T_P/T_0)=73.03\\) steps. <strong>Divide them and the expansion law appears</strong> (\\(\\bar p=0.513\\), just above radiation). \\(c\\cdot t=\\text{const}\\) demands \\(140.24=73.03\\) — a verdict reached with no dynamics at all, using only today\'s temperature and today\'s age. Neutrons freeze out at 0.8 MeV after 4.05 years; a free neutron lives 880 seconds.',
  '\\(d\\ln T/d\\ln t=-p\\) — the <strong>9th characterisation</strong> (the two clocks tick 1:1)')

BODY += card(3,'wakaru-ct-03-whichclock.html','\\(c\\cdot t=\\)const can be realised in any universe',
  '"A rewriting moves no dimensionless quantity. So how can it fail?" — we push that objection all the way. Push it hard enough and \\(c\\cdot t\\) can be held <strong>exactly constant</strong> in a radiation universe or a matter universe alike (take the time coordinate \\(T=e^{\\eta/\\eta_0}\\); verified numerically to 1.000000). All that differs is what \\(T\\) <em>is</em> — for radiation, \\(T\\propto e^{\\sqrt t}\\), nobody\'s clock. Exactly one claim survives: <strong>that this clock is the age of the universe</strong>.',
  '\\(T=e^{\\eta/\\eta_0}\\) — the <strong>10th characterisation</strong> (three clocks coincide)',
  ' <span class="badge b-q">from a reader\'s question</span>')

BODY += card(4,'wakaru-ct-04-onemass.html','Everything collapses into a single mass',
  'Why use a rewriting that says nothing? <strong>Because the equations get shorter.</strong> Erase everything a conformal transformation can erase and the expansion of space, the curvature, the temperature and the light all vanish in turn — <em>leaving exactly one thing that varies in time</em>. Cosmic history collapses to "a growing mass overtaking a fixed \\(k_BT_0\\)" (recombination at \\(1+z=1100.9\\), neutron freeze-out at 0.800 MeV — exactly the standard numbers). Distances and ages become closed forms, with no integrals.',
  '\\(H_0d_L/c=(1+z)\\ln(1+z)\\) — a prediction with <strong>zero</strong> dimensionless parameters')

BODY += card(5,'wakaru-ct-05-price.html','What can shortness buy?',
  'Zero description length (Ep.4) against a 0.21 mag mismatch at \\(z\\simeq1.1\\). We convert both into one currency: <strong>bits</strong>. A parameter costs 1.443 bits under AIC (independent of sample size) and \\(\\tfrac12\\log_2N\\) — 5.37 bits for 1701 supernovae — under BIC. The fit loss is \\(\\Delta\\chi^2/(2\\ln2)=\\) <strong>154 bits</strong>, so the ledger closes 149 bits in the red. And yet <em>with fewer than 26 supernovae, \\(c\\cdot t=\\text{const}\\) is the better model</em>: shortness pays \\(\\log N\\), misfit costs \\(N\\). Occam\'s razor has an expiry date.',
  'One parameter \\(=\\tfrac12\\log_2 N\\) bits')

BODY += card(6,'wakaru-ct-06-empty.html','Only \\(10^{-18}\\) of the memory is in use',
  'The occupancy turns out to be <strong>a ratio of areas</strong> — glue together the horizons of every black hole in the universe and you get <em>a sphere 17 light-years in radius</em>. And <strong>99.999999999999986%</strong> of today\'s entropy sits on the gravitational (Weyl) side. The history comes in three steps: at the Planck era the occupancy was \\(\\approx1\\) (full), today the thermal side alone is \\(7\\times10^{-34}\\) (it emptied out), and with black holes \\(1.5\\times10^{-18}\\) (gravity refilled 15.4 orders). <strong>A conformal transformation can only move the side that is not in use</strong> — how broken the tool is, is the arrow of time.',
  'occupancy \\(=\\sum A_{\\rm BH}/A_H\\)')

BODY += part('II', 'Feeding it to every equation in reach',
  'The notation is built, so we carry it out of cosmology. Quantum mechanics, gravity, heat, light, fluids, critical phenomena, biology — one at a time, <strong>what happens when you put it in</strong>. The answer, every time: only one thing moves.')

BODY += card(7,'wakaru-ct-07-gravity.html','Feeding it to gravity',
  'Here \\(\\tilde G=G/a^2\\) is <strong>forced</strong>, giving \\(\\dot G/G=-2H_0=-1.45\\times10^{-10}\\)/yr — <strong>1450 times</strong> the lunar-laser-ranging bound. And still nobody can notice (because \\(\\alpha_G\\) does not move). Then the punchline: the two large numbers Dirac used in 1937 to predict \\(G\\propto1/t\\), \\(N_1=2.27\\times10^{39}\\) and \\(N_2=4.63\\times10^{40}\\), turn out to be <em>both invariant when you actually vary \\(G\\)</em> — <strong>you cannot move \\(G\\) alone</strong>, so Dirac\'s prescription spins in place.',
  'Only black-hole entropy and the strain \\(h\\) stay put — the tool cannot reach the memory that is in use')

BODY += card(8,'wakaru-ct-08-quantum.html','Feeding it to quantum mechanics',
  'Both sides of the Schrödinger equation carry weight \\(-5/2\\), so <strong>not a single character changes</strong> — only \\(m(t)=m_0t/t_0\\). Then free-particle velocity decays as \\(1/t\\) and a wave packet spreads as <strong>\\(\\Delta x\\propto\\ln t\\)</strong>. Integrate and the comoving reach of anything with mass saturates at \\(v_1t_1\\) (1.9 parsecs for a hydrogen atom at recombination); only light runs on forever as \\(c\\,t_1\\ln(t/t_1)\\). Tunnelling probability is dimensionless and therefore exactly invariant — the Sun burns at the same rate.',
  '<strong>Matter stops walking; light keeps walking</strong>')

BODY += card(9,'wakaru-ct-09-atom.html','Feeding it to the atom',
  'Atoms shrink as \\(1/t\\) here — and in 1918 <strong>Einstein killed Weyl\'s unified theory with exactly this argument</strong>. Two reasons the same blade misses: (i) \\(\\Omega\\) is single-valued, so there is no path dependence to begin with; (ii) the adiabatic parameter is \\(\\hbar H/\\Delta E=1.1\\times10^{-34}\\). Even the softest transition (21 cm) would only break adiabaticity before \\(10^{-10}\\) s, so <em>throughout the entire era in which atoms exist, the evolution is perfectly adiabatic</em>. The induced line blurring is \\(9\\times10^{-20}\\) of the natural width — 19 orders down.',
  'The Bohr radius shrinks at \\(7.2\\times10^{-11}\\)/yr, yet every possible yardstick has weight \\(+1\\)')

BODY += card(10,'wakaru-ct-10-erase.html','Feeding it to heat and information',
  'Temperature does not move here (\\(\\tilde T=aT=\\)const), so <strong>the cost of erasing one bit is fixed for all of cosmic history</strong> (\\(1.63\\times10^{-4}\\) eV). But energy is dimensionful — the price is undefined until you name both a comparison and <em>which bath you dump into</em>. Counting how many bits the universe\'s whole energy could erase, the answer swings 60 orders with temperature, and at the CMB temperature <strong>you can only erase \\(10^{-30}\\) of what you can write</strong>. And "exactly at the Landauer limit" turns out to be <em>reading off an identity</em>, \\(E=T_HS\\).',
  'writable \\(10^{122}\\), erasable \\(10^{92}\\) — the universe is very nearly write-once')

BODY += card(11,'wakaru-ct-11-light.html','Feeding it to light',
  'Number density, energy density, temperature, photon energy, wavelength — <strong>every one of them constant</strong>. The exponent of \\(a\\) in the standard picture and the weight of the quantity are the same number, so they cancel exactly. <em>The photon gas in this picture is completely at rest.</em> Observation still does not budge: the CMB is fixed by just two dimensionless numbers, \\(s/n=3.60\\,k_B\\) and \\(\\eta=6.1\\times10^{-10}\\). So redshift flips over entirely — not "the light stretched" but "<strong>the receiver grew</strong>".',
  '\\(\\Omega^{D-4}\\) — living in four dimensions is why this picture works at all')

BODY += card(12,'wakaru-ct-12-vacuum.html','Feeding it to the vacuum',
  'Energy density has weight \\(-4\\), so \\(\\tilde\\rho=a^4\\rho\\). Applied to the three components, <strong>the ordering inverts completely</strong>: radiation becomes <em>constant</em>, matter goes as \\(\\propto t\\), and the cosmological constant grows fastest of all at \\(\\propto t^4\\). <strong>The very name "cosmological constant" depended on which picture you chose.</strong> And yet \\(\\rho_\\Lambda/M_{\\rm Pl}^4=1.13\\times10^{-123}\\) and \\(\\rho_\\Lambda/\\rho_m\\propto a^3\\) are both invariant — neither the cosmological constant problem nor the "why now?" problem moves by a millimetre.',
  '<em>Good puzzles are written in dimensionless form</em>')

BODY += card(13,'wakaru-ct-13-fluid.html','Feeding it to fluids and turbulence',
  'Reynolds, Mach, Prandtl, Froude, Weber, Strouhal — <strong>every one of them has weight 0</strong>. So similarity laws and wind-tunnel tests carry over untouched. The interesting part is the breakdown: the four pieces of \\(\\mathrm{Re}=\\rho vL/\\eta\\) move as \\(a^4,a^0,a^{-1},a^3\\) — <em>wildly and separately</em> — yet the exponents sum to \\(4-1-3=0\\). Kolmogorov\'s \\(-5/3\\), the critical exponents and the fractal dimensions are all invariant too: <strong>a conformal transformation touches "size" only, and cannot reach "shape"</strong>.',
  'The Navier–Stokes equations survive this picture completely intact')

BODY += card(14,'wakaru-ct-14-critical.html','Feeding it to phase transitions',
  'The weight table this series has used for thirteen episodes was a <strong>classical approximation</strong> — in field theory \\(\\Delta=\\Delta_{\\rm cl}+\\gamma\\). For the 3D Ising spin operator the free-field value 0.5 becomes <strong>0.5181489(10)</strong>, a discrepancy of \\(\\gamma_\\sigma=0.0181489\\) (3.6%). In two dimensions it is 12.5%, and <em>in four dimensions it vanishes exactly</em>. Through \\(\\eta=2\\gamma_\\sigma\\), <strong>that discrepancy is measurable in water and in magnets</strong>. What broke was not "dimensionless is invariant" but the assumption that <em>weights follow from dimensional analysis</em>.',
  'The ledger entries acquire error bars — weights were something to be measured')

BODY += card(15,'wakaru-ct-15-life.html','Feeding it to chemistry and biology',
  'Arrhenius factors, equilibrium constants and pH all have dimensionless exponents, so they come through <strong>entirely unscathed</strong>. Take Kleiber\'s law apart and the exponent 3/4 is invariant while <em>only the coefficient moves, as \\(\\times a^{5/4}\\)</em> (dimensionful, hence bookkeeping). Heart rate \\(\\propto M^{-1/4}\\) times lifespan \\(\\propto M^{1/4}\\) gives <strong>about 1.5 billion beats per lifetime</strong>, independent of body mass and therefore invariant. Everything life can measure is dimensionless — so <strong>living things cannot tell which picture they are in</strong>.',
  'Ep.9\'s "the atom has nothing to compare against", pushed up to the scale of biology')

BODY += card(16,'wakaru-ct-16-partII.html','Only one thing ever moves (Part II summary)',
  'Nine fields, one notation, and a count of what moves. The answer had the same shape every time: <strong>everything that moved was dimensionful, everything that stayed was dimensionless</strong> — without a single exception. The map of weights is complete (from \\(+3\\) down to \\(-4\\)), and the range of the tool becomes clear: <em>powerful where size is the protagonist, entirely powerless where shape is</em>. With the caveat from Ep.14 that the weight table itself carries error bars.',
  'Not "safe because dimensionless" but <strong>"safe because observable"</strong>')

BODY += part('III', 'Measuring it as information',
  'Writing the universe as a computer with finite resources, and counting it all the way down: memory, communication, error correction, the cost of erasure. This part walks through the door the previous series left open when it concluded "we were constraining the wrong thing".')

BODY += card(17,'wakaru-ct-17-consensus.html','9600 nodes that never communicated agree to 17 bits',
  'The horizon problem, restated in the language of distributed systems. \\(\\Delta T/T\\sim10^{-5}\\) is <strong>16.6 bits of agreement</strong>, the causally disconnected regions number <strong>9600</strong>, and the product is <strong>about 20 kilobytes</strong> — a phone would send it instantly. <em>The problem was never the quantity; it was that there was no channel.</em> With \\(a\\propto t\\) the particle horizon diverges, so there is one patch and zero bits to agree on — until you put radiation back in, at which point it breaks at \\(z>103\\) and \\(1.2\\times10^4\\) nodes return. Inflation solves it not by consensus but by <strong>replication</strong>.',
  'Coincidence would need \\(10^{-48000}\\) — the option is gone')

BODY += card(18,'wakaru-ct-18-address.html','There are not enough address lines',
  'Holography read as addressing. The universe has \(5.27\times10^{182}\) spatial cells and can write \(2.96\times10^{122}\) bits, so <strong>only \(10^{-61}\) of the cells can be addressed</strong> — and since the ratio goes as \(1/R_H\), the gap widens as the universe grows. Inverted, one bit is responsible for a cube of side <strong>1.96 fm — the size of a proton</strong>, the cube-root intermediate scale \((R_H\ell_P^2)^{1/3}\), an unexplained coincidence. Holography is <em>not compression</em>: volume cells were never given addresses at all.',
  'Addresses grow only with area — and the address table will not fit in memory')

BODY += card(19,'wakaru-ct-19-surprise.html','Is an identity really not physics?',
  'This series has sorted coincidences as identity, coincidence or physics again and again — here the criterion is stated. Surprise \(=-\log_2(\text{width}/\text{prior range})\), and the strata separate cleanly: <strong>identities at 0 bits, coincidences at a few, real problems at \(10^5\)</strong>. The factor-22 agreement of \(\rho_\Lambda^{1/4}\) and \(m_\nu\) is five coin flips; only <strong>Koide’s relation, at 15.7 bits</strong>, is surprising by orders. And an identity is not a prediction but <em>a consistency check</em>.',
  'Identities are 0 bits — but 0 bits is not the same as meaningless')

BODY += card(20,'wakaru-ct-20-lightsheet.html','Actually constraining the light sheets',
  'The previous series closed with the line “what should be constrained is the information on the light sheets — nobody has done that calculation.” Done here. The occupancy \(f=s/(3H/4\ell_P^2)\) <strong>saturates exactly at the Planck era and opens to a margin of 33 orders</strong> — and that saturation is an <em>identity</em>, 0 bits of surprise. As a constraint it excludes almost nothing. Fix the bit count and you get de Sitter, the address space and you get \(a\propto t\), the occupancy and you get stiff \(a\propto t^{1/3}\); the observed universe is none of them.',
  'Right in form, insufficient in effect — it bites only at the Planck era')

BODY += card(21,'wakaru-ct-21-arrows.html','There are four scales for the arrow of time',
  'Total entropy (+104 orders), memory occupancy (−18), holographic margin (+33), degrees of freedom \(a\) (−1.2). Two up, two down — and <strong>all four are dimensionless</strong>, so the arrow sits entirely in the physics column. Put in the same units, the denominator grows at 0.872 orders per step and the numerator at 0.745: <em>a difference of only 0.127</em>, which over 140 steps gives exactly Episode 6’s occupancy. <strong>The arrow lives in the numerator; the denominator is the stage.</strong>',
  'Rewriting the books cannot touch the direction of time')

BODY += card(22,'wakaru-ct-22-instruction.html','The instruction set of the universe-as-computer',
  'The ML rate is proportional to energy, so the operational budget <em>is</em> the energy budget. And ML measures energy above the ground state — the vacuum <strong>has nowhere to transition to</strong>, removing 68.5% at a stroke; of what remains, 84.1% is dark matter, which interacts only gravitationally. <strong>95.0% of the budget goes to components in which nothing happens.</strong> Starlight, the most conspicuous activity there is, accounts for one millionth of the total, and Episode 1’s 0.035 operations per bit falls to one per 580 bits.',
  'The gap Episode 1 flagged as “a spec sheet, not a benchmark”, measured')

BODY += card(23,'wakaru-ct-23-code.html','The horizon as error correction',
  'Read the horizon as a code: \(n=2.96\times10^{122}\) physical bits, \(k=4.47\times10^{104}\) logical, giving <strong>a redundancy of \(6.6\times10^{17}\)</strong> — fourteen orders beyond the quantum surface code. That is Episode 6’s occupancy read inside out, and the heart of it: <em>“empty” and “redundant” are the same number until you name the comparison</em>. Episode 3’s surgery, this time applied to the series’ own figure. Closing with an act of restraint — the logical bit’s length matches nothing, so nothing is said.',
  'AdS/CFT is the precedent, but a cosmological horizon is not established')

BODY += card(24,'wakaru-ct-24-channel.html','How many bits per second cross the horizon?',
  'Dividing the Bekenstein bound by a crossing time gives \(C=2\pi E/(\hbar\ln2)=6.79\times10^{104}\) bit/s. Its factor-of-two relation to Episode 1’s \(dN/dt\) is an identity, and the clean form is <strong>\(C\cdot t=N\)</strong> — <em>the universe has exactly enough bandwidth to move its entire memory once per Hubble time</em>. Which settles Episode 17: the 20 KB could have been sent in \(10^{-96}\) seconds. <strong>Bandwidth was never the bottleneck; the wiring was.</strong>',
  'Three routes now agree: the universe has power to spare')

BODY += card(25,'wakaru-ct-25-mdl.html','Are physical laws a compression algorithm?',
  '\(a\propto t\) is 66 bits, the Einstein equations 512, the Standard Model 33,000; \(\Lambda\)CDM compresses \(10^6\)-fold. But totalled with MDL it breaks: counting \(a\propto t\) as an added constraint or as a replacement flips <strong>the same model on the same data from losing by 214 bits to winning by 200</strong>. Only \(L(\text{law})\) moved — a language-dependent quantity. What is trustworthy is the parameter count and the residual, and those alone give \(-148\) bits. <strong>Compression ratio measures the size of the bet, not the quality.</strong>',
  'MDL’s compression ratio and Popper’s falsifiability are one axis')

BODY += mini([
])

BODY += part('IV', 'Putting other theories on the same table',
  'The operation from Ep.3 — <em>naming the comparison hidden inside a name</em> — applied to other models. In every case an "equivalent rewriting" and an "observable claim" are travelling under one label.')
BODY += card(26,'wakaru-ct-26-partIII.html','The same numbers, in eight languages (Part III wrap-up)',
  '\(1.5\times10^{-18}\) three times, \(140\) four times — chased down, they are all one number. Occupancy equals black hole share by a one-line identity from holography. Part III’s <strong>24 headline numbers reduce to 12 independent inputs</strong>, and the surprises total 8.4 bits, of which 7.4 is the 1.96 fm already judged a coincidence in Episode 18. <em>Part III did not discover; it restated the same numbers in eight languages</em> — and that is how five identities and exactly one unexplained agreement became visible.',
  'A map of structure, not new physics')

BODY += card(27,'wakaru-ct-27-inflation.html','Inflation, on the same operating table',
  'Cut “it solves the horizon problem” in two: (A) establishing causal contact, (B) producing a fluctuation spectrum. (A) is cheap — the particle horizon \(ct/(1-p)\) diverges at \(p=1\), so <strong>\(a\propto t\) removes the problem with zero e-folds and zero parameters</strong>. What survives is (B): the horizon fixes \(N_{\min}=62.1\) and the same \(N\) predicts \(n_s\), against an observed \(N=57.0\pm6.8\) — <em>agreement at 0.75σ</em>. The most famous motivation turns out to be the weakest argument.',
  'Same surgery, different survivor')

BODY += card(28,'wakaru-ct-28-vsl.html','VSL — where the surgery went wrong',
  'The \(c\) called “the speed of light” appears in four separate roles (Ellis &amp; Uzan), and VSL fixes \(e\) and \(\hbar\), so its observable content is <strong>entirely “\(\alpha\) varies”</strong> — against \(\alpha\) pinned to 32.5 bits in the laboratory and 26.4 at Oklo. Solving the horizon problem demands \(\alpha(z)/\alpha_0\ge1+z\), <strong>ten orders over the nucleosynthesis bound</strong>. A phase transition escapes that — and loses every prediction in the observable era at the same stroke.',
  'The failure was not moving c, but continuing to call it c')

BODY += card(29,'wakaru-ct-29-mond.html','MOND — the comparison hidden inside an acceleration',
  '\(a_0\) is dimensionful (weight \(-1\)), so “the acceleration is small” needs a comparison — and \(cH_0\) is sitting right next door, at \(a_0/cH_0=0.18\). The ratio has weight 0, so <strong>the coincidence cannot be moved by a conformal transformation</strong>; measured in bits it is 5.9, the same stratum as \(\rho_\Lambda\) and \(m_\nu\). On Episode 5’s scales, <strong>MOND wins galaxy rotation curves by 1971 bits</strong> — and loses clusters, the Bullet Cluster and the CMB. <em>“Dark matter or MOND?” was never one question.</em>',
  'And the coincidence hides a testable fork: constant \(a_0\), or \(a_0\propto H\)?')

BODY += card(30,'wakaru-ct-30-measure.html','Measuring varying constants for real',
  'Atomic clocks, the Oklo natural reactor, quasar absorption lines — three different physics, one skeleton: (change in the observable) = K × (Δα/α). <strong>Oklo’s precision is a coarse 2% and it matches an atomic clock, because its amplification is \(10^7\)</strong> — the 97.3 meV resonance is a difference of MeV-scale quantities. Placed on the logarithmic axis, data cover <strong>29% of cosmic history and 26-bit precision covers 0.1%</strong>. And measurement of constants sits entirely in the weight-0 column — which is why it can be the referee.',
  'A cancellation of orders can be a mystery or a tool')

BODY += card(31,'wakaru-ct-31-ccc.html','Penrose’s conformal cyclic cosmology',
  'CCC’s central move is exactly Episode 11’s result — <em>with no mass there is no ruler, and with no ruler the conformal factor has no meaning</em>. Measuring its three conditions with this series’ quantities: 31.4% of today’s energy must lose its rest mass; the gluing falls at logarithmic step 348, with <strong>today only 40% of the way</strong>; occupancy falls from \(1.5\times10^{-18}\) to \(3.2\times10^{-22}\). And Episode 16 plus Episode 6 show <em>why CCC has no choice but to bet on information loss</em>.',
  'The theory in Part IV that best withstands the surgery')

BODY += card(32,'wakaru-ct-32-cosmon.html','Wetterich’s cosmon',
  'Episode 4’s picture put \(a(t)\) in by hand; the cosmon has field equations determine \(\chi(t)\). In the ledger it <strong>pays 2 parameters = 10.7 bits and buys back up to 408</strong> — the tuning of \(\rho_\Lambda/M_{\rm Pl}^4\). And it does not die like VSL because <em>one field sets every mass, so the ratios are fixed</em> — \(\alpha\)’s 26 bits catch nothing. Judgement moves to \(w=-1.03\pm0.03\).',
  'A notation shortens L(law); a theory pays L(parameters) to reduce L(residual)')

BODY += card(33,'wakaru-ct-33-milne.html','Milne versus R_h=ct',
  'Both have \(a\propto t\), but for \(a=t\) the FLRW curvature is \(R=6(1+k)/t^2\) — <strong>exactly zero at \(k=-1\)</strong>, so Milne is Minkowski in other coordinates. From this follows a three-step test, and <em>every FLRW lands in the “needs a conformal transformation” step</em>. And at \(z=1\) the empty Milne universe fits \(\Lambda\)CDM better than \(R_h=ct\) does — which is why “fits the Hubble diagram” is a weak test.',
  'Tell them apart by looking at k')

BODY += card(34,'wakaru-ct-34-conformal-gravity.html','Conformal gravity (Mannheim)',
  'With the Weyl-squared action, \(S\to\Omega^{D-4}S\) — <strong>conformally invariant only at \(D=4\)</strong>, exactly Episode 11’s Maxwell structure. Then the coupling \(\alpha_g\) is dimensionless, the symmetry <em>forbids</em> a cosmological constant term (Episode 32’s 408 bits, for free), and the vacuum solution’s linear term crosses over at 44 kpc. The price is <strong>ghosts</strong> — the conformal factor’s ghost is gauged away and a massive spin-2 ghost arrives instead.',
  'The one theory in Part IV that never made it onto the operating table')

BODY += card(35,'wakaru-ct-35-asymptotic-safety.html','Asymptotic safety and a running G',
  'Pair \(G\) with a scale to form \(g=Gk^2\) and run it: the slope is <strong>exactly 2</strong>, the classical dimension — and “gravity is \(10^{-38}\) times weaker” turns out to mean only that we look at small scales. At the ultraviolet fixed point \(g\) stops, so \(\eta_N=-2\) exactly: <strong>Episode 14’s 3.6% error in the weight table becomes 100% in gravity</strong>. The Higgs prediction of 126 GeV against a measured 125.25 is a 4–6 bit surprise.',
  'The same entrance as conformal gravity — physics is in a dimensionless coupling')

BODY += mini([
])

BODY += part('V', 'Going looking for where it breaks',
  'Hunting deliberately for the places the notation stops working: quantum anomalies, ghosts, rotating spacetimes, gravitational entropy — everything a conformal transformation cannot erase.')
BODY += card(36,'wakaru-ct-36-partIV.html','Onto the operating table (Part IV wrap-up)',
  'Nine theories on one table, all given the same surgery: exactly one — VSL — failed to separate (A) notation from (B) an observable claim. The line was not whether the name points at (A) but whether the theory itself can tell them apart. Every prediction sat in a dimensionless quantity, without exception. And something new: six of the coincidences fall between 4 and 7.5 bits of surprise — most likely a selection effect, the band where a result is enough for a paper but not for a consensus.',
  'Good theories have already performed Episode 3’s surgery')

BODY += card(37,'wakaru-ct-37-anomaly.html','Quantum anomalies — writing into the zero column',
  'Episode 11’s "nothing happens to light" was a classical statement. Quantum theory cannot stay at D=4 (D=4-e with dimensional regularisation, a mu with a cutoff), so Episode 34’s exponent Omega^(D-4) becomes the breaking itself. Alpha is dimensionless only at D=4. The running is 7.1 per cent, which against the laboratory noise floor sits 28.7 bits above the noise — far past the band of coincidences. It does not contradict Episode 30’s "constant to 26 bits" because that is a different question. And the size of the breaking turns out to be a count of the fields.',
  'What broke was not the field but the coupling')

BODY += mini([
 (38,'The conformal factor problem — the ledger is the first thing to break'),
 (39,'Phase shows up only in a rotating spacetime'),
 (40,'How do you count gravitational entropy?'),
 (41,'The Weyl curvature hypothesis, measured as occupancy'),
 (42,'What happens to the notation inside a black hole'),
 (43,'The Planck scale — the edge of the band'),
 (44,'What changes if you make it discrete'),
 (45,'Summary: the list of things that could not be erased'),
])

BODY += part('VI', 'What the notation was',
  'Fifty episodes of ledger and physics, folded into a single sheet.')
BODY += mini([
 (46,'Every characterisation of \\(a\\propto t\\)'),
 (47,'A map of the dimensionless — what is physics and what is bookkeeping'),
 (48,'Shortness, fit, beauty — three currencies'),
 (49,'The doors still open'),
 (50,'Finale: only one thing was ever moving'),
])

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>c·t = const, That Clicks ── Series Contents</title>
<script>
  window.MathJax = { tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['$$','$$']]}, svg:{fontCache:'global'} };
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js" id="MathJax-script"></script>
<style>
''' + css + '''</style>
</head>
<body>
<article class="sheet">

<p class="series">A SEQUEL TO "CONFORMAL TRANSFORMATIONS THAT CLICK"</p>
<h1>c·t = const, That Clicks
<span class="sub">On its own, \\(c\\cdot t=\\text{const}\\) says nothing at all — it can be realised in any universe.<br>
<em>Which is exactly why it can be substituted into every equation there is</em>: it is a notation for writing cosmology as short as it will go.<br>
This series measures that shortness, all the way, in the language of information theory.</span></h1>

<p class="meta"><span>50 episodes planned / 6 parts</span><span>Each episode: count → divide → interactive figure → the reveal → exercises</span><span>Episodes 1–17 live</span><span>Print / PDF ready</span></p>

<p class="lead">The backbone of the previous series was "dimensionful is bookkeeping, dimensionless is physics". But the quantities of information theory — bits, operation counts, parameter counts, entropy — are <strong>dimensionless from the outset</strong>. They carry no units. So a cosmology written in that language can only ever live in the "physics" column. We start again from where bonus episode ② of the previous series asked "is the universe a computer with finite resources?" and answered "the motivation was apt, the implementation missed" — this time not as a verdict, but as <strong>compression</strong>.</p>

<div class="keybox">
<p class="lbl">The method</p>
<p style="margin:6px 0 0">Count, then <strong>divide</strong>. Memory \\(N=\\dfrac{\\pi}{\\ln2}\\left(\\dfrac{R_H}{\\ell_P}\\right)^2\\), clock \\(\\ln\\dfrac{t_0}{t_P}=140\\), operations \\(\\Omega=\\displaystyle\\int\\frac{2E}{\\pi\\hbar}dt\\), parameter counts — all dimensionless. Divide any two and <em>the expansion law itself</em> comes out.</p>
</div>

<h2>EPISODES</h2>

''' + BODY + '''

<div class="aside">
<span class="tag">You do not need the earlier series</span>
Every formula is given where it is needed. That said, reading <strong>"Conformal Transformations That Click", Ep.3 and bonus episodes ②③</strong> (what "light slowing down" really is / is the universe a computer with finite resources / one cell per tick) makes it much clearer where this series starts from.<br>
The position here is consistent throughout: <em>\\(c\\cdot t=\\text{const}\\) is a rewriting, not new physics</em> (proved in Ep.3). That is precisely why it can be substituted into any equation safely. <strong>What is under discussion is "shortness", never "correctness".</strong> The verdict of the previous series stands unchanged: extrapolated to the early universe at face value, it contradicts nucleosynthesis.
</div>

<p class="foot">"c·t = const, That Clicks" / a sequel to "Conformal Transformations That Click" (itself a sequel to "Cosmology That Clicks"). Every episode carries both an accessible narrative and the reveal of what it means physically. The quantities of information theory (bit counts, operation counts, parameter counts, entropy) are dimensionless and are therefore unmoved by a conformal transformation — they belong, from the start, to the "physics" column of the previous series' decision procedure. Note that the "operation count" used here is the energetic upper bound from the Margolus–Levitin limit and does not refer to meaningful computation. Linear expansion (\\(c\\cdot t=\\)const, \\(R_h=ct\\)) is a minority model still under test; Melia and collaborators argue it is favoured by low-redshift data, while extrapolating it into the early universe contradicts big-bang nucleosynthesis (Lewis, Barnes &amp; Kaushik 2016, MNRAS 460, 291). This series treats \\(c\\cdot t=\\text{const}\\) purely from the standpoint of <strong>notational brevity</strong> and does not argue for its correctness. The academic standard remains the \\(\\Lambda\\)CDM model including inflation. ── Each page can be saved as PDF via the browser's Print dialogue. Keep this contents page and the episode files in the same folder (the links are relative). Japanese original: <a href="../wakaru-ct/index.html" style="color:inherit;text-decoration:underline">わかる c·t=一定</a>.</p>

</article>
</body>
</html>
'''

io.open('../index.html','w',encoding='utf-8').write(HEAD)
import re as _re
o=len(_re.findall(r'<div\b',HEAD)); c=HEAD.count('</div>')
print(f'EN index: {len(HEAD)} chars  div {o}/{c} {"OK" if o==c else "*** NG ***"}  a.ep={HEAD.count(chr(60)+"a class=")}')
