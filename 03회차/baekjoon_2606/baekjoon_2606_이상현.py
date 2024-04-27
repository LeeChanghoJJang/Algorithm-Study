# 백준 2606번 바이러스

# dfs를 이용한 접근
def dfs(vertex, graph):

    # 이미 방문한 곳이라면 함수 종료
    if visited[vertex]:
        return
    
    visited[vertex] = 1

    # 정점에 연결된 각 정점에서 dfs함수를 호출
    [dfs(v, graph) for v in graph[vertex]]

input()

# E는 간선의 수
E = int(input())
graph = [[] for _ in range(101)]
visited = [0] * 101

for _ in range(E):
    a, b = map(int, input().split())
    
    # 양방향 간선
    graph[a].append(b)
    graph[b].append(a)

dfs(1, graph)

# 자기 자신을 제외하고 방문한 컴퓨터의 수를 세어 출력
print(sum(visited[i] for i in range(101)) - 1)