# 2344 거울
N, M = map(int, input().split())
grid = [input().split() for _ in range(N)]
change_dir = [1, 0, 3, 2]  # 입력(출력) : 우(상) - 상(좌) - 좌(하) - 하(우)

for hole in range(1, 2*(N+M)+1):
    # 시작
    if 0 < hole <= N: i, j, dir = hole-1, 0, 0
    elif N < hole <= M+N: i, j, dir = N-1, hole-N-1, 1
    elif M+N < hole <= 2*N+M: i, j, dir = 2*N+M-hole, M-1, 2
    elif 2*N+M < hole <= 2*(M+N): i, j, dir = 0, 2*(N+M)-hole, 3

    while 0<=i<N and 0<=j<M:

        # 거울 -> 방향 전환
        if grid[i][j] == '1':
            dir = change_dir[dir]

        # 진행
        if dir == 0: j += 1
        elif dir == 1: i -= 1
        elif dir == 2: j -= 1
        elif dir == 3: i += 1

    # 종료
    if j < 0: exit_hole = i+1
    elif i == N: exit_hole = j+N+1
    elif j == M: exit_hole = 2*N+M-i
    elif i < 0: exit_hole = 2*(N+M)-j

    print(exit_hole, end=' ')