# 11049 행렬 곱셈 순서
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = [a for a, _ in arr] + [arr[-1][1]]

# DP 테이블 초기화
DP = [[0] * n for _ in range(n)]

# DP 계산
for step in range(1, n):
    for loc in range(n - step):
        end = loc + step
        mul = arr[loc] * arr[end + 1]
        
        # 최소 곱셈 연산 횟수 계산
        minimum = min(yk + xk + sz * mul for yk, xk, sz in zip(DP[loc][loc:end], DP[end][loc + 1:end + 1], arr[loc + 1:end + 1]))
        
        DP[loc][end] = DP[end][loc] = minimum

# 결과 출력
print(DP[0][-1])
