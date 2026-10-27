# Sign problem = negative probability.  2D U(1) with a θ-term: Z(θ) = ∫ dU e^{β Σ cos φ_P} e^{iθQ}, Q = Σ_P φ_P/2π.
# Original representation: weight complex -> reweight: <sign> = <cos θQ>_{θ=0} = Z(θ)/Z(0) ~ e^{-V Δf}: exponential wall.
# Dual (character) representation: Z(θ) = Σ_n c_n(θ)^V with c_n(θ) = ∫ dφ/2π e^{β cos φ} cos((θ/2π - n) φ) -> all terms positive.
import numpy as np
from scipy.integrate import quad
from scipy.special import iv
rng = np.random.default_rng(11); beta = 2.0
def c_n(n, theta): return quad(lambda f: np.exp(beta*np.cos(f))*np.cos((theta/(2*np.pi)-n)*f), -np.pi, np.pi)[0]/(2*np.pi)
def Z_ratio_exact(V, theta):
    num = sum(c_n(n, theta)**V for n in range(-6, 7)); den = sum(iv(n, beta)**V for n in range(-6, 7)); return num/den
def plaq(th):
    t1, t2 = th[0], th[1]; p = t1 + np.roll(t2, -1, 0) - np.roll(t1, -1, 1) - t2
    return (p + np.pi) % (2*np.pi) - np.pi                       # principal value in (-π, π]
def sweep(th, L):
    for mu in (0, 1):
        for parity in (0, 1):
            mask = (np.indices((L, L)).sum(0) % 2 == parity); d = rng.uniform(-1.0, 1.0, (L, L))
            prop = th.copy(); prop[mu] = np.where(mask, th[mu]+d, th[mu])
            dS = -beta*(np.cos(plaq(prop)) - np.cos(plaq(th)))
            dl = dS + (np.roll(dS, 1, 1) if mu == 0 else np.roll(dS, 1, 0))
            acc = mask & (rng.random((L, L)) < np.exp(-dl)); th[mu] = np.where(acc, th[mu]+d, th[mu])
    return th
theta = np.pi/2
print(f"2D U(1), β={beta}, θ={theta:.4f}.  per-plaquette Δf = -ln(c_0(θ)/I_0) = {-np.log(c_n(0, theta)/iv(0, beta)):.5f}")
print(f"{'L':>4}{'V':>6}{'exact Z(θ)/Z(0)':>17}{'MC <cos θQ>':>24}{'neg. weight %':>14}{'rel. error':>11}{'negative-term fraction (dual)':>31}")
for L in [4, 8, 12, 16, 24]:
    V = L*L; th = rng.uniform(-np.pi, np.pi, (2, L, L))
    for _ in range(300): th = sweep(th, L)
    nmeas = 4000; vals = np.empty(nmeas)
    for k in range(nmeas):
        for _ in range(3): th = sweep(th, L)
        Q = plaq(th).sum()/(2*np.pi); vals[k] = np.cos(theta*Q)
    m, e = vals.mean(), vals.std()/np.sqrt(nmeas); ex = Z_ratio_exact(V, theta)
    neg = np.mean(vals < 0)*100
    terms = [c_n(n, theta)**V for n in range(-6, 7)]; negfrac = sum(t for t in terms if t < 0)/sum(abs(t) for t in terms)
    print(f"{L:>4}{V:>6}{ex:>17.3e}{m:>14.4f} ± {e:<7.4f}{neg:>14.1f}{(e/abs(m) if m != 0 else np.inf):>11.2f}{negfrac:>31.1e}", flush=True)
print("\n  <sign> ~ e^{-V Δf}: the statistical error of any reweighted observable grows like 1/<sign> -> exponential cost in V.")
print("  In the dual variables every term c_n(θ)^V is positive (V even): the same Z(θ) with no sign problem at all.")
