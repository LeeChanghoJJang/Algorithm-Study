# 5650 핀볼 게임

def game(r, c, d):
    score, nr, nc, nd = 0, r, c, d

    while True:
        # 이동
        nr += ds[nd][0]; nc += ds[nd][1]
        # 범위
        if 0 <= nr < N and 0 <= nc < N:
            now = board[nr][nc]
            # 블록
            if 1 <= now <= 5:
                nd = guide[now][nd]
                score += 1
            # 웜홀
            elif 6 <= now <= 10:
                if (nr, nc) == guide[now][0]:
                    nr, nc = guide[now][1]
                else:
                    nr, nc = guide[now][0]
            # 출발위치
            elif (nr, nc) == (r, c): return score
            # 블랙홀
            elif now == -1: return score
        else:
            nd = guide[5][nd]
            score += 1

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

for tc in range(int(input())):
    N, ans = int(input()), 0
    board = [list(map(int, input().split())) for _ in range(N)]
    # 블록과 웜홀의 가이드 제시
    guide = [[],[2, 0, 3, 1],[2, 3, 1, 0],[1, 3, 0, 2],[3, 2, 0, 1],[2, 3, 0, 1],[],[],[],[],[]]
    [guide[board[i][j]].append((i, j)) for i in range(N) for j in range(N) if 5 < board[i][j] < 11]

    # 출발위치와 진행방향 변경
    for r in range(N):
        for c in range(N):
            if not board[r][c]:
                for d in range(4):
                    ans = max(ans, game(r, c, d))

    print(f'#{tc+1} {ans}')