# 시간 초과

def dfs(vertex):
    for v in graph[vertex]:
        if list_[vertex][v]:
            list_[vertex][v] -= 1
            list_[v][vertex] -= 1
            dfs(v)

    print(vertex + 1, end = " ")

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

for row in range(N):
    sum_ = 0

    for col in range(N):
        for cnt in range(list_[row][col]):
            graph[row].append(col)
            sum_ += 1

    if sum_ % 2 != 0:
        print(-1)
        exit()

dfs(0)