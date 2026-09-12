#!/usr/bin/env python3
"""
Bookkeeping for integration-by-parts derivative envelopes.

If J_{m,q} bounds integral |d^q/du^q (u^m e^{t u^2} Phi(u))|, then
|H_t^(m)(x)| <= J_{m,q}/|x|^q.
"""
import argparse, json

def envelope(xmin, candidates):
    rows=[]
    for item in candidates:
        q=int(item["q"]); J=float(item["J"])
        rows.append({"q":q,"J":J,"bound":J/(abs(xmin)**q)})
    rows.sort(key=lambda z:z["bound"])
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--xmin",type=float,required=True)
    ap.add_argument("--candidates",required=True)
    args=ap.parse_args()
    rows=envelope(args.xmin,json.loads(args.candidates))
    print(json.dumps(rows,indent=2))
    if rows: print("BEST:",rows[0])

if __name__=="__main__":
    main()
