import sys
input = sys.stdin.readline
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 방문 가능한 위치 count
def zero_cnt(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1

    while q:
        i, j = q.popleft()
        zeros[i][j] = group
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 그룹 번호
zeros = [[0] * m for _ in range(n)]

group_dict = {}
group_dict[0] = 0
group = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = 1
            cnt = zero_cnt(i, j)
            group_dict[group] = cnt
            group += 1

for i in range(n):
    for j in range(m):
        add_set = set()

        if arr[i][j] == 1:
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < n and 0 <= nj < m:
                    add_set.add(zeros[ni][nj])

            for add in add_set:
                arr[i][j] += group_dict[add]
                arr[i][j] %= 10

for i in arr:
    print(''.join(map(str, i)))




