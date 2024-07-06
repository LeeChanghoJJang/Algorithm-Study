from collections import deque
from itertools import permutations


N = int(input())

SCV = [0,0,0]
scv = [*map(int,input().split())]
for i in range(N) :
    SCV[i] += scv[i]
    
# DP 형태로 visit 테이블을 구성
visit = [[[0] * 61 for _ in range(61)] for _ in range(61)]

# BFS
q = deque([(SCV[0],SCV[1],SCV[2])])
while q : 
    a,b,c = q.popleft()

    if a==b==c==0:
        exit(print(visit[a][b][c]))
    
    for x,y,z in permutations([1,3,9],3):
        i,j,k = max(a-x,0), max(b-y,0), max(c-z,0)

        if not visit[i][j][k]:
            visit[i][j][k] = visit[a][b][c] +1
            q.append((i,j,k))
