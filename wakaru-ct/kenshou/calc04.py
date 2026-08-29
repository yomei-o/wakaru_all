# -*- coding: utf-8 -*-
# 第2回：二つのクロック（宇宙の対数時間 と 繰り込み群の対数エネルギー）
import math

c=299792458.0; hbar=1.054571817e-34; G=6.67430e-11; kB=1.380649e-23
lP=math.sqrt(hbar*G/c**3); tP=lP/c; mP=math.sqrt(hbar*c/G)
TP=mP*c*c/kB
t0=4.3536e17; T0=2.7255
Gyr=3.1557e16; yr=3.1557e7

print("=== 二つのクロック ===")
Nt=math.log(t0/tP)
NT=math.log(TP/T0)
print(f"時間クロック   ln(t0/tP)  = {Nt:.2f} ステップ")
print(f"エネルギークロック ln(TP/T0) = {NT:.2f} ステップ")
print(f"比 = {NT/Nt:.4f}   <- これが対数平均の膨張指数 p")
print(f"  放射なら 0.5 / 物質なら 0.6667 / c*t=const なら 1.0")

# エントロピー放出の補正 T ∝ g*s^{-1/3}/a
gs_hi, gs_lo = 106.75, 3.909
corr=math.log((gs_hi/gs_lo)**(1/3))
print(f"\ng*s 補正 (106.75 -> 3.909): ln 補正 = {corr:.3f}")
print(f"補正後 ln(a比) = {NT-corr:.2f}  ->  p = {(NT-corr)/Nt:.4f}")

print(f"\nc*t=const が要求するのは p=1、すなわち {Nt:.1f} = {NT:.1f}")
print(f"実測との食い違い: 係数 {Nt/NT:.3f} 倍（約2倍）")

print("\n=== d ln T / d ln t ===")
for p,name in [(0.5,'放射'),(2/3,'物質'),(1.0,'c*t=const')]:
    print(f"  {name:10s} p={p:.4f}  d lnT/d lnt = {-p:+.4f}"
          + ("   <- 1:1 同期（9つ目）" if abs(p-1)<1e-9 else ""))

print("\n=== a定理の階段を、宇宙の対数時間に載せる ===")
# 放射優勢の T-t 関係: t[s] = 2.42/sqrt(g*) * (MeV/T)^2
def t_of_T_MeV(T_MeV,gstar): return 2.42/math.sqrt(gstar)*(1.0/T_MeV)**2
rows=[
 ("プランク",       None, None, 995.5, "標準模型ぜんぶ"),
 ("173 GeV  t,H,W,Z",1.73e5,106.75, 772.5,"トップ・ヒッグス・W・Z が抜ける"),
 ("4.2 GeV  b",      4.2e3, 86.25,  739.5,"ボトム"),
 ("1.3 GeV  tau,c",  1.3e3, 75.75,  695.5,"タウ・チャーム"),
 ("0.2 GeV  QCD",    2.0e2, 61.75,   89.5,"閉じ込め（最大の段）"),
 ("0.511MeV e",      0.511, 10.75,   78.5,"電子"),
]
prev=None
for name,TMeV,gs,a,note in rows:
    if TMeV is None:
        x=0.0; t=tP
    else:
        t=t_of_T_MeV(TMeV,gs); x=math.log(t/tP)
    drop = "" if prev is None else f"  落差 {prev/a:.3f}倍 ({math.log(prev/a):.3f} nat)"
    print(f"  {name:18s} t={t:9.3e}s  ステップ {x:6.1f}   a={a:6.1f}{drop}   {note}")
    prev=a
# ニュートリノ（物質期）: T=0.05 eV -> z = 0.05/(kT0 in eV) ; kT0 = 2.35e-4 eV
kT0_eV=kB*T0/1.602176634e-19
z_nu=0.05/kT0_eV
t_nu=t0/ (1+z_nu)**1.5          # 物質優勢の近似
print(f"  {'0.05 eV  nu':18s} t={t_nu:9.3e}s  ステップ {math.log(t_nu/tP):6.1f}   a=  62.0"
      f"  落差 {78.5/62.0:.3f}倍 ({math.log(78.5/62.0):.3f} nat)   最後の一段（kT0={kT0_eV:.3e} eV, z={z_nu:.0f}）")

print(f"\n総落差 995.5 -> 62.0 = {995.5/62.0:.3f} 倍 = {math.log(995.5/62.0):.4f} nat")
print(f"140ステップで割ると 1ステップあたり {math.log(995.5/62.0)/Nt*100:.2f} %")
print(f"ただし実際に落ちるのはステップ {math.log(t_of_T_MeV(1.73e5,106.75)/tP):.0f} 〜 {math.log(t_nu/tP):.0f} の間だけ")
span=math.log(t_nu/tP)-math.log(t_of_T_MeV(1.73e5,106.75)/tP)
print(f"  その区間 {span:.1f} ステップで割ると 1ステップあたり {math.log(995.5/62.0)/span*100:.2f} %")
print(f"QCD閉じ込めの一段だけで {math.log(695.5/89.5)/math.log(995.5/62.0)*100:.1f} % を占める")

print("\n=== メモリは1ステップで何倍か ===")
print(f"N ∝ t^2 なので 1ステップで e^2 = {math.e**2:.4f} 倍")
print(f"140.24 ステップぶん: e^(2*140.24) = 10^{2*Nt/math.log(10):.2f}")
