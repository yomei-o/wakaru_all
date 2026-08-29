# -*- coding: utf-8 -*-
# 第4回の下ごしらえ：無次元パラメータを何個持っているか
#  R_h=ct は無次元パラメータ 0 個 -> 全ての無次元観測量がパラメータフリーの予言になる
import numpy as np

def E_lcdm(z, Om=0.315, Or=9.2e-5):
    return np.sqrt(Or*(1+z)**4 + Om*(1+z)**3 + (1-Om-Or))

def dL_lcdm(z, Om=0.315):
    zs=np.linspace(0,z,20001)
    chi=np.trapezoid(1.0/E_lcdm(zs,Om), zs) if hasattr(np,'trapezoid') else np.trapz(1.0/E_lcdm(zs,Om), zs)
    return (1+z)*chi                      # H0 dL / c

def dL_rhct(z):
    return (1+z)*np.log(1+z)              # H0 dL / c   ← パラメータゼロ

print("=== 無次元パラメータの数 ===")
print("  LCDM      : 6 個  (Ω_b h², Ω_c h², θ*, τ, A_s, n_s)  ※ H0 は次元付き＝単位を決めるだけ")
print("  R_h=ct    : 0 個  (H0 のみ。無次元パラメータなし)")
print("  -> R_h=ct では、あらゆる無次元観測量が調整不能な予言になる")
print()
print("=== 光度距離（無次元）H0 dL / c ===")
print(f"  {'z':>6} | {'R_h=ct':>10} | {'LCDM':>10} | {'比':>7} | {'等級差 Δm':>9}")
for z in [0.1,0.3,0.5,1.0,1.5,2.0,3.0,5.0,10.0,1100.0]:
    a=dL_rhct(z); b=dL_lcdm(z)
    dm=5*np.log10(a/b)
    print(f"  {z:6.1f} | {a:10.4f} | {b:10.4f} | {a/b:7.4f} | {dm:+9.3f}")

print()
print("  R_h=ct の予言式:  H0 dL / c = (1+z) ln(1+z)   ← 定数が一つも入っていない")
print("  LCDM         :  H0 dL / c = (1+z) ∫dz'/E(z'),  E に Ω_m が入る（＝調整できる）")

# 差が最大になる z（超新星の範囲）
zs=np.linspace(0.01,2.5,500)
dm=np.array([5*np.log10(dL_rhct(z)/dL_lcdm(z)) for z in zs])
i=np.argmax(np.abs(dm))
print(f"\n  超新星の範囲 (z<2.5) で差が最大なのは z={zs[i]:.2f} の Δm={dm[i]:+.3f} 等")
print(f"  現代の SNe Ia の統計誤差は ~0.01-0.02 等 -> 桁で見えるはずの差")

print()
print("=== 情報の言葉に直すと ===")
print("  モデルの記述長 = パラメータ数 × ビット")
print("  R_h=ct は記述長ゼロ ── オッカムの剃刀の極限")
print("  だが最小記述長は『データを説明できたうえで』の話。説明できないなら短さは意味を持たない")
