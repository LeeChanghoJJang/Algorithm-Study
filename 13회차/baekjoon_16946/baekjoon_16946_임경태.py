# 16946 벽 부수고 이동하기 4

from collections import deque

go = ((0, 1), (1, 0), (0, -1), (-1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
group_num = 2
group = {}

def check_empty(i, j, num):
    Q = deque([[i, j]]); cnt = 0

    while Q:
        i, j = Q.popleft()
        cnt += 1
        grid[i][j] = num

        for di, dj in go:
            ni = i + di
            nj = j + dj

            if (0 <= ni < N and 0 <= nj < M and 
                not grid[ni][nj] and not visit[ni][nj]):
                visit[ni][nj] = 1
                Q.append([ni, nj])
    return cnt

# 0인 부분 크기 구하여 채우기
for i in range(N):
    for j in range(M):
        # 벽이거나 체크한 곳이면 패스
        if grid[i][j] > 0: continue
        # BFS 실행
        group[group_num] = check_empty(i, j, group_num)
        group_num += 1

# 1 인 부분 주위 4칸 탐색 및 카운트
for i in range(N):
    for j in range(M):
        if grid[i][j] > 1:
            print(0, end='')
        else:
            cnt = set()
            for di, dj in go:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] > 1:
                    cnt.add(grid[ni][nj])
            print((sum(map(lambda x: group[x], cnt))+1) % 10, end='')
    print()

'''
    핵심 : 0인 부분 크기 구할 때 딕셔너리로 그룹번호: 그룹 크기 저장
    이런 BFS류 문제 풀 때 유용하게 사용
'''