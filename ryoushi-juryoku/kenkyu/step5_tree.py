# -*- coding: utf-8 -*-
"""
step5: スペクトル次元の測定コードを、答えの分かっている対象で較正する。

なぜやるか
----------
DT の c=4 相で d_s ≈ 1.03 が出た。枝分かれポリマーの既知値は 4/3 ≈ 1.33
（Alexander–Orbach: d_H=2, d_w=3 → d_s=2d_H/d_w=4/3）。
d_H のほうは 1.78 で 2 に近いのに、d_s だけ 1 に寄る。
**測定コードが悪いのか、相が別物なのか**を切り分ける。

対照実験
--------
一様ランダム木（Prüfer 列から復元）は、臨界 Galton–Watson 木を頂点数で条件付けたものに等しく、
d_H = 2、d_s = 4/3 が既知。**同じ拡散コードでこれを測って 4/3 が出れば、コードは正しい。**
"""
import sys, io
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
rng = np.random.default_rng(20260817)


def random_tree(n):
    """Prüfer 列から一様ランダム木を作る（辺のリストを返す）"""
    if n == 2:
        return [(0, 1)]
    pruf = rng.integers(0, n, size=n - 2)
    deg = np.ones(n, dtype=np.int64)
    for v in pruf:
        deg[v] += 1
    import heapq
    leaves = [i for i in range(n) if deg[i] == 1]
    heapq.heapify(leaves)
    edges = []
    ptr = 0
    for v in pruf:
        leaf = heapq.heappop(leaves)
        edges.append((leaf, int(v)))
        deg[v] -= 1
        if deg[v] == 1:
            heapq.heappush(leaves, int(v))
    u = heapq.heappop(leaves); w = heapq.heappop(leaves)
    edges.append((int(u), int(w)))
    return edges


def adjacency(n, edges):
    """CSR 風の隣接リスト"""
    deg = np.zeros(n, dtype=np.int64)
    for a, b in edges:
        deg[a] += 1; deg[b] += 1
    start = np.zeros(n + 1, dtype=np.int64)
    np.cumsum(deg, out=start[1:])
    fill = start[:-1].copy()
    lst = np.zeros(start[-1], dtype=np.int64)
    for a, b in edges:
        lst[fill[a]] = b; fill[a] += 1
        lst[fill[b]] = a; fill[b] += 1
    return start, lst, deg


def spectral(n, start, lst, deg, sigmax, nstart, lazy=True):
    """怠惰ウォークの戻り確率 P(σ)。CDT の測定コードと同じ式"""
    P = np.zeros(sigmax + 1)
    cnt = 0
    invdeg = 1.0 / deg
    for _ in range(nstart):
        v0 = int(rng.integers(0, n))
        p = np.zeros(n); p[v0] = 1.0
        for sg in range(1, sigmax + 1):
            share = p * invdeg
            q = np.zeros(n)
            np.add.at(q, lst, np.repeat(share, deg))
            p = 0.5 * p + 0.5 * q if lazy else q
            P[sg] += p[v0]
        cnt += 1
    return P / cnt


def hausdorff(n, start, lst, nstart):
    """平均グラフ距離（BFS）"""
    from collections import deque
    acc = 0
    for _ in range(nstart):
        v0 = int(rng.integers(0, n))
        dist = np.full(n, -1, dtype=np.int64); dist[v0] = 0
        dq = deque([v0])
        while dq:
            v = dq.popleft()
            for j in range(start[v], start[v + 1]):
                u = lst[j]
                if dist[u] < 0:
                    dist[u] = dist[v] + 1; dq.append(u)
        acc += dist.mean()
    return acc / nstart


print("=== 対照実験：一様ランダム木（既知 d_H=2, d_s=4/3≈1.333）===")
print()
print("--- ハウスドルフ次元（<r> ~ N^{1/d_H}）---")
Ns = [500, 2000, 8000, 32000]
rs = []
for n in Ns:
    e = random_tree(n)
    st, ls, dg = adjacency(n, e)
    r = hausdorff(n, st, ls, 6)
    rs.append(r)
    print(f"  N={n:>6}  <r> = {r:8.2f}")
p = np.polyfit(np.log(Ns), np.log(rs), 1)
print(f"  → 1/d_H = {p[0]:.4f}  ⇒  d_H = {1/p[0]:.3f}   （期待 2）")
print()
print("--- スペクトル次元（P(σ) ~ σ^{-d_s/2}）---")
n = 32000
e = random_tree(n)
st, ls, dg = adjacency(n, e)
P = spectral(n, st, ls, dg, 400, 12)
print(f"{'σ':>7}{'P(σ)':>14}{'d_s':>10}")
sg = 8
while True:
    s2 = int(sg * 1.7) + 1
    if s2 > 400: break
    ds = -2.0 * (np.log(P[s2]) - np.log(P[sg])) / (np.log(s2) - np.log(sg))
    print(f"{sg:>7}{P[sg]:>14.6e}{ds:>10.3f}")
    sg = s2
print()
print("  期待 d_s = 4/3 = 1.3333")
print()
print("★ これで 4/3 が出れば測定コードは正しく、DT の c=4 相（d_s≈1.03）は")
print("  枝分かれポリマーとは別物ということになる。")
