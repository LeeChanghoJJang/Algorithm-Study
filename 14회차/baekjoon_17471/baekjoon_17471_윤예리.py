'''
1. 조합 나누기
2. 나눠진 선거구 확인
3. 계산
'''

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def check(A, B):
    global result

    a_2 = 0
    b_2 = 0

    for a in A:
        a_2 += people[a]
    for b in B:
        b_2 += people[b]

    result = min(result, abs(a_2-b_2))

def bfs(g):
    q = deque()
    q.append(g[0])

    visited = [0] * (n+1)
    visited[g[0]] = 1

    while q:
        v = q.popleft()

        for i in arr[v]:
            if i in g and not visited[i]:
                visited[i] = 1
                q.append(i)

    for j in g:
        if not visited[j]:
            return False
    return True

n = int(input())
people = [0] + list(map(int, input().split()))

arr = [[] for _ in range(n+1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    arr[i+1] = tmp[1:]

result = float('inf')
for x in range(1, n//2+1):
    for y in combinations([k for k in range(1, n+1)], x):
        A = y
        B = [z for z in range(1, n+1) if z not in A]

        # print(A, B)
        if bfs(A) and bfs(B):
            check(A, B)

print(result if result != float('inf') else -1)
