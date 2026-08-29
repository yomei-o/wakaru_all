# -*- coding: utf-8 -*-
# 第5回：短さと当てはまりを、ビットで取引する
#   記述長 = 当てはまりの損 + パラメータの値段
#   ・AIC  : パラメータ1個 = 1/ln2 = 1.443 bit（データ数に依らない）
#   ・BIC  : パラメータ1個 = (1/2)log2 N bit（データ数で高くなる）
#   ・当てはまりの損 = Δχ² / (2 ln2) bit
import numpy as np
ln2=np.log(2)

def E(z,Om=0.315,Or=9.2e-5): return np.sqrt(Or*(1+z)**4+Om*(1+z)**3+(1-Om-Or))
def dc_lcdm(z,Om=0.315,n=4000):
    zs=np.linspace(0,z,n)
    return np.trapz(1.0/E(zs,Om),zs)
def mu_diff(z,Om=0.315):
    """R_h=ct と LCDM の距離指標の差（定数項を除く前）[mag]"""
    return 5*np.log10(np.log(1+z)/dc_lcdm(z,Om))

print("=== パラメータ1個の値段（ビット）===")
for N in [100,1000,1701,10000]:
    print(f"  N={N:6d}:  AIC {1/ln2:.3f} bit   BIC {0.5*np.log2(N):.3f} bit"
          f"   （BIC の Δχ² 予算 = ln N = {np.log(N):.3f}）")

print("\n=== 距離指標の差 Δμ(z)（定数項はまだ引いていない）===")
zs=np.array([0.01,0.05,0.1,0.3,0.5,0.8,1.0,1.5,2.0,2.3])
dm=np.array([mu_diff(z) for z in zs])
for z,d in zip(zs,dm): print(f"  z={z:5.2f}  Δμ = {d:+.4f} mag")

# --- Pantheon+ 風の赤方偏移分布（模式）: 低zに厚く、テールが z~2.3 まで
rng=np.random.default_rng(0)
def sample_z(n):
    z=rng.gamma(shape=2.0,scale=0.16,size=int(n*2.5))
    z=z[(z>0.01)&(z<2.3)]
    return z[:n]

N=1701; sig=0.15
z=sample_z(N)
d=np.array([mu_diff(zi) for zi in z])
w=1/sig**2
off=np.average(d,weights=np.full_like(d,w))      # 絶対等級＝定数項を最良に吸わせる
res=d-off
chi2=np.sum(res**2)/sig**2

print(f"\n=== Pantheon+ 規模（N={N}, 1本あたり σ={sig} mag）での見積もり ===")
print(f"  z の中央値 {np.median(z):.3f}  平均 {np.mean(z):.3f}  最大 {np.max(z):.2f}")
print(f"  定数項を吸わせたあとの残差 RMS = {np.sqrt(np.mean(res**2)):.4f} mag")
print(f"  Δχ² (R_h=ct − ΛCDM) = {chi2:.1f}")
print(f"  → 当てはまりで失うビット = Δχ²/(2 ln2) = {chi2/(2*ln2):.1f} bit")
print(f"  → パラメータ1個で得するビット = {0.5*np.log2(N):.2f} bit (BIC) / {1/ln2:.2f} bit (AIC)")
print(f"  → 差し引き {chi2/(2*ln2)-0.5*np.log2(N):+.1f} bit（BIC基準）")

print("\n=== 逆算：Δχ² が予算に収まるのは、1本あたりの残差がいくつまでか ===")
for name,budget in [("AIC (Δχ²=2)",2.0),("BIC (Δχ²=ln N)",np.log(N))]:
    rms=sig*np.sqrt(budget/N)
    print(f"  {name:18s}: 残差 RMS < {rms*1000:.2f} mmag  （実際は {np.sqrt(np.mean(res**2))*1000:.0f} mmag）")

print("\n=== 何本あれば決着がつくか（残差RMSを固定して N を振る）===")
rms=np.sqrt(np.mean(res**2))
for n in [10,30,100,300,1000]:
    c=n*(rms/sig)**2
    print(f"  N={n:5d}:  Δχ² = {c:8.2f}   BIC予算 lnN = {np.log(n):5.2f}   "
          f"{'ΛCDM の勝ち' if c>np.log(n) else 'R_h=ct の勝ち'}")
