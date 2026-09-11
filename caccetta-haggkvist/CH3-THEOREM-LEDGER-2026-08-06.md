# Caccetta–Häggkvist directed-triangle campaign — complete theorem ledger

**Campaign:** 2026-08-06  
**Owner/operator:** Jared Wilder  
**Flagship:** `NOT CLOSED`  
**Exact-boundary kernel studied:** a triangle-free oriented graph on `n=3d` vertices with every outdegree `d`.

This is the authoritative theorem ledger extracted from the fifteen-round campaign. A theorem-shaped name does **not** mean the statement is valid, novel, or load-bearing. The `Status` column is part of the release and must travel with the statement.

The principal surviving asset is the source-claimed **Cubic Directed-C4 Theorem**

\[
C_4(D)\ge \left\lceil\frac{3d^3}{2}\right\rceil,
\qquad
\operatorname{tr}(A^4)\ge 6d^3,
\]

for a triangle-free oriented `d`-out-regular graph on `3d` vertices. The source packet explicitly says this remains subject to independent machine verification and historical novelty review. It does **not** close the Caccetta–Häggkvist triangle case.

The surviving fourth-moment identity is

\[
\operatorname{tr}(A^4)=\|A^2\|_F^2-\frac12\|A^2-(A^{\mathsf T})^2\|_F^2.
\]

The exact remaining closure obligation is to control the skew two-path energy strongly enough to rule out the exact-boundary kernel.

## Complete theorem ledger

| ID | Round | Name | Status | Authoritative extraction |
|---|---:|---|---|---|
| R1-L1 | 1 | Neighborhood Acyclicity Pressure | SUPPORTED | For every v, D[N+(v)] and D[N-(v)] are directed-triangle-free; for every arc v→x, N+(x)∩N-(v)=∅. |
| R1-L2 | 1 | Half-Degree Escape Lemma | SUPPORTED | For a minimum-outdegree vertex v with d=δ+(D), some x∈N+(v) has at least (d+1)/2 outneighbors in M_v. |
| R1-L3 | 1 | Minimal-Counterexample Hereditary Deficit | SUPPORTED_CONDITIONAL | In a vertex-minimal counterexample, every proper nonempty S has a vertex x with d_S^+(x)<|S|/3. |
| R1-ME | 1 | Minimal Escape Lemma | SUPPORTED_CONDITIONAL | For every proper nonempty S, some x∈S has d^+_{V\S}(x)>d-|S|/3. |
| T1 | 2 | Arc-Minimal Regularization Theorem | SUPPORTED_CONDITIONAL | After choosing a counterexample with minimum order and then minimum arcs, every vertex has outdegree d=ceil(n/3). |
| T2 | 2 | Forbidden Residue Theorem | SUPPORTED_CONDITIONAL | A vertex-minimal counterexample cannot have n≡1 mod 3. |
| T3 | 2 | Universal Minimum-Tail Theorem | SUPPORTED_CONDITIONAL | Every vertex has an incoming tail of minimum outdegree; in the arc-minimal kernel this is automatic because all vertices have outdegree d. |
| T4 | 2 | Hereditary Deficit Theorem | SUPPORTED_CONDITIONAL | Every proper nonempty induced subgraph has minimum outdegree below one third of its order. |
| T5 | 2 | Exact Escape Theorem | SUPPORTED_CONDITIONAL | For every proper nonempty S, some x∈S has d^+_{V\S}(x)≥d-ceil(|S|/3)+1. |
| T6 | 2 | A-to-B Exclusion Theorem | SUPPORTED | For A=N+(v), B=N-(v), E(A,B)=∅. |
| T7 | 2 | Quadratic Escape-Mass Theorem | SUPPORTED | For |A|=d, e(A,M_v)≥d(d+1)/2 and hence |M_v|≥(d+1)/2. |
| T8 | 2 | Two-Thirds Escape Vertex Theorem | SUPPORTED_CONDITIONAL | Some x∈A has |N_M^+(x)|≥d-ceil(d/3)+1>2d/3. |
| T9 | 2 | Second-Generation Forbidden-Indegree Theorem | SUPPORTED | If X=N_M^+(x), then for z∈X, N+(z)∩N-(x)=∅. |
| T10 | 2 | Second-Escape Compression Theorem | SUPPORTED_CONDITIONAL | Applying hereditary deficit to X yields z∈X with a large external outneighbor set W=N+(z)\X, disjoint from N-(x). |
| T11 | 2 | Pair-Cell Indegree Ceiling | SUPPORTED_CONDITIONAL | For the selected x and X, d^-(x)≤n-d-|X|+ceil(|X|/3)-2. |
| T12 | 2 | Layer-Folding Obstruction Theorem | STRUCTURAL_DIAGNOSIS | Naive recursive escape fails because later forward layers may overlap older forward layers; only immediate backward walls are forbidden. |
| CA | 2 | Candidate A — Fold-or-Triangle Lemma | PROPOSAL | A large overlap of a new escape layer with earlier layers should either force a triangle or pay an explicit expansion penalty. |
| CB | 2 | Candidate B — Selected-Vertex Indegree Floor | PROPOSAL | Select a low-internal-outdegree x with an unusually large indegree sufficient to contradict T11. |
| CC | 2 | Candidate C — Weighted Pair-Cell Inequality | PROPOSAL | Sum pair-cell inequalities over many low-internal-degree vertices instead of selecting one vertex. |
| T13 | 3 | Universal Three-Chamber Theorem | SUPPORTED | For each x, V\{x} partitions into P_x=N+(x), I_x=N-(x), M_x, and E(P_x,I_x)=∅. |
| T14 | 3 | Exact Escape-Slack Identity | SUPPORTED | If σ(x)=binom(d,2)-e(P_x), then e(P_x,M_x)=d(d+1)/2+σ(x). |
| T15 | 3 | Nonneighbor Capacity Theorem | SUPPORTED | |M_x|≥(d+1)/2+σ(x)/d, hence an indegree upper bound follows. |
| T16 | 3 | Global Nonneighbor Conservation Theorem | SUPPORTED | Σ_x |M_x|=n(n-1-2d); at n=3d the average is d-1. |
| T17 | 3 | Global Defect Budget Theorem | SUPPORTED | Σ_xσ(x) is bounded by the global nonneighbor budget; at n=3d, Σσ(x)≤nd(d-3)/2. |
| T18 | 3 | Directed Two-Path Classification Theorem | SUPPORTED | Every directed two-path x→p→y is either transitively closed by x→y or has nonadjacent endpoints; y→x is forbidden. |
| T19 | 3 | Global Escape-Path Theorem | SUPPORTED | The total escape two-path count is nd(d+1)/2+Σσ(x). |
| T20 | 3 | Common-Inneighborhood Identity | SUPPORTED | Σ_{p→y}|N-(p)∩N-(y)|=nd(d-1)/2-Σσ(x). |
| T21 | 3 | Folding Conservation Theorem | SUPPORTED | Transitive two-path mass plus escape two-path mass equals nd²; lost transitive closure becomes escape mass one-for-one. |
| T22 | 3 | High-Multiplicity Escape Pair Theorem | SUPPORTED | At n=3d some ordered nonadjacent pair has q(x,y)≥ceil(d(d+1)/(2(d-1)))>d/2+1. |
| T23 | 3 | Parallel-Bridge Chamber Theorem | SUPPORTED | For P=N+(x)∩N-(y), E(P,N-(x))=∅ and E(N+(y),P)=∅. |
| T24 | 3 | Rectangle-to-C4 Theorem | SUPPORTED | For H=N+(y)∩N-(x), every (p,h)∈P×H yields x→p→y→h→x; the pair lies in |P||H| directed 4-cycles. |
| T25 | 3 | Fold-or-Expansion Theorem | SUPPORTED_DICHOTOMY | For any η, either |H|<ηd and L∪R expands, or |H|≥ηd and the pair supports at least ηd|P| directed 4-cycles. |
| T26 | 3 | Rectangle Orientation Theorem | SUPPORTED | No arc points P→H; every adjacency between H and P is oriented H→P. |
| T27 | 3 | Four-Chamber Extremal Skeleton Theorem | STRUCTURAL_SYNTHESIS | Surviving profiles resemble a cyclic four-chamber skeleton x→P→y→H→x with a one-way H→P reservoir. |
| T28 | 3 | One-Way Rectangle Saturation Lemma | SUPPORTED | e(H,P)≥|H|(d-n+|P|+|H|) whenever the right side is positive. |
| CD | 3 | Candidate D — Rectangle Diversity Lemma | PROPOSAL | A large one-way H→P rectangle cannot have nearly identical tail inneighborhoods. |
| CE | 3 | Candidate E — Common-Inneighborhood Compression Lemma | PROPOSAL | If H-vertex inneighborhoods overlap too strongly, a large common core should violate hereditary subcriticality. |
| T29 | 4 | Escape Multiplicity Identity | SUPPORTED | Σ_{ordered nonedges}q(x,y)=Σ_x e(N+(x),M_x)≥nd(d+1)/2. |
| T30 | 4 | Ordered Nonadjacency Identity | SUPPORTED | At n=3d the number of ordered nonadjacent pairs is n(d-1). |
| T31 | 4 | Super-Half Bridge Theorem | SUPPORTED | Some ordered nonedge has q(x,y)≥ceil(d(d+1)/(2(d-1)))=ceil(d/2+1+1/(d-1)). |
| T32 | 4 | Bidirectional Bridge Exclusion Theorem | SUPPORTED | For P=N+(x)∩N-(y), H=N+(y)∩N-(x), all P–H adjacencies point H→P. |
| T33 | 4 | Bridge Deficit Theorem | SUPPORTED_CONDITIONAL | For bridge size s, d^-(x)≤n-d-s+ceil(s/3)-2. |
| T34 | 4 | Reverse-Bridge Capacity Theorem | SUPPORTED | d^-(x)≤n-d-(s+1)/2; at n=3d, d^-(x)≤2d-(s+1)/2. |
| T35 | 4 | Total Bridge Energy Identity | SUPPORTED | For fixed x, Q_x=Σ_{y∈M_x}q(x,y)=d²-e(N+(x))≥d(d+1)/2. |
| T36 | 4 | Indegree–Bridge Amplification Theorem | SUPPORTED | Some nonneighbor y has q(x,y)≥ceil(d(d+1)/(2(2d-1-d^-(x)))) at n=3d. |
| T37 | 4 | Exact Closure Criterion | SUPPORTED_SUFFICIENT_CONDITIONS | Any of several explicit bridge-amplification or deficit inequalities would close the kernel. |
| T38 | 4 | Half-Bridge Closure Theorem | SUPPORTED_IMPLICATION_ONLY | If every nonedge had q(x,y)≤(d-1)/2, global escape mass would contradict the exact nonedge count. |
| T39 | 4 | Half-Bridge Failure Structure Theorem | SUPPORTED | Failure of the half-bridge premise yields a large one-way rectangular certificate P,H around a nonedge. |
| T40 | 5 | High-Indegree Root Theorem | SUPPORTED | Some vertex has indegree at least d. |
| T41 | 5 | Root Escape-Energy Theorem | SUPPORTED | For high-indegree root x, Σ_{y∈M}q_y=d²-e(A)≥d(d+1)/2. |
| T42 | 5 | Bridge Export Theorem | SUPPORTED | For bridge P of size s, e(P,U)≥s(d-1)-binom(s,2), yielding 2r+s≤4d-3 at n=3d. |
| T43 | 5 | Reverse-Wall Theorem | SUPPORTED | For R=N+(y), E(R,P)=∅. |
| T44 | 5 | Two-Block Degree Identity | SUPPORTED | Exact outgoing-degree decomposition for P∪R with E(R,P)=∅. |
| T45 | 5 | Bridge Collision Identity | SUPPORTED | Σ_{z∈M}binom(q(x,z),2)=Σ_{pairs {a,b}⊂A}|N+(a)∩N+(b)∩M|. |
| T46 | 5 | Double-Wall Escape Theorem | SUPPORTED_CONDITIONAL | A large common forward target set C forces |N-(a)∪N-(b)|≤2d-|C|+ceil(|C|/3)-1. |
| T47 | 5 | Transitive-Fan Obstruction Theorem | STRUCTURAL_DIAGNOSIS | Large common in- and out-neighborhoods can coexist as a transitive layered configuration without forming a directed triangle. |
| T48 | 5 | Fan-Reversal Closure Criterion | SUPPORTED | For I=N-(a)∩N-(b), C=N+(a)∩N+(b), E(C,I)=∅; any forced C→I arc closes a triangle. |
| T49 | 5 | One-Way Fan Capacity Inequality | SUPPORTED | |I|≤2d-(|C|+1)/2 at n=3d. |
| T50 | 6 | Cubic-Zero Theorem | SUPPORTED | tr(A³)=0. |
| T51 | 6 | Reverse-Arc Annihilation Theorem | SUPPORTED | A²∘Aᵀ=0. |
| T52 | 6 | Two-Path Mass Theorem | SUPPORTED | Σ_{x,y}(A²)_{xy}=nd². |
| T53 | 6 | Exact Support Partition Theorem | SUPPORTED | Two-path mass partitions into transitive-arc endpoints and nonadjacent endpoints; reverse-arc entries vanish. |
| T54 | 6 | Escape-Mass Floor | SUPPORTED | Σ_{ordered nonedges}(A²)_{xy}≥nd(d+1)/2. |
| T55 | 6 | Two-Path Collision Theorem | SUPPORTED | ||A²||_F²=Σ_{u,v}|N-(u)∩N-(v)|·|N+(u)∩N+(v)|. |
| T56 | 6 | Global Fan-Energy Identity | SUPPORTED | The common-in/common-out rectangle energy equals ||A²||_F². |
| T57 | 6 | Row Concentration Theorem | SUPPORTED | Σ_yQ_{xy}²≥d⁴/(n-1-d^-(x)). |
| T58 | 6 | Fan-Energy Floor | SUPPORTED | At n=3d, ||A²||_F²≥nd⁴/(2d-1)=3d⁵/(2d-1). |
| T59 | 6 | Multiplicity-Collapse Obstruction | STRUCTURAL_DIAGNOSIS | A lower bound on ||A²||_F² can concentrate on few ordered pairs and does not force many distinct forbidden pairs. |
| T60 | 6 | Maximal-Bridge Matrix Theorem | SUPPORTED | If μ=max Q_{xy}, then μ≥d²/(2d-1)>d/2 at n=3d. |
| T61 | 6 | Large Transitive-or-Escape Fan Theorem | SUPPORTED | Some ordered pair has more than d/2 internally distinct two-paths; endpoints are either adjacent forward or nonadjacent. |
| T62 | 6 | Fan-Coherence Closure Theorem | PROPOSAL_UNVERIFIED | A sufficiently large exact twin class inside a fan should admit quotient compression to a smaller counterexample. |
| T63 | 6 | Fan-Union Inequality | SUPPORTED | |∪S_p|≥(Σ|S_p|)²/Σ|S_p∩S_q| and Σ|S_p|≥sd-binom(s,2). |
| T64 | 6 | Second-Order Concentration Theorem | SUPPORTED | Some p,q in a fan have a common external outneighbor set at least the average lower bound from T63. |
| T65 | 6 | Fan Cascade Theorem | RETRACTED_OVERCLAIM | The second-order concentration was described as recursively iterable; that iteration was not proved. |
| T66 | 7 | Fan Rectangle Prohibition Theorem | SUPPORTED | For I=N-(u)∩N-(v), C=N+(u)∩N+(v), E(C,I)=∅. |
| T67 | 7 | Universal Fan Capacity Theorem | SUPPORTED | I(u,v)+(C(u,v)+1)/2≤2d at n=3d. |
| T68 | 7 | Universal Indegree Ceiling | SUPPORTED | d^-(u)≤(3d-3)/2. |
| T69 | 7 | Common-Out Sum Identity | SUPPORTED | Σ_{u,v}C(u,v)=Σ_w d^-(w)². |
| T70 | 7 | Fan Energy Identity | SUPPORTED | ||A²||_F²=Σ_{u,v}I(u,v)C(u,v). |
| T71 | 7 | Common-Out Energy Floor | SUPPORTED | ΣC(u,v)²≥(ΣC(u,v))²/n². |
| T72 | 7 | Two-Path Energy Floor | SUPPORTED | ||A²||_F²≥nd⁴/(2d-1) at n=3d. |
| T73 | 7 | Fan-Capacity Saturation Theorem | SUPPORTED | C·Λ equals missing internal adjacencies in C plus missing permitted outgoing arcs from C. |
| T74 | 7 | Global Slack Identity | SUPPORTED | 2dS-||A²||_F²-(T+S)/2=Σ C(u,v)Λ(u,v). |
| T75 | 7 | Elimination-Ordering Theorem | SUPPORTED_CONDITIONAL | Every proper S has an ordering with each removed vertex having residual outdegree below one third of the remaining order. |
| T76 | 7 | Exact Hereditary Edge Bound | RETRACTED | Claimed e(D[S])≤Σ(ceil(t/3)-1); false because backward arcs are not counted. |
| T77 | 7 | Hereditarily Sharpened Fan Capacity Theorem | RETRACTED | Used the false T76 to replace the coefficient 1/2 by 5/6. |
| T78 | 7 | Coefficient Required for Closure | CONDITIONAL_META | Within a simplified pointwise fan-capacity/energy architecture, an unrealistically large coefficient would be needed for closure. |
| T79 | 7 | One-Pair Strategy Impossibility Theorem | STRUCTURAL_DIAGNOSIS | Pairwise fan statistics plus first/second moments are quantitatively insufficient in the analyzed architecture. |
| T80 | 7 | Triple-Fan Prohibition Theorem | SUPPORTED | For triple common-in I₃ and common-out C₃, E(C₃,I₃)=∅. |
| T81 | 8 | Five-Sixths Escape Theorem | RETRACTED | Claimed e(A,M)≥d²-F(d)≈5d²/6. |
| T82 | 8 | Five-Sixths Bridge Theorem | RETRACTED | Claimed a bridge of size ≈5d/6 from a high-indegree root. |
| T83 | 8 | Hereditary Bridge Export Theorem | RETRACTED | Used false edge bound inside a bridge. |
| T84 | 8 | Seven-Sixths Indegree Barrier | RETRACTED | Claimed high roots or all vertices satisfy d^-(x)≤7d/6+O(1). |
| T85 | 8 | Low-Indegree Mass Bound | RETRACTED | Derived distributional bounds from T84. |
| T86 | 8 | Near-Regular Core Theorem | RETRACTED | Derived a large near-inregular core from T84. |
| T87 | 8 | Boundary Bridge Rigidity Theorem | RETRACTED | Near 7d/6 was claimed to force almost-full bridges. |
| T88 | 8 | Full-Bridge Boundary Theorem | RETRACTED | Used F(d) from the false hereditary edge bound. |
| T89 | 8 | Multi-Sink Rigidity Theorem | RETRACTED | Near-boundary roots claimed to force many almost-full sinks. |
| T90 | 8 | Blow-Up Backflow Prohibition Theorem | PARTIAL_LOCAL_FACT | The local fact a→y implies N+(y)∩N-(a)=∅ is valid; the global near-complete blow-up conclusion was not. |
| T91 | 8 | Inneighborhood-Union Closure Criterion | PROPOSAL | A sufficiently large union of forbidden inneighborhoods would deprive a sink of d legal outtargets. |
| T92 | 8 | Three-Layer Product-Zero Theorem | SUPPORTED | For B=N-(x), A=N+(x), M=M_x, tr(XYZ)=0 for cyclic matrices B→A, A→M, M→B. |
| T93 | 8 | Tripartite Closure Criterion | PROPOSAL_UNVERIFIED | A sufficiently strong tripartite supersaturation inequality would make tr(XYZ)>0. |
| T94 | 9 | Corrected High-Root Barrier | RETRACTED | The numerical barrier still depended on the false F(s) edge bound. |
| T95 | 9 | A-to-B Zero Theorem | SUPPORTED | E(A,B)=∅. |
| T96 | 9 | First Cyclic-Layer Lower Bound | RETRACTED | Used d²-F(d). |
| T97 | 9 | M-to-B Lower Bound | RETRACTED | Used F(m). |
| T98 | 9 | B-to-A Lower Bound | RETRACTED | Used F(r), F(m). |
| T99 | 9 | Three-Layer Density Ledger | RETRACTED | All three cyclic layer bounds depended on T76. |
| T100 | 9 | Mantel Gap Theorem | RETRACTED_ROUTE | The apparent near-Mantel contradiction was an artifact of the retracted density ledger. |
| T101 | 9 | Split-Chamber Obstruction Theorem | STRUCTURAL_DIAGNOSIS | Whole-chamber bipartite cuts are constructions, not automatic upper bounds for triangle-free subgraphs of a tripartite host. |
| T102 | 9 | Forbidden-Rectangle Union Theorem | SUPPORTED | e(M,B)+|∪_{a∈A}(N_M^+(a)×N_B^-(a))|≤mr. |
| T103 | 9 | Anticorrelation-or-Overlap Closure Theorem | PROPOSAL | Closure follows if rectangle areas correlate positively and their overlap is controlled. |
| T104 | 10 | One-Sided Peeling Does Not Count All Arcs | SUPPORTED | Residual outdegree sums count only forward arcs in the peeling order. |
| T105 | 10 | Exact Refutation of the Hereditary Edge Bound | SUPPORTED | A transitive tournament can have zero residual outdegree under a removal order while containing binom(s,2) arcs. |
| T106 | 10 | Outneighborhood Wall Theorem | SUPPORTED | E(A,B)=∅. |
| T107 | 10 | Exact Local Defect Identity | SUPPORTED | e(A,M)=d(d+1)/2+σ(x). |
| T108 | 10 | Reverse-Arc Annihilation Theorem | SUPPORTED | A²∘Aᵀ=0. |
| T109 | 10 | Two-Path Conservation Theorem | SUPPORTED | A²1=d²1 and ΣQ=nd². |
| T110 | 10 | Valid Indegree Ceiling | SUPPORTED | d^-(x)≤(3d-3)/2. |
| T111 | 10 | Correct Terminal Obstruction Theorem | SUPPORTED_SUMMARY | The audited elementary kernel forces escape mass but permits backward density, overlap, concentration, and long-range folding. |
| T112 | 10 | Machine Closure Contract | PROTOCOL | A genuine close requires an exact rational certificate, a verified new structural lemma, or an exact bounded surviving model. |
| T113 | 11 | Rooted Chamber Equations | SUPPORTED | Rooted sizes and E(A,B)=∅; d²=e(A)+e(A,M). |
| T114 | 11 | Rooted Cyclic Product-Zero Theorem | SUPPORTED | Σ_{b,a,m}X_{ba}Y_{am}Z_{mb}=0. |
| T115 | 11 | Tripartite Union-Bound Theorem | SUPPORTED | m e(B,A)+r e(A,M)+d e(M,B)≤2drm. |
| T116 | 11 | Valid M-to-B Floor | SUPPORTED | e(M,B)≥max(0,d(d+1)/2-binom(m,2)). |
| T117 | 11 | Exact B-to-A Ledger | SUPPORTED | e(B,A)=rd-r-e(B)-e(B,M), with a derived lower bound using M–B capacity. |
| T118 | 11 | Missing Cyclic Edge Theorem | SUPPORTED_DIAGNOSIS | Current valid bounds force A→M strongly and sometimes M→B, but not B→A quadratically. |
| T119 | 11 | Backward Reservoir Theorem | SUPPORTED | If e(B,A) is small, exact degree accounting forces e(B)+e(B,M) large. |
| T120 | 11 | Backward-Hierarchy Theorem | SUPPORTED_CONDITIONAL | Hereditary deficit gives a peeling order on B; dense internal arcs may point backward across it. |
| T121 | 11 | Two-Reservoir Classification Theorem | STRUCTURAL_SYNTHESIS | A surviving rooted profile stores B-degree internally or in the reverse B→M direction. |
| T122 | 11 | Pair-Marginal Phantom Theorem | PROPOSAL_MODEL | Pairwise chamber marginals admit a zero-cyclic-product profile; no actual global graph was constructed. |
| T123 | 11 | Five-Flag Necessity Theorem | METHODOLOGICAL | Rooted four-flags do not retain the correlation between internal B hierarchy, B→A degree, and A→M neighborhoods. |
| R12-T124 | 12 | Second-Neighborhood Deficit Theorem | SUPPORTED | |N^{++}(v)\N+(v)|≥(d+1)/2. |
| R12-T125 | 12 | Folding Creates Codegree | SUPPORTED | If two-step mass folds into a small support, row energy forces high multiplicity. |
| R12-T126 | 12 | Concentration Self-Bound | PARTIAL_RETRACTED | The exact row-energy and indegree inequalities were valid; the derived numerical q≥0.68614d was invalid. |
| R12-T127 | 12 | Forced Double-Codegree Alternative | PROPOSAL_QUALITATIVE | Insufficient expansion should create a large common-out set and forbidden rectangle. |
| R13-T124 | 13 | Retraction of the 0.686d Fan Bound | SUPPORTED | The denominator inequality was substituted in the wrong direction; q≥0.68614d is withdrawn. |
| R13-T125 | 13 | Maximum-Fan Kernel | SUPPORTED | For a high-indegree root, some two-path fan has q≥d²/(2d-1)>d/2. |
| R13-T126 | 13 | Zero-Support Maximum-Fan Inequality | SUPPORTED | d²≤q(3d-1-d^-(p)) for a fan vertex p. |
| R13-T127 | 13 | Fan-to-Inneighborhood Rectangle | SUPPORTED | For P⊆N-(y), ∪_{p∈P}N-(p) is disjoint from N+(y), hence has size at most 2d. |
| R13-T128 | 13 | Weighted Maximum-Fan Selection | SUPPORTED | Some nonempty P_{xy} has average indegree at least d. |
| R13-T129 | 13 | Dual Fan Theorem | SUPPORTED | There are x,z,y and C⊆N+(x)∩N+(z)∩N-(y) with |C|≥|P|/2 for a weighted fan P. |
| T130 | 14 | First Three Vanishing Trace Theorem | SUPPORTED | tr(A)=tr(A²)=tr(A³)=0. |
| T131 | 14 | Perron Moment Cancellation Theorem | SUPPORTED | The non-Perron eigenvalues cancel d in the first three power sums. |
| T132 | 14 | Singular-Energy Budget Theorem | SUPPORTED | ||A||_F²=3d² and residual singular-value squared mass is at most 2d². |
| T133 | 14 | Spectral Modulus Budget | SUPPORTED | Σ_{i≥2}|λ_i/d|²≤2. |
| T134 | 14 | Cubic Defect Identity | SUPPORTED | Σ μ_i(1-μ_i)=Σ μ_i²(1-μ_i)=Σ μ_i(1-μ_i)²=0. |
| T135 | 14 | Real-Part Defect Formula | SUPPORTED | Re[z(1-z)²]=r cosθ-2r² cos2θ+r³ cos3θ. |
| T136 | 14 | Peripheral Period Theorem | SUPPORTED_STANDARD | For irreducible d-regular A, peripheral eigenvalues are d times roots of unity determined by the period. |
| T137 | 14 | Aperiodicity Theorem | SUPPORTED_CONDITIONAL | A minimal kernel is primitive after eliminating periods 2 and 3. |
| T138 | 14 | Strong Connectivity Theorem | SUPPORTED_CONDITIONAL | A smallest counterexample is strongly connected. |
| T139 | 14 | Strict Spectral Radius Gap | SUPPORTED_CONDITIONAL | All non-Perron eigenvalues satisfy |λ|<d. |
| T140 | 14 | Abstract Spectral Phantom | STRUCTURAL_DIAGNOSIS | The abstract finite moment system may be feasible; moments alone do not encode entrywise support. |
| T141 | 14 | Energy Equality Rigidity Theorem | SUPPORTED | Equality in the continuous row-energy floor forces d=1; for d>1 the inequality is strict. |
| T142 | 14 | Exact Integral Row-Energy Floor | SUPPORTED | If d²=kq+t, the integer row energy is at least (k-t)q²+t(q+1)². |
| T143 | 15 | Opposite Two-Path Product Theorem | SUPPORTED | For Q=A², tr(A⁴)=Σ_{x,y}Q_{xy}Q_{yx}=4C4(D). |
| T144 | 15 | Opposite Vertices Are Nonadjacent | SUPPORTED | Opposite vertices of a directed 4-cycle are nonadjacent. |
| T145 | 15 | Exact Nonedge Count | SUPPORTED | The number of unordered nonedges is 3d(d-1)/2. |
| T146 | 15 | Escape-Mass Floor | SUPPORTED | The ordered nonedge two-path mass is at least 3d²(d+1)/2. |
| T147 | 15 | Forced Opposite-Path Product Theorem | SUPPORTED | Σ_{unordered nonedges}Q_{xy}Q_{yx}≥3d³. |
| T148 | 15 | Cubic Directed-C4 Theorem | SUPPORTED_TERMINAL_ASSET | C4(D)≥ceil(3d³/2), equivalently tr(A⁴)≥6d³. |
| T149 | 15 | Every Kernel Contains a Directed C4 | SUPPORTED | A triangle-free exact-boundary regular kernel necessarily contains a directed 4-cycle. |
| T150 | 15 | Heavy Four-Cycle Vertex Theorem | SUPPORTED | Some vertex lies on at least 2d² directed 4-cycles. |
| T151 | 15 | Heavy Bidirectional Bridge Theorem | SUPPORTED | Some nonedge {x,y} has Q_{xy}Q_{yx}≥ceil(2d²/(2d-1)). |
| T152 | 15 | Asymmetric Four-Cycle Reservoir Theorem | STRUCTURAL_DIAGNOSIS | The C4 lower bound is compatible with Q_{xy}≈d and Q_{yx}=O(1) on significant pairs. |
| T153 | 15 | Exact Fourth-Moment Decomposition | SUPPORTED | tr(A⁴)=||A²||_F²-(1/2)||A²-(Aᵀ)²||_F²; C4 is one quarter of this. |

## Court

- `THEOREM_CLOSURE`: **NO**
- `PRINCIPAL RESULT`: source-claimed cubic directed-C4 lower bound
- `EXACT OPEN OBLIGATION`: skew two-path energy closure
- `RETRACTION AUDIT`: part of this public ledger; retracted branches above must not be reused as live mathematics.
