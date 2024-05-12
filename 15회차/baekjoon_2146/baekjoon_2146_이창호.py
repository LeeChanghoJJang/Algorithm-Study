import sys
from collections import deque
from itertools import combinations

# 표준 입력을 'input.txt' 파일에서 읽도록 설정합니다.
sys.stdin = open('input.txt')

# 상하좌우 이동을 위한 좌표 변화를 나타내는 리스트입니다.
dr = [(1,0),(0,1),(-1,0),(0,-1)]

# 같은 섬은 색칠하고 같은 무리로 담기 위한 BFS 함수입니다.
def BFS(x, y, num):
    # 해당 지점을 num으로 색칠하고, 해당 무리의 좌표들을 임시 리스트에 저장합니다.
    colors[x][y] = num
    temp = [(x, y)]
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        # 상하좌우로 이동하며 같은 섬을 탐색합니다.
        for i in range(4):
            nx = x + dr[i][0]
            ny = y + dr[i][1]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and not colors[nx][ny]:
                colors[nx][ny] = num
                queue.append([nx, ny])
                temp.append((nx, ny))
    return temp

# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 각 지점의 색상을 나타내는 2차원 리스트입니다.
colors = [[0] * N for _ in range(N)]

# 색깔별로 무리를 나누어 저장하는 딕셔너리입니다.
color_dict = {}
num = 0

# 같은 곳끼리 색칠을 시작합니다.
for i in range(N):
    for j in range(N):
        if arr[i][j] and not colors[i][j]:
            num += 1
            color_dict[num] = BFS(i, j, num)

# 최소 거리를 나타내는 변수를 무한대로 초기화합니다.
min_distance = float('inf')

# 색깔이 다르면 거리를 재기 시작합니다.
for combi in combinations(range(1, num+1), 2):
    a, b = combi
    for i in color_dict[a]:
        i1, i2 = i
        for j in color_dict[b]:
            j1, j2 = j
            # 두 지점 간의 거리를 계산합니다.
            cal_dis = abs(i1 - j1) + abs(i2 - j2) - 1
            # 최소 거리를 업데이트합니다.
            min_distance = min(min_distance,cal_dis)
            # 최소 거리가 1이면 더 이상 계산할 필요 없이 1을 출력하고 종료합니다.
            if min_distance == 1:
                exit(print(1))

print(min_distance)
