import sys
from bisect import insort, bisect_left

data = iter(map(int, sys.stdin.buffer.read().split()))

n = next(data)
points = [(next(data), next(data)) for _ in range(n)]

points.sort(lambda x: x[0])
d_squared = 8 * 10**18
d = int(d_squared**0.5)

s = []
removed = 0

for px, py in points:
    while removed < n:
        qx, qy = points[removed]
        if (px - qx) ** 2 > d_squared:
            idx = bisect_left(s, (qy, qx))
            if idx < len(s) and s[idx] == (qy, qx):
                s.pop(idx)
            removed += 1
        else:
            break

    for i in range(bisect_left(s, (py - d, -8 * 10**18)), len(s)):
        sy, sx = s[i]
        if (sy - py) ** 2 > d_squared:
            break
        distance = (sx - px) ** 2 + (sy - py) ** 2
        if distance < d_squared:
            d_squared = distance
            d = int(d_squared**0.5)

    insort(s, (py, px))

sys.stdout.write(str(d_squared))
