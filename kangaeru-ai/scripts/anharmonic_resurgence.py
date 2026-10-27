# Resurgence one level up: H = p²/2 + x²/2 + g x⁴ (quantum mechanics = 1-d field theory).
# 1) perturbative E0(g) = Σ e_k g^k to order K by Rayleigh–Schrödinger recursion in the oscillator basis (mpmath)
# 2) g>0: Borel–Padé sum vs exact diagonalisation   3) g<0: Im of lateral Borel sum vs Γ/2 from complex scaling
import numpy as np
from mpmath import mp, mpf, sqrt, factorial, pade, polyval, quad, exp, inf, mpc, im, re
mp.dps = 60; K = 60; NB = 4*K+9
def x2_apply(v):                       # x² in oscillator basis, v is a list of mpf of length NB
    out = [mpf(0)]*NB
    for n in range(NB):
        if v[n] == 0: continue
        out[n] += (2*n+1)/mpf(2)*v[n]
        if n >= 2: out[n-2] += sqrt(mpf(n*(n-1)))/2*v[n]
        if n+2 < NB: out[n+2] += sqrt(mpf((n+1)*(n+2)))/2*v[n]
    return out
def V_apply(v): return x2_apply(x2_apply(v))                       # x⁴
E = [mpf(0)]*(K+1); psi = [[mpf(0)]*NB]; psi[0][0] = mpf(1)
for k in range(1, K+1):
    w = V_apply(psi[k-1]); E[k] = w[0]                                # E^(k) = <0|V|ψ^(k-1)>
    r = [w[n] - sum(E[j]*psi[k-j][n] for j in range(1, k+1)) for n in range(NB)]
    nxt = [mpf(0)] + [-r[n]/n for n in range(1, NB)]                  # R = Q/(E0 - H0) = -1/n on |n>
    psi.append(nxt)
e = [mpf('0.5')] + E[1:]
print("perturbative coefficients e_k of E0(g), H = p²/2 + x²/2 + g x⁴:")
print("  ", ", ".join(f"{float(e[k]):.6g}" for k in range(0, 6)), " ...  e_60/e_59 =", f"{float(e[60]/e[59]):.3f}", "(large-order growth ~ -3k: Bender–Wu)")
b = [e[k]/factorial(k) for k in range(K+1)]; P, Q = pade(b, K//2, K//2)
B = lambda t: polyval(P[::-1], t)/polyval(Q[::-1], t)
def borel(g, th=0): w = exp(mpc(0, th)); return quad(lambda s: exp(-s*w)*B(g*s*w)*w, [0, inf])
# exact: diagonalise in a big basis (numpy)
n = np.arange(600); a = np.diag(np.sqrt(n[1:]), 1); X = (a + a.T)/np.sqrt(2); X2 = X@X; X4 = X2@X2; H0 = np.diag(n+0.5)
print(f"\ng>0: {'g':>6}{'Borel–Padé':>22}{'exact diag':>22}{'|diff|':>10}{'optimal truncation':>20}")
for g in [0.01, 0.05, 0.1, 0.5, 1.0]:
    ex = np.linalg.eigvalsh(H0 + g*X4)[0]; bs = float(re(borel(mpf(g))))
    partial = [float(sum(e[k]*mpf(g)**k for k in range(N+1))) for N in range(1, K)]; opt = min(abs(pp-ex) for pp in partial)
    print(f"     {g:>6}{bs:>22.12f}{ex:>22.12f}{abs(bs-ex):>10.1e}{opt:>20.1e}")
print(f"\ng<0: lateral Borel sum vs complex scaling (resonance E - iΓ/2)")
print(f"     {'g':>6}{'Re Borel':>14}{'Im Borel':>12}{'Re E (c.s.)':>14}{'Γ/2 (c.s.)':>12}{'ratio':>7}{'e^(-1/3|g|)':>12}")
for g in [-0.02, -0.03, -0.05, -0.08]:
    th = 0.35; sc = np.exp(2j*th); Hc = np.diag(n+0.5)*0 + (np.diag(n+0.5) - X2/2)/sc + X2/2*sc + g*X4*sc**2   # p²/2 = H0 - x²/2
    ev = np.linalg.eigvals(Hc); res = ev[np.argmin(np.abs(ev - 0.5))]
    bl = borel(mpf(g), 0.3)
    print(f"     {g:>6}{float(re(bl)):>14.8f}{float(abs(im(bl))):>12.3e}{res.real:>14.8f}{-res.imag:>12.3e}{float(abs(im(bl)))/(-res.imag):>7.3f}{np.exp(-1/(3*abs(g))):>12.1e}")
