# # 전략: S-F로 BFS한번, F-E로 BFS 한번
# # 문제점 1) 물고기 서식지가 하나가 아니라서..
# import sys
# from collections import deque

# input = sys.stdin.readline

# dr = (1,0),(0,1),(-1,0),(0,-1)

# def search(char):
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == char:
#                 return i,j

# def bfs(start,end):
#     si,sj = start
#     ei,ej = end
#     visit = [[0]*M for _ in range(N)]
#     visit[si][sj]=1
#     q = deque([(si,sj,False)])
#     while q:
#         x,y,check = q.popleft()

#         if x==ei and y==ej and check:
#             return visit[x][y]-1

#         for dx,dy in dr:
#             di,dj = x+dx, y+dy
#             if 0<=di<N and 0<=dj<M and arr[di][dj]!="D":
#                 visit[di][dj] = visit[x][y]+1
#                 if arr[di][dj] == "F":
#                     check = True
#                 q.append((di,dj,check))
#     return -1


# N,M = map(int,input().split())
# arr = [list(input()) for _ in range(N)]

# s_idx = search("S")
# h_idx = search("H")

# print(bfs(s_idx,h_idx))

# 반례 1)
# 3 3
# FDH
# SDE
# EEF

# S-F-H
# S-F 위치와 거리 저장
# H-F 위치와 거리 저장
# F 위치가 같은 경우 거리 합산해서 최소치 출력
# F 위치가 같은 경우가 없다면 -1 출력

import sys
from collections import deque


input = sys.stdin.readline

dr = (1,0),(0,1),(-1,0),(0,-1)

def bfs(char):
    global ans
    si,sj = search(char)
    visit = [[0]*M for _ in range(N)]
    q = deque([(si,sj)])
    visit[si][sj] = 1
    while q:
        x,y = q.popleft()

        if arr[x][y] == "F":
            if (x,y) in data: ans = min(ans,data[(x,y)]+visit[x][y]-1)
            else : data[(x,y)] = visit[x][y]-1

        for dx,dy in dr:
            di,dj = x+dx, y+dy
            if 0<=di<N and 0<=dj<M and not visit[di][dj] and arr[di][dj] !="D":
                visit[di][dj] = visit[x][y] +1
                q.append((di,dj))

def search(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                return i,j


N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

data = dict()
ans = float('inf')
bfs("S")
bfs("H")
print(ans if ans != float('inf') else -1)