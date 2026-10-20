# Steps S vs samples E to reach a target loss with ES, best eta per batch size N.
# McCandlish et al. 2018 predict (S/Smin-1)(E/Emin-1)=1 with Bcrit=Emin/Smin.
import numpy as np
rng=np.random.default_rng(5)
d=10; sig=1.0; a=np.linspace(0.5,2,d); target=0.3; R=32
L=lambda th: 0.5*np.sum(a*th**2,axis=-1)
def steps(eta,N,maxk=3000):
    th=np.ones((R,d))*1.5; k=0; hit=np.full(R,maxk)
    alive=np.ones(R,bool)
    while alive.any() and k<maxk:
        e=rng.standard_normal((N,R,d))
        g=((1.0+L(th+sig*e))/sig)[...,None]*e
        th=th-eta*g.mean(0); k+=1
        newly=alive&(L(th)<target); hit[newly]=k; alive&=~newly
        if not np.isfinite(L(th)).all() or L(th).max()>1e4: return maxk
    return np.median(hit)
Ns=[1,4,16,64,256,1024,4096]
S=[];E=[]
for N in Ns:
    best=min(steps(eta,N) for eta in np.geomspace(0.002,1.5,18))
    S.append(best); E.append(best*N)
S=np.array(S,float);E=np.array(E,float)
# fit Smin,Emin by least squares on the hyperbola S = Smin(1+Bcrit/N)
print("raw S:",S)
from scipy.optimize import curve_fit
f=lambda N,Smin,Bc: Smin*(1+Bc/N)
(Smin,Bc),_=curve_fit(f,np.array(Ns,float),S,p0=[S[-1],10],maxfev=20000)
Emin=Smin*Bc
print(f"fit: Smin={Smin:.1f}  Emin={Emin:.1f}  Bcrit={Bc:.2f}")
print(f"{'N':>5}{'S':>8}{'E':>9}{'(S/Smin-1)(E/Emin-1)':>23}{'phi=ln(N/Bcrit)':>17}")
for N,s,e in zip(Ns,S,E):
    print(f"{N:>5}{s:>8.0f}{e:>9.0f}{(s/Smin-1)*(e/Emin-1):>23.3f}{np.log(N/Bc):>17.2f}")
