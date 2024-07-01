import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, v):
    global result

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in v:
            dfs(nx, ny, v+arr[nx][ny])

    if result < len(v):
        result = len(v)

r, c = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(r)]
result = 0
dfs(0, 0, arr[0][0])
print(result)