import sys
from collections import deque
import pprint
sys.stdin = open('input.txt')

# 8개의 방향에 대한 상대 좌표
dr = [(1,0), (-1,0), (0,-1), (-1,-1), (1,-1), (0,1), (-1,1), (1,1)]

def BFS(start):
    # 시작 지점으로부터 BFS 탐색을 시작한다.
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        # 만약 보물을 찾았다면 해당 보물까지의 거리를 반환한다.
        if treasure[x][y] == '*':
            return distance[x][y]
        # 8방향으로 이동하며 탐색한다.
        for i in range(8):
            nx = x + dr[i][0]  # 다음 위치의 행 좌표
            ny = y + dr[i][1]  # 다음 위치의 열 좌표
            # 다음 위치가 유효한 범위 내에 있고, 갈 수 있는 곳이라면
            if 0 <= nx < H and 0 <= ny < W and treasure[nx][ny] in ['.', '*']:
                # 거리를 갱신한다. 기존보다 왼쪽 방향일 경우 거리에 1을 더한다.
                if distance[nx][ny] > distance[x][y] + (i < 5):
                    distance[nx][ny] = distance[x][y] + (i < 5)
                    # 다음 위치를 큐에 추가하여 계속해서 탐색한다.
                    queue.append([nx, ny])
    # 보물에 도달할 수 없는 경우 -1을 반환한다.
    return -1 if distance[end[0]][end[1]] == float('inf') else distance[end[0]][end[1]]

# 보물 지도의 세로와 가로 길이를 입력받는다.
H, W = map(int, input().split())
# 보물 지도를 입력받는다.
treasure = [input() for _ in range(H)]

# 각 위치까지의 최소 거리를 저장하는 배열을 초기화한다.
distance = [[float('inf')] * W for _ in range(H)]
# 시작 지점의 좌표를 찾아 거리를 0으로 초기화한다.
for i in range(H):
    for j in range(W):
        if treasure[i][j] == 'K':
            start = (i, j)
            distance[i][j] = 0
            continue

        if treasure[i][j]=='*':
            end = (i, j)
            continue
# BFS 탐색을 수행하고 결과를 출력한다.
print(int(BFS(start)))
