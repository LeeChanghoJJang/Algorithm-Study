# 2665 미로만들기
from heapq import heappush, heappop

# 다익스트라 - 64번
n = int(input())
go = ((0, 1), (1, 0), (0, -1), (-1, 0))
arr = [list(map(int, input())) for _ in range(n)]
dist = [[2*n] * n for _ in range(n)]; dist[0][0] = 0

Q = [[0, 0, 0]]
while Q:
    # 이동 비용이 가장 적은 이웃 노드부터 방문
    now_cost, i, j = heappop(Q)

    # 현재 노드의 기존 비용과 신규 비용 비교
    if dist[i][j] < now_cost:
        continue

    # 이웃 노드 순회
    for di, dj in go:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            # 이웃 노드의 신규 비용 계산
            next_cost = now_cost + (1 - arr[ni][nj])

            # 이웃 노드의 기존 비용과 신규 비용 비교
            if dist[ni][nj] > next_cost:
                dist[ni][nj] = next_cost
                heappush(Q, [next_cost, ni, nj])

print(dist[-1][-1])


# 백트래킹 - 시간초과, 1787번
'''
go = ((0, 1), (1, 0), (0, -1), (-1, 0))
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
ans = 2*n

def DFS(arr, visit, i, j, cnt):
    global ans
    if cnt >= ans: return

    if i == n-1 and j == n-1:
        ans = min(ans, cnt)
        return

    for di, dj in go:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and not visit[ni][nj]:
            visit[ni][nj] = 1
            if arr[ni][nj]:
                DFS(arr, visit, ni, nj, cnt)
            else:
                DFS(arr, visit, ni, nj, cnt+1)
            visit[ni][nj] = 0

DFS(arr, visit, 0, 0, 0)
print(ans)
'''