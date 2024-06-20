n = int(input())
# 행은 집, 열은 색
arr = [list(map(int, input().split())) for _ in range(n)]

# rgb 나누어서 최소비용 계산
memo = [[0] * 3 for _ in range(n)]

for i in range(n):
    memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + arr[i][0]    # r
    memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + arr[i][1]    # g
    memo[i][2] = min(memo[i-1][0], memo[i-1][1]) + arr[i][2]    # b

# 최종 작은 수
print(min(memo[n-1]))

# 일차원으로 바꿔서 해볼 예정