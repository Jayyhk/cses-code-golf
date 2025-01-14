import math

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

boundary_lattice = 0
area = 0

for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    cp = x1 * y2 - x2 * y1
    area += cp

area = abs(area)

for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    boundary_lattice += math.gcd(abs(x2 - x1), abs(y2 - y1))

inside_lattice = (area - boundary_lattice + 2) // 2

print(int(inside_lattice), int(boundary_lattice))