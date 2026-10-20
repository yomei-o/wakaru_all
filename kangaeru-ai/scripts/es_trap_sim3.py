# (C) fixed eta/N, growing N: kurtosis of the averaged kick falls as 1/N -> real ES should approach the SDE theory.
# (B) antithetic ES on the symmetric well: noise vanishes at the saddle -> no escape in the SDE limit;
#     escapes only through finite steps, so the eta/N exchange law should fail.
import sys, numpy as np
sys.path.insert(0, r'C:\prog\claude\lines\scripts')
from es_trap_theory import mfpt, Lf
rng = np.random.default_rng(23)
def run(s, kind, c, eta, N, M=400, tcap=1e4):
    xm = np.sqrt(1-3*s*s); x = np.full(M, -xm); t = np.full(M, np.nan); alive = np.ones(M, bool); k = 0
    while alive.any() and k*eta < tcap:
        xa = x[alive]; e = rng.standard_normal((N, xa.size))
        if kind == 'one': g = ((c + Lf(xa+s*e))/s*e).mean(0)
        else:             g = ((Lf(xa+s*e) - Lf(xa-s*e))/(2*s)*e).mean(0)
        xa = xa - eta*g; x[alive] = xa; k += 1
        bad = ~np.isfinite(xa) | (np.abs(xa) > 50); done = (xa > xm) | bad
        idx = np.flatnonzero(alive)[done]; t[idx] = k*eta; alive[idx] = False
    return np.nanmean(t), np.isfinite(t).mean()
part = sys.argv[1] if __name__ == "__main__" else ""
if part == 'C':
    for s in [0.28, 0.32]:
        th, _ = mfpt(s, 'one', 1.5, 0.005)
        print(f"(C) one-sided c=1.5 sigma={s} eta/N=0.005   SDE theory tau={th:.1f}")
        for eta, N in [(0.005, 1), (0.01, 2), (0.02, 4), (0.04, 8), (0.08, 16)]:
            m, f = run(s, 'one', 1.5, eta, N)
            print(f"    eta={eta:<6} N={N:<3} kurtosis/N={ {0.28:23.0,0.32:42.2}[s]/N:6.1f}   tau={m:7.1f}", flush=True)
else:
    print("(B) sigma=0.3, eta/N=0.05, cap t=400: fraction escaped")
    for kind, c in [('one', 1.5), ('anti', 0.0)]:
        th, _ = mfpt(0.3, kind, c, 0.05)
        for eta, N in [(0.05, 1), (0.1, 2), (0.2, 4)]:
            m, f = run(0.3, kind, c, eta, N, tcap=400)
            print(f"    {kind:4s} eta={eta:<5} N={N}  escaped {f*100:5.1f}%  mean tau={m:7.1f}   SDE theory {th:.3g}", flush=True)
