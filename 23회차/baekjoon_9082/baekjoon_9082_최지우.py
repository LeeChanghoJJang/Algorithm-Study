import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().strip()))]
    arr.append(list(input().strip()))

    bomb = [0] * N
    visited = [0] * N
    cnt = 0
    que = deque()

    for i in range(N):
        if arr[1][i] == '*':
            bomb[i] = 1
            cnt += 1
            for j in range(-1, 2):
                if 0 <= i+j < N:
                    arr[0][i+j] -= 1
        if arr[0][i] > 0:
            que.append(i)
    
    while que:
        now = que.popleft()
        if visited[now]:
            continue
        visited[now] = 1      
        for i in range(-1, 2):
            if 0 <= now+i < N and not bomb[now+i]:
                f = True
                for j in range(-1, 2):
                    if 0 <= now+i+j < N and arr[0][now+i+j] == 0:
                        f = False
                        break
                
                if f:
                    cnt += 1
                    bomb[now+i] = 1

                    for j in range(-1, 2):
                        if 0 <= now+i+j < N:
                            arr[0][now+i+j] -= 1
                            if arr[0][now+i+j] > 0:
                                que.append(now+i+j)
                    break
    print(cnt)