import sys
input = sys.stdin.readline

N = int(input())
lv_list = list(map(int, input().split()))
str_list = list(map(int, input().split()))
D = int(input())
dp = [0] * (D + 1)
result = 0

for i in range(1, N + 1):
    result += lv_list[i - 1] * str_list[i - 1]
    lv_list[i - 1] = min(D, lv_list[i - 1])

for i in range(1, N + 1):
    for _ in range(lv_list[i - 1]):
        for j in range(D, -1, -1):
            for k in range(i + 1, N + 1):
                if k + j - i <= D:
                    dp[k + j - i] = max(dp[k + j - i], dp[j] + str_list[k - 1] - str_list[i - 1])

print(dp[D] + result)