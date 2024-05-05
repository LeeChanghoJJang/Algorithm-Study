import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

input = sys.stdin.readline
dr = [(0, -1), (-1, 0), (0, 1)]


def archer(narr, com):
    global result
    cnt = 0
    for i in range(N-1, -1, -1):
        catched = [[0] * M for _ in range(N)]
        used = [0 if x in com else 1 for x in range(M)]
        for j in range(M):
            if not used[j]:
                if narr[i][j]:
                    catched[i][j] = 1
                    continue

                que = deque([(i, j)])
                visited = [[0] * M for _ in range(N)]
                visited[i][j] = 1
                catch = False

                while que:
                    x, y = que.popleft()
                    d = visited[x][y]

                    if d == D:
                        continue

                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if narr[nx][ny]:
                                catched[nx][ny] = 1
                                catch = True
                                break

                            if not visited[nx][ny]:
                                visited[nx][ny] = d+1
                                que.append((nx, ny))

                    if catch:
                        break

                if catch:
                    continue

        for i in range(N):
            for j in range(M):
                if catched[i][j]:
                    cnt += 1
                    narr[i][j] = 0

    result = max(result, cnt)


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for com in combinations(range(M), 3):
    new_arr = deepcopy(arr)
    archer(new_arr, com)

print(result)