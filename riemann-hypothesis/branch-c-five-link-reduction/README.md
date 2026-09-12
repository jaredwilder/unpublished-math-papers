# Branch C — historical reduction and decisive refutation

**Author:** Jared Wilder  
**Historical intermediate state:** 2026-09-11 / epoch 20  
**Refutation:** 2026-09-12 / epoch 23

## Current verdict

**Branch C is closed as a route to the Riemann Hypothesis.**

The earlier campaign successfully reduced and certified a substantial determinant/coefficient criterion, including kernel-checked algebra, exact rational interval certification, and a finite first-rung reduction. That mathematics remains valid at its stated scope.

What failed was the top implication:

> the certified criterion does **not** imply real-rootedness / RH.

The failure is explicit and reproducible.

## Exact falsifier

The criterion under test was the full square-free lattice inequality

\[
rD_{r,k-1}D_{r,k+1}\le kD_{r+1,k}D_{r-1,k}.
\]

A family was constructed by multiplying positive linear factors by one irreducible quadratic

\[
1+pz+qz^2,
\qquad p^2<4q,
\]

so every test object contains a provably non-real conjugate pair while retaining nonnegative coefficients.

Fresh rerun from the 2026-09-12 session export:

- 3,059 non-real-rooted polynomials tested;
- **1,686 satisfy the criterion anyway**.

A second audit removed the three strongest objections simultaneously:

- demand the criterion at every available determinant order;
- keep shifts in the interior of the finite coefficient window;
- test both the square-free reduction and the original entry form.

Result:

- 2,284 non-real-rooted polynomials tested at full available depth;
- **1,445 satisfy the square-free criterion**;
- **the same 1,445 satisfy the original entry form**.

Therefore the criterion is a genuine necessary condition on the intended real-rooted family, but it is **not sufficient**.

An explicit degree-five witness is

\[
a=(1,113/12,2549/72,1265/16,32629/288,1615/24),
\]

coming from a factor with

\[
p=4/3,\qquad q=19/4,\qquad p^2-4q=-155/9<0.
\]

It contains a non-real conjugate pair and passes both criterion forms at every admissible interior lattice entry.

Reproducibility files in this directory:

- `criterion_is_not_sufficient.py`
- `criterion_is_not_sufficient.out.txt`
- `criterion_kill_audit.py`
- `criterion_kill_audit.out.txt`

## What survives

The refutation does **not** invalidate the lower mathematics developed while studying the criterion. In particular, the following remain valid at their own scope:

- Desnanot–Jacobi identities and rearrangements;
- determinant/curvature normalizations;
- exact first-rung algebraic reductions;
- exact rational interval certifications of the theta-kernel inequalities;
- kernel-checked equivalences and obstruction lemmas;
- the multiplicity-blindness theorem for consecutive Toeplitz minors;
- the August Encirclement II–V determinant geometry.

Those results are mathematical assets. They simply do not close RH through this criterion.

## Historical intermediate state

At epoch 20 the live state had reached a real reduction:

- five-link chain formalized;
- one link reduced to a first-rung quadratic;
- numerical sign settled with large margin;
- finite certification remaining.

That intermediate state was published before the later sufficiency falsifier was run. The later test is decisive and supersedes the RH-route interpretation of that snapshot.

## Campaign lesson

The route was killed by a test that should precede expensive certification:

> **Before proving a criterion on the target object, first test whether the criterion can hold on an explicit family for which the target property is false.**

One counterexample refutes the implication. Here there are more than a thousand.

## Current campaign map

As of the 2026-09-12 export:

- **Branch A:** active, but its best candidate quantities were successively falsified or rendered uninformative;
- **Branch B:** screened and passing the campaign's three evidence laws, but otherwise untouched;
- **Branch C:** **closed as dead**.

RH remains open.