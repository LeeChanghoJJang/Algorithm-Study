import sys
sys.stdin = open('input.txt')  # input.txt 파일을 표준 입력으로 사용

from collections import deque

# 상하좌우 이동을 위한 방향 벡터
dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def BFS(x, y):
    queue = deque([[x, y]])  # 시작점을 큐에 추가합니다.
    cnt = 1  # 현재 영역의 크기를 저장할 변수를 초기화합니다.
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dr[i][0]  # 다음 행 좌표를 계산합니다.
            ny = y + dr[i][1]  # 다음 열 좌표를 계산합니다.
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == '1':
                arr[nx][ny] = '0'  # 방문한 영역을 표시합니다.
                cnt += 1  # 영역의 크기를 증가시킵니다.
                queue.append([nx, ny])  # 다음 위치를 큐에 추가합니다.
    return cnt  # 현재 영역의 크기를 반환합니다.

N = int(input())  # 그리드의 크기 N을 입력받습니다.
arr = [list(input()) for _ in range(N)]  # 그리드 정보를 입력받습니다.

result = []  # 각 영역의 크기를 저장할 리스트를 초기화합니다.
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':  # 아직 방문하지 않은 1이라면,
            arr[i][j] = '0'  # 해당 위치를 방문했다고 표시합니다.
            result.append(BFS(i, j))  # BFS를 통해 현재 영역의 크기를 구하고 결과 리스트에 추가합니다.

print(len(result))  # 영역의 개수를 출력합니다.
for area in sorted(result):  # 영역의 크기를 오름차순으로 출력합니다.
    print(area)
