from sys import stdin
from collections import deque

input = stdin.readline


dr = (0,1),(1,0),(0,-1),(-1,0)
N = int(input())

# arr은 좌표
arr = [[0]*N for _ in range(N)]
for _ in range(int(input())):
    x,y = map(lambda x: int(x)-1 , input().split())
    arr[x][y] = 1

# 커맨드 저장 (시간, 커맨드)
cmd = deque([input().split() for _ in range(int(input()))])

# 뱀
snake = deque([(0,0)])

time = 0    # 시간
d = 0       # 델타 (오른쪽 방향부터 시작)

while True:
    time += 1
    # di,dj : 머리가 움직일 좌표
    x,y = snake[0][0], snake[0][1]
    dx,dy = dr[d]
    di, dj = x+dx, y+dy

    # 머리가 움직인 곳의 좌표가 범위 내이고, 뱀의 몸통에 닿지 않았다면 (진행조건)
    if 0<=di<N and 0<=dj<N and (di,dj) not in snake:
        # 머리를 앞에 더하고
        snake.appendleft((di,dj))
        # 꼬리를 뺀다
        i,j = snake.pop()
        # 머리가 사과를 먹은 경우
        if arr[di][dj] == 1:
            # 사과를 없애고
            arr[di][dj] = 0
            # 꼬리를 뒤에 다시 더한다 
            snake.append((i,j))
    # 진행조건에 맞지 않다면
    else :
        # 시간을 출력하고 종료
        exit(print(time))
        
    
    # 커맨드가 남아있고, 커맨드 앞의 시간이 현재 시간과 같다면
    if cmd and int(cmd[0][0]) == time:
        # 커맨드를 뱉어서
        t,c = cmd.popleft()
        # D 인 경우 델타값을 1 올려 오른쪽으로 돌리고, L인 경우 1 내려 왼쪽으로 돌린다
        d = (d+1 if c=="D" else d-1)%4