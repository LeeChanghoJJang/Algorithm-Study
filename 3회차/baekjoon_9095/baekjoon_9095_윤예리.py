T = int(input())
for _ in range(T):
    n = int(input())
    memo = [1] * 11
    memo[1] = 1
    memo[2] = 2
    for i in range(3, 11):
        memo[i] = memo[i-1]+memo[i-2]+memo[i-3]
    print(memo[n])

