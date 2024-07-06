import sys
from collections import deque

# 입력 파일을 열어서 stdin으로 설정합니다.
sys.stdin = open('input.txt')

# 상하좌우 이동을 위한 변수 설정
dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 치즈를 녹이는 함수
def BFS(x, y, visited):
    # BFS를 위한 큐 설정
    queue = deque([[x, y]])
    # 현재 위치 방문 표시
    visited[x][y] = 1
    # BFS 탐색 시작
    while queue:
        x, y = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dr[i][0]
            ny = y + dr[i][1]
            # 배열 범위 내에서 이동 가능하고, 방문하지 않은 위치인 경우
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 치즈가 아닌 경우, 방문 표시 후 큐에 추가
                if not arr[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                else:
                    # 치즈인 경우
                    # 접촉한 횟수를 기록
                    if contact_cheese.get((nx, ny)):
                        contact_cheese[(nx, ny)] += 1
                        # 두 번 이상 접촉한 경우, hubo에 추가
                        if contact_cheese.get((nx, ny)) >= 2:
                            hubo.add((nx, ny))
                    else:
                        contact_cheese[(nx, ny)] = 1

# 치즈를 없애는 함수
def zero_trans():
    # hubo에 있는 좌표들을 0으로 변환
    while hubo:
        i, j = hubo.pop()
        arr[i][j] = 0

# 치즈가 남아있는지 확인하는 함수
def possible(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return True
    return False

# 행과 열의 개수 입력
N, M = map(int, input().split())
# 치즈 상태 입력
arr = [list(map(int, input().split())) for _ in range(N)]
# 치즈 접촉 횟수 기록을 위한 딕셔너리 초기화
contact_cheese = {}
# 치즈가 접촉된 좌표를 기록할 set 초기화
hubo = set()

# 치즈가 모두 녹을 때까지 반복
cnt = 0
while possible(arr):
    # 치즈가 녹는 과정
    contact_cheese = {}  # 치즈 접촉 횟수 초기화
    BFS(0, 0, [[0] * M for _ in range(N)])  # BFS 탐색 및 치즈 접촉 횟수 계산
    zero_trans()  # hubo에 있는 좌표들을 0으로 변환
    cnt += 1  # 시간 증가

# 결과 출력
print(cnt)
