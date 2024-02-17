# 재귀 깊이 정해주는 코드
# 이거 안 붙이니까 RuntimeError
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
    arr[x][y] = 1   # 방문했다면 1로 표시
    area += 1   # 0 이면 area + 1

    for i in range(4):
        if 0 <= x+di[i] < m and 0 <= y+dj[i] < n:
            if arr[x+di[i]][y+dj[i]] == 0:
                dfs(x+di[i], y+dj[i])   # 재귀로 넓이 계산
            else:
                continue

result = [] # 영역 넓이 리스트
num = 0     # 영역 개수
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            area = 0    # 영역 0으로 초기화
            dfs(i, j)   # 영역 넓이 계산
            num += 1    # 개수 + 1
            result.append(area) # 나온 넓이를 list에 저장

print(num)
print(*sorted(result))