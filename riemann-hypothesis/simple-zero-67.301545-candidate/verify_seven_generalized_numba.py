import math,time,itertools,sys
import numpy as np
import mpmath as mp
from numba import njit
mp.iv.dps=50; iv=mp.iv
G=int(sys.argv[1]) if len(sys.argv)>1 else 1000
QN=int(sys.argv[2]) if len(sys.argv)>2 else 29
QD=int(sys.argv[3]) if len(sys.argv)>3 else 100000
TN=int(sys.argv[4]) if len(sys.argv)>4 else 341
TD=int(sys.argv[5]) if len(sys.argv)>5 else 100000
q=QN/QD; target=TN/TD
cut=math.ceil(TN*QD*G/(TD*QN)); ncell=cut+8
coeff=np.zeros(7); coeff[1:]=[1/3,2/5,1/2,2/3,1,2]
cd=np.nextafter(coeff,-np.inf); cu=np.nextafter(coeff,np.inf)
qlo=np.nextafter(q,-np.inf); qhi=np.nextafter(q,np.inf); targetup=np.nextafter(target,np.inf)
SQ2=iv.sqrt(2); ISQ2=1/SQ2; PI=iv.pi; K0=SQ2*iv.sin(ISQ2)
def ends(x): return float(x.a),float(x.b)
def cell(i):
 lo=0 if i==0 else math.nextafter(i/G,-math.inf); hi=math.nextafter((i+1)/G,math.inf); return iv.mpf([lo,hi])
def sinciv(z):
 lo,hi=ends(z)
 if lo<=0<=hi:
  M=max(abs(lo),abs(hi)); assert M<.01
  return iv.mpf([math.nextafter(1-M*M/6,-math.inf),1.0])
 return iv.sin(z)/z
def deriv(x):
 zl=PI*x-ISQ2;zr=PI*x+ISQ2
 def sd(z):
  s=iv.sin(z);c=iv.cos(z);z2=z*z
  return s/z,(z*c-s)/z2,((2-z2)*s-2*z*c)/(z2*z)
 l,lp,lpp=sd(zl);r,rp,rpp=sd(zr)
 raw=(l+r)/2; rp0=PI*(lp+rp)/2; rpp0=PI*PI*(lpp+rpp)/2;ns=K0*K0
 return raw*raw/ns,2*raw*rp0/ns,2*(rp0*rp0+raw*rpp0)/ns

t=time.time(); table=np.empty(ncell)
for i in range(ncell):
 x=cell(i);f=2*PI*x;k=((sinciv((SQ2-f)/2)+sinciv((SQ2+f)/2))/2)/K0;lo,hi=ends(k)
 table[i]=0 if lo<=0<=hi else math.nextafter(min(abs(lo),abs(hi))**2,-math.inf)
start2=math.floor(.95*G); second=np.full(ncell,-np.inf)
for i in range(start2,ncell): second[i]=math.nextafter(ends(deriv(cell(i))[2])[0],-math.inf)
hmax=2*ncell+16; plo=np.zeros(hmax);dlo=np.full(hmax,-np.inf);dhi=np.full(hmax,np.inf)
for h in range(2*start2,hmax):
 x0=h/(2*G); x=iv.mpf([math.nextafter(x0,-math.inf),math.nextafter(x0,math.inf)]);p,d,_=deriv(x); pl,_=ends(p); dl,dh=ends(d)
 plo[h]=math.nextafter(pl,-math.inf);dlo[h]=math.nextafter(dl,-math.inf);dhi[h]=math.nextafter(dh,np.inf)
print('tables',time.time()-t,'ncell',ncell,flush=True)
def rmqmat(v):
 levels=(len(v)).bit_length(); out=np.full((levels,len(v)),np.inf);out[0,:]=v;w=1
 for lev in range(1,levels):
  half=w;w*=2
  upto=len(v)-w+1
  if upto<=0:break
  out[lev,:upto]=np.minimum(out[lev-1,:upto],out[lev-1,half:half+upto])
 return out
rt=rmqmat(table); rs=rmqmat(second)
# components surviving one-body
sur=[]
for i in range(cut):
 one=math.nextafter(qlo*math.nextafter(i/G,-math.inf),-math.inf)
 one=math.nextafter(one+math.nextafter(cd[1]*table[i],-math.inf),-math.inf)
 if one<targetup:sur.append(i)
com=[]
for i in sur:
 if not com or i>com[-1][1]+1:com.append([i,i])
 else:com[-1][1]=i
print('components',com,'surv',len(sur),flush=True)
init=np.array([sum(([a,b] for a,b in parts),[]) for parts in itertools.product(com,repeat=6)],dtype=np.int64)

@njit
def rmq(qm,l,r):
 n=r-l+1;lev=0
 while (1<<(lev+1))<=n:lev+=1
 w=1<<lev
 a=qm[lev,l];b=qm[lev,r-w+1]
 return a if a<b else b
@njit
def dadd(a,b):return np.nextafter(a+b,-np.inf)
@njit
def uadd(a,b):return np.nextafter(a+b,np.inf)
@njit
def mulint(al,ah,bl,bh):
 p1=al*bl;p2=al*bh;p3=ah*bl;p4=ah*bh
 lo=min(p1,p2,p3,p4);hi=max(p1,p2,p3,p4)
 return np.nextafter(lo,-np.inf),np.nextafter(hi,np.inf)
@njit
def subint(al,ah,bl,bh):return np.nextafter(al-bh,-np.inf),np.nextafter(ah-bl,np.inf)
@njit
def divint(al,ah,bl,bh):
 # bl>0
 p1=al/bl;p2=al/bh;p3=ah/bl;p4=ah/bh
 return np.nextafter(min(p1,p2,p3,p4),-np.inf),np.nextafter(max(p1,p2,p3,p4),np.inf)
@njit
def interval_pd(terms_start,terms_span,terms_c,nt):
 Ml=np.zeros((6,6));Mh=np.zeros((6,6))
 for z in range(nt):
  st=terms_start[z];sp=terms_span[z];c=terms_c[z]
  for i in range(st,st+sp):
   for j in range(st,st+sp):
    Ml[i,j]=dadd(Ml[i,j],c);Mh[i,j]=uadd(Mh[i,j],c)
 Ll=np.zeros((6,6));Lh=np.zeros((6,6));Dl=np.zeros(6);Dh=np.zeros(6)
 for col in range(6):
  Ll[col,col]=1;Lh[col,col]=1;pl=Ml[col,col];ph=Mh[col,col]
  for j in range(col):
   al,ah=mulint(Ll[col,j],Lh[col,j],Ll[col,j],Lh[col,j]);al,ah=mulint(al,ah,Dl[j],Dh[j]);pl,ph=subint(pl,ph,al,ah)
  if pl<=0:return False
  Dl[col]=pl;Dh[col]=ph
  for row in range(col+1,6):
   vl=Ml[row,col];vh=Mh[row,col]
   for j in range(col):
    al,ah=mulint(Ll[row,j],Lh[row,j],Ll[col,j],Lh[col,j]);al,ah=mulint(al,ah,Dl[j],Dh[j]);vl,vh=subint(vl,vh,al,ah)
   Ll[row,col],Lh[row,col]=divint(vl,vh,pl,ph)
 return True

@njit
def run(init,rt,rs,plo,dlo,dhi,cd,cu,qlo,qhi,target,targetup,G,cut,start2,hmax,maxstack=2000000):
 stack=np.zeros((maxstack,13),dtype=np.int64);top=0
 for z in range(init.shape[0]):
  stack[top,:12]=init[z];stack[top,12]=0;top+=1
 nodes=pruned=splits=tpr=ipr=ppr=0;maxdep=0
 fail=np.zeros(13,dtype=np.int64)
 ts=np.empty(21,dtype=np.int64);tp=np.empty(21,dtype=np.int64);tc=np.empty(21)
 while top>0:
  top-=1;b=stack[top].copy();nodes+=1;dep=b[12];maxdep=max(maxdep,dep)
  sl=0
  for j in range(6):sl+=b[2*j]
  if sl>=cut:pruned+=1;ppr+=1;continue
  lp=np.zeros(7,np.int64);hp=np.zeros(7,np.int64)
  for j in range(6):lp[j+1]=lp[j]+b[2*j];hp[j+1]=hp[j]+b[2*j+1]
  xlo=np.nextafter(lp[6]/G,-np.inf); lower=np.nextafter(qlo*xlo,-np.inf)
  for sp in range(1,7):
   for st in range(7-sp):
    l=lp[st+sp]-lp[st];r=hp[st+sp]-hp[st]+sp-1
    km=0.0 if r>=rt.shape[1] else rmq(rt,l,r)
    lower=dadd(lower,np.nextafter(cd[sp]*km,-np.inf))
  if lower>=targetup:pruned+=1;ipr+=1;continue
  # build Hessian lower terms + float LDL heuristic
  heur=np.zeros((6,6));nt=0;ok=True
  for sp in range(1,7):
   for st in range(7-sp):
    l=lp[st+sp]-lp[st];r=hp[st+sp]-hp[st]+sp-1
    if r>=rs.shape[1]:ok=False;break
    sec=rmq(rs,l,r)
    if not np.isfinite(sec):ok=False;break
    c=cd[sp] if sec>=0 else cu[sp];sc=np.nextafter(c*sec,-np.inf)
    ts[nt]=st;tp[nt]=sp;tc[nt]=sc;nt+=1
    for i in range(st,st+sp):
     for j in range(st,st+sp):heur[i,j]+=sc
   if not ok:break
  tangent=-np.inf
  if ok:
   # cheap LDL
   L=np.zeros((6,6));D=np.zeros(6);pd=True
   for col in range(6):
    pv=heur[col,col]
    for j in range(col):pv-=L[col,j]*L[col,j]*D[j]
    if pv<=1e-11:pd=False;break
    D[col]=pv;L[col,col]=1
    for row in range(col+1,6):
     vv=heur[row,col]
     for j in range(col):vv-=L[row,j]*L[col,j]*D[j]
     L[row,col]=vv/pv
   if pd:
    mid=np.zeros(6,np.int64); rad=np.zeros(6)
    sm=0
    for j in range(6):
     mid[j]=b[2*j]+b[2*j+1]+1;sm+=mid[j];rad[j]=np.nextafter((b[2*j+1]-b[2*j]+1)/(2*G),np.inf)
    smlo=np.nextafter(sm/(2*G),-np.inf); val=np.nextafter(qlo*smlo,-np.inf)
    gl=np.full(6,qlo);gh=np.full(6,qhi)
    valid=True
    for sp in range(1,7):
     for st in range(7-sp):
      hiidx=0
      for j in range(st,st+sp):hiidx+=mid[j]
      if hiidx<2*start2 or hiidx>=hmax:valid=False;break
      val=dadd(val,np.nextafter(cd[sp]*plo[hiidx],-np.inf))
      dl=dlo[hiidx];dh=dhi[hiidx]
      ccl=cu[sp] if dl<0 else cd[sp]; cch=cu[sp] if dh>0 else cd[sp]
      xl=np.nextafter(ccl*dl,-np.inf);xh=np.nextafter(cch*dh,np.inf)
      for j in range(st,st+sp):gl[j]=dadd(gl[j],xl);gh[j]=uadd(gh[j],xh)
     if not valid:break
    if valid:
     tangent=val
     for j in range(6):tangent=np.nextafter(tangent-max(abs(gl[j]),abs(gh[j]))*rad[j],-np.inf)
     if tangent>=target:
      if interval_pd(ts,tp,tc,nt):pruned+=1;tpr+=1;continue
  # split or fail terminal
  maxw=-1;coord=0
  for j in range(6):
   w=b[2*j+1]-b[2*j]
   if w>maxw:maxw=w;coord=j
  if maxw==0:
   fail[:]=b;fail[12]=nodes
   return False,nodes,pruned,splits,maxdep,ppr,ipr,tpr,fail,lower,tangent,top
  splits+=1;lo=b[2*coord];hi=b[2*coord+1];md=(lo+hi)//2
  if top+2>=maxstack:
   fail[:]=b;fail[12]=-999
   return False,nodes,pruned,splits,maxdep,ppr,ipr,tpr,fail,lower,tangent,top
  stack[top]=b;stack[top,2*coord]=lo;stack[top,2*coord+1]=md;stack[top,12]=dep+1;top+=1
  stack[top]=b;stack[top,2*coord]=md+1;stack[top,2*coord+1]=hi;stack[top,12]=dep+1;top+=1
 return True,nodes,pruned,splits,maxdep,ppr,ipr,tpr,fail,0.,0.,top

# compile/run
res=run(init,rt,rs,plo,dlo,dhi,cd,cu,qlo,qhi,target,targetup,G,cut,start2,hmax)
print('RESULT',res[:8],'fail',res[8],'lower/tan/top',res[9:], 'total_sec',time.time()-t,flush=True)
