from collections import deque
 
def bfs(row, col):
    result = []
    q = deque()
    q.append((row, col))
    visited[row][col] = True
 
    while q:
        row, col = q.popleft()
        result.append((row, col))
 
        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]
 
            if not (0 <= nrow < N and 0 <= ncol < N) or visited[nrow][ncol] or not list_[nrow][ncol]:
                continue
 
            visited[nrow][ncol] = True
            q.append((nrow, ncol))
 
    if len(result) >= 2:
        return max(result)[0] - min(result)[0] + 1, max(result)[1] - min(result)[1] + 1
    return
 
T = int(input())
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
 
for tc in range(T):
    N = int(input())
    list_ = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = []
 
    for row in range(N):
        for col in range(N):
            if list_[row][col] and not visited[row][col]:
                result.append(bfs(row, col))
 
    result.sort(key = lambda x : (x[0] * x[1], x[0]))
    print(f'#{tc + 1} {len(result)}', end = ' ')
    [print(*pair, end = ' ') for pair in result]
    print()