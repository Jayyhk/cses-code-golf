n = int(input())
numbers = list(map(int, input().split()))

total = (n * (n + 1)) // 2

sum = sum(numbers)

print(total - sum)