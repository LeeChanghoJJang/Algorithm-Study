N = int(input())
memo = [0] * (N+1)
memo[1] = 0

for i in range(2, N+1):
    memo[i] = memo[i-1] + 1     # memo[i]에 기본값을 다 넣어놓음
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i//3]+1)    # 3으로 나눈 경우와 1을 빼는 경우 수 비교
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i//2]+1)

print(memo[N])
