# 2D Ising block-spin RG: each 2x2 majority block = one "pooling layer". What flows with depth?
import numpy as np
rng=np.random.default_rng(4)
Tc=2/np.log(1+np.sqrt(2))
def sample(T,n=256,sweeps=4000,keep=40,cold=False):
    s=np.ones((n,n),int) if cold else rng.choice([-1,1],(n,n)); out=[]
    ii,jj=np.indices((n,n)); masks=[(ii+jj)%2==0,(ii+jj)%2==1]
    for k in range(sweeps):
        for m in masks:
            nb=np.roll(s,1,0)+np.roll(s,-1,0)+np.roll(s,1,1)+np.roll(s,-1,1)
            dE=2*s*nb; flip=(rng.random(s.shape)<np.exp(-dE/T))&m
            s=np.where(flip,-s,s)
        if k>=sweeps-keep*25 and k%25==0: out.append(s.copy())
    return out
def block(s):
    b=s.reshape(s.shape[0]//2,2,s.shape[1]//2,2).sum((1,3)).astype(float)
    b[b==0]=rng.choice([-1,1],(b==0).sum()); return np.sign(b)
nn=lambda s: np.mean(s*np.roll(s,1,0)+s*np.roll(s,1,1))/2
for T in [0.9*Tc]:
    confs=sample(T,cold=True); row=[]
    for lev in range(6):
        row.append(np.mean([nn(c) for c in confs]))
        confs=[block(c) for c in confs]
    print(f"T/Tc={T/Tc:.2f}  nn-correlation per layer (256->8):  "+"  ".join(f"{v:.3f}" for v in row),flush=True)
