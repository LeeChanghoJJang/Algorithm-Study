import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

from pprint import pprint

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

n = int(input())
arr = [[0] * n for _ in range(n)]
# 0: 아무것도 없음, 1: 사과, 2: 뱀
arr[0][0] = 2

k = int(input())
for _ in range(k): 
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

l = int(input())
dir = {}
for _ in range(l):
    x, c = input().split()
    x = int(x)
    dir[x] = c

snake = deque([(0, 0)])
def solution(x, y, d, time):

    # print(time)
    # pprint(arr)

    nx = x + dx[d]
    ny = y + dy[d]

    if time in dir:
        if dir[time] == 'L':
            d = (d-1) % 4
        elif dir[time] == 'D':
            d = (d+1) % 4

    # print(d)

    if 0 <= nx < n and 0 <= ny < n:
        if arr[nx][ny] == 1:
            arr[nx][ny] = 2
            snake.appendleft((nx, ny))
            solution(nx, ny, d, time+1)
        
        elif arr[nx][ny] == 2:
            print(time)
            return

        else:
            arr[nx][ny] = 2
            snake.appendleft((nx, ny))
            xx, yy = snake.pop()
            arr[xx][yy] = 0
            solution(nx, ny, d, time+1)

    else:
        print(time)
        return 

solution(0, 0, 1, 1)
