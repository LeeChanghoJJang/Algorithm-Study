T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 8 for _ in range(8)]

def is_safe(board, row, col, N):
    # 같은 열에 퀸이 있는지 확인
    for i in range(row):
        if board[i][col] == 1:
            return False

    # 왼쪽 위 대각선에 퀸이 있는지 확인
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 오른쪽 위 대각선에 퀸이 있는지 확인
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        # 모든 행에 퀸을 놓았으면 현재의 보드를 출력하거나 다른 처리 수행
        for i in range(N):
            print(board[i])
        print("\n")
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, N):
                return True  # 한 가지 해답을 찾으면 중단
            board[row][col] = 0  # 현재 위치에서 해답을 찾지 못하면 퀸 제거

    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        print("해답이 존재하지 않습니다.")

# 예시로 N=4일 때의 호출
solve_n_queens(4)
