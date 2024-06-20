import sys
from collections import deque
sys.stdin = open('input.txt')

# 아기 상어의 이동 방향
dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# BFS 함수 정의
def BFS(x, y, visited):
    visited[x][y] = 1  # 시작점 방문 처리
    queue = deque([(x, y, 0)])  # 시작점을 큐에 추가하고 거리 0으로 설정
    temp = 0  # 이전에 방문한 지점의 거리를 저장할 변수
    selected = (N, N, -1)  # 선택된 먹이의 좌표와 거리를 저장할 변수 초기화
    while queue:
        x, y, s = queue.popleft()  # 큐에서 하나의 지점을 가져옴
        if temp != s and selected[-1] != -1:  # 이전 지점과 현재 지점의 거리가 다르면서 선택된 먹이가 있는 경우
            return selected  # 선택된 먹이의 좌표와 거리 반환
        for i in range(4):  # 상하좌우에 대해 이동 가능한지 확인
            nx, ny = x + dr[i][0], y + dr[i][1]  # 다음 이동할 지점 계산
            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny] or graph[nx][ny] > size:
                continue  # 범위를 벗어나거나 이미 방문했거나 상어보다 큰 물고기가 있는 경우 무시
            if graph[nx][ny] and graph[nx][ny] < size:  # 물고기가 있고 상어보다 작은 경우
                selected = min(selected, (nx, ny, s + 1))  # 선택된 먹이 갱신
            visited[nx][ny] = 1  # 다음 지점 방문 처리
            queue.append((nx, ny, s + 1))  # 다음 지점 큐에 추가
        temp = s  # 이전에 방문한 지점의 거리 갱신
    return (-1, -1, -1)  # 선택된 먹이가 없는 경우

# 입력 받기
N = int(sys.stdin.readline())  # 공간의 크기
graph = [list(map(int, input().split())) for _ in range(N)]  # 공간 정보 입력
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:  # 아기 상어의 위치 찾기
            x, y = i, j
            break
size = 2  # 아기 상어의 크기 초기화
result, count = 0, 0  # 결과 및 먹이 먹은 횟수 초기화
graph[x][y] = 0  # 아기 상어의 위치를 0으로 설정하여 먹었다고 표시

# 아기 상어가 먹이를 먹으며 성장하는 과정 시뮬레이션
while 1:
    visited = [[0] * N for _ in range(N)]  # 방문 여부 초기화
    x, y, s = BFS(x, y, visited)  # BFS를 통해 가장 가까운 먹이의 위치와 거리 계산
    if s == -1:  # 먹이를 찾지 못한 경우
        break
    graph[x][y] = 0  # 먹이를 먹었으므로 해당 위치를 0으로 설정하여 먹었다고 표시
    result += s  # 결과에 먹이까지의 거리 추가
    count += 1  # 먹은 먹이의 개수 증가
    if count == size:  # 아기 상어의 크기와 먹이를 먹은 횟수가 같은 경우
        size += 1  # 아기 상어의 크기 증가
        count = 0  # 먹은 먹이의 개수 초기화

# 결과 출력
print(result)
