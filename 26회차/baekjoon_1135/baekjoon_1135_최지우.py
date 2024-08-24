N = int(input())
line = list(map(int, input().split()))
link = {i:[] for i in range(N)}

for i, n in enumerate(line):
    if n == -1:
        continue
    link[n].append(i)


def dfs(v):
    if not link[v]:
        return 0
    tmp = []
    for child in link[v]:
        tmp.append(dfs(child))
    tmp.sort(reverse=True)
    for i in range(len(tmp)):
        tmp[i] += i + 1
    
    return max(tmp)

print(dfs(0))