# -*- coding: utf-8 -*-
"""
step2: 「素の作用には運動項が無いのに、数え上げから運動項が生える」を厳密に出す。

2次元では曲率項 ∫√g R は位相不変量（オイラー標数）なので定数。
だから素の格子作用は体積項だけ：
        S_bare = λ N   （N = 三角形の総数）
運動項は一行も入っていない。

ところが配位の重みは  (帯の数) × e^{-λN}  なので、体積プロファイル {l_t} についての
有効作用は
        S_eff[{l}] = λ Σ_t (l_t + l_{t+1})  −  Σ_t ln N(l_t, l_{t+1})
第2項がエントロピー。step1 で N(l,l') = (l+l'-1)!/((l-1)!(l'-1)!) = 1/B(l,l') と確かめた。

これを大きい l で展開すると何が出るかを、厳密値と突き合わせて確かめる。
"""
import sys, io
from math import comb, lgamma, log, pi, sqrt
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LN2 = log(2.0)


def lnN(l, lp):
    """ln N(l,l') = -ln B(l,l') = lnΓ(l+l') - lnΓ(l) - lnΓ(l')  （厳密）"""
    return lgamma(l + lp) - lgamma(l) - lgamma(lp)


def lnN_asym(l, lp):
    """
    導出：u=l-1, v=l'-1, n=u+v として
        ln N = ln(n+1)! - ln u! - ln v! = ln(n+1) + ln C(n,u)
    C(n, n/2+Δ) の Stirling 展開（Δ=(u-v)/2）：
        ln C = n ln2 - (1/2)ln(πn/2) - 2Δ²/n + O(Δ⁴/n³)
    よって
        ln N ≈ (l+l'-2) ln2  -  (l-l')²/(2(l+l'-2))  +  ln(l+l'-1)  -  (1/2)ln(π(l+l'-2)/2)
    """
    n = l + lp - 2
    if n <= 0:
        return lnN(l, lp)
    d = l - lp
    return n * LN2 - d * d / (2.0 * n) + log(n + 1) - 0.5 * log(pi * n / 2.0)


print("=== ln N(l,l') の展開が合っているか（厳密 vs 漸近） ===")
print("導出した式:  ln N ≈ (l+l'-2)ln2 - (l-l')²/(2(l+l'-2)) + ln(l+l'-1) - ½ln(π(l+l'-2)/2)")
print()
print(f"{'l':>6}{'l\'':>6}{'厳密 ln N':>14}{'漸近':>14}{'差':>12}{'相対差':>12}")
for l, lp in [(10, 10), (10, 12), (50, 50), (50, 56), (100, 100), (100, 110),
              (1000, 1000), (1000, 1040), (10000, 10000), (10000, 10200)]:
    e = lnN(l, lp); a = lnN_asym(l, lp)
    print(f"{l:>6}{lp:>6}{e:>14.6f}{a:>14.6f}{a-e:>12.2e}{(a-e)/e:>12.2e}")

print()
print("=== 有効作用の形 ===")
print("  S_eff = Σ_t [ λ(l_t+l_{t+1}) - ln N(l_t,l_{t+1}) ]")
print("        = Σ_t [ (λ - ln2)(l_t+l_{t+1}) + (l_{t+1}-l_t)²/(2(l_t+l_{t+1}-2)) + 2ln2 - (対数項) ]")
print()
print("  ★ 運動項 (l_{t+1}-l_t)²/(2(l_t+l_{t+1}-2)) ≈ (Δl)²/(4l)  ── 符号は【正】")
print("  ★ 素の作用には運動項が一行も無い。これは100%エントロピー（二項係数）から来ている")
print("  ★ 体積項の係数は (λ - ln2)。正になる条件は λ > ln2 = λ_c ── 無次元比 λ/ln2 > 1")
print()

# 運動項の符号を、厳密値から数値的に取り出して確かめる
print("=== 運動項の符号と係数を厳密値から取り出す ===")
print("  l を固定して Δl を振り、 -ln N を Δl の2次でフィットする")
print(f"{'l':>8}{'2次係数(厳密フィット)':>24}{'1/(4l) の予想':>16}{'比':>10}")
for l in (25, 50, 100, 400, 1600, 6400):
    xs, ys = [], []
    for dl in range(-6, 7):
        lp = l + dl
        xs.append(dl); ys.append(-lnN(l, lp))
    # y = a + b x + c x^2 でフィット
    import numpy as np
    c2, c1, c0 = np.polyfit(xs, ys, 2)
    pred = 1.0 / (4.0 * l)
    print(f"{l:>8}{c2:>24.8e}{pred:>16.8e}{c2/pred:>10.5f}")

print()
print("=== 連続の第9回との対比 ===")
print("  第9回：φ=1+ε sin(2πkx) を細かくすると S_E ∝ -k² → いくらでも負 → e^{-S_E} が爆発")
print("  ここ  ：l_t を細かく振動させると 運動項 (Δl)²/(4l) が【増える】 → 重みは小さくなる")
print("  同じ自由度（空間体積＝共形因子）なのに符号が逆。差はエントロピーを数えたかどうかだけ。")
print()
# 実際に「さざ波」を入れて有効作用が増えることを厳密値で見る
print("  さざ波 l_t = L + A(-1)^t を入れたときの S_eff（λ=ln2+0.05, T=64, L=200）:")
lam = LN2 + 0.05
T, L = 64, 200
for A in (0, 1, 2, 5, 10, 20, 40):
    ls = [L + A * (1 if t % 2 == 0 else -1) for t in range(T)]
    S = 0.0
    for t in range(T):
        a, b = ls[t], ls[(t + 1) % T]
        S += lam * (a + b) - lnN(a, b)
    print(f"    A={A:>3}   S_eff = {S:>14.4f}    重み e^-S = 10^{-S/log(10):>10.2f}")
