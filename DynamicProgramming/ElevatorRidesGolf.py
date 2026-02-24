R=range
n,x,*w=map(int,open(0).read().split())
s=1<<n
d=[(n,x)]*s
d[0]=1,0
for i in R(1,s):
 for j in R(n):
  if i>>j&1:
   p,q=d[i^1<<j]
   q+=w[j]
   d[i]=min(d[i],(p+1,w[j])if q>x else(p,q))
print(d[-1][0])