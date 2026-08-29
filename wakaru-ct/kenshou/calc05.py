# -*- coding: utf-8 -*-
# 「モデルとしては失格」を、今日の二つの数だけで言い直す
import math
kB=1.380649e-23; eV=1.602176634e-19
t0=4.3536e17; T0=2.7255
tP=5.391247e-44; TP=1.41678e32
yr=3.1557e7

def K_to_eV(T): return kB*T/eV

print("=== c*t=const（T ∝ 1/t、今日で規格化）で、各温度に到達する時刻 ===")
targets=[("0.8 MeV（中性子の凍結）",0.8e6),("1 MeV",1e6),("0.1 MeV（重水素）",0.1e6),
         ("100 GeV（電弱）",1e11),("0.2 GeV（QCD）",2e8)]
for name,E_eV in targets:
    T=E_eV*eV/kB                    # K
    t=t0*T0/T                       # T ∝ 1/t
    print(f"  {name:22s} T={T:9.3e} K   t = {t:9.3e} s = {t/yr:9.3e} 年")

print("\n  中性子の寿命 tau_n = 879.4 s = {:.3e} 年".format(879.4/yr))
T_f=0.8e6*eV/kB
t_f=t0*T0/T_f
print(f"  -> 凍結温度に達するのは t={t_f:.3e} s ({t_f/yr:.2f} 年)、寿命の {t_f/879.4:.3e} 倍")

print("\n=== 参考：標準宇宙論（放射優勢 T ∝ t^-1/2）===")
# t = 2.42/sqrt(g*) (MeV/T)^2 s
for name,E_eV,gs in [("0.8 MeV（中性子の凍結）",0.8e6,10.75),("0.1 MeV（重水素）",0.1e6,3.36)]:
    TMeV=E_eV/1e6
    t=2.42/math.sqrt(gs)*(1.0/TMeV)**2
    print(f"  {name:22s} t = {t:9.3e} s")

print("\n=== 1秒の時点での温度 ===")
print(f"  標準:      約 1 MeV")
T1=T0*t0/1.0
print(f"  c*t=const: T = T0*(t0/1s) = {T1:.3e} K = {K_to_eV(T1)/1e9:.1f} GeV")

print("\n=== 逆に、プランク温度に達するのはいつか ===")
t_TP=t0*T0/TP
print(f"  c*t=const: t = {t_TP:.3e} s   (プランク時刻の {t_TP/tP:.3e} 倍、ステップ {math.log(t_TP/tP):.1f})")
print(f"  つまり最初の {math.log(t_TP/tP):.0f} 対数ステップは、プランク温度より熱い領域にいる")

print("\n=== 二つのクロックの比（第2回の核）===")
Nt=math.log(t0/tP); NT=math.log(TP/T0)
print(f"  ln(t0/tP)={Nt:.2f}  ln(TP/T0)={NT:.2f}  比={NT/Nt:.4f}")
print(f"  p=1 を課すと今日の温度は T0={TP*math.exp(-Nt):.3e} K（実測 2.7255 K の {TP*math.exp(-Nt)/T0:.2e} 倍）")
print(f"  逆に T0 を合わせると、プランク時刻の温度は TP の {math.exp(Nt-NT):.3e} 倍")
