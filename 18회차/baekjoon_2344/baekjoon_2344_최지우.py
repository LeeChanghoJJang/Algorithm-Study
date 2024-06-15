import sys
input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]


def start(v, d):
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
            if nx == -1:
                return 2*N + 2*M - ny
            elif ny == -1:
                return nx+1
            elif nx == N:
                return N + ny + 1
            else:
                return 2*N + M - nx


dr = [(0, 1), (-1, 0), (0, -1), (1, 0)]
change_dr = [1, 0, 3, 2]
result = []
for i in range(N):
    result.append(start(i, 0))

for i in range(M):
    result.append(start(i, 1))

for i in range(N):
    result.append(start(N-i-1, 2))

for i in range(M):
    result.append(start(M-i-1, 3))

print(*result)