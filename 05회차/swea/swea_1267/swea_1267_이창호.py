import sys
sys.stdin = open('input.txt')
from collections import deque

def find_start(arr,visited) :
    for i in range(1, V + 1):
        if not arr[i]:
            return i

def find_parents(start,arr,visited) :
    stack = deque([start])
    print(start,end=' ')
    while stack:
        now = stack.popleft()
        visited[now]=1
        temp = deque([now])
        for i in range(1,V+1):
            if not arr[i] and not visited[i]:
                print(i,end=' ')
                visited[i]=1
                temp.append(i)
        while temp:
            new = temp.popleft()
            for j in arr:
                if new in j:
                    j.remove(new)
                    stack.append(new)

for tc in range(1,11):
    V,E = map(int,input().split())
    arr = [[] for _ in range(V+1)]
    work = list(map(int,input().split()))
    for i in range(E):
        arr[work[2*i+1]].append(work[2*i])
    visited = [0] * (V+1)
    print(f'#{tc}',end=' ')
    start= find_start(arr,visited)
    find_parents(start,arr,visited)
    print()

