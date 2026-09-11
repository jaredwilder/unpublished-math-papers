# Strict consecutive Toeplitz positivity does not imply simple zeros

**Author:** Jared Wilder  
**Public proof:** 2026-09-11

## Theorem

Let

`F(z) = (1+z)^2 e^z = sum_{n>=0} a_n z^n`,

with `a_n=0` for `n<0`. For every `r>=1` and `k>=0`, the consecutive Toeplitz minor

`D_{r,k}(F) = det[a_{k+j-i}]_{i,j=0}^{r-1}`

is strictly positive.

But `F` has a double zero at `z=-1`.

Therefore:

> **Strict positivity of every consecutive Toeplitz minor is not, by itself, a simplicity criterion for the zeros.**

This closes the gap in the source-session node K12. The session had checked only a finite block of minors; the argument below proves the all-`r`, all-`k` statement.

## Proof

Work first in a finite upper-triangular Toeplitz truncation large enough to contain the desired minor. For a formal power series `f(z)=sum f_n z^n`, write

`T_f(i,j)=f_{j-i}`

with `f_m=0` for `m<0`.

Multiplication of generating functions becomes matrix multiplication:

`T_{fg}=T_f T_g`.

Set

`B=T_{e^z}` and `C=T_{(1+z)^2}`.

Then

`T_F = B C`.

### 1. Both factors are totally nonnegative

Let `S` denote the one-step upper shift in the finite truncation.

For the exponential factor,

`B = exp(S)`.

Equivalently,

`B = lim_{m->infinity} (I+S/m)^m`.

Every matrix `I+tS` with `t>=0` is the path matrix of a one-layer planar network (or, equivalently, an upper bidiagonal matrix with nonnegative diagonal and superdiagonal entries), so all of its minors are nonnegative. Products of totally nonnegative matrices are totally nonnegative by Cauchy-Binet, and entrywise limits preserve nonnegativity of every fixed minor. Hence `B` is totally nonnegative.

For the polynomial factor,

`C=(I+S)^2`,

so `C` is also totally nonnegative.

### 2. The needed consecutive minor of the exponential factor is strictly positive

Take row set

`I={0,1,...,r-1}`

and column set

`J={k,k+1,...,k+r-1}`.

The corresponding minor of `B` is

`det[1/(k+j-i)!]_{i,j=0}^{r-1}`,

using the convention `1/n!=0` for `n<0`.

Multiply column `j` by `(k+j)!`. The entry in row `i` becomes the falling factorial

`(k+j)_(i) = (k+j)(k+j-1)...(k+j-i+1)`,

which is a monic polynomial of degree `i` in `x_j=k+j`. (When `i>x_j`, both the Toeplitz entry and the falling factorial are zero.)

The determinant of monic degree-`0,1,...,r-1` polynomials evaluated at the distinct points

`x_j=k+j`

is the Vandermonde determinant. Therefore

`det[(k+j)_(i)] = product_{0<=p<q<=r-1} (x_q-x_p)`

`= product_{0<=p<q<=r-1} (q-p)`

`= product_{j=0}^{r-1} j!`.

Undoing the column scaling gives the exact formula

`D_{r,k}(e^z) = [product_{j=0}^{r-1} j!] / [product_{j=0}^{r-1} (k+j)!] > 0`.

### 3. Cauchy-Binet transfers strict positivity to `(1+z)^2 e^z`

Apply Cauchy-Binet to the minor of `BC` with row set `I` and column set `J`:

`det((BC)[I,J]) = sum_K det(B[I,K]) det(C[K,J])`,

where `K` runs over `r`-element intermediate index sets in the finite truncation.

Every summand is nonnegative because both `B` and `C` are totally nonnegative.

Now take the particular intermediate set `K=J`. Since `C` is upper triangular with diagonal entry `1`,

`det(C[J,J])=1`.

Hence the `K=J` summand equals

`det(B[I,J]) > 0`.

Therefore the whole sum is strictly positive:

`D_{r,k}(F)>0`.

This holds for every `r>=1` and `k>=0`. QED.

## Consequence for the RH determinant program

The result is an **ambient logical separation**, not an RH theorem:

- the property “all consecutive Toeplitz minors are strictly positive” can coexist with a repeated zero;
- therefore that determinant property, taken alone, cannot imply zero simplicity;
- so a determinant-positivity route is not logically equivalent to a universal simplicity criterion such as PTS merely because both can be used in real-zero programs.

This does **not** say that additional structure specific to the Riemann xi function could never connect determinant positivity to simplicity. It says the consecutive-minor positivity property itself does not.

## Relation to the exported campaign

The source session's W9 computation checked a finite block and correctly found strict positivity there. Its K12 node then promoted that observation to the all-minors statement without supplying the missing argument. This note supplies that argument and turns the intended witness into a theorem.
