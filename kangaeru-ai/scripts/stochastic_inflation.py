# Stochastic inflation on the heat-kernel "CNN": depth = e-folds N (the RG clock ln a), kernel = (H/2pi)^2 diffusion.
# Flat-well benchmark: dphi/dN = -v + sigma*xi, absorbing end of inflation at phi = 0, start at phi0.
# Number of e-folds N to exit = first-passage time = curvature perturbation zeta = N - <N>.
# Exact: inverse-Gaussian pdf with mean phi0/v and exponential tail exp(-v^2 N / 2 sigma^2).
import numpy as np, math
rng = np.random.default_rng(3)
v, sigma, phi0 = 1.0, 1.0, 6.0                 # Peclet number phi0*v/sigma^2 = 6 (classical 6 e-folds)
dphi = 0.01; phis = np.arange(0, 25, dphi); dN = 0.2*dphi**2/sigma**2
rho = np.exp(-0.5*((phis-phi0)/0.03)**2); rho /= rho.sum()*dphi   # initial density
D = sigma**2/2; flux = []; Ns = []; N = 0.0
lap = np.array([1, -2, 1])/dphi**2; grad = np.array([1, 0, -1])/(2*dphi)   # the two kernels (np.convolve flips the kernel)
while N < 30:
    rho_p = np.pad(rho, 1); rho_p[0] = 0                          # absorbing boundary at phi=0 (end of inflation)
    rho = rho + dN*(D*np.convolve(rho_p, lap, 'valid') + v*np.convolve(rho_p, grad, 'valid'))
    rho[0] = 0; N += dN
    flux.append(D*rho[1]/dphi + v*rho[0]); Ns.append(N)          # probability flux out through phi=0 = P(N)
Ns = np.array(Ns); P_cnn = np.array(flux)
P_ex = phi0/np.sqrt(2*np.pi*sigma**2*Ns**3)*np.exp(-(phi0-v*Ns)**2/(2*sigma**2*Ns))   # inverse Gaussian
# Langevin walkers for a third opinion
M = 400000; phi = np.full(M, phi0); t = np.zeros(M); alive = np.ones(M, bool); dn = 1e-3; k = 0
while alive.any() and k*dn < 30:
    phi[alive] += -v*dn + sigma*np.sqrt(dn)*rng.standard_normal(alive.sum()); k += 1
    hit = alive & (phi <= 0); t[hit] = k*dn; alive &= ~hit
print(f"flat well: Peclet = {phi0*v/sigma**2:.0f}, classical <N> = {phi0/v:.1f}")
print(f"  <N>:  heat-CNN {np.trapezoid(Ns*P_cnn, Ns):.4f}   exact {phi0/v:.4f}   Langevin {t[t>0].mean():.4f}")
print(f"  normalisation of P(N) from CNN flux: {np.trapezoid(P_cnn, Ns):.5f}")
print(f"  {'N':>5}{'P_cnn':>12}{'P_exact':>12}{'Gaussian w/ same mean,var':>28}")
mu, var = phi0/v, phi0*sigma**2/v**3
for n in [3, 6, 9, 12, 16, 20, 25]:
    i = np.argmin(np.abs(Ns-n)); g = np.exp(-(n-mu)**2/(2*var))/np.sqrt(2*np.pi*var)
    print(f"  {n:>5}{P_cnn[i]:>12.3e}{P_ex[i]:>12.3e}{g:>28.3e}")
m = (Ns > 14) & (Ns < 28); slope = np.polyfit(Ns[m], np.log(P_cnn[m]), 1)[0]
print(f"  tail decay rate: CNN {-slope:.4f}   exact v^2/2sigma^2 = {v**2/(2*sigma**2):.4f}")
print(f"  P(N > 12) = P(zeta > 6): CNN {np.trapezoid(P_cnn[Ns>12], Ns[Ns>12]):.2e}   Gaussian {0.5*math.erfc((12-mu)/np.sqrt(2*var)):.2e}   exact {np.trapezoid(P_ex[Ns>12], Ns[Ns>12]):.2e}")
