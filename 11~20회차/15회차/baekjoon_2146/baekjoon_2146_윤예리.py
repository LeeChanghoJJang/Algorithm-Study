from pprint import pprint
import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def numbering(i, j):
    q = deque([(i, j)])
    arr[i][j] = number
    numbered[i][j] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not numbered[nx][ny]:
                arr[nx][ny] = number
                numbered[nx][ny] = 1
                q.append((nx, ny))

def bfs(i, j, num):
    global result
    q = deque([(i, j, num)])
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1

    while q:
        x, y, value = q.popleft()

        if visited[x][y] > result:
            return float('inf')

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1

                if arr[nx][ny] != 0 and arr[nx][ny] != value:
                    return visited[x][y]
                else:
                    q.append((nx, ny, value))

    return float('inf')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = float('inf')
number = 1
numbered = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and not numbered[i][j]:
            numbering(i, j)
            number += 1

# pprint(arr)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            for d in range(4):
                ni, nj = i+dx[d], j+dy[d]
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 0:
                    result = min(bfs(i, j, arr[ni][nj]), result)

print(result)