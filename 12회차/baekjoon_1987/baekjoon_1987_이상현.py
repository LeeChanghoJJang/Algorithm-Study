def dfs(row, col, memo, cnt):
    global max_

    max_ = max(max_, cnt)

    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]

        if not (0 <= nrow < R and 0 <= ncol < C) or list_[nrow][ncol] in memo:
            continue
        dfs(nrow, ncol, memo + list_[nrow][ncol], cnt + 1)

R, C = map(int, input().split())
list_ = [list(input()) for _ in range(R)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
max_ = 0
dfs(0, 0, list_[0][0], 1)
print(max_)