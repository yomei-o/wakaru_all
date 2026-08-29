# -*- coding: utf-8 -*-
# 第27回：インフレーションを、同じ手術にかける
#   「地平線問題を解く」という言い方の中に、二つの別物が同じ名前で入っている
import math
ln2 = math.log(2)
c = 299792458.0
Mpl = 2.435e18            # 換算プランク質量 [GeV]
hbar_GeVs = 6.582119569e-25
GeV_to_K = 1.16045e13
T0 = 2.725                # [K]
H0 = 2.184e-18            # [1/s]（67.4 km/s/Mpc）
gstar = 106.75

print("=== ① 手術：『地平線問題を解く』の中身を二つに分ける ===")
print("  (A) 因果的に繋げる      … 幾何の話。等価な書き換えでも達成できる")
print("  (B) ゆらぎのスペクトルを出す … 観測にかかる主張。n_s, r, 断熱性, ガウス性")
print("  → 第3回と同じ手術。以下、(A) がどれだけ『安い』かを数える。")

print("")
print("=== ② (A) は、a∝t なら 0 e-folds で済む ===")
print("  a∝t^p の粒子的地平線：d_p = ct/(1-p)")
for p in (0.5, 2.0 / 3, 0.9, 0.99):
    print("    p=%-5.3f  d_p = %.2f ct   （有限 → 地平線問題あり）" % (p, 1 / (1 - p)))
print("    p=1.000  d_p = ∞         （∫dt'/t' が対数発散 → 地平線問題なし）")
print("  ★ c・t=一定 は、地平線問題を e-folds 0・パラメータ 0 で消す。")
print("     つまり (A) は インフレーション固有の成果ではない。")
print("     地平線問題は『宇宙の問題』ではなく『減速する宇宙の問題』だった。")

print("")
print("=== ③ (A) の情報量は 20 KB（第17回）===")
patches = 1.0e4
bits = 1.6e5
print("  再結合時の因果的に切れたパッチ数 ≈ %.0e" % patches)
print("  合意に必要な情報 = %.1e bit = 20 KB（第17回）" % bits)
print("  1 パッチあたり %.0f bit（温度を 5 桁ぶん）" % (bits / patches))
print("  p=1 なら パッチ数 1 → 必要な情報 0 bit")

print("")
print("=== ④ (A) がインフレーションに要求する e-folds ===")
print("  条件：今日の共動ハッブル半径が、インフレーション開始時のそれの内側にあること")
print("    e^N ≥ (a_e/a_0)(H_inf/H_0)")
print("  %-14s %-12s %-12s %-10s %s" % ("V^(1/4)", "H_inf [1/s]", "T_reh [GeV]", "a_e/a_0", "N_min"))
res = {}
for V4 in (1e16, 1e13, 1e10, 1e6):
    V = V4 ** 4                                  # [GeV^4]
    H = math.sqrt(V / (3 * Mpl ** 2)) / hbar_GeVs  # [1/s]
    Treh = (30 * V / (math.pi ** 2 * gstar)) ** 0.25  # [GeV]
    ae = T0 / (Treh * GeV_to_K)
    N = math.log(ae * H / H0)
    res[V4] = N
    print("  %-14.0e %-12.3e %-12.3e %-10.3e %.1f" % (V4, H, Treh, ae, N))
N_hor = res[1e16]
print("  → GUT スケールなら N_min = %.1f。よく言われる『60』はこれ。" % N_hor)
print("  ★ N は自由パラメータではなく、(A) の要求から決まる。ここが重要。")

print("")
print("=== ⑤ (B)：同じ N が、n_s を予言する ===")
ns_obs, ns_err = 0.9649, 0.0042
print("  スローロールの標準結果（大場インフレーション一般）：n_s ≈ 1 − 2/N")
print("  (A) が決めた N = %.1f を入れると n_s = %.4f" % (N_hor, 1 - 2 / N_hor))
print("  観測（Planck 2018）        n_s = %.4f ± %.4f" % (ns_obs, ns_err))
N_ns = 2 / (1 - ns_obs)
sN = 2 / (1 - ns_obs) ** 2 * ns_err
print("  逆に n_s から N を出すと  N = %.1f ± %.1f" % (N_ns, sN))
print("  ずれ = %.2f σ" % (abs(N_hor - N_ns) / sN))
print("  ★ 別々の要求から決めた二つの N が、1σ 以内で一致した。")

print("")
print("=== ⑥ 第19回の手続きで、この一致の驚きをビットで測る ===")
lo, hi = 10.0, 1000.0
prior = math.log(hi / lo)
frac = sN / N_ns
s1 = math.log2(prior / frac)
band_lo, band_hi = 55.0, 70.0
p_band = math.log(band_hi / band_lo) / prior
s2 = -math.log2(p_band)
print("  事前範囲：N は 10〜1000 のあいだ（対数一様）→ ln レンジ %.3f" % prior)
print("  測り方 A：n_s から決まる相対幅 σ_N/N = %.4f  → 驚き %.1f bit" % (frac, s1))
print("  測り方 B：N が [%.0f,%.0f] に入る確率 %.4f → 驚き %.1f bit" % (band_lo, band_hi, p_band, s2))
print("  → およそ 4〜5 ビット。第19回の目盛りでは【偶然】の帯だが、")
print("     こちらには説明（同じ N が両方を決める）があるので【物理】に分類される。")

print("")
print("=== ⑦ 帳簿：c・t=一定 と並べる ===")
bic = 0.5 * math.log2(1701)
print("  %-16s %-14s %-16s %s" % ("", "払う", "買う", "差し引き"))
print("  %-16s %-14s %-16s %s" % ("インフレーション",
                                  "N + V の形 ≈ 2 個",
                                  "n_s を %.1f bit で当てる" % s2,
                                  "%+.1f bit" % (s2 - 2 * bic)))
print("  %-16s %-14s %-16s %s" % ("c・t=一定",
                                  "パラメータ −1 個",
                                  "地平線問題が消える",
                                  "%+.1f bit（第25回）" % (bic - 213 / (2 * ln2))))
print("  【この帳簿の限界】インフレーション側は n_s ひとつしか計上していない。")
print("     実際には r の上限、断熱性、ガウス性、地平線を越えた TE 反相関、平坦性、")
print("     モノポール問題まで同じ 2 パラメータが買っている。つまり -6.5 は【過小評価】。")
print("     いっぽう c・t=一定 の -148.3 は、当てはまりの損そのものなので過小評価ではない。")
print("  ★ 桁が違う（-6.5 vs -148）。同じ手術をしても、残るものが違う：")
print("     インフレーションは (A) を捨てても (B) が残る。")
print("     c・t=一定 は (A) を無料で解くが、(B) に対応するものを持たない。")

print("")
print("=== ⑧ 正直な線：N=60 はどれだけ動くか ===")
print("  再加熱温度が決まらないと N は決まらない：")
for V4 in (1e16, 1e13, 1e10, 1e6):
    print("    V^(1/4)=%-8.0e GeV → N_min = %.1f" % (V4, res[V4]))
print("  レンジ %.1f 〜 %.1f、幅 %.1f。" % (res[1e6], res[1e16], res[1e16] - res[1e6]))
print("  → 『N=60』はスケール依存。n_s との一致は、GUT スケールを仮定したときの話。")
print("     n_s ≈ 1 − 2/N も α-attractor / R² 型での結果で、模型に依存する。")
