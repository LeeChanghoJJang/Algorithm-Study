import sys
from collections import deque
import copy

# 입력 파일을 표준 입력으로 설정
sys.stdin = open('input.txt')

# 상하좌우 방향벡터 정의
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 블록을 찾고 그룹화하여 탐색하는 함수
def find_block(x, y, arr, visited):
    visited[x][y] = 1
    color = arr[x][y]
    arr[x][y] = -9
    queue = deque([[x, y]])
    rainbows = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == color or arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    arr[nx][ny] = -9
                    cnt += 1
                    if arr[nx][ny] == 0:
                        rainbows += 1
    return cnt, rainbows, arr

# 중력 작용 함수
def gravity(arr):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if arr[i][j] != -1:
                k = i
                while k < N-1 and arr[k+1][j] == -9:
                    arr[k+1][j] = arr[k][j]
                    arr[k][j] = -9
                    k += 1
    return arr

# 90도 회전 함수
def rotate_90_degree(arr):
    n = len(arr)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[n - j - 1][i] = arr[i][j]
    return rotated

# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

point = 0

# 반복적으로 최대 블록 그룹 찾기
while True:
    max_cnt, max_rainbows, max_i, max_j = 1, 0, 0, 0
    # 모든 칸에 대해 반복
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 1:  # 블록이 존재하는 경우
                arr_temp = copy.deepcopy(arr)
                cnt, rainbows, temp_arr = find_block(i, j, arr_temp, [[0] * N for _ in range(N)])
                # 가장 큰 블록 그룹 찾기
                if max_cnt < cnt:
                    max_cnt = cnt
                    max_rainbows = rainbows
                    result = copy.deepcopy(temp_arr)
                    max_i, max_j = i, j
                # 블록 그룹의 크기가 같은 경우, 무지개 블록의 개수가 더 많은 경우 선택
                elif max_cnt == cnt and max_rainbows < rainbows:
                    max_rainbows = rainbows
                    max_i, max_j = i, j
                    result = copy.deepcopy(temp_arr)
                # 블록 그룹의 크기와 무지개 블록의 개수가 같은 경우, 기준 블록의 위치로 판단
                elif max_cnt == cnt and max_rainbows == rainbows and max_i < i:
                    max_i, max_j = i, j
                    result = copy.deepcopy(temp_arr)
                elif max_cnt == cnt and max_rainbows == rainbows and max_i == i and max_j < j:
                    max_j = j
                    result = copy.deepcopy(temp_arr)
    # 블록 그룹이 2개 미만이면 종료
    if max_cnt < 2:
        break
    # 점수 계산
    point += max_cnt ** 2
    # 중력 작용 후 90도 회전 반복
    arr = gravity(rotate_90_degree(gravity(result)))

# 결과 출력
print(point)
