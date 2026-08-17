# -*- coding: utf-8 -*-
"""
step4: 格子から連続極限のハミルトニアンのスペクトルを取り出す。

これが「連続極限が存在する」の中身。転送行列 K の固有値 μ_k は
    μ_k = e^{-a E_k}          (a = 時間方向の格子間隔)
なので、-ln μ_k が a×(連続のエネルギー) になる。

連続側は自分で解いた（step4 の前半、sympy で確認済み）：
    H = -L ∂_L² + Λ L,   境界条件 ψ(0)=0
    → E_k = 2k√Λ,  k=1,2,3,…      ★ 比は 1:2:3:4:… ── パラメータ0個の予言

K は非対称だが、K = A D^{-1}（A は対称、D=diag(l)）なので
    S = D^{-1/2} A D^{-1/2}
と相似変換すれば実対称になり、固有値は同じ。
このとき内積の重みが 1/l になるが、連続側 H の自己共役な重みも dL/L ── 一致している。
（これ自体が、格子と連続が同じ内積を持っているという非自明なチェック）
"""
import sys, io
import numpy as np
from scipy.special import gammaln
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LN2 = np.log(2.0)


def spectrum(delta, LMAX, nev=8):
    """λ = ln2 + delta での転送行列の上位固有値"""
    lam = LN2 + delta
    l = np.arange(1, LMAX + 1, dtype=np.float64)
    L1 = l[:, None]; L2 = l[None, :]
    # S(l,l') = Γ(l+l')/(Γ(l)Γ(l')) / sqrt(l l') * e^{-λ(l+l')}
    E = (gammaln(L1 + L2) - gammaln(L1) - gammaln(L2)
         - 0.5 * np.log(L1) - 0.5 * np.log(L2) - lam * (L1 + L2))
    S = np.exp(E)
    w = np.linalg.eigvalsh(S)          # 実対称なので実固有値
    w = np.sort(w)[::-1]
    return w[:nev]


print("=== 連続側（自分で解いた結果） ===")
print("  H = -L ∂_L² + ΛL,  ψ(0)=0  →  E_k = 2k√Λ,  k=1,2,3,…")
print("  ★ 比 E_k/E_1 = k  ── 無次元の純粋な数。格子間隔にも Λ にも依らない")
print()

print("=== 格子： -ln μ_k の比を見る（フィット無し・パラメータ0個） ===")
print(f"{'δ=λ-ln2':>10}{'LMAX':>7}   " + "".join(f"{'-lnμ_'+str(k):>12}" for k in range(5)))
print(f"{'':>10}{'':>7}   " + "".join(f"{'比 /k=1':>12}" for k in range(5)))
rows = []
for delta, LMAX in [(0.05, 900), (0.02, 1100), (0.01, 1300), (0.005, 1500),
                    (0.002, 1800), (0.001, 2200), (0.0005, 2600)]:
    w = spectrum(delta, LMAX, nev=6)
    e = -np.log(w[:5])
    rows.append((delta, e))
    print(f"{delta:>10.4f}{LMAX:>7}   " + "".join(f"{x:>12.6f}" for x in e))
    print(f"{'':>10}{'':>7}   " + "".join(f"{x/e[0]:>12.5f}" for x in e))
    print()

print("=== 予想との突き合わせ ===")
print("  比が 1, 2, 3, 4, 5 に近づくか（δ→0 が連続極限）")
print(f"{'δ':>10}" + "".join(f"{'E'+str(k+1)+'/E1':>12}" for k in range(1, 5)) + f"{'ずれ最大':>12}")
for delta, e in rows:
    r = e / e[0]
    dev = max(abs(r[k] - (k + 1)) for k in range(1, 5))
    print(f"{delta:>10.4f}" + "".join(f"{r[k]:>12.6f}" for k in range(1, 5)) + f"{dev:>12.2e}")

print()
print("=== 間隔が √δ に比例するか（Λ ∝ δ なら E ∝ √Λ ∝ √δ） ===")
print(f"{'δ':>10}{'-lnμ_0':>14}{'(-lnμ_0)/√δ':>16}")
for delta, e in rows:
    print(f"{delta:>10.4f}{e[0]:>14.8f}{e[0]/np.sqrt(delta):>16.8f}")
print()
print("  → 一定値に近づけば、格子の刻み a と Λ の関係が正しく取れている証拠")

print()
print("=== 収束チェック（LMAX を変えても同じか） ===")
for LMAX in (1200, 1800, 2400, 3000):
    e = -np.log(spectrum(0.002, LMAX, nev=4))
    print(f"  LMAX={LMAX:>5}  -lnμ = " + " ".join(f"{x:.7f}" for x in e)
          + f"   比 = " + " ".join(f"{x/e[0]:.5f}" for x in e))
