"""Re-audit the epoch-23 Branch-C falsifier.

The epoch-23 falsifier constructs a finite polynomial with a non-real conjugate pair and
checks the determinant inequality only on an interior portion of its finite Toeplitz lattice.
That is not a counterexample to the infinite positive-coefficient implication needed for the
Riemann xi coefficient sequence.

This script reproduces the original seeded family/count and records the load-bearing domain
failure: every polynomial has finite support, hence a_k=0 after its degree, whereas the
strict-consecutive-minor implication is applied to the xi sequence with a_k>0 for every k.
"""
from fractions import Fraction as F
import random

def poly(roots,p,q):
    c=[F(1)]
    for a in roots:
        c=[(c[i] if i<len(c) else F(0)) + (a*c[i-1] if i>=1 and i-1<len(c) else F(0)) for i in range(len(c)+1)]
    nc=[F(0)]*(len(c)+2)
    for i,ci in enumerate(c):
        nc[i]+=ci; nc[i+1]+=p*ci; nc[i+2]+=q*ci
    return nc

def det(M):
    n=len(M)
    if n==0:return F(1)
    M=[r[:] for r in M]; d=F(1)
    for cc in range(n):
        pv=next((r for r in range(cc,n) if M[r][cc]!=0),None)
        if pv is None:return F(0)
        if pv!=cc:M[cc],M[pv]=M[pv],M[cc]; d=-d
        piv=M[cc][cc]; d*=piv; inv=F(1)/piv
        for r in range(cc+1,n):
            f=M[r][cc]*inv
            if f:
                for c2 in range(cc,n):M[r][c2]-=f*M[cc][c2]
    return d

def D(a,r,k):
    if r==0:return F(1)
    if k<0:return F(0)
    N=len(a)
    return det([[(a[k+j-i] if 0<=k+j-i<N else F(0)) for j in range(r)] for i in range(r)])

def orig_ok_interior(a):
    N=len(a); deg=N-1; R=max(1,deg//2); kmax=max(1,deg//2)
    for r in range(1,R+1):
        for k in range(1,kmax+1):
            # This is the epoch-23 exclusion that removes the polynomial boundary.
            if k+r+1>=N: continue
            lhs=F(k+r)*D(a,r,k-1)*D(a,r,k+1)
            rhs=F(k)*D(a,r,k)**2
            if lhs>rhs:return False
    return True

random.seed(19)
tested=hits=finite_support_failures=0
for _ in range(3000):
    m=random.randint(4,8)
    roots=[F(random.randint(1,20),random.randint(1,6)) for _ in range(m)]
    p=F(random.randint(1,12),random.randint(1,6)); q=F(random.randint(1,30),random.randint(1,6))
    if p*p>=4*q:continue
    c=poly(roots,p,q)
    if any(x<0 for x in c):continue
    tested+=1
    if orig_ok_interior(c):
        hits+=1
        N=len(c)
        assert D(c,1,N)==0
        finite_support_failures+=1

print('seeded non-real-rooted polynomials tested:',tested)
print('interior hits for original criterion:',hits)
print('hits violating everywhere-positive coefficient premise:',finite_support_failures)
assert (tested,hits,finite_support_failures)==(2284,1445,1445)
print('VERDICT: 1445/1445 purported counterexamples lie outside the infinite positive-coefficient hypothesis.')
