n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if (a + b) % 3 == 0 and 2 * a >= b and 2 * b >= a:
        print("YES\n")
    else:
        print("NO\n")
