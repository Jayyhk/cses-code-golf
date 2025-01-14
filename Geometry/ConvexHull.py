import math
import sys
 
def cross_product(p, q, r):
    # > 0 if r lies on the right side of vector pq
    # = 0 if p-q-r are collinear
    # < 0 if r lies on the left side of vector pq
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
 
 
def polar_angle(p0, p1):
    return math.atan2(p1[1] - p0[1], p1[0] - p0[0])
 
 
def distance(p0, p1):
    return (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2
 

data = iter(map(int, sys.stdin.buffer.read().split()))
 
n = next(data)
points = [(next(data), next(data)) for _ in range(n)]
 
p0 = min(points, key=lambda p: p[1])
points.remove(p0)
 
points.sort(key=lambda p: (polar_angle(p0, p), -distance(p0, p)))
 
if cross_product(p0, points[0], points[1]) == 0:
    temp = points[0]
    points[0] = points[1]
    points[1] = temp
 
convex_hull = [p0, points[0], points[1]]
 
for i in range(2, n - 1):
    while cross_product(convex_hull[-2], convex_hull[-1], points[i]) > 0:
        convex_hull.pop()
    convex_hull.append(points[i])
 
sys.stdout.write(str(len(convex_hull)) + '\n')
print('\n'.join(' '.join(map(str, point)) for point in convex_hull))