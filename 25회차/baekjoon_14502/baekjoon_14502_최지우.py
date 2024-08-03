import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline


def bfs(arr, virus):
    que = deque(virus)
    dr = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    while que:
        x, y = que.popleft()
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                que.append((nx, ny))


def count_safe(arr):
    return sum(row.count(0) for row in arr)


N, M = map(int, input().split())

arr = []
virus = []
empty = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 2:
            virus.append((i, j))
        elif row[j] == 0:
            empty.append((i, j))
    arr.append(row)
    
max_safe = 0
for walls in combinations(empty, 3):
    new_arr = copy.deepcopy(arr)
    for i, j in walls:
        new_arr[i][j] = 1
    bfs(new_arr, virus)
    max_safe = max(max_safe, count_safe(new_arr))

print(max_safe)