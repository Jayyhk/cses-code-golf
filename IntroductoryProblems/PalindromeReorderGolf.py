l=""
d={l}
for c in input():
    l+=c*(c in d)
    d^={c}
print("NO SOLUTION"*(len(d)>2)or l+max(d)+l[::-1])