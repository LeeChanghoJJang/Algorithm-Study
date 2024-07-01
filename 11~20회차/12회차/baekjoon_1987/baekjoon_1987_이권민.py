def BT(r,c,cnt):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt
    for i in range(4):
        lr = dr[i]+r
        lc = dc[i]+c
        if 0 <= lr < R and 0 <= lc < C and visited[ord(alpha_mrx[lr][lc])-65] == 0:
            visited[ord(alpha_mrx[lr][lc])-65] = 1
            BT(lr,lc,cnt+1)
            visited[ord(alpha_mrx[lr][lc])-65] = 0
        
        
R,C = map(int,input().split())
alpha_mrx = []
dr = [1,0,-1,0]
dc = [0,1,0,-1]
max_cnt = 0
for _ in range(R):
    alpha_mrx.append(input())
visited = [0]*26
visited[ord(alpha_mrx[0][0])-65] = 1
BT(0,0,1)
print(max_cnt)

# 시간 줄이기.
