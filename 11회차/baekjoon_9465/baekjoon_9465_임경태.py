# 9465 스티커

for tc in range(int(input())):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]
    DP = [[score[i][0]] * n for i in range(2)]

    if n > 1:  # 열이 2개 이상인 경우
        for y in range(2):
            DP[y][1] = DP[1-y][0] + score[y][1]

    if n > 2:  # 열이 3개 이상인 경우
        for x in range(2, n):
            for y in range(2):
                # 이전 열의 반대 행, 두 열 전 같은 행, 두 열 전 반대 행 중 최대값 선택
                DP[y][x] = max(DP[1-y][x-1], DP[y][x-2], DP[1-y][x-2]) + score[y][x]

    print(max(DP[0][-1], DP[1][-1]))