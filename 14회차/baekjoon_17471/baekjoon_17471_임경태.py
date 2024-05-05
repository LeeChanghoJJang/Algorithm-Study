# 17471 게리맨더링
from collections import deque
from itertools import combinations

# 선거구 체크
def BFS(area):
    s = area[0]
    sumPop = population[s]
    Q = deque([s])
    visit = {s,}

    while Q:
        now = Q.popleft()

        for next in graph[now]:
            if next in area and next not in visit:
                sumPop += population[next]
                Q.append(next)
                visit.add(next)

    return sumPop, len(visit)

N = int(input())
population = list(map(int, input().split()))
graph = [[] for _ in range(N)]
ans = 10000

# 그래프 제작
for i in range(N):
    _, *info = list(map(int, input().split()))
    graph[i] = list(map(lambda x: x-1, info))

# 조합 만들어 BFS 실행
for i in range(1, N//2+1):
    for area in combinations(range(N), i):
        sumA, lenA = BFS(area)
        sumB, lenB = BFS([i for i in range(N) if i not in area])

        if lenA + lenB == N:
            ans = min(ans, abs(sumA - sumB))

print(ans if ans != 10000 else -1)
