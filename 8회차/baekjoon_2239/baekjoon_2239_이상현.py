def chk(row, col, num):
    for r in range(3 * (row // 3), 3 * (row // 3) + 3):
        for c in range(3 * (col // 3), 3 * (col // 3) + 3):
            if list_[r][c] == num:
                return False

    for i in range(9):
        if list_[row][i] == num or list_[i][col] == num:
            return False
    return True

def dfs(cnt, zeros):
    if cnt == zeros:
        [print(*row, sep = '') for row in list_]
        exit()

    for num in range(1, 10):
        if chk(zero_list[cnt][0], zero_list[cnt][1], num):
            list_[zero_list[cnt][0]][zero_list[cnt][1]] = num
            dfs(cnt + 1, zeros)
            list_[zero_list[cnt][0]][zero_list[cnt][1]] = 0

list_ = [list(map(int, list(input()))) for _ in range(9)]
zero_list = []

for row in range(9):
    for col in range(9):
        if not list_[row][col]:
            zero_list.append((row, col))

dfs(0, len(zero_list))