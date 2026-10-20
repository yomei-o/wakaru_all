# Is the gap between real ES and the SDE theory caused by heavy-tailed kicks?
# Compare real one-sided ES with a Gaussian surrogate (same mean grad L_sigma and same variance V(x)).
import sys, numpy as np
sys.path.insert(0, r'C:\prog\claude\lines\scripts')
from es_trap_theory import mfpt, Lf, est_moments
rng = np.random.default_rng(22)
c, eta, N, M, tcap = 1.5, 0.005, 1, 400, 1500.0
sig = [0.15, 0.2, 0.25, 0.28, 0.3, 0.32, 0.35, 0.4, 0.45, 0.5]
# excess kurtosis of the single-sample estimator at the left minimum
z = rng.standard_normal(2_000_000)
print("single-sample ES gradient at the minimum: excess kurtosis (Gaussian = 0)")
for s in sig:
    xm = -np.sqrt(1-3*s*s); g = (c + Lf(xm+s*z))/s*z
    k = ((g-g.mean())**4).mean()/g.var()**2 - 3
    print(f"   sigma={s:.2f}  kurtosis={k:8.1f}")
def run(kind):
    S = np.repeat(np.array(sig), M); xm = np.sqrt(1-3*S**2)
    x = -xm.copy(); t = np.full(S.size, np.nan); alive = np.ones(S.size, bool); blow = np.zeros(S.size, bool); k = 0
    while alive.any() and k*eta < tcap:
        xa, sa = x[alive], S[alive]
        if kind == 'es':
            e = rng.standard_normal((N, xa.size)); g = ((c + Lf(xa+sa*e))/sa*e).mean(0)
        else:
            m1 = np.empty_like(xa); V = np.empty_like(xa)
            for s in np.unique(sa):
                j = sa == s; a_, b_ = est_moments(xa[j], s, 'one', c); m1[j] = a_; V[j] = b_
            g = m1 + np.sqrt(V/N)*rng.standard_normal(xa.size)
        xa = xa - eta*g; x[alive] = xa; k += 1
        bad = ~np.isfinite(xa) | (np.abs(xa) > 50)
        done = (xa > xm[alive]) | bad; idx = np.flatnonzero(alive)[done]
        t[idx] = k*eta; blow[np.flatnonzero(alive)[bad]] = True; alive[idx] = False
    return t.reshape(len(sig), M), blow.reshape(len(sig), M)
te, be = run('es'); tg, bg = run('gauss')
print(f"\nescape time, eta={eta} N={N} c={c}")
print(f"{'sigma':>6}{'real ES':>10}{'blowups':>9}{'Gauss surrogate':>17}{'SDE theory':>12}")
for i, s in enumerate(sig):
    th, _ = mfpt(s, 'one', c, eta/N)
    print(f"{s:>6.2f}{np.nanmean(te[i]):>10.1f}{be[i].sum():>9d}{np.nanmean(tg[i]):>17.1f}{th:>12.1f}", flush=True)
