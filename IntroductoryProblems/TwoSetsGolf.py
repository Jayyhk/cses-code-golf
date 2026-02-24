n=int(input())
a=n-n//2
b=n//4+1
r=range
print(*n+1&2 and["NO"]or["YES",n-a,*r(1,b),*r(a+b,n+1),a,*r(b,a+b)])