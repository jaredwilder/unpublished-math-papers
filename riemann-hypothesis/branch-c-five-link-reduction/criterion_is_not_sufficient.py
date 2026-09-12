"""Test whether the certified Branch C determinant criterion is sufficient for real-rootedness.

Criterion:
    r D(r,k-1) D(r,k+1) <= k D(r+1,k) D(r-1,k)
for the available Toeplitz lattice.

The test family consists of products of positive linear factors with one irreducible
quadratic 1+p z+q z^2, p^2<4q, so every object has a provably non-real conjugate pair.
"""
import random
from fractions import Fraction as F

def poly_from_roots_real(neg_roots, quad_pairs):
    c=[F(1)]
    for a in neg_roots:
        c=[(c[i] if i<len(c) else F(0)) +
           (a*c[i-1] if i>=1 and i-1<len(c) else F(0))
           for i in range(len(c)+1)]
    for p,q in quad_pairs:
        nc=[F(0)]*(len(c)+2)
        for i,ci in enumerate(c):
            nc[i]+=ci; nc[i+1]+=p*ci; nc[i+2]+=q*ci
        c=nc
    return c

def det(M):
    n=len(M)
    if n==0: return F(1)
    M=[r[:] for r in M]; d=F(1)
    for cc in range(n):
        p=next((r for r in range(cc,n) if M[r][cc]!=0),None)
        if p is None: return F(0)
        if p!=cc: M[cc],M[p]=M[p],M[cc]; d=-d
        d*=M[cc][cc]; inv=F(1)/M[cc][cc]
        for r in range(cc+1,n):
            f=M[r][cc]*inv
            if f:
                for c2 in range(cc,n): M[r][c2]-=f*M[cc][c2]
    return d

def D(a,r,k,N):
    if r==0: return F(1)
    if k<0: return F(0)
    return det([[(a[k+j-i] if 0<=k+j-i<N else F(0))
                 for j in range(r)] for i in range(r)])

def criterion_ok(a,N,R=4):
    for r in range(1,R+1):
        for k in range(1,N-r-1):
            lhs=F(r)*D(a,r,k-1,N)*D(a,r,k+1,N)
            rhs=F(k)*D(a,r+1,k,N)*D(a,r-1,k,N)
            if lhs>rhs: return False
    return True

random.seed(17)
found=tested=0
for _ in range(4000):
    m=random.randint(3,7)
    roots=[F(random.randint(1,20),random.randint(1,6)) for _ in range(m)]
    p=F(random.randint(1,12),random.randint(1,6))
    q=F(random.randint(1,30),random.randint(1,6))
    if p*p>=4*q: continue
    c=poly_from_roots_real(roots,[(p,q)])
    N=len(c)
    if any(x<0 for x in c): continue
    tested+=1
    if criterion_ok(c,N): found+=1

print('non-real-rooted tested:',tested)
print('satisfying criterion:',found)
assert tested==3059
assert found==1686
