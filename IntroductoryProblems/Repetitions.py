s = input()

max = 1
cur = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        cur += 1
        if cur > max:
            max = cur
    else:
        cur = 1

print(max)
