# Deep dive on "ES is most trapped at sigma = 1/3".
# Exact 1D theory: drift -U_sigma'(x), diffusion D(x) = eta*V(x)/(2N) with V the exact per-sample variance
# of the ES estimator (Gauss-Hermite, exact for polynomials). Exact MFPT by the double-integral formula.
import numpy as np
from numpy.polynomial.hermite_e import hermegauss
z, wq = hermegauss(160); wq = wq/np.sqrt(2*np.pi)
def Lf(x, a=0.0): return (x**2-1)**2 + a*x**3
def est_moments(x, sig, kind, c, a=0.0):
    X = x[:, None] + sig*z[None, :]
    if kind == 'one':  g = (c + Lf(X, a))/sig*z[None, :]
    else:              g = (Lf(X, a) - Lf(x[:, None]-sig*z[None, :], a))/(2*sig)*z[None, :]
    m1 = (g*wq).sum(1); m2 = (g*g*wq).sum(1)
    return m1, m2 - m1**2                       # m1 = grad L_sigma (exact), variance
def mfpt(sig, kind, c, eta_over_N, a=0.0, xl=-3.0, n=6001):
    # minima / saddle of L_sigma from m1 on a grid
    xs = np.linspace(xl, 3.0, n+1); m1, V = est_moments(xs, sig, kind, c, a)
    sgn = np.sign(m1); idx = np.where(np.diff(sgn) != 0)[0]
    roots = xs[idx] - m1[idx]*(xs[idx+1]-xs[idx])/(m1[idx+1]-m1[idx])
    roots = roots[np.concatenate([[True], np.diff(roots) > 1e-6])]   # x=0 on the grid gives a double root
    if len(roots) < 3: return np.inf, None
    xa, xs0, xb = roots[0], roots[1], roots[2]   # left min, saddle, right min
    y = np.linspace(xl, xb, n); m1, V = est_moments(y, sig, kind, c, a)
    D = eta_over_N*V/2; mu = -m1
    with np.errstate(divide='ignore', invalid='ignore'):
        r = mu/D
    if not np.isfinite(r).all(): return np.inf, (xa, xs0, xb)
    dy = y[1]-y[0]
    logpsi = np.concatenate([[0], np.cumsum(0.5*(r[1:]+r[:-1])*dy)])
    inner = np.cumsum(np.exp(logpsi - np.log(D) - logpsi.max()))*dy      # scaled
    outer_int = np.exp(-logpsi + logpsi.max())*inner
    m = y >= xa
    tau = np.trapezoid(outer_int[m], y[m])
    return tau, (xa, xs0, xb)
def eff_barrier(sig, kind, c, a=0.0):
    # Phi = int_{xa}^{saddle} U'/V dx * 2  (per unit eta/N); trap strength independent of eta/N
    xs = np.linspace(-3, 3, 6000); m1, V = est_moments(xs, sig, kind, c, a)
    sgn = np.sign(m1); idx = np.where(np.diff(sgn) != 0)[0]
    if len(idx) < 3: return 0.0
    i0, i1 = idx[0], idx[1]
    seg = slice(i0, i1+1)
    with np.errstate(divide='ignore', invalid='ignore'):
        f = 2*m1[seg]/V[seg]
    return np.trapezoid(f, xs[seg]) if np.isfinite(f).all() else np.inf
if __name__ == '__main__':
    sg = np.linspace(0.05, 0.56, 103)
    print("(1) one-sided ES with offset c: sigma* maximizing the effective barrier Phi (independent of eta/N)")
    print("    naive prediction (c >> L): sigma* = 1/3 = 0.3333")
    for c in [0.0, 0.1, 0.3, 1.0, 1.5, 3.0, 10.0, 100.0]:
        ph = np.array([eff_barrier(s, 'one', c) for s in sg])
        k = np.argmax(ph)
        print(f"    c={c:<6} sigma*={sg[k]:.3f}   Phi_max*(c^2)={ph[k]*max(c,1e-9)**2 if c>0 else ph[k]:.4g}")
    print("(2) antithetic ES, symmetric well: noise variance at the saddle x=0")
    for s in [0.2, 0.3, 0.4]:
        _, V0 = est_moments(np.array([0.0, 1e-3, 1e-2]), s, 'anti', 0)
        print(f"    sigma={s}: V(0)={V0[0]:.2e}  V(1e-3)={V0[1]:.2e}  V(1e-2)={V0[2]:.2e}")
    print("    asymmetric well L=(x^2-1)^2 + a x^3: V at saddle")
    for a in [0.05, 0.1, 0.2]:
        xs = np.linspace(-1, 1, 20001); m1, V = est_moments(xs, 0.3, 'anti', 0, a)
        i = np.argmin(np.abs(m1[(xs>-0.5)&(xs<0.5)])); sub = xs[(xs>-0.5)&(xs<0.5)]
        print(f"    a={a}: saddle x={sub[i]:+.4f}  V(saddle)={V[(xs>-0.5)&(xs<0.5)][i]:.3e}")
