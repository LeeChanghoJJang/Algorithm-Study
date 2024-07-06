def solution(temperature, t1, t2, a, b, onboard):
    k = 1000 * 100

    t1 += 10
    t2 += 10
    temperature += 10

    dp = [[k] * 51 for _ in range(len(onboard))]
    dp[0][temperature] = 0

    updown = 1
    if temperature > t2:
        updown = -1

    for i in range(1, len(onboard)):
        for j in range(51):
            arr = [k]
            if (onboard[i] == 1 and t1 <= j <=t2) or onboard[i] == 0:
                if 0 <= j + updown <= 50:
                    arr.append(dp[i-1][j+updown])
                elif j == temperature:
                    arr.append(dp[i-1][j])
                elif 0 <= j - updown <= 50:
                    arr.append(dp[i-1][j-updown] + a)
                elif t1 <= j <= t2:
                    arr.append(dp[i-1][j] + b)

                dp[i][j] = min(arr)

    answer = min(dp[len(onboard)-1])
    return answer