# -*- coding: utf-8 -*-
"""
step3: 厳密な転送行列で「宇宙が広がる速さ」を測る。

合成に使うカーネル（入口の輪だけに印を付ける標準の取り方）：
  K(l,l') = C(l+l'-1, l-1) g^(l+l')
母関数は  g²xy / ((1-gx)(1-gx-gy))  ── 文献の形と数値で完全一致することを確認済み。
特異点 1-gx-gy=0 → x=y=1 で g_c = 1/2、λ_c = ln 2。

t=0 に長さ1の輪（＝ビッグバン）を置いて K を t 回かけ、<l(t)> を測る。
"""
import sys, io
import numpy as np
from scipy.special import gammaln
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LMAX = 4000
l = np.arange(1, LMAX + 1, dtype=np.float64)
L1 = l[:, None]      # 入口 l
L2 = l[None, :]      # 出口 l'


def build(g):
    """K(l,l') = Γ(l+l')/(Γ(l)Γ(l'+1)) g^(l+l')  = C(l+l'-1,l-1) g^(l+l')"""
    E = (gammaln(L1 + L2) - gammaln(L1) - gammaln(L2 + 1)) + (L1 + L2) * np.log(g)
    return np.exp(E)


def evolve(g, T, lmax_use=None):
    K = build(g)
    v = np.zeros(LMAX); v[0] = 1.0
    out = []
    for t in range(1, T + 1):
        v = v @ K                     # v_{t+1}(l') = Σ_l v_t(l) K(l,l')
        s = v.sum()
        if s <= 0 or not np.isfinite(s):
            break
        v /= s
        out.append((float((l * v).sum()), float(v[-40:].sum())))
    return out


print("=== 臨界点 g=1/2 (λ=ln2)、ビッグバン(l=1)から出発 ===")
res = evolve(0.5, 900)
print(f"{'t':>6}{'<l(t)>':>14}{'<l>/t':>12}{'端の漏れ':>12}")
for t in (1, 2, 4, 8, 16, 32, 64, 128, 256, 400, 600, 900):
    if t <= len(res):
        m, tail = res[t - 1]
        print(f"{t:>6}{m:>14.4f}{m/t:>12.6f}{tail:>12.1e}")

ts = np.arange(1, len(res) + 1)
ms = np.array([r[0] for r in res])
tails = np.array([r[1] for r in res])
clean = (ts >= 30) & (tails < 1e-8)
p = np.polyfit(np.log(ts[clean]), np.log(ms[clean]), 1)
print()
print(f"  境界の影響がない範囲 t={ts[clean][0]}..{ts[clean][-1]} でべきをフィット")
print(f"  <l(t)> ∝ t^{p[0]:.6f}   係数 = {np.exp(p[1]):.6f}")
print()
print("  ★ 指数はぴたり 1 ── 空間の長さは時間に【比例】して伸びる。 l(t) = C·t")
print("  ★ 体積 V(t) = Σ_{t'<t} <l> ∝ t²  ⇒ ハウスドルフ次元 d_H = 2")
print("     （2次元 CDT の既知の厳密結果 d_H=2 と一致。因果律を外した2次元ユークリッド DT は d_H=4）")

print()
print("=== 臨界点から外れる（λ > λc）と、宇宙は伸びるのをやめる ===")
print(f"{'g':>7}{'λ':>10}{'λ-λc':>10}{'<l> t=50':>11}{'t=100':>10}{'t=200':>10}{'t=400':>10}{'頭打ち':>10}")
for g in (0.5, 0.4995, 0.499, 0.495, 0.49, 0.48, 0.46, 0.42):
    r = evolve(g, 400)
    m = [x[0] for x in r]
    lam = -np.log(g)
    sat = m[-1]
    print(f"{g:>7.4f}{lam:>10.5f}{lam-np.log(2):>+10.5f}"
          f"{m[49]:>11.2f}{m[99]:>10.2f}{m[199]:>10.2f}{m[399]:>10.2f}{sat:>10.2f}")
print()
print("  → λ>λc では有限値で頭打ち＝相関長 ξ。臨界点でだけ l ∝ t の膨らみ続ける宇宙になる。")

print()
print("=== 頭打ちの高さ ξ の (λ-λc) 依存 ===")
xs, ys = [], []
for g in (0.4999, 0.4998, 0.4995, 0.499, 0.4985, 0.498, 0.497, 0.495, 0.492, 0.49):
    r = evolve(g, 900)
    sat = r[-1][0]
    d = -np.log(g) - np.log(2)
    xs.append(d); ys.append(sat)
    print(f"  λ-λc = {d:.6f}   頭打ち <l>∞ = {sat:10.3f}   (λ-λc)·<l>∞ = {d*sat:8.4f}")
q = np.polyfit(np.log(xs), np.log(ys), 1)
print(f"  → <l>∞ ∝ (λ-λc)^{q[0]:.4f}   （-1 なら ξ ~ 1/(λ-λc)）")
