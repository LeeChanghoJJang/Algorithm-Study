# 1199 오일러 회로

import sys
sys.stdin = open("input.txt")

N = int(input())
count = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

for i in range(N):
    # 모든 정점이 짝수 차수를 갖지 않으면 오일러 회로 불가능
    if sum(count[i]) & 1: exit(print(-1))

    # 그래프 제작
    for j in range(i):
        if count[i][j]:
            graph[i].append(j)
            graph[j].append(i)

# DFS 진행
S = [0]
while S:
    now = S[-1]

    while graph[now]:
        next = graph[now][-1]

        # x가 y보다 더 작게
        x, y = (next, now) if now > next else (now, next)
        # 두 노드 사이에 남은 간선이 있다면 패스
        if count[x][y]: break
        # 두 노드 사이에 남은 간선이 없다면 그래프에서 해당 노드 제거
        graph[now].pop()

    # 현재 노드에서 갈 수 있는 노드가 있다면 스택에 다음 노드 추가 및 간선 소모
    if graph[now]:
        S.append(next)
        count[x][y] -= 1
    # 현재 노드에서 갈 수 있는 노드가 없다면 스택에서 현재 노드 제거 및 출력
    else:
        S.pop()
        print(now + 1, end=" ")

"""
    - 오일러 경로 : 그래프의 모든 간선을 정확히 한 번씩 지나는 경로
    - 오일러 회로 : 오일러 경로 + 시작점이 종료점과 같음

    - Euler's Theorem
        1. 홀수 차수를 가지는 정점이 0 or 2개인 경우 오일러 경로를 적어도 1개 갖는다.
        2. 모든 정점이 짝수 차수를 가지는 경우 오일러 회로를 적어도 1개 갖는다.
"""