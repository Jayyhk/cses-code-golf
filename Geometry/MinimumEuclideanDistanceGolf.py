from bisect import*
I=map(int,open(0).read().split()[1:])
P=sorted(zip(I,I))
d=9e18
S=[]
r=0
for x,y in P:
 D=d**.5
 while x-P[r][0]>D:
  X,Y=P[r]
  S.remove((Y,X))
  r+=1
 for Y,X in S[bisect_left(S,(y-D,)):]:
  w=Y-y
  if w*w>d:break
  d=min(d,(X-x)**2+w*w)
 insort(S,(y,x))
print(d)