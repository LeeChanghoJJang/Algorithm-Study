import sys
sys.setrecursionlimit(10000)

T = int(input())
for tc in range(1, T+1):
    # m: 행의 수, n: 열의 수
    n, m, k = map(int, input().split())

    # 그래프 그리기
    arr = [[0] * n for _ in range(m)]
    for i in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1

    # 상하좌우
    def find(i, j):
        arr[i][j] = 0

        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0<=ni<m and 0<=nj<n and arr[ni][nj] == 1:
                find(ni, nj)

    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
                find(i, j)

    print(cnt)