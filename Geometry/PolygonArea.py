n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

area = 0
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    cp = x1 * y2 - x2 * y1
    area += cp

print(int(abs(area)))
