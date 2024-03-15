import sys
sys.stdin = open('input.txt')
from collections import deque
def BFS(start,end):
    visited = [0] * (N+1)
    queue = deque([start])
    while queue:
        now = queue.popleft()
        visited[now] = 1
        if now == end:
            return True
        for next in travel[now]:
            if not visited[next]:
                queue.append(next)
    return False

N,M = int(input()), int(input())
travel = [[] for _ in range(N+1)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]:
            travel[i].append(j)
plan = list(map(lambda x : int(x)-1,input().split()))
result = 'YES'
for i in range(len(plan)-1):
    if not BFS(plan[i],plan[i+1]):
        result='NO'
        break
print(result)