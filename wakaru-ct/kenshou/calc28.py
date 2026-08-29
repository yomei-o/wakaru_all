# -*- coding: utf-8 -*-
# 第24回：地平面を、毎秒何ビットが渡れるか
import math
c=299792458.0; hbar=1.054571817e-34; G=6.67430e-11; kB=1.380649e-23; eV=1.602176634e-19
lP=math.sqrt(hbar*G/c**3); ln2=math.log(2)
t0=4.3536e17; RH=c*t0; t_rec=1.2e13
E=c**4*RH/(2*G)
N=math.pi*(RH/lP)**2/ln2

print("=== 二つの『毎秒ビット』を区別する ===")
dNdt=2*N/t0
print(f"  ① 容量が増える速さ dN/dt = 2N/t₀ = {dNdt:.4e} bit/s   （第1回）")
C=2*math.pi*E/(hbar*ln2)
print(f"  ② 通信路容量（ベケンシュタイン＝ブレーメルマン）")
print(f"     C = 2πE/(ħ ln2) = {C:.4e} bit/s")
print(f"  比 dN/dt ÷ C = {dNdt/C:.6f}")

print("\n=== これは恒等式 ===")
print("  C = 2πE/(ħln2), E = c⁴R/2G, ℓ_P² = ħG/c³ より")
print("    C = π c R /(ℓ_P² ln2)")
print("  N = π R²/(ℓ_P² ln2), R=ct, Ṙ=c より")
print("    dN/dt = 2π c R /(ℓ_P² ln2) = 2C")
print("  → dN/dt = 2C ちょうど。第19回の分類では【恒等式】＝驚き 0 ビット。")
print("  ★ 意味：宇宙はメモリを、情報を動かせる速さのちょうど2倍で増設している。")

print("\n=== 第17回の 20 KB は、どれだけで送れたか ===")
bits=1.6e5
for n,t in [("再結合 (t=1.2e13 s)",t_rec),("元素合成 (t=1 s)",1.0),("今日",t0)]:
    R=c*t; Ct=math.pi*c*R/(lP**2*ln2)
    print(f"  {n:22s} C = {Ct:.3e} bit/s   →  20KB の送信に {bits/Ct:.2e} 秒")
print("  → チャネルさえあれば、地平線問題の 20 KB は一瞬で送れた。")
print("     問題は帯域ではなく、チャネルが存在しなかったこと（第17回の結論の裏づけ）。")

print("\n=== 1粒子あたりの帯域 ===")
for n,Ej in [("CMB 光子 1 個", 2.349e-4*eV),("陽子 1 個", 1.6726e-27*c*c),("1 kg の物質", 1.0*c*c)]:
    C1=2*math.pi*Ej/(hbar*ln2)
    print(f"  {n:16s} E={Ej:.3e} J  →  C = {C1:.3e} bit/s")
print("  → CMB 光子 1 個は毎秒 3 兆ビットを運べる（原理上）。実際に運んでいるのは数ビット。")

print("\n=== 人間の作ったものと比べる ===")
net=1.3e15
print(f"  世界のインターネット総トラフィック ≈ {net:.1e} bit/s")
print(f"  1 kg の物質の原理上の帯域           = {2*math.pi*c*c/(hbar*ln2):.3e} bit/s")
print(f"  → 人類の全通信は、1 kg の限界の {net/(2*math.pi*c*c/(hbar*ln2)):.2e} 倍")
print(f"  宇宙の地平面                        = {C:.3e} bit/s")
print(f"  → 人類の全通信は、地平面の {net/C:.2e} 倍")

print("\n=== 140 手に、帯域を足す ===")
print(f"  1 対数ステップ（宇宙年齢が e 倍）のあいだに渡れるビット数：")
for n,t in [("プランク期",5.391e-44),("元素合成",1.0),("今日",t0)]:
    R=c*t; Ct=math.pi*c*R/(lP**2*ln2)
    print(f"    {n:12s} C×t = {Ct*t:.3e} bit  （そのときのメモリ {math.pi*(R/lP)**2/ln2:.3e} の {Ct*t/(math.pi*(R/lP)**2/ln2):.3f} 倍）")
print("  ★ C×t = N ちょうど。つまり『1ハッブル時間で、メモリ全体をちょうど1回動かせる』")
print("     dN/dt = 2C とは同じ恒等式の裏表（N∝t² なので dN/dt = 2N/t = 2C）")
print("\n=== 第1回とつなぐ ===")
print(f"  帯域はメモリ 1 回ぶん/ハッブル時間 ある。ところが実際の演算は 1ビットあたり 0.035 回。")
print(f"  → 動かす力は十分あるのに、動かしていない。使っていないのは能力不足ではない。")
