# -*- coding: utf-8 -*-
import math
c=299792458.0; hbar=1.054571817e-34; G=6.67430e-11
lP=math.sqrt(hbar*G/c**3); ln2=math.log(2); t0=4.3536e17
Gyr=3.1557e16

print("=== ops/bit の正体 ===")
print("Omega/N = (ln2/2pi^2) * (ct/R_H)     R_H=ct/p なので ct/R_H = p")
print(f"ln2/(2pi^2) = {ln2/(2*math.pi**2):.7f}  = 1/{2*math.pi**2/ln2:.4f}")
print("=> R_h = ct  <=>  Omega/N = 0.0351158...  (8つ目の特徴づけ)")

print("\n=== ops/bit = 1 に必要な膨張則 ===")
p_need = 2*math.pi**2/ln2
print(f"p = 2pi^2/ln2 = {p_need:.3f}   (a ∝ t^28.5 ── 現実にはあり得ない)")

print("\n=== ド・ジッターでは時間とともに増える ===")
print("Omega/N = (ln2/pi^2) * H t     ( = e-fold 数に比例 )")
coef = ln2/math.pi**2
print(f"係数 ln2/pi^2 = {coef:.5f} /e-fold")
Ht1 = math.pi**2/ln2
print(f"1 ops/bit を超えるのは Ht = pi^2/ln2 = {Ht1:.3f} e-fold")
# 実際の宇宙(LCDM, Lambda優勢)で何年後か
H0 = 67.66*1000/3.0857e22       # s^-1
OmL = 0.685
HL = H0*math.sqrt(OmL)
t_cross = Ht1/HL
print(f"H0 = {H0:.4e} /s, H_Lambda = {HL:.4e} /s")
print(f"-> t = {t_cross:.3e} s = {t_cross/Gyr:.1f} Gyr = {t_cross/Gyr/1000:.2f} 兆年? -> {t_cross/Gyr:.0f} 億年ではなく Gyr 単位")
print(f"   すなわち約 {t_cross/Gyr:.0f} Gyr ({t_cross/Gyr*10:.0f} 億年)後")

print("\n=== 各膨張則の ops/bit ===")
for p,name in [(1/2,'放射 a∝t^1/2'),(2/3,'物質 a∝t^2/3'),(1,'c·t=const'),(1/3,'stiff w=1')]:
    v=p*ln2/(2*math.pi**2)
    print(f"  {name:16s} p={p:.4f}  ops/bit={v:.5f} = 1/{1/v:.1f}")

print("\n=== 検算：R_H/ct と ops/bit の対応 ===")
for p in [0.5,2/3,1.0]:
    print(f"  p={p:.3f}: R_H/(ct)={1/p:.4f}, ops/bit*2pi^2/ln2={p:.4f}")

print("\n=== メモリ増設 vs 演算（同じ数の逆数）===")
print(f"dN/dOmega = 1/(p ln2/2pi^2) = {2*math.pi**2/ln2:.2f} (p=1)")
print("宇宙は1回演算するあいだに 28.5 ビット増設している")
