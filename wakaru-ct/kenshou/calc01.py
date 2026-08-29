# -*- coding: utf-8 -*-
import math

c   = 299792458.0
hbar= 1.054571817e-34
G   = 6.67430e-11
kB  = 1.380649e-23
lP  = math.sqrt(hbar*G/c**3)
tP  = lP/c
mP  = math.sqrt(hbar*c/G)
ln2 = math.log(2)

t0  = 4.3536e17          # 13.797 Gyr [s]  (既存シリーズ準拠)
RH  = c*t0               # c*t=const なので地平半径= ct

print("=== 単位 ===")
print(f"lP = {lP:.6e} m   tP = {tP:.6e} s   mP = {mP:.6e} kg")
print(f"t0 = {t0:.4e} s   RH = c*t0 = {RH:.4e} m")

# --- セル数・ティック数（番外編③の再検算）---
Rcell = RH/lP
Ttick = t0/tP
print("\n=== 1ティック1セル ===")
print(f"RH/lP = {Rcell:.5e}   t0/tP = {Ttick:.5e}   ratio = {Rcell/Ttick:.9f}")

# --- メモリ（地平面エントロピー、bit）---
N = math.pi*Rcell**2/ln2
print(f"\nN(bit) = pi(R/lP)^2/ln2 = {N:.4e}")

# --- 総演算数：Margolus-Levitin 2E/(pi hbar) を積算 ---
# 平坦FLRW恒等式 M = c^2 R_H /(2G),  R_H = ct/p
def ops(p, t):
    # E = M c^2 = c^4 R_H /(2G) = c^5 t /(2 G p)
    # rate = 2E/(pi hbar) = c^5 t/(pi hbar G p)
    # integrate: c^5 t^2/(2 pi hbar G p) = (ct/lP)^2/(2 pi p)
    return (c*t/lP)**2/(2*math.pi*p)

Om = ops(1.0, t0)
print(f"Omega(ops) = {Om:.4e}    (Lloyd 2002 の ~1e120 と同桁)")

print("\n=== 今回の主役：1ビットあたりの演算回数 ===")
print(f"Omega/N (数値, p=1) = {Om/N:.6f}")
print(f"解析式 p*ln2/(2 pi^2) = {1*ln2/(2*math.pi**2):.6f}")
for p,name in [(0.5,'放射'),(2/3.,'物質'),(1.0,'c*t=const'),(2.0,'加速')]:
    print(f"  p={p:.4f} ({name}):  ops/bit = {p*ln2/(2*math.pi**2):.5f}  = 1/{2*math.pi**2/(p*ln2):.1f}")

# --- 速度比 ---
dNdt  = 2*N/t0
dOmdt = 2*Om/t0
print(f"\ndN/dt  = {dNdt:.3e} bit/s")
print(f"dOm/dt = {dOmdt:.3e} ops/s")
print(f"メモリ増設は演算より {dNdt/dOmdt:.2f} 倍速い")

# --- 対数クロック ---
efold = math.log(t0/tP)
print(f"\n=== 対数ティック ===")
print(f"ln(t0/tP) = {efold:.2f}")
print(f"1ティックあたり N は e^2 = {math.e**2:.3f} 倍")
print(f"再構成 N = pi e^(2*{efold:.2f})/ln2 = {math.pi*math.exp(2*efold)/ln2:.3e}  (直接値 {N:.3e})")

# --- ホログラフィー：体積セル vs 面ビット ---
V3 = Rcell**3
V4 = (c*t0/lP)**4
print(f"\n=== ホログラフィー ===")
print(f"空間セル (R/lP)^3 = {V3:.3e}")
print(f"4体積セル (ct/lP)^4 = {V4:.3e}")
print(f"N / (R/lP)^3 = {N/V3:.3e}    1/(R/lP) = {1/Rcell:.3e}   比 = {(N/V3)*Rcell:.4f}")

# --- 使用率（番外編②の再検算）---
S_obs = 3.1e104          # Egan & Lineweaver 2010, S/k
N_cap = math.pi*Rcell**2 # nat単位の容量 S/k = A/4lP^2
print(f"\n=== メモリ使用率 ===")
print(f"容量 S/k = pi(R/lP)^2 = {N_cap:.3e}")
print(f"使用 S/k = {S_obs:.2e}  ->  使用率 {S_obs/N_cap:.3e}")

# --- ランダウアー ---
TH = hbar*c/(2*math.pi*kB*RH)      # ハッブル温度 hbar H/(2 pi kB), H=1/t0=c/RH
E  = c**4*RH/(2*G)
print(f"\n=== ランダウアー ===")
print(f"T_H = {TH:.4e} K")
print(f"E   = {E:.4e} J")
print(f"E/N = {E/N:.4e} J   kB T_H ln2 = {kB*TH*ln2:.4e} J   比 = {(E/N)/(kB*TH*ln2):.6f}")

# --- 地平線問題を情報で ---
dTT = 1e-5
print(f"\n=== 合意問題 ===")
print(f"CMB の一様性 1e-5 -> 1パッチあたり log2(1/1e-5) = {math.log2(1/dTT):.2f} bit の一致")
