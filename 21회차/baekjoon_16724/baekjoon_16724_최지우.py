import sys
input = sys.stdin.readline

dr = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def sol(x, y):
    global num
    num += 1
    start = (x, y)
    visited[x][y] = num
    while True:
        dx, dy = dr[arr[x][y]]
        nx, ny = x + dx, y + dy
        if (nx, ny) == start:
            return 1
        
        if not visited[nx][ny]:
            visited[nx][ny] = num
            x, y = nx, ny
            continue

        if visited[nx][ny] == num:
            return 1
        else: return 0
        
    

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

result = 0
num = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            result += sol(i, j)

print(result)