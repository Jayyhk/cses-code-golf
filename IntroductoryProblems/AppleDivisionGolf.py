_, b = open(0)
*P, = map(int, b.split())
W = [sum(P)]
for p in P:
    W += [w - p * 2 for w in W if w >= p * 2]
print(min(W))