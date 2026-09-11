#!/usr/bin/env python3
"""Exact-rational regression checks for MULTIPLICITY-BLINDNESS-THEOREM.md.

This script is a finite sanity check, not the proof. The theorem is proved by
Toeplitz factorization + total nonnegativity + Cauchy-Binet.
"""
from fractions import Fraction
from math import factorial


def det(M):
    """Exact determinant by fraction Gaussian elimination."""
    A = [row[:] for row in M]
    n = len(A)
    sign = 1
    for col in range(n):
        pivot_row = next((i for i in range(col, n) if A[i][col]), None)
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != col:
            A[col], A[pivot_row] = A[pivot_row], A[col]
            sign = -sign
        pivot = A[col][col]
        for i in range(col + 1, n):
            if A[i][col]:
                q = A[i][col] / pivot
                for j in range(col, n):
                    A[i][j] -= q * A[col][j]
    out = Fraction(sign)
    for i in range(n):
        out *= A[i][i]
    return out


def b(n):
    """Coefficient of e^z."""
    return Fraction(0) if n < 0 else Fraction(1, factorial(n))


def a(n):
    """Coefficient of (1+z)^2 e^z.

    1/n! + 2/(n-1)! + 1/(n-2)! = (n^2+n+1)/n!.
    """
    return Fraction(0) if n < 0 else Fraction(n * n + n + 1, factorial(n))


def minor(coeff, r, k):
    return det([[coeff(k + j - i) for j in range(r)] for i in range(r)])


def exp_closed_form(r, k):
    out = Fraction(1)
    for j in range(r):
        out *= Fraction(factorial(j), factorial(k + j))
    return out


def main():
    checked = 0
    for r in range(1, 9):
        for k in range(13):
            got = minor(b, r, k)
            want = exp_closed_form(r, k)
            assert got == want, ("exponential closed form", r, k, got, want)

            repeated_zero_minor = minor(a, r, k)
            assert repeated_zero_minor > 0, (
                "repeated-zero consecutive minor not positive",
                r,
                k,
                repeated_zero_minor,
            )
            checked += 1

    print("PASS exponential closed form and repeated-zero positivity")
    print("exact rational (r,k) cases:", checked)
    print("range: 1 <= r <= 8, 0 <= k <= 12")
    print("NOTE: finite regression only; see theorem note for the all-r,k proof")


if __name__ == "__main__":
    main()
