import sys
from collections import deque

# input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 0
    q = deque([x, y])
    arr[x][y] = 0

    while q:
        i, j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
                cnt += 1
                q.append([ni, nj])
                arr[ni][nj] = 0
    result.append(cnt)

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))
# print(arr)
result = []
num = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            # print(i, j)
            bfs(i, j)
            num += 1
print(num)
print(sorted(result))