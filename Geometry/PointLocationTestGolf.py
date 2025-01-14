I=input
for _ in' '*int(I()):
    a,b,c,d,e,f=map(int,I().split())
    o=(d-b)*(e-c)-(f-d)*(c-a)
    print(["TOUCH",["RIGHT","LEFT"][o<0]][o!=0])