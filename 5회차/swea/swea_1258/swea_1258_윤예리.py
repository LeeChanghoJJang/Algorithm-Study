import sys
sys.stdin = open('input.txt')

from collections import deque

di = [1, 0]
dj = [0, 1]

def find(x, y):
    origin_x, origin_y = x, y
    q = deque([(x, y)])
    while q:
        i, j = q.popleft()

        # 남, 동
        for d in range(2):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 0:
                arr[ni][nj] = 0
                q.append((ni, nj))

    return ((i + 1 - origin_x) * (j + 1 - origin_y), (i + 1 - origin_x), (j + 1 - origin_y))

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                result.append(find(i, j))

    result.sort()
    print(len(result), end=' ')

    for k in result:
        print(*k[1:], end=' ')
    print()
