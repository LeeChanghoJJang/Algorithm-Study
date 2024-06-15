import sys

input = sys.stdin.readline

def go(x, y, s, d, cnt):
    dx = [-1 * s, 0]
    dy = [0, +1 * s]
    while a[x][y] != -1:
        if a[x][y] == 1:
            d = (d + 1) % 2
        x += dx[d]
        y += dy[d]
    res[cnt] = num[x][y]

# 입력 받기
n, m = map(int, input().split())

# 배열 초기화
a = [[-1] * (m + 2) for _ in range(n + 2)]
num = [[0] * (m + 2) for _ in range(n + 2)]
res = [0] * ((n + m) * 2 + 1)

# 배열 값 입력 받기
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, m + 1):
        a[i][j] = row[j - 1]

# num 배열 설정
for i in range(1, n + 1):
    num[i][0] = i
    num[n - i + 1][m + 1] = i + n + m

for i in range(1, m + 1):
    num[n + 1][i] = i + n
    num[0][m - i + 1] = i + n + m + n

# go 함수 호출
for i in range(1, n + 1):
    go(i, 1, 1, 1, num[i][0])
    go(i, m, -1, 1, num[i][m + 1])

for i in range(1, m + 1):
    go(n, i, 1, 0, num[n + 1][i])
    go(1, i, -1, 0, num[0][i])

# 결과 출력
for i in range(1, (n + m) * 2 + 1):
    print(res[i], end=' ')


