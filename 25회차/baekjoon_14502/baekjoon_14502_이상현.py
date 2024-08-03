import sys
input = sys.stdin.readline

from collections import deque
import copy

def bfs():
    global max_
    
    list_copy = copy.deepcopy(list_)
    q = deque()

    for row in range(N):
        for col in range(M):
            if list_copy[row][col] == 2:
                q.append((row, col))

    while q:
        row, col = q.popleft()

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if (0 <= nrow < N and 0 <= ncol < M) and not list_copy[nrow][ncol]:
                list_copy[nrow][ncol] = 2
                q.append((nrow, ncol))

    safe = 0
    for row in range(N):
        for col in range(M):
            if not list_copy[row][col]:
                safe += 1
    max_ = max(max_, safe)

def create_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for row in range(N):
        for col in range(M):
            if not list_[row][col]:
                list_[row][col] = 1
                create_wall(cnt + 1)
                list_[row][col] = 0


N, M = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(N)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
max_ = 0
create_wall(0)
print(max_)