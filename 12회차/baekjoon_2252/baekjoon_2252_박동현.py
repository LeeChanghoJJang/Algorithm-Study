import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())     # N : 학생 수 M : 노드 수

graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)                # 진입 차수에 대한 리스트. 

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1                  # 종착 노드의 간선이 몇 개 존재하는지 기록한다.

q = deque()

for i in range(1,N+1):
    if degree[i] == 0 :             # 진입 차수가 0이다 == 정렬 시 선순위에 배치된다.
        q.append(i)

ans = []

while q :
    now = q.popleft()               # 앞에서부터 순회하면서
    ans.append(now)                 # 담으면 위상 정렬된 리스트가 만들어진다.

    for next in graph[now]:         # 그래프의 다음 노드에서
        degree[next] -= 1           # 차수를 한 단계 낮추고
        if degree[next] == 0 :      # 차수가 0이라면
            q.append(next)          # q에 담근다.

print(*ans)                         # 출력