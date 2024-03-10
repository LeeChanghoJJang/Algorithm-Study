# 백준 17406번 배열 돌리기 4

from itertools import permutations

def rotation_func(r, c, s):
    for depth in range(s):
        temp1 = temp[r - 1 - (s - depth)][c - 1 - (s - depth)]

        for row in range(r - 1 - (s - depth), r - 1 + (s - depth)):
            temp[row][c - 1 - (s - depth)] = temp[row + 1][c - 1 - (s - depth)]
        for col in range(c - 1 - (s - depth), c - 1 + (s - depth)):
            temp[r - 1 + (s - depth)][col] = temp[r - 1 + (s - depth)][col + 1]
        for row in range(r - 1 + (s - depth), r - 1 - (s - depth), -1):
            temp[row][c - 1 + (s - depth)] = temp[row - 1][c - 1 + (s - depth)]
        for col in range(c - 1 + (s - depth), c - 1 - (s - depth), -1):
            temp[r - 1 - (s - depth)][col] = temp[r - 1 - (s - depth)][col - 1]

        temp[r - 1 - (s - depth)][c - (s - depth)] = temp1

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
rotation_list = [list(map(int, input().split())) for _ in range(K)]
rotation_list = permutations(rotation_list)
min_ = float('inf')

for rotation in rotation_list:
    temp = [row[:] for row in matrix]

    for r, c, s in rotation:
        rotation_func(r, c, s)

    min_ = min(min_, min(sum(row) for row in temp))

print(min_)