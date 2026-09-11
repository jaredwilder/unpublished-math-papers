# Erdős #689 — incidence necessary condition for double residue coverage

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

Suppose that for every prime `p<=n` one chooses a residue class `a_p mod p`, and that every integer in `[1,n]` belongs to at least two of the chosen residue classes.

## Theorem

Necessarily

\[
\boxed{\sum_{p\le n}\left\lceil\frac np\right\rceil\ge2n.}
\]

## Proof

For a fixed prime `p`, any residue class modulo `p` contains at most

\[
\left\lceil\frac np\right\rceil
\]

integers in `[1,n]`. Therefore the total number of incidences between integers `m<=n` and chosen residue classes is at most the displayed sum.

If every integer is covered at least twice, the same incidence count is at least `2n`. Comparing the two bounds proves the inequality.

## Scope

This is only a necessary counting condition. The historical audit already noted that it is asymptotically too weak by itself to settle the parent problem.
