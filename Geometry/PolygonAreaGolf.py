n,*P=map(int,open(0).read().split())
r=0
n*=2
while n:
    n-=2
    r+=P[n-1]*(P[n]-P[n-4])
print(abs(r))