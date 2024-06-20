import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(q):
    while q:
        now = q.popleft()
        for k in arr[now]:
            next_[k] -= 1
            if next_[k] == 0:
                print(k, end=' ')
                q.append(k)


for tc in range(1, 11):
    print(f'#{tc}', end=' ')
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    arr = [[] for _ in range(V+1)]
    next_ = [0] * (V+1)

    for i in range(0, E*2, 2):
        arr[edge[i]].append(edge[i+1])
        next_[edge[i+1]] += 1

    q = deque()
    for i in range(1, V+1):
        if next_[i] == 0:
            print(i, end=' ')
            q.append(i)
    BFS(q)
    print()
