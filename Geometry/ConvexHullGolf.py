s=map(int,open(0).read().split()[1:])
P=sorted(zip(s,s))
L=[]
for p in P+P[-2::-1]:
 x,y=p
 while(n:=len(L))>1 and(x-L[-1][0])*(y-L[-2][1])<(y-L[-1][1])*(x-L[-2][0]):L.pop()
 L+=p,
p=print
p(n)
for i in L[1:]:p(*i)