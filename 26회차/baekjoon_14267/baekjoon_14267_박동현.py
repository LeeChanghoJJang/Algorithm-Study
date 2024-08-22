N,M = map(int,input().split())
arr = [0] + [*map(int,input().split())]

DP = [0]*(N+1)
for _ in range(M):
    i,w = map(int,input().split())
    DP[i] += w
# 내리 칭찬을 갈겨버림
for idx in range(2,N+1):
    DP[idx] += DP[arr[idx]]

print(*DP[1:])