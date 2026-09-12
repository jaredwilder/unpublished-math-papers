import Mathlib

/-! Recovered clean formal layer from RH epochs 22-23.
    These theorems formalize algebraic/logical reductions and generic proof-engineering laws.
    They are not a proof of RH. -/

set_option autoImplicit false

theorem msl_rh_square_free_entry_068 (P S C r k : Real) (hDJ : C = P + S) : (k + r) * P <= k * C <-> r * P <= k * S := by
  subst hDJ
  constructor <;> intro h <;> nlinarith [h]

theorem msl_rh_boundary_comparison_069 (P S C r k : Real) (hr : 0 < r) (hk : 0 < k) (hDJ : C = P + S) (hP : 0 < P) (hbnd : (k + r) * P = k * C) : r * P = k * S := by
  subst hDJ
  nlinarith [hbnd]

theorem msl_rh_corner_three_term_070 (a0 a1 a2 : Real) (h0 : 0 < a0) (hD2 : 0 < a1 * a1 - a0 * a2) : (1 * (a1 * a1) < (1 + 1) * (a1 * a1 - a0 * a2)) <-> (2 * (a0 * a2) < a1 * a1) := by
  constructor <;> intro h <;> nlinarith [h]

theorem msl_rh_criticality_no_uniform_margin_071 (f : Nat -> Real) (hpos : ∀ k, 1 < f k) (hcrit : ∀ eps : Real, 0 < eps → ∃ k, f k < 1 + eps) : ¬ ∃ c : Real, 1 < c ∧ ∀ k, c ≤ f k := by
  rintro ⟨c, hc, hall⟩
  obtain ⟨k, hk⟩ := hcrit (c - 1) (by linarith)
  have := hall k
  linarith

theorem msl_rh_moment_log_convexity_atom_074 (A B u1 u2 : Real) (hA : 0 < A) (hB : 0 < B) : (A * u1 ^ 2 + B * u2 ^ 2) * (A + B) ≥ (A * u1 + B * u2) ^ 2 := by
  nlinarith [mul_pos hA hB, sq_nonneg (u1 - u2), mul_nonneg (le_of_lt (mul_pos hA hB)) (sq_nonneg (u1 - u2))]

theorem msl_rh_exponential_defect_exact_075 (k : Nat) (s t : Real) (hs : s * ((k : Real) + 1) = 1) (ht : t * ((k : Real) + 2) = 1) (hk : (0:Real) ≤ (k : Real)) : t * ((k : Real) + 2) = s * ((k : Real) + 1) ∧ s * ((k : Real) + 2) = ((k:Real) + 2) / ((k:Real) + 1) * (t * ((k:Real)+2)) := by
  have h1 : ((k : Real) + 1) ≠ 0 := by positivity
  constructor
  · rw [hs, ht]
  · rw [ht]
    field_simp
    nlinarith [hs]

theorem msl_rh_exponential_defect_factorial_077 (j : Nat) : (j + 2) * (Nat.factorial j * Nat.factorial (j+2)) = (j+2) * (Nat.factorial (j+1) * Nat.factorial (j+1)) + Nat.factorial j * Nat.factorial (j+2) := by
  simp only [Nat.factorial_succ]
  ring

theorem msl_rh_truncation_artifact_078 (p q r t : Real) (hp : 0 < p) (hq : 0 < q) (hr : 0 < r) (ht : 0 < t) (hneg : p * 0 - q * r < 0) (hbig : q * r < p * t) : p * 0 - q * r < 0 ∧ 0 < p * t - q * r := by
  constructor
  · linarith
  · linarith

theorem msl_rh_curvature_sign_argument_079 (E Dd Bp FB : Real) (hE : 0 < E) (hD : 0 < Dd) (hBp : Bp * (Dd * Dd) = -(96 * Real.pi * E)) (hFB : FB * Dd = 36 * Dd + 48) (hpi : 0 < Real.pi) : Bp < 0 ∧ 0 < FB ∧ Bp < FB := by
  have hDD : 0 < Dd * Dd := mul_pos hD hD
  have h1 : Bp < 0 := by
    nlinarith [mul_pos hpi hE]
  have h2 : 0 < FB := by
    nlinarith
  exact ⟨h1, h2, lt_trans h1 h2⟩

theorem msl_rh_hinge_telescope_atom_080 (r1 r2 r3 r4 : Real) (h1 : 0 < r4) (h2 : r4 ≤ r3) (h3 : r3 ≤ r2) (h4 : r2 ≤ r1) : r3 * r4 ≤ r1 * r2 := by
  have hr3 : 0 < r3 := lt_of_lt_of_le h1 h2
  have hr2 : 0 < r2 := lt_of_lt_of_le hr3 h3
  nlinarith

theorem msl_rh_necessary_not_sufficient_081 (Obj : Type) (Crit RealRooted : Obj -> Prop) (w : Obj) (hw1 : Crit w) (hw2 : ¬ RealRooted w) : ¬ (∀ x : Obj, Crit x → RealRooted x) := by
  intro h
  exact hw2 (h w hw1)

theorem msl_rh_gap_rate_bound_083 (g : Real -> Real) (c g0 s : Real) (hc : 0 < c) (hg0 : g 0 = g0) (hg0pos : 0 ≤ g0) (hs : s = g0 / c + 1) (hrate : g (-s) ≤ g 0 - c * s) : g (-s) < 0 := by
  have hcs : c * s = g0 + c := by rw [hs]; field_simp
  rw [hg0, hcs] at hrate
  linarith

theorem msl_rh_energy_no_collision_084 (E B d : Real) (hB : 0 < B) (hd : 0 < d) (hE : E ≤ B) (hterm : 1 ≤ E * (d * d)) : 1 ≤ B * (d * d) := by
  nlinarith [mul_pos hd hd]

theorem msl_rh_sum_dominates_term_085 (s : Finset Nat) (f : Nat -> Real) (hf : ∀ i ∈ s, 0 ≤ f i) (a : Nat) (ha : a ∈ s) : f a ≤ ∑ i ∈ s, f i := by
  exact Finset.single_le_sum hf ha

theorem msl_rh_monotone_range_ceiling_086 (E : Real -> Real) (a b : Real) (hab : a ≤ b) (hmono : ∀ x y : Real, a ≤ x → x ≤ y → y ≤ b → E y ≤ E x) (B : Real) (hB : E a ≤ B) : ∀ x : Real, a ≤ x → x ≤ b → E x ≤ B := by
  intro x hax hxb
  exact le_trans (hmono a x le_rfl hax hxb) hB

theorem msl_rh_zero_displacement_088 (R m d c : Real) (hm : 0 < m) (hslope : m * d ≤ R) (hc : m * c = R) : d ≤ c := by
  have h : m * d ≤ m * c := by rw [hc]; exact hslope
  exact le_of_mul_le_mul_left h hm

theorem msl_rh_removal_lowers_sum_089 (s : Finset Nat) (f : Nat -> Real) (hf : ∀ i ∈ s, 0 ≤ f i) (a : Nat) (ha : a ∈ s) (hpos : 0 < f a) : ∑ i ∈ s.erase a, f i < ∑ i ∈ s, f i := by
  have h := Finset.sum_erase_add s f ha
  have hnn : (0:Real) ≤ ∑ i ∈ s.erase a, f i := Finset.sum_nonneg (fun i hi => hf i (Finset.mem_of_mem_erase hi))
  linarith [h, hpos]

theorem msl_rh_tautological_separator_090 (X : Type) (P : X -> Prop) (Q : X -> Prop) (hQP : ∀ x, Q x ↔ P x) : (∀ x, Q x → P x) ∧ (∀ x, P x → Q x) ∧ (∀ R : X -> Prop, (∀ x, Q x → R x) ↔ (∀ x, P x → R x)) := by
  refine ⟨fun x hx => (hQP x).mp hx, fun x hx => (hQP x).mpr hx, ?_⟩
  intro R
  constructor
  · intro h x hx; exact h x ((hQP x).mpr hx)
  · intro h x hx; exact h x ((hQP x).mp hx)

theorem msl_rh_uninformative_test_091 (Obj Approx : Type) (app : Obj -> Approx) (T : Approx -> Prop) (P : Obj -> Prop) (hconst : ∀ a : Approx, ¬ T a) : (∀ o : Obj, ¬ T (app o)) ∧ ¬ (∃ o1 o2 : Obj, P o1 ∧ ¬ P o2 ∧ (T (app o1) ↔ ¬ T (app o2))) := by
  refine ⟨fun o => hconst (app o), ?_⟩
  rintro ⟨o1, o2, _, _, hiff⟩
  exact (hconst (app o1)) (hiff.mpr (hconst (app o2)))
