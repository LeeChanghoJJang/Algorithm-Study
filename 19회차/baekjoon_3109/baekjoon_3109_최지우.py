import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def pipe(x, y):
    if y == c-1:
        return True

    for dx, dy in dr:
        nx, ny = x+dx, y+dy
        if 0 <= nx < r and 0 <= ny < c:
            if arr[nx][ny] == '.':
                arr[nx][ny] = 'x'
                if pipe(nx, ny):
                    return True
    return False


r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

dr = [(-1, 1), (0, 1), (1, 1)]

cnt = 0

for sx in range(r):
    arr[sx][0] = 'x'
    if pipe(sx, 0):
        cnt += 1

print(cnt)