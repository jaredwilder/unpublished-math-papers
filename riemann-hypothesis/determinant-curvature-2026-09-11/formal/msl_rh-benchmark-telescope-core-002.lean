set_option autoImplicit false

def fct : Nat → Nat
  | 0 => 1
  | (n+1) => (n+1) * fct n

def Pfc : Nat → Nat
  | 0 => 1
  | (n+1) => Pfc n * fct n

theorem msl_rh_benchmark_telescope_core_002 (n : Nat) : Pfc (n+2) * Pfc n = (n+1) * (Pfc (n+1) * Pfc (n+1)) := by
  simp [Pfc, fct, Nat.mul_comm, Nat.mul_assoc, Nat.mul_left_comm]
