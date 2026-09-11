# unpublished-math-papers

Five mathematical writeups that were finished, or nearly finished, and never went anywhere.

Author: Jared Wilder. First public timestamp: 2026-09-10.

## 1. A combinatorial sieve lower bound for the family m * 2^k * 3^l + 1

`sieve-preprint/` — six .tex sources, main file `wilder-2026-V-family-rosser-iwaniec.tex`.

For every m coprime to 6 and every (k, l) with k + l <= D, let V(m,k,l) = m * 2^k * 3^l + 1 and let
pi_V(m,D) count the pairs where V is prime. The paper establishes effectively computable constants
c > 0 and D_0 such that for every such m and every D >= D_0,

    pi_V(m, D) >= c * S(m) * D

where S(m) is the Bateman-Horn singular series for the family, itself uniformly bounded below by an
absolute constant over all such m.

This is the **Erdos-Graham #203 family.** The paper's own title block carries the label
**"preprint, expert review pending"** and that label stands. It has not been refereed.

The supporting files are structured as intro-and-kappa, an adversarial pass on kappa and its
repair, Bombieri-Vinogradov and Iwaniec, an adversarial pass on those and their repair, and
almost-primes and constants. **Two of the six files are adversarial attacks on the paper's own
argument**, which is the reason to read them.

## 2. Graham / Alspach in Z_29, with a compiled PDF

`graham-z29-paper/main.tex` and `main.pdf`. The write-up of the dual-verifier computational
certificate: every subset of Z_29 minus {0} admits an ordering with pairwise distinct partial sums
and nonzero proper partial sums, exhaustively certified for cardinalities 21 through 28, where
published general results reach only 20.

The certificate itself and both verifiers are at
github.com/jaredwilder/graham-alspach-sequenceability.

## 3. Exact Gamma-fiber local density and the Kummer-character remainder

`notes/exact_gamma_fiber_local_density.tex` — a complete standalone writeup, roughly 400 lines.

## 4. Stepanov auxiliary theorem notes

`notes/stepanov_auxiliary_theorem.tex` — roughly 323 lines of supporting development.

## 5. Program overview

`notes/PROGRAM_OVERVIEW.tex` — the EG203 program stated as one document.

## Status

None of these is refereed. The sieve preprint says so on its own title page. Publishing them here
establishes a date and an author, nothing more.

## License

Apache-2.0.
