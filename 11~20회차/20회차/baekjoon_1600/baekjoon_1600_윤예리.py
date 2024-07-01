import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

monkey = [[1, 0], [0, 1], [-1, 0], [0, -1]]
horse = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [2, -1], [2, 1], [1, -2], [1, 2]]

def bfs():
    visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]-1

        for (i, j) in monkey:
            nx, ny = x+i, y+j
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][z] and not arr[nx][ny]:
                visited[nx][ny][z] = visited[x][y][z]+1
                q.append([nx, ny, z])

        if z < k:
            for (i, j) in horse:
                nx, ny = x + i, y + j
                if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny] and not visited[nx][ny][z+1]:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    q.append([nx, ny, z+1])

    return -1

print(bfs())