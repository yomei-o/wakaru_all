# Double well V = x²(1-√g x)²/2 = x²/2 - √g x³ + g x⁴/2  (Zinn-Justin normalisation, hbar=m=1).
# 1) RS series of E0 in ε=√g with V1 = -x³ (order ε), V2 = x⁴/2 (order ε²); odd orders must vanish -> e_k = E^(2k).
# 2) coefficients should be ALL NEGATIVE (non-alternating) -> Borel singularity on the positive axis: non-Borel-summable.
# 3) lateral Borel sum has Im part; compare with the two-instanton scale ΔE² where ΔE = E1-E0 ~ e^{-1/(6g)} (one instanton).
#    Also compare Re(lateral Borel) with the exact (E0+E1)/2.
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
from mpmath import mp, mpf, sqrt, factorial, pade, polyval, quad, exp, inf, mpc, im, re, log
mp.dps = 60; K = 70; NB = 3*K+12
def x_apply(v):
    out = [mpf(0)]*NB
    for n in range(NB):
        if v[n] == 0: continue
        if n >= 1: out[n-1] += sqrt(mpf(n))/sqrt(2)*v[n]
        if n+1 < NB: out[n+1] += sqrt(mpf(n+1))/sqrt(2)*v[n]
    return out
def V1(v): return [-c for c in x_apply(x_apply(x_apply(v)))]          # -x³
def V2(v): return [c/2 for c in x_apply(x_apply(x_apply(x_apply(v))))]  # x⁴/2
E = [mpf(0)]*(K+1); psi = [[mpf(0)]*NB]; psi[0][0] = mpf(1)
for k in range(1, K+1):
    w = V1(psi[k-1]); 
    if k >= 2:
        w2 = V2(psi[k-2]); w = [a+b for a, b in zip(w, w2)]
    E[k] = w[0]
    r = [w[n] - sum(E[j]*psi[k-j][n] for j in range(1, k+1)) for n in range(NB)]
    psi.append([mpf(0)] + [-r[n]/n for n in range(1, NB)])
print("odd orders (should vanish):", ", ".join(f"{float(E[k]):.1e}" for k in [1, 3, 5, 7]))
e = [mpf('0.5')] + [E[2*k] for k in range(1, K//2+1)]; Kg = len(e)-1
print("e_k (series in g):", ", ".join(f"{float(e[k]):.6g}" for k in range(0, 6)), "...")
print("signs of e_1..e_35 all negative?", all(e[k] < 0 for k in range(1, Kg+1)), "   e_35/e_34 =", f"{float(e[Kg]/e[Kg-1]):.2f}", "(expect ~ 3k: Borel radius 1/3, singularity at t=+1/3 -> non-Borel-summable)")
b = [e[k]/factorial(k) for k in range(Kg+1)]; P, Q = pade(b, Kg//2, Kg//2)
B = lambda t: polyval(P[::-1], t)/polyval(Q[::-1], t)
def borel(g, th): w = exp(mpc(0, th)); return quad(lambda s: exp(-s*w)*B(g*s*w)*w, [0, inf])
def exact_pair(g):
    L = 1/np.sqrt(g); x = np.linspace(-6, L+6, 6000); h = x[1]-x[0]; V = x**2*(1-np.sqrt(g)*x)**2/2
    H = sp.diags([np.full(len(x)-1, -0.5/h**2), 1/h**2 + V, np.full(len(x)-1, -0.5/h**2)], [-1, 0, 1])
    ev = spl.eigsh(H, k=2, which='SA')[0]; return np.sort(ev)
print(f"\n{'g':>6}{'E0 exact':>14}{'ΔE=E1-E0':>12}{'(E0+E1)/2':>14}{'Re Borel±':>14}{'mean-ReBorel':>14}{'|Im Borel|':>12}{'ΔE²':>11}{'Im/ΔE²':>9}")
rows = []
for g in [0.02, 0.025, 0.03, 0.04, 0.05]:
    E0, E1 = exact_pair(g); bl = borel(mpf(g), 0.25)
    mean = (E0+E1)/2; dE = E1-E0; rb = float(re(bl)); ib = float(abs(im(bl)))
    rows.append((g, ib, mean-rb, dE))
    print(f"{g:>6}{E0:>14.8f}{dE:>12.3e}{mean:>14.8f}{rb:>14.8f}{mean-rb:>14.2e}{ib:>12.3e}{dE*dE:>11.3e}{ib/dE**2:>9.3f}")
r = np.array(rows); sl = np.polyfit(1/r[:, 0], np.log(r[:, 1]), 1)[0]
print(f"\nslope of ln|Im Borel| vs 1/g = {sl:.3f}   (two-instanton action 2S = 1/(3g) -> expect -1/3 = -0.333)")
sl2 = np.polyfit(1/r[:, 0], np.log(r[:, 3]), 1)[0]
print(f"slope of ln ΔE vs 1/g = {sl2:.3f}   (one instanton S = 1/(6g) -> expect -0.167)")
