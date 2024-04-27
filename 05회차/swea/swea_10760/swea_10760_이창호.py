import sys
sys.stdin = open('input.txt')

dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,-1,1,1,-1]

def nearby_search(arr):
    result = 0
    for x in range(N):
        for y in range(M):
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M and arr[x][y] > arr[nx][ny]:
                    cnt+=1
                if cnt>=4:
                    result +=1
                    break
    return result

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc} {nearby_search(arr)}')