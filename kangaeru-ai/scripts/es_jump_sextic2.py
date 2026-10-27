# Recovery of 第4回: degree -> exponent lemma. Antithetic ES on a sextic well: predict ln tau ∝ (1/r)^{1/3} (vs 1/2 for quartic).
import sys, numpy as np
sys.path.insert(0, r'C:\prog\claude\lines\scripts')
from es_jump_sextic import L, s, xm, g, sim, rng
print(f"sextic well, sigma={s}, x_min={xm:.4f}; one-jump prediction tau = r / P(-r g > |x_min|) (no fit)")
print(f"{'r':>8}{'pred':>9}{'measured':>10}{'esc%':>6}")
rows = []
for r in [0.016, 0.008, 0.004, 0.002, 0.001]:
    P = np.mean(-r*g > -xm); pred = r/P; m, f = sim(r, M=300, tcap=80*pred); rows.append((r, pred, m)); print(f"{r:>8}{pred:>9.1f}{m:>10.1f}{f*100:>6.0f}", flush=True)
rows = np.array(rows); lt = np.log(rows[:, 2])
for al in [0.5, 1/3, 0.25]:
    X = np.c_[np.ones(len(rows)), (1/rows[:, 0])**al]; coef, res, *_ = np.linalg.lstsq(X, lt, rcond=None)
    print(f"  ln tau = A + B (1/r)^alpha, alpha={al:.3f}: residual {float(res[0]) if len(res) else 0:.4f}")
