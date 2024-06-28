from collections import deque
import sys
input = sys.stdin.readline

# 원숭이 무빙
dr = (1,0),(0,1),(-1,0),(0,-1)
# 말 무빙
hr = (2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)


def BFS():
    visit = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    q = deque([(0,0,0)])
    visit[0][0][0] = 1

    def delta(i,j,k,move,ishorse):
        for dx,dy in move:
            di,dj = i+dx,j+dy
            if 0<=di<N and 0<=dj<M and not visit[di][dj][k+ishorse] and not arr[di][dj]:
                visit[di][dj][k+ishorse] = visit[i][j][k]+1
                q.append((di,dj,k+ishorse))

    while q:
        i,j,k = q.popleft()

        if i==N-1 and j==M-1:
            return print(visit[i][j][k]-1)
        
        delta(i,j,k,dr,False)
        if K>k:
            delta(i,j,k,hr,True)

    return print(-1)


K = int(input())
M,N = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

BFS()