import sys
sys.stdin = open('input.txt')
def is_possible(x, y, n):
    for i in range(9):
        if arr[x][i] == n:
            return False
        if arr[i][y] == n:
            return False

    ny = (y // 3) * 3
    nx = (x // 3) * 3

    for dx in range(3):
        for dy in range(3):
            if arr[nx + dx][ny + dy] == n:
                return False
    return True

def dfs(idx):
    if idx == len(zero):
        for row in arr:
            print(*row, sep='')
        exit(0)

    x, y  = zero[idx]
    for i in range(1, 10):
        if is_possible(x, y, i):
            arr[x][y] = i
            dfs(idx + 1)
            arr[x][y] = 0

N = 9
arr = []
for _ in range(N):
    row = list(input())
    row = list(map(int, row))
    arr.append(row)

zero = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            zero.append((i, j))

dfs(0)