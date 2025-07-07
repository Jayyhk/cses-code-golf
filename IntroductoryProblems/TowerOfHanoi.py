n = int(input())

moves = []

def hanoi(n, src, tgt, aux):
    if n == 1:
        moves.append((src, tgt))
    else:
        hanoi(n - 1, src, aux, tgt)
        moves.append((src, tgt))
        hanoi(n - 1, aux, tgt, src)

hanoi(n, 1, 3, 2)
print(len(moves))
for move in moves:
    print(move[0], move[1])
