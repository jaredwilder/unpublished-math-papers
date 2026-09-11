set_option autoImplicit false

theorem msl_rh_determinant_does_not_imply_simplicity_003 (Obj : Type) (DetPositive : Obj → Prop) (AllZerosSimple : Obj → Prop) (w : Obj) (hdet : DetPositive w) (hnotsimple : ¬ AllZerosSimple w) : ¬ (∀ z, DetPositive z → AllZerosSimple z) := by
  intro h
  exact hnotsimple (h w hdet)
