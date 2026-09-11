# Erdős #727 — an infinite `k=2` factorial-divisibility obstruction family

**Author:** Jared Wilder  
**Recovered from:** September 2026 theorem / novelty audit  
**Public extraction:** 2026-09-11

## Exact theorem

For every prime `p >= 7`, set

\[
n=2p-2.
\]

Then

\[
((n+2)!)^2 \nmid (2n)!.
\]

Equivalently,

\[
((2p)!)^2 \nmid (4p-4)!.
\]

## Proof

Compare `p`-adic valuations. Since `p>=7`, one has `4p-4<p^2`. Therefore

\[
v_p((4p-4)!)=\left\lfloor\frac{4p-4}{p}\right\rfloor=3.
\]

On the other hand,

\[
v_p((2p)!)=2,
\]

again with no `p^2` contribution, so

\[
v_p(((2p)!)^2)=4.
\]

Thus the left-hand factorial square contains one more factor of `p` than `(4p-4)!`, proving the
non-divisibility.

## Scope

This is an **infinite obstruction family in the `k=2` stratum**. It does not settle Erdős #727 and
does not imply there are only finitely many successes. The recovered novelty audit labelled the
family `APPARENTLY_UNRECORDED_EXACT` with medium confidence: the #727 tracker and targeted exact
searches did not expose this family, but specialist prior-art review remains appropriate.

## License

Apache-2.0 for repository-authored material.
