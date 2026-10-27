# Can any positive-probability process reproduce the quantum two-time correlation of ψ1?
# (i) Cauchy–Schwarz: C(π) = -C(0) forces x(π) = -x(0) a.s.  -> impossible for a diffusion.
# (ii) Classical phase-space flow x(t) = x cos t + p sin t with the WIGNER function as (signed) weights reproduces
#      both the stationary marginal |ψ1|² and C(t) = 1.5 cos t.  Clip the negative part -> both fail (Hudson 1974).
import numpy as np
x = np.linspace(-6, 6, 601); p = np.linspace(-6, 6, 601); X, P = np.meshgrid(x, p, indexing='ij'); dx = x[1]-x[0]
psi1 = lambda x: np.pi**-0.25*np.sqrt(2)*x*np.exp(-x*x/2)
# Wigner function by direct integral W(x,p) = (1/π) ∫ ψ(x+y) ψ(x-y) e^{2ipy} dy
y = np.linspace(-8, 8, 1601); dy = y[1]-y[0]
W = np.array([[np.sum(psi1(xi+y)*psi1(xi-y)*np.cos(2*pi_*y))*dy/np.pi for pi_ in p] for xi in x])
R2 = X**2+P**2; W_formula = (2*R2-1)*np.exp(-R2)/np.pi
print(f"Wigner of ψ1: max|numeric - formula| = {np.abs(W-W_formula).max():.1e};  W(0,0) = {W[300,300]:.4f} (= -1/π = {-1/np.pi:.4f});  negative volume = {-W[W<0].sum()*dx*dx:.4f}")
def marginal_at(Wt, t):                       # rotate phase space by t (classical oscillator flow), take x-marginal
    Xr = X*np.cos(t) - P*np.sin(t); Pr = X*np.sin(t) + P*np.cos(t)
    from scipy.interpolate import RegularGridInterpolator
    f = RegularGridInterpolator((x, p), Wt, bounds_error=False, fill_value=0.0)
    Wr = f(np.stack([Xr.ravel(), Pr.ravel()], 1)).reshape(X.shape)
    return Wr.sum(1)*dx
Wclip = np.clip(W, 0, None); Wclip /= Wclip.sum()*dx*dx
Wprod = psi1(X)**2*psi1(P)**2                 # positive product ensemble with the right marginals at t=0
print(f"\n{'weights':>22}{'ρ(x=0) at t=0':>15}{'ρ(x=0) at t=π/4':>17}{'C(0)=<x²>':>11}{'C(π/2)':>9}{'C(π)':>9}   (QM: 0, 0, 1.5, 0, -1.5)")
for name, Wt in [('Wigner (signed)', W), ('Wigner clipped ≥0', Wclip), ('product ψ1²(x)ψ1²(p)', Wprod)]:
    C = lambda t: np.sum(Wt*(X*np.cos(t)+P*np.sin(t))*X)*dx*dx
    m0 = marginal_at(Wt, 0.0)[300]; m4 = marginal_at(Wt, np.pi/4)[300]
    print(f"{name:>22}{m0:>15.4f}{m4:>17.4f}{C(0):>11.4f}{C(np.pi/2):>9.4f}{C(np.pi):>9.4f}")
print("\n(i) for any real process with stationary variance C(0): |C(π)| ≤ C(0), equality iff x(π) = -x(0) a.s. (Cauchy–Schwarz).")
print("    QM demands equality -> a continuous diffusion cannot do it; only the signed Wigner flow reproduces marginal AND C(t).")
