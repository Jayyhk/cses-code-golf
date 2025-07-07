n = int(input())

res = []
for i in range(1 << n):
    res.append(f"{i ^ (i >> 1):0{n}b}")
for i in res:
    print(i)
