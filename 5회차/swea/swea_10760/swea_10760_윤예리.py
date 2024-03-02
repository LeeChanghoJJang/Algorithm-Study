import sys
sys.stdin = open('input.txt')

di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

def find(i, j):
    global result
    height = arr[i][j]

    cnt = 0
    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] < height:
            cnt += 1

    if cnt >= 4:
        result += 1

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(m):
            find(i, j)

    print(result)