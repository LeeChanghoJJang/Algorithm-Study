import sys
from collections import deque

# 표준 입력을 파일로 변경
sys.stdin = open('input.txt')

# 방향 벡터 정의
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


# 너비 우선 탐색(BFS) 함수 정의
def BFS(x, y, visited):
    queue = deque([[x, y]])
    visited[x][y] = 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 8방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 배열 범위 내에 있고, 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 거리를 계산하여 방문 표시
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

                # 1로 표시된 지뢰를 만났다면 최단 거리 반환
                if arr[nx][ny] == 1:
                    return visited[nx][ny] - 1


# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_val = 0

# 모든 위치에 대해 확인
for i in range(N):
    for j in range(M):
        # 지뢰가 없는 경우에만 최단 거리 계산
        if arr[i][j] == 0:
            temp = BFS(i, j, [[0] * M for _ in range(N)])
            max_val = max(max_val, temp)

# 결과 출력
print(max_val)
