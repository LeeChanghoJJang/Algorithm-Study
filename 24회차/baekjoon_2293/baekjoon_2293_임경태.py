# 2293 동전 1
# 동전의 종류 수 (n)와 목표 금액 (k)를 입력받음
n, k = map(int, input().strip().split())
arr = []

# 각 동전의 가치를 입력받음
for _ in range(n):
    arr.append(int(input()))

# 0부터 k까지의 금액을 만들 수 있는 방법의 수를 저장할 리스트 초기화
dp = [0 for _ in range(k + 1)]
dp[0] = 1  # 금액 0을 만드는 방법은 동전을 사용하지 않는 한 가지 방법

# 각 동전 종류를 처리
for coin in arr:
    # coin부터 k까지의 각 금액을 만드는 방법의 수를 업데이트
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

# 금액 k를 만드는 방법의 수를 출력
print(dp[k])
