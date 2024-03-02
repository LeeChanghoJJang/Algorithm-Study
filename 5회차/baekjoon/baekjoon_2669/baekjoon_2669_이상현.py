list_ = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for row in range(y1, y2):
        for col in range(x1, x2):
            list_[row][col] = 1

print(sum(row.count(1) for row in list_))