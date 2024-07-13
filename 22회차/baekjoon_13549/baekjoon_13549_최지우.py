from collections import deque

N, K = map(int, input().split())
visited = [-1]*100001

def bfs():
    que = deque()
    que.append(N)
    visited[N] = 0

    while que:
        v = que.popleft()
        
        if v == K:
            return visited[v]
            
        for nxt in (v*2, v-1, v+1):
            if nxt>100000 or nxt<0: continue
            
            if visited[nxt] == -1:
                if nxt==v*2:
                    visited[nxt] = visited[v]
                    que.appendleft(nxt)
                else:
                    visited[nxt] = visited[v] + 1
                    que.append(nxt)
            else:
                if nxt==v*2:
                    visited[nxt] = min(visited[nxt], visited[v])
                else:
                    visited[nxt] = min(visited[nxt], visited[v]+1)
                    
            
print(bfs())