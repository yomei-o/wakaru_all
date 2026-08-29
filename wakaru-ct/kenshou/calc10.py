# -*- coding: utf-8 -*-
# 第6回：メモリの使用率 ── 空っぽさ＝共形平坦さ＝時間の矢
import math
c=299792458.0; hbar=1.054571817e-34; G=6.67430e-11; kB=1.380649e-23
lP=math.sqrt(hbar*G/c**3); tP=lP/c
t0=4.3536e17; RH=c*t0
yr=3.1557e7; ly=9.4607e15

print("=== 容量と使用量 ===")
A_H = 4*math.pi*RH**2
S_max = A_H/(4*lP**2)                      # S/k_B （nat）
N_bit = S_max/math.log(2)
print(f"  地平面積 A_H = {A_H:.3e} m^2")
print(f"  容量 S_max/k_B = A/4lP^2 = {S_max:.3e}  （= {N_bit:.3e} bit）")

S_obs = 3.1e104        # Egan & Lineweaver 2010（超巨大BHが支配）
S_cmb = 2.03e88
S_nu  = 1.93e88
use = S_obs/S_max
print(f"  使用 S_obs/k_B = {S_obs:.2e}  ->  使用率 = {use:.3e}")
print(f"  ほぼ空。空きは {1-use:.20f}")

print("\n=== 使用率は、じつは面積比そのもの ===")
print("  S = A/4lP^2 は BH でも地平面でも同じ形なので")
A_BH = use*A_H
r_eq = math.sqrt(A_BH/(4*math.pi))
print(f"  使用率 = ΣA_BH / A_H = {use:.3e}")
print(f"  -> 宇宙の全ブラックホールの地平面を合計すると A = {A_BH:.3e} m^2")
print(f"     一つの球にまとめると半径 {r_eq:.3e} m = {r_eq/ly:.1f} 光年")

print("\n=== 使われているメモリは、どちら側か ===")
frac_matter=(S_cmb+S_nu)/S_obs
print(f"  CMB光子 {S_cmb:.2e} ＋ ニュートリノ {S_nu:.2e}  → 合計 {(S_cmb+S_nu):.2e}")
print(f"  物質・放射側の割合 = {frac_matter:.3e}")
print(f"  重力側（ブラックホール＝ワイル側）の割合 = {1-frac_matter:.20f}")
print(f"  -> 今日のエントロピーの {100*(1-frac_matter):.15f} % が重力側")

print("\n=== 使用率の履歴（エントロピー密度 ÷ ホログラフィック上限）===")
print("  番外編③の s <= 3H/4lP^2 を使う。比 ∝ t^(1-3p)")
def ratio_evolution():
    t_eq=1.6e12         # 等密度期 [s]
    seg=[("プランク→等密度（放射 p=1/2）", tP, t_eq, 0.5),
         ("等密度→今日（物質 p=2/3）",     t_eq, t0,  2/3.)]
    r=1.0
    print(f"  {'区間':32s} {'指数 1-3p':>10} {'倍率':>12}   {'到達点':>12}")
    for name,ta,tb,p in seg:
        e=1-3*p
        f=(tb/ta)**e
        r*=f
        print(f"  {name:32s} {e:10.3f} {f:12.3e}   {r:12.3e}")
    return r
r_final=ratio_evolution()
print(f"  プランク期を O(1) とすると、今日の物質・放射だけの使用率 ≈ {r_final:.2e}")
print(f"  （番外編③の直接計算値 1.3e-34 と同じ桁）")

print("\n=== まとめの三段 ===")
print(f"  プランク期            : 使用率 ~ 1        （満杯）")
print(f"  今日・物質と放射だけ  : 使用率 ~ {r_final:.0e}   （空になった）")
print(f"  今日・ブラックホール込 : 使用率 = {use:.1e}   （重力が埋め戻した）")
print(f"  埋め戻し量 = {use/r_final:.1e} 倍 = {math.log10(use/r_final):.1f} 桁")

print("\n=== エントロピーそのものは増えている ===")
print(f"  再結合ごろ（光子のみ） S/k ~ {S_cmb:.2e}")
print(f"  今日                   S/k = {S_obs:.2e}")
print(f"  増加 {S_obs/S_cmb:.2e} 倍 = {math.log10(S_obs/S_cmb):.1f} 桁 ── 全部が重力側の寄与")
