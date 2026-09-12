#!/usr/bin/env python3
"""Exact finite rational checks for the Hausdorff–Schur bridge note.

This is a replay/sanity checker for the algebraic identities in README.md.
It is not a proof of RH and does not certify the infinite zeta zero set.
"""

from fractions import Fraction as F


def bridge_from_u(u: F):
    # tau = 1/4-u, alpha = -1/(4u), y=1/(4tau)
    tau = F(1, 4) - u
    alpha = -F(1, 1) / (4 * u)
    y = F(1, 1) / (4 * tau)
    assert y == alpha / (1 + alpha)
    assert alpha == y / (1 - y)
    return tau, alpha, y


def beta(alpha: F, n: int, q: int) -> F:
    return 4 * alpha ** (n + 1) / (1 + alpha) ** (n + q + 1)


def beta_y(y: F, n: int, q: int) -> F:
    return 4 * y ** (n + 1) * (1 - y) ** q


def H(alphas, n: int, q: int) -> F:
    return sum((beta(a, n, q) for a in alphas), F(0, 1))


def derivative_identity(alpha: F, n: int, q: int) -> F:
    # Both the radial logarithmic response and first angular phase response.
    return F(n + 1, 1) / (1 + alpha) - F(q, 1) * alpha / (1 + alpha)


def main():
    # Positive PF-side parameters correspond to negative u=(rho-1/2)^2 on RH.
    for u in [F(-1, 1), F(-9, 4), F(-25, 16), F(-49, 9)]:
        tau, alpha, y = bridge_from_u(u)
        assert tau >= F(1, 4)
        assert alpha > 0
        assert 0 < y < 1

    alphas = [F(1, 3), F(2, 5), F(5, 7), F(7, 11)]

    for n in range(7):
        for q in range(7):
            for a in alphas:
                y = a / (1 + a)
                assert beta(a, n, q) == beta_y(y, n, q)

            # Exact Pascal splitting law.
            assert H(alphas, n, q) == H(alphas, n + 1, q) + H(alphas, n, q + 1)

    # At the radial saddle alpha=(n+1)/q, the shared first derivative vanishes.
    for n in range(8):
        for q in range(1, 9):
            a = F(n + 1, q)
            assert derivative_identity(a, n, q) == 0

    print("PASS: exact bridge, Beta form, Pascal law, and saddle derivative checks")


if __name__ == "__main__":
    main()
