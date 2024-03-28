# 16236 아기상어
from collections import deque

def BFS(i, j, size):
    Q = deque([[i, j]])
    dist = [[0] * N for _ in range(N)]
    dist[i][j] = 1
    fish = []

    while Q:
        i, j = Q.popleft()
        for di, dj in go:
            ni, nj = i + di, j + dj

            # 범위, 방문, 크기 같거나 작음 -> 이동 가능
            if 0<=ni<N and 0<=nj<N and dist[ni][nj] == 0 and sea[ni][nj] <= size:
                dist[ni][nj] = dist[i][j] + 1
                Q.append([ni, nj])

                # 상어 크기보다 작으면 먹잇감 후보에 등극
                if 0 < sea[ni][nj] < size:
                    # 우선순위 : 가까움 - 가장 위 - 가장 왼쪽
                    fish.append([dist[ni][nj]-1, ni, nj])

        # 거리가 가까운 물고기만 찾으면 되므로 많이 찾을 필요 없음
        if len(fish) > 2: break

    if fish: return sorted(fish)[0]
    else: return

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
go = ((-1, 0), (0, -1), (0, 1), (1, 0))
time, size, feed = 0, 2, 2

# 초기 위치 확인
def search():
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                sea[i][j] = 0
                return i, j
i, j = search()

while True:
    # 사냥할 물고기 탐색
    info = BFS(i, j, size)

    # 사냥 가능한 물고기가 없다면 종료
    if not info: break

    # 물고기 먹고 쑥쑥 자라나자
    dist, i, j = info
    sea[i][j] = 0
    time += dist
    feed -= 1

    # 먹이 할당량 충족
    if not feed:
        size += 1
        feed = size

print(time)