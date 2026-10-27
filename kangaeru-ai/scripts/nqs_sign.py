# Can a learned network carry the sign?  J1-J2 Heisenberg chain, N=16, Sz=0 sector (12870 states), periodic.
# Energy minimised EXACTLY on the full state vector (no sampling): isolates representability/learnability of signs.
#  A: positive  ψ = exp(f(s))             B: Marshall sign × exp(f(s))     (sign given, like fixed-node)
#  C: real, sign free  ψ = f(s)           D: complex  ψ = exp(f(s) + i g(s))
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl, torch, itertools, time
torch.manual_seed(0); N = 16
states = np.array([s for s in itertools.product([0, 1], repeat=N) if sum(s) == N//2], dtype=np.int8)   # 1 = up
idx = {tuple(s): i for i, s in enumerate(states)}; M = len(states)
def build_H(J1, J2):
    rows, cols, vals = [], [], []
    for i, s in enumerate(states):
        diag = 0.0
        for d, J in ((1, J1), (2, J2)):
            if J == 0: continue
            for a in range(N):
                b = (a+d) % N
                if s[a] == s[b]: diag += J/4
                else:
                    diag -= J/4; t = s.copy(); t[a], t[b] = s[b], s[a]
                    rows.append(i); cols.append(idx[tuple(t)]); vals.append(J/2)
        rows.append(i); cols.append(i); vals.append(diag)
    return sp.csr_matrix((vals, (rows, cols)), shape=(M, M))
X = torch.tensor(2.0*states - 1.0, dtype=torch.float32)            # ±1 inputs
A_mask = torch.tensor([(1 if (j % 2 == 0) else 0) for j in range(N)], dtype=torch.float32)
marshall = torch.tensor([(-1.0)**int(((states[i] == 1) & (np.arange(N) % 2 == 0)).sum()) for i in range(M)])
class F(torch.nn.Module):
    def __init__(s, out=1, h=24):
        super().__init__(); s.net = torch.nn.Sequential(torch.nn.Linear(N, h), torch.nn.Tanh(), torch.nn.Linear(h, h), torch.nn.Tanh(), torch.nn.Linear(h, out))
    def forward(s, x): return s.net(x)
def psi_of(kind, f):
    o = f(X)
    if kind == 'A': return torch.exp(o[:, 0]).to(torch.complex64)
    if kind == 'B': return (marshall*torch.exp(o[:, 0])).to(torch.complex64)
    if kind == 'C': return o[:, 0].to(torch.complex64)
    if kind == 'D': return torch.exp(torch.complex(o[:, 0], o[:, 1]))
def train(kind, Ht, steps=3000):
    f = F(out=2 if kind == 'D' else 1); opt = torch.optim.Adam(f.parameters(), 1e-2)
    best = np.inf
    for it in range(steps):
        psi = psi_of(kind, f); Hpsi = torch.sparse.mm(Ht, psi.unsqueeze(1)).squeeze(1)
        E = (torch.conj(psi) @ Hpsi).real/(torch.conj(psi) @ psi).real
        opt.zero_grad(); E.backward(); opt.step(); best = min(best, E.item())
        if it == 1500:
            for g in opt.param_groups: g['lr'] = 3e-3
    return best
print(f"N={N}, Sz=0 sector {M} states, network params = {sum(p.numel() for p in F().parameters())} (<< {M})")
print(f"{'J2':>5}{'exact E0':>11}{'A positive':>12}{'B Marshall×pos':>16}{'C sign-free':>13}{'D complex':>12}   (relative errors)")
for J2 in [0.0, 0.5, 0.8]:
    H = build_H(1.0, J2); E0 = spl.eigsh(H, k=1, which='SA')[0][0]
    Hc = H.tocoo(); Ht = torch.sparse_coo_tensor(np.vstack([Hc.row, Hc.col]), torch.tensor(Hc.data, dtype=torch.complex64), (M, M)).coalesce()
    res = {k: train(k, Ht) for k in 'ABCD'}
    print(f"{J2:>5}{E0:>11.5f}" + "".join(f"{(res[k]-E0)/abs(E0):>{w}.2e}" for k, w in zip('ABCD', (12, 16, 13, 12))), flush=True)
