import sys
sys.stdin = open('input.txt')

# 주어진 좌표에서 숫자 n이 유효한지 확인하는 함수
def is_possible(x, y, n):
    # 가로, 세로, 3x3 박스에 중복된 숫자가 있는지 확인
    for i in range(9):
        if arr[x][i] == n:  # 같은 행에 이미 n이 있는 경우
            return False
        if arr[i][y] == n:  # 같은 열에 이미 n이 있는 경우
            return False

    # 3x3 박스에 이미 n이 있는 경우
    ny = (y // 3) * 3
    nx = (x // 3) * 3
    for dx in range(3):
        for dy in range(3):
            if arr[nx + dx][ny + dy] == n:
                return False
    return True

# 백트래킹을 이용한 DFS 함수
def dfs(idx):
    # 0인 칸이 없는 경우, 즉 모든 칸이 채워진 경우에는 결과 출력 후 프로그램 종료
    if idx == len(zero):
        for row in arr:
            print(*row, sep='')
        exit(0)

    # 0인 칸에 대해 가능한 숫자를 넣어보고 DFS 호출하여 퍼즐 완성
    x, y  = zero[idx]  # 0인 칸의 좌표
    for i in range(1, 10):  # 1부터 9까지 가능한 숫자 시도
        if is_possible(x, y, i):  # 숫자 i가 유효한 경우
            arr[x][y] = i  # 해당 위치에 숫자 i를 넣음
            dfs(idx + 1)  # 다음 0인 칸으로 진행
            arr[x][y] = 0  # 백트래킹: 이전 상태로 돌아가기 위해 다시 0으로 초기화

N = 9
arr = []
# 스도쿠 퍼즐 입력 받기
for _ in range(N):
    row = list(input())
    row = list(map(int, row))  # 문자열로 입력 받은 숫자를 정수로 변환
    arr.append(row)

zero = []  # 0인 칸의 좌표를 저장할 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:  # 0인 칸인 경우
            zero.append((i, j))  # 좌표를 zero 리스트에 추가

dfs(0)  # DFS 탐색 시작
