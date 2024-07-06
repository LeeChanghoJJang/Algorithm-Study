import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
aps = []

for _ in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    aps.append([x, y])
    
L = int(input())
change = [input().split() for _ in range(L)]

for i in range(L):
    change[i][0] = int(change[i][0])
    
arr = [[0] * N for _ in range(N)]
for x, y in aps:
    arr[x][y] = 1

dr = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
cd = {"L": -1, "D": 1}
d = 1

snake = deque([(0, 0)])

arr[0][0] = 2
time = -1
idx = 0
nx, ny = 0, 0

while True:
    time += 1
    apple = False
    x, y = nx, ny
    
    if idx < L and time == change[idx][0]:
        d += cd[change[idx][1]]
        d %= 4
        idx += 1
    
    dx, dy = dr[d]
    nx, ny = x+dx, y+dy
    
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break
    
    if arr[nx][ny] == 2:
        break
    
    if arr[nx][ny] == 1:
        apple = True
    
    arr[nx][ny] = 2
    snake.append((nx, ny))
    
    if apple:
        continue
    else:
        lx, ly = snake.popleft()
        arr[lx][ly] = 0
    
print(time+1)