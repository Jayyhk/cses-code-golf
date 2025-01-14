n = int(input())
arr = list(map(int, input().split()))
moves = 0

for i in range(0, n - 1):
    if arr[i] > arr[i + 1]:
        moves += arr[i] - arr[i + 1]
        arr[i + 1] = arr[i]
if arr[n - 1] < arr[n - 2]:
    moves += arr[n - 2] - arr[n - 1]
    arr[n - 1] = arr[n - 2]
print(moves)