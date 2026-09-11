# Erdős #153 — Sidon sumset bookkeeping and gap inequality

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact elementary theorem; prior formal receipt covered only one concrete instance.

Let `A` be a finite Sidon set of integers in the convention that all unordered pair sums with repetition are distinct.

Write `|A|=n` and

`A+A={s_1<...<s_t}`.

## Theorem

One has

`t = n(n+1)/2`.

Moreover

`(s_t-s_1)^2 <= (t-1) Σ_{i=1}^{t-1}(s_{i+1}-s_i)^2`.

## Proof

Because `A` is Sidon under the stated convention, each unordered pair `{a,b}` with `a<=b` gives a different sum. There are exactly

`C(n+1,2)=n(n+1)/2`

such pairs, proving the value of `t`.

Let

`g_i=s_{i+1}-s_i >0`.

Then

`Σ g_i = s_t-s_1`.

Cauchy-Schwarz gives

`(Σ g_i)^2 <= (t-1) Σ g_i^2`,

which is exactly the claimed inequality.

## Formalization note

The recovered green receipt `fmz-erdos153-campaign-001-R001-L1.cable.json` checked only the concrete set `A={1,2,4,8}`. It is therefore recorded as `KERNEL_CHECKED_SINGLE_INSTANCE_ONLY`, not as a universal formalization of this theorem.
