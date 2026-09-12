#!/usr/bin/env python3
"""
Cauchy error transfer for the normalized Polymath approximation.

If E = H/B - f is holomorphic in |z-z0|<=rho and |E|<=M on the disk:
    |E^(k)(z0)| <= k! M/rho^k.

At a double zero H=H'=0, G=H/B satisfies G=G'=0.
Hence double zero => |f|<=M and |f'|<=M/rho.
"""
import argparse, math, json

def budgets(M,rho,max_order=2):
    return {k:math.factorial(k)*M/(rho**k) for k in range(max_order+1)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--M",type=float,required=True)
    ap.add_argument("--rho",type=float,required=True)
    ap.add_argument("--max-order",type=int,default=2)
    args=ap.parse_args()
    print(json.dumps(budgets(args.M,args.rho,args.max_order),indent=2))

if __name__=="__main__":
    main()
