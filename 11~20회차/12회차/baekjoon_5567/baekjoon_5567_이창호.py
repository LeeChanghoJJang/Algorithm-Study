import sys

# 표준 입력을 'input.txt'에서 읽도록 재지정
sys.stdin = open('input.txt')

from collections import deque

# 도시의 수 입력
n = int(input())

# 친구 관계의 수 입력
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 친구 관계 입력 및 그래프에 저장
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문한 노드를 저장할 집합 초기화하고, 시작 노드 1을 방문한 것으로 표시
visited = set([1])

# BFS를 위한 큐 초기화
q = deque([[1, 0]])

# BFS 탐색
while q:
    # 현재 노드와 거리 정보를 가져옴
    friends, cnt = q.popleft()
    # 거리가 2보다 작은 경우에만 이웃 노드들을 탐색
    if cnt < 2:
        for next_friend in graph[friends]:
            if next_friend not in visited:  # 방문하지 않은 이웃 노드인 경우
                visited.add(next_friend)  # 방문 표시
                q.append((next_friend, cnt + 1))  # 다음 노드와 거리를 큐에 추가

# 친구의 수에서 자기 자신을 제외한 결과를 출력
print(len(visited) - 1)
