import sys
input = sys.stdin.readline
N,K = map(int,input().split())
item_lst = [[0,0]]
for _ in range(N):
    W,V = map(int,input().split())
    item_lst.append([W,V])


d = [[0]*(K+1) for _ in range(N+1)]



for i in range(1, N+1):
    for j in range(1, K+1):
        w = item_lst[i][0]
        v = item_lst[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[N][K])
                
            
    
