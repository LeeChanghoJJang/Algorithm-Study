import sys
sys.stdin = open('input.txt')  # input.txt 파일을 표준 입력으로 사용

from collections import deque

# 이동 방향을 나타내는 리스트
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def djikstra(x, y):
    # 출발점의 거리를 0으로 설정하고 큐에 추가합니다.
    queue = deque([[x, y]])
    dist[x][y] = 0

    # BFS를 사용하여 최단 거리를 탐색합니다.
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 벽이 아닌 경우
                if arr[nx][ny] == '1' and dist[nx][ny] > dist[x][y]:
                    dist[nx][ny] = dist[x][y]  # 현재 위치의 거리를 할당합니다.
                    queue.append([nx, ny])  # 다음 위치를 큐에 추가합니다.
                # 벽인 경우
                elif arr[nx][ny] == '0' and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1  # 현재 위치의 거리에 1을 더한 값을 할당합니다.
                    queue.append([nx, ny])  # 다음 위치를 큐에 추가합니다.
    return dist[-1][-1]  # 도착점의 거리를 반환합니다.

N = int(input())  # 그리드의 크기 N을 입력받습니다.
arr = [list(input()) for _ in range(N)]  # 그리드 정보를 입력받습니다.

dist = [[float('inf')] * N for _ in range(N)]  # 출발점부터의 거리를 저장할 리스트를 초기화합니다.

# 출발점에서 도착점까지의 최단 거리를 출력합니다.
print(djikstra(0, 0))
