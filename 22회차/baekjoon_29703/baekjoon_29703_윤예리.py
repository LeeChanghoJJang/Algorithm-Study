import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def goEat(i, j):
    global answer, posFish

    q = deque([(i, j)])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        if arr[x][y] == 'F':
            answer += (visited[x][y] - 1)
            posFish = [x, y]
            return

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] != 'D':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return -1

def goHome(i, j):
    global answer

    q = deque([(i, j)])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        if arr[x][y] == 'H':
            answer += (visited[x][y] - 1)
            return

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] != 'D':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return -1


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
answer = 0
posFish = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            tmp = goEat(i, j)

            if tmp == -1:
                exit(print(-1))
            else:
                tmp2 = goHome(posFish[0], posFish[1])
                print(answer if tmp2 != -1 else answer)

            break