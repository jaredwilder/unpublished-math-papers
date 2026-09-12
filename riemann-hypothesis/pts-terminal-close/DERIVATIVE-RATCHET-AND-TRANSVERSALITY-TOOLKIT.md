# PTS derivative-ratchet and transversality toolkit

**Author:** Jared Wilder  
**Recovered from:** RH-PTS-TERMINAL-CLOSE-10ROUNDS-2026-08-11

This note extracts the exact mathematical tools from the ten-round PTS campaign. The original campaign framed them as machine strikes; here they are stated as reusable lemmas and proof primitives.

## 1. Heat-derivative collapse

For the de Bruijn–Newman heat flow in the normalization used by the campaign,

\[
\partial_t H_t=-\partial_x^2H_t.
\]

Therefore for integers \(a,b\ge0\),

\[
\boxed{
\partial_t^a\partial_x^bH_t(x)=(-1)^aH_t^{(2a+b)}(x).
}
\]

In particular,

\[
\boxed{
\partial_t^aH_t'(x)=(-1)^aH_t^{(2a+1)}(x).
}
\]

Every coefficient of a two-variable Taylor model in \((t,x)\) is therefore supplied by one one-dimensional bank of \(x\)-derivatives.

---

## 2. Odd derivative ratchet for slope propagation

For a time box centered at \(t_0\) with radius \(r_t\),

\[
H_t'(x)
=
\sum_{a=0}^{p}
\frac{(-1)^a(t-t_0)^a}{a!}H_{t_0}^{(2a+1)}(x)
+R_{p+1},
\]

with

\[
\boxed{
|R_{p+1}|
\le
\frac{r_t^{p+1}}{(p+1)!}
\sup_{\mathcal B}|H^{(2p+3)}|.
}
\]

At the next nontrivial rung \(p=2\),

\[
H_t'
=
H_{t_0}'-(t-t_0)H_{t_0}^{(3)}
+\frac{(t-t_0)^2}{2}H_{t_0}^{(5)}+R_3,
\]

\[
\boxed{|R_3|\le \frac{r_t^3}{6}\sup_{\mathcal B}|H^{(7)}|.}
\]

This is the exact slope-propagation mechanism behind the derivative-ratchet strategy.

---

## 3. Mixed-variable Taylor remainder from one derivative bank

For the slope field \(H_x\), a total-degree \(r\) line-Taylor remainder on radii \((r_t,r_x)\) has the safe envelope

\[
\boxed{
R_r^{(H_x)}
\le
\sum_{a=0}^{r+1}
\frac{r_t^a r_x^{r+1-a}}{a!(r+1-a)!}
B_{r+a+2},
}
\]

where \(B_m\) is any valid bound for \(|H^{(m)}|\) on the box.

No separate mixed-partial enclosure engine is required.

---

## 4. Height-decaying integration-by-parts envelope

Let

\[
W_t(u)=e^{tu^2}\Phi(u).
\]

Using the even extension of \(W_t\),

\[
2H_t^{(m)}(x)
=
i^m\int_{\mathbb R}u^mW_t(u)e^{ixu}\,du.
\]

Since \(W_t\) and its derivatives decay super-exponentially, integrating by parts \(q\) times yields

\[
\boxed{
|H_t^{(m)}(x)|
\le
\frac1{|x|^q}
\int_0^\infty
\left|\frac{d^q}{du^q}(u^mW_t(u))\right|\,du.
}
\]

This gives an explicit height-decaying alternative to global moment envelopes.

---

## 5. Adaptive derivative-order selection

For a time radius \(r_t\), define

\[
C_p
=
\sum_{a=1}^{p}
\frac{r_t^a}{a!}\widehat H_{2a+1}
+
\frac{r_t^{p+1}}{(p+1)!}B_{2p+3},
\]

where \(\widehat H_{2a+1}\) is a certified enclosure contribution and \(B_{2p+3}\) is a rigorous remainder envelope.

Choose

\[
\boxed{p_*=\arg\min_p C_p.}
\]

This converts “raise derivative order” into an explicit optimization rather than a blind ladder.

---

## 6. Co-moving zero coordinates

For a simple zero track \(x=x(t)\),

\[
H_t(x(t))=0.
\]

Differentiating and using the heat equation gives

\[
\boxed{x'(t)=\frac{H_{xx}}{H_x}.}
\]

With a predictor \(p(t)\) and co-moving coordinate

\[
F(t,y)=H_t(p(t)+y),
\]

one has

\[
F_t=-H_{xx}+p'(t)H_x.
\]

Choosing

\[
p'(t_0)=\frac{H_{xx}}{H_x}(t_0,x_0)
\]

makes

\[
F_t(t_0,0)=0,
\]

removing first-order root motion from the local interval problem.

---

## 7. Quadratic zero-track predictor

At a simple zero write

\[
A=H_x,\quad B=H_{xx},\quad C=H_{xxx},\quad D=H_{xxxx}.
\]

Differentiating the velocity identity gives

\[
\boxed{
x''(t)
=-\frac DA+\frac{2BC}{A^2}-\frac{B^3}{A^3}.
}
\]

The quadratic predictor

\[
p(t)=x_0+v(t-t_0)+\frac12a(t-t_0)^2
\]

with

\[
v=B/A,
\qquad
 a=-D/A+2BC/A^2-B^3/A^3
\]

cancels the track motion through second order at the center.

---

## 8. Even derivative ratchet for boundary-sign propagation

At a fixed boundary point \(x_e\),

\[
\boxed{
\partial_t^aH_t(x_e)=(-1)^aH_t^{(2a)}(x_e).
}
\]

Hence

\[
H_t(x_e)
=
\sum_{a=0}^{p}
\frac{(-1)^a(t-t_0)^a}{a!}H_{t_0}^{(2a)}(x_e)+R,
\]

with

\[
\boxed{|R|\le \frac{r_t^{p+1}}{(p+1)!}B_{2p+2}.}
\]

### Rectangle uniqueness theorem

On \(I_t\times[a,b]\), if

1. \(H_x\) has one strict sign throughout the rectangle; and
2. \(H_t(a)\) and \(H_t(b)\) have opposite strict signs uniformly in \(t\),

then for every \(t\in I_t\), \(H_t\) has **exactly one** zero in \([a,b]\), and that zero is simple.

---

## 9. Zero-independent transversality certificate

Define

\[
\boxed{Q(t,x)=H_t(x)^2+H_t'(x)^2.}
\]

For real \(t,x\),

\[
Q=0\iff H=H_x=0.
\]

Therefore any rigorous box lower bound

\[
\boxed{Q>0}
\]

certifies simplicity/transversality throughout the entire box **without locating or counting zero tracks**.

This supplies a covering primitive complementary to root-tracking rectangles.

---

## 10. Laguerre witness

Define

\[
L(t,x)=H_x^2-HH_{xx}=H_x^2+HH_t.
\]

At a real zero \(H=0\),

\[
\boxed{L=H_x^2.}
\]

Thus a rigorous box certificate

\[
\boxed{L>0}
\]

is sufficient to show that every zero in that box is simple.

---

## 11. High-x Cauchy transversality criterion

Suppose a high-x approximation has the form

\[
G_t(z)=f_t(z)+E_t(z)
\]

on a complex disk \(D(z_0,\rho)\), with

\[
|E_t(z)|\le M.
\]

Cauchy's estimate gives

\[
\boxed{|E_t'(z_0)|\le M/\rho.}
\]

At a common real zero satisfying \(G_t(x)=G_t'(x)=0\), a double zero would force both

\[
|f_t(x)|\le \varepsilon_0,
\qquad
|f_t'(x)|\le \varepsilon_1,
\]

where \(\varepsilon_0\) bounds the value error and \(\varepsilon_1\) is the Cauchy derivative-error bound.

Therefore the box condition

\[
\boxed{
|f_t(x)|>\varepsilon_0
\quad\text{or}\quad
|f_t'(x)|>\varepsilon_1
}
\]

for every \((t,x)\) in the box is a rigorous high-x simplicity certificate.

---

## 12. Global covering architecture identified by the packet

The ten-round packet naturally decomposes a potential PTS proof into three compatible engines:

1. direct/PDE interval boxes at low and moderate height;
2. high-x asymptotic transversality boxes with simultaneous value/derivative control;
3. published eventual high-zero results for the ultimate tail.

For time descent, dyadic slabs such as

\[
[0.1,0.2],\ [0.05,0.1],\ [0.025,0.05],\ldots
\]

allow derivative envelopes to improve as the upper time endpoint decreases, because the crude kernel moments are monotone increasing in \(t\).

The exact tools above are independent reusable components. The remaining global problem is to assemble a certified covering whose union spans the full PTS domain.
