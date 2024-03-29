# 2098 외판원 순회

N = int(input())  # 도시의 수
W = [list(map(int, input().split())) for _ in range(N)]  # 각 도시간 이동 비용
DP = [[None] * (2**N) for _ in range(N)]

def TSP(now, visit):
    # 모든 도시를 방문한 경우
    if visit == 2**N - 1:
        return W[now][0] if W[now][0] > 0 else float('inf')
    
    # 이미 계산된 경우
    if DP[now][visit] is not None:
        return DP[now][visit]
    
    # 최소 비용 초기화
    min_cost = float('inf')
    
    # 모든 도시를 순회
    for next in range(N):
        # 이미 방문했거나 갈 수 없는 경우 스킵
        if visit & (2**next) or W[now][next] == 0:
            continue
        
        # 다음 도시로 이동하는 비용 계산
        cost = W[now][next] + TSP(next, visit | 2**next)
        min_cost = min(min_cost, cost)
    
    DP[now][visit] = min_cost
    return min_cost

print(TSP(0, 1))


# prim 오답
'''
from heapq import heappush, heappop
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 16000000

for i in range(N):
    cost = 0; visit = [0] * N; Q = [[0, i]]
    while Q:
        w, now = heappop(Q)
        cost += w; visit[now] = 1; Q = []
        for next in range(N):
            if arr[now][next] and not visit[next]:
                heappush(Q, [arr[now][next], next])
        if not Q: cost += arr[now][i]; break
    if 0 not in visit: ans = min(ans, cost)
print(ans)
'''