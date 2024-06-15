import sys
sys.stdin = open('input.txt')

# 방향에 따른 행과 열의 변화량 정의
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

# 빛을 쏘는 함수 정의
def shoot(row, col, dir):
    nrow, ncol = row, col
    ndir = dir

    # 무한 루프를 통해 빛의 경로 추적
    while True:
        # 거울을 만나면 방향 전환
        if box[nrow][ncol] == 1:
            if ndir == 0:
                ndir = 1
            elif ndir == 1:
                ndir = 0
            elif ndir == 2:
                ndir = 3
            else:
                ndir = 2
        # 위치 업데이트
        nrow += drow[ndir]
        ncol += dcol[ndir]

        # 경계를 벗어나면 종료
        if not (1 <= nrow < N + 1 and 1 <= ncol < M + 1):
            break
    # 종료 지점 반환
    return hole[nrow][ncol]


# 입력 처리
N, M = map(int, input().split())
hole = [[0] * (M + 2) for _ in range(N + 2)]
box = [[0] * (M + 2) for _ in range(N + 2)]

cnt = 1
for row in range(N):
    hole[row + 1][0] = cnt
    cnt += 1
for col in range(M):
    hole[N + 1][col + 1] = cnt
    cnt += 1
for row in range(N - 1, -1, -1):
    hole[row + 1][M + 1] = cnt
    cnt += 1
for col in range(M - 1, -1, -1):
    hole[0][col + 1] = cnt
    cnt += 1

# 박스(거울의 위치) 입력 받기
for row in range(N):
    line = list(map(int, input().split()))

    for col in range(M):
        box[row + 1][col + 1] = line[col]

# 각 시작점에서 빛을 쏘고 결과 출력
for row in range(1, N + 1):
    print(shoot(row, 1, 1), end=" ")
for col in range(1, M + 1):
    print(shoot(N, col, 0), end=" ")
for row in range(N, 0, -1):
    print(shoot(row, M, 3), end=" ")
for col in range(M, 0, -1):
    print(shoot(1, col, 2), end=" ")