# Erdős #400 — logarithmic upper bound for factorial-product excess

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11

For fixed `k>=2`, define

\[
g_k(n)=\max\Bigl\{(a_1+\cdots+a_k)-n:\ a_1!\cdots a_k!\mid n!\Bigr\}.
\]

## Theorem

For every `n>=1`,

\[
\boxed{g_k(n)\le k(\lfloor\log_2 n\rfloor+1).}
\]

Hence

\[
\boxed{g_k(n)=O_k(\log n)}
\]

and

\[
\boxed{\sum_{n\le x}g_k(n)=O_k(x\log x).}
\]

There is also an infinite lower family: for every `m>=2`, with `N=m!`,

\[
\boxed{g_k(N)\ge m+k-3.}
\]

## Proof of the upper bound

Legendre at the prime 2 gives

\[
v_2(t!)=t-s_2(t),
\]

where `s_2(t)` is the binary digit sum. If

\[
a_1!\cdots a_k!\mid n!,
\]

then

\[
\sum_{i=1}^k(a_i-s_2(a_i))\le n-s_2(n).
\]

Rearranging,

\[
(a_1+\cdots+a_k)-n
\le
\sum_i s_2(a_i)-s_2(n).
\]

Each `a_i!|n!` forces `a_i<=n` (apart from the harmless `0!,1!` equality at 1), so

\[
s_2(a_i)\le\lfloor\log_2 n\rfloor+1.
\]

Dropping the nonnegative term `s_2(n)` proves the stated bound.

## Infinite lower family

Put `N=m!` and choose

\[
(a_1,a_2,a_3,\ldots,a_k)=(N-1,m,1,\ldots,1).
\]

Then

\[
(N-1)!\,m!=(N-1)!\,N=N!,
\]

so this tuple is admissible and its excess is

\[
(N-1)+m+(k-2)-N=m+k-3.
\]

## Correction record

The historical route registry later contained a purported `FALSE` refutation asserting that `(n!)^k` divides `n!` and hence `g_k(n)=(k-1)n`. That divisibility is false for `k>=2` and `n>=2`. The explicit counterexample is already `n=2,k=2`: `2!\,2!=4` does not divide `2!=2`.

Therefore that later workflow label does **not** refute the theorem above. This packet is an example of why exact mathematics outranks registry chronology.

## Scope

These bounds do not establish the conjectured asymptotic constant or almost-all law in the parent problem. They are unconditional universal bounds and an infinite lower family.
