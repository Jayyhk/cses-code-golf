from itertools import *
a = {*permutations(input())}
print(len(a), *sorted(map("".join, a)))