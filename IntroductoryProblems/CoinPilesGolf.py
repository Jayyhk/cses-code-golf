I=input
for _ in' '*int(I()):
    a,b=map(int,I().split())
    print("YNEOS"[a>2*b or b>2*a or (a+b)%3>0::2])