import sys
from copy import deepcopy

input = sys.stdin.readline

dr = (0, 1, 2, 3)

N = int(input())
arr = []
max_ = 0

for _ in range(N):
    line = list(map(int, input().split()))
    for i in line:
        max_ = max(max_, i)
    arr.append(line)


def move(arr, d, cnt, max_):
    global result
    if max_ * 2**(5-cnt) < result:
        return

    if cnt == 5:
        result = max(result, max_)
        return
    
    new_arr = deepcopy(arr)
    if d == 0:
        for i in range(N):
            nxt = N-1
            for j in range(N-1, -1, -1):
                if new_arr[i][j]:
                    tmp = new_arr[i][j]
                    new_arr[i][j] = 0

                    if new_arr[i][nxt] == 0:
                        new_arr[i][nxt] = tmp
                    elif new_arr[i][nxt] == tmp:
                        new_arr[i][nxt] *= 2
                        nxt -= 1
                        if tmp == max_:
                            max_ *= 2
                    else:
                        nxt -= 1
                        new_arr[i][nxt] = tmp

    elif d == 1:
        for j in range(N):
            nxt = N-1
            for i in range(N-1, -1, -1):
                if new_arr[i][j]:
                    tmp = new_arr[i][j]
                    new_arr[i][j] = 0

                    if new_arr[nxt][j] == 0:
                        new_arr[nxt][j] = tmp
                    elif new_arr[nxt][j] == tmp:
                        new_arr[nxt][j] *= 2
                        nxt -= 1
                        if tmp == max_:
                            max_ *= 2
                    else:
                        nxt -= 1
                        new_arr[nxt][j] = tmp

    elif d == 2:
        for i in range(N):
            nxt = 0
            for j in range(N):
                if new_arr[i][j]:
                    tmp = new_arr[i][j]
                    new_arr[i][j] = 0

                    if new_arr[i][nxt] == 0:
                        new_arr[i][nxt] = tmp
                    elif new_arr[i][nxt] == tmp:
                        new_arr[i][nxt] *= 2
                        nxt += 1
                        if tmp == max_:
                            max_ *= 2
                    else:
                        nxt += 1
                        new_arr[i][nxt] = tmp

    else:
        for j in range(N):
            nxt = 0
            for i in range(N):
                if new_arr[i][j]:
                    tmp = new_arr[i][j]
                    new_arr[i][j] = 0

                    if new_arr[nxt][j] == 0:
                        new_arr[nxt][j] = tmp
                    elif new_arr[nxt][j] == tmp:
                        new_arr[nxt][j] *= 2
                        nxt += 1
                        if tmp == max_:
                            max_ *= 2
                    else:
                        nxt += 1
                        new_arr[nxt][j] = tmp

    for d in dr:
        move(new_arr, d, cnt+1, max_)


result = 0
for i in dr:
    new_arr = deepcopy(arr)
    move(new_arr, i, 0, max_)

print(result)
