from collections import deque

# 상하좌우, 대각선 방향 설정
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 입력 받기
H, W = map(int, input().split())
board = [input().rstrip() for _ in range(H)]

# 보물과 배의 위치 찾기
treasure = None
ship = None
for i in range(H):
    for j in range(W):
        if board[i][j] == '*':
            treasure = (i, j)
        elif board[i][j] == 'K':
            ship = (i, j)

# BFS를 통해 보물까지의 최단 거리 계산
def bfs(start):
    visited = [[False] * W for _ in range(H)]
    q = deque([start])
    visited[start[0]][start[1]] = True
    fuel = 0
    
    while q:
        size = len(q)
        fuel += 1
        
        for _ in range(size):
            x, y = q.popleft()
            
            if (x, y) == treasure:
                return fuel - 1
            
            for k in range(8):
                nx, ny = x + dx[k], y + dy[k]
                
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and board[nx][ny] != '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
    return -1

# 결과 출력
result = bfs(ship)
print(result)