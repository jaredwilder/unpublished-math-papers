import Mathlib

set_option autoImplicit false

theorem msl_rh_pts_chain_001 (L : Real) (RiemannHyp : Prop) (hDBN : RiemannHyp <-> L <= 0) (hRodgersTao : 0 <= L) (hPTS : Not (0 < L)) : RiemannHyp := by rw [hDBN]; exact not_lt.mp hPTS
