# 가능한 조합들 다 돌면서. 좌, 우 노드개수 맞으면 최솟값 갱신
from collections import deque
from itertools import combinations


def bfs(arr):
    global people, link
    start = arr[0]
    queue = deque([start])
    visited = set([start])
    num = 0

    while queue:
        value = queue.popleft()
        num += people[value]
        for i in link[value]:
            if i not in visited and i in arr:
                queue.append(i)
                visited.add(i)
    return num, len(visited)
# 조합 안에 있는 애들만


N = int(input())  # 구역 개수
people = [0] + list(map(int, input().split()))  # 구역별 인구수
link = [0]  # 연결된 구역들 리스트
result = float('inf')

for i in range(1, N + 1):
    link.append(list(map(int, input().split())))
    link[i] = link[i][1:]
# 그래프 받기


for i in range(1, N // 2 + 1):
    combis = list(combinations(range(1, N + 1), i))
    # 절반까지.
    for combi in combis:
        sum1, node1 = bfs(combi)
        sum2, node2 = bfs([i for i in range(1, N + 1) if i not in combi])
        # combi안에 없는 애들로.
        # 두 선거구의 모든 노드가 연결되어 있는지 확인
        if node1 + node2 == N:
            result = min(result, abs(sum1 - sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)