import sys
sys.stdin = open('input.txt')

dx = [1,0,-1,0]
dy = [0,1,0,-1]
# 자리를 찾기위해 달팽이 모양으로 좌표를 찾는 함수 
def finds(x,y,K):
    cnt= 1
    i=0
    x,y=0,0
    # while문 돌다가 가장 마지막에 적히는 숫자가 C*R임.
    # C*R이 K보다 작다면? 대기순서 K는 공연을 못봄
    if C*R < K:
        return 0
    while cnt < K:
        # 반시계방향으로 돎
        nx = x + dx[i%4]
        ny = y + dy[i%4]
        # 가로길이 R, 세로길이 C 이내가 아닌 경우나 방문한적이 있다면
        if nx < 0 or nx >= R or ny < 0 or ny >= C or visited[nx][ny]:
            #방향만 바꾸고 다음 차례로
            i+=1
            continue
        # 방문했음 방문처리
        visited[x][y]=1
        # 자리이동된만큼 cnt올리고, 그것을 행렬값에 저장
        arr[x][y] += cnt
        cnt+=1
        x,y =nx,ny
    return y+1,x+1

C, R = map(int,input().split())
arr =[[0] *C for _ in range(R)]
visited = [[0] *C for _ in range(R)]
K = int(input())
a= finds(0,0,K)
# 만일, 단일값(0)이면 0을 반환하고, 아니라면, 언팩해서 반환 
if type(a) != int:
    print(*a)
else:
    print(a)

