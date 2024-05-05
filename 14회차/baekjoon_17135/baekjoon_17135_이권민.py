# 공격범위 삼각형 모양으로 커짐
# 가장 왼쪽에 있는 애부터 공격. 범위만 채우기엔 상대 위치도 중요
# 거리는 루트 안씌운거.제일 가까운 놈부터. 제일 많은 곳에? 제일 많은 곳이어도 걔들 사이 간격.

def kill(arr_loc):
    mat = deepcopy(matrix)
    visited = [[0]*M for _ in range(N)]
    kill_score = 0
    for i in range(N-1,-1,-1):
        die = []
        for j in arr_loc:
            deq = deque([[i,j,1]])
            while deq:
                r,c,d = deq.popleft()
                if mat[r][c]:
                    die.append([r,c])
                    if not visited[r][c]:
                        visited[r][c] = 1
                        kill_score+= 1
                    break
                # 한턴에 하나. 가장 가까운 애부터. 그다음은 가장 왼쪽. 못잡았으면 아래로. 
                
                
                if d < D:
                    for dc,dr in move:
                        lc,lr = c+dc, r+dr
                        if 0 <= lr < N and 0<= lc < M:
                            deq.append([lr,lc,d+1])
        for y, x in die:# (조건3) 모든 궁수가 동시에 공격하니 마지막에 처리
            mat[y][x] = 0
            # 같은 적 공격할수도. 

    return kill_score
                        
from copy import deepcopy
from collections import deque
N,M,D = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
move = [[-1,0],[0,-1],[1,0]]  # 궁수가 이동. 적을 모두 이동시키는 것보다 궁수만 이동하는게
max_n = 0

for i in range(1<<M):
    arr_loc = []
    cnt = 0
    for j in range(M):
        if i & (1<<j):
            arr_loc.append(j)
            cnt += 1
    if cnt == 3:
        max_n = max(max_n,kill(arr_loc))
print(max_n)