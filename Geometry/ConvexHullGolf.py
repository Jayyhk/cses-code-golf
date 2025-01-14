import sys
P=print
I=sys.stdin.buffer.readline
p=sorted(tuple(map(int, I().split())) for _ in' '*int(I()))
V=lambda a, b, c: (b[0]-a[0])*(c[1]-a[1])<(b[1]-a[1])*(c[0]-a[0])
H=[]
for q in p+p[-2::-1]:
    while len(H) > 1 and V(H[-2],H[-1],q):
        H.pop()
    H+=q,
H.pop()
P(len(H))
for a, b in H:
    P(a,b)