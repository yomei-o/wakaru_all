# -*- coding: utf-8 -*-
"""第6回 06節の経験則 A·n̄ = C q³ を、記事に載っている実測値だけで検算し直す。
2026-08-29 の見直し。後続の測定（q を 0.06 付近まで広げたもの）で
『指数はちょうど3』は窓の狭さが作った見かけだと分かったので、
記事の表そのものから同じ結論が読めるかを確かめる。"""
import math

# 記事 06節の表（k0, q, n̄, A·n̄）
DAT = [(0, 0.473, 132.5, 0.4011),
       (1, 0.440, 142.7, 0.3353),
       (2, 0.402, 154.7, 0.2503),
       (3, 0.357, 168.9, 0.1632),
       (4, 0.299, 187.1, 0.1113),
       (5, 0.221, 211.7, 0.0396)]
T = 32


def lsq(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    a = sxy / sxx
    b = my - a * mx
    res = [y - (a * x + b) for x, y in zip(xs, ys)]
    chi = sum(r * r for r in res)
    sa = math.sqrt(chi / (n - 2) / sxx)
    return a, b, chi, sa


print("=== ① 記事の表そのもので、指数を自由にして当てる ===")
xs = [math.log(d[1]) for d in DAT]
ys = [math.log(d[3]) for d in DAT]
th, lc, chi, sth = lsq(xs, ys)
print("  A·n̄ = C q^θ を当てると θ = %.2f ± %.2f,  C = %.2f" % (th, sth, math.exp(lc)))
print("  残差二乗和 = %.5f（対数で）" % chi)
print("  → 記事が固定した θ=3 は、当てはめた値 %.2f と %.1fσ 離れている。" % (th, abs(th - 3) / sth))

print("")
print("=== ② しきい値つき A·n̄ = C(q−q_c)^θ を当てる ===")
best = None
qc = -0.20
while qc < 0.20:
    if all(d[1] - qc > 0 for d in DAT):
        xs2 = [math.log(d[1] - qc) for d in DAT]
        a, b, c2, sa = lsq(xs2, ys)
        if best is None or c2 < best[2]:
            best = (a, b, c2, sa, qc)
    qc += 0.001
a, b, c2, sa, qcb = best
print("  最良：q_c = %.3f,  θ = %.2f ± %.2f,  C = %.2f" % (qcb, a, sa, math.exp(b)))
print("  残差二乗和 = %.5f（θ 固定なしの %.5f より小さい）" % (c2, chi))
print("  → 記事の 6 点だけでも、しきい値を許すと当てはまりが良くなる。")
print("     ただしこの 6 点は q∈[0.22,0.47] しかないので q_c は決まらない（後続測定で 0.06±0.03）。")

print("")
print("=== ③ 縮退：q と n̄ は独立ではない ===")
print("  トーラスの恒等式  q = 1 − 2T·n̄/N  （T=%d）" % T)
print("  %-6s %-8s %-8s %-10s %s" % ("k0", "q(実測)", "n̄", "N=2Tn̄/(1-q)", "q(N=16000)"))
for k0, q, nb, An in DAT:
    Nimp = 2 * T * nb / (1 - q)
    qpred = 1 - 2 * T * nb / 16000.0
    print("  %-6d %-8.3f %-8.1f %-10.0f %.3f" % (k0, q, nb, Nimp, qpred))
print("  → N は 16.1k→17.4k と 8%% しか動いていない。つまりこのスキャンの中で")
print("     n̄ は q のほぼ一意な関数。q と n̄ を独立変数として扱えない。")

print("")
print("=== ④ 縮退の帰結：A = C' q^a n̄^b は決まらない ===")
print("  A·n̄ = C q^θ は、恒等式を使えば A = (2TC/N) q^θ/(1−q) とも書ける。")
print("  同じ 6 点に A = C' q^a n̄^b を当てると、(a,b) は一本の縮退線しか決まらない：")
xq = [math.log(d[1]) for d in DAT]
xn = [math.log(d[2]) for d in DAT]
ya = [math.log(d[3] / d[2]) for d in DAT]     # log A
slope, _, _, _ = lsq(xq, xn)
print("  log n̄ を log q に当てると 傾き %.3f（相関係数の絶対値がほぼ 1）" % slope)
print("  → b を 1 動かすと a が %.2f 動くだけで、残差はほとんど変わらない。" % slope)
print("     （記事の形 A·n̄ = C q^θ は b = −1、θ = a に当たる）")
for b_ in (-2.0, -1.5, -1.0, -0.5, 0.0, 0.5):
    yy = [la - b_ * xnn for la, xnn in zip(ya, xn)]
    aa, bb, cc, _ = lsq(xq, yy)
    print("     b=%.1f と決め打つと a=%.2f、残差二乗和 %.5f" % (b_, aa, cc))
print("  ★ 残差はどれもほぼ同じ。データは (a,b) の組を選べない。")
print("     記事が n̄ を掛けたのは『ミニ超空間の形 A=1/(Γn̄)』という理論側の理由であって、")
print("     このデータが n̄ の指数を決めたわけではない ── ここは記事に書かれていない。")

print("")
print("=== ⑤ 結論（記事に足すべきこと）===")
print("  (1) θ=3 はこの窓（q∈[0.22,0.47]）での見かけ。窓を広げると θ≈2.55、q_c≈0.06。")
print("  (2) q と n̄ は恒等式で結ばれており、このスキャンでは独立変数ではない。")
print("  (3) 誤差棒（±0.108 など）はジャックナイフで、統計を増やすと 1.5〜2 倍に膨らんだ。")
