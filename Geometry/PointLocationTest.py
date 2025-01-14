t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for i in range(t):
    x1, y1, x2, y2, x3, y3 = cases[i]

    # p1p2 x p1p3
    cp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    if cp == 0:
        print("TOUCH")
    elif cp > 0:
        print("LEFT")
    else:
        print("RIGHT")