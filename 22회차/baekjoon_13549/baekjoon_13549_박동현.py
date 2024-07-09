from collections import deque

N,K = map(int,input().split())    
q = deque([K])
visit = {}
visit[K] = 1

if K % 2 == 0 :
    q.append(K//2)
    visit[K//2] = 1

while q :
    now = q.popleft()
    if now == N :
        exit(print(visit[now]-1))

    if now % 2 == 0 and now//2 not in visit :
        q.append(now//2)
        visit[now//2] = visit[now] 
    if now+1 not in visit and 0 <= now+1 <= 100000:
        visit[now+1] = visit[now] + 1
        q.append(now+1)
    if now-1 not in visit and 0 <= now-1 <= 100000:
        visit[now-1] = visit[now] + 1
        q.append(now-1)
