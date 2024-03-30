import sys
sys.stdin = open("input.txt")

def row_check(i, num):
    # 가로
    for j in range(9):
        if arr[i][j] == num:
            return False
    return True

def col_check(j, num):
    # 세로
    for i in range(9):
        if arr[i][j] == num:
            return False
    return True

def square_check(i, j, num):
    # 3x3

    # 0, 3, 6
    r = i // 3 * 3
    c = j // 3 * 3

    for a in range(3):
        for b in range(3):
            if arr[r+a][c+b] == num:
                return False
    return True

def dfs(sudoku):
    if sudoku == len(zeros):
        # for m in range(9):
        #     for n in range(9):
        print(arr)
        anwser.append(arr)
        return

    x, y = zeros[sudoku]
    for n in range(1, 10):
        if row_check(x, n) and col_check(y, n) and square_check(x, y, n):
            arr[x][y] = n
            dfs(sudoku+1)
            arr[x][y] = 0

arr = [list(map(int, input())) for _ in range(9)]
# print(arr)
zeros = []
# 0인 위치 다 넣어놓고 걔네만 넣어보면서 dfs
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            zeros.append((i, j))

anwser = []
dfs(0)
print(anwser)
for i in range(9):
    print(*sorted(anwser)[0][i], sep='')
