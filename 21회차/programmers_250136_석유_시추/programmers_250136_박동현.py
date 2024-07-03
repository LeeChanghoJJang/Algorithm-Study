from collections import deque

dr = (1,0),(0,1),(-1,0),(0,-1)
def solution(land):
    N = len(land)
    M = len(land[0])
    data = [0] * M
    visit = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and land[i][j]:
                q = deque([(i,j)])
                visit[i][j] = 1
                vst = {j}
                cnt = 1
                while q:
                    x,y = q.popleft()
                    
                    for dx,dy in dr:
                        di,dj = x+dx, y+dy
                        if 0<=di<N and 0<=dj<M and land[di][dj] and not visit[di][dj]:
                            cnt += 1
                            vst.add(dj)
                            visit[di][dj] = 1
                            q.append((di,dj))
                            
                for v in vst:
                    data[v] += cnt
    return max(data)