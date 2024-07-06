# 사라지는 발판 (2022 KAKAO BLIND RECRUITMENT)

def solution(board, aloc, bloc):
    move = ((0, 1), (0, -1), (1, 0), (-1, 0))
    N, M = len(board), len(board[0])
    visit = [[0] * M for _ in range(N)]

    def play(board, i, j, oi, oj):
        if visit[i][j]:
            return 0
        
        me_res = 0

        for di, dj in move:
            ni, nj = i + di, j + dj

            if not (0 <= ni < N and 0 <= nj < M) or visit[ni][nj] or not board[ni][nj]:
                continue

            visit[i][j] = 1
            op_res = play(board, oi, oj, ni, nj) + 1
            visit[i][j] = 0

            # 나 - 패배 / 상대 - 패배
            if me_res % 2 == 0 and op_res % 2 == 1:
                me_res = op_res
            # 나 - 패배 / 상대 - 승리
            elif me_res % 2 == 0 and op_res % 2 == 0:
                me_res = max(me_res, op_res)
            # 나 - 승리 / 상대 - 패배
            elif me_res % 2 == 1 and op_res % 2 == 1:
                me_res = min(me_res, op_res)

        return me_res

    return play(board, aloc[0], aloc[1], bloc[0], bloc[1])
