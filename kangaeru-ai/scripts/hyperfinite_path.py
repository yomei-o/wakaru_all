# D. The path integral as a hyperfinite product: Euclidean propagator of the harmonic oscillator (hbar = m = omega = 1)
#    K_N = (K_eps)^N with eps = T/N, K_eps(x,y) = (2π eps)^{-1/2} exp(-(x-y)²/(2 eps) - eps (V(x)+V(y))/2).
#    Standard part (N -> ∞) should be the Mehler kernel; ground-state energy from the trace.
import numpy as np
T = 2.0; L = 8.0; n = 1601; x = np.linspace(-L, L, n); dx = x[1]-x[0]; V = 0.5*x**2
def mehler(x, y, T):
    s, c = np.sinh(T), np.cosh(T); return np.exp(-((x**2+y**2)*c - 2*x*y)/(2*s))/np.sqrt(2*np.pi*s)
X, Y = np.meshgrid(x, x, indexing='ij'); K_exact = mehler(X, Y, T)
print(f"{'N slices':>9}{'eps':>8}{'max|K_N - Mehler|':>20}{'K_N(0,0)':>12}{'E0 from trace':>15}")
for N in [4, 16, 64, 256, 1024]:
    eps = T/N
    K = np.exp(-(X-Y)**2/(2*eps) - eps*(V[:, None]+V[None, :])/2)/np.sqrt(2*np.pi*eps)*dx
    M = np.eye(n)
    # fast power by repeated squaring
    P, e = K.copy(), N
    while e:
        if e & 1: M = M @ P
        P = P @ P; e >>= 1
    KN = M/dx
    tr = np.trace(M)                                   # Z(T) = Σ_n e^{-E_n T}; E0 ≈ -ln Z / T for large T (correction e^{-T})
    E0 = -np.log(tr)/T
    print(f"{N:>9}{eps:>8.4f}{np.abs(KN-K_exact).max():>20.2e}{KN[n//2, n//2]:>12.6f}{E0:>15.5f}")
print(f"  exact: K(0,0;T)={mehler(0,0,T):.6f},  -ln Z(T)/T with Z = 1/(2 sinh(T/2)) = {-np.log(1/(2*np.sinh(T/2)))/T:.5f}  (E0 = 0.5 only as T -> ∞)")
