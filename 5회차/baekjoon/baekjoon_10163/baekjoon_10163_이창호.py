import sys
sys.stdin=open('input.txt')
# 각 사각형별로 색깔을 칠함 
def coloring(x1,y1,x2,y2,color):
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j]=color
# 각 색별로 카운팅 
def counting(arr,color):
    cnt = 0
    for i in range(min_x,max_x):
        for j in range(min_y,max_y):
            if arr[i][j]==color:
                cnt+=1
    return cnt

max_x = 0
max_y = 0
min_x = 1e9
min_y = 1e9
arr = [[0] * 1001 for _ in range(1001)]
color = 1
T = int(input())
# 시작점의 x,y 도착점의 x,y를 받음
for tc in range(T):
    x1,y1,x1_alpha,y1_alpha = map(int,input().split())
    if x1 + x1_alpha > max_x:
        max_x = x1 + x1_alpha
    if y1 + y1_alpha > max_y:
        max_y = y1 + y1_alpha
    if x1 < min_x:
        min_x = x1
    if y1 < min_y:
        min_y = y1
    coloring(x1,y1,x1 + x1_alpha,y1 + y1_alpha ,color)
    color += 1
for i in range(T):
    print(counting(arr,i+1))
