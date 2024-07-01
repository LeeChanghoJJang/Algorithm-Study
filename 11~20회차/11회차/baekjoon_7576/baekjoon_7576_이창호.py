import sys
sys.stdin = open('input.txt')  # 입력을 파일에서 읽도록 설정
from collections import deque
dr = [(1,0),(0,1),(-1,0),(0,-1)]  # 이동할 방향 (아래, 오른쪽, 위, 왼쪽)

def finds(arr):
    temps = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:  # 익은 토마토의 좌표를 찾아서 temps 리스트에 추가
                temps.append((i,j,0))  # 토마토의 행, 열, 익는데 걸리는 시간(초기값 0)을 튜플 형태로 추가
    return temps

def testing(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:  # 아직 익지 않은 토마토가 있다면
                return False  # False 반환
    return True  # 모든 토마토가 익었으면 True 반환

def BFS(temp):
    queue = deque(temp)  # 익은 토마토의 좌표와 익는데 걸리는 시간을 가진 큐를 생성
    time = 0  # 경과 시간을 초기화
    while queue:
        x, y, time = queue.popleft()  # 큐에서 좌표와 시간을 추출
        for i in range(4):  # 네 방향에 대해 탐색
            nx = x + dr[i][0]  # 다음 행 위치 계산
            ny = y + dr[i][1]  # 다음 열 위치 계산
            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:  # 범위 내에 있고, 익지 않은 토마토라면
                tomatoes[nx][ny] = 1  # 해당 위치의 토마토를 익게 변경
                queue.append((nx, ny, time + 1))  # 큐에 다음 위치와 시간을 추가하여 탐색 계속
    return time  # 모든 토마토가 익는데 걸린 시간을 반환

M, N = map(int, input().split())  # 박스의 가로, 세로 크기를 입력 받음
tomatoes = [list(map(int, input().split())) for _ in range(N)]  # 박스의 상태를 입력 받음
times = BFS(finds(tomatoes))  # 익은 토마토의 위치를 찾고 BFS 함수 호출하여 걸린 시간을 계산
if testing(tomatoes):  # 모든 토마토가 익었는지 확인
    print(times)  # 익는데 걸린 시간 출력
else:
    print(-1)  # 모든 토마토가 익지 못하는 경우 -1 출력
