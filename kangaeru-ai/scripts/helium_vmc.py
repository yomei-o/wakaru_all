# Line 5: learned network as a wavefunction. Helium ground state by variational Monte Carlo.
# psi = exp(-Z r1 - Z r2 + r12/(2(1+b r12)) + NN(r1,r2,r12) symmetrised). Exact E0 = -2.903724, HF = -2.8617
# Note: the VMC gradient 2<(E_L - <E_L>) dlnpsi> is a covariance -- the same form as Price / ES.
import torch, math, time
dev = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(0); torch.set_default_dtype(torch.float64)
class Psi(torch.nn.Module):
    def __init__(s):
        super().__init__()
        s.Z = torch.nn.Parameter(torch.tensor(2.0)); s.b = torch.nn.Parameter(torch.tensor(0.5))
        s.nn = torch.nn.Sequential(torch.nn.Linear(3,32), torch.nn.Tanh(), torch.nn.Linear(32,32), torch.nn.Tanh(), torch.nn.Linear(32,1))
        with torch.no_grad(): s.nn[-1].weight.mul_(0.01); s.nn[-1].bias.zero_()
    def logpsi(s, x):                       # x: (B,6)
        r1 = x[:,:3].norm(dim=1); r2 = x[:,3:].norm(dim=1); r12 = (x[:,:3]-x[:,3:]).norm(dim=1)
        f = lambda a, c: s.nn(torch.stack([a, c, r12], 1)/2.0)[:,0]
        J = 0.5*(f(r1, r2) + f(r2, r1)) * torch.exp(-0.1*(r1+r2))   # exchange-symmetric, decays at large r
        return -s.Z.abs()*(r1+r2) + r12/(2*(1+s.b.abs()*r12)) + J
def local_energy(m, x):
    x = x.detach().requires_grad_(True); lp = m.logpsi(x)
    g = torch.autograd.grad(lp.sum(), x, create_graph=True)[0]
    lap = sum(torch.autograd.grad(g[:,i].sum(), x, retain_graph=True)[0][:,i] for i in range(6))
    r1 = x[:,:3].norm(dim=1); r2 = x[:,3:].norm(dim=1); r12 = (x[:,:3]-x[:,3:]).norm(dim=1)
    return (-0.5*(lap + (g**2).sum(1)) - 2/r1 - 2/r2 + 1/r12).detach()
m = Psi().to(dev); opt = torch.optim.Adam(m.parameters(), 3e-3)
W = 4096; x = torch.randn(W, 6, device=dev)
def mcmc(x, n, step=0.4):
    with torch.no_grad():
        lp = m.logpsi(x)
        for _ in range(n):
            y = x + step*torch.randn_like(x); ly = m.logpsi(y)
            acc = torch.rand(W, device=dev).log() < 2*(ly-lp)
            x = torch.where(acc[:,None], y, x); lp = torch.where(acc, ly, lp)
    return x
x = mcmc(x, 500); t0 = time.time()
for it in range(1, 3001):
    x = mcmc(x, 10); EL = local_energy(m, x)
    EL = EL.clamp(EL.median()-5*(EL-EL.median()).abs().mean(), EL.median()+5*(EL-EL.median()).abs().mean())
    loss = 2*((EL - EL.mean()) * m.logpsi(x)).mean()           # covariance form
    opt.zero_grad(); loss.backward(); opt.step()
    if it in (1, 100, 300, 1000, 2000, 3000): print(f"iter {it:5d}  E = {EL.mean().item():.5f}   ({time.time()-t0:.0f}s)", flush=True)
for g in opt.param_groups: g['lr'] = 0
Es = []
for _ in range(400):
    x = mcmc(x, 10); Es.append(local_energy(m, x).mean().item())
Es = torch.tensor(Es); print(f"final E = {Es.mean():.5f} ± {Es.std()/math.sqrt(len(Es))*2:.5f}  (exact -2.903724, HF -2.86168; Z_eff={m.Z.abs().item():.3f})")
# baseline: same ansatz without NN (Z, b only) would be the Hylleraas-like 2-parameter form
