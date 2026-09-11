#!/usr/bin/env python3
"""Independent finite audit for selected theorem-bank claims.

This is not a substitute for Lean. It exhaustively checks local claims on all
triangle-free graphs through five vertices, critical/clique-cutset claims
through six vertices, and directly verifies the parity-defect host family for
several parameters.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from pathlib import Path
from typing import Iterable


def edges_of_mask(n: int, mask: int):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    adj = [0] * n
    for bit, (i, j) in enumerate(pairs):
        if (mask >> bit) & 1:
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj


def vertices(mask: int):
    while mask:
        b = mask & -mask
        yield b.bit_length() - 1
        mask ^= b


def popcount(x: int) -> int:
    return x.bit_count()


def induced_adj(adj, S: int):
    return [adj[v] & S for v in range(len(adj))]


def triangle_free(adj) -> bool:
    n = len(adj)
    for u in range(n):
        for v in vertices(adj[u] & ~((1 << (u + 1)) - 1)):
            if adj[u] & adj[v]:
                return False
    return True


def is_stable(adj, S: int) -> bool:
    return all((adj[v] & S) == 0 for v in vertices(S))


def connected(adj, S: int) -> bool:
    if S == 0:
        return False
    start = (S & -S).bit_length() - 1
    seen = 1 << start
    frontier = seen
    while frontier:
        nxt = 0
        for v in vertices(frontier):
            nxt |= adj[v] & S & ~seen
        seen |= nxt
        frontier = nxt
    return seen == S


def chromatic_number(adj, S: int | None = None) -> int:
    n = len(adj)
    if S is None:
        S = (1 << n) - 1
    vs = list(vertices(S))
    if not vs:
        return 0
    # Degree ordering is enough for n <= 6.
    vs.sort(key=lambda v: popcount(adj[v] & S), reverse=True)
    colors = [-1] * n

    def can_color(k: int, idx: int = 0) -> bool:
        if idx == len(vs):
            return True
        v = vs[idx]
        forbidden = {colors[w] for w in vertices(adj[v] & S) if colors[w] >= 0}
        for c in range(k):
            if c not in forbidden:
                colors[v] = c
                if can_color(k, idx + 1):
                    return True
                colors[v] = -1
        return False

    for k in range(1, len(vs) + 1):
        if can_color(k):
            return k
    raise AssertionError('unreachable')


def open_union(adj, S: int) -> int:
    out = 0
    for v in vertices(S):
        out |= adj[v]
    return out


def closed_neighborhood(adj, S: int) -> int:
    return S | open_union(adj, S)


def isolated_in_induced(adj, S: int) -> int:
    out = 0
    for v in vertices(S):
        if (adj[v] & S) == 0:
            out |= 1 << v
    return out


def is_induced_path_order(adj, order: tuple[int, ...]) -> bool:
    q = len(order)
    if len(set(order)) != q:
        return False
    for i in range(q):
        for j in range(i + 1, q):
            edge = ((adj[order[i]] >> order[j]) & 1) == 1
            should = j == i + 1
            if edge != should:
                return False
    return True


def is_clique(adj, S: int) -> bool:
    for v in vertices(S):
        if popcount(adj[v] & S) != popcount(S) - 1:
            return False
    return True


def components(adj, S: int):
    out = []
    rem = S
    while rem:
        start = (rem & -rem).bit_length() - 1
        comp = 1 << start
        frontier = comp
        while frontier:
            nxt = 0
            for v in vertices(frontier):
                nxt |= adj[v] & rem & ~comp
            comp |= nxt
            frontier = nxt
        out.append(comp)
        rem &= ~comp
    return out


def vertex_critical(adj) -> bool:
    V = (1 << len(adj)) - 1
    k = chromatic_number(adj, V)
    if k <= 1:
        return False
    return all(chromatic_number(adj, V & ~(1 << v)) < k for v in range(len(adj)))


def has_clique_cutset(adj) -> bool:
    V = (1 << len(adj)) - 1
    # Empty and whole sets excluded; a cutset must leave at least two components.
    for K in range(1, V):
        if not is_clique(adj, K):
            continue
        rem = V & ~K
        if rem and len(components(adj, rem)) >= 2:
            return True
    return False


def exhaustive_local(max_n: int):
    checked_graphs = 0
    checks = {k: 0 for k in ['N01','N02','N03','N05','N08','N09','P01','M01','M11','C05','C07']}
    for n in range(1, max_n + 1):
        e = n * (n - 1) // 2
        V = (1 << n) - 1
        for mask in range(1 << e):
            adj = edges_of_mask(n, mask)
            if not triangle_free(adj):
                continue
            checked_graphs += 1
            chiG = chromatic_number(adj, V)
            # N01/N09
            for v in range(n):
                assert is_stable(adj, adj[v])
                checks['N01'] += 1
            for u in range(n):
                for v in range(n):
                    assert is_stable(adj, adj[u] & adj[v])
                    checks['N09'] += 1
            # Subset budget claims
            for S in range(1 << n):
                U = open_union(adj, S)
                assert chromatic_number(adj, U) <= popcount(S)
                checks['N02'] += 1
                I = isolated_in_induced(adj, S)
                bound = popcount(S) + (1 if I else 0)
                NS = closed_neighborhood(adj, S)
                assert chromatic_number(adj, NS) <= bound
                checks['N03'] += 1
                if I == 0:
                    assert chromatic_number(adj, V & ~NS) >= chiG - popcount(S)
                    checks['N05'] += 1
            # Edge closed-neighborhood bipartite/chi<=2
            for u in range(n):
                for v in range(u + 1, n):
                    if (adj[u] >> v) & 1:
                        NS = closed_neighborhood(adj, (1 << u) | (1 << v))
                        assert chromatic_number(adj, NS) <= 2
                        checks['N08'] += 1
            # P01 induced cycle from consecutive path contacts
            for q in range(2, n + 1):
                for order in itertools.permutations(range(n), q):
                    if not is_induced_path_order(adj, order):
                        continue
                    Pset = sum(1 << v for v in order)
                    for x in range(n):
                        if (Pset >> x) & 1:
                            continue
                        contacts = [i for i, v in enumerate(order) if (adj[x] >> v) & 1]
                        for a, b in zip(contacts, contacts[1:]):
                            cyc = (x,) + order[a:b+1]
                            # Consecutive sequence should be induced cycle.
                            L = len(cyc)
                            for i in range(L):
                                for j in range(i + 1, L):
                                    edge = ((adj[cyc[i]] >> cyc[j]) & 1) == 1
                                    should = (j == i + 1) or (i == 0 and j == L - 1)
                                    assert edge == should
                            checks['P01'] += 1
            # M01 and M11
            for v in range(n):
                rest = V & ~(1 << v)
                mixed_sets = []
                for C in range(1, 1 << n):
                    if C & (1 << v) or not connected(adj, C):
                        continue
                    neigh = C & adj[v]
                    non = C & ~adj[v]
                    if neigh and non:
                        ok = any(((adj[a] >> b) & 1) for a in vertices(neigh) for b in vertices(non))
                        assert ok
                        checks['M01'] += 1
                        mixed_sets.append(C)
                if n <= 5:
                    for i, C1 in enumerate(mixed_sets):
                        for C2 in mixed_sets[i+1:]:
                            if C1 & C2:
                                continue
                            if any(adj[a] & C2 for a in vertices(C1)):
                                continue
                            # Find transition edges and verify induced P5.
                            pairs=[]
                            for C in (C1,C2):
                                found=None
                                for a in vertices(C & adj[v]):
                                    for b in vertices(C & ~adj[v]):
                                        if (adj[a] >> b) & 1:
                                            found=(b,a)  # b-a-v orientation
                                            break
                                    if found: break
                                assert found
                                pairs.append(found)
                            order=(pairs[0][0],pairs[0][1],v,pairs[1][1],pairs[1][0])
                            assert is_induced_path_order(adj, order)
                            checks['M11'] += 1
            # C05 first contamination C4
            for u,a,x,b in itertools.permutations(range(n),4):
                if not is_induced_path_order(adj,(u,a,x)):
                    continue
                if ((adj[b]>>u)&1) and ((adj[b]>>x)&1):
                    cyc=(u,a,x,b)
                    for i in range(4):
                        for j in range(i+1,4):
                            edge=((adj[cyc[i]]>>cyc[j])&1)==1
                            should=(j==i+1) or (i==0 and j==3)
                            assert edge==should
                    checks['C05'] += 1
            # C07 complete pairs stable
            for labels in itertools.product(range(3), repeat=n):
                A=sum((1<<i) for i,x in enumerate(labels) if x==1)
                B=sum((1<<i) for i,x in enumerate(labels) if x==2)
                if not A or not B:
                    continue
                complete=all((adj[a]&B)==B for a in vertices(A))
                if complete:
                    assert is_stable(adj,A) and is_stable(adj,B)
                    checks['C07'] += 1
    return {'triangle_free_graphs':checked_graphs,'assertion_counts':checks}


def exhaustive_critical(max_n: int):
    checked = 0
    critical = 0
    for n in range(2, max_n + 1):
        e=n*(n-1)//2
        for mask in range(1<<e):
            adj=edges_of_mask(n,mask)
            checked += 1
            if vertex_critical(adj):
                critical += 1
                assert not has_clique_cutset(adj)
    return {'all_graphs':checked,'vertex_critical_graphs':critical,'clique_cutset_violations':0}


def build_complete_tree(d: int, k: int):
    parent=[-1]
    depth=[0]
    child_index=[-1]
    levels=[[0]]
    for dep in range(k):
        nxt=[]
        for p in levels[-1]:
            for j in range(d):
                idx=len(parent)
                parent.append(p); depth.append(dep+1); child_index.append(j); nxt.append(idx)
        levels.append(nxt)
    n=len(parent)
    ancestors=[]
    for v in range(n):
        arr=[]; x=v
        while x!=-1:
            arr.append(x); x=parent[x]
        ancestors.append(arr[::-1])
    def lca(u,v):
        ans=0
        for a,b in zip(ancestors[u],ancestors[v]):
            if a!=b: break
            ans=a
        return ans
    def comparable(u,v):
        return u in ancestors[v] or v in ancestors[u]
    def earlier(u,v):
        w=lca(u,v)
        au=ancestors[u][depth[w]+1]
        av=ancestors[v][depth[w]+1]
        return child_index[au] < child_index[av]
    adj=[0]*n
    for v in range(1,n):
        p=parent[v]; adj[v]|=1<<p; adj[p]|=1<<v
    for u in range(n):
        for v in range(u+1,n):
            if comparable(u,v):
                continue
            if (depth[u]-depth[v])%2:
                adj[u]|=1<<v; adj[v]|=1<<u
    return adj,parent,depth,ancestors,lca,comparable,earlier


def verify_parity_hosts(max_k: int, d: int):
    receipts=[]
    for k in range(1,max_k+1):
        adj,parent,depth,ancestors,lca,comparable,earlier=build_complete_tree(d,k)
        n=len(adj)
        assert triangle_free(adj)
        # root paths induced and levels stable
        for v in range(n):
            path=ancestors[v]
            assert is_induced_path_order(adj,tuple(path))
        for dep in range(k+1):
            S=sum(1<<v for v in range(n) if depth[v]==dep)
            assert is_stable(adj,S)
        # Type uniformity and counts
        by_type={}
        for u in range(n):
            for v in range(u+1,n):
                if comparable(u,v):
                    continue
                w=lca(u,v)
                if earlier(u,v): a,b=depth[u],depth[v]
                else: a,b=depth[v],depth[u]
                t=(a,b,depth[w])
                val=(adj[u]>>v)&1
                by_type.setdefault(t,set()).add(val)
        assert all(len(vals)==1 for vals in by_type.values())
        active=sum(1 for vals in by_type.values() if 1 in vals)
        formula=sum((r*r)//2 for r in range(1,k+1))
        assert active==formula
        if k%2==0:
            m=k//2; closed=m*(m+1)*(4*m-1)//3
        else:
            m=(k-1)//2; closed=m*(m+1)*(4*m+5)//3
        assert formula==closed
        receipts.append({'d':d,'k':k,'vertices':n,'types':len(by_type),'active_types':active,'formula':formula})
    return receipts


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--local-n',type=int,default=5)
    ap.add_argument('--critical-n',type=int,default=6)
    ap.add_argument('--parity-k',type=int,default=4)
    ap.add_argument('--branching',type=int,default=3)
    ap.add_argument('--output',default='/mnt/data/ERDOS-738-THEOREM-BANK-VERIFICATION.json')
    args=ap.parse_args()
    t=time.time()
    result={
        'schema':'erdos738.theorem-bank.verification.v1',
        'local_exhaustion':exhaustive_local(args.local_n),
        'critical_exhaustion':exhaustive_critical(args.critical_n),
        'parity_hosts':verify_parity_hosts(args.parity_k,args.branching),
        'parameters':vars(args),
        'elapsed_seconds':None,
        'status':'PASS',
        'scope_note':'Finite exhaustive audit only; Lean remains the proof authority requested by the user.'
    }
    result['elapsed_seconds']=round(time.time()-t,3)
    Path(args.output).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
