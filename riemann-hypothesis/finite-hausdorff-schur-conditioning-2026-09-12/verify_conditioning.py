#!/usr/bin/env python3
"""Dependency-free / optional-numpy replay for the finite Hausdorff->Schur conditioning note.

This script checks the algebraic identities behind the theorem on explicit rational examples:
1. the power-sum Jacobian factorization J = D V;
2. the Lagrange-polynomial formula for V^{-1};
3. the explicit l1 row bound (2-eta)^(m-1)/Delta^(m-1);
4. the Möbius logarithmic derivative d log(alpha)/dy = 1/[y(1-y)].

It is a replay/sanity checker, not a substitute for the analytic proof in README.md.
"""

from fractions import Fraction
from math import prod


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def poly_mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def lagrange_coeffs(y, j):
    p = [Fraction(1)]
    den = Fraction(1)
    for ell, z in enumerate(y):
        if ell == j:
            continue
        p = poly_mul(p, [-z, Fraction(1)])
        den *= y[j] - z
    return [c / den for c in p]


def check(y, eta, Delta):
    m = len(y)
    assert all(eta <= z <= 1 - eta for z in y)
    assert all(abs(y[i] - y[j]) >= Delta
               for i in range(m) for j in range(i))

    # V has power index down rows, atom index across columns.
    V = [[y[j] ** s for j in range(m)] for s in range(m)]

    # Row j of V^{-1} is the coefficient vector of L_j(x).
    Vinv = [lagrange_coeffs(y, j) for j in range(m)]
    assert matmul(Vinv, V) == eye(m)

    # J_(s,j) = s*y_j^(s-1), s=1..m; J = D V.
    J = [[Fraction(s + 1) * y[j] ** s for j in range(m)]
         for s in range(m)]
    D = [[Fraction(i + 1) if i == j else Fraction(0)
          for j in range(m)] for i in range(m)]
    assert matmul(D, V) == J

    # Explicit inverse-Vandermonde l1 bound.
    C = (Fraction(2) - eta) ** (m - 1) / (Delta ** (m - 1))
    row_norms = [sum(abs(c) for c in row) for row in Vinv]
    assert all(norm <= C for norm in row_norms)

    # Möbius logarithmic derivative identity.
    # alpha = y/(1-y), so d/dy log(alpha) = 1/[y(1-y)].
    for z in y:
        lhs = Fraction(1, 1) / z + Fraction(1, 1) / (1 - z)
        rhs = Fraction(1, 1) / (z * (1 - z))
        assert lhs == rhs

    print("PASS", {
        "m": m,
        "max_Vinv_row_l1": str(max(row_norms)),
        "explicit_bound_C": str(C),
    })


def main():
    check(
        [Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)],
        eta=Fraction(3, 20),
        Delta=Fraction(3, 10),
    )
    check(
        [Fraction(3, 20), Fraction(7, 20), Fraction(3, 5), Fraction(17, 20)],
        eta=Fraction(1, 10),
        Delta=Fraction(1, 5),
    )
    print("PASS all exact conditioning replays")


if __name__ == "__main__":
    main()
