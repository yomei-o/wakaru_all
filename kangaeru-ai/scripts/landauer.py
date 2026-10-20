# Landauer's principle on plain SGD-with-noise (Langevin at temperature T = 1, the eta/N of map 01).
# 1 bit = which well. Erase: lower barrier -> tilt left -> raise barrier -> remove tilt (Berut et al. 2012).
# Prediction: <W> >= T[ln2 + p ln p + (1-p) ln(1-p)], excess work ~ Lambda^2 / tau (thermodynamic length).
import numpy as np, sys
rng = np.random.default_rng(31)
T, h0, f0, eta, M = 1.0, 8.0, 6.0, 0.002, 4000
def U(x, b, f):  return b*h0*(x*x-1)**2 + (1-b)*2.0*x*x + f*x
def dU(x, b, f): return b*h0*4*x*(x*x-1) + (1-b)*4.0*x + f
def protocol(s):                        # s in [0,1] -> (b, f)
    q = 4*s
    if q < 1: return 1-q, 0.0
    if q < 2: return 0.0, f0*(q-1)
    if q < 3: return q-2, f0
    return 1.0, f0*(4-q)
# equilibrium start in the symmetric double well (sample by long relaxation)
x = rng.choice([-1.0, 1.0], M) + 0.1*rng.standard_normal(M)
for _ in range(20000): x += -eta*dU(x, 1.0, 0.0) + np.sqrt(2*T*eta)*rng.standard_normal(M)
x0 = x.copy()
print(f"barrier h0={h0} kT, start: {np.mean(x0<0)*100:.1f}% left (information ln2 = {np.log(2):.4f} kT)")
print(f"{'tau':>6}{'<W>/kT':>9}{'success p':>11}{'bound':>9}{'excess':>9}{'excess*tau':>12}")
for tau in [2, 5, 10, 20, 50, 100, 200]:
    x = x0.copy(); W = np.zeros(M); n = int(tau/eta)
    b, f = protocol(0.0)
    for k in range(n):
        b2, f2 = protocol((k+1)/n)
        W += U(x, b2, f2) - U(x, b, f); b, f = b2, f2      # work = change of U at fixed x
        x += -eta*dU(x, b, f) + np.sqrt(2*T*eta)*rng.standard_normal(M)
    p = np.mean(x < 0); bound = T*(np.log(2) + (p*np.log(p) if p > 0 else 0) + ((1-p)*np.log(1-p) if p < 1 else 0))
    ex = W.mean()/T - bound
    print(f"{tau:>6}{W.mean()/T:>9.4f}{p:>11.4f}{bound:>9.4f}{ex:>9.4f}{ex*tau:>12.3f}", flush=True)
