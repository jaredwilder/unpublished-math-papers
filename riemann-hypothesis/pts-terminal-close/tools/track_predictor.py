#!/usr/bin/env python3
"""Zero-track predictor formulas for H_t = -H_xx."""
import argparse, json

def track_jet(A,B,C,D):
    xp=B/A
    xpp=-D/A + 2*B*C/(A*A) - (B**3)/(A**3)
    return xp,xpp

def main():
    ap=argparse.ArgumentParser()
    for name in "ABCD": ap.add_argument(f"--{name}",type=float,required=True)
    ap.add_argument("--t0",type=float,default=0.15)
    ap.add_argument("--x0",type=float,required=True)
    args=ap.parse_args()
    xp,xpp=track_jet(args.A,args.B,args.C,args.D)
    print(json.dumps({
        "x0":args.x0,"t0":args.t0,"xprime":xp,"xsecond":xpp,
        "linear_predictor":f"x={args.x0}+({xp})*(t-{args.t0})",
        "quadratic_predictor":f"x={args.x0}+({xp})*(t-{args.t0})+0.5*({xpp})*(t-{args.t0})^2"
    },indent=2))

if __name__=="__main__": main()
