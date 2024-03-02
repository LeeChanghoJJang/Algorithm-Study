import sys
sys.stdin = open('input.txt')
import pprint
def coloring(x1,y1,x2,y2):
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j]=1

def counting(arr):
    cnt = 0
    for i in range(min_x,max_x):
        for j in range(min_y,max_y):
            if arr[i][j]:
                cnt+=1
    return cnt
max_x = 0
max_y = 0
min_x = 1e9
min_y = 1e9
arr = [[0] * 100 for _ in range(100)]
for i in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    coloring(x1,y1,x2,y2)
    if x2 > max_x:
        max_x = x2
    if y2 > max_y:
        max_y = y2
    if x1 < min_x:
        min_x = x1
    if y1 < min_y:
        min_y = y1
print(counting(arr))
