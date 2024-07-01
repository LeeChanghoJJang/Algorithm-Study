import sys
input = sys.stdin.readline

from collections import deque

mdrow = (0, 1, 0, -1)
mdcol = (1, 0, -1, 0)
hdrow = (-2, -1, 1, 2, 2, 1, -1, -2)
hdcol = (1, 2, 2, 1, -1, -2, -2, -1)

def bfs():
    global K

    q = deque()
    q.append((0, 0, K))
    cnt = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

    while q:
        row, col, K = q.popleft()

        if row == H - 1 and col == W - 1:
            return cnt[row][col][K]

        if K:
            for k in range(8):
                nrow = row + hdrow[k]
                ncol = col + hdcol[k]

                if 0 <= nrow < H and 0 <= ncol < W:
                    if list_[nrow][ncol] != 1 and cnt[nrow][ncol][K - 1] == 0:
                        cnt[nrow][ncol][K - 1] = cnt[row][col][K] + 1
                        q.append((nrow, ncol, K - 1))

        for k in range(4):
            nrow = row + mdrow[k]
            ncol = col + mdcol[k]

            if 0 <= nrow < H and 0 <= ncol < W:
                if list_[nrow][ncol] != 1 and cnt[nrow][ncol][K] == 0:
                    cnt[nrow][ncol][K] = cnt[row][col][K] + 1
                    q.append((nrow, ncol, K))
    return -1

K = int(input())
W, H = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(H)]

print(bfs())