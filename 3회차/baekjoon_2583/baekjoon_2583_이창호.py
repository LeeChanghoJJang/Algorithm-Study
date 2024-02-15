# baekjoon_2583 영역 구하기
import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def paint(x1,y1,x2,y2,graph):
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] =1
    return graph

def BFS(x,y):
    area = 1
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        graph[x][y]=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and graph[nx][ny]==0:
                graph[nx][ny]=1
                queue.append([nx,ny])
                area += 1
    return area

# BFS 활용문제 인듯
M,N,K = map(int,input().split())
graph = [[0] * N for _ in range(M)]

for _ in range(K):
    y1,x1,y2,x2 = map(int,input().split())
    graph = paint(x1,y1,x2,y2,graph)
temp = []
for i in range(M):
    for j in range(N):
        if graph[i][j] ==0:
            temp.append(BFS(i,j))
print(len(temp))
print(*sorted(temp))