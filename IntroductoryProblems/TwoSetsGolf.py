n=int(input())
s=n*n+n
a=[0]
b=[0]
while n:
    c=b
    if s>=4*n:
        s-=4*n
        c=a
    c+=n,
    c[0]+=1
    n-=1
print(*("NO",) if s/2%2 else ("YES",*a+b))