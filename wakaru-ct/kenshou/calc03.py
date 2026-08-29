# -*- coding: utf-8 -*-
import math
ln2=math.log(2); pi=math.pi
def opsbit_w(w): return ln2/(3*pi**2*(1+w))
def opsbit_p(p): return p*ln2/(2*pi**2)
print("Omega/N = ln2/(3 pi^2 (1+w))   [= p ln2/(2 pi^2), p=2/(3(1+w))]")
print("check w=-1/3 :", opsbit_w(-1/3), " vs p=1 :", opsbit_p(1.0))
rows=[("放射",1/3),("物質",0.0),("ct=const",-1/3),("stiff",1.0)]
for n,w in rows:
    p=2/(3*(1+w)); v=opsbit_w(w)
    print(f"  {n:9s} w={w:+.4f} p={p:.4f}  ops/bit={v:.5f} = 1/{1/v:.2f}")
w1=ln2/(3*pi**2)-1
print(f"\nops/bit = 1 になる w = {w1:.5f}   (1+w = {ln2/(3*pi**2):.5f})")
print(f"観測の暗黒エネルギー w = -1.03 +- 0.03  ->  すでに向こう側")
print(f"\nド・ジッター: ops/bit = (ln2/pi^2) H t = {ln2/pi**2:.5f} * (e-fold)")
print(f"  1 を超える e-fold = {pi**2/ln2:.3f}")
H0=67.66*1000/3.0857e22; HL=H0*math.sqrt(0.685); Gyr=3.1557e16
print(f"  H_Lambda={HL:.4e}/s -> t={pi**2/ln2/HL/Gyr:.0f} Gyr = {pi**2/ln2/HL/Gyr/10:.1f} 千億年")
print(f"\n宇宙の対数クロック ln(t0/tP)=140.2, 1 e-fold で N は e^2={math.e**2:.3f} 倍")
