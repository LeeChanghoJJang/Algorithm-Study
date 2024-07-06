# 12100 2048 (Easy)
from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
go = ((-1, 0), (1, 0), (0, -1), (0, 1))

def move(grid, dir):
    changed = []

    if dir == 0 or dir == 2:  # 상, 좌
        for i in range(N):
            for j in range(N):
                if grid[i][j]: BFS(grid, dir, i, j, changed)
    else:  # 하, 우
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                if grid[i][j]: BFS(grid, dir, i, j, changed)

    return grid

def BFS(grid, dir, i, j, changed):
    di, dj = go[dir]
    Q = deque([(i, j)])

    while Q:
        i, j = Q.popleft()
        ni, nj = i + di, j + dj

        if not (0 <= ni < N and 0 <= nj < N): continue

        # 다음칸 : 같은 숫자이며 합쳐진 블록이 아닐 때
        if grid[ni][nj] == grid[i][j] and (ni, nj) not in changed:
            grid[ni][nj] *= 2
            grid[i][j] = 0
            changed.append((ni, nj))

        # 다음칸 : 진행할 수 있는 칸일 때
        elif grid[ni][nj] == 0:
            grid[ni][nj] = grid[i][j]
            grid[i][j] = 0
            Q.append((ni, nj))

def DFS(grid, cnt):
    global ans
    # 가지치기
    if ans >= max(max(row) for row in grid)*(2**(5 - cnt)):
        return

    # 5번 이동 완료 시 최댓값 비교 후 종료
    if cnt == 5:
        for row in grid:
            ans = max(ans, max(row))
        return

    # 각 방향으로 DFS 가동
    for dir in range(4):
        DFS(move([row[:] for row in grid], dir), cnt+1)

ans = 0
DFS(grid, 0)
print(ans)
