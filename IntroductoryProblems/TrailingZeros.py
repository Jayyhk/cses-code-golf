n = int(input())
count = 0
while n > 0:
    count += n // 5
    n //= 5
print(count)
