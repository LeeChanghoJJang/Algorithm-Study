# 백준 2583번 영역 구하기

import sys
sys.setrecursionlimit(100000)

# dfs를 이용하여 접근
def dfs(row, col, temp):

    # 인덱스를 벗어나거나 이미 방문한 곳 혹은 직사각형의 내부라면 0을 반환
    if not (0 <= row < len(temp) and 0 <= col < len(temp[0])) or temp[row][col]:
        return 0

    # 만약 직사각형의 내부가 아니라면 그 영역과 연결된 모든 영역을
    # 탐색하고 다른 영역을 탐색할 때마다 area의 값을 1 증가시킴
    area = 1
    temp[row][col] = 1

    area += dfs(row + 1, col, temp)
    area += dfs(row - 1, col, temp)
    area += dfs(row, col + 1, temp)
    area += dfs(row, col - 1, temp)

    return area

M, N, K = map(int, input().split())
paper = [[0] * N for _ in range(M)]
area_cnt = 0
area = []

# 주어진 직사각형의 좌표를 이용하여 직사각형들의 내부에
# 위치해 있는 칸의 값을 1증가시킴
for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())

    for row in range(r1, r2):
        for col in range(c1, c2):
            paper[row][col] += 1

for row in range(M):
    for col in range(N):

        # 직사각형의 내부가 아닐 때마다 area_cnt의 값을 1 증가시킴
        if paper[row][col] == 0:
            area_cnt += 1

            # 반환된 넓이를 area에 추가
            area.append(dfs(row, col, paper))

print(area_cnt)
print(*sorted(area))