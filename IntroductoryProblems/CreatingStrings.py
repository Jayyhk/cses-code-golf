s = input()
chars = sorted(s)
perms = [''.join(chars)]

def get_perm(a):
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i+1]:
        i -= 1
    if i < 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i]:
        j -= 1

    a[i], a[j] = a[j], a[i]
    a[i+1:] = reversed(a[i+1:])
    return True

while get_perm(chars):
    perms.append(''.join(chars))

print(len(perms))
print('\n'.join(perms))
