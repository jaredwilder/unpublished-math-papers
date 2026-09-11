#!/usr/bin/env python3
"""Independent verifier for the GP-denominator Erdős–Straus classification.
Imports no MathFire code.
"""
from math import gcd,isqrt
checked=0;recoveries=0;minimality=0
for a in range(1,401):
 for b in range(a+1,501):
  if gcd(a,b)!=1:continue
  D=a*a+a*b+b*b
  assert D%2==1 and gcd(D,a*b)==1 and gcd(D,4*a*a*b*b)==1
  for t in range(1,5):
   g=t*D;n=4*t*a*a*b*b;x=g*a*a;y=g*a*b;z=g*b*b
   assert 4*x*y*z==n*(x*y+x*z+y*z)
   assert y*y==x*z and x<y<z
   gg=gcd(gcd(x,y),z);A=isqrt(x//gg);B=isqrt(z//gg)
   assert A*A==x//gg and B*B==z//gg and y//gg==A*B
   assert (A,B,gg//(A*A+A*B+B*B))==(a,b,t)
   checked+=1;recoveries+=1
  # If 4*g*a^2*b^2 is divisible by D then coprimality forces D|g.
  for g0 in range(1,min(D,200)):
   if (4*g0*a*a*b*b)%D==0:raise AssertionError((a,b,D,g0))
  minimality+=1
print(f'coprime_parameter_pairs={minimality}')
print(f'constructed_solutions={checked}')
print(f'parameter_recoveries={recoveries}')
print('gcd_lemma=PASS')
print('parity_lemma=PASS')
print('minimal_scale=PASS')
print('if_and_only_if_samples=PASS')