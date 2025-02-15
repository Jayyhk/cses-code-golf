n=int(input())
A=*B,=[0]
d=n*n+n
while n:
    C=B
    if d>=4*n:
        d-=4*n
        C=A
    C+=n,
    C[0]+=1
    n-=1
print("NO "*d,"YES",*A+B)