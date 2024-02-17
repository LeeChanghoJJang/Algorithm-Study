T = int(input())
for _ in range(T):
    n = int(input())
    memo = [1] * 11     # n < 11
    memo[1] = 1     # [1]
    memo[2] = 2     # [1, 1], [2]
    for i in range(3, 11):      # i까지 해도 되는데 숫자가 작기도 하고 혹시 모를 경우를 대비해 11까지 그냥 다 했음
        memo[i] = memo[i-1]+memo[i-2]+memo[i-3]     # 규칙: 이전 세 개의 경우를 합한다.
    print(memo[n])

