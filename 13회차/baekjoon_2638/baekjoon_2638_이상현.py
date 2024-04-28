from collections import deque

def chk_cheese():
    # 치즈가 남아있는지 확인하는 함수입니다.
    for row in range(N):
        for col in range(M):
            if list_[row][col]:  # 치즈가 있으면
                return True  # True 반환
    return False  # 치즈가 없으면 False 반환

def bfs():
    q = deque()  # BFS를 위한 큐를 생성합니다.
    q.append((0, 0))  # 시작 지점을 큐에 추가합니다.
    visited = [[False] * M for _ in range(N)]  # 방문 여부를 저장하는 배열을 생성합니다.
    visited[0][0] = True  # 시작 지점을 방문했다고 표시합니다.
    temp = []  # 외부 공기와 접촉한 치즈를 저장하는 리스트입니다.

    while q:
        row, col = q.popleft()  # 큐에서 좌표를 하나 꺼냅니다.

        for i in range(4):  # 상하좌우로 이동합니다.
            nrow, ncol = row + drow[i], col + dcol[i]

            # 범위를 벗어나거나 이미 방문한 곳이면 건너뜁니다.
            if not (0 <= nrow < N and 0 <= ncol < M) or visited[nrow][ncol]:
                continue

            # 외부 공기와 접촉한 치즈를 찾습니다.
            if list_[nrow][ncol] >= 1:
                temp.append((nrow, ncol))  # 외부 공기와 접촉한 치즈를 저장합니다.
            else:
                visited[nrow][ncol] = True  # 방문 표시를 합니다.
                q.append((nrow, ncol))  # 큐에 새로운 좌표를 추가합니다.

    # 외부 공기와 접촉한 치즈의 개수를 증가시킵니다.
    for row, col in temp:
        list_[row][col] += 1

    # 치즈를 녹입니다.
    for row in range(N):
        for col in range(M):
            if list_[row][col] >= 3:  # 외부 공기와 접촉한 횟수가 3 이상이면
                list_[row][col] = 0  # 치즈가 녹습니다.
            elif list_[row][col] == 2:  # 외부 공기와 한 번만 접촉한 경우
                list_[row][col] = 1  # 외부 공기로 변합니다.

# 입력 받기
N, M = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(N)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]  # 이동 방향을 나타내는 리스트입니다.
t = 0  # 시간 변수입니다.

# 치즈가 모두 녹을 때까지 반복합니다.
while True:
    if not chk_cheese():  # 치즈가 없으면 반복문을 종료합니다.
        break

    bfs()  # 치즈를 녹입니다.
    t += 1  # 시간을 증가시킵니다.

print(t)  # 결과를 출력합니다.
