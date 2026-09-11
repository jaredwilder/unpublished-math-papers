#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 50
#define MAXE 512
static uint64_t edges[MAXE]; static uint64_t solutions[20000]; static int E=0,best=N+1,solution_count=0; static unsigned long long nodes=0; static uint64_t first_cover=0,core_independent=~0ULL;
static int cmp_u64(const void *a,const void*b){uint64_t x=*(const uint64_t*)a,y=*(const uint64_t*)b;return x<y?-1:x>y;}
static void add_edge(uint64_t m){for(int i=0;i<E;i++)if(edges[i]==m)return;edges[E++]=m;}
static int isqrt_int(int x){int r=0;while((r+1)*(r+1)<=x)r++;return r;}
static int pop(uint64_t x){return __builtin_popcountll(x);}
static void build(void){
 add_edge(1ULL);
 for(int x=1;x<=N;x++)for(int y=x;y<=N;y++){int z=x*y;if(z>N)break;uint64_t m=(1ULL<<(x-1))|(1ULL<<(y-1))|(1ULL<<(z-1));add_edge(m);}
 for(int a=1;a<=N;a++)for(int c=a+1;c<=N;c++){int b=isqrt_int(a*c);if(b*b==a*c&&a<b&&b<c)add_edge((1ULL<<(a-1))|(1ULL<<(b-1))|(1ULL<<(c-1)));}
 qsort(edges,E,sizeof(uint64_t),cmp_u64);
}
static void dfs(uint64_t cover){
 nodes++;int k=pop(cover);if(k>best)return;
 uint64_t rem[MAXE];int R=0;for(int i=0;i<E;i++)if(!(edges[i]&cover))rem[R++]=edges[i];
 if(!R){uint64_t full=(1ULL<<N)-1,ind=full^cover;if(k<best){best=k;solution_count=0;first_cover=cover;core_independent=ind;}if(k==best){for(int i=0;i<solution_count;i++)if(solutions[i]==cover)return;solutions[solution_count++]=cover;core_independent&=ind;}return;}
 uint64_t used=0;int lb=0;for(int i=0;i<R;i++){uint64_t e=rem[i];if(!(e&used)){used|=e;lb++;}}
 if(k+lb>best)return;
 int freq[N];memset(freq,0,sizeof(freq));for(int i=0;i<R;i++)for(int v=0;v<N;v++)if(rem[i]&(1ULL<<v))freq[v]++;
 int pick=0,bestsize=99,bestscore=-1;for(int i=0;i<R;i++){int sz=pop(rem[i]),score=0;for(int v=0;v<N;v++)if(rem[i]&(1ULL<<v))score+=freq[v];if(sz<bestsize||(sz==bestsize&&score>bestscore)){pick=i;bestsize=sz;bestscore=score;}}
 uint64_t e=rem[pick];int verts[N],nv=0;for(int v=0;v<N;v++)if(e&(1ULL<<v))verts[nv++]=v;
 for(int i=0;i<nv;i++)for(int j=i+1;j<nv;j++)if(freq[verts[j]]>freq[verts[i]]){int t=verts[i];verts[i]=verts[j];verts[j]=t;}
 for(int i=0;i<nv;i++)dfs(cover|(1ULL<<verts[i]));
}
static void print_set(uint64_t m){int first=1;putchar('[');for(int v=0;v<N;v++)if(m&(1ULL<<v)){if(!first)putchar(',');printf("%d",v+1);first=0;}puts("]");}
int main(void){build();dfs(0);uint64_t full=(1ULL<<N)-1,first=full^first_cover;
 printf("limit=%d\n",N);printf("edge_count=%d\n",E);printf("minimum_transversal=%d\n",best);printf("maximum=%d\n",N-best);printf("extremal_count=%d\n",solution_count);printf("nodes=%llu\n",nodes);printf("first_witness=");print_set(first);printf("extremizer_core=");print_set(core_independent);
 return (best==15&&solution_count==240)?0:1;
}