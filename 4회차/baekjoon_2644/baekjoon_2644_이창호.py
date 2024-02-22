import sys

def DFS(start,end,visited):
    stack =[start]
    visited[start]=1
    while stack:
        now = stack.pop()
        if now == end:
            return visited[now]-1
        for next in connection[now]:
            if not visited[next]:
                visited[next] = visited[now] + 1
                stack.append(next)
    return -1

n = int(sys.stdin.readline())
target1, target2 = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
connection = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    connection[x].append(y)
    connection[y].append(x)
print(DFS(target1,target2,[0]*(n+1)))
