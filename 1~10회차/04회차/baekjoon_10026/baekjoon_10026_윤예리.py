import sys
sys.setrecursionlimit(10000)
import copy
n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
arr_1 = copy.deepcopy(arr)  # 색약 아닌 사람
arr_2 = copy.deepcopy(arr)  # 색약

# 색맹용은 R을 G로 다 바꿔놓기
for i in range(n):
    for j in range(n):
        if arr_2[i][j] == 'R':
            arr_2[i][j] = 'G'

# 구역 세기
def normal(arr, i, j):
    a = arr[i][j]
    if a == '_':
        return
    arr[i][j] = '_'
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0<=ni<n and 0<=nj<n and arr[ni][nj] == a:
            normal(arr, ni, nj)

result = []

# 색약 아닌 사람이 보는 구역 카운트
cnt = 0
for i in range(n):
    for j in range(n):
        if arr_1[i][j] != '_':
            cnt += 1
            normal(arr_1, i, j)
result.append(cnt)

# 색약이 보는 구역 카운트
cnt = 0
for i in range(n):
    for j in range(n):
        if arr_2[i][j] != '_':
            cnt += 1
            normal(arr_2, i, j)
result.append(cnt)

print(*result)