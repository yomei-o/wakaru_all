import numpy as np
rng=np.random.default_rng(0)
d=10; sig=1.0; a=np.linspace(0.5,2,d)
L=lambda th: 0.5*np.sum(a*th**2,axis=-1)
def run(eta,N,t_total,stat_from):
    th=np.ones(d); T=int(t_total/eta); acc=[]
    for k in range(T):
        e=rng.standard_normal((N,d))
        g=((1.0+L(th+sig*e))/sig)[:,None]*e   # one-sided ES, offset 1 keeps noise at optimum
        th=th-eta*g.mean(0)
        if k*eta>=stat_from: acc.append(L(th))
    return np.mean(acc)
print("eta      N     eta/N    <L> stationary")
for eta,N in [(0.001,1),(0.002,2),(0.004,4),(0.008,8),(0.001,4),(0.004,1)]:
    print(f"{eta:<8}{N:<6}{eta/N:<9.5f}{run(eta,N,150,30):.5f}",flush=True)
