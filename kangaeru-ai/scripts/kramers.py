# ES on double well: is N an inverse temperature? Kramers prediction vs measurement.
import numpy as np
rng=np.random.default_rng(1)
sig=0.3; c=1.0
L=lambda x: (x**2-1)**2
q=1-3*sig**2
xm=np.sqrt(q); dU=q**2; Umin=8*q; Umax=4*q          # smoothed landscape L_sigma
# per-sample ES gradient noise variance at the minimum (quadrature)
e=rng.standard_normal(4_000_000)
g1=(c+L(xm+sig*e))/sig*e
V=g1.var()
print(f"sigma={sig}  barrier of L_sigma={dU:.4f} (raw L: 1)  per-sample var V={V:.3f}")
def mfpt(eta,N,M=2000):
    x=np.full(M,-xm); t=np.full(M,np.nan); alive=np.ones(M,bool); k=0
    while alive.any():
        xa=x[alive]; e=rng.standard_normal((N,xa.size))
        g=((c+L(xa+sig*e))/sig*e).mean(0)
        xa=xa-eta*g; x[alive]=xa; k+=1
        done=xa>xm; idx=np.flatnonzero(alive)[done]; t[idx]=k*eta; alive[idx]=False
    return t.mean(), t.std()/np.sqrt(M)
print(f"{'eta':>6}{'N':>4}{'T':>8}{'dU/T':>7}{'tau meas':>11}{'tau Kramers':>13}")
for eta,N in [(0.004,1),(0.008,2),(0.016,4),(0.004,2),(0.004,3),(0.004,4),(0.004,5)]:
    T=eta*V/(2*N)
    pred=2*np.pi/np.sqrt(Umin*Umax)*np.exp(dU/T)
    m,s=mfpt(eta,N)
    print(f"{eta:>6}{N:>4}{T:>8.4f}{dU/T:>7.2f}{m:>8.1f}±{s:<4.1f}{pred:>11.1f}",flush=True)
