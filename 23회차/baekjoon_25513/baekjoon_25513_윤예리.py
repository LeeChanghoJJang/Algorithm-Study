import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def bfs():
    q = deque([(r, c, 0, 0)])
    visited[r][c][0] = 1

    while q:
        cr, cc, idx, cnt = q.popleft()

        if idx == 6:
            return cnt

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < 5 and 0 <= nc < 5 and arr[nr][nc] != -1 and visited[nr][nc][idx] == 0:
                visited[nr][nc][idx] = 1

                if arr[nr][nc] == idx+1:
                    q.append((nr, nc, idx+1, cnt+1))
                else:
                    q.append((nr, nc, idx, cnt+1))

    return -1

arr = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
visited = [[[0] * 7 for _ in range(5)] for _ in range(5)]

print(bfs())
# print(visited)