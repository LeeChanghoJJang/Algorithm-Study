import sys
sys.stdin = open('input.txt')
from collections import deque
# BFS 구현(출발점에서 도착점 갈 수 있다면 True 반환)
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
# 인접한 국가들
travel = [[] for _ in range(N+1)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]:
            travel[i].append(j)
# 여행 경로 계획
plan = list(map(lambda x : int(x)-1,input().split()))
result = 'YES'
for i in range(len(plan)-1):
    # 한번이라도 다음경로로 가지 못한다면
    if not BFS(plan[i],plan[i+1]):
        result='NO'
        break
print(result)
