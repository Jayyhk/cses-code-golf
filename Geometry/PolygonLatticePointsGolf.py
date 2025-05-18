import math
A=abs
t=map(int,open(0).read().split()[1:])
*a,=zip(t,t)
s=B=0 
for(i,j),(x,y)in zip(a,a[1:]+a[:1]):
    s+=i*y-j*x
    B+=math.gcd(A(x-i),A(y-j))
print(A(s)//2+1-B//2,B)