# Effective receptive field of random CNNs vs depth: stride 1 (heat clock) vs stride 2 (RG clock)
import torch, numpy as np
torch.manual_seed(0); torch.set_num_threads(8)
def erf_radius(depth, stride, relu, C=16, H=257, trials=8):
    rs=[]
    for _ in range(trials):
        layers=[]; cin=1
        for i in range(depth):
            conv=torch.nn.Conv2d(cin,C,3,stride=(2 if stride==2 else 1),padding=1,bias=False)
            torch.nn.init.kaiming_normal_(conv.weight); layers.append(conv)
            if relu: layers.append(torch.nn.ReLU())
            cin=C
        net=torch.nn.Sequential(*layers)
        x=torch.randn(1,1,H,H,requires_grad=True)
        y=net(x); c=y.shape[-1]//2
        y[0,:,c,c].sum().backward()
        g=x.grad[0,0].abs().numpy(); g=g/g.sum()
        ii,jj=np.mgrid[:H,:H]; mi=(g*ii).sum(); mj=(g*jj).sum()
        rs.append(np.sqrt((g*((ii-mi)**2+(jj-mj)**2)).sum()/2))
    return np.mean(rs)
print("stride 1  (no pooling)")
print(f"{'L':>4}{'r linear':>10}{'r ReLU':>9}{'r/sqrt(L) ReLU':>16}")
for L in [1,2,4,8,16,32]:
    a=erf_radius(L,1,False); b=erf_radius(L,1,True)
    print(f"{L:>4}{a:>10.2f}{b:>9.2f}{b/np.sqrt(L):>16.3f}",flush=True)
print("stride 2  (every layer downsamples)")
print(f"{'L':>4}{'r ReLU':>9}{'log2 r':>8}")
for L in [1,2,3,4,5,6]:
    b=erf_radius(L,2,True,H=513)
    print(f"{L:>4}{b:>9.2f}{np.log2(b):>8.2f}",flush=True)
