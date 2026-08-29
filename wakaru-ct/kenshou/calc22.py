# -*- coding: utf-8 -*-
# 第18回：アドレス線が足りない ── ホログラフィーをアドレスの言葉で書く
import math
c=299792458.0; hbar=1.054571817e-34; G=6.67430e-11
lP=math.sqrt(hbar*G/c**3); ln2=math.log(2)
t0=4.3536e17; RH=c*t0; fm=1e-15
R=RH/lP
print(f"=== 数える ===")
print(f"  R_H/ℓ_P = {R:.4e}")
V3=R**3; V4=R**4
N=math.pi*R**2/ln2
print(f"  空間セル  (R/ℓ_P)³ = {V3:.4e}")
print(f"  4体積セル (ct/ℓ_P)⁴ = {V4:.4e}")
print(f"  書けるビット N      = {N:.4e}")

print("\n=== 比 ===")
print(f"  N / (空間セル)  = {N/V3:.4e}")
print(f"  1/(R/ℓ_P)       = {1/R:.4e}")
print(f"  比の比           = {(N/V3)*R:.6f}   （＝ π/ln2 = {math.pi/ln2:.6f}）")
print(f"  N / (4体積セル) = {N/V4:.4e}")
print("  → ホログラフィー＝『空間セルの 10^-61 にしか番地が振れない』")

print("\n=== 1ビットが担当する体積 ===")
vb=V3/N                      # プランク体積の個数
print(f"  V₃/N = (ln2/π)(R/ℓ_P) = {vb:.4e} プランク体積")
vol=vb*lP**3
side=vol**(1/3.)
print(f"     = {vol:.4e} m³   → 一辺 {side:.4e} m = {side/fm:.3f} fm")
print(f"  参考：陽子の電荷半径 0.84 fm（直径 1.68 fm）、原子核の典型 ~2 fm")
print(f"  ★ 1ビットあたりの体積は、一辺およそ陽子の大きさ")

print("\n=== これは何のスケールか ===")
mid=(RH*lP**2)**(1/3.)
print(f"  (R_H ℓ_P²)^(1/3) = {mid:.4e} m = {mid/fm:.2f} fm")
print(f"  係数 (ln2/π)^(1/3) = {(ln2/math.pi)**(1/3.):.4f} を掛けて {mid*(ln2/math.pi)**(1/3.)/fm:.3f} fm")
print("  → 地平半径とプランク長の『三分の一乗の中間スケール』。")
print("     説明のない数値的一致（前シリーズ番外編⑤の ρ_Λ^(1/4)≈m_ν と同じ種類）")

print("\n=== アドレス幅 ===")
addr=math.log2(V3)
print(f"  空間セル1個を指定するのに必要なビット数 = log2({V3:.2e}) = {addr:.1f} ビット")
print(f"  4体積セルなら log2({V4:.2e}) = {math.log2(V4):.1f} ビット")
print(f"  → 番地を書くのに {addr:.0f} ビット。メモリ全体は {N:.2e} ビット。")
print(f"     番地を全部書き並べると {V3*addr:.2e} ビット必要 ── メモリの {V3*addr/N:.2e} 倍")
print("  → 『全セルに番地を振る』こと自体が、メモリに収まらない。")

print("\n=== 時間方向も足りない ===")
print(f"  4体積セル {V4:.2e} 個に対して、メモリ {N:.2e} ビット")
print(f"  比 = {N/V4:.2e} ── 空間だけのときよりさらに 61 桁足りない")
print("  → 『宇宙の全履歴を記録する』のは、原理的に不可能")
