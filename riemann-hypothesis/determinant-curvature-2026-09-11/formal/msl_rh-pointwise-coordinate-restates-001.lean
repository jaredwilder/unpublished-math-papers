import Mathlib

set_option autoImplicit false

theorem msl_rh_pointwise_coordinate_restates_001 (IsZero : Real → Prop) (IsSimple : Real → Prop) (G : Real → Real) (hnn : ∀ x, 0 ≤ G x) (hco : ∀ x, IsZero x → (G x = 0 ↔ ¬ IsSimple x)) : (∀ x, IsZero x → 0 < G x) ↔ (∀ x, IsZero x → IsSimple x) := by
  constructor
  · intro h x hx
    exact not_not.mp (fun hs => (ne_of_gt (h x hx)) ((hco x hx).mpr hs))
  · intro h x hx
    have hne : G x ≠ 0 := fun hz => (hco x hx).mp hz (h x hx)
    exact lt_of_le_of_ne (hnn x) (Ne.symm hne)
