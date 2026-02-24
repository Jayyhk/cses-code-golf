from math import*
i=map(int,open(0).read().split()[1:])
p=[*zip(i,i)]
s=b=0
for(x,y),(u,v)in zip(p,p[1:]+p[:1]):
 s+=x*v-y*u
 b+=gcd(x-u,y-v)
print((abs(s)-b)//2+1,b)