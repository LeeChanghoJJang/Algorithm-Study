def sol(n, distance, graph):
    distance[1] = 0
    for check in range(n):
        for vertex in range(1, n+1):
            for next_vertex, next_cost in graph[vertex]:
                if distance[next_vertex] > distance[vertex] + next_cost:
                    distance[next_vertex] = distance[vertex] + next_cost
                    if check == n-1:
                        return False

    return True

t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    distance = [10000] * (n+1)

    for _ in range(m):     # 도로의 정보
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])

    for _ in range(w): # 웜홀의 정보
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    if sol(n, distance, graph):
        print('NO')
    else:
        print('YES')


