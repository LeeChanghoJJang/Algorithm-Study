from collections import deque

def bfs(row, col):
    q = deque()
    q.append((row, col, 0, 0))
    visited[row][col][0] = True

    while q:
        row, col, num, cnt = q.popleft()

        if num == 6:
            return cnt

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < 5 and 0 <= ncol < 5) or list_[nrow][ncol] == -1 or visited[nrow][ncol][num]:
                continue

            visited[nrow][ncol][num] = True

            nnum = num
            if list_[nrow][ncol] == num + 1:
                nnum += 1
            q.append((nrow, ncol, nnum, cnt + 1))
    return -1

list_ = [list(map(int, input().split())) for _ in range(5)]
visited = [[[False] * 7 for _ in range(5)] for _ in range(5)]
drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]
print(bfs(*map(int, input().split())))