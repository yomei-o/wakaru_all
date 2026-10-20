# 線の地図 05: five numeric checks on "LLM = physics" lines.
# 1 softmax: Jacobian = covariance, FDT by sampling   2 attention = Hopfield update (energy monotone, T melts memory)
# 3 tokens cluster with depth (depth = time, beta = 1/T)  4 in-context learning = one GD step (exact + trained)
# 5 backprop = adjoint, Hamiltonian H = a.f conserved along forward/backward pair
import numpy as np, torch
torch.set_default_dtype(torch.float64); rng = np.random.default_rng(5); torch.manual_seed(5)
def softmax(h): e = np.exp(h - h.max(-1, keepdims=True)); return e/e.sum(-1, keepdims=True)

print("=== 1. softmax: 逆伝播の信号 = ゆらぎ（揺動散逸） ===")
h = rng.standard_normal(8); p = softmax(h)
J = np.array([(softmax(h + 1e-6*np.eye(8)[j]) - softmax(h - 1e-6*np.eye(8)[j]))/2e-6 for j in range(8)]).T
print(f"  max|dp_i/dh_j - (p_i d_ij - p_i p_j)| = {np.abs(J - (np.diag(p) - np.outer(p, p))).max():.1e}")
f = rng.standard_normal(8)                                 # observable f(token)
for T in [1.0, 0.5]:
    pT = softmax(h/T); M = 2_000_000; s = rng.choice(8, M, p=pT)
    onehot = np.eye(8)[s]; cov = ((f[s] - f[s].mean())[:, None]*(onehot - onehot.mean(0))).mean(0)   # Cov(f, 1_j) from samples
    resp = np.array([(f @ softmax((h + 1e-4*np.eye(8)[j])/T) - f @ softmax((h - 1e-4*np.eye(8)[j])/T))/2e-4 for j in range(8)])
    print(f"  T={T}: response d<f>/dh_j vs Cov(f,1_j)/T from samples, max|diff| = {np.abs(resp - cov/T).max():.1e}  (|resp| up to {np.abs(resp).max():.3f})")

print("\n=== 2. attention 1 回 = 現代ホップフィールドの 1 更新（エネルギー単調減少、温度で記憶が溶ける） ===")
d, Np = 64, 20
X = rng.choice([-1.0, 1.0], (Np, d))/np.sqrt(d)            # stored patterns (keys = values), unit norm
def energy(xi, b):
    z = b*X@xi; return -np.log(np.exp(z - z.max()).sum())/b - z.max()/b + 0.5*xi@xi
def update(xi, b): return X.T @ softmax(b*X@xi)            # = attention(q=xi, K=V=X)
print(f"  {'beta':>6}{'steps':>7}{'E monotone':>12}{'overlap w/ nearest':>20}{'#distinct fixed pts (200 starts)':>34}")
for b in [1, 4, 16, 64]:
    fps = []; mono = True; steps = []; ov = []
    for _ in range(200):
        xi = rng.standard_normal(d)/np.sqrt(d); E = energy(xi, b)
        for k in range(1, 500):
            xi2 = update(xi, b); E2 = energy(xi2, b)
            if E2 > E + 1e-12: mono = False
            done = np.linalg.norm(xi2 - xi) < 1e-9; xi, E = xi2, E2
            if done: break
        steps.append(k); ov.append(np.max(X@xi)/(np.linalg.norm(xi)/np.sqrt(d)*d/np.sqrt(d))); fps.append(tuple(np.round(xi, 4)))
    print(f"  {b:>6}{np.mean(steps):>7.1f}{str(mono):>12}{np.mean(ov):>20.3f}{len(set(fps)):>34}")

print("\n=== 3. 層を重ねるとトークンが凝集する（深さ = 時間、β = 1/T） ===")
n, dd = 64, 16
def clusters(Xt, thr=0.99):
    C = Xt@Xt.T; seen = np.zeros(n, bool); c = 0
    for i in range(n):
        if not seen[i]: c += 1; seen |= C[i] > thr
    return c
X0 = rng.standard_normal((n, dd)); X0 /= np.linalg.norm(X0, axis=1, keepdims=True)
layers = [0, 5, 10, 20, 50, 100, 200, 500]
print(f"  {'beta':>6}" + "".join(f"{'L='+str(L):>8}" for L in layers))
for b in [1, 4, 9]:
    Xt = X0.copy(); out = []
    for L in range(max(layers)+1):
        if L in layers: out.append(clusters(Xt))
        A = softmax(b*Xt@Xt.T); Xt = Xt + 0.1*A@Xt; Xt /= np.linalg.norm(Xt, axis=1, keepdims=True)
    print(f"  {b:>6}" + "".join(f"{c:>8d}" for c in out))

print("\n=== 4. 文脈内学習 = 勾配降下 1 歩（線形 attention、構成で厳密 ／ 学習でも） ===")
dx, nc = 4, 16
def task(B):
    W = rng.standard_normal((B, 1, dx)); x = rng.standard_normal((B, nc+1, dx)); y = (x*W).sum(-1, keepdims=True)
    y_in = y.copy(); y_in[:, -1] = 0; return x, y_in, y[:, -1, 0]
x, y_in, yq = task(5); eta = 1/nc
gd = eta*np.einsum('bjd,bj->bd', x[:, :-1], y_in[:, :-1, 0]); pred_gd = (gd*x[:, -1]).sum(-1)       # one GD step from W=0
attn = eta*np.einsum('bd,bjd,bj->b', x[:, -1], x[:, :-1], y_in[:, :-1, 0])                              # linear attention q.k v
print(f"  construction: max|attention - GD step| = {np.abs(attn - pred_gd).max():.1e}")
class LinAttn(torch.nn.Module):
    def __init__(s): super().__init__(); D = dx+1; s.Wq = torch.nn.Linear(D, D, bias=False); s.Wk = torch.nn.Linear(D, D, bias=False); s.Wv = torch.nn.Linear(D, D, bias=False); s.P = torch.nn.Linear(D, 1, bias=False)
    def forward(s, tok):                      # tok: (B, nc+1, dx+1); query is last; linear attention over context
        q = s.Wq(tok[:, -1:]); k = s.Wk(tok[:, :-1]); v = s.Wv(tok[:, :-1])
        return s.P((q @ k.transpose(1, 2)) @ v)[:, 0, 0]
net = LinAttn(); opt = torch.optim.Adam(net.parameters(), 3e-3)
for it in range(6000):
    x, y_in, yq = task(256); tok = torch.tensor(np.concatenate([x, y_in], -1))
    loss = ((net(tok) - torch.tensor(yq))**2).mean(); opt.zero_grad(); loss.backward(); opt.step()
x, y_in, yq = task(20000); tok = torch.tensor(np.concatenate([x, y_in], -1))
with torch.no_grad(): mse_net = ((net(tok) - torch.tensor(yq))**2).mean().item()
best = None
for e in np.linspace(0.02, 0.12, 51):
    p = e*np.einsum('bd,bjd,bj->b', x[:, -1], x[:, :-1], y_in[:, :-1, 0]); m = ((p - yq)**2).mean()
    if best is None or m < best[1]: best = (e, m)
ls = np.array([np.linalg.lstsq(x[b, :-1], y_in[b, :-1, 0], rcond=None)[0] @ x[b, -1] for b in range(20000)])
print(f"  test MSE: trained linear attention {mse_net:.4f} | best 1-step GD (eta={best[0]:.3f}) {best[1]:.4f} | least squares {((ls-yq)**2).mean():.4f} | predict 0: {np.var(yq):.3f}")

print("\n=== 5. 逆伝播 = 随伴方程式（時間反転）、H = a·f は保存 ===")
W = torch.randn(4, 4)*0.8; bb = torch.randn(4); x0 = torch.randn(4); tgt = torch.randn(4); Tend = 2.0
f = lambda x: torch.tanh(W@x + bb)
def rk4(g, y, h):
    k1 = g(y); k2 = g(y + h/2*k1); k3 = g(y + h/2*k2); k4 = g(y + h*k3); return y + h/6*(k1 + 2*k2 + 2*k3 + k4)
n = 2000; h = Tend/n; xs = [x0]
for _ in range(n): xs.append(rk4(f, xs[-1], h))
a = xs[-1] - tgt; Hs = []
for i in range(n, -1, -1):
    x = xs[i].clone().requires_grad_(True)
    if i % 400 == 0: Hs.append((a @ f(x)).item())
    if i == 0: break
    Jt = torch.autograd.functional.jacobian(f, x)
    a = rk4(lambda aa: Jt.T@aa, a, h)          # adjoint da/dt=-J^T a, stepped backward in time (J frozen over the small step)
print("  H = a.f along the backward pass (t = 2.0 -> 0):", " ".join(f"{v:.6f}" for v in Hs))
# gradient wrt W: autograd through the discrete forward vs adjoint integral
Wg = W.clone().requires_grad_(True); x = x0
for _ in range(n): x = rk4(lambda z: torch.tanh(Wg@z + bb), x, h)
gW = torch.autograd.grad(0.5*((x - tgt)**2).sum(), Wg)[0]
a = xs[-1] - tgt; G = torch.zeros(4, 4)
for i in range(n, 0, -1):
    x = xs[i]; s = 1 - torch.tanh(W@x + bb)**2; G += h*torch.outer(a*s, x)
    Jt = torch.autograd.functional.jacobian(f, x); a = rk4(lambda aa: Jt.T@aa, a, h)
print(f"  dL/dW: autograd through 2000 RK4 steps vs adjoint integral, rel diff = {((gW - G).norm()/gW.norm()).item():.1e}")
