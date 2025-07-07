p = print
d = int(input())
p(2**d - 1)
def f(n, a=1, b=3):
    if n:
        f(n - 1, a, a ^ b)
        p(a, b)
        f(n - 1, a ^ b, b)
f(d)