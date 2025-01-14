I=input
a=[[*map(int,I().split())]for _ in' '*int(I())]
print(abs(sum(X*y-Y*x for(X,Y),(x,y)in zip(a,a[1:]+a[:1]))))