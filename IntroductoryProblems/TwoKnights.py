n = int(input())

for k in range(1, n + 1):
    total = (k**2) * (k**2 - 1) // 2
    attack = 2 * (k - 1) * (k - 2) + 2 * (k - 2) * (k - 1)
    print(total - attack)
