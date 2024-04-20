import sys

# 이동 방향 정의 (아래, 오른쪽, 위, 왼쪽)
dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# DFS를 이용하여 탐색하는 함수
def back(x, y, visited, cnt):
    global max_cnt
    if max_cnt < cnt:  # 현재까지의 최대 칸 수 업데이트
        max_cnt = cnt

    for i in range(4):  # 네 방향에 대해서
        nx = x + dr[i][0]
        ny = y + dr[i][1]
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(arr[nx][ny]) - ord('A')]:
            # 배열 범위를 벗어나지 않고, 방문하지 않은 알파벳인 경우
            visited[ord(arr[nx][ny]) - ord('A')] = True  # 방문 표시
            back(nx, ny, visited, cnt + 1)  # DFS 재귀 호출
            visited[ord(arr[nx][ny]) - ord('A')] = False  # 방문 해제 (백트래킹)

# 행과 열의 수 입력
R, C = map(int, input().split())

# 보드 상태 입력
arr = [input() for _ in range(R)]

# 알파벳 방문 여부를 나타내는 리스트 초기화
visited = [False] * 26  # 알파벳은 총 26개

max_cnt = 0  # 최대 칸 수 초기화
visited[ord(arr[0][0]) - ord('A')] = True  # 시작 지점 알파벳 방문 표시

# DFS 시작
back(0, 0, visited, 1)

# 결과 출력
print(max_cnt)
