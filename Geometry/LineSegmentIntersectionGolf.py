_,*l=open(0)
m=min
M=max
for s in l:
 a,b,c,d,e,f,g,h=map(int,s.split())
 A=c-a
 B=d-b
 C=g-e
 D=h-f
 print('NO'*(M(a,c)<m(e,g)or M(e,g)<m(a,c)or M(b,d)<m(f,h)or M(f,h)<m(b,d)or(A*(f-b)-B*(e-a))*(A*(h-b)-B*(g-a))>0 or(C*(b-f)-D*(a-e))*(C*(d-f)-D*(c-e))>0)or'YES')