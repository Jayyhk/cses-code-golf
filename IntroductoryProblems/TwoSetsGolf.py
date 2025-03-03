n=int(input())
a=n-n//2
b=n//4+1
r=range
print(*["NO"]if n+1&2 else["YES",n-a,*r(1,b),*r(a+b,n+1),a,*r(b,a+b)])