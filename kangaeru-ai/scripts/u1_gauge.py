# Line 4: 2D U(1) lattice gauge theory. (a) MC vs exact Wilson loops (area law = confinement)
# (b) plain CNN vs gauge-equivariant CNN learning the 2x2 Wilson loop; test under random gauge transforms.
import numpy as np, torch
from scipy.special import iv
rng = np.random.default_rng(7); torch.manual_seed(7)
L = 16; beta = 2.0
def plaq(th):        # th: (...,2,L,L) link angles; theta_P(x) = th1(x)+th2(x+e1)-th1(x+e2)-th2(x)
    t1, t2 = th[...,0,:,:], th[...,1,:,:]
    return t1 + np.roll(t2,-1,-2) - np.roll(t1,-1,-1) - t2
def sweep(th):
    for mu in (0,1):
        for parity in (0,1):
            prop = th.copy(); d = rng.uniform(-1.2,1.2,(L,L))
            mask = ((np.indices((L,L)).sum(0)) % 2 == parity)
            prop[mu] = np.where(mask, th[mu]+d, th[mu])
            # local action change: each link sits in 2 plaquettes; compute full delta (cheap at L=16)
            dS = -beta*(np.cos(plaq(prop)) - np.cos(plaq(th)))
            # attribute plaquette changes to the updated links: sum over the 2 plaquettes touching each link
            if mu == 0: dl = dS + np.roll(dS, 1, -1)       # plaquettes at x and x-e2
            else:       dl = dS + np.roll(dS, 1, -2)       # plaquettes at x and x-e1
            acc = mask & (rng.random((L,L)) < np.exp(-dl))
            th[mu] = np.where(acc, th[mu]+d, th[mu])
    return th
def wilson(th, R, T):
    tp = plaq(th); s = np.zeros_like(tp)
    for i in range(R):
        for j in range(T): s += np.roll(np.roll(tp,-i,-2),-j,-1)
    return np.cos(s).mean()
th = rng.uniform(-np.pi,np.pi,(2,L,L))
for _ in range(500): th = sweep(th)
confs = []
for k in range(3000*5):
    th = sweep(th)
    if k % 5 == 0: confs.append(th.copy())
confs = np.array(confs)
r = iv(1,beta)/iv(0,beta)
print(f"(a) beta={beta}: exact I1/I0 = {r:.4f}, string tension -ln(I1/I0) = {-np.log(r):.4f}")
print("    loop   MC <W>           exact (I1/I0)^area")
for R,T in [(1,1),(1,2),(2,2),(2,3),(3,3)]:
    w = np.array([wilson(c,R,T) for c in confs[::3]])
    print(f"    {R}x{T}   {w.mean():.4f} ± {w.std()/np.sqrt(len(w)):.4f}   {r**(R*T):.4f}")
# (b) learning task: per-site 2x2 Wilson loop cos(sum of 4 plaquette angles)
def target(c):
    tp = plaq(c); s = tp + np.roll(tp,-1,-2) + np.roll(tp,-1,-1) + np.roll(np.roll(tp,-1,-2),-1,-1)
    return np.cos(s)
def gauge(c):        # random gauge transform: th_mu(x) -> th_mu(x) + a(x) - a(x+mu)
    a = rng.uniform(-np.pi,np.pi,(L,L)); c = c.copy()
    c[0] += a - np.roll(a,-1,-2); c[1] += a - np.roll(a,-1,-1); return c
def feats_plain(c):  # raw links
    return np.concatenate([np.cos(c), np.sin(c)], 0)
def feats_gauge(c):  # gauge-invariant building block: plaquette
    tp = plaq(c); return np.stack([np.cos(tp), np.sin(tp)], 0)
class Net(torch.nn.Module):
    def __init__(s, cin):
        super().__init__()
        s.f = torch.nn.Sequential(torch.nn.Conv2d(cin,64,3,padding=1,padding_mode='circular'), torch.nn.GELU(),
                                  torch.nn.Conv2d(64,64,3,padding=1,padding_mode='circular'), torch.nn.GELU(),
                                  torch.nn.Conv2d(64,64,3,padding=1,padding_mode='circular'), torch.nn.GELU(),
                                  torch.nn.Conv2d(64,1,1))
    def forward(s,x): return s.f(x)[:,0]
ntr = 2400; tr, te = confs[:ntr], confs[ntr:]
Ytr = torch.tensor(np.array([target(c) for c in tr]), dtype=torch.float32)
Yte = torch.tensor(np.array([target(c) for c in te]), dtype=torch.float32)
te_g = np.array([gauge(c) for c in te])
print("(b) predict per-site 2x2 Wilson loop.  target variance =", f"{Yte.var().item():.4f}")
for name, F in [("plain CNN (links)", feats_plain), ("gauge-equivariant (plaquettes)", feats_gauge)]:
    Xtr = torch.tensor(np.array([F(c) for c in tr]), dtype=torch.float32)
    Xte = torch.tensor(np.array([F(c) for c in te]), dtype=torch.float32)
    Xg  = torch.tensor(np.array([F(c) for c in te_g]), dtype=torch.float32)
    net = Net(Xtr.shape[1]); opt = torch.optim.Adam(net.parameters(), 2e-3)
    for ep in range(60):
        perm = torch.randperm(ntr)
        for i in range(0, ntr, 64):
            b = perm[i:i+64]; loss = ((net(Xtr[b])-Ytr[b])**2).mean()
            opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        m1 = ((net(Xte)-Yte)**2).mean().item(); m2 = ((net(Xg)-Yte)**2).mean().item()
    print(f"    {name:32s} test MSE {m1:.4f}   after gauge transform {m2:.4f}")
