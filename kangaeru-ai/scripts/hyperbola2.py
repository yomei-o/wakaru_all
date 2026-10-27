# Recovery of 第1回: steps S vs samples E for ES on a HARDER landscape (50-dim, condition number 100, target far from start).
import numpy as np
from scipy.optimize import curve_fit
rng = np.random.default_rng(5); d = 50; sig = 1.0; a = np.geomspace(0.02, 2.0, d); target = 2.0; R = 16
L = lambda th: 0.5*np.sum(a*th**2, axis=-1)
def steps(eta, N, maxk=4000):
    th = np.ones((R, d))*3.0; hit = np.full(R, maxk); alive = np.ones(R, bool)
    for k in range(1, maxk+1):
        e = rng.standard_normal((N, R, d)); g = ((1.0+L(th+sig*e))/sig)[..., None]*e; th = th - eta*g.mean(0)
        Lt = L(th)
        if not np.isfinite(Lt).all() or Lt.max() > 1e6: return maxk
        newly = alive & (Lt < target); hit[newly] = k; alive &= ~newly
        if not alive.any(): break
    return np.median(hit)
Ns = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]; S = []
for N in Ns:
    S.append(min(steps(eta, N) for eta in np.geomspace(1e-3, 0.3, 16))); print(f"N={N:<4} S={S[-1]:.0f}  E=NS={N*S[-1]:.0f}", flush=True)
S = np.array(S, float); E = np.array(Ns)*S
f = lambda N, Smin, Bc: Smin*(1+Bc/N)
(Smin, Bc), _ = curve_fit(f, np.array(Ns, float), S, p0=[S[-1], 10], maxfev=20000); Emin = Smin*Bc
print(f"fit: Smin={Smin:.1f} Emin={Emin:.0f} Bcrit={Bc:.1f}")
print(f"{'N':>5}{'S':>7}{'E':>8}{'(S/Smin-1)(E/Emin-1)':>22}")
for N, s, e in zip(Ns, S, E): print(f"{N:>5}{s:>7.0f}{e:>8.0f}{(s/Smin-1)*(e/Emin-1):>22.2f}")
