"""Exhaustively verify f(4)=2 and f(5)=f(6)=f(7)=3 for Erdős #85.

f(n) is one plus the maximum minimum degree of a C4-free labeled graph
on n vertices.
"""


def has_c4(n: int, mask: int, pairs: list[tuple[int, int]]) -> bool:
    adj = [0] * n
    for e, (u, v) in enumerate(pairs):
        if (mask >> e) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    # A graph contains a C4 iff some two vertices have at least two
    # common neighbours (the vertices themselves need not be adjacent).
    for u in range(n):
        for v in range(u + 1, n):
            if (adj[u] & adj[v]).bit_count() >= 2:
                return True
    return False


def min_degree(n: int, mask: int, pairs: list[tuple[int, int]]) -> int:
    deg = [0] * n
    for e, (u, v) in enumerate(pairs):
        if (mask >> e) & 1:
            deg[u] += 1
            deg[v] += 1
    return min(deg)


def exact_f(n: int) -> int:
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    best = -1
    for mask in range(1 << len(pairs)):
        # Minimum degree is cheap and lets us skip most C4 checks once a
        # reasonable lower witness has appeared.
        d = min_degree(n, mask, pairs)
        if d <= best:
            continue
        if not has_c4(n, mask, pairs):
            best = d
    return best + 1


expected = {4: 2, 5: 3, 6: 3, 7: 3}
for n, want in expected.items():
    got = exact_f(n)
    print(f"f({n}) = {got}")
    assert got == want, (n, got, want)

print("Erdos 85 small-value exhaustive verification: PASS")
