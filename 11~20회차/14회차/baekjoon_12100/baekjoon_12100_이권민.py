# 한 방향으로 쏟기. 합치기는 한번만. 횟수는 다섯번. 제일 큰 값만
# 시간제한. 제일 큰 놈이 합쳐지면 바로 break.
# 큰 놈만 보기엔 주변 놈들 합쳐지면. 합치는 방법도 여러가지.

from collections import deque
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
side = 0
deq = deque()

def get(i, j):
    if matrix[i][j]: # 0이 아닌 값이라면
        deq.append(matrix[i][j]) # queue에 board의 값을 넣는다.
        matrix[i][j] = 0 # 처리가 된 빈 자리는 0으로 값 업데이트
        
def merge(i, j, di, dj): # row index, column index, y방향, x방향 
    while deq:
        x = deq.popleft() # 움직이려는 블록 값을 가져온다. FIFO 
        if not matrix[i][j]: # 0이라면 그대로 놓는다.
            matrix[i][j] = x
        elif matrix[i][j] == x: # 값이 일치한다면
            matrix[i][j] = x*2 # 합쳐지므로 2배로 증가
            i, j = i+di, j+dj 
        else: # 값이 일치하지 않으면
            i, j = i+di, j+dj
            matrix[i][j] = x 

def move(k):
    if k == 0: # 위로 이동, 블락들이 위로 모두 이동하면 row index는 0
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0) # row index 1씩 증가하면서 아래쪽 블락들을 합쳐감
    elif k == 1: # 아래로 이동, 블락들이 아래로 모두 이동하면 row index는 n-1
        for j in range(n):
            for i in range(n-1, -1, -1):
                get(i, j)
            merge(n-1, j, -1, 0) # row 인덱스 1씩 감소하면서 위쪽들을 합쳐감
    elif k == 2: # 오른쪽으로 이동, column index는 0
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1) # column 인덱스 증가 오른쪽으로 이동
    else: # 왼쪽으로 이동, column index는 n-1
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i, j)
            merge(i, n-1, 0, -1) # column 인덱스 감소 왼쪽으로 이동
            
def solve(count):
    global matrix, answer
    if count == 5: # 최대 5번까지 움직였다면
        for i in range(n):
            answer = max(answer, max(matrix[i])) # 가장 큰 값이 answer
        return
    b = [x[:] for x in matrix] # 방향을 바꾸기 전에 원래의 보드를 기억해야 한다.
    
    for k in range(4): # 4방향으로 움직인다.
        move(k) # 움직인다.
        solve(count+1) # 재귀적으로 호출한다.
        matrix = [x[:] for x in b]

solve(0)
print(answer)