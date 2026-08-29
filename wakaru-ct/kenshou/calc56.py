# -*- coding: utf-8 -*-
# 深掘り：定数の変化は 3 次元の問題 ── 感度行列に縮退はあるか
#
# 基本パラメータ（Flambaum らの標準的な取り方）
#   x1 = Δα/α
#   x2 = Δ(X_e)/X_e,  X_e = m_e / Λ_QCD
#   x3 = Δ(X_q)/X_q,  X_q = m_q / Λ_QCD   （m_q = (m_u+m_d)/2）
#
# 観測量はこの 3 つの線形結合しか測っていない。行列のランクと最悪方向を見る。
import math

# ---- 感度係数（文献値。幅があるので後で振る）----
S_SIGMA = 0.048     # d ln(m_p/Λ) / d ln X_q  ≈ σ_πN/m_p ≈ 45/938
S_GP = -0.087       # d ln g_p / d ln X_q     （Flambaum & Tedesco 2006）

def rows(sig=S_SIGMA, gp=S_GP):
    """(ラベル, [x1,x2,x3] の係数, 1σ 相当の上限, 赤方偏移)"""
    return [
        ("Mg/Fe 多重項（Δα/α）",        [1.0, 0.0, 0.0],                  1.0e-5, "z≈1〜4"),
        ("H₂ Lyman-Werner（Δμ/μ）",     [0.0, -1.0, sig],                 5.0e-6, "z≈2〜4"),
        ("NH₃・メタノール（Δμ/μ）",      [0.0, -1.0, sig],                 1.0e-7, "z≈0.7〜0.9"),
        ("21cm 対 光学（α²μg_p）",       [2.0, -1.0, sig + gp],            1.0e-6, "z≈0.2〜0.7"),
        ("OH 18cm（g_p(α²μ)^1.85）",     [3.70, -1.85, 1.85 * sig + gp],   1.0e-5, "z≈0.2〜0.8"),
    ]

def fisher(rs):
    F = [[0.0] * 3 for _ in range(3)]
    for _, r, s, _z in rs:
        w = 1.0 / (s * s)
        for i in range(3):
            for j in range(3):
                F[i][j] += w * r[i] * r[j]
    return F

def jacobi(A, iters=200):
    """対称 3x3 の固有値・固有ベクトル（ヤコビ法）"""
    n = 3
    a = [row[:] for row in A]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(iters):
        p, q, off = 0, 1, 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > off:
                    off, p, q = abs(a[i][j]), i, j
        if off < 1e-300:
            break
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        theta = 0.5 * (aqq - app) / apq
        t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
        c = 1.0 / math.sqrt(t * t + 1.0)
        s = t * c
        for k in range(n):
            akp, akq = a[k][p], a[k][q]
            a[k][p] = c * akp - s * akq
            a[k][q] = s * akp + c * akq
        for k in range(n):
            apk, aqk = a[p][k], a[q][k]
            a[p][k] = c * apk - s * aqk
            a[q][k] = s * apk + c * aqk
        for k in range(n):
            vkp, vkq = v[k][p], v[k][q]
            v[k][p] = c * vkp - s * vkq
            v[k][q] = s * vkp + c * vkq
    ev = [a[i][i] for i in range(n)]
    vecs = [[v[i][k] for i in range(n)] for k in range(n)]
    pairs = sorted(zip(ev, vecs), key=lambda t: -t[0])
    return pairs

NAMES = ["Δα/α", "ΔX_e/X_e", "ΔX_q/X_q"]

print("=== ① 観測量は、3 つの量の線形結合しか測っていない ===")
rs = rows()
print("  %-30s %-9s %-9s %-9s %-10s %s" % ("測定", "α", "X_e", "X_q", "1σ 上限", "赤方偏移"))
for lab, r, s, z in rs:
    print("  %-30s %-9.3f %-9.3f %-9.4f %-10.1e %s" % (lab, r[0], r[1], r[2], s, z))
print("")
print("  ★ **X_q（軽いクォーク質量）の列が、どれも極端に小さい。**")
print("     陽子質量が m_q に依存するのはシグマ項の %.3f だけ、g_p は %.3f。" % (S_SIGMA, S_GP))
print("     → 分光は X_q をほとんど見ていない。")

print("")
print("=== ② フィッシャー行列を対角化する ===")
F = fisher(rs)
pairs = jacobi(F)
print("  %-6s %-14s %s" % ("方向", "その方向の σ", "中身（固有ベクトル）"))
for k, (lam, vec) in enumerate(pairs):
    sig = 1.0 / math.sqrt(lam) if lam > 0 else float('inf')
    body = "  ".join("%+.3f·%s" % (vec[i], NAMES[i]) for i in range(3))
    print("  %-6s %-14.2e %s" % ("第%d" % (k + 1), sig, body))
best = 1.0 / math.sqrt(pairs[0][0])
worst = 1.0 / math.sqrt(pairs[-1][0])
print("")
print("  最良方向 %.2e、最悪方向 %.2e" % (best, worst))
print("  → **条件数 %.0f 倍、ビットで %.1f ビットの差**" % (worst / best, math.log2(worst / best)))
wv = pairs[-1][1]
purity = wv[2] ** 2
print("  ★ 最悪方向の **%.1f パーセントが X_q 成分** ── ほぼ純粋なクォーク質量方向。" % (100 * purity))

print("")
print("=== ③ 係数の不確かさを振っても、結論は動くか ===")
print("  シグマ項と g_p の感度は文献に幅がある。両端で回してみる：")
print("  %-16s %-16s %-12s %-12s %s" % ("σ_πN/m_p", "dln g_p/dln X_q", "最悪 σ", "条件数", "X_q 純度"))
for sg in (0.030, 0.048, 0.070, 0.128):
    for gp in (-0.040, -0.087, -0.150):
        ps = jacobi(fisher(rows(sg, gp)))
        w = 1.0 / math.sqrt(ps[-1][0])
        b = 1.0 / math.sqrt(ps[0][0])
        pur = ps[-1][1][2] ** 2
        print("  %-16.3f %-16.3f %-12.2e %-12.0f %.1f%%" % (sg, gp, w, w / b, 100 * pur))
print("  ★ **係数を 4 倍振っても、最悪方向はつねに X_q でほぼ 100 パーセント。**")
print("     この縮退は係数の細部ではなく、**構造から来ている**。")

print("")
print("=== ④ では X_q を縛っているのは何か ── 時代で並べる ===")
# 第2回の対数ステップ ln(t/t_P) と同じ目盛りに載せる
tP = 5.391247e-44
def step(t_s):
    return math.log(t_s / tP)
probes = [
    ("元素合成（重陽子の束縛エネルギー）", 1.0, 1.0e-2, "**強い**", "m_q → m_π → 核力"),
    ("CMB（再結合）", 1.2e13, None, "実質なし", "X_q への感度がほぼ無い"),
    ("クエーサー分光（z≈2〜4）", 3.29e9 * 3.1557e7, None, "**縮退**", "②の最悪方向"),
    ("オクロ天然原子炉（2 Gyr 前）", 12.0e9 * 3.1557e7, 1.0e-9, "**強い**", "¹⁴⁹Sm 共鳴は核力に敏感"),
    ("実験室（いま）", 13.79e9 * 3.1557e7, 1.0e-6, "中くらい", "時計の比較（年あたり）"),
]
print("  %-36s %-10s %-12s %-10s %s" % ("測り方", "対数ステップ", "|ΔX_q/X_q|", "強さ", "効く仕組み"))
for lab, t, lim, tag, how in probes:
    st = step(t)
    ls = ("%.1e" % lim) if lim else "──"
    print("  %-36s %-10.1f %-12s %-10s %s" % (lab, st, ls, tag, how))
print("")
gap_lo, gap_hi = step(1.0), step(12.0e9 * 3.1557e7)
print("  ★ **X_q を強く縛っているのは、元素合成（ステップ %.1f）とオクロ（ステップ %.1f）の二点だけ。**" %
      (gap_lo, gap_hi))
print("     そのあいだ **%.1f 対数ステップ**が、実質的に空白。" % (gap_hi - gap_lo))
total = 140.24
print("     全歴史 %.2f ステップのうち **%.0f パーセント**が、クォーク質量については未検証。" %
      (total, 100 * (gap_hi - gap_lo) / total))
print("  ※ 第30回では α について『データがあるのは全歴史の 29 パーセント』だった。")
print("     X_q はそれよりさらに悪く、**二つの孤立した点しかない**。")

print("")
print("=== ⑤ 核心 ── 見えない方向は、いちばん効く方向だった ===")
print("  X_q ＝ m_q/Λ_QCD が動くと、何が動くか：")
eff = [
    ("パイ中間子の質量", "m_π² ∝ m_q", "0.50", "核力の到達距離"),
    ("重陽子の束縛エネルギー", "d ln B_d / d ln m_q ≈ −1 前後", "1.0", "元素合成そのもの"),
    ("ホイル状態の位置", "d ln E_H / d ln m_q は大きい", "大", "炭素の生成"),
    ("陽子・中性子の質量差", "m_n−m_p は m_d−m_u に直結", "大", "陽子の安定性"),
    ("陽子質量そのもの", "σ 項ぶんだけ", "0.048", "**分光が見ているのはここだけ**"),
]
print("  %-24s %-34s %-8s %s" % ("動くもの", "感度", "係数", "効く先"))
for a, b, c, d in eff:
    print("  %-24s %-34s %-8s %s" % (a, b, c, d))
print("")
print("  ★ **分光が見ている 0.048 は、いちばん鈍いチャンネル。**")
print("     核物理が効くチャンネル（0.5〜1 以上）は、分光にはまったく載っていない。")
print("  ★ つまり：**定数の変化のうち、いちばん影響が大きい方向が、いちばん見えていない。**")

print("")
print("=== ⑥ ビットで言い直す ===")
a_bits = -math.log2(1.0e-7)          # μ（第55計算より）
q_bits_spec = -math.log2(worst)      # 分光だけでの X_q 方向
q_bits_oklo = -math.log2(1.0e-9)
q_bits_bbn = -math.log2(1.0e-2)
print("  α・μ 方向（分光、z≈0.9）        %.1f ビット" % a_bits)
print("  X_q 方向（分光だけ）             %.1f ビット   ← **%.1f ビットの穴**" %
      (q_bits_spec, a_bits - q_bits_spec))
print("  X_q 方向（オクロ、1 点のみ）      %.1f ビット" % q_bits_oklo)
print("  X_q 方向（元素合成、1 点のみ）    %.1f ビット" % q_bits_bbn)
print("  ★ 分光だけを見れば、**クォーク質量方向には %.0f ビットの盲点**がある。" %
      (a_bits - q_bits_spec))
print("     埋めているのは、時代の離れた二点（オクロと元素合成）だけ。")

print("")
print("=== ⑦ 模型ごとに、見えやすさは二通りある ===")
print("  ・**条件付き**：模型が方向を決めてくれる場合  σ = 1/√(uᵀFu)")
print("  ・**周辺化**  ：他の定数も自由に動ける場合    σ = √(uᵀF⁻¹u)")
print("  二つの比が、その方向が他とどれだけ縮退しているかを表す。")
print("")
models = [
    ("電磁的なディラトン（α だけ）", [1.0, 0.0, 0.0]),
    ("ヒッグス的なスカラー（m_e だけ）", [0.0, 1.0, 0.0]),
    ("**q̄q に結合するスカラー（m_q だけ）**", [0.0, 0.0, 1.0]),
    ("大統一ディラトン（R≈35 で連動）", [1.0, 35.0, 35.0]),
]
print("  %-42s %-14s %-14s %s" % ("模型が動かす方向", "条件付き σ", "周辺化 σ", "縮退の度合い"))
for lab, d in models:
    nrm = math.sqrt(sum(x * x for x in d))
    u = [x / nrm for x in d]
    # 条件付き： uᵀFu
    fu = 0.0
    for a in range(3):
        for b in range(3):
            fu += u[a] * F[a][b] * u[b]
    s_cond = 1.0 / math.sqrt(fu)
    # 周辺化： uᵀF⁻¹u を固有分解から
    var = 0.0
    for lam, vec in pairs:
        proj = sum(u[k] * vec[k] for k in range(3))
        var += proj * proj / lam
    s_marg = math.sqrt(var)
    print("  %-42s %-14.2e %-14.2e %.0f 倍" % (lab, s_cond, s_marg, s_marg / s_cond))
print("")
print("  ★ **模型が方向を決めてくれるなら、どれもよく見える**（条件付きの列）。")
print("     大統一ディラトンが 10⁻⁷ 台で縛られるのは、第55計算⑤の結論と整合する。")
print("  ★ ところが**方向を仮定しないと、q̄q 方向だけが 60 倍以上悪化する**。")
print("     ── これは『測れていない』のではなく、**他の定数と分離できていない**。")

print("")
print("=== ⑧ 盲点に隠れるには、どれだけ調整が要るか ===")
print("  縮退の正体は簡単：Δμ/μ = %.3f·x₃ − x₂ = 0 になればよい。" % S_SIGMA)
print("  → **x₂ = %.3f · x₃**、つまり m_e/Λ の変化が m_q/Λ の変化のちょうど %.1f パーセント。" %
      (S_SIGMA, 100 * S_SIGMA))
for xq in (1e-4, 1e-3):
    need = 1.0e-7 / (S_SIGMA * xq)
    print("    x₃ = %.0e で隠れるには、この比を **%.1e** の精度で合わせる必要がある（%.1f ビット）" %
          (xq, need, -math.log2(need)))
print("  ★ **盲点はあるが、そこに隠れるには %.0f 〜 %.0f ビットの調整が要る。**" %
      (-math.log2(1.0e-7 / (S_SIGMA * 1e-4)), -math.log2(1.0e-7 / (S_SIGMA * 1e-3))))
print("     ── 第48回の作法で言えば、**盲点に隠れる模型は、それ自体が微調整**。")
print("        穴は空いているが、通り抜けるには値段がかかる。これが正直な結論。")
