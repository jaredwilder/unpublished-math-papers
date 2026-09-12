#!/usr/bin/env python3
"""Derivative-ratchet planner for PTS time-box certificates."""
import argparse, json, math

def t_cost(rt, enclosed, remainder):
    rows=[]
    odds=sorted(k for k in enclosed if k>=3 and k%2==1)
    for p in range(1,len(odds)+1):
        expected=[2*a+1 for a in range(1,p+1)]
        if any(k not in enclosed for k in expected): continue
        rem_order=2*p+3
        if rem_order not in remainder: continue
        cost=0.0; terms=[]
        for a in range(1,p+1):
            k=2*a+1
            term=(rt**a/math.factorial(a))*float(enclosed[k])
            cost+=term; terms.append((k,term))
        rem=(rt**(p+1)/math.factorial(p+1))*float(remainder[rem_order])
        cost+=rem
        rows.append({"p":p,"through_derivative":2*p+1,"remainder_derivative":rem_order,
                     "terms":terms,"remainder":rem,"cost":cost})
    return rows

def choose(rt,margin,enclosed,remainder):
    rows=t_cost(rt,enclosed,remainder)
    for r in rows: r["condition_number"]=float(margin)/r["cost"] if r["cost"]>0 else math.inf
    rows.sort(key=lambda r:r["cost"])
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--rt",type=float,required=True)
    ap.add_argument("--margin",type=float,required=True)
    ap.add_argument("--enclosed",required=True)
    ap.add_argument("--remainder",required=True)
    args=ap.parse_args()
    enclosed={int(k):v for k,v in json.loads(args.enclosed).items()}
    remainder={int(k):v for k,v in json.loads(args.remainder).items()}
    rows=choose(args.rt,args.margin,enclosed,remainder)
    print(json.dumps(rows,indent=2))
    if rows: print("BEST:",rows[0])

if __name__=="__main__": main()
