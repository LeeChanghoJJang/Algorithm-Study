import sys
sys.stdin = open('input.txt')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def finds(x,y,K):
    cnt= 1
    i=0
    x,y=0,0
    if C*R < K:
        return 0
    while cnt < K:
        nx = x + dx[i%4]
        ny = y + dy[i%4]
        if nx < 0 or nx >= R or ny < 0 or ny >= C or visited[nx][ny]:
            i+=1
            continue
        visited[x][y]=1
        arr[x][y] += cnt
        cnt+=1
        x,y =nx,ny
    return y+1,x+1

C, R = map(int,input().split())
arr =[[0] *C for _ in range(R)]
visited = [[0] *C for _ in range(R)]
K = int(input())
a= finds(0,0,K)
if type(a) != int:
    print(*a)
else:
    print(a)

