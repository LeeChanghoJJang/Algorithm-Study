import sys
input = sys.stdin.readline
N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
result = []

direction = [1,0,3,2]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def out_num(x,y):
    if x == -1:
        return 2*N + 2*M -y
    elif y == -1:
        return x+1
    elif x == N:
        return N + y + 1
    else:
        return 2*N + M - x
    
def search(start,dir):
    x,y = start
    while 0 <= x < N and 0 <= y < M:
        if matrix[x][y] == 1:
            dir = direction[dir]
        x += dx[dir]
        y += dy[dir]
    return str(out_num(x,y))

for i in range(N):
    result.append(search([i,0],1))
for i in range(M):
    result.append(search([N-1,i],0))
for i in range(N-1,-1,-1):
    result.append(search([i,M-1],3))
for i in range(M-1,-1,-1):
    result.append(search([0,i],2))
print(*result)

