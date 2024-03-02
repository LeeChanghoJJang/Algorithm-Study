import sys
sys.stdin = open('input.txt')

def coloring(x,y):
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1

def counting(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==1:
                cnt+=1
    return cnt

T = int(input())
arr = [[0] * 100 for _ in range(100)]
for tc in range(T):
    x,y = map(int,input().split())
    coloring(x,y)
print(counting(arr))

