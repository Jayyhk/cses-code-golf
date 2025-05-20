from sys import stdin

input = stdin.readline

n, x = map(int, input().split())
w = list(map(int, input().split()))

N = [float("inf")] * (1 << n)
W = [float("inf")] * (1 << n)

N[0] = 1
W[0] = 0

for mask in range(1, 1 << n):
    for i in range(n):
        if mask & (1 << i):
            prev_mask = mask ^ (1 << i)

            new_ride = 0
            valid_ride = 0

            if W[prev_mask] + w[i] > x:
                new_ride = 1
            else:
                valid_ride = 1

            N[mask] = min(N[mask], N[prev_mask] + new_ride)
            W[mask] = min(W[mask], W[prev_mask] * valid_ride + w[i])

print(N[(1 << n) - 1])
