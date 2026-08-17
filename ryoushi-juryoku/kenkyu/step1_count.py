# -*- coding: utf-8 -*-
"""
step1: 2次元 CDT の帯（ストリップ）の数え上げを、力ずくの列挙で確かめる。

設定：
  時刻 t の空間スライスは長さ l の輪（頂点 l 個・リンク l 本）。
  時刻 t+1 は長さ l' の輪。
  そのあいだを三角形で埋める。下のリンクを底辺にするものが l 個（上向き）、
  上のリンクを底辺にするものが l' 個（下向き）。合計 l+l' 個。

幾何の表し方（これがすべて）：
  下の各リンク i (=0..l-1) について、その上向き三角形の頂点 apex[i] ∈ Z_{l'} を決める。
  apex は輪を一周するあいだ後戻りしない（因果的＝葉層が保たれる条件）。
  つまり d_i = apex[i+1] - apex[i] >= 0、Σ d_i = l'。
  境界に番号が付いている（下の頂点0・上の頂点0が指定されている）ので apex[0] も自由。

  → 数は  l' * C(l+l'-1, l-1)  になるはず。これを力ずくで確かめる。
"""
import sys, io
from math import comb, factorial, log, pi
from itertools import product
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def brute_strips(l, lp):
    """下リンク -> 上頂点 の単調な巻き付きを全部作って、幾何として重複しないか確かめる。"""
    seen = set()
    # d_i >= 0, sum = lp を全部
    def compositions(n, k):
        if k == 1:
            yield (n,)
            return
        for first in range(n + 1):
            for rest in compositions(n - first, k - 1):
                yield (first,) + rest
    for a0 in range(lp):                       # apex[0]
        for d in compositions(lp, l):          # 各下リンクで上を何個進むか
            apex = []
            a = a0
            for i in range(l):
                apex.append(a % lp)
                a += d[i]
            # 三角形の一覧を作る（上向き：下リンク i と 上頂点 apex[i]）
            tris = []
            for i in range(l):
                tris.append(('U', i, (i + 1) % l, apex[i]))
            # 下向き：上リンク j と、その底になる下頂点
            # 上頂点 j から j+1 へ進む間に下側は動かないので、その下頂点を求める
            a = a0
            pos = {}
            for i in range(l):
                for s in range(d[i]):
                    pos[(a + s) % lp] = (i + 1) % l     # 上リンク (a+s -> a+s+1) の底になる下頂点
                a += d[i]
            for j in range(lp):
                tris.append(('D', j, (j + 1) % lp, pos[j]))
            key = (tuple(sorted(tris)))
            seen.add(key)
    return len(seen)


def formula(l, lp):
    return lp * comb(l + lp - 1, l - 1)


print("=== 帯の三角形分割の数 N(l,l') ===")
print(f"{'l':>3}{'l\'':>4}{'力ずく':>10}{'式':>10}{'(l+l\'-1)!/((l-1)!(l\'-1)!)':>28}  一致")
ok = True
for l in range(1, 7):
    for lp in range(1, 7):
        if l * lp > 30:      # 列挙が爆発しない範囲で
            continue
        b = brute_strips(l, lp)
        f = formula(l, lp)
        g = factorial(l + lp - 1) // (factorial(l - 1) * factorial(lp - 1))
        same = (b == f == g)
        ok &= same
        print(f"{l:>3}{lp:>4}{b:>10}{f:>10}{g:>28}  {'OK' if same else 'ちがう'}")
print("すべて一致" if ok else "★不一致あり")

print()
print("=== 対称性（時間反転） N(l,l') == N(l',l) ===")
bad = [(l, lp) for l in range(1, 20) for lp in range(1, 20) if formula(l, lp) != formula(lp, l)]
print("対称" if not bad else f"★非対称: {bad[:5]}")

print()
print("=== 母関数の特異点 = 臨界結合 ===")
print("  G(x,y;1) = Σ N(l,l') (gx)^l (gy)^l' を計算すると g^2 xy/(1-gx-gy)^2")
print("  → 特異点は gx+gy=1。x=y=1 で g_c = 1/2、つまり λ_c = ln 2 = %.10f" % log(2))
# 数値で確かめる：部分和が g<1/2 で収束し g>1/2 で発散する
for g in (0.45, 0.49, 0.50, 0.51, 0.55):
    tot = 0.0
    L = 400
    for l in range(1, L + 1):
        for lp in range(1, L + 1):
            if l + lp > L:
                continue
            tot += formula(l, lp) * g ** (l + lp)
    print(f"    g={g:.2f}  Σ_(l+l'<=400) N g^(l+l') = {tot:.6e}")
