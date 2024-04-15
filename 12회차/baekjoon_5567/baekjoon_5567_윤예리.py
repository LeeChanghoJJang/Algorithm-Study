import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = [0, 1] + [0] * (n-1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 친구 찾기
for i in graph[1]:
    if not visited[i]:
        visited[i] = 1
    
    # 친구의 친구 찾기
    for j in graph[i]:
        if not visited[j]:
            visited[j] = 1

print(sum(visited)-1)