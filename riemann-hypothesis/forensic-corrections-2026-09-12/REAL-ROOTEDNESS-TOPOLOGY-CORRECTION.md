# Forensic correction: real-rootedness is not an open condition

**Author:** Jared Wilder  
**Date:** 2026-09-12  
**Status:** correction to the internal campaign state; classical topology, no novelty claim

## The incorrect campaign claim

Epoch 24 contains the statement, recorded as `K568`, that

> real rootedness is an OPEN condition and therefore an inequality; hence every criterion equivalent to it is an inequality and is subject to the campaign's margin law.

Later state objects (`K569`–`K574`) use this to claim that a large class of possible criteria has been structurally closed.

That conclusion is not valid.

## Correct topology

Fix a polynomial degree `n` and work in the real coefficient space of monic degree-`n` polynomials.

Let

\[
\mathcal R_n
=
\{p:\text{every zero of }p\text{ is real}\}.
\]

Then

\[
\boxed{\mathcal R_n\text{ is closed}.}
\]

One way to see this is by continuity of polynomial roots as an unordered multiset with respect to the coefficients. If a sequence of monic real polynomials `p_m` has only real zeros and converges coefficientwise to `p`, every limiting zero of `p_m` is real, so `p` also has only real zeros.

Equivalently, a polynomial with a nonreal zero has a zero whose imaginary part has nonzero magnitude; sufficiently small coefficient perturbations preserve a nearby nonreal zero, so the complement of `R_n` is open.

The subset

\[
\mathcal R_n^{\mathrm{simp}}
=
\{p:\text{all }n\text{ zeros are real and simple}\}
\]

is open. This is the statement the campaign's interlacing/sign argument actually supports: away from the discriminant locus, sufficiently small coefficient perturbations preserve `n` distinct real roots.

Polynomials with multiple real zeros belong to `R_n` but lie on its boundary. For example,

\[
p(x)=x^2
\]

is real-rooted, while

\[
p_\varepsilon(x)=x^2+\varepsilon
\]

has nonreal zeros for every `\varepsilon>0`.

Thus

\[
\boxed{
\text{simple real-rootedness is locally open; all real-rootedness is closed.}
}
\]

## What this invalidates

The following inference is not available:

\[
\text{real-rootedness is open}
\Longrightarrow
\text{every equivalent criterion is an inequality}
\Longrightarrow
\text{every equivalent criterion obeys one universal margin law}.
\]

The first premise is false for the full real-rooted property. The second implication would also be too strong even for an open property: equivalent formulations can use auxiliary variables, quantified statements, identities plus inequalities, discrete data, or other structures.

Therefore the campaign's claimed epoch-24 **closure of the entire criterion space** is retracted. Its individual instrument-specific margin results may still be valid at their stated scopes, but they cannot be promoted into a theorem about every possible criterion equivalent to real-rootedness.

## What survives

The correctly scoped local statement survives:

> Around a polynomial with distinct real roots, there is a coefficient neighborhood in which all roots remain distinct and real.

That is useful for finite strict-sign/no-go arguments, but it does not imply a global impossibility theorem for RH criteria.
