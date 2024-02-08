# baekjoon_17276 배열돌리기
import sys
sys.stdin = open('input.txt')
import copy
T = int(input())

for tc in range(1,T+1):
    N,angle = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr_sum = copy.deepcopy(arr)
    angle = (angle // 45) % 8
    visited = [[0]*N for _ in range(N)]
    # 동 남 서 북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    if angle <0:
        # 남 동 북 서
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        angle=abs(angle)
    for _ in range(angle):
        i = 0  # 방향조절
        j = 0  # 한칸 안쪽으로
        x, y = 0, 0  # 초기점
        visited = [[0] * N for _ in range(N)]
        while (x,y) != (N//2, N//2):
            if visited[x][y]:
                x+=1
                y+=1
                i+=1
                j+=1
            else:
                visited[x][y]=1
                if x in [y, N-1-y, N//2] or y ==N//2 :
                    nx = x + dx[i%4] * max(abs(N//2 - x),abs(N//2 - y))
                    ny = y + dy[i%4] * max(abs(N//2 - x),abs(N//2 - y))

                    if nx < 0 +j  or nx >= N-j or ny < 0+j or ny >= N-j:
                        i += 1
                        nx = x + dx[i%4] * max(abs(N//2 - x),abs(N//2 - y))
                        ny = y + dy[i%4] * max(abs(N//2 - x),abs(N//2 - y))
                    arr_sum[nx][ny] = arr[x][y]
                    x, y= nx, ny
        arr = copy.deepcopy(arr_sum)
    for i in range(N):
        print(*arr_sum[i])
