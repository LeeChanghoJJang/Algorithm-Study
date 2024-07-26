import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = sorted([int(input()) for _ in range(N)])

DP = [0]*(M+1)              # DP table 0 ~ M+1 원을 만드는 방법
DP[0] = 1                   # 0원을 만드는 방법은 아무것도 안쓰는 한 가지 방법이 존재

for i in arr:
    for j in range(i,M+1):
        DP[j] += DP[j-i]
print(DP[-1])