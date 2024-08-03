import sys
input = sys.stdin.readline
from collections import deque

dr = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def bfs(x, y, arr, visited, room_id):
    que = deque([(x, y)])
    visited[x][y] = room_id
    room_size = 0
    
    while que:
        x, y = que.popleft()
        room_size += 1
        
        for i, (dx, dy) in enumerate(dr):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                if not (arr[x][y] & (1 << i)):
                    visited[nx][ny] = room_id
                    que.append((nx, ny))
    
    return room_size

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
room_id = 0
room_sizes = []

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            room_id += 1
            room_size = bfs(i, j, arr, visited, room_id)
            room_sizes.append(room_size)

max_size = max(room_sizes)

comb = 0

for x in range(M):
    for y in range(N):
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny] != visited[x][y]:
                    tmp = room_sizes[visited[x][y] -1] + room_sizes[visited[nx][ny] - 1]
                    comb = max(comb, tmp)

print(room_id)
print(max_size)
print(comb)
