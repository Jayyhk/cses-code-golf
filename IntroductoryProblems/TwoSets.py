n = int(input())

sum = n * (n + 1) // 2

if sum % 2 == 1:
    print("NO")
else:
    half = sum // 2
    a = []
    b = []
    for i in range(n, 0, -1):
        if i <= half:
            a.append(i)
            half -= i
        else:
            b.append(i)

    print("YES")
    print(len(a))
    for i in a:
        print(i, end=" ")
    print(f"\n{len(b)}")
    for i in b:
        print(i, end=" ")
