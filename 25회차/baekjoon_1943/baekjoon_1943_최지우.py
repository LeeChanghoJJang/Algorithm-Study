import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    coins = []
    total = 0
    for _ in range(N):
        val, n = map(int, input().split())
        total += val * n
        coins.append((val, n))
    
    if total % 2:
        print(0)
        continue
    
    target = total // 2
    dp = [0] * (target + 1)
    dp[0] = 1
    
    coins.sort()
    
    for val, n in coins:
        if val > target:
            break
        for i in range(target, val-1, -1):
            if dp[i]: continue
            for j in range(1, n+1):
                if i - val*j < 0: break
                if dp[i - val*j]:
                    dp[i] = 1
                    break
    
    print(dp[target])