# Does "diffusion + single jumps" explain real one-sided ES?  k = 1/tau_SDE + (1/r) P(-r g > x_min), no fit.
import sys, numpy as np
sys.path.insert(0, r'C:\prog\claude\lines\scripts')
from es_trap_theory import mfpt, Lf
c, r = 1.5, 0.005
e = np.random.default_rng(5).standard_normal(20_000_000)
meas = {0.15:10.3, 0.2:28.4, 0.25:48.5, 0.28:54.4, 0.3:50.9, 0.32:45.8, 0.35:36.5, 0.4:21.3, 0.45:13.1, 0.5:7.8}
print(f"{'sigma':>6}{'SDE':>8}{'jump only':>11}{'combined':>10}{'measured':>10}")
for s, m in meas.items():
    xm = np.sqrt(1-3*s*s); g = (c + Lf(-xm+s*e))/s*e
    pj = np.mean(-r*g > xm); kj = pj/r
    tsde, _ = mfpt(s, 'one', c, r)
    print(f"{s:>6.2f}{tsde:>8.1f}{(1/kj if kj>0 else np.inf):>11.1f}{1/(1/tsde+kj):>10.1f}{m:>10.1f}")
