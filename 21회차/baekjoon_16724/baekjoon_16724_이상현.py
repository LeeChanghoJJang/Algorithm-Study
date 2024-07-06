def move(row, col, idx):
    global answer

    if visited[row][col]:
        if visited[row][col] == idx:
            answer = answer + 1
        return

    visited[row][col] = idx
    d = list_[row][col]
    move(row + dict_[d][0], col + dict_[d][1], idx)

N, M = map(int, input().split())
list_ = [list(input()) for _ in range(N)]
dict_ = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
visited = [[0] * M for _ in range(N)]
answer = 0

idx = 1
for row in range(N):
    for col in range(M):
        move(row, col, idx)
        idx = idx + 1

print(answer)