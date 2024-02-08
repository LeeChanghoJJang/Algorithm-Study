# 2806 N-Queen
# 1. 말을 임의의 자리에 놓는다
# 2. 못 놓는 부분 표시
# 3-1. 다음 행에 말을 놓는다 + 재귀
# 3-2. 자리가 없다면 그대로 실행 끝
# 4. 모든 행에 말이 다 있다면 카운트 +1


# queen 놓은 곳 체크 및 해제
def update_board(board, row, col, check):
    # check가 True면 체크, False면 해제
    if check:
        board[row][col] += 1
    else:
        board[row][col] -= 1
    
    for k in range(8):
        ni = row + di[k]
        nj = col + dj[k]
        while 0 <= ni < N and 0 <= nj < N:
            if check:
                board[ni][nj] += 1
                ni += di[k]
                nj += dj[k]
            else:
                board[ni][nj] -= 1
                ni += di[k]
                nj += dj[k]
    
    return board


# DFS 실행 함수
def queen(board, row):
    # 모든 말을 다 놓았다면 cnt +1
    if row == N:
        global cnt
        cnt += 1
    else:
        # 열 순회하며 말을 놓을 수 있다면 말을 놓고 다음 행에서 함수 실행
        for col in range(N):
            if board[row][col] == 0:
                update_board(board, row, col, True)    # attack range check
                queen(board, row+1)                    # search in next row
                update_board(board, row, col, False)   # attack range clear


di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

for tc in range(int(input())):
    N = int(input()); cnt = 0
    board = [[0] * N for _ in range(N)]
    queen(board, 0)
    print(f'#{tc+1} {cnt}')

'''
61,428KB / 304ms
'''