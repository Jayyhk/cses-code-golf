n, m = map(int, input().split())
polypoints = [list(map(int, input().split())) for _ in range(n)]
points = [list(map(int, input().split())) for _ in range(m)]

for point in range(m):
    x3, y3 = points[point]

    count = 0
    boundary = False

    for i in range(n):
        x1, y1 = polypoints[i]
        x2, y2 = polypoints[(i + 1) % n]

        if (
            (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1)
            and min(x1, x2) <= x3 <= max(x1, x2)
            and min(y1, y2) <= y3 <= max(y1, y2)
        ):
            boundary = True
            break

        if y1 <= y3 < y2 or y2 <= y3 < y1:
            x = x1 + (y3 - y1) * (x2 - x1) / (y2 - y1)
            if x3 < x:
                count += 1

    if boundary:
        print("BOUNDARY")
    elif count % 2 == 0:
        print("OUTSIDE")
    else:
        print("INSIDE")
