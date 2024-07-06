# 250136 [PCCP 기출문제] 2번 / 석유 시추
from collections import deque

def solution(land):
    def bfs(ci, cj, idx):
        Q = deque([(ci, cj)])
        area = 1

        while Q:
            i, j = Q.popleft()

            for di, dj in dr:
                ni, nj = i + di, j + dj

                if 0<=ni<n and 0<=nj<m and not visit[ni][nj] and land[ni][nj]:
                    Q.append((ni, nj))
                    visit[ni][nj] = idx
                    area += 1

        return area

    ans = 0
    idx = 1
    n, m = len(land), len(land[0])
    visit = [[0] * m for _ in range(n)]
    dr = (0, 1), (1, 0), (0, -1), (-1, 0)
    spots = {}

    for i in range(n):
        for j in range(m):
            if land[i][j] and not visit[i][j]:
                visit[i][j] = idx
                spots[idx] = bfs(i, j, idx)
                idx += 1
    
    for j in range(m):
        oil = set(visit[i][j] for i in range(n) if visit[i][j])
        ans = max(ans, sum(spots[s] for s in oil))

    return ans