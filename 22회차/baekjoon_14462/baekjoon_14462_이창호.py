def can_be_friends(a, b):
    return abs(a - b) <= 4

def maximum_crosswalks(n, left_cows, right_cows):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if can_be_friends(left_cows[i - 1], right_cows[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]

# 입력 처리
import sys
sys.stdin= open('input.txt')
input = sys.stdin.read
data = input().split()

n = int(data[0])
left_cows = [int(data[i + 1]) for i in range(n)]
right_cows = [int(data[i + 1 + n]) for i in range(n)]

# 최대 횡단보도 개수 계산 및 출력
print(maximum_crosswalks(n, left_cows, right_cows))
