i=n=int(input())
P=print
if 1<n<4:
    P("NO SOLUTION")
    i=0
while i:
    P(i-i%2*~n>>1)
    i-=1