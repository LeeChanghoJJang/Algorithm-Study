import sys
import copy
from itertools import permutations

sys.stdin = open('input.txt')
dx = [1,0,-1,0]
dy = [0,-1,0,1]

def rotation(x,y,wing,arr2,arr):
    x-=1
    y-=1
    visited = [[0] * M for _ in range(N)]
    visited[x][y] =1
    original_x, original_y = x,y
    for s in range(wing,0,-1):
        i = 0
        trans_y = y + s
        cnt = 0
        while cnt < s*8:
            nx,ny  = x + dx[i], trans_y + dy[i]
            if 0 <=nx < N and 0<= ny <M and abs(nx - original_x) <= s and abs(ny-original_y) <=s and not visited[nx][ny]:
                cnt +=1
                visited[nx][ny]=1
                arr2[nx][ny] = arr[x][trans_y]
                x, trans_y = nx,ny
            else:
                i =(i+1)%4
    return arr2

N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
orders = []
for i in range(K):
    orders.append(tuple(map(int,input().split())))

min_val = int(1e9)
for i in permutations(orders,K):
    arr2 = copy.deepcopy(arr)
    arr3 = copy.deepcopy(arr)
    for x,y,wings in i:
        arr2 = rotation(x,y,wings,arr2,arr3)
        arr3 = copy.deepcopy(arr2)
    for j in arr2:
        temp_sum = sum(j)
        if min_val > temp_sum:
            min_val = temp_sum

print(min_val)
