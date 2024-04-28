import sys
from collections import deque
# from pprint import pprint as print
input = sys.stdin.readline
dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_outer(v):
    que = deque([v])
    while que:
        x, y = que.popleft()
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0 and not outer[nx][ny]:
                    outer[nx][ny] = 1
                    que.append((nx, ny))


def melt_check(v):
    x, y = v
    meet = 0
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if outer[nx][ny] == 1:
                meet += 1
    return meet


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


'''
외부 공기와 2면 이상 닿아있으면 녹음
외부 공기인지 체크를 해줘야 한다.
한 사이클 녹일 때마다 일단 체크
'''

outer = [[0] * M for _ in range(N)]
for i in (0, N-1):
    for j in (0, M-1):
        if arr[i][j] == 0 and not outer[i][j]:
            # 초기상태 외부공기 확인
            outer[i][j] = 1
            is_outer((i, j))

# print(outer)
time = 0
melt_list = deque([])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            if melt_check((i, j)) >= 2:
                melt_list.append((i, j))

while melt_list:

    while melt_list:
        x, y = melt_list.popleft()
        outer[x][y] = 1
        arr[x][y] = 0

        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0 and outer[nx][ny] == 0:
                    outer[nx][ny] = 1
                    is_outer((nx, ny))
    time += 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not outer[i][j]:
                if melt_check((i, j)) >= 2:
                    melt_list.append((i, j))

print(time)

'''
melt_list 돌면서
녹일 때 마다 현재칸 1로 만들어야 할듯 함

녹이자마자 옆 4칸 보면서
arr = 0이고 outer = 0이면 is_outer 돌려주면 될듯
다 녹은 타이밍 ? 어케 멈추지
'''