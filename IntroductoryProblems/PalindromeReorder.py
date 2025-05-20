s = input()
h = {}
for i in s:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1
odd = 0
for i in h:
    if h[i] % 2 == 1:
        odd += 1
if odd > 1:
    print("NO SOLUTION")
else:
    middle = ""
    if odd == 1:
        for i in h:
            if h[i] % 2 == 1:
                middle = i
                h[i] -= 1
                break
    half = ""
    for i in h:
        if h[i] % 2 == 0:
            half += i * (h[i] // 2)
    palindrome = half + middle + half[::-1]
    print(palindrome)
