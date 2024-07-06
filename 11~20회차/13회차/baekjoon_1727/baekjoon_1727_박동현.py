import sys
input = sys.stdin.readline


N,M = map(int, input().split())
boys = sorted([*map(int, input().split())])
girls = sorted([*map(int, input().split())])

# 무조건 M>N , g>b 순으로 저장 
if N > M: 
    boys, girls = girls, boys
    N, M = M, N

# DP 2차원으로 설정
DP = [ [0] * M for _ in range(N) ]
DP[0][0] = abs(boys[0] - girls[0])

# 초기값 설정
for j in range(1, M-N+1):
    DP[0][j] = min(abs(boys[0] - girls[j]), DP[0][j - 1])

# 순회하면서
for i in range(1, N):
    for j in range(i, M-N+i+1):
        # 
        if i == j:
            DP[i][j] = DP[i - 1][j - 1] + abs(boys[i] - girls[j])
        else:
            DP[i][j] = min(DP[i - 1][j - 1] + abs(boys[i] - girls[j]), DP[i][j - 1])
print(DP[N - 1][M - 1])