# 혼자서 하는 틱택토

def check_win(player, board):
    # 행 & 열 체크
    for j in range(3):
        if (
            all(board[i][j] == player for i in range(3)) or
            all(cell == player for cell in board[j])
        ):
            return True

    # 대각 체크
    if (
        all(board[i][i] == player for i in range(3)) or
        all(board[i][2-i] == player for i in range(3))
    ):
        return True

    return False

def solution(board):
    num_x = sum(row.count('X') for row in board)  # 'X' 개수
    num_o = sum(row.count('O') for row in board)  # 'O' 개수

    # 잘못된 경우 판별
    if (
        # 'X'가 'O'보다 많음
        num_x > num_o or
        # 둘의 개수 차이 1 초과
        abs(num_x - num_o) > 1 or
        # 'X'가 이겼는데 개수가 맞지 않음
        (check_win('X', board) and num_x != num_o) or
        # 'O'가 이겼는데 개수가 맞지 않음
        (check_win('O', board) and num_x != num_o - 1)
    ):
        return 0

    return 1