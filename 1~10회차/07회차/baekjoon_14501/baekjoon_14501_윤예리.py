'''
dp
'''
n = int(input())
dp = [0] * (n+1)
schedule = [tuple(map(int, input().split())) for _ in range(n)]     # (기간, 금액)

for i in range(n-1, -1, -1):    # 마지막 날 부터 확인하면서
    if i + schedule[i][0] > n:  # 상담을 했을 때 날짜가 퇴사일을 넘어가면 안 함
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i+schedule[i][0]])     # 안 하는 경우랑 하는 경우 비교해서 큰 값 dp에 저장
        # dp[i+schedule[i][0]]: 마지막으로 상담한 날 금액

print(dp[0])