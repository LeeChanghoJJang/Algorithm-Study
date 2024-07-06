N = int(input())
lv = [0]+[*map(int,input().split())]
power = [0]+[*map(int,input().split())]

day = int(input())


r = 0
dp = [0] * (day + 1)

for i in range(1, N + 1):
    r += lv[i] * power[i]
    lv[i] = min(day, lv[i])


for i in range(1, N + 1):
    while lv[i] :
        lv[i] -= 1
        for j in range(day, -1, -1):
            for k in range(i + 1, N + 1):
                if k + j - i <= day:
                    dp[k + j - i] = max(dp[k + j - i], dp[j] + (power[k] - power[i]))
print(dp[day] + r)