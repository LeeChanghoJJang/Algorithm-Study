import sys
sys.stdin = open('input.txt')
# 첫번째 방법 : swea에서는 시간초과 안됬으나, 백준에서는 시간초과 됨
# def nqueen(row,col,num_sum,row_col_diff):
#     global cnt
#     global complete
#     if cnt == N:
#         complete +=1
#         return
#
#     for i in range(N):
#         for j in range(N-1,-1,-1):
#             if len(row)==0 or i>=row[-1] and i not in row and j not in col and i+j not in num_sum and i-j not in row_col_diff:
#                 row.append(i)
#                 col.append(j)
#                 num_sum.append(i+j)
#                 row_col_diff.append(i-j)
#                 cnt+=1
#                 nqueen(row,col,num_sum,row_col_diff)
#                 cnt-=1
#                 row_col_diff.pop()
#                 num_sum.pop()
#                 row.pop()
#                 col.pop()
# row = []
# col=[]
# num_sum = []
# row_col_diff = []
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     cnt = 0
#     complete = 0
#     nqueen(row,col,num_sum,row_col_diff)
#     print(f'#{tc} {complete}')
# 두번째 방법 : ChatGPT 개선 --> 변수 오류 존나 많아서 내가 일일이 수정함
def nqueen(row, col, num_sum, row_col_diff):
    global complete
    if len(row) == N:
        complete += 1
        return

    for i in range(N):
        for j in range(N):
            if is_safe(i,j, row, col, num_sum, row_col_diff):
                place_queen(i, j, row, col, num_sum, row_col_diff)
                nqueen(row, col, num_sum, row_col_diff)
                remove_queen(row, col, num_sum, row_col_diff)

def is_safe(i,j, row, col, num_sum, row_col_diff):
    return len(row) == 0 or i >= row[-1] and i not in row and j not in col and i+j not in num_sum and i-j not in row_col_diff

def place_queen(i, j, row, col, num_sum, row_col_diff):
    row.append(i)
    col.append(j)
    num_sum.append(i + j)
    row_col_diff.append(i - j)

def remove_queen(row, col, num_sum, row_col_diff):
    row.pop()
    col.pop()
    num_sum.pop()
    row_col_diff.pop()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    complete = 0
    nqueen([], [], [], [])
    print(f'#{tc} {complete}')


# 세번째 방법 :
    def nqueen(row, col, num_sum, row_col_diff):
        global complete
        if len(row) == N:
            complete += 1
            return

        for i in range(N):
            for j in range(N):
                if is_safe(i, j, row, col, num_sum, row_col_diff):
                    place_queen(i, j, row, col, num_sum, row_col_diff)
                    nqueen(row, col, num_sum, row_col_diff)
                    remove_queen(row, col, num_sum, row_col_diff)


    def is_safe(i, j, row, col, num_sum, row_col_diff):
        return len(row) == 0 or i >= row[
            -1] and i not in row and j not in col and i + j not in num_sum and i - j not in row_col_diff


    def place_queen(i, j, row, col, num_sum, row_col_diff):
        row.append(i)
        col.append(j)
        num_sum.append(i + j)
        row_col_diff.append(i - j)


    def remove_queen(row, col, num_sum, row_col_diff):
        row.pop()
        col.pop()
        num_sum.pop()
        row_col_diff.pop()


    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        cnt = 0
        complete = 0
        nqueen([], [], [], [])
        print(f'#{tc} {complete}')