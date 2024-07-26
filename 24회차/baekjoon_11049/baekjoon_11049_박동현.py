# 항상 순서대로 곱할 수 있는 크기만 입력으로 주어진다.
# DP[시작][끝] <> DP[시작][중간] + DP[중간][끝] + 추가값

import sys
input = sys.stdin.readline


N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]
DP = [[0]*N for _ in range(N)]

for e in range(1,N):
    for s in range(N):
        if e+s>=N: break
        DP[s][e+s] = float('inf')
        for t in range(s,s+e):
            # 플루이드-워셜 하듯이
            DP[s][e+s] = min(DP[s][e+s], DP[s][t] + DP[t+1][e+s] + arr[s][0] * arr[t][1] * arr[e+s][1])
print(DP[0][-1])