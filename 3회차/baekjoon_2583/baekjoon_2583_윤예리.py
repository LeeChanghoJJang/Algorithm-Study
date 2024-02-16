# 재귀 깊이 정해주는 코드
from sys import*
setrecursionlimit(10**6)
from pprint import pprint

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

# graph
for _ in range(k):
    a1, b1, a2, b2 = map(int, input().split())
    for i in range(m-b2, m-b1):
        for j in range(a1, a2):
            arr[i][j] = 1
# pprint(arr)

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# dfs
def dfs(x, y):
    global area
    arr[x][y] = 1
    area += 1

    for i in range(4):
        if 0 <= x+di[i] < m and 0 <= y+dj[i] < n:
            if arr[x+di[i]][y+dj[i]] == 0:
                dfs(x+di[i], y+dj[i])
            else:
                continue

result = []
num = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            area = 0
            dfs(i, j)
            num += 1
            result.append(area)

print(num)
print(*sorted(result))