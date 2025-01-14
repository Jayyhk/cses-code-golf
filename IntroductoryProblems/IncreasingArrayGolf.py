_,b=open(0)
p=m=0
for i in b.split():
    i=int(i)
    if p<i:p=i
    m+=p-i
print(m)