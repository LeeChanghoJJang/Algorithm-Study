import sys
sys.stdin = open('input.txt')

num_dict = {}
N, M = map(int,input().split())
num_dict = {i:0 for i in range(2,2*(N+M)+2)}
mirrors = []
mirrors.append([0] * (M+2))
for i in range(N):
    mirrors.append([0] + list(map(int,input().split())) + [0])
mirrors.append([0] * (M+2))
# start 방향
start = {1:(0,1),2:(-1,0),3:(0,-1),4:(1,0)}
dr = [(0,1),(-1,0),(0,-1),(1,0)]
for i in range(2,2*(N+M)+2):
    if i <= N+1:
        mirrors[i-1][0] = i
        num_dict[i] = (i-1,0,1)
    elif N+1 < i <= N+M+1:
        mirrors[N+1][i-N-1] = i
        num_dict[i] = (N+1, i-N-1,2)
    elif N+M+1 < i <= 2*N+M+1:
        mirrors[2*N+M+1 - i+1][M+1] = i
        num_dict[i] = (2*N+M+1 - i+1, M+1,3)
    elif 2*N+M+1 < i:
        mirrors[0][2*(N+M)+1 - i+1] = i
        num_dict[i] = (0, 2*(N+M)+1 - i+1,4)

result = []
i = 2
while i < 2*(N+M)+2:
    x, y, way = num_dict[i]
    while 1:
        nx = x + start[way][0]
        ny = y + start[way][1]
        if 0<=nx<N+2 and 0<=ny<M+2:
            if mirrors[nx][ny]==0:
                x = nx;y = ny;
            elif mirrors[nx][ny]==1:
                # (0,1) - > (-1,0) / (1,0) -> (0,-1) / (-1,0) -> (0,1) / (0,-1) -> (1,0)
                if way <=2:way = 3-way
                else: way = 7-way
                x = nx;y = ny;

            elif mirrors[nx][ny] >=2:
                result.append(mirrors[nx][ny]-1)
                i+=1
                break
print(*result)