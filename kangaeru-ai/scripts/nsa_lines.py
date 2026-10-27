# A. Divergent perturbation series as a true series at infinitesimal g (resurgence in one integral)
#    Z(g) = ∫ exp(-x²/2 - g x⁴/4) dx / √(2π) = Σ c_n g^n,  c_n = (-1/4)^n (4n-1)!! / n!  ~ n! growth
#    optimal truncation error should be ~ exp(-1/(4g)) = the instanton (saddle of the exponent at x² = -1/g).
import numpy as np, math
from scipy.integrate import quad
from mpmath import mp, mpf, factorial, exp, quad as mquad, sqrt, pi, gamma as mgamma
def factorial2(n): return mgamma(n/mpf(2)+1)*mpf(2)**((n+1)/mpf(2))/sqrt(pi) if n % 2 == 1 else mpf(2)**(n/2)*factorial(n/2)
mp.dps = 40
def Z(g): return mquad(lambda x: exp(-x**2/2 - g*x**4/4), [-mp.inf, mp.inf])/sqrt(2*pi)
c = [mpf(-1)**n/mpf(4)**n*factorial2(4*n-1)/factorial(n) for n in range(0, 120)]
print("A. divergent series Z(g) = Σ c_n g^n   (c_n/c_{n-1} ~ -4n: factorial growth)")
print(f"{'g':>7}{'exact Z':>16}{'best N':>8}{'|error| at best N':>19}{'exp(-1/4g)':>13}{'ratio':>8}")
for g in [mpf('0.02'), mpf('0.05'), mpf('0.1'), mpf('0.2')]:
    ex = Z(g); best = None
    for N in range(1, 119):
        s = sum(c[n]*g**n for n in range(N+1)); e = abs(s-ex)
        if best is None or e < best[1]: best = (N, e)
    inst = exp(-1/(4*g))
    print(f"{float(g):>7}{float(ex):>16.10f}{best[0]:>8}{float(best[1]):>19.2e}{float(inst):>13.2e}{float(best[1]/inst):>8.2f}")
print("   -> the smallest error you can get from the series is the instanton; the series 'knows' the non-perturbative sector.")

# B. Dimension as an infinitesimal dial: delta well in d = 2 - eps dimensions.
#    Bound state: 1 = g ∫ d^d k/(2π)^d / (k²/2 + |E|) = g * C_d * |E|^{d/2-1},  C_d = (2π)^{-d} S_{d-1} ∫ q^{d-1} dq/(q²/2+1)
#    For d < 2 this is finite: |E| = (1/(g C_d))^{2/(2-d)}.  As d -> 2 the exponent 2/(2-d) -> ∞: that is exp(-const/g).
from scipy.special import gamma
def Cd(d):
    Sd = 2*np.pi**(d/2)/gamma(d/2)
    val, _ = quad(lambda q: q**(d-1)/(q*q/2+1), 0, np.inf)
    return Sd/(2*np.pi)**d*val
print("\nB. delta well in d = 2 - eps dimensions: |E| for g = 1 (no cutoff needed when eps > 0)")
print(f"{'eps':>8}{'d':>8}{'|E|':>14}{'2/(2-d)':>9}")
for eps in [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]:
    d = 2-eps; E = (1/(1.0*Cd(d)))**(2/(2-d))
    print(f"{eps:>8}{d:>8}{E:>14.4e}{2/(2-d):>9.1f}")
print("   compare 2D with cutoff 1/eps_width: |E| = (Λ²/2) exp(-2π/g) -> at g=1: exp(-2π) =", f"{math.exp(-2*math.pi):.3e}", "× Λ²/2")
print("   -> as eps -> 0 the finite answer in d = 2 - eps goes to 0 (g standard) : same verdict as the cutoff version, 'no standard part at fixed g'.")
