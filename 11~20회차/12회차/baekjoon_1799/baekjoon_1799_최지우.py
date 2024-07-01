import sys
from copy import deepcopy
input = sys.stdin.readline


def Warr(arr):
    arr = deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if (i+j)%2 == 0:
                arr[i][j] = 0
    return arr


def Barr(arr):
    arr = deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if (i+j)%2 != 0:
                arr[i][j] = 0
    return arr


def bishop(x, y, cnt, color):
    global wcnt, bcnt
    x, y = x, y
    if y == N:
        y = 0
        x += 1
    if color:
        if x == N:
            if wcnt < cnt:
                wcnt = cnt
            return

        if (x+y)%2 == 1:
            if white[x][y] and not used[1][x+y] and not used[0][x-y]:
                used[1][x+y] = 1
                used[0][x-y] = 1
                bishop(x, y+1, cnt+1, color)
                used[1][x+y] = 0
                used[0][x-y] = 0

    else:
        if x == N:
            if bcnt < cnt:
                bcnt = cnt
            return

        if (x+y)%2 == 0:
            if black[x][y] and not used[1][x+y] and not used[0][x-y]:
                used[1][x+y] = 1
                used[0][x-y] = 1
                bishop(x, y, cnt+1, color)
                used[1][x+y] = 0
                used[0][x-y] = 0

    bishop(x, y+1, cnt, color)


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

white = Warr(arr)
black = Barr(arr)

used = [[0] * (N*3) for _ in range(2)]
wcnt = bcnt = 0

bishop(0, 0, 0, 1)
bishop(0, 0, 0, 0)

print(wcnt+bcnt)
