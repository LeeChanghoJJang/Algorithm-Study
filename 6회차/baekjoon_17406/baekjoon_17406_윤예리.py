from itertools import permutations
from copy import deepcopy

def rotate(ls, graph):
    r, c, s = ls

    for j in range(s):
        tmp = graph[r-s+j][c-s+j]

        # 좌
        for i in range(r-s+j, r+s-j):
            graph[i][c-s+j] = graph[i+1][c-s+j]

        # 하
        for i in range(c-s+j, c+s-j):
            graph[r+s-j][i] = graph[r+s-j][i+1]

        # 우
        for i in range(r+s-j, r-s+j, -1):
            graph[i][c+s-j] = graph[i-1][c+s-j]

        # 상
        for i in range(c+s-j, c-s+j, -1):
            graph[r-s+j][i] = graph[r-s+j][i-1]

        graph[r-s+j][c-s+1+j] = tmp

n, m, k = map(int, input().split())
arr = [[]]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

op = [[*map(int, input().split())] for _ in range(k)]

cnt = float('INF')
for k in permutations(op):
    g = deepcopy(arr)

    for i in k:
        rotate(i, g)

    for i in range(1, n+1):
        cnt = min(cnt, sum(g[i]))

print(cnt)




# 얜 또 왜...
# for ls in permutations(rotate, k):
#     result = deepcopy(aij)
#
#     for r, c, s in ls:
#         r -= 1
#         c -= 1
#
#         for n in range(s, 0, -1):
#             tmp = result[r-n][c+n]
#
#             # 상
#             result[r-n][c-n+1:c+n+1] = result[r-n][c-n:c+n]
#
#             # 좌
#             for j in range(r-n, r+n):
#                 result[j][c-n] = result[j+1][c-n]
#
#             # 하
#             result[r+n][c-n:c+n] = result[r+n][c-n+1:c+n+1]
#
#             # 우
#             for i in range(r+n, r-n-1):
#                 result[i][c+n] = result[i-1][c+n]
#
#             result[r-n+1][c+n] = tmp
#
#     for i in result:
#         if sum(i) < cnt:
#             cnt = sum(i)
#
# print(cnt)


# 왜 틀렸을까....
# order = list(permutations(rotate, k))
# result = [[0 * m for _ in range(n)]]
# for i in range(len(order)):
#     arr = deepcopy(aij)
#     result = deepcopy(arr)
#
#     for j in range(k):
#         start_i = order[i][j][0] - order[i][j][2] - 1
#         start_j = order[i][j][1] - order[i][j][2] - 1
#         end_i = order[i][j][0] + order[i][j][2] - 1
#         end_j = order[i][j][1] + order[i][j][2] - 1
#
#         while start_i <= end_i and start_j <= end_j:
#             for r in range(start_i, end_i+1):
#                 for c in range(start_j, end_j+1):
#
#                     if r == start_j and c != start_j:
#                         result[r][c] = arr[r][c-1]
#                     elif c == end_j and r != start_i:
#                         result[r][c] = arr[r-1][c]
#                     elif r == end_i and c != end_j:
#                         result[r][c] = arr[r][c+1]
#                     elif c == start_j and r != end_i:
#                         result[r][c] = arr[r+1][c]
#
#             start_i += 1
#             start_j += 1
#             end_i -= 1
#             end_j -= 1
#
#         arr = deepcopy(result)
#
#     for d in result:
#         if sum(d) < cnt:
#             cnt = sum(d)
# print(cnt)