# Candidate small lemma: for antithetic ES on a symmetric polynomial well of degree 2k, the single-sample
# estimator is ~ eps^(2k), so P(jump) ~ exp(-c y^(1/k)) and  ln tau ∝ (N/eta)^(1/k).  Quartic (k=2): 1/2 (verified).
# Test k=3 (sextic): prediction 1/3, and the absolute one-jump formula tau = r / P(-r g > |x_min|), no fit.
import numpy as np
rng = np.random.default_rng(9); s = 0.3; a = 0.5
L = lambda x: (x*x-1)**2*(x*x+a)
z = rng.standard_normal(4_000_000)
Ls = lambda x: L(x[:, None] + s*z[None, :4000]).mean(1)                 # L_sigma on a grid
xs = np.linspace(-1.5, -0.3, 1201); xm = xs[np.argmin(Ls(xs))]
g = (L(xm+s*z) - L(xm-s*z))/(2*s)*z                                      # single-sample antithetic estimator at the minimum
print(f"sextic well, sigma={s}: x_min of L_sigma = {xm:.4f}, excess kurtosis of g = {((g-g.mean())**4).mean()/g.var()**2-3:.0f}")
def sim(r, M=300, tcap=None):
    x = np.full(M, xm); t = np.full(M, np.nan); alive = np.ones(M, bool); k = 0
    while alive.any() and (tcap is None or k*r < tcap):
        xa = x[alive]; e = rng.standard_normal(xa.size)
        xa = xa - r*(L(xa+s*e) - L(xa-s*e))/(2*s)*e; x[alive] = xa; k += 1
        done = (xa > -xm) | ~np.isfinite(xa) | (np.abs(xa) > 50); idx = np.flatnonzero(alive)[done]; t[idx] = k*r; alive[idx] = False
    return np.nanmean(t), np.isfinite(t).mean()
if __name__ == "__main__":
    print(f"{'r=eta/N':>9}    {'P(jump)':>10}{'pred tau':>10}{'measured':>10}{'esc%':>6}")
    rows = []
    for r in [0.1, 0.06, 0.04, 0.025, 0.016]:
        P = np.mean(-r*g > -xm); pred = r/P
        m, f = sim(r, tcap=60*pred); rows.append((r, pred, m))
        print(f"{r:>9}{P:>10.2e}{pred:>10.1f}{m:>10.1f}{f*100:>6.0f}", flush=True)
    rows = np.array(rows); lr = np.log(1/rows[:, 0]); lt = np.log(rows[:, 2])
    # fit ln tau = A + B (1/r)^alpha for alpha in {1/2, 1/3, 1/4}: compare residuals
    for al in [0.5, 1/3, 0.25]:
        X = np.c_[np.ones_like(lr), (1/rows[:, 0])**al]; coef, res, *_ = np.linalg.lstsq(X, lt, rcond=None)
        print(f"  alpha={al:.3f}: residual {float(res[0]) if len(res) else 0:.4f}")
