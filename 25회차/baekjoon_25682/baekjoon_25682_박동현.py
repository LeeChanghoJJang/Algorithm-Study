N,M,K = map(int,input().split())
arr = [list(input()) for _ in range(N)]

res = [[0] * (M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        # 누적합공식
        tmp = res[i-1][j] + res[i][j-1] - res[i-1][j-1]
        if (i+j)%2==0:
            if arr[i-1][j-1] == "B":
                res[i][j] = tmp
            else:
                res[i][j] = tmp+1
        else:
            if arr[i-1][j-1] == "W":
                res[i][j] = tmp
            else:
                res[i][j] = tmp+1

max_v = -float('inf')
min_v = float('inf')

for i in range(K,N+1):
    for j in range(K,M+1):
        max_v = max(res[i][j] - res[i-K][j] - res[i][j-K] + res[i-K][j-K], max_v)
        min_v = min(res[i][j] - res[i-K][j] - res[i][j-K] + res[i-K][j-K], min_v)

print(min(min_v,max_v, K*K - min_v, K*K - max_v))