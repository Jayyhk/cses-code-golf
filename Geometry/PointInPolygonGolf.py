S=map(int,open(0).read().split())
n=next(S)
next(S)
o=[*zip(S,S)]
for f,t in o[n:]:
 b=c=0
 d,r=o[n-1]
 for e,s in o[:n]:
  A=e-d
  B=t-r
  C=s-r
  D=f-d
  b|=A*B==C*D and D*(D-A)<1>B*(B-C)
  c^=(r>t)^(s>t)and D<B*A/C
  d=e
  r=s
 print(["OUTSIDE","BOUNDARY","INSIDE"][b or -c])