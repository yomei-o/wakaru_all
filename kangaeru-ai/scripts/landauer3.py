# (1) 1/τ where it is exact: overdamped particle (γ=1, T=1) in a trap k=1 moved by L in time τ.
#     Schmiedl–Seifert optimal protocol: jump by L/(τ+2) at start and end, linear in between: W_excess = L²/(τ+2).
# (2) erasure with fast barrier operations: lower barrier instantly, tilt slowly (optimal-like linear ramp), raise instantly.
import numpy as np
rng = np.random.default_rng(41); eta = 0.001; M = 20000; T = 1.0
print("(1) trap translation L=2, k=1: excess work vs τ  (exact optimal: L²/(τ+2); naive linear ramp ~ L²/τ for large τ)")
print(f"{'tau':>6}{'optimal W':>11}{'L²/(τ+2)':>10}{'linear W':>10}")
L = 2.0
for tau in [1, 2, 5, 10, 20, 50]:
    for name in ['opt', 'lin']:
        x = rng.standard_normal(M); n = int(tau/eta); W = np.zeros(M); lam = 0.0
        for k in range(n):
            s = (k+1)/n
            lam2 = (L/(tau+2))*(1 + k*eta) if name == 'opt' else L*s      # opt: jump L/(τ+2) then slope L/(τ+2) per unit time
            if name == 'opt' and k == n-1: lam2 = L
            W += 0.5*((x-lam2)**2 - (x-lam)**2); lam = lam2
            x += -eta*(x-lam) + np.sqrt(2*T*eta)*rng.standard_normal(M)
        if name == 'opt': wo = W.mean()
        else: wl = W.mean()
    print(f"{tau:>6}{wo:>11.4f}{L*L/(tau+2):>10.4f}{wl:>10.4f}", flush=True)
print("\n(2) erasure, barrier 8kT: lower instantly -> tilt slowly over τ -> raise instantly")
h0, f0 = 8.0, 6.0
def U(x, b, f):  return b*h0*(x*x-1)**2 + (1-b)*2.0*x*x + f*x
def dU(x, b, f): return b*h0*4*x*(x*x-1) + (1-b)*4.0*x + f
x = rng.choice([-1.0, 1.0], M) + 0.1*rng.standard_normal(M)
for _ in range(20000): x += -eta*dU(x, 1.0, 0.0) + np.sqrt(2*T*eta)*rng.standard_normal(M)
x0 = x.copy()
print(f"{'tau':>6}{'<W>/kT':>9}{'p':>8}{'bound':>8}{'excess':>9}{'excess*tau':>12}")
for tau in [2, 5, 10, 20, 50, 100, 200]:
    x = x0.copy(); W = np.zeros(M); n = int(tau/eta)
    W += U(x, 0.0, 0.0) - U(x, 1.0, 0.0)                          # instant lowering (work = ΔU at fixed x)
    for _ in range(2000): x += -eta*dU(x, 0.0, 0.0) + np.sqrt(2*T*eta)*rng.standard_normal(M)   # short relax in single well
    f = 0.0
    for k in range(n):
        f2 = f0*(k+1)/n; W += (f2-f)*x; f = f2
        x += -eta*dU(x, 0.0, f) + np.sqrt(2*T*eta)*rng.standard_normal(M)
    W += U(x, 1.0, f0) - U(x, 0.0, f0)                             # instant raising
    for _ in range(2000): x += -eta*dU(x, 1.0, f0) + np.sqrt(2*T*eta)*rng.standard_normal(M)
    W += U(x, 1.0, 0.0) - U(x, 1.0, f0)                            # remove tilt instantly (barrier up: particle stays)
    p = np.mean(x < 0); bound = T*(np.log(2) + (p*np.log(p) if p > 0 else 0) + ((1-p)*np.log(1-p) if p < 1 else 0))
    ex = W.mean()/T - bound; print(f"{tau:>6}{W.mean()/T:>9.4f}{p:>8.4f}{bound:>8.4f}{ex:>9.4f}{ex*tau:>12.2f}", flush=True)
