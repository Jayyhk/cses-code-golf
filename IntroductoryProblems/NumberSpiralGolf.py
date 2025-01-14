I=input
for _ in' '*int(I()):
    x,y=map(int, I().split())
    v=max(x,y)
    print(v*v - v + 1 + (x-y)*(-1)**v)