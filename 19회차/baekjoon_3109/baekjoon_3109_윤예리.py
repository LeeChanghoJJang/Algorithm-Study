import sys
input = sys.stdin.readline

def dfs(x, y):
    if y == c-1:
        return True

    for dx in [-1, 0, 1]:
        nx = x + dx
        ny = y + 1

        if 0 <= nx < r and 0 < ny < c:
            if arr[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True

    return False


r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
answer = 0
for i in range(r):
    if dfs(i, 0):
        answer += 1
print(answer)