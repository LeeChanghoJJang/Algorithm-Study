import sys
from collections import deque

input = sys.stdin.readline

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

num = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            que = deque([(i, j)])
            arr[i][j] = num
            while que:
                x, y = que.pop()
                for dx, dy in dr:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 1:
                            arr[nx][ny] = num
                            que.append((nx, ny))
            num += 1

result = 1e9
for k in range(2, num):
    dist = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == k and dist[i][j] == -1:
                que = deque([(i, j)])
                dist[i][j] = 0
                while que:
                    x, y = que.popleft()
                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if not arr[nx][ny]:
                                if dist[nx][ny] == -1:
                                    dist[nx][ny] = dist[x][y] + 1
                                    que.append((nx, ny))
                                else:
                                    if dist[nx][ny] > dist[x][y] + 1:
                                        dist[nx][ny] = dist[x][y] + 1
                                        que.append((nx, ny))
                            if arr[nx][ny] and arr[nx][ny] != k:
                                result = min(result, dist[x][y])
                                break

print(result)
