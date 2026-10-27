# Does a learned sign structure generalise?  Train a translation-invariant (circular CNN) NQS on N=12 (full state),
# then apply the SAME network to N=16 and compare with exact: overlap, and amplitude-weighted sign agreement.
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl, torch, itertools
torch.manual_seed(0)
def sector(N):
    st = np.array([s for s in itertools.product([0, 1], repeat=N) if sum(s) == N//2], dtype=np.int8)
    return st, {tuple(s): i for i, s in enumerate(st)}
def build_H(N, states, idx, J1, J2):
    rows, cols, vals = [], [], []
    for i, s in enumerate(states):
        diag = 0.0
        for d, J in ((1, J1), (2, J2)):
            if J == 0: continue
            for a in range(N):
                b = (a+d) % N
                if s[a] == s[b]: diag += J/4
                else:
                    diag -= J/4; t = s.copy(); t[a], t[b] = s[b], s[a]; rows.append(i); cols.append(idx[tuple(t)]); vals.append(J/2)
        rows.append(i); cols.append(i); vals.append(diag)
    return sp.csr_matrix((vals, (rows, cols)), shape=(len(states), len(states)))
class CNN(torch.nn.Module):                       # circular conv, translation invariant, works for any N
    def __init__(s, ch=8):
        super().__init__(); s.c1 = torch.nn.Conv1d(2, ch, 3, padding=1, padding_mode='circular'); s.c2 = torch.nn.Conv1d(ch, ch, 3, padding=1, padding_mode='circular'); s.out = torch.nn.Linear(ch, 2)
    def forward(s, x):                             # x: (B, N) ±1
        sub = torch.tensor([(-1.0)**i for i in range(x.shape[1])]).expand(x.shape[0], -1)      # sublattice label channel
        h = torch.tanh(s.c1(torch.stack([x, sub], 1))); h = torch.tanh(s.c2(h)); return s.out(h.sum(2))   # sum (not mean): phases add
def psi(net, X): o = net(X); return torch.exp(torch.complex(o[:, 0], o[:, 1]))
def exact(N, J2):
    st, idx = sector(N); H = build_H(N, st, idx, 1.0, J2); E0, v = spl.eigsh(H, k=1, which='SA'); v = v[:, 0]; v *= np.sign(v[np.argmax(np.abs(v))])
    return st, H, E0[0], v
def to_torch(H): Hc = H.tocoo(); return torch.sparse_coo_tensor(np.vstack([Hc.row, Hc.col]), torch.tensor(Hc.data, dtype=torch.complex64), H.shape).coalesce()
def metrics(net, st, v):
    with torch.no_grad(): p = psi(net, torch.tensor(2.0*st-1.0, dtype=torch.float32)).numpy()
    p /= np.linalg.norm(p); ov = abs(np.vdot(v, p))**2
    ph = np.exp(-1j*np.angle(np.vdot(v, p)))                            # align global phase
    sgn = np.sign((p*ph).real); sign_acc = np.sum(np.abs(v)**2*(sgn == np.sign(v)))   # amplitude-weighted sign agreement
    return ov, sign_acc
print('input channels: spin and sublattice label (-1)^i; phase = sum of local terms')
print(f"{'J2':>5}{'train N':>8}{'E err (train)':>14}{'overlap N=12':>13}{'sign acc N=12':>14}{'overlap N=16':>13}{'sign acc N=16':>14}{'E err N=16':>12}{'overlap N=20':>13}{'sign acc N=20':>14}{'E err N=20':>12}")
for J2 in [0.0, 0.8]:
    st12, H12, E12, v12 = exact(12, J2); st16, H16, E16, v16 = exact(16, J2); Ht = to_torch(H12)
    X12 = torch.tensor(2.0*st12-1.0, dtype=torch.float32); net = CNN(); opt = torch.optim.Adam(net.parameters(), 1e-2)
    for it in range(4000):
        p = psi(net, X12); Hp = torch.sparse.mm(Ht, p.unsqueeze(1)).squeeze(1); E = (torch.conj(p) @ Hp).real/(torch.conj(p) @ p).real
        opt.zero_grad(); E.backward(); opt.step()
        if it == 2000:
            for g in opt.param_groups: g['lr'] = 3e-3
    torch.save(net.state_dict(), f'nqs_transfer_J2_{J2}.pt')
    ov12, sa12 = metrics(net, st12, v12); ov16, sa16 = metrics(net, st16, v16)
    st20, H20, E20, v20 = exact(20, J2); ov20, sa20 = metrics(net, st20, v20)
    with torch.no_grad():
        p20 = psi(net, torch.tensor(2.0*st20-1.0, dtype=torch.float32)); Ht20 = to_torch(H20)
        E20n = ((torch.conj(p20) @ torch.sparse.mm(Ht20, p20.unsqueeze(1)).squeeze(1)).real/(torch.conj(p20) @ p20).real).item()
    with torch.no_grad():
        p16 = psi(net, torch.tensor(2.0*st16-1.0, dtype=torch.float32)); Ht16 = to_torch(H16)
        E16n = ((torch.conj(p16) @ torch.sparse.mm(Ht16, p16.unsqueeze(1)).squeeze(1)).real/(torch.conj(p16) @ p16).real).item()
    print(f"{J2:>5}{12:>8}{(E.item()-E12)/abs(E12):>14.2e}{ov12:>13.4f}{sa12:>14.4f}{ov16:>13.4f}{sa16:>14.4f}{(E16n-E16)/abs(E16):>12.2e}{ov20:>13.4f}{sa20:>14.4f}{(E20n-E20)/abs(E20):>12.2e}", flush=True)
print("  sign acc = amplitude-weighted fraction of basis states whose sign matches the exact ground state (random = 0.5).")
