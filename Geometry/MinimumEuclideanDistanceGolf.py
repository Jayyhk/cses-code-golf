import bisect as B
b = B.bisect_left
I = input
z = int
p = [[*map(z, I().split())] for _ in " " * z(I())]
p.sort(lambda x: x[0])
d = 9e18
s = []
r = 0
for x, y in p:
    D = z(d**.5)
    while x - p[r][0] > D:
        l, m = p[r]
        s.pop(b(s, (m, l)))
        r += 1
    for i in range(b(s, (y - D, -d)), len(s)):
        k, j = s[i]
        w = k - y
        if w * w > d:
            break
        d = min(d, w * w + (j - x) ** 2)
    B.insort(s, (y, x))
print(d)