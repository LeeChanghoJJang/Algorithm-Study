import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
inf = int(1e9)
min_val = int(1e9)
for i in range(3):
    DP = [[inf] * 3 for _ in range(N)]
    DP[0][i] = arr[0][i]
    for j in range(1,N):
        DP[j][0] = arr[j][0] + min(DP[j - 1][1], DP[j - 1][2])
        DP[j][1] = arr[j][1] + min(DP[j - 1][0], DP[j - 1][2])
        DP[j][2] = arr[j][2] + min(DP[j - 1][0], DP[j - 1][1])

for i in range(N):
    for j in range(3):
        if i==0:
            DP[i % N][j] = arr[i % N][j] + min(arr[(i-1)%N][(j-1)%3],arr[(i-1)%N][(j+1)%3])
        DP[i%N][j] = arr[i%N][j] + min(DP[(i-1)%N][(j-1)%3],DP[(i-1)%N][(j+1)%3])

print(DP)
    for k in range(3):
        if i != k:
            min_val = min(min_val, DP[-1][k])
    print(DP,i)
print(min_val)
