for _ in range(3):
    N = int(input())
    dict_ = {}
    sum_ = 0

    for _ in range(N):
        coin, cnt = map(int, input().split())
        sum_ += coin * cnt
        dict_[coin] = cnt

    if sum_ % 2:
        print(0)
        continue

    sum_ //= 2
    dp = [True] + [False] * sum_

    result = 0
    for coin in dict_:
        for price in range(sum_, coin - 1, -1):
            if not dp[price - coin]:
                continue

            for i in range(dict_[coin]):
                if price + coin * i <= sum_:
                    dp[price + coin * i] = True
                else:
                    break

        if dp[-1]:
            result = 1
            break
    print(result)