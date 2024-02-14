import sys
sys.stdin = open('input.txt')
# 첫번째 방법 : swea에서는 시간초과 안됬으나, 백준에서는 시간초과 됨
def nqueen(row,col,num_sum,row_col_diff):
    global cnt
    global complete
    if cnt == N:
        complete +=1
        return

    for i in range(N):
        for j in range(N-1,-1,-1):
            if len(row)==0 or i>=row[-1] and i not in row and j not in col and i+j not in num_sum and i-j not in row_col_diff:
                row.append(i)
                col.append(j)
                num_sum.append(i+j)
                row_col_diff.append(i-j)
                cnt+=1
                nqueen(row,col,num_sum,row_col_diff)
                cnt-=1
                row_col_diff.pop()
                num_sum.pop()
                row.pop()
                col.pop()
row = []
col=[]
num_sum = []
row_col_diff = []

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    complete = 0
    nqueen(row,col,num_sum,row_col_diff)
    print(f'#{tc} {complete}')

# 두번째 방법 : N=12까지 동작 ( 13도 동작은 하나.. 매우 늦음)
def is_safe(board, row, col):
    # 행이 인덱스 값이 1. 같은 열에 있는지, 2. 우하향 대각선, 3. 우상승 대각선인지
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens_util(board, row, N):
    global cnt
    if row == N:
        cnt += 1
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(board, row + 1, N)
            # Backtrack
            board[row] = 0

def solve_nqueens(N):
    global cnt
    board = [0] * N
    cnt=0
    solve_nqueens_util(board, 0, N)
    return cnt

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = solve_nqueens(N)
    print(f'#{tc} {cnt}')

# 세번째 방법 : visited 리스트 설정하여 백트래킹
# 백준 pypy로 돌렸을 때, 141924KB, 13372ms

def n_queen(depth):
    global result

    if depth ==N:
        result +=1
        return

    # depth별 반복문
    for i in range(N):
        # 해당 depth를 visited 하지 않았을 때
    # 행을 반복문을 통해 순회
    for i in range(n):
        # 열이 동일하거나, 대각선에 있거나 둘중 하나임
        if (board[n]==board[i]) or (n-i == abs(board[n] - board[i])):
            return False
    return True

N = int(input())
board = [0] * N # 인덱스가 행이고, 값이 열이라고 생각하면 됨
visited = [False] * N
result = 0

n_queen(0)
print(result)
