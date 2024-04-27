list_ = [[0] * 1001 for _ in range(1001)]
N = int(input())

for i in range(N):
    x1, y1, w, h = map(int, input().split())

    for row in range(y1, y1 + h):
        for col in range(x1, x1 + w):
            list_[row][col] = i + 1

for i in range(1, N + 1):
    print(sum(list_[r][c] == i for r in range(1001) for c in range(1001)))