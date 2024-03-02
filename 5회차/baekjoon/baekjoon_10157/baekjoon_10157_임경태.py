import sys
sys.stdin = open("input.txt")

dr = ((1, 0), (0, 1), (-1, 0), (0, -1))
C, R = map(int, input().split())
seat = [[0] * C for _ in range(R)]
K = int(input())
i, j, k = 0, 0, 0

if K <= C * R:
    for _ in range(1, K):
        seat[i][j] = 1
        ni, nj = i + dr[k][0], j + dr[k][1]
        if 0 <= ni < R and 0 <= nj < C and not seat[ni][nj]:
            i, j = ni, nj
        else:
            k = (k + 1) % 4
            i, j = i + dr[k][0], j + dr[k][1]
    print(j+1, i+1)
else:
    print(0)