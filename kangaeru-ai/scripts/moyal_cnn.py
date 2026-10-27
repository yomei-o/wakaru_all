# Where does negative probability come from?  Moyal equation for W(x,p) in V = x²/2 + g x⁴ (exact for quartic):
#   ∂W/∂t = -p ∂x W + V'(x) ∂p W - (ħ²/24) V'''(x) ∂p³ W          (ħ = 1)
# Liouville = the same without the ħ² term (classical flow, preserves positivity).  The ħ² term = conv kernel [-1,3,-3,1]/dp³.
# Compare <x>(t) against exact Schrödinger (split-operator) from a coherent state; track min W.
import numpy as np
g = 0.1; x0 = 1.5
# --- exact QM: split operator ---
Nx = 2048; Lx = 16; x = np.linspace(-Lx/2, Lx/2, Nx, endpoint=False); dx = x[1]-x[0]; k = 2*np.pi*np.fft.fftfreq(Nx, dx)
V = x**2/2 + g*x**4; dt = 2e-3
psi = np.pi**-0.25*np.exp(-(x-x0)**2/2).astype(complex)
# --- phase space grid ---
N = 160; L = 10.0; q = np.linspace(-L/2, L/2, N, endpoint=False); dq = q[1]-q[0]; X, P = np.meshgrid(q, q, indexing='ij')
kx = 2*np.pi*np.fft.fftfreq(N, dq); kp = 2*np.pi*np.fft.fftfreq(N, dq)
W0 = np.exp(-(X-x0)**2 - P**2)/np.pi                                   # coherent state Wigner function (ħ=1)
Vp = X + 4*g*X**3; Vppp = 24*g*X
# split-operator for the Moyal equation (exact phases: the p-derivative terms are multiplications in (x,kp), the x-advection in (kx,p))
def step(W, quantum, h):
    ph = np.exp(1j*h/2*(Vp*kp[None, :] + (Vppp*kp[None, :]**3/24 if quantum else 0.0)))   # Vp, Vppp are (N,N) grids
    Wk = np.fft.fft(W, axis=1)*ph; W = np.real(np.fft.ifft(Wk, axis=1))
    Wk = np.fft.fft(W, axis=0)*np.exp(-1j*h*P*kx[:, None]); W = np.real(np.fft.ifft(Wk, axis=0))
    Wk = np.fft.fft(W, axis=1)*ph; return np.real(np.fft.ifft(Wk, axis=1))
Wc, Wq = W0.copy(), W0.copy()
print(f"V = x²/2 + {g} x⁴, coherent state at x0={x0}.  Kernel of the ħ² term: third p-derivative.")
print(f"{'t':>5}{'<x> QM':>10}{'<x> Moyal':>11}{'<x> Liouville':>14}{'min W Moyal':>13}{'min W Liouv':>13}")
T = 24.0; steps = int(T/dt); every = int(2.0/dt)
expV = np.exp(-0.5j*V*dt); expT = np.exp(-0.5j*k**2*dt)
for s in range(steps+1):
    t = s*dt
    if s % every == 0:
        xq = np.sum(np.abs(psi)**2*x)*dx
        print(f"{t:>5.1f}{xq:>10.4f}{np.sum(Wq*X)*dq*dq:>11.4f}{np.sum(Wc*X)*dq*dq:>14.4f}{Wq.min():>13.4f}{Wc.min():>13.4f}", flush=True)
    psi = expV*np.fft.ifft(expT*np.fft.fft(expV*psi))
    Wq = step(Wq, True, dt); Wc = step(Wc, False, dt)
print("  Liouville keeps W ≥ 0 and loses the quantum revivals; the single ħ² layer makes W negative and restores <x>(t).")
