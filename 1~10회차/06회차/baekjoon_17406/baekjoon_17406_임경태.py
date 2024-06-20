# 17406 배열돌리기 4

from itertools import permutations as per
from copy import deepcopy

ds = ((1, 0), (0, 1), (-1, 0), (0, -1))

def rotate(r, c, s):  # row, column, seal
    for l in range(1, s+1):
        i, j = r-l-1, c-l-1
        temp = B[i][j]
        for di, dj in ds:
            for _ in range(2*l):
                B[i][j] = B[i+di][j+dj]
                i += di; j += dj
        B[i][j+1] = temp


N, M, K = map(int, input().split())  # row_num, column_num, oper_num
A = [list(map(int, input().split())) for _ in range(N)]  # array
oper = [list(map(int, input().split())) for _ in range(K)]  # operation
ans = 5e+4

for p in per(oper, K):  # 각 연산 순열로 순회
    B = deepcopy(A)
    [rotate(r, c, s) for r, c, s in p]
    ans = min(ans, min(map(sum, B)))

print(ans)

'''
31740KB / 1008ms
'''