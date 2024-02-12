import sys
sys.stdin = open('input.txt')
# 처음 썻던 코드 : 뭐가 틀렸는지 모르겠음.. 테케 4개만 맞고 나머지 조금씩만 틀림
# 8방향에 *이 있는지 확인
def check(x,y):
    global click
    if arr[x][y] == '*':
        return False
    elif arr[x][y] == '.':
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] =='*':
                return False
        else:
            return True

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    out = [[1] * N for _ in range(N)]
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,-1,1,1,-1]
    click = 0

    #.에 클릭한번 했을 때, 팔방이 빈 경우 퍼져가는 곳은 visited에 1로 채우기
    for x in range(N):
        for y in range(N):
            if check(x,y) and not visited[x][y]:
                # 처음 클릭때만 1추가
                click += 1
                stack = deque([[x,y]])
                # stack에 방문처리해야할 것들이 줄어들 때까지 반복
                while stack:
                    temp =[]
                    # stack에 저장된건 전부 방문처리
                    x,y = stack.pop()
                    visited[x][y]=1
                    # 방문한 곳은 전부 1로 표시
                    # out 앞번 while문에서 인접한 방향에 False로 전환되지 않았으면 8방 계속 탐색
                    if out[x][y]:
                        for i in range(8):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            # 일단 nx,ny 들은 전부 .인건 확인됨
                            # 그러면 일단 *일리는 없으며, 무조건 추가
                            # 다만 nx,ny 주변에 *이 있거나 방문한적 있으면 out =True처리
                            if 0<=nx<N and 0<=ny<N and visited[nx][ny] ==0:
                                temp.append([nx, ny])
                                if check(nx,ny) and visited[nx][ny]==0:
                                    pass
                            # 만약 주변에 하나라도 *이 있거나 방문한 경우 out 처리하고, while문 그대로 간다.
                                else:
                                    out[nx][ny]=False
                        stack.extend(temp)

    for i in range(N):
        for j in range(N):
            if arr[i][j] != '*' and not visited[i][j]:
                click +=1
    print(f'#{tc} {click} ')

### 두번째 시도
from collections import deque
# 1. 8방향에 지뢰 숫자가 있는만큼 모든 배열에 숫자로 표시하기
def count_land_mine(x,y):
    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny <N and arr[nx][ny] =='*':
            cnt +=1
    arr[x][y] = cnt

# 2. 주변 숫자를 전부 *로 만들기
def make_land_mine(x,y):
    queue = deque([[x,y]])
    arr[x][y]='*'
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny] ==0:
                    arr[nx][ny]='*'
                    queue.append([nx,ny])
                elif arr[nx][ny] != '*':
                    arr[nx][ny]='*'

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, -1, 1, 1, -1]
    click = 0
    # 좌표가 .인 경우, 그 배열의 8방향에 위치한 지뢰 숫자만큼 좌표에 표기
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='.':
                count_land_mine(i,j)
    # 전체 갯수가 0부터 시작하고, 0인 좌표를 찾으면 주변 전부 *로 표시
    # 0이 아닌 숫자 발견할 때는 거기까지만 *로 표시
    total_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==0:
                total_cnt +=1
                make_land_mine(i,j)
    # 0도 없고, 남은건 0이 아닌 숫자밖에 없으며, 발견시마다 카운트 세기
    for i in range(N):
        for j in range(N):
            if arr[i][j] !='*':
                total_cnt +=1
    print(f'#{tc} {total_cnt}')
