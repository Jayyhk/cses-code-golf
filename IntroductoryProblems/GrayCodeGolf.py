n = int(input())
i = 2**n
while i:
    i -= 1
    print(f"{i ^ i >> 1:0{n}b}")