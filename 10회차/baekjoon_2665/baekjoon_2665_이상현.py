from collections import deque

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while q:
        row, col, cnt = q.popleft()

        if (row, col) == (n - 1, n - 1):
            return cnt

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < n and 0 <= ncol < n) or visited[nrow][ncol]:
                continue

            visited[nrow][ncol] = True

            if list_[nrow][ncol]:
                q.appendleft((nrow, ncol, cnt))
            else:
                q.append((nrow, ncol, cnt + 1))

n = int(input())
list_ = [list(map(int, list(input()))) for _ in range(n)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
print(bfs())