from collections import deque

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def cnt_find(x, y):
    global idx
    global visited

    tmp = 1
    que = deque([(x, y)])
    while que:
        x, y = que.popleft()
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = idx
                    que.append((nx, ny))
                    tmp += 1

    return tmp


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = {}
idx = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = idx
            cnt[idx] = cnt_find(i, j)
            idx += 1

result = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tmp = set()
            for di, dj in dr:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if visited[ni][nj]:
                        tmp.add(visited[ni][nj])
            for k in tmp:
                result[i][j] += cnt[k]
            result[i][j] += 1
            result[i][j] %= 10
# print(cnt)
# print(visited)
for r in result:
    print(*r, sep='')