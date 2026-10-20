# Measure ES escape times. (A) one-sided c=1.5 vs sigma, compare with exact MFPT theory.
# (B) antithetic vs one-sided at fixed eta/N but different (eta, N): does the eta/N exchange law hold?
import sys, numpy as np
sys.path.insert(0, r'C:\prog\claude\lines\scripts')
from es_trap_theory import mfpt, Lf
rng = np.random.default_rng(21)
def run(sigmas, kind, c, eta, N, M=400, tcap=1e9, a=0.0):
    S = np.repeat(np.array(sigmas, float), M)
    xm = np.sqrt(np.clip(1-3*S**2, 0, None))           # minima of L_sigma (a=0)
    x = -xm.copy(); t_hit = np.full(S.size, np.nan); alive = np.ones(S.size, bool); k = 0
    while alive.any() and k*eta < tcap:
        xa, sa = x[alive], S[alive]; e = rng.standard_normal((N, xa.size))
        if kind == 'one': g = ((c + Lf(xa+sa*e, a))/sa*e).mean(0)
        else:             g = ((Lf(xa+sa*e, a) - Lf(xa-sa*e, a))/(2*sa)*e).mean(0)
        xa = xa - eta*g; x[alive] = xa; k += 1
        done = xa > xm[alive]; idx = np.flatnonzero(alive)[done]; t_hit[idx] = k*eta; alive[idx] = False
    t_hit = t_hit.reshape(len(sigmas), M)
    return [(np.nanmean(r), np.isfinite(r).mean()) for r in t_hit]
part = sys.argv[1] if len(sys.argv) > 1 else 'A'
if part == 'A':
    sig = [0.15, 0.2, 0.25, 0.3, 0.32, 0.35, 0.4, 0.45, 0.5]
    for eta, N in [(0.005, 1), (0.01, 2)]:
        res = run(sig, 'one', 1.5, eta, N)
        print(f"(A) one-sided c=1.5  eta={eta} N={N} (eta/N={eta/N})")
        for s, (m, f) in zip(sig, res):
            th, _ = mfpt(s, 'one', 1.5, eta/N)
            print(f"   sigma={s:.2f}  measured tau={m:7.1f}  theory={th:7.1f}", flush=True)
else:
    for eN, pairs in [(0.05, [(0.05, 1), (0.1, 2), (0.2, 4)])]:
        for kind, c in [('one', 1.5), ('anti', 0.0)]:
            print(f"(B) {kind:4s} sigma=0.3  eta/N={eN}  (cap t=400)")
            for eta, N in pairs:
                (m, f), = run([0.3], kind, c, eta, N, M=400, tcap=400)
                th, _ = mfpt(0.3, kind, c, eN)
                print(f"   eta={eta:<5} N={N}  escaped {f*100:5.1f}%  mean tau(escaped)={m:7.1f}   SDE theory tau={th:.3g}", flush=True)
