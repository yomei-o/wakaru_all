# -*- coding: utf-8 -*-
# 第17回：地平線問題を、分散合意として書き直す
import math
t0=4.3536e17; t_rec=1.2e13
dTT=1e-5
print("=== CMB の一様性を、ビットで測る ===")
bits=math.log2(1/dTT)
print(f"  ΔT/T ≈ {dTT:.0e}  →  1パッチあたり log2(1/{dTT:.0e}) = {bits:.2f} ビットの一致")

print("\n=== 因果的に切れたパッチの数 ===")
chi_lss=14100.0   # Mpc（共動）
chi_hor=288.0     # Mpc（再結合時の共動粒子的地平線）
theta=chi_hor/chi_lss
omega=2*math.pi*(1-math.cos(theta))
N=4*math.pi/omega
print(f"  再結合時の共動地平線 {chi_hor:.0f} Mpc / 最終散乱面まで {chi_lss:.0f} Mpc")
print(f"  → 地平線角 θ = {theta:.4f} rad = {math.degrees(theta):.2f}°")
print(f"  → パッチ数 = 4π/Ω = {N:.3e}  （よく引かれる 10⁴ と同じ桁）")

print("\n=== 合意している情報の総量 ===")
tot=N*bits
print(f"  {N:.2e} 台 × {bits:.1f} ビット = {tot:.3e} ビット ≈ {tot/8/1e3:.1f} KB")
print("  → スマホなら一瞬で送れる量。問題は量ではなく、送る手段が無かったこと。")

print("\n=== 偶然で説明できるか ===")
p_each=dTT
print(f"  各パッチが独立ランダムなら、一致する確率は 1パッチ {p_each:.0e}")
print(f"  全部そろう確率 ≈ ({p_each:.0e})^{N:.0f} = 10^({math.log10(p_each)*N:.3e})")
print("  → 天文学的どころではない。偶然は完全に排除される。")

print("\n=== 膨張則を変えると、パッチ数はどう変わるか ===")
R=t0/t_rec
print(f"  t₀/t_rec = {R:.3e}")
print(f"  {'p':>8} {'共動地平線の比':>16} {'パッチ数':>14}")
for p in [0.5, 0.513, 2/3, 0.9, 0.99]:
    ratio=R**(1-p)
    print(f"  {p:8.3f} {ratio:16.3e} {ratio**2:14.3e}")
print(f"  {1.0:8.3f} {'発散（∞）':>16} {1:14d}   ← 粒子的地平線が無限")
print("  → a∝t だけがパッチ 1 個。番外編②の『アドレス空間が動かない』の、天球版。")

print("\n=== ただし、放射を入れると壊れる（番外編②）===")
Or=9.2e-5
z_r=1/math.sqrt(Or)-1
print(f"  放射が総和を乗っ取るのは z > {z_r:.0f}（√Ω_r = {math.sqrt(Or):.2e}）")
print("  再結合 z=1100 は完全にその内側 → a∝t は再結合より前で成立できない")
print("  → 番外編②の分岐B：パッチ数が 1.2e4 に戻り、地平線問題が ΛCDM 並みに復活")

print("\n=== インフレーションの解を、情報の言葉で ===")
Nef=60
print(f"  必要な e-fold ≈ {Nef}")
print(f"  1台のノードの状態を e^{Nef} = {math.exp(Nef):.1e} 倍の体積にコピーしてから切り離す")
print("  → 通信（peer-to-peer）ではなく、ブロードキャスト＋分割。")
print("     『合意』ではなく『複製』で解いている。")
