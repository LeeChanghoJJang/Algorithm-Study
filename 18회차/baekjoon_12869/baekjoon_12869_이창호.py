import sys
from collections import deque
from itertools import permutations
sys.stdin = open('input.txt')
n = int(input())
scv = list(map(int, input().split()))

scv += [0] * (3 - n)
visited = [[[-1] * 61 for _ in range(61)] for _ in range(61)]
visited[scv[0]][scv[1]][scv[2]] = 0

q = deque()
q.append([scv[0], scv[1], scv[2]])

while q:
    here = q.popleft()

    if here[0] == 0 and here[1] == 0 and here[2] == 0:
        print(visited[here[0]][here[1]][here[2]])
        break

    for i in permutations([9, 3, 1], 3):
        t = [max(here[0] - i[0], 0), max(here[1] - i[1], 0), max(here[2] - i[2], 0)]

        if visited[t[0]][t[1]][t[2]] == -1:
            visited[t[0]][t[1]][t[2]] = visited[here[0]][here[1]][here[2]] + 1
            q.append(t)