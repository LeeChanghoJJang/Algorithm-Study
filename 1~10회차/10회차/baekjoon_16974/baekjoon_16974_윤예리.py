def check(n, x):
    if n == 0:
        if x == 0:
            return 0
        elif x == 1:
            return 1
    elif x == 1:
        return 0

    # x가 중간 패티 보다 작음
    elif x <= 1 + h[n-1]:
        return check(n-1, x-1)

    # x가 중간 패티임
    elif x == 1 + h[n-1]+1:
        return p[n-1] + 1

    # x가 중간 패티 위치보다 크고 전채 재료수보다 작음
    elif x <= 1 + h[n-1] + 1 + h[n-1]:
        return p[n-1] + 1 + check(n-1, x-(1 + h[n-1] + 1))

    # x가 마지막임
    else:
        return p[n-1] + 1 + p[n-1]

n, x = map(int, input().split())

h = [1] * (n+1)
p = [1] * (n+1)

for i in range(1, n+1):
    h[i] = 1 + h[i-1] + 1 + h[i-1] + 1
    p[i] = p[i-1] + 1 + p[i-1]

print(check(n, x))


# 메모리 초과
# dp 싫어!!!!
# n, x = map(int, input().split())
#
# dp = []
# dp.append('P')
#
# for i in range(1, n+1):
#     dp.append('B'+str(dp[i-1])+'P'+str(dp[i-1])+'B')
# print(dp[n][:x].count('P'))