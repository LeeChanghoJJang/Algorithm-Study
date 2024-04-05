from collections import deque
# import sys
# input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 블록 그룹 찾기
def find_block(i, j, num):
    q = deque()
    q.append((i, j))

    rainbows = []
    normals = []

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                # 무지개 블록
                if not block[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    rainbows.append([nx, ny])
                    visited[nx][ny] = 1

                # 일반 블록
                elif block[nx][ny] == block_num and not visited[nx][ny]:
                    q.append((nx, ny))
                    normals.append([nx, ny])
                    visited[nx][ny] = 1

    for x, y in rainbows:
        visited[x][y] = 0

    return [len(normals+rainbows), len(rainbows), normals+rainbows]

# 블록 제거
def remove_block(group):
    global score
    score += group[0] ** 2

    for x, y in group[2]:
        block[x][y] = -2

# 중력
def gravity():
    for i in range(n-2, -1, -1):
        for j in range(n):
            if block[i][j] != 1:
                pointer = i

                while pointer + 1 < n and block[pointer+1][j] == -2:
                    block[pointer+1][j] = block[pointer][j]
                    block[pointer][j] = -2
                    pointer += 1

# 회전
def rotate_block():
    global block

    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[n-j-1][i] = block[i][j]

    block = tmp

n, m = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(n)]
score = 0

while True:
    visited = [[0] * n for _ in range(n)]
    groups = []

    for i in range(n):
        for j in range(n):
            if block[i][j] >= 1 and not visited[i][j]:
                visited[i][j] = 1
                group = find_block(i, j, block[i][j])

                if group[0] >= 2:
                    groups.append(group)
    groups.sort(reverse=True)

    if not groups:
        break

    remove_block(groups[0])
    gravity()
    rotate_block()
    gravity()

print(score)