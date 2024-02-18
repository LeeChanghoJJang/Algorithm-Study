# 11725 / 트리의 부모 찾기 / 실버2

N = int(input()) # 노드 개수
link = [[] for _ in range(N+1)]  # 연결 노드
prnt = [0] * (N+1)  # 부모 노드

# 무방향 그래프 제작
for _ in range(N-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

# DFS - 트리의 루트 1을 시작으로 탐색
stack = [1]
while stack:
    now = stack.pop()

    # 다음 노드에 부모 노드로 자신 입력
    for next in link[now]:
        if not prnt[next]:
            prnt[next] = now
            stack.append(next)

for i in prnt[2:]:
    print(i)