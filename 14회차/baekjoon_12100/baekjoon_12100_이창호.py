import sys, copy
sys.stdin = open('input.txt')

# 입력
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_ = 0

# 블록 이동 함수
def move(board, m):
    if m == 'U':  # 위로 이동
        for y in range(n):
            end = 0
            for x in range(1, n):
                if board[x][y]:  # 현재 위치에 블록이 있을 경우
                    tmp = board[x][y]  # 현재 블록 값 저장
                    board[x][y] = 0  # 현재 위치 블록 제거
                    if board[end][y] == 0:  # 이동할 위치에 블록이 없는 경우
                        board[end][y] = tmp  # 이동
                    elif board[end][y] == tmp:  # 이동할 위치에 같은 값의 블록이 있는 경우
                        board[end][y] *= 2  # 합쳐지므로 값 두 배로 증가
                        end += 1
                    else:  # 이동할 위치에 다른 값의 블록이 있는 경우
                        end += 1
                        board[end][y] = tmp  # 블록 이동
    if m == 'D':  # 아래로 이동
        for y in range(n):
            end = n - 1
            for x in range(n - 2, -1, -1):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[end][y] == 0:
                        board[end][y] = tmp
                    elif board[end][y] == tmp:
                        board[end][y] *= 2
                        end -= 1
                    else:
                        end -= 1
                        board[end][y] = tmp
    if m == 'L':  # 왼쪽으로 이동
        for x in range(n):
            end = 0
            for y in range(1, n):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[x][end] == 0:
                        board[x][end] = tmp
                    elif board[x][end] == tmp:
                        board[x][end] *= 2
                        end += 1
                    else:
                        end += 1
                        board[x][end] = tmp
    if m == 'R':  # 오른쪽으로 이동
        for x in range(n):
            end = n - 1
            for y in range(n - 2, -1, -1):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[x][end] == 0:
                        board[x][end] = tmp
                    elif board[x][end] == tmp:
                        board[x][end] *= 2
                        end -= 1
                    else:
                        end -= 1
                        board[x][end] = tmp
    return board


# 백트래킹 함수
def backtracking(board, cnt):
    global max_
    if cnt == 5:  # 5번의 이동 후에 최댓값 갱신
        max_ = max(max_, max(map(max, board)))
        return

    for m in 'UDLR':
        tmp = move(copy.deepcopy(board), m)  # 현재 보드를 복사하여 이동
        backtracking(tmp, cnt + 1)


backtracking(board, 0)  # 백트래킹 시작
print(max_)  # 최댓값 출력
