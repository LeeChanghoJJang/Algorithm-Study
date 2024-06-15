import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations

n = int(input())
scv = list(map(int, input().split()))
scv += [0] * (3-n)

visited = [[[-1] * 61 for _ in range(61)] for _ in range(61)]
visited[scv[0]][scv[1]][scv[2]] = 0

q = deque()
q.append([scv[0], scv[1], scv[2]])

while q:
    x, y, z = q.popleft()

    # 모든 scv의 체력이 0이면 끝
    if x == 0 and y == 0 and z == 0:
        print(visited[x][y][z])
        break

    # 순열별로 확인
    for i in permutations([9, 3, 1], 3):
        # 공격
        # 체력은 0 보다 작아질 수 없음
        nx, ny, nz = max(x-i[0], 0), max(y-i[1], 0), max(z-i[2], 0)

        # 안 가본 visited라면 이전 횟수 + 1
        if visited[nx][ny][nz] == -1:
            visited[nx][ny][nz] = visited[x][y][z] + 1
            q.append([nx, ny, nz])