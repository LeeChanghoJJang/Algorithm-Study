def solution(temperature, t1, t2, a, b, onboard):
    t1 += 10
    t2 += 10
    temperature += 10
    len_ = len(onboard)
    flag = 1

    dp = [[float('inf')] * 51 for _ in range(len_)]
    dp[0][temperature] = 0

    if temperature > t2:
        flag = -1

    for i in range(1, len_):
        for j in range(51):
            temp = []

            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                if 0 <= j + flag <= 50:
                    temp.append(dp[i - 1][j + flag])

                if j == temperature:
                    temp.append(dp[i - 1][j])

                if 0 <= j - flag <= 50:
                    temp.append(dp[i - 1][j - flag] + a)

                if t1 <= j <= t2:
                    temp.append(dp[i - 1][j] + b)


                dp[i][j] = min(temp)

    answer = min(dp[len_ - 1])
    return answer