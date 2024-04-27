import sys
sys.stdin = open('input.txt')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def pop_(i, j):
    global max_value
    total = arr[i][j]
    for d in range(4):

        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < n and 0 <= nj < m:
            total += arr[ni][nj]

    if total > max_value:
        max_value = total

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_value = 0

    for i in range(n):
        for j in range(m):
            pop_(i, j)
    print(max_value)