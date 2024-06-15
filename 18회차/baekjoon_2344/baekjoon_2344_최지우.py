import sys
input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]


def start(v, d):
    global out_p

    if d == 0:
        p = [(v, 0)]
    elif d == 1:
        p = [(N-1, v)]
    elif d == 2:
        p = [(v, M-1)]
    else:
        p = [(0, v)]

    while p:

        x, y = p.pop()
        if box[x][y]:
            d = change_dr[d]
        dx, dy = dr[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            p.append((nx, ny))
        else:
            out_p.append((nx, ny))
            return


dr = [(0, 1), (-1, 0), (0, -1), (1, 0)]
change_dr = {0: 1, 1: 0, 2: 3, 3: 2}
out_num = {}
out_p = []
idx = 1
for i in range(N):
    start(i, 0)
    out_num[(i, -1)] = idx
    idx += 1

for i in range(M):
    start(i, 1)
    out_num[(N, i)] = idx
    idx += 1

for i in range(N):
    start(N-i-1, 2)
    out_num[(N-i-1, M)] = idx
    idx += 1

for i in range(M):
    start(M-i-1, 3)
    out_num[(-1, M-i-1)] = idx
    idx += 1

for i in out_p:
    print(out_num[i], end=' ')
