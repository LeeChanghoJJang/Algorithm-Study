T = int(input())
drow, dcol = [-1, 0, 1, 0], [0, 1, 0, -1]
block_dict = {
    1 : {0 : 2, 1 : 3, 2 : 1, 3 : 0},
    2 : {0 : 1, 1 : 3, 2 : 0, 3 : 2},
    3 : {0 : 3, 1 : 2, 2 : 0, 3 : 1},
    4 : {0 : 2, 1 : 0, 2 : 3, 3 : 1},
    5 : {0 : 2, 1 : 3, 2 : 0, 3 : 1}
    }

for tc in range(T):
    N = int(input())
    list_ = [list(map(int, input().split())) for _ in range(N)]
    wormhole_dict = {}
    max_ = 0

    for row in range(N):
        for col in range(N):
            temp = list_[row][col]

            if 6 <= temp <= 10:
                if temp in wormhole_dict:
                    wormhole_dict[temp] = {wormhole_dict[temp] : (row, col), (row, col) : wormhole_dict[temp]}
                else:
                    wormhole_dict[temp] = (row, col)

    for row in range(N):
        for col in range(N):
            if list_[row][col] != 0:
                continue

            for d in range(4):
                nrow, ncol = row, col
                score = 0

                while True:
                    nrow, ncol = nrow + drow[d], ncol + dcol[d]

                    if not (0 <= nrow < N and 0 <= ncol < N):
                        d = block_dict[5][d]
                        score += 1
                        continue

                    temp = list_[nrow][ncol]

                    if temp == -1 or (nrow, ncol) == (row, col):
                        max_ = max(max_, score)
                        break

                    if 1 <= temp <= 5:
                        score += 1
                        d = block_dict[temp][d]
                        continue

                    if 6 <= temp <= 10:
                        nrow, ncol = wormhole_dict[temp][(nrow, ncol)]

    print(f'#{tc + 1} {max_}')