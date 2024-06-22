R, C = map(int, input().split())
store = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
dirs = [-1, 0, 1]
result = 0

def dfs(row, col):
    if col == C - 1:
        return True

    for dir in dirs:
        nrow, ncol = row + dir, col + 1

        if not (0 <= nrow < R) or visited[nrow][ncol]:
            continue

        if store[nrow][ncol] == '.':
            visited[nrow][ncol] = True

            if dfs(nrow, ncol):
                return True
    return False

for row in range(R):
    if store[row][0] == '.':
        visited[row][0] = True

        if dfs(row, 0):
            result += 1

print(result)