# 1727 커플 만들기
# 구해야 하는 것 : 성격의 차이의 합의 최솟값

import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

if a > b:
    a, b = b, a
    A, B = B, A

# 성격의 차 저장하는 배열
DP = [[0] * (b+1) for _ in range(a+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        DP[i][j] = DP[i-1][j-1] + abs(A[i-1]-B[j-1])
        if i == j: continue
        DP[i][j] = min(DP[i][j], DP[i][j-1])
        
print(DP[a][b])