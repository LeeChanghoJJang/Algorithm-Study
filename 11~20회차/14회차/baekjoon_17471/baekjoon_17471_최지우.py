import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def bfs(same):
    start = same[0]
    q = deque([start])
    visited = set([start])
    _sum = 0
    while q:
        v = q.popleft()
        _sum += node_number[v]
        for u in linked_list[v]:
            if u not in visited and u in same:
                q.append(u)
                visited.add(u)
    return _sum, len(visited)


n = int(input())
node_number = list(map(int,input().split()))

result = float('inf')
linked_list = [[] for _ in range(n)]

for i in range(n):
    near_node = list(map(int,input().split()))
    for j in range(1, near_node[0] + 1):
        linked_list[i].append(near_node[j] - 1)

for i in range(1, n//2 + 1):
    combis = list(combinations(range(n), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(n) if i not in combi])
        if v1 + v2 == n:
            result = min(result, abs(sum1 - sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)