# 10844 쉬운 계단 수 (실버1)

N = int(input())
DP = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
DP2 = DP[:]

# 일의 자리를 인덱스로하여 진행
for _ in range(N-1):
    DP2[0] = DP[1]; DP2[9] = DP[8]
    for i in range(1, 9):
        DP2[i] = DP[i-1] + DP[i+1]
    DP = DP2[:]

print(sum(DP)%(1000000000))


# DFS : 시간 초과 날듯
'''
def stair(i, now):
    if i == N-1:
        global ans; ans += 1
        return
    edge = now % 10
    if edge < 9: stair(i+1, now*10+edge+1)
    if edge > 0: stair(i+1, now*10+edge-1)

N, ans = int(input()), 0
for i in range(1, 10): stair(0, i)
print(ans)
'''