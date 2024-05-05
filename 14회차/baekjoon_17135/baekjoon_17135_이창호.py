import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')

def hunt(archor):
    boards = deepcopy(board)
    visited = [[0] * N for _ in range(M)]
    cnt = 0
    for a in range(N-1,-1,-1): # 궁수가 전진 (각 행 기준)
        die =[]
        for m in archor: # 궁수들 한명씩(각 열 기준)
            queue =deque([[a,m,1]])
            while queue:
                x,y,d = queue.popleft()
                if boards[x][y]:
                    die.append([x,y])
                    if not visited[x][y]:
                        visited[x][y] =1
                        cnt +=1 # 죽이면 그다음 턴으로 넘어가야지.
                    break
                if d < D:
                    # 후보 리스트 삽입
                    for dx,dy in move:
                        nx,ny = x+ dx,y+dy
                        if 0<=nx<N and 0<= ny<M:
                            queue.append([nx,ny,d+1])
        for x,y in die:# (조건3) 모든 궁수가 동시에 공격하니 마지막에 처리
            boards[x][y] = 0

    return cnt


N,M,D =map(int,input().split())
board = [list(map(int,input().split())) for _  in range(N)]
move = [(-1,0),(0,-1),(0,1)] # 위 왼 오른
result = 0
for archor in combinations(list(range(M)),3):
    result = max(result,hunt(archor))
print(result)