N = int(input())
list_ = [[0] * 101 for _ in range(101)]

for _ in range(N):
    r, c = map(int, input().split())

    for row in range(10):
        for col in range(10):
            list_[r + row][c + col] = 1

print(sum(row.count(1) for row in list_))