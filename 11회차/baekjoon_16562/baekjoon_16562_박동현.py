from collections import deque

N,M,k = map(int,input().split())     # N 친구 번호 M 친구 관계 k 가지고 있는 돈 

fee = [0] + list(map(int,input().split()))      # fee : 친구비 
graph = [[] for _ in range(N+1)]                # graph : 친구관계

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (N+1)
ans = 0
# 친구 순번들을 순회하면서
for i in range(N+1):
    q = deque([i])                      # 한 친구를 큐에 넣고
    mini = float('inf')                 # 최소값 설정 
    while q :                           # 그래프 순회
        now = q.popleft()
        if not visit[now] :             # 방문하지 않았으면
            mini = min(mini, fee[now])  # 최소값 갱신 하고
            visit[now] = True           # 방문처리

            for next in graph[now]:     # 다른 친구관계에 대해서
                q.append(next)          # q에 담기

    # mini가 갱신된 경우에만 ans에 추가하기
    if mini != float('inf') :
        ans += mini
# 계산이 끝나고, 
# 내야할 친구비가 가지고 있는 돈보다 많으면
if k < ans:
    print("Oh no")
# 돈으로 해결할 수 있다면 
else :
    print(ans)