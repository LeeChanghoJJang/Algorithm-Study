import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(R)]

clear_list = []
drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

for row in range(R):
    for col in range(C):
        if list_[row][col] == -1:
            clear_list.append((row, col))

def diffusion():
    change = [[0] * C for _ in range(R)]

    for row in range(R):
        for col in range(C):
            if list_[row][col] < 1:
                continue

            cnt = 0

            for i in range(4):
                nrow, ncol = row + drow[i], col + dcol[i]

                if not (0 <= nrow < R and 0 <= ncol < C) or list_[nrow][ncol] == -1:
                    continue
                cnt += 1
                change[nrow][ncol] += list_[row][col] // 5
            list_[row][col] -= cnt * (list_[row][col] // 5)

    for row in range(R):
        for col in range(C):
            list_[row][col] += change[row][col]

def clear():
    ccw = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    row, col = clear_list[0]
    i = 0

    while True:
        nrow, ncol = row + ccw[i][0], col + ccw[i][1]

        if (nrow, ncol) == clear_list[0]:
            break

        if not (0 <= nrow <= clear_list[0][0] and 0 <= ncol < C):
            i += 1
            continue

        list_[row][col] = list_[nrow][ncol]
        row, col = nrow, ncol
    list_[clear_list[0][0]][1] = 0
    list_[clear_list[0][0]][clear_list[0][1]] = -1

    cw = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    row, col = clear_list[1]
    i = 0

    while True:
        nrow, ncol = row + cw[i][0], col + cw[i][1]

        if (nrow, ncol) == clear_list[1]:
            break

        if not (clear_list[1][0] <= nrow < R and 0 <= ncol < C):
            i += 1
            continue

        list_[row][col] = list_[nrow][ncol]
        row, col = nrow, ncol
    list_[clear_list[1][0]][1] = 0
    list_[clear_list[1][0]][clear_list[1][1]] = -1

for _ in range(T):
    diffusion()
    clear()

print(sum(sum(row) for row in list_) + 2)