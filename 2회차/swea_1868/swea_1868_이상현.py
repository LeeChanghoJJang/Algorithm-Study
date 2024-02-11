# SWEA 1868번 파핑파핑 지뢰찾기

# row, col을 클릭했을 때 연쇄적으로 주변칸을 확인하는 함수
def dfs(row, col, temp):
    # 확인했다는 표시를 나타내기 위해 임의의 다른 문자열로 저장
    temp[row][col] = ''

    for i in range(8):
        nrow, ncol = row + drow[i], col + dcol[i]

        if not (0 <= nrow < N and 0 <= ncol < N):
            continue

        # safe는 근처에 지뢰가 없으면 True, 있으면 False의 값을 가짐
        safe = all(temp[nrow + drow[i]][ncol + dcol[i]] != '*' for i in range(8)
                   if 0 <= nrow + drow[i] < N and 0 <= ncol + dcol[i] < N)

        # 만약 새로운 칸에 지뢰가 없고 그 새로운 칸의 주변에 지뢰가 없다면
        # 다시 그 새로운 칸을 기준으로 dfs함수를 호출
        if temp[nrow][ncol] == '.' and safe:
            dfs(nrow, ncol, temp)
        
        # 만약 새로운 칸 주변에 지뢰가 있다면 dfs함수를 호출하지 않고
        # 확인했다는 표시만 해줌
        else:
            temp[nrow][ncol] = ''

T = int(input())
# 근처에 지뢰가 있는지 확인할 때 델타를 이용하기 위해 미리 drow, dcol 선언
drow = (-1, -1, 0, 1, 1, 1, 0, -1)
dcol = (0, 1, 1, 1, 0, -1, -1, -1)

for tc in range(T):
    N = int(input())
    list_ = [list(input()) for _ in range(N)]

    cnt = 0

    for row in range(N):
        for col in range(N):
            # safe는 근처에 지뢰가 없으면 True, 있으면 False의 값을 가짐
            safe = all(list_[row + drow[i]][col + dcol[i]] != '*' for i in range(8)
                       if 0 <= row + drow[i] < N and 0 <= col + dcol[i] < N)

            # 만약 현재 칸이 지뢰가 아니고 근처에 지뢰가 없으면 (최소한의 클릭을 해야함)
            if list_[row][col] == '.' and safe:

                # 클릭 += 1을 해주고, 주변 칸도 탐색하기 위해 dfs함수를 호출함
                cnt += 1
                dfs(row, col, list_)

    # 만약 주변이 지뢰로 둘러싸이는 등 확인하지 못한 칸이 남아있으면 클릭 += 1
    for row in range(N):
        for col in range(N):
            if list_[row][col] == '.':
                cnt += 1

    print(f'#{tc + 1} {cnt}')