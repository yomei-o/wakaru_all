# Line 1: a conv kernel's Fourier transform IS the dispersion relation.
# Same kernel, 1st-order time -> diffusion (x^2 ~ t), 2nd-order time -> waves (x ~ t, speed c from the kernel).
import numpy as np, torch
torch.set_default_dtype(torch.float64)
n = 4096; a = 1.0; Km = 1.0                       # spacing, K/m
kern = torch.tensor([[[1.0, -2.0, 1.0]]])*Km/a**2 # discrete Laplacian (circular)
def conv(u): return torch.nn.functional.conv1d(torch.nn.functional.pad(u,(1,1),mode='circular'), kern)
x = torch.arange(n)*a
# (a) monatomic chain: plane wave eigenvalue of kernel vs analytic omega^2 = 2K/m (1-cos ka)
print("(a) kernel acting on plane waves e^{ikx}: eigenvalue = -omega^2")
for k in [0.1, 0.5, 1.0, 2.0, np.pi]:
    kq = 2*np.pi*round(k*n/(2*np.pi))/n; u = torch.cos(kq*x).view(1,1,-1)
    lam = (conv(u)*u).sum()/(u*u).sum()
    print(f"   k={kq:.4f}  -lambda={-lam.item():.6f}   2(1-cos ka)={2*Km*(1-np.cos(kq*a)):.6f}")
c_pred = a*np.sqrt(Km); D_pred = 0.5                # c^2 = K a^2/m ; second moment of kernel / 2
# (b) wave equation u_tt = conv(u): packet speed
dt = 0.2; k0 = 0.3; w = 40.0
u0 = torch.exp(-((x-n/4)/w)**2)*torch.cos(k0*x); u = u0.view(1,1,-1).clone()
vg = a*np.sqrt(Km)*np.cos(k0*a/2)                  # d omega / dk
up = u.clone()
# start with a right-moving packet: u(-dt) = packet shifted by +vg*dt
up = (torch.exp(-((x+vg*dt-n/4)/w)**2)*torch.cos(k0*(x+vg*dt) - np.sqrt(2*(1-np.cos(k0)))*0)).view(1,1,-1)
T = 1500.0; steps = int(T/dt)
for _ in range(steps):
    un = 2*u - up + dt**2*conv(u); up, u = u, un
env = (u[0,0]**2).numpy(); pos = (env*x.numpy()).sum()/env.sum()
print(f"(b) wave eq: packet moved {pos-n/4:.1f} in t={T}:  speed {(pos-n/4)/T:.4f}   group velocity from kernel {vg:.4f}  (k->0 limit c = {c_pred:.4f})")
# (c) diffusion u_t = D conv(u): spread of a spike, x^2 = 2 D_eff t
u = torch.zeros(1,1,n); u[0,0,n//2] = 1.0; dt = 0.2; T = 2000.0
for _ in range(int(T/dt)): u = u + dt*conv(u)
p = u[0,0].numpy(); xc = x.numpy()-n//2
print(f"(c) diffusion: <x^2>/(2t) = {(p*xc**2).sum()/p.sum()/(2*T):.4f}   kernel 2nd moment/2 = {(kern[0,0].numpy()*np.array([1,0,1])).sum()/2:.4f}")
# (d) diatomic chain = 2-channel conv: masses m1,m2 alternate. Fourier of 2x2 kernel -> acoustic + optical
m1, m2, K = 1.0, 3.0, 1.0
print("(d) two-channel kernel (diatomic chain): bands from the 2x2 Fourier matrix vs direct lattice diagonalization")
N = 64; M = np.zeros((2*N,2*N))
for i in range(2*N):
    mi = m1 if i%2==0 else m2
    M[i,i] = 2*K/mi; M[i,(i+1)%(2*N)] = -K/np.sqrt(mi*(m1 if (i+1)%2==0 else m2)); M[i,(i-1)%(2*N)] = -K/np.sqrt(mi*(m1 if (i-1)%2==0 else m2))
wl = np.sqrt(np.clip(np.linalg.eigvalsh(M),0,None))
def bands(q):   # q = k * (2a), unit cell 2a
    A = np.array([[2*K/m1, -K*(1+np.exp(-1j*q))/np.sqrt(m1*m2)],[-K*(1+np.exp(1j*q))/np.sqrt(m1*m2), 2*K/m2]])
    return np.sqrt(np.clip(np.linalg.eigvalsh(A),0,None))
qs = 2*np.pi*np.arange(N)/N; fb = np.sort(np.concatenate([bands(q) for q in qs]))
print(f"   max |direct - Fourier| over all {2*N} modes = {np.abs(np.sort(wl)-fb).max():.2e}")
print(f"   acoustic top {bands(np.pi)[0]:.4f} = sqrt(2K/m2)={np.sqrt(2*K/m2):.4f};  optical bottom {bands(np.pi)[1]:.4f} = sqrt(2K/m1)={np.sqrt(2*K/m1):.4f};  gap ratio sqrt(m2/m1)={np.sqrt(m2/m1):.4f}")
