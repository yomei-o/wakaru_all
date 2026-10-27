# Fermion sign problem = the node problem of 第8回.  Two spinless fermions in a 1D harmonic trap (hbar=m=ω=1).
# Exact: ψ_F ∝ φ0(x1)φ1(x2) - φ1(x1)φ0(x2), E_F = 2;  bosonic ground state E_B = 1.
# Diffusion Monte Carlo = imaginary-time heat kernel with branching.  Positive walkers cannot carry a sign:
#   (i) free DMC   -> collapses to the boson, E -> 1
#  (ii) fixed node: kill walkers that cross x1 = x2 (node exact in 1D) -> E -> 2
# (iii) released node: walkers cross and flip sign; <sign>(t) ~ e^{-(E_F-E_B) t} = e^{-t}: exponential wall in imaginary time.
import numpy as np
rng = np.random.default_rng(13); dt = 0.01; N0 = 20000
V = lambda x: 0.5*(x**2).sum(1)
def run(mode, T):
    x = rng.normal(0, 1, (N0, 2))
    if mode != 'boson': x = np.sort(x, axis=1); x[:, 1] += 0.05        # start with x1 < x2
    s = np.ones(len(x)); ET = 1.5; Eacc = []; out = []
    for k in range(1, int(T/dt)+1):
        xn = x + np.sqrt(dt)*rng.standard_normal(x.shape); n_before = len(xn)
        cross = np.sign(xn[:, 1]-xn[:, 0]) != np.sign(x[:, 1]-x[:, 0])
        w = np.exp(-(0.5*(V(xn)+V(x)) - ET)*dt)
        if mode == 'fixed': w = np.where(cross, 0.0, w)
        if mode == 'released': s = np.where(cross, -s, s)
        m = np.floor(w + rng.random(len(w))).astype(int); x = np.repeat(xn, m, axis=0); s = np.repeat(s, m)
        Eacc.append(ET - np.log(len(x)/n_before)/dt)                 # growth estimator (includes killing)
        ET -= 0.2*np.log(len(x)/N0)
        if k % int(2.0/dt) == 0: out.append((k*dt, np.mean(Eacc[-200:]), s.mean(), len(x)))
    return out
print("(i) free DMC (boson), exact E = 1:")
for t, E, sm, n in run('boson', 8.0): print(f"    t={t:4.1f}  E={E:.4f}  walkers {n}")
print("(ii) fixed-node DMC (fermion), exact E = 2:")
for t, E, sm, n in run('fixed', 8.0): print(f"    t={t:4.1f}  E={E:.4f}  walkers {n}")
print("(iii) released node: <sign>(t) vs e^{-(E_F-E_B)t}")
for t, E, sm, n in run('released', 10.0): print(f"    t={t:4.1f}  <sign>={sm:+.4f}   e^(-t)={np.exp(-t):.2e}   noise floor 1/√N={1/np.sqrt(n):.1e}   E(sign-blind)={E:.3f}")
