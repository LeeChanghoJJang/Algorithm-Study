from collections import deque
 
def topological_sort():
    result = []
    q = deque()
 
    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)
 
    while q:
        vertex = q.popleft()
        result.append(vertex)
 
        for v in graph[vertex]:
            indegree[v] -= 1
 
            if indegree[v] == 0:
                q.append(v)
 
    return result
 
for tc in range(10):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    indegree = [0] * (V + 1)
    list_ = list(map(int, input().split()))
 
    for i in range(0, 2 * E, 2):
        graph[list_[i]].append(list_[i + 1])
        indegree[list_[i + 1]] += 1
 
    print(f'#{tc + 1}', *topological_sort())