# 2583 영역 구하기

from collections import deque

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# M: 행 / N: 열 / K: 직사각형 개수
M, N, K = map(int, input().split())
# quad: 직사각형 저장 / paper: 모눈종이
quad = [tuple(map(int, input().split())) for _ in range(K)]
paper = [[0] * N for _ in range(M)]
total_area = []

# 직사각형 그리기
for sj, si, ej, ei in quad:
    for i in range(M-ei, M-si):
        for j in range(sj, ej):
            paper[i][j] = 1

#분리된 영역의 넓이 구하기
for i in range(M):
    for j in range(N):
        if not paper[i][j]:
            paper[i][j] = 1
            # BFS - 분리된 영역 넓이 구하기
            Q = deque([(i, j)])
            area = 1
            while Q:
                i, j = Q.popleft()
                # 델타 탐색 - 0인 부분 1로 바꿔주고 카운트
                for di, dj in dr:
                    ni = i + di; nj = j + dj
                    if (0<=ni<M and 0<=nj<N) and not paper[ni][nj]:
                        Q.append((ni, nj))
                        paper[ni][nj] = 1; area += 1
            total_area.append(area)

print(len(total_area))
print(*sorted(total_area))

'''
34088KB / 76ms
'''