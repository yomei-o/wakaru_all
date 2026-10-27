# Nelson's stochastic mechanics (1966): dx = b(x,t) dt + sqrt(2D) dW, D = hbar/2m,
# b = (hbar/m) Im(∇ψ/ψ) + (hbar/m) Re(∇ψ/ψ)  (current + osmotic velocity).  Theorem: density of x(t) = |ψ(x,t)|².
# Where it breaks (Grabert–Hänggi–Talkner 1979): multi-time correlations. Test on the oscillator (hbar=m=ω=1).
import numpy as np
rng = np.random.default_rng(7); D = 0.5
# (a) superposition (ψ0 + ψ1)/√2: time-dependent density must track |ψ|²  (theorem, check)
def psi(x, t):
    p0 = np.pi**-0.25*np.exp(-x*x/2)*np.exp(-0.5j*t); p1 = np.pi**-0.25*np.sqrt(2)*x*np.exp(-x*x/2)*np.exp(-1.5j*t)
    return (p0+p1)/np.sqrt(2)
def drift(x, t, h=1e-4):
    r = np.log(psi(x+h, t)) - np.log(psi(x-h, t)); g = r/(2*h)         # ∇ln ψ
    b = g.real + g.imag; return np.clip(np.nan_to_num(b), -CAP, CAP)   # (hbar/m)(Re + Im) with hbar=m=1
M = 200000; dt = 2e-4; CAP = 200.0                    # drift is singular at nodes: cap it, use small dt
x = rng.normal(0, 1/np.sqrt(2), M)                                     # start from |ψ0|²... then let density relax? No: start exactly from |ψ(x,0)|² by rejection
cand = rng.uniform(-6, 6, 4*M); keep = rng.uniform(0, 0.6, 4*M) < np.abs(psi(cand, 0))**2; x = cand[keep][:M]; M = x.size
print("(a) superposition: moments of Nelson process vs quantum <x>(t) = cos t, <x²>(t) = 1 + ... (exact from ψ)")
xs = np.linspace(-6, 6, 2401)
for step in range(0, 30001):
    t = step*dt
    if step % 7500 == 0:
        p = np.abs(psi(xs, t))**2; qm1 = np.trapezoid(xs*p, xs); qm2 = np.trapezoid(xs*xs*p, xs)
        print(f"   t={t:4.1f}  <x>: Nelson {x.mean():+.4f} QM {qm1:+.4f}   <x²>: Nelson {np.mean(x*x):.4f} QM {qm2:.4f}")
    x = np.clip(x + drift(x, t)*dt + np.sqrt(2*D*dt)*rng.standard_normal(M), -8, 8)
# (b) stationary excited state ψ1: two lobes separated by a node at x=0. Two-time correlation C(t) = <x(t) x(0)>.
#     Quantum (symmetrised): Re<1|x(t)x(0)|1> = (|x_10|² + |x_12|²) cos t = 1.5 cos t.
print("\n(b) excited state ψ1, two-time correlation <x(t)x(0)>")
def drift1(x): return np.clip(1/x - x, -CAP, CAP)                                          # ∇ln ψ1 = 1/x - x  (real ψ, osmotic only)
cand = rng.uniform(-6, 6, 4*M); keep = rng.uniform(0, 0.5, 4*M) < 2/np.sqrt(np.pi)*cand**2*np.exp(-cand**2); x = cand[keep][:M]; M = x.size
x0 = x.copy(); crossed = np.zeros(M, bool)
print(f"   {'t':>5}{'Nelson C(t)':>13}{'QM 1.5 cos t':>14}{'crossed node %':>16}")
for step in range(0, 31416):
    t = step*dt
    if step % 3927 == 0: print(f"   {t:>5.2f}{np.mean(x*x0):>13.4f}{1.5*np.cos(t):>14.4f}{crossed.mean()*100:>16.3f}")
    xn = x + drift1(x)*dt + np.sqrt(2*D*dt)*rng.standard_normal(M)
    crossed |= np.sign(xn) != np.sign(x0); x = xn
print(f"   Nelson C(∞) -> (mean of one lobe)² = (2/√π)² = {(2/np.sqrt(np.pi))**2:.4f};  QM crosses zero at t = π/2.")
