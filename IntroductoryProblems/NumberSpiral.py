t = int(input())
tests = [map(int, input().split()) for _ in range(t)]

for y, x in tests:
    n = max(x, y)
    value = 0
    if n == y and n % 2 == 0:
        value = n ** 2 - (x - 1)
    elif n == y and n % 2 != 0:
        value = (n - 1) ** 2 + 1 + (x - 1)
    elif n == x and n % 2 == 0:
        value = (n - 1) ** 2 + 1 + (y - 1)
    elif n == x and n % 2 != 0:
        value = n ** 2 - (y - 1)

    print(value)