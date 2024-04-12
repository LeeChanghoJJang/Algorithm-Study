from collections import deque

def bfs():
    q = deque()
    result = 0

    for row, col in set_:
        q.append((0, row, col))

    while q:
        day, row, col = q.popleft()
        result = max(result, day)

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not(0 <= nrow < N and 0 <= ncol < M) or list_[nrow][ncol] != 0:
                continue

            list_[nrow][ncol] = 1
            q.append((day + 1, nrow, ncol))

    for row in range(N):
        for col in range(M):
            if list_[row][col] == 0:
                return -1
    return result

M, N = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(N)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
set_ = set()

for row in range(N):
    for col in range(M):
        if list_[row][col] == 1:
            set_.add((row, col))

print(bfs())