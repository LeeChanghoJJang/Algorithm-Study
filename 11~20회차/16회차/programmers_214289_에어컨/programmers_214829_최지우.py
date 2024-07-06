def solution(temperature, t1, t2, a, b, onboard):
    temp = t1 - (temperature - t2) if temperature > t2 else temperature
    
    t1 -= temp
    t2 -= temp
    temp = 0

    leng = len(onboard)

    dp = [[1e9] * (t2 + 2) for _ in range(leng)]
    dp[0][0] = 0

    for i in range(1, leng):
        for j in range(t2 + 2):
            if onboard[i] == 1 and (j < t1 or j > t2):
                continue

            min_cost = 1e9

            if j == 0:
                min_cost = min(min_cost, dp[i-1][j])
                if j + 1 <= t2 + 1:
                    min_cost = min(min_cost, dp[i-1][j+1])

            else:
                min_cost = min(min_cost, dp[i-1][j-1] + a)
                min_cost = min(min_cost, dp[i-1][j] + b)

                if j + 1 <= t2 + 1:
                    min_cost = min(min_cost, dp[i-1][j+1])

            dp[i][j] = min_cost

    result = min(dp[leng-1][j] for j in range(t2 + 2))
    return result
