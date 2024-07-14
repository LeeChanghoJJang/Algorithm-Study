from collections import deque
import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

N, M = map(int,input().split())
Map = [list(input()) for _ in range(N)]
Dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N) :
    for j in range(M) :
        if Map[i][j] == 'S' : p, q = i, j ; Map[i][j] = 'E'
        elif Map[i][j] == 'H' : r, s = i, j ; Map[i][j] = 'E'

D = deque([[0, p, q]])
visit = [[[-1] * M for _ in range(N)] for _ in range(2)]
visit[0][p][q] = 0

while D :
    d, x, y = D.popleft()
    if d == 1 and x == r and y == s : exit(print(visit[d][x][y]))

    for a, b in Dir :
        nx = x+a ; ny = y+b
        if 0<=nx<N and 0<=ny<M and Map[nx][ny] != 'D' :
            if Map[nx][ny] == 'E' and visit[d][nx][ny] == -1 :
                visit[d][nx][ny] = visit[d][x][y]+1
                D.append((d, nx, ny))
            elif Map[nx][ny] == 'F' and visit[1][nx][ny] == -1 :
                visit[1][nx][ny] = visit[d][x][y]+1
                D.append((1, nx, ny))
print(-1)