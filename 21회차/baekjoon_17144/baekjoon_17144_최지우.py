import sys
from copy import deepcopy
input = sys.stdin.readline


def clean(n):
    sx, sy = cp[n]
    x, y = sx, sy+1
    tmp = arr[x][y]
    arr[x][y] = 0
    d = dr[n]
    k = 0
    
    while (x, y) != (sx, sy):
        cur = tmp
        dx, dy = d[k]
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if arr[nx][ny] > 0:
                tmp = arr[nx][ny]
            elif arr[nx][ny] == -1:
                return
            else:
                tmp = 0
            arr[nx][ny] = cur
            x, y = nx, ny
        else:
            k += 1
            k %= 4
        

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dr = [[(0, 1), (-1, 0), (0, -1), (1, 0)], [(0, 1), (1, 0), (0, -1), (-1, 0)]]
for i in range(R):
    if arr[i][0] == -1:
        cp = [(i, 0), (i+1, 0)]
        break

while T:
    change = deepcopy(arr)
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                cur = arr[i][j]
                diffuse = cur//5
                
                if not diffuse:
                    continue
                
                for dx, dy in dr[0]:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < R and 0 <= ny < C:
                        if arr[nx][ny] != -1:
                            change[nx][ny] += diffuse
                            change[i][j] -= diffuse
    arr = change

    clean(0)
    clean(1)

    T -= 1
    
result = 0
for i in arr:
    result += sum(i)
print(result + 2)