# 27978 보물 찾기 2
from heapq import heappop, heappush

di = (0, 1, -1, 1, -1, 1, -1, 0)
dj = (1, 1, 1, 0, 0, -1, -1, -1)
H, W = map(int, input().split())
sea = [input().rstrip() for _ in range(H)]

# 배 위치 검색
def ship():
    for i in range(H):
        for j in range(W):
            if sea[i][j] == 'K':
                return i, j
i, j = ship()

# 다익스트라
dist = [[10**8] * W for _ in range(H)]
dist[i][j] = 0
Q = [[0, i, j]]
while Q:
    w, i, j = heappop(Q)

    if dist[i][j] < w:
        continue

    for k in range(8):
        ni, nj = i + di[k], j + dj[k]

        # 오른쪽으로 가면 연료 소모 없음
        if k < 3: next_w = w
        else: next_w = w + 1

        # 범위, 암초, 비용 고려
        if 0<=ni<H and 0<=nj<W and sea[ni][nj] != '#' and dist[ni][nj] > next_w:
            dist[ni][nj] = next_w
            heappush(Q, [next_w, ni, nj])

            # 보물 발견하면 끝
            if sea[ni][nj] == '*':
                exit(print(dist[ni][nj]))

print(-1)