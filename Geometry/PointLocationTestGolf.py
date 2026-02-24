_,*l=open(0)
for s in l:
    a,b,c,d,e,f=map(int,s.split())
    v=(f-b)*(c-a)-(e-a)*(d-b)
    print(v and("RIGHT","LEFT")[v>0]or"TOUCH")