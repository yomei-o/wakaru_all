# Check two small theorems from the map.
import numpy as np, torch
rng = np.random.default_rng(11); torch.manual_seed(11)
# (A) selection = ES + variance-seeking term:  sigma^2 grad ln E[e^{-bL}] = -b s^2 grad<L> + (b^2 s^2/2) grad Var[L] + O(b^3)
sig = 0.4; e = rng.standard_normal(2_000_000); L0 = lambda x: (x**2-1)**2
def stats(z):
    v = L0(z+sig*e); return v.mean(), v.var()
def num_grad(f, z, h=1e-3): return (f(z+h)-f(z-h))/(2*h)
print("(A) z=0.9, sigma=0.4: selection shift vs cumulant expansion")
print(f"{'beta':>6}{'selection':>12}{'1st (ES)':>11}{'1st+2nd':>10}")
for b in [0.1, 0.3, 1.0]:
    sel = sig**2*num_grad(lambda z: np.log(np.exp(-b*L0(z+sig*e)).mean()), 0.9)
    g1 = -b*sig**2*num_grad(lambda z: stats(z)[0], 0.9)
    g2 = b**2*sig**2/2*num_grad(lambda z: stats(z)[1], 0.9)
    print(f"{b:>6}{sel:>12.5f}{g1:>11.5f}{g1+g2:>10.5f}")
# (B) receptive-field variance of a random linear CNN = v * [L]_q, q = s^2  ([L]_q = (q^L-1)/(q-1))
def rf_var(L, s, H=1025, trials=6):
    out = []
    for _ in range(trials):
        layers = [torch.nn.Conv1d(1 if i == 0 else 8, 8, 3, stride=s, padding=1, bias=False) for i in range(L)]
        for c in layers: torch.nn.init.normal_(c.weight)
        x = torch.randn(1, 1, H, requires_grad=True); y = x
        for c in layers: y = c(y)
        k = y.shape[-1]//2; y[0, :, k].sum().backward()
        g2 = (x.grad[0, 0]**2).numpy(); g2 /= g2.sum(); i = np.arange(H)
        m = (g2*i).sum(); out.append((g2*(i-m)**2).sum())
    return np.mean(out)
v = 2/3                                    # per-layer variance of offsets {-1,0,1} with equal weight
print("(B) receptive-field variance (g^2-weighted) vs v*[L]_{s^2}")
print(f"{'s':>3}{'L':>4}{'measured':>11}{'v[L]_q':>10}")
for s in [1, 2]:
    for L in ([1, 4, 16, 64] if s == 1 else [1, 2, 4, 6]):
        q = s*s; pred = v*(L if q == 1 else (q**L-1)/(q-1))
        print(f"{s:>3}{L:>4}{rf_var(L, s):>11.2f}{pred:>10.2f}", flush=True)
