# -*- coding: utf-8 -*-
# 「c*t=一定」を、どんな a(t) でも実現する時間座標を作れるか（＝立場Aの検証）
#   ds^2 = -c0^2 dt^2 + a^2 dx^2
#   Omega=1/a で共形変換:  ds~^2 = -(c0/a)^2 dt^2 + dx^2
#   時間座標 T(t) に取り替え: c_B(T) = c0/(a T')     T' = dT/dt
#   c_B * T = C を要求 ->  dlnT/dt = c0/(a C)  ->  lnT = (c0/C) * eta
#   すなわち  T = exp(eta/eta0)     eta = ∫dt/a （共形時間）
import numpy as np

c0=1.0
def check(p, name, C=1.0, t0=1.0):
    # a = (t/t0)^p ,  eta = ∫dt/a
    t=np.logspace(-3,0.0,4001)*t0
    a=(t/t0)**p
    # eta を数値積分
    eta=np.concatenate([[0.0], np.cumsum(np.diff(t)/(0.5*(a[1:]+a[:-1])))])
    T=np.exp(c0*eta/C)
    # T' = dT/dt を数値微分し、c_B = c0/(a T')
    Tp=np.gradient(T,t)
    cB=c0/(a*Tp)
    prod=cB*T
    s=slice(50,-50)
    print(f"  {name:16s} p={p:.4f}  c_B*T = {prod[s].mean():.6f} ± {prod[s].std():.2e}"
          f"   （一定であるべき値 C={C}）")
    # T と 宇宙年齢 t の関係
    sl=np.polyfit(np.log(t[s]),np.log(T[s]),1)[0]
    print(f"                    d lnT/d lnt = {sl:.4f}"
          + ("   <- 宇宙年齢と一致（比が一定）" if abs(sl-1)<1e-2 else "   <- 宇宙年齢とは別物"))

print("=== どの膨張則でも c_B*T = 一定 にできるか ===")
for p,name in [(0.5,'放射'),(2/3,'物質'),(1.0,'c*t=const'),(0.3,'適当な冪')]:
    check(p,name)

print()
print("=== 各膨張則で、その時計 T は何の関数か ===")
print("  eta = ∫dt/a ∝ t^(1-p) （p≠1）,  eta = ln t （p=1）")
for p,name in [(0.5,'放射'),(2/3,'物質'),(1.0,'c*t=const')]:
    if abs(p-1)<1e-12:
        print(f"  {name:10s}: eta ∝ ln t     -> T = e^(eta/eta0) ∝ t      ← 宇宙年齢そのもの")
    else:
        print(f"  {name:10s}: eta ∝ t^{1-p:.4f}  -> T = e^(eta/eta0) ∝ exp(t^{1-p:.4f})")

print()
print("=== 立場Aのもとで残る唯一の主張 ===")
print("  d lnT / d lnt = (c0/C) * t/a ∝ t^(1-p)")
print("  これが一定（＝T が宇宙年齢に比例）になるのは p=1 のときだけ")
print("  T/t は時間どうしの比 = 無次元。だからここだけが観測にかかる。")
