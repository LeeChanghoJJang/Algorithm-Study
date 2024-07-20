# 2281 데스노트
N, M = map(int, input().split())
name = [int(input()) for _ in range(N)]

# 가능한 최대 값으로 DP 배열 초기화
max_num = M**2 * N
DP = [max_num] * (N+1)
DP[N] = 0

# 역순으로 DP 값을 계산
for idx in range(N-1, -1, -1):
    remain = M - name[idx]

    # 현재 인덱스 이후의 책들을 확인하면서 DP 값을 갱신
    for i in range(idx+1, N+1):
        if remain >= 0:
            if i == N:
                DP[idx] = 0
                break

            # 현재 책을 포함한 페이지의 여백 제곱을 계산하고 DP 값을 갱신
            DP[idx] = min(DP[idx], remain**2 + DP[i])
            remain -= name[i] + 1

print(DP[0])
