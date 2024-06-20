# 21609 상어 중학교

def DFS(i, j, C):
    stack = [[i, j]]
    n_cnt, r_cnt = 1, 0
    n_cube, r_cube = [[i, j]], []

    while stack:
        i, j = stack.pop()
        for di, dj in go:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0:
                # 특정 색 블록
                if grid[ni][nj] == C:
                    visit[ni][nj] = 1
                    stack.append([ni, nj])
                    n_cube.append([ni, nj])
                    n_cnt += 1

                # 무지개 블록
                if grid[ni][nj] == 0:
                    visit[ni][nj] = 1
                    stack.append([ni, nj])
                    r_cube.append([ni, nj])
                    n_cnt += 1; r_cnt += 1

    for i, j in r_cube: visit[i][j] = 0

    return n_cnt, r_cnt, n_cube + r_cube

def gravity(arr):
    # 밑에서 부터 탐색
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if 0 <= arr[i][j] <= M:
                temp = arr[i][j]; arr[i][j] = -2; ni = i
                # 바닥이나 검은 블록에 닿을 때까지 낙하
                while ni < N - 1 and arr[ni + 1][j] == -2: ni += 1
                arr[ni][j] = temp

def turn(arr):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[j][N - i - 1]
    return new_arr

go = ((1, 0), (0, 1), (0, -1), (-1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    visit = [[0] * N for _ in range(N)]
    groups = []

    # 블록 그룹 탐색
    for i in range(N):
        for j in range(N):
            if 0 < grid[i][j] and visit[i][j] == 0:
                visit[i][j] = 1
                group = DFS(i, j, grid[i][j])
                if group[0] > 1: groups.append(group)

    # 블록 그룹이 존재하지 않으면 종료
    if not groups: exit(print(ans))
    # 조건에 맞는 블록 찾기 : 블록 개수 - 무지개 개수 - 행과 열
    B, R, cubes = sorted(groups, reverse=True)[0]

    # 블록 제거 - 점수 획득 - 중력 - 회전 - 중력
    for i, j in cubes: grid[i][j] = -2
    ans += B**2
    gravity(grid)
    grid = turn(grid)
    gravity(grid)