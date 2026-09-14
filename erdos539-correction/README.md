# Erdős #539 — correction of a false estate close

**Author:** Jared Wilder  
**Public correction:** 2026-09-14  
**Canonical problem status:** not closed by this estate route

For finite `A⊂Z_{>0}`, let

\[
Q(A)=\{a/\gcd(a,b):a,b\in A\},
\qquad
h(n)=\min_{|A|=n}|Q(A)|.
\]

A raw campaign route incorrectly concluded `h(n)=n` from the supposed diagonal identity

\[
a/\gcd(a,a)=a.
\]

The correct identity is

\[
\boxed{a/\gcd(a,a)=1}.
\]

Hence the claimed diagonal injection does not exist and the lower bound `h(n)>=n` collapses.

## Surviving elementary theorem

The construction

\[
A=\{1,2,\ldots,n\}
\]

does give

\[
\boxed{h(n)\le n}.
\]

Indeed every quotient `a/gcd(a,b)` is a positive divisor of `a` and therefore at most `n`; conversely `b=1` yields every value `a=1,...,n`. Thus `Q(A)={1,...,n}`.

The separately audited small value `h(2)=2` is unaffected.

## Provenance

The false `PROVED` close appears in the recovered raw Pass-3 high-score stream, SHA-256

`8990b20d7807e878033a8cc0c403729620a6fb27ca1b838890da11370f42ec71`.

The detailed correction record with exact row hashes is public at:

`jaredwilder/msl-ore-estate/corrections/ERDOS-539-DIAGONAL-GCD-ERROR-2026-09-14.md`

Public #539 references checked during release:

- `https://www.erdosproblems.com/539`
- `https://www.erdosproblemaday.com/report/539`
- `https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/539.lean`

No novelty is claimed for the surviving elementary upper bound. The purpose of this packet is to make the correction externally timestamped and prevent the stale local `PROVED` status from being recycled into a false headline.
