# Lines 2+3: hydrogen spectrum from a deep 3D CNN (imaginary-time layers), then classify each level
# by the irreps of the cubic group O_h (the symmetry of the conv grid). Expect 3d -> e_g + t_2g.
import torch, numpy as np, sys, time
dev = 'cuda' if torch.cuda.is_available() else 'cpu'
N = int(sys.argv[1]) if len(sys.argv) > 1 else 160; h = float(sys.argv[2]) if len(sys.argv) > 2 else 0.4
K = 15; steps = int(sys.argv[3]) if len(sys.argv) > 3 else 20000; dt = float(sys.argv[4]) if len(sys.argv) > 4 else 0.04
c = (torch.arange(N, device=dev) - (N-1)/2)*h            # nucleus at a cube centre -> exact O_h about origin
X, Y, Z = torch.meshgrid(c, c, c, indexing='ij'); R = torch.sqrt(X**2+Y**2+Z**2)
V = (-1.0/R).float()
kern = torch.zeros(1,1,3,3,3, device=dev)
kern[0,0,1,1,1] = 6.0
for (i,j,k) in [(0,1,1),(2,1,1),(1,0,1),(1,2,1),(1,1,0),(1,1,2)]: kern[0,0,i,j,k] = -1.0
kern *= 0.5/h**2                                        # -1/2 Laplacian as a conv kernel
def H(p): return torch.nn.functional.conv3d(p, kern, padding=1) + V*p
def orth(p):
    q = p.reshape(K, -1).T.double(); q, _ = torch.linalg.qr(q); return q.T.reshape(K,1,N,N,N).float()
torch.manual_seed(0)
psi = orth(torch.randn(K,1,N,N,N, device=dev))
t0 = time.time()
with torch.no_grad():
    for s in range(1, steps+1):
        psi = psi - dt*H(psi)
        if s % 25 == 0: psi = orth(psi)
        if s % 5000 == 0 or s == steps:
            # Rayleigh-Ritz in the current subspace
            Hp = H(psi); A = (psi.reshape(K,-1).double() @ Hp.reshape(K,-1).double().T)
            e, U = torch.linalg.eigh((A+A.T)/2)
            print(f"layer {s:6d}  tau={s*dt:7.1f}  E: " + " ".join(f"{v:.5f}" for v in e.tolist()) + f"   ({time.time()-t0:.0f}s)", flush=True)
    psi = (U.T.float() @ psi.reshape(K,-1)).reshape(K,1,N,N,N)
E = e.cpu().numpy()
# symmetry operations on the grid (all map grid->grid exactly)
ops = {
 'C4z': lambda p: torch.rot90(p, 1, dims=(2,3)),
 'C3' : lambda p: p.permute(0,1,4,2,3),              # (x,y,z)->(z,x,y) cyclic
 'C2z': lambda p: torch.rot90(p, 2, dims=(2,3)),
 'i'  : lambda p: torch.flip(p, dims=(2,3,4)),
}
table = {'A1g':(1,1,1,1,1),'A2u':(1,-1,1,1,-1),'Eg':(2,0,-1,2,2),'T1u':(3,1,0,-1,-3),'T2g':(3,-1,0,-1,3),
         'T1g':(3,1,0,-1,3),'T2u':(3,-1,0,-1,-3),'Eu':(2,0,-1,2,-2),'A1u':(1,1,1,1,-1),'A2g':(1,-1,1,1,1)}
# cluster levels
order = np.argsort(E); groups = []; cur = [order[0]]
for a_, b_ in zip(order[:-1], order[1:]):
    if E[b_]-E[a_] < 1e-5: cur.append(b_)
    else: groups.append(cur); cur = [b_]
groups.append(cur)
print("\nlevel   E (hartree)    exact -1/2n^2   deg   characters (E,C4z,C3,C2z,i)   O_h irrep")
for g in groups:
    P = psi[g].reshape(len(g), -1).double()
    chi = [len(g)] + [float(sum((P[j] @ op(psi[g][j:j+1]).reshape(-1).double()).item() for j in range(len(g)))) for op in ops.values()]
    name = min(table, key=lambda k: sum((x-y)**2 for x, y in zip(chi, table[k])))
    n = round(1/np.sqrt(-2*np.mean(E[g]))) if np.mean(E[g]) < 0 else 0
    print(f"{np.mean(E[g]):12.6f}   {-0.5/n**2 if n else float('nan'):12.6f}   {len(g):3d}   " + " ".join(f"{x:5.2f}" for x in chi) + f"   {name}")
