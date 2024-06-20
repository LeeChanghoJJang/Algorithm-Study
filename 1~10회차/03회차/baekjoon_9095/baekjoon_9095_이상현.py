# 백준 9095번 1, 2, 3 더하기

# dp를 이용한 접근
dp = [0, 1, 2, 4] + [0] * 7

for i in range(4, 11):

    # 각 수의 합을 나타낼 때 가장 오른쪽의 수는 1, 2, 3 셋 중 하나임
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

T = int(input())

for tc in range(T):
    print(dp[int(input())])