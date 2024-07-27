import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

    # N*N dp에서 해당 행렬이 나온 차례.
    # 그냥 쌩으로 곱한거랑 비교.
    
for term in range(1, N):
    for start in range(N):  # 첫행렬 : i, 끝행렬: i+term
        if start + term >= N:  # 범위를 벗어나면 무시
            break

        dp[start][start+term] = int(1e9)  # 지금 계산할 첫행렬과 끝행렬
        
        for t in range(start, start+term):
            dp[start][start+term] = min(dp[start][start+term],dp[start][t]+dp[t+1][start+term] + lst[start][0] * lst[t][1] * lst[start+term][1])

print(dp[0][N-1])