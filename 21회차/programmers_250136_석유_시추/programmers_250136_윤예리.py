from collections import deque

def solution(land):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(land)
    m = len(land[0])
    
    visited = [[0] * m for _ in range(n)]
    result = [0 for i in range(m+1)]

    def bfs(i, j):
        cnt = 0
        visited[i][j] = 1

        q = deque([(i, j)])
        min_y, max_y = j, j

        while q:
            x, y = q.popleft()
            min_y, max_y = min(min_y, y), max(max_y, y)
            cnt += 1

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

        for i in range(min_y, max_y+1):
            result[i] += cnt
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j]:
                bfs(i, j)
        
    # print(visited)
    answer = max(result)
    return answer

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))