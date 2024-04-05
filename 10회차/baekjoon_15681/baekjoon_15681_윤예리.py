import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
cnt = [0] * (n+1)

def count(x):
    cnt[x] = 1
    for y in graph[x]:
        if not cnt[y]:
            count(y)
            cnt[x] += cnt[y]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count(r)

for j in range(q):
    u = int(input())
    print(cnt[u])