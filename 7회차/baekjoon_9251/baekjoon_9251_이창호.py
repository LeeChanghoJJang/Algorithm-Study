import sys
sys.stdin = open('input.txt')
str1, str2 = input(), input()
N = len(str1)
M = len(str2)
DP = [[0] * (M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        if str1[i] == str2[j]:
            DP[i+1][j+1] = DP[i][j]+1
        else:
            DP[i+1][j+1] = max(DP[i+1][j],DP[i][j+1])
print(DP[-1][-1])