b=x=r=0
for c in input():
    r=(b==c)*r+1
    b=c
    if r>x:x=r
print(x)