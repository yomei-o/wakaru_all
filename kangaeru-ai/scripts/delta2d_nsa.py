# Nonstandard-analysis picture of renormalisation: a 2D well of infinitesimal width eps and total strength g.
# Bound state (s-wave, hbar = m = 1): inside J0(k r), outside K0(kappa r), match log-derivatives at r = eps.
# Question: does E(eps, g) have a standard part as eps -> 0 at fixed g?  If not, what must g(eps) be?
import numpy as np
from scipy.special import j0, j1, k0, k1
from scipy.optimize import brentq
def E_bound(eps, g):
    V0 = g/(np.pi*eps**2)                                   # depth so that ∫V d²r = g
    def f(E):                                               # E < 0
        k = np.sqrt(2*(V0 + E)); ka = np.sqrt(-2*E)
        return -k*j1(k*eps)/j0(k*eps) + ka*k1(ka*eps)/k0(ka*eps)
    lo, hi = -V0*(1-1e-12), -1e-300
    # scan for a sign change on a log grid
    Es = -np.logspace(np.log10(V0*(1-1e-9)), -300, 4000)
    v = [f(E) for E in Es]
    for i in range(len(Es)-1):
        if np.isfinite(v[i]) and np.isfinite(v[i+1]) and v[i]*v[i+1] < 0: return brentq(f, Es[i], Es[i+1])
    return np.nan
print("2D well: bound-state energy at fixed g as the width eps -> 0 (infinitesimal)")
print(f"{'eps':>8}{'E (g=0.5)':>14}{'E (g=1)':>14}{'E (g=2)':>14}")
for eps in [1, 0.1, 0.01, 1e-3, 1e-4]:
    print(f"{eps:>8g}" + "".join(f"{E_bound(eps, g):>14.4e}" for g in [0.5, 1, 2]))
print("  -> |E| ∝ (1/eps^2) exp(-2π/g): no standard part at fixed g (the limit is -∞ ... or 0 if g infinitesimal).")
print("\nWhat g(eps) keeps E = -1 fixed?  (the 'running coupling')")
print(f"{'eps':>8}{'g(eps)':>10}{'1/g':>8}{'ln(1/eps)':>10}{'Δ(1/g)/Δln(1/eps)':>20}")
prev = None
for eps in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    g = brentq(lambda g: E_bound(eps, g) + 1.0, 0.05, 20)
    slope = (1/g - prev[0])/(np.log(1/eps) - prev[1]) if prev else float('nan')
    print(f"{eps:>8g}{g:>10.4f}{1/g:>8.3f}{np.log(1/eps):>10.2f}{slope:>20.4f}")
    prev = (1/g, np.log(1/eps))
print(f"  prediction from 1 = g∫d²k/(2π)²/(k²/2+|E|):  1/g = (1/π) ln(1/eps) + const  ->  slope 1/π = {1/np.pi:.4f}")
