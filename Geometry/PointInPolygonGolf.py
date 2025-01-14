I=lambda:map(int,input().split())
n,m=I()
o=[[*I()]for _ in' '*(n+m)]
for f,t in o[n:]:
    b=c=0
    d,r=o[n-1]
    for e,s in o[:n]:
        A=e-d
        B=t-r
        C=s-r
        D=f-d
        b|=A*A>=D*A>=0<=B*C<=C*C and A*B==C*D
        c^=(r>t)^(s>t)and D<B*A/C
        d=e
        r=s
    print(["OUTSIDE","BOUNDARY","INSIDE"][b or -c])