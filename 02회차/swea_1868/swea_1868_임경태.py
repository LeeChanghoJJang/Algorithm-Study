# 1868 파핑파핑 지뢰찾기

'''
BFS 사용 : 근접한 노드를 우선적으로 탐색
최단 경로 : 최소한의 클릭으로 모든 빈 공간을 발견하는 데 유용
queue 사용 : 원하는 지점을 기억해 두었다가 순차적으로 명령을 수행시키기 좋음
'''

from collections import deque
import sys
sys.stdin = open("input.txt")

# 델타 탐색
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]


# 인접한 8칸에 지뢰가 몇개 있는지 체크
def check_mine(i, j):
    cnt = 0
    for k in range(8):
        ni, nj = i + di[k], j + dj[k]
        if (0 <= ni < N and 0 <= nj < N) and board[ni][nj] == '*':
            cnt += 1
    board[i][j] = cnt


# 0을 눌렀을 때 연쇄적으로 숫자 표시 체크
def zero_chain(i, j):
    Q = deque()
    Q.append([i, j])
    board[i][j] = '*'

    while Q:
        i, j = Q.popleft()

        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] != '*':
                    if board[ni][nj] == 0:
                        Q.append([ni, nj])
                    board[ni][nj] = '*'


# 클릭 개수 세기
def click_count(N, board):
    click = 0
    # 지뢰 개수 세기
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                check_mine(i, j)
    
    # 클릭 -> 숫자 연쇄 표시 
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                click += 1
                zero_chain(i, j)

    # 클릭 -> 단일 숫자 표시
    for i in range(N):
        for j in range(N):
            if board[i][j] != '*':
                click += 1
    
    return click


for tc in range(int(input())):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    print(f'#{tc+1} {click_count(N, board)}')
