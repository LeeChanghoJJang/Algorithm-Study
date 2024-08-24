import sys
input = sys.stdin.readline

def dfs(node):
    if not child[node]: return 0

    result = []
    for c in child[node]:
        result.append(dfs(c))
    result.sort(reverse=True)
    result = [result[i] + i + 1 for i in range(len(child[node]))]
    return max(result)

n = int(input())
par = list(map(int, input().split()))
child = [[] for _ in range(n)]

for c in range(1, n):
    p = par[c]
    child[p].append(c)

print(dfs(0))
