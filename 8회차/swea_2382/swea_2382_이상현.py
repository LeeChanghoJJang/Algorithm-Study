def next_():
    for row in range(N):
        for col in range(N):
            if not list_[row][col]:
                continue

            temp = list_[row][col][0]

            if temp[2]:
                continue

            nrow, ncol = row + drow[temp[1]], col + dcol[temp[1]]

            if nrow in [0, N - 1] or ncol in [0, N - 1]:
                list_[nrow][ncol].append([temp[0] // 2, change_d[temp[1]], 1])
            else:
                list_[nrow][ncol].append([temp[0], temp[1], 1])

            list_[row][col].pop(0)

    for row in range(N):
        for col in range(N):
            for elem in list_[row][col]:
                elem[2] = 0

            if len(list_[row][col]) >= 2:
                max_ = max(list_[row][col], key=lambda x: x[0])[:]
                temp1 = 0

                for elem in list_[row][col]:
                    temp1 += elem[0]

                list_[row][col] = [[temp1, max_[1], 0]]


T = int(input())
drow, dcol = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
change_d = {1: 2, 2: 1, 3: 4, 4: 3}

for tc in range(T):
    N, M, K = map(int, input().split())
    list_ = [[[] for _ in range(N)] for _ in range(N)]
    result = 0

    for _ in range(K):
        row, col, num, d = map(int, input().split())
        list_[row][col].append([num, d, 0])

    [next_() for _ in range(M)]

    for row in range(N):
        for col in range(N):
            if list_[row][col]:
                result += list_[row][col][0][0]

    print(f'#{tc + 1} {result}')