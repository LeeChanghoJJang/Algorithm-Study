import sys
input = sys.stdin.readline

## DP를 세가지 값만 가진 튜플로 만들고, 한줄 받을때마다 계속 갱신

t = int(input())
arr = list(map(int,input().split()))

max_DP = arr[:]
min_DP = arr[:]

for _ in range(t-1):
    arr = list(map(int,input().split()))
    max_DP = (arr[0] + max(max_DP[0],max_DP[1]), arr[1] + max(max_DP[0],max_DP[1],max_DP[2]), arr[2] + max(max_DP[1],max_DP[2]))
    min_DP = (arr[0] + min(min_DP[0],min_DP[1]), arr[1] + min(min_DP[0],min_DP[1],min_DP[2]), arr[2] + min(min_DP[1],min_DP[2]))

print(max(max_DP), min(min_DP))