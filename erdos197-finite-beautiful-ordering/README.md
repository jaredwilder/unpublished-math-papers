# Erdős #197 — every finite set admits a beautiful ordering

**Author:** Jared Wilder  
**Recovered from:** September 2026 full-corpus theorem audit  
**Public extraction:** 2026-09-11

## Finite theorem

Every finite set

\[
S\subseteq\mathbb N
\]

admits an ordering with no monotone three-term arithmetic progression: there do not exist indices
`i<j<k` whose ordered values `x_i,x_j,x_k` satisfy

\[
x_i+x_k=2x_j.
\]

This settles the complete **finite analogue** used in the campaign. It does not settle the infinite
order-type problem.

## Proof by parity recursion

Proceed by induction on `|S|`.

Split

\[
S=S_{\rm odd}\sqcup S_{\rm even}.
\]

Order the odd elements first and the even elements second. Within each parity class, subtract the
appropriate parity and divide by 2:

\[
T_{\rm odd}=\{(x-1)/2:x\in S_{\rm odd}\},
\qquad
T_{\rm even}=\{x/2:x\in S_{\rm even}\}.
\]

Both are smaller finite sets, so by induction choose beautiful orderings of them and lift those
orderings back to the corresponding parity classes.

Suppose a monotone three-term progression nevertheless occurred in the concatenated ordering.
Its endpoints have the same parity, because

\[
x_i+x_k=2x_j
\]

is even. The two endpoints therefore lie in the same parity block. Since the blocks are contiguous,
the middle indexed term lies in that same block as well. Dividing the entire progression by 2 after
the parity normalization produces a monotone three-term progression in the recursively ordered
smaller set, contradiction.

Thus the recursively concatenated ordering is beautiful.

## Scope boundary

The source audit classifies this as a complete finite theorem but a classical/known mechanism. Its
value is structural: it isolates the real difficulty of Erdős #197 at the infinite ordering / order-
type level rather than at any finite obstruction. No historical novelty claim is made.

## License

Apache-2.0 for repository-authored material.
