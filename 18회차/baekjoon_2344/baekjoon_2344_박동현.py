import sys
input = sys.stdin.readline
# 빛을 움직일 델타
dx,dy=(0,-1),(1,0)

# 번호를 계산할 델타
dt = (1,0),(0,1)

N,M = map(int,input().split())
arr = [ [*map(int,input().split())] for _ in range(N) ]
length = N+M
ans = [0]*(2*(length)+1)

start = (0,0)
d = 0
for i in range(1,length+1):
    x,y=start
    # t : dx,dy의 인덱스로의 역할을 함
    if i <= N : t=0
    else : t=1
    # 범위를 벗어나는 순간 종료
    while 0<=x<N and 0<=y<M:
        if arr[x][y] == 1:
            # 
            t = 1-t
        x,y = x+dx[t],y+dy[t]

    if x==-1: res = 2*length-y
    elif y == M: res = length+N-x
    ans[res],ans[i]= i,res

    if i == N : d+=1
    else : start = tuple(map(sum, zip(start,dt[d])))
print(*ans[1:])