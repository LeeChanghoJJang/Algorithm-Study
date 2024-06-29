from collections import deque
import sys
sys.stdin = open('input.txt')

# 방향 벡터 정의 (네 방향 이동 + 말의 이동)
normal_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
horse_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]

def is_valid(nx, ny, h, w):
    return 0 <= nx < h and 0 <= ny < w

# 입력 처리
k = int(input())
w, h = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(h)]

# BFS 초기 설정
locations = deque([(0, 0, k, 0)])  # (x, y, 남은 점프 횟수, 현재 동작 수)
visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]
visited[0][0][k] = True

# BFS 탐색
result = -1
while locations:
    x, y, jump, cnt = locations.popleft()

    if x == h - 1 and y == w - 1:
        result = cnt
        break

    # 일반 이동
    for dx, dy in normal_moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, h, w) and chess[nx][ny] == 0 and not visited[nx][ny][jump]:
            visited[nx][ny][jump] = True
            locations.append((nx, ny, jump, cnt + 1))

    # 말의 이동
    if jump > 0:
        for dx, dy in horse_moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, h, w) and chess[nx][ny] == 0 and not visited[nx][ny][jump - 1]:
                visited[nx][ny][jump - 1] = True
                locations.append((nx, ny, jump - 1, cnt + 1))

print(result)
