import sys


def cross_product(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0])


data = iter(map(int, sys.stdin.buffer.read().split()))
n = next(data)
p = [(next(data), next(data)) for _ in range(n)]

p.sort()

hull = []
s = 0

for t in range(2):
    for i in range(n):
        while len(hull) - s >= 2:
            p1 = hull[-2]
            p2 = hull[-1]
            if cross_product(p1, p2, p[i]) <= 0:
                break
            hull.pop()
        hull.append(p[i])
    hull.pop()
    s = len(hull)
    p.reverse()

sys.stdout.write(str(len(hull)) + "\n")
print("\n".join(" ".join(map(str, point)) for point in hull))
