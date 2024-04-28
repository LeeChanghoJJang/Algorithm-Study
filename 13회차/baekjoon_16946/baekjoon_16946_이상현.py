from collections import deque

# BFS를 수행하여 그룹의 크기를 계산하는 함수
def bfs(row, col, group):
    q = deque([(row, col)])
    visited[row][col] = group
    count = 1

    while q:
        row, col = q.popleft()

        # 상하좌우 이웃 노드를 확인하여 방문 여부를 체크하고 그룹에 추가
        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            # 범위를 벗어난 경우 무시
            if not (0 <= nrow < N and 0 <= ncol < M):
                continue

            # 이미 방문한 경우 무시 또는 벽인 경우 무시
            if visited[nrow][ncol] or list_[nrow][ncol]:
                continue

            # 새로운 그룹의 크기를 증가시키고 방문 체크
            count += 1
            visited[nrow][ncol] = group
            q.append((nrow, ncol))
    return count

# 입력
N, M = map(int, input().split())
list_ = [list(map(int, list(input()))) for _ in range(N)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[0] * M for _ in range(N)]
answer = [[0] * M for _ in range(N)]
group_size = {}
group_num = 1

# 그룹의 크기를 계산하고 그룹 번호에 따라 저장
for row in range(N):
    for col in range(M):
        if list_[row][col] == 0 and visited[row][col] == 0:
            group_size[group_num] = bfs(row, col, group_num)
            group_num += 1

# 각 칸의 주변의 그룹 크기를 계산하여 벽을 그룹 크기로 대체
for row in range(N):
    for col in range(M):
        if list_[row][col] == 1:
            nbd_set = set()
            total_size = 1

            # 주변 칸의 그룹 번호를 확인하여 중복된 것은 제외하고 크기 계산
            for k in range(4):
                nrow, ncol = row + drow[k], col + dcol[k]

                # 범위를 벗어난 경우 무시 또는 벽인 경우 무시
                if not(0 <= nrow < N and 0 <= ncol < M) or list_[nrow][ncol]:
                    continue
                nbd_set.add(visited[nrow][ncol])

            # 주변 그룹의 크기를 모두 더하여 현재 위치의 값을 갱신
            for group in nbd_set:
                total_size += group_size[group]

            answer[row][col] = total_size % 10

# 결과 출력
[print(''.join(map(str, row))) for row in answer]
