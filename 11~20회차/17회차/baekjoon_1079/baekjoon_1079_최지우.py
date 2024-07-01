import sys
input = sys.stdin.readline

N = int(input())
gp = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
E = int(input())

turn = 0
dead = [0 for _ in range(N)]


def day(t, n):
    global turn
    target = gp.index(max(gp))

    if n == 1 or target == E:
        turn = max(turn, t)
        return

    dead[target] = 1
    gpbuff = gp[target]
    gp[target] = 0

    night(t, n-1)

    dead[target] = 0
    gp[target] = gpbuff


def night(t, n):
    global turn
    if n == 2:
        turn = max(turn, t+1)
        return

    for i in range(N):
        if dead[i] or i == E:
            continue

        dead[i] = 1
        gpbuff = gp[i]
        for j in range(N):
            if dead[j] or i == j:
                continue
            gp[j] += arr[i][j]
        gp[i] = 0

        day(t+1, n-1)

        dead[i] = 0
        for j in range(N):
            if dead[j] or i == j:
                continue
            gp[j] -= arr[i][j]
        gp[i] = gpbuff


if N%2:
    day(0, N)
else:
    night(0, N)

print(turn)
