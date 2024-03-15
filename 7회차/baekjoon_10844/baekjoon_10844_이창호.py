import sys
sys.stdin = open('input.txt')

N= int(input())
DP =  [[0] +[1]* 9] + [[0] * 10 for _ in range(N-1)]
for i in range(1,N):
    for j in range(10):
        if j ==0:
            DP[i][0] = DP[i-1][1]
        elif j==9:
            DP[i][9] = DP[i-1][8]
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]
print(DP)
print(sum(DP[N-1])%int(1e9))