# ES gradient of a NON-differentiable landscape == gradient of the heat-equation solution at time sigma^2/2
import numpy as np
rng=np.random.default_rng(2)
L=lambda x: np.abs(np.sin(3*x)) + 0.5*(x>0.4)          # kinks + a jump: no gradient exists
dx=0.005; xs=np.arange(-8,8,dx); u0=L(xs)
def heat(u,s):                                          # explicit FD, du/ds = u_xx
    dt=0.4*dx*dx; n=int(np.ceil(s/dt)); dt=s/n; u=u.copy()
    for _ in range(n): u[1:-1]+=dt*(u[2:]-2*u[1:-1]+u[:-2])/dx**2
    return u
def es_grad(x,sig,N=2_000_000):
    e=rng.standard_normal(N)
    return np.mean((L(x+sig*e)-L(x-sig*e))/(2*sig)*e)   # antithetic, no derivative anywhere
pts=[-1.0,-0.5,0.0,0.4,0.7,1.2]
for sig in [0.1,0.3]:
    u=heat(u0,sig**2/2); gu=np.gradient(u,dx)
    print(f"sigma={sig}  heat time s=sigma^2/2={sig**2/2}")
    print(f"{'x':>6}{'ES grad':>10}{'heat grad':>11}")
    for x in pts:
        print(f"{x:>6}{es_grad(x,sig):>10.4f}{np.interp(x,xs,gu):>11.4f}")
# semigroup: smoothing 0.1 then 0.2828 == smoothing 0.3 (variances add = times add)
u_a=heat(heat(u0,0.1**2/2),(0.3**2-0.1**2)/2); u_b=heat(u0,0.3**2/2)
m=np.abs(xs)<3
print("max |two-step - one-step| =",np.abs(u_a-u_b)[m].max())
