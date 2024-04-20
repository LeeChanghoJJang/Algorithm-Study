N = int(input())
dp = [[] for _ in range(N+1)]
# 하노이 탑 1일때 1 -> 3 이동
dp[1].append([1, 3])

# 2번부터 N까지 높이가 i일 때의 이동은
# i-1번째 이동을 2 <-> 3 위치만 바꿔서 그대로 진행
# => 1 -> 3
# => 1 <-> 2 바꿔서 그대로 진행한 거랑 같음

for i in range(2, N+1):
    for a, b in dp[i-1]:
        if a+b == 5:
            a, b = b, a
        else:
            if a != 1:
                a = 5 - a
            if b != 1:
                b = 5 - b
        dp[i].append([a, b])

    dp[i].append([1, 3])

    for a, b in dp[i-1]:
        if a+b == 3:
            a, b = b, a
        else:
            if a != 3:
                a = 3 - a
            if b != 3:
                b = 3 - b
        dp[i].append([a, b])

print(len(dp[N]))
for i in dp[N]:
    print(*i)
