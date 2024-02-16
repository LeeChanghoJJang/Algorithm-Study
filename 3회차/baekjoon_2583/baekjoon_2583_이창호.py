# baekjoon_2583 영역 구하기
import sys
sys.stdin = open('input.txt')
from collections import deque
# 델타 설정
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 일단 주어진 조건대로 영역을 나눠보자
def paint(x1,y1,x2,y2,graph):
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] =1
    return graph
    
# BFS를 활용해서 한번 0을 만난 경우, 인접한 것들도 전부 색칠해줌
def BFS(x,y):
    # area로 그 구역의 넓이 계산
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

# M : 행 N : 열 K : 직사각형의 범위 
M,N,K = map(int,input().split())
graph = [[0] * N for _ in range(M)]

for _ in range(K):
    # 직사각형의 범위를 시작점 행,열과 도착점 행,열로 구분해서 언팩 
    y1,x1,y2,x2 = map(int,input().split())
    # 직사각형으로 일단 전 구역 색칠
    graph = paint(x1,y1,x2,y2,graph)
temp = []
for i in range(M):
    for j in range(N):
        # BFS를 활용해서 한번 0을 만난 경우, 인접한 것들도 전부 색칠해줌 ==> temp의 길이가 총 구역의 갯수이며, 각 원소는 그 구역의 넓이
        if graph[i][j] ==0:
            temp.append(BFS(i,j))
print(len(temp))
print(*sorted(temp))
