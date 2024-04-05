from collections import deque

def bfs(row, col):
    q = deque()
    q.append((0, row, col))
    visited = [[False] * M for _ in range(N)]
    visited[row][col] = True

    while q:
        dist_, row, col = q.popleft()

        if list_[row][col]:
            return dist_

        for i in range(8):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < N and 0 <= ncol < M) or visited[nrow][ncol]:
                continue
            visited[nrow][ncol] = True
            q.append((dist_ + 1, nrow, ncol))

N, M = list(map(int, input().split()))
list_ = [list(map(int, input().split())) for _ in range(N)]
shark_set = set((row, col) for row in range(N) for col in range(M) if list_[row][col])
drow, dcol = [1, 1, 1, 0, -1, -1, -1, 0], [1, 0, -1, -1, -1, 0, 1, 1]
max_ = 0

for row in range(N):
    for col in range(M):
        if list_[row][col]:
            continue
        max_ = max(max_, bfs(row, col))

print(max_)