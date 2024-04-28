import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append((0, 0))
    visited[0][0] = -1

    while q:
        x, y = q.popleft()
        # print(x, y)
        if arr[x][y] == 1:  # 치즈는 패스하고
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:   # 방문 했던 곳 패스하고
                    continue

                if arr[nx][ny] == 1:  # 치즈라면 visited += 1
                    visited[nx][ny] += 1
                else:
                    visited[nx][ny] = -1
            else:
                continue

            q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:  # 2변 이상이 공기와 접촉이면 녹는다.
                arr[i][j] = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

while True:
    flag = True

    # 1이 하나도 없으면 break
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                flag = False
                break

    if flag:
        break

    check()
    answer += 1

print(answer)