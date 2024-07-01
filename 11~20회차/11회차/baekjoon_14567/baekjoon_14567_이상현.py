from heapq import*

def topological_sort():
    q = []
    result = [0] * (N + 1)

    for vertex in range(1, N + 1):
        if indegree[vertex] == 0:
            heappush(q, (1, vertex))

    while q:
        semester, vertex = heappop(q)
        result[vertex] = semester

        for v in graph[vertex]:
            indegree[v] -= 1
            
            if indegree[v] == 0:
                heappush(q, (semester + 1, v))

    return result

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

result = topological_sort()

for i in result:
    if i:
        print(i, end = ' ')