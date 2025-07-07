import bisect

n = int(input())
w = list(map(int, input().split()))

def get_best_diff(w):
    total_weight = sum(w)
    half_weight = total_weight // 2
    k = n // 2
    L = w[:k]
    R = w[k:]

    left_sums = [sum(L[i] for i in range(k) if (m >> i) & 1) for m in range(1 << k)]
    right_sums = [sum(R[i] for i in range(n - k) if (m >> i) & 1) for m in range(1 << (n - k))]
    right_sums.sort()

    best_diff = total_weight
    for s in left_sums:
        target = half_weight - s
        i = bisect.bisect_left(right_sums, target)
        for j in (i, i - 1):
            if 0 <= j < len(right_sums):
                curr = abs(total_weight - 2 * (s + right_sums[j]))
                if curr < best_diff:
                    best_diff = curr
                    if best_diff == 0:
                        return 0
    return best_diff

print(get_best_diff(w))