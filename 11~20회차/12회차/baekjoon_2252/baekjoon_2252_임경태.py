# 2252 줄 세우기

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
stack = []

# 그래프 제작
for _ in range(M):
    f, b = map(int, input().split())
    graph[f].append(b)

def DFS(now):
    visit[now] = True
    # 그래프 순회
    for next in graph[now]:
        if not visit[next]:
            DFS(next)
    # 제일 우선순위가 낮은 것부터 스택에 저장
    stack.append(now)

# 각 번호 순회하며 방문하지 않았으면 DFS 가동
for i in range(1, N+1):
    if not visit[i]: DFS(i)

# 우선순위가 높은 것부터 출력
while stack:
    print(stack.pop(), end=' ')