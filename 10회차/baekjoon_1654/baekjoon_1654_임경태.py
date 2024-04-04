# 1654 랜선 자르기

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
start, end = 1, max(cables)

while start <= end:
    mid = (start + end) // 2
    cnt = sum(cable // mid for cable in cables)

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)