from collections import deque

def bfs(row, col, cur):
    global min_

    q = deque()
    q.append((row, col, 0))
    dist_list = [[float('inf')] * N for _ in range(N)]
    dist_list[row][col] = 0

    while q:
        row, col, dist_ = q.popleft()

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < N and 0 <= ncol < N):
                continue

            if list_[nrow][ncol] == cur and dist_list[nrow][ncol] != 0:
                dist_list[nrow][ncol] = 0
                q.append((nrow, ncol, 0))
            elif list_[nrow][ncol] == 0 and dist_ + 1 < dist_list[nrow][ncol]:
                dist_list[nrow][ncol] = dist_ + 1
                q.append((nrow, ncol, dist_ + 1))
            elif list_[nrow][ncol] and list_[nrow][ncol] != cur:
                min_ = min(min_, dist_)

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
min_ = float('inf')
cnt = 1

for row in range(N):
    for col in range(N):
        if not list_[row][col] == 1:
            continue

        cnt += 1
        q = deque()
        q.append((row, col))
        list_[row][col] = cnt

        while q:
            row, col = q.popleft()

            for i in range(4):
                nrow, ncol = row + drow[i], col + dcol[i]

                if not (0 <= nrow < N and 0 <= ncol < N) or list_[nrow][ncol] != 1:
                    continue
                list_[nrow][ncol] = cnt
                q.append((nrow, ncol))

visited_set = set()
for row in range(N):
    for col in range(N):
        if list_[row][col] and list_[row][col] not in visited_set:
            visited_set.add(list_[row][col])
            bfs(row, col, list_[row][col])

print(min_)