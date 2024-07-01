import sys, copy
input = sys.stdin.readline

def left(brd):      # 왼쪽으로 슬라이드
    for i in range(n):
        k = 0
        for j in range(1, n):
            if brd[i][j] != 0:
                tmp = brd[i][j]
                brd[i][j] = 0   # 비울 예정임

                if brd[i][k] == 0:  # 비어있으면 그냥 넣어주고
                    brd[i][k] = tmp
                elif brd[i][k] == tmp:  # 같으면 합쳐주고
                    brd[i][k] *= 2
                    k += 1
                else:   # 다르면 옆에 붙여줌
                    k += 1
                    brd[i][k] = tmp
    return brd

def right(brd):
    for i in range(n):
        k = n-1
        for j in range(n-1, -1, -1):
            if brd[i][j] != 0:
                tmp = brd[i][j]
                brd[i][j] = 0

                if brd[i][k] == 0:
                    brd[i][k] = tmp
                elif brd[i][k] == tmp:
                    brd[i][k] *= 2
                    k -= 1
                else:
                    k -= 1
                    brd[i][k] = tmp
    return brd

def up(brd):
    for j in range(n):
        k = 0
        for i in range(n):
            if brd[i][j] != 0:
                tmp = brd[i][j]
                brd[i][j] = 0

                if brd[k][j] == 0:
                    brd[k][j] = tmp
                elif brd[k][j] == tmp:
                    brd[k][j] *= 2
                    k += 1
                else:
                    k += 1
                    brd[k][j] = tmp
    return brd

def down(brd):
    for j in range(n):
        k = n-1
        for i in range(n-1, -1, -1):
            if brd[i][j] != 0:
                tmp = brd[i][j]
                brd[i][j] = 0

                if brd[k][j] == 0:
                    brd[k][j] = tmp
                elif brd[k][j] == tmp:
                    brd[k][j] *= 2
                    k -= 1
                else:
                    k -= 1
                    brd[k][j] = tmp
    return brd

def dfs(cnt, arr):
    global result
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if arr[i][j] > result:
                    result = arr[i][j]
        return

    for i in range(4):
        arr2 = copy.deepcopy(arr)
        if i == 0:
            dfs(cnt+1, left(arr2))
        elif i == 1:
            dfs(cnt+1, right(arr2))
        elif i == 2:
            dfs(cnt+1, up(arr2))
        else:
            dfs(cnt+1, down(arr2))

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
dfs(0, arr)
print(result)
