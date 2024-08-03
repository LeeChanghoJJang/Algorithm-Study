for _ in range(3):
    N = int(input())

    coins = dict()

    total = 0
    for _ in range(N):
        a,b = map(int,input().split())
        coins[a]=b
        total += a*b
    if total&1:print(0); continue
    total //= 2
    DP = [0] * (total+1)
    DP[0] = 1
    for coin in coins:
        for money in range(total, coin-1,-1):
            if DP[money-coin]:
                for j in range(coins[coin]):
                    if money + coin*j <= total:
                        DP[money + coin*j] = 1
    print(DP[total])