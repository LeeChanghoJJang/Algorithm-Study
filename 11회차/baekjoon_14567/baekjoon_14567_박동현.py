# 위상 정렬 ?
import sys
from collections import deque

input = sys.stdin.readline


N,M = map(int,input().split())


graph = [[] for _ in range(N+1)]    # 관계 그래프
degree = [0] * (N+1)                # 관계 차수
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1                  


DP = [0] * (N+1)

q = deque()
for i in range(1,N+1):              # 각 과목에 대해
    if degree[i] == 0 :             # 선수 과목이 없는 경우에
        q.append((i,1))             # q에 담아 초기조건을 만든다.
        DP[i] = 1                  

while q :
    now, cost = q.popleft()         # 그래프를 순회하면서
    for next in graph[now]:         # 이후 노드에 대해서 
        degree[next] -= 1           # 다음 차례의 관계를 한 차수 내리면서
        if degree[next] == 0 :      # 더 이상 선수과목이 없는 경우
            q.append((next,cost+1)) # q에 더하고
            DP[next] = cost+1       # DP의 값을 확정한다.

print(*DP[1:])