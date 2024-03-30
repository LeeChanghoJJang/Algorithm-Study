from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

pos = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            pos.append(i)
            pos.append(j)

cnt = 0


def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x, y]])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ii, jj = i + dx[idx], j + dy[idx]

            if 0 <= ii and ii < N and 0 <= jj and jj < N and visited[ii][jj] == 0:
                if space[x][y] > space[ii][jj] and space[ii][jj] != 0:
                    visited[ii][jj] = visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif space[x][y] == space[ii][jj]:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])
                elif space[ii][jj] == 0:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])

    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


i, j = pos
size = [2, 0]
while True:
    space[i][j] = size[0]
    cand = deque(bfs(i, j))

    if not cand:
        break

    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[i][j] = 0
    i, j = xx, yy

print(cnt)

# from collections import deque
#
# # 상, 좌, 우, 하
# di = [-1, 0, 0, 1]
# dj = [0, -1, 1, 0]
#
# def bfs(i, j):
#     global size
#     global fish
#     global sec
#
#     q = deque([[(i, j), 0]])
#
#     while q:
#         # print(q)
#         if fish == size:
#             size += 1
#             fish = 0
#
#         now = q.popleft()
#         sec = max(sec, now[1])
#         # print(now)
#
#         for d in range(4):
#             ni = now[0][0] + di[d]
#             nj = now[0][1] + dj[d]
#
#             if 0 <= ni < n and 0 <= nj < n and 0 <= arr[ni][nj] <= size:
#                 if arr[ni][nj] == 0:        # 빈 칸일 때
#                     q.append([(ni, nj), now[1]+1])
#                     arr[ni][nj] = -1
#                 elif arr[ni][nj] < size:    # 잡아먹는 경우
#                     fish += 1
#                     arr[ni][nj] = 9
#                     return
#                 elif arr[ni][nj] == size:   # 같을 때
#                     q.append([(ni, nj), now[1]+1])
#     return
#
#
# def cnt(baby):
#     for i in range(n):
#         for j in range(n):
#             if 0 < arr[i][j] <= baby:
#                 return True     # 먹을 물고기가 있음
#     return False
#
# def reset():
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == -1:
#                 arr[i][j] = 0
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# size = 2
# fish = 0
# sec = 0
#
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 9:
#             arr[i][j] = 0
#             bfs(i, j)
#             print(sec)
#             print(arr)
#             print(fish, size)
#             reset()
#             print(arr)
#     else:
#         break
# print(sec)