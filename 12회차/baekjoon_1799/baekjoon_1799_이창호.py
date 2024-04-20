import sys
import copy
input =sys.stdin.readline

# 대각선 방향 정의
dr = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# 색깔에 따라 보드의 색을 변환하는 함수
def exceptcolor(arr, color):
    for i in range(N):
        for j in range(N):
            if color == 'white':
                if (i + j) % 2 == 0:  # 흰색 영역에 있는 칸을 0으로 설정
                    arr[i][j] = 0
            if color == 'black':
                if (i + j) % 2 != 0:  # 검은색 영역에 있는 칸을 0으로 설정
                    arr[i][j] = 0

# 해당 위치에 말을 놓을 수 있는지 확인하는 함수
def is_possible(x, y, arr):
    for i in range(4):
        dx, dy = dr[i]
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == -1:  # 해당 방향으로 퀸이 있으면 놓을 수 없음
                return False
            nx += dx;ny += dy
    return True

# 백트래킹을 이용한 재귀적 탐색 함수
def back(x, y, arr, cnt):
    global max_cnt

    if x >= N:
        max_cnt = max(cnt, max_cnt)  # 최대 퀸의 개수 업데이트
        return

    if y >= N:
        back(x + 1, 0, arr, cnt)
        return

    if arr[x][y] == 1 and is_possible(x, y, arr):
        arr[x][y] = -1  # 퀸을 놓은 곳을 -1로 표시
        back(x, y + 1, arr, cnt + 1)  # 다음 열로 이동하여 탐색 계속
        arr[x][y] = 1  # 백트래킹

    back(x, y + 1, arr, cnt)  # 해당 칸에 퀸을 놓지 않고 다음 칸으로 이동하여 탐색

# 보드의 크기 입력
N = int(input())

# 보드 상태 입력
board = [list(map(int, input().split())) for i in range(N)]

# 대각선 방향에 퀸이 없는지를 확인하기 위한 3차원 배열 초기화
diagonal = [[[False] * 4 for _ in range(N)] for _ in range(N)]

result = 0  # 결과값 초기화

# 흰색과 검은색 영역에 대해 각각 탐색
for board_ in [copy.deepcopy(board), copy.deepcopy(board)]:
    max_cnt = 0  # 각 색깔별 최대 퀸의 개수 초기화
    back(0, 0, board_, 0)  # 백트래킹을 이용한 탐색 시작
    result += max_cnt  # 최대 퀸의 개수를 결과값에 더함

# 결과 출력
print(result)
