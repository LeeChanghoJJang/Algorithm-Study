C, R = map(int, input().split())
list_ = [[0] * C for _ in range(R)]

target = int(input())
drow, dcol = [-1, 0, 1, 0], [0, 1, 0, -1]
d = result = col = 0
row = R - 1

for i in range(1, C * R + 1):
    list_[row][col] = i

    if i == target:
        result = (col + 1, R - row)
        break

    nrow, ncol = row + drow[d], col + dcol[d]

    if not (0 <= nrow < R and 0 <= ncol < C) or list_[nrow][ncol]:
        d += 1
        d %= 4
        nrow, ncol = row + drow[d], col + dcol[d]

    row, col = nrow, ncol

print(*result) if result != 0 else print(0)