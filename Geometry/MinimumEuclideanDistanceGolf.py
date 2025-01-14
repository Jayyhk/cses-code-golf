from bisect import insort as t, bisect_left as b
I = input
R = range
z = int
n = z(I())
p = [list(map(z, I().split())) for _ in R(n)]
p.sort(lambda x: x[0])
d = 9**20
s = []
r = 0
for x, y in p:
    while (x - p[r][0]) ** 2 > d:
        l, m = p[r]
        s.pop(b(s, (m, l)))
        r += 1
    for i in R(b(s, (y - z(d ** .5), -d)), len(s)):
        k, j = s[i]
        w = (k - y) ** 2
        if w > d:
            break
        d = min(d, w + (j - x) ** 2)
    t(s, (y, x))
print(d)