# One generation of selection on a Gaussian population vs diffusion-model score (Tweedie) vs ES.
import numpy as np
rng=np.random.default_rng(3)
sig=0.4
dx=0.004; xs=np.arange(-8,8,dx)
def heat(u,s):
    dt=0.4*dx*dx; n=int(np.ceil(s/dt)); dt=s/n; u=u.copy()
    for _ in range(n): u[1:-1]+=dt*(u[2:]-2*u[1:-1]+u[:-2])/dx**2
    return u
for beta in [0.3,1.0,3.0]:
    L=lambda x: beta*(x**2-1)**2            # "energy";  fitness w = exp(-L)
    w=lambda x: np.exp(-L(x))
    lnwbar=np.log(heat(w(xs),sig**2/2)); Lsig=heat(L(xs),sig**2/2)
    g_score=np.gradient(lnwbar,dx); g_es=-np.gradient(Lsig,dx)
    print(f"beta={beta}   (population sd sigma={sig})")
    print(f"{'z':>6}{'selection dz (MC)':>19}{'Tweedie s^2*dlnwbar':>21}{'ES -s^2*dL_s':>14}")
    for z in [-1.5,-0.6,0.3,0.9]:
        pop=z+sig*rng.standard_normal(4_000_000); wt=w(pop)
        dz=(wt*pop).sum()/wt.sum()-z                     # Price: Cov(w,z)/wbar
        print(f"{z:>6}{dz:>19.4f}{sig**2*np.interp(z,xs,g_score):>21.4f}{sig**2*np.interp(z,xs,g_es):>14.4f}")
