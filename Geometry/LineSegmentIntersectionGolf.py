T=lambda a,b,c,d,e,f:(a*d-b*c)*(a*f-b*e)>0
M=max
N=min
I=input
for _ in' '*int(I()):
    a,b,c,d,e,f,g,h=map(int,I().split())
    print('NO' if M(a,c)<N(e,g) or M(e,g)<N(a,c) or M(b,d)<N(f,h) or M(f,h)<N(b,d) or T(c-a,d-b,e-a,f-b,g-a,h-b) | T(g-e,h-f,a-e,b-f,c-e,d-f) else 'YES')