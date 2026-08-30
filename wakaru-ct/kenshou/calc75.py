# -*- coding: utf-8 -*-
# 深掘り⑳：強い力を、単純な計算の層に分解できるか
#           ── 実際に当てはめて、各層が何ビット説明するか測る
import math

hbarc = 197.3269804          # MeV·fm

print("=== ① 方針 ── 一気に解かず、層に切る ===")
layers = [
    ("第 0 層", "なぜ 1 GeV なのか（スケールそのもの）", "**次元転移**", "1 行"),
    ("第 1 層", "結合定数がどう走るか", "**1 ループの β 関数**", "1 行"),
    ("第 2 層", "全部の質量が Λ の O(1) 倍", "**次元解析**", "暗算"),
    ("第 3 層", "その O(1) の**中身のパターン**", "**構成子＋超微細**", "四則演算"),
    ("第 4 層", "残り", "**格子 QCD**", "10¹⁹ flops"),
]
print("  %-10s %-38s %-22s %s" % ("層", "何を決めるか", "使う道具", "計算の重さ"))
for a, b, c, d in layers:
    print("  %-10s %-38s %-22s %s" % (a, b, c, d))
print("")
print("  ★ **各層が何ビット説明するかを、実際に測る。**")

print("")
print("=== ② 第 0 層 ── スケールは 1 個の数から出る ===")
print("  Λ = μ · exp(−2π / (b₀ α_s(μ)))     b₀ = 11 − 2n_f/3")
nf = 5
b0 = 11 - 2 * nf / 3.0
mz, asz = 91.1876, 0.1180
lam = mz * math.exp(-2 * math.pi / (b0 * asz))
print("  n_f = %d → b₀ = %.3f、α_s(M_Z) = %.4f" % (nf, b0, asz))
print("  → Λ ≈ **%.0f MeV**（1 ループなので粗い。2 ループなら 210 MeV）" % (lam * 1000))
print("")
dec = math.log10(1.22e22 / 300.0)
print("  プランク質量 1.22×10²² MeV から Λ ≈ 300 MeV まで **%.1f 桁**" % dec)
b_gap = dec / math.log10(2)
b_cost = math.log2(b_gap)
print("  = **%.0f ビットの階層**。これを買う値段は log₂(%.0f) = **%.1f ビット**" %
      (b_gap, b_gap, b_cost))
print("  ★ **%.0f ビットを %.1f ビットで買っている（圧縮 %.0f 倍）。**" %
      (b_gap, b_cost, b_gap / b_cost))
print("     ── 深掘り⑩の B → log₂B。**強い力の最大の圧縮はここ**。")
print("     指数関数 1 個で、原子核のスケールが全部決まる。")

print("")
print("=== ③ 第 2 層 ── 次元解析だけで、どこまで行くか ===")
L = 332.0
things = [("π", 138.0), ("ρ", 775.3), ("K", 495.6), ("K*", 893.6), ("φ", 1019.5),
          ("核子", 938.9), ("Δ", 1232.0), ("Λ_baryon", 1115.7), ("Σ", 1193.2),
          ("Σ*", 1384.6), ("Ξ", 1318.3), ("Ξ*", 1533.4), ("Ω", 1672.5)]
print("  Λ_MS(n_f=3) ≈ %.0f MeV で全部を割る：" % L)
print("  %-14s %-12s %s" % ("ハドロン", "質量 [MeV]", "Λ の何倍"))
for nm, m in things:
    print("  %-14s %-12.1f %.2f" % (nm, m, m / L))
rs = [m / L for _, m in things]
print("")
print("  ★ **全部 %.2f 〜 %.2f 倍**。桁で外れているものは一つも無い。" % (min(rs), max(rs)))
print("     ── **これが「強い力の量は Λ の O(1) 倍」の中身**。")
print("     ただし 0.42 と 5.04 では **12 倍の開き**がある。ここを次の層で潰す。")

print("")
print("=== ④ 第 3 層 ── 構成子クォークと超微細だけで組む ===")
print("  法則はこれだけ：")
print("    M = Σ(構成子の質量) + A × Σ_{i<j} ⟨S_i·S_j⟩ / (m_i m_j)")
print("  ⟨S_i·S_j⟩ は**スピンの足し算だけ**で出る（動力学は一切なし）：")
sp = [
    ("中間子 S=0（π, K）", "−3/4"),
    ("中間子 S=1（ρ, K*, φ）", "+1/4"),
    ("バリオン J=1/2 同種3個（N）", "−3/4"),
    ("バリオン J=3/2（Δ, Ω）", "+3/4"),
    ("Λ（ud が S=0）", "ud: −3/4、s とは 0"),
    ("Σ（ud が S=1）", "ud: +1/4、s とは −1"),
]
print("  %-34s %s" % ("状態", "Σ⟨S_i·S_j⟩"))
for a, b in sp:
    print("  %-34s %s" % (a, b))

# ---- 中間子のフィット（3 パラメータ）----
mes = [("π", 138.0, 'uu', -0.75), ("ρ", 775.3, 'uu', 0.25),
       ("K", 495.6, 'us', -0.75), ("K*", 893.6, 'us', 0.25),
       ("φ", 1019.5, 'ss', 0.25)]


def mes_model(p, kind, ss):
    mu, ms, A = p
    m1 = mu if kind[0] == 'u' else ms
    m2 = mu if kind[1] == 'u' else ms
    return m1 + m2 + A * ss / (m1 * m2)


# ---- バリオンのフィット（3 パラメータ）----
# (名前, 質量, u の数, s の数, [(係数, 質量ペア)])
bar = [
    ("N",   938.9, 3, 0, [(-0.75, 'uu')]),
    ("Δ",  1232.0, 3, 0, [(0.75, 'uu')]),
    ("Λ",  1115.7, 2, 1, [(-0.75, 'uu')]),
    ("Σ",  1193.2, 2, 1, [(0.25, 'uu'), (-1.0, 'us')]),
    ("Σ*", 1384.6, 2, 1, [(0.25, 'uu'), (0.5, 'us')]),
    ("Ξ",  1318.3, 1, 2, [(0.25, 'ss'), (-1.0, 'us')]),
    ("Ξ*", 1533.4, 1, 2, [(0.25, 'ss'), (0.5, 'us')]),
    ("Ω",  1672.5, 0, 3, [(0.75, 'ss')]),
]


def bar_model(p, nu, ns, terms):
    mu, ms, A = p
    m = nu * mu + ns * ms
    for coef, pair in terms:
        m1 = mu if pair[0] == 'u' else ms
        m2 = mu if pair[1] == 'u' else ms
        m += A * coef / (m1 * m2)
    return m


def fit(p0, resid):
    p = list(p0)
    step = [30.0, 30.0, 5e6]
    for _ in range(400):
        for i in range(len(p)):
            best = resid(p)
            for d in (+step[i], -step[i]):
                q = list(p); q[i] += d
                if q[i] <= 0:
                    continue
                r = resid(q)
                if r < best:
                    best, p = r, q
        step = [s * 0.85 for s in step]
    return p


def rms_mes(p):
    return math.sqrt(sum((mes_model(p, k, s) - m) ** 2 for _, m, k, s in mes) / len(mes))


def rms_bar(p):
    return math.sqrt(sum((bar_model(p, nu, ns, t) - m) ** 2
                         for _, m, nu, ns, t in bar) / len(bar))


pm = fit([310.0, 480.0, 1.6e7], rms_mes)
pb = fit([363.0, 538.0, 5.0e6], rms_bar)

print("")
print("  中間子（データ 5、パラメータ 3）：m_u = %.0f、m_s = %.0f MeV" % (pm[0], pm[1]))
print("  %-10s %-12s %-12s %s" % ("", "実測", "模型", "ずれ"))
for nm, m, k, s in mes:
    v = mes_model(pm, k, s)
    print("  %-10s %-12.1f %-12.1f %+.1f %%" % (nm, m, v, (v - m) / m * 100))
print("  RMS = **%.1f MeV**" % rms_mes(pm))
print("")
print("  バリオン（データ 8、パラメータ 3）：m_u = %.0f、m_s = %.0f MeV" % (pb[0], pb[1]))
print("  %-10s %-12s %-12s %s" % ("", "実測", "模型", "ずれ"))
for nm, m, nu, ns, t in bar:
    v = bar_model(pb, nu, ns, t)
    print("  %-10s %-12.1f %-12.1f %+.1f %%" % (nm, m, v, (v - m) / m * 100))
print("  RMS = **%.1f MeV**" % rms_bar(pb))

print("")
print("=== ⑤ 各層が何ビット説明したか ===")
allm = [m for _, m in things]
mean = sum(allm) / len(allm)
sd0 = math.sqrt(sum((m - mean) ** 2 for m in allm) / len(allm))
resid = ([mes_model(pm, k, s) - m for _, m, k, s in mes] +
         [bar_model(pb, nu, ns, t) - m for _, m, nu, ns, t in bar])
sd3 = math.sqrt(sum(r * r for r in resid) / len(resid))
print("  %-26s %-30s %s" % ("層", "何を説明したか", "ビット"))
print("  %-26s %-30s %.0f ビットを %.1f ビットで" %
      ("第 0 層 次元転移", "スケールそのもの", b_gap, b_cost))

lo, hi = min(rs), max(rs)
b_prior = 4.0 / math.log10(2)        # 事前：Λ の 10⁻² 〜 10² 倍
b_after = math.log2(hi / lo)
print("  %-26s %-30s %.1f → %.1f、買い **%.1f ビット**（パラメータ 0）" %
      ("第 2 層 次元解析", "Λ の何倍かの幅",
       b_prior, b_after, b_prior - b_after))

b3 = math.log2(sd0 / sd3)
n_had = len(things)
pay3 = 6 * 5.37
print("  %-26s %-30s %.1f × %d = **%.0f ビット**（払い %.1f）" %
      ("第 3 層 構成子＋超微細", "13 個の質量のばらつき",
       b3, n_had, b3 * n_had, pay3))
print("")
print("    ばらつき（生）　　 σ₀ = %.0f MeV" % sd0)
print("    ばらつき（模型後） σ₃ = %.0f MeV" % sd3)
print("  ★ **%.0f → %.0f MeV。ハドロン 1 個あたり %.1f ビット。**" % (sd0, sd3, b3))
print("     払い 6 × 5.37 = %.1f、買い %.0f → **差し引き %+.0f ビット**。" %
      (pay3, b3 * n_had, b3 * n_had - pay3))

print("")
print("=== ⑥ しかも、パラメータを一つも足さない予言が残る ===")
free = []
# Gell-Mann–Okubo
mN, mXi, mLam, mSig = 938.92, 1318.3, 1115.68, 1193.15
gmo_l, gmo_r = (mN + mXi) / 2, (3 * mLam + mSig) / 4
free.append(("Gell-Mann–Okubo", "(m_N+m_Ξ)/2 = (3m_Λ+m_Σ)/4",
             abs(gmo_l - gmo_r) / gmo_r))
# 十重項の等間隔
dec10 = [1232.0, 1384.6, 1533.4, 1672.5]
gaps = [dec10[i + 1] - dec10[i] for i in range(3)]
free.append(("十重項の等間隔", "Δ→Σ*→Ξ*→Ω の間隔が等しい",
             (max(gaps) - min(gaps)) / (sum(gaps) / 3)))
# Coleman–Glashow
cg_l = (938.272 - 939.565) + (1314.86 - 1321.71)
cg_r = 1189.37 - 1197.45
free.append(("Coleman–Glashow", "(p−n)+(Ξ⁰−Ξ⁻) = Σ⁺−Σ⁻",
             abs(cg_l - cg_r) / abs(cg_r)))
# 超微細の質量スケーリング
r_meas = (1384.6 - 1193.15) / (1232.0 - 938.92)
r_pred = pb[0] / pb[1]
free.append(("超微細のスケーリング", "(Σ*−Σ)/(Δ−N) = m_u/m_s",
             abs(r_meas - r_pred) / r_pred))
# 磁気能率
free.append(("磁気能率の比", "μ_n/μ_p = −2/3",
             abs(-1.91304273 / 2.7928473446 - (-2.0 / 3.0)) / (2.0 / 3.0)))
print("  %-24s %-38s %-12s %s" % ("関係", "中身", "ずれ [%]", "ビット"))
tot_free = 0.0
for nm, expr, r in free:
    b = -math.log2(r)
    tot_free += b
    print("  %-24s %-38s %-12.2f %.1f" % (nm, expr, r * 100, b))
print("  %-24s %-38s %-12s **%.1f**" % ("合計", "", "", tot_free))
print("")
print("  ★ **全部、紙と鉛筆。パラメータの追加はゼロ。合計 %.0f ビット。**" % tot_free)
print("     十重項の等間隔と Coleman–Glashow は、**動力学を一切使っていない**。")
print("     使ったのは **SU(3) の足し算と、スピンの足し算だけ**。")

print("")
print("=== ⑦ 質量以外も、同じ層で行けるか ===")
print("  MIT バッグ模型：**不確定性原理 ＋ 真空の一定圧力**、それだけ。")
print("    E(R) = (3×2.04 − 1.84)/R + (4/3)πR³B")
B4 = 145.0
Bv = B4 ** 4
K = 3 * 2.04 - 1.84
R = (K / (4 * math.pi * Bv)) ** 0.25
E = (4.0 / 3.0) * K / R
print("    B^(1/4) = %.0f MeV とすると：" % B4)
print("      dE/dR = 0 → R = **%.2f fm**、E = (4/3)K/R = **%.0f MeV**" %
      (R * hbarc, E))
print("      実測の核子質量 938.9 MeV に対して **%+.0f %%**" % ((E - 938.9) / 938.9 * 100))
print("  ★ **微分 1 回で陽子の質量が 15 % 以内。** グルーオン交換を足せば 938 に合う。")
print("     ── 閉じ込めを『一定の圧力』に置き換えるだけで、この精度。")

print("")
print("=== ⑧ 分解の結果 ===")
summary = [
    ("**なぜ 1 GeV か**", "指数関数 1 個", "**%.0f ビットを %.1f ビットで**" % (b_gap, b_cost), "1 行"),
    ("**どれも Λ の O(1) 倍**", "次元解析", "桁は全部当たる", "暗算"),
    ("**質量のパターン**", "構成子＋スピンの足し算", "**%.1f ビット / 6 パラメータ**" %
     math.log2(sd0 / sd3), "四則演算"),
    ("**パラメータ不要の関係 5 本**", "SU(3) とスピン", "**%.0f ビット / 0 パラメータ**" % tot_free, "紙と鉛筆"),
    ("**大きさとエネルギー**", "不確定性 ＋ 一定圧力", "15 % 以内", "微分 1 回"),
    ("残り（数 % 以下）", "格子 QCD", "─", "**10¹⁹ flops**"),
]
print("  %-30s %-24s %-30s %s" % ("何が", "何で", "どれだけ", "重さ"))
for a, b, c, d in summary:
    print("  %-30s %-24s %-30s %s" % (a, b, c, d))
print("")
print("  ★ **数 % までは、全部が単純な計算で届く。**")
print("     格子 QCD が要るのは **最後の数 % だけ**。")
print("  ★ そして層の切れ目が明確 ── ")
print("     **スケール（指数）／桁（次元解析）／パターン（足し算）／残り（数値計算）**。")

print("")
print("=== ⑨ 正直な線 ===")
print("  ・④の構成子質量は**この模型の中でだけ意味のある数**。")
print("    カレント質量（u ≈ 2 MeV）とは別物で、**閉じ込めを質量に繰り込んだ記法**。")
print("  ・π が %.0f MeV 実測に対して模型が高く出るのは既知の欠陥。" % 138.0)
print("    π は南部・ゴールドストン粒子で、構成子模型の枠外にある。")
print("  ・⑤の『ビット』は、あくまで**ばらつきの縮み**であって予言力ではない。")
print("    6 パラメータで 13 個を合わせているので、深掘り⑪の帳簿を別に取る必要がある。")
print("  ・⑥の 5 本のうち、十重項等間隔と GMO は**同じ SU(3) 破れの一次から出る**ので、")
print("    完全に独立ではない（合計ビットは上振れしている）。")
print("  ・⑦のバッグ模型は B と Z₀ という 2 個のパラメータ込み。『微分 1 回』は計算の話。")
