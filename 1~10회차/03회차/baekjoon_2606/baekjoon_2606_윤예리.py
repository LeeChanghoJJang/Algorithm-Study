computer = int(input())
network = int(input())
connection = [[] for _ in range(computer+1)]
visited = [0] * (computer+1)

# 그래프 만들기
for n in range(network):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

def dfs(s):
    visited[s] = 1
    for i in connection[s]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(sum(visited)-1)
# bfs 안 배웠을 때 푼 거라 bfs로 풀어도 될듯
