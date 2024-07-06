from collections import deque

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]
visited = [[0] * 500  for _ in range(500)]

def bfs(row, col, n, m, land, answer_list):
    q = deque()
    q.append((row, col))
    cnt = 1
    visited[row][col] = 1
    visited_col = [col]

    while q:
        row, col = q.popleft()

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < n and 0 <= ncol < m) or visited[nrow][ncol] or not land[nrow][ncol]:
                continue
            
            visited[nrow][ncol] = 1

            if ncol not in visited_col:
                visited_col.append(ncol)

            q.append((nrow, ncol))
            cnt += 1

    for col in visited_col:
        answer_list[col] += cnt

def solution(land):
    n, m = len(land), len(land[0])
    answer_list = [0 for _ in range(m)]

    for row in range(n):
        for col in range(m):
            if land[row][col] == 1 and not visited[row][col]:
                bfs(row, col, n, m, land, answer_list)

    answer = max(answer_list)
    return answer