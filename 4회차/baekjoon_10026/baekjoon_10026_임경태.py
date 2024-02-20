# 10226 / 적록색약 /골드5

import sys
sys.stdin = open("input.txt")
from collections import deque

# 색 영역 체크
def BFS(pic, visited, i, j, color):
    Q = deque([[i, j]])
    visited[i][j] = 1

    while Q:
        ci, cj = Q.popleft()
        for di, dj in dr:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and pic[ni][nj] == color:
                    visited[ni][nj] = 1
                    Q.append([ni, nj])

# 영역 개수 세기
def count_area(pic):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(pic, visited, i, j, pic[i][j])
                cnt += 1
    
    return cnt

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
pic = [input() for _ in range(N)]

n_cnt = count_area(pic)  # 일반인
pic = [pic[i].replace('G', 'R') for i in range(N)]  # 변환
w_cnt = count_area(pic) # 적록색약

print(n_cnt, w_cnt)

'''
34072KB / 80ms
'''