def stars(i,j,now):
    if now == 3:
        ans[i+1][j-1] = ans[i+1][j+1] = ans[i][j] = "*"
        for k in range(-2,3):
            ans[i+2][j-k] = "*"
        return
    
    nxt = now // 2
    stars(i,j,nxt)
    stars(i+nxt, j+nxt, nxt)
    stars(i+nxt, j-nxt, nxt)

N = int(input())

ans = [[" "]*2*N for _ in range(N)]
stars(0,N-1,N)
for a in ans:
    print(*a, sep="")