t = int(input())

cases = []
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    cases.append((x1, y1, x2, y2, x3, y3, x4, y4))

for case in cases:
    x1, y1, x2, y2, x3, y3, x4, y4 = case

    if (
        max(x1, x2) < min(x3, x4)
        or max(x3, x4) < min(x1, x2)
        or max(y1, y2) < min(y3, y4)
        or max(y3, y4) < min(y1, y2)
    ):
        print("NO")
        continue

    def cross_product(x1, y1, x2, y2, x3, y3):
        return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    cp1 = cross_product(x1, y1, x2, y2, x3, y3)
    cp2 = cross_product(x1, y1, x2, y2, x4, y4)
    cp3 = cross_product(x3, y3, x4, y4, x1, y1)
    cp4 = cross_product(x3, y3, x4, y4, x2, y2)

    if cp1 * cp2 <= 0 and cp3 * cp4 <= 0:
        print("YES")
    else:
        print("NO")