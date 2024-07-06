# 17135 캐슬디펜스

from collections import deque
from itertools import combinations

def game(archers):
    newGrid = [row[:] for row in grid]
    score = 0

    # 모든 적이 격자판에서 제외되면 게임 끝
    for row in range(N-1, -1, -1):
        attackList = set()

        # 공격 대상 찾기
        for archer in archers:
            Q = deque([[row, archer, 1]])

            while Q:
                i, j, d = Q.popleft()

                if newGrid[i][j]:
                    attackList.add((i, j))
                    break

                if d < D:
                    for di, dj in go:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M:
                            Q.append([ni, nj, d+1])

        # 공격
        for i, j in attackList:
            newGrid[i][j] = 0
            score += 1

    return score

go = ((0, -1), (-1, 0), (0, 1))
N, M, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for archers in combinations(range(M), 3):
    ans = max(ans, game(archers))

print(ans)