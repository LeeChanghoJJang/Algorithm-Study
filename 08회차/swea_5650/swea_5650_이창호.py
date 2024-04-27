import sys
sys.stdin = open('input.txt')  # input.txt 파일로부터 입력을 받도록 설정

# 블록의 방향을 저장한 딕셔너리
block = {1:{1:0,2:3},2:{2:1,3:0},3:{0:1,3:2},4:{0:3,1:2},5:{}}
# 상하좌우 이동을 위한 방향 리스트
dr = [(0,1),(1,0),(0,-1),(-1,0)]

# 웜홀 위치를 찾는 함수
def finds_hole(arr):
    for i in range(N):
        for j in range(N):
            idx = arr[i][j]
            if 6 <= idx <= 10:
                worm_hole[idx].add((i,j))

# 핀볼 이동을 위한 DFS 함수
def DFS(x,y,dir):
    cnt = 0
    original_x, original_y = x,y
    while 1:
        nx = x + dr[dir][0]
        ny = y + dr[dir][1]
        if [original_x,original_y] == [nx,ny]:  # 처음 출발한 위치로 돌아온 경우
            return cnt
        if not (0<= nx < N and 0<= ny < N) or arr[nx][ny]==5:  # 범위를 벗어나거나 블랙홀인 경우
            cnt += 1
            return 2*cnt-1
        else:
            if arr[nx][ny] == -1:  # 블럭의 끝에 도달한 경우
                return cnt
            elif arr[nx][ny] == 0:  # 빈 공간으로 이동한 경우
                x, y= nx, ny
            elif 1 <= arr[nx][ny] <= 4:  # 블록을 만난 경우
                dir = block[arr[nx][ny]].get(dir)
                cnt += 1
                if dir == None:  # 블록의 방향 변환을 할 수 없는 경우
                    return cnt*2-1
                x,y = nx,ny
            elif 6 <= arr[nx][ny] <= 10:  # 웜홀을 만난 경우
                x,y = list(worm_hole[arr[nx][ny]]-{(nx,ny)})[0]
    return cnt

for tc in range(1,int(input())+1):
    N = int(input())  # 보드의 크기 N을 입력받음
    arr = [list(map(int,input().split())) for _ in range(N)]  # N*N 보드의 정보를 입력받음
    worm_hole = {i: set() for i in range(6, 11)}  # 웜홀의 위치를 저장하기 위한 딕셔너리 초기화
    finds_hole(arr)  # 웜홀의 위치를 찾는 함수 호출
    max_val = 0  # 최대 점수 초기화
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==0:  # 빈 공간일 경우에만 핀볼 이동을 시작함
                for k in range(4):  # 상하좌우 방향으로 이동을 시작함
                    max_val = max(max_val,DFS(i,j,k))  # 최대 점수를 업데이트함
    print(f"#{tc} {max_val}")  # 결과 출력
