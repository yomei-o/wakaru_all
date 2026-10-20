# Molecular vibrational spectrum (Morse diatomic) computed by a stack of conv layers.
# One layer = one imaginary-time step: psi <- psi - dtau*(conv(psi, laplacian kernel) + V*psi).
# Depth = imaginary time; channels = states (kept orthogonal). hbar = m = 1.
import torch, numpy as np
torch.set_default_dtype(torch.float64)
D, a, x0 = 20.0, 1.0, 0.0
w0 = a*np.sqrt(2*D)
exact = [w0*(n+.5) - (w0*(n+.5))**2/(4*D) for n in range(5)]
dx = 0.01; x = torch.arange(-2.5, 9.0, dx); V = D*(1-torch.exp(-a*(x-x0)))**2
lap = torch.nn.Conv1d(1, 1, 3, padding=1, bias=False)
with torch.no_grad(): lap.weight[:] = torch.tensor([[[-0.5, 1.0, -0.5]]])/dx**2   # -1/2 d2/dx2
H = lambda psi: lap(psi) + V*psi
K = 5; psi = torch.randn(K, 1, x.numel()); dtau = 0.4*dx**2
def orth(p):                                   # Gram-Schmidt across channels
    q = p.squeeze(1).T; q, _ = torch.linalg.qr(q); return q.T.unsqueeze(1)
psi = orth(psi)
print(f"omega0={w0:.4f}  exact Morse levels: " + "  ".join(f"{e:.4f}" for e in exact))
print(f"{'depth':>8}{'imag time':>11}  " + "  ".join(f"E{n:<7}" for n in range(K)))
with torch.no_grad():
    for layer in range(1, 200001):
        psi = psi - dtau*H(psi)
        if layer % 50 == 0: psi = orth(psi)
        if layer in (1000, 5000, 20000, 50000, 100000, 200000):
            psi = orth(psi)
            E = [(p*H(p)).sum().item()/(p*p).sum().item() for p in psi.split(1)]
            print(f"{layer:>8}{layer*dtau:>11.3f}  " + "  ".join(f"{e:<8.4f}" for e in E), flush=True)
