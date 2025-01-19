I = lambda: map(int,input().split())
R = range
n, x = I()
s = 2 ** n
*w, = I()
b = [(1, 0)] * s
for i in R(1, s):
    b[i] = s, 0
    for j in R(n):
        if i & 2 ** j:
            p, q = b[i ^ 2 ** j]
            q += w[j]
            if q > x:
                p += 1
                q = w[j]
            b[i] = min(b[i], (p, q))
print(b[-1][0])