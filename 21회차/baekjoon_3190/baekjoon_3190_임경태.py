# 3190 뱀
from collections import deque

def game():
    dr = (0, 1), (1, 0), (0, -1), (-1, 0)
    Q = deque([(0, 0)])
    time = hq = m = 0

    while True:
        i, j = Q[-1]

        # 방향 전환
        if m < len(mov) and time == int(mov[m][0]):
            if mov[m][1] == 'D':
                hq = (hq + 1) % 4
            else:
                hq = (hq + 3) % 4
            m += 1
        
        ni, nj = i+dr[hq][0], j+dr[hq][1]
        
        # 게임 끝
        if not (0<=ni<N and 0<=nj<N) or (ni, nj) in Q:
            return time + 1

        # 몸길이 늘림
        Q.append((ni, nj))
        
        # 이동 칸에 사과 유무
        if board[ni][nj]:
            board[ni][nj] = 0
        else:
            Q.popleft()

        time += 1


N = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(int(input())):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

mov = [input().split() for _ in range(int(input()))]

game()