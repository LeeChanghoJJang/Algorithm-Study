import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
cleaner = []

# 1. 미세먼지가 확산된다.
cur = []
def diff():
    while cur:
        x, y, value = cur.pop()
        cnt = 0
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in cleaner:
                arr[ny][ny] += value // 5
                cnt += 1
        arr[x][y] -= (value//5) * cnt

# 2. 공기청정기가 작동한다.
def airClean(a, b):
    # 위
    x, y = a, 1
    d = 1
    tmp = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]
        if nx == r or ny == c or nx == -1 or ny == -1:
            d = (d-1) % 4
            continue
        if x == b or y == 0:
            break

        arr[x][y], tmp = tmp, arr[x][y]
        x, y = nx, ny

    # 아래
    x, y = b, 1
    d = 1
    tmp = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]
        if nx == r or ny == c or nx == -1 or ny == -1:
            d = (d + 1) % 4
            continue
        if x == b or y == 0:
            break

        arr[x][y], tmp = tmp, arr[x][y]
        x, y = nx, ny

for i, line in enumerate(arr):
    for j, value in enumerate(line):
        if value > 0:
            cur.append((i, j, value))
        if value == -1:
            cleaner.append((i, j))

a, b = cleaner[0], cleaner[1]
for time in range(t):
    diff()
    airClean(a, b)
    for i, line in enumerate(arr):
        for j, value in enumerate(line):
            if value > 0:
                cur.append((i, j, value))

print(sum(cur[i][2] for i in range(len(cur))))
