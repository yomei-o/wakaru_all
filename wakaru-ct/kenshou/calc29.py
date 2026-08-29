# -*- coding: utf-8 -*-
# 第25回：物理法則は圧縮アルゴリズムか ── 記述長で理論を並べると、どこで崩れるか
import math
ln2 = math.log(2)

print("=== ① 法則そのものの長さ（式を書き下す文字数 → ビット）===")
# 1 文字 = log2(95) ビット（印字可能 ASCII 95 種）で見積もる
b = math.log2(95)
laws = [
    ("c・t=一定（膨張則）",     r"a\propto t"),
    ("ニュートン重力",           r"F=Gm_1m_2/r^2"),
    ("シュレディンガー方程式",   r"i\hbar\partial_t\psi=\hat H\psi"),
    ("ディラック方程式",         r"(i\gamma^\mu\partial_\mu-m)\psi=0"),
    ("マクスウェル（テンソル）", r"\partial_\mu F^{\mu\nu}=\mu_0J^\nu,\ \partial_{[\mu}F_{\nu\rho]}=0"),
    ("フリードマン方程式",       r"H^2=\frac{8\pi G}{3}\rho-\frac{kc^2}{a^2}+\frac{\Lambda c^2}{3}"),
    ("アインシュタイン方程式",   r"R_{\mu\nu}-\tfrac12Rg_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}"),
]
print("  %-26s %5s %8s" % ("法則", "文字", "ビット"))
for n, s in laws:
    print("  %-26s %5d %8.0f" % (n, len(s), len(s) * b))
sm_chars = 5000
print("  %-26s %5d %8.0f   ← 概算" % ("標準模型ラグランジアン(展開)", sm_chars, sm_chars * b))
L_at = len(laws[0][1]) * b
L_fried = len(laws[5][1]) * b
print("  → 最短は a∝t の %d 文字 = %.0f ビット" % (len(laws[0][1]), L_at))

print("")
print("=== ② 説明する数の個数 ===")
lmax = 2500
modes = sum(2 * l + 1 for l in range(2, lmax + 1))
print("  CMB の球面調和モード数（l=2..%d, TT のみ）= %s" % (lmax, format(modes, ",")))
print("    TT+TE+EE なら ×3 = %s" % format(3 * modes, ","))
print("  ΛCDM のパラメータ数 = 6")
print("    → 圧縮率 = %s 倍（TT のみ）／ %s 倍（TT+TE+EE）"
      % (format(modes // 6, ","), format(3 * modes // 6, ",")))
for nm in (10, 100, 1000):
    k = nm * (nm - 1) // 2
    print("  リュードベリ公式（R∞ 1 個）：n≤%d の水素線 %s 本 → 圧縮率 %s 倍"
          % (nm, format(k, ","), format(k, ",")))
print("  一般相対論：自由パラメータ 0 個 → 圧縮率は形式的に無限大")

print("")
print("=== ③ パラメータの値段と、外したときの罰金（第20回の再利用）===")
N = 1701
aic = 1 / ln2
bic = 0.5 * math.log2(N)
dchi2 = 213.0
fit = dchi2 / (2 * ln2)
print("  データ点 N = %d（Planck の binned C_l）" % N)
print("  パラメータ 1 個の値段：AIC %.3f bit ／ BIC %.3f bit" % (aic, bic))
print("  c・t=一定 が失う当てはまり Δχ² = %.0f → %.1f bit" % (dchi2, fit))
print("  減らせるパラメータ 1 個ぶんの得 = %.2f bit" % bic)
print("  差し引き = %+.1f bit  → オッズ比 2^%.0f = %.2e で不利" % (bic - fit, fit - bic, 2 ** (fit - bic)))
print("  ★ 第3回の判決を、圧縮の言葉だけで書き直すとこうなる（判定は蒸し返さない）")

print("")
print("=== ④ 逆説：短い理論ほど壊れやすい ===")
print("  パラメータ k 個の理論が持つ『逃げ場』：")
for k in (0, 1, 6, 19, 25):
    tag = "合わせにいくことが原理的にできない" if k == 0 else ("%d 個の方向に逃げられる" % k)
    print("    k=%2d → %s" % (k, tag))
print("  MDL の圧縮率と、ポパーの反証可能性は同じ軸の裏表：")
print("    圧縮率が高い ⟺ パラメータが少ない ⟺ 逃げ場がない ⟺ 反証されやすい")
print("  → a∝t は最短（%.0f ビット）・パラメータ 0 個。したがって最も反証されやすく、実際に反証された。"
      % L_at)
print("     『圧縮率が高い＝良い理論』ではない。圧縮率は良さではなく、掛け金の大きさ。")

print("")
print("=== ⑤ 法則の長さを MDL に入れようとすると、崩れる ===")
print("  総記述長 L = L(法則) + L(パラメータ) + L(残差)")
print("  同じモデル・同じデータを、二通りの数え方で測る：")
print("")
print("  【書き方 A】a∝t を『フリードマン式に足す拘束』と数える")
A = []
for n, Ll, k, Lr in [("ΛCDM", L_fried, 6, 0.0), ("c・t=一定", L_fried + L_at, 5, fit)]:
    tot = Ll + k * bic + Lr
    A.append(tot)
    print("    %-10s L(法則)=%6.0f  L(param)=%6.1f  L(残差)=%6.1f  合計 %7.1f bit"
          % (n, Ll, k * bic, Lr, tot))
print("    → c・t=一定 の負け %+.0f bit" % (A[1] - A[0]))
print("")
print("  【書き方 B】a∝t を『フリードマン式を丸ごと置き換える』と数える")
B = []
for n, Ll, k, Lr in [("ΛCDM", L_fried, 6, 0.0), ("c・t=一定", L_at, 5, fit)]:
    tot = Ll + k * bic + Lr
    B.append(tot)
    print("    %-10s L(法則)=%6.0f  L(param)=%6.1f  L(残差)=%6.1f  合計 %7.1f bit"
          % (n, Ll, k * bic, Lr, tot))
print("    → c・t=一定 の勝ち %+.0f bit" % (B[0] - B[1]))
print("")
print("  ★ 同じモデル・同じデータで、結論がひっくり返った。")
print("    差の正体は法則の文字数 %.0f ビットだけ。これは『どの言語で書くか』で動く。" % L_fried)
print("    → コルモゴロフ複雑度の不変性定理：記述長は、言語に依る定数を除いてしか決まらない。")
print("      その『定数』が、ここでは勝敗をひっくり返せる大きさを持っている。")

print("")
print("=== ⑥ では、圧縮率のどこが信用できるのか ===")
print("  L(法則) ：記述言語に依存。今回の例で %.0f ビット動いた。→ 使えない" % L_fried)
print("  L(param)：パラメータの個数は再パラメトライズで変わらない。%.2f bit/個。→ 使える" % bic)
print("  L(残差) ：尤度はデータだけで決まる。%.1f bit。→ 使える" % fit)
print("  → 後ろ二つだけで比べると %+.1f bit（③と同じ）。第3回の判決はこちらにしか依存していない。"
      % (bic - fit))
print("  ★ 「式が短いから良い理論」は、情報理論の言葉では支えられない。")

print("")
print("=== ⑦ 第1回とつなぐ：宇宙自身の圧縮率 ===")
n_bits = 2.9556e122
S = 3.1e104
print("  地平面の容量 n = %.3e bit" % n_bits)
print("  実際に使われている k = S/ln2 = %.3e bit" % (S / ln2))
print("  → 宇宙の状態は、容量の %.2e に収まっている（第6回・第23回）" % (S / ln2 / n_bits))
print("  一方、物理法則が使うパラメータはたかだか 25 個 = %.0f bit 程度。" % (25 * bic))
print("  しかし法則は初期条件を圧縮しない。%.2e ビットの内訳を持っているのは、法則ではなく履歴。"
      % (S / ln2))
