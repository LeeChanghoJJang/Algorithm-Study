N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 배열의 누적 합 계산
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

# 각 부분 배열에 대한 합 계산
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    print(total)

# 시간 초과
# for m in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     total = 0
#     for i in range(x1-1, x2):
#         for j in range(y1-1, y2):
#             total += arr[i][j]
#     print(total)
