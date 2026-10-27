# E: Marshall sign × complex correction  ψ = marshall · exp(f + i g): give the approximate sign, let the network fix it.
import sys; sys.argv = ['x']
exec(open('nqs_sign.py', encoding='utf-8').read().split("print(f\"N={N}")[0])
def psi_E(f):
    o = f(X); return marshall*torch.exp(torch.complex(o[:, 0], o[:, 1]))
def train_E(Ht, steps=3000):
    f = F(out=2); opt = torch.optim.Adam(f.parameters(), 1e-2); best = np.inf
    for it in range(steps):
        psi = psi_E(f); Hpsi = torch.sparse.mm(Ht, psi.unsqueeze(1)).squeeze(1)
        E = (torch.conj(psi) @ Hpsi).real/(torch.conj(psi) @ psi).real
        opt.zero_grad(); E.backward(); opt.step(); best = min(best, E.item())
        if it == 1500:
            for g in opt.param_groups: g['lr'] = 3e-3
    return best
print(f"{'J2':>5}{'exact E0':>11}{'E Marshall×complex':>20}   (relative error)")
for J2 in [0.0, 0.8]:
    H = build_H(1.0, J2); E0 = spl.eigsh(H, k=1, which='SA')[0][0]
    Hc = H.tocoo(); Ht = torch.sparse_coo_tensor(np.vstack([Hc.row, Hc.col]), torch.tensor(Hc.data, dtype=torch.complex64), (M, M)).coalesce()
    print(f"{J2:>5}{E0:>11.5f}{(train_E(Ht)-E0)/abs(E0):>20.2e}", flush=True)
