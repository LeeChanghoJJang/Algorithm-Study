from collections import deque

def solution(land):
    n,m = len(land), len(land[0])
    locations = dict({0:0})
    dr = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = [[False] * m for _ in range(n)]
    idx = 1

    def bfs(i,j,idx):
        cnt = 1
        queue = deque([[i,j]])
        land[i][j]=idx
        visited[i][j]=True
        while queue:
            x,y = queue.popleft()
            for j in range(4):
                nx = x + dr[j][0]
                ny = y + dr[j][1]
                if 0<= nx < n and 0<= ny < m and not visited[nx][ny] and land[nx][ny]==1:
                    visited[nx][ny] = True
                    land[nx][ny]=idx
                    queue.append((nx,ny))
                    cnt+=1
        return cnt

    for i in range(n):
        for j in range(m):
            if land[i][j]==1 and not visited[i][j]:
                locations[idx] = bfs(i,j,idx)
                idx+=1
    result = 0
    for i in range(m):
        temp =set()
        for j in range(n):
            temp.add(land[j][i])
        result = max(result,sum(map(lambda x : locations[x], temp)))

    return result
