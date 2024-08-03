import sys
input = sys.stdin.readline

from collections import deque

def bfs(row, col):
    q = deque()
    q.append((row, col))
    visited[row][col] = True
    area = 1

    while q:
        row, col = q.popleft()
        wall = 1

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if list_[row][col] & wall != wall:
                if (0 <= nrow < M and 0 <= ncol < N) and not visited[nrow][ncol]:
                    area += 1
                    visited[nrow][ncol] = True
                    q.append((nrow, ncol))
            wall *= 2
    return area

N, M = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(M)]
drow, dcol = [0, -1, 0, 1], [-1, 0, 1, 0]
visited = [[False] * N for _ in range(M)]
room_cnt = max_area1 = max_area2 = 0

for row in range(M):
    for col in range(N):
        if not visited[row][col]:
            room_cnt += 1
            max_area1 = max(max_area1, bfs(row, col))

for row in range(M):
    for col in range(N):
        wall = 1

        while wall < 16:
            if list_[row][col] & wall:
                visited = [[False] * N for _ in range(M)]
                list_[row][col] -= wall
                max_area2 = max(max_area2, bfs(row, col))
                list_[row][col] += wall
            wall *= 2

print(room_cnt)
print(max_area1)
print(max_area2)