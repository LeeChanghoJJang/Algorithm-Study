from collections import deque

def bfs(start, end):
    q = deque()
    q.append((0, start[0], start[1]))
    cost_list = [[float('inf')] * W for _ in range(H)]
    cost_list[start[0]][start[1]] = 0

    while q:
        fuel, row, col = q.popleft()

        if (row, col) == end:
            cost_list[end[0]][end[1]] = min(cost_list[end[0]][end[1]], fuel)
            continue

        for i in range(8):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < H and 0 <= ncol < W) or list_[nrow][ncol] == '#':
                continue

            if i in {0, 1, 2}:
                if fuel >= cost_list[nrow][ncol]:
                    continue
                cost_list[nrow][ncol] = fuel
                q.appendleft((fuel, nrow, ncol))
            else:
                if fuel + 1 >= cost_list[nrow][ncol]:
                    continue
                cost_list[nrow][ncol] = fuel + 1
                q.append((fuel + 1, nrow, ncol))
    return -1 if cost_list[end[0]][end[1]] == float('inf') else cost_list[end[0]][end[1]]

H, W = list(map(int, input().split()))
drow, dcol = [-1, 0, 1, 1, 1, 0, -1, -1], [1, 1, 1, 0, -1, -1, -1, 0]
list_ = [list(input()) for _ in range(H)]
start = end = 0

for row in range(H):
    for col in range(W):
        if list_[row][col] == 'K':
            start = (row, col)
            continue

        if list_[row][col] == '*':
            end = (row, col)
            continue

        if start and end:
            break
    if start and end:
        break

print(bfs(start, end))