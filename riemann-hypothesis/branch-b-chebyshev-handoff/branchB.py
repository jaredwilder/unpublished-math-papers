from mpmath import mp, mpf, log, sqrt, nstr
mp.dps=30

def primes(n):
    s=[True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i in range(2,n+1) if s[i]]

P=primes(200000)
def psi(x):
    t=mpf(0)
    for p in P:
        if p>x: break
        k=1; pk=p
        while pk<=x:
            t+=log(p); k+=1; pk=p**k
    return t

print("   the Chebyshev function and its error, on real primes")
print("      x         psi(x)          psi(x)-x        |err|/sqrt(x)   |err|/(sqrt(x) log^2 x)")
for x in (1000,10000,50000,100000,200000):
    x=mpf(x); v=psi(x); e=v-x
    print("      %-9s %-15s %-15s %-15s %s" %(nstr(x,6),nstr(v,10),nstr(e,8),nstr(abs(e)/sqrt(x),8),nstr(abs(e)/(sqrt(x)*log(x)**2),8)),flush=True)
print("\nDONE",flush=True)
